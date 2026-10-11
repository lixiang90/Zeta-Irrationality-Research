"""Certify the six-pole bound uniformly in a p-integral deformation parameter.

Only delta=0 is the original zeta(7) functional. For a>=1, the determinant
degree in delta is at most p-a<p. Values at 0,...,p-a determine its
coefficients through a p-unit Vandermonde matrix, coefficientwise in X.
Thus finite full-pencil bounds prove a statement for ALL delta in Z_p.
This is still a finite (K,N,p) certificate, not a uniform theorem in p.
"""
import argparse, json, time
from pathlib import Path
from coupled_pencil import normalized_pencil
from coupled_candidate_law import prediction
from distribution_modular import smith_mod
from coupled_schur import counts, integral_solve_certificate


def point(K,N,p,delta):
    z=normalized_pencil(K,N,p,10,harmonic_deformation=delta)
    ss,censored,_=smith_mod(z['A'],p,10)
    assert not censored
    # Smith transforms preserve the ideal of entries divisible by p^B_min.
    # Factoring p^min(s_i,B_min) from each transformed row bounds all X.
    low=z['tropical']+sum(min(s,z['B_min']) for s in ss)
    exact=z['B_min']>=max(ss)
    if not exact:
        solve=integral_solve_certificate(z['A'],z['B'],p,10)
        if solve['certified']:
            exact=True;low=z['tropical']+sum(ss)
    return dict(delta=delta,tropical=z['tropical'],smith_counts=counts(ss),
                B_min=z['B_min'],gauss_lower=low,exact_gauss=exact)


def run(jobs,out):
    start=time.time()
    saved=json.loads(out.read_text()) if out.exists() else dict(rows=[])
    cache={(r['K'],r['N'],r['p']):r for r in saved['rows']}
    for K,N,p in jobs:
        if (K,N,p) in cache:continue
        pre=prediction(K,N,p);a=pre['a'];degree=p-a
        assert 1<=a<=N and degree<p
        values=[]
        for delta in range(degree+1):
            v=point(K,N,p,delta);values.append(v)
            if v['gauss_lower']<pre['gauss']:
                print('LOWER CERTIFICATE FAIL '+json.dumps(dict(K=K,N=N,p=p,target=pre['gauss'],**v)),flush=True)
            if delta%10==0:print(f'K={K},N={N},p={p}: {delta+1}/{degree+1} values, elapsed={time.time()-start:.1f}s',flush=True)
        lower=min(v['gauss_lower'] for v in values)
        row=dict(K=K,N=N,p=p,a=a,degree_bound=degree,target=pre['gauss'],
                 coefficient_gauss_lower=lower,all_p_integral_parameters_certified=lower>=pre['gauss'],
                 values=values)
        cache[K,N,p]=row
        result=dict(rows=list(cache.values()),scope='uniform in deformation delta and indeterminate X for each listed finite K,N,p; only delta=0 is original')
        out.write_text(json.dumps(result,indent=2))
        print('BUNDLE '+json.dumps({k:v for k,v in row.items() if k!='values'}),flush=True)
    rows=list(cache.values())
    summary=dict(bundles=len(rows),passed=sum(r['all_p_integral_parameters_certified'] for r in rows),
                 evaluations=sum(len(r['values']) for r in rows),
                 exact_evaluations=sum(v['exact_gauss'] for r in rows for v in r['values']),
                 seconds=time.time()-start)
    result=dict(summary=summary,rows=rows,scope='finite parameter bundles, NOT a uniform prime theorem')
    out.write_text(json.dumps(result,indent=2));print('SUMMARY '+json.dumps(summary),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--pairs',default='31:4:11,37:5:13,49:6:17,67:8:23,125:16:43,155:18:53')
    ap.add_argument('--out',default='parameter_bundle.json');args=ap.parse_args()
    run([tuple(map(int,s.split(':'))) for s in args.pairs.split(',')],Path(__file__).with_name(args.out))
