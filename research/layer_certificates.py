"""Generic Gauss-valuation certificates from a p-adically stable pencil.

If the integral normalized A has Smith exponents <= s and every entry of B
is divisible by p^s, then det(A+XB)/det(A) is p-integral with constant term 1.
Thus the entire polynomial's Gauss valuation equals v(det A). No sampled-X
extrapolation is used when generic_certified is true.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction as F
from sympy import primerange
from joint_padic import val,hungarian,smith_slopes
from joint_outer_strong import delta_bound
from layer_projection import local_data,modrank


def certify(K,N,p,exact_det=False):
    A,B,Y,w,tags=local_data(K,N,p);h=K-N
    cost=[[min(val(A[i,j],p),val(B[i,j],p)) for j in range(h)] for i in range(h)]
    u,v,T=hungarian(cost)
    slopes=smith_slopes(A,B,p,u,v,0,precision=16)
    assert max(slopes)<16
    Bmin=min(val(B[i,j],p)-u[i]-v[j] for i in range(h) for j in range(h))
    total=T+sum(slopes)
    if exact_det:assert val(A.det(),p)==total
    Z=[i for i in range(h) if w[i]==0];H=[i for i in range(h) if w[i]==-F(1,2)]
    projected=modrank(Y,p,Z+H,Z)
    old,parts=delta_bound(K,N,p)
    projection_bound=parts['weight2']+parts['zero']-min(parts['rank'],projected)
    assert total>=projection_bound
    r=dict(K=K,N=N,p=p,previous_bound=old,projected_rank=projected,
           projection_bound=projection_bound,tropical=T,normalized_B_min=Bmin,
           smith_counts={str(s):slopes.count(s) for s in sorted(set(slopes))},
           smith_sum=sum(slopes),specialized_valuation=total,
           generic_certified=Bmin>=max(slopes),all_integral_X_stable=Bmin>max(slopes),
           exact_det_crosscheck=exact_det)
    if r['generic_certified']:
        r['generic_valuation']=total;r['gain_over_previous']=total-old
    if 3*p<=K+N+1 and K<3*p:
        r['six_class_weight_candidate']=max(29*N-3*K-10*p+12,
                                            34*N-2*K-14*p+15,38*N-2*K-15*p+17)
        assert T>=r['six_class_weight_candidate'],r
    return r


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['targets','grid','scale'],default='targets')
    args=ap.parse_args();rows=[];start=time.time()
    if args.mode=='targets':jobs=[(32,4,11),(40,5,17),(48,6,17),(56,7,19),(64,8,23)]
    elif args.mode=='grid':jobs=[(3*p-1,N,p) for p in [11,13,17,19,23] for N in range(1,(3*p-1)//8+1)]
    else:
        jobs=[(8*N,N,p) for N in [4,6,8,10,12,14,16]
              for p in primerange((8*N)//3+1,(9*N+1)//3+1)]
    out=Path(__file__).with_name(f'layer_certificates_{args.mode}.json')
    for K,N,p in jobs:
        r=certify(K,N,p,exact_det=args.mode=='targets');rows.append(r)
        out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(json.dumps(r)+f' elapsed={time.time()-start:.1f}',flush=True)
