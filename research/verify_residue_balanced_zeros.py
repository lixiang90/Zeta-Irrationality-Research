"""Rational separation certificates and whole-polynomial checks for exchanges."""
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from flint import fmpq,fmpq_poly,fmpz_mat
from joint_exact import Dcache,entries_from_polynomial


def unique_certificate(K,N,M,primes):
    js=list(range(N+1,K+1));rows=[[1]*len(js)];labels=['cardinality']
    for p in primes:
        for c in range((p+1)//2):
            rows.append([int(min(j%p,(-j)%p)==c) for j in js]);labels.append(f'{p}:{c}')
    mat=np.array(rows,dtype=float);sign=np.array([1 if j<=M else -1 for j in js])
    lp=linprog(np.zeros(len(rows)),A_ub=-sign[:,None]*mat.T,
               b_ub=-np.ones(len(js)),bounds=[(None,None)]*len(rows),method='highs')
    if not lp.success:return dict(K=K,N=N,M=M,primes=primes,certified=False,status=str(lp.message))
    y=[F(float(x)).limit_denominator(1000000) for x in lp.x]
    den=math.lcm(*(v.denominator for v in y));y=[int(v*den) for v in y]
    g=math.gcd(*y);y=[v//g for v in y]
    coefficients=[sum(y[i]*rows[i][j] for i in range(len(rows))) for j in range(len(js))]
    assert all(c>=1 if j<=M else c<=-1 for j,c in zip(js,coefficients))
    return dict(K=K,N=N,M=M,primes=primes,certified=True,
                nonzero_multipliers={label:v for label,v in zip(labels,y) if v},
                column_coefficients=coefficients,
                min_signed_margin=min(c if j<=M else -c for j,c in zip(js,coefficients)),
                scope='unique even among real solutions in [0,1]')


def check_polynomial(row):
    K,N,M,h=(row[k] for k in ('K','N','M','h'));t=fmpq_poly([0,1]);DA=fmpq_poly([1])
    for j in row['set']:DA*=t+j*j
    aa,bb=entries_from_polynomial(K,Dcache(N)**6*DA**2,h)
    P=fmpq_poly([fmpq(x) for x in row['primitive_polynomial']])*fmpq(row['content'])
    den=math.lcm(*(int(x.q) for x in aa+bb));scale=den**h
    for x in range(h+1):
        matrix=fmpz_mat(h,h,[int(den*(aa[i+j]+x*bb[i+j])) for i in range(h) for j in range(h)])
        assert matrix.det()==P(x)*scale
    return dict(K=K,N=N,M=M,h=h,set=row['set'],determinant_specializations=h+1,verified=True)


def main():
    folder=Path(__file__).parent;data=json.loads((folder/'residue_balanced_zeros.json').read_text())['rows']
    unique=[];polys=[];seen=set()
    for row in data:
        if not row['selection']['changed']:
            unique.append(unique_certificate(row['K'],row['N'],row['M'],row['primes']))
        else:
            result=row['result'];key=(row['K'],tuple(result['set']))
            if key not in seen:polys.append(check_polynomial(result));seen.add(key)
    output=dict(separation_certificates=unique,full_polynomial_certificates=polys)
    (folder/'residue_balanced_zeros_validation.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print(json.dumps(output),flush=True)


if __name__=='__main__':main()
