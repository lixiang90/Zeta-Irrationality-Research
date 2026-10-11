"""Exact universal leading pole packet for a six-pole residue class.

This describes the pole contribution only. It does not identify the full
Schur block, which also includes quotient moments and coupling terms.
"""
import json,itertools
from pathlib import Path
import sympy as S

if __name__=='__main__':
    H=S.Symbol('H');nodes=[0,1,-1,-2,2,3]
    weights={-1:S.Integer(1),-2:H,2:S.Integer(1),3:H}
    cs=[S.factor(sum(w*z**k/S.prod(z-y for y in nodes if y!=z) for z,w in weights.items()))
        for k in range(15)]
    determinants=[]
    for size in range(1,5):
        M=S.Matrix(size,size,lambda i,j:cs[i+j]);d=S.factor(M.det())
        value=d.subs(H,S.Rational(129,128))
        determinants.append(dict(size=size,formula=str(d),value=str(value),
                                 numerator_factors={str(p):v for p,v in S.factorint(S.numer(value)).items()}))
    assert cs[0]==0 and S.simplify(cs[1]-(H-3)/24)==0 and S.simplify(cs[3]-(7*H-9)/24)==0
    assert S.Matrix(4,4,lambda i,j:cs[i+j]).det().factor()==H**2/144
    exceptional_minors=[]
    for r in [2,3]:
        for ii in itertools.combinations(range(5),r):
            for jj in itertools.combinations(range(5),r):
                d=S.factor(S.Matrix(r,r,lambda i,j:cs[ii[i]+jj[j]]).det())
                value=d.subs(H,S.Rational(129,128))
                if value and any(int(S.numer(value))%p==0 for p in [53,83]):
                    exceptional_minors.append(dict(rows=ii,columns=jj,formula=str(d),value=str(value),
                       numerator_factors={str(p):v for p,v in S.factorint(S.numer(value)).items()}))
    out=dict(nodes=nodes,moments=[str(c) for c in cs],determinants=determinants,
             selected_exceptional_minors=exceptional_minors,
             scope='universal pole-packet algebra only, not a complete-pencil Smith theorem')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out),flush=True)
