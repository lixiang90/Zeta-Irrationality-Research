"""Exact primitive-content checks for the natural third connection.

Input: the frozen, independently proved excellent-ratio certificate.
Output: all coefficients of the fully cleared reduced order1 row, modulo p^3.
This checks p=7,11,13; it does not independently regenerate the source packets
or prove a no-go theorem for arbitrary higher-order constructions.
"""
from pathlib import Path
import hashlib, json
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'research/cdt_odd_level20_frobenius_20261006_verify.json'
CHECKS=[]
def check(label, value):
    assert value,label
    CHECKS.append(label)

def run(sample):
    p=sample['prime']; mod=p**3; size=12*p+40
    def pad(a): return list(a[:size])+[0]*max(0,size-len(a))
    def add(a,b): return [(x+y)%mod for x,y in zip(a,b)]
    def scale(a,c): return [x*c%mod for x in a]
    def mul(a,b):
        out=[0]*size
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b[:size-i]):
                    if y: out[i+j]=(out[i+j]+x*y)%mod
        return out
    def theta(a): return [i*x%mod for i,x in enumerate(a)]
    def power(a,n):
        out=pad([1])
        while n:
            if n&1: out=mul(out,a)
            n//=2
            if n: a=mul(a,a)
        return out
    def inv(a):
        out=pad([pow(a[0],-1,mod)]); ii=out[0]
        for n in range(1,size):out[n]=-ii*sum(a[j]*out[n-j] for j in range(1,n+1))%mod
        return out
    def pmul(a,b): return add(mul(a[0],b[0]),scale(mul(a[1],b[1]),5)),add(mul(a[0],b[1]),mul(a[1],b[0]))
    def padd(a,b): return add(a[0],b[0]),add(a[1],b[1])
    def pscale(a,c): return scale(a[0],c),scale(a[1],c)
    def ptheta(a): return theta(a[0]),theta(a[1])
    def scalar(a): return a,pad([])
    def pdiv(a,n): return all(x%p**n==0 for v in a for x in v)
    def degree(a): return max(i for i,x in enumerate(a) if x) if any(a) else -1
    G=pad(sample['ratio_polynomial_mod_p3']); d=degree(G)
    Delta=pad([1,-12,28,-32,16]); om=pad([1,-1]); t=pad([0,1])
    J=mul(om,Delta)
    # h=theta(log gs)=H/J; h coefficients have integer numerators.
    dDelta=pad([i*Delta[i] for i in range(1,5)])
    H=mul(t,add(scale(Delta,-1),scale(mul(om,dDelta),pow(2,-1,mod))))
    Dz=mul(J,G); Znum=add(mul(H,G),mul(J,theta(G)))
    poly8=pad([6,-49,320,-1316,3104,-4176,3200,-1344,256])
    # F=2 theta z+z^2+4 qproj=Fnum/Dz^2.
    Fnum=add(add(scale(mul(Dz,theta(Znum)),2),scale(mul(Znum,theta(Dz)),-2)),
             add(mul(Znum,Znum),mul(mul(t,poly8),mul(G,G))))
    check(f'p{p}_F_numerator_all_coefficients_divisible_p2',all(x%p**2==0 for x in Fnum))
    check(f'p{p}_F_numerator_not_divisible_p3',any(x%p**3!=0 for x in Fnum))
    Fseries=mul(Fnum,inv(mul(Dz,Dz)))
    check(f'p{p}_curvature_first_nonzero_degree_p',all(x==0 for x in Fseries[:p]))
    check(f'p{p}_curvature_exact_leading_minus8',Fseries[p]//p**2%p==(-8)%p)
    # The closed expression for F/p^2 mod p is
    # -8 t^p(1-t^p) P4(t^p)/[(1-t)^2 Delta P_p^2].
    P4=pad([1,-10,28,-36,18])
    base=scale(mul(mul(t,om),P4),-8)
    frob=[base[i//p] if i%p==0 else 0 for i in range(size)]
    rhs=mul(frob,inv(mul(mul(om,om),mul(Delta,mul(G,G)))))
    check(f'p{p}_curvature_full_modp_formula',all((Fseries[i]//p**2-rhs[i])%p==0 for i in range(size)))
    results=[]
    for sign in [-1,1]:
        N=(pad([1,-6,1]),pad([0,sign,-sign]))
        C=(pad([1,-6,6]),pad([0,-2*sign,2*sign]))
        Co=(C[0],scale(C[1],-1))
        # Atilde=N*J*a, a=theta(log k), k=N/[(1-t)sqrt(Co)].
        Atilde=padd(padd(pmul(scalar(J),ptheta(N)),pmul(N,scalar(mul(t,Delta)))),
                    pscale(pmul(pmul(N,scalar(om)),pmul(C,ptheta(Co))),-pow(2,-1,mod)))
        D=pmul(N,scalar(power(Dz,3)))
        P1=pscale(pmul(N,scalar(mul(Dz,Fnum))),-1)
        thetaFnum=add(mul(Dz,theta(Fnum)),scale(mul(Fnum,theta(Dz)),-2))
        P0=padd(pmul(scalar(mul(G,Fnum)),Atilde),pscale(pmul(N,scalar(thetaFnum)),-pow(2,-1,mod)))
        check(f'p{p}_embedding{sign}_denominator_unit',D[0][0]==1 and D[1][0]==0)
        check(f'p{p}_embedding{sign}_both_target_rows_content_p2',pdiv(P0,2) and pdiv(P1,2))
        check(f'p{p}_embedding{sign}_target_content_exact_p2',not pdiv(P1,3))
        check(f'p{p}_embedding{sign}_normalized_derivative_coefficient_8',P1[0][p]//p**2%p==8%p and P1[1][p]==0)
        P0n=tuple([x//p**2 for x in a] for a in P0)
        P1n=tuple([x//p**2 for x in a] for a in P1)
        # After division by p^2, the row is an ordinary modp logarithmic
        # annihilator of A=kS: P0n+P1n(a+z)=0 modp.
        AlogDen=pmul(N,scalar(mul(J,Dz)))
        AlogNum=padd(pmul(Atilde,scalar(Dz)),pmul(N,scalar(mul(J,Znum))))
        cross=padd(pmul(P0n,AlogDen),pmul(P1n,AlogNum))
        check(f'p{p}_embedding{sign}_primitive_row_in_existing_first_order_module',pdiv(cross,1))
        safe=3*d+17
        check(f'p{p}_embedding{sign}_all_cleared_coefficients_degree_bound',all(degree(a)<=safe for row in [D,P0,P1] for a in row))
        results.append({'sign':sign,'safe_denominator_degree':safe,'target_row_content_valuation':2,
                        'normalized_derivative_t_p_coefficient':8%p,
                        'normalized_row_only_guaranteed_output_valuation':1})
    return {'prime':p,'G_degree_mod_p3':d,'safe_uniform_denominator_degree':9*p+17,
            'F_t_p_coefficient_mod_p3':Fseries[p],'embedding_checks':results}

if __name__=='__main__':
    tv=sp.Symbol('t'); DD=1-12*tv+28*tv**2-32*tv**3+16*tv**4
    P8=256*tv**8-1344*tv**7+3200*tv**6-4176*tv**5+3104*tv**4-1316*tv**3+320*tv**2-49*tv+6
    qp=tv*P8/(4*(1-tv)**2*DD**2)
    hh=-tv/(1-tv)+tv*sp.diff(DD,tv)/(2*DD)
    curvature=sp.factor(4*qp+2*tv*sp.diff(hh,tv)+hh**2)
    expected=-8*tv*(18*tv**4-36*tv**3+28*tv**2-10*tv+1)/((1-tv)*DD)
    check('exact_rational_curvature_identity',sp.cancel(curvature-expected)==0)
    check('curvature_first_coefficient_minus8',sp.limit(curvature/tv,tv,0)==-8)
    data=json.loads(INPUT.read_text(encoding='utf-8'))
    check('input_fixed_primes', [x['prime'] for x in data['samples']]==[7,11,13])
    samples=[run(x) for x in data['samples']]
    out={'scope':'primitive content of the natural third connection after exact Bol/constant reduction; no all-method no-go',
         'input_certificate':str(INPUT),'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),
         'checks_passed':len(CHECKS),'check_labels':CHECKS,'rational_curvature':str(curvature),'samples':samples}
    target=Path(__file__).with_suffix('.json'); target.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'checks_passed':len(CHECKS),'certificate':str(target),'sha256':hashlib.sha256(target.read_bytes()).hexdigest()},ensure_ascii=False))
