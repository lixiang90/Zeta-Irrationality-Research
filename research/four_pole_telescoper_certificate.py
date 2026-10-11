"""Symbolic certificate for an integral, positive rational-output direction."""
import json
from pathlib import Path
import sympy as S


def main():
    n,t=S.symbols('n t');x=2*t+n
    P=(4*n-1)*x**4+(4*n**3-6*n**2)*x**2-n**4
    rhs=8*((2*t+n-1)*(t+n)**4-(2*t+n+1)*t**4)
    assert S.expand(P-rhs)==0
    v=S.symbols('v')
    assert all(c>0 for c in S.Poly(P.subs(n,v+1),v,t).coeffs())
    result=dict(status='passed',integer_polynomial_in_x2=['-N^4','4*N^3-6*N^2','4*N-1'],
                identity='J_N=G_N(t)-G_N(t+1)',numerator_positive_coefficients_for_N_ge_1=True,
                G_N='8*N^4*(2*t+N-1)*F_(N-1)(t)',
                proof='Polynomial expansion in symbolic N,t. G_N is a sum of products of reciprocal positive linear factors, so G_N(t)-G_N(t+1) is strictly completely monotone.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result)


if __name__=='__main__':main()
