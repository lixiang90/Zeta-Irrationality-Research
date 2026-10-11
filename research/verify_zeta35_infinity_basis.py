"""Verify saved infinity-basis certificates using full polynomial products.

Does not call the producer's series recurrence or transformed-matrix routine.
"""
import json,math
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly

ROOT=Path(__file__).parent


def product_D(n):
    D=Poly([1])
    for j in range(1,n+1):D*=Poly([j*j,1])
    return D


def verify(path):
    data=json.loads(path.read_text());K,N,m,h=(data[k] for k in ('K','N','m','ambient'))
    D=product_D(K);W=product_D(N)**m
    root=[Q(v) for v in data['basis_root']]
    S=Poly(root);Dr=Poly(list(D)[::-1]);Wr=Poly(list(W)[::-1])
    residual=S*S*Wr-Dr
    assert all(residual[k]==0 for k in range(h))
    assert all(int(v.denominator)&(int(v.denominator)-1)==0 for v in root)
    basis=[Poly(root[:i+1][::-1]) for i in range(h)]
    lower=max(0,h-1+W.degree()-K);pairs=coefficients=0
    for i in range(h):
        for j in range(i,h):
            quotient,remainder=divmod(W*basis[i]*basis[j],D)
            assert remainder.degree()<K
            upper=max(lower,quotient.degree())
            for e in range(lower,upper+1):
                assert quotient[e]==(1 if i+j==K-W.degree()+e else 0)
                coefficients+=1
            pairs+=1
    sums={r['s'] for r in data['prime_checks']}
    for r in data['rows']:
        keep=r['keep'];assert len(set(keep))==data['target']
        assert all(i+j not in sums for i in keep for j in keep)
        assert r['degree']>0 and r['target_rank']>0
    return dict(file=path.name,status='passed',pair_count=pairs,coefficient_count=coefficients,
                support_count=len(data['rows']),exact_identity_lower=lower)


def main():
    rows=[]
    for path in sorted(ROOT.glob('zeta35_infinity_basis_n*_m*.json')):
        r=verify(path);rows.append(r);print(r,flush=True)
    out=dict(status='passed',rows=rows)
    (ROOT/'verify_zeta35_infinity_basis.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
