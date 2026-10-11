"""Fixed exact checks for the log-moment arithmetic report; no parameter scan."""
from pathlib import Path
from fractions import Fraction
from math import comb, gcd
import hashlib
import json
import sys
import sympy as sp

sys.stdout.reconfigure(encoding='utf-8')
HERE = Path(__file__).resolve().parent
REPORT = HERE / 'odd_zeta_log_arithmetic_20261005.md'
OUT = Path(__file__).with_suffix('.json')

def valuation_integer(value, p):
    if value == 0:
        return 'infinity'
    value = abs(value)
    v = 0
    while value % p == 0:
        value //= p
        v += 1
    return v

def mod_fraction(value, p):
    assert value.denominator % p
    return value.numerator * pow(value.denominator, -1, p) % p

def data(n):
    N = 7 * n
    a = [comb(N, r) * comb(n + r, n)**7 for r in range(N + 1)]
    B = sum(a)
    T = [0] * (N + 1)
    tail = 0
    for j in range(N, 0, -1):
        tail += a[j]
        T[j] = tail
    Q = [(-1)**j * T[j] for j in range(1, N + 1)]
    assert Q[0] + B == 1
    for r in range(1, N):
        assert Q[r - 1] + Q[r] == (-1)**r * a[r]
    assert Q[N - 1] == (-1)**N * a[N]
    S = sum((Fraction(Q[j - 1], j**7) for j in range(1, N + 1)), Fraction())
    check = -sum((a[r] * sum((Fraction((-1)**(j - 1), j**7)
                     for j in range(1, r + 1)), Fraction()) for r in range(1, N + 1)), Fraction())
    assert S == check and S < 0
    M, num = S.denominator, S.numerator
    h = gcd(63 * M * B, 64 * num)
    assert gcd(M, num) == 1
    assert h <= 64 * gcd(63 * B, abs(num)) <= 64 * 63 * B
    L = 1
    for j in range(1, N + 1):
        L = L // gcd(L, j) * j
    assert L**7 % M == 0
    return {'n': n, 'degree': N, 'B': B, 'S': str(S), 'M': M,
            's': num, 'complete_content': h, 'primitive_target': 63*M*B//h,
            'primitive_rational': 64*num//h, 'tail_identity_exact': True,
            'uniform_L_N_power_clears': True}, a, T, S

kappas = []
for H in range(1, 7):
    kappa = sum((Fraction((-1)**l * sum(comb(H, v) for v in range(l, H + 1)), l**7)
                 for l in range(1, H + 1)), Fraction())
    alternate = -sum((comb(H, v) * sum((Fraction((-1)**(j-1), j**7)
                     for j in range(1, v+1)), Fraction()) for v in range(1, H+1)), Fraction())
    assert kappa == alternate and kappa < 0
    kappas.append({'H': H, 'kappa': str(kappa)})

fixed = {}
cases = []
for n in [1, 2, 3, 7]:
    record, a, T, S = data(n)
    fixed[n] = (record, a, T, S)
    cases.append(record)

local = []
for n, p in [(1, 5), (2, 11), (3, 19), (7, 19)]:
    record, a, T, S = fixed[n]
    N = 7*n
    assert sp.isprime(p) and n < p <= N and p*p > N
    H, d = divmod(N, p)
    assert p > H
    e = min(d, p-n-1)
    C = sum(comb(d, s) * comb(n+s, n)**7 for s in range(e+1))
    for r, ar in enumerate(a):
        l, s = divmod(r, p)
        expected = comb(H, l)*comb(d, s)*comb(n+s, n)**7 if s <= e else 0
        assert ar % p == expected % p
    assert record['B'] % p == pow(2, H, p)*C % p
    for l in range(1, H+1):
        assert T[l*p] % p == C*sum(comb(H, v) for v in range(l, H+1)) % p
    kappa = Fraction(kappas[H-1]['kappa'])
    assert mod_fraction(p**7*S, p) == C*mod_fraction(kappa, p) % p
    vB = valuation_integer(record['B'], p)
    vM = valuation_integer(record['M'], p)
    vs = valuation_integer(record['s'], p)
    vh = valuation_integer(record['complete_content'], p)
    assert vh == min(vM+vB+valuation_integer(63,p), vs+valuation_integer(64,p))
    assert (C % p != 0) == (vM == 7) == (vB == 0)
    local.append({'n': n, 'p': p, 'H': H, 'd': d, 'C_mod_p': C % p,
                  'B_mod_p': record['B'] % p, 'p7S_mod_p': mod_fraction(p**7*S,p),
                  'v_B': vB, 'v_M': vM, 'v_s': vs, 'v_content': vh,
                  'all_block_and_tail_identities_exact': True})

n, p = 7, 19
assert p % 16 == 3 and n == (3*p-1)//8 and n % 2
d = p-n-1
assert d % 2
reflection = sum((-1)**s * comb(d,s)**8 for s in range(d+1))
assert reflection == 0
for s in range(d+1):
    assert comb(n+s,n) % p == (-1)**s * comb(d,s) % p
assert local[-1]['v_B'] == 2 and local[-1]['v_M'] == 5 and local[-1]['v_content'] == 0

t = sp.symbols('t')
poly = (7-t)*(1+t)**7-t**8
lo = sp.Rational(5373,1000)
hi = sp.Rational(5374,1000)
flo, fhi = poly.subs(t,lo), poly.subs(t,hi)
assert flo > 0 and fhi < 0
out = {
    'status': 'fixed_exact_arithmetic_certificates_passed', 'as_of': '2026-10-05',
    'report_sha256': hashlib.sha256(REPORT.read_bytes()).hexdigest(),
    'saddle': {'polynomial': str(sp.expand(poly)), 'isolating_interval': [str(lo),str(hi)],
               'left_value': str(flo), 'right_value': str(fhi),
               'exponent_exact_definition': '7*log(7*(1+t7)/(7-t7))'},
    'kappas': kappas, 'fixed_cases': cases, 'fixed_local_checks': local,
    'reflection': {'n': n, 'p': p, 'd': d, 'integer_alternating_binomial_power_sum': reflection},
    'all_scale_claims_from_written_proof': [
        'Strict concavity and Stirling discrete Laplace asymptotics of B',
        'Integer tail-sum formula and negativity of rational S',
        'Lucas block reduction and exact top denominator layer criterion',
        'Infinite parity-reflection family of nonunit local factors',
        'Complete content valuation formula and conditional primitive lower budget'],
    'not_claimed': ['Actual denominator exponent exists or equals 49',
                    'Content has subexponential growth', 'Weighted exceptions E_n=o(n)',
                    'Endpoint I is eventually nonzero or has a specified exponent',
                    'New irrationality theorem or Lean formalization']
}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'status':out['status'],'fixed_cases':len(cases),'local_checks':len(local),
                  'reflected_prime':p}, ensure_ascii=False))
