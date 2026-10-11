"""Fixed exact checks for the mixed-gauge filtration, not a parameter scan.

The report proves every sufficiently large prime by coefficient packets and
finite-dimensional filtrations. These checks include a moved target packet,
a cancelled first logarithmic packet, and the global rational inequalities.
No frozen producer is imported or executed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb, factorial
import hashlib
import json

HERE=Path(__file__).resolve().parent

def mul(a,b,N):
    return [sum((a[j]*b[n-j] for j in range(n+1)),F(0)) for n in range(N+1)]

def compose(a,b,N):
    ans=[F(0)]*(N+1)
    power=[F(1)]+[F(0)]*N
    for c in a[:N+1]:
        ans=[v+c*w for v,w in zip(ans,power)]
        power=mul(power,b,N)
    return ans

def inv_unit(a,N):
    assert a[0]==1
    out=[F(1)]+[F(0)]*N
    for n in range(1,N+1):
        out[n]=-sum((a[j]*out[n-j] for j in range(1,n+1)),F(0))
    return out

def vp(q,p):
    if not q:
        return None
    a,b=q.numerator,q.denominator
    v=0
    while a%p==0:
        a//=p;v+=1
    while b%p==0:
        b//=p;v-=1
    return v

def mod(q,p):
    assert q.denominator%p
    return (q.numerator%p)*pow(q.denominator,-1,p)%p

def harmonic(n):
    return sum((F(1,j) for j in range(1,n+1)),F(0))

def sigma(n,k):
    return sum(d**k for d in range(1,n+1) if n%d==0)

# Actual eta coordinate from the independently established level12 model.
N=17
eta_exponents={1:-3,2:2,3:1,4:-1,6:-2,12:3}
prod=[F(1)]+[F(0)]*N
for d,e in eta_exponents.items():
    for k in range(1,N//d+1):
        step=d*k
        factor=[F(0)]*(N+1)
        for j in range(N//step+1):
            if e>=0:
                factor[j*step]=F((-1)**j*comb(e,j)) if j<=e else F(0)
            else:
                factor[j*step]=F(comb(-e+j-1,j))
        prod=mul(prod,factor,N)
xq=[F(0)]+prod[:N]
x2=mul(xq,xq,N)
den=[F(1)]+[F(0)]*N
den=[v+8*a+12*b for v,a,b in zip(den,xq,x2)]
tq=mul(xq,inv_unit(den,N),N)
assert tq[:4]==[F(0),F(1),F(-5),F(11)]
qt=[F(0),F(1)]+[F(0)]*(N-1)
for n in range(2,N+1):
    qt[n]=-compose(tq,qt,N)[n]
assert compose(tq,qt,N)==[F(0),F(1)]+[F(0)]*(N-1)
assert all(q.denominator==1 for q in qt)
assert qt[:4]==[F(0),F(1),F(5),F(39)]

F8_weights={1:4,2:-2288,3:46332,4:-146432,6:185328,12:-82944}
aq=[F(-1727)]+[F(-504*sigma(n,5)+(1728*504*sigma(n//12,5) if n%12==0 else 0)) for n in range(1,N+1)]
f7=[F(0)]+[F(sum(u*sigma(n//d,7) for d,u in F8_weights.items() if n%d==0),n**7) for n in range(1,N+1)]
Hq=mul(aq,f7,N)
Ht=compose(Hq,qt,N)
At=compose(aq,qt,N)
assert At[1]==-504 and At[2]==-19152

# A derivative filter deliberately kills the r=1 target packet, but r=2
# remains. A genuine logarithmic mixed term is included in the same row.
p=13
M=N+8
L=[F(0)]+[F(1,n) for n in range(1,M+1)]
T=[[F(1)]+[F(0)]*M]
for j in range(1,10):
    T.append([v/F(j) for v in mul(T[-1],L,M)])
background=[T[9][n+8]+(T[9][n+7] if n+7<=M else F(0))-2*sum(T[2][:n+1],F(0)) for n in range(N+1)]
filtered=[F((n-1)**7)*Ht[n] for n in range(N+1)]
mixed=[a+b for a,b in zip(filtered,background)]
assert vp(Ht[p+1],p)==-7
assert mod(F(p**7)*Ht[p+1],p)==mod(4*At[1],p)
assert vp(filtered[p+1],p)==0
assert vp(mixed[p+2],p)==-7
assert mod(F(p**7)*mixed[p+2],p)==mod(4*At[2],p)
assert all(vp(background[n],p) is None or vp(background[n],p)>=-1 for n in [p+1,p+2])

# A high logarithmic packet: h=T8-t*T7. At a=7 the offset1 cancels,
# while offset2 survives with (L-t)/7! coefficient 1/(2*7!).
p_log=11
a=7
Nlog=a*p_log+2
Llog=[F(0)]+[F(1,n) for n in range(1,Nlog+1)]
Tlog=[[F(1)]+[F(0)]*Nlog]
for j in range(1,9):
    Tlog.append([v/F(j) for v in mul(Tlog[-1],Llog,Nlog)])
hlog=[Tlog[8][n]-(Tlog[7][n-1] if n else F(0)) for n in range(Nlog+1)]
assert vp(hlog[a*p_log+1],p_log)>=-6
assert vp(hlog[a*p_log+2],p_log)==-7
assert mod(F(p_log**7)*hlog[a*p_log+2],p_log)==mod(F(1,2*factorial(7)),p_log)

# The complete all-r proof has four concave intervals and one eventual
# dimension bound. Every inequality here is exact, not floating-point.
c=F(43,10)
segments=[(10,20,F(29,10)),(20,30,F(359,100)),
          (30,45,F(399,100)),(45,70,F(439,100))]
segment_checks=[]
for lo,hi,h in segments:
    assert harmonic(lo)>h
    def numerator(r):
        return r*(r+2)*h-F(r*(r+5),2)+7*(14*r+63)-c*(r+8)**2
    assert h<c+F(1,2)
    assert numerator(lo)>0 and numerator(hi)>0
    segment_checks.append({'lo':lo,'hi':hi,'harmonic_lower':str(h),
                           'endpoint_values':[str(numerator(lo)),str(numerator(hi))]})
assert harmonic(235)<7
assert harmonic(70)>F(483,100)
assert harmonic(56)>F(23,5)
assert F(7*(14*10+63),(10+8)**2)>c
assert F(23,5)*(1-F(57**2,244**2))>c
assert sum((F(41,10)**k/factorial(k) for k in range(16)),F(0))>60

md=HERE/'cdt_odd_mixed_filtration_20261005.md'
payload={
    'scope':'Fixed exact examples and rational endpoints; full-scale proof is in the report.',
    'all_checks_passed':True,
    'actual_coordinate':{'tq_first':[str(v) for v in tq[:4]],'qt_first':[str(v) for v in qt[:4]],'integer_inverse':True},
    'mixed_target_example':{'p':p,'operator':'(theta-1)^7',
        'background':'(1+t)*t^(-8)*T9-2*T2/(1-t)',
        'A1':str(At[1]),'A2':str(At[2]),
        'H_at_p1_valuation':vp(Ht[p+1],p),
        'filtered_at_p1_valuation':vp(filtered[p+1],p),
        'mixed_at_p2_valuation':vp(mixed[p+2],p),
        'mixed_at_p2_scaled_residue':mod(F(p**7)*mixed[p+2],p)},
    'logarithmic_offset_cancellation':{'p':p_log,'a':7,'row':'T8-t*T7',
        'valuation_at_7p1':vp(hlog[a*p_log+1],p_log),
        'valuation_at_7p2':vp(hlog[a*p_log+2],p_log),
        'scaled_residue_at_7p2':mod(F(p_log**7)*hlog[a*p_log+2],p_log)},
    'all_r_flat_lower':'43/10','exact_concave_intervals':segment_checks,
    'report_sha256':hashlib.sha256(md.read_bytes()).hexdigest() if md.exists() else None,
    'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(HERE/'cdt_odd_mixed_filtration_20261005_verify.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_checks_passed':True,'mixed_target_at_p2_valuation':-7,
                  'log_at_7p2_valuation':-7,'all_r_flat_lower':'43/10'},ensure_ascii=False))
