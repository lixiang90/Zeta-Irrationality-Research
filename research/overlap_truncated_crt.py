"""Weighted-minor compression of the pole CRT bound to h <= K-M.

The proof uses all mixed minors, not just the ambient determinant. The
exceptional-moment rank is computed at the actual truncated dimension.
"""
import json
from pathlib import Path
from flint import fmpq, fmpq_poly, fmpq_mat
from sympy import primerange
from joint_exact import Dcache, entries, moment, determinant, content
from two_prefix_outer import vp
from verify_overlapping_prefix import allocation


def count(J,p,c):
    return J//p if c==0 else (J-c)//p+(J+c)//p+1


def crt_bound(K,profile,h,p):
    M=max(J for J,e in profile if e);n=K-M;w=sum(J*e for J,e in profile)
    assert 0<h<=n and p>=7 and p*p>2*K
    assert all(e>=0 for J,e in profile) and sum(e for J,e in profile if J==M)>=2
    classes=[];weights=[]
    for c in range(1,(p+1)//2):
        ell=count(K,p,c);removed=count(M,p,c);eta=sum(e*count(J,p,c) for J,e in profile)
        ps=[j for j in range(M+1,K+1) if j%p in (c,p-c)]
        big=sum(j>p for j in ps);d=len(ps)
        local=[min(0,2*i+eta-ell-6) for i in range(big)]+[0]*(d-big)
        weights+=local
        if d:classes.append(dict(c=c,ell=ell,removed=removed,eta=eta,big=big,poles=ps,weights=local))
    eta0=sum(e*(J//p) for J,e in profile);d0=(K//p)-(M//p)
    zero=[min(0,4*i+2*eta0-2*(K//p)+1) for i in range(d0)];weights+=zero
    assert len(weights)==n
    ordered=sorted(weights);selected=ordered[:h];base=sum(selected);z=selected.count(0)
    rank=min(h,max(0,w+2*h-K-3*p+3))
    mixed=min(sum(ordered[:h-j])-j for j in range(rank+1))
    assert mixed==base-min(rank,z)
    return dict(K=K,profile=profile,h=h,p=p,ambient=n,classes=classes,
                weights=weights,zero_weights=zero,selected_weights=selected,
                base=base,zero_selected=z,moment_rank=rank,lower=mixed)


def basis_check(K,profile,h,p):
    info=crt_bound(K,profile,h,p);n=info['ambient'];M=K-n;t=fmpq_poly([0,1])
    T=fmpq_poly(Dcache(K)//Dcache(M));W=fmpq_poly([1])
    for J,e in profile:W*=Dcache(J)**e
    aa,bb=entries(K,profile,n);yy=[];Q=W
    for i in range(2*n-1):
        quotient=Q//fmpq_poly(Dcache(K))
        yy.append(sum((quotient[k]*moment(k) for k in range(3*p-4,quotient.degree()+1)),fmpq(0)))
        Q*=t
    basis=[]
    for row in info['classes']:
        c=row['c'];local=fmpq_poly([1]);big=fmpq_poly([1])
        for j in row['poles']:
            local*=t+j*j
            if j>p:big*=t+j*j
        for i in range(len(row['poles'])):
            basis.append((T//local)*((t+c*c)**i if i<row['big'] else big*(t+c*c)**(i-row['big'])))
    zero=fmpq_poly([1]);d0=0
    for j in range(M+1,K+1):
        if j%p==0:zero*=t+j*j;d0+=1
    basis +=[(T//zero)*t**i for i in range(d0)]
    C=fmpq_mat(n,n,[q[j] for q in basis for j in range(n)]);assert vp(C.det(),p)==0
    Y=fmpq_mat(h,h,[yy[i+j] for i in range(h) for j in range(h)])
    assert Y.rank()<=info['moment_rank'];assert all(not x or vp(x,p)>=-1 for x in Y.entries())
    # C transforms old monomials to CRT rows. E expresses the first h old
    # monomials in those rows, so E*C is the coordinate inclusion matrix.
    inv=C.inv();E=fmpq_mat(h,n,[inv[i,j] for i in range(h) for j in range(n)])
    inclusion=fmpq_mat(h,n,[int(i==j) for i in range(h) for j in range(n)])
    assert E*C==inclusion and all(not x or vp(x,p)>=0 for x in E.entries())
    # Within each local block the weights increase with the jet order. Thus a
    # minimum-weight subset can be chosen as a prefix in each block. Its minor
    # on the first k monomials is a confluent CRT evaluation determinant: a unit.
    minor_checks=[]
    for k in sorted({1,max(1,h//2),h}):
        chosen=sorted(sorted(range(n),key=lambda i:(info['weights'][i],i))[:k])
        minor=fmpq_mat(k,k,[E[i,j] for i in range(k) for j in chosen]).det()
        assert vp(minor,p)==0
        assert sum(info['weights'][i] for i in chosen)==sum(sorted(info['weights'])[:k])
        minor_checks.append(dict(size=k,columns=chosen,valuation=0))
    for vals in ([a-y for a,y in zip(aa,yy)],bb):
        R=fmpq_mat(n,n,[vals[i+j] for i in range(n) for j in range(n)]);R=C*R*C.transpose()
        for i in range(n):
            for j in range(n):
                if R[i,j]:assert 2*vp(R[i,j],p)>=info['weights'][i]+info['weights'][j]
        compressed=E*R*E.transpose()
        assert compressed==fmpq_mat(h,h,[vals[i+j] for i in range(h) for j in range(h)])
    return dict(K=K,profile=profile,h=h,p=p,ambient=n,entry_checks=2*n*n,
                compression_entries=h*n,moment_rank_bound=info['moment_rank'],actual_moment_rank=Y.rank(),lower=info['lower'],
                minimum_weight_unit_minors=minor_checks)


def main():
    folder=Path(__file__).parent;saved=json.loads((folder/'overlapping_prefix_scan.json').read_text())['rows']
    saved+=json.loads((folder/'balanced_prefix_scan.json').read_text())['rows']
    rows=[]
    for r in saved:
        K,h=r['K'],r['h'];profile=r['profile'];ct=fmpq(r['content'])
        assert ct==content(fmpq_poly([fmpq(c) for c in r['raw_polynomial']]))
        for p in primerange(7,2*K+1):
            if p*p<=2*K:continue
            b=crt_bound(K,profile,h,p);actual=vp(ct,p);assert actual>=b['lower']
            a=allocation(K,profile,h,p)['bound'] if p*p>max(2*K,2*sum(J*e for J,e in profile)+4*h-2*K+4) else None
            best=max(b['lower'],a) if a is not None else b['lower']
            rows.append(dict(K=K,N=r['N'],profile=profile,h=h,p=p,actual=actual,crt=b['lower'],
                             allocation=a,slack=actual-best,selected_zero=b['zero_selected'],rank=b['moment_rank']))
    jobs=[(24,[(1,4),(2,2),(3,2)],h,p) for h in (1,7,20) for p in (7,11,17)]
    jobs +=[(48,[(2,4),(4,2),(6,2)],h,p) for h in (5,40) for p in (11,13,23)]
    jobs +=[(30,[(2,4),(8,2),(15,2)],h,p) for h in (3,10) for p in (11,17)]
    checks=[];extra=[]
    for job in jobs:
        checks.append(basis_check(*job))
        K,profile,h,p=job;aa,bb=entries(K,profile,h);ct=content(determinant(aa,bb,h));bound=crt_bound(*job)['lower']
        assert vp(ct,p)>=bound
        extra.append(dict(K=K,profile=profile,h=h,p=p,bound=bound,actual=vp(ct,p)))
    result=dict(records=len(saved),rows=rows,basis_checks=checks,additional_determinants=extra,
                scope='Written weighted-minor proof plus exact finite validation; not a Lean proof.')
    (folder/'overlap_truncated_crt.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(records=len(saved),prime_checks=len(rows),basis_checks=len(checks),
                         basis_entries=sum(r['entry_checks'] for r in checks),
                         minimum_weight_unit_minors=sum(len(r['minimum_weight_unit_minors']) for r in checks),
                         stronger_than_allocation=sum(r['allocation'] is not None and r['crt']>r['allocation'] for r in rows),
                         equalities=sum(r['slack']==0 for r in rows))),flush=True)


if __name__=='__main__':main()
