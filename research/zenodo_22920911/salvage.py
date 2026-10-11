"""Validated real bounds salvaged from the paper, using 160-bit Arb balls.

Does not use, or prove, the article's claimed determinant decay.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from flint import arb, ctx

ctx.prec=160
def A(q):
    q=F(q)
    return arb(q.numerator)/arb(q.denominator)

alpha=F(3,40)
lam=1-alpha
lengths=list(map(F,['.87','.8','.7','.6','.5','.4','.3','.25','.2','.15','.12','.1','.08','.06','.04','.02']))
weights=list(map(F,['.1','.08','.06']+['.05']*11+['.015','.12']))


def potential(t):
    t=F(t)
    out=arb(0)
    for L,c in zip(lengths,weights):
        u=(A(L)/4).log() if t<=L else ((A(t)-A(L)/2+(A(t)*A(t-L)).sqrt())/2).log()
        out+=A(c)*u
    return out


def field(t):
    t=F(t)
    if not t:
        return -2-16*A(alpha)*A(alpha).log()+16*A(alpha)
    s=A(t).sqrt()
    return (1+A(t)).log()-8*A(alpha)*(A(t)+A(alpha)**2).log()-2+16*A(alpha)+2*s*(arb.pi()+(1/s).atan()-8*(A(alpha)/s).atan())


def phi_prime(t):
    s=A(t).sqrt()
    return 2*(arb.pi()+(1/s).atan()-8*(A(alpha)/s).atan())


def certify_measure():
    ql,qr=F(13415500,10**9),F(13415502,10**9)
    assert phi_prime(ql)<0 and phi_prime(qr)>0
    # Phi'' changes sign once; Phi' starts at -5*pi and tends to 2*pi.
    # Hence the bracket contains the unique minimum of V.
    factor=arb.pi()+(1/A(qr).sqrt()).atan()-8*(A(alpha)/A(ql).sqrt()).atan()
    assert factor<0
    vstar=(1+A(ql)).log()-8*A(alpha)*(A(qr)+A(alpha)**2).log()-2+16*A(alpha)+2*A(qr).sqrt()*factor
    ends=sorted(set([F(0),ql,qr]+lengths+[lengths[0]+(F(2)-lengths[0])*F(k,8) for k in range(9)]))
    rows=[]
    for l,r in zip(ends,ends[1:]):
        vmin=field(r) if r<=ql else field(l) if l>=qr else vstar
        bound=2*potential(r)-vmin
        assert bound<A(-F(109,20))
        rows.append(dict(left=str(l),right=str(r),upper_bound=str(bound)))
    # Corrected version of (99): 2*lambda-1+8*alpha=29/20,
    # not the paper's 13/10. Use J_alpha <= alpha*log(t)+alpha^3/(3t).
    at2=A(1+6*alpha)*A(2).log()+8*A(alpha)**3/6-2*arb.pi()*A(2).sqrt()
    assert at2<A(-F(109,20))
    # Derivative after multiplication by t is <=29/20-pi*sqrt(t)<0.
    I=sum(A(weights[i]*weights[j])*(A(max(lengths[i],lengths[j]))/4).log()
          for i in range(16) for j in range(16))
    C=-2*A(lam)+16*A(alpha*lam)*(1-A(alpha).log())+3*A(lam)**2-2*A(lam)**2*(2*A(lam)).log()
    U=-A(lam)*A(F(109,20))-I+C
    assert U<A(F(557,1000))
    return dict(status='M=-5.45 independently certified for the printed measure',
                intervals=rows,energy=str(I),real_bound=str(U),
                valid_rational_real_bound='557/1000',
                potential_at_paper_claimed_max=str(2*potential(F(2648,10000))-field(F(2648,10000))))


def kappa(a,b):
    aa,bb=A(a),A(b)
    Y=(2+aa+bb)/(bb-aa)
    return 2*arb.pi()*bb.sqrt()+(1+bb).log()-8*A(alpha)*aa.log()+A(lam)*(1-A(alpha*lam).log())+2*A(lam)*(Y+(Y**2-1).sqrt()).log()


def norm_bound():
    original=kappa(F(1,18),F(1,3))
    improved=kappa(F(159,2000),F(177,500))
    assert original<A(F(14301,1000))
    assert improved<A(F(3567,250))  # 14.268; strict slack absorbs K^3.
    return dict(original_kappa=str(original),improved_kappa=str(improved),
                interval=['159/2000','177/500'],rho='3567/250',
                lambda_times_rho=str(lam*F(3567,250)),
                necessary_max_uniform_decay=str(lam*F(3567,250)/2),
                status='valid relative norm exponent; no irrationality measure follows without valid quadratic decay')


if __name__=='__main__':
    result=dict(measure=certify_measure(),norm=norm_bound())
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({**result,'measure':{k:v for k,v in result['measure'].items() if k!='intervals'}},indent=2))
