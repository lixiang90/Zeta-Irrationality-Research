"""Exact CRT analysis of the highest-parameter-coefficient determinant.

No sampled Smith pattern is asserted as a uniform theorem.
"""
import argparse,json,time
from pathlib import Path
from collections import Counter
from flint import fmpq_poly,fmpq_mat
from joint_exact import Dcache,entries_from_polynomial,determinant,content
from joint_padic import val,hungarian,residue,smith_slopes
from layer_projection import local_basis
from coupled_schur import integral_solve_certificate,split_layer


def matrices(p,N):
    K=2*p-1;h=K-N
    T=fmpq_poly([1])
    for j in range(2*p,3*p):T*=fmpq_poly([j*j,1])
    aa,bb=entries_from_polynomial(K,Dcache(N)**8*T,h)
    basis,_,tags=local_basis(K,N,p)
    C=fmpq_mat(h,h,[q[j] for q in basis for j in range(h)])
    assert val(C.det(),p)==0
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    return C*A*C.transpose(),C*B*C.transpose(),tags,aa,bb


def analyze(p,N,exact=False):
    A,B,tags,aa,bb=matrices(p,N);h=A.nrows();precision=14
    cost=[[min(val(A[i,j],p),val(B[i,j],p)) for j in range(h)] for i in range(h)]
    u,v,T=hungarian(cost)
    an=[[residue(A[i,j],p,u[i]+v[j],precision) for j in range(h)] for i in range(h)]
    bn=[[residue(B[i,j],p,u[i]+v[j],precision) for j in range(h)] for i in range(h)]
    slopes=smith_slopes(A,B,p,u,v,0,precision)
    cert=integral_solve_certificate(an,bn,p,precision)
    layers=[];m=an
    for level in range(precision):
        if not m:break
        layer,m=split_layer(m,p,precision-level)
        layers.append({k:v for k,v in layer.items() if k not in ('pivot_rows','pivot_columns')})
    out=dict(p=p,N=N,h=h,d=3*N-p+1,target=32*N-13*p+14,
             tropical=T,smith=dict(Counter(slopes)),constant_valuation=T+sum(slopes),
             integral_solve=cert,layers=layers,
             weights=[dict(**tag,row=u[i],col=v[i]) for i,tag in enumerate(tags)])
    if cert['certified']:out['gauss_valuation']=T+sum(slopes)
    if exact:
        out['exact_gauss_valuation']=val(content(determinant(aa,bb,h)),p)
        if cert['certified']:assert out['exact_gauss_valuation']==out['gauss_valuation']
    return out


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='11:4,13:5,17:6,19:7,23:8')
    ap.add_argument('--exact',action='store_true');args=ap.parse_args()
    rows=[];start=time.time();out=Path(__file__).with_suffix('.json')
    for item in args.pairs.split(','):
        p,N=map(int,item.split(':'));r=analyze(p,N,args.exact);rows.append(r)
        out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(json.dumps({k:v for k,v in r.items() if k not in ('weights','layers')})+f' time={time.time()-start:.1f}',flush=True)
        print('weights '+str([(q['c'],q['i'],q['row'],q['col']) for q in r['weights']]),flush=True)
