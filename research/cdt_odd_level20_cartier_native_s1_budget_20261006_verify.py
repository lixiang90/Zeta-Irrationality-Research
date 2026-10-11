"""Exact, fixed native-S1 threshold account; no prime or denominator-family scan."""
from fractions import Fraction as F
from pathlib import Path
import math
import json

labels=[]


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    labels.append(label)


def harmonic(n):
    return sum((F(1,k) for k in range(1,n+1)),F(0))


def clamp(x):
    return min(F(1),max(F(0),x))


def i19(x):
    if x<=1:
        return F(3,2)+18*harmonic(17)+harmonic(18)/2-19*x+x*x/2
    return (
        sum((max(F(0),F(18)-k*x)/k for k in range(1,19)),F(0))
        +sum((clamp(F(19)-k*x)**2/(2*k) for k in range(1,19)),F(0))
    )


def gh(x,h):
    lower=F(18,h)
    upper=F(19,h)
    if x<=lower:
        return F(0)
    if x<=upper:
        return F(h,2)*(x-lower)**2
    return x-F(37,2*h)


def g(x):
    return sum((gh(x,h) for h in range(1,7)),F(0))


m=19
flat=F(963,361)
h14=harmonic(14)
h11=harmonic(11)
p14=F(37,2)*h14
p11=F(37,2)*h11
gamma=F(5,6)
k0=flat+F(2,361)*(p14-gamma)
x0=F(9,7)
k_local=k0-F(2,361)*3*x0
gate_local=F(19,18)*k_local
check("Old fixed table exact kappa",k0==F(389780201,130089960))
check("Same old cutoff S1 mass twenty-seven-sevenths",3*x0==F(27,7))
check("Local optimistic kappa",k_local==F(387000281,130089960))
check("Local optimistic necessary geometry",gate_local==F(387000281,123243120))
check("Local optimistic gate above fourteen-fifths",gate_local>F(14,5))

check("Six slope onsets have smallest three",min(F(18,h) for h in range(1,7))==3)
check("Raw length area at nineteen",g(F(19))==F(2747,40))
for h in range(1,7):
    lower=F(18,h)
    upper=F(19,h)
    check(f"Ramp {h} starts with zero area",gh(lower,h)==0)
    check(f"Ramp {h} area formula joins",F(h,2)*(upper-lower)**2==upper-F(37,2*h))

# Polynomial coefficients of clamp(z)+clamp(1-z), in all three regions.
pieces=[((0,0),(0,1)),((1,0),(-1,1)),((0,1),(0,0))]
for index,(first,second) in enumerate(pieces):
    check(f"Clamp complementary identity region {index}",first[0]+second[0]==0 and first[1]+second[1]==1)
check("All k>=7 I derivative terms vanish for xi>=3",19-7*3<0)
check("P19 minus G derivative eight",14-6==8)
check("P19 minus three-xi minus G derivative five",14-3-6==5)

left=F(19,12)
right=F(18,11)
check("Optimistic plateau within actual matching window",1<left<right<2)
check("Harmonic eleven",h11==F(83711,27720))
for name,x in (("left",left), ("right",right)):
    check(f"Plateau {name}: eleven active terms",all(19-k*x>=1 for k in range(1,12)))
    check(f"Plateau {name}: twelve onward inactive",all(19-k*x<=0 for k in range(12,19)))
    check(f"Plateau {name}: direct I formula",11*x+i19(x)==p11)
    check(f"Plateau {name}: no raw length credit",g(x)==0)
check("Small xi derivative negative",11-19+1<0)
kappa_over=flat+F(2,361)*(p11-gamma)
gate_over=F(19,18)*kappa_over
check("All-xi optimistic kappa",kappa_over==F(29745467,10006920))
check("All-xi optimistic geometry gate",gate_over==F(29745467,9480240))
check("Gate minus fourteen-fifths",gate_over-F(14,5)==F(640159,1896048))

# Strict logarithm interval, using only rational positive Taylor bounds.
log_lower=F(693,250)
log_upper=F(2773,1000)
degree=20
lower_exp_upper=sum((log_lower**j/F(math.factorial(j)) for j in range(degree+1)),F(0))
lower_exp_upper+=log_lower**(degree+1)/F(math.factorial(degree+1))/(1-log_lower/F(degree+2))
upper_exp_lower=sum((log_upper**j/F(math.factorial(j)) for j in range(degree+1)),F(0))
check("Geometric tail ratio less than one",log_lower<F(degree+2))
check("exp(2.772) strictly below sixteen",lower_exp_upper<16)
check("exp(2.773) strictly above sixteen",upper_exp_lower>16)
req_lower=p14-gamma+F(963,2)-171*log_upper
req_upper=p14-gamma+F(963,2)-171*log_lower
check("Required extra gamma lower endpoint",req_lower==F(1200675731,18018000))
check("Required extra gamma upper endpoint",req_upper==F(1203756809,18018000))
check("Positive required interval",F(66)<req_lower<req_upper<F(67))
check("Density lower at original cutoff",req_lower/x0==F(1200675731,23166000)>51)
check("Three direction depth seventeen insufficient",3*17*x0<req_lower)
check("Three direction depth eighteen clears necessary interval only",3*18*x0>req_upper)
check("Six direction depth eight insufficient",6*8*x0<req_lower)
check("Six direction depth nine clears necessary interval only",6*9*x0>req_upper)
check("All six directions capped at four in matching window insufficient",6*4*2<req_lower)
check("Three S1 directions require window above twenty-two",req_lower/3==F(1200675731,54054000)>22)
check("Six depth-four directions require window beyond matching",req_lower/24==F(1200675731,432432000)>F(277,100))

# Same nine species, p<=2D, cap four: old H baseline is already counted.
support_extra_floor=3*(4-1)+6*(4-0)
support_total_credit=2*support_extra_floor
kappa_support=flat+F(2,361)*(p14-support_total_credit)
gate_support=F(19,18)*kappa_support
check("Nine-species extra capped floor per monomial",support_extra_floor==33)
check("All matching-window capped credit includes old gain",support_total_credit==66)
check("Support ceiling optimistic kappa",kappa_support==F(342813281,130089960))
check("Support ceiling necessary geometry",gate_support==F(342813281,123243120))
check("Support gate strictly above logarithm upper bound",gate_support-log_upper==F(26502731,3081078000)>0)
check("Support gate is below fourteen-fifths",gate_support<F(14,5))

payload={
    "scope":"One fixed rank19 unit account, conditional native net gain and strictly more optimistic all-xi credit. No prime scan, no nonordinary-density assumption, no new global net-height theorem.",
    "checks_passed":len(labels),
    "check_labels":labels,
    "local_cutoff":str(x0),
    "local_S1_mass_upper":str(3*x0),
    "local_kappa_optimistic":str(k_local),
    "local_geometry_gate":str(gate_local),
    "raw_length_area_at_19":str(g(F(19))),
    "optimistic_minimizer_interval":[str(left),str(right)],
    "all_xi_optimistic_kappa":str(kappa_over),
    "all_xi_optimistic_gate":str(gate_over),
    "log16_strict_interval":[str(log_lower),str(log_upper)],
    "required_extra_gamma_strict_interval":[str(req_lower),str(req_upper)],
    "same_support_cap4_credit_upper":support_total_credit,
    "same_support_cap4_optimistic_kappa":str(kappa_support),
    "same_support_cap4_geometry_gate":str(gate_support),
    "unproved_inputs":[
        "Native first-layer floor's exact identification with original CDT global net-height gain",
        "Any actual nonordinary density",
        "Unknown small-prime cross-residue polynomial kernels",
        "New second or higher Smith layers",
        "Cross-background, outside-window or above-cap credit is outside the same-support ceiling",
    ],
}
destination=Path(__file__).with_suffix(".json")
destination.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"checks_passed":len(labels),"certificate":str(destination)},ensure_ascii=False))
