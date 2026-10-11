"""Exact content bound, exhaustive local roots, and short-vector CRT search.

The content maximum is proved for this finite two-parameter family only.
Short-vector sampling does not certify a global minimum of primitive values.
"""
import itertools
import json
import math
from pathlib import Path
from flint import fmpz_mat, arb, arb_poly, ctx
from sympy import factorint

ROOT = Path(__file__).parent


def main():
    source = json.loads((ROOT/'zeta35_local_graph.json').read_text())
    cols = source['coefficients']
    C = fmpz_mat(list(map(list, zip(*cols))))
    H, T = C.hnf(transform=True)
    assert T*C == H and abs(T.det()) == 1
    rows = [[int(H[i,j]) for j in range(3)] for i in range(34)]
    assert all(row == [0,0,0] for row in rows[3:])
    assert rows[0][0] == 1 and rows[1][0] == rows[2][0] == rows[2][1] == 0
    _, a, b = rows[0]
    _, m, ell = rows[1]
    k = rows[2][2]

    def content(u,v):
        assert math.gcd(u,v) == 1
        return math.gcd(u*u+a*u*v+b*v*v, m*u+ell*v, k)

    for row in source['rows']:
        assert content(row['u'],row['v']) == int(row['content'])
    local = []
    max_content = 1
    for pp, ee in factorint(k).items():
        p, cap = int(pp), int(ee)
        roots, modulus, exponent = [0], 1, 0
        for e in range(1,cap+1):
            nxt = [x+j*modulus for x in roots for j in range(p)
                   if ((x+j*modulus)**2+a*(x+j*modulus)+b)%(modulus*p) == 0
                   and (m*(x+j*modulus)+ell)%(modulus*p) == 0
                   and (p != 41 or (x+j*modulus)%41 != 0)]
            if not nxt:
                break
            roots, modulus, exponent = nxt, modulus*p, e
        period = modulus
        rootset = set(roots)
        while period > 1 and all((x+period//p)%modulus in rootset for x in roots):
            period //= p
        compressed = sorted({x%period for x in roots})
        assert len(roots) == len(compressed)*(modulus//period)
        local.append(dict(p=p,e=exponent,cap=cap,period=period,roots=compressed))
        max_content *= p**exponent

    residues, modulus = [0], 1
    for row in local:
        q = row['period']
        if q == 1:
            continue
        residues = [r+modulus*((s-r)*pow(modulus,-1,q)%q)
                    for r in residues for s in row['roots']]
        modulus *= q
    ctx.prec = max(abs(v).bit_length() for col in cols for v in col)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    values = [arb_poly(col)(theta) for col in cols]
    # A positive exact rational metric approximates the analytic metric.
    ratios = [v/values[0] for v in values]
    g0, gc, g1 = [v.mid().fmpq() for v in ratios]
    assert g0*g1-gc*gc/4 > 0
    def dot(v,w):
        return g0*v[0]*w[0]+gc*(v[0]*w[1]+v[1]*w[0])/2+g1*v[1]*w[1]
    def reduce(r):
        v,w = [modulus,0],[r,1]
        steps = 0
        while True:
            if dot(w,w) < dot(v,v):
                v,w = w,v
            ratio = dot(v,w)/dot(v,v)
            if abs(ratio) <= g0/2:
                break
            rounded = ratio+g0/2
            j = int(rounded.numerator)//int(rounded.denominator)
            w = [w[i]-j*v[i] for i in range(2)]
            steps += 1
            assert steps < 10000
        assert abs(v[0]*w[1]-v[1]*w[0]) == modulus
        return v,w

    found = {(1,0)}
    bases = []
    for r in residues:
        v,w = reduce(r)
        bases.append(dict(residue=r,basis=[v,w]))
        for i,j in itertools.product(range(-4,5),repeat=2):
            if i == j == 0:
                continue
            u,vv = i*v[0]+j*w[0],i*v[1]+j*w[1]
            gg = math.gcd(u,vv)
            u,vv = u//gg,vv//gg
            if vv < 0 or (vv == 0 and u < 0):
                u,vv = -u,-vv
            if u%41:
                found.add((u,vv))
    results = []
    for u,v in sorted(found):
        ct = content(u,v)
        direct = math.gcd(*(u*u*x+u*v*y+v*v*z for x,y,z in zip(*cols)))
        assert direct == ct and max_content%ct == 0
        value = (u*u*values[0]+u*v*values[1]+v*v*values[2])/ct
        assert value > 0
        results.append(dict(u=u,v=v,content=str(ct),maximal=ct == max_content,
                            log_p=float(value.log()),log_p_interval=value.log().str(40)))
    results.sort(key=lambda r:r['log_p'])
    out = dict(scope='exact family content maximum; finite CRT short-vector sample',
               hnf=rows[:3],local=local,max_content=str(max_content),modulus=str(modulus),
               classes=len(residues),bases=bases,count=len(results),results=results)
    (ROOT/'zeta35_local_graph_crt.json').write_text(json.dumps(out,indent=2))
    print('MAX_CONTENT',max_content,'MODULUS',modulus,'CLASSES',len(residues))
    print('LOCAL',local)
    print('COUNT',len(results),'BEST',results[:8])


if __name__ == '__main__':
    main()
