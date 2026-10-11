"""Interpret and scale the hyperplane u=(1,4,1,0,...).

Its normal is evaluation at t=-4, hence the polynomial subspace is
(t+4) P_{<h}. Compare full primitive polynomials at equal K, N and h.
"""
import json
import argparse
from pathlib import Path
from flint import fmpq, fmpq_poly, ctx, arb
from joint_exact import (entries_from_polynomial, determinant_pole_split,
                         Dcache, evaluate_primitive_ball, content)


def compute(K,N,h,roots,label):
    multiplier=fmpq_poly([1])
    for s in roots:
        multiplier*=fmpq_poly([s*s,1])
    W=fmpq_poly(Dcache(N))**8*multiplier**2
    aa,bb=entries_from_polynomial(K,W,h)
    poles=fmpq_poly([1])
    for s in range(1,K+1):
        if W(-s*s):
            poles*=fmpq_poly([s*s,1])
    P=determinant_pole_split(aa,bb,poles,h)
    ct,lv,bits=evaluate_primitive_ball(P)
    with ctx.workprec(160):
        score=lv/K**2
        row=dict(K=K,N=N,h=h,roots=roots,label=label,degree=P.degree(),
                 score=float(score.mid()),score_ball=score.str(30),precision_bits=bits,
                 primitive_polynomial=[str(c) for c in P/ct])
    print(json.dumps({k:v for k,v in row.items() if k not in ['primitive_polynomial']}),flush=True)
    return row


def run():
    output=Path(__file__).with_name('forced_pole_subspaces.json');rows=[]
    # First identify the exact polynomial independently of the adjugate code.
    row=compute(24,1,23,[2],'single_pole')
    prior=json.loads(Path(__file__).with_name('joint_padic_existence_K24_N1_m24.json').read_text())
    witness=next(r['witness'] for r in prior['charts'] if r['label']=='radical_2_2_2')
    P=fmpq_poly([fmpq(c) for c in witness['poly']])
    assert P/content(P)==fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])
    row['independent_adjugate_match']=True; rows.append(row)
    jobs=[(24,1,23,[],'baseline')]
    jobs += [(24,1,23,[s],'single_pole') for s in [1,3,4,6,12,24]]
    # Fixed alpha=1/24, a block of N added zeros. Equal h in each pair.
    for N in [2,3,4]:
        K=24*N;h=K-N
        jobs += [(K,N,h,[],'scaled_baseline'),(K,N,h,list(range(N+1,2*N+1)),'scaled_block')]
    # A single fixed zero as K grows is a separate, non-scaling experiment.
    for K in [12,36,48]:
        jobs += [(K,1,K-1,[],'fixed_N_baseline'),(K,1,K-1,[2],'fixed_pole')]
    for args in jobs:
        rows.append(compute(*args))
        output.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
    return rows


def degree_controls():
    rows=[]
    for N in [1,2,3,4]:
        K=24*N
        rows.append(compute(K,N,K-2*N,[],'same_degree_baseline'))
    Path(__file__).with_name('forced_pole_degree_controls.json').write_text(
        json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
    return rows


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--degree-controls',action='store_true')
    args=parser.parse_args()
    degree_controls() if args.degree_controls else run()
