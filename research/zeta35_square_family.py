"""Rational parametrization of positive, target-preserving square modifiers."""
import json
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly
from zeta35_numerator_space import coefficient_map,combine,evaluate


def run(N,M,degree):
    shift=(M+1)*(M+N+1)
    rows=coefficient_map(N,M,2*degree+1,shift)
    T=[v[1]-3*v[0] for v in rows]
    lam=-T[1]/T[0] # base polynomial z+lam, z=y-shift
    assert lam>0
    J=[[ (rows[j+1][i]+lam*rows[j][i])/N**(2*j) for i in range(3)] for j in range(2*degree+1)]
    S=[v[1]-3*v[0] for v in J]
    assert S[0]==0
    directions=[]
    for k in range(1,degree+1):
        directions.append((f'monomial_{k}',Poly([0]*k+[1])))
        for root in (Q(1,4),Q(1,2),Q(1),Q(2),Q(4),Q(8)):
            directions.append((f'root_{root}_power_{k}',Poly([1,-1/root])**k-1))
    output=[]
    for name,v in directions:
        B=sum((v[j]*S[j] for j in range(len(v))),Q(0))
        vv=v*v
        A=sum((vv[j]*S[j] for j in range(len(vv))),Q(0))
        q=Poly([A])-2*B*v
        if not q:
            q=v
        qq=q*q
        coeff=combine(J,qq)
        assert coeff[1]==3*coeff[0]
        if q.degree()==0:
            continue
        val=evaluate(coeff[0],coeff[2])
        output.append(dict(direction=name,q=[str(c) for c in q],**val))
    baseline=evaluate(J[0][0],J[0][2])
    best=min(output,key=lambda r:r['log_L'])
    print('square',N,M,degree,'tested',len(output),'base',round(baseline['log_L'],6),
          'best',best['direction'],round(best['log_L'],6),flush=True)
    return dict(N=N,M=M,degree=degree,shift=shift,lambda_shifted=str(lam),
                baseline=baseline,best=best,count=len(output),
                rows=[[str(c) for c in v] for v in J],candidates=output)


if __name__=='__main__':
    cases=[]
    for N in (10,20,40,80):
        cases.append(run(N,N,N//2))
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(
        scope='exact square-family parametrization and finite direction scan; no asymptotic success',cases=cases),indent=2),encoding='utf-8')
