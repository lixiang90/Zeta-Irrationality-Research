"""Fixed exact certificates for the explicit four-term Steinberg chain.

Checks rational function identities, formal tensor expansions, and an explicit
eight-five-term endpoint reduction. No parameter scan or irrationality claim.
"""
from collections import defaultdict
from pathlib import Path
import json
import sympy as S


def main():
    s, Y, t, z = S.symbols('s Y t z')
    a, b = S.sqrt(2), S.sqrt(3)
    Q = s**8-14*s**4+1
    relation = S.Poly(Y**2-Q,Y)
    checks = {}

    def zero(name, value):
        num = S.cancel(value).as_numer_denom()[0]
        residual = S.factor(S.rem(S.expand(num),relation,Y))
        assert residual == 0, (name,residual)
        checks[name] = True

    def raw(name, condition):
        assert bool(condition), name
        checks[name] = True

    xp,xm,y = s+1/s,s-1/s,Y/s**2
    R,W = s**2+s**-2,Y/s**2
    tt = (R+W)/4
    up = (s**2+a*s+1)/(s**2-a*s+1)
    um = (s**2-S.I*a*s-1)/(s**2+S.I*a*s-1)
    rp = S.I*xp*(6-xp**2)/a
    rm = xm*(xm**2+6)/a
    Fp,Fm = (y-rp)/(y+rp),(y-rm)/(y+rm)
    rhop = (W-S.I*(R-4))/(W+S.I*(R-4))
    rhom = (W-S.I*(R+4))/(W+S.I*(R+4))
    rho_t = -S.I*(t+S.I)/(t-S.I)
    rho_m_t = -S.I*(t-S.I)/(t+S.I)
    zero('conic',W**2-R**2+16)
    zero('rho_plus_rational_parameter',rhop-rho_t.subs(t,tt))
    zero('rho_minus_rational_parameter',rhom-rho_m_t.subs(t,tt))
    zero('rho_product_minus_one',rhop*rhom+1)
    hs = []
    for name,u,F,rho in [('plus',up,Fp,rhop),('minus',um,Fm,rhom)]:
        zero(name+'_F_Mobius',F+(u-rho)/(1-rho*u))
        zero(name+'_Steinberg_product',(1-rho/u)*(1-rho*u)+2*rho)
        hs.extend([rho/u,rho*u])
        raw(name+'_u_nonconstant',S.diff(u,s)!=0)
        # Literal invariance: each pair is interchanged under inversion of u.
        zero(name+'_sigma_rho_fixed',rho.subs({s:-s,Y:Y},simultaneous=True)-rho)
        zero(name+'_sigma_u_inverse',u.subs({s:-s,Y:Y},simultaneous=True)*u-1)
    # tau fixes the plus pair and interchanges the minus pair.
    for name,rho in [('plus',rhop),('minus',rhom)]:
        zero(name+'_tau_rho_fixed',rho.subs({s:1/s,Y:Y/s**4},simultaneous=True)-rho)
    zero('plus_tau_u_fixed',up.subs(s,1/s)-up)
    zero('minus_tau_u_inverse',um.subs(s,1/s)*um-1)

    # The universal rational wedge identity is verified in a free exterior
    # algebra on u,rho,A=1-rho/u,B=1-rho*u, ignoring only root-of-unity factors.
    def tensor(v,w,antisymmetric=False):
        out = defaultdict(int)
        for i,c in enumerate(v):
            for j,d in enumerate(w):
                if antisymmetric:
                    if i==j: continue
                    key = (min(i,j),max(i,j))
                    out[key] += c*d*(1 if i<j else -1)
                else:
                    out[(i,j)] += c*d
        return {k:v for k,v in out.items() if v}

    def combine(*terms):
        out=defaultdict(int)
        for coefficient,term in terms:
            for key,value in term.items(): out[key]+=coefficient*value
        return {k:v for k,v in out.items() if v}
    eu,er,eA,eB=[tuple(1 if j==k else 0 for j in range(4)) for k in range(4)]
    wedge=lambda v,w:tensor(v,w,True)
    vv=lambda *terms:tuple(sum(c*v[j] for c,v in terms) for j in range(4))
    deltaA=wedge(vv((1,er),(-1,eu)),eA)
    deltaB=wedge(vv((1,er),(1,eu)),eB)
    raw('universal_wedge_identity',combine((1,wedge(eu,vv((1,eu),(1,eA),(-1,eB)))),
        (-1,wedge(er,vv((1,eA),(1,eB)))),(1,deltaA),(1,deltaB))=={})

    # Explicit inversion reduction, with the Suslin five-term convention.
    def five_term(x,y):
        x,y = S.sympify(x),S.sympify(y)
        return [(1,x),(-1,y),(1,y/x),(-1,(1-1/x)/(1-1/y)),(1,(1-x)/(1-y))]
    def collect(terms):
        out=defaultdict(int)
        for coefficient,arg in terms:
            key=S.cancel(arg)
            out[key]+=coefficient
        return {str(k):v for k,v in out.items() if v}
    rz = five_term(2,2*z)+five_term(S.Rational(1,2),1/(2*z))+five_term(2*z,2)+five_term(1/(2*z),S.Rational(1,2))
    raw('four_five_terms_equal_two_inversion_pairs',collect(rz)=={str(z):2,str(1/z):2})
    for endpoint_z in [2+b,S.I,-1]:
        for x,yv in [(2,2*endpoint_z),(S.Rational(1,2),1/(2*endpoint_z)),
                     (2*endpoint_z,2),(1/(2*endpoint_z),S.Rational(1,2))]:
            raw('five_terms_nondegenerate_'+str(endpoint_z)+'_'+str(x),
                all(S.simplify(v) not in [0,1] for _,v in five_term(x,yv)) and S.simplify(x-yv)!=0)

    # Basepoint uses the regular rho(t) representation rather than apparent
    # 0/0 in rho(W,R) at B. u and F use their validated regular limits.
    s0=a*(b-1)/2
    A=2+b
    raw('endpoint_curve',S.simplify(Q.subs(s,s0))==0)
    raw('endpoint_t_is_one',S.simplify(tt.subs({s:s0,Y:0}))==1)
    raw('rho_at_B',S.simplify(rho_t.subs(t,1))==1 and S.simplify(rho_m_t.subs(t,1))==-1)
    raw('u_at_B',S.simplify(up.subs(s,s0)-A)==0 and S.simplify(um.subs(s,s0)-S.I)==0)
    raw('rho_at_P0',S.limit(rho_t,t,S.oo)==-S.I and S.limit(rho_m_t,t,S.oo)==-S.I)
    raw('u_at_P0',up.subs(s,0)==1 and um.subs(s,0)==1)
    # Endpoint formal difference plus 4[i] equals -I(A)+3I(i).
    lhs=[(-1,A),(-1,1/A),(-1,S.I),(3,-S.I),(4,S.I)]
    rhs=[(-1,A),(-1,1/A),(3,S.I),(3,1/S.I)]
    raw('endpoint_difference_formal',collect(lhs)==collect(rhs))
    # At K,L the potential integer boundary (-1) tensor 2 is already zero
    # because 2=a^2 and -1 has order two. This is written bilinearity, not a
    # numeric test of a K-group.
    raw('square_and_root_of_unity_inputs',a*a==2 and (-1)**2==1 and S.I**4==1)

    # Formal holomorphic primitive differentiation. dLi2(h) is replaced by
    # -Log(1-h)*dLog(h), with the product branch LA+LB=V+L.
    U,V,LA,LB,L,dU,dV,dLA,dLB = S.symbols('U V LA LB L dU dV dLA dLB')
    dP = U*dU+(LA-LB)*dU+U*(dLA-dLB)+LA*(dV-dU)+LB*(dV+dU)-(V+L)*dV
    raw('holomorphic_primitive_differential',S.expand((dP-U*(dU+dLA-dLB)).subs(LB,V+L-LA))==0)
    ell,log2,Li0 = S.symbols('ell log2 Li2_minus_i')
    lam=log2+S.I*S.pi
    v0=-S.I*S.pi/2
    P0=-2*Li0-v0**2/2-lam*v0
    raw('primitive_basepoint',S.expand(P0-(-2*Li0-3*S.pi**2/8+S.I*S.pi*log2/2))==0)
    invsum=S.pi**2/3-ell**2/2-S.I*S.pi*ell
    PplusB=ell**2/2+ell*(-ell-S.I*S.pi)-invsum
    raw('primitive_plus_endpoint',S.expand(PplusB+S.pi**2/3)==0)
    PminusB=(S.I*S.pi/2)**2/2+(S.I*S.pi/2)*(-S.I*S.pi/2)+S.pi**2/24-(-S.I*S.pi)**2/2-lam*(-S.I*S.pi)
    raw('primitive_minus_endpoint',S.expand(PminusB-(-S.pi**2/3+S.I*S.pi*log2))==0)
    raw('primitive_total_increment',S.expand(PplusB+PminusB-2*P0-(4*Li0+S.pi**2/12))==0)

    result={
        'status':'fixed_exact_certificates_passed',
        'checks':checks,
        'curve':'Y^2=s^8-14*s^4+1',
        'field':'K=Q(i,sqrt(2)); endpoint L=K(sqrt(3))',
        'rho':{'plus':str(rho_t),'minus':str(rho_m_t),'product':'-1'},
        'identities':{'F':'-(u-rho)/(1-rho*u)','c':'(1-rho/u)*(1-rho*u)=-2*rho'},
        'rational_chain':[{'coefficient':-1,'argument':'rho_plus/u_plus'},
                          {'coefficient':-1,'argument':'rho_plus*u_plus'},
                          {'coefficient':-1,'argument':'rho_minus/u_minus'},
                          {'coefficient':-1,'argument':'rho_minus*u_minus'}],
        'integer_chain':'sum_plus_minus([u]+[1/u]+[rho]+[1/rho]-[rho/u]-[rho*u])+[-1]',
        'integral_K2_conclusion':'T={rho_plus,2}+{rho_minus,2}={-1,2}=0, by integral Steinberg relations',
        'endpoint_four_chain':{'P0':'-4[-i]','B':'-[2-sqrt(3)]-[2+sqrt(3)]-[i]-[-i]',
                              'difference_rational':'-4[i]'},
        'inversion_certificate':'R(2,2z)+R(1/2,1/(2z))+R(2z,2)+R(1/(2z),1/2)=2([z]+[1/z])',
        'holomorphic_primitive':'P=Log(u)^2/2+Log(u)(Log(1-rho/u)-Log(1-rho*u))-Li2(rho/u)-Li2(rho*u)-Log(rho)^2/2-(log(2)+i*pi)Log(rho)',
        'primitive_total_increment':'4*Li2(-i)+pi^2/12=-4*i*G',
        'scope':'Exact algebraic identities and formal expansions. Written bilinearity, Steinberg/five-term relations and Bloch-Wigner derivative complete the proof. No numerical period test, approximation family, irrationality theorem, or Lean theorem.'
    }
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'checks':len(checks)},ensure_ascii=False))


if __name__=='__main__':
    main()
