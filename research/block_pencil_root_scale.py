"""Exact rational root brackets for 2 B_(N,L)-B_(N+s,L)."""
import json,math
from fractions import Fraction as F
from pathlib import Path
from restart_obstruction_certificate import log_iv,outward_decimal,iv


def sign(N,L,s,t,r=1):
    a,b=t.numerator,t.denominator
    original=math.prod(a+b*j*j for j in range(N+1,N+L+1))
    shifted=math.prod(a+b*(j+s)**2 for j in range(N+1,N+L+1))
    value=r*shifted-(r+1)*original
    return (value>0)-(value<0)


def bracket(K,N,L,s,r=1):
    lo=F(0);hi=F(1);assert sign(N,L,s,lo,r)>0
    while sign(N,L,s,hi,r)>0:hi*=2
    for _ in range(60):
        mid=(lo+hi)/2;sgn=sign(N,L,s,mid,r)
        if sgn==0:lo=hi=mid;break
        if sgn>0:lo=mid
        else:hi=mid
    assert sign(N,L,s,lo,r)>=0 and sign(N,L,s,hi,r)<=0
    return dict(K=K,N=N,L=L,s=s,r=r,root_interval=[str(lo),str(hi)],
                root_over_K2=[str(lo/K**2),str(hi/K**2)],
                root_over_K3=[str(lo/K**3),str(hi/K**3)],
                root_over_K3_float=float((lo+hi)/(2*K**3)))


def main():
    rows=[bracket(24*m,m,3*m,m) for m in (1,2,4,8,16,32,64)]
    constant=iv(F(1,768))/log_iv(2)
    result=dict(theoretical_limit=outward_decimal(constant),rows=rows)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(theoretical_limit=result['theoretical_limit'],
                         rows=[{k:r[k] for k in ('K','root_over_K3_float')} for r in rows])),flush=True)


if __name__=='__main__':main()
