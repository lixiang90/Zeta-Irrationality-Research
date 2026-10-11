"""Check the same global basis on ALL nonintegral polynomial moments.

This includes intermediate primes where the pole contribution must still be
handled separately. No integrality conclusion for the full matrix is made there.
"""
import json
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,nmod_mat
from zeta35_target31 import primes_to
from verify_zeta35_infinity_basis import product_D

ROOT=Path(__file__).parent


def modq(q,p):
    assert int(q.denominator)%p
    return int(q.numerator)*pow(int(q.denominator),-1,p)%p


def run(path):
    data=json.loads(path.read_text());K,N,m,h=(data[k] for k in ('K','N','m','ambient'))
    D=product_D(K);W=product_D(N)**m;w=W.degree();degree=w+2*h-2-K
    lower=max(0,h-1+w-K);root=list(map(Q,data['basis_root']))
    quotients=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    moments=[(-1)**e*(Q.bernoulli(2*e+2)*(2*e+3)*(2*e+4)*(2*e+5)/24
                     +3*Q.bernoulli(2*e+4)*(2*e+5)/2) for e in range(degree+1)]
    rows=[];skipped=[]
    for p in primes_to(degree+3):
        if p<5 or 3*p<=K:continue
        gamma=[modq(p*v,p) for v in moments]
        nonzero=[e for e,v in enumerate(gamma) if v]
        if nonzero and min(nonzero)<lower:
            skipped.append(dict(p=p,first_bad=min(nonzero),threshold=lower));continue
        sequence=[sum(int(q[e])*gamma[e] for e in range(q.degree()+1))%p for q in quotients]
        T=nmod_mat([[modq(root[i-j],p) if j<=i else 0 for j in range(h)] for i in range(h)],p)
        H=nmod_mat([[sequence[i+j] for j in range(h)] for i in range(h)],p)
        transformed=T*H*T.transpose()
        for i in range(h):
            for j in range(h):
                e=i+j+w-K
                expected=gamma[e] if 0<=e<len(gamma) else 0
                assert int(transformed[i,j])==expected
        rows.append(dict(p=p,rank=transformed.rank(),antidiagonals=[dict(s=K-w+e,value=gamma[e]) for e in nonzero]))
    out=dict(source=path.name,status='passed',rows=rows,skipped=skipped)
    print(path.name,'verified primes',len(rows),'skipped',skipped,flush=True)
    return out


if __name__=='__main__':
    data=[run(path) for path in sorted(ROOT.glob('zeta35_infinity_basis_n*_m*.json'))]
    (ROOT/'zeta35_infinity_moment_blocks.json').write_text(json.dumps(dict(status='passed',cases=data),indent=2),encoding='utf-8')
