"""Pure zeta(7) Hankel pencils using the positive mu5 measure and triple poles.

Discovery uses LP; rational candidates and all nuisance eliminations are
checked exactly. No asymptotic claim. All zeta(5), zeta(6) coefficients must
vanish entry by entry before a candidate is called a pure zeta(7) pencil.
"""
import json, math, sys
from pathlib import Path
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog
from flint import fmpq as Q, fmpq_mat, fmpq_poly, arb, arb_mat, arb_poly, ctx
from zeta35_target31 import content_and_primitive, rational_log

sys.set_int_max_str_digits(0)


def coefficient_sequences(K, maximum):
    h5 = [Q(0)]; h6 = [Q(0)]; h7 = [Q(0)]
    for j in range(1, K+1):
        h5.append(h5[-1]+Q(1,j**5))
        h6.append(h6[-1]+Q(1,j**6))
        h7.append(h7[-1]+Q(1,j**7))
    seqs = [[Q(0) for _ in range(maximum+1)] for _ in range(4)]
    for j in range(1,K+1):
        r = -j*j
        E = math.prod((k*k-j*j)**3 for k in range(1,K+1) if k!=j)
        l1 = sum((Q(3,k*k-j*j) for k in range(1,K+1) if k!=j),Q(0))
        l2 = -sum((Q(3,(k*k-j*j)**2) for k in range(1,K+1) if k!=j),Q(0))
        # mu5((t+j^2)^-q), q=1,2,3, in basis 1,zeta5,zeta6,zeta7.
        z5 = [Q(j**4),Q(-2*j*j),Q(1)]
        z6 = [Q(0),Q(5*j**3,2),Q(-35*j,8)]
        z7 = [Q(0),Q(0),Q(15*j*j,4)]
        const = [
            -j**4*h5[j-1]-Q(1,2*j)-Q(1,4),
            2*j*j*h5[j-1]-Q(5*j**3,2)*h6[j-1]-Q(1,4*j**3),
            -h5[j-1]+Q(35*j,8)*h6[j-1]-Q(15*j*j,4)*h7[j-1]-Q(3,16*j**5),
        ]
        for n in range(maximum+1):
            f = Q(r)**n
            f1 = n*Q(r)**(n-1) if n else Q(0)
            f2 = n*(n-1)*Q(r)**(n-2) if n>=2 else Q(0)
            partial = [(f2-2*l1*f1+(l1*l1-l2)*f)/(2*E), (f1-l1*f)/E, f/E]
            for seq, values in zip(seqs,(const,z5,z6,z7)):
                seq[n] += sum((c*v for c,v in zip(partial,values)),Q(0))
    # Polynomial quotient has rational mu5 moments, no nuisance zeta values.
    D=fmpq_poly([1])
    for j in range(1,K+1):
        D *= fmpq_poly([j*j,1])**3
    for n in range(3*K,maximum+1):
        quotient=fmpq_poly([0]*n+[1])//D
        seqs[0][n] += sum((quotient[e]*Q(-1)**e*Q.bernoulli(2*e+2)*
                          (2*e+3)*(2*e+4)*(2*e+5)/24
                          for e in range(quotient.degree()+1)),Q(0))
    return seqs


def aq(q):
    return arb(int(q.numerator))/int(q.denominator)


def evaluate_exact(K,h,coeff,seqs=None,require_nonnegative=True):
    coeff=list(map(Q,coeff))
    assert any(c!=0 for c in coeff)
    if require_nonnegative:
        assert all(c>=0 for c in coeff) and any(c>0 for c in coeff)
    scalar=Q(math.gcd(*(int(c.numerator) for c in coeff)),
             math.lcm(*(int(c.denominator) for c in coeff)))
    coeff=[c/scalar for c in coeff]
    assert all(c.denominator==1 for c in coeff)
    if seqs is None:
        seqs=coefficient_sequences(K,len(coeff)+2*h-3)
    entries=[[sum((seq[s+e]*c for e,c in enumerate(coeff)),Q(0))
              for s in range(2*h-1)] for seq in seqs]
    assert all(x==0 for z in (1,2) for x in entries[z])
    Am=fmpq_mat([[entries[0][i+j] for j in range(h)] for i in range(h)])
    Bm=fmpq_mat([[entries[3][i+j] for j in range(h)] for i in range(h)])
    if Bm.det():
        poly=(-(Bm.inv()*Am)).charpoly()*Bm.det()
    else:
        vals=[(Am+Bm*Q(x)).det() for x in range(h+1)]
        inv=fmpq_mat([[Q(x)**e for e in range(h+1)] for x in range(h+1)]).inv()
        poly=fmpq_poly([sum((inv[e,x]*vals[x] for x in range(h+1)),Q(0))
                        for e in range(h+1)])
    cont, primitive=content_and_primitive(poly)
    bits=max(abs(c).bit_length() for c in primitive)
    ctx.prec=max(4000,bits+2*K*K+2000)
    value=arb_poly(primitive)(arb(7).zeta())
    assert value>0
    positive_pivots=[]
    if not require_nonnegative:
        xi=arb(7).zeta()
        S=[[aq(entries[0][i+j])+xi*aq(entries[3][i+j]) for j in range(h)] for i in range(h)]
        for k in range(h):
            pivot=S[k][k]
            assert pivot>0
            positive_pivots.append(pivot.str(45))
            for i in range(k+1,h):
                for j in range(i,h):
                    S[i][j]-=S[i][k]*S[j][k]/pivot
                    S[j][i]=S[i][j]
    for x in (Q(-1),Q(0),Q(1)):
        assert (Am+Bm*x).det()==poly(x)
    return dict(positive_candidate_exact=True,numerator=list(map(str,coeff)),
                degree_numerator=max(e for e,c in enumerate(coeff) if c),
                zeta7_slope_rank=Bm.rank(),degree_polynomial=poly.degree(),content=str(cont),
                primitive_coefficients=list(map(str,primitive)),
                log_primitive=value.log().str(45),normalized_log_primitive=float(value.log())/(K*K),
                exact_nuisance_equalities=2*(2*h-1),
                all_coefficients_nonnegative=all(c>=0 for c in coeff),
                finite_positive_pivots=positive_pivots,
                integral_positivity=('All numerator coefficients nonnegative and nonzero; '
                    'mu5 positive and D_K^3 positive on [0,infinity).' if require_nonnegative else
                    'Finite truncated Gram positivity by strict Arb LDL; the measure has changing sign.'))


def run(K,h):
    d=3*K-1
    seqs=coefficient_sequences(K,d+2*h-2)
    M=fmpq_mat([[seqs[z][s+e] for e in range(d+1)]
               for z in (1,2) for s in range(2*h-1)])
    rank=M.rank()
    # Positive coefficient cone in powers (t/K^2)^e. Scale rows before LP.
    rows=[]
    for row in M.tolist():
        transformed=[q/Q(K*K)**e for e,q in enumerate(row)]
        maxq=max(map(abs,transformed))
        if maxq:
            rows.append([float(q/maxq) for q in transformed])
    A=np.array(rows+[[1.0]*(d+1)])
    b=np.array([0.0]*len(rows)+[1.0])
    lp=linprog(np.array([e/(d+1) for e in range(d+1)]),A_eq=A,b_eq=b,
               bounds=[(0,None)]*(d+1),method='highs',
               options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9})
    result=dict(K=K,h=h,degree_limit=d,nuisance_constraint_rank=rank,
                rational_kernel_dimension=d+1-rank,lp_status=int(lp.status),
                lp_message=lp.message,positive_candidate_exact=False)
    if lp.success:
        # Recover the basic vertex from its support by exact rational solve.
        support=[e for e,x in enumerate(lp.x) if x>1e-8]
        from sympy import Matrix, Rational
        exact=Matrix([[Rational(str(M[i,e]))/Rational(K*K)**e for e in support]
                     for i in range(M.nrows())]+[[1]*len(support)])
        rhs=Matrix([0]*M.nrows()+[1])
        try:
            sol, params=exact.gauss_jordan_solve(rhs)
            if params.rows:
                raise ValueError('LP support is not a unique exact vertex')
            coeff=[Q(0)]*(d+1)
            for e,x in zip(support,sol):
                coeff[e]=Q(str(x))/Q(K*K)**e
            assert all(c>=0 for c in coeff) and any(c>0 for c in coeff)
            assert M*fmpq_mat(d+1,1,coeff)==fmpq_mat(M.nrows(),1)
            content=Q(math.gcd(*(int(c.numerator) for c in coeff)),
                      math.lcm(*(int(c.denominator) for c in coeff)))
            coeff=[c/content for c in coeff]
            assert all(c.denominator==1 for c in coeff)
            entries=[[sum((seq[s+e]*c for e,c in enumerate(coeff)),Q(0))
                      for s in range(2*h-1)] for seq in seqs]
            assert all(x==0 for z in (1,2) for x in entries[z])
            Am=fmpq_mat([[entries[0][i+j] for j in range(h)] for i in range(h)])
            Bm=fmpq_mat([[entries[3][i+j] for j in range(h)] for i in range(h)])
            result.update(numerator=list(map(str,coeff)),
                          degree_numerator=max(e for e,c in enumerate(coeff) if c),
                          zeta7_slope_rank=Bm.rank())
            if Bm.det():
                poly=(-(Bm.inv()*Am)).charpoly()*Bm.det()
            else:
                # Exact interpolation also covers lower degree pencils.
                vals=[(Am+Bm*Q(x)).det() for x in range(h+1)]
                inv=fmpq_mat([[Q(x)**e for e in range(h+1)] for x in range(h+1)]).inv()
                poly=fmpq_poly([sum((inv[e,x]*vals[x] for x in range(h+1)),Q(0))
                                for e in range(h+1)])
            cont, primitive=content_and_primitive(poly)
            bits=max(abs(c).bit_length() for c in primitive)
            ctx.prec=max(4000,bits+2*K*K+2000)
            value=arb_poly(primitive)(arb(7).zeta())
            assert value>0
            for x in (Q(-1),Q(0),Q(1)):
                assert (Am+Bm*x).det()==poly(x)
            result.update(positive_candidate_exact=True,degree_polynomial=poly.degree(),content=str(cont),
                          primitive_coefficients=list(map(str,primitive)),
                          log_primitive=value.log().str(45),
                          normalized_log_primitive=float(value.log())/(K*K),
                          exact_nuisance_equalities=2*(2*h-1),
                          integral_positivity='All numerator coefficients nonnegative and nonzero; '
                              'mu5 positive and D_K^3 positive on [0,infinity).')
        except (ValueError,AssertionError) as exc:
            result['candidate_recovery_failure']=str(exc)
    print(K,h,'rank',rank,'kernel',d+1-rank,'LP',lp.status,
          'exact',result['positive_candidate_exact'],'score',result.get('normalized_log_primitive'),flush=True)
    return result


if __name__=='__main__':
    cases=[(K,h) for K in (2,4,6,8,12) for h in sorted({max(1,K//2),max(1,3*K//4),K})]
    records=[run(K,h) for K,h in cases]
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='Finite positive-coefficient numerator cone with triple integer square poles; '
              'LP infeasibility alone is not an exact no-go theorem.',records=records),indent=2),encoding='utf-8')
