"""Finite exact tests of the mixed functional b*mu5(f)-a*mu3(t*f).

The symbolic parameter is X=a*zeta(3)+b*zeta(5). This is an exploratory
arithmetic test, not a transferred asymptotic divisibility theorem.
"""
import sys,json,math,importlib.util
from pathlib import Path
from flint import fmpq as Q,fmpq_poly,fmpz_poly,fmpq_mat,arb,arb_poly,ctx

sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('original_hankel',root/'Zeta5-mo271/scripts/hankel.py')
original=importlib.util.module_from_spec(spec);spec.loader.exec_module(original)

def mu3(k):return Q(-1)**k*(2*k+3)*Q.bernoulli(2*k+2)/2

def shifted_mu3_entries(n):
    K,N,h=40*n,3*n,37*n;DN=original.Dpoly(N);DK=original.Dpoly(K)
    W=fmpq_poly(DN**6);DK=fmpq_poly(DK);E=2*h-1
    H=[Q(0)]
    for j in range(1,K+1):H.append(H[-1]+Q(1,j**3))
    residues={}
    for j in range(N+1,K+1):
        den=math.prod(k*k-j*j for k in range(1,K+1) if k!=j)
        residues[j]=Q(DN(-j*j))**6/den
    answer=[]
    for e in range(E):
        quotient=(W*fmpq_poly([0]*e+[1]))//DK
        value=sum((quotient[k]*mu3(k+1) for k in range(quotient.degree()+1)),Q(0))
        for j,c in residues.items():
            value+=c*Q(-j*j)**e*(Q(j**4)*H[j]+Q(j*j-j,2)+Q(1,4))
        answer.append(value)
    return answer

def main():
    K,N,h,A5,B=original.entries(1);A3t=shifted_mu3_entries(1)
    rows=[]
    for aa,bb in ((0,1),(-1,1),(1,1),(3,1),(4,1)):
        A=[bb*x-aa*y for x,y in zip(A5,A3t)]
        delta=original.det_poly(h,A,B);assert delta.degree()==h
        den=math.lcm(*(int(delta[i].denominator) for i in range(h+1)))
        nums=[int(delta[i]*den) for i in range(h+1)];g=math.gcd(*nums);content=Q(g,den)
        primitive=[x//g for x in nums];assert math.gcd(*primitive)==1
        bits=max(abs(x).bit_length() for x in primitive);ctx.prec=bits+K*K+4000
        theta=aa*arb(3).zeta()+bb*arb(5).zeta()
        value=arb_poly(primitive)(theta);positive=value>0;nonzero=not value.contains(0)
        logabs=abs(value).log() if nonzero else None
        # Exact independent determinant evaluations check interpolation values.
        checks=[]
        for x in (Q(-1),Q(0),Q(1),Q(2),Q(1,2)):
            v=fmpq_mat([[A[i+j]+x*B[i+j] for j in range(h)] for i in range(h)]).det()
            assert v==delta(x);checks.append(str(x))
        row=dict(a=aa,b=bb,n=1,K=K,N=N,h=h,constant_entries=list(map(str,A)),
                 linear_entries=list(map(str,B)),primitive_coefficients=list(map(str,primitive)),
                 content=str(content),value_interval=str(value),positive=positive,
                 log_abs_interval=str(logabs),log_abs_approx=float(logabs) if logabs is not None else None,
                 max_coefficient_bits=bits,determinant_check_points=checks,
                 weight_globally_positive=(aa<=3))
        rows.append(row);print('mixed',aa,bb,'log|P|',row['log_abs_approx'],'positive',positive,flush=True)
    result=dict(status='finite_checks_passed',scope='n=1 only; no asymptotic arithmetic claim',rows=rows)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')

if __name__=='__main__':main()
