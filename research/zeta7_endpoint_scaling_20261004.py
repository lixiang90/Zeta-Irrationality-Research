"""Three exact scales of the rank-two next-to-highest moment endpoint family.

K=15N-5, h=14N-5, q=6N-1 prime.  The bad m=7 moment is d-1.
All determinant and coset coefficients/content are exact; Arb certifies the
Schur endpoint and the head-polynomial obstruction to the uniform budget.
"""
import argparse, json, math, sys, time
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, arb, arb_mat, arb_poly, ctx
from sympy import primerange, isprime
from joint_exact import entries, content
from zeta7_space_extension_probe import polynomial
from zeta7_moment_extension_20261004 import aq, vp, centered_principal_part, positive_pivots
from b8_hankel import Dpoly, mu_monomial

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent;PREFIX='zeta7_endpoint_scaling_20261004'

def logq(v):return aq(v).log()
def ball(v):return v.str(55)
def polyeval(p,z):return arb_poly([aq(v) for v in p])(z)
def cjoin(polys):return content(Poly([v for p in polys for v in p]))
def table(p):return [str(p[i]) for i in range(p.degree()+1)]
def prefix(M,n):return type(M)([[M[i,j] for j in range(n)] for i in range(n)])

def protected_step(f,q,bound):
    c=[content(p) for p in f];L=1;rows=[]
    primes=list(primerange(2,bound+1))
    for p in primes:
        if p==q:continue
        v=[vp(v,p) for v in c]
        e=int(max(0,*(math.ceil(Q(v[0]-v[j],j)) for j in (1,2))))
        if e:L*=p**e;rows.append(dict(prime=p,required_valuation=e,coefficient_content_valuations=v))
    # Do not assume no exceptional large prime occurs in the numerator gcds.
    # The unused numerator part gives a safe, potentially excessive correction.
    residuals=[]
    for j in (1,2):
        x=abs(int((c[0]/c[j]).numerator))
        for p in primes:
            while x%p==0:x//=p
        if x>1:L*=x
        residuals.append(str(x))
    for p in primes:
        if p==q:continue
        for j in (1,2):assert vp(c[j],p)+j*vp(Q(L),p)>=vp(c[0],p)
    return L,dict(prime_valuations=rows,unfactored_safe_numerator_multipliers=residuals,
                  complete_coverage=True,scope='Sufficient termwise preservation of baseline content outside q.')

def coset(f,N,K,h,q,beta,mu,step,label,z,base,head,H,prec):
    f0,f1,f2=f;ctT=content(-f2);headvalue=polyeval(-f2,z)
    assert headvalue>0
    a=prefix(H,h-1).det()/headvalue;assert a>0
    c=polyeval(f1,z)/(2*headvalue)
    R2=polyeval(f0,z)/headvalue+c*c;assert R2>0
    R=R2.sqrt();assert R>abs(c)
    residue=int((q*mu).numerator)*pow(int((q*mu).denominator),-1,q)%q
    assert vp(mu,q)==-1 and math.gcd(step,q)==1
    u=residue*pow(step,-1,q)%q
    if u>q//2:u-=q
    alpha=Q(step*u,q)
    Qs=[f0+alpha*f1+alpha*alpha*f2,step*f1+2*alpha*step*f2,step*step*f2]
    cstar=cjoin(Qs);assert cstar>0
    m=step*step*ctT/cstar;assert m.denominator==1 and m>0
    PT=polyeval((-f2)/ctT,z);assert PT>0
    width=2*R/step
    out=dict(label=label,step=str(step),coset_start=str(alpha),principal_part_residue=residue,
             beta=beta,head_dimension=h-2,head_content=str(ctT),
             all_parameter_content=str(cstar),integer_M=str(m),
             center_interval=ball(c),radius_interval=ball(R),
             log_radius_interval=ball(R.log()),log_step_interval=ball(arb(step).log()),
             log_head_determinant_interval=ball(headvalue.log()),
             log_coset_content_interval=ball(logq(cstar)),
             log_head_primitive_interval=ball(PT.log()),
             log_head_primitive=float(PT.log()),log_head_primitive_over_K2=float(PT.log()/K**2),
             log_width_over_step_interval=ball(width.log()),positive_interval_wider_than_step=bool(width>1),
             coset_coefficient_polynomials=[table(p) for p in Qs])
    if not width>1:
        out['status']='uniform_endpoint_hypothesis_fails'
        return out
    U=2*R*step*headvalue/aq(cstar);assert U>PT
    assert U.overlaps(width*aq(m)*PT)
    k=int(((c+R-aq(alpha))/step).floor().unique_fmpz())
    y=alpha+step*k;delta=c+R-aq(y)
    assert delta>0 and delta<step and delta<2*R
    assert vp(mu-y,q)>=0
    p=f0+y*f1+y*y*f2;ct=content(p);extra=ct/cstar
    assert extra.denominator==1 and extra>0
    primitive=p/ct;assert all(v.denominator==1 for v in primitive)
    value=polyeval(primitive,z);assert value>0 and value<U
    direct=headvalue*(2*R*delta-delta*delta)/aq(ct);assert value.overlaps(direct)
    endpoint_factor=(delta/step)*(1-delta/(2*R))/aq(extra)
    assert value.overlaps(U*endpoint_factor)
    rawchange=polyeval(p,z).log()-polyeval(f0,z).log()
    contentchange=logq(ct)-logq(content(f0))
    assert (value.log()-base.log()).overlaps(rawchange-contentchange)
    out.update(status='exact_coset_and_endpoint_certified',parameter_k=str(k),endpoint_y=str(y),
               distance_over_step_interval=ball(delta/step),extra_parameter_content=str(extra),
               actual_content=str(ct),primitive_coefficients=[str(int(v)) for v in primitive],
               actual_primitive_degree=primitive.degree(),log_endpoint_distance_factor_interval=ball(endpoint_factor.log()),
               log_uniform_upper_interval=ball(U.log()),log_uniform_upper=float(U.log()),
               log_uniform_upper_over_K2=float(U.log()/K**2),
               uniform_gap_above_head_interval=ball(U.log()-PT.log()),
               uniform_gap_identity_interval=ball(width.log()+logq(m)),
               log_actual_primitive_interval=ball(value.log()),log_actual_primitive=float(value.log()),
               log_actual_primitive_over_K2=float(value.log()/K**2),
               log_raw_change_interval=ball(rawchange),log_content_change_interval=ball(contentchange),
               log_change_from_baseline_interval=ball(value.log()-base.log()),
               actual_minus_baseline=float(value.log()-base.log()),
               log_uniform_upper_minus_actual_interval=ball(U.log()-value.log()))
    return out

def run(N):
    start=time.perf_counter();q=6*N-1;assert isprime(q)
    K,h=15*N-5,14*N-5;d=8*N+2*h-2-K;e=d-1
    assert e==(7*q-9)//2 and 2*e+2==7*(q-1)
    D,W=Poly(Dpoly(K)),Poly(Dpoly(N)**8)
    beta=sum(j*j for j in range(1,K+1))-8*sum(j*j for j in range(1,N+1))
    corr=[]
    for s in range(2*h-1):
        quotient=(W*Poly([0]*s+[1]))//D
        corr.append(quotient[e])
    assert corr==[Q(0)]*(2*h-3)+[Q(1),Q(-beta)]
    aa,bb=entries(K,[(N,8)],h)
    A=Mat([[aa[i+j] for j in range(h)] for i in range(h)])
    B=Mat([[bb[i+j] for j in range(h)] for i in range(h)])
    C=Mat([[corr[i+j] for j in range(h)] for i in range(h)])
    assert C.rank()==2
    ps=[]
    for y in (-1,0,1):
        p=polynomial(A-y*C,B)
        for x in (-1,0,1):assert p(x)==(A-y*C+x*B).det()
        ps.append(p)
        print('N',N,'K',K,'exact y',y,'seconds',round(time.perf_counter()-start,2),flush=True)
    f=[ps[1],(ps[2]-ps[0])/2,(ps[2]+ps[0])/2-ps[1]]
    head=polynomial(prefix(A,h-2),prefix(B,h-2));assert f[2]==-head
    # A fourth point is a validation of the structural quadratic identity.
    for x in (-1,0,1):assert sum((f[j](x)*2**j for j in range(3)),Q(0))==(A-2*C+x*B).det()
    prec=max(abs(int(v.numerator)).bit_length()+int(v.denominator).bit_length() for p in f for v in p)+K*K+10000
    ctx.prec=prec;z=arb(7).zeta()
    H=arb_mat([[aq(A[i,j])+z*aq(B[i,j]) for j in range(h)] for i in range(h)])
    assert positive_pivots(H)['positive_definite'] is True
    ct0=content(f[0]);baseline=polyeval(f[0]/ct0,z);assert baseline>0
    assert prefix(H,h-2).det().overlaps(polyeval(head,z))
    mu=mu_monomial(e);pp=centered_principal_part(mu,q)
    assert pp.denominator==q and vp(mu-pp,q)>=0
    L,protection=protected_step(f,q,max(2*K,2*d+3))
    out=dict(N=N,K=K,h=h,q=q,top_moment=d,corrected_moment=e,
             bernoulli_layer=7,beta=beta,correction_rank=2,correction_sequence=list(map(str,corr)),
             moment_original=str(mu),centered_q_principal_part=str(pp),
             coefficient_polynomials=[table(p) for p in f],
             head_polynomial=table(head),baseline_content=str(ct0),
             baseline_primitive_coefficients=[str(int(v)) for v in f[0]/ct0],
             baseline_log_interval=ball(baseline.log()),baseline_log=float(baseline.log()),
             baseline_log_over_K2=float(baseline.log()/K**2),precision_bits=prec,
             determinant_checks=dict(interpolation_y=[-1,0,1],independent_y=2,X=[-1,0,1],
                                     complete_head_identity=True),termwise_protection=protection,cosets=[])
    for label,step in [('principal_part_step_one',1),('baseline_content_protected_step',L)]:
        row=coset(f,N,K,h,q,beta,mu,step,label,z,baseline,head,H,prec)
        out['cosets'].append(row)
        print('N',N,'coset',label,'logL',float(arb(step).log()),'width',row['positive_interval_wider_than_step'],
              'logU',row.get('log_uniform_upper'),'logP',row.get('log_actual_primitive'),
              'head',row['log_head_primitive'],flush=True)
    out['seconds']=time.perf_counter()-start
    (ROOT/f'{PREFIX}_N{N}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    return dict(N=N,K=K,h=h,q=q,baseline_log=out['baseline_log'],baseline_J=out['baseline_log_over_K2'],
                cosets=[{k:r[k] for k in ('label','step','log_head_primitive','positive_interval_wider_than_step',
                                         'log_uniform_upper','log_uniform_upper_over_K2','log_actual_primitive',
                                         'log_actual_primitive_over_K2','actual_minus_baseline') if k in r} for r in out['cosets']])

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--N',type=int,nargs='+',default=[3,4,5]);args=p.parse_args()
    out=dict(status='in_progress',cases=[],scope='Finite three-scale exact endpoint study, no extrapolated asymptotic exponent.')
    for N in args.N:
        out['cases'].append(run(N));(ROOT/f'{PREFIX}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='complete';(ROOT/f'{PREFIX}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
