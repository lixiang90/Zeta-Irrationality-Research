"""NEW independent, first-only finite mechanism and exact affine certificate.

This source reads no old/peer mathematics files.  Its finite cases do not prove
the all-scale assertions in the accompanying paper.  The output guard is
created before mathematical work; a failure is preserved and cannot be rerun.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd
from pathlib import Path
import json
import traceback


OUT = Path(__file__).with_suffix('.json')
with OUT.open('x', encoding='utf-8') as handle:
    json.dump({'state': 'started_first_only', 'old_or_peer_inputs_read': 0}, handle)


def valuation(x, p):
    if x == 0:
        return 10**9
    result = 0
    while x % p == 0:
        result += 1
        x //= p
    return result


def isprime(p):
    return p > 1 and all(p % d for d in range(2, int(p**0.5) + 1))


def binomial(z, i):
    if i == 0:
        return 1
    if z >= 0:
        return comb(z, i) if i <= z else 0
    return (-1)**i * comb(i - z - 1, i)


def rref(rows, p, width):
    a = [[x % p for x in row] for row in rows]
    pivot_columns = []
    rr = 0
    for col in range(width):
        pivot = next((j for j in range(rr, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        inv = pow(a[rr][col], -1, p)
        a[rr] = [(x * inv) % p for x in a[rr]]
        for j in range(len(a)):
            if j != rr and a[j][col]:
                cc = a[j][col]
                a[j] = [(x - cc*y) % p for x, y in zip(a[j], a[rr])]
        pivot_columns.append(col)
        rr += 1
        if rr == len(a):
            break
    return a, pivot_columns


def rank(rows, p, width):
    return len(rref(rows, p, width)[1])


def original_basis(n):
    m = 2*n
    dd = [None] + [factorial(6*n+j)//factorial(j-1) for j in range(1, m+1)]
    primitive = []
    columns = []
    for j in range(1, n+1):
        jp = m+1-j
        gg = gcd(dd[j], dd[jp])
        pp, qq = dd[j]//gg, dd[jp]//gg
        primitive.append((j, jp, pp, qq))
        vec = [0]*(3*n)
        for i in range(m):
            if i >= j-1:
                vec[i] += pp*(-1)**(i-j+1)*comb(i, j-1)
            if i >= jp-1:
                vec[i] += qq*(-1)**(i-jp+1)*comb(i, jp-1)
        columns.append(vec)
    for i in range(m, 3*n):
        vec = [0]*(3*n)
        vec[i] = 1
        columns.append(vec)
    return columns, primitive


def evaluate_coefficients(column, t):
    return sum(cc*binomial(t-1, i) for i, cc in enumerate(column))


def newton_value_and_p_derivative(n, p, t):
    modulus = p*p
    values = [binomial(t-1, i) % modulus for i in range(3*n)]
    coeff = [0]*(3*n)
    for rr in range(1, 3*n):
        if rr % p == 0:
            coeff[rr] = pow(rr//p, -1, modulus)
        else:
            coeff[rr] = p*pow(rr, -1, modulus)
        coeff[rr] = ((-1)**(rr-1)*coeff[rr]) % modulus
    derivative = [sum(coeff[rr]*values[i-rr] for rr in range(1, i+1)) % modulus
                  for i in range(3*n)]
    return values, derivative


def harmonic(l, power, modulus):
    return sum(pow(pow(d, -1, modulus), power, modulus)
               for d in range(1, l+1)) % modulus


def scaled_harmonic1(z, p):
    modulus = p*p
    return sum(pow(d//p, -1, modulus) if d % p == 0
               else p*pow(d, -1, modulus) for d in range(1, z+1)) % modulus


def one_case(n, p):
    assert p > 5 and n < p <= 2*n and p*p > 8*n
    width = 2*n
    modulus = p*p
    original, primitive = original_basis(n)
    for column in original:
        for mm, mp, pp, qq in primitive:
            assert qq*evaluate_coefficients(column, mm) == pp*evaluate_coefficients(column, mp)
    qs, remainder = divmod(3*n, p)
    hh, ee = divmod(6*n, p)
    uu = min(ee+1, 2*p-2*n)
    unit_tail = []
    newton_rows = []
    value_rows = []
    cache = []
    weights = []
    for j in range(6*n+1):
        weight = comb(6*n, j)**2*comb(2*n+j, j)**3
        ww = valuation(weight, p)
        assert ww in (0, 2, 3, 5)
        rho = j % p
        assert ww == 2*(rho > ee)+3*(rho >= 2*p-2*n)
        values, derivatives = newton_value_and_p_derivative(n, p, -j)
        cache.append((values, derivatives))
        weights.append(weight % modulus)
        if j >= p and ww == 0:
            unit_tail.append(j)
            newton_rows.extend([values, derivatives])
            value_rows.append(values)
    assert {j % p for j in unit_tail} == set(range(uu))
    assert all(sum(j % p == rho for j in unit_tail) == hh for rho in range(uu))
    ambient_dimension = qs*uu+min(remainder, uu)
    assert rank(newton_rows, p, 3*n) == ambient_dimension
    assert rank(value_rows, p, 3*n) == ambient_dimension
    actual_rows = [[sum(row[i]*column[i] for i in range(3*n)) % p
                    for column in original] for row in newton_rows]
    reduced, pivots = rref(actual_rows, p, width)
    free = [i for i in range(width) if i not in pivots]
    change = []
    for ii in pivots:
        cc = [0]*width
        cc[ii] = 1
        change.append(cc)
    for ii in free:
        cc = [0]*width
        cc[ii] = 1
        for rr, pivot in enumerate(pivots):
            cc[pivot] = (-reduced[rr][ii]) % p
        change.append(cc)
    assert rank(list(map(list, zip(*change))), p, width) == width
    actual = [[sum(original[jj][ii]*cc[jj] for jj in range(width))
               for ii in range(3*n)] for cc in change]
    for column in actual:
        for mm, mp, pp, qq in primitive:
            assert qq*evaluate_coefficients(column, mm) == pp*evaluate_coefficients(column, mp)
    strong = len(pivots)
    kk = width-strong
    k0 = max(0, width-ambient_dimension)
    assert kk >= k0
    eval_cache = []
    for j, (values, derivatives) in enumerate(cache):
        vv = [sum(cc*val for cc, val in zip(column, values)) % modulus
              for column in actual]
        dd = [sum(cc*val for cc, val in zip(column, derivatives)) % modulus
              for column in actual]
        eval_cache.append((vv, dd))
        if j in unit_tail:
            assert all(vv[i] % p == dd[i] % p == 0 for i in range(strong, width))
    source_checks = []
    for aa, bb in [(0, 1), (1, 1)]:
        gram = [[0]*width for _ in range(width)]
        for j, (vv, dd) in enumerate(eval_cache):
            ww = weights[j]
            ll = j//p
            h3 = harmonic(ll, 3, modulus)
            h4 = harmonic(ll, 4, modulus)
            h5 = harmonic(ll, 5, modulus)
            uhat = (-8*aa*p*h3-6*bb*h4) % modulus
            chat = (5*scaled_harmonic1(j, p)-3*scaled_harmonic1(2*n+j, p)
                    -2*scaled_harmonic1(6*n-j, p)) % modulus
            vhat = (chat*uhat-24*aa*p*h4-24*bb*h5) % modulus
            for ii in range(width):
                for jj in range(ii, width):
                    gram[ii][jj] = (gram[ii][jj]+ww*(uhat*(vv[ii]*dd[jj]+dd[ii]*vv[jj])
                                                       +vhat*vv[ii]*vv[jj])) % modulus
        for ii in range(width):
            for jj in range(max(ii, strong), width):
                expected = modulus if ii >= strong else p
                assert gram[ii][jj] % expected == 0
        # The whole-X coefficient of p^5 B is 24 p^5 W vv^T, identically 0 mod p^2.
        assert 24*p**5 % modulus == 0
        source_checks.append({'a': aa, 'b': bb, 'strong_weak_p': True,
                              'weak_weak_p2': True, 'whole_X_coefficient_p2': True})
    return {'n': n, 'p': p, 'Q': qs, 'R': remainder, 'u': uu,
            'ambient_rank': ambient_dimension, 'actual_Hermite_rank': strong,
            'actual_kernel': kk, 'lower_kernel': k0,
            'exact_characteristic_zero_paired_lifts': True,
            'sources': source_checks}


RAW = [(F(1), F(8, 7), F(4), F(-12)),
       (F(8, 7), F(6, 5), F(25), F(-36)),
       (F(6, 5), F(4, 3), F(0), F(-10)),
       (F(4, 3), F(3, 2), F(18), F(-34)),
       (F(3, 2), F(8, 5), F(-2), F(-8)),
       (F(8, 5), F(2), F(8), F(-24))]
DIRECT = [(F(1), F(8, 7), F(-12), F(6)),
          (F(8, 7), F(6, 5), F(30), F(-42)),
          (F(6, 5), F(5, 4), F(-12), F(6)),
          (F(5, 4), F(4, 3), F(-4), F(-4)),
          (F(4, 3), F(3, 2), F(20), F(-36)),
          (F(3, 2), F(5, 3), F(0), F(-10)),
          (F(5, 3), F(2), F(12), F(-30))]
TENTS = []
for hh in (3, 4, 5):
    ll, mid, rr = F(6, hh+1), F(14, 2*hh+3), F(8, hh+2)
    TENTS.extend([(ll, mid, F(hh+1), F(-6)),
                  (mid, rr, F(-hh-2), F(8))])


def piece(table, x, zero=False):
    for lo, hi, slope, intercept in table:
        if lo < x < hi:
            return slope, intercept
    if zero:
        return F(0), F(0)
    raise AssertionError(('uncovered point', x))


def value(line, x):
    return line[0]*x+line[1]


def integral(line, lo, hi):
    return line[0]*(hi*hi-lo*lo)/2+line[1]*(hi-lo)


def affine_certificate():
    cut = {F(1), F(2)}
    for table in (RAW, DIRECT, TENTS):
        for lo, hi, _, _ in table:
            cut.update([lo, hi])
    ordered = sorted(cut)
    for lo, hi in zip(ordered, ordered[1:]):
        xx = (lo+hi)/2
        aa, bb = piece(RAW, xx)
        cc, dd = piece(TENTS, xx, True)
        original = (aa+2*cc, bb+2*dd)
        direct = piece(DIRECT, xx)
        lines = [original, direct, (F(0), F(-10))]
        for i in range(3):
            for j in range(i):
                slope = lines[i][0]-lines[j][0]
                intercept = lines[i][1]-lines[j][1]
                if slope:
                    root = -intercept/slope
                    if lo < root < hi:
                        cut.add(root)
    ordered = sorted(cut)
    rows = []
    area = F(0)
    for lo, hi in zip(ordered, ordered[1:]):
        xx = (lo+hi)/2
        aa, bb = piece(RAW, xx)
        cc, dd = piece(TENTS, xx, True)
        rawcarry = (aa+2*cc, bb+2*dd)
        old = max([rawcarry, (F(0), F(-10))], key=lambda z: value(z, xx))
        direct = piece(DIRECT, xx)
        new = max([old, direct], key=lambda z: value(z, xx))
        delta = (new[0]-old[0], new[1]-old[1])
        # All possible crossing roots were inserted; endpoint checks certify closed pieces.
        assert all(value(old, t) >= max(value(rawcarry, t), F(-10)) for t in (lo, hi))
        assert all(value(new, t) >= max(value(old, t), value(direct, t)) for t in (lo, hi))
        assert all(value(delta, t) >= 0 for t in (lo, hi))
        paid = integral(delta, lo, hi)
        area += paid
        rows.append({'lo': str(lo), 'hi': str(hi), 'old': list(map(str, old)),
                     'direct': list(map(str, direct)), 'delta': list(map(str, delta)),
                     'paid_area': str(paid)})
    expected = F(1,14)+F(21,400)+F(15,1936)+F(28,1089)+F(5,36)+F(1,24)+F(3,8)
    assert area == expected
    base = F(790225879771, 17925027120)
    return {'partition': rows, 'area': str(area), 'prior_safe_A': str(base),
            'new_safe_A': str(base-area),
            'gain_window_millionths': [area.numerator*10**6//area.denominator,
                                      area.numerator*10**6//area.denominator+1],
            'new_A_window_millionths': [(base-area).numerator*10**6//(base-area).denominator,
                                       (base-area).numerator*10**6//(base-area).denominator+1],
            'scope': 'exact closed affine comparison; PNT/all-scale proof is in the paper'}


try:
    cases = [one_case(n, p) for n in range(1, 19)
             for p in range(n+1, 2*n+1)
             if isprime(p) and p > 5 and p*p > 8*n]
    result = {'state': 'PASS', 'own_execution': 'first_only_once',
              'old_or_peer_inputs_read': 0, 'finite_mechanism_cases': cases,
              'finite_case_count': len(cases), 'affine_certificate': affine_certificate(),
              'finite_scope': 'actual degree<3n paired lifts and original scaled Gram mod p^2',
              'not_claimed': ['infinite nonzero', 'exact Gram Smith', 'all-scale theorem from samples']}
except BaseException as exc:
    result = {'state': 'FAIL_PRESERVED', 'old_or_peer_inputs_read': 0,
              'exception': repr(exc), 'traceback': traceback.format_exc()}
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    raise
OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
print(json.dumps({'state': result['state'], 'cases': result['finite_case_count'],
                  'gain': result['affine_certificate']['area'],
                  'new_safe_A': result['affine_certificate']['new_safe_A']}, ensure_ascii=False))
