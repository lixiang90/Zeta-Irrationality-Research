"""NEW first-only certificate. No old/peer producer is read/imported/executed.

Finite graph tests do not prove all-n Smith facts. Piecewise integration proves
the affine bound-model gate once its paper lower-bound hypotheses are supplied.
"""
from fractions import Fraction as F
from math import comb, gcd, isqrt
from pathlib import Path
import hashlib
import json

out = Path(__file__).with_suffix('.json')
if out.exists():
    raise SystemExit('FIRST-ONLY guard: output exists; do not rerun')

def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))

def rank_mod(matrix, p):
    a = [row[:] for row in matrix]
    rows, cols = len(a), len(a[0]) if a else 0
    k = 0
    for j in range(cols):
        pivot = next((i for i in range(k, rows) if a[i][j] % p), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        inv = pow(a[k][j] % p, -1, p)
        a[k] = [(v * inv) % p for v in a[k]]
        for i in range(k + 1, rows):
            q = a[i][j] % p
            if q:
                a[i] = [(u - q * v) % p for u, v in zip(a[i], a[k])]
        k += 1
        if k == rows:
            break
    return k

def mixed_count(p, z, tau):
    return max(0, min(tau, z + 1 - tau)) + max(0, min(tau - z - 1, p - tau))

graph_cases = []
for n in range(1, 41):
    for p in range(n // 2 + 1, n + 1):
        if not prime(p) or p * p <= 8 * n:
            continue
        a, z = divmod(2 * n - 1, p)
        h, e = divmod(6 * n + 1, p)
        tau = p - e
        pairs = [(r, (z - r) % p) for r in range(p) if r < (z - r) % p]
        actual_m = sum((r >= tau) != (s >= tau) for r, s in pairs)
        assert actual_m == mixed_count(p, z, tau)
        graph = []
        for m in range(1, n + 1):
            mp = 2 * n + 1 - m
            bm, bp = comb(6 * n + m, m - 1), comb(6 * n + mp, mp - 1)
            g = gcd(bm, bp)
            pm, qm = bm // g, bp // g
            row = [0] * p
            row[(m - 1) % p] += qm % p
            row[(mp - 1) % p] -= pm % p
            graph.append([v % p for v in row])
        graph_rank = rank_mod(graph, p)
        assert graph_rank <= p - actual_m
        falling = []
        for r in range(p):
            row, v = [], 1
            for j in range(p):
                row.append(v)
                v = v * (r - j) % p
            falling.append(row)
        weighted_first_layer = [
            [sum(row[r] * falling[r][j] for r in range(p)) % p for j in range(p)]
            for row in graph
        ]
        assert rank_mod(weighted_first_layer, p) == graph_rank
        graph_cases.append({'n': n, 'p': p, 'a': a, 'z': z, 'h': h,
                            'e': e, 'mixed_count': actual_m,
                            'actual_mod_p_rank': graph_rank,
                            'proved_delta_lower': n - p + actual_m})

# Literal affine raw rows from the frozen mathematical model, transcribed
# as data. Its old producer/source is not read or run by this certificate.
raw_rows = [
 ('1/4','8/31',208,-72), ('8/31','6/23',301,-96),
 ('6/23','4/15',186,-70), ('4/15','3/11',276,-94),
 ('3/11','8/29',144,-62), ('8/29','2/7',231,-86),
 ('2/7','8/27',161,-64), ('8/27','3/10',242,-88),
 ('3/10','4/13',122,-56), ('4/13','6/19',200,-80),
 ('6/19','8/25',105,-54), ('8/25','1/3',180,-78),
 ('1/3','8/23',108,-52), ('8/23','6/17',177,-76),
 ('6/17','4/11',92,-50), ('4/11','3/8',158,-74),
 ('3/8','8/21',62,-42), ('8/21','2/5',125,-66),
 ('2/5','8/19',75,-44), ('8/19','3/7',132,-68),
 ('3/7','4/9',48,-36), ('4/9','6/13',102,-60),
 ('6/13','8/17',37,-34), ('8/17','1/2',88,-58),
 ('1/2','8/15',40,-32), ('8/15','6/11',85,-56),
 ('6/11','4/7',30,-30), ('4/7','3/5',72,-54),
 ('3/5','8/13',12,-22), ('8/13','2/3',51,-46),
 ('2/3','8/11',21,-24), ('8/11','3/4',54,-48),
 ('3/4','4/5',6,-16), ('4/5','6/7',36,-40),
 ('6/7','8/9',1,-14), ('8/9','1',28,-38)
]
raw_rows = [(F(l), F(r), (F(s), F(b))) for l, r, s, b in raw_rows]
assert raw_rows[0][0] == F(1, 4) and raw_rows[-1][1] == 1
assert all(raw_rows[i][1] == raw_rows[i + 1][0] for i in range(len(raw_rows) - 1))

def val(line, x):
    return line[0] * x + line[1]

def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def scale(k, u):
    return (k * u[0], k * u[1])

def choose_max(lines, x):
    return max(lines, key=lambda u: val(u, x))

def choose_min(lines, x):
    return min(lines, key=lambda u: val(u, x))

def zero_roots(lines, l, r):
    roots = set()
    for i, u in enumerate(lines):
        for v in lines[i + 1:]:
            s, b = u[0] - v[0], u[1] - v[1]
            if s:
                root = -b / s
                if l < root < r:
                    roots.add(root)
    return roots

def integrate(line, l, r):
    return line[0] * (r * r - l * l) / 2 + line[1] * (r - l)

def string_line(line):
    return {'slope': str(line[0]), 'intercept': str(line[1])}

breaks = {l for l, _, _ in raw_rows} | {r for _, r, _ in raw_rows}
breaks |= {F(6, j) for j in range(6, 25) if F(1, 4) <= F(6, j) <= 1}
breaks |= {F(2, j) for j in range(2, 9) if F(1, 4) <= F(2, j) <= 1}
zero, cap = (F(0), F(0)), (F(0), F(-10))
base = sorted(breaks)
pieces, first_gain, weighted_gain, weighted_subhalf_gain = [], F(0), F(0), F(0)
for l, r in zip(base, base[1:]):
    mid = (l + r) / 2
    a, h = int(2 / mid), int(6 / mid)
    raw = next(u for lo, hi, u in raw_rows if lo <= mid < hi)
    t, z = (F(h + 1), F(-6)), (F(-a), F(2))
    head_lines = [zero, t, add(z, scale(-1, t))]
    rest_lines = [zero, add(t, scale(-1, z)), add((F(1), F(0)), scale(-1, t))]
    fine = sorted({l, r} | zero_roots(head_lines, l, r) | zero_roots(rest_lines, l, r))
    for lo, hi in zip(fine, fine[1:]):
        q = (lo + hi) / 2
        head = choose_max([zero, choose_min(head_lines[1:], q)], q)
        rest = choose_max([zero, choose_min(rest_lines[1:], q)], q)
        first_credit = add(head, rest) if lo >= F(1, 2) else zero
        weighted_credit = add(scale((a + 1) // 2, head), scale(a // 2, rest))
        old_candidates = [raw, cap]
        first_candidates = [add(raw, scale(2, first_credit)), cap]
        weighted_candidates = [add(raw, scale(2, weighted_credit)), cap]
        last = sorted({lo, hi} | zero_roots(old_candidates, lo, hi)
                      | zero_roots(first_candidates, lo, hi)
                      | zero_roots(weighted_candidates, lo, hi))
        for u, v in zip(last, last[1:]):
            q = (u + v) / 2
            old = choose_max(old_candidates, q)
            new_first = choose_max(first_candidates, q)
            new_weighted = choose_max(weighted_candidates, q)
            gf = add(new_first, scale(-1, old))
            gw = add(new_weighted, scale(-1, old))
            assert all(val(gf, end) >= 0 and val(gw, end) >= 0 for end in (u, v))
            # Every expression is affine on the complete closed interval;
            # endpoint checks prove the asserted cap/credit inequalities there.
            assert all(0 <= val(weighted_credit, end) <= F(1, 2) for end in (u, v))
            fi, wi = integrate(gf, u, v), integrate(gw, u, v)
            first_gain += fi
            weighted_gain += wi
            if v <= F(1, 2):
                weighted_subhalf_gain += wi
            pieces.append({'left': str(u), 'right': str(v), 'a': a, 'h': h,
                           'raw': string_line(raw), 'head': string_line(head),
                           'rest': string_line(rest), 'first_gain': string_line(gf),
                           'weighted_gain': string_line(gw),
                           'first_integral': str(fi), 'weighted_integral': str(wi)})

expected_first = F(16, 58905) + F(43, 2090) + F(1, 8092) + F(23, 10404) + F(1, 252)
assert first_gain == expected_first
# The exact extra M4 lies only on the a=3 head tent and is cap-hidden.
half_upper_difference = sum(F(p['weighted_integral']) - F(p['first_integral'])
                            for p in pieces if F(p['left']) >= F(1, 2))
assert half_upper_difference == 0
assert weighted_gain == first_gain + weighted_subhalf_gain
previous_joint_A = F(4624049789, 104824720)
payload = {
 'status': 'PASS', 'execution_count': 1, 'old_or_peer_execute_import_rerun_count': 0,
 'scope': 'All-n paper first-layer credit has independent proof. Weighted-cap model below x=1/2 is conditional on root NEW CRT/capacity theorem; this program does not prove that theorem or exact Smith.',
 'graph_case_count': len(graph_cases), 'graph_cases': graph_cases,
 'affine_domain': ['1/4', '1'], 'closed_affine_piece_count': len(pieces),
 'first_layer_paid_gain_exact': str(first_gain),
 'first_layer_paid_gain_decimal': float(first_gain),
 'weighted_paid_gain_exact': str(weighted_gain),
 'weighted_subhalf_gain_exact': str(weighted_subhalf_gain),
 'M4_paid_extra_on_half_to_one': str(half_upper_difference),
 'safe_A_after_first_layer_exact': str(previous_joint_A - first_gain),
 'conditional_safe_A_after_weighted_capacity_exact': str(previous_joint_A - weighted_gain),
 'small_x_gate': 'For x<=1/4, root capacity credit<=1/2 and old raw<=-4/x+2+x/4, so new raw remains below -10.',
 'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'pieces': pieces,
 'not_claimed': ['Infinite nonzero', 'Exact Smith by finite tests', 'Matched margin',
                 'Actual arithmetic cost lower bound', 'Special-value theorem', 'External Lean']
}
out.write_text(json.dumps(payload, indent=2), encoding='utf-8')
print(json.dumps({k: v for k, v in payload.items() if k not in ('graph_cases', 'pieces')}, indent=2))
