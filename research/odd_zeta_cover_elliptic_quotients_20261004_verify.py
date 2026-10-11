"""Fixed exact certificates for the three elliptic quotients.

No parameter search or numerical periods.  These identities do not establish
arithmetic integrality of a K2 class or irrationality of Catalan's constant.
"""
from pathlib import Path
import json
import sympy as S


def zero(value):
    value = S.factor(S.cancel(value))
    assert value == 0, value


def leading(poly, t):
    poly = S.Poly(S.expand(poly), t)
    exponent = min((powers[0] for powers, coefficient in poly.terms() if coefficient != 0))
    return exponent, poly.nth(exponent)


def main():
    s, x, y, t = S.symbols('s x y t')
    a = S.sqrt(2)
    Q = s**8 - 14*s**4 + 1
    assert S.gcd(Q, S.diff(Q, s)) == 1
    models = {
        'E0': {'x': s**2, 'y_factor': 1, 'quartic': x**4 - 14*x**2 + 1, 'b': 1, 'a': -14},
        'Eplus': {'x': s + 1/s, 'y_factor': 1/s**2, 'quartic': x**4 - 4*x**2 - 12, 'b': -12, 'a': -4},
        'Eminus': {'x': s - 1/s, 'y_factor': 1/s**2, 'quartic': x**4 + 4*x**2 - 12, 'b': -12, 'a': 4},
    }
    pullbacks = []
    j_values = {}
    quartic_discriminants = {}
    for name, m in models.items():
        zero(m['quartic'].subs(x, m['x']) - Q*m['y_factor']**2)
        assert S.gcd(m['quartic'], S.diff(m['quartic'], x)) == 1
        pullbacks.append(S.factor(S.diff(m['x'], s)/m['y_factor']))
        # Birational Weierstrass coordinates X=2(y+x^2)+a, Z=2xX.
        X = 2*(y + x**2) + m['a']
        Z = 2*x*X
        residual = S.expand(Z**2 - X*(X**2 - 2*m['a']*X + m['a']**2 - 4*m['b']))
        zero(S.rem(residual, S.Poly(y**2 - m['quartic'], y), y))
        A = -2*m['a']
        B = m['a']**2 - 4*m['b']
        j_values[name] = S.Rational(256)*(A*A - 3*B)**3/(B*B*(A*A - 4*B))
        quartic_discriminants[name] = S.discriminant(m['quartic'], x)
    for value, expected in zip(pullbacks, [2*s, s**2 - 1, s**2 + 1]):
        zero(value - expected)
    cotangent = S.Matrix([[0, -1, 1], [2, 0, 0], [0, 1, 1]])
    assert cotangent.det() == 4
    sigma = S.diag(-1, 1, -1)
    tau = S.Matrix([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
    assert sigma*sigma == tau*tau == S.eye(3)
    assert sigma*tau == tau*sigma
    assert S.eye(3) + sigma + tau + sigma*tau == S.zeros(3)

    eta_A = 4*s**2*(s**4 - 7)/(1 + s**4)
    eta_B = 4*(1 - 7*s**4)/(1 + s**4)
    outer_plus = 4*(x**2 + 6)/(x**2 - 2)
    outer_minus = 4*(x**2 - 6)/(x**2 + 2)
    zero(eta_A - eta_B - outer_plus.subs(x, models['Eplus']['x'])*(s**2 - 1))
    zero(eta_A + eta_B - outer_minus.subs(x, models['Eminus']['x'])*(s**2 + 1))
    zero((1 - s**2)/(1 + s**4) + S.diff(models['Eplus']['x'], s)/(models['Eplus']['x']**2 - 2))
    zero((1 + s**2)/(1 + s**4) - S.diff(models['Eminus']['x'], s)/(models['Eminus']['x']**2 + 2))

    data = {
        'Eplus': {'r': S.I*x*(6 - x**2)/a, 'u': (x + a)/(x - a), 'root': a, 'outer': outer_plus, 'C': S.I/a, 'norm': (x**2 - 2)**2*(x**2 - 6)/2},
        'Eminus': {'r': x*(x**2 + 6)/a, 'u': (x - S.I*a)/(x + S.I*a), 'root': S.I*a, 'outer': outer_minus, 'C': 1/a, 'norm': -(x**2 + 2)**2*(x**2 + 6)/2},
    }
    tame_rows = {}
    for name, d in data.items():
        f = models[name]['quartic']
        r = d['r']
        zero(f - r*r - d['norm'])
        # d log((y-r)/(y+r)) using y'=f'/(2y), y^2=f.
        logarithmic_numerator = (r*S.diff(f, x) - 2*f*S.diff(r, x))/(f-r*r)
        zero(logarithmic_numerator - d['C']*d['outer'])
        rows = []
        for xsign in [-1, 1]:
            for ysign in [-1, 1]:
                x0 = xsign*d['root']
                y0 = ysign*4*S.I
                zero(f.subs(x, x0) - y0*y0)
                assert S.simplify(S.diff(f, x).subs(x, x0)) == 0
                # Exact leading jets at each of the four nonbranch points.
                yjet = y0 + S.diff(f, x, 2).subs(x, x0)*t**2/(4*y0)
                rjet = S.expand(r.subs(x, x0+t))
                fn, fnc = leading(yjet - rjet, t)
                fd, fdc = leading(yjet + rjet, t)
                vf, lf = fn-fd, S.simplify(fnc/fdc)
                un, ud = S.fraction(d['u'])
                unv, unl = leading(un.subs(x, x0+t), t)
                udv, udl = leading(ud.subs(x, x0+t), t)
                vu, lu = unv-udv, S.simplify(unl/udl)
                tame = S.simplify(S.Integer(-1)**(vu*vf) * lu**vf/lf**vu)
                expected = (S.Integer(2) if ysign == 1 else S.Rational(1,2)) if name == 'Eplus' else (S.Rational(1,2) if ysign == 1 else S.Integer(2))
                zero(tame-expected)
                rows.append({'x': str(x0), 'y': str(y0), 'ord_u': vu, 'leading_u': str(lu), 'ord_F': vf, 'leading_F': str(lf), 'tame_symbol': str(tame)})
        tame_rows[name] = rows

    # E+ and E- are isomorphic over Q(i), but the two maps from C differ.
    zero(models['Eminus']['quartic'].subs(x, S.I*x)-models['Eplus']['quartic'])
    zero(data['Eminus']['r'].subs(x, S.I*x)-data['Eplus']['r'])
    zero(data['Eminus']['u'].subs(x, S.I*x)*data['Eplus']['u']-1)
    assert j_values == {'E0': S.Rational(35152,9), 'Eplus': S.Rational(2048,3), 'Eminus': S.Rational(2048,3)}

    result = {
        'status': 'fixed_exact_identities_passed_not_irrationality_or_arithmetic_integrality',
        'curve_polynomial': str(Q),
        'quotient_pullback_dx_over_y_coefficients': [str(z) for z in pullbacks],
        'cotangent_matrix_determinant': str(cotangent.det()),
        'V4_average_on_holomorphic_forms': 'zero',
        'j_invariants': {name: str(z) for name,z in j_values.items()},
        'quartic_discriminants': {name: str(z) for name,z in quartic_discriminants.items()},
        'elliptic_outer_kernels': {'Eplus': str(outer_plus), 'Eminus': str(outer_minus)},
        'logarithmic_norm_factors': {name: str(S.factor(d['norm'])) for name,d in data.items()},
        'tame_symbols_at_all_horizontal_u_or_F_divisors': tame_rows,
        'scope': 'Checks quotient equations, differential identities, j, and geometric tame symbols over Q(i,sqrt(2)); no vertical divisors, integral model, regulator nonzero theorem, or numerical period claim is checked.',
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ['status','j_invariants','cotangent_matrix_determinant']},ensure_ascii=False))


if __name__ == '__main__':
    main()
