"""Independent finite content-bound certificate via quadratic residues.

Does not call the production residue-cylinder root lifting algorithm.
"""
import argparse
import json
import math
import sys
from pathlib import Path
from flint import fmpq_mat as Mat, fmpz_mat as ZMat, arb, arb_poly, ctx
from sympy import factorint
sys.set_int_max_str_digits(0)


def valuation(x,p,cap):
    if not x:
        return cap
    k = 0
    while k < cap and x%p == 0:
        x //= p
        k += 1
    return k


def square_exists(x,p,e):
    if e <= 0:
        return True
    x %= p**e
    v = valuation(x,p,e)
    if v == e:
        return True
    if v%2:
        return False
    unit = x//p**v
    return unit%2**min(e-v,3) == 1 if p == 2 else pow(unit%p,(p-1)//2,p) == 1


def quadratic_exists(a,b,c,p,e):
    if e <= 0:
        return True
    common = min(valuation(x,p,e) for x in (a,b,c))
    if common == e:
        return True
    a,b,c = a//p**common,b//p**common,c//p**common
    e -= common
    if a%p == 0:
        return b%p != 0
    if p != 2:
        return square_exists(b*b-4*a*c,p,e)
    if b%2:
        return c%2 == 0
    return square_exists((b//2)**2-a*c,2,e)


def normal_exists(H,p,E,rho):
    a,b,c = H[0]
    _,d,ell = H[1]
    f = H[2][2]
    modulus = p**E
    if f%modulus:
        return False
    r = valuation(d,p,E)
    if ell%p**r:
        return False
    period = p**(E-r)
    x = (-ell//p**r)*pow(d//p**r,-1,period)%period if period > 1 else 0
    starts = [(x,period)]
    if rho%p == 0:
        if period > 1:
            if x%p == 0:
                return False
        else:
            starts = [(i,p) for i in range(1,p)]
    return any(quadratic_exists(a*q*q,(2*a*x+b)*q,a*x*x+b*x+c,p,E)
               for x,q in starts)


def infinity_exists(H,p,E):
    a,b,c = H[0]
    _,d,ell = H[1]
    f = H[2][2]
    if a%p:
        return False
    modulus = p**E
    assert modulus//p <= 2_000_000, 'Independent infinity chart enumeration budget'
    return any((a+b*y+c*y*y)%modulus == 0
               and (d*y+ell*y*y)%modulus == 0 and f*y*y%modulus == 0
               for y in range(0,modulus,p))


def verify(path):
    src = json.loads(path.read_text())
    opt = json.loads(path.with_name(path.stem+'_optimized.json').read_text())
    cols,H,rho = src['coefficients'],src['hnf'],src['rho']
    C = ZMat(list(map(list,zip(*cols))))
    HH,T = C.hnf(transform=True)
    assert T*C == HH
    assert [[int(HH[i,j]) for j in range(3)] for i in range(3)] == H
    assert all(HH[i,j] == 0 for i in range(3,C.nrows()) for j in range(3))
    coordinates = Mat(C)*Mat(H).inv()
    assert all(v.denominator == 1 for v in coordinates.entries())
    factors = {int(p):int(e) for p,e in factorint(math.prod(H[i][i] for i in range(3))).items()}
    assert factors == {int(k):v for k,v in opt['factors'].items()}
    certs = []
    for row in opt['local']:
        p,e,cap = row['p'],row['e'],row['cap']
        assert factors[p] == cap
        if e:
            assert normal_exists(H,p,e,rho) or infinity_exists(H,p,e)
        if e < cap:
            assert not normal_exists(H,p,e+1,rho)
            assert not infinity_exists(H,p,e+1)
        certs.append(dict(p=p,max_exponent=e,independent_residue_test=True))
    gmax = math.prod(r['p']**r['max_exponent'] for r in certs)
    assert gmax == int(opt['max_content'])
    ctx.prec = max(abs(v).bit_length() for c in cols for v in c)+6000
    theta = 3*arb(3).zeta()+arb(5).zeta()
    q0,qc,q1 = [arb_poly(c)(theta) for c in cols]
    base = q0/math.gcd(*cols[0])
    schur = q1-qc*qc/(4*q0)
    bound = schur/gmax
    assert q0 > 0 and schur > 0
    if bound < base:
        lower = bound
    else:
        assert base < bound
        lower = base
    for row in opt['best']:
        u,v = int(row['u']),int(row['v'])
        assert math.gcd(u,v) == 1 and math.gcd(u,rho) == 1
        coeff = [u*u*x+u*v*y+v*v*z for x,y,z in zip(*cols)]
        g = math.gcd(*coeff)
        assert g == int(row['content']) and gmax%g == 0
        value = arb_poly([c//g for c in coeff])(theta)
        assert value > 0
        assert abs(float(value.log())-row['log_p']) < 1e-10
    result = dict(K=src['K'],h=src['h'],high=src['high'],rho=rho,
                  exact_row_lattice_verified=True,local=certs,
                  lower_log_interval=lower.log().str(45),
                  lower_log_integer=int(lower.log().floor().unique_fmpz()),
                  best_log=opt['best'][0]['log_interval'])
    path.with_name(path.stem+'_bound_verified.json').write_text(json.dumps(result,indent=2))
    print(result,flush=True)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('source')
    args = p.parse_args()
    verify(Path(args.source))
