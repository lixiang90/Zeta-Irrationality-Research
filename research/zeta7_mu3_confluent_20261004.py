"""Exact mu_3/fifth-order-pole experiments for a pure zeta(7) Gram.

The common numerator, full nuisance coefficient matrices, and primitive
determinant are rational. Positive pivots and target values use Arb.
Finite experiments do not establish an irrationality theorem.
"""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, arb, arb_mat, arb_poly, ctx
from b8_hankel import Dpoly, mu_monomial
from joint_exact import content
from zeta7_space_extension_probe import polynomial
from zeta7_moment_extension_20261004 import aq, positive_pivots

sys.set_int_max_str_digits(0)


def mu3(e):
    return Q(-1)**e*Q.bernoulli(2*e+2)*(2*e+3)/2


def pole_values(j):
    j=Q(j)
    # Each row is (rational constant, zeta3, zeta4, zeta5, zeta6, zeta7).
    return [
        [Q(-1,2)-1/(2*j),j*j,0,0,0,0],
        [-1/(4*j**3),-1,3*j/2,0,0,0],
        [-3/(16*j**5),0,-9/(8*j),Q(3,2),0,0],
        [-5/(32*j**7),0,-3/(16*j**3),-3/(4*j*j),5/(4*j),0],
        [-35/(256*j**9),0,-9/(128*j**5),-9/(32*j**4),-5/(16*j**3),15/(16*j*j)],
    ]


def sequences(K,maxs):
    D=Poly(Dpoly(K));den=D**5
    seq=[[Q(0) for _ in range(maxs+1)] for _ in range(6)]
    hs={s:Q(0) for s in range(3,8)}
    for j in range(1,K+1):
        r=-j*j;dj=D//Poly([j*j,1]);der=dj
        jet=[]
        for k in range(5):
            jet.append(der(r)/math.factorial(k));der=der.derivative()
        f=Poly(jet)**5;inv=[1/f[0]]
        for k in range(1,5):
            inv.append(-sum((f[i]*inv[k-i] for i in range(1,k+1)),Q(0))/f[0])
        assert all((f*Poly(inv))[k]==(1 if k==0 else 0) for k in range(5))
        vals=pole_values(j)
        vals=[[Q(v) for v in row] for row in vals]
        for row in vals:
            row[0]-=sum((row[s-2]*hs[s] for s in range(3,8)),Q(0))
        for e in range(maxs+1):
            pjet=[Q(math.comb(e,n))*Q(r)**(e-n) if n<=e else Q(0) for n in range(5)]
            for m in range(1,6):
                k=5-m
                c=sum((pjet[n]*inv[k-n] for n in range(k+1)),Q(0))
                for a in range(6):seq[a][e]+=c*vals[m-1][a]
        for s in range(3,8):hs[s]+=Q(1,j**s)
    for e in range(maxs+1):
        q=Poly([0]*e+[1])//den
        seq[0][e]+=sum((v*mu3(k) for k,v in enumerate(q)),Q(0))
    return seq


def run(K,h):
    L=3*(2*h-1)
    assert L+2*h<=5*K-1
    ss=sequences(K,L+2*h-2)
    C=Mat([[ss[a][s+e] for e in range(L)] for a in (2,3,4) for s in range(2*h-1)])
    rank=C.rank()
    out=dict(K=K,h=h,degree_numerator=L,constraint_rank=rank,expected_constraints=L)
    if rank<L:
        out['status']='singular_minimal_monic_constraints';return out
    rhs=Mat([[-ss[a][s+L]] for a in (2,3,4) for s in range(2*h-1)])
    sol=C.inv()*rhs;w=[sol[i,0] for i in range(L)]+[Q(1)]
    moments=[[sum((ss[a][s+e]*w[e] for e in range(L+1)),Q(0)) for s in range(2*h-1)] for a in range(6)]
    assert all(v==0 for a in (1,2,3,4) for v in moments[a])
    out.update(rational_numerator=list(map(str,w)),coefficient_positive=all(v>0 for v in w),
               nuisance_equalities=4*(2*h-1))
    A=Mat([[moments[0][i+j] for j in range(h)] for i in range(h)])
    B=Mat([[moments[5][i+j] for j in range(h)] for i in range(h)])
    d=polynomial(A,B);ct=content(d);pr=d/ct
    coeff=[int(v) for v in pr];bits=max(abs(v).bit_length() for v in coeff)+K*K+4000
    ctx.prec=bits;z=arb(7).zeta()
    G=arb_mat([[aq(A[i,j])+z*aq(B[i,j]) for j in range(h)] for i in range(h)])
    pd=positive_pivots(G)
    neg=positive_pivots(-G)
    sign=1 if pd['positive_definite'] else -1 if neg['positive_definite'] else 0
    out.update(monic_positive_check=pd,negative_orientation_positive_check=neg,target_rank=B.rank(),
               determinant_degree=d.degree(),finite_positive_orientation=sign)
    if sign:
        if sign==-1:
            w=[-v for v in w];d=d*((-1)**h);pr=d/ct;coeff=[int(v) for v in pr]
        value=arb_poly(coeff)(z);assert value>0
        assert math.gcd(*coeff)==1
        for x in range(h+1):assert d(x)==(A*sign+B*(sign*x)).det()
        out.update(status='finite_exact_and_arb_positive_checks_passed',
                   chosen_numerator=list(map(str,w)),positive_weight_coefficients=all(v>=0 for v in w),
                   primitive_coefficients=list(map(str,coeff)),content=str(ct),
                   log_primitive_interval=value.log().str(50),J=float(value.log())/(K*K),
                   exact_determinant_points=h+1)
    else:out['status']='finite_gram_not_definite'
    print(K,h,out['status'],out.get('J'),flush=True)
    return out


def euler_checks():
    for e in range(35):
        multiplier=Q(math.prod(2*e+i for i in range(4,8)),360)
        assert mu_monomial(e)==mu3(e)*multiplier
    return 35


if __name__=='__main__':
    records=[];path=Path(__file__).with_suffix('.json')
    for K,h in [(2,1),(3,1),(4,2),(6,3),(8,4),(12,6),(16,8)]:
        records.append(run(K,h))
        path.write_text(json.dumps(dict(euler_monomial_checks=euler_checks(),records=records,
             scope='Finite minimal monic common-numerator mu3/fifth-order-pole family only. '
                   'No asymptotic positivity or irrationality assertion.'),indent=2),encoding='utf-8')
