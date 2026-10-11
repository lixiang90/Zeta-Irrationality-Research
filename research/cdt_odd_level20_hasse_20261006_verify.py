"""Fixed-prime exact checks for the global Hasse and highest-packet lemmas.

The geometric proof and the local-lattice proof are in the report; these finite
checks do not prove a global CDT improvement or any numerical irrationality.
"""
from pathlib import Path
from math import comb
import hashlib, json, sys
import sympy as sp

sys.stdout.reconfigure(encoding='utf-8')
ROOT = Path(__file__).resolve().parents[1]
CHECKS = []

def check(label, value):
    assert value, label
    CHECKS.append(label)

def run(p):
    size = p*p
    def pad(a, n=size): return list(a[:n])+[0]*max(0,n-len(a))
    def add(a,b): return [(x+y)%p for x,y in zip(a,b)]
    def scale(a,c): return [x*c%p for x in a]
    def mul(a,b,n=None):
        if n is None: n=min(len(a),len(b))
        out=[0]*n
        for i,x in enumerate(a[:n]):
            if x:
                for j,y in enumerate(b[:n-i]):
                    if y: out[i+j]=(out[i+j]+x*y)%p
        return out
    def inv(a):
        n=len(a); out=[0]*n; c=pow(a[0],-1,p); out[0]=c
        for j in range(1,n): out[j]=-c*sum(a[k]*out[j-k] for k in range(1,j+1))%p
        return out
    def power(a,k):
        if k<0: return power(inv(a),-k)
        out=[1]+[0]*(len(a)-1)
        while k:
            if k&1: out=mul(out,a)
            k//=2
            if k: a=mul(a,a)
        return out
    def compose(a,b):
        n=len(b); out=[0]*n; power_b=[1]+[0]*(n-1)
        for j,c in enumerate(a[:n]):
            if c:
                for i in range(j,n): out[i]=(out[i]+c*power_b[i])%p
            if j+1<n: power_b=mul(power_b,b)
        return out
    def derivative(a): return [(i*a[i])%p for i in range(1,len(a))]+[0]
    def theta(a): return [i*x%p for i,x in enumerate(a)]
    def eta(exponents):
        out=[1]+[0]*(size-1)
        for d,r in zip([1,2,4,5,10,20],exponents):
            for m in range(d,size,d):
                fac=[0]*size
                for j in range((size-1)//m+1):
                    bc=comb(r,j) if r>=0 and j<=r else (0 if r>=0 else (-1)**j*comb(-r+j-1,j))
                    fac[j*m]=(-1)**j*bc%p
                out=mul(out,fac)
        return out
    def revert(a):
        b=[0,1]
        while len(b)<len(a):
            n=min(2*len(b)-1,len(a)); b=pad(b,n)
            err=compose(a[:n],b); err[1]=(err[1]-1)%p
            slope=compose(derivative(a)[:n],b)
            correction=mul(err,inv(slope))
            b=[(x-y)%p for x,y in zip(b,correction)]
        return b
    Hunit=eta([-2,0,2,2,0,-2])
    BB=eta([0,2,0,0,2,0])
    U=Hunit[:]; U[1]=(U[1]+1)%p
    tq=pad([0]+inv(U)); qt=revert(tq)
    check(f'p{p}_coordinate_inverse',compose(tq,qt)==pad([0,1]))
    q_over_t=pad(qt[1:])
    B_over_t=mul(q_over_t,compose(BB,qt))
    om=pad([1,-1])
    P=mul(power(om,p-1),power(B_over_t,1-p))
    degree=3*(p-1)
    # Last jet of B/t uses one unavailable coefficient; do not test it.
    check(f'p{p}_global_hasse_degree_jets',P[0]==1 and all(x==0 for x in P[degree+1:-2]))
    PP=sp.Poly(sum(P[i]*sp.Symbol('t')**i for i in range(degree+1)),sp.Symbol('t'), modulus=p)
    check(f'p{p}_hasse_exact_degree',PP.degree()==degree)
    common=sp.gcd(PP,PP.diff())
    radical=PP.exquo(common)
    # Hasse has simple zeros upstairs. Its square has multiplicities 2 away
    # from branch points and 1 at branch points after the tame quotient.
    odd_support=PP.exquo(common**2)
    check(f'p{p}_hasse_multiplicities_at_most_two',sp.gcd(radical,radical.diff()).degree()==0)
    Dc=sp.Poly(16*PP.gens[0]**4-32*PP.gens[0]**3+28*PP.gens[0]**2-12*PP.gens[0]+1,PP.gens[0],modulus=p)
    check(f'p{p}_odd_hasse_support_on_branches',Dc.rem(odd_support).is_zero)
    check(f'p{p}_radical_degree_bound',2*radical.degree()<=3*p+1)
    rad=pad([int(radical.nth(i))%p for i in range(radical.degree()+1)])
    Pprime=derivative(pad(P[:degree+1]))
    # P'/P = V/rad(P), exactly in F_p(t), including multiplicities.
    Vpoly=(PP.diff()*radical).exquo(PP)
    V=pad([int(Vpoly.nth(i))%p for i in range(Vpoly.degree()+1)])
    check(f'p{p}_log_derivative_radical',mul(V,pad(P[:degree+1]))==mul(Pprime,rad))
    def chi(n): return (0,1,-1,-1,1)[n%5]
    AE=pad([(-pow(5,-1,p))%p]+[sum(chi(d)*d for d in range(1,n+1) if n%d==0)%p for n in range(1,size)])
    AF=pad([0]+[-4*sum(chi((n//4)//d)*d for d in range(1,n//4+1) if (n//4)%d==0)%p if n%4==0 else 0 for n in range(1,size)])
    Ek=[0]+[sum(chi(d)*d**3 for d in range(1,n+1) if n%d==0) for n in range(1,size)]
    Fk=[0]+[sum(chi(n//d)*d**3 for d in range(1,n+1) if n%d==0) for n in range(1,size)]
    VE=[0]+[Ek[n]-(5*Ek[n//2] if n%2==0 else 0)+(4*Ek[n//4] if n%4==0 else 0) for n in range(1,size)]
    VF=[0]+[-5*pow(4,-1,p)*(Fk[n]-(20*Fk[n//2] if n%2==0 else 0)+(64*Fk[n//4] if n%4==0 else 0))%p for n in range(1,size)]
    fe=pad([0]+[VE[n]*pow(n,-3,p)%p for n in range(1,p)])
    ff=pad([0]+[VF[n]*pow(n,-3,p)%p for n in range(1,p)])
    top_e=[0]*size; top_f=[0]*size
    for n in range(p,size,p):
        top_e[n]=VE[n]*pow(n//p,-3,p)%p
        top_f[n]=VF[n]*pow(n//p,-3,p)%p
    check(f'p{p}_whole_E_source_packet',all(top_e[p*j]==fe[j] for j in range(1,p)))
    check(f'p{p}_whole_F_source_packet',all(top_f[p*j]==chi(p)*ff[j]%p for j in range(1,p)))
    # Whole source packet modulo p^3. Do not reduce the whole Eichler
    # series or use q(t)^p=q(t^p) in this stronger congruence.
    modulus3=p**3
    VFraw=[0]+[Fk[n]-(20*Fk[n//2] if n%2==0 else 0)+(64*Fk[n//4] if n%4==0 else 0) for n in range(1,size)]
    for label, source, eigenvalue in [('E',VE,1),('F',VFraw,chi(p))]:
        actual=[]; predicted=[]
        for n in range(size):
            if n==0:
                actual.append(0); predicted.append(0)
            elif n%p:
                actual.append(modulus3*source[n]*pow(n,-3,modulus3)%modulus3)
                predicted.append(0)
            else:
                j=n//p
                actual.append(source[n]*pow(j,-3,modulus3)%modulus3)
                predicted.append(eigenvalue*source[j]*pow(j,-3,modulus3)%modulus3)
        check(f'p{p}_whole_{label}_source_packet_mod_p_cubed',actual==predicted)
    A0,A1=compose(AE,qt),compose(AF,qt)
    f0,f1=compose(fe,qt),compose(ff,qt)
    pe,pf=compose(top_e,qt),compose(top_f,qt)
    frob0=[f0[i//p] if i%p==0 else 0 for i in range(size)]
    frob1=[chi(p)*f1[i//p]%p if i%p==0 else 0 for i in range(size)]
    check(f'p{p}_integer_coordinate_Frobenius_packet',pe==frob0 and pf==frob1)
    def pairmul(a,b):
        return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),5)),add(mul(a[0],b[1]),mul(a[1],b[0]))
    def pairadd(a,b): return add(a[0],b[0]),add(a[1],b[1])
    def pairscale(a,c): return scale(a[0],c),scale(a[1],c)
    def pairtheta(a): return theta(a[0]),theta(a[1])
    def pairderiv(a): return derivative(a[0]),derivative(a[1])
    one=(pad([1]),pad([])); radpair=(rad,pad([])); vpair=(V,pad([]))
    results=[]
    for sign in [-1,1]:
        # sign -1 is root's A_-; AF=-4 F2(4tau), so A_-=AE+r AF.
        A=(A0,scale(A1,-sign))
        NM=(pad([1,-6,1]),pad([0,sign,-sign]))
        CM=(pad([1,-6,6]),pad([0,-2*sign,2*sign]))
        D=pairmul(pairmul(NM,CM),radpair)
        numerator=pairadd(pairadd(pairmul(pairmul(pairderiv(NM),CM),radpair),
                                pairscale(pairmul(pairmul(NM,pairderiv(CM)),radpair),pow(2,-1,p))),
                          pairmul(pairmul(NM,CM),vpair))
        Nt=(pad([0]+numerator[0]),pad([0]+numerator[1]))
        def apply(jet): return pairadd(pairmul(D,pairtheta(jet)),pairscale(pairmul(Nt,jet),-1))
        check(f'p{p}_embedding{sign}_first_order_hasse_relation',all(v==0 for a in apply(A) for v in a))
        jet=pairmul((pe,scale(pf,-sign)),A)
        predicted=pairmul((frob0,scale(frob1,-sign)),A)
        check(f'p{p}_embedding{sign}_actual_highest_packet',jet==predicted)
        killed=apply(jet)
        check(f'p{p}_embedding{sign}_highest_layer_removed',all(v==0 for a in killed for v in a))
        check(f'p{p}_embedding{sign}_differentiated_relation',all(v==0 for a in pairtheta(killed) for v in a))
        dd=max(i for a in D for i,v in enumerate(a) if v)
        check(f'p{p}_embedding{sign}_polynomial_operator_degree',dd<= (3*p+9)//2 and all(v==0 for a in Nt for v in a[dd+1:]))
        # Compute the actual finite-prefix evaluation rank over each residue
        # field. Split p is tested at both roots of r^2=5; otherwise the pair
        # representation is the field F_{p^2}.
        polynomial_degree=dd+2
        roots=[x for x in range(p) if x*x%p==5%p]
        field_modes=roots if roots else [None]
        ranks=[]
        jets=[jet,pairtheta(jet),pairtheta(pairtheta(jet))]
        for root in field_modes:
            def cmul(a,b): return ((a[0]*b[0]+5*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
            def cinv(a):
                norm=(a[0]*a[0]-5*a[1]*a[1])%p
                ii=pow(norm,-1,p)
                return (a[0]*ii%p,-a[1]*ii%p)
            basis={}
            for component in jets:
                values=[((a+b*root)%p,0) if root is not None else (a,b)
                        for a,b in zip(*component)]
                for k in range(polynomial_degree+1):
                    column=[(0,0)]*k+values[:size-k]
                    for n in range(size):
                        if column[n]==(0,0): continue
                        if n in basis:
                            multiplier=column[n]
                            vec=basis[n]
                            for i in range(n,size):
                                sub=cmul(multiplier,vec[i])
                                column[i]=((column[i][0]-sub[0])%p,(column[i][1]-sub[1])%p)
                        else:
                            ii=cinv(column[n])
                            column=[cmul(v,ii) for v in column]
                            basis[n]=column
                            break
            rank=len(basis); ambient=3*(polynomial_degree+1)
            bound=min(ambient,size-p,polynomial_degree+2*dd+1)
            check(f'p{p}_embedding{sign}_residue{root}_actual_lattice_rank_bound',rank<=bound)
            check(f'p{p}_embedding{sign}_residue{root}_explicit_kernel_gain',ambient-rank>=2*(polynomial_degree-dd+1))
            ranks.append({'sqrt5_residue':root,'residue_degree':1 if root is not None else 2,
                          'polynomial_degree':polynomial_degree,'prefix_length':size,
                          'ambient_dimension':ambient,'actual_rank':rank,'proven_rank_bound':bound,
                          'actual_kernel_dimension':ambient-rank})
        results.append({'embedding_sign':sign,'operator_degree':dd,'local_lattice_samples':ranks})
    return {'prime':p,'truncation_exclusive':size,'hasse_polynomial':[int(PP.nth(i))%p for i in range(degree+1)],
            'hasse_degree':degree,'radical_degree':radical.degree(),'odd_branch_factor':str(odd_support.as_expr()),
            'operators':results}

if __name__=='__main__':
    samples=[run(p) for p in [7,11,13]]
    for D,delta in [(20,15),(30,21),(40,24)]:
        kernel=2*(D-delta+1)
        check(f'local_lattice_dimension_D{D}_delta{delta}',3*(D+1)-kernel==D+2*delta+1)
    report=Path(__file__).with_name('cdt_odd_level20_hasse_20261006.md')
    out={'status':'exact_level20_hasse_checks_passed','checks':CHECKS,'fixed_samples':samples,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'report_sha256':hashlib.sha256(report.read_bytes()).hexdigest() if report.exists() else None,
         'proof_scope':'Finite exact samples supplement global Hasse divisor and packet proofs. Local highest-layer lattice gain only; no revised global holonomy tau and no numerical irrationality theorem.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':out['status'],'checks_passed':len(CHECKS),'samples':[{k:s[k] for k in ['prime','hasse_degree','radical_degree','operators']} for s in samples]}))
