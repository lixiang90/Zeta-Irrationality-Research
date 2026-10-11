"""Positive rational sections, finite residue groups, and signed rounding cells.

All section/group/cell calculations are exact. A fixed section is only a
sufficient integer-lifting mechanism, not a characterization of all lifts.
"""
import json,sys,math
import numpy as np
from pathlib import Path
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from four_pole_positive_lattice import maps,dot
from four_pole_minimal_lifts import nearest,ceil

sys.set_int_max_str_digits(0)
def matrix_rows(M):
    return [[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def integer_rows(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]
def column(M,j):return [M[i,j] for i in range(M.nrows())]
def group(F):
    d=F.nrows();den=math.lcm(*(int(x.denominator) for x in F))
    R=fmpz_mat([[den,0],[0,den]]+[[int(den*F[i,j]) for j in range(2)] for i in range(d)])
    H,T=R.hnf(transform=True)
    H2=fmpq_mat([[H[i,j] for j in range(2)] for i in range(2)])
    L=den*H2.inv();assert all(x.denominator==1 for x in L)
    L=fmpz_mat([[int(L[i,j]) for j in range(2)] for i in range(2)])
    assert all(x.denominator==1 for x in F*fmpq_mat(L))
    order=abs(int(L.det()));s1=math.gcd(*(int(x) for x in L));s2=order//s1
    assert s2%s1==0
    return dict(denominator=str(den),row_generators=integer_rows(R),row_hnf=integer_rows(H),
                hnf_transform=integer_rows(T),zero_phase_basis=integer_rows(L),
                invariants=[str(s1),str(s2)],order=str(order),order_bits=order.bit_length(),
                exponent_bits=s2.bit_length())

def ray_search(real,A,fv,Z,slopes,axis,slack):
    beta=[sum((abs(A[i,j]) for j in range(A.ncols())),Q(0))/2 for i in range(A.nrows())]
    g0=max([Q(0)]+[bb/v for bb,v in zip(beta,axis) if bb])
    assert all(v>0 for bb,v in zip(beta,axis) if bb)
    upper=max(1,ceil(g0/slack))
    use=[i for i,bb in enumerate(beta) if bb]
    normalized=np.array([[float(A[i,j]/beta[i]) for j in range(A.ncols())] for i in use])
    y=np.array([float(slopes[i]/beta[i]) for i in use])
    candidates=set(range(1,min(1000,upper)+1))
    candidates.update(max(1,upper*j//128) for j in range(1,129))
    for k in sorted(candidates):
        error=[nearest(k*x)-k*x for x in fv]
        # Floating arithmetic screens candidates only; acceptance is exact.
        if np.min(k*y+normalized@np.array(list(map(float,error)))) < -1e-9:continue
        vals=[k*slopes[i]+sum((A[i,j]*error[j] for j in range(A.ncols())),Q(0)) for i in range(A.nrows())]
        if min(vals)<0:continue
        p=[k*real[i]+sum((Q(Z[i,j])*error[j] for j in range(A.ncols())),Q(0)) for i in range(Z.nrows())]
        assert all(x.denominator==1 for x in p)
        return dict(dilation=str(k),integer_polynomial=list(map(str,p)),
                    phase=list(map(str,[-x for x in error])),phase_is_zero=all(x==0 for x in error),
                    universal_real_buffer=str(g0),guaranteed_dilation=str(upper),
                    status='exact_minimum' if k==1 else 'certified_upper_bound',
                    input_bits=max(abs(int(x)).bit_length() for x in p))
    raise AssertionError('guaranteed lift was not found')

def probe(row,lift,period,geometry=None,chart_sign=None):
    n,m,s=[row[k] for k in ('n','m','s')];d=m-2
    C2,a,b,B=maps(n,m,s)
    K=fmpz_mat(row['lattice']['saturated_kernel']);V=fmpz_mat(row['lattice']['image_unimodular'])
    E=K*V.transpose();U=fmpz_mat(row['lattice']['kernel_unimodular'])
    Z=fmpz_mat((geometry or lift)['zero_basis'])
    W=fmpz_mat([[U[0,i],E[i,0],E[i,1]]+[Z[i,j] for j in range(d)] for i in range(m+1)])
    assert abs(int(W.det()))==1
    D=int(row['lattice']['clearing_scale']);H=row['lattice']['image_hnf']
    image=fmpq_mat([[Q(H[j][i],D) for j in range(2)] for i in range(2)])
    edges=row['edges'];P=fmpq_mat([[Q(edges[j]['polynomial'][i]) for j in range(2)] for i in range(m+1)])
    O=fmpq_mat([[Q(e['constant']) for e in edges],[Q(e['sign']) for e in edges]])
    section=P*O.inv();S=section*image
    if chart_sign is not None:
        assert geometry is not None and chart_sign in (-1,1)
        z=list(map(Q,geometry['rounding_certificate']['coordinates']))
        p0=list(map(Q,geometry['particular']));h=Q(geometry['axis_period'])
        axis_p=[(p0[i]+sum((Q(Z[i,j])*z[j] for j in range(d)),Q(0)))/h for i in range(m+1)]
        edge=next(e for e in edges if e['sign']==chart_sign)
        ep=list(map(Q,edge['polynomial']));ea=Q(edge['constant'])
        section=fmpq_mat([[axis_p[i],(ep[i]-ea*axis_p[i])/chart_sign] for i in range(m+1)])
        S=section*image
    coords=fmpq_mat(W).inv()*S
    assert [[coords[i,j] for j in range(2)] for i in range(3)]==[[0,0],[1,0],[0,1]]
    F=fmpq_mat([[coords[i+3,j] for j in range(2)] for i in range(d)])
    G=group(F)
    A=fmpq_mat(B)*fmpq_mat(Z);BS=fmpq_mat(B)*S
    axis=list(fmpq_mat(B)*section*fmpq_mat([[1],[0]]))
    assert all(x>=0 for x in axis)
    w=list(map(int,period['image_primitive_coordinates']));fv=list(F*fmpq_mat([[x] for x in w]))
    phase=[x-nearest(x) for x in fv];error=[-x for x in phase]
    signed=list(A*fmpq_mat([[x] for x in error]));real=list(S*fmpq_mat([[x] for x in w]))
    p=[real[i]+sum((Q(Z[i,j])*error[j] for j in range(d)),Q(0)) for i in range(m+1)]
    assert all(x.denominator==1 for x in p)
    values=[dot(line,p) for line in B];positive=all(x>=0 for x in values)
    direction_order=math.lcm(*(int(x.denominator) for x in fv))
    assert int(G['invariants'][1])%direction_order==0
    if chart_sign is None:assert direction_order==int(period['constructed_dilation'])
    beta=[sum((abs(A[i,j]) for j in range(d)),Q(0))/2 for i in range(A.nrows())]
    coordinate_orders=[math.lcm(*(int(F[j,k].denominator) for k in range(2))) for j in range(d)]
    radii=[Q(q//2,q) for q in coordinate_orders]
    restricted=[sum((abs(A[i,j])*radii[j] for j in range(d)),Q(0)) for i in range(A.nrows())]
    ratios=[v/bb for v,bb in zip(restricted,beta) if bb]
    finite=all(axis[i]>0 or signed[i]>=0 for i in range(len(axis)))
    grow=max([Q(0)]+[-signed[i]/axis[i] for i in range(len(axis)) if axis[i]>0]) if finite else None
    v=list(map(int,row['optimized']['pair']));c0=Q(period['minimum_arithmetic_output_multiplier'])
    output=[dot(a,p),dot(b,p)];assert output==[c0*x for x in v] and dot(C2,p)==0
    lo,hi=Q(row['optimized']['lower']),Q(row['optimized']['upper'])
    slack=c0*min(v[0]+v[1]*lo,v[0]+v[1]*hi)
    in_chart=chart_sign is None or v[1]*chart_sign>=0
    if chart_sign is not None:
        endpoint=lo if chart_sign==1 else hi
        slack=c0*(v[0]+v[1]*endpoint)
    # A height cap in the SAME output-lattice coordinates, not physical coefficient height.
    L=fmpz_mat(G['zero_phase_basis']);small=0;nonzero=0
    inv=fmpq_mat(L).inv()
    for x in range(-16,17):
        for y in range(-16,17):
            if x==y==0:continue
            nonzero+=1
            small+=all(t.denominator==1 for t in inv*fmpq_mat([[x],[y]]))
    result=dict(n=n,m=m,s=s,chart_sign=chart_sign,section=matrix_rows(section),image_basis=matrix_rows(image),
                zero_basis=integer_rows(Z),unimodular_completion=integer_rows(W),
                phase_matrix=matrix_rows(F),group=G,coordinate_orders=list(map(str,coordinate_orders)),
                componentwise_restricted_radius_ratio=[str(min(ratios)),str(max(ratios))],
                zero_phase_nonzero_points_in_coordinate_box_16=small,tested_coordinate_box_points=nonzero,
                target=dict(pair=list(map(str,v)),period=str(c0),image_coordinates=list(map(str,w)),
                            phase=list(map(str,phase)),signed_correction=list(map(str,signed)),
                            integer_polynomial=list(map(str,p)),round_section_positive=positive,
                            in_chart=in_chart,
                            direction_order=str(direction_order),direction_order_bits=direction_order.bit_length(),
                            same_phase_scalar_buffer=str(grow) if grow is not None else None,
                            endpoint_slack=str(slack),
                            scalar_buffer_suffices=(in_chart and grow is not None and slack>=grow),
                            known_minimum_status=lift['status'] if 'status' in lift else None,
                            known_dilation=lift.get('dilation'),
                            input_bits=max(abs(int(x)).bit_length() for x in p)))
    if chart_sign is not None and in_chart:
        result['ray_lift']=ray_search(real,A,fv,Z,list(BS*fmpq_mat([[x] for x in w])),axis,slack)
    print(n,m,s,chart_sign,'group bits',G['order_bits'],'direction bits',direction_order.bit_length(),
          'rounded positive',positive,'zero box',small,flush=True)
    if 'ray_lift' in result:print('ray',result['ray_lift']['dilation'],'guarantee',result['ray_lift']['guaranteed_dilation'],flush=True)
    return result

def main():
    root=Path(__file__).parent
    def keyed(file,field='rows'):
        return {(r['n'],r['m'],r['s']):r for r in json.loads((root/file).read_text())[field]}
    source=keyed('four_pole_positive_lattice.json');lifts=keyed('four_pole_minimal_lifts.json')
    periods=keyed('four_pole_lift_periods.json');geometry=keyed('four_pole_buffer_geometry.json')
    keys=[(2,3,7),(4,3,7)]+list(geometry)+[(16,8,5),(16,8,9)]
    result=dict(status='in_progress',rows=[],charts=[])
    for key in keys:
        result['rows'].append(probe(source[key],lifts[key],periods[key],geometry.get(key)))
        Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    for key in geometry:
        for sign in (1,-1):
            result['charts'].append(probe(source[key],lifts[key],periods[key],geometry[key],sign))
            Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    result['status']='passed'
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')

if __name__=='__main__':main()
