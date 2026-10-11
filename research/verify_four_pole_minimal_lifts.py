"""Independent exact verification of affine lattices and positive integer lifts."""
import json,math,itertools,sys
from pathlib import Path
from fractions import Fraction as F
from flint import fmpz_mat,fmpq_mat
from verify_four_pole_positive_lattice import reconstruct

sys.set_int_max_str_digits(0)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)


def interval_minimum(lo,hi,cert):
    kind=cert['kind']
    if kind=='point':assert lo==hi;return lo.denominator
    if kind=='integer':assert lo<=cert['integer']<=hi;return 1
    assert kind=='farey'
    shift=cert['shift'];l,h=lo-shift,hi-shift
    p,q=cert['left'];r,s=cert['right']
    assert 0<=l<h and r*q-p*s==1
    assert F(p,q)<=l and (s==0 or h<=F(r,s))
    assert l<F(p+r,q+s)<h
    assert cert['open_min_denominator']==q+s
    chosen=F(cert['selected']);assert lo<=chosen<=hi
    result=min(lo.denominator,hi.denominator,q+s)
    assert chosen.denominator==result
    return result


def polygon_minimum(A,c,cert,k_expected):
    vertices=set()
    for i,j in itertools.combinations(range(len(A)),2):
        det=A[i][0]*A[j][1]-A[i][1]*A[j][0]
        if not det:continue
        v=((-c[i]*A[j][1]+A[i][1]*c[j])/det,
           (-A[i][0]*c[j]+c[i]*A[j][0])/det)
        if all(value+dot(line,v)>=0 for value,line in zip(c,A)):vertices.add(v)
    assert vertices=={tuple(map(F,v)) for v in cert['vertices']}
    U=cert['slice_transform'];a,b=U[0];cc,dd=U[1]
    assert a*dd-b*cc==1
    inv=[[dd,-b],[-cc,a]]
    lo=min(dot(U[0],v) for v in vertices);hi=max(dot(U[0],v) for v in vertices)
    assert [lo,hi]==list(map(F,cert['slice_interval']))
    M=[[line[0]*inv[0][j]+line[1]*inv[1][j] for j in range(2)] for line in A]
    visited=0
    for k in range(1,k_expected+1):
        for x in range(ceil(k*lo),floor(k*hi)+1):
            visited+=1
            offsets=[k*v+line[0]*x for v,line in zip(c,M)]
            if any(v<0 for v,line in zip(offsets,M) if not line[1]):continue
            lower=max(-v/line[1] for v,line in zip(offsets,M) if line[1]>0)
            upper=min(-v/line[1] for v,line in zip(offsets,M) if line[1]<0)
            if ceil(lower)<=upper:
                assert k==k_expected and [x,ceil(lower)]==cert['selected_slice']
                assert visited==cert['tested_integer_slices']
                return
    raise AssertionError('claimed polygon minimum not found')


def main():
    folder=Path(__file__).parent
    source=json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows']
    lifts=json.loads((folder/'four_pole_minimal_lifts.json').read_text())['rows']
    periods=json.loads((folder/'four_pole_lift_periods.json').read_text())['rows']
    minima=0;upper=0;boxes=0;polygons=0;one_dim=0;unit=0
    for index,(row,lift,periodrow) in enumerate(zip(source,lifts,periods)):
        n,m,s=(row[k] for k in ('n','m','s'));d=m-2
        assert (n,m,s)==tuple(lift[k] for k in ('n','m','s'))
        C2,a,b,B=reconstruct(n,m,s)
        U=fmpz_mat(row['lattice']['kernel_unimodular']);K=fmpz_mat(row['lattice']['saturated_kernel'])
        V=fmpz_mat(row['lattice']['image_unimodular']);H=fmpz_mat(row['lattice']['image_hnf'])
        D=int(row['lattice']['clearing_scale'])
        Arow=fmpz_mat([[int(x) for x in row['lattice']['constraint']]])
        assert abs(int(U.det()))==abs(int(V.det()))==1
        assert K==fmpz_mat([[U[j,i] for j in range(1,m+1)] for i in range(m+1)])
        AU=U*Arow.transpose();assert abs(int(AU[0,0]))==1 and all(AU[i,0]==0 for i in range(1,m+1))
        assert all(int(Arow[0,j])*C2[0]==int(Arow[0,0])*C2[j] for j in range(m+1))
        M=fmpz_mat([[int(x*D) for x in line] for line in (a,b)]);G=M*K
        assert H==V*G.transpose()
        assert all(H[i,j]==0 for i in range(2,m) for j in range(2))
        image_basis=fmpq_mat([[H[j,i] for j in range(2)] for i in range(2)])
        pair=list(map(int,lift['pair']));assert pair==list(map(int,row['optimized']['pair']))
        period=F(lift['period']);assert period==F(periodrow['minimum_arithmetic_output_multiplier'])
        coeff=list(image_basis.inv()*fmpq_mat([[D*x] for x in pair]))
        intcoords=[period*F(str(x)) for x in coeff]
        assert all(x.denominator==1 for x in intcoords) and math.gcd(*(int(x) for x in intcoords))==1
        E=K*V.transpose();Z=fmpz_mat(lift['zero_basis']);T=fmpz_mat(lift['lll_transform'])
        if d:
            original=fmpz_mat([[E[i,j] for j in range(2,m)] for i in range(m+1)])
            assert abs(int(T.det()))==1 and Z==original*T.transpose()
        p0=list(map(int,lift['particular']))
        assert dot(C2,p0)==0 and [dot(a,p0),dot(b,p0)]==[period*x for x in pair]
        for j in range(d):assert all(dot(line,[int(Z[i,j]) for i in range(m+1)])==0 for line in (C2,a,b))
        A=[[sum((line[i]*int(Z[i,j]) for i in range(m+1)),F(0)) for j in range(d)] for line in B]
        c=[dot(line,p0) for line in B]
        if 'rounding_certificate' in lift:
            cert=lift['rounding_certificate'];tau=F(cert['tau']);center=list(map(F,cert['coordinates']))
            beta=[sum(map(abs,line),F(0))/2 for line in A]
            assert beta==list(map(F,cert['beta'])) and tau>0
            assert all(v+dot(line,center)>=tau*bb for v,line,bb in zip(c,A,beta))
            active=cert['active'];weights=list(map(F,cert['dual']));assert all(x>=0 for x in weights)
            assert sum(w*beta[i] for w,i in zip(weights,active))==1
            assert all(sum(w*A[i][j] for w,i in zip(weights,active))==0 for j in range(d))
            assert sum(w*c[i] for w,i in zip(weights,active))==tau
            assert int(lift['guaranteed_dilation'])==max(1,ceil(1/tau));boxes+=1
        k=int(lift['dilation']);p=list(map(int,lift['integer_polynomial']));z=list(map(int,lift['integer_coordinates']))
        assert p==[k*p0[i]+sum(int(Z[i,j])*z[j] for j in range(d)) for i in range(m+1)]
        assert math.gcd(*p)==1 and max(abs(x).bit_length() for x in p)==lift['input_bits']
        assert dot(C2,p)==0 and [dot(a,p),dot(b,p)]==[k*period*x for x in pair]
        values=[dot(line,p) for line in B];assert min(values)>=0 and any(values)
        assert k<=int(lift['old_dilation']) and lift['input_bits']<=lift['old_input_bits']
        if lift['status']=='certified_minimum':
            assert int(lift['minimum_dilation'])==k;minima+=1
            if k==1:unit+=1
            elif d==1:
                lo=max(-v/line[0] for v,line in zip(c,A) if line[0]>0)
                hi=min(-v/line[0] for v,line in zip(c,A) if line[0]<0)
                assert [lo,hi]==list(map(F,lift['interval']))
                assert interval_minimum(lo,hi,lift['minimality'])==k;one_dim+=1
            else:
                assert d==2 and lift['minimality']['kind']=='enumerated_polygon'
                polygon_minimum(A,c,lift['minimality'],k);polygons+=1
        else:
            assert lift['status']=='certified_upper_bound' and lift['minimum_dilation'] is None;upper+=1
        if (index+1)%10==0:print('verified',index+1,flush=True)
    result=dict(status='passed',cases=len(lifts),exact_minima=minima,upper_bounds_only=upper,
                unit_dilation_minima=unit,nonunit_interval_minima=one_dim,nonunit_polygon_minima=polygons,
                optimal_rounding_box_certificates=boxes,
                method='Independent Fraction pole/derivative reconstruction; complete affine lattice certificates; Farey closed-interval minima; exhaustive polygon slices; primal/dual rounding radius and integer positivity checks.')
    (folder/'verify_four_pole_minimal_lifts.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result,flush=True)


if __name__=='__main__':main()
