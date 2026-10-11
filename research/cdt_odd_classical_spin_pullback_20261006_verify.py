"""NEW fixed symbolic exterior-square certificate. No old producer imports."""
from pathlib import Path
import hashlib
import json
import sympy as S

base=Path(__file__).resolve().parent
x=S.symbols('x')
checks=[]
def check(name,v):
    v=bool(v)
    checks.append({'name':name,'passed':v})
    if not v: raise AssertionError(name)
def red(v): return S.factor(S.cancel(v))
def theta_powers(degree):
    rows=[[S.Integer(1)]]
    for j in range(degree):
        old=rows[-1]
        new=[S.Integer(0)]*(len(old)+1)
        for k,v in enumerate(old):
            new[k]+=x*S.diff(v,x)
            new[k+1]+=x*v
        rows.append(new)
    return rows
th=theta_powers(5)
theta5=[x*x-S.Rational(3,8)*x,5*x*x-S.Rational(9,4)*x,
        10*x*x-S.Rational(11,2)*x,10*x*x-7*x,
        5*x*(x-1),(1-x)**2]
p=[red(sum(theta5[j]*th[j][k] for j in range(k,6))) for k in range(6)]
b=[red(v/p[5]) for v in p]
check('fifth-normalized-leading',b[5]==1)
q=[red(b[j]+S.Rational(j+1)*b[j+1]/x) for j in range(5)]+[S.Integer(1)]
a3=red(S.Rational(2,5)*q[4])
a2=red((q[3]-2*S.diff(a3,x)-S.Rational(7,4)*a3*a3)/2)
a1=red(a2*a3/2-a3**3/8+S.diff(a2,x)-3*a3*S.diff(a3,x)/4-S.diff(a3,x,2)/2)
a0=red((S.diff(a2,x,2)+2*S.diff(a1,x)+3*a3*(S.diff(a2,x)+a1)/2
         +(a2+a3*a3/4)*a2-q[1])/4)
aa=[a0,a1,a2,a3,S.Integer(1)]

# Derive the fifth-order operator on an arbitrary exterior minor Y.
rowU=[a1,a2,a3,S.Integer(1)]
def derivative(row):
    ans=[S.Integer(0)]*(len(row)+1)
    for j,v in enumerate(row):
        ans[j]+=S.diff(v,x)
        ans[j+1]+=v
    return [red(v) for v in ans]
DU=derivative(rowU)
D2U=derivative(DU)
derived=[]
for j in range(6):
    value=D2U[j]+(3*a3/2*DU[j] if j<len(DU) else 0)
    value+=(a2+a3*a3/4)*rowU[j] if j<len(rowU) else 0
    value-=4*a0 if j==1 else 0
    value-=2*(S.diff(a0,x)+a3*a0) if j==0 else 0
    derived.append(red(value))
for j in range(6):
    check('full-exterior-fifth-coefficient-'+str(j),red(derived[j]-q[j])==0)
V=red(S.diff(a3,x,2)-2*S.diff(a2,x)+3*a3*S.diff(a3,x)/2-a2*a3+a3**3/4+2*a1)
check('CY2-full-relation',V==0)

# Convert the new fourth-order operator back to theta form.
tcoef=[S.Integer(0)]*5
remaining=list(aa)
for j in range(4,-1,-1):
    tcoef[j]=red(remaining[j]/x**j)
    for k in range(j+1): remaining[k]=red(remaining[k]-tcoef[j]*th[j][k])
check('fourth-theta-conversion-complete',all(v==0 for v in remaining))
fourth_theta=[red(v*x**4*(1-x)**4) for v in tcoef]
check('all-fourth-coefficients-polynomial',all(v.is_polynomial(x) for v in fourth_theta))

# Direct exterior companion matrix; all six minors are retained.
mat=S.zeros(4)
for j in range(3): mat[j,j+1]=1
for j in range(4): mat[3,j]=-aa[j]
pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
ext=S.zeros(6)
def add_wedge(row,i,j,v):
    if i==j:return
    if i>j:i,j,v=j,i,-v
    ext[row,pairs.index((i,j))]+=v
for row,(i,j) in enumerate(pairs):
    for k in range(4):
        add_wedge(row,k,j,mat[i,k])
        add_wedge(row,i,k,mat[j,k])
obs=[S.Matrix([[x,0,0,0,0,0]])]
for j in range(5):obs.append((obs[-1].diff(x)+obs[-1]*ext).applyfunc(red))
res=sum((b[j]*obs[j] for j in range(6)),S.zeros(1,6)).applyfunc(red)
check('all-six-minors-obey-original-fifth-operator',all(v==0 for v in res))
check('exterior-output-rank-exact-five',S.Matrix.vstack(*obs[:5]).rank()==5)

# Indicial polynomials at0 and1, with ordinary derivative coefficients.
r=S.symbols('r')
def indicial(coeff,point):
    d=len(coeff)-1
    return red(sum(S.limit(coeff[j]*(x-point)**(d-j),x,point)
                   *S.prod(r-k for k in range(j)) for j in range(d+1)))
ind4zero=indicial(aa,0)
ind4one=indicial(aa,1)
ind5zero=indicial(b,0)
ind5one=indicial(b,1)
check('fourth-MUM-zero',ind4zero==r**4)
check('fifth-MUM-zero',ind5zero==r**5)
check('fifth-one-exponents',red(ind5one-r*r*(r-1)*(r-2)*(r-2))==0)

pins={name:hashlib.sha256((base/name).read_bytes()).hexdigest() for name in [
 'cdt_odd_classical_derivative_projection_20261006.md',
 'cdt_odd_classical_derivative_projection_20261006_verify.json']}
check('frozen-projection-MD-pin',pins['cdt_odd_classical_derivative_projection_20261006.md']==
      'c24a4d7807bed750f63746b4506f2a238a7d9b9122e2e39ac4871653b39d5c1e')
payload={'scope':'Actual fifth homogeneous differential module is an exact exterior-minor image of an explicit rational fourth-order CY2/MUM module. Not a geometric realization, numerical special-value theorem, or free rank reduction of the inhomogeneous zeta7 target.',
 'run_history':'First execution; retained only on success.',
 'b_fifth':[str(v) for v in b],'a_fourth':[str(v) for v in aa],
 'fourth_theta_common_multiplier':'x^4*(1-x)^4',
 'fourth_theta_coefficients':[str(v) for v in fourth_theta],
 'indicial_fourth_zero':str(ind4zero),'indicial_fourth_one':str(ind4one),
 'indicial_fifth_zero':str(ind5zero),'indicial_fifth_one':str(ind5one),
 'input_pins':pins,'checks':checks,'check_count':len(checks),
 'all_passed':all(c['passed'] for c in checks)}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'a_fourth':payload['a_fourth'],
                  'theta4':payload['fourth_theta_coefficients'],
                  'ind4one':str(ind4one)},ensure_ascii=False))
