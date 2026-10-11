"""Validated position-dependent relative-norm exponent for W=D_N^8.

Full proof in stability_parameter_analysis.md. For alpha=N/K, eta=h/K,
rho > max_[a,b] V + sup_s (R_alpha(s)+2 eta acosh(Y_s)) implies
||G^-1/2 B G^-1/2|| <= exp(rho K), eventually.

R_alpha is strictly concave, allowing certified tangent upper bounds.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from flint import arb,ctx

ctx.prec=160


def A(q):
    q=F(q)
    return arb(q.numerator)/arb(q.denominator)


def xlog(q):
    return arb(0) if not q else A(q)*A(abs(q)).log()


def log_integral(c,s):
    return xlog(c+s)+xlog(c-s)-2*A(c)


def residue_rate(alpha,s):
    return 8*log_integral(alpha,s)-log_integral(F(1),s)


def residue_derivative(alpha,s):
    return 8*(A(s+alpha)/A(s-alpha)).log()-(A(1+s)/A(1-s)).log()


def legendre(eta,a,b,s):
    y=A((2*s*s+a+b)/(b-a))
    return 2*A(eta)*(y+(y*y-1).sqrt()).log()


def field(alpha,t):
    s=A(t).sqrt()
    def J(c):
        return A(c)*(A(t)+A(c)**2).log()-2*A(c)+2*s*(A(c)/s).atan()
    return 2*arb.pi()*s+J(F(1))-8*J(alpha)


def certify(alpha,eta,a,b,rho):
    # For 0<alpha<1, beta=8, V has a unique minimum, so endpoint max suffices.
    va,vb=field(alpha,a),field(alpha,b)
    vmax=va if va>vb else vb if vb>va else (va+vb+abs(va-vb))/2
    stack=[(alpha,F(1))];intervals=[];maximum=arb(-1000)
    while stack:
        l,r=stack.pop();m=(l+r)/2
        # Concavity: R(s)<=R(m)+R'(m)(s-m). Legendre term increases in s.
        bound=vmax+residue_rate(alpha,m)+abs(residue_derivative(alpha,m))*(A(r-l)/2)+legendre(eta,a,b,r)
        if bound<A(rho):
            intervals.append(dict(left=str(l),right=str(r),upper=str(bound)))
            if bound.mid()>maximum.mid():maximum=bound
        else:
            assert r-l>F(1,10**12),'rho too small or precision insufficient'
            stack.extend([(l,m),(m,r)])
        assert len(intervals)+len(stack)<20000
    intervals.sort(key=lambda z:F(z['left']))
    assert F(intervals[0]['left'])==alpha and F(intervals[-1]['right'])==1
    assert all(x['right']==y['left'] for x,y in zip(intervals,intervals[1:]))
    return dict(alpha=str(alpha),eta=str(eta),a=str(a),b=str(b),rho=str(rho),
                certified_upper_max=str(maximum),subintervals=len(intervals),
                necessary_decay_ceiling=str(eta*rho/2),intervals=intervals,
                status='rigorous asymptotic norm exponent, not an arithmetic gain')


if __name__=='__main__':
    rows=[]
    for alpha,b,rho in [(F(1,40),F(1049,5000),F(1127,125)),
                        (F(3,40),F(2771,10000),F(9269,1000)),
                        (F(1,8),F(3541,10000),F(9437,1000))]:
        r=certify(alpha,1-alpha,F(1,10**6),b,rho);rows.append(r)
        print(json.dumps({k:v for k,v in r.items() if k!='intervals'}),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
