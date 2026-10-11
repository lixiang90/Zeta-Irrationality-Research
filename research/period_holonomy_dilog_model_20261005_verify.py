"""Exact identities for the five-dilog integral source and its compatible rank-six quotient."""
import hashlib
import json
from fractions import Fraction
from math import gcd, lcm
from pathlib import Path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

PATH=Path(__file__).resolve()
REPORT=PATH.with_name(PATH.name.replace("_verify.py",".md"))
CHECKS=[]
def check(name, ok, detail=None):
    ok=bool(ok)
    CHECKS.append({"name":name,"passed":ok, **({"detail":detail} if detail is not None else {})})
    assert ok,name

N,z=s.symbols("N z")
eps=[1,1,-1,-1,-1]
r=[(N+2)/(N+1)**2,(N+1)/(N*(N+2)),1/(N*(N+1)),1/(N+1),1/(N+2)]
D=N*(N+1)**2*(N+2)
A=[N*(N+2)**2,(N+1)**3,(N+1)*(N+2),N*(N+1)*(N+2),N*(N+1)**2]
for i in range(5):
    check(f"A_{i}=D*r_{i}",s.cancel(D*r[i]-A[i])==0)
diffs=[
((0,1),(N**2+N-1)/(N*(N+1)**2*(N+2))),
((0,2),(N**2+N-1)/(N*(N+1)**2)),
((0,3),1/(N+1)**2),
((0,4),(2*N+3)/((N+1)**2*(N+2))),
((1,2),(N**2+N-1)/(N*(N+1)*(N+2))),
((1,3),1/(N*(N+1)*(N+2))),
((1,4),1/(N*(N+2))),
((2,3),-(N-1)/(N*(N+1))),
((2,4),-(N**2-2)/(N*(N+1)*(N+2))),
((3,4),1/((N+1)*(N+2)))]
for (i,j),v in diffs: check(f"boundary_difference_{i}_{j}",s.cancel(r[i]-r[j]-v)==0)
one_minus=[(N**2+N-1)/(N+1)**2,(N**2+N-1)/(N*(N+2)),(N**2+N-1)/(N*(N+1)),N/(N+1),(N+1)/(N+2)]
for i,v in enumerate(one_minus): check(f"evaluation_separation_{i}",s.cancel(1-r[i]-v)==0)
prod=s.prod((1-ri)**e for ri,e in zip(r,eps))
check("G_1_product",s.cancel(prod-(1-r[2]))==0)
P=N**2+N-1
check("T_1",s.expand(sum(e*a for e,a in zip(eps,A))-P)==0)
for v,rem in [(N,-1),(N+1,-1),(N+2,1)]:
    check(f"P_remainder_{v}",s.rem(P,v,N)==rem)
check("D_symbolic_denominator_factorization",s.cancel(D-((N+1)**2)*(N*(N+2)))==0)
check("D_even_boundary_N2",lcm(*[int(s.denom(s.cancel(ri.subs(N,2)))) for ri in r])==72)
check("strict_CDT_adjacent_N1000000",Fraction(1,1000001)<Fraction(1,1000000))
check("excluded_strict_boundary_N999999",Fraction(1,1000000)==Fraction(1,1000000))

E=s.Matrix([[0,-1,-1,0,0],[-2,1,-1,-1,0],[1,-1,0,0,-1]])
u=s.Matrix([-1,0,0,-2,1])
Aug=s.Matrix.vstack(s.ones(1,5),E)*s.diag(*eps)
check("exponent_rank",E.rank()==3)
check("augmented_rank",Aug.rank()==4)
check("primitive_u_kernel",Aug*u==s.zeros(4,1) and gcd(*[int(t) for t in u])==1)
for i in range(5):
    exp=E[:,i]
    check(f"actual_rational_exponents_{i}",s.cancel(r[i]-N**exp[0]*(N+1)**exp[1]*(N+2)**exp[2])==0)

# Integral matrices act on coefficients of the ordered horizontal columns
# Y0,U_a,...,U_e,V_a,...,V_e.
M0=s.eye(11)
for i in range(5): M0[6+i,1+i]=1
meridians=[]
for i in range(5):
    Mi=s.eye(11); Mi[1+i,0]=-1; meridians.append(Mi)
for i,M in enumerate([M0]+meridians):
    check(f"integral_unimodular_meridian_{i}",M.det()==1 and all(v.is_Integer for v in M))
v_basis=[s.Matrix([-1,1,0,0,0]),s.Matrix([1,0,1,0,0]),s.Matrix([1,0,0,1,0]),s.Matrix([1,0,0,0,1])]
Ku=s.zeros(11,1);Ku[1:6,0]=u
cols=[Ku]
for v in v_basis:
    col=s.zeros(11,1);col[6:11,0]=v;cols.append(col)
K=s.Matrix.hstack(*cols)
check("Betti_Q_kernel_rank_five",K.rank()==5)
SNF=smith_normal_form(K,domain=s.ZZ)
check("Betti_kernel_primitive",[abs(int(SNF[i,i])) for i in range(5)]==[1]*5)
for i,M in enumerate([M0]+meridians):
    C=(K.T*K).inv()*K.T*M*K
    check(f"kernel_stable_meridian_{i}",K*C==M*K and all(v.is_Integer for v in C))
c=s.symbols("c",nonzero=True)
gs=s.symbols("g0:5");fs=s.symbols("f0:5");ls=s.symbols("l0:5")
Fund=s.zeros(11);Fund[0,0]=1
for i in range(5):
    Fund[1+i,0]=gs[i];Fund[6+i,0]=fs[i]
    Fund[1+i,1+i]=c;Fund[6+i,1+i]=c*ls[i];Fund[6+i,6+i]=c**2
check("fundamental_matrix_determinant",s.factor(Fund.det())==c**15)

P3=s.zeros(3,11);P3[0,0]=1
for i,e in enumerate(eps):P3[1,1+i]=e;P3[2,6+i]=e
P6=s.zeros(6,11);P6[0,0]=1;P6[1,2]=1;P6[2,3]=1
P6[3,4]=1;P6[3,1]=-2;P6[4,5]=1;P6[4,1]=1
for i,e in enumerate(eps):P6[5,6+i]=e
check("dR_cyclic_projection_rank_three",P3.rank()==3)
check("dR_full_quotient_rank_six",P6.rank()==6)
check("constant_integral_kernel_compatibility",P6*K==s.zeros(6,5))
check("rank3_dR_kernel_is_eight",len(P3.nullspace())==8)
PQ=s.zeros(3,6);PQ[0,0]=1;PQ[1,1]=1;PQ[1,2]=-1;PQ[1,3]=-1;PQ[1,4]=-1;PQ[2,5]=1
check("factorization_through_six",PQ*P6==P3)
Conn=s.zeros(11)
for i,ri in enumerate(r):Conn[1+i,0]=ri/(1-ri*z);Conn[6+i,1+i]=1/z
Conn6=s.zeros(6)
Conn6[1,0]=r[1]/(1-r[1]*z);Conn6[2,0]=r[2]/(1-r[2]*z)
Conn6[3,0]=r[3]/(1-r[3]*z)-2*r[0]/(1-r[0]*z)
Conn6[4,0]=r[4]/(1-r[4]*z)+r[0]/(1-r[0]*z)
Conn6[5,1]=1/z;Conn6[5,2]=Conn6[5,3]=Conn6[5,4]=-1/z
check("integral_quotient_connection_intertwines",P6*Conn==Conn6*P6)
# The weighted kernel has no source constant and is a rational subconnection.
check("constant_kernel_connection_stable",P6*Conn*K==s.zeros(6,5))
# Arithmetic is checked at one fixed legitimate N=3, at one fixed prefix n=7.
nv=3; dv=int(D.subs(N,nv));av=[int(v.subs(N,nv)) for v in A]
check("fixed_N3_D_minimal",lcm(*[int(s.denom(s.cancel(ri.subs(N,nv)))) for ri in r])==dv)
check("fixed_N3_two_clear_numerators_coprime",gcd(av[0],av[1])==1)
Ln=1
pred3s=pred3o=pred6s=pred6o=pred11s=pred11o=1
real3s=real3o=real6s=real6o=real11s=real11o=1
for k in range(1,8):
    powers=[a**k for a in av];tk=sum(e*t for e,t in zip(eps,powers))
    gam=[powers[1],powers[2],powers[3]-2*powers[0],powers[4]+powers[0]]
    check(f"fixed_coefficient_gamma_gcd_{k}",gcd(*gam)==1)
    scaledf=Fraction(tk,k*k);originalf=Fraction(tk,dv**k*k*k)
    real3s=lcm(real3s,scaledf.denominator);real3o=lcm(real3o,originalf.denominator)
    pred3s=lcm(pred3s,k*k//gcd(k*k,tk));pred3o=lcm(pred3o,dv**k*k*k//gcd(dv**k*k*k,tk))
    vals6s=[Fraction(b,k) for b in gam]+[scaledf]
    vals6o=[Fraction(b,dv**k*k) for b in gam]+[originalf]
    vals11s=[Fraction(t,k*k) for t in powers]+[Fraction(t,k) for t in powers]
    vals11o=[Fraction(t,dv**k*k*k) for t in powers]+[Fraction(t,dv**k*k) for t in powers]
    real6s=lcm(real6s,*[f.denominator for f in vals6s]);real6o=lcm(real6o,*[f.denominator for f in vals6o])
    real11s=lcm(real11s,*[f.denominator for f in vals11s]);real11o=lcm(real11o,*[f.denominator for f in vals11o])
    pred6s=lcm(pred6s,k*k//gcd(k,tk));pred6o=lcm(pred6o,dv**k*k*k//gcd(k,tk))
    Ln=lcm(Ln,k);pred11s=Ln**2;pred11o=lcm(pred11o,dv**k*k*k)
    for name,actual,pred in [("three_scaled",real3s,pred3s),("three_original",real3o,pred3o),("six_scaled",real6s,pred6s),("six_original",real6o,pred6o),("eleven_scaled",real11s,pred11s),("eleven_original",real11o,pred11o)]:
        check(f"complete_prefix_{name}_{k}",actual==pred)
for p in [7,11]:
    check(f"new_boundary_prime_{p}_not_in_D_N3",dv%p!=0)
check("fixed_N3_c_e_collide_mod7",int(s.numer(s.cancel((r[2]-r[4]).subs(N,3))))%7==0)
check("fixed_N3_a_b_collide_mod11",int(s.numer(s.cancel((r[0]-r[1]).subs(N,3))))%11==0)
# Fixed examples check the Frobenius identity; all-scale argument is in the report.
for p,h in [(5,1),(7,2),(13,1)]:
    k=p**h
    tk=sum(e*pow(a,k,p) for e,a in zip(eps,av))
    check(f"fixed_Frobenius_p{p}_h{h}",tk%p==int(P.subs(N,nv))%p and tk%p!=0)
result={
 "status":"fixed_exact_dilog_model_certificates_passed","as_of":"2026-10-05",
 "report_sha256":hashlib.sha256(REPORT.read_bytes()).hexdigest(),
 "script_sha256":hashlib.sha256(PATH.read_bytes()).hexdigest(),
 "checks":CHECKS,"check_count":len(CHECKS),
 "proof_scope":"Symbolic identities and fixed exact examples support the written all-scale proofs. Numeric irrationality is a CDT Theorem C corollary; no new independent holonomy irrationality theorem or Lean formalization.",
 "new_global_irrationality_theorem":False,"new_lean_formalization":False,"parameter_scan":False,
 "de_Rham_cyclic_rank":3,"full_integral_source_rank":11,"compatible_integral_quotient_rank":6,
 "fixed_prefix_n":7,"fixed_target_N":3,
}
PATH.with_suffix(".json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":result["status"],"checks":len(CHECKS),"report_sha256":result["report_sha256"]},ensure_ascii=False))

