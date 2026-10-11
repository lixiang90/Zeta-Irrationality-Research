"""Read-back independent verification plus basis-invariant buffer lower bounds."""
import json,sys,math,itertools
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from verify_four_pole_positive_lattice import reconstruct
from four_pole_minimal_lifts import exact_box_center

sys.set_int_max_str_digits(0)
def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))
def ceil(x):return -((-x.numerator)//x.denominator)
def qgcd(row):
    den=math.lcm(*(x.denominator for x in row))
    return F(math.gcd(*(int(x*den) for x in row)),den)

def check_lp(A,c,beta,cert):
    center=list(map(F,cert['coordinates']));tau=F(cert['tau'])
    assert list(map(F,cert['beta']))==beta and tau>0
    assert all(v+dot(line,center)>=tau*bb for v,line,bb in zip(c,A,beta))
    indices=cert['active'];dual=list(map(F,cert['dual']))
    assert len(indices)==len(dual)==len(center)+1 and min(dual)>=0
    assert sum(lam*beta[i] for i,lam in zip(indices,dual))==1
    assert all(sum(lam*A[i][j] for i,lam in zip(indices,dual))==0 for j in range(len(center)))
    assert sum(lam*c[i] for i,lam in zip(indices,dual))==tau
    return tau

def polygon(A,c):
    vertices=set()
    for i,j in itertools.combinations(range(len(A)),2):
        det=A[i][0]*A[j][1]-A[i][1]*A[j][0]
        if not det:continue
        p=((-c[i]*A[j][1]+A[i][1]*c[j])/det,
           (-A[i][0]*c[j]+c[i]*A[j][0])/det)
        if all(v+dot(line,p)>=0 for v,line in zip(c,A)):vertices.add(p)
    def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
    seq=sorted(vertices);assert len(seq)>=3
    chains=[]
    for points in (seq,list(reversed(seq))):
        hull=[]
        for p in points:
            while len(hull)>=2 and cross(hull[-2],hull[-1],p)<=0:hull.pop()
            hull.append(p)
        chains.append(hull[:-1])
    hull=chains[0]+chains[1]
    area=abs(sum(p[0]*q[1]-p[1]*q[0] for p,q in zip(hull,hull[1:]+hull[:1])))/2
    assert area>0
    return hull,area

def main():
    folder=Path(__file__).parent
    data=json.loads((folder/'four_pole_buffer_geometry.json').read_text());assert data['status']=='passed'
    source={(r['n'],r['m'],r['s']):r for r in json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows']}
    old={(r['n'],r['m'],r['s']):r for r in json.loads((folder/'four_pole_conductor.json').read_text())['rational_axis_regions']}
    out=dict(status='in_progress',rows=[])
    for row in data['rows']:
        n,m,s=[row[k] for k in ('n','m','s')];d=m-2;src=source[n,m,s]
        C2,a,b,B=reconstruct(n,m,s)
        Z=row['zero_basis'];Z0=row['original_basis'];T=fmpz_mat(row['unimodular_transform'])
        assert abs(int(T.det()))==1 and fmpz_mat(Z)==fmpz_mat(Z0)*T
        p0=list(map(int,row['particular']));period=F(row['axis_period'])
        assert [dot(v,p0) for v in (C2,a,b)]==[0,period,0]
        assert all(dot(v,col)==0 for v in (C2,a,b) for col in zip(*Z))
        # A unimodular completion certifies the full saturated zero lattice.
        U=fmpz_mat(src['lattice']['kernel_unimodular'])
        K=fmpz_mat(src['lattice']['saturated_kernel']);V=fmpz_mat(src['lattice']['image_unimodular'])
        assert abs(int(U.det()))==abs(int(V.det()))==1
        assert K==fmpz_mat([[U[j,i] for j in range(1,m+1)] for i in range(m+1)])
        assert all(dot(C2,[int(K[i,j]) for i in range(m+1)])==0 for j in range(m))
        E=K*V.transpose()
        W=fmpz_mat([[U[0,i],E[i,0],E[i,1]]+Z0[i] for i in range(m+1)])
        assert abs(int(W.det()))==1
        M=fmpq_mat([[Q(str(dot(v,[int(W[i,j]) for i in range(m+1)]))) for j in range(3)] for v in (C2,a,b)])
        assert M.det()!=0
        D=int(src['lattice']['clearing_scale']);H=src['lattice']['image_hnf']
        G=fmpq_mat([[Q(str(D*dot(v,[int(K[i,j]) for i in range(m+1)]))) for j in range(m)] for v in (a,b)])
        assert fmpq_mat(V)*G.transpose()==fmpq_mat(H)
        assert all(int(H[i][j])==0 for i in range(2,m) for j in range(2))
        image=fmpq_mat([[H[j][i] for j in range(2)] for i in range(2)])
        w=list(image.inv()*fmpq_mat([[Q(str(D*period))],[0]]))
        assert all(x.denominator==1 for x in w) and math.gcd(*(int(x) for x in w))==1
        A=[[sum(line[i]*Z[i][j] for i in range(m+1)) for j in range(d)] for line in B]
        c=[dot(line,p0) for line in B];beta=[sum(map(abs,line),F(0))/2 for line in A]
        tau=check_lp(A,c,beta,row['rounding_certificate'])
        initial_tau=F(old[n,m,s]['rounding_certificate']['tau'])
        assert F(row['history'][0]['tau'])==initial_tau
        assert F(row['basis_improvement'])==tau/initial_tau
        buf=row['buffer'];k=int(buf['dilation']);zi=list(map(int,buf['coordinates']))
        p=list(map(int,buf['integer_polynomial']))
        assert p==[k*p0[i]+sum(Z[i][j]*zi[j] for j in range(d)) for i in range(m+1)]
        assert all(dot(line,p)>=bb for line,bb in zip(B,beta))
        g=F(row['constant']);assert [dot(v,p) for v in (C2,a,b)]==[0,g,0] and g==k*period
        assert F(row['continuous_lower_bound'])==period/tau
        assert int(buf['integer_lower_bound'])==max(1,ceil(1/tau))
        assert buf['optimal_for_basis']==(k==int(buf['integer_lower_bound']))
        assert F(row['total_improvement'])==F(row['old_constant'])/g
        assert max(abs(x).bit_length() for x in p)==buf['input_bits']
        # Row-image gcd is invariant under unimodular basis change.
        A0=[[sum(line[i]*Z0[i][j] for i in range(m+1)) for j in range(d)] for line in B]
        gamma=[qgcd(line)/2 for line in A]
        assert gamma==[qgcd(line)/2 for line in A0]
        Aq=[[Q(str(x)) for x in line] for line in A];cq=list(map(lambda x:Q(str(x)),c))
        _,_,gcert=exact_box_center(Aq,cq,list(map(lambda x:Q(str(x)),gamma)))
        gtau=check_lp(A,c,gamma,gcert)
        lower=period*max(1,ceil(1/gtau))
        result=dict(n=n,m=m,s=s,constant=str(g),basis_continuous_lower_bound=str(period/tau),
                    buffer_to_continuous_lower_bound=str(k*tau),
                    invariant_gcd_lower_bound=str(lower),gcd_margin_certificate=gcert,
                    input_bits=buf['input_bits'],total_improvement=row['total_improvement'])
        if d==2:
            vertices,area=polygon(A,c)
            klower=math.isqrt(area.denominator//area.numerator)
            if klower*klower*area<1:klower+=1
            assert klower*klower*area>=1 and (klower-1)**2*area<1
            result.update(fiber_area=str(area),vertices=[list(map(str,p)) for p in vertices],
                          invariant_volume_integer_lower_bound=str(klower),
                          invariant_volume_output_lower_bound=str(period*klower),
                          volume_lower_bound_ratio_squared=str(k*k*area))
        target=list(map(int,src['optimized']['pair']))
        coords=list(image.inv()*fmpq_mat([[D*x] for x in target]))
        denom=math.lcm(*(int(x.denominator) for x in coords))
        numer=math.gcd(*(int(x*denom) for x in coords));tperiod=F(denom,numer)
        lo,hi=F(src['optimized']['lower']),F(src['optimized']['upper'])
        slack=min(target[0]+target[1]*lo,target[0]+target[1]*hi)
        assert int(row['target_dilation_bound'])==max(1,ceil(g/(tperiod*slack)))
        out['rows'].append(result)
        print('verified',n,m,'g',float(g),'gcd floor',float(lower),
              'volume floor',float(F(result.get('invariant_volume_output_lower_bound','0'))),flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed';out['certified_cases']=len(out['rows'])
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('all exact buffer, lattice and LP certificates passed',len(out['rows']))

if __name__=='__main__':main()
