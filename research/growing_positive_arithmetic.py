"""Exact determinant content and positive first-term budgets for moment edges."""
import json
import math
from pathlib import Path
from flint import fmpq, fmpq_mat, arb, ctx
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from growing_positive_moment import shifted_map, dot, node, eval_poly


def small_prime_split(value,cutoff):
    remainder=abs(value);factors=[]
    for p in range(2,cutoff+1):
        if any(p%q==0 for q in range(2,math.isqrt(p)+1)):continue
        exponent=0
        while remainder%p==0:remainder//=p;exponent+=1
        if exponent:factors.append([p,exponent])
    return factors,remainder


def audit(edge,M):
    n,w=edge['n'],edge['w'];h=list(map(fmpq,edge['H']))
    B=[[dot(line,[fmpq(0)]*i+h) for i in range(3)] for line in M]
    denominator=math.lcm(*(int(x.denominator) for line in B for x in line))
    ints=[[int(x*denominator) for x in line] for line in B]
    # Divide column contents before taking minors: these known factors cancel
    # identically in both determinants and should not be called new savings.
    contents=[math.gcd(*(row[j] for row in ints)) for j in range(3)]
    primitive_columns=[[row[j]//contents[j] for j in range(3)] for row in ints]
    det0=int(fmpq_mat([primitive_columns[k] for k in (0,1,2)]).det())
    det7=int(fmpq_mat([primitive_columns[k] for k in (3,1,2)]).det())
    g=math.gcd(det0,det7);assert g>0 and det7
    r3,r5=primitive_columns[1],primitive_columns[2]
    vector=[r3[1]*r5[2]-r3[2]*r5[1],r3[2]*r5[0]-r3[0]*r5[2],r3[0]*r5[1]-r3[1]*r5[0]]
    input_content=math.gcd(*vector);assert input_content>0 and g%input_content==0
    primitive_input_content=g//input_content
    snf=smith_normal_form(S.Matrix(primitive_columns),domain=S.ZZ)
    smith=[abs(int(snf[i,i])) for i in range(3)]
    assert all(smith) and smith[2]%primitive_input_content==0
    pair=edge['primitive_output']
    assert abs(det7)//g==abs(pair[1]) and fmpq(-det0,det7)==fmpq(edge['endpoint'])
    P=list(map(fmpq,edge['polynomial']));scale=fmpq(edge['primitive_scale']);assert scale>0
    r=0
    while eval_poly(P,node(n,r))==0:r+=1
    t=n+1+r;x=2*t+n
    factor=fmpq(math.prod(x*x-(n+2*j)**2 for j in range(1,n+1)),math.prod((t+j)**7 for j in range(n+1)))
    first=scale*factor*eval_poly(P,node(n,r));assert first>0
    cutoff=8*n
    gcd_small,gcd_rough=small_prime_split(g,cutoff)
    denominator_small,denominator_rough=small_prime_split(abs(pair[1]),cutoff)
    smith_small,smith_rough=small_prime_split(smith[-1],cutoff)
    denominator_smooth=abs(pair[1])//denominator_rough
    with ctx.workprec(256):
        rate=lambda x:(arb(x).log()/n).str(17)
        return dict(sign=edge['sign'],first_nonzero_node=r,first_term=str(first),
            first_term_greater_than_one=bool(first>1),log_first_term_per_n=rate(first),
            matrix_common_denominator=str(denominator),column_contents=list(map(str,contents)),
            primitive_column_matrix=primitive_columns,
            constant_minor=str(det0),zeta7_minor=str(det7),joint_minor_gcd=str(g),
            elimination_vector_content=str(input_content),primitive_input_output_content=str(primitive_input_content),
            smith_invariants=list(map(str,smith)),log_primitive_input_output_content_per_n=rate(primitive_input_content),
            largest_smith_small_prime_factors=smith_small,largest_smith_rough_part=str(smith_rough),
            prime_cutoff=cutoff,joint_gcd_small_prime_factors=gcd_small,
            joint_gcd_rough_part=str(gcd_rough),log_joint_gcd_rough_part_per_n=rate(gcd_rough),
            denominator_small_prime_factors=denominator_small,
            denominator_rough_part=str(denominator_rough),log_denominator_rough_part_per_n=rate(denominator_rough),
            discounted_first_term=str(first/denominator_smooth),
            log_discounted_first_term_per_n=rate(first/denominator_smooth),
            log_raw_zeta_minor_per_n=rate(abs(det7)),log_joint_gcd_per_n=rate(g),
            log_final_denominator_per_n=rate(abs(pair[1])))


def main():
    folder=Path(__file__).parent
    from positive_head_cone import cone
    source=json.loads((folder/'growing_positive_moment.json').read_text())['rows'];rows=[];head_rows=[]
    for r in source:
        M=shifted_map(r['n'],r['w'])
        edges=[audit(r[name],M) for name in ('lower','upper')]
        rows.append(dict(n=r['n'],w=r['w'],edges=edges))
        baseline=cone(r['n'],r['n']+r['w'],0)
        gain=(fmpq(baseline['upper_bound'])-fmpq(baseline['lower_bound']))/fmpq(r['width'])
        with ctx.workprec(256):
            head_rows.append(dict(n=r['n'],w=r['w'],baseline_lower=baseline['lower_bound'],
                baseline_upper=baseline['upper_bound'],gain=str(gain),gain_arb=arb(gain).str(16),
                log_gain_per_n=(arb(gain).log()/r['n']).str(16)))
        print(r['n'],r['w'],[(e['sign'],e['log_first_term_per_n'],e['log_joint_gcd_per_n']) for e in edges],flush=True)
    (folder/'growing_positive_arithmetic.json').write_text(json.dumps(dict(
        scope='Exact finite determinant-content identities and strict positive first-term lower bounds; no extrapolation to all n.',rows=rows),indent=2),encoding='utf-8')
    (folder/'growing_positive_head_comparison.json').write_text(json.dumps(dict(
        scope='Same numerator-degree budget, comparison to allocating all extra degree to a consecutive head.',rows=head_rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
