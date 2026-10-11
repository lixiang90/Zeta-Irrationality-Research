"""One bounded CRT protection experiment for the M_38 correction at K=40.

The computed scalar conductor is sufficient for termwise preservation of the
old determinant content at all primes except 41.  It is not claimed necessary
for every possible determinant cancellation, nor for a vector of corrections.
"""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpz, fmpq_poly as Poly, fmpq_mat, arb, arb_mat, arb_poly, ctx
from sympy import nextprime
import zeta35_mixed_moments as mixed
from zeta35_target31 import content_and_primitive, rational_log, primes_to

sys.set_int_max_str_digits(0)


def vp(q,p):
    n,d=abs(int(q.numerator)),int(q.denominator)
    assert n
    ans=0
    while n%p==0:
        n//=p;ans+=1
    while d%p==0:
        d//=p;ans-=1
    return ans


def aq(x):
    return arb(int(x.numerator))/int(x.denominator)


def positive_check(M):
    S=M.tolist()
    for k in range(len(S)):
        d=S[k][k]
        if d<0:
            return dict(positive_definite=False,negative_pivot_index=k,pivot_interval=str(d))
        if not d>0:
            return dict(positive_definite=None,uncertain_pivot_index=k,pivot_interval=str(d))
        for i in range(k+1,len(S)):
            for j in range(i,len(S)):
                S[i][j] -= S[i][k]*S[j][k]/d
                S[j][i] = S[i][j]
    return dict(positive_definite=True,all_positive_pivots=len(S))


def main():
    K,N,h,A5,B=mixed.original.entries(1)
    A3=mixed.shifted_mu3_entries(1)
    A=[a-3*b for a,b in zip(A5,A3)]
    W=Poly(mixed.original.Dpoly(N)**6)
    D=Poly(mixed.original.Dpoly(K))
    E=[((W*Poly([0]*s+[1]))//D)[38] for s in range(2*h-1)]
    Cq=fmpq_mat([[E[i+j] for j in range(h)] for i in range(h)])
    r=Cq.rank();assert r==13
    # Reconstruct Delta(X;c)=sum b_j(X)c^j exactly from degree <= rank(C).
    values=[mixed.original.det_poly(h,[a-c*e for a,e in zip(A,E)],B) for c in range(r+1)]
    inv=fmpq_mat([[Q(c)**j for j in range(r+1)] for c in range(r+1)]).inv()
    polys=[sum((values[c]*inv[j,c] for c in range(r+1)),Poly()) for j in range(r+1)]
    for c in (Q(-1),Q(1,2)):
        assert sum((p*c**j for j,p in enumerate(polys)),Poly()) == \
               mixed.original.det_poly(h,[a-c*e for a,e in zip(A,E)],B)
    contents=[content_and_primitive(p)[0] for p in polys]
    c0=contents[0]
    # Justify that no omitted prime needs a positive protection exponent:
    # b_0 has no prime factor outside this packet, and no b_j denominator does.
    n0,d0=abs(int(c0.numerator)),int(c0.denominator)
    for p in primes_to(200):
        while n0%p==0:
            n0//=p
        while d0%p==0:
            d0//=p
    assert n0==d0==1
    for cc in contents:
        dc=int(cc.denominator)
        for p in primes_to(200):
            while dc%p==0:
                dc//=p
        assert dc==1
    protection={}
    term_valuations={}
    for p in primes_to(200):
        if p==41:
            continue
        original=vp(c0,p)
        vals=[vp(c,p) for c in contents]
        # v_p(b_j c^j)>=v_p(b_0) simultaneously for every j>=1.
        req=max(0,max(-((vals[j]-original)//j) for j in range(1,r+1)))
        if req:
            protection[str(p)]=req
            term_valuations[str(p)]=dict(original=original,coefficients=vals)
    L=math.prod(int(p)**e for p,e in protection.items())
    assert L%41
    residue=3*pow(2,-1,41)%41
    def centered(a):
        a%=41
        return a-41 if a>20 else a
    a0=centered(residue*pow(L,-1,41))
    c_integer=Q(L*a0,41)
    # A single new prime denominator coprime to the protection conductor.
    d=int(nextprime(L))
    assert d>200 and math.gcd(d,L*41)==1
    # nextprime's large-number search alone is not our primality certificate.
    assert fmpz(d).is_prime() == 1
    ad=centered(residue*d*pow(L,-1,41))
    c_rational=Q(L*ad,41*d)
    ctx.prec=14000
    theta=3*arb(3).zeta()+arb(5).zeta()
    H=arb_mat([[aq(A[i+j])+theta*aq(B[i+j]) for j in range(h)] for i in range(h)])
    Hinv=H.inv()
    C=arb_mat([[aq(E[i+j]) for j in range(h)] for i in range(h)])
    rel=Hinv*C
    trace2_unit=(rel*rel).trace()
    rows=[]
    for label,c,newp in [('protected_integer',c_integer,None),('protected_new_denominator',c_rational,d)]:
        assert all(vp(c,int(pp))>=e for pp,e in protection.items())
        assert vp(c,41)==-1 and (int((41*c).numerator)*pow(int((41*c).denominator),-1,41))%41==residue
        ppoly=sum((p*c**j for j,p in enumerate(polys)),Poly())
        content,coeff=content_and_primitive(ppoly)
        trace2=trace2_unit*aq(c)**2
        pd=positive_check(H-C*aq(c))
        if trace2<1:
            assert pd['positive_definite'] is True
        vals={str(p):vp(content/c0,p) for p in primes_to(200) if vp(content/c0,p)}
        if newp:
            vals[str(newp)]=vp(content/c0,newp)
            assert vals[str(newp)] == -r
        for p in primes_to(200):
            if p!=41:
                assert vp(content/c0,p)>=0
        value=arb_poly(coeff)(theta)
        row=dict(label=label,correction=str(c),new_denominator_prime=str(newp) if newp else None,
                 new_denominator_prime_proven=True if newp else None,
                 trace_relative_square_interval=str(trace2),relative_norm_certified=trace2<1,
                 positive_check=pd,log_abs_primitive=float(abs(value).log()),
                 log_abs_primitive_interval=str(abs(value).log()),content=str(content),
                 log_content_gain=float(rational_log(content/c0)),content_gain_valuations=vals,
                 new_denominator_cost=r*math.log(newp) if newp else 0)
        rows.append(row)
        print(label,'log|c|',math.log(abs(int(c.numerator)))-math.log(int(c.denominator)),
              'positive',pd['positive_definite'],'log|P|',row['log_abs_primitive'],
              'contentgain',row['log_content_gain'],flush=True)
    data=dict(status='passed',K=K,N=N,m=6,h=h,p=41,corrected_moment=38,correction_rank=r,
              scalar_conductor=str(L),scalar_conductor_log=math.log(L),protection=protection,
              term_content_valuations=term_valuations,
              bivariate_coefficient_contents=list(map(str,contents)),
              interpolation_check_points=['-1','1/2'],rows=rows,
              scope='One scalar correction direction only. The conductor is a sufficient '
                    'termwise criterion, not an optimal simultaneous congruence bound. '
                    'No asymptotic no-go theorem follows from the finite tests.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2),encoding='utf-8')


if __name__=='__main__':
    main()
