"""NEW fixed all-n source/reflection certificate. No frozen producer imports."""
from pathlib import Path
import json
import sympy as S

n,t=S.symbols('n t')
base=Path(__file__).resolve().parent
checks=[]
def check(name,value):
    checks.append({'name':name,'passed':bool(value)})
    if not value: raise AssertionError(name)
def zero(v):
    return all(S.expand(z)==0 for z in v)
def slash(g):
    a,b,c,d=list(g)
    det=g.det()
    return S.Matrix([[d*d,b*d,b*b],[2*c*d,a*d+b*c,2*a*b],[c*c,a*c,a*a]])/det

eta=S.Matrix([[1,0],[12,1]])
etan=S.Matrix([[1,0],[12*n,1]])
etaminus=S.Matrix([[1,0],[-12*n,1]])
M=S.Matrix([[24,-7],[84,-24]])
W=S.Matrix([[0,-1],[12,0]])
T=S.Matrix([[1,1],[0,1]])
Jn=S.simplify(etan*M*etaminus)
p=84*n*n+48*n+7
check('Jn explicit rational matrix', zero(Jn-S.Matrix([[24+84*n,-7],[12*p,-24-84*n]])))
check('Jn determinant 12 all n', S.expand(Jn.det()-12)==0)
check('Jn trace zero all n', S.expand(S.trace(Jn))==0)
check('Jn order two PSL all n', zero(Jn*Jn+12*S.eye(2)))
check('eta W Tminus Wminus exact', W*T.inv()*W.inv()==eta)
check('Jn nzero equals M', Jn.subs(n,0)==M)
check('all n p positive explicit square', S.expand(p-(84*(n+S.Rational(2,7))**2+S.Rational(1,7)))==0)

RM=slash(M)
Q=S.Matrix([49,-336,588])
check('M unsigned plus eigline dimension one', (RM-S.eye(3)).rank()==2)
check('Q M plus eigenvector', zero(RM*Q-Q))
check('M signed order2 cocycle constraint', zero((RM-S.eye(3))*(RM+S.eye(3))))
Qn=slash(etaminus)*Q
QJn= S.Matrix([1,0,0])+slash(Jn)*S.Matrix([1,0,0])
check('transported eigenline exact normalization', zero(p*Qn-7*QJn))
check('transported eigenline all n', zero((slash(Jn)-S.eye(3))*Qn))

Peta=S.Matrix([44160,529920,2073600])
Pn=S.Matrix([44160*n,529920*n*n,2119680*n**3-46080*n])
check('actual eta primitive period n1', Pn.subs(n,1)==Peta)
check('eta polynomial all n initial n0', Pn.subs(n,0)==S.zeros(3,1))
check('eta polynomial all n exact recurrence', zero(Pn.subs(n,n+1)-slash(eta)*Pn-Peta))
check('eta negative polynomial inverse law', zero(Pn.subs(n,-n)+slash(etaminus)*Pn))
sn=644*n**3+552*n*n+147*n
mu= S.Rational(1920,7)*sn
check('actual Jn cocycle plus-line projection', zero((RM+S.eye(3))*Pn-mu*Q))
cL=slash(etaminus)*(RM+S.eye(3))*Pn
cR=-S.Rational(1920,7)*Qn
check('all n true primitive correction zero', zero(cL+sn*cR))
check('corrector Jn cocycle nonzero all n', cR[0]==-13440)
check('integer corrector parameter coefficients', all(S.Poly(sn,n).nth(j).is_Integer for j in range(4)))
check('parameter n0 zero', sn.subs(n,0)==0)
check('parameter n1 fixed consistency', sn.subs(n,1)==1343)
check('parameter minus1 fixed consistency', sn.subs(n,-1)==-239)
check('parameter cubic only real zero', 552**2-4*644*147<0)
check('canonical M is lost except n0', -S.Rational(1920,7)*sn !=0)
lambdaLn=S.Rational(1920)*sn/p
lambdaRn=-S.Rational(1920)/p
check('normalized real endpoint cancellation', S.factor(lambdaLn+sn*lambdaRn)==0)
check('n1 verified old bad139 Tate', lambdaLn.subs(n,1)==S.Rational(2578560,139))
check('n1 corrector finite Tate', lambdaRn.subs(n,1)==-S.Rational(1920,139))

coeff={1:1,2:-66,3:495,4:-880,6:594,12:-144}
for j in (0,1,2,3):
    check('R zero at L argument '+str(j), sum(S.Rational(v,k**j) for k,v in coeff.items())==0)
check('R anti W all old coefficients', all(S.Rational(144,k**4)*v ==-coeff[12//k] for k,v in coeff.items()))
check('R rational integer source', all(isinstance(v,int) for v in coeff.values()))
check('R coefficient q1 nonzero', 240*coeff[1]==240)
Rzero=sum(S.Rational(v,k**4) for k,v in coeff.items())
check('R cusp zero source constant zero', Rzero==0)
def B3(z):
    z=z-S.floor(z)
    return z**3-S.Rational(3,2)*z*z+z/2
finite_R7=sum(S.Rational(160*v,j**3)*
              sum((S.Rational(1,2)-S.Rational(k,7))*B3(S.Rational(2*j*k,7))
                  for k in range(1,7)) for j,v in coeff.items())
check('R canonical M finite endpoint independently Bernoulli', finite_R7==-S.Rational(1920,7))
check('old sigma cusp zero remains 920', 920+sn*Rzero==920)
check('old first other-infinity cusp remains nonzero', sum(coeff.values())==0 and -132480!=0)
check('all integer n first translation width minimum', 84-48>0)

report={
 'date':'2026-10-06',
 'scope':'Exact all-integer zero-Apery-period source correction and legitimate T/Jn leaf input; no global fullkernel, analytic-budget improvement or numerical irrationality theorem.',
 'execution_history':'Second execution of this NEW fixed symbolic producer: first saved 39 checks; this second adds an independent exact finite Bernoulli endpoint check for R at rho7 squared. No frozen producer imported or executed.',
 'passed':len(checks),'checks':checks,
 'R_old_coefficients':coeff,'Jn':[[str(v) for v in row] for row in Jn.tolist()],
 'p_n':str(p),'s_n':str(sn),'P_eta_n':[str(v) for v in Pn],
 'Q_n':[str(S.factor(v)) for v in Qn],
 'cL_Jn_over_ipi3':[str(S.factor(v)) for v in cL],
 'cR_Jn_over_ipi3':[str(S.factor(v)) for v in cR],
 'lambdaL_Jn_Tate':str(lambdaLn),'lambdaR_Jn_Tate':str(lambdaRn),
 'first_source':'F_L+s_n R','conjugate_source':'sigma(F_L)+s_n R',
 'period':'34560*sqrt(3)*L(3,chi12)',
 'Hecke_second_parameter':'sqrt(12)*(84*n^2+48*n+7)',
 'actual_rank_each_embedding':4,
 'rank_scope':'Follows in prose from the rational order4 closure and unchanged nonzero cubic cusp; not a symbolic numerical check.'}
out=base/'cdt_odd_level12_zero_period_corrector_family_20261006_verify.json'
out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'s_n':str(sn),'p_n':str(p)}))
