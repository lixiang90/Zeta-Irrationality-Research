"""Projective p-adic content bounds and weighted CRT lattice optimization.

Local roots are represented by residue cylinders, avoiding enumeration of
redundant singular lifts. Both projective charts are covered exactly.
"""
import argparse
import itertools
import json
import math
import sys
from pathlib import Path
from flint import arb, arb_poly, ctx, fmpq as Q
from sympy import factorint

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent


def refine(polys, residue, period, p, modulus):
    """All roots inside residue+period*Z, as disjoint complete cylinders."""
    universal = True
    for a,b,c in polys:
        c0 = a*residue**2+b*residue+c
        c1 = (2*a*residue+b)*period
        c2 = a*period**2
        if c0 % math.gcd(modulus,c1,c2):
            return []
        if c0%modulus or (c1+c2)%modulus or (2*c2)%modulus:
            universal = False
    if universal:
        return [(residue,period)]
    assert period < modulus
    out = []
    for j in range(p):
        out.extend(refine(polys,residue+j*period,period*p,p,modulus))
    return out


def local_roots(H,p,cap,rho):
    a,b,c = H[0]
    _,d,e = H[1]
    f = H[2][2]
    # Normal chart (u,v)=(x,1), and infinity chart (1,y) with p|y.
    normal = [(i,p) for i in range(1,p)] if rho%p == 0 else [(0,1)]
    infinity = [(0,p)]
    polys_n = [(a,b,c),(0,d,e),(0,0,f)]
    polys_i = [(c,b,a),(e,d,0),(f,0,0)]
    history = []
    for level in range(1,cap+1):
        modulus = p**level
        new_n = [z for r,q in normal for z in refine(polys_n,r,q,p,modulus)]
        new_i = [z for r,q in infinity for z in refine(polys_i,r,q,p,modulus)]
        if not new_n and not new_i:
            break
        normal,infinity = new_n,new_i
        history.append(dict(e=level,normal=normal,infinity=infinity))
    best = history[-1] if history else dict(e=0,normal=[(0,1)],infinity=[])
    return dict(p=p,cap=cap,**best,history=history)


def lattice_intersection(basis,alpha,beta,modulus):
    if modulus == 1:
        return basis
    v,w = basis
    a,b = alpha*v[0]+beta*v[1],alpha*w[0]+beta*w[1]
    if math.gcd(a,modulus) != 1:
        v,w = w,v
        a,b = b,a
    assert math.gcd(a,modulus) == 1
    r = -b*pow(a,-1,modulus)%modulus
    return [[modulus*v[0],modulus*v[1]], [w[0]+r*v[0],w[1]+r*v[1]]]


def optimize(path,partial=True):
    source = json.loads(path.read_text())
    H,cols,rho = source['hnf'],source['coefficients'],source['rho']
    determinant = math.prod(H[i][i] for i in range(3))
    factors = {int(p):int(e) for p,e in factorint(determinant).items()}
    local = [local_roots(H,p,e,rho) for p,e in factors.items()]
    gmax = math.prod(r['p']**r['e'] for r in local)
    print('LOCAL',[(r['p'],r['e'],len(r['normal']),len(r['infinity'])) for r in local],flush=True)

    ctx.prec = max(abs(v).bit_length() for c in cols for v in c)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    values = [arb_poly(c)(theta) for c in cols]
    baseline_content = math.gcd(*cols[0])
    baseline = values[0]/baseline_content
    schur = values[2]-values[1]**2/(4*values[0])
    assert schur > 0
    lower_nonzero_v = schur/gmax
    lower_all = lower_nonzero_v if lower_nonzero_v < baseline else baseline

    # Keep a manageable exact metric for candidate selection. Certification
    # always uses the original Arb evaluations and exact content afterwards.
    metric_precision = ctx.prec
    ctx.prec = 256
    g0 = Q(1)
    gc,g1 = [(v/values[0]).mid().fmpq() for v in values[1:]]
    assert g1-gc*gc/4 > 0
    ctx.prec = metric_precision
    def dot(v,w):
        return v[0]*w[0]+gc*(v[0]*w[1]+v[1]*w[0])/2+g1*v[1]*w[1]
    def reduce(basis):
        v,w = [list(z) for z in basis]
        det = abs(v[0]*w[1]-v[1]*w[0])
        for step in range(10000):
            if dot(w,w) < dot(v,v):
                v,w = w,v
            ratio = dot(v,w)/dot(v,v)
            if abs(ratio) <= Q(1,2):
                break
            rounded = ratio+Q(1,2)
            j = int(rounded.numerator)//int(rounded.denominator)
            w = [w[i]-j*v[i] for i in range(2)]
        else:
            raise AssertionError('Gauss iteration limit')
        assert abs(v[0]*w[1]-v[1]*w[0]) == det
        return v,w
    def content(u,v):
        return math.gcd(*(row[0]*u*u+row[1]*u*v+row[2]*v*v for row in H))

    positive = [r for r in local if r['e']]
    # Maximal layer, then omit each local constraint once. This is a specified
    # partial-content search, not an exhaustive optimization over every layer.
    layers = [None]+([r['p'] for r in positive] if partial else [])
    candidates = {(1,0),(0,1)} if rho == 1 else {(1,0)}
    counts = []
    for omitted in layers:
        bases = [[[1,0],[0,1]]]
        for row in positive:
            if row['p'] == omitted:
                continue
            constraints = [(1,-r,q) for r,q in row['normal']]
            constraints += [(-r,1,q) for r,q in row['infinity']]
            bases = [lattice_intersection(B,a,b,q) for B in bases for a,b,q in constraints]
            assert len(bases) <= 65536, 'Too many CRT classes; no silent truncation'
        counts.append(dict(omitted=omitted,classes=len(bases)))
        for basis in bases:
            v,w = reduce(basis)
            for i,j in itertools.product(range(-2,3),repeat=2):
                if i == j == 0:
                    continue
                uu,vv = i*v[0]+j*w[0],i*v[1]+j*w[1]
                g = math.gcd(uu,vv)
                uu,vv = uu//g,vv//g
                if vv < 0 or (vv == 0 and uu < 0):
                    uu,vv = -uu,-vv
                if math.gcd(uu,rho) == 1:
                    candidates.add((uu,vv))
        print('LAYER',omitted,'classes',len(bases),'candidates',len(candidates),flush=True)
    results = []
    for u,v in sorted(candidates):
        ct = content(u,v)
        assert gmax%ct == 0
        val = (u*u*values[0]+u*v*values[1]+v*v*values[2])/ct
        assert val > 0
        results.append(dict(u=str(u),v=str(v),content=str(ct),log_p=float(val.log()),
                            log_interval=val.log().str(35)))
    results.sort(key=lambda r:r['log_p'])
    for row in results[:10]:
        u,v = int(row['u']),int(row['v'])
        assert int(row['content']) == math.gcd(*(u*u*x+u*v*y+v*v*z for x,y,z in zip(*cols)))
    out = dict(source=path.name,scope='exact all-parameter content bound; finite candidate optimization',
               K=source['K'],h=source['h'],high=source['high'],rho=rho,
               factors=factors,local=local,max_content=str(gmax),
               baseline_log=float(baseline.log()),schur_log=schur.log().str(35),
               all_parameter_lower_log=lower_all.log().str(35),
               all_parameter_lower_log_float=float(lower_all.log()),
               uniform_lower_exceeds_one=bool(lower_all > 1),
               layers=counts,candidate_count=len(results),best=results[:20])
    dest = path.with_name(path.stem+'_optimized.json')
    dest.write_text(json.dumps(out,indent=2))
    print('RESULT',source['K'],'baseline',out['baseline_log'],'best',results[0],
          'UNIFORM_LOWER_LOG',out['all_parameter_lower_log'],flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    p.add_argument('--max-only',action='store_true')
    args = p.parse_args()
    optimize(Path(args.source),partial=not args.max_only)
