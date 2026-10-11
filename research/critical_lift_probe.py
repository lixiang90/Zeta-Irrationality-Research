"""Exact output maps in the centered near-critical fixed-pole space.

Finite experiments only. The polynomial variable below is x=2*t+n.
"""
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq


def harmonic_table(n, s):
    h = [[fmpq(0) for _ in range(s + 1)] for _ in range(n + 1)]
    for j in range(1, n + 1):
        for k in range(1, s + 1):
            h[j][k] = h[j - 1][k] + fmpq(1, j ** k)
    return h


def output_map(n, s=7, degrees=(0, 2, 4, 6), head=0):
    h = harmonic_table(n, s)
    out = [[fmpq(0) for _ in degrees] for _ in range(s + 1)]
    coefficients = []
    for j in range(n + 1):
        log = [fmpq(0)] + [fmpq(s * (-1) ** r, r)
               * (h[n-j][r] + (-1) ** r * h[j][r]) for r in range(1, s)]
        b = [fmpq(1)]
        for m in range(1, s):
            b.append(sum((r * log[r] * b[m-r] for r in range(1, m+1)), fmpq(0))/m)
        scale = fmpq(1, ((-1) ** j * math.factorial(j) * math.factorial(n-j)) ** s)
        head_jet = [fmpq(1)] + [fmpq(0)]*(s-1)
        center = n-2*j
        for ell in range(1, head+1):
            factor = [center**2-(n+2*ell)**2, 4*center, 4]
            head_jet = [sum((head_jet[m-r]*factor[r] for r in range(min(2,m)+1)), fmpq(0))
                        for m in range(s)]
        local = []
        for col, d in enumerate(degrees):
            p = [fmpq(math.comb(d, r) * 2**r * (n-2*j)**(d-r))
                 if r <= d else fmpq(0) for r in range(s)]
            p = [sum((p[r]*head_jet[m-r] for r in range(m+1)), fmpq(0)) for m in range(s)]
            c = [fmpq(0)] * (s+1)
            for k in range(1, s+1):
                c[k] = scale * sum((p[r]*b[s-k-r] for r in range(s-k+1)), fmpq(0))
                out[k][col] += c[k]
                out[0][col] -= c[k]*h[j][k]
            local.append(c)
        coefficients.append(local)
    return out, coefficients


def primitive(values):
    den = math.lcm(*(int(x.denominator) for x in values))
    ints = [int(x * den) for x in values]
    g = math.gcd(*ints)
    return [x//g for x in ints], fmpq(den, g)


def cross(a, b):
    return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]


def probe(n):
    out, local = output_map(n)
    assert all(out[k][j] == 0 for k in (1, 2, 4, 6) for j in range(4))
    p, _ = primitive(cross(out[3][:3], out[5][:3]))
    if p[-1] < 0:
        p = [-x for x in p]
    a = [sum((out[k][j]*p[j] for j in range(3)), fmpq(0)) for k in range(8)]
    assert all(a[k] == 0 for k in (1, 2, 3, 4, 5, 6))
    assert a[7]
    pair, factor = primitive([a[0], a[7]])
    # For P(x)=p0+p1*x^2+p2*x^4, x>=n+2 for t>=1.
    # All shifted y=x^2-(n+2)^2 coefficients nonnegative certify positivity.
    y0 = (n+2)**2
    shifted = [p[0]+p[1]*y0+p[2]*y0*y0, p[1]+2*p[2]*y0, p[2]]
    positive_certificate = all(x >= 0 for x in shifted) and shifted[0] > 0
    q0, q7 = pair
    bits = max(abs(q0).bit_length(), abs(q7).bit_length()) + 512
    with ctx.workprec(bits):
        value = arb(q0) + arb(q7)*arb(7).zeta()
        assert not value.contains(0)
        raw = value/arb(factor)
        error = value/arb(q7)
        result = dict(n=n, s=7, decay_M=7*n+2,
            numerator_centered_even_coefficients=list(map(str,p)),
            output_pair=list(map(str,pair)), output_scale=str(factor),
            positive_on_t_ge_1_certificate=positive_certificate,
            shifted_numerator_coefficients=list(map(str,shifted)),
            primitive_form_value=value.str(25),
            log_abs_primitive_per_n=(abs(value).log()/n).str(20),
            log_denominator_per_n=(arb(abs(q7)).log()/n).str(20),
            log_approximation_error_per_n=(abs(error).log()/n).str(20),
            raw_sum=raw.str(20),
            rational_approximation=str(fmpq(-q0,q7)))
    # Independent rational evaluations validate the entire partial fraction map.
    for t in (1, 2, n+1):
        for col, degree in enumerate((0, 2, 4, 6)):
            direct = fmpq((2*t+n)**degree, math.prod((t+j)**7 for j in range(n+1)))
            pf = sum((local[j][col][k]/(t+j)**k for j in range(n+1) for k in range(1,8)), fmpq(0))
            assert direct == pf
    return result


def main():
    rows = []
    path = Path(__file__).with_suffix('.json')
    for n in (2, 4, 6, 8, 12, 16, 24, 32):
        row = probe(n)
        rows.append(row)
        path.write_text(json.dumps(dict(scope='Finite exact arithmetic and Arb enclosures; no asymptotic claim.', rows=rows), indent=2), encoding='utf-8')
        print(json.dumps({k:row[k] for k in ('n','positive_on_t_ge_1_certificate','log_abs_primitive_per_n','log_denominator_per_n','log_approximation_error_per_n')}), flush=True)


if __name__ == '__main__':
    main()
