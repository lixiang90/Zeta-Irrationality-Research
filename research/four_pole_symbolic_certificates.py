"""Exact polynomial certificates proving baseline nondegeneracy for every n.

These identities, together with shift invariance of aggregate pole coefficients,
give the proof in four_pole_fixed_window_analysis.md. No guessed recurrence is
accepted without a rational-function identity.
"""
import json
from pathlib import Path
import sympy as S


def certificates():
    n,t=S.symbols('n t',nonzero=True)
    beta=2*(2*n+1)*(3*n*n+3*n+1)
    gamma=4*n*(4*n-1)*(4*n+1)
    # F_n(t+1)/F_n(t)=t^4/(t+n+1)^4.
    P=(75*n**6+15*n**5+3*n**4+n**3
       +(260*n**5+8*n**4-12*n**3)*t
       +(374*n**4-10*n**3-24*n**2)*t**2
       +(276*n**3-16*n)*t**3
       +(104*n**2+10*n-4)*t**4+(16*n+4)*t**5)/n**3
    rhs=(n+1)**7-beta*(t+n+1)**4-gamma*(t+n)**4*(t+n+1)**4/n**4
    assert S.expand(t**4*P.subs(t,t+1)-(t+n+1)**4*P-rhs)==0
    alpha=-n*n/5
    b=4*n*(4*n-1)/5
    p=(4*t+10*n-4)/(5*n**3)
    assert S.expand(t**4*p.subs(t,t+1)-(t+n)**4*p-((2*t+n)**2-alpha-b*(t+n)**4/n**4))==0
    # W_n=V_n U_{n-1}-V_{n-1} U_n; D_n=b_n W_n.
    ratio=S.factor((b/b.subs(n,n-1))*(-gamma.subs(n,n-1)/n**3))
    wanted=-4*(4*n-1)*(4*n-3)/n**2
    assert S.simplify(ratio-wanted)==0
    # D_1=48; the closed form is (-1)^(n+1)*4*(4n)!/((2n)!*n!^2).
    factorial_ratio=-S.prod(4*n-j for j in range(4))/((2*n)*(2*n-1)*n*n)
    assert S.simplify(ratio-factorial_ratio)==0
    return dict(status='passed',recurrence_certificate=str(P),moment_certificate=str(p),
                determinant_ratio=str(ratio),determinant_initial=48,
                determinant_closed_form='(-1)^(n+1)*4*binomial(4*n,2*n)*binomial(2*n,n)',
                scope='Polynomial identities in symbolic n,t; not finite interpolation.')


if __name__=='__main__':
    result=certificates()
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result)
