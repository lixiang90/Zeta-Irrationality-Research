"""Buffered positive lattice points certify an entire translated output cone.

Uses the independent partial-fraction reconstruction to verify every buffer.
"""
import json,sys
import copy
from pathlib import Path
from fractions import Fraction as F
from verify_four_pole_positive_lattice import reconstruct
from flint import fmpq_mat,fmpq as Q
from critical_lift_probe import primitive
from four_pole_positive_lattice import maps
from four_pole_minimal_lifts import affine,exact_box_center

sys.set_int_max_str_digits(0)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def ceil(x):return -((-x.numerator)//x.denominator)
def nearest(x):
    x=F(str(x))+F(1,2)
    return x.numerator//x.denominator


def rational_axis_seed(source):
    row=copy.deepcopy(source);n,m,s=[row[k] for k in ('n','m','s')]
    C2,a,b,B=maps(n,m,s)
    J=[-n**4,4*n**3-6*n*n,4*n-1]+[0]*(m-2)
    J,scale=primitive(list(map(Q,J)));output=dot(a,J)
    H=row['lattice']['image_hnf'];D=int(row['lattice']['clearing_scale'])
    basis=fmpq_mat([[H[j][i] for j in range(2)] for i in range(2)])
    coords=list(basis.inv()*fmpq_mat([[D],[0]]));w,period=primitive(coords)
    oldk=output/period;assert oldk.denominator==1
    row['optimized'].update(pair=['1','0'],integer_polynomial=list(map(str,J)))
    periodrow=dict(image_primitive_coordinates=list(map(str,w)),constructed_dilation=str(oldk))
    p0,Z,z,T=affine(row,periodrow)
    shift=[nearest(x) for x in z]
    p0=[p0[i]+sum(int(Z[i,j])*shift[j] for j in range(m-2)) for i in range(m+1)]
    A=[[sum((line[i]*int(Z[i,j]) for i in range(m+1)),Q(0)) for j in range(m-2)] for line in B]
    c=[dot(line,p0) for line in B]
    center,tau,cert=exact_box_center(A,c);assert tau>0
    k=max(1,ceil(2/F(str(tau))));zi=[nearest(k*x) for x in center]
    p=[k*p0[i]+sum(int(Z[i,j])*zi[j] for j in range(m-2)) for i in range(m+1)]
    # Independent partial-fraction derivative reconstruction validates the buffer.
    C2i,ai,bi,Bi=reconstruct(n,m,s)
    Ai=[[sum(line[i]*int(Z[i,j]) for i in range(m+1)) for j in range(m-2)] for line in Bi]
    beta=[sum(map(abs,line),F(0))/2 for line in Ai]
    assert all(dot(line,p)>=bb for line,bb in zip(Bi,beta))
    g=dot(ai,p);assert dot(C2i,p)==dot(bi,p)==0 and g==k*F(str(period))>0
    target=list(map(int,source['optimized']['pair']))
    targetcoords=list(basis.inv()*fmpq_mat([[D*x] for x in target]))
    _,targetperiod=primitive(targetcoords)
    lo,hi=F(source['optimized']['lower']),F(source['optimized']['upper'])
    slack=min(target[0]+target[1]*lo,target[0]+target[1]*hi)
    bound=max(1,ceil(g/(F(str(targetperiod))*slack))) if slack>0 else None
    if bound is not None:assert bound*F(str(targetperiod))*slack>=g
    return dict(n=n,m=m,s=s,axis_period=str(period),dilation=str(k),constant=str(g),
                integer_polynomial=list(map(str,p)),zero_basis=[[int(Z[i,j]) for j in range(m-2)] for i in range(m+1)],
                input_bits=max(abs(x).bit_length() for x in p),rounding_certificate=cert,
                assessed_target=source['optimized']['pair'],target_dilation_bound=str(bound) if bound is not None else None,
                theorem='(g,0)+(Gamma intersect C) is positively integrally liftable.')


def main():
    folder=Path(__file__).parent
    lifts=json.loads((folder/'four_pole_minimal_lifts.json').read_text())['rows'];rows=[]
    for lift in lifts:
        if 'rounding_certificate' not in lift:continue
        n,m,s=[lift[k] for k in ('n','m','s')];d=m-2
        C2,a,b,B=reconstruct(n,m,s)
        Z=lift['zero_basis'];p0=list(map(int,lift['particular']))
        cert=lift['rounding_certificate'];tau=F(cert['tau']);center=list(map(F,cert['coordinates']))
        k=max(1,ceil(2/tau));coords=[nearest(k*x) for x in center]
        p=[k*p0[i]+sum(Z[i][j]*coords[j] for j in range(d)) for i in range(m+1)]
        A=[[sum(line[i]*Z[i][j] for i in range(m+1)) for j in range(d)] for line in B]
        beta=[sum(map(abs,line),F(0))/2 for line in A]
        positive=[dot(line,p) for line in B]
        assert all(v>=rad for v,rad in zip(positive,beta))
        pair=list(map(int,lift['pair']));period=F(lift['period'])
        output=[dot(a,p),dot(b,p)]
        assert dot(C2,p)==0 and output==[k*period*x for x in pair]
        margin=min(v/rad for v,rad in zip(positive,beta) if rad)
        rows.append(dict(n=n,m=m,s=s,dilation=str(k),integer_polynomial=list(map(str,p)),
                         output=list(map(str,output)),zero_basis=Z,rounding_radius=list(map(str,beta)),
                         minimum_buffer_ratio=str(margin),input_bits=max(abs(x).bit_length() for x in p)))
    source=json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows']
    axis=[]
    for n,m in ((4,4),(8,8),(16,12),(24,12),(32,12)):
        seed=rational_axis_seed(next(x for x in source if (x['n'],x['m'],x['s'])==(n,m,7)))
        axis.append(seed);print('rational axis seed',n,m,'bits',seed['input_bits'],flush=True)
    result=dict(status='passed',certified_conductor_regions=len(rows),rows=rows,rational_axis_regions=axis,
                theorem='If w_star is this output, then w_star + (Gamma intersect C) is contained in the positive integer output semigroup. The cone C is the previously certified coefficient-positive output cone.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('independently verified buffered seeds',len(rows))


if __name__=='__main__':main()
