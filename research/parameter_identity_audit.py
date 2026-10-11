"""Exact independent check of the top-parameter block identity."""
import json
from pathlib import Path
from math import factorial
from flint import fmpq,fmpq_poly,fmpq_mat
from joint_exact import Dcache,entries_from_polynomial,determinant
from joint_padic import val


if __name__=='__main__':
    rows=[]
    for p,N in [(11,4),(13,5),(17,6)]:
        K=3*p-1;h=K-N;s=h-p
        aa,bb=entries_from_polynomial(K,Dcache(N)**8,h)
        T=fmpq_poly([1]);gammas=[]
        for j in range(2*p,K+1):
            T*=fmpq_poly([j*j,1])
            gamma=fmpq(2*(-1)**(j-1)*factorial(j+N)**8,
                       factorial(j-N-1)**8*factorial(K-j)*factorial(K+j))
            gammas.append((j,-gamma/p**7))
        dd=[sum((g*(-j*j)**e for j,g in gammas),fmpq(0)) for e in range(2*h-1)]
        factor=fmpq(1)
        for _,g in gammas:factor*=g
        for i,(j,_) in enumerate(gammas):
            for k,_ in gammas[i+1:]:factor*=(k*k-j*j)**2
        assert val(factor,p)==16*N-11*p+8
        lowa,lowb=entries_from_polynomial(K,Dcache(N)**8*T*T,s)
        # Independently cancel T from the denominator.
        aa2,bb2=entries_from_polynomial(2*p-1,Dcache(N)**8*T,s)
        assert lowa==aa2 and lowb==bb2
        for x in [0,1,2]:
            det_delta=determinant([a+x*b for a,b in zip(aa,bb)],dd,h)
            bottom=fmpq_mat(s,s,[lowa[i+j]+x*lowb[i+j] for i in range(s) for j in range(s)])
            assert det_delta.degree()<=p
            assert det_delta[p]==factor*bottom.det()
        rows.append(dict(K=K,N=N,p=p,x_values=[0,1,2],top_factor_valuation=val(factor,p),
                         exact_identity_passed=True))
    Path(__file__).with_suffix('.json').write_text(json.dumps(rows,indent=2))
    print(json.dumps(rows))
