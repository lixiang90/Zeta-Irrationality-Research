"""NEW fixed Levelt monodromy / Lie-algebra certificate, no research imports.

Closure is exact finite-dimensional linear algebra on two prescribed matrices.
It is not a search over research parameters, primes, or group words.
"""
from pathlib import Path
import json
import sympy as S

base = Path(__file__).resolve().parent
checks = []
def check(name, value):
    value = bool(value)
    checks.append({'name': name, 'passed': value})
    if not value:
        raise AssertionError(name)
def vals(mat): return S.Matrix(list(mat))
def independent(basis, mat):
    return S.Matrix.hstack(*[vals(v) for v in basis], vals(mat)).rank() > len(basis)
def string_matrix(mat): return [[str(mat[i,j]) for j in range(mat.cols)] for i in range(mat.rows)]

A = S.Matrix([[0,0,0,-1],[1,0,0,-4],[0,1,0,-6],[0,0,1,-4]])
B = S.Matrix([[0,0,0,-1],[1,0,0,4],[0,1,0,-6],[0,0,1,4]])
C = A.inv()*B
t = S.symbols('t')
check('Levelt infinity characteristic (t+1)^4', S.expand(A.charpoly(t).as_expr()-(t+1)**4)==0)
check('Levelt zero inverse characteristic (t-1)^4', S.expand(B.charpoly(t).as_expr()-(t-1)**4)==0)
check('all three matrices unimodular integral', all(M.det()==1 and all(v.is_Integer for v in M) for M in [A,B,C]))
check('conifold transvection rank1', (C-S.eye(4)).rank()==1)
check('conifold nilpotent square0', (C-S.eye(4))**2==S.zeros(4))

pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
unknown=S.symbols('j0:6')
J=S.zeros(4)
for u,(i,j) in zip(unknown,pairs): J[i,j]=u;J[j,i]=-u
equations=list(A.T*J*A-J)+list(B.T*J*B-J)
sol=S.linsolve(equations,unknown)
vector=list(sol)[0]
free=set().union(*(v.free_symbols for v in vector))
check('unique alternating form up to scale',len(free)==1)
parameter=next(iter(free))
J=J.subs(dict(zip(unknown,vector))).subs(parameter,1)
den=S.ilcm(*[S.denom(v) for v in J])
J=J*den
check('alternating form nondegenerate',J.det()!=0)
check('A and B preserve complete J',A.T*J*A==J and B.T*J*B==J)

NB=B-S.eye(4)
check('zero regular unipotent size4',NB**4==S.zeros(4) and NB**3!=S.zeros(4))
N0=NB-NB**2/2+NB**3/3
N1=C-S.eye(4)
lie=[N0,N1]
labels=['log(B)','C-I']
check('initial logarithms independent',S.Matrix.hstack(*[vals(v) for v in lie]).rank()==2)
# Prescribed breadth-first commutator closure, bounded by dim sp4=10.
pos=0
while pos<len(lie):
    M=lie[pos]
    for j in range(pos):
        V=M*lie[j]-lie[j]*M
        if independent(lie,V):
            labels.append('['+labels[pos]+','+labels[j]+']')
            lie.append(V)
    pos+=1
check('Lie closure exactly dimension10',len(lie)==10)
check('all Lie generators in sp(J)',all(V.T*J+J*V==S.zeros(4) for V in lie))
check('all commutators in retained Lie basis',all(not independent(lie,U*V-V*U) for U in lie for V in lie))

def wedge_matrix(M):
    return S.Matrix([[M[i,k]*M[j,l]-M[i,l]*M[j,k] for k,l in pairs] for i,j in pairs])
wa,wb,wc=map(wedge_matrix,[A,B,C])
contraction=S.Matrix([[J[i,j] for i,j in pairs]])
P=S.Matrix.hstack(*contraction.nullspace())
check('primitive exterior component dimension5',P.rank()==5)
restricted=[]
for name,W in [('A',wa),('B',wb),('C',wc)]:
    U=P.gauss_jordan_solve(W*P)[0]
    check(name+' preserves primitive exterior component',P*U==W*P)
    restricted.append(U)
PA,PB,PC=restricted
check('primitive conifold has Jordan 2,2,1',(PC-S.eye(5)).rank()==2 and (PC-S.eye(5))**2==S.zeros(5))
# Algebra closure (rather than sampled words) certifies absolute irreducibility.
algebra=[S.eye(5)]
pos=0
while pos<len(algebra):
    M=algebra[pos]
    for G in [PA,PB]:
        V=M*G
        if independent(algebra,V):algebra.append(V)
    pos+=1
check('primitive associative algebra equals full M5',len(algebra)==25)

report={
 'execution_record':'First execution of this NEW fixed certificate; retained only after all exact checks passed.',
 'scope':'Levelt matrices for the hypergeometric rank4 module have Zariski closure Sp4; the primitive exterior-square representation has dimension5 and is absolutely irreducible. No claim about the inhomogeneous zeta7 extension, a common analytic leaf, or special-value irrationality.',
 'A':string_matrix(A),'B':string_matrix(B),'C':string_matrix(C),'J':string_matrix(J),
 'lie_dimension':len(lie),'lie_basis_labels':labels,'lie_basis':[string_matrix(V) for V in lie],
 'primitive_basis':string_matrix(P),'primitive_A':string_matrix(PA),'primitive_B':string_matrix(PB),
 'primitive_C':string_matrix(PC),'associative_algebra_dimension':len(algebra),
 'checks':checks,'check_count':len(checks),'all_passed':all(c['passed'] for c in checks)}
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'J':report['J'],'lie_dimension':len(lie),'primitive_algebra_dimension':len(algebra)}))
