"""Independent exact checks for head-zero dimension and partial fractions."""
import json
import math
from pathlib import Path

import sympy as sp
from flint import fmpq, fmpq_poly
from parameter_space_quotient import coefficient_rows, rank
from critical_lift_probe import output_map


def check_rank(s,n,M,L):
    columns,_,out=coefficient_rows(s,n)
    rows=[]
    for m in range(1,M+1):
        rows.append([(-1)**(m-k)*sp.binomial(m-1,k-1)*j**(m-k)
                     if k<=m else 0 for k,j in columns])
    for t in range(1,L+1):
        rows.append([sp.Rational(1,(t+j)**k) for k,j in columns])
    a=sp.Matrix(rows);r=rank(a)
    dim=len(columns)-r
    image=rank(a.col_join(out))-r
    assert dim==max(s*(n+1)-M-L,0)
    assert dim-image==max(s*n-M-L,0)
    assert image==min(s,max(s*(n+1)-M-L,0))
    return dict(s=s,n=n,M=M,L=L,dimension=dim,output_rank=image)


def check_pf(n,L):
    degrees=(0,2,4,6)
    _,local=output_map(n,head=L,degrees=degrees)
    t=fmpq_poly([0,1]);den=fmpq_poly([1])
    for j in range(n+1):den*=(t+j)**7
    x=2*t+n;head=fmpq_poly([1])
    for ell in range(1,L+1):head*=x*x-(n+2*ell)**2
    for col,d in enumerate(degrees):
        rebuilt=fmpq_poly([0])
        for j in range(n+1):
            for k in range(1,8):
                quotient,remainder=divmod(den,(t+j)**k)
                assert remainder==0
                rebuilt+=local[j][col][k]*quotient
        assert rebuilt==head*x**d
    return dict(n=n,L=L,full_polynomial_identities=len(degrees))


def main():
    ranks=[check_rank(s,n,M,L) for s in (3,7) for n in (1,2)
           for M in sorted(set((1,s*n-2,s*n,s*n+1))) for L in (0,1,3)]
    pf=[check_pf(n,L) for n,L in ((2,0),(4,4),(8,8))]
    result=dict(rank_cases=len(ranks),full_polynomial_identities=sum(r['full_polynomial_identities'] for r in pf),ranks=ranks,partial_fraction_checks=pf)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if isinstance(v,int)}))


if __name__=='__main__':main()
