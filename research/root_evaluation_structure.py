"""Smith invariants and explicit lost-multiplicity counterexamples."""
import json
import math
from pathlib import Path
from flint import fmpq
from sympy import Matrix, ZZ, factorint
from sympy.matrices.normalforms import smith_normal_form
from directional_congruence import Family
from growing_integer_space import basis
from joint_exact import content
from two_prefix_outer import vp


def main():
    rows=[]
    for N,L in [(1,3),(2,6),(4,12)]:
        E=Matrix([[int(basis(i)(-j*j)) for i in range(L)] for j in range(N+1,N+L+1)])
        S=smith_normal_form(E,domain=ZZ);det=abs(int(E.det()))
        formula=fmpq(2**(L-1)*math.prod((j-i)*(2*N+i+j) for i in range(1,L+1) for j in range(i+1,L+1)),
                     math.prod(math.factorial(2*i) for i in range(1,L)))
        assert det==formula
        rows.append(dict(N=N,L=L,determinant=str(det),smith=[str(abs(int(S[i,i]))) for i in range(L)],
                         prime_factors={str(p):int(e) for p,e in factorint(det).items()}))
    fam=Family();ct0=content(fam.det([0,0,0]));examples=[]
    for p,u,c in [(5,[-1,1,2],1),(7,[3,-1,1],5)]:
        Q=fam.polynomial(u);ev=[sum(row[i]*u[i] for i in range(3)) for row in fam.E]
        assert all(x%p==0 for x in ev)
        assert int(fam.Q0(c))%p==0 and int(fam.Q0.derivative()(c))%p==0
        assert int(Q(c))%p==0 and int(Q.derivative()(c))%p!=0
        ct=content(fam.det(u));loss=vp(ct0,p)-vp(ct,p);assert loss>0
        examples.append(dict(p=p,u=u,evaluations=ev,merged_t_residue=c,Q=list(map(str,Q)),
                             derivative_mod_p=int(Q.derivative()(c))%p,content_loss_exponent=loss))
    result=dict(rows=rows,lost_multiplicity_examples=examples)
    Path(__file__).with_name('root_evaluation_smith.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(examples,indent=2))


if __name__=='__main__':main()
