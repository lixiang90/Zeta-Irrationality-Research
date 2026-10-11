"""Exact fixed-prime certificate for the low-degree square lift.

Reads the frozen excellent-ratio certificate.  Verifies complete polynomials,
not finite Taylor jets: curvature mod p^2, H|E, factor lift, log derivative,
unit denominators and degree bounds.  No target scanning or new height claim.
"""
from pathlib import Path
import hashlib,json
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'research/cdt_odd_level20_frobenius_20261006_verify.json'
t=sp.Symbol('t'); CHECKS=[]
def check(label, value):
    assert value,label
    CHECKS.append(label)
def theta(expr):return sp.expand(t*sp.diff(expr,t))
def integral_poly(expr):return sp.Poly(sp.expand(expr),t,domain=sp.ZZ)
def divisible(poly,n):return all(int(x)%n==0 for x in poly.all_coeffs())
def lift(poly):return sum((int(poly.nth(i))%poly.get_modulus())*t**i for i in range(poly.degree()+1))

def run(sample):
    p=sample['prime']; G=integral_poly(sum(c*t**i for i,c in enumerate(sample['ratio_polynomial_mod_p3'])))
    P=sp.Poly(G.as_expr(),t,modulus=p); H=sp.gcd(P,P.diff()).monic(); B=P.exquo(H**2)
    h=H.degree(); b=B.degree(); H0=lift(H); B0=lift(B); P0=integral_poly(B0*H0**2)
    Delta=1-12*t+28*t**2-32*t**3+16*t**4; J=(1-t)*Delta
    hnum=theta(Delta)*(1-t)/2-t*Delta
    Tnum=-8*t*(18*t**4-36*t**3+28*t**2-10*t+1)
    def curvature_num(g):return integral_poly(J*(2*g*theta(theta(g))-theta(g)**2)+2*hnum*g*theta(g)+Tnum*g*g)
    RG=curvature_num(G.as_expr()); RP0=curvature_num(P0.as_expr())
    check(f'p{p}_full_polynomial_curvature_modp2',divisible(RG,p*p))
    check(f'p{p}_base_curvature_divisible_H0_squared',RP0.rem(integral_poly(H0**2)).is_zero)
    check(f'p{p}_base_curvature_p_saturated_divisibility',divisible(RP0,p) and integral_poly(RP0.as_expr()/p).rem(integral_poly(H0**2)).is_zero)
    check(f'p{p}_Hasse_multiplicities',sp.gcd(H,H.diff()).degree()==0 and sp.gcd(B,H).degree()==0)
    check(f'p{p}_branch_factor_degree',b<=4 and sp.Poly(Delta,t,modulus=p).rem(B).is_zero)
    check(f'p{p}_generic_H_away_from_cusp_and_branch',sp.gcd(H,sp.Poly(t*Delta,t,modulus=p)).degree()==0)
    diff=G-P0; check(f'p{p}_E_numerator_divisible_p',divisible(diff,p))
    E=integral_poly(diff.as_expr()/p); Ef=sp.Poly(E.as_expr(),t,modulus=p)
    linear=integral_poly((RG-RP0).as_expr()/p)
    residue=sp.Poly(linear.as_expr(),t,modulus=p).rem(H)
    expected=sp.Poly(4*J*B.as_expr()*theta(H.as_expr())**2*Ef.as_expr(),t,modulus=p).rem(H)
    check(f'p{p}_linearization_residue',residue==expected)
    check(f'p{p}_generic_multiplier_unit',sp.gcd(H,sp.Poly(4*J*B.as_expr()*theta(H.as_expr())**2,t,modulus=p)).degree()==0)
    check(f'p{p}_E_divisible_H',Ef.rem(H).is_zero)
    E1=Ef.exquo(H)
    H1=(E1*sp.invert(2*B,H)).rem(H)
    B1=(E1-2*B*H1).exquo(H)
    hh=H0+p*lift(H1); bb=B0+p*lift(B1)
    product=integral_poly(bb*hh**2)
    check(f'p{p}_square_factor_lift_modp2',divisible(G-product,p*p))
    check(f'p{p}_H1_degree',H1.is_zero or H1.degree()<h)
    check(f'p{p}_B1_degree',B1.is_zero or B1.degree()<=b+3)
    check(f'p{p}_lift_unit_constants',int(integral_poly(bb).nth(0))%p!=0 and int(integral_poly(hh).nth(0))%p!=0)
    log_cross=integral_poly(G.as_expr()*theta(product.as_expr())-product.as_expr()*theta(G.as_expr()))
    check(f'p{p}_global_logderivative_congruence_modp2',divisible(log_cross,p*p))
    actual_d0=4+integral_poly(bb).degree()+integral_poly(hh).degree()
    safe_d0=h+b+7; safe_delta2=2*safe_d0+5
    check(f'p{p}_safe_degree_bound',actual_d0<=safe_d0 and safe_delta2==3*p+b+16 and safe_delta2<=3*p+20)
    check(f'p{p}_low_order2_top_coordinate_modp_nonzero',int(integral_poly(bb*hh).nth(0))%p!=0)
    return {'prime':p,'P_degree':P.degree(),'H_degree':h,'B_degree':b,
            'E_mod_H_zero':True,'H1_coefficients':[int(H1.nth(i))%p for i in range(max(0,H1.degree())+1)],
            'B1_coefficients':[int(B1.nth(i))%p for i in range(max(0,B1.degree())+1)],
            'lift_H_degree':integral_poly(hh).degree(),'lift_B_degree':integral_poly(bb).degree(),
            'actual_low_D0_degree':actual_d0,'safe_low_order2_degree':safe_delta2,
            'actual_degree_based_order2_bound':2*actual_d0+5}

if __name__=='__main__':
    data=json.loads(INPUT.read_text(encoding='utf-8'))
    samples=[run(s) for s in data['samples']]
    out={'scope':'all-polynomial square lift and coefficient-degree inputs only; full-prime proof and source/height limits in report',
         'input_certificate':str(INPUT),'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
         'checks_passed':len(CHECKS),'check_labels':CHECKS,'samples':samples}
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_passed':len(CHECKS),'certificate':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False))
