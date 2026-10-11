"""Exact bounded Hensel fibers for full coefficient-content protection.

At a fixed small q-adic x=q^a*u, solve all 38 quadratic coefficient
congruences for y=q^b*V.  Solutions are exact residue classes up to the old
content threshold.  A branch cap is explicit and any capped case is not
reported as an impossibility.
"""
import json,sys,math
from pathlib import Path
from flint import fmpq as Q
from zeta7_joint_lattice_20261004 import vp,unit

sys.set_int_max_str_digits(0)


def qmod(c,p,mod):
    if not c:return 0
    n,d=int(c.numerator),int(c.denominator)
    assert d%p
    return n*pow(d,-1,mod)%mod


def fiber(coeff,p,x,b,v0,cap=4096):
    raw=[[Q(0) for _ in range(38)] for _ in range(3)]
    for i,j,cs in coeff:
        xx=x**i*p**(j*b)
        for k,c in enumerate(cs):raw[j][k]+=c*xx
    m=min(vp(c,p) for cs in raw for c in cs if c);depth=v0-m
    if depth<=0:return dict(protected=True,depth=depth,normalization=m,roots=[1],complete=True)
    mod=p**depth
    raw=[[c/Q(p)**m for c in cs] for cs in raw]
    cs=[[qmod(c,p,mod) for c in row] for row in raw]
    def evaluate(v,modulus):
        return [(a+b*v+c*v*v)%modulus for a,b,c in zip(*cs)]
    roots=[v for v in range(1,p) if not any(evaluate(v,p))]
    maxbranches=len(roots)
    for r in range(1,depth):
        power=p**r;nextmod=power*p;new=[]
        for v in roots:
            residual=[t//power for t in evaluate(v,nextmod)]
            derivative=[(b+2*c*v)%p for b,c in zip(cs[1],cs[2])]
            pivot=next((k for k,d in enumerate(derivative) if d),None)
            if pivot is not None:
                digit=-residual[pivot]*pow(derivative[pivot],-1,p)%p
                if all((z+d*digit)%p==0 for z,d in zip(residual,derivative)):
                    new.append(v+power*digit)
            elif not any(residual):
                new.extend(v+power*d for d in range(p))
        roots=new;maxbranches=max(maxbranches,len(roots))
        if len(roots)>cap:
            return dict(protected=None,depth=depth,normalization=m,complete=False,
                        stopped_layer=r+1,branches=len(roots),maxbranches=maxbranches)
        if not roots:
            return dict(protected=False,depth=depth,normalization=m,complete=True,
                        obstruction_layer=r+1,maxbranches=maxbranches)
    assert all(not any(evaluate(v,mod)) for v in roots)
    return dict(protected=bool(roots),depth=depth,normalization=m,roots=list(map(str,roots)),
                complete=True,maxbranches=maxbranches)


def main():
    folder=Path(__file__).parent
    coefficient_path=folder/'zeta7_two_moment_partial_20261004_coefficients.json'
    data=json.loads(coefficient_path.read_text(encoding='utf-8'))
    coeff=[(r['i'],r['j'],[Q(c) for c in r['polynomial_coefficients']]) for r in data['coefficients']]
    local=json.loads((folder/'zeta7_joint_lattice_20261004.json').read_text(encoding='utf-8'))
    results=[]
    for info in local['results']:
        p=info['p'];v0=info['baseline_content_valuation']
        terms=[(r['i'],r['j'],r['v']) for r in info['coefficient_content_valuations']]
        face_map={tuple(tuple(s) for s in f['support']):f for f in info['faces']}
        amin=info['termwise_protection_minimum_x_valuation']
        btop=info['termwise_protection_boundary'][0][1]
        rows=[]
        for a in range(amin):
            for b in range(btop+1):
                weights=[v+i*a+j*b for i,j,v in terms];minimum=min(weights)
                support=tuple((i,j) for (i,j,v),w in zip(terms,weights) if w==minimum)
                face=face_map.get(support)
                if not face or not face['unit_roots']:continue
                for u in sorted(set(r[0] for r in face['unit_roots'])):
                    ans=fiber(coeff,p,Q(p**a*u),b,v0)
                    rows.append(dict(a=a,b=b,x_unit=u,**ans))
        successes=[r for r in rows if r['protected'] is True]
        complete=all(r['complete'] for r in rows)
        best=min(successes,key=lambda r:(r['a'],r['b']+max(r['depth'],0))) if successes else None
        result=dict(p=p,tested_fibers=len(rows),successful_fibers=len(successes),all_tests_complete=complete,
                    smallest_successful_x_valuation=best['a'] if best else None,best_fiber=best,rows=rows,
                    scope=f'0<=a<{amin}; 0<=b<={btop}; fixed integer x=p^a*u with 1<=u<p. '
                          'Absence in a fixed fiber does not exclude other higher x digits.')
        results.append(result)
        print('p',p,'fibers',len(rows),'success',len(successes),'complete',complete,
              'smallest x',best['a'] if best else None,
              'best b',best['b'] if best else None,flush=True)
        out=dict(status='in_progress',K=40,N=3,h=37,results=results,
                 scope='Bounded fixed-x unit representatives only. Congruences protect the entire '
                       'polynomial coefficient vector. No universal lower bound on x is asserted.')
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed';Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
