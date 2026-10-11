"""Fixed exact checks accompanying the convexity lower-bound proofs.

Jensen and convexity are proved in the report, not by these finite checks.
No new numeric irrationality theorem, no all-metric lower bound.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import sympy as S

checks=[]
def check(label,value):
    assert bool(value),label
    checks.append(label)

m=S.symbols("m",positive=True)
T0=S.symbols("T0")
a1,a2,d1,d2=S.symbols("a1 a2 d1 d2")
J=T0+a1*d1+a2*d2
corrected=J-(a1*a1*d1+a2*a2*d2)/m
expanded=T0+a1*(1-a1/m)*d1+a2*(1-a2/m)*d2
check("exact discrete convexity numerator rewriting",S.expand(corrected-expanded)==0)

# Exact binomial rewriting; p is the original metric exponent r>1.
p,lam,xx,qq,dd,mu=S.symbols("p lam x q d mu",positive=True)
uu=mu+lam*p*xx**(p-1)
rho_bin=uu+dd
g0=lam*(p-1)*xx**p
tt=g0+qq*dd
original_bin=2*(lam/(p+1)+mu/2+tt)-2/m*(
    qq**2*dd/2+xx*g0-xx**2*(uu-mu)*(S.Rational(1,2)-1/(p*(p+1))))
am=2/(p+1)-p*xx**(p-1)+2*(p-1)*xx**p-p*(p-1)*xx**(p+1)/(m*(p+1))
rewritten_bin=rho_bin+lam*am+dd*(2*qq-qq**2/m-1)
check("binomial exact full numerator rewriting",S.simplify(original_bin-rewritten_bin)==0)
aone=am.subs(m,1)
check("binomial A1 value at one",S.simplify(aone.subs(xx,1))==0)
check("binomial A1 derivative negative-square identity",
      S.simplify(S.diff(aone,xx)+p*(p-1)*xx**(p-2)*(1-xx)**2)==0)
rank_diff=(1-1/m)*(qq**2*dd+lam*p*(p-1)*xx**(p+1)/(p+1))
check("binomial rank-one numerator difference",
      S.simplify(original_bin-original_bin.subs(m,1)-rank_diff)==0)
shift=S.symbols("shift",real=True)
check("binomial auxiliary scaling numerator shifts exactly",
      S.simplify(original_bin.subs(mu,mu+shift)-original_bin-shift)==0)
energy,full_energy,self_energy=S.symbols("energy full_energy self_energy")
raw_m=2*full_energy-self_energy-energy/m
check("raw7.6 rank-one numerator difference",
      S.expand(raw_m-raw_m.subs(m,1)-(1-1/m)*energy)==0)
check("raw7.6 auxiliary scaling numerator shifts exactly",
      S.expand(raw_m.subs({full_energy:full_energy+shift,
                          self_energy:self_energy+shift})-raw_m-shift)==0)

models=[("Krank7",7,F(18,7),F(3)),("Qrank10",10,F(279,100),F(31,10))]
for name,rank,cost,threshold in models:
    check(name+" exact full numerator threshold",F(rank,rank-1)*cost==threshold)
    check(name+" threshold at least three",threshold>=3)

def exp_lower(x,n):
    term=F(1);out=F(1)
    for k in range(1,n+1):
        term=term*x/k;out+=term
    return out

check("rigorous log16 below3",exp_lower(F(3),4)>16)
check("rigorous log16 belowQrank10 cost",exp_lower(F(279,100),12)>16)
check("Möbius cost threshold exceeds log2",exp_lower(F(18,7),8)>2)

z,w,c,b,A,D=S.symbols("z w c b A D")
phi=lambda v:c*v/(1+b*v)
check("exact Mobius difference factorization",
      S.cancel(phi(A*z)-phi(D*w)-c*(A*z-D*w)/((1+b*A*z)*(1+b*D*w)))==0)
check("exact Mobius derivative",S.diff(phi(z),z).subs(z,0)==c)
check("exact Mobius value1 solution",S.cancel(phi(1/(c-b))-1)==0)

# Cross-intersection values for every univalent map are rho+max(log radii).
# These fixed matrices test the stationary equations, not a numeric integral.
for rank in (7,10):
    for xs in ((F(-1,2),F(0)),(F(-2),F(-1,2),F(0)),
               (F(-3),F(-2),F(-1),F(0))):
        size=len(xs)
        rows=[]
        for k in range(1,size):
            delta=xs[k]-xs[k-1]
            row=[]
            for h in range(size):
                beta=(max(xs[h],xs[k])-max(xs[h],xs[k-1]))/delta
                check(f"Mobius intersection slope m{rank} n{size} h{h} k{k}",
                      beta==(1 if h<k else 0))
                row.append(rank*(1 if h<k else 0)-beta)
            rows.append(row)
        rows.append([F(1)]*size)
        matrix=S.Matrix(rows)
        rhs=S.Matrix([0]*(size-1)+[1])
        check(f"Mobius stationary nonsingular m{rank} n{size}",matrix.det()!=0)
        sol=matrix.inv()*rhs
        check(f"Mobius stationary all mass on full radius m{rank} n{size}",
              sol==S.Matrix([0]*(size-1)+[1]))
        check(f"Mobius stationary nonnegative m{rank} n{size}",
              all(v>=0 for v in sol))
        # Any raw weights have C=rho+(1-1/m)sum cumulative_s^2*delta.
        weight_vars=S.symbols(f"s0:{size-1}")
        weights=list(weight_vars)+[1-sum(weight_vars)]
        rho=S.symbols("rho")
        kernel=lambda h,k:rho+S.Rational(max(xs[h],xs[k]).numerator,
                                        max(xs[h],xs[k]).denominator)
        hfull=sum(weights[h]*kernel(h,size-1) for h in range(size))
        selfenergy=sum(weights[h]*weights[k]*kernel(h,k)
                       for h in range(size) for k in range(size))
        accum=[]
        correction=0
        for k in range(1,size):
            cumulative=sum(weights[:k])
            delta=S.Rational((xs[k]-xs[k-1]).numerator,
                             (xs[k]-xs[k-1]).denominator)
            accum.append(cumulative**2*delta)
            correction+=cumulative**2*delta/rank
        raw=2*hfull-selfenergy-correction
        expected=rho+(1-S.Rational(1,rank))*sum(accum)
        check(f"univalent raw-weight identity m{rank} n{size}",
              S.expand(raw-expected)==0)

cc=F(4209,4120);bb=F(80,103)
check("legal common map Mobius coefficient",bb==F(3200,4120))
check("legal common map denominator analytic",abs(bb)<1)
check("legal common map omitted1",abs(cc-bb)<1)
check("legal common map exact omission root coefficient",cc-bb==F(1009,4120))
check("legal common map derivative above1",cc>1)
check("legal common map derivative below2",cc<2)

result={
    "status":"exact_level20_convexity_checks_passed",
    "fixed_check_count":len(checks),
    "checks":checks,
    "proven_lower_bound_scope":[
        "plain Bost-Charles double integral",
        "Theorem7.1.6 with slopes0..m",
        "Theorem7.1.10 with area0..m",
        "Theorem7.6.4 with nonnegative stationary weights",
        "raw(7.6.2) nonnegative weights for every univalent map and m>1",
        "Theorem7.1.13 legal binomial metrics, auxiliary scaling handles all rho",
        "raw(7.6.2) nonnegative weights when beta_last<=1",
        "corresponding embedding averages of these exact numerators"
    ],
    "lower_bound":"corrected_numerator >= log_abs_phi_derivative0",
    "necessary_thresholds":{"Krank7":"3","Qrank10":"31/10"},
    "mobius_numerator":"exactly log_abs_phi_derivative0",
    "not_proved":[
        "arbitrary nonstationary raw(7.6.2) weights lower bound for nonunivalent maps with beta_last>1",
        "all multimap or Hermitian metric lower bound",
        "new numerical irrationality",
        "the full number-field convexity theorem"
    ]
}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"fixed_check_count":len(checks)}))
