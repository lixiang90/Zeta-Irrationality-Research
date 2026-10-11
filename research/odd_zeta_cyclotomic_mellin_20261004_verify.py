"""Fixed exact certificates for the elementary cyclotomic Mellin family.

No parameter optimization or scan.  The all-scale prime-window and positivity
theorems are proved in the Markdown report; these fixed cases check signs,
normalizations, residue formulas, and exact rational positivity budgets.
"""
from fractions import Fraction as F
from math import comb, factorial, gcd, lcm
from pathlib import Path
import json
import sympy as S


def vp(x, p):
    x = F(x)
    if x == 0:
        return None
    result = 0
    numerator, denominator = abs(x.numerator), x.denominator
    while numerator % p == 0:
        result += 1
        numerator //= p
    while denominator % p == 0:
        result -= 1
        denominator //= p
    return result


def mod_fraction(x, p):
    x = F(x)
    assert x.denominator % p
    return (x.numerator % p)*pow(x.denominator % p, -1, p) % p


def log_bounds(q, count):
    q = F(q)
    y = (q - 1)/(q + 1)
    assert 0 <= y < 1
    lower = 2*sum((y**(2*j + 1)/F(2*j + 1) for j in range(count)), F(0))
    upper = lower + 2*y**(2*count + 1)/(F(2*count + 1)*(1 - y*y))
    return lower, upper


def make_quadratic_case(a, b, n, k, prime_witnesses):
    t = S.symbols('t')
    P = t**(a*n)*(1 - t)**(b*n)
    Q, remainder = S.div(S.Poly(P, t), S.Poly(1 + t*t, t))
    A, B = int(remainder.nth(0)), int(remainder.nth(1))
    assert S.expand(S.I**(a*n)*(1 - S.I)**(b*n)) == A + S.I*B
    R = sum((F(int(Q.nth(m)), (m + 1)**k)
             for m in range(max(0, Q.degree()) + 1)), F(0))
    degree = (a + b)*n
    assert Q.degree() <= degree - 2
    safe = lcm(*range(1, degree))**k
    assert safe % R.denominator == 0
    assert (A == 0) != (B == 0)
    target = 'beta' if B == 0 else 'zeta'
    if target == 'beta':
        assert A == (-1)**(((2*a - b)*n)//4)*2**(b*n//2)
        Dk, Ck, target_integer = 1, 1, A
    else:
        assert B == (-1)**(((2*a - b)*n - 2)//4)*2**(b*n//2)
        Dk, Ck, target_integer = 2**(2*k - 1), 2**(k - 1) - 1, B
    M, r = R.denominator, R.numerator
    q, p_num = M*target_integer*Ck, -Dk*r
    content = gcd(abs(q), abs(p_num))
    assert content <= Dk*abs(target_integer*Ck)
    for m in range(a*n):
        expected = (-1)**(m//2 + 1)*(A if m % 2 == 0 else B)
        assert int(Q.nth(m)) == expected
    residues = []
    for p, h in prime_witnesses:
        assert S.isprime(p)
        assert F(degree, h + 1) < p < F(a*n, h)
        assert p*p > degree and p > h
        if target == 'beta':
            partial = sum((F((-1)**((j - 1)//2), j**k)
                           for j in range(1, h + 1, 2)), F(0))
            predicted = (-1)**((p + 1)//2)*A*partial
        else:
            partial = sum((F((-1)**(j//2), j**k)
                           for j in range(2, h + 1, 2)), F(0))
            predicted = B*partial
        residue = mod_fraction(p**k*R, p)
        assert residue == mod_fraction(predicted, p) != 0
        assert vp(R, p) == -k
        residues.append({'p': p, 'h': h, 'v_p_R': -k,
                         'residue_p_to_k_R': residue,
                         'fixed_partial_sum': str(partial)})
    return {'a': a, 'b': b, 'n': n, 'k': k, 'target': target,
            'degree_P': degree, 'A': A, 'B': B, 'R': str(R),
            'M_den_R': str(M), 'integer_content': str(content),
            'gcd_bound': str(Dk*abs(target_integer*Ck)),
            'prime_window_witnesses': residues}


def make_parity_case():
    u, t = S.symbols('u t')
    a, b, n, k, p, h = 2, 1, 6, 7, 11, 1
    Rpoly = u**(a*n)*(1 - u)**(b*n)
    Squot, remainder = S.div(S.Poly(Rpoly, u), S.Poly(1 + u, u))
    B = int(remainder.nth(0))
    assert B == (-1)**(a*n)*2**(b*n)
    rational = sum((F(int(Squot.nth(j)), (j + 1)**k)
                    for j in range(Squot.degree() + 1)), F(0))
    P = t*Rpoly.subs(u, t*t)
    Q, rem_t = S.div(S.Poly(P, t), S.Poly(1 + t*t, t))
    assert rem_t.nth(0) == 0 and int(rem_t.nth(1)) == B
    assert S.expand(Q.as_expr() - t*Squot.as_expr().subs(u, t*t)) == 0
    original_rational = sum((F(int(Q.nth(m)), (m + 1)**k)
                            for m in range(Q.degree() + 1)), F(0))
    assert original_rational == rational/2**k
    degree = (a + b)*n
    assert lcm(*range(1, degree + 1))**k % rational.denominator == 0
    assert F(degree, h + 1) < p < F(a*n, h)
    assert vp(rational, p) == -k
    partial = sum((F((-1)**j, j**k) for j in range(1, h + 1)), F(0))
    assert mod_fraction(p**k*rational, p) == mod_fraction(B*partial, p) != 0
    Ck, Dk = 2**(k - 1) - 1, 2**(k - 1)
    M, r = rational.denominator, rational.numerator
    content = gcd(abs(M*B*Ck), abs(Dk*r))
    assert content <= Dk*abs(B*Ck)
    return {'a': a, 'b': b, 'n': n, 'k': k, 'degree_R': degree,
            'degree_P': 2*degree + 1, 'B': B,
            'rational_in_2_to_k_J': str(rational), 'M': str(M),
            'content': str(content), 'p': p, 'h': h, 'v_p_R': -k}


def main():
    cases = [
        make_quadratic_case(1, 1, 4, 2, []),
        make_quadratic_case(1, 1, 2, 7, []),
        make_quadratic_case(4, 1, 4, 2, [(11, 1), (7, 2)]),
        make_quadratic_case(4, 1, 10, 7, [(17, 2), (13, 3)]),
    ]
    parity = make_parity_case()
    log2_lower, _ = log_bounds(2, 3)
    _, log3_upper = log_bounds(3, 10)
    _, log5_upper = log_bounds(5, 12)
    assert log2_lower > F(693, 1000)
    assert log3_upper < F(1099, 1000)
    assert log5_upper < F(161, 100)
    zeta_budget_lower = F(35, 12) - 5*F(161, 100) + F(15, 2)*F(693, 1000)
    beta_budget_lower = F(23, 6) - 5*F(161, 100) + F(15, 2)*F(693, 1000)
    parity_budget_lower = F(7, 2) - 3*F(1099, 1000) + F(693, 1000)
    assert zeta_budget_lower == F(77, 1200) > 0
    assert beta_budget_lower == F(1177, 1200) > 0
    assert parity_budget_lower == F(112, 125) > 0

    # One fixed exact coefficient check for the all-degree Rodrigues proof.
    t, N = S.symbols('t'), 7
    LD = S.legendre(N, 2*t - 1)
    rodrigues = S.diff(t**N*(t - 1)**N, t, N)/factorial(N)
    assert S.expand(LD - rodrigues) == 0
    assert S.Poly(LD, t).LC() == comb(2*N, N)
    assert S.integrate(t**N*LD, (t, 0, 1)) == F(1, (2*N + 1)*comb(2*N, N))

    result = {'status': 'all fixed exact certificates passed',
              'scope': 'No parameter scan; all-scale statements are proofs in the report.',
              'quadratic_kernel_cases': cases, 'parity_kernel_case': parity,
              'strict_rational_budget_lower_bounds': {
                  'beta_k2_at_a_over_b_4': str(beta_budget_lower),
                  'zeta_k7_at_a_over_b_4': str(zeta_budget_lower),
                  'parity_zeta_k7_at_a_over_b_2': str(parity_budget_lower)},
              'log_bounds': {'log2_lower': str(log2_lower),
                             'log3_upper': str(log3_upper),
                             'log5_upper': str(log5_upper)},
              'Legendre_fixed_certificate_degree': N}
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('all fixed exact certificates passed:', path.name)


if __name__ == '__main__':
    main()
