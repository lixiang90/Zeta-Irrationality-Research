"""Eliminate the second correction from pairs of determinant coefficients.

Quadratic-in-y resultants give exact necessary congruence conditions on x.
This records their Newton data, rather than replacing common coefficient
conditions with determinant-value sampling.
"""
import json,sys,math
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly
from zeta7_joint_lattice_20261004 import vp,unit

sys.set_int_max_str_digits(0)


def main():
    folder=Path(__file__).parent
    d=json.loads((folder/'zeta7_two_moment_partial_20261004_coefficients.json').read_text(encoding='utf-8'))
    coefficients=[(r['i'],r['j'],[Q(c) for c in r['polynomial_coefficients']]) for r in d['coefficients']]
    polynomials=[]
    for k in range(4):
        p=[Poly() for _ in range(3)]
        for i,j,cs in coefficients:
            if len(cs)>k:p[j]+=Poly([0]*i+[cs[k]])
        polynomials.append(p)
    results=[]
    for k,l in [(0,1),(0,2),(1,2),(0,3)]:
        c,b,a=polynomials[k];f,e,d=polynomials[l]
        R=(a*f-c*d)**2-(a*e-b*d)*(b*f-c*e)
        assert R
        packets=[]
        for p in [2,3,5,7,11,13]:
            vals=[(i,vp(c,p)) for i,c in enumerate(R) if c]
            rows=[]
            for aa in range(101):
                minimum=min(v+i*aa for i,v in vals)
                initial=[(i,unit(R[i],p)) for i,v in vals if v+i*aa==minimum]
                roots=[u for u in range(1,p) if sum(c*pow(u,i,p) for i,c in initial)%p==0]
                if len(initial)>1 or aa==0:rows.append(dict(x_valuation=aa,minimum=minimum,initial=initial,unit_roots=roots))
            packets.append(dict(p=p,coefficient_valuations=vals,interesting_integer_valuations=rows))
        results.append(dict(X_coefficients=[k,l],degree=R.degree(),resultant_coefficients=list(map(str,R)),primes=packets))
        print('pair',k,l,'degree',R.degree(),'integer cancellation valuations',
              [(r['p'],[(s['x_valuation'],s['unit_roots']) for s in r['interesting_integer_valuations'] if s['unit_roots']]) for r in packets],flush=True)
    out=dict(status='passed',K=40,N=3,h=37,results=results,
             identity='R=(a*f-c*d)^2-(a*e-b*d)*(b*f-c*e), for ay²+by+c and dy²+ey+f',
             necessary_condition='If coefficients after y=p^b V normalization have minima mA,mB, '
                'then v_p R(x) >= 2mA+2mB-4b+min(v0-mA,v0-mB) whenever both target deficits are positive.',
             scope='Exact polynomial resultants and integer valuation Newton data through 100. '
                   'This file alone is not a complete elimination certificate for all parameters.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
