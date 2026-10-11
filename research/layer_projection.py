"""Investigate the relative position of the exceptional-moment correction.

Exact rational matrices; mod-p ranks are exact. Higher Smith slopes are still
specializations unless separately certified, as explicitly labelled in output.
"""
import argparse,json,time
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq,fmpq_poly,fmpq_mat,nmod_mat
from joint_exact import entries,Dcache,moment,experiment
from joint_padic import val,residue,analyze
from joint_outer_strong import delta_bound


def local_basis(K,N,p):
    tail=list(range(N+1,K+1));classes={}
    for j in tail:classes.setdefault(min(j%p,(-j)%p),[]).append(j)
    polys=[];weights=[];tags=[]
    for c,inside in sorted(classes.items()):
        base=fmpq_poly([1]);big=fmpq_poly([1])
        for j in tail:
            if j not in inside:base*=fmpq_poly([j*j,1])
        larger=[j for j in inside if j>p]
        for j in larger:big*=fmpq_poly([j*j,1])
        nb=len(larger)
        ell=sum(min(j%p,(-j)%p)==c for j in range(1,K+1))
        for i in range(len(inside)):
            polys.append(base*(fmpq_poly([c*c,1])**i if i<nb else big*fmpq_poly([c*c,1])**(i-nb)))
            weights.append(-F(2*ell-1,2) if c==0 else
                           min(F(0),i+4*int(c<=N)-F(ell+6,2)) if i<nb else F(0))
            tags.append(dict(c=c,i=i,ell=ell,nb=nb,delta=int(0<c<=N)))
    return polys,weights,tags


def local_data(K,N,p):
    h=K-N;aa,bb=entries(K,[(N,8)],h)
    polys,weights,tags=local_basis(K,N,p)
    C=fmpq_mat(h,h,[v[j] for v in polys for j in range(h)])
    assert val(C.det(),p)==0
    A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    P=Dcache(N)**8;D=Dcache(K);bad=[];t=fmpq_poly([0,1])
    for e in range(2*h-1):
        quotient=P//D
        bad.append(sum((quotient[k]*moment(k) for k in range(3*p-4,quotient.degree()+1)),fmpq(0)))
        P*=t
    Y=fmpq_mat(h,h,[bad[i+j] for i in range(h) for j in range(h)])
    return C*A*C.transpose(),C*B*C.transpose(),C*Y*C.transpose(),weights,tags


def modrank(M,p,rows,cols,shift=-1):
    if not rows or not cols:return 0
    return nmod_mat(len(rows),len(cols),[residue(M[i,j],p,shift) for i in rows for j in cols],p).rank()


def run(K,N,p):
    _,P,*_=experiment(K,[(N,8)],K-N)
    A,B,Y,w,tags=local_data(K,N,p);h=K-N
    allrows=list(range(h));zero=[i for i in allrows if w[i]==0]
    half=[i for i in allrows if w[i]==-F(1,2)]
    bound,parts=delta_bound(K,N,p)
    result=dict(K=K,N=N,p=p,previous_bound=bound,previous_parts=parts,
                correction_rank=Y.rank(),mod_p_correction_rank=modrank(Y,p,allrows,allrows),
                zero_block_rank=modrank(Y,p,zero,zero),zero_half_block_rank=modrank(Y,p,zero+half,zero+half),
                zero_rows=len(zero),half_rows=len(half),local=analyze(A,B,P,p))
    result['zero_tags']=[tags[i] for i in zero]
    result['zero_block_row_support']=[sum(residue(Y[i,j],p,-1)!=0 for j in zero) for i in zero]
    return result


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='32:4:11,40:5:17,48:6:17,56:7:19,64:8:23')
    args=ap.parse_args();rows=[];start=time.time();out=Path(__file__).with_suffix('.json')
    for item in args.pairs.split(','):
        K,N,p=map(int,item.split(':'));r=run(K,N,p);rows.append(r)
        out.write_text(json.dumps(rows,indent=2),encoding='utf-8')
        print(json.dumps(r)+f' elapsed={time.time()-start:.1f}',flush=True)
