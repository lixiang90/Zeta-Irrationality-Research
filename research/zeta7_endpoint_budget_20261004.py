"""Uniform arithmetic-coset upper bound for Schur endpoint candidates.

Uses full coefficient content in the integer coset parameter, including 17.
This is a finite audit of an infinite-scale sufficient criterion, not an
irrationality proof.
"""
import hashlib,json,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
from joint_exact import content
from zeta7_moment_extension_20261004 import aq

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def main():
    inputs={name:(ROOT/name).read_bytes() for name in
            ['zeta7_two_moment_partial_20261004_coefficients.json',
             'zeta7_joint_lattice_20261004_completion.json']}
    packet=json.loads(inputs['zeta7_two_moment_partial_20261004_coefficients.json'])
    source=json.loads(inputs['zeta7_joint_lattice_20261004_completion.json'])
    coeff=[(r['i'],r['j'],Poly([Q(v) for v in r['polynomial_coefficients']])) for r in packet['coefficients']]
    ctx.prec=16000;z=arb(7).zeta();rows=[]
    for r in source['rows']:
        if not r.get('completion_possible'):continue
        x=Q(r['x']);L=int(r['y_conductor']);uy=-pow(L,-1,17)%17;a=Q(L*uy,17)
        f=[sum((p*x**i for i,j,p in coeff if j==jj),Poly()) for jj in range(3)]
        integer_parameter_coeff=[f[0]+a*f[1]+a*a*f[2],L*f[1]+2*a*L*f[2],L*L*f[2]]
        cstar=content(Poly([v for p in integer_parameter_coeff for v in p]));assert cstar>0
        radius=arb(r['radius_interval']);assert radius*2>L
        det_head=-arb_poly([aq(v) for v in f[2]])(z);assert det_head>0
        upper=2*radius*L*det_head/aq(cstar);assert upper>0
        for c in r['choices']:
            y=Q(c['y']);k=(y-a)/L;assert k.denominator==1
            poly=f[0]+f[1]*y+f[2]*y*y
            ct=content(poly);ratio=ct/cstar;assert ratio.denominator==1
            val=arb_poly([int(v) for v in poly/ct])(z);assert val>0
            assert val<upper
        rows.append(dict(powers=r['powers'],x=str(x),coset_start=str(a),coset_step=str(L),
             all_parameter_content=str(cstar),positive_interval_wider_than_step=True,
             log_uniform_primitive_upper_bound=upper.log().str(70),
             log_uniform_primitive_upper_bound_midpoint=float(upper.log()),
             certified_endpoint_candidates=len(r['choices'])))
    best=min(rows,key=lambda r:r['log_uniform_primitive_upper_bound_midpoint'])
    out=dict(status='uniform_coset_endpoint_bound_checked',K=source['K'],N=source['N'],h=source['h'],
             input_sha256={k:hashlib.sha256(v).hexdigest() for k,v in inputs.items()},rows=rows,best_bound=best,
             scope='Nine fixed-x Schur completions and a written sufficient infinite-scale criterion. '
                   'No asymptotic negative exponent established.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('rows',len(rows),'best powers',best['powers'],'log upper',best['log_uniform_primitive_upper_bound'],flush=True)


if __name__=='__main__':main()
