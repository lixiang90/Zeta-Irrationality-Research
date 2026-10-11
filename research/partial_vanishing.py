"""Partial zero constraints in a positive Gram subspace.

V(r,M,h) = span(1,...,t^(r-1), D_M,...,t^(h-r-1) D_M), M>=r.
M=r is exactly the old full polynomial space, and must give the same polynomial.
M>r changes the subspace. Mixed versions are positive by Cauchy-Binet and
total nonnegativity of the Toeplitz coefficient matrix of D_M.
"""
import argparse
import json
import time
from pathlib import Path
from flint import fmpq_poly
from joint_exact import Dcache
from mixed_subspaces import run, exponents


def basis(h,r,M):
    assert 0 <= r <= M and r < h
    return [fmpq_poly([0]*i+[1]) for i in range(r)]+[
        fmpq_poly(Dcache(M))*fmpq_poly([0]*j+[1]) for j in range(h-r)]


def run_design(K,profile,h,r,gap,mode):
    M=r+gap
    C=basis(h,r,M);E=[p.degree() for p in C]
    F=E if mode=='symmetric' else list(range(h))
    D=C if mode=='symmetric' else None
    row,P,A,B=run(K,profile,E,F,H=h+gap,polys_E=C,polys_F=D)
    assert P.degree() <= min(h,K-max(n for n,b in profile),r+max(0,K-M))
    row.update(basis_type='partial_D',split=r,M=M,gap=gap,mode=mode)
    return row,P,A,B


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--K',type=int,default=24)
    ap.add_argument('--refine',action='store_true');args=ap.parse_args()
    K=args.K;assert K%24==0;m=K//24;start=time.time()
    out=Path(__file__).with_name(f'partial_vanishing{K}.json');rows=[];jobs=[]
    if args.refine:
        prior=json.loads(Path(__file__).with_name('partial_vanishing24.json').read_text())
        chosen=sorted([r for r in prior if r['gap']],key=lambda r:r['score_per_lambda'])[:4]
        for r in chosen:
            profile=[(n*m,b) for n,b in r['profile']]
            jobs.append((profile,r['h']*m,r['split']*m,r['gap']*m,r['mode']))
            jobs.append((profile,r['h']*m,r['split']*m,0,r['mode']))
    else:
        for profile in [[(m,8)],[(m,3),(2*m,3)],[(m,4),(2*m,2)],[(m,3),(2*m,2),(3*m,1)]]:
            h=K
            for r in [h//3,2*h//3]:
                for gap in [0,2*m,4*m,6*m]:
                    for mode in ['mixed','symmetric']:
                        jobs.append((profile,h,r,gap,mode))
    done=set()
    for profile,h,r,gap,mode in jobs:
        key=(tuple(profile),h,r,gap,mode)
        if key in done:continue
        done.add(key)
        row,*_=run_design(K,profile,h,r,gap,mode);rows.append(row)
        out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        if args.refine or len(rows)%8==0:
            best=min(rows,key=lambda r:r['score_per_lambda'])
            print(f"K={K} cases={len(rows)} best={best['score']:.9f} split={best['split']} gap={best['gap']} mode={best['mode']} seconds={time.time()-start:.1f}",flush=True)
    print('completed',len(rows),'seconds',time.time()-start,flush=True)


if __name__=='__main__':main()
