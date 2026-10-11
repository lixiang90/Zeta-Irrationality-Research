"""Exact obstruction to target-preserving symmetric seeds of degree <= 6.

All computations are over Q. These are finite-degree algebraic certificates,
not an irrationality proof or a claim about seeds of unbounded degree.
"""
import json
from pathlib import Path
import sympy as s

x,a,b,c,d,e,f=s.symbols('x a b c d e f')
t=lambda z:z*(z+1)


def equations(w,u):
    return s.Poly(s.expand(1-(1+3*x*x)*w(x-1)*w(x)
                  -x**5*(u(x)*w(x-1)-u(x-1)*w(x))),x).coeffs()


def main():
    w4=lambda z:1+a*t(z)+b*t(z)**2
    u4=lambda z:c*t(z)+d
    G4=s.groebner(equations(w4,u4),a,b,c,d)
    for identity in (a-3,b,2*c-6*d+27):
        assert G4.reduce(identity)[1]==0

    w6=lambda z:1+a*t(z)+b*t(z)**2+c*t(z)**3
    product=s.Poly(s.expand(w6(x-1)*w6(x)),x)
    e2=product.coeff_monomial(x**2)
    e4=product.coeff_monomial(x**4)
    bvalue=(a-3)*(a+1)/2
    assert s.expand((e2+3).subs(b,bvalue))==0
    necessary=s.factor((e4-9).subs(b,bvalue))
    assert s.expand(necessary-(a-3)*(a**3-5*a*a-a-8*c+13)/4)==0

    u6=lambda z:d*t(z)**2+e*t(z)+f
    special=lambda z:1+3*t(z)+c*t(z)**3
    Gspecial=s.groebner(equations(special,u6),c,d,e,f,order='grevlex')
    # Every field-valued solution has c=0 since c^2 lies in the ideal.
    assert Gspecial.reduce(c*c)[1]==0
    assert Gspecial.reduce(2*d-3*c)[1]==0
    assert Gspecial.reduce(2*c+2*e-6*f+27)[1]==0
    general=lambda z:1+a*t(z)+bvalue*t(z)**2+(a**3-5*a*a-a+13)*t(z)**3/8
    Ggeneral=s.groebner(equations(general,u6),a,d,e,f,order='grevlex')
    assert list(Ggeneral)==[s.S.One]
    result=dict(scope='target-preserving symmetric polynomial seeds of degree <= 6',
                quartic_basis=[str(v) for v in G4],
                local_factorization=str(necessary),
                sextic_special_basis=[str(v) for v in Gspecial],
                sextic_special_c_squared_remainder='0',
                sextic_general_basis=['1'],
                conclusion='Only w=1+3*x*(x+1); the proper rational correction is 9/(2*w).')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
