"""Affine zero-output lattices, exact 1D minima and certified rounding lifts."""
import json,math,sys
from pathlib import Path
from fractions import Fraction as F
from flint import fmpz_mat, fmpq_mat, fmpq as Q
from critical_lift_probe import primitive
from four_pole_positive_lattice import maps, dot, dual_feasible_basis
from joint_positive_module import rows_of
from farey_cone_optimizer import simplest_parents

sys.set_int_max_str_digits(0)


def floor(x):return int(x.numerator)//int(x.denominator)
def ceil(x):return -floor(-x)
def nearest(x):return floor(x+Q(1,2))


def simplest_closed(lo,hi):
    lo,hi=F(str(lo)),F(str(hi));assert lo<=hi
    if lo==hi:return lo,dict(kind='point',value=str(lo))
    if ceil(lo)<=hi:return F(ceil(lo)),dict(kind='integer',integer=ceil(lo))
    shift=floor(lo);l,h=lo-shift,hi-shift
    left,right,_=simplest_parents(l,h)
    p,q=left;r,s=right;inside=F(p+r,q+s)+shift
    best=min((lo,hi,inside),key=lambda x:(x.denominator,x.numerator))
    return best,dict(kind='farey',shift=shift,left=list(left),right=list(right),
                     open_min_denominator=q+s,selected=str(best))


def exact_box_center(A,c,beta=None):
    """Maximize tau with c+A*z >= tau*sum(abs(A_i))/2.

    The rational dual is a certificate for the optimum. This is a sufficient
    rounding radius, not a lower bound on the first feasible integer dilation.
    An optional nonnegative beta solves the same LP with prescribed margins;
    the default retains the original coordinate-box rounding radius.
    """
    if beta is None:
        beta=[sum((abs(x) for x in line),Q(0))/2 for line in A]
    else:
        beta=list(map(Q,beta))
        assert len(beta)==len(A) and all(x>=0 for x in beta)
    keep=[i for i,x in enumerate(beta) if x]
    assert all(v>=0 for i,v in enumerate(c) if i not in keep)
    cons=[[beta[i]]+A[i] for i in keep];rhs=[-c[i] for i in keep]
    dim=len(cons[0]);chosen,phase1=dual_feasible_basis(cons)
    for iteration in range(10000):
        M=fmpq_mat([cons[i] for i in chosen]);inv=M.inv()
        sol=list(inv*fmpq_mat([[rhs[i]] for i in chosen]))
        dual=list(inv.transpose()*fmpq_mat([[int(i==0)] for i in range(dim)]))
        assert all(x>=0 for x in dual)
        entering=next((i for i in range(len(cons)) if dot(cons[i],sol)<rhs[i]),None)
        if entering is None:
            tau=-sol[0];z=sol[1:]
            assert all(v+dot(line,z)>=tau*b for v,line,b in zip(c,A,beta))
            return z,tau,dict(beta=list(map(str,beta)),active=[keep[i] for i in chosen],
                              dual=list(map(str,dual)),tau=str(tau),coordinates=list(map(str,z)),
                              phase1_pivots=phase1,optimization_pivots=iteration)
        alpha=list(fmpq_mat([cons[entering]])*inv)
        candidates=[j for j in range(dim) if alpha[j]>0]
        assert candidates
        leaving=min(candidates,key=lambda j:(dual[j]/alpha[j],chosen[j]))
        chosen[leaving]=entering
    raise RuntimeError('box center pivot limit')


def polygon_minimum(A,c,upper,limit=100000):
    """Exact enumeration of thin integer slices for a bounded 2D fiber."""
    import itertools
    vertices=set()
    for i,j in itertools.combinations(range(len(A)),2):
        M=fmpq_mat([A[i],A[j]])
        if not M.det():continue
        v=tuple(M.inv()*fmpq_mat([[-c[i]],[-c[j]]]))
        if all(dot(line,v)+value>=0 for line,value in zip(A,c)):vertices.add(v)
    assert len(vertices)>=3
    directions=[(1,0),(0,1),(1,1),(1,-1),(2,1),(2,-1),(1,2),(1,-2)]
    direction=min(directions,key=lambda w:max(dot(w,v) for v in vertices)-min(dot(w,v) for v in vertices))
    a,b=direction
    def egcd(a,b):
        if b==0:return abs(a),1 if a>0 else -1,0
        g,x,y=egcd(b,a%b);return g,y,x-(a//b)*y
    g,s,t=egcd(a,b);assert g==1
    U=[[a,b],[-t,s]];inv=[[s,-b],[t,a]]
    transformed=[[line[0]*inv[0][j]+line[1]*inv[1][j] for j in range(2)] for line in A]
    lo=min(dot(direction,v) for v in vertices);hi=max(dot(direction,v) for v in vertices)
    visited=0
    for k in range(1,upper+1):
        left,right=ceil(k*lo),floor(k*hi)
        if visited+max(0,right-left+1)>limit:return None
        for y0 in range(left,right+1):
            visited+=1
            offsets=[k*v+line[0]*y0 for v,line in zip(c,transformed)]
            if any(v<0 for v,line in zip(offsets,transformed) if not line[1]):continue
            yl=max(-v/line[1] for v,line in zip(offsets,transformed) if line[1]>0)
            yu=min(-v/line[1] for v,line in zip(offsets,transformed) if line[1]<0)
            if ceil(yl)<=yu:
                y=[y0,ceil(yl)];z=[sum(inv[i][j]*y[j] for j in range(2)) for i in range(2)]
                assert all(k*v+dot(line,z)>=0 for v,line in zip(c,A))
                return k,z,dict(kind='enumerated_polygon',vertices=[list(map(str,v)) for v in sorted(vertices)],
                                slice_transform=U,slice_interval=[str(lo),str(hi)],
                                tested_integer_slices=visited,selected_slice=y)
    raise AssertionError('known upper bound not found in polygon')


def affine(row,period):
    m=row['m'];U=fmpz_mat(row['lattice']['kernel_unimodular'])
    K=fmpz_mat(row['lattice']['saturated_kernel']);V=fmpz_mat(row['lattice']['image_unimodular'])
    E=K*V.transpose();w=list(map(int,period['image_primitive_coordinates']))
    p0=[sum(int(E[i,j])*w[j] for j in range(2)) for i in range(m+1)]
    Z=fmpz_mat([[E[i,j] for j in range(2,m)] for i in range(m+1)])
    full=fmpz_mat([[U[0,i]]+[E[i,j] for j in range(m)] for i in range(m+1)])
    assert abs(int(full.det()))==1
    oldk=Q(period['constructed_dilation'])
    oldp=[Q(int(x))/oldk for x in row['optimized']['integer_polynomial']]
    zall=list(fmpq_mat(full).inv()*fmpq_mat([[x] for x in oldp]))
    assert zall[:3]==[0]+w
    z=zall[3:]
    if m>2:
        reduced,T=Z.transpose().lll(transform=True)
        assert abs(int(T.det()))==1 and T*Z.transpose()==reduced
        Z=reduced.transpose();z=list(fmpq_mat(T.transpose()).inv()*fmpq_mat([[x] for x in z]))
    else:T=fmpz_mat(0,0)
    assert oldp==[p0[i]+sum((Q(Z[i,j])*z[j] for j in range(m-2)),Q(0)) for i in range(m+1)]
    return p0,Z,z,T


def probe(row,period):
    n,m,s=(row[k] for k in ('n','m','s'));d=m-2
    p0,Z,z,T=affine(row,period);C2,a,b,B=maps(n,m,s)
    A=[[sum((line[i]*int(Z[i,j]) for i in range(m+1)),Q(0)) for j in range(d)] for line in B]
    c=[dot(line,p0) for line in B]
    out=dict(n=n,m=m,s=s,pair=row['optimized']['pair'],period=period['minimum_arithmetic_output_multiplier'],
             particular=list(map(str,p0)),zero_basis=rows_of(Z),lll_transform=rows_of(T),
             old_dilation=period['constructed_dilation'],old_input_bits=row['optimized']['input_height_bits'])
    k=1;coords=[]
    if d==0:
        assert min(c)>=0;out['minimality']=dict(kind='zero_dimensional')
    elif d==1:
        lo=max(-v/line[0] for v,line in zip(c,A) if line[0]>0)
        hi=min(-v/line[0] for v,line in zip(c,A) if line[0]<0)
        assert all(v>=0 for v,line in zip(c,A) if line[0]==0)
        chosen,certificate=simplest_closed(lo,hi);k=chosen.denominator;coords=[chosen.numerator]
        out.update(interval=[str(lo),str(hi)],minimality=certificate)
    else:
        coords=[nearest(x) for x in z]
        if any(k*v+dot(line,coords)<0 for v,line in zip(c,A)):
            # Translate the affine origin so the known point is near z=0.
            p0=[p0[i]+sum(int(Z[i,j])*coords[j] for j in range(d)) for i in range(m+1)]
            c=[dot(line,p0) for line in B]
            out['particular']=list(map(str,p0))
            center,tau,cert=exact_box_center(A,c);out['rounding_certificate']=cert
            if tau<=0:
                out.update(status='lower_dimensional_fiber',old_center_coordinates=list(map(str,z)))
                return out
            guaranteed=max(1,ceil(1/tau));out['guaranteed_dilation']=str(guaranteed)
            candidates=list(range(1,min(1000,guaranteed)+1))
            if guaranteed>1000:candidates.append(guaranteed)
            for k in candidates:
                coords=[nearest(k*x) for x in center]
                if all(k*v+dot(line,coords)>=0 for v,line in zip(c,A)):break
            else:raise AssertionError('rounding bound failed')
        out['minimality']=dict(kind='positive_at_arithmetic_minimum' if k==1 else 'upper_bound_only')
        if d==2 and k>1:
            refined=polygon_minimum(A,c,k)
            if refined is not None:k,coords,out['minimality']=refined
    p=[k*p0[i]+sum(int(Z[i,j])*coords[j] for j in range(d)) for i in range(m+1)]
    assert all(dot(line,p)>=0 for line in B)
    scale=Q(out['period'])*k;pair=list(map(int,out['pair']))
    assert dot(C2,p)==0 and dot(a,p)==scale*pair[0] and dot(b,p)==scale*pair[1]
    g=math.gcd(*p)
    if g>1:
        assert k%g==0 and all(x%g==0 for x in coords)
        k//=g;p=[x//g for x in p];coords=[x//g for x in coords]
    minimum=(d<=1 or k==1 or out['minimality']['kind']=='enumerated_polygon')
    out.update(status='certified_minimum' if minimum else 'certified_upper_bound',dilation=str(k),
               minimum_dilation=str(k) if minimum else None,integer_coordinates=list(map(str,coords)),
               integer_polynomial=list(map(str,p)),input_bits=max(abs(x).bit_length() for x in p))
    return out


def main():
    folder=Path(__file__).parent
    source=json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows']
    periods=json.loads((folder/'four_pole_lift_periods.json').read_text())['rows']
    rows=[]
    for row,period in zip(source,periods):
        result=probe(row,period);rows.append(result)
        print(result['n'],result['m'],result['s'],result['status'],result.get('minimum_dilation'),
              'bits',result.get('input_bits'),flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
