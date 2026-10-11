"""Handle the degree-p boundary a=0 by certifying its top delta coefficient.

The top coefficient splits into a residue Vandermonde determinant and a
smaller full X-pencil after multiplying the numerator by T_delta^2.
"""
import json,time,argparse
from pathlib import Path
from math import factorial
from flint import fmpq,fmpq_poly,fmpq_mat
from joint_exact import Dcache,entries_from_polynomial,content,determinant
from joint_padic import val,hungarian,smith_slopes
from coupled_candidate_law import prediction
from parameter_bundle import point


def leading(K,N,p,exact=False):
    assert K==3*p-1
    h=K-N;m=p;s=h-m
    T=fmpq_poly([1])
    for j in range(2*p,K+1):T*=fmpq_poly([j*j,1])
    vdet=-7*m
    for j in range(2*p,K+1):
        gamma=fmpq(2*factorial(j+N)**8,factorial(j-N-1)**8*factorial(K-j)*factorial(K+j))
        vdet+=val(gamma,p)
    for j in range(2*p,K+1):
        for k in range(j+1,K+1):vdet+=2*val(fmpq(k*k-j*j),p)
    aa,bb=entries_from_polynomial(K,Dcache(N)**8*T*T,s)
    A=fmpq_mat(s,s,[aa[i+j] for i in range(s) for j in range(s)])
    B=fmpq_mat(s,s,[bb[i+j] for i in range(s) for j in range(s)])
    cost=[[min(val(A[i,j],p),val(B[i,j],p)) for j in range(s)] for i in range(s)]
    u,v,trop=hungarian(cost)
    ss=smith_slopes(A,B,p,u,v,0,precision=18)
    assert max(ss)<18
    bm=min(val(B[i,j],p)-u[i]-v[j] for i in range(s) for j in range(s))
    low=trop+sum(min(q,bm) for q in ss)
    result=dict(residue_block=vdet,bottom_tropical=trop,B_min=bm,
                bottom_smith=ss,lower=vdet+low,exact=(bm>=max(ss)))
    if exact:
        P=determinant(aa,bb,s)
        result['exact_polynomial_valuation']=vdet+val(content(P),p)
        assert result['exact_polynomial_valuation']>=result['lower']
        if result['exact']:assert result['exact_polynomial_valuation']==result['lower']
        result['lower']=result['exact_polynomial_valuation']
        result['exact']=True
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='32:4:11,38:5:13,50:6:17,68:8:23,128:16:43')
    ap.add_argument('--out',default='parameter_boundary.json');ap.add_argument('--leading-only',action='store_true')
    args=ap.parse_args();rows=[];out=Path(__file__).with_name(args.out);start=time.time()
    for item in args.pairs.split(','):
        K,N,p=map(int,item.split(':'));pre=prediction(K,N,p);top=leading(K,N,p,exact=True)
        r=dict(K=K,N=N,p=p,target=pre['gauss'],leading=top)
        print('TOP '+json.dumps(r)+f' elapsed={time.time()-start:.1f}s',flush=True)
        if not args.leading_only and top['lower']>=pre['gauss']:
            values=[point(K,N,p,d) for d in range(p)]
            lower=min([top['lower']]+[v['gauss_lower'] for v in values])
            r.update(values=values,coefficient_gauss_lower=lower,
                     all_p_integral_parameters_certified=lower>=pre['gauss'])
        rows.append(r);out.write_text(json.dumps(dict(rows=rows),indent=2))
