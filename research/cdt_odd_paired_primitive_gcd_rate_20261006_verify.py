"""NEW first-execution-only exact arithmetic for the primitive paired gcd rate.

Does not read, import or run any earlier/peer mathematical producer.  This checks
the finite piecewise-affine formula and encloses its proved integral, not a
special-value irrationality theorem or a finite-n extrapolation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve()
OUT = HERE.with_suffix('.json')
if OUT.exists():
    raise SystemExit('Refusing a second execution: certificate already exists')

ZERO, ONE, D = (F(0), F(0)), (F(0), F(1)), (F(1), F(0))

def ev(line, d):
    return line[0] * d + line[1]

def add(a, b):
    return a[0] + b[0], a[1] + b[1]

def sub(a, b):
    return a[0] - b[0], a[1] - b[1]

def choose(lines, d, kind):
    return kind(lines, key=lambda line: ev(line, d))

def interval_length(lo, hi, d, truncated=False):
    if truncated:
        hi = choose([hi, D], d, min)
    return sub(hi, lo) if ev(hi, d) > ev(lo, d) else ZERO

cells = []
for j in range(6):
    base_lo, base_hi = F(j, 6), F(j + 1, 6)
    midpoint = (base_lo + base_hi) / 2
    k = int(2 * midpoint)
    a, b = (F(6), F(-j)), (F(2), F(-k))
    c = sub(ONE, a)
    lines = [ZERO, ONE, D, c, b, sub(b, c), add(b, a)]
    cuts = {base_lo, base_hi}
    for left in lines:
        for right in lines:
            if left[0] != right[0]:
                root = (right[1] - left[1]) / (left[0] - right[0])
                if base_lo < root < base_hi:
                    cuts.add(root)
    ordered = sorted(cuts)
    for lo, hi in zip(ordered, ordered[1:]):
        d = (lo + hi) / 2
        lo2 = choose([c, b], d, max)
        hi2 = choose([ONE, add(b, a)], d, min)
        L = add(interval_length(c, sub(b, c), d),
                interval_length(lo2, hi2, d))
        K = add(interval_length(c, sub(b, c), d, True),
                interval_length(lo2, hi2, d, True))
        assert 0 <= ev(K, d) <= d and 0 <= ev(L, d) <= 1
        if cells and cells[-1][1] == lo and cells[-1][2:] == (L, K):
            cells[-1] = (cells[-1][0], hi, L, K)
        else:
            cells.append((lo, hi, L, K))
assert cells[0][0] == 0 and cells[-1][1] == 1

def antiderivative(q, d, L, K):
    l1, l0 = L
    k1, k0 = K
    return (-l1 / 2 - (l0 + k1) / (2 * (q + d))
            + (d * ev(L, d) - ev(K, d)) / (2 * (q + d) ** 2))

# Every trigamma boundary term cancels, including six reset jumps.
psi_coeffs = {}
boundary_coeffs = {}
for lo, hi, L, K in cells:
    factor = (L[1] + K[0]) / 2
    psi_coeffs[lo] = psi_coeffs.get(lo, F(0)) - factor
    psi_coeffs[hi] = psi_coeffs.get(hi, F(0)) + factor
    boundary_coeffs[lo] = boundary_coeffs.get(lo, F(0)) - (lo * ev(L, lo) - ev(K, lo)) / 2
    boundary_coeffs[hi] = boundary_coeffs.get(hi, F(0)) + (hi * ev(L, hi) - ev(K, hi)) / 2
assert all(value == 0 for value in boundary_coeffs.values())
psi_coeffs = {d: value for d, value in sorted(psi_coeffs.items()) if value}
assert sum(psi_coeffs.values(), F(0)) == 0

# x in [1,2] corresponds to d in [1/2,1], q=0; x>2 contributes 11/12.
large = F(11, 12)
for lo, hi, L, K in cells:
    lo = max(lo, F(1, 2))
    if lo < hi:
        large += antiderivative(0, hi, ZERO, K) - antiderivative(0, lo, ZERO, K)

# Exact finite integration, with the analytic tail bound 0 <= tail <= 1/(Q+1).
Q = 512
partial = large
for q in range(1, Q + 1):
    partial += sum((antiderivative(q, hi, L, K) - antiderivative(q, lo, L, K)
                    for lo, hi, L, K in cells), F(0))
upper = partial + F(1, Q + 1)
scale = 10 ** 6
lower_millionths = partial.numerator * scale // partial.denominator
upper_millionths = -((-upper.numerator * scale) // upper.denominator)

# Finite exact consistency checks of the folding identity; paper supplies all d.
checks = 0
for x in [F(i, 17) for i in range(1, 35)]:
    inv = 1 / x
    q = int(inv)
    d = inv - q
    if d in {lo for lo, _, _, _ in cells} | {F(1)}:
        continue
    chosen = next(cell for cell in cells if cell[0] < d < cell[1])
    folded = x * (q * ev(chosen[2], d) + ev(chosen[3], d))
    cuts = {F(0), F(1)}
    for k in range(0, int(8 / x) + 3):
        for value in [k*x, k*x-6, 2-k*x, 8-k*x]:
            if 0 < value < 1:
                cuts.add(value)
    direct = F(0)
    points = sorted(cuts)
    for lo, hi in zip(points, points[1:]):
        t = (lo + hi) / 2
        def carry(v):
            return int((6+v)/x)-int(6/x)-int(v/x)
        direct += (hi-lo) * min(carry(t), carry(2-t))
    assert direct == folded
    checks += 1

result = {
    'status': 'exact_piecewise_integral_and_tail_checks_passed',
    'scope': 'Finite affine identities and exact rational enclosure of a paper-proved limiting integral. No old/peer producer execution, no finite-n extrapolation, no special-value theorem, no Lean.',
    'first_execution_only': True,
    'producer_sha256': hashlib.sha256(HERE.read_bytes()).hexdigest(),
    'piecewise_cells': [
        {'lo': str(lo), 'hi': str(hi), 'L': list(map(str, L)), 'K': list(map(str, K))}
        for lo, hi, L, K in cells],
    'gamma_large_x_rational_part': str(large),
    'gamma_psi_one_plus_d_coefficients': [
        {'d': str(d), 'coefficient': str(c)} for d, c in psi_coeffs.items()],
    'trigamma_boundary_coefficients_all_zero': True,
    'psi_coefficients_sum_zero': True,
    'exact_folding_consistency_cases': checks,
    'exact_integrated_full_period_count': Q,
    'tail_bound': str(F(1, Q + 1)),
    'gamma_rigorous_decimal_enclosure': [f'{lower_millionths/scale:.6f}', f'{upper_millionths/scale:.6f}'],
}
OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status': result['status'], 'cells': len(cells), 'large': str(large),
                  'psi_coefficients': result['gamma_psi_one_plus_d_coefficients'],
                  'gamma_window': result['gamma_rigorous_decimal_enclosure'],
                  'folding_cases': checks}, ensure_ascii=False))
