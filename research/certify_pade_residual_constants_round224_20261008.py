"""One finite rational certificate, m=1,3 and degrees<=4; no prime input.

This certifies constants in the paper's p-adic argument, not that argument itself.
No recurrence guessing, prime/parameter scan, or floating point arithmetic.
"""
from fractions import Fraction as Q
from math import comb
import json
from pathlib import Path


def hs(n, order=1):
    return sum((Q(1, j**order) for j in range(1, n + 1)), Q(0))


def convolution(left, right, degree=4):
    return [sum((left[i] * right[h-i]
                 for i in range(h + 1)
                 if i < len(left) and h-i < len(right)), Q(0))
            for h in range(degree + 1)]


def det3(rows):
    a, b, c = rows
    return (a[0] * (b[1]*c[2] - b[2]*c[1])
            - a[1] * (b[0]*c[2] - b[2]*c[0])
            + a[2] * (b[0]*c[1] - b[1]*c[0]))


def exact_string(value):
    value = Q(value)
    return str(value.numerator) if value.denominator == 1 else str(value)


psi = convolution(
    convolution([Q((-1)**h * comb(3, h)) for h in range(4)],
                [Q(comb(3, h), 2**h) for h in range(4)]),
    [Q((-1)**h * comb(5+h, h)) for h in range(5)])
assert psi == [Q(1), Q(-15,2), Q(117,4), Q(-653,8), Q(1491,8)]

kappas = [Q(3,2), Q(15,4), Q(189,32)]
depths = [4, 2, 0]
v1 = [k * (psi[h] + (2*psi[h-1] if h else 0))
      for k, h in zip(kappas, depths)]
cubic_basis = convolution(psi, [Q(1,8), Q(3,4), Q(3,2), Q(1)])
v3 = [k * 2*cubic_basis[h] for k, h in zip(kappas, depths)]
w = [Q(0), Q(-45,2), Q(-189,16)]

assert v1 == [Q(555,16), Q(855,16), Q(189,32)]
assert v3 == [Q(-297,64), Q(-225,64), Q(189,128)]
matrix_det = det3([w, v1, v3])
assert matrix_det == Q(1148175,4096)

packet = {}
for m in (1, 3):
    local = []
    for a in range(m + 1):
        b = m-a
        ta = comb(m,a)**2 * comb(m+a,m) * comb(2*m-a,m)
        la = hs(m+a) + 2*hs(2*m-a) - 3*hs(m-a)
        ma = hs(m+a,2) + 4*hs(2*m-a,2) - 3*hs(m-a,2)
        qa = 3*(hs(2*m-a) - hs(m+a) + 3*hs(a) - 3*hs(m-a))
        ell = 3*(hs(m+a,2) - 2*hs(2*m-a,2) + 3*hs(m-a,2))
        rho = 3*(hs(m+a,2) + hs(2*m-a,2) - 3*hs(a,2) - 3*hs(m-a,2))
        nu = 3*(hs(2*m-a,3) - hs(m+a,3) + 3*hs(a,3) - 3*hs(m-a,3))
        da = Q(9,2)*la**2 - Q(3,2)*ma
        cubic = qa**3/6 - qa*rho/2 + nu/3
        gamma = ell + 3*la*qa
        delta = (qa**2-rho)/2
        lb = hs(m+b) + 2*hs(2*m-b) - 3*hs(m-b)
        mb = hs(m+b,2) + 4*hs(2*m-b,2) - 3*hs(m-b,2)
        db = Q(9,2)*lb**2 - Q(3,2)*mb
        assert qa == 3*(la-lb)
        assert gamma-delta == da-db
        local.append(dict(a=a, T=ta, L=la, M=ma, q=qa, ell=ell,
                          rho=rho, nu=nu, D=da, cubic=cubic, mirror_D=db))
    bm = sum(((-1)**e['a'] * 8*e['T']**3 * e['q'] for e in local), Q(0))
    dm = sum(((-1)**e['a'] * 8*e['T']**3 * (e['D']-e['mirror_D'])
              for e in local), Q(0))
    fm = sum(((-1)**e['a'] * 8*e['T']**3 * e['cubic'] for e in local), Q(0))
    packet[m] = dict(local=local, B=bm, D=dm, F=fm)

assert packet[1]['B'] == -960
assert packet[3]['B'] == 2909459200
assert packet[1]['D'] == -6048
assert packet[3]['D'] == 23729805120
assert packet[1]['F'] == -10448
assert packet[3]['F'] == Q(660203246512,27)
beta = packet[3]['B']/packet[1]['B']
d = packet[3]['D']-beta*packet[1]['D']
f = packet[3]['F']-beta*packet[1]['F']
constant = packet[1]['B'] * f * matrix_det
assert beta == Q(-9092060,3)
assert d == 5400212160
assert f == Q(-194741339408,27)
assert constant == Q(7763789492179875,4)

output = {
    'scope': 'fixed m=1,3; finite harmonic/binomial constants; no prime input or scan',
    'arithmetic': 'Python Fraction exact rational arithmetic only',
    'pass': True,
    'psi_0_to_4': [exact_string(x) for x in psi],
    'w': [exact_string(x) for x in w],
    'v1': [exact_string(x) for x in v1],
    'v3': [exact_string(x) for x in v3],
    'det_w_v1_v3': exact_string(matrix_det),
    'packet': {str(m): {
        'B': exact_string(e['B']), 'D': exact_string(e['D']), 'F': exact_string(e['F']),
        'local': [{key: (val if key in ('a','T') else exact_string(val))
                   for key,val in row.items()} for row in e['local']]
    } for m,e in packet.items()},
    'beta': exact_string(beta),
    'second_layer_scalar_d': exact_string(d),
    'cubic_residual_scalar_f': exact_string(f),
    'delta_div_p_constant': exact_string(constant),
    'global_proof_note': 'All-prime expansions, error bounds and determinant cancellation are paper proofs; this output certifies only these finite constants.'
}
target = Path(__file__).with_name('pade_residual_constants_round224_20261008.json')
target.write_text(json.dumps(output, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(output, ensure_ascii=False, indent=2))
