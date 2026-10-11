"""Exact fixed identities for the arithmetic K2 vertical-tame report.

No parameter search and no regulator numerics.  The Milnor K2 transfer and
resolution arguments are proved in the accompanying report, not by SymPy.
"""
from pathlib import Path
import json
import sympy as S


def zero(value):
    value = S.simplify(S.cancel(S.expand(value)))
    assert value == 0, value


def main():
    s, Y, z, r, y, lam = S.symbols('s Y z r y lam')
    a = S.sqrt(2)
    Q = s**8 - 14*s**4 + 1
    A = (s**2 + 1)*(-s**4 + 4*s**2 - 1)
    B = (s**2 - 1)*(s**4 + 4*s**2 + 1)
    up = (s**2 + a*s + 1)/(s**2 - a*s + 1)
    um = (s**2 - S.I*a*s - 1)/(s**2 + S.I*a*s - 1)
    Fp = (a*s*Y - S.I*A)/(a*s*Y + S.I*A)
    Fm = (a*s*Y - B)/(a*s*Y + B)
    fs = {'uplus': up, 'Fplus': Fp, 'uminus': um, 'Fminus': Fm}

    # Explicit pullbacks from the two elliptic-quotient formulas.
    xp, xm, yy = s + 1/s, s - 1/s, Y/s**2
    rp = S.I*xp*(6 - xp**2)/a
    rm = xm*(xm**2 + 6)/a
    zero(up - (xp + a)/(xp - a))
    zero(um - (xm - S.I*a)/(xm + S.I*a))
    zero(Fp - (yy - rp)/(yy + rp))
    zero(Fm - (yy - rm)/(yy + rm))

    actions = {}
    for name, f in fs.items():
        sigma_f = f.subs(s, -s)
        tau_f = f.subs({s: 1/s, Y: Y/s**4}, simultaneous=True)
        zero(sigma_f*f - 1)
        tau_action = 'fixed' if name.endswith('plus') else 'inverse'
        zero(tau_f - f if tau_action == 'fixed' else tau_f*f - 1)
        actions[name] = {'sigma': 'inverse', 'tau': tau_action}

    rr, yy = s**2 + s**-2, Y/s**2
    zero(yy**2 - rr**2 + 16 - (Y**2 - Q)/s**4)
    parametrized_r = 2*(lam + 1/lam)
    parametrized_y = 2*(lam - 1/lam)
    zero(parametrized_y**2 - parametrized_r**2 + 16)
    zero((parametrized_r + parametrized_y)/4 - lam)

    disc_Q = S.discriminant(Q, s)
    assert disc_Q == 2**40*3**4
    phi8 = z**4 + 1
    disc_K = S.discriminant(phi8, z)
    assert disc_K == 2**8
    phi8_factors_3 = [z**2 + z - 1, z**2 - z - 1]
    assert S.Poly(S.prod(phi8_factors_3) - phi8, z, modulus=3).is_zero
    # Both quadratic discriminants are 2 mod 3, a nonsquare, so each is
    # irreducible.  This avoids a SymPy/flint ordering issue in factor_list.
    assert all(S.discriminant(f, z) % 3 == 2 for f in phi8_factors_3)
    zero(s**8*Q.subs(s, 1/s) - Q)

    # The special fibers and an exact arithmetic node chart at residue 3.
    q3 = S.Poly(Q - (s**4 - 1)**2, s, modulus=3)
    assert q3.is_zero
    delta = s**4 - 1
    small_x, small_z = Y - delta, Y + delta
    zero(small_x*small_z - (Y**2 - Q) + 12*s**4)
    node_u, node_v = Y - s**4 + 7, Y + s**4 - 7
    zero(node_u*node_v - (Y**2 - Q) + 48)
    zero((node_v - node_u + 14)/2 - s**4)
    zero((node_u + node_v)/2 - Y)
    assert S.gcd(S.Poly(delta, s, modulus=3),
                 S.Poly(S.diff(delta, s), s, modulus=3)).degree() == 0

    A3 = S.Poly(A, s, modulus=3).as_expr()
    B3 = S.Poly(B, s, modulus=3).as_expr()
    assert A3 == -s**6 - 1
    assert B3 == s**6 - 1
    # After Y = +/- (s^4-1), the Y contribution has degree 5, whereas
    # the other contribution has degree 6 and nonzero leading coefficient.
    reduction_degrees = {
        'a_s_Y_on_each_component': 5,
        'i_A_on_each_component': 6,
        'B_on_each_component': 6,
        'uplus_numerator_and_denominator': 2,
        'uminus_numerator_and_denominator': 2,
    }
    assert S.degree(s*delta, s) == 5
    assert S.degree(A3, s) == S.degree(B3, s) == 6

    # At residue 2 the naive fiber is doubled, not a component census of a
    # regular resolution.  The report treats every char-2 residue valuation.
    assert S.Poly(Q - (s + 1)**8, s, modulus=2).is_zero
    e = S.symbols('e')
    assert S.Poly(e**4 - 1 - (e - 1)**4, e, modulus=2).is_zero

    specialization = {name: str(S.simplify(f.subs({s: 0, Y: 1})))
                      for name, f in fs.items()}
    assert specialization == {'uplus': '1', 'Fplus': '-1',
                              'uminus': '1', 'Fminus': '-1'}

    out = {
        'status': 'all fixed exact identities passed',
        'scope': ('Symbolic identities only; integral 4T=0, resolution existence, '
                  'and all-divisorial char-2 tame are mathematical proofs in the report.'),
        'curve': str(Q),
        'disc_Q': str(disc_Q),
        'disc_Q_factorization': {'2': 40, '3': 4},
        'integer_ring': 'Z[zeta_8]',
        'disc_K': str(disc_K),
        'Phi8_mod_3_factors': [str(f) for f in phi8_factors_3],
        'pullback_functions': {name: str(f) for name, f in fs.items()},
        'V4_actions': actions,
        'quotient_conic': 'y^2 = r^2 - 16',
        'conic_parameter': {'r': str(parametrized_r), 'y': str(parametrized_y)},
        'p3_fiber': 'Y = +/- (s^4 - 1)',
        'p3_nodes': 's^4 = 1, Y = 0 (four distinct residue-field-rational nodes)',
        'p3_exact_node_chart': {'u': str(node_u), 'v': str(node_v), 'uv': '-48'},
        'p3_A': str(A3),
        'p3_B': str(B3),
        'p3_generic_nonzero_degree_witnesses': reduction_degrees,
        'p2_naive_fiber': '(Y - (s+1)^4)^2 = 0',
        'specialization_s0_Y1': specialization,
    }
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print('all fixed exact identities passed:', path.name)


if __name__ == '__main__':
    main()
