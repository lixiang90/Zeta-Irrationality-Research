"""Global dyadic basis for the first bad moment and true-subspace experiments.

All matrix, content and congruence computations are exact. No finite experiment
in this file is an irrationality proof.
"""
import argparse,itertools,json,math,time
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat as Mat,arb,arb_poly,ctx
from zeta35_target31_scan import entries
from zeta35_target31 import primes_to,content_and_primitive,rational_log
from zeta35_true_subspaces import pencil_polynomial
import zeta35_mixed_moments as mixed

ROOT=Path(__file__).parent


def dyadic_basis(K,N,m,h):
    D=Poly(mixed.original.Dpoly(K));W=Poly(mixed.original.Dpoly(N))**m
    d=D.degree();w=W.degree()
    dr=[D[d-i] if i<=d else Q(0) for i in range(h)]
    wr=[W[w-i] if i<=w else Q(0) for i in range(h)]
    ratio=[];root=[]
    for n in range(h):
        ratio.append(dr[n]-sum((wr[k]*ratio[n-k] for k in range(1,n+1)),Q(0)))
        root.append(Q(1) if n==0 else (ratio[n]-sum((root[k]*root[n-k] for k in range(1,n)),Q(0)))/2)
    assert root[0]==1
    for c in root:
        den=int(c.denominator);assert den&(den-1)==0
    T=Mat([[root[i-j] if j<=i else 0 for j in range(h)] for i in range(h)])
    assert T.det()==1
    return D,W,root,T


def modq(q,p):
    assert int(q.denominator)%p
    return int(q.numerator)*pow(int(q.denominator),-1,p)%p


def finite_check(K,N,m,aa,bb,T):
    h=T.nrows();degree=m*N+2*h-2-K
    primes=[p for p in primes_to(degree+3) if p>K]
    A=Mat([[aa[i+j] for j in range(h)] for i in range(h)])
    B=Mat([[bb[i+j] for j in range(h)] for i in range(h)])
    A=T*A*T.transpose();B=T*B*T.transpose()
    checked=[]
    for p in primes:
        assert degree<(3*p-7)//2
        s=K-m*N+p-3
        assert s>=h-1
        for i in range(h):
            for j in range(h):
                assert modq(p*A[i,j],p)==(3*pow(2,-1,p)%p if i+j==s else 0)
                assert modq(p*B[i,j],p)==0
        checked.append(dict(p=p,s=s,rank=2*h-1-s))
    return A,B,checked


def supports(h,target,sums,limit=20000):
    # All coordinates in the common radical are retained. Enumerate coordinate
    # subspaces in the remaining tail, avoiding forbidden sums and loops.
    radical=max(0,min(sums)-h+1) if sums else h
    prefix=tuple(range(radical));need=target-radical
    assert need>=0
    vertices=[i for i in range(radical,h) if 2*i not in sums]
    result=[];truncated=False
    def visit(chosen,remaining):
        nonlocal truncated
        if len(result)>=limit:truncated=True;return
        if len(chosen)==need:result.append(prefix+tuple(chosen));return
        if len(chosen)+len(remaining)<need:return
        for k,v in enumerate(remaining):
            tail=[w for w in remaining[k+1:] if v+w not in sums]
            visit(chosen+[v],tail)
            if truncated:return
    visit([],vertices)
    return result,radical,truncated


def evaluate(A,B,keep,K):
    start=time.perf_counter();A=Mat([[A[i,j] for j in keep] for i in keep]);B=Mat([[B[i,j] for j in keep] for i in keep])
    poly=pencil_polynomial(A,B)
    for x in (-1,0,1):assert poly(x)==(A+x*B).det()
    content,coeffs=content_and_primitive(poly)
    ctx.prec=max(abs(c).bit_length() for c in coeffs)+K*K+4000
    value=arb_poly(coeffs)(3*arb(3).zeta()+arb(5).zeta());assert value>0
    logp=value.log();logc=rational_log(content)
    return dict(keep=list(keep),dimension=len(keep),degree=poly.degree(),target_rank=B.rank(),
                content=str(content),log_p=float(logp),log_p_interval=str(logp),
                log_content=float(logc),log_delta=float(logp+logc),seconds=time.perf_counter()-start)


def run(n,m,max_evals=30):
    start=time.perf_counter();K=40*n;N=3*n;ambient=37*n;target=K-m*N//2-1
    _,aa,bb=entries(K,N,m,ambient)
    D,W,root,T=dyadic_basis(K,N,m,ambient)
    A,B,checks=finite_check(K,N,m,aa,bb,T)
    sums={r['s'] for r in checks};choices,radical,truncated=supports(ambient,target,sums)
    canonical=tuple(range(target));assert canonical in choices
    choices.sort(key=lambda c:sum(c))
    # Evaluate low-degree supports first and retain a representative high-degree
    # one; all counts and truncation are recorded rather than called exhaustive.
    selected=choices[:max_evals]
    if choices[-1] not in selected:selected.append(choices[-1])
    path=ROOT/f'zeta35_infinity_basis_n{n}_m{m}.json';rows=[];cached={}
    if path.exists():
        old=json.loads(path.read_text())
        assert old['basis_root']==list(map(str,root))
        cached={tuple(r['keep']):r for r in old['rows']}
    print('setup',n,m,'ambient',ambient,'target',target,'radical',radical,'supports',len(choices),'truncated',truncated,flush=True)
    for k,keep in enumerate(selected):
        assert all(i+j not in sums for i in keep for j in keep)
        row=cached[keep] if keep in cached else evaluate(A,B,keep,K)
        rows.append(row)
        print('candidate',k+1,'tail',[v for v in keep if v>=radical],'logP',round(row['log_p'],6),flush=True)
        out=dict(n=n,K=K,N=N,m=m,ambient=ambient,target=target,common_radical=radical,
                 basis_root=list(map(str,root)),prime_checks=checks,support_count=len(choices),
                 enumeration_truncated=truncated,evaluation_limit=max_evals,rows=rows,seconds=time.perf_counter()-start)
        path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    base=next(r for r in rows if r['keep']==list(canonical));best=min(rows,key=lambda r:r['log_p'])
    print('BEST',n,m,'baseline',base['log_p'],'best',best['log_p'],flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=1);p.add_argument('--m',type=int,default=4);p.add_argument('--limit',type=int,default=30)
    a=p.parse_args();run(a.n,a.m,a.limit)
