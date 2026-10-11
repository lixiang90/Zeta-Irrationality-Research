"""Exact-rational enclosures for a variational obstruction, no numerical quadrature.

Analytic lemma (proved in restart_analysis.md): for any admissible comparison rho,
 lambda*sup(2 U_rho - V)-I(rho)+Cstar >= I(sigma)-int V d sigma+Cstar.
Here sigma is uniform of mass lambda on [0,4/25]. This does not bound the
optimal arithmetic normalizer; it rules out fixing the REPORTED bound by rho alone.
All transcendental enclosures below use finite rational series with explicit tails.
"""
from fractions import Fraction as F
from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class IV:
    lo: F
    hi: F

    def __add__(self, other):
        other=iv(other)
        return IV(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self): return IV(-self.hi,-self.lo)
    def __sub__(self,other): return self+-iv(other)
    def __rsub__(self,other): return iv(other)+-self
    def __mul__(self,other):
        other=iv(other)
        v=[a*b for a in (self.lo,self.hi) for b in (other.lo,other.hi)]
        return IV(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,other):
        other=iv(other)
        assert other.lo*other.hi>0
        return self*IV(1/other.hi,1/other.lo)


def iv(x): return x if isinstance(x,IV) else IV(F(x),F(x))


def log_reduced(x,n=40):
    assert 1<=x<=2
    z=(x-1)/(x+1)
    value=2*sum((z**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    tail=2*z**(2*n+1)/(F(2*n+1)*(1-z*z))
    return IV(value,value+tail)


LOG2=log_reduced(F(2))
def log_iv(x):
    x=F(x); assert x>0
    k=0
    while x<1: x*=2; k-=1
    while x>=2: x/=2; k+=1
    return log_reduced(x)+k*LOG2


def atan_small(x,n=60):
    x=F(x); assert abs(x)<=F(1,2)
    if x<0: return -atan_small(-x,n)
    value=sum(((-1)**k*x**(2*k+1)/F(2*k+1) for k in range(n)),F(0))
    next_value=value+(-1)**n*x**(2*n+1)/F(2*n+1)
    return IV(min(value,next_value),max(value,next_value))


PI=16*atan_small(F(1,5))-4*atan_small(F(1,239))
def atan_iv(x):
    x=F(x)
    if x<0: return -atan_iv(-x)
    if x>1: return PI/2-atan_iv(1/x)
    if x>F(1,2): return PI/4+atan_small((x-1)/(x+1))
    return atan_small(x)


def double_integral(c,s):
    # int_0^(s^2) int_0^c log(t+u^2) du dt.
    D=s*s
    return ((D*c+c**3/3)*log_iv(D+c*c)-c**3/3*log_iv(c*c)
            -F(7,3)*D*c+F(4,3)*s**3*atan_iv(c/s))


def primal_bound(alpha,s=F(2,5),beta=8):
    lam=1-alpha; D=s*s
    mean=F(4,3)*PI*s+(double_integral(F(1),s)-beta*double_integral(alpha,s))/D
    C=-2*lam+2*beta*alpha*lam*(1-log_iv(alpha))+3*lam*lam-2*lam*lam*log_iv(2*lam)
    return lam*lam*(log_iv(D)-F(3,2))-lam*mean+C


def outward_decimal(x,places=12):
    den=10**places
    low=x.lo.numerator*den//x.lo.denominator
    high=-((-x.hi.numerator*den)//x.hi.denominator)
    assert F(low,den)<=x.lo<=x.hi<=F(high,den)
    return [str(F(low,den)),str(F(high,den))]


def run():
    folder=Path(__file__).parent
    specs={F(r["al"]):F(*r["Aeff"]) for r in json.loads((folder/"aeff_scan.json").read_text())}
    specs[F(1,40)]=F(5715056524986876059171,1669030017063552000000)
    specs[F(3,40)]=F(137743476530383649272771363,70835302954194210432000000)+F(37,2000)
    rows=[]
    for alpha,A in sorted(specs.items()):
        B=primal_bound(alpha)
        assert B.hi-B.lo<F(1,10**25)
        gap=A+B
        assert gap.lo>0
        # Exact integral of the ENTIRE outer rank-loss term on the current range.
        rank=(F(1,2)*(1+6*alpha)-F(1,3))**2
        assert (gap-rank).lo>0
        row=dict(alpha=str(alpha),lam=str(1-alpha),test_interval=["0","4/25"],
                 A=str(A),B_interval=outward_decimal(B),gap_interval=outward_decimal(gap),
                 full_rank_term=str(rank),remaining_gap_interval=outward_decimal(gap-rank))
        rows.append(row)
        print(f"alpha={alpha}: B in {outward_decimal(B)}, A+B >= {float(gap.lo):.9f}; "
              f"after deleting all rank loss >= {float((gap-rank).lo):.9f}")
    out=dict(status="exact rational interval calculation; analytic lemma written, not Lean formalized",
             pi_interval=outward_decimal(PI),rows=rows)
    (folder/"restart_obstruction_certificate.json").write_text(json.dumps(out,indent=2),encoding="utf-8")


if __name__=="__main__": run()
