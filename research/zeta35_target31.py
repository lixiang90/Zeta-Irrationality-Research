"""Exact finite arithmetic diagnostics for 3*zeta(3)+zeta(5).

No finite run establishes irrationality. Contents and p-adic differences are
exact; values of polynomials at zeta values are enclosed using Arb.
"""
import argparse, json, math, sys, time
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, fmpq_mat, arb, arb_poly, ctx
import zeta35_mixed_moments as mixed

sys.set_int_max_str_digits(0)

def primes_to(n):
    flags = [True]*(n+1)
    for p in range(2,math.isqrt(n)+1):
        if flags[p]:
            for k in range(p*p,n+1,p): flags[k]=False
    return [p for p in range(2,n+1) if flags[p]]

def content_and_primitive(poly):
    den=math.lcm(*(int(c.denominator) for c in poly))
    nums=[int(c*den) for c in poly]
    g=math.gcd(*nums)
    return Q(g,den), [v//g for v in nums]

def rational_log(q):
    return (arb(int(q.numerator))/arb(int(q.denominator))).log()

def smooth_valuations(q,limit):
    num,den=int(q.numerator),int(q.denominator)
    values={}
    for p in primes_to(limit):
        v=0
        while num%p==0: num//=p;v+=1
        while den%p==0: den//=p;v-=1
        if v: values[str(p)]=v
    assert num==den==1,(num,den,limit)
    return values

def run(n):
    start=time.perf_counter()
    K,N,h,A5,B=mixed.original.entries(n)
    A3t=mixed.shifted_mu3_entries(n)
    rows=[]
    for a in (0,3):
        A=[v-a*w for v,w in zip(A5,A3t)]
        poly=mixed.original.det_poly(h,A,B)
        assert poly.degree()==h
        content,coeff=content_and_primitive(poly)
        bits=max(abs(v).bit_length() for v in coeff)
        ctx.prec=bits+K*K+4000
        value=arb_poly(coeff)(a*arb(3).zeta()+arb(5).zeta())
        assert value>0
        logp=value.log();logc=rational_log(content)
        checks=[]
        for x in (Q(0),Q(1)):
            direct=fmpq_mat([[A[i+j]+x*B[i+j] for j in range(h)] for i in range(h)]).det()
            assert direct==poly(x);checks.append(str(x))
        rows.append(dict(a=a,b=1,content=str(content),primitive_coefficients=list(map(str,coeff)),
            log_p_interval=str(logp),log_p=float(logp),log_content=float(logc),
            log_delta=float(logp+logc),degree=h,positive=True,checks=checks))
        print('n',n,'a',a,'logP',float(logp),'logP/K2',float(logp)/(K*K),
              'seconds',round(time.perf_counter()-start,2),flush=True)
    ratio=Q(rows[0]['content'])/Q(rows[1]['content'])
    vals=smooth_valuations(ratio,max(2*K,2*(6*N+2*h-K)+10))
    loss=float(rational_log(ratio))
    rawgap=rows[1]['log_delta']-rows[0]['log_delta']
    lower=h*math.log(1-9/math.pi**2)
    assert lower-1e-7<=rawgap<=1e-7
    assert abs((rows[1]['log_p']-rows[0]['log_p'])-(rawgap+loss))<1e-6
    result=dict(n=n,K=K,N=N,h=h,rows=rows,content_ratio=str(ratio),
        content_loss_log=loss,content_loss_over_K2=loss/(K*K),
        raw_log_ratio=rawgap,raw_log_ratio_lower=lower,prime_losses=vals,
        loss_prime_above_K_over_3=sum(v*math.log(int(p)) for p,v in vals.items() if 3*int(p)>K),
        elapsed=time.perf_counter()-start,status='finite_exact_and_arb_checks_passed')
    out=Path(__file__).with_name(f'zeta35_target31_n{n}.json')
    out.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('content loss',loss,'raw gap',rawgap,'prime losses',vals,flush=True)
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('n',nargs='+',type=int)
    for n in parser.parse_args().n:
        run(n)
