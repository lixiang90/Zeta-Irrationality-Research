"""Exact leading-coefficient barrier for the uniform Schur endpoint bound.

All content ratios are exact. Arb audits the primitive head value and the
parameter-specific endpoint/content decomposition on nine saved cosets.
"""
import hashlib,json,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
from joint_exact import content
from zeta7_moment_extension_20261004 import aq

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def main():
    filenames=['zeta7_two_moment_partial_20261004_coefficients.json',
               'zeta7_joint_lattice_20261004_completion.json','zeta7_endpoint_budget_20261004.json']
    sources={name:(ROOT/name).read_bytes() for name in filenames}
    packet=json.loads(sources[filenames[0]]);completion=json.loads(sources[filenames[1]])
    budget=json.loads(sources[filenames[2]])
    coeff=[(r['i'],r['j'],Poly([Q(v) for v in r['polynomial_coefficients']])) for r in packet['coefficients']]
    ctx.prec=16000;z=arb(7).zeta();rows=[]
    for r,br in zip(completion['rows'],budget['rows']):
        assert r['completion_possible'] and r['powers']==br['powers']
        x=Q(r['x']);L=Q(r['y_conductor']);alpha=Q(br['coset_start'])
        f=[sum((p*x**i for i,j,p in coeff if j==jj),Poly()) for jj in range(3)]
        head=-f[2];cT=content(head);pT=head/cT
        assert all(v.denominator==1 for v in pT) and content(pT)==1
        cstar=Q(br['all_parameter_content']);M=L*L*cT/cstar
        assert M>0 and M.denominator==1
        assert content(-L*L*head/cstar)==M
        phead=arb_poly([int(v) for v in pT])(z);assert phead>0
        center=arb(r['center_interval']);R=arb(r['radius_interval']);assert 2*R>aq(L)
        geometric=2*R/aq(L);factor=geometric*aq(M)
        U=phead*factor;assert U>phead
        assert U.log().overlaps(arb(br['log_uniform_primitive_upper_bound']))
        endpoints=[]
        for c in r['choices']:
            y=Q(c['y']);delta=(center+R-aq(y)) if c['endpoint']=='upper' else (aq(y)-center+R)
            assert delta>0 and delta<=aq(L)
            poly=f[0]+y*f[1]+y*y*f[2];ct=content(poly);J=ct/cstar
            assert J>0 and J.denominator==1
            ratio=factor*(delta/aq(L))*(1-delta/(2*R))/aq(J)
            pvalue=arb_poly([int(v) for v in poly/ct])(z);assert pvalue>0
            assert (pvalue-phead*ratio).contains(0)
            endpoints.append(dict(endpoint=c['endpoint'],extra_parameter_content_integer=str(J),
                log_extra_parameter_content=aq(J).log().str(60),
                log_fractional_endpoint_distance=(delta/aq(L)).log().str(60),
                log_endpoint_shape_factor=(1-delta/(2*R)).log().str(60),
                log_candidate_to_head_ratio=ratio.log().str(60),
                log_candidate_primitive=pvalue.log().str(60)))
        rows.append(dict(powers=r['powers'],x=str(x),degree_head=pT.degree(),head_content=str(cT),
            uniform_content_integer_M=str(M),log_head_primitive=phead.log().str(60),
            log_head_primitive_midpoint=float(phead.log()),log_radius_to_step=geometric.log().str(60),
            log_uniform_content_integer_M=aq(M).log().str(60),
            log_uniform_bound_excess_over_head=factor.log().str(60),endpoints=endpoints))
    out=dict(status='exact_head_content_barrier_and_arb_decompositions_passed',
        input_sha256={k:hashlib.sha256(v).hexdigest() for k,v in sources.items()},rows=rows,
        scope='General written leading-coefficient barrier and nine finite coset checks. '
              'No asymptotic decay or full parameter-content bound asserted.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    best=min(rows,key=lambda r:r['log_head_primitive_midpoint'])
    print('cases',len(rows),'smallest log head',best['log_head_primitive'],'powers',best['powers'],flush=True)
    chosen=next(r for r in rows if r['powers']==[64,24,10,7])
    print('old best head',chosen['log_head_primitive'],'U/head log',chosen['log_uniform_bound_excess_over_head'],flush=True)
    print('upper endpoint decomposition',chosen['endpoints'][1],flush=True)


if __name__=='__main__':main()
