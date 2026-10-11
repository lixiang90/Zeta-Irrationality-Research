"""Exact function-field certificates for the degeneration of the fixed K2 symbol.

This checks the algebraic inputs of the proof, not Milnor K2 transfer theorems.
No parameter scan, numerical period, or claimed integral-model verification.
"""
from pathlib import Path
import json
import sympy as S


def main():
    s, Y, t = S.symbols('s Y t')
    a = S.sqrt(2)
    Q = s**8 - 14*s**4 + 1
    relation = S.Poly(Y**2 - Q, Y)

    def zero(expr):
        numerator = S.cancel(expr).as_numer_denom()[0]
        remainder = S.rem(S.expand(numerator), relation, Y)
        assert S.factor(remainder) == 0, S.factor(remainder)

    def act(expr, image_s, image_Y):
        return expr.subs({s: image_s, Y: image_Y}, simultaneous=True)

    xplus, xminus, y = s + 1/s, s - 1/s, Y/s**2
    uplus = (s**2+a*s+1)/(s**2-a*s+1)
    uminus = (s**2-S.I*a*s-1)/(s**2+S.I*a*s-1)
    # Multiplication by a*s^3 cancels all coordinate poles at the basepoint.
    Fplus = (a*s*Y+S.I*(s**2+1)*(s**4-4*s**2+1))/(a*s*Y-S.I*(s**2+1)*(s**4-4*s**2+1))
    Fminus = (a*s*Y-(s**2-1)*(s**4+4*s**2+1))/(a*s*Y+(s**2-1)*(s**4+4*s**2+1))
    rplus = S.I*xplus*(6-xplus**2)/a
    rminus = xminus*(xminus**2+6)/a
    zero(Fplus-(y-rplus)/(y+rplus))
    zero(Fminus-(y-rminus)/(y+rminus))

    maps = {'sigma': (-s, Y), 'tau': (1/s, Y/s**4), 'delta': (S.I*s, Y), 'iota': (s, -Y)}
    for name, (ss, yy) in maps.items():
        zero(yy**2-Q.subs(s, ss))
    for u, F in [(uplus,Fplus),(uminus,Fminus)]:
        zero(act(u,*maps['sigma'])*u-1)
        zero(act(F,*maps['sigma'])*F-1)
        zero(act(u,*maps['iota'])-u)
        zero(act(F,*maps['iota'])*F-1)
    zero(act(uplus,*maps['tau'])-uplus)
    zero(act(Fplus,*maps['tau'])-Fplus)
    zero(act(uminus,*maps['tau'])*uminus-1)
    zero(act(Fminus,*maps['tau'])*Fminus-1)
    zero(act(uplus,*maps['delta'])-uminus)
    zero(act(Fplus,*maps['delta'])-Fminus)
    zero(act(uminus,*maps['delta'])*uplus-1)
    zero(act(Fminus,*maps['delta'])*Fplus-1)

    R, W = s**2+s**-2, Y/s**2
    zero(W**2-R**2+16)
    for name in ['sigma','tau']:
        zero(act(R,*maps[name])-R)
        zero(act(W,*maps[name])-W)
    t_expr = (R+W)/4
    zero(R-2*(t_expr+1/t_expr))
    zero(W-2*(t_expr-1/t_expr))
    zero(s**4-R*s**2+1)
    zero(Y-W*s**2)
    zero(act(t_expr,*maps['iota'])-1/t_expr)

    basepoint = {'uplus':uplus, 'uminus':uminus, 'Fplus':Fplus, 'Fminus':Fminus}
    base_values = {}
    for name, expr in basepoint.items():
        numerator, denominator = S.cancel(expr).as_numer_denom()
        nv, dv = numerator.subs({s:0,Y:1}), denominator.subs({s:0,Y:1})
        assert nv != 0 and dv != 0
        value = S.simplify(nv/dv)
        expected = 1 if name.startswith('u') else -1
        assert value == expected
        base_values[name] = str(value)

    # At every s^4=-1 point, the elliptic x coordinates have x+^2=2,
    # x-^2=-2 and the same y; neither degree-two map is ramified there.
    def zero_mod_log_points(expr):
        num = S.cancel(expr).as_numer_denom()[0]
        assert S.rem(S.Poly(num,s), S.Poly(s**4+1,s)).as_expr() == 0
    zero_mod_log_points(xplus**2-2)
    zero_mod_log_points(xminus**2+2)
    assert S.gcd(s**4+1, s**2-1) == 1
    assert S.gcd(s**4+1, s**2+1) == 1
    tame_pairs = [{'y':'4*i','plus':'2','minus':'1/2','product':'1'},
                  {'y':'-4*i','plus':'1/2','minus':'2','product':'1'}]
    # Symbolic inverse identities used here are integral bilinearity,
    # {u^-1,F^-1}={u,F}; the JSON records but does not computer-prove K2.
    result = {
        'status':'exact_function_field_inputs_passed',
        'curve':'Y^2=s^8-14*s^4+1',
        'coefficient_field':'Q(i,sqrt(2))',
        'symbol_action':{'sigma':{'Splus':'Splus','Sminus':'Sminus'},
                         'tau':{'Splus':'Splus','Sminus':'Sminus'},
                         'delta':{'Splus':'Sminus','Sminus':'Splus'},
                         'iota':{'Splus':'-Splus','Sminus':'-Sminus'}},
        'V4_quotient':{'R':str(R),'W':str(W),'equation':'W^2=R^2-16',
                       'parameter':'t=(R+W)/4','inverse_R':'2*(t+1/t)',
                       'inverse_W':'2*(t-1/t)','degree':'4, by four distinct automorphisms and quartic for s'},
        'basepoint':{'s':'0','Y':'1','unit_residues':base_values},
        'horizontal_tame_pullback_pairs':tame_pairs,
        'theorem_not_computationally_checked':'Rost integral transfer/basechange and residue compatibility, Bass-Tate exact sequence and specialization imply 4*T=0.',
        'not_claimed':['T=0 integrally','nonzero elliptic regulator','period irrationality','arithmetic-model verification']
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'unit_residues':base_values},ensure_ascii=False))


if __name__ == '__main__':
    main()
