"""DISTINCT FIRST-ONLY exact affine certificate; no mathematical file imports.

This program reads no old/peer MD/PY/JSON.  It has no finite-prime probes.
All formulas are literal implementations of the accompanying paper.
The exclusive JSON guard is created before the mathematical calculation.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import traceback

OUT = Path(__file__).with_suffix('.json')
with OUT.open('x', encoding='utf-8') as guard:
    json.dump({'status': 'RUNNING', 'first_only': True, 'rerun_allowed': False}, guard)


def af(m=0, b=0):
    return F(m), F(b)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[0], -a[1]


def sub(a, b):
    return add(a, neg(b))


def mul(k, a):
    return F(k) * a[0], F(k) * a[1]


def val(a, x):
    return a[0] * x + a[1]


def choose_min(items, x):
    return min(items, key=lambda a: val(a, x))


def choose_max(items, x):
    return max(items, key=lambda a: val(a, x))


def crossing(a, b):
    m, c = sub(a, b)
    return None if m == 0 else -c / m


def inside_root(cuts, lo, hi, a, b):
    x = crossing(a, b)
    if x is not None and lo < x < hi:
        cuts.add(x)


def fmt(x):
    return str(x)


RAW_LITERAL = '''
1/4 8/31 208 -72
8/31 6/23 301 -96
6/23 4/15 186 -70
4/15 3/11 276 -94
3/11 8/29 144 -62
8/29 2/7 231 -86
2/7 8/27 161 -64
8/27 3/10 242 -88
3/10 4/13 122 -56
4/13 6/19 200 -80
6/19 8/25 105 -54
8/25 1/3 180 -78
1/3 8/23 108 -52
8/23 6/17 177 -76
6/17 4/11 92 -50
4/11 3/8 158 -74
3/8 8/21 62 -42
8/21 2/5 125 -66
2/5 8/19 75 -44
8/19 3/7 132 -68
3/7 4/9 48 -36
4/9 6/13 102 -60
6/13 8/17 37 -34
8/17 1/2 88 -58
1/2 8/15 40 -32
8/15 6/11 85 -56
6/11 4/7 30 -30
4/7 3/5 72 -54
3/5 8/13 12 -22
8/13 2/3 51 -46
2/3 8/11 21 -24
8/11 3/4 54 -48
3/4 4/5 6 -16
4/5 6/7 36 -40
6/7 8/9 1 -14
8/9 1 28 -38
1 8/7 4 -12
8/7 6/5 25 -36
6/5 4/3 0 -10
4/3 3/2 18 -34
3/2 8/5 -2 -8
8/5 2 8 -24
2 8/3 -1 -4
8/3 3 8 -28
3 4 -2 -2
4 5 2 -18
5 6 12 -68
'''


def alpha(w, q, Q, lam, eta):
    # Exactly the paper's finite local prefix minimum, including Q=0/q=0.
    return min(w * r + 4 * max(0, r - 2 * q)
               + 2 * max(0, r - Q) - lam * r - eta * (r > Q)
               for r in range(2 * q + 3))


def integrate(a, lo, hi):
    return a[0] * (hi * hi - lo * lo) / 2 + a[1] * (hi - lo)


def serialize_aff(a):
    return {'slope': fmt(a[0]), 'intercept': fmt(a[1])}


def raw_at(raw, x):
    matches = [a for lo, hi, a in raw if lo < x < hi]
    assert len(matches) == 1
    return matches[0]


def data_at(x):
    Q, h, a = int(F(3) / x), int(F(6) / x), int(F(2) / x)
    c, t, rr = af(-h, 6), af(a + 1, -2), af(-Q, 3)
    return Q, h, a, c, t, rr


def branch_breaks(lo, hi):
    x = (lo + hi) / 2
    Q, h, a, c, t, rr = data_at(x)
    zero, xx = af(), af(1)
    z, carryT = af(-a, 2), af(h + 1, -6)
    pieces = [zero, c, t, rr, mul(F(1, 2), t),
              carryT, sub(z, carryT), sub(carryT, z), sub(xx, carryT)]
    cuts = {lo, hi}
    for i, aa in enumerate(pieces):
        for bb in pieces[i + 1:]:
            inside_root(cuts, lo, hi, aa, bb)
    # Every potential positive-part root is inserted before winner selection.
    for u in (c, t):
        for top in (rr, u):
            ambient = sub(sub(af(0, 2), mul(Q, u)), top)
            inside_root(cuts, lo, hi, ambient, zero)
            for ff in (u, mul(F(1, 2), t)):
                paired = add(ambient, mul(a, ff))
                inside_root(cuts, lo, hi, paired, zero)
    return sorted(cuts)


def families(raw, x):
    Q, h, a, c, t, rr = data_at(x)
    zero, xx = af(), af(1)
    rawline = raw_at(raw, x)
    carry = zero
    if F(1, 2) < x < 2:
        z, carryT = af(-a, 2), af(h + 1, -6)
        din = choose_max([zero, choose_min([carryT, sub(z, carryT)], x)], x)
        carry = mul(2, din)
        if x < 1:
            dout = choose_max([zero, choose_min([sub(carryT, z), sub(xx, carryT)], x)], x)
            carry = add(carry, mul(2, dout))
    base = [('entrycap', af(0, -10)), ('old_common_minor_carry', add(rawline, carry))]
    if x < 2:
        u = choose_min([c, t], x)
        top = choose_min([rr, u], x)
        k = sub(sub(af(0, 2), mul(Q, u)), top)
        k = choose_max([zero, k], x)
        base.append(('471_unit_sector_C_G', add(af(0, -10), mul(2, k))))
    if 3 < x < 4:
        base += [('old_jet_3_4_A', af(-2, -2)), ('old_jet_3_4_B', af(1, -13))]
    if 4 < x < 6:
        base += [('old_jet_4_6_A', af(2, -18)), ('old_jet_4_6_B', af(1, -13))]
    if F(31, 42) < x < F(3, 4):
        base.append(('471_root_weighted_paid', af(240, -184)))

    if val(c, x) <= val(t, x):
        counts = [(0, h, c), (2, h - 1, sub(t, c)), (5, h - 1, sub(xx, t))]
    else:
        counts = [(0, h, t), (3, h, sub(c, t)), (5, h - 1, sub(xx, c))]
    omega = []
    for lam in range(12):
        for eta in range(3):
            ph = sub(af(0, 2 * lam - 10), mul(2 - eta, rr))
            for w, q, count in counts:
                assert val(count, x) >= 0
                ph = add(ph, mul(alpha(w, q, Q, lam, eta), count))
            omega.append((f'lambda{lam}_eta{eta}', ph))

    pair = []
    if x < 2:
        u = choose_min([c, t], x)
        top = choose_min([rr, u], x)
        ff = mul(a, choose_min([u, mul(F(1, 2), t)], x))
        kp = add(sub(sub(af(0, 2), mul(Q, u)), top), ff)
        kp = choose_max([zero, kp], x)
        pair = [('actual_paired_unit_sector', add(af(0, -10), mul(2, kp)))]
    return (Q, h, a), base, omega, pair


def winner(items, x):
    return max(items, key=lambda item: val(item[1], x))


def merge_rows(rows):
    merged = []
    for row in rows:
        signature = tuple((k, json.dumps(v, sort_keys=True))
                          for k, v in row.items() if k not in ('lo', 'hi', 'omega_area', 'combined_area'))
        if merged and merged[-1][0] == signature and merged[-1][1]['hi'] == row['lo']:
            old = merged[-1][1]
            old['hi'] = row['hi']
            for k in ('omega_area', 'combined_area'):
                old[k] = fmt(F(old[k]) + F(row[k]))
        else:
            merged.append((signature, row.copy()))
    return [r for _, r in merged]


try:
    raw = []
    for line in RAW_LITERAL.strip().splitlines():
        lo, hi, m, b = line.split()
        raw.append((F(lo), F(hi), af(int(m), int(b))))
    assert len(raw) == 47
    assert raw[0][0] == F(1, 4) and raw[-1][1] == 6
    assert all(raw[i][1] == raw[i + 1][0] for i in range(len(raw) - 1))

    initial = {F(1, 4), F(6), F(1, 2), F(1), F(2), F(3), F(4),
               F(31, 42), F(3, 4), F(17, 24)}
    for lo, hi, _ in raw:
        initial.update((lo, hi))
    for k in (2, 3, 6):
        for j in range(1, 25):
            r = F(k, j)
            if F(1, 4) < r < 6:
                initial.add(r)
    initial = sorted(initial)
    branch_cells = []
    for lo, hi in zip(initial, initial[1:]):
        cuts = branch_breaks(lo, hi)
        branch_cells += list(zip(cuts, cuts[1:]))

    rows = []
    baseline_integral = F(0)
    gain_omega = F(0)
    gain_combined = F(0)
    exact_checks = 0
    omega_positive_support = []
    combined_positive_support = []
    for blo, bhi in branch_cells:
        midpoint = (blo + bhi) / 2
        floors, base, omega, pair = families(raw, midpoint)
        allfamilies = base + omega + pair
        # Complete pairwise affine arrangement; duplicates do not matter.
        distinct = list(dict.fromkeys(a for _, a in allfamilies))
        cuts = {blo, bhi}
        for i, aa in enumerate(distinct):
            for bb in distinct[i + 1:]:
                inside_root(cuts, blo, bhi, aa, bb)
        cuts = sorted(cuts)
        for lo, hi in zip(cuts, cuts[1:]):
            mid = (lo + hi) / 2
            bw = winner(base, mid)
            ow = winner(base + omega, mid)
            cw = winner(allfamilies, mid)
            for selected, allowed in ((bw, base), (ow, base + omega), (cw, allfamilies)):
                for _, other in allowed:
                    assert val(selected[1], lo) >= val(other, lo)
                    assert val(selected[1], hi) >= val(other, hi)
                    exact_checks += 2
            dg_o = sub(ow[1], bw[1])
            dg_c = sub(cw[1], bw[1])
            ao, ac = integrate(dg_o, lo, hi), integrate(dg_c, lo, hi)
            assert ao >= 0 and ac >= ao
            exact_checks += 2
            baseline_integral += integrate(bw[1], lo, hi)
            gain_omega += ao
            gain_combined += ac
            if ao > 0:
                omega_positive_support.append((lo, hi))
            if ac > 0:
                combined_positive_support.append((lo, hi))
            rows.append({'lo': fmt(lo), 'hi': fmt(hi), 'floors_Q_h_a2': list(floors),
                         'baseline_label': bw[0], 'baseline': serialize_aff(bw[1]),
                         'omega_label': ow[0], 'omega_bound': serialize_aff(ow[1]),
                         'combined_label': cw[0], 'combined_bound': serialize_aff(cw[1]),
                         'omega_gain': serialize_aff(dg_o), 'combined_gain': serialize_aff(dg_c),
                         'omega_area': fmt(ao), 'combined_area': fmt(ac)})

    assert rows[0]['lo'] == '1/4' and rows[-1]['hi'] == '6'
    assert all(rows[i]['hi'] == rows[i + 1]['lo'] for i in range(len(rows) - 1))
    A471 = F(45711182732576087, 1070827036198920) - F(16469, 23100) - F(1, 84)
    assert F(5, 2) - baseline_integral == A471
    # Independent paper triangle; no producer is needed for this theorem.
    assert integrate(af(-48, 34), F(2, 3), F(17, 24)) == F(1, 24)
    assert gain_omega >= F(1, 24)
    assert gain_combined >= gain_omega
    merged = merge_rows(rows)
    result = {
        'status': 'PASS', 'first_only': True, 'rerun_allowed': False,
        'producer_runs': {'new_first': 1, 'failed': 0, 'rerun': 0, 'old_peer_execution_import': 0},
        'scope': 'closed exact affine cover; no finite-prime samples; no old/peer mathematical file reads/imports',
        'domain': ['1/4', '6'], 'raw_literal_rows': 47,
        'dual_candidates': 36, 'initial_cells': len(initial) - 1,
        'branch_cells': len(branch_cells), 'arrangement_cells': len(rows),
        'merged_certificate_rows': len(merged), 'closed_endpoint_checks': exact_checks,
        'baseline_A471': fmt(A471), 'baseline_integral': fmt(baseline_integral),
        'paid_gain_omega_only': fmt(gain_omega), 'paid_gain_combined': fmt(gain_combined),
        'new_A_omega_only': fmt(A471 - gain_omega),
        'new_A_combined': fmt(A471 - gain_combined),
        'decimal_information_only': {'gain_omega': float(gain_omega), 'gain_combined': float(gain_combined),
                                     'A_omega': float(A471 - gain_omega), 'A_combined': float(A471 - gain_combined)},
        'manual_independent_gain': '1/24',
        'all_places': 'only large primes in [n/4,6n] changed; small primes and p>6n retain proven baseline bounds',
        'not_claimed': ['actual Gram Smith exactness', 'target nonzero', 'strict margin', 'special-value irrationality'],
        'closed_certificate_rows': merged,
    }
    with OUT.open('w', encoding='utf-8') as output:
        json.dump(result, output, ensure_ascii=False, indent=2)
    print(json.dumps({k: result[k] for k in ('status', 'arrangement_cells', 'merged_certificate_rows',
                                           'closed_endpoint_checks', 'paid_gain_omega_only', 'paid_gain_combined',
                                           'new_A_omega_only', 'new_A_combined', 'decimal_information_only')},
                     ensure_ascii=False))
except Exception:
    failed = {'status': 'FAILED', 'first_only': True, 'rerun_allowed': False,
              'traceback': traceback.format_exc(), 'failed_source_preserved': True}
    with OUT.open('w', encoding='utf-8') as output:
        json.dump(failed, output, ensure_ascii=False, indent=2)
    raise
