"""Cross-scale parity spaces in the uniform infinity basis for zeta(7).

Exact coefficients and full contents, with Arb target intervals.  Nonintegral
polynomial moment layers are checked separately from pole contributions.
"""
import argparse, functools, json, math, sys, time
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, nmod_mat, arb, arb_poly, ctx
from joint_exact import entries, content
from b8_hankel import Dpoly, mu_monomial
from zeta35_target31 import primes_to

sys.set_int_max_str_digits(0)


def basis(K,N,H):
    D=Poly(Dpoly(K));W=Poly(Dpoly(N)**8);w=W.degree()
    dr=[D[K-i] if i<=K else Q(0) for i in range(H)]
    wr=[W[w-i] if i<=w else Q(0) for i in range(H)]
    ratio=[];root=[]
    for n in range(H):
        ratio.append(dr[n]-sum((wr[k]*ratio[n-k] for k in range(1,n+1)),Q(0)))
        root.append(Q(1) if n==0 else (ratio[n]-sum((root[k]*root[n-k] for k in range(1,n)),Q(0)))/2)
    S=Poly(root);residual=S*S*Poly(list(W)[::-1])-Poly(list(D)[::-1])
    assert all(not residual[i] for i in range(H))
    assert all(int(v.denominator)&(int(v.denominator)-1)==0 for v in root)
    T=Mat([[root[i-j] if j<=i else 0 for j in range(H)] for i in range(H)])
    assert T.det()==1
    return D,W,root,T


def modq(q,p):
    assert int(q.denominator)%p
    return int(q.numerator)*pow(int(q.denominator),-1,p)%p


def moment_layers(K,N,H,D,W,root):
    degree=W.degree()+2*H-2-K
    threshold=max(0,H-1+W.degree()-K)
    moments=[mu_monomial(e) for e in range(degree+1)]
    quotients=[(W*Poly([0]*s+[1]))//D for s in range(2*H-1)]
    rows=[];sums=set();matrices={}
    for p in primes_to(2*degree+3):
        if p<11 or 3*p<=K:
            continue
        gamma=[modq(p*m,p) for m in moments]
        bad=[e for e,g in enumerate(gamma) if g]
        if not bad:
            continue
        assert min(bad)==3*p-4 and min(bad)>=threshold
        seq=[sum(modq(q[e],p)*gamma[e] for e in range(q.degree()+1))%p for q in quotients]
        C=nmod_mat([[modq(root[i-j],p) if j<=i else 0 for j in range(H)] for i in range(H)],p)
        Qp=nmod_mat([[seq[i+j] for j in range(H)] for i in range(H)],p)
        L=C*Qp*C.transpose()
        for i in range(H):
            for j in range(H):
                e=i+j+W.degree()-K
                assert int(L[i,j])==(gamma[e] if 0<=e<len(gamma) else 0)
        ss=[K-W.degree()+e for e in bad]
        sums.update(ss);matrices[p]=L
        if p%4==1:
            assert all(e%2==1 for e in bad)
        rows.append(dict(p=p,p_mod4=p%4,bad_moments=bad,antidiagonals=ss,
                         gamma_values=[gamma[e] for e in bad],ambient_rank=L.rank(),
                         standard_form_threshold=threshold,quotient_checks=H*H))
    return rows,sums,matrices


def best_parity_tail(H,radical,parity,sums):
    vertices=[i for i in range(radical,H) if i%2==parity and 2*i not in sums]
    neigh=[]
    for i in vertices:
        mask=0
        for jidx,j in enumerate(vertices):
            if i!=j and i+j in sums:
                mask|=1<<jidx
        neigh.append(mask)
    @functools.lru_cache(None)
    def choose(mask):
        if not mask:
            return ()
        k=(mask&-mask).bit_length()-1
        without=mask&~(1<<k)
        a=choose(without)
        b=(k,)+choose(without&~neigh[k])
        return min((a,b),key=lambda q:(-len(q),sum(vertices[j] for j in q),q))
    keep=list(range(radical))+[vertices[k] for k in choose((1<<len(vertices))-1)]
    assert all(i+j not in sums for i in keep for j in keep)
    return keep


def polynomial(A,B):
    h=A.nrows();b=B.det()
    if b:
        return (-(B.inv()*A)).charpoly()*b
    a=A.det()
    if a:
        cp=(-(A.inv()*B)).charpoly()
        return Poly([cp[h-i] for i in range(h+1)])*a
    vals=[(A+x*B).det() for x in range(h+1)]
    ans=Poly();q=Poly([1])
    for k in range(h+1):
        ans+=q*vals[0]
        vals=[vals[i+1]-vals[i] for i in range(len(vals)-1)]
        q=q*Poly([-k,1])/Q(k+1)
    return ans


def evaluate(A,B,keep,K,label,layers):
    start=time.perf_counter();h=len(keep)
    a=Mat([[A[i,j] for j in keep] for i in keep]);b=Mat([[B[i,j] for j in keep] for i in keep])
    poly=polynomial(a,b);rank=b.rank();assert poly.degree()<=rank
    for x in (-1,0,1):
        assert poly(x)==(a+x*b).det()
    ct=content(poly);pr=poly/ct
    assert all(c.denominator==1 for c in pr)
    coeff=[int(c.numerator) for c in pr];assert math.gcd(*coeff)==1
    ctx.prec=max(abs(c).bit_length() for c in coeff)+K*K+3000
    value=arb_poly(coeff)(arb(7).zeta());assert value>0
    lp=value.log();lc=(arb(int(ct.numerator))/int(ct.denominator)).log()
    local=[dict(p=p,restricted_bad_rank=nmod_mat([[int(L[i,j]) for j in keep] for i in keep],p).rank())
           for p,L in layers.items()]
    row=dict(label=label,keep=keep,dimension=h,max_degree=max(keep),target_rank=rank,
             degree=poly.degree(),content=str(ct),primitive_coefficients=list(map(str,coeff)),
             log_primitive=float(lp),score=float(lp)/(K*K),log_primitive_interval=lp.str(30),
             log_content=float(lc),log_delta=float(lp+lc),local_polynomial_layers=local,
             determinant_checks=['-1','0','1'],seconds=time.perf_counter()-start)
    print(K,label,'h',h,'score',row['score'],'bad ranks',[r['restricted_bad_rank'] for r in local],flush=True)
    return row


def run(K):
    assert K%24==0;N=K//24;H=K-N
    D,W,root,T=basis(K,N,H)
    aa,bb=entries(K,[(N,8)],H)
    A=T*Mat([[aa[i+j] for j in range(H)] for i in range(H)])*T.transpose()
    B=T*Mat([[bb[i+j] for j in range(H)] for i in range(H)])*T.transpose()
    local,sums,layers=moment_layers(K,N,H,D,W,root)
    radical=max(0,min(sums)-H+1) if sums else H
    specs=[('even',list(range(0,H,2))),('odd',list(range(1,H,2)))]
    if sums:
        specs += [(f'head_parity_{r}',best_parity_tail(H,radical,r,sums)) for r in (0,1)]
    rows=[];cache={}
    for label,keep in specs:
        h=len(keep)
        if h not in cache:
            base=evaluate(A,B,list(range(h)),K,f'low_degree_h{h}',layers)
            rows.append(base);cache[h]=base
        row=evaluate(A,B,keep,K,label,layers)
        base=cache[h]
        row.update(baseline_label=base['label'],log_delta_ratio=row['log_delta']-base['log_delta'],
                   log_content_ratio=row['log_content']-base['log_content'],
                   log_primitive_ratio=row['log_primitive']-base['log_primitive'])
        rows.append(row)
    return dict(K=K,N=N,beta=8,ambient=H,basis_root=list(map(str,root)),
                standard_form_threshold=max(0,H-1+W.degree()-K),
                polynomial_layers=local,forbidden_sums=sorted(sums),common_radical=radical,rows=rows)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',nargs='+',type=int,default=[48,96,120])
    args=p.parse_args();out=dict(status='finite_exact_and_Arb_checks_passed',cases=[],
                               scope='Fixed alpha=1/24; finite tests only. Polynomial-layer removal '
                                     'does not imply whole-pencil integrality at p<=K.')
    path=Path(__file__).with_suffix('.json')
    for K in args.K:
        out['cases'].append(run(K))
        path.write_text(json.dumps(out,indent=2),encoding='utf-8')
