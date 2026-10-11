"""Explicit unimodular kernel lifts certifying the projected-rank bound."""
import json
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq_mat
from layer_projection import local_data,modrank
from joint_padic import residue,val

def kernel_basis(a,p):
    a=[row[:] for row in a];m=len(a);n=len(a[0]) if m else 0
    r=0;piv=[]
    for j in range(n):
        k=next((k for k in range(r,m) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];inv=pow(a[r][j],-1,p)
        a[r]=[v*inv%p for v in a[r]]
        for k in range(m):
            if k!=r and a[k][j]:
                c=a[k][j];a[k]=[(u-c*v)%p for u,v in zip(a[k],a[r])]
        piv.append(j);r+=1
        if r==m:break
    basis=[[int(i==j) for i in range(n)] for j in piv]
    for j in range(n):
        if j in piv:continue
        v=[int(i==j) for i in range(n)]
        for k,col in enumerate(piv):v[col]=-a[k][j]%p
        basis.append(v)
    return basis,r

def audit(K,N,p):
    A,B,Y,w,tags=local_data(K,N,p);h=K-N
    Z=[i for i in range(h) if w[i]==0];H=[i for i in range(h) if w[i]==-F(1,2)]
    R=[[residue(Y[i,j],p,-1) for j in Z] for i in Z+H]
    basis,r=kernel_basis(R,p)
    assert r==modrank(Y,p,Z+H,Z)
    T=fmpq_mat(h,h,[int(i==j) for i in range(h) for j in range(h)])
    neww=w[:]
    for k,row in enumerate(Z):
        for l,col in enumerate(Z):T[row,col]=basis[k][l]
        neww[row]=-F(1,2) if k<r else F(0)
    assert val(T.det(),p)==0
    AA=T*A*T.transpose();BB=T*B*T.transpose()
    margins=[min(val(AA[i,j],p),val(BB[i,j],p))-neww[i]-neww[j] for i in range(h) for j in range(h)]
    assert min(margins)>=0
    return dict(K=K,N=N,p=p,rectangular_rank=r,new_bound=int(2*sum(neww)),
                minimum_entry_margin=str(min(margins)),zero_indices=Z,half_indices=H,
                residue_matrix=R,change_of_basis_rows=basis)

if __name__=='__main__':
    rows=[]
    for K,N,p in [(32,4,11),(40,5,17),(48,6,17),(56,7,19),(64,8,23)]:
        r=audit(K,N,p);rows.append(r);print({k:v for k,v in r.items() if k not in ['residue_matrix','change_of_basis_rows']})
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
