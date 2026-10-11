"""Exact integer certificate for the p12-last-nonzero Pluecker stratum.

Original six coordinates are p01,p02,p03,p12,p13,p23. On p13=p23=0,
p12!=0, the Pluecker equation forces p03=0, leaving p01,p02,p12.
The certificate proves a uniform primitive-polynomial value > exp(25)
at theta=3*zeta(3)+zeta(5), for K=80,N=6 and the saved exact pencil.
"""
import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path
from flint import fmpz_mat as ZMat,fmpq_mat as QMat,arb,arb_poly,arb_mat,ctx
from zeta35_plucker_content import macaulay
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
VARIABLES=[0,1,3]
PAIRS=list(itertools.combinations_with_replacement(VARIABLES,2))
QUADRATIC=[(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]


def basis(rows):
    H=ZMat(rows).hnf()
    return [[int(H[i,j]) for j in range(H.ncols())] for i in range(H.nrows())
            if any(H[i,j] for j in range(H.ncols()))]


def short_generating_subset(rows):
    target=basis(rows)
    chosen=list(range(len(rows)))
    order=sorted(chosen,key=lambda i:max(abs(v).bit_length() for v in rows[i]),reverse=True)
    for i in order:
        trial=[j for j in chosen if j!=i]
        if trial and basis([rows[j] for j in trial])==target:
            chosen=trial
    return target,chosen


def tracked_basis(rows):
    target,selected=short_generating_subset(rows)
    M=ZMat([rows[i] for i in selected])
    H,T=M.hnf(transform=True)
    assert T*M==H
    U=[[0]*len(rows) for row in target]
    for i in range(len(target)):
        for j,k in enumerate(selected):
            U[i][k]=int(T[i,j])
    assert ZMat(U)*ZMat(rows)==ZMat(target)
    return target,U,selected


def generators(force=False):
    path=ROOT/'zeta35_plucker_p12_generators.json'
    src=json.loads((ROOT/'zeta35_two_row_pencil.json').read_text())
    indices=[src['quadratic_monomials'].index(list(pair)) for pair in PAIRS]
    F=[[src['coefficients'][j][k] for j in indices] for k in range(68)]
    if path.exists() and not force:
        cached=json.loads(path.read_text())
        H=[[int(v) for v in row] for row in cached['hnf']]
        U=[[int(v) for v in row] for row in cached['multipliers']]
        assert ZMat(U)*ZMat(F)==ZMat(H)
        return F,H,U,cached['selected_coefficient_indices']
    H,U,selected=tracked_basis(F)
    path.write_text(json.dumps(dict(variables=VARIABLES,quadratic_pairs=PAIRS,
         selected_coefficient_indices=selected,coefficients=F,hnf=H,
         multipliers=[[str(v) for v in row] for row in U],
         identity='U * original restricted coefficient rows = H'),indent=2))
    return F,H,U,selected


def main(force=False):
    start=time.perf_counter()
    F,H,U,selected=generators(force)
    monomials,multiplier_monomials,M=macaulay(H,5,QUADRATIC)
    HH,TT,selected_macaulay=tracked_basis(M)
    n=len(monomials)
    assert len(HH)==n==21
    inverse=QMat(HH).inv()
    d=math.lcm(*(int(v.denominator) for v in inverse.entries()))
    scaled_inverse=inverse*d
    assert all(v.denominator==1 for v in scaled_inverse.entries())
    L=ZMat([[int(scaled_inverse[i,j]) for j in range(n)] for i in range(n)])
    R=L*ZMat(TT)
    identity=ZMat([[d if i==j else 0 for j in range(n)] for i in range(n)])
    assert R*ZMat(M)==identity
    ctx.prec=max(abs(v).bit_length() for row in F for v in row)+6000
    theta=3*arb(3).zeta()+arb(5).zeta()
    q=[arb_poly([row[j] for row in F])(theta) for j in range(6)]
    metric=arb_mat([[q[0],q[1]/2,q[2]/2],[q[1]/2,q[3],q[4]/2],[q[2]/2,q[4]/2,q[5]]])
    B=arb_mat([[q[0],q[1]/2],[q[1]/2,q[3]]])
    sigma=metric.det()/B.det()
    assert q[0]>0 and B.det()>0 and sigma>0
    lower=sigma/d
    assert lower>arb(25).exp()
    result=dict(K=80,N=6,head_dimension=65,tail=[65,66,67,68],tail_weights=[1,1,1,83],
         stratum='p12 != 0 and p13 = p23 = 0, hence p03 = 0',variables=['p01','p02','p12'],
         primitive_parameter_scope='all primitive integer triples with p12 nonzero',
         quadratic_pairs=PAIRS,quadratic_monomials=QUADRATIC,coefficients=F,hnf=H,
         coefficient_to_hnf_multipliers=[[str(v) for v in row] for row in U],
         selected_coefficient_indices=selected,degree=5,monomials=monomials,
         multiplier_monomials=multiplier_monomials,selected_macaulay_rows=selected_macaulay,
         macaulay_multipliers=[[str(R[i,j]) for j in range(R.ncols())] for i in range(R.nrows())],
         content_upper=str(d),content_upper_log=arb(d).log().str(55),
         identity='U*F=H and R*Macaulay(H,5)=d*I21; all matrices integer',
         schur_log=sigma.log().str(55),lower_log=lower.log().str(55),
         theorem='Every rational plane in this stratum has primitive integer polynomial value > exp(25) at theta.',
         seconds=time.perf_counter()-start)
    (ROOT/'zeta35_plucker_p12_certificate.json').write_text(json.dumps(result,indent=2))
    print({k:result[k] for k in ('degree','content_upper_log','schur_log','lower_log','seconds')},flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--rebuild-generators',action='store_true')
    args=parser.parse_args()
    main(args.rebuild_generators)
