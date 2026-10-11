"""Higher-degree coefficient ideals bound the content of primitive triples.

For degree D, multiply the six integer quadratic generators by all monomials
of degree D-2. A local row-module exponent annihilates every degree-D monomial,
so it bounds the p-adic content on ALL primitive integer triples.
"""
import argparse
import json
import math
import sys
import time
from pathlib import Path
from flint import arb, arb_poly, arb_mat, ctx
from sympy import factorint
sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def monomials(d):
    return [(i,j,d-i-j) for i in range(d,-1,-1) for j in range(d-i,-1,-1)]


def macaulay(H,degree):
    columns = monomials(degree)
    index = {m:i for i,m in enumerate(columns)}
    quadratic = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
    out = []
    for m in monomials(degree-2):
        positions = [index[tuple(a+b for a,b in zip(m,q))] for q in quadratic]
        for row in H:
            target = [0]*len(columns)
            for j,v in zip(positions,row):
                target[j] = v
            out.append(target)
    return columns,out


def vp(x,p,cap):
    if not x:
        return cap
    e = 0
    while e < cap and x%p == 0:
        x //= p
        e += 1
    return e


def local_smith(matrix,p,cap):
    modulus = p**(cap+1)
    A = [[v%modulus for v in row] for row in matrix]
    rows,cols = len(A),len(A[0])
    valuations = []
    for k in range(cols):
        best = cap+1
        selected = None
        for i in range(k,rows):
            for j in range(k,cols):
                v = vp(A[i][j],p,best)
                if v < best:
                    best,selected = v,(i,j)
                    if best == 0:
                        break
            if best == 0:
                break
        assert selected is not None and best <= cap
        i,j = selected
        A[k],A[i] = A[i],A[k]
        if j != k:
            for row in A:
                row[k],row[j] = row[j],row[k]
        pivot = p**best
        inv = pow(A[k][k]//pivot,-1,modulus)
        A[k] = [(v*inv)%modulus for v in A[k]]
        assert A[k][k] == pivot
        for i in range(k+1,rows):
            multiplier = A[i][k]//pivot
            assert A[i][k]%pivot == 0
            if multiplier:
                A[i] = [0]*(k+1)+[(A[i][j]-multiplier*A[k][j])%modulus for j in range(k+1,cols)]
        # Clearing pivot-row entries by column operations does not change the
        # remaining submatrix, since its pivot column has just become zero.
        valuations.append(best)
    assert valuations == sorted(valuations)
    return valuations


def run(max_degree):
    src = json.loads((ROOT/'zeta35_three_direction_bound.json').read_text())
    H,cols = src['hnf'],src['coefficients']
    factors = {int(p):int(e) for p,e in factorint(int(src['smith_exponent'])).items()}
    ctx.prec = max(abs(c).bit_length() for col in cols for c in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    q = [arb_poly(col)(theta) for col in cols]
    M = arb_mat([[q[0],q[1]/2,q[2]/2],[q[1]/2,q[3],q[4]/2],[q[2]/2,q[4]/2,q[5]]])
    spectral_lower = 4*M.det()/(q[0]+q[3]+q[5])**2
    assert spectral_lower > 0
    rows = []
    for degree in range(2,max_degree+1):
        start = time.perf_counter()
        mons,mat = macaulay(H,degree)
        local = {p:local_smith(mat,p,cap) for p,cap in factors.items()}
        upper = math.prod(p**max(v) for p,v in local.items())
        bound = spectral_lower/upper
        row = dict(degree=degree,shape=[len(mat),len(mons)],local=local,
                   content_upper=str(upper),upper_log=float(arb(upper).log()),
                   lower_log=bound.log().str(45),lower_log_float=float(bound.log()),
                   seconds=time.perf_counter()-start)
        rows.append(row)
        (ROOT/'zeta35_macaulay_content.json').write_text(json.dumps(dict(scope='all primitive triples',rows=rows),indent=2))
        print('DEGREE',degree,'LOCAL',[(p,max(v)) for p,v in local.items()],
              'UPPER_LOG',row['upper_log'],'LOWER_LOG',row['lower_log'],'SECONDS',row['seconds'],flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--max-degree',type=int,default=6)
    args = p.parse_args()
    run(args.max_degree)
