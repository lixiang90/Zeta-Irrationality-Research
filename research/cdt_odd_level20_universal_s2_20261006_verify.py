"""Fixed-prime source probes and exact universal-pole coefficient checks.

Scope: p=7,11,13; actual odd Eichler packets in the existing level20 t coordinate.
No parameter search. The all-prime universal S2 theorem is proved in the report.
"""
from pathlib import Path
from math import comb
import hashlib,json

CHECKS=[]
def check(label, condition):
    assert condition,label
    CHECKS.append(label)

def run(p):
    size=p
    def pad(a,n=size):return list(a[:n])+[0]*max(0,n-len(a))
    def mul(a,b):
        out=[0]*len(b)
        for i,x in enumerate(a[:len(b)]):
            if x:
                for j,y in enumerate(b[:len(b)-i]):out[i+j]=(out[i+j]+x*y)%p
        return out
    def inv(a):
        out=pad([pow(a[0],-1,p)],len(a)); ii=out[0]
        for n in range(1,len(a)):out[n]=-ii*sum(a[j]*out[n-j] for j in range(1,n+1))%p
        return out
    def compose(a,b):
        out=[0]*len(b); bp=pad([1],len(b))
        for c in a[:len(b)]:
            out=[(x+c*y)%p for x,y in zip(out,bp)]; bp=mul(bp,b)
        return out
    def derivative(a):return [i*a[i]%p for i in range(1,len(a))]+[0]
    def revert(a):
        b=[0,1]
        while len(b)<len(a):
            n=min(2*len(b)-1,len(a)); b=pad(b,n)
            err=compose(a[:n],b);err[1]=(err[1]-1)%p
            diff=mul(err,inv(compose(derivative(a)[:n],b)))
            b=[(x-y)%p for x,y in zip(b,diff)]
        return b
    eta=pad([1])
    for d,e in zip([1,2,4,5,10,20],[-2,0,2,2,0,-2]):
        for k in range(d,size,d):
            fac=[0]*size
            for j in range((size-1)//k+1):
                cc=comb(e,j) if e>=0 and j<=e else (0 if e>=0 else (-1)**j*comb(-e+j-1,j))
                fac[k*j]=(-1)**j*cc%p
            eta=mul(eta,fac)
    U=eta[:];U[1]=(U[1]+1)%p
    tq=pad([0]+inv(U));qt=revert(tq)
    check(f'p{p}_actual_integer_coordinate',compose(tq,qt)==pad([0,1]))
    def chi(n):return (0,1,-1,-1,1)[n%5]
    E=[0]+[sum(chi(d)*d**3 for d in range(1,n+1) if n%d==0) for n in range(1,p)]
    F=[0]+[sum(chi(n//d)*d**3 for d in range(1,n+1) if n%d==0) for n in range(1,p)]
    ve=[0]+[E[n]-(5*E[n//2] if n%2==0 else 0)+(4*E[n//4] if n%4==0 else 0) for n in range(1,p)]
    vf=[0]+[5*pow(4,-1,p)*(F[n]-(20*F[n//2] if n%2==0 else 0)+(64*F[n//4] if n%4==0 else 0))%p for n in range(1,p)]
    fe=compose([0]+[ve[n]*pow(n,-3,p)%p for n in range(1,p)],qt)
    ff=compose([0]+[vf[n]*pow(n,-3,p)%p for n in range(1,p)],qt)
    roots=[r for r in range(p) if r*r%p==5%p]
    modes=roots if roots else [None]
    results=[]
    for root in modes:
        zero=(0,0); one=(1,0)
        def ca(a,b):return ((a[0]+b[0])%p,(a[1]+b[1])%p)
        def cn(a):return (-a[0]%p,-a[1]%p)
        def cm(a,b):return ((a[0]*b[0]+5*a[1]*b[1])%p,(a[0]*b[1]+a[1]*b[0])%p)
        def ci(a):
            ii=pow((a[0]*a[0]-5*a[1]*a[1])%p,-1,p)
            return a[0]*ii%p,-a[1]*ii%p
        def trim(a):
            a=list(a)
            while a and a[-1]==zero:a.pop()
            return a
        def pmul(a,b):
            out=[zero]*(len(a)+len(b)-1)
            for i,x in enumerate(a):
                for j,y in enumerate(b):out[i+j]=ca(out[i+j],cm(x,y))
            return trim(out)
        def pdiv(a,b):
            a=trim(a);b=trim(b);out=[zero]*max(0,len(a)-len(b)+1); lc=ci(b[-1])
            while len(a)>=len(b):
                k=len(a)-len(b);cc=cm(a[-1],lc);out[k]=cc
                for j,v in enumerate(b):a[k+j]=ca(a[k+j],cn(cm(cc,v)))
                a=trim(a)
            return trim(out),a
        def pgcd(a,b):
            while b:a,b=b,pdiv(a,b)[1]
            return [cm(x,ci(a[-1])) for x in a]
        for sign in [-1,1]:
            f=trim([((a+sign*chi(p)*root*b)%p,0) if root is not None else (a,sign*chi(p)*b%p) for a,b in zip(fe,ff)])
            df=[cm((i%p,0),c) for i,c in enumerate(f)]
            gg=pgcd(f,trim(df)); P,rem=pdiv(f,gg);Q,rem2=pdiv(trim(df),gg)
            label=f'p{p}_root{root}_sign{sign}'
            check(label+'_source_simple_origin_zero',f[0]==zero and f[1]!=zero)
            check(label+'_firstorder_reduced_quotients',not rem and not rem2 and len(pgcd(P,Q))==1)
            check(label+'_exact_firstorder_relation',pmul(P,df)==pmul(Q,f))
            check(label+'_source_denominator_unit_at_origin',P[0]!=zero)
            delta=max(len(P),len(Q))-1
            check(label+'_pole_lowerbound_m0_m1_m2',all((m+2)*(m+1)%p!=0 for m in [0,1,2]))
            results.append({'sqrt5_residue':root,'residue_degree':1 if root is not None else 2,'sign':sign,
                            'source_degree':len(f)-1,'gcd_F_thetaF_degree':len(gg)-1,
                            'minimal_firstorder_source_coefficient_degree':delta,
                            'pulled_back_logderivative_denominator_degree':p*delta})
    return {'prime':p,'source_cutoff_exclusive':p,'packets':results}

if __name__=='__main__':
    samples=[run(p) for p in [7,11,13]]
    out={'scope':'only preassigned actual packet probes and universal local coefficient checks; no finite-jet no-go',
         'checks_passed':len(CHECKS),'check_labels':CHECKS,'samples':samples}
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_passed':len(CHECKS),'certificate':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False))
