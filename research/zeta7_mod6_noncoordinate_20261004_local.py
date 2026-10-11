"""A bounded actual-quotient test of a nearby unsafe three-direction tail.

This checks polynomial bad layers only. Pole terms are intentionally not
identified with this local matrix. No irrationality assertion follows.
"""
import json
from pathlib import Path
from flint import nmod_mat
from zeta7_space_extension_probe import basis, moment_layers
from zeta7_mod6_noncoordinate_20261004 import kernel

ROOT=Path(__file__).parent
PREFIX='zeta7_mod6_noncoordinate_20261004'

def points(p):
    return [(1,a,b) for a in range(p) for b in range(p)]+[(0,1,b) for b in range(p)]+[(0,0,1)]

def restriction(M,u,p):
    E=nmod_mat([list(row) for row in kernel(u)],p)
    return E*M*E.transpose()

K,N,H=80,2,78
saved=json.loads((ROOT/f'{PREFIX}_n2.json').read_text(encoding='utf-8'))
F=saved['head_indices'];tail=[73,74,76]
D,W,root,T=basis(K,N,H);local,sums,layers=moment_layers(K,N,H,D,W,root)
out=dict(K=K,N=N,H=H,fixed_head=F,nearby_tail=tail,cases=[],
         scope='Actual transformed polynomial bad moments only; whole-pencil integrality not asserted.')
for row in local:
    p=row['p'];L=layers[p]
    cross=nmod_mat([[int(L[i,j]) for j in tail] for i in F],p)
    tailform=nmod_mat([[int(L[i,j]) for j in tail] for i in tail],p)
    assert cross.rank()==0
    solutions=[]
    for u in points(p):
        R=restriction(tailform,u,p)
        if R.rank()==0:solutions.append(list(u))
    if p==29:
        assert solutions==[[1,0,0],[0,1,0]]
        gamma=row['gamma_values'][0]
        assert [[int(tailform[i,j]) for j in range(3)] for i in range(3)]==[[0,gamma,0],[gamma,0,0],[0,0,0]]
        tests=[]
        for a,b in ((1,0),(0,1),(1,1),(-1,2)):
            u=(1,p*a,p*b);assert restriction(tailform,u,p).rank()==0
            tests.append(dict(normal=list(u),restriction_rank=0))
    else:
        assert p==31 and tailform.rank()==0 and len(solutions)==p*p+p+1
        tests=[]
    out['cases'].append(dict(prime=p,bad_moments=row['bad_moments'],antidiagonals=row['antidiagonals'],
                            quotient_element_checks=row['quotient_checks'],head_tail_rank=cross.rank(),
                            tail_matrix=[[int(tailform[i,j]) for j in range(3)] for i in range(3)],
                            tail_rank=tailform.rank(),projective_normals_tested=p*p+p+1,
                            isotropic_count=len(solutions),isotropic_normals=solutions if p==29 else 'all',
                            saturated_congruence_tests=tests))
(ROOT/f'{PREFIX}_local.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
for c in out['cases']:print('p',c['prime'],'rank',c['tail_rank'],'isotropic planes',c['isotropic_count'],flush=True)
