"""Fixed exact Mellin/parity/Rodrigues certificates, not an irrationality test.

Only four prescribed ordinary-Rodrigues examples and three prescribed log-moment
examples.  No numerical zeta evaluation or parameter optimization.
"""
from pathlib import Path
from math import gcd, lcm
import json
import sympy as S
from sympy.functions.combinatorial.numbers import stirling


def zero(expr):
    assert S.factor(S.cancel(expr)) == 0, expr


def primitive_form(constant, coefficient):
    constant, coefficient = S.Rational(constant), S.Rational(coefficient)
    d = lcm(int(constant.q), int(coefficient.q))
    p, q = int(d*constant), int(d*coefficient)
    g = gcd(abs(p), abs(q))
    return {'constant': str(constant), 'target_coefficient': str(coefficient),
            'minimal_common_denominator': d, 'coefficient_content': g,
            'primitive_constant': p//g, 'primitive_target_coefficient': q//g,
            'actual_period_value_not_evaluated': True}


def ik_form(R, k, u):
    Q, B = S.div(R, 1+u, u)
    assert S.Poly(B, u).degree() == 0
    rat = sum(c/S.Integer(e[0]+1)**k for e, c in S.Poly(Q, u).terms())
    zeta_coefficient = B*(1-S.Rational(1,2)**(k-1))
    return S.Rational(rat), S.Rational(zeta_coefficient), S.Rational(B)


def jk_form(P, k, t):
    Q, rem = S.div(P, 1+t*t, t)
    A, B = S.Poly(rem, t).nth(0), S.Poly(rem, t).nth(1)
    rat = sum(c/S.Integer(e[0]+1)**k for e, c in S.Poly(Q, t).terms())
    zeta_coefficient = B*(S.Integer(2)**(k-1)-1)/S.Integer(2)**(2*k-1)
    return S.Rational(rat), S.Rational(A), S.Rational(zeta_coefficient)


def main():
    u, t, z = S.symbols('u t z')
    ordinary = []
    for n, A in [(1, 1), (2, 1), (3, 1), (2, 2)]:
        R = S.expand(S.diff(u**((A+1)*n)*(1-u)**n, u, n)/S.factorial(n))
        closed = sum((-1)**ell*S.binomial(n, ell)*S.binomial((A+1)*n+ell,n)
                     *u**(A*n+ell) for ell in range(n+1))
        zero(R-closed)
        assert all(c.is_Integer for c in S.Poly(R, u).all_coeffs())
        assert S.degree(R, u) == (A+1)*n
        moments = [S.factor(sum(c/S.Integer(e[0]+j+1)
                                for e,c in S.Poly(R,u).terms())) for j in range(n)]
        assert moments == [0]*n
        target = (-1)**(A*n)*sum(S.binomial(n,ell)*S.binomial((A+1)*n+ell,n)
                                    for ell in range(n+1))
        zero(R.subs(u,-1)-target)
        assert target != 0
        rat, coeff, B = ik_form(R, 7, u)
        jr, beta7, zeta7 = jk_form(t*R.subs(u,t*t),7,t)
        assert beta7 == 0
        zero(jr-rat/128)
        zero(zeta7-coeff/128)
        gr, catalan, contaminant = jk_form(R.subs(u,t*t),2,t)
        assert contaminant == 0
        zero(catalan-B)
        ordinary.append({'n':n,'A':A,'R':str(R),'degree':int(S.degree(R,u)),
                         'ordinary_moments':moments, 'R_minus_one':str(target),
                         'I7':primitive_form(rat,coeff),
                         'J7_odd_parity':primitive_form(jr,zeta7),
                         'J2_even_parity':primitive_form(gr,catalan)})

    derivatives = []
    for m,n in [(1,1),(1,3),(2,2),(6,1),(6,2),(6,3)]:
        L = -S.log(u)
        rhs = u**(-n)*sum(stirling(n,j,kind=1,signed=False)
                           *L**(m-j)/S.factorial(m-j)
                           for j in range(1,min(n,m)+1))
        zero((-1)**n*S.diff(L**m/S.factorial(m),u,n)-rhs)
        derivatives.append({'log_power':m,'derivative_order':n,'identity':'passed'})

    ug = S.symbols('ug', positive=True)
    catalan_derivatives = []
    for n in [1, 2, 3]:
        Lg = -S.log(ug)
        v = ug/(1+ug)
        rhs = ug**(-n-S.Rational(1,2))/(1+ug)*sum(
            S.rf(S.Rational(1,2),r)/S.factorial(r)
            *(Lg+sum(1/(S.Rational(1,2)+j) for j in range(r)))
            *v**(n-r) for r in range(n+1))
        lhs = (-1)**n*S.diff(ug**(-S.Rational(1,2))*Lg/(1+ug),ug,n)/S.factorial(n)
        zero(S.simplify(lhs-rhs))
        catalan_derivatives.append({'derivative_order':n,'exact_full_kernel_convolution':'passed'})

    log_moments = []
    for n,q in [(2,2),(1,6),(1,7)]:
        N=n*q
        R=sum((-1)**r*S.binomial(N,r)*S.binomial(n+r,n)**q*u**r for r in range(N+1))
        M=sum(c/(z+e[0]) for e,c in S.Poly(R,u).terms())
        C=(-1)**N*S.factorial(N)/S.factorial(n)**q
        prescribed=C*S.prod((z-j)**q for j in range(1,n+1))/S.prod(z+r for r in range(N+1))
        zero(M-prescribed)
        zeros=[]
        for j in range(n):
            for ell in range(q):
                moment=S.factor(S.factorial(ell)*sum(c/S.Integer(e[0]+j+1)**(ell+1)
                                            for e,c in S.Poly(R,u).terms()))
                assert moment == 0
                zeros.append([j,ell])
        rat,coeff,B=ik_form(R,7,u)
        tailrat,tailcoeff,_=ik_form(u**n*R,7,u)
        topfirst=S.factor(sum(c/S.Integer(e[0]+1)**7 for e,c in S.Poly(R,u).terms()))
        if q>=7:
            zero(rat-(-1)**n*tailrat)
            zero(coeff-(-1)**n*tailcoeff)
        if q==6 and n==1:
            assert topfirst == S.Rational(1,7)
            zero(rat+tailrat-topfirst)
            zero(coeff+tailcoeff)
        log_moments.append({'n':n,'q':q,'degree':N,'M_constant':str(C),
                            'M_factorized':str(prescribed),
                            'vanishing_log_moments':zeros,
                            'R_minus_one':str(B),
                            'normalized_first_toplog_moment':str(topfirst),
                            'I7':primitive_form(rat,coeff),
                            'n_order_tail_identity':q>=7,
                            'actual_nonzero_not_claimed':True})

    out={'status':'fixed_exact_identities_passed_no_parameter_scan',
         'ordinary_Rodrigues_examples':ordinary,'log_derivative_identities':derivatives,
         'Catalan_half_power_kernel_derivative_identities':catalan_derivatives,
         'root_log_moment_family_independent_checks':log_moments,
         'not_checked_by_computation':['complete-monotonicity nonzero theorem',
           'fixed-weight asymptotic Rodrigues rate',
           'positive-polynomial normalized geometric bound',
           'actual nonzero or asymptotic budget for root log-moment family',
           'any irrationality theorem']}
    path=Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2,
                              default=lambda x:int(x) if x.is_Integer else str(x)),encoding='utf-8')
    print(json.dumps({'status':out['status'],'file':str(path)},ensure_ascii=False))


if __name__=='__main__':
    main()
