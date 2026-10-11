"""Exact outer simplices for positive fibers near the output-cone boundary.

Strictly positive edge duals of full zero-lattice rank certify unique boundary
lifts. They also give bounded simplices containing EVERY positive lift, not
only the section library explored in four_pole_height_cover.py.
"""
import json,sys,math,itertools
from pathlib import Path
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from four_pole_positive_lattice import maps,dot
from four_pole_minimal_lifts import floor,ceil,nearest

sys.set_int_max_str_digits(0)
def qm(rows):return fmpq_mat([[Q(str(x)) for x in row] for row in rows])
def serialize(rows):return [list(map(str,v)) for v in rows]

def make_simplex(src,geo,chart):
    n,m,s=[src[k] for k in ('n','m','s')];d=m-2;sign=chart['chart_sign']
    C2,a,b,B=maps(n,m,s);Z=fmpz_mat(geo['zero_basis']);A=fmpq_mat(B)*fmpq_mat(Z)
    axis=[Q(line[0]) for line in chart['section']];c=[dot(line,axis) for line in B]
    edge=next(e for e in src['edges'] if e['sign']==sign);ep=list(map(Q,edge['polynomial']))
    I=[i for i,v in zip(edge['active'],edge['dual']) if Q(v)>0]
    lambdas=[Q(v) for v in edge['dual'] if Q(v)>0]
    AA=[[A[i,j] for j in range(d)] for i in I]
    assert len(I)==d+1 and fmpq_mat(AA).rank()==d
    assert all(sum((lam*A[i,j] for i,lam in zip(I,lambdas)),Q(0))==0 for j in range(d))
    assert sum((lam*c[i] for i,lam in zip(I,lambdas)),Q(0))==1
    assert all(dot(B[i],ep)==0 for i in I)
    vertices=[]
    for omit in range(d+1):
        keep=[j for j in range(d+1) if j!=omit]
        v=list(fmpq_mat([AA[j] for j in keep]).inv()*fmpq_mat([[-c[I[j]]] for j in keep]))
        assert all(c[i]+sum((A[i,j]*v[j] for j in range(d)),Q(0))>=0 for i in I)
        vertices.append(v)
    edgeB=[dot(line,ep) for line in B]
    mins=[min(c[i]+sum((A[i,j]*v[j] for j in range(d)),Q(0)) for v in vertices) for i in range(len(B))]
    zero_ok=all(mn>=0 for eb,mn in zip(edgeB,mins) if eb==0)
    threshold=max([Q(0)]+[-mn/eb for eb,mn in zip(edgeB,mins) if eb>0]) if zero_ok else None
    certificate=dict(sign=sign,active=I,positive_dual=list(map(str,lambdas)),vertices=serialize(vertices),
                     all_zero_rows_redundant=zero_ok,exact_simplex_ratio_threshold=str(threshold) if threshold is not None else None)
    centroid=[sum((v[j] for v in vertices),Q(0))/(d+1) for j in range(d)]
    slacks=[c[i]+sum((A[i,j]*centroid[j] for j in range(d)),Q(0)) for i in I]
    assert min(slacks)>0
    embedding=fmpz_mat([[nearest(2**64*A[i,j]/slack) for i,slack in zip(I,slacks)]
                       +[int(j==k) for k in range(d)] for j in range(d)])
    _,change=embedding.lll(transform=True);change=change.transpose();assert abs(int(change.det()))==1
    inverse=fmpq_mat(change).inv()
    reduced_vertices=[list(inverse*fmpq_mat([[x] for x in v])) for v in vertices]
    certificate.update(basis_transform=[[int(change[i,j]) for j in range(d)] for i in range(d)],
                       reduced_vertices=serialize(reduced_vertices))
    return certificate,reduced_vertices,A*fmpq_mat(change),c,B,Z*change,inverse

def classify(candidate,src,chart,prepared):
    cert,vertices,A,c,B,Z,inverse=prepared;d=Z.ncols();pair=list(map(int,candidate['pair']))
    w=list(map(int,candidate['image_coordinates']));r=Q(candidate['raw_endpoint_slack']);assert r>0
    phase=inverse*qm(chart['phase_matrix']);f=list(phase*fmpq_mat([[x] for x in w]))
    W=fmpz_mat(chart['unimodular_completion'])
    base=[int(W[i,1])*w[0]+int(W[i,2])*w[1] for i in range(Z.nrows())]
    lower=[min(v[j] for v in vertices) for j in range(d)];upper=[max(v[j] for v in vertices) for j in range(d)]
    ranges=[[ceil(f[j]+r*lower[j]),floor(f[j]+r*upper[j])] for j in range(d)]
    result=dict(pair=candidate['pair'],integer_coordinate_ranges=[[str(x),str(y)] for x,y in ranges])
    centroid=[sum((v[j] for v in vertices),Q(0))/(d+1) for j in range(d)]
    z=[nearest(f[j]+r*centroid[j]) for j in range(d)]
    p=[base[i]+sum(int(Z[i,j])*z[j] for j in range(d)) for i in range(Z.nrows())]
    if all(dot(line,p)>=0 for line in B):
        result.update(status='positive_integer_lift_at_k1',method='boundary_centroid',coordinates=list(map(str,z)),
                      integer_polynomial=list(map(str,p)),input_bits=max(abs(x).bit_length() for x in p));return result
    # A valid certificate can use any primitive integer projection.
    directions=[]
    for j in range(d):directions.append([int(k==j) for k in range(d)])
    for i,j in itertools.combinations(range(d),2):
        for sgn in (-1,1):directions.append([int(k==i)+sgn*int(k==j) for k in range(d)])
    for u in directions:
        lo=dot(u,f)+r*min(dot(u,v) for v in vertices)
        hi=dot(u,f)+r*max(dot(u,v) for v in vertices)
        if ceil(lo)>floor(hi):
            result.update(status='no_positive_integer_lift_at_k1',method='empty_integer_projection',
                          direction=u,projection_interval=[str(lo),str(hi)])
            return result
    count=math.prod(max(0,hi-lo+1) for lo,hi in ranges)
    result['bounding_box_integer_points']=str(count)
    if count>65536:
        result.update(status='unresolved',method='enumeration_cap');return result
    rejected=[]
    for z in itertools.product(*(range(lo,hi+1) for lo,hi in ranges)):
        p=[base[i]+sum(int(Z[i,j])*z[j] for j in range(d)) for i in range(Z.nrows())]
        bad=next((i for i,line in enumerate(B) if dot(line,p)<0),None)
        if bad is not None:
            rejected.append(dict(coordinates=list(map(str,z)),negative_row=bad));continue
        result.update(status='positive_integer_lift_at_k1',method='complete_outer_box',coordinates=list(map(str,z)),
                      integer_polynomial=list(map(str,p)),input_bits=max(abs(x).bit_length() for x in p))
        return result
    result.update(status='no_positive_integer_lift_at_k1',method='complete_outer_box',rejected_points=rejected)
    assert len(rejected)==count
    return result

def main():
    root=Path(__file__).parent
    def keyed(file):return {(r['n'],r['m'],r['s']):r for r in json.loads((root/file).read_text())['rows']}
    srcs=keyed('four_pole_positive_lattice.json');geos=keyed('four_pole_buffer_geometry.json')
    coverage=keyed('four_pole_height_cover.json');allcharts=json.loads((root/'four_pole_residue_sections.json').read_text())['charts']
    out=dict(status='in_progress',rows=[])
    for key,geo in geos.items():
        charts={r['chart_sign']:r for r in allcharts if tuple(r[k] for k in ('n','m','s'))==key}
        simplexes={sgn:make_simplex(srcs[key],geo,charts[sgn]) for sgn in (-1,1)}
        cases=[]
        for candidate in coverage[key]['candidates']:
            if candidate['covered']:continue
            sgn=1 if int(candidate['pair'][1])>=0 else -1
            cases.append(classify(candidate,srcs[key],charts[sgn],simplexes[sgn]))
        summary={s:sum(c['status']==s for c in cases) for s in ('positive_integer_lift_at_k1','no_positive_integer_lift_at_k1','unresolved')}
        row=dict(n=key[0],m=key[1],s=key[2],boundary_simplexes=[v[0] for v in simplexes.values()],cases=cases,summary=summary)
        out['rows'].append(row);print('intrinsic classification',key,summary,
            'exact tangent',[v[0]['all_zero_rows_redundant'] for v in simplexes.values()],flush=True)
    out['status']='passed'
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__':main()
