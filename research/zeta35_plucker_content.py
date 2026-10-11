"""Macaulay ranks and optional exact integer exponents for Gr(2,4).

Coefficient generators of the exact two-row pencil are supplemented by
p01*p23-p02*p13+p03*p12. Finite-degree HNF computations are exact algorithm
results; only the separate p12 certificate supplies original-ideal integer
multipliers independently checked without HNF.
"""
import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path
from flint import fmpz_mat as ZMat,fmpq_mat as QMat
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def monomials(degree,variables=6):
    if variables==1:
        return [(degree,)]
    return [(first,)+rest for first in range(degree,-1,-1)
            for rest in monomials(degree-first,variables-1)]


def macaulay(H,degree,quadratic):
    variables=len(quadratic[0])
    mons=monomials(degree,variables)
    positions={m:i for i,m in enumerate(mons)}
    rows=[]
    multipliers=monomials(degree-2,variables)
    for m in multipliers:
        indices=[positions[tuple(a+b for a,b in zip(m,q))] for q in quadratic]
        for h in H:
            row=[0]*len(mons)
            for j,v in zip(indices,h):
                row[j]=v
            rows.append(row)
    return mons,multipliers,rows


def modular_rank(rows,prime):
    # Full modular column rank proves full rank over Q.
    pivots={}
    for source in rows:
        row=[v%prime for v in source]
        while True:
            lead=next((j for j,x in enumerate(row) if x),None)
            if lead is None:
                break
            if lead not in pivots:
                inverse=pow(row[lead],-1,prime)
                pivots[lead]=[(x*inverse)%prime for x in row]
                break
            multiple=row[lead]
            pivot=pivots[lead]
            for j in range(lead,len(row)):
                row[j]=(row[j]-multiple*pivot[j])%prime
        if len(pivots)==len(source):
            break
    return len(pivots)


def degree_two_generators(rebuild=False):
    path=ROOT/'zeta35_plucker_degree2.json'
    if path.exists() and not rebuild:
        return json.loads(path.read_text())
    source=json.loads((ROOT/'zeta35_two_row_pencil.json').read_text())
    rows=list(map(list,zip(*source['coefficients'])))+[source['relation']]
    H=ZMat(rows).hnf()
    basis=[[int(H[i,j]) for j in range(21)] for i in range(H.nrows())
           if any(H[i,j] for j in range(21))]
    out=dict(hnf=basis,quadratic_monomials=source['quadratic_monomials'],
             relation=source['relation'],common_scale=source['common_rational_scale'],
             exact_hnf_algorithm_result=True,explicit_reverse_inclusion_certificate=False)
    path.write_text(json.dumps(out,indent=2))
    return out


def integer_exponent(rows):
    H=ZMat(rows).hnf()
    n=H.ncols()
    assert all(H[i,j]==0 for i in range(n,H.nrows()) for j in range(n))
    basis=ZMat([[H[i,j] for j in range(n)] for i in range(n)])
    inverse=QMat(basis).inv()
    d=math.lcm(*(int(v.denominator) for v in inverse.entries()))
    scaled=inverse*d
    assert all(v.denominator==1 for v in scaled.entries())
    R=ZMat([[int(scaled[i,j]) for j in range(n)] for i in range(n)])
    assert R*basis==ZMat([[d if i==j else 0 for j in range(n)] for i in range(n)])
    return dict(exponent=str(d),exponent_log=math.log(d),
                hnf=[[str(basis[i,j]) for j in range(n)] for i in range(n)],
                scaled_hnf_inverse=[[str(R[i,j]) for j in range(n)] for i in range(n)],
                inverse_identity='scaled_hnf_inverse * HNF = exponent * I',
                exact_hnf_algorithm_result=True,
                explicit_original_ideal_membership_certificate=False)


def run(max_degree,integer_degrees,rebuild=False):
    src=degree_two_generators(rebuild)
    H,quad=src['hnf'],src['quadratic_monomials']
    quadratic=[tuple(2 if i==a==b else 1 if i==a or i==b else 0
                     for i in range(6)) for a,b in quad]
    results=[]
    for degree in range(2,max_degree+1):
        start=time.perf_counter()
        mons,mult,rows=macaulay(H,degree,quadratic)
        ranks={str(p):modular_rank(rows,p) for p in (1000000007,1000000009)}
        full=any(r==len(mons) for r in ranks.values())
        item=dict(degree=degree,shape=[len(rows),len(mons)],modular_ranks=ranks,
                  rational_full_rank_verified=full)
        if degree in integer_degrees:
            assert full,'An exponent annihilating the whole degree component requires full rank.'
            exact=integer_exponent(rows)
            (ROOT/f'zeta35_plucker_degree{degree}_hnf.json').write_text(json.dumps(dict(degree=degree,**exact),indent=2))
            item.update(exponent=exact['exponent'],exponent_log=exact['exponent_log'],
                        exact_hnf_algorithm_result=True)
        item['seconds']=time.perf_counter()-start
        results.append(item)
        (ROOT/'zeta35_plucker_content.json').write_text(json.dumps(dict(
             source='zeta35_two_row_pencil.json',variables=['p01','p02','p03','p12','p13','p23'],
             quadratic_generators=len(H),quadratic_monomials=quad,rows=results),indent=2))
        print({k:v for k,v in item.items() if k!='exponent'},flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-degree',type=int,default=4)
    parser.add_argument('--integer-degree',action='append',type=int,default=[])
    parser.add_argument('--rebuild-degree-two',action='store_true')
    args=parser.parse_args()
    run(args.max_degree,args.integer_degree,args.rebuild_degree_two)
