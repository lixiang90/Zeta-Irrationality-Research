"""Target-independent conductor buffers with geometry-adapted lattice bases.

LLL proposes unimodular changes; all LP bounds and accepted buffers are exact.
The LP lower bound is for the chosen basis/parallelepiped, not an intrinsic
lower bound for every possible conductor of the positive output semigroup.
"""
import copy,json,sys,math
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from critical_lift_probe import primitive
from four_pole_positive_lattice import maps,dot
from four_pole_minimal_lifts import affine,exact_box_center,nearest,ceil

sys.set_int_max_str_digits(0)

def rows(M):
    return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]

def setup(source):
    row=copy.deepcopy(source);n,m,s=[row[k] for k in ('n','m','s')]
    C2,a,b,B=maps(n,m,s)
    J,_=primitive(list(map(Q,[-n**4,4*n**3-6*n*n,4*n-1]+[0]*(m-2))))
    H=row['lattice']['image_hnf'];D=int(row['lattice']['clearing_scale'])
    image=fmpq_mat([[H[j][i] for j in range(2)] for i in range(2)])
    w,period=primitive(list(image.inv()*fmpq_mat([[D],[0]])))
    row['optimized'].update(pair=['1','0'],integer_polynomial=list(map(str,J)))
    p0,Z,z,_=affine(row,dict(image_primitive_coordinates=list(map(str,w)),
                           constructed_dilation=str(dot(a,J)/period)))
    shift=list(map(nearest,z))
    p0=[p0[i]+sum(int(Z[i,j])*shift[j] for j in range(m-2)) for i in range(m+1)]
    return C2,a,b,B,p0,Z,period

def projected(B,Z):
    return [[sum((line[i]*int(Z[i,j]) for i in range(Z.nrows())),Q(0))
             for j in range(Z.ncols())] for line in B]

def propose(A,c,center,precision=48):
    """LLL in the derivative-slack metric; integer rounding only proposes T."""
    d=len(center);slacks=[v+dot(line,center) for v,line in zip(c,A)]
    use=[i for i,line in enumerate(A) if any(line)]
    assert all(slacks[i]>0 for i in use)
    scale=2**precision
    M=fmpz_mat([[nearest(scale*A[i][j]/slacks[i]) for i in use]
               +[int(j==k) for k in range(d)] for j in range(d)])
    _,T=M.lll(transform=True)
    assert abs(int(T.det()))==1
    return T.transpose()

def integer_buffer(p0,Z,A,c,center,tau):
    beta=[sum(map(abs,line),Q(0))/2 for line in A]
    lower=max(1,ceil(1/tau));upper=max(lower,ceil(2/tau))
    candidates=set(range(lower,min(upper,lower+127)+1))
    candidates.update(lower+(upper-lower)*j//128 for j in range(129))
    best=None
    for k in sorted(candidates):
        zi=[nearest(k*x) for x in center]
        if all(k*v+dot(line,zi)>=bb for v,line,bb in zip(c,A,beta)):
            best=(k,zi);break
    assert best is not None
    # Non-monotone feasibility: bisection only searches for a better witness.
    left=lower;right=best[0]
    for _ in range(100):
        if right-left<=1:break
        k=(left+right)//2;zi=[nearest(k*x) for x in center]
        if all(k*v+dot(line,zi)>=bb for v,line,bb in zip(c,A,beta)):
            best=(k,zi);right=k
        else:left=k
    k,zi=best
    p=[k*p0[i]+sum(int(Z[i,j])*zi[j] for j in range(Z.ncols())) for i in range(Z.nrows())]
    return dict(dilation=str(k),integer_lower_bound=str(lower),guaranteed_upper_bound=str(upper),
                integer_polynomial=list(map(str,p)),coordinates=list(map(str,zi)),
                optimal_for_basis=(k==lower),input_bits=max(abs(x).bit_length() for x in p))

def solve(B,p0,Z):
    A=projected(B,Z);c=[dot(line,p0) for line in B]
    center,tau,cert=exact_box_center(A,c)
    assert tau>0
    return A,c,center,tau,cert

def case(source,old):
    n,m,s=[source[k] for k in ('n','m','s')];d=m-2
    C2,a,b,B,p0,Z,period=setup(source)
    original=Z;total=fmpz_mat([[int(i==j) for j in range(d)] for i in range(d)])
    A,c,center,tau,cert=solve(B,p0,Z)
    history=[dict(iteration=0,tau=str(tau),continuous_buffer=str(period/tau))]
    initial_tau=tau
    rejected=0
    for iteration in range(1,16):
        T=propose(A,c,center,64+8*rejected)
        candidate=Z*T
        A1,c1,center1,tau1,cert1=solve(B,p0,candidate)
        history.append(dict(iteration=iteration,tau=str(tau1),continuous_buffer=str(period/tau1),
                            accepted=tau1>tau,transform=rows(T)))
        print('basis',n,m,iteration,'gain',float(tau1/tau),flush=True)
        if tau1>tau:
            rejected=0
            Z=candidate;total=total*T
            A,c,center,tau,cert=A1,c1,center1,tau1,cert1
        else:
            rejected+=1
            if candidate==Z or rejected>=2:break
    assert Z==original*total and abs(int(total.det()))==1
    buffer=integer_buffer(p0,Z,A,c,center,tau)
    p=list(map(int,buffer['integer_polynomial']));k=int(buffer['dilation'])
    g=k*period
    assert dot(C2,p)==dot(b,p)==0 and dot(a,p)==g
    beta=list(map(Q,cert['beta']))
    assert all(dot(line,p)>=bb for line,bb in zip(B,beta))
    target=list(map(int,source['optimized']['pair']))
    H=source['lattice']['image_hnf'];D=int(source['lattice']['clearing_scale'])
    image=fmpq_mat([[H[j][i] for j in range(2)] for i in range(2)])
    _,targetperiod=primitive(list(image.inv()*fmpq_mat([[D*x] for x in target])))
    lo,hi=Q(source['optimized']['lower']),Q(source['optimized']['upper'])
    slack=min(target[0]+target[1]*lo,target[0]+target[1]*hi)
    bound=max(1,ceil(g/(targetperiod*slack)))
    out=dict(n=n,m=m,s=s,axis_period=str(period),particular=list(map(str,p0)),
             original_basis=rows(original),zero_basis=rows(Z),unimodular_transform=rows(total),
             rounding_certificate=cert,buffer=buffer,constant=str(g),continuous_lower_bound=str(period/tau),
             old_constant=old['constant'],basis_improvement=str(tau/initial_tau),
             total_improvement=str(Q(old['constant'])/g),history=history,target_dilation_bound=str(bound))
    print('done',n,m,'g',float(g),'totalgain',float(Q(old['constant'])/g),
          'lower ratio',float(k*tau),flush=True)
    return out

def main():
    folder=Path(__file__).parent
    sources=json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows']
    old=json.loads((folder/'four_pole_conductor.json').read_text())['rational_axis_regions']
    out=dict(status='in_progress',rows=[])
    path=Path(__file__).with_suffix('.json')
    for seed in old:
        source=next(r for r in sources if all(r[k]==seed[k] for k in ('n','m','s')))
        out['rows'].append(case(source,seed))
        path.write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed'
    path.write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__':main()
