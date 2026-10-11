"""Exact congruence lattices and bounded searches in a reduced basis.

Search failures are bounded-search observations, not nonexistence proofs.
"""
import itertools
import json
import math
from pathlib import Path
from flint import fmpz_mat, fmpq, arb, ctx
from joint_positive_module import saturated_kernel, rows_of


def probe(row,source,modulus,radius=3):
    C=fmpz_mat(row['matrix']);L=fmpz_mat(row['saturated_nuisance_kernel'])
    G=row['eliminated_target_map'];m=modulus
    augmented=[G[i]+[-m if j==i else 0 for j in range(2)] for i in range(2)]
    K,U=saturated_kernel(augmented)
    Z=fmpz_mat([[K[i,j] for j in range(4)] for i in range(4)])
    index=abs(int(Z.det()));smith=list(map(int,row['target_smith_invariants']))
    expected=math.prod(m//math.gcd(m,s) for s in smith);assert index==expected
    basis=(L*Z).transpose();reduced,T=basis.lll(transform=True)
    assert reduced==T*basis and abs(int(T.det()))==1
    RB=rows_of(reduced);Rout=rows_of((C*reduced.transpose()).transpose())
    assert all(v[1]==v[2]==0 and all(x%m==0 for x in v) for v in Rout)
    lo=fmpq(source['lower']['endpoint']);hi=fmpq(source['upper']['endpoint'])
    positive=0;zero_outputs=0;best=None;best_bound=None;directions=set()
    for coeff in itertools.product(range(-radius,radius+1),repeat=4):
        if not any(coeff):continue
        if next(x for x in coeff if x)!=abs(next(x for x in coeff if x)):continue
        c=[sum(coeff[i]*RB[i][j] for i in range(4)) for j in range(6)]
        out=[sum(coeff[i]*Rout[i][j] for i in range(4)) for j in range(4)]
        if not any(out):zero_outputs+=1
        if all(x<=0 for x in c):c=[-x for x in c];out=[-x for x in out]
        if not all(x>=0 for x in c):continue
        positive+=1;assert any(out)
        content=math.gcd(*out);a,b=out[0]//content,out[3]//content
        assert content%m==0 and a+b*lo>=0 and a+b*hi>=0
        bound=max(a+b*lo,a+b*hi);directions.add((a,b))
        if best is None or bound<best_bound:
            best_bound=bound;best=dict(input=list(map(str,c)),input_content=str(math.gcd(*c)),
                output=list(map(str,out)),output_content=str(content),primitive_pair=[a,b],
                rational_upper=str(bound),coefficient_l1=str(sum(c)))
    with ctx.workprec(256):
        return dict(n=row['n'],w=row['w'],modulus=m,index=str(index),
            change_of_lattice_basis=rows_of(Z),augmented_hnf_transform=rows_of(U),
            reduced_basis=RB,lll_transform=rows_of(T),radius=radius,
            checked_up_to_sign=((2*radius+1)**4-1)//2,positive_vectors=positive,
            distinct_primitive_outputs=len(directions),zero_output_vectors=zero_outputs,
            best=best,best_upper_arb=None if best is None else arb(best_bound).str(18))


def main():
    folder=Path(__file__).parent
    modules=json.loads((folder/'joint_positive_module.json').read_text())['rows']
    sources=json.loads((folder/'growing_positive_moment.json').read_text())['rows'];rows=[]
    for n in (8,16,24,32):
        row=next(x for x in modules if x['n']==n and x['w']==n)
        source=next(x for x in sources if x['n']==n)
        for m in (1,5,25,1009,1009**2):
            result=probe(row,source,m);rows.append(result)
            print(n,m,'index',result['index'],'positive',result['positive_vectors'],
                'zero outputs',result['zero_output_vectors'],'best',result['best_upper_arb'],flush=True)
        (folder/'joint_positive_congruence_probe.json').write_text(json.dumps(dict(
            scope='Exact congruence-lattice index and finite radius-three LLL-coordinate searches. No unbounded search or irrationality conclusion.',
            rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
