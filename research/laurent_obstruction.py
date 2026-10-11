"""Exact finite-field audit of the universal Laurent obstruction model."""
import json
from pathlib import Path
from flint import nmod_poly,nmod_mat
from joint_exact import Dcache


def check(p,a,d):
    D=nmod_poly([int(c)%p for c in Dcache(a)],p)
    moments=[]
    for k in range(2*d-1):
        if a==0:moments.append(0)
        else:
            remainder=nmod_poly([0]*k+[1],p)%D
            moments.append(int(remainder[a-1]))
    M=nmod_mat(d,d,[moments[i+j] for i in range(d) for j in range(d)],p)
    rank=M.rank();b=max(0,min(a,2*d-a));assert rank==b
    if a<=d:basis=[D*nmod_poly([0]*k+[1],p) for k in range(d-a)]
    else:basis=[nmod_poly([0]*k+[1],p) for k in range(min(d,a-d))]
    if basis:
        Z=nmod_mat(d,len(basis),[int(q[i]) for i in range(d) for q in basis],p)
        assert Z.rank()==d-b and not M*Z
    else:assert b==d
    return dict(p=p,a=a,d=d,rank=rank,radical_dimension=d-b)


if __name__=='__main__':
    rows=[check(p,a,d) for p in [11,13,17,43,53,83] for d in range(1,9)
          for a in range(min((p-1)//2,2*d+1)+1)]
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(cases=len(rows),rows=rows),indent=2))
    print(json.dumps(dict(cases=len(rows),all_rank_and_radical_checks=True)))
