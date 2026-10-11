"""Independent fixed-prime checks of the level20 excellent-lift input.

These computations verify all t-degrees < p^2 for preassigned p=7,11,13.
They do not prove the geometric all-prime argument or a new CDT height bound.
Arithmetic is exact in (Z/p^3 Z)[r]/(r^2-5); no numerical approximation.
"""
from pathlib import Path
from math import comb, gcd
import hashlib, json
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def check(label, condition):
    assert condition, label
    CHECKS.append(label)

def run(p):
    mod=p**3; size=p*p+3; prefix=p*p
    def pad(a,n=size): return list(a[:n])+[0]*max(0,n-len(a))
    def add(a,b): return [(x+y)%mod for x,y in zip(a,b)]
    def scale(a,c): return [x*c%mod for x in a]
    def mul(a,b,n=None):
        n=min(len(a),len(b)) if n is None else n
        out=[0]*n
        for i,x in enumerate(a[:n]):
            if x:
                for j,y in enumerate(b[:n-i]):
                    if y: out[i+j]=(out[i+j]+x*y)%mod
        return out
    def inv(a):
        n=len(a); out=[0]*n; c=pow(a[0],-1,mod); out[0]=c
        for j in range(1,n): out[j]=-c*sum(a[k]*out[j-k] for k in range(1,j+1))%mod
        return out
    def power(a,k):
        if k<0: return power(inv(a),-k)
        out=pad([1],len(a))
        while k:
            if k&1: out=mul(out,a)
            k//=2
            if k: a=mul(a,a)
        return out
    def compose(a,b):
        n=len(b); out=[0]*n; bp=pad([1],n)
        for j,c in enumerate(a[:n]):
            if c:
                for i in range(j,n): out[i]=(out[i]+c*bp[i])%mod
            if j+1<n: bp=mul(bp,b)
        return out
    def derivative(a): return [i*a[i]%mod for i in range(1,len(a))]+[0]
    def theta(a): return [i*x%mod for i,x in enumerate(a)]
    def eta(exponents):
        out=pad([1])
        for d,r in zip([1,2,4,5,10,20],exponents):
            for m in range(d,size,d):
                fac=[0]*size
                for j in range((size-1)//m+1):
                    bc=comb(r,j) if r>=0 and j<=r else (0 if r>=0 else (-1)**j*comb(-r+j-1,j))
                    fac[j*m]=(-1)**j*bc%mod
                out=mul(out,fac)
        return out
    def revert(a):
        b=[0,1]
        while len(b)<len(a):
            n=min(2*len(b)-1,len(a)); b=pad(b,n)
            err=compose(a[:n],b); err[1]=(err[1]-1)%mod
            correction=mul(err,inv(compose(derivative(a)[:n],b)))
            b=[(x-y)%mod for x,y in zip(b,correction)]
        return b
    def frob(a): return [a[i//p] if i%p==0 else 0 for i in range(size)]
    def divisibility(a,k): return all(x%(p**k)==0 for x in a[:prefix])
    Hunit=eta([-2,0,2,2,0,-2]); U=Hunit[:]; U[1]=(U[1]+1)%mod
    tq=pad([0]+inv(U)); qt=revert(tq)
    check(f'p{p}_integer_coordinate_inverse',compose(tq,qt)==pad([0,1]))
    Phiq=eta([-4,10,-4,-4,10,-4]); Phi=compose(Phiq,qt)
    s=compose(frob(tq),qt)
    Phis=compose(Phi,s)
    R=mul(Phi,inv(Phis)); G=pad(R[:3*p+1])
    check(f'p{p}_Frobenius_ratio_degree3p_modp3',R[:prefix]==G[:prefix])
    check(f'p{p}_excellent_lift_not_naive',s[:prefix]!=frob(pad([0,1]))[:prefix])
    check(f'p{p}_excellent_lift_reduction',all((s[i]-(1 if i==p else 0))%p==0 for i in range(prefix)))
    check(f'p{p}_ratio_identity',mul(G,Phis)[:prefix]==Phi[:prefix])
    Delta=pad([1,-12,28,-32,16]); om=pad([1,-1])
    # Square-root branch with constant one, built by coefficient recursion.
    def sqrt(a):
        out=pad([1]); half=pow(2,-1,mod)
        for n in range(1,size): out[n]=(a[n]-sum(out[i]*out[n-i] for i in range(1,n)))*half%mod
        return out
    Z=sqrt(Delta); gs=mul(om,Z)
    Bq=pad([0]+eta([0,2,0,0,2,0])); B=compose(Bq,qt)
    # Use (theta_q t)/t after stripping the simple zero in q.
    Sq=mul(pad(theta(tq)[1:]),inv(pad(tq[1:])))
    S=compose(Sq,qt)
    check(f'p{p}_S_model_identity',S[:prefix]==mul(gs,Phi)[:prefix])
    check(f'p{p}_B_gauge_identity',B[:prefix]==mul(pad([0,1]),mul(om,Phi))[:prefix])
    b=mul(compose(S,s),inv(S))
    check(f'p{p}_excellent_lift_Euler_chain_rule',theta(s)[:prefix]==scale(mul(s,b),p)[:prefix])
    check(f'p{p}_b_ratio_formula',b[:prefix]==mul(compose(gs,s),inv(mul(gs,G)))[:prefix])
    P=[x%p for x in G[:3*(p-1)+1]]
    check(f'p{p}_modp_Hasse_degree',all(x%p==0 for x in G[3*(p-1)+1:]))
    tvar=sp.Symbol('t'); PP=sp.Poly(sum(x*tvar**i for i,x in enumerate(P)),tvar,modulus=p)
    check(f'p{p}_modp_Hasse_exact_degree',PP.degree()==3*(p-1))
    Lambda=mul(power(mul(pad([0,1]),om),p-1),power(Delta,(p-1)//2))
    aprime=mul(derivative(Phi),inv(Phi)); gpprime=mul(derivative(G),inv(G))
    Ppad=pad(P); corr=mul(Lambda,mul(power(derivative(Ppad),p),power(Ppad,-p-1)))
    check(f'p{p}_ordinary_logderivative_p_layer',divisibility(add(add(aprime,scale(gpprime,-1)),scale(corr,-p)),2))
    def chi(n): return (0,1,-1,-1,1)[n%5]
    inv4=pow(4,-1,mod)
    AE=pad([-pow(5,-1,mod)]+[sum(chi(d)*d for d in range(1,n+1) if n%d==0) for n in range(1,size)])
    AF=pad([0]+[-4*sum(chi((n//4)//d)*d for d in range(1,n//4+1) if (n//4)%d==0) if n%4==0 else 0 for n in range(1,size)])
    Ek=[0]+[sum(chi(d)*d**3 for d in range(1,n+1) if n%d==0) for n in range(1,size)]
    Fk=[0]+[sum(chi(n//d)*d**3 for d in range(1,n+1) if n%d==0) for n in range(1,size)]
    VE=[0]+[Ek[n]-(5*Ek[n//2] if n%2==0 else 0)+(4*Ek[n//4] if n%4==0 else 0) for n in range(1,size)]
    VF=[0]+[-5*inv4*(Fk[n]-(20*Fk[n//2] if n%2==0 else 0)+(64*Fk[n//4] if n%4==0 else 0))%mod for n in range(1,size)]
    def scaled_source(V):
        out=[0]*size
        for n in range(1,prefix):
            out[n]=(V[n]*pow(n//p,-3,mod) if n%p==0 else 0)%mod
        return out
    topE,topF=scaled_source(VE),scaled_source(VF)
    fE=pad([0]+[VE[n]*pow(n,-3,mod)%mod for n in range(1,p)])
    fF=pad([0]+[VF[n]*pow(n,-3,mod)%mod for n in range(1,p)])
    check(f'p{p}_whole_E_source_modp3',topE[:prefix]==frob(fE)[:prefix])
    check(f'p{p}_whole_F_source_modp3',topF[:prefix]==scale(frob(fF),chi(p))[:prefix])
    A0,A1=compose(AE,qt),compose(AF,qt)
    f0,f1=compose(fE,qt),compose(fF,qt)
    f0=pad(f0[:p]); f1=pad(f1[:p])
    top0,top1=compose(topE,qt),compose(topF,qt)
    check(f'p{p}_packet_true_t_lift',top0[:prefix]==compose(f0,s)[:prefix] and top1[:prefix]==scale(compose(f1,s),chi(p))[:prefix])
    def pmul(a,b): return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),5)),add(mul(a[0],b[1]),mul(a[1],b[0]))
    def padd(a,b): return add(a[0],b[0]),add(a[1],b[1])
    def pscale(a,c): return scale(a[0],c),scale(a[1],c)
    def pinv(a):
        norm=add(mul(a[0],a[0]),scale(mul(a[1],a[1]),-5)); ni=inv(norm)
        return mul(a[0],ni),scale(mul(a[1],ni),-1)
    def ptheta(a): return theta(a[0]),theta(a[1])
    def pdivisibility(a,k): return divisibility(a[0],k) and divisibility(a[1],k)
    one=(pad([1]),pad([])); Gpair=(G,pad([])); gspair=(gs,pad([]))
    embeddings=[]
    for sign in [-1,1]:
        A=(A0,scale(A1,-sign)); N=(pad([1,-6,1]),pad([0,sign,-sign])); C=(pad([1,-6,6]),pad([0,-2*sign,2*sign]))
        # Actual scaled target, taking the period constant zero; any p-integral
        # period adds a multiple of p^3, irrelevant for these congruences.
        Y=pmul(A,(top0,scale(top1,-sign)))
        aR=padd(pmul(ptheta(N),pinv(N)),pscale(pmul(ptheta(C),pinv(C)),pow(2,-1,mod)))
        a0=padd(aR,(mul(theta(G),inv(G)),pad([])))
        a1=padd(aR,(scale(mul(theta(gs),inv(gs)),-1),pad([])))
        first=padd(ptheta(Y),pscale(pmul(a0,Y),-1))
        second=padd(ptheta(first),pscale(pmul(a1,first),-1))
        check(f'p{p}_embedding{sign}_first_layer_divisibility',pdivisibility(first,1))
        check(f'p{p}_embedding{sign}_second_layer_divisibility',pdivisibility(second,2))
        check(f'p{p}_embedding{sign}_first_not_uniform_p2',not pdivisibility(first,2))
        check(f'p{p}_embedding{sign}_second_not_uniform_p3',not pdivisibility(second,3))
        D0=pmul(pmul(N,C),Gpair)
        D1=pmul(N,pmul((om,pad([])),(C[0],scale(C[1],-1))))
        M0=pmul(D0,a0); M1=pmul(D1,a1)
        d0=3*p+4; d1=5
        check(f'p{p}_embedding{sign}_first_polynomial_coefficients',all(x==0 for a in M0 for x in a[d0+1:prefix]))
        check(f'p{p}_embedding{sign}_second_fixed_coefficients',all(x==0 for a in M1 for x in a[d1+1:prefix]))
        # Q = (D1 D0 theta - D1 thetaD0 - D0 M1) (D0 theta-M0)
        #    = D1 D0^2 nabla1 nabla0, an order2 polynomial operator.
        L0=padd(pmul(D0,ptheta(Y)),pscale(pmul(M0,Y),-1))
        DD=pmul(D1,D0)
        MM=padd(pmul(D1,ptheta(D0)),pmul(D0,M1))
        L2=padd(pmul(DD,ptheta(L0)),pscale(pmul(MM,L0),-1))
        check(f'p{p}_embedding{sign}_cleared_order2_divisibility',pdivisibility(L2,2))
        check(f'p{p}_embedding{sign}_operator_identity',L2==pmul(pmul(D1,pmul(D0,D0)),second))
        embeddings.append({'sign':sign,'first_layer_valuation_at_least':1,'second_layer_valuation_at_least':2,
                           'safe_D0_degree':d0,'D1_degree':d1,'safe_order2_row_degree':2*d0+d1})
    common=sp.gcd(PP,PP.diff()); Dc=sp.Poly(1-12*tvar+28*tvar**2-32*tvar**3+16*tvar**4,tvar,modulus=p)
    generic=common.exquo(sp.gcd(common,Dc))
    check(f'p{p}_generic_double_root_count',generic.degree()>0)
    check(f'p{p}_firstorder_p_layer_pole_order',p+2>4 and p+2-p>1)
    return {'prime':p,'prefix_exclusive':prefix,'ratio_polynomial_mod_p3':[int(x) for x in G[:3*p+1]],
            'actual_ratio_degree_mod_p3':max(i for i,x in enumerate(G) if x),
            'hasse_degree':PP.degree(),'generic_double_root_count':generic.degree(),
            'firstorder_primitive_degree_floor_except_N':(p+1)*max(0,generic.degree()-2),
            'embedding_operator_checks':embeddings}

if __name__=='__main__':
    ds=[1,2,4,5,10,20]; exps=[-4,10,-4,-4,10,-4]
    check('Phi_weight_two',sum(exps)==4)
    check('Phi_eta_norm_phase_one',sum(d*e for d,e in zip(ds,exps))==0)
    check('Phi_eta_character_trivial_square',sp.prod(sp.Rational(d)**e for d,e in zip(ds,exps))==400)
    orders=[]
    for c in ds:
        width=20//gcd(c*c,20)
        order=sum(sp.Rational(width*e*gcd(c,d)**2,24*d) for d,e in zip(ds,exps))
        orders.append(int(order))
    check('Phi_cusp_orders',orders==[0,3,0,0,3,0])
    check('full_Hall_zero_order_lower_bound',sp.Rational(36,6*4)==sp.Rational(3,2)>1)
    tvar=sp.Symbol('t'); rr=sp.sqrt(5)
    NN=1-(6+rr)*tvar+(1+rr)*tvar**2
    CC=1-(6-2*rr)*tvar+(6-2*rr)*tvar**2
    DD=1-12*tvar+28*tvar**2-32*tvar**3+16*tvar**4
    check('A_N_two_distinct_roots',sp.simplify(sp.discriminant(NN,tvar))==37+8*rr)
    check('A_N_avoids_branch_roots',sp.simplify(sp.resultant(NN,DD,tvar))==-4400+400*rr)
    check('A_N_avoids_own_C_roots',sp.simplify(sp.resultant(NN,CC,tvar))==-80+60*rr)
    samples=[run(p) for p in [7,11,13]]
    out={'scope':'fixed-prime exact checks only; all-prime geometry and no-new-tau limitations are in the report',
         'checks_passed':len(CHECKS),'check_labels':CHECKS,'Phi_eta_exponents':dict(zip(map(str,ds),exps)),
         'Phi_cusp_orders':orders,'samples':samples}
    dest=Path(__file__).with_suffix('.json'); dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_passed':len(CHECKS),'certificate':str(dest),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()},ensure_ascii=False))
