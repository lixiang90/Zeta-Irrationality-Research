"""Two-prefix all-coefficient bounds, with exact local basis certificates.

The allocation bound uses the existing general tpol entry lemma, not a
substitution into a fixed-parameter Lean determinant theorem. See the report.
"""
import heapq
import json
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat
from sympy import primerange
from joint_exact import entries, Dcache
from two_prefix_outer import vp


def counts(J,p,c):
    if c==0:return J//p
    return (J-c)//p+(J+c)//p+1


def allocation_bound(K,N,M,h,p):
    assert 1<=N<=M<K and h>0 and p>=7
    assert p*p>max(2*K,12*N+4*M+4*h-2*K+4)
    offsets=[1+12*(N//p)+4*(M//p)-2*(K//p)]
    offsets += [6*counts(N,p,c)+2*counts(M,p,c)-counts(K,p,c)-6
                for c in range(1,(p+1)//2)]
    heap=[(b,c) for c,b in enumerate(offsets)];heapq.heapify(heap)
    L=[0]*len(offsets);weights=[]
    for _ in range(h):
        a,c=heapq.heappop(heap);weights.append((c,L[c],a));L[c]+=1
        heapq.heappush(heap,(a+(4 if c==0 else 2),c))
    assert max(a for c,i,a in weights)<=heap[0][0]
    return dict(p=p,lower=sum(a for c,i,a in weights),allocation=L,
                offsets=offsets,weights=weights,threshold=heap[0][0])


def residue_bound(K,N,M,h,p):
    """CRT pole bound for arbitrary q and prefix counts; p^2>2K."""
    assert h>=K-M and p>=7 and p*p>2*K
    weights=[];classes=[]
    for c in range(1,(p+1)//2):
        ell=counts(K,p,c);m=counts(M,p,c);eta=6*counts(N,p,c)+2*m
        ps=[j for j in range(M+1,K+1) if j%p in (c,p-c)]
        n=sum(j>p for j in ps);d=len(ps)
        ws=[min(0,2*i+eta-ell-6) for i in range(n)]+[0]*(d-n)
        weights+=ws
        if d:classes.append(dict(c=c,ell=ell,removed=m,eta=eta,big=n,
                                 surviving=d,twice_weights=ws))
    q=K//p;qM=M//p;qN=N//p
    zw=[min(0,4*i+12*qN+4*qM-2*q+1) for i in range(q-qM)]
    weights+=zw+[0]*(h-(K-M))
    assert len(weights)==h
    r=min(h,max(0,2*h+6*N+2*M-K-3*p+3));z=weights.count(0)
    return dict(p=p,lower=sum(weights)-min(r,z),base=sum(weights),
                moment_rank=r,zero_weights=z,twice_weights=weights,
                zero_class_weights=zw,classes=classes)


def check_allocation_basis(K,N,M,h,p):
    row=allocation_bound(K,N,M,h,p);L=row['allocation'];t=fmpq_poly([0,1])
    factors=[(t+c*c)**n for c,n in enumerate(L)]
    full=fmpq_poly([1])
    for f in factors:full*=f
    basis=[];w=[];idx=[]
    for c,n in enumerate(L):
        for i in range(n):
            basis.append((full//factors[c])*(t+c*c)**i)
            w.append(row['offsets'][c]+(4 if c==0 else 2)*i);idx.append((c,i))
    C=fmpq_mat(h,h,[b[j] for b in basis for j in range(h)])
    assert vp(C.det(),p)==0
    # Verify the abstract entry inequalities independently of the determinant.
    for s,(c,i) in enumerate(idx):
        for u,(d,j) in enumerate(idx):
            for a in range(len(L)):
                nu=(i if c==a else L[a])+(j if d==a else L[a])
                assert w[s]+w[u]<=2*row['offsets'][a]+(4 if a==0 else 2)*nu
    aa,bb=entries(K,[(N,6),(M,2)],h)
    for values in (aa,bb):
        A=fmpq_mat(h,h,[values[i+j] for i in range(h) for j in range(h)])
        A=C*A*C.transpose()
        for i in range(h):
            for j in range(h):
                assert not A[i,j] or 2*vp(A[i,j],p)>=w[i]+w[j],(K,N,M,h,p,i,j)
    return dict(K=K,N=N,M=M,h=h,p=p,lower=row['lower'],allocation=L,
                threshold=row['threshold'],entry_checks=2*h*h,unit_basis=True)


def run():
    folder=Path(__file__).parent;rows=[];seen=set()
    for fn in sorted(folder.glob('two_prefix_*_K*.json')):
        for row in json.loads(fn.read_text())['rows']:
            K,N,M,h=(row[k] for k in ('K','N','M','h'));key=(K,N,M,h)
            if key in seen:continue
            seen.add(key);ct=fmpq(row['content'])
            for p in primerange(7,2*(K+6*N)+2):
                if p*p<=max(2*K,12*N+4*M+4*h-2*K+4):continue
                a=allocation_bound(*key,p);b=residue_bound(*key,p) if h>=K-M else None
                actual=vp(ct,p);best=max(a['lower'],b['lower']) if b else a['lower']
                assert actual>=best,(key,p,actual,best)
                rows.append(dict(K=K,N=N,M=M,h=h,p=p,actual=actual,
                                 allocation=a['lower'],residue=b['lower'] if b else None,
                                 best=best,slack=actual-best,
                                 new_region=(3*p<=K or p<=2*M)))
    jobs=[(24,1,4,20,11),(24,1,4,23,11),(48,2,8,40,13),
          (48,2,8,46,13),(72,3,12,60,17),(96,4,16,80,17),
          (40,4,15,25,13),(56,8,20,36,17),(60,2,31,29,13),
          (60,2,31,29,17),(30,2,13,17,11),(15,1,4,11,7)]
    certs=[]
    for job in jobs:
        certs.append(check_allocation_basis(*job));print(json.dumps(certs[-1]),flush=True)
    result=dict(configurations=len(seen),local_checks=len(rows),
                new_region_checks=sum(r['new_region'] for r in rows),
                nonzero_checks=sum(r['best']!=0 for r in rows),
                equality=sum(r['slack']==0 for r in rows),
                basis_certificates=certs,rows=rows)
    (folder/'two_prefix_inner_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('rows','basis_certificates')}),flush=True)


if __name__=='__main__':run()
