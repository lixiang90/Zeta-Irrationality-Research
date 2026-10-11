"""Positive-cone lattice certificates using rational bounds only.

Continued fractions select candidates, not a claimed global optimizer.
No zeta digits enter candidate selection or the rigorous upper bound.
"""
import json
from pathlib import Path
from flint import fmpq as Q
from zeta35_numerator_space import combine,evaluate


def cf_candidates(value,side):
    v=value;p0,p1=0,1;q0,q1=1,0
    candidates=set()
    while True:
        a=int(v.floor())
        for k in set((1,a)):
            if not 1<=k<=a:
                continue
            p,q=k*p1+p0,k*q1+q0
            if q and (Q(p,q)<=value if side=='lower' else Q(p,q)>=value):
                candidates.add((q,-p) if side=='lower' else (-q,p))
        p0,p1=p1,a*p1+p0;q0,q1=q1,a*q1+q0
        rem=v-a
        if not rem:
            candidates.add((q1,-p1) if side=='lower' else (-q1,p1))
            break
        v=1/rem
    return candidates


def certificate(case):
    if 'lower' not in case['endpoints'] or 'upper' not in case['endpoints']:
        return None
    lo=Q(case['endpoints']['lower']['bound']);hi=Q(case['endpoints']['upper']['bound'])
    assert lo<hi
    candidates=cf_candidates(lo,'lower')|cf_candidates(hi,'upper')|{(0,1)}
    def upper(pair):
        a,c=pair
        return a*(hi if a>=0 else lo)+c
    a,c=min(candidates,key=upper)
    bound=upper((a,c));assert bound>0
    L=case['endpoints']['lower']['ray'];U=case['endpoints']['upper']['ray']
    la,lc,ua,uc=map(int,(L['a'],L['c'],U['a'],U['c']))
    det=la*uc-ua*lc
    alpha=Q(a*uc-ua*c,det);beta=Q(la*c-a*lc,det)
    assert alpha>=0 and beta>=0 and alpha+beta>0
    rows=[[Q(v) for v in row] for row in case['rows']]
    p=[Q(0)]*len(rows)
    scales=[]
    for ray,mult in ((L,alpha),(U,beta)):
        i,j=ray['i'],ray['j'];u,v=Q(ray['u']),Q(ray['v'])
        rawA=u*rows[i][0]+v*rows[j][0]
        scale=Q(int(ray['a']))/rawA
        assert scale>0
        p[i]+=mult*scale*u;p[j]+=mult*scale*v
        scales.append(str(scale))
    assert all(v>=0 for v in p)
    assert combine(rows,p)==[Q(a),Q(3*a),Q(c)]
    value=evaluate(Q(a),Q(c))
    # Strict upper bound comes from independently proved lo < theta < hi.
    exclusion=int((1/bound).floor())+1
    record=dict(N=case['N'],M=case['M'],d=case['d'],a=str(a),c=str(c),
                lower=str(lo),upper=str(hi),strict_error_upper=str(bound),
                rational_denominator_at_least=str(exclusion),
                endpoint_weights=[str(alpha),str(beta)],endpoint_normalizations=scales,
                positive_polynomial_coefficients=[str(v) for v in p],
                candidate_count=len(candidates),log_L=value['log_L'])
    print('lattice',case['N'],case['d'],'logL',round(value['log_L'],6),
          'denominator exclusion digits',len(str(exclusion)),flush=True)
    return record


if __name__=='__main__':
    path=Path(__file__).parent
    cases=json.loads((path/'zeta35_positive_cone.json').read_text(encoding='utf-8'))['cases']
    results=[v for c in cases if (v:=certificate(c)) is not None]
    (path/'zeta35_cone_lattice.json').write_text(json.dumps(dict(
        scope='finite positivity certificates and denominator exclusions; no asymptotic irrationality claim',
        rows=results),indent=2),encoding='utf-8')
