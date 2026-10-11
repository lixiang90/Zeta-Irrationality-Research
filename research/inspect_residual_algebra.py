"""Exact diagnostics of the difficult p=17, level-three residual system."""
import json
from pathlib import Path
from flint import nmod_mat
from padic_subspace_flags import rows


def run():
    data=json.loads(Path(__file__).with_name('padic_subspace_flags_K24_N1_m24.json').read_text())
    row=next(r for r in data['flags'] if r['p']==17 and r['step']==3)
    p=17; Q=[nmod_mat(q,p) for q in row['residual_form_basis']]; n=Q[0].nrows()
    print('ranks',[q.rank() for q in Q])
    R=next((q for q in Q if q.det()),None)
    if R is None:
        R=sum(Q,nmod_mat(n,n,p))
    print('R determinant',R.det())
    if R.det():
        M=[R.inv()*q for q in Q]
        assert all(a*b==b*a for a in M for b in M)
        generator=M[1]; cp=generator.charpoly()
        assert cp.gcd(cp.derivative()).degree()==0
        powers=[]; power=R
        for k in range(n):
            powers.append(power); power=power*generator
        qflat=nmod_mat(n,n*n,[int(x) for q in Q for x in q.entries()],p)
        rr,rank=qflat.rref(); assert rank==n
        pivots=[next(j for j in range(n*n) if rr[i,j]) for i in range(n)]
        minor=nmod_mat(n,n,[int(qflat[i,j]) for i in range(n) for j in pivots],p)
        power_minor=nmod_mat(n,n,[int(q.entries()[j]) for q in powers for j in pivots],p)
        change=power_minor*minor.inv()
        assert change.det()
        assert change*qflat==nmod_mat(n,n*n,[int(x) for q in powers for x in q.entries()],p)
        certificate=dict(p=p,dimension=n,base_form_index=0,generator_form_index=1,
                         base_form=rows(R),generator=rows(generator),
                         characteristic_polynomial=[int(c) for c in cp],
                         squarefree=True,power_coefficients=rows(change),
                         factorization=[dict(coefficients=[int(c) for c in f],exponent=e)
                                        for f,e in cp.factor()[1]],
                         conclusion='The only common quadratic zero, even over the algebraic closure, is zero.')
        output=Path(__file__).with_name('residual_etale_certificate_K24_p17_level3.json')
        output.write_text(json.dumps(certificate,indent=2),encoding='utf-8')
        print(json.dumps(dict(determinant_R=int(R.det()),determinant_change=int(change.det()),
                             characteristic_polynomial=str(cp),
                             factorization=[(str(f),e) for f,e in cp.factor()[1]],
                             squarefree=True,power_span_verified=True)),flush=True)


if __name__=='__main__':
    run()
