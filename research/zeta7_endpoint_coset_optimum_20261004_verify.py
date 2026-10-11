"""Independent ideal/root verification and source-matrix audit of the optimum."""
import hashlib,json,math,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,arb_poly,ctx
import b8_hankel as b8
from joint_exact import content,determinant
from zeta7_moment_extension_20261004 import aq,positive_pivots

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def main():
    names=['zeta7_endpoint_coset_content_20261004.json','zeta7_endpoint_coset_optimum_20261004.json',
           'zeta7_two_moment_partial_20261004_coefficients.json']
    sources={n:(ROOT/n).read_bytes() for n in names}
    data,opt,packet=[json.loads(sources[n]) for n in names]
    F=data['normalized_coefficient_rows']
    assert data['input_sha256'][names[2]]==hashlib.sha256(sources[names[2]]).hexdigest()
    assert opt['input_sha256'][names[0]]==hashlib.sha256(sources[names[0]]).hexdigest()
    x=Q(opt['x']);alpha=Q(opt['coset_start']);L=Q(opt['coset_step']);cs=Q(opt['all_parameter_content'])
    f=[sum((Poly([Q(v) for v in r['polynomial_coefficients']])*x**r['i']
            for r in packet['coefficients'] if r['j']==j),Poly()) for j in range(3)]
    normalized=[(f[0]+alpha*f[1]+alpha*alpha*f[2])/cs,
                L*(f[1]+2*alpha*f[2])/cs,L*L*f[2]/cs]
    assert all(v.denominator==1 for p in normalized for v in p)
    assert F==[[int(p[e]) for p in normalized] for e in range(38)]
    for c in data['constant_certificates']:
        values=[0]*(c['degree']+1)
        for term in c['identity_multipliers']:
            e=term['X_coefficient'];s=term['k_power'];w=int(term['multiplier'])
            for j,a in enumerate(F[e]):values[j+s]+=w*a
        assert values==[int(c['constant'])]+[0]*c['degree']
    d=int(data['constant_certificates'][-1]['constant'])
    assert math.prod(int(p)**e for p,e in data['constant_factorization'].items())==d
    lifts=0
    for local in data['local_classes']:
        p=local['p'];old=[0];power=1
        for level in local['levels']:
            modulus=power*p
            candidates=[a+digit*power for a in old for digit in range(p)]
            roots=[a for a in candidates if all((u+v*a+w*a*a)%modulus==0 for u,v,w in F)]
            expected=[]
            for ball in level['root_cosets']:
                residue=int(ball['residue']);step=p**ball['modulus_exponent']
                expected.extend(range(residue,modulus,step))
            assert sorted(roots)==sorted(expected)
            lifts+=len(candidates);old=roots;power=modulus
    K,N,h,A,B=b8.entries(1);assert (K,N,h)==(40,3,37)
    W=Poly(b8.Dpoly(N))**8;D=Poly(b8.Dpoly(K))
    quot=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    y=Q(opt['minimum']['y']);k=int(opt['minimum']['k'])
    AA=[A[s]-x*quot[s][47]-y*quot[s][55] for s in range(2*h-1)]
    source_poly=determinant(AA,B,h)
    expected=sum((Poly([Q(c) for c in r['polynomial_coefficients']])*x**r['i']*y**r['j']
                 for r in packet['coefficients']),Poly())
    assert source_poly==expected
    ct=content(source_poly);J=ct/cs
    assert J.denominator==1 and str(J)==opt['minimum']['extra_content']
    assert int(J)==math.gcd(*(a+b*k+c*k*k for a,b,c in F))
    ctx.prec=16000;z=arb(7).zeta()
    H=arb_mat([[aq(AA[i+j])+z*aq(B[i+j]) for j in range(h)] for i in range(h)])
    pivots=positive_pivots(H);assert pivots['positive_definite'] is True
    primitive=source_poly/ct;assert all(c.denominator==1 for c in primitive)
    value=arb_poly([int(v) for v in primitive])(z)
    assert value>0 and (H.det()-aq(ct)*value).contains(0)
    assert value.log().overlaps(arb(opt['minimum']['log_primitive'])) and value.log()>1390
    out=dict(status='independent_constant_identities_full_hensel_lifts_and_source_matrix_passed',
        input_sha256={n:hashlib.sha256(v).hexdigest() for n,v in sources.items()},
        integer_ideal_identities=len(data['constant_certificates']),full_hensel_candidates=lifts,
        exact_source_determinant_coefficients=len(source_poly),primitive_degree=primitive.degree(),
        full_content=str(ct),extra_content=str(J),positive_check=pivots,
        log_primitive_from_source_matrix=value.log().str(70),
        scope='Independent exact ideal and complete local-root verification; source-matrix '
              'verification of the globally selected endpoint. The global CRT/concavity '
              'reduction is a mathematical lemma stated in the companion report.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('all checks passed; explicit Hensel candidates',lifts,'degree',primitive.degree(),
          'log primitive',out['log_primitive_from_source_matrix'],flush=True)


if __name__=='__main__':main()
