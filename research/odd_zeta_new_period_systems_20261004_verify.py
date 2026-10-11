"""Exact identities for the Borwein--Bradley binomial tail lift.

No numerical zeta values, parameter scans, or irrationality assumptions are used.
The literature identity identifying the connection value is an external theorem.
"""
from pathlib import Path
import json
import sympy as s


def harmonic(n, weight):
    return sum((s.Rational(1, k**weight) for k in range(1, n + 1)), s.S.Zero)


def valuation(q, prime):
    q = s.Rational(q)
    a, b = abs(int(q.p)), int(q.q)
    result = 0
    while a and a % prime == 0:
        result += 1
        a //= prime
    while b % prime == 0:
        result -= 1
        b //= prime
    return result


def main():
    z, c, w = s.symbols('z c w')
    cutoff = 12
    summands = [s.S.Zero]
    partial = [s.S.Zero]
    forcing = [s.S.Zero]
    lifted = [c]
    for n in range(1, cutoff + 1):
        h = harmonic(n - 1, 4)
        t = (-1)**(n - 1) * (s.Rational(1, n**4) + 5*h) / (n**3 * s.binomial(2*n, n))
        summands.append(t)
        partial.append(partial[-1] + s.Rational(5, 2)*t)
        forcing.append((-1)**n * (s.Rational(1, n**6) + 5*h/n**2))
        lifted.append(s.binomial(2*n, n)*(c - partial[n]))
    recurrence_checks = []
    for n in range(1, cutoff + 1):
        residual = s.expand(n*lifted[n] - (4*n - 2)*lifted[n - 1] - s.Rational(5, 2)*forcing[n])
        assert residual == 0
        recurrence_checks.append(n)

    # Basis order f,V,U,Li4,Li3,Li2,Li1,1.  The derivative matrix
    # has one nonzero superdiagonal, making the cyclic rows triangular.
    matrix = s.zeros(8)
    matrix[0, 0] = 2*z/(1 - 4*z)
    matrix[0, 1] = s.Rational(5, 2)/(1 - 4*z)
    matrix[1, 2] = 1
    matrix[2, 3] = (1 - 4*z)/(1 + z)
    matrix[3, 4] = matrix[4, 5] = matrix[5, 6] = 1
    matrix[6, 7] = -z/(1 + z)
    rows = []
    row = s.zeros(1, 8)
    row[0, 0] = 1
    for order in range(8):
        rows.append(row)
        assert all(row[0, col] == 0 for col in range(order + 1, 8))
        if order < 7:
            row = (z*row.diff(z) + row*matrix).applyfunc(s.cancel)
    cyclic = s.Matrix.vstack(*rows)
    pivots = [s.factor(cyclic[j, j]) for j in range(8)]
    determinant = s.factor(s.prod(pivots))
    expected = -5**7*z/(2**7*(1 - 4*z)**2*(1 + z)**6)
    assert s.cancel(determinant - expected) == 0

    # Direct Taylor checks of theta U=((1-4z)/(1+z))*Li4 and theta V=U.
    u = [s.S.Zero] + [(-1)**n*(s.Rational(1, n**5) + 5*harmonic(n - 1, 4)/n) for n in range(1, cutoff + 1)]
    v = forcing
    li4 = [s.S.Zero] + [s.Rational((-1)**n, n**4) for n in range(1, cutoff + 1)]
    d = [1] + [5*(-1)**n for n in range(1, cutoff + 1)]
    for n in range(1, cutoff + 1):
        assert n*v[n] == u[n]
        assert n*u[n] == sum((d[j]*li4[n-j] for j in range(n+1)), s.S.Zero)

    prime_certificates = []
    for p in [2, 3, 5, 7, 11]:
        vp = valuation(v[p], p)
        assert vp == -6
        prime_certificates.append({'p': p, 'forcing_coefficient': str(v[p]), 'valuation': vp})

    prime_power_certificates = []
    for p, power in [(2, 2), (2, 3), (3, 2)]:
        n = p**power
        vp = valuation(v[n], p)
        assert vp == -6*power
        prime_power_certificates.append({'p': p, 'power': power, 'n': n, 'valuation': vp})
    prefix_certificates = []
    prefix_v = prefix_constant = lcm_n = 1
    for n in range(1, cutoff+1):
        lcm_n = int(s.ilcm(lcm_n, n))
        prefix_v = int(s.ilcm(prefix_v, int(v[n].q)))
        constant = s.Rational(lifted[n].subs(c, 0))
        prefix_constant = int(s.ilcm(prefix_constant, int(constant.q)))
        assert prefix_v == lcm_n**6
        assert (2*lcm_n**7) % prefix_constant == 0
        assert lifted[n].diff(c) == s.binomial(2*n, n)
        prefix_certificates.append({'N': n, 'delta_V': str(prefix_v), 'equals_L_N_power_6': True, 'delta_f_constant_divides_2_L_N_power_7': True})

    # Finite coefficient checks of the parameter recurrence for the full
    # Borwein--Bradley family; w is the fourth-power parameter, not z.
    parameter_rows = []
    bb = {}
    koecher = {}
    def truncated_product(left, right):
        return [sum((left[j]*right[k-j] for j in range(k+1)), s.S.Zero) for k in range(3)]

    for n in range(1, 9):
        base = s.Rational((-1)**(n-1), n**3*s.binomial(2*n, n))
        bb_product = [base, base/n**4, base/n**8]
        koecher_product = [base, base/n**2, base/n**4]
        for j in range(1, n):
            bb_product = truncated_product(bb_product, [1, s.Rational(5, j**4), s.Rational(5, j**8)])
            koecher_product = truncated_product(koecher_product, [1, s.Rational(-1, j**2), 0])
        bb[n] = sum((bb_product[j]*w**j for j in range(3)), s.S.Zero)
        koecher[n] = sum((koecher_product[j]*w**j for j in range(3)), s.S.Zero)
    for n in range(2, 9):
        bb_residual = 2*(n-1)*(2*n-1)*(n**4 - w)*bb[n] + n**2*((n-1)**4 + 4*w)*bb[n-1]
        koecher_residual = 2*(n-1)*(2*n-1)*(n**2-w)*koecher[n] + ((n-1)**2-w)**2*koecher[n-1]
        assert all(s.expand(bb_residual).coeff(w, j) == 0 for j in range(3))
        assert all(s.expand(koecher_residual).coeff(w, j) == 0 for j in range(3))
        parameter_rows.append(n)

    result = {
        'status': 'exact_identities_passed_not_irrationality_proof',
        'cutoff': cutoff,
        'uses_numerical_zeta_values': False,
        'lift_recurrence_checked_n': recurrence_checks,
        'closed_polylog_system_taylor_checked_n': list(range(1, cutoff+1)),
        'basis_order': ['f', 'V', 'U', 'Li4(-z)', 'Li3(-z)', 'Li2(-z)', 'Li1(-z)', '1'],
        'cyclic_pivots': [str(x) for x in pivots],
        'cyclic_determinant': str(determinant),
        'cyclic_determinant_expected': str(s.factor(expected)),
        'prime_prefix_lower_bound_samples': prime_certificates,
        'prime_power_lower_bound_samples': prime_power_certificates,
        'prefix_denominator_identity_checks': prefix_certificates,
        'parameter_recurrences': {
            'parameter_orders': [0, 1, 2],
            'BB_checked_n': parameter_rows,
            'Koecher_checked_n': parameter_rows,
        },
        'lifted_coefficients': [str(s.expand(x)) for x in lifted[:5]],
        'scope': 'Exact algebra only; connection identity, slit analyticity, and functional independence have separate proofs in the Markdown report.',
    }
    destination = Path(__file__).with_suffix('.json')
    destination.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ['status', 'cutoff', 'cyclic_determinant']}, ensure_ascii=False))


if __name__ == '__main__':
    main()
