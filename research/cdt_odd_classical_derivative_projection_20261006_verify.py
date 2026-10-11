"""NEW fixed symbolic audit, not a parameter search or a proof by sampling.

No old/peer mathematical producer is imported or executed.  Formal n,t
check the telescoper; n=0,1,2 only check the declared initial examples.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
checks = []
def check(name, value):
    value = bool(value)
    checks.append({"name": name, "passed": value})
    if not value:
        raise AssertionError(name)

n,t,u = s.symbols('n t u')
Q = 8*n**4+16*n**3+20*n**2+12*n+3
U = (8*(2*n+1)*t**4+48*n*(2*n+1)*t**3
     +2*(2*n+1)*(48*n**2-6*n-5)*t**2
     +2*(80*n**4+16*n**3-28*n**2-3*n+3)*t
     +48*n**5-24*n**3+3*n**2+4*n-1)
a=(t+n+1)**4
b=(t+n-s.Rational(1,2))**4
residual=(256*(n+1)**5*(2*t+n+1)*(t+n+s.Rational(1,2))**4*b
          -32*(2*n+1)*Q*(2*t+n)*a*b
          +256*n**5*(2*t+n-1)*(t+n)**4*a
          -16*(U.subs(t,t+1)*t**4*b-U*(t-s.Rational(1,2))**4*a))
check('all-n-t-cleared-telescoper-identity',s.expand(residual)==0)
printed_U=U+720*n*(2*n+1)*t**3
printed_residual=residual-16*((printed_U-U).subs(t,t+1)*t**4*b
                             -(printed_U-U)*(t-s.Rational(1,2))**4*a)
check('printed-v1-t3-coefficient-is-not-identity',s.expand(printed_residual)!=0)
check('U-at-half',s.expand(U.subs(t,s.Rational(1,2))
                         -n**2*(48*n**3+80*n**2+40*n+5))==0)

def R(k):
    return s.cancel(256**k*(2*t+k)*s.rf(t+s.Rational(1,2),k)**4/s.rf(t,k+1)**4)
examples=[]
for k in (0,1,2):
    f=R(k)
    check('antisymmetry-n'+str(k),s.cancel(f.subs(t,-k-t)+f)==0)
    residue={}
    for j in range(k+1):
        local=s.cancel(f*(t+j)**4).subs(t,-j+u)
        for i in range(1,5):
            residue[i,j]=s.cancel(s.diff(local,u,4-i).subs(u,0)/s.factorial(4-i))
    reconstructed=sum(v/(t+j)**i for (i,j),v in residue.items())
    check('partial-fraction-reconstruction-n'+str(k),s.cancel(f-reconstructed)==0)
    totals={i:sum(residue[i,j] for j in range(k+1)) for i in range(1,5)}
    check('only-total-r3-survives-n'+str(k),all(totals[i]==0 for i in (1,2,4)))
    A=totals[3]/2
    Cs={}
    for r in (1,2):
        C=-sum(s.rf(i,2*r)*residue[i,j]*sum((s.Rational(2*l-1,2))**(-i-2*r)
               for l in range(1,j+1)) for (i,j) in residue)
        Cs[r]=s.cancel(C)
    examples.append({'n':k,'A':str(A),'C_r1':str(Cs[1]),'C_r2':str(Cs[2])})
check('A-initial-1-96-14944',[v['A'] for v in examples]==['1','96','14944'])
check('C-r1-initial',[v['C_r1'] for v in examples]==['0','-1024','-181248'])
check('C-r2-second-prefix',examples[2]['C_r2']=='1129136128/27')
check('C-r2-denominator-beyond-n2',s.denom(s.Rational(examples[2]['C_r2']))==27)

T1=16*U.subs(n,1)*256*s.rf(t-s.Rational(1,2),1)**4/s.rf(t,2)**4
check('r1-forcing-vanishes',s.diff(T1,t,2).subs(t,s.Rational(1,2))==0)
force1=-384*(48+80+40+5)*256/s.rf(s.Rational(1,2),2)**4
check('r2-fourth-derivative-forcing-n1',
      s.cancel(-s.diff(T1,t,4).subs(t,s.Rational(1,2))-force1)==0)
check('r2-C-recurrence-n1',
      32*s.Rational(examples[2]['C_r2'])
      -32*3*59*s.Rational(examples[1]['C_r2'])-force1==0)
poly=n*n*(48*n**3+80*n**2+40*n+5)
check('all-large-prime-forcing-unit',s.cancel(poly.subs(n,-s.Rational(1,2)))==-s.Rational(1,4))

x,e,z=s.symbols('x e z')
L=e**5-32*z*(2*e+1)*(8*e**4+16*e**3+20*e**2+12*e+3)+65536*z**2*(e+1)**5
Lx=s.Poly(s.expand(L.subs(z,x/256)),e)
expected=[(1-x)**2,5*x*(x-1),10*x*x-7*x,
          10*x*x-s.Rational(11,2)*x,5*x*x-s.Rational(9,4)*x,
          x*x-s.Rational(3,8)*x]
check('normalized-five-theta-coefficients',
      all(s.expand(a-b)==0 for a,b in zip(Lx.all_coeffs(),expected)))

pdf_files=['cdt2026_effective_holonomy_author_20261006.pdf',
           'lai_sprang_zudilin2025_zeta2_5_v1_20261006.pdf']
pdf_pins={name:hashlib.sha256((ROOT/'literature'/name).read_bytes()).hexdigest()
          for name in pdf_files}
payload={'description':'Classical all-odd derivative projection and corrected displayed telescoper',
 'run_history':'Second execution after replacing structural equality of factored/expanded theta coefficients by exact polynomial equality; first run stopped at that audit check, no JSON was produced.',
 'scope':'Formal n,t identity, declared n=0,1,2 initials, one n=1 derivative example. No numerical irrationality theorem or optimal denominator cost.',
 'corrected_U':str(U),'forcing_r2_polynomial':str(poly),'examples':examples,
 'source_pdf_sha256':pdf_pins,'checks':checks,'check_count':len(checks),
 'all_passed':all(v['passed'] for v in checks)}
out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':len(checks),'all_passed':True,'examples':examples},ensure_ascii=False))
