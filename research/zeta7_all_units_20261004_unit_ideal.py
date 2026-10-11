"""All-unit exclusions on fixed Newton faces by finite Macaulay identities.

Any isolated parameter monomial is a unit on this domain.  Thus a certificate
p^A U^i V^j in the coefficient ideal modulo p^D with A<D excludes every higher
unit pair, without expanding a Hensel tree.
"""
import json,sys,math
from pathlib import Path
from flint import fmpq as Q
from zeta7_all_units_20261004 import valq,modq
from zeta7_all_units_20261004_macaulay import reduce

sys.set_int_max_str_digits(0)


def main():
    p=int(sys.argv[1]) if len(sys.argv)>1 else 2
    shift_degree=int(sys.argv[2]) if len(sys.argv)>2 else 4
    folder=Path(__file__).parent
    d=json.loads((folder/'zeta7_two_moment_partial_20261004_coefficients.json').read_text(encoding='utf-8'))
    coeff=[(r['i'],r['j'],[Q(c) for c in r['polynomial_coefficients']]) for r in d['coefficients']]
    v0=valq(Q(json.loads((folder/'zeta7_joint_lattice_20261004_completion.json').read_text(encoding='utf-8'))['original_baseline_content']),p)
    fronts=json.loads((folder/f'zeta7_all_units_20261004_hensel_p{p}.json').read_text(encoding='utf-8'))
    pairs=[(r['a'],c['b']) for r in fronts['rows'] for c in r['cases'] if c['status']=='unresolved_frontier_cap' and 'b' in c]
    shifts=[(a,b) for a in range(shift_degree+1) for b in range(shift_degree+1-a)]
    results=[]
    for a,b in pairs:
        minimum=min(valq(c,p)+i*a+j*b for i,j,cs in coeff for c in cs if c);D=v0-minimum;mod=p**D
        polys=[{} for _ in range(38)]
        for i,j,cs in coeff:
            for k,c in enumerate(cs):
                if not c:continue
                scaled=c*Q(p)**(i*a+j*b-minimum)
                if valq(scaled,p)<D:polys[k][(i,j)]=modq(scaled,p,mod)
        monomials=sorted(set((i+r,j+s) for poly in polys for i,j in poly for r,s in shifts))
        index={v:i for i,v in enumerate(monomials)};A=[];labels=[]
        for r,s in shifts:
            for k,poly in enumerate(polys):
                if not poly:continue
                row=[0]*len(monomials)
                for (i,j),c in poly.items():row[index[(i+r,j+s)]]=c
                A.append(row);labels.append([k,r,s])
        diagonal,certificates=reduce(A,p,D,None)
        column,conductor,R=certificates[0];i,j=monomials[column]
        result=dict(a=a,b=b,target_power=D,coefficient_minimum_valuation=minimum,
                    shift_degree=shift_degree,rows=len(A),columns=len(monomials),
                    unit_monomial=[i,j],conductor=conductor,
                    all_unit_exclusion_certified=conductor<D,
                    multipliers=list(map(str,R)),row_labels=labels,monomials=monomials,
                    scaled_macaulay_matrix=[[str(v) for v in row] for row in A])
        results.append(result)
        print('p',p,'face',a,b,'matrix',len(A),len(monomials),'unit-conductor',conductor,'D',D,'excluded',conductor<D,flush=True)
        out=dict(status='in_progress',K=40,N=3,h=37,p=p,shift_degree=shift_degree,results=results,
                 scope='Every successful modular identity excludes all unit digits on its fixed valuation pair. '
                       'A conductor equal to the target is an unresolved case, not an existence proof.')
        Path(__file__).with_name(Path(__file__).stem+f'_p{p}_d{shift_degree}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed';Path(__file__).with_name(Path(__file__).stem+f'_p{p}_d{shift_degree}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
