"""Complete physical-height boxes and a predetermined family of positive sections.

Candidate selection uses only rational cone endpoints, not zeta evaluations.
Corner sections are fixed before any output is tested. Exact rounding endpoints
compress their evaluation; floating computations only screen actual witnesses.
"""
import json,sys,math,itertools
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from four_pole_positive_lattice import maps,dot
from four_pole_minimal_lifts import nearest,ceil,floor

sys.set_int_max_str_digits(0)
HEIGHT_EXPONENTS=list(range(8,77,4))
EPSILON_NUMERATOR=8

def qm(x):return fmpq_mat([[Q(str(y)) for y in row] for row in x])
def rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]

def height_polygon(lo,hi,H,epsilon):
    # line dot (a,b) + constant >= 0, all closed; discard the origin.
    cons=[([Q(1),Q(0)],Q(H)),([-Q(1),Q(0)],Q(H)),
          ([Q(0),Q(1)],Q(H)),([Q(0),-Q(1)],Q(H)),
          ([Q(1),lo],Q(0)),([Q(1),hi],Q(0)),
          ([-Q(1),-lo],epsilon),([-Q(1),-hi],epsilon)]
    vertices=set()
    for i,j in itertools.combinations(range(len(cons)),2):
        a,c=cons[i];b,e=cons[j];det=a[0]*b[1]-a[1]*b[0]
        if not det:continue
        v=((-c*b[1]+a[1]*e)/det,(-a[0]*e+c*b[0])/det)
        if all(dot(line,v)+off>=0 for line,off in cons):vertices.add(v)
    assert len(vertices)>=3
    return cons,vertices

def enumerate_box(lo,hi,H,epsilon):
    cons,vertices=height_polygon(lo,hi,H,epsilon)
    scale=ceil(Q(H)/epsilon);mid=(lo+hi)/2
    lattice=fmpz_mat([[scale,0],[nearest(scale*mid),1]])
    _,T=lattice.lll(transform=True);U=T.transpose();assert abs(int(U.det()))==1
    inv=fmpq_mat(U).inv()
    verts=[tuple(inv*fmpq_mat([[x],[y]])) for x,y in vertices]
    widths=[max(v[j] for v in verts)-min(v[j] for v in verts) for j in (0,1)]
    if widths[1]<widths[0]:
        U=U*fmpz_mat([[0,1],[1,0]]);inv=fmpq_mat(U).inv()
        verts=[tuple(inv*fmpq_mat([[x],[y]])) for x,y in vertices]
    transformed=[(list(fmpq_mat([line])*fmpq_mat(U)),off) for line,off in cons]
    left=ceil(min(v[0] for v in verts));right=floor(max(v[0] for v in verts))
    assert right-left<100000,'slice cap would invalidate completeness'
    pts=[];visited=0;raw=0
    for x in range(left,right+1):
        offsets=[off+line[0]*x for line,off in transformed]
        if any(y<0 for y,(line,off) in zip(offsets,transformed) if not line[1]):continue
        lower=max(-y/line[1] for y,(line,off) in zip(offsets,transformed) if line[1]>0)
        upper=min(-y/line[1] for y,(line,off) in zip(offsets,transformed) if line[1]<0)
        bottom,top=ceil(lower),floor(upper)
        assert top-bottom<100000,'point cap would invalidate completeness'
        visited+=1
        for y in range(bottom,top+1):
            a,b=[int(t) for t in U*fmpz_mat([[x],[y]])]
            if a==b==0:continue
            raw+=1
            if math.gcd(a,b)!=1:continue
            assert all(dot(line,[a,b])+off>=0 for line,off in cons)
            pts.append((a,b))
    return sorted(pts),dict(transform=rows(U),slice_interval=[left,right],visited_slices=visited,
                            all_nonzero_points=raw,primitive_points=len(pts))

def period_coordinates(image_inv,pair):
    v=list(image_inv*fmpq_mat([[x] for x in pair]))
    den=math.lcm(*(int(x.denominator) for x in v));g=math.gcd(*(int(x*den) for x in v))
    period=Q(den,g);w=[int(x*period) for x in v];assert math.gcd(*w)==1
    return period,w

def prepare(src,geo,charts):
    n,m,s=[src[k] for k in ('n','m','s')];d=m-2
    C2,a,b,B=maps(n,m,s);Z=fmpz_mat(geo['zero_basis']);A=fmpq_mat(B)*fmpq_mat(Z)
    beta=[sum((abs(A[i,j]) for j in range(d)),Q(0))/2 for i in range(A.nrows())]
    use=[i for i,v in enumerate(beta) if v]
    norm=np.array([[float(A[i,j]/beta[i]) for j in range(d)] for i in use])
    image=qm(charts[1]['image_basis']);inverse=image.inv()
    S={sgn:qm(charts[sgn]['section']) for sgn in (-1,1)}
    FF={sgn:qm(charts[sgn]['phase_matrix']) for sgn in (-1,1)}
    W=fmpz_mat(charts[1]['unimodular_completion'])
    J=fmpz_mat([[W[i,j+1] for j in range(2)] for i in range(m+1)])
    g0=Q(geo['continuous_lower_bound'])
    return C2,a,b,B,Z,A,beta,use,norm,image,inverse,S,FF,J,g0

def lift_candidate(pair,src,prepared):
    C2,a,b,B,Z,A,beta,use,norm,image,inverse,S,FF,J,g0=prepared
    d=Z.ncols();period,w=period_coordinates(inverse,pair);sgn=1 if pair[1]>=0 else -1
    f=list(FF[sgn]*fmpq_mat([[x] for x in w]));z0=list(map(nearest,f))
    particular=list(J*fmpz_mat([[x] for x in w]))
    p0=[int(particular[i])+sum(int(Z[i,j])*z0[j] for j in range(d)) for i in range(Z.nrows())]
    values=[dot(line,p0) for line in B]
    endpoint=Q(src['optimized']['lower' if sgn==1 else 'upper'])
    slack=period*(pair[0]+pair[1]*endpoint);t=slack/(4*g0)
    base_ok=all(x>=0 for x in values)
    entry=dict(pair=list(map(str,pair)),period=str(period),image_coordinates=list(map(str,w)),
               raw_endpoint_slack=str(slack),relative_slack=str(slack/g0),baseline=base_ok)
    if base_ok:
        entry.update(covered=True,section='center',coordinates=list(map(str,z0)),
                     integer_polynomial=list(map(str,p0)),input_bits=max(abs(x).bit_length() for x in p0))
        return entry
    assert slack<g0 # The universal theorem guarantees the center otherwise.
    # t<1/4, so each interval has at most two rounded integer values. Every
    # value combination occurs at one of the PREDETERMINED corner sections.
    choices=[sorted(set([nearest(fj-t),nearest(fj+t)])) for fj in f]
    assert all(len(q)<=2 for q in choices)
    entry['distinct_corner_lifts']=math.prod(map(len,choices))
    entry['varying_coordinates']=sum(len(q)==2 for q in choices)
    normalized=np.array([float(values[i]/beta[i]) for i in use])
    rejected=[]
    for z in itertools.product(*choices):
        delta=[x-y for x,y in zip(z,z0)]
        approximate=normalized+norm@np.array(delta)
        # Negative floating result proposes an exact separating row only.
        index=use[int(np.argmin(approximate))]
        value=values[index]+sum((A[index,j]*delta[j] for j in range(d)),Q(0))
        if value<0:
            rejected.append(dict(coordinates=list(map(str,z)),negative_row=index));continue
        exact=[values[i]+sum((A[i,j]*delta[j] for j in range(d)),Q(0)) for i in range(A.nrows())]
        bad=next((i for i,v in enumerate(exact) if v<0),None)
        if bad is not None:
            rejected.append(dict(coordinates=list(map(str,z)),negative_row=bad));continue
        p=[int(particular[i])+sum(int(Z[i,j])*z[j] for j in range(d)) for i in range(Z.nrows())]
        sigma=[-1 if z[j]==nearest(f[j]-t) else 1 for j in range(d)]
        assert [nearest(f[j]+sigma[j]*t) for j in range(d)]==list(z)
        entry.update(covered=True,section='corner',corner_signs=sigma,coordinates=list(map(str,z)),
                     integer_polynomial=list(map(str,p)),input_bits=max(abs(x).bit_length() for x in p))
        return entry
    assert len(rejected)==entry['distinct_corner_lifts']
    entry.update(covered=False,rejected_corner_lifts=rejected)
    return entry

def case(src,geo,charts):
    n,m,s=[src[k] for k in ('n','m','s')];prepared=prepare(src,geo,charts)
    lo,hi=Q(src['optimized']['lower']),Q(src['optimized']['upper'])
    candidates={};boxes=[]
    for e in HEIGHT_EXPONENTS:
        H=2**e;epsilon=Q(EPSILON_NUMERATOR,H)
        pairs,cert=enumerate_box(lo,hi,H,epsilon)
        boxes.append(dict(height_exponent=e,height=str(H),epsilon=str(epsilon),
                          pairs=[list(map(str,p)) for p in pairs],enumeration=cert))
        for pair in pairs:
            if pair not in candidates:candidates[pair]=lift_candidate(pair,src,prepared)
    data=list(candidates.values())
    for box in boxes:
        vals=[candidates[tuple(map(int,p))] for p in box['pairs']]
        box.update(baseline_count=sum(x['baseline'] for x in vals),covered_count=sum(x['covered'] for x in vals))
    result=dict(n=n,m=m,s=s,dimension=m-2,sections_per_half_cone=1+2**(m-2),
                center_perturbation_rule='z_star + (tau/4)*sigma for sigma in {-1,1}^d',
                boxes=boxes,candidates=data,summary=dict(unique_candidates=len(data),
                    baseline=sum(x['baseline'] for x in data),covered=sum(x['covered'] for x in data),
                    additional=sum(x['covered'] and not x['baseline'] for x in data),
                    failed=sum(not x['covered'] for x in data)))
    print('height coverage',n,m,result['summary'],flush=True)
    return result

def main():
    root=Path(__file__).parent
    def keyed(file):return {(r['n'],r['m'],r['s']):r for r in json.loads((root/file).read_text())['rows']}
    source=keyed('four_pole_positive_lattice.json');geometry=keyed('four_pole_buffer_geometry.json')
    allcharts=json.loads((root/'four_pole_residue_sections.json').read_text())['charts']
    out=dict(status='in_progress',height_exponents=HEIGHT_EXPONENTS,epsilon_numerator=EPSILON_NUMERATOR,rows=[])
    for key,geo in geometry.items():
        charts={r['chart_sign']:r for r in allcharts if tuple(r[k] for k in ('n','m','s'))==key}
        out['rows'].append(case(source[key],geo,charts))
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed'
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__':main()
