"""Exact certificates for odd, even-character targets.

No zeta/L-value evaluation, prime scan, or numerical independence assumption.
The all-scale results are proved in the companion note; these are fixed checks.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd, lcm, factorial
from functools import lru_cache
import hashlib
import json
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

HERE = Path(__file__).resolve().parent
x, y, t, u, z = S.symbols('x y t u z')
checks = []
def check(name, ok):
    assert ok, name
    checks.append(name)
def ser(expr, var, N):
    p = S.series(expr, var, 0, N + 1).removeO().expand()
    return [Q(p.coeff(var, n)) for n in range(N + 1)]
def mul(a, b, N):
    return [sum((a[k] * b[n-k] for k in range(n+1)), Q(0))
            for n in range(N+1)]
def compose(a, b, N):
    out = [Q(0)]*(N+1)
    power = [Q(1)]+[Q(0)]*N
    for c in a[:N+1]:
        for n in range(N+1): out[n] += c*power[n]
        power = mul(power, b, N)
    return out
def pol(a, var):
    return sum((S.Rational(c.numerator, c.denominator)*var**n
                for n,c in enumerate(a)), S.Rational(0))
def L(N): return lcm(*range(1,N+1)) if N else 1
def content_den(a, D):
    ints = [int(D*c) for c in a]
    check('safe denominator is integral', all((D*c).denominator == 1 for c in a))
    h = D
    for v in ints: h = gcd(h, abs(v))
    actual = lcm(*(c.denominator for c in a))
    check('complete scalar content formula', actual == D//h)
    return {'safe_D':str(D), 'complete_h':str(h), 'actual_delta':str(actual)}

# The named genuinely noncritical character: chi_5=(0,1,-1,-1,1).
chi = [0,1,-1,-1,1]
P = sum(chi[a]*x**a for a in range(1,5))
G0 = S.cancel(P/(1-x**5))
check('chi5 rational forcing', S.cancel(G0-x*(1-x*x)/(1+x+x*x+x**3+x**4)) == 0)
check('chi5 true reciprocal antisymmetry', S.cancel(G0+G0.subs(x,1/x)) == 0)
g = -1/(u*u+5*u+5)
check('chi5 quotient rational forcing', S.cancel(G0/(x-1/x)-g.subs(u,x+1/x-2)) == 0)
scaled = S.cancel(G0.subs(x,1+5*y))
expected = -y*(1+5*y)*(2+5*y)/(1+10*y+50*y*y+125*y**3+125*y**4)
check('chi5 integral basepoint-one scale', S.cancel(scaled-expected) == 0)

# A few fixed even, unit-supported, mean-zero forcings; no modulus scan.
fixed_weights = {
    5: [0,1,-1,-1,1],
    7: [0,1,-1,0,0,-1,1],
    8: [0,1,0,-1,0,-1,0,1],
}
for q,c in fixed_weights.items():
    pq = sum(c[a]*x**a for a in range(1,q))
    check(f'period {q}: double zero of P at 1', pq.subs(x,1)==0 and S.diff(pq,x).subs(x,1)==0)
    cq = S.div(pq,1-x,x)[0]
    bq = sum(x**a for a in range(q))
    cn = S.Poly(S.expand(cq.subs(x,1+q*y)/q),y)
    bn = S.Poly(S.expand(bq.subs(x,1+q*y)/q),y)
    check(f'period {q}: normalized integral numerator', all(v.q==1 for v in cn.all_coeffs()))
    check(f'period {q}: normalized integral unit denominator',
          all(v.q==1 for v in bn.all_coeffs()) and bn.eval(0)==1)
    check(f'period {q}: exact reciprocal identity', S.cancel(pq/(1-x**q)+(pq/(1-x**q)).subs(x,1/x))==0)

# Zero-initial-jet system J_j: theta J_1=G0, theta J_j=J_(j-1).
N=20
omega=[Q(5*(-5)**n) for n in range(N+1)]
forcing=ser(scaled,y,N)
rows={}
prev=forcing
for j in range(1,6):
    rhs=mul(omega,prev,N)
    row=[Q(0)]+[rhs[n-1]/n for n in range(1,N+1)]
    rows[j]=row
    for n in range(1,N+1):
        check(f'J{j} coefficient {n}: fine integer row',
              (n*L(n-1)**(j-1)*row[n]).denominator==1)
    prev=row
check('J1 leading term',rows[1][2]==-5)
check('J2 leading term',rows[2][3]==Q(-25,3))
check('J3 leading term',rows[3][4]==Q(-125,12))
prefix={str(j):content_den(rows[j][:17],L(16)**j) for j in range(1,6)}

# Exact cyclic determinant, with theta=x*d/dx; it does not assume L_s irrational.
cyclic={}
for s in (3,5):
    A=S.zeros(s+1)
    A[1,0]=G0
    for j in range(2,s+1): A[j,j-1]=1
    rr=S.zeros(1,s+1);rr[0,s]=1
    mat=[]
    for k in range(s+1):
        mat.append(list(rr))
        rr=rr.applyfunc(lambda v:x*S.diff(v,x))+rr*A
    det=S.factor(S.Matrix(mat).det())
    check(f'weight {s}: cyclic determinant',S.cancel(det-(-1)**(s*(s+1)//2)*G0)==0)
    cyclic[str(s)]=str(det)

# Actual local odd jets, with formal (not numerically evaluated) periods.
Ls=S.symbols('L1:6')
Ft=S.series(G0.subs(x,S.exp(t)),t,0,11).removeO().expand()
check('forcing is odd in logarithmic coordinate to checked order',
      all(Ft.coeff(t,n)==0 for n in range(0,11,2)))
local={}
for s in (3,5):
    zerojet=sum(Ft.coeff(t,n)*S.Rational(factorial(n),factorial(n+s))*t**(n+s)
                for n in range(0,11) if n+s<=10)
    original=sum(Ls[s-h-1]*t**h/S.factorial(h) for h in range(s))+zerojet
    critical=sum(Ls[2*k-1]*t**(s-2*k)/S.factorial(s-2*k)
                 for k in range(1,s//2+1))
    K=S.expand(original-critical)
    check(f'weight {s}: critical-only reflection leaves lower odd periods',
          S.expand(K.subs(t,-t)-K)==0)
    check(f'weight {s}: lower L1 coefficient',K.coeff(t,s-1)==Ls[0]/S.factorial(s-1))
    if s==5: check('weight 5: lower L3 coefficient',K.coeff(t,2)==Ls[2]/2)
    local[str(s)]=str(K)

# Genuine reciprocal quotient and a complete, deliberately coarse integer model.
# u=400*w, w=z^2; x=(sqrt(1+100*z^2)+10*z)^2.
Z=17
sqrtcoef=[Q(0)]*(Z+1)
invsqrt=[Q(0)]*(Z+1)
for k in range(Z//2+1):
    sqrtcoef[2*k]=Q(S.binomial(S.Rational(1,2),k)*100**k)
    invsqrt[2*k]=Q(S.binomial(S.Rational(-1,2),k)*100**k)
check('integral square-root series at scale 100',all(c.denominator==1 for c in sqrtcoef+invsqrt))
ysub=[Q(0)]*(Z+1)
for n in range(1,Z+1): ysub[n]=4*sqrtcoef[n-1]
ysub[2]+=40
check('reciprocal quotient exact square relation',
      S.simplify(((S.sqrt(1+100*z*z)+10*z)**2+
                  (S.sqrt(1+100*z*z)-10*z)**2-2)-400*z*z)==0)
check('reciprocal quotient exact v relation',
      S.simplify(((S.sqrt(1+100*z*z)+10*z)**2-
                  (S.sqrt(1+100*z*z)-10*z)**2)-40*z*S.sqrt(1+100*z*z))==0)
comp={j:compose(rows[j][:Z+1],ysub,Z) for j in range(1,6)}
F={};QZ={}
for h in range(3):
    j=2*h+1
    check(f'quotient F{h}: exact even series',all(comp[j][n]==0 for n in range(1,Z+1,2)))
    F[h]=[comp[j][2*n] for n in range(9)]
    check(f'quotient F{h}: complete safe prefix',all((L(16)**j*c).denominator==1 for c in F[h]))
for h in range(1,3):
    j=2*h
    check(f'quotient Z{h}: exact odd numerator',all(comp[j][n]==0 for n in range(0,Z+1,2)))
    divided=[comp[j][n+1] if n+1<=Z else Q(0) for n in range(Z+1)]
    pp=mul(divided,invsqrt,Z)
    QZ[h]=[pp[2*n]/40 for n in range(9)]
    check(f'quotient Z{h}: complete safe prefix',all((40*L(17)**j*c).denominator==1 for c in QZ[h]))
w=S.symbols('w')
fpol={h:pol(a,w) for h,a in F.items()}
zpol={h:pol(a,w) for h,a in QZ.items()}
check('quotient F0 forcing',S.series(S.diff(fpol[0],w)-400*g.subs(u,400*w),w,0,8).removeO()==0)
for h in (1,2):
    check(f'quotient F{h} derivative',S.series(S.diff(fpol[h],w)-400*zpol[h],w,0,8).removeO()==0)
    check(f'quotient Z{h} rational closed system',
          S.series(w*(400*w+4)*S.diff(zpol[h],w)-fpol[h-1]+(400*w+2)*zpol[h],w,0,8).removeO()==0)

# Full joint prefix, rather than a product of row denominators.
NN=8;D=L(NN)**3
B=S.Matrix([[int(D*c) for c in rows[j][:NN+1]] for j in (1,2,3)])
M=B.T.row_join(D*S.eye(NN+1))
SM=smith_normal_form(M,domain=ZZ)
smith=[abs(int(SM[i,i])) for i in range(NN+1)]
joint_index=D**(NN+1)
for v in smith: joint_index//=v
joint={'N':NN,'rows':[1,2,3],'D':str(D),'smith_factors':list(map(str,smith)),
       'joint_index':str(joint_index),
       'product_of_scalar_deltas':str(lcm(*(c.denominator for c in rows[1][:NN+1]))*
                                      lcm(*(c.denominator for c in rows[2][:NN+1]))*
                                      lcm(*(c.denominator for c in rows[3][:NN+1])))}
check('joint index divides product of scalar delta',int(joint['product_of_scalar_deltas'])%joint_index==0)

# Endpoint character/hurwitz projection and exact disjoint-support filter lattice.
projection=S.Matrix([[1,1],[1,-1]])
SN=smith_normal_form(projection,domain=ZZ)
check('chi5 projection finite index exactly two',abs(SN[0,0])==1 and abs(SN[1,1])==2)
orbit=[]
for a in (1,2):
    den=lcm(*(n**3 for n in range(1,17) if n%5 in (a,5-a)))
    orbit.append(den)
strip=L(16)
while strip%5==0:strip//=5
check('chi5 full unramified prefix equality',lcm(*orbit)==strip**3)

# Complete mean-zero sublattice: its index is prod(delta_a)/gcd(delta_a).
mean_lattice=[]
for q,NN in ((5,16),(7,8)):
    reps=[a for a in range(1,(q+1)//2) if gcd(a,q)==1]
    ds=[lcm(*(n**3 for n in range(1,NN+1) if n%q in (a,q-a))) for a in reps]
    D=lcm(*ds)
    coeff=S.Matrix([[int(D*(Q(1,n**3) if n%q in (a,q-a) else
                                Q(-1,n**3) if n%q in (reps[-1],q-reps[-1]) else Q(0)))
                     for n in range(1,NN+1)] for a in reps[:-1]])
    sm=smith_normal_form(coeff.T.row_join(D*S.eye(NN)),domain=ZZ)
    image=D**NN
    for n in range(NN):image//=abs(int(sm[n,n]))
    expected=1
    for a in ds:expected*=a
    expected//=gcd(*ds)
    check(f'period {q}: complete mean-zero index',image==expected)
    mean_lattice.append({'q':q,'N':NN,'weight':3,'orbit_deltas':list(map(str,ds)),
                         'mean_zero_index':str(image),'formula':'product(delta)/gcd(delta)'})

# Copy of the exact CDT sharp integral helper: no import-time side effects.
v=S.symbols('v')
def harmonic(n):return sum((S.Rational(1,j) for j in range(1,n+1)),S.Rational(0))
@lru_cache(None)
def Ipieces(m):
    points={S.Rational(1),S.Rational(m)}
    for h in range(1,m):points.update(a for a in [S.Rational(m-1,h),S.Rational(m,h)] if 1<a<m)
    points=sorted(points)
    C=S.Rational(3,2)+(m-1)*harmonic(m-2)+harmonic(m-1)/2
    pieces=[(S.Rational(0),S.Rational(1),C-m*v+v*v/2)]
    for lo,hi in zip(points,points[1:]):
        mid=(lo+hi)/2;I=S.Rational(0)
        for h in range(1,m):
            if m-1-h*mid>0:I+=(m-1-h*v)/h
        for k in range(1,m):
            a=m-k*mid
            if a>=1:I+=S.Rational(1,2*k)
            elif a>0:I+=(m-k*v)**2/(2*k)
        pieces.append((lo,hi,S.expand(I)))
    return pieces
def sharp(m,total,maximum):
    candidates=[]
    for lo,hi,I in Ipieces(m):
        H=S.expand(total*v+maximum*I)
        pts=[lo,hi];d=S.diff(H,v)
        if d.has(v):
            rt=S.solve(d,v)[0]
            if lo<=rt<=hi:pts.append(rt)
        for a in pts:candidates.append((S.factor(S.Rational(2,m*m)*H.subs(v,a)),a))
    return min(candidates,key=lambda a:a[0])
cost=[]
for s in (3,5):
    m=s+1
    flat=S.Rational(s*(s-1)*(4*s+7),6*m*m)
    sh,xi=sharp(m,s,1)
    safe=S.Rational(s*(4*s+5),6*m)
    cost.append({'s':s,'m':m,'e':[0]+[1]*s,'sigma':[0]+list(range(s)),
                 'flat':str(flat),'sharp':str(sh),'xi':str(xi),'tau':str(flat+sh),
                 'all_LCM_only_tau':str(safe),'quotient_coarse_tau':str(2*safe)})

payload={'scope':'Fixed exact symbolic/prefix checks; no numerical L/zeta or LI assumption.',
         'all_checks_passed':True,'check_count':len(checks),'checks':checks,
         'chi5_forcing':str(G0),'chi5_quotient_forcing':str(g),
         'local_critical_only_jets':local,'cyclic_determinants':cyclic,
         'J_prefix_N16':prefix,'joint_J_prefix':joint,'chi5_orbit_N16':list(map(str,orbit)),
         'complete_mean_zero_lattice':mean_lattice,
         'chi5_full_delta_s3_N16':str(strip**3),'CDT_safe_types':cost,
         'quotient_F_prefixes':{str(h):list(map(str,a)) for h,a in F.items()},
         'quotient_Z_prefixes':{str(h):list(map(str,a)) for h,a in QZ.items()},
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
md=HERE/'cdt_odd_character_targets_20261005.md'
payload['report_sha256']=hashlib.sha256(md.read_bytes()).hexdigest() if md.exists() else None
out=HERE/'cdt_odd_character_targets_20261005_verify.json'
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'all_checks_passed':True,'count':len(checks),'safe_costs':cost,
                  'joint_prefix':joint},ensure_ascii=False))
