"""Bounded zeta(7) moment modifications, preserving the coefficient of X.

The principal-part corrections preserve every simple-pole value.  The
Christoffel corrections preserve only the coefficient of X, and change pole
constants.  All determinant coefficients/content are exact; Arb certifies
relative norms and positive pivots.  No asymptotic conclusion is asserted.
"""
import json, math, sys, hashlib
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat, arb, arb_mat, arb_poly, ctx
from sympy import primerange
import b8_hankel as b8
from joint_exact import determinant, content

sys.set_int_max_str_digits(0)


def aq(x):
    return arb(int(x.numerator))/int(x.denominator)


def vp(q,p):
    if not q:
        return None
    n,d=abs(int(q.numerator)),int(q.denominator)
    ans=0
    while n%p==0:
        n//=p; ans+=1
    while d%p==0:
        d//=p; ans-=1
    return ans


def centered_principal_part(q,p):
    n,d=int(q.numerator),int(q.denominator)
    pe=1
    while d%p==0:
        d//=p;pe*=p
    if pe==1:
        return Q(0)
    u=n*pow(d,-1,pe)%pe
    if u>pe//2:
        u-=pe
    c=Q(u,pe)
    assert not(q-c) or vp(q-c,p)>=0
    return c


def positive_pivots(M):
    S=M.tolist(); pivots=[]
    for k in range(len(S)):
        d=S[k][k]
        pivots.append(str(d))
        if d<0:
            return dict(positive_definite=False,negative_pivot=k,pivot_interval=str(d))
        if not d>0:
            return dict(positive_definite=None,uncertain_pivot=k,pivot_interval=str(d))
        for i in range(k+1,len(S)):
            for j in range(i,len(S)):
                S[i][j]-=S[i][k]*S[j][k]/d
                S[j][i]=S[i][j]
    return dict(positive_definite=True,positive_pivot_count=len(S))


def mu5(k):
    return Q(-1)**k*Q.bernoulli(2*k+2)*(2*k+3)*(2*k+4)*(2*k+5)/24


def qlog(q):
    return aq(abs(q)).log()


def ball(x):
    return x.str(80)


def main():
    K,N,h,A,B=b8.entries(1)
    assert (K,N,h)==(40,3,37)
    W=Poly(b8.Dpoly(N)**8);D=Poly(b8.Dpoly(K))
    quotients=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    top=max(q.degree() for q in quotients)
    moments=[b8.mu_monomial(k) for k in range(top+1)]
    base=determinant(A,B,h); c0=content(base)
    coeff0=[int(q) for q in base/c0]
    ctx.prec=16000
    z=arb(7).zeta()
    H=arb_mat([[aq(A[i+j])+z*aq(B[i+j]) for j in range(h)] for i in range(h)])
    Hinv=H.inv();basevalue=arb_poly(coeff0)(z)
    assert basevalue>0
    assert positive_pivots(H)['positive_definite'] is True
    experiments=[]
    primes=[7,11,13,17,19]
    for ps in [(p,) for p in primes]+[tuple(primes)]:
        changes=[sum((centered_principal_part(m,p) for p in ps),Q(0)) for m in moments]
        specs=[dict(e=k,correction=str(c),original=str(moments[k])) for k,c in enumerate(changes) if c]
        corr=[sum((q[k]*changes[k] for k in range(q.degree()+1)),Q(0)) for q in quotients]
        assert all(not m-c or all(vp(m-c,p)>=0 for p in ps) for m,c in zip(moments,changes))
        experiments.append(('all_principal_parts_'+('_'.join(map(str,ps))),corr,
                            dict(primes=list(ps),moment_specs=specs,
                                 simple_pole_values_preserved=True,polynomial_integrality_verified=True)))
    C5=[sum((c*mu5(k) for k,c in enumerate(W*Poly([0]*s+[1]))),Q(0)) for s in range(2*h-1)]
    fact=math.factorial(K)
    for label,lam in [('subtract_mu5_DK_factorial2',Q(1,fact**2)),
                      ('add_mu5_DK_factorial2',Q(-1,fact**2)),
                      ('subtract_mu5_DK_factorial4',Q(1,fact**4))]:
        experiments.append((label,[lam*c for c in C5],
                            dict(lambda_value=str(lam),simple_pole_values_preserved=False,
                                 zeta7_parameter_coefficient_preserved=True,
                                 functional_correction='lambda * mu5(D_K R)')))
    rows=[]
    for label,corr,metadata in experiments:
        Cq=fmpq_mat([[corr[i+j] for j in range(h)] for i in range(h)])
        C=arb_mat([[aq(corr[i+j]) for j in range(h)] for i in range(h)])
        rel=Hinv*C;trace2=(rel*rel).trace()
        pd=positive_pivots(H-C)
        modified=[a-c for a,c in zip(A,corr)]
        poly=determinant(modified,B,h);ct=content(poly)
        coeff=[int(q) for q in poly/ct]
        value=arb_poly(coeff)(z)
        for x in (Q(-1),Q(0),Q(1)):
            direct=fmpq_mat([[modified[i+j]+x*B[i+j] for j in range(h)] for i in range(h)]).det()
            assert direct==poly(x)
        if trace2<1:
            assert pd['positive_definite'] is True
        packet={str(p):vp(ct/c0,p) for p in primerange(2,200) if vp(ct/c0,p)}
        ratio=ct/c0;n,d=abs(int(ratio.numerator)),int(ratio.denominator)
        for p in primerange(2,200):
            while n%p==0:n//=p
            while d%p==0:d//=p
        row=dict(label=label,**metadata,correction_rank=Cq.rank(),
                 trace_relative_square_interval=ball(trace2),relative_norm_certified=bool(trace2<1),
                 positive_check=pd,determinant_positive=bool(value>0),degree=poly.degree(),
                 content=str(ct),content_ratio=str(ratio),
                 log_content_gain_interval=ball(qlog(ratio)),log_content_gain=float(qlog(ratio)),
                 content_gain_valuations=packet,unfactored_content_ratio_numerator=str(n),
                 unfactored_content_ratio_denominator=str(d),
                 log_abs_primitive_interval=ball(abs(value).log()),
                 log_abs_primitive=float(abs(value).log()),
                 score_interval=ball(abs(value).log()/K**2),
                 coefficient_checks=[-1,0,1],
                 primitive_coefficients_sha256=hashlib.sha256(','.join(map(str,coeff)).encode()).hexdigest())
        rows.append(row)
        print(label,'positive',pd['positive_definite'],'rank',row['correction_rank'],
              'logtrace',float(abs(trace2).log()),'contentgain',row['log_content_gain'],
              'logP',row['log_abs_primitive'],flush=True)
        data=dict(status='in_progress',K=K,N=N,h=h,top_quotient_moment=top,
                  baseline_content=str(c0),baseline_log_primitive_interval=ball(basevalue.log()),
                  baseline_score_interval=ball(basevalue.log()/K**2),rows=rows,
                  scope='Finite K=40 experiments only; exact full content is used. '
                        'Negative determinant is not used as an irrationality criterion. '
                        'Failure of sufficient relative norm bound does not prove indefiniteness.')
        Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    data['status']='passed';Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2),encoding='utf-8')


if __name__=='__main__':
    main()
