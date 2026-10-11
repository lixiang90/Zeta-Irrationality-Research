from __future__ import annotations
import json, hashlib, sys
from pathlib import Path
from fractions import Fraction
import sympy as s
sys.stdout.reconfigure(encoding="utf-8")
N=12
I=s.eye(2); S=s.Matrix([[0,-1],[1,0]]); T=s.Matrix([[1,1],[0,1]])
U=T*S; E=s.diag(-1,1); W=s.Matrix([[0,-1],[12,0]])
def chi(d):
    a=int(d)%12
    if a in (1,11): return 1
    if a in (5,7): return -1
    raise ValueError(("nonunit chi",a))
def key(A):
    c,d=map(int,A[1,:])
    return min(((u*c)%12,(u*d)%12) for u in (1,5,7,11))
reps=[I]; keys={key(I):0}
for A in reps:
    for g in (S,T):
        B=A*g; k=key(B)
        if k not in keys:
            keys[k]=len(reps);reps.append(B)
assert len(reps)==24
def normalize(A):
    j=keys[key(A)]
    ga=A*reps[j].inv()
    assert ga[1,0]%12==0 and ga.det()==1
    return j,chi(ga[1,1])
def polyR(g):
    a,b,c,d=list(g)
    return s.Matrix([[d*d,b*d,b*b],[2*c*d,a*d+b*c,2*a*b],[c*c,a*c,a*a]])
def induced(g):
    B=s.zeros(72)
    for i,A in enumerate(reps):
        j,e=normalize(A*g.inv())
        B[3*i:3*i+3,3*j:3*j+3]=e*polyR(g)
    return B
BS,BT,BU=map(induced,(S,T,U))
BE=s.zeros(72)
for i,A in enumerate(reps):
    j,e=normalize(E*A*E)
    BE[3*i:3*i+3,3*j:3*j+3]=e*polyR(E)
relations=(s.eye(72)+BS).col_join(s.eye(72)+BU+BU**2)
V=s.Matrix.hstack(*relations.nullspace())
CT=s.Matrix.hstack(*(BT-s.eye(72)).nullspace())
CB=(s.eye(72)-BS)*CT
C=s.Matrix.hstack(*CB.columnspace())
def cf_convergents(x):
    x=Fraction(x);a=x.numerator;b=x.denominator
    out=[(1,0)];p0,p1=0,1;q0,q1=1,0
    while b:
        z=a//b;a,b=b,a-z*b
        p0,p1=p1,z*p1+p0;q0,q1=q1,z*q1+q0
        out.append((p1,q1))
    return out
def adjacent_row(alpha,beta,Q):
    # g(0)=alpha, g(infty)=beta, determinant +1
    a,c=beta;b,d=alpha
    g=s.Matrix([[a,b],[c,d]])
    if g.det()==-1:g[:,0]=-g[:,0]
    assert g.det()==1
    j,e=normalize(g)
    q=polyR(g)*s.Matrix(Q)
    row=s.zeros(1,72)
    row[0,3*j:3*j+3]=e*s.Matrix([[q[2],-q[1]/2,q[0]]])
    return row
def cusp_inf_row(x,Q):
    if x is None:return s.zeros(1,72)
    cv=cf_convergents(x)
    row=s.zeros(1,72)
    for z in range(1,len(cv)):row+=adjacent_row(cv[z],cv[z-1],Q)
    return row
def cusp(A,col):
    a,b=map(int,A[:,col])
    return Fraction(a,b) if b else None
def path_row(alpha,beta,Q):
    return cusp_inf_row(alpha,Q)-cusp_inf_row(beta,Q)
def form_slash_operator(g):
    # rho_(F|g) from rho_F, det-normalized slash
    B=s.zeros(72);det=g.det()
    for j,A in enumerate(reps):
        a,b,c,d=list(g*A)
        qs=[(b*b,-2*b*d,d*d),(2*a*b,-2*(a*d+b*c),2*c*d),(a*a,-2*a*c,c*c)]
        al,be=cusp(g*A,1),cusp(g*A,0)
        for z,Q in enumerate(qs):B[3*j+z,:]=path_row(al,be,[q/det for q in Q])
    return B
BW=form_slash_operator(W)
def hecke(p):
    B=sum((form_slash_operator(s.Matrix([[1,b],[0,p]])) for b in range(p)),s.zeros(72))
    return p*(B+chi(p)*form_slash_operator(s.Matrix([[p,0],[0,1]])))
B5=hecke(5); B7=hecke(7)
def ker_restrict(B,K):
    ns=(B*K).nullspace()
    return K*s.Matrix.hstack(*ns) if ns else s.zeros(K.rows,0)
CS=ker_restrict(B5**2+80*s.eye(72),V)
PM=ker_restrict(BE-s.eye(72),CS)
MM=ker_restrict(BE+s.eye(72),CS)
AM=ker_restrict(BW+s.eye(72),PM)
AP=ker_restrict(BW-s.eye(72),PM)
BM=ker_restrict(BW+s.eye(72),MM)
BP=ker_restrict(BW-s.eye(72),MM)
Omega=cusp_inf_row(Fraction(0),[0,0,1])
Endpoint=cusp_inf_row(Fraction(2,7),[Fraction(4,49),Fraction(-4,7),1])
def restricted_matrix(B,K):
    return K.gauss_jordan_solve(B*K)[0]
def jserial(A):
    return [[str(z) for z in row] for row in A.tolist()]
checks={}
def check(label,ok):
    checks[label]=bool(ok)
    if not ok:raise AssertionError(label)
check("24 projective cosets",len(reps)==24)
check("S2 identity",BS**2==s.eye(72))
check("U3 identity",BU**3==s.eye(72))
check("star2 identity",BE**2==s.eye(72))
check("dim period W 12",V.cols==12)
check("dim coboundaries 4",C.cols==4)
check("C satisfies Manin",relations*C==s.zeros(144,4))
check("cusp Hecke5 dimension8",CS.cols==8)
check("cusp parity4+4",PM.cols==4 and MM.cols==4)
check("W minus2 in each parity",AM.cols==2 and BM.cols==2)
check("W plus2 in each parity",AP.cols==2 and BP.cols==2)
check("W preserves cusp",relations*BW*CS==s.zeros(144,8))
check("W2 cusp",BW**2*CS==CS)
check("5 preserves cusp",relations*B5*CS==s.zeros(144,8))
check("7 preserves cusp",relations*B7*CS==s.zeros(144,8))
check("5 commutes star",(BE*B5-B5*BE)*CS==s.zeros(72,8))
check("7 commutes star",(BE*B7-B7*BE)*CS==s.zeros(72,8))
check("5 antiW",(BW*B5+B5*BW)*CS==s.zeros(72,8))
check("7 antiW",(BW*B7+B7*BW)*CS==s.zeros(72,8))
check("5 7 commute",(B5*B7-B7*B5)*CS==s.zeros(72,8))
check("T57 squared 4800",(B5*B7)**2*CS==4800*CS)
check("endpoint minusstar nonzero",Endpoint*BM!=s.zeros(1,2))
data={"date":"2026-10-06","scope":"NEW fixed 24-coset exact Manin model; no frozen producer imported or executed. Formal Betti dimensions do not prove numerical period linear independence.","checks":checks,"passed":sum(checks.values()),"coset_representatives":[jserial(A) for A in reps],"period_basis":jserial(V),"coboundary_basis":jserial(C),"cusp_plus_basis":jserial(PM),"cusp_minus_basis":jserial(MM),"Wminus_plusparity_basis":jserial(AM),"Wminus_minusparity_basis":jserial(BM),"Wplus_plusparity_basis":jserial(AP),"Wplus_minusparity_basis":jserial(BP),"Omega_row":jserial(Omega),"endpoint_2_7_row":jserial(Endpoint),"Omega_Wminus_plusparity":jserial(Omega*AM),"endpoint_Wminus_plusparity":jserial(Endpoint*AM),"endpoint_Wminus_minusparity":jserial(Endpoint*BM),"T57_Wminus_plusparity":jserial(restricted_matrix(B5*B7,AM)),"T57_Wminus_minusparity":jserial(restricted_matrix(B5*B7,BM)),"T5_cusp_charpoly":str(restricted_matrix(B5,CS).charpoly().as_expr()),"T7_cusp_charpoly":str(restricted_matrix(B7,CS).charpoly().as_expr())}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:v for k,v in data.items() if k not in ("period_basis","coboundary_basis","cusp_plus_basis","cusp_minus_basis","Wminus_plusparity_basis","Wminus_minusparity_basis","Wplus_plusparity_basis","Wplus_minusparity_basis","coset_representatives","Omega_row","endpoint_2_7_row")},ensure_ascii=False,indent=2))

# Independently recomputed fixed q expansion to the Sturm bound after T5,T7.
QMAX=281
def mul(a,b):
    c=[0]*(QMAX+1)
    for i,ai in enumerate(a):
        if ai:
            for j,bj in enumerate(b[:QMAX+1-i]):
                if bj:c[i+j]+=ai*bj
    return c
def inv(a):
    assert a[0]==1
    c=[1]+[0]*QMAX
    for n in range(1,QMAX+1):c[n]=-sum(a[j]*c[n-j] for j in range(1,n+1))
    return c
def lin(*terms):
    return [sum(k*a[j] for k,a in terms) for j in range(QMAX+1)]
one=[1]+[0]*QMAX
exp_eta={1:-3,2:2,3:1,4:-1,6:-2,12:3}
ls=[0]*(QMAX+1)
for m in range(1,QMAX+1):
    ls[m]=-sum(e*d*sum(j for j in range(1,m//d+1) if (m//d)%j==0) for d,e in exp_eta.items() if m%d==0)
eta=[1]+[0]*QMAX
for n in range(1,QMAX+1):
    num=sum(ls[j]*eta[n-j] for j in range(1,n+1));assert num%n==0
    eta[n]=num//n
x=[0]+eta[:QMAX]
u=[0]*(QMAX+1);u2=[0]*(QMAX+1)
for n in range(1,QMAX+1):
    u[n]=x[n]-u2[n]-2*sum(x[j]*u[n-j] for j in range(1,n+1))-2*sum(x[j]*u2[n-j] for j in range(1,n+1))
    for j in range(1,min(n,QMAX-n+1)):
        u2[n+j]+=2*u[n]*u[j]
    if 2*n<=QMAX:u2[2*n]+=u[n]**2
v=lin((1,one),(2,u))
den=mul(mul(lin((1,one),(1,u)),lin((1,one),(-2,u),(-2,u2))),mul(lin((1,one),(2,u),(2,u2)),lin((1,one),(1,u),(1,u2))))
du=[n*u[n] for n in range(QMAX+1)]
du2=mul(du,du);u_over_q=u[1:]+[0]
common=mul(mul(du2[1:]+[0],inv(u_over_q)),inv(den))
common=[-a for a in common]
Cs={0:mul(common,inv(v)),2:mul(common,v)}
Cs[4]=mul(Cs[2],mul(v,v));Cs[6]=mul(Cs[4],mul(v,v))
r=s.sqrt(3)
xm=s.Matrix([[Cs[6][n]-3*r*Cs[0][n],Cs[4][n]-r*Cs[2][n]] for n in range(1,9)])
xp=xm.applyfunc(lambda z:s.expand(z).subs(r,-r))
def tcoef(p,k,n):
    c=lambda a:Cs[k][a] if a<=QMAX else 0
    return c(p*n)+(chi(p)*p**3*c(n//p) if n%p==0 else 0)
tm={}
for p in (5,7):
    y=s.Matrix([[tcoef(p,6,n)-3*r*tcoef(p,0,n),tcoef(p,4,n)-r*tcoef(p,2,n)] for n in range(1,9)])
    h=xp.gauss_jordan_solve(y)[0].applyfunc(s.simplify)
    check("q Sturm T"+str(p)+" basis transfer",(xp*h-y).applyfunc(s.simplify)==s.zeros(8,2))
    tm[p]=h
H57=tm[5].applyfunc(lambda z:z.subs(r,-r))*tm[7]
check("q T57 square 4800",s.simplify(H57**2)==4800*s.eye(2))
check("q T5 square minus80",s.simplify(tm[5].applyfunc(lambda z:z.subs(r,-r))*tm[5])==-80*s.eye(2))
check("q T7 square minus60",s.simplify(tm[7].applyfunc(lambda z:z.subs(r,-r))*tm[7])==-60*s.eye(2))
check("no numerical period assumptions",Omega*AM!=s.zeros(1,2))
data.update({"checks":checks,"passed":sum(checks.values()),"execution_history":["First NEW execution: 22 Manin-only checks passed.","Second NEW execution: source transfer solve succeeded but structural Sympy equality failed without simplification; 22 base checks passed, no final extended certificate.","Third NEW execution: simplifies exact algebraic equality, retains one extra q jet for shifted products, and adds independently recomputed fixed q/Sturm source transfer and actual W-plus endpoint rows; no old producers."],"T5_Xminus_to_sigmaXminus":jserial(tm[5]),"T7_Xminus_to_sigmaXminus":jserial(tm[7]),"T57_Xminus":jserial(H57),"q_Xminus_1_to_8":jserial(xm),"Omega_Wplus_plusparity":jserial(Omega*AP),"Omega_Wplus_minusparity":jserial(Omega*BP),"endpoint_Wplus_plusparity":jserial(Endpoint*AP),"endpoint_Wplus_minusparity":jserial(Endpoint*BP),"T5_Wminus_to_Wplus_plusparity":jserial(AP.gauss_jordan_solve(B5*AM)[0]),"T5_Wminus_to_Wplus_minusparity":jserial(BP.gauss_jordan_solve(B5*BM)[0])})
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:data[k] for k in ("passed","T5_Xminus_to_sigmaXminus","T7_Xminus_to_sigmaXminus","T57_Xminus","Omega_Wplus_plusparity","Omega_Wplus_minusparity","endpoint_Wplus_plusparity","endpoint_Wplus_minusparity")},ensure_ascii=False,indent=2))

# Actual real/imaginary critical endpoint formula. Rows are exact on the
# cuspidal parity spaces, so no transcendental comparison matrix is guessed.
def row_coordinates(row,rows,K):
    X=s.Matrix.vstack(*[rr*K for rr in rows])
    return X.T.gauss_jordan_solve((row*K).T)[0]
B57=B5*B7
r1=s.zeros(1,72);r1[0,1]=1
ab0=row_coordinates(Omega*B5,[Omega,Omega*B57],AM)
abe=row_coordinates(Endpoint,[Omega,Omega*B57],AP)
abo=row_coordinates(Endpoint,[r1,r1*B57],BP)
H5=tm[5];Hplus=H57.applyfunc(lambda z:z.subs(r,-r))
Momega=((ab0[0]*s.eye(2)+ab0[1]*H57)*H5.inv()).applyfunc(s.simplify)
Mreal=(Momega*(abe[0]*s.eye(2)+abe[1]*Hplus)).applyfunc(s.simplify)
Modd=(abo[0]*s.eye(2)+abo[1]*Hplus).applyfunc(s.simplify)
check("even endpoint identity exact",(Endpoint-abe[0]*Omega-abe[1]*Omega*B57)*AP==s.zeros(1,2))
check("odd endpoint identity exact",(Endpoint-abo[0]*r1-abo[1]*r1*B57)*BP==s.zeros(1,2))
check("T5 critical value identity exact",(Omega*B5-ab0[0]*Omega-ab0[1]*Omega*B57)*AM==s.zeros(1,2))
check("Omega basis rows independent",s.Matrix.vstack(Omega*AM,Omega*B57*AM).det()!=0)
check("central plusW rows independent",s.Matrix.vstack(r1*BP,r1*B57*BP).det()!=0)
data.update({"checks":checks,"passed":sum(checks.values()),"T5_Omega_row_coefficients":jserial(ab0),"Wplus_even_endpoint_row_coefficients":jserial(abe),"Wplus_odd_endpoint_row_coefficients":jserial(abo),"L3_sigmaX_from_L3_X_matrix":jserial(Momega),"Re_endpoint_sigmaX_from_L3_X_matrix":jserial(Mreal),"Im_endpoint_sigmaX_from_2pi_L2_sigmaX_matrix":jserial(Modd)})
data["execution_history"].append("Fourth NEW execution: derives exact real/imaginary 2/7 endpoint formulas from the finite Manin matrices.")
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:data[k] for k in ("passed","T5_Omega_row_coefficients","Wplus_even_endpoint_row_coefficients","Wplus_odd_endpoint_row_coefficients","L3_sigmaX_from_L3_X_matrix","Re_endpoint_sigmaX_from_L3_X_matrix","Im_endpoint_sigmaX_from_2pi_L2_sigmaX_matrix")},ensure_ascii=False,indent=2))

# The anisotropic two-equation obstruction is arithmetic, not numerical LI.
aa,bb,rr=s.symbols("A B r")
alpha=aa+bb*rr;beta=aa-bb*rr
reduced=s.rem((alpha-beta)*(1-3*rr)-33+27*rr-(1+rr)*alpha*beta,rr**2-3,rr).expand()
f0=reduced.coeff(rr,0);f1=reduced.coeff(rr,1)
check("real endpoint rational coefficient",s.expand(f0)==-aa**2+3*bb**2-18*bb-33)
check("real endpoint sqrt3 coefficient",s.expand(f1)==-aa**2+3*bb**2+2*bb+27)
check("two equations force B minus3",s.expand(f1-f0)==20*(bb+3))
check("B minus3 forces A squared48",s.expand(f0.subs(bb,-3))==48-aa**2)
check("48 not rational square",s.sqrt(48).is_Rational is False)
check("source eigenline plus",s.simplify(H57*s.Matrix([1,-r]))==40*r*s.Matrix([1,-r]))
check("source eigenline minus",s.simplify(H57*s.Matrix([1,7*r]))==-40*r*s.Matrix([1,7*r]))
data.update({"checks":checks,"passed":sum(checks.values()),"source_eigenvectors":{"plus40sqrt3":["1","-sqrt(3)"],"minus40sqrt3":["1","7*sqrt(3)"]},"no_go_real_endpoint_equations":[str(f0),str(f1)],"no_go_scope":"No nonzero C=u X0+w X2 over K can have both L3(C)=0 and Re f_(sigma C)(2/7)=0. Does not prove numerical K-independence of Omega0,Omega2; does not include U or other reflections."})
data["execution_history"].append("Fifth NEW execution: adds the exact anisotropic K two-cusp-source obstruction and fixed Hecke eigenlines.")
out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"final_passed":data["passed"],"no_go_scope":data["no_go_scope"]},ensure_ascii=False,indent=2))




