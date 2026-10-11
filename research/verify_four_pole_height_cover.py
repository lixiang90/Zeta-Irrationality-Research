"""Independent certificates: complete height enumeration, covers, and fiber holes."""
import json,sys,math,itertools
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from verify_four_pole_positive_lattice import reconstruct

sys.set_int_max_str_digits(0)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def ceil(x):return -((-x.numerator)//x.denominator)
def floor(x):return x.numerator//x.denominator
def nearest(x):return floor(x+F(1,2))
def qm(a):return fmpq_mat([[Q(str(x)) for x in line] for line in a])
def asf(x):return F(str(x))

def enumerate_independent(lo,hi,H,eps,U):
    cons=[([F(1),F(0)],F(H)),([-F(1),F(0)],F(H)),([F(0),F(1)],F(H)),([F(0),-F(1)],F(H)),
          ([F(1),lo],F(0)),([F(1),hi],F(0)),([-F(1),-lo],eps),([-F(1),-hi],eps)]
    vertices=set()
    for (a,c),(b,e) in itertools.combinations(cons,2):
        det=a[0]*b[1]-a[1]*b[0]
        if det==0:continue
        v=((-c*b[1]+a[1]*e)/det,(c*b[0]-a[0]*e)/det)
        if all(dot(line,v)+off>=0 for line,off in cons):vertices.add(v)
    assert len(vertices)>=3
    det=U[0][0]*U[1][1]-U[0][1]*U[1][0];assert abs(det)==1
    inv=[[F(U[1][1],det),F(-U[0][1],det)],[F(-U[1][0],det),F(U[0][0],det)]]
    vtx=[[dot(line,v) for line in inv] for v in vertices]
    lower=ceil(min(v[0] for v in vtx));upper=floor(max(v[0] for v in vtx))
    lines=[([sum(line[k]*U[k][j] for k in range(2)) for j in range(2)],off) for line,off in cons]
    found=[];allcount=0;visited=0
    for x in range(lower,upper+1):
        offsets=[off+line[0]*x for line,off in lines]
        if any(y<0 for (line,off),y in zip(lines,offsets) if line[1]==0):continue
        left=max(-y/line[1] for (line,off),y in zip(lines,offsets) if line[1]>0)
        right=min(-y/line[1] for (line,off),y in zip(lines,offsets) if line[1]<0);visited+=1
        for y in range(ceil(left),floor(right)+1):
            a,b=[line[0]*x+line[1]*y for line in U]
            if a==b==0:continue
            allcount+=1
            if math.gcd(a,b)==1:found.append((a,b))
    return sorted(found),[lower,upper],allcount,visited

def context(src,geo,charts):
    n,m,s=[src[k] for k in ('n','m','s')]
    C2,a,b,B=reconstruct(n,m,s);Z=fmpz_mat(geo['zero_basis']);Bq=qm(B)
    W=fmpz_mat(charts[1]['unimodular_completion']);J=fmpz_mat([[W[i,j+1] for j in range(2)] for i in range(m+1)])
    image=qm(charts[1]['image_basis']);A=Bq*fmpq_mat(Z)
    return C2,a,b,B,Bq,Z,J,image,A

def check_coverage(row,src,geo,charts):
    C2,a,b,B,Bq,Z,J,image,A=context(src,geo,charts);d=Z.ncols()
    lo,hi=F(src['optimized']['lower']),F(src['optimized']['upper']);g0=F(geo['continuous_lower_bound'])
    candidates={tuple(map(int,c['pair'])):c for c in row['candidates']};allpairs=set()
    assert row['sections_per_half_cone']==1+2**d
    for box in row['boxes']:
        H=int(box['height']);eps=F(box['epsilon']);assert H==2**box['height_exponent'] and eps==F(8,H)
        cert=box['enumeration'];found,interval,raw,visited=enumerate_independent(lo,hi,H,eps,cert['transform'])
        assert found==list(map(lambda p:tuple(map(int,p)),box['pairs']))
        assert cert['slice_interval']==interval and cert['all_nonzero_points']==raw
        assert cert['visited_slices']==visited and cert['primitive_points']==len(found)
        allpairs.update(found)
        assert box['baseline_count']==sum(candidates[p]['baseline'] for p in found)
        assert box['covered_count']==sum(candidates[p]['covered'] for p in found)
    assert allpairs==set(candidates)
    frozen=0
    for pair,candidate in candidates.items():
        assert math.gcd(*pair)==1
        sgn=1 if pair[1]>=0 else -1;chart=charts[sgn]
        v=list(image.inv()*qm([[x] for x in pair]));den=math.lcm(*(int(x.denominator) for x in v));g=math.gcd(*(int(x*den) for x in v))
        period=F(den,g);w=[int(x*Q(str(period))) for x in v]
        assert str(period)==candidate['period'] and list(map(str,w))==candidate['image_coordinates']
        f=[asf(x) for x in qm(chart['phase_matrix'])*qm([[x] for x in w])]
        z0=list(map(nearest,f));base=[int(x) for x in J*fmpz_mat([[x] for x in w])]
        def polynomial(z):return [base[i]+sum(int(Z[i,j])*z[j] for j in range(d)) for i in range(Z.nrows())]
        p0=polynomial(z0);baseline=all(dot(line,p0)>=0 for line in B)
        assert baseline==candidate['baseline']
        r=period*(pair[0]+pair[1]*(lo if sgn==1 else hi));t=r/(4*g0)
        assert r==F(candidate['raw_endpoint_slack']) and r/g0==F(candidate['relative_slack'])
        choices=[sorted(set((nearest(fj-t),nearest(fj+t)))) for fj in f]
        if not baseline:
            assert r<g0 and all(len(q)<=2 for q in choices)
            assert candidate['distinct_corner_lifts']==math.prod(map(len,choices))
            assert candidate['varying_coordinates']==sum(len(q)==2 for q in choices)
            frozen+=candidate['varying_coordinates']==0
        if candidate['covered']:
            z=list(map(int,candidate['coordinates']));p=list(map(int,candidate['integer_polynomial']))
            assert p==polynomial(z) and all(dot(line,p)>=0 for line in B)
            assert [dot(vv,p) for vv in (C2,a,b)]==[0,period*pair[0],period*pair[1]]
            assert math.gcd(*p)==1 and max(abs(x).bit_length() for x in p)==candidate['input_bits']
            if baseline:assert candidate['section']=='center' and z==z0
            else:
                sigma=candidate['corner_signs'];assert all(x in (-1,1) for x in sigma)
                assert z==[nearest(f[j]+t*sigma[j]) for j in range(d)]
        else:
            rejected=candidate['rejected_corner_lifts'];seen=set()
            for witness in rejected:
                z=tuple(map(int,witness['coordinates']));assert z not in seen;seen.add(z)
                assert dot(B[witness['negative_row']],polynomial(z))<0
            assert seen==set(itertools.product(*choices))
    summary=dict(unique_candidates=len(candidates),baseline=sum(c['baseline'] for c in candidates.values()),
                 covered=sum(c['covered'] for c in candidates.values()),additional=sum(c['covered'] and not c['baseline'] for c in candidates.values()),
                 failed=sum(not c['covered'] for c in candidates.values()))
    assert summary==row['summary'];summary['frozen_failures']=frozen
    return summary

def check_boundary(row,cover,src,geo,charts):
    C2,a,b,B,Bq,Z,J,image,A=context(src,geo,charts);d=Z.ncols();prepared={};thresholds={}
    for simplex in row['boundary_simplexes']:
        sgn=simplex['sign'];chart=charts[sgn];I=simplex['active'];lam=list(map(Q,simplex['positive_dual']))
        axis=[Q(line[0]) for line in chart['section']];c=list(Bq*qm([[x] for x in axis]))
        ep=list(map(Q,next(e for e in src['edges'] if e['sign']==sgn)['polynomial']))
        assert len(I)==d+1 and min(lam)>0
        AA=fmpq_mat([[A[i,j] for j in range(d)] for i in I]);assert AA.rank()==d
        assert all(sum(lam[k]*A[i,j] for k,i in enumerate(I))==0 for j in range(d))
        assert sum(lam[k]*c[i] for k,i in enumerate(I))==1
        assert all(sum(Q(str(B[i][j]))*ep[j] for j in range(len(ep)))==0 for i in I)
        vertices=[list(map(Q,v)) for v in simplex['vertices']];assert len(vertices)==d+1
        for omit,v in enumerate(vertices):
            vals=[c[i]+sum(A[i,j]*v[j] for j in range(d)) for i in I]
            assert min(vals)>=0 and all(vals[k]==0 for k in range(d+1) if k!=omit)
        edgeB=list(Bq*qm([[x] for x in ep]));mins=[min(c[i]+sum(A[i,j]*v[j] for j in range(d)) for v in vertices) for i in range(len(B))]
        zero_ok=all(mn>=0 for eb,mn in zip(edgeB,mins) if eb==0);assert zero_ok==simplex['all_zero_rows_redundant']
        threshold=max([Q(0)]+[-mn/eb for eb,mn in zip(edgeB,mins) if eb>0]) if zero_ok else None
        assert simplex['exact_simplex_ratio_threshold']==(str(threshold) if threshold is not None else None)
        thresholds[sgn]=threshold
        T=fmpz_mat(simplex['basis_transform']);assert abs(int(T.det()))==1
        inv=fmpq_mat(T).inv();newvertices=[list(inv*qm([[x] for x in v])) for v in vertices]
        assert [[str(x) for x in v] for v in newvertices]==simplex['reduced_vertices']
        prepared[sgn]=(Z*T,inv*qm(chart['phase_matrix']),newvertices)
    candidates={tuple(map(int,c['pair'])):c for c in cover['candidates']}
    failed={p for p,c in candidates.items() if not c['covered']};assert failed=={tuple(map(int,c['pair'])) for c in row['cases']}
    summary={s:0 for s in ('positive_integer_lift_at_k1','no_positive_integer_lift_at_k1','unresolved')}
    for case in row['cases']:
        pair=tuple(map(int,case['pair']));candidate=candidates[pair];sgn=1 if pair[1]>=0 else -1
        ZZ,FF,vertices=prepared[sgn];w=list(map(int,candidate['image_coordinates']));r=Q(candidate['raw_endpoint_slack'])
        f=list(FF*qm([[x] for x in w]));base=[int(x) for x in J*fmpz_mat([[x] for x in w])]
        def polynomial(z):return [base[i]+sum(int(ZZ[i,j])*z[j] for j in range(d)) for i in range(ZZ.nrows())]
        ranges=[[ceil(asf(f[j]+r*min(v[j] for v in vertices))),floor(asf(f[j]+r*max(v[j] for v in vertices)))] for j in range(d)]
        assert ranges==[[int(x),int(y)] for x,y in case['integer_coordinate_ranges']]
        summary[case['status']]+=1
        if case['status']=='positive_integer_lift_at_k1':
            z=list(map(int,case['coordinates']));p=list(map(int,case['integer_polynomial']));assert p==polynomial(z)
            assert min(dot(line,p) for line in B)>=0 and math.gcd(*p)==1
            period=F(candidate['period']);assert [dot(vv,p) for vv in (C2,a,b)]==[0,period*pair[0],period*pair[1]]
            if case['method']=='boundary_centroid':
                center=[sum(v[j] for v in vertices)/(d+1) for j in range(d)]
                assert z==[nearest(asf(f[j]+r*center[j])) for j in range(d)]
        elif case['method']=='empty_integer_projection':
            u=case['direction'];assert math.gcd(*u)==1
            lo=sum(u[j]*f[j] for j in range(d))+r*min(sum(u[j]*v[j] for j in range(d)) for v in vertices)
            hi=sum(u[j]*f[j] for j in range(d))+r*max(sum(u[j]*v[j] for j in range(d)) for v in vertices)
            assert case['projection_interval']==[str(lo),str(hi)] and ceil(asf(lo))>floor(asf(hi))
        else:
            count=math.prod(max(0,y-x+1) for x,y in ranges);assert str(count)==case['bounding_box_integer_points']
            if case['status']=='unresolved':assert count>65536;continue
            seen=set()
            for witness in case['rejected_points']:
                z=tuple(map(int,witness['coordinates']));assert z not in seen;seen.add(z)
                assert dot(B[witness['negative_row']],polynomial(z))<0
            assert seen==set(itertools.product(*(range(x,y+1) for x,y in ranges)))
    assert summary==row['summary']
    exact_count=0
    for candidate in cover['candidates']:
        sgn=1 if int(candidate['pair'][1])>=0 else -1
        ratio=Q(abs(int(candidate['pair'][1])))*Q(candidate['period'])/Q(candidate['raw_endpoint_slack'])
        exact_count+=thresholds[sgn] is not None and ratio>=thresholds[sgn]
    return dict(**summary,exact_simplex_candidates=exact_count)

def check_facet_residues(row,cover,src,geo,charts):
    C2,a,b,B,Bq,Z,J,image,A=context(src,geo,charts);d=Z.ncols();models={}
    def rational_gcd(values):
        den=math.lcm(*(int(x.denominator) for x in values));g=math.gcd(*(int(x*den) for x in values))
        return Q(g,den)
    for model in row['models']:
        I=model['active'];lam=list(map(Q,model['positive_dual']))
        rho=[rational_gcd([A[i,j] for j in range(d)]) for i in I]
        assert list(map(str,rho))==model['row_steps']
        weights=[x*y for x,y in zip(lam,rho)];kappa=rational_gcd(weights)
        assert str(kappa)==model['weight_unit']
        coins=[int(x/kappa) for x in weights];assert list(map(str,coins))==model['primitive_positive_weights']
        assert min(coins)>0 and math.gcd(*coins)==1
        D=fmpz_mat(model['facet_lattice'])
        assert all(A[i,j]==rho[k]*int(D[k,j]) for k,i in enumerate(I) for j in range(d))
        assert all(sum(coins[i]*int(D[i,j]) for i in range(d+1))==0 for j in range(d))
        minors=[int(fmpz_mat([[D[i,j] for j in range(d)] for i in range(d+1) if i!=omit]).det()) for omit in range(d+1)]
        assert list(map(str,minors))==model['maximal_minors']
        index=math.gcd(*minors);assert str(index)==model['saturation_index'] and index.bit_length()==model['index_bits']
        models[model['sign']]=(I,lam,rho,kappa,coins)
    candidates={tuple(c['pair']):c for c in cover['candidates']};assert set(candidates)=={tuple(c['pair']) for c in row['cases']}
    excluded=0
    for case in row['cases']:
        candidate=candidates[tuple(case['pair'])];sgn=1 if int(case['pair'][1])>=0 else -1
        I,lam,rho,kappa,coins=models[sgn];w=list(map(int,candidate['image_coordinates']));p=list(J*fmpz_mat([[x] for x in w]))
        vals=[sum(Q(str(B[i][j]))*p[j] for j in range(len(p))) for i in I]
        n0=[floor(asf(x/rr)) for x,rr in zip(vals,rho)];delta=[x-rr*j for x,rr,j in zip(vals,rho,n0)]
        assert all(0<=x<rr for x,rr in zip(delta,rho))
        budget=sum(x*y for x,y in zip(lam,delta));r=Q(candidate['raw_endpoint_slack'])
        assert sum(x*y for x,y in zip(lam,vals))==r
        M=(r-budget)/kappa;assert M.denominator==1 and M==sum(c*j for c,j in zip(coins,n0))
        assert str(budget)==case['residue_budget'] and str(r)==case['slack'] and str(M)==case['integer_budget']
        assert case['status']==('excluded_by_negative_residue_budget' if M<0 else 'necessary_budget_passes')
        excluded+=M<0
    assert excluded==row['summary']['excluded']
    return dict(facet_models=len(models),residue_budgets=len(row['cases']),negative_budgets=excluded)

def main():
    root=Path(__file__).parent
    def keyed(name):return {(r['n'],r['m'],r['s']):r for r in json.loads((root/name).read_text())['rows']}
    srcs=keyed('four_pole_positive_lattice.json');geos=keyed('four_pole_buffer_geometry.json')
    coverdata=json.loads((root/'four_pole_height_cover.json').read_text());assert coverdata['status']=='passed'
    assert coverdata['height_exponents']==list(range(8,77,4)) and coverdata['epsilon_numerator']==8
    cover=keyed('four_pole_height_cover.json');boundary=keyed('four_pole_boundary_fibers.json');facet=keyed('four_pole_facet_residues.json')
    allcharts=json.loads((root/'four_pole_residue_sections.json').read_text())['charts'];out=dict(status='in_progress',rows=[])
    for key,geo in geos.items():
        charts={c['chart_sign']:c for c in allcharts if tuple(c[k] for k in ('n','m','s'))==key}
        counts=check_coverage(cover[key],srcs[key],geo,charts)
        fiber=check_boundary(boundary[key],cover[key],srcs[key],geo,charts)
        residue=check_facet_residues(facet[key],cover[key],srcs[key],geo,charts)
        out['rows'].append(dict(n=key[0],m=key[1],s=key[2],coverage=counts,boundary=fiber,facet_residues=residue))
        print('verified',key,counts,fiber,flush=True)
    out.update(status='passed',complete_height_boxes=sum(len(r['boxes']) for r in cover.values()),
               unique_parameter_direction_pairs=sum(r['coverage']['unique_candidates'] for r in out['rows']),boundary_simplexes=10)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('all complete enumeration and fiber certificates passed')

if __name__=='__main__':main()
