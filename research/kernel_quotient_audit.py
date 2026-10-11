"""Independent exact audit of the polynomial-quotient part of the new proof.

This separates quotient moments from pole terms, so a final cancellation
cannot mask a wrong component estimate in the written Taylor argument.
"""
import json
from pathlib import Path
from flint import fmpq_poly
from joint_exact import Dcache,moment
from joint_padic import val
from layer_projection import local_basis


def audit(p,N,a=None):
    boundary=a is None;K=2*p-1 if boundary else 3*p-1-a;h=K-N
    basis,_,tags=local_basis(K,N,p);W=Dcache(N)**8;F=Dcache((p-1)//2)
    if boundary:
        for j in range(2*p,3*p):W*=fmpq_poly([j*j,1])
        phi=fmpq_poly([0,1])*(F**6//Dcache(N)**5)
    else:phi=fmpq_poly([0,0,1])*(F**8//Dcache(N)**5)
    checks=0;rows=[];D=Dcache(K)
    for E,tag in zip(basis,tags):
        c,i=tag['c'],tag['i']
        if boundary:
            lower=2 if not c else ((1 if i==0 else 2) if tag['delta'] else (-1 if i<2 else 0))
        else:
            lower=(1 if i==0 else 3) if not c else (min(i-(c>a),3) if tag['delta'] else (-1 if i<4 else 0))
        values=[];P=W*phi*E
        for k in range(h-phi.degree()):
            quotient=(P*fmpq_poly([0]*k+[1]))//D
            value=sum((q*moment(j) for j,q in enumerate(quotient)),0)
            values.append(val(value,p));assert values[-1]>=lower;checks+=1
        rows.append(dict(c=c,i=i,proved_lower=lower,observed_minimum=min(values)))
    return dict(p=p,N=N,a=a,family='boundary' if boundary else 'six_pole',checks=checks,rows=rows)


if __name__=='__main__':
    rows=[audit(11,4),audit(13,5),audit(11,4,0),audit(11,4,2),audit(11,4,4),audit(13,5,2)]
    result=dict(checks=sum(r['checks'] for r in rows),rows=rows)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(cases=len(rows),checks=result['checks'],all_component_bounds_pass=True)))
