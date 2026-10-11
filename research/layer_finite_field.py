"""Bernoulli-free computation of the exceptional-moment pairing over F_p.

If Q=(D_K F_p^6)/gcd(W,D_K F_p^6), U=W/gcd(...), then
  pY_ij mod p = -1/6 * coeff_{deg Q-1}(U E_i E_j mod Q).
Only exact finite-field polynomial arithmetic is used here.
"""
import json,time
from pathlib import Path
from fractions import Fraction as F
from flint import nmod_poly,nmod_mat
from layer_projection import local_data
from joint_padic import residue
from layer_uniform_rank import rank_cap


def data(K,N,p):
    assert p>2*N and p>=7 and 2*K<p*p
    h=K-N;D=nmod_poly([1],p);W=nmod_poly([1],p);tail=nmod_poly([1],p)
    classes={}
    for j in range(1,K+1):
        factor=nmod_poly([j*j,1],p);D*=factor
        if j<=N:W*=factor**8
        else:
            tail*=factor;classes.setdefault(min(j%p,(-j)%p),[]).append(j)
    m=(p-1)//2;Fpoly=nmod_poly([-(-1)**m]+[0]*(m-1)+[1],p)
    denominator=D*Fpoly**6;g=W.gcd(denominator);U=W//g;Q=denominator//g
    assert Q[Q.degree()]==1
    basis=[];weights=[]
    for c,inside in sorted(classes.items()):
        factor=nmod_poly([c*c,1],p);O=tail//(factor**len(inside))
        ell=len(inside)+int(0<c<=N);nb=sum(j>p for j in inside)
        for i in range(len(inside)):
            basis.append(O*factor**i)
            weights.append(-F(2*ell-1,2) if c==0 else
                           min(F(0),i+4*int(c<=N)-F(ell+6,2)) if i<nb else F(0))
    assert len(basis)==h
    return U,Q,basis,weights


def gram(K,N,p,full=False):
    U,Q,E,w=data(K,N,p);h=K-N;d=Q.degree();scale=-pow(6,-1,p)%p
    Z=[i for i in range(h) if w[i]==0];H=[i for i in range(h) if w[i]==-F(1,2)]
    rows=list(range(h)) if full else Z+H;cols=list(range(h)) if full else Z
    UE=[(U*E[i])%Q for i in rows]
    values=([int(((a*E[j])%Q)[d-1])*scale%p for a in UE for j in cols]
            if d else [0]*(len(rows)*len(cols)))
    M=nmod_mat(len(rows),len(cols),values,p)
    return M,rows,cols,w


if __name__=='__main__':
    checked=[];scaled=[];start=time.time()
    for K,N,p in [(32,4,11),(40,5,17),(48,6,17),(56,7,19),(64,8,23),(40,1,11)]:
        M,rows,cols,_=gram(K,N,p,True);_,_,Y,_,_=local_data(K,N,p)
        assert all(M[i,j]==residue(Y[i,j],p,-1) for i in range(K-N) for j in range(K-N))
        checked.append(dict(K=K,N=N,p=p,entries=(K-N)**2))
    for K,N,p in [(128,16,43),(256,32,89),(400,50,137)]:
        t=time.time();M,rows,cols,_=gram(K,N,p);rank=M.rank();cap=rank_cap(K,N,p)
        assert rank<=cap
        r=dict(K=K,N=N,p=p,rows=len(rows),columns=len(cols),projected_rank=rank,uniform_cap=cap,seconds=time.time()-t)
        scaled.append(r);print(json.dumps(r),flush=True)
    out=dict(full_matrix_checks=checked,entries_checked=sum(r['entries'] for r in checked),scaled=scaled,seconds=time.time()-start)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print('entries_checked',out['entries_checked'],'total_seconds',out['seconds'],flush=True)
