"""Independent exact read-back checks for positive sections and residue cells."""
import json,sys,math
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq_mat,fmpq as Q,fmpz_mat
from verify_four_pole_positive_lattice import reconstruct

sys.set_int_max_str_digits(0)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def ceil(x):return -((-x.numerator)//x.denominator)
def nearest(x):return (x+F(1,2)).numerator//(x+F(1,2)).denominator
def qm(rows):return fmpq_mat([[Q(str(x)) for x in row] for row in rows])
def col(M,j):return [F(str(M[i,j])) for i in range(M.nrows())]

def verify(row,source,geometry):
    n,m,s=[row[k] for k in ('n','m','s')];d=m-2
    C2,a,b,B=reconstruct(n,m,s)
    S=qm(row['section']);image=qm(row['image_basis']);Z=fmpz_mat(row['zero_basis'])
    W=fmpz_mat(row['unimodular_completion']);phase=qm(row['phase_matrix'])
    assert abs(int(W.det()))==1
    assert [[int(W[i,j+3]) for j in range(d)] for i in range(m+1)]==row['zero_basis']
    assert [dot(C2,col(S,j)) for j in range(2)]==[0,0]
    assert [[dot(v,col(S,j)) for j in range(2)] for v in (a,b)]==[[1,0],[0,1]]
    for j in range(d):assert all(dot(v,[int(Z[i,j]) for i in range(m+1)])==0 for v in (C2,a,b))
    D=int(source['lattice']['clearing_scale']);H=source['lattice']['image_hnf']
    assert image==qm([[F(H[j][i],D) for j in range(2)] for i in range(2)])
    assert [[dot(v,[int(W[i,j+1]) for i in range(m+1)]) for j in range(2)] for v in (a,b)]==[col(image.transpose(),j) for j in range(2)]
    assert dot(C2,[int(W[i,0]) for i in range(m+1)])!=0
    T=fmpq_mat(W).inv()*S*image
    assert [[T[i,j] for j in range(2)] for i in range(3)]==[[0,0],[1,0],[0,1]]
    assert phase==fmpq_mat([[T[i+3,j] for j in range(2)] for i in range(d)])
    sign=row['chart_sign'];edges=source['edges']
    axis=col(S,0);axisB=[dot(line,axis) for line in B]
    assert min(axisB)>=0
    for edge in edges:
        if sign is not None and edge['sign']!=sign:continue
        p=[F(str(x)) for x in S*qm([[F(edge['constant'])],[edge['sign']]])]
        assert all(dot(line,p)>=0 for line in B)
        if sign is not None:assert p==list(map(F,edge['polynomial']))
    group=row['group'];den=int(group['denominator'])
    assert den==math.lcm(*(int(x.denominator) for x in phase))
    R=fmpz_mat([[den,0],[0,den]]+[[int(den*phase[i,j]) for j in range(2)] for i in range(d)])
    Hn=fmpz_mat(group['row_hnf']);U=fmpz_mat(group['hnf_transform'])
    assert R==fmpz_mat(group['row_generators']) and U*R==Hn and abs(int(U.det()))==1
    assert all(Hn[i,j]==0 for i in range(2,d+2) for j in range(2))
    H2=fmpq_mat([[Hn[i,j] for j in range(2)] for i in range(2)])
    L=fmpz_mat(group['zero_phase_basis']);assert fmpq_mat(L)==den*H2.inv()
    assert all(x.denominator==1 for x in phase*fmpq_mat(L))
    order=abs(int(L.det()));s1=math.gcd(*(int(x) for x in L));s2=order//s1
    assert group['invariants']==list(map(str,(s1,s2))) and s2%s1==0
    assert int(group['order'])==order and group['order_bits']==order.bit_length() and group['exponent_bits']==s2.bit_length()
    qj=[math.lcm(*(int(phase[i,j].denominator) for j in range(2))) for i in range(d)]
    assert list(map(str,qj))==row['coordinate_orders']
    target=row['target'];w=list(map(int,target['image_coordinates']));v=list(map(int,target['pair']));c0=F(target['period'])
    assert math.gcd(*w)==1
    assert list(image*qm([[x] for x in w]))==[Q(str(c0*x)) for x in v]
    fv=[F(str(x)) for x in phase*qm([[x] for x in w])]
    expected_phase=[x-nearest(x) for x in fv]
    assert expected_phase==list(map(F,target['phase']))
    period=math.lcm(*(x.denominator for x in fv))
    assert period==int(target['direction_order']) and s2%period==0
    assert period%s1==0
    A=[[dot(line,[int(Z[i,j]) for i in range(m+1)]) for j in range(d)] for line in B]
    beta=[sum(map(abs,line),F(0))/2 for line in A]
    radii=[F(q//2,q) for q in qj]
    restricted=[sum(abs(x)*r for x,r in zip(line,radii)) for line in A]
    ratios=[x/y for x,y in zip(restricted,beta) if y]
    assert list(map(F,row['componentwise_restricted_radius_ratio']))==[min(ratios),max(ratios)]
    correction=[-dot(line,expected_phase) for line in A]
    assert correction==list(map(F,target['signed_correction']))
    real=[F(str(x)) for x in S*image*qm([[x] for x in w])]
    p=[real[i]-sum(int(Z[i,j])*expected_phase[j] for j in range(d)) for i in range(m+1)]
    assert all(x.denominator==1 for x in p) and p==list(map(F,target['integer_polynomial']))
    vals=[dot(line,p) for line in B]
    assert target['round_section_positive']==all(x>=0 for x in vals)
    assert [dot(vv,p) for vv in (C2,a,b)]==[0]+[c0*x for x in v]
    blocked=[i for i,(x,e) in enumerate(zip(axisB,correction)) if x==0 and e<0]
    grow=None if blocked else max([F(0)]+[-e/x for x,e in zip(axisB,correction) if x>0])
    assert target['same_phase_scalar_buffer']==(str(grow) if grow is not None else None)
    in_chart=sign is None or v[1]*sign>=0;assert target['in_chart']==in_chart
    lo,hi=F(source['optimized']['lower']),F(source['optimized']['upper'])
    slack=c0*(min(v[0]+v[1]*lo,v[0]+v[1]*hi) if sign is None else v[0]+v[1]*(lo if sign==1 else hi))
    assert slack==F(target['endpoint_slack'])
    assert target['scalar_buffer_suffices']==(in_chart and grow is not None and slack>=grow)
    # Independently enumerate the specified small coordinate box.
    count=0
    for x in range(-16,17):
        for y in range(-16,17):
            if x==y==0:continue
            count+=all((x*F(str(phase[j,0]))+y*F(str(phase[j,1]))).denominator==1 for j in range(d))
    assert count==row['zero_phase_nonzero_points_in_coordinate_box_16']
    result=dict(n=n,m=m,s=s,chart_sign=sign,phase_order_bits=group['order_bits'],
                zero_coordinate_radius_gain=(min(ratios)==max(ratios)==1),
                boundary_section_obstructed_rows=blocked,round_section_positive=target['round_section_positive'])
    if sign is not None:
        assert not blocked and all(x>0 for bb,x in zip(beta,axisB) if bb)
        g0=max([F(0)]+[bb/x for bb,x in zip(beta,axisB) if bb])
        assert g0==F(geometry['continuous_lower_bound'])
        assert grow<=g0
        result.update(universal_real_buffer=str(g0),target_phase_buffer=str(grow))
    if 'ray_lift' in row:
        ray=row['ray_lift'];k=int(ray['dilation']);p=list(map(int,ray['integer_polynomial']))
        ph=[k*x-nearest(k*x) for x in fv]
        assert ph==list(map(F,ray['phase'])) and ray['phase_is_zero']==all(x==0 for x in ph)
        assert p==[k*real[i]-sum(int(Z[i,j])*ph[j] for j in range(d)) for i in range(m+1)]
        assert all(dot(line,p)>=0 for line in B) and math.gcd(*p)==1
        assert [dot(vv,p) for vv in (C2,a,b)]==[0]+[k*c0*x for x in v]
        assert k<=int(ray['guaranteed_dilation'])==max(1,ceil(g0/slack))
        assert F(ray['universal_real_buffer'])==g0 and ray['input_bits']==max(abs(x).bit_length() for x in p)
        assert ray['status']==('exact_minimum' if k==1 else 'certified_upper_bound')
        result.update(ray_dilation=k,ray_phase_nonzero=not ray['phase_is_zero'],input_bits=ray['input_bits'])
    print('verified',n,m,s,sign,'blocked rows',len(blocked),flush=True)
    return result

def main():
    root=Path(__file__).parent
    def keyed(name):return {(r['n'],r['m'],r['s']):r for r in json.loads((root/name).read_text())['rows']}
    source=keyed('four_pole_positive_lattice.json');geometry=keyed('four_pole_buffer_geometry.json')
    data=json.loads((root/'four_pole_residue_sections.json').read_text());assert data['status']=='passed'
    out=dict(status='in_progress',rows=[])
    for row in data['rows']+data['charts']:
        key=tuple(row[k] for k in ('n','m','s'))
        out['rows'].append(verify(row,source[key],geometry.get(key)))
    out.update(status='passed',sections=len(out['rows']),ray_lifts=sum('ray_dilation' in r for r in out['rows']))
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('passed',out['sections'],'sections;',out['ray_lifts'],'nonzero-phase positive integer lifts')

if __name__=='__main__':main()
