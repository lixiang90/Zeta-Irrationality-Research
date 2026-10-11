"""Exact content-preserving CRT for one rank-four pure zeta(7) correction.

This is a bounded test of a full determinant polynomial.  It is not an
asymptotic construction, and the termwise conductor is sufficient only.
"""
import json,math,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat,arb,arb_mat,arb_poly,ctx
from sympy import primerange
import b8_hankel as b8
from joint_exact import determinant,content
from zeta7_moment_extension_20261004 import aq,vp,positive_pivots,ball

sys.set_int_max_str_digits(0)


def main():
    K,N,h,A,B=b8.entries(1)
    W=Poly(b8.Dpoly(N)**8);D=Poly(b8.Dpoly(K))
    E=[((W*Poly([0]*s+[1]))//D)[53] for s in range(2*h-1)]
    Cq=fmpq_mat([[E[i+j] for j in range(h)] for i in range(h)])
    rank=Cq.rank();assert rank==4
    vals=[determinant([a-c*e for a,e in zip(A,E)],B,h) for c in range(rank+1)]
    inv=fmpq_mat([[Q(c)**j for j in range(rank+1)] for c in range(rank+1)]).inv()
    polynomials=[sum((vals[c]*inv[j,c] for c in range(rank+1)),Poly()) for j in range(rank+1)]
    for c in [Q(-1),Q(1,2)]:
        assert sum((v*c**j for j,v in enumerate(polynomials)),Poly())==determinant([a-c*e for a,e in zip(A,E)],B,h)
    contents=[content(poly) for poly in polynomials];c0=contents[0]
    primes=list(primerange(2,200))
    n0,d0=abs(int(c0.numerator)),int(c0.denominator)
    for p in primes:
        while n0%p==0:n0//=p
        while d0%p==0:d0//=p
    assert n0==d0==1
    for ct in contents:
        d=int(ct.denominator)
        for p in primes:
            while d%p==0:d//=p
        assert d==1
    protect={}
    for p in primes:
        if p==19:continue
        v0=vp(c0,p)
        required=max(0,max(-((vp(contents[j],p)-v0)//j) for j in range(1,rank+1)))
        if required:protect[str(p)]=required
    L=math.prod(int(p)**e for p,e in protect.items())
    # 19*c == 3 modulo 19 removes the bad principal part of moment 53.
    u=3*pow(L,-1,19)%19
    if u>9:u-=19
    c=Q(L*u,19)
    assert (int((19*c).numerator)*pow(int((19*c).denominator),-1,19))%19==3
    assert all(vp(c,int(p))>=e for p,e in protect.items())
    poly=sum((v*c**j for j,v in enumerate(polynomials)),Poly())
    assert poly==determinant([a-c*e for a,e in zip(A,E)],B,h)
    ct=content(poly);gain=ct/c0
    assert all(vp(gain,p)>=0 for p in primes if p!=19)
    ctx.prec=16000;z=arb(7).zeta()
    H=arb_mat([[aq(A[i+j])+z*aq(B[i+j]) for j in range(h)] for i in range(h)])
    C=arb_mat([[aq(E[i+j]) for j in range(h)] for i in range(h)])
    rel=H.inv()*C;trace2=(rel*rel).trace()*aq(c)**2
    pd=positive_pivots(H-C*aq(c))
    # Every integer numerator satisfying the congruence is u+19k.  The
    # nearest coefficient on the other side of zero also gives an indefinite
    # Gram matrix.  Positive definiteness of H-cC is an interval in real c,
    # since the positive definite cone is convex.  Hence these two failures
    # rule out this whole termwise-protected integer numerator family.
    u_other=u-19 if u>0 else u+19
    c_other=Q(L*u_other,19)
    pd_other=positive_pivots(H-C*aq(c_other))
    primitive=poly/ct;value=arb_poly([int(q) for q in primitive])(z)
    original=arb_poly([int(q) for q in polynomials[0]/c0])(z)
    ratio=(H-C*aq(c)).det()/H.det()
    data=dict(status='passed',K=K,N=N,h=h,corrected_moment=53,p=19,rank=rank,
              scalar_conductor=str(L),scalar_conductor_log=math.log(L),protection=protect,
              scalar_correction=str(c),scalar_correction_log=float(aq(abs(c)).log()),
              bivariate_coefficient_contents=list(map(str,contents)),
              trace_relative_square_interval=ball(trace2),relative_norm_certified=bool(trace2<1),
              positive_check=pd,determinant_ratio_interval=ball(ratio),
              opposite_nearest_scalar_correction=str(c_other),
              opposite_nearest_positive_check=pd_other,
              protected_integer_family_has_no_positive_gram=(pd['positive_definite'] is False and pd_other['positive_definite'] is False),
              content_ratio=str(gain),content_gain_valuations={str(p):vp(gain,p) for p in primes if vp(gain,p)},
              log_content_gain_interval=ball(aq(gain).log()),
              baseline_log_primitive_interval=ball(original.log()),
              modified_log_abs_primitive_interval=ball(abs(value).log()),
              primitive_improvement_interval=ball(original.log()-abs(value).log()),
              modified_target_positive=bool(value>0),
              scope='K40N3h37 and one moment only. The sufficient conductor protects all '
                    'old content termwise; no asymptotic or minimality claim is made.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    print('Llog',math.log(L),'clog',data['scalar_correction_log'],'relative',data['relative_norm_certified'],
          'positive',pd['positive_definite'],'gain',data['log_content_gain_interval'],
          'logP',data['modified_log_abs_primitive_interval'],flush=True)


if __name__=='__main__':main()
