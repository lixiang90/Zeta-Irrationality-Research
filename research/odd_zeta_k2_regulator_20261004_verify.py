"""Independent fixed algebra certificates for the Catalan regulator audit.

No period numerics, no parameter scan.  Transfer, Matsumoto exactness, and the
Borel--Suslin regulator theorem are mathematical inputs, not asserted by this
symbolic script.  All checks concern this one explicit curve and its paths.
"""
from pathlib import Path
import json
import sympy as S


def zero(expr):
    expr = S.factor(S.cancel(expr))
    assert S.simplify(expr) == 0, expr


def leading(expr, t):
    p = S.Poly(S.expand(expr), t)
    terms = [(e[0], c) for e, c in p.terms() if c != 0]
    e, c = min(terms)
    return int(e), c


def main():
    x, y, s, Y, t, z = S.symbols('x y s Y t z')
    a, b = S.sqrt(2), S.sqrt(3)
    s0 = a*(b-1)/2
    xp, xm, w = s+1/s, s-1/s, Y/s**2
    Q = s**8-14*s**4+1
    R = s**2+s**(-2)
    zero(R**2-16-Q/s**4)
    zero((2*(t+1/t))**2-16-(2*(t-1/t))**2)
    zero(((2*(t+1/t)+2*(t-1/t))/4)-t)
    zero(xp.subs(s, -s)+xp)
    zero(xm.subs(s, -s)+xm)
    zero(xp.subs(s, 1/s)-xp)
    zero(xm.subs(s, 1/s)+xm)
    zero((Y/s**4)/(1/s)**2-w)

    sigma = S.diag(-1, 1, -1)
    tau = S.Matrix([[0, 0, -1], [0, -1, 0], [-1, 0, 0]])
    assert sigma*tau == tau*sigma
    assert S.eye(3)+sigma+tau+sigma*tau == S.zeros(3)

    models = {
        'plus': {'f': x**4-4*x**2-12,
                 'u': (x+a)/(x-a), 'r': S.I*x*(6-x**2)/a,
                 'root': a, 'correction_sign': -1},
        'minus': {'f': x**4+4*x**2-12,
                  'u': (x-S.I*a)/(x+S.I*a), 'r': x*(x**2+6)/a,
                  'root': S.I*a, 'correction_sign': 1},
    }
    rows, asymptotic = {}, {}
    v = (y-4*S.I)/(y+4*S.I)
    for name, m in models.items():
        u, r, f = m['u'], m['r'], m['f']
        F = (y-r)/(y+r)
        zero(u*u.subs(x, -x)-1)
        zero(F*F.subs(x, -x)-1)
        zero(F*F.subs(y, -y)-1)
        zero(v.subs(x, -x)-v)
        zero(f+16-(x**2-(2 if name == 'plus' else -2))**2)
        # These two distinct infinity branches agree on the unit limits.
        inf_y = z**(-2)+(-2 if name == 'plus' else 2)
        asymptotic[name] = {
            'u': str(S.limit(u.subs(x, 1/z), z, 0)),
            'F': str(S.limit(F.subs({x: 1/z, y: inf_y}), z, 0)),
            'v': str(S.limit(v.subs(y, inf_y), z, 0)),
        }
        assert asymptotic[name] == {'u': '1', 'F': '-1', 'v': '1'}
        local_rows = []
        for sx in [-1, 1]:
            for sy in [-1, 1]:
                x0, y0 = sx*m['root'], sy*4*S.I
                zero(f.subs(x, x0)-y0**2)
                zero(S.diff(f, x).subs(x, x0))
                yjet = y0+S.diff(f, x, 2).subs(x, x0)*t**2/(4*y0)
                rjet = S.expand(r.subs(x, x0+t))
                fn, fc = leading(yjet-rjet, t)
                fd, fdc = leading(yjet+rjet, t)
                ordF, leadF = fn-fd, S.simplify(fc/fdc)
                un, ud = S.fraction(u)
                unv, unl = leading(un.subs(x, x0+t), t)
                udv, udl = leading(ud.subs(x, x0+t), t)
                ordu, leadu = unv-udv, S.simplify(unl/udl)
                tameS = S.simplify(S.Integer(-1)**(ordu*ordF)*leadu**ordF/leadF**ordu)
                vn, vc = leading(yjet-4*S.I, t)
                vd, vdc = leading(yjet+4*S.I, t)
                ordv = vn-vd
                assert ordv == 2*sy
                tame_const = S.Integer(2)**ordv
                tame_corrected = S.simplify(tameS**2*tame_const**m['correction_sign'])
                assert tame_corrected == 1
                local_rows.append({'x': str(x0), 'y': str(y0), 'ord_u': ordu,
                                   'ord_F': ordF, 'ord_v': ordv,
                                   'tame_S': str(tameS),
                                   'tame_corrected': str(tame_corrected)})
        rows[name] = local_rows

    zero(xp.subs(s, s0)-a*b)
    zero(xm.subs(s, s0)+a)
    zero(Q.subs(s, s0))
    zero(models['plus']['u'].subs(x, a*b)-(2+b))
    zero(models['minus']['u'].subs(x, -a)-S.I)
    # Fplus is 0/0 in x,y coordinates, so use the curve's branch parameter y=t.
    fplus = models['plus']['f']
    x0 = a*b
    assert S.diff(fplus, x).subs(x, x0) != 0
    xjet = x0+t**2/S.diff(fplus, x).subs(x, x0)
    rjet = models['plus']['r'].subs(x, xjet)
    Fplus_limit = S.simplify(S.limit((t-rjet)/(t+rjet), t, 0))
    assert Fplus_limit == 1
    rminus_end = models['minus']['r'].subs(x, -a)
    assert rminus_end != 0
    assert S.simplify((-rminus_end)/rminus_end) == -1
    assert v.subs(y, 0) == -1

    # Galois point actions used in the finite-chain endpoint argument.
    a_flip_s0 = -a*(b-1)/2
    b_flip_s0 = a*(-b-1)/2
    zero(a_flip_s0+s0)
    zero(b_flip_s0*s0+1)
    # Both signs of sqrt(2) invert u and F, so their wedge is unchanged.
    aa = S.symbols('aa', nonzero=True)
    for u_generic in [(x+aa)/(x-aa), (x-S.I*aa)/(x+S.I*aa)]:
        zero(u_generic*u_generic.subs(aa, -aa)-1)
    rr = S.symbols('rr')
    Fgeneric = (y-rr)/(y+rr)
    zero(Fgeneric*Fgeneric.subs(rr, -rr)-1)

    # Generic real/imaginary decomposition, with all formal variables real.
    A, psi, B, phi, dA, dpsi, dB, dphi = S.symbols(
        'A psi B phi dA dpsi dB dphi', real=True)
    imaginary = S.im((A+S.I*psi)*(dB+S.I*dphi)).expand()
    eta = A*dphi-B*dpsi
    boundary_derivative = B*dpsi+psi*dB
    zero(imaginary-eta-boundary_derivative)

    # Boundary matrix of gamma, iota gamma, iota sigma gamma, sigma gamma.
    # Rows Pplus, Pminus, Bplus, Bminus; all paths retain their original orientation.
    boundary = S.Matrix([[-1, 0, 0, -1],
                         [0, -1, -1, 0],
                         [1, 1, 0, 0],
                         [0, 0, 1, 1]])
    closed = S.Matrix([1, -1, 1, -1])
    assert boundary*closed == S.zeros(4, 1)
    eta_signs = S.Matrix([[1, -1, -1, 1]])
    assert (eta_signs*closed)[0] == 0

    out = {
        'status': 'fixed_exact_algebra_passed_no_period_numerics',
        'V4_average_holomorphic_matrix': (S.eye(3)+sigma+tau+sigma*tau).tolist(),
        'quotient': {'R': str(R), 'W': str(w), 'equation': 'W^2=R^2-16',
                    'parameter': '(R+W)/4'},
        'corrected_symbols': {'plus': '2{uplus,Fplus}-{2,v}',
                              'minus': '2{uminus,Fminus}+{2,v}',
                              'v': '(y-4i)/(y+4i)'},
        'corrected_tame_jets': rows,
        'infinity_unit_limits': asymptotic,
        'endpoint': {'s0': str(s0), 'xplus': 'sqrt(6)', 'xminus': '-sqrt(2)',
                     'uplus': '2+sqrt(3)', 'uminus': 'i',
                     'Fplus': str(Fplus_limit), 'Fminus': '-1', 'v': '-1'},
        'galois_point_actions': {'aFlip': 'sigma(B)', 'bFlip': 'sigma*tau(B)'},
        'real_boundary_identity': 'Im(log(u)dlog(F))=eta(u,F)+d(arg(u)log|F|)',
        'closed_chain': {'coefficients': list(closed),
                         'boundary': list(boundary*closed),
                         'eta_integral_multiple': int((eta_signs*closed)[0])},
        'not_computationally_checked': [
            '4T=0 from transfer, Bass-Tate, and specialization',
            'existence of a finite Steinberg/Bloch chain from Matsumoto exactness',
            'actual value of the open integral from the frozen Catalan identity',
            'full Borel--Suslin regulator injectivity',
            'any arithmetic-model integrality or irrationality claim'],
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(out, ensure_ascii=False, indent=2,
                                 default=lambda q: int(q) if q.is_Integer else str(q)),
                      encoding='utf-8')
    print(json.dumps({'status': out['status'], 'output': str(output)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
