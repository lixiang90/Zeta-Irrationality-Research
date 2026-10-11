"""Global primitive minimum on a fixed rational y coset.

The saved integer ideal certificate bounds every extra content J(k).  All
prime-power root balls are combined by CRT.  Concavity reduces each class
to its two points next to the positivity endpoints, without a height cut.
"""
import hashlib,itertools,json,math,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_poly,ctx
from zeta7_moment_extension_20261004 import aq

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def crt(a,m,b,n):
    if n==1:return a,m
    assert math.gcd(m,n)==1
    return a+m*((b-a)*pow(m,-1,n)%n),m*n


def unique_integer(v):
    z=v.unique_fmpz()
    assert z is not None,'insufficient precision for endpoint rounding'
    return int(z)


def main():
    names=['zeta7_endpoint_coset_content_20261004.json',
           'zeta7_joint_lattice_20261004_completion.json',
           'zeta7_two_moment_partial_20261004_coefficients.json']
    sources={n:(ROOT/n).read_bytes() for n in names}
    data,completion,packet=[json.loads(sources[n]) for n in names]
    row=next(r for r in completion['rows'] if r['powers']==data['selected_powers'])
    F=data['normalized_coefficient_rows'];x=Q(data['x'])
    alpha=Q(data['coset_start']);L=Q(data['coset_step']);cs=Q(data['all_parameter_content'])
    f=[sum((Poly([Q(v) for v in r['polynomial_coefficients']])*x**r['i']
            for r in packet['coefficients'] if r['j']==j),Poly()) for j in range(3)]
    ctx.prec=16000;z=arb(7).zeta()
    logdetT=arb_poly([aq(v) for v in -f[2]])(z).log()
    base=logdetT-aq(cs).log()
    ctx.prec=800
    center=arb(row['center_interval']);R=arb(row['radius_interval'])
    low_y=center-R;high_y=center+R
    low_k=(low_y-aq(alpha))/aq(L);high_k=(high_y-aq(alpha))/aq(L)
    options=[]
    for local in data['local_classes']:
        p=local['p'];choices=[(1,0,1)]
        for level in local['levels']:
            e=level['exponent']
            for ball in level['root_cosets']:
                choices.append((p**e,int(ball['residue']),p**ball['modulus_exponent']))
        options.append(choices)
    assert math.prod(map(len,options))==data['total_crt_classes']
    cache={};top=[];empty=0;all_floor=10**9;best=None;classes=0
    def evaluate(k):
        nonlocal all_floor,best
        if k in cache:return cache[k]
        J=math.gcd(*(a+b*k+c*k*k for a,b,c in F));assert J>0
        y=alpha+L*k
        dl=aq(y)-low_y;du=high_y-aq(y)
        assert dl>0 and du>0
        delta=dl if dl<du else du
        logP=base+(delta*(2*R-delta)).log()-arb(J).log()
        floor=unique_integer(logP.floor());all_floor=min(all_floor,floor)
        point=dict(k=str(k),y=str(y),extra_content=str(J),
            log_primitive=logP.str(70),log_primitive_midpoint=float(logP),
            log_endpoint_distance_over_step=(delta/aq(L)).log().str(60))
        cache[k]=(J,logP,point)
        if best is None or logP<best[1]:best=(k,logP,point)
        elif not logP>best[1]:
            assert k==best[0],'unresolved interval comparison for the minimum'
        return cache[k]
    for group in itertools.product(*options):
        g=1;r=0;m=1
        for gp,rp,mp in group:g*=gp;r,m=crt(r,m,rp,mp)
        low=r+m*unique_integer(((low_k-r)/m).ceil())
        high=r+m*unique_integer(((high_k-r)/m).floor())
        classes+=1
        if low>high:empty+=1;continue
        for k in {low,high}:
            J,logP,point=evaluate(k)
            assert J%g==0
        if classes%2000==0:print('classes',classes,'points',len(cache),'best',best[2]['log_primitive_midpoint'],flush=True)
    assert classes==data['total_crt_classes']
    top=sorted((v[2] for v in cache.values()),key=lambda p:p['log_primitive_midpoint'])[:20]
    out=dict(status='all_integer_parameters_in_fixed_coset_globally_optimized',
        input_sha256={n:hashlib.sha256(v).hexdigest() for n,v in sources.items()},
        selected_powers=data['selected_powers'],x=str(x),coset_start=str(alpha),coset_step=str(L),
        all_parameter_content=str(cs),crt_classes=classes,empty_classes=empty,
        distinct_endpoint_parameters=len(cache),all_candidate_log_primitive_strict_lower_bound=all_floor,
        minimum=best[2],top_endpoints=top,
        proof='For any admissible k, its exact J divides the certified ideal constant. '
              'Its prime-power root balls occur among the CRT classes. Concavity gives '
              'an endpoint k1 of that class with raw determinant at most that of k; '
              'J(k1)>=J(k). Thus some enumerated endpoint has primitive value <=P(k).',
        scope='All integer k in this fixed-x rational y coset and its positive-definite interval; '
              'not all rational parameters and not an asymptotic theorem.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('minimum',best[2],flush=True)
    print('classes',classes,'distinct points',len(cache),'strict lower log bound',all_floor,flush=True)


if __name__=='__main__':main()
