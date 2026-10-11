"""Distribution rigidity and pure-zeta(7) Bernoulli derivative deformations.

All coefficient arithmetic is exact. Target evaluation and positive-definiteness
checks use Arb. No new asymptotic divisibility or irrationality claim is made.
"""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, fmpq_mat, arb, ctx
import joint_exact as engine

sys.set_int_max_str_digits(0)
OUT=Path(__file__).with_suffix('.json')

def moment(s,e):
    return Q((-1)**e)*Q.bernoulli(2*e+2)*math.prod(range(2*e+3,2*e+s+1))/math.factorial(s-1)

def kappa(s,d):
    r=s-2
    if d<r:return Q(0)
    return Q(math.prod(range(d-r+1,d+1)))*Q.bernoulli(d-r)/math.factorial(s-1)

def rigidity_checks():
    rows=[];identities=0
    D=72
    for p in (2,3,7,11,13):
        sums=[sum(a**k for a in range(p)) for k in range(D+1)]
        mat=fmpq_mat(D+1,D+1,[Q(math.comb(n,k)*p**k*sums[n-k] if k<=n else 0)-Q(p**6 if k==n else 0)
                                          for n in range(D+1) for k in range(D+1)])
        vec=fmpq_mat(D+1,1,[kappa(7,d) for d in range(D+1)])
        assert mat*vec==fmpq_mat(D+1,1)
        assert mat.rank()==D
        for a,b in ((Q(0),Q(0)),(Q(1,8),Q(-2,7)),(Q(-3),Q(2))):
            kap=[kappa(7,d)+a*kappa(5,d)+b*kappa(3,d) for d in range(D+1)]
            kap_after=[kappa(7,d)+a*p**2*kappa(5,d)+b*p**4*kappa(3,d) for d in range(D+1)]
            for d in range(D+1):
                value=sum(Q(math.comb(d,k)*p**k*sums[d-k])*kap_after[k] for k in range(d+1))
                assert value==p**6*kap[d]
                identities+=1
        rows.append(dict(p=p,degree=D,distribution_constraint_rank=D,nullity=1))
    valuation_checks=[]
    for p in (7,11,13,17,19,23):
        for name,a,b,expected in (('pure',Q(0),Q(0),6*p-1),('tau5_unit',Q(1),Q(0),4*p-1),
                                   ('tau3_unit',Q(0),Q(1),2*p-1),('flowed',Q(p*p),Q(p**4),6*p-1)):
            first=None
            for d in range(expected+1):
                value=kappa(7,d)+a*kappa(5,d)+b*kappa(3,d)
                if value and engine.vp(value.p,p)-engine.vp(value.q,p)<0:
                    first=d;break
            assert first==expected
            valuation_checks.append(dict(p=p,family=name,first_nonintegral_x_degree=first))
    return dict(truncated_rigidity=rows,weighted_family_exact_identities=identities,
                first_bad_moment_checks=valuation_checks)

def derivative_entries(K,N,h):
    W=fmpq_poly(engine.Dcache(N))**8;D=fmpq_poly(engine.Dcache(K))
    derivative=D.derivative()
    H={s:[Q(0)] for s in (3,5,7)}
    for s in H:
        for j in range(1,K+1):H[s].append(H[s][-1]+Q(1,j**s))
    residues=[(j,W(-j*j)/derivative(-j*j)) for j in range(1,K+1) if W(-j*j)]
    powers=[Q(1)]*len(residues);A={s:[] for s in H};B=[];P=W
    for e in range(2*h-1):
        quotient=P//D
        values={s:sum((c*Q((-1)**((7-s)//2))*moment(s,k+(7-s)//2)
                          for k,c in enumerate(quotient)),Q(0)) for s in H}
        slope=Q(0)
        for idx,(j,residue) in enumerate(residues):
            c=residue*powers[idx]
            constants={7:-Q(1,6)+Q(1,2*j),
                       5:-Q(5,12)-Q(j*j,4)+Q(j,2),
                       3:Q(1,12)-Q(j*j,4)-Q(j**4,2)+Q(j**3,2)}
            for s in H:values[s]+=c*(-j**6*H[s][j]+constants[s])
            slope+=c*j**6;powers[idx]*=-j*j
        for s in H:A[s].append(values[s])
        B.append(slope);P*=fmpq_poly([0,1])
    oldA,oldB=engine.entries(K,((N,8),),h)
    assert A[7]==oldA and B==oldB
    # Independent shifted-functional computation, including polynomial parts.
    for s in (3,5):
        r=(7-s)//2;P=W*fmpq_poly([0]*r+[1]);powers=[Q((-j*j)**r) for j,_ in residues]
        check=[]
        for e in range(2*h-1):
            quotient=P//D
            v=sum((c*moment(s,k) for k,c in enumerate(quotient)),Q(0))
            for idx,(j,residue) in enumerate(residues):
                v+=residue*powers[idx]*(-j**(s-1)*H[s][j]-Q(1,s-1)+Q(1,2*j))
                powers[idx]*=-j*j
            check.append(Q((-1)**r)*v);P*=fmpq_poly([0,1])
        assert check==A[s]
    return A,B

def ldlt(M):
    n=len(M);L=[[arb(0) for _ in range(n)] for _ in range(n)];D=[]
    for j in range(n):
        d=M[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),arb(0))
        if not d>0:return None
        D.append(d);L[j][j]=arb(1)
        for i in range(j+1,n):
            L[i][j]=(M[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/d
    return L,D

def ldlt_diagnostic(M):
    n=len(M);L=[[arb(0) for _ in range(n)] for _ in range(n)];D=[]
    for j in range(n):
        d=M[j][j]-sum((L[j][k]**2*D[k] for k in range(j)),arb(0))
        if not d>0:
            return dict(status='negative_pivot' if d<0 else 'inconclusive',pivot_index=j,pivot_ball=d.str(35))
        D.append(d);L[j][j]=arb(1)
        for i in range(j+1,n):
            L[i][j]=(M[i][j]-sum((L[i][k]*L[j][k]*D[k] for k in range(j)),arb(0)))/d
    return dict(status='positive',all_positive_pivots=True,smallest_pivot_lower_bound=min(float(d.lower()) for d in D))

def inverse_lower(L):
    n=len(L);I=[[arb(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        I[j][j]=arb(1)
        for i in range(j+1,n):I[i][j]=-sum((L[i][k]*I[k][j] for k in range(j,i)),arb(0))
    return I

def relative_component(M,I,D):
    n=len(M)
    left=[[sum((I[i][k]*M[k][j] for k in range(i+1)),arb(0)) for j in range(n)] for i in range(n)]
    return [[sum((left[i][k]*I[j][k] for k in range(j+1)),arb(0))/(D[i]*D[j]).sqrt()
                     for j in range(n)] for i in range(n)]

def norm_squared(M):
    return sum((v*v for row in M for v in row),arb(0))

def analyze(K):
    N=max(1,K//40);h=K-N
    A,B=derivative_entries(K,N,h)
    with ctx.workprec(16000):
        z=arb(7).zeta();G=[[arb(A[7][i+j])+z*arb(B[i+j]) for j in range(h)] for i in range(h)]
        baseline=ldlt(G);assert baseline is not None
        L,D=baseline;I=inverse_lower(L)
        rel={s:relative_component([[arb(A[s][i+j]) for j in range(h)] for i in range(h)],I,D) for s in (3,5)}
        norms={s:norm_squared(rel[s]).sqrt() for s in rel}
        rows=[];parameters=[('baseline',Q(0),Q(0))]
        for name,u,v in (('tau5',1,0),('tau3',0,1),('tau5_plus_tau3',1,1),('tau5_minus_tau3',1,-1)):
            R=[[u*rel[5][i][j]+v*rel[3][i][j] for j in range(h)] for i in range(h)]
            nr=norm_squared(R).sqrt()
            exponent=max(0,math.ceil(float((nr.log()/arb(2).log()).upper()))+3)
            for sign in (-1,1):parameters.append((name+'_safe_'+str(sign),Q(sign*u,2**exponent),Q(sign*v,2**exponent)))
        parameters += [('tau5_unit',Q(1),Q(0)),('tau5_minus_unit',Q(-1),Q(0)),('tau3_unit',Q(0),Q(1)),('tau3_minus_unit',Q(0),Q(-1))]
        S=engine.norm_scalar(K,((N,8),),h)
        for name,a,b in parameters:
            aa=[A[7][e]+a*A[5][e]+b*A[3][e] for e in range(2*h-1)]
            poly=engine.determinant(aa,B,h)
            ct=engine.content(poly);primitive=poly/ct
            value=arb(0)
            for c in reversed(list(primitive)):value=value*z+arb(c)
            relative=[[a*rel[5][i][j]+b*rel[3][i][j] for j in range(h)] for i in range(h)]
            ns=norm_squared(relative)
            targetM=[[arb(1 if i==j else 0)+relative[i][j] for j in range(h)] for i in range(h)]
            diagnostic=ldlt_diagnostic(targetM);positive=diagnostic['status']=='positive'
            if name=='baseline' or '_safe_' in name:
                assert positive and ns<1 and value>0
            row=dict(name=name,a=str(a),b=str(b),degree=poly.degree(),
                     denominator_bits=max(int(a.q).bit_length(),int(b.q).bit_length()),
                     relative_frobenius_squared=ns.str(35),relative_norm_sufficient=bool(ns<1),
                     target_gram_positive=positive,relative_ldlt_diagnostic=diagnostic,
                     target_value_sign=1 if value>0 else -1 if value<0 else 0,
                     content=str(ct),primitive_coefficients=[str(c) for c in primitive],
                     primitive_value_interval=value.str(35))
            if value>0 or value<0:
                lv=abs(value).log();lc=arb(S*ct).log()
                row.update(score_ball=(lv/K**2).str(35),score=float((lv/K**2).mid()),
                           arithmetic_ball=(-lc/K**2).str(35),real_log_abs_ball=((lv+lc)/K**2).str(35))
            rows.append(row)
            print('K',K,name,'positive',positive,'J',row.get('score'),flush=True)
        return dict(K=K,N=N,h=h,working_precision_bits=16000,
                    unit_relative_norm_bounds={str(s):norms[s].str(35) for s in norms},rows=rows,
                    independent_entries_checked=4*(2*h-1))

def main():
    result=dict(status='running',scope='finite exact and Arb checks only',rigidity=rigidity_checks(),experiments=[])
    for K in (12,24):
        result['experiments'].append(analyze(K));OUT.write_text(json.dumps(result,indent=2),encoding='utf-8')
    result['status']='finite_exact_and_arb_checks_passed'
    OUT.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('saved',OUT,flush=True)

if __name__=='__main__':main()
