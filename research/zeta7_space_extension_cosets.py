"""One bounded mixed mod-6 coset test at K=80,N=2 for zeta(7).

The uniform theorem starts at n>=4; this n=2 instance independently checks
that all actual outer bad moments are still the m=6 ones.
"""
import json
from pathlib import Path
from flint import fmpq_mat as Mat, nmod_mat
from joint_exact import entries
from zeta7_space_extension_probe import basis,moment_layers,evaluate


def main():
    n=2;K=40*n;N=n;H=39*n
    D,W,root,T=basis(K,N,H)
    aa,bb=entries(K,[(N,8)],H)
    A=T*Mat([[aa[i+j] for j in range(H)] for i in range(H)])*T.transpose()
    B=T*Mat([[bb[i+j] for j in range(H)] for i in range(H)])*T.transpose()
    local,sums,layers=moment_layers(K,N,H,D,W,root)
    assert all(row['bad_moments']==[3*row['p']-4] for row in local)
    c=(2*n+5)%6
    residue_set=[0,1,4]
    assert all((i+j)%6!=c for i in residue_set for j in residue_set)
    r=33*n-2
    keep=list(range(r))+[i for i in range(r,H) if i%6 in residue_set]
    assert len(keep)==71
    assert all(i+j not in sums for i in keep for j in keep)
    for p,L in layers.items():
        assert nmod_mat([[int(L[i,j]) for j in keep] for i in keep],p).rank()==0
    base=evaluate(A,B,list(range(len(keep))),K,'low_degree_h71',layers)
    mixed=evaluate(A,B,keep,K,'mixed_mod6_014',layers)
    mixed.update(log_delta_ratio=mixed['log_delta']-base['log_delta'],
                 log_content_ratio=mixed['log_content']-base['log_content'],
                 log_primitive_ratio=mixed['log_primitive']-base['log_primitive'])
    out=dict(status='finite_exact_and_Arb_checks_passed',K=K,N=N,ambient=H,
             basis_root=list(map(str,root)),head_dimension=r,
             forbidden_residue=c,residue_set=residue_set,
             polynomial_layers=local,rows=[base,mixed],
             scope='K=80 mixed coset only; all actual bad layers independently checked. '
                   'No asymptotic irrationality result or optimality claim.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':
    main()
