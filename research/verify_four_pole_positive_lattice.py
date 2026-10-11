"""Independent certificates for the higher-dimensional positive output cones.

Pole jets use Fraction products. Derivatives are reconstructed from partial
fractions, not the discovery program's quotient differentiation recurrence.
No numerical LP or Arb zeta is used here.
"""
import json, math, itertools, sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from flint import fmpq as Q, fmpq_poly, fmpq_mat, fmpz_mat
from verify_four_pole_fixed_window import local
from verify_pure_odd_derivatives import harmonic, zeta_interval, displayed_interval

sys.set_int_max_str_digits(0)


def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))


@lru_cache(None)
def reconstruct(n,m,s):
    r=s-4;seed=local(n,0,0);norm=math.factorial(n)**4
    q=fmpq_poly([1])
    for k in range(n+1):q*=fmpq_poly([k+1,1])
    power=q**s
    quotients={}
    for k in range(n+1):
        for j in range(1,5):
            quotient,rem=divmod(power,fmpq_poly([k+1,1])**(j+r));assert not rem
            quotients[k,j]=quotient
    C2=[];a=[];b=[];polys=[]
    for col in range(m+1):
        degree=2*col;local_c=[];T=fmpq_poly([])
        for k in range(n+1):
            center=n-2*k
            jet=[F(math.comb(degree,i)*2**i*center**(degree-i)) if i<=degree else F(0) for i in range(4)]
            c=[F(0)]+[sum((jet[i]*seed[k][0][j+i] for i in range(5-j)),F(0)) for j in range(1,5)]
            local_c.append(c)
            for j in range(1,5):
                coefficient=c[j]*math.comb(j+r-1,r)/norm
                T+=Q(coefficient.numerator,coefficient.denominator)*quotients[k,j]
        C2.append(sum(c[2] for c in local_c))
        b.append(math.comb(s-1,3)*sum(c[4] for c in local_c))
        a.append(-sum((math.comb(j+r-1,r)*local_c[k][j]*harmonic(k,j+r)
                       for k in range(n+1) for j in range(1,5)),F(0)))
        assert len(T)<=2*col+r*n+1
        polys.append(T)
    B=[[F(str(p[i])) for p in polys] for i in range(max(len(p) for p in polys))]
    return C2,a,b,B


def main():
    folder=Path(__file__).parent
    rows=json.loads((folder/'four_pole_positive_lattice.json').read_text())['rows']
    bounds={s:zeta_interval(s) for s in (5,7,9)}
    edges_checked=0;telescopers=0;large_edges=0
    for index,row in enumerate(rows):
        n,m,s=(row[k] for k in ('n','m','s'))
        C2,a,b,B=reconstruct(n,m,s)
        assert [C2,a,b]==[list(map(F,line)) for line in row['map']]
        # Explicit integral telescoper has strictly positive rational output.
        J=[-n**4,4*n**3-6*n*n,4*n-1]+[0]*(m-2)
        assert dot(C2,J)==dot(b,J)==0 and dot(a,J)>0;telescopers+=1
        lattice=row['lattice'];A=fmpz_mat([[int(x) for x in lattice['constraint']]])
        assert math.gcd(*(int(x) for x in A))==1
        assert all(int(A[0,j])*C2[0]==int(A[0,0])*C2[j] for j in range(m+1))
        U=fmpz_mat(lattice['kernel_unimodular']);K=fmpz_mat(lattice['saturated_kernel'])
        assert abs(int(U.det()))==1
        AU=U*A.transpose();assert abs(int(AU[0,0]))==1 and all(AU[i,0]==0 for i in range(1,m+1))
        assert K==fmpz_mat([[U[j,i] for j in range(1,m+1)] for i in range(m+1)])
        assert not any(A*K)
        D=int(lattice['clearing_scale']);assert D==math.lcm(*range(1,n+1))**s
        M=fmpz_mat([[int(x*D) for x in line] for line in (a,b)])
        assert all((x*D).denominator==1 for line in (a,b) for x in line)
        G=fmpz_mat(lattice['target_map']);assert G==M*K and G.rank()==2
        H=fmpz_mat(lattice['image_hnf']);V=fmpz_mat(lattice['image_unimodular'])
        assert abs(int(V.det()))==1 and H==V*G.transpose()
        assert all(H[i,j]==0 for i in range(2,H.nrows()) for j in range(2))
        g1=math.gcd(*(int(x) for x in G))
        g2=math.gcd(*(int(G[0,i]*G[1,j]-G[0,j]*G[1,i]) for i,j in itertools.combinations(range(m),2)))
        assert [g1,g2//g1]==list(map(int,lattice['smith']))
        basis=[list(map(F,p)) for p in row['coordinate_basis']]
        for i,p in enumerate(basis):
            assert dot(C2,p)==0 and dot(a,p)==(i==0) and dot(b,p)==(i==1)
        coeff=[[dot(line,p) for p in basis] for line in B]
        for edge in row['edges']:
            assert edge['status']=='certified'
            p=list(map(F,edge['polynomial']));sign=edge['sign'];constant=F(edge['constant'])
            assert dot(C2,p)==0 and dot(a,p)==constant and dot(b,p)==sign
            positive=[dot(line,p) for line in B]
            assert positive==list(map(F,edge['derivative_coefficients']))
            assert all(x>=0 for x in positive) and any(positive)
            weights=list(map(F,edge['dual']));active=edge['active']
            assert all(x>=0 for x in weights)
            # c = B_active^T lambda for all free variables at fixed b.
            for j in [0]+list(range(2,m)):
                assert sum(w*coeff[i][j] for w,i in zip(weights,active))==(j==0)
            assert constant==-sign*sum(w*coeff[i][1] for w,i in zip(weights,active))
            assert all(positive[i]==0 for i in active)
            ea,eb=map(int,edge['primitive_pair']);scale=F(edge['primitive_scale'])
            assert [scale*constant,scale*sign]==[ea,eb] and math.gcd(ea,eb)==1
            assert min(ea+eb*z for z in bounds[s])>1;large_edges+=1
            edges_checked+=1
        opt=row['optimized'];lo,hi=F(opt['lower']),F(opt['upper'])
        zlo,zhi=bounds[s];assert lo<zlo<zhi<hi
        pair=list(map(int,opt['pair']));eps=F(opt['epsilon'])
        pl,ql=map(int,opt['farey_left']);pu,qu=map(int,opt['farey_right'])
        Qmin=int(opt['minimum_internal_denominator'])
        assert pu*ql-pl*qu==1 and Qmin==ql+qu
        assert F(pl,ql)<=lo and (qu==0 or hi<=F(pu,qu))
        assert lo<F(pl+pu,Qmin)<hi and F(1,Qmin)<=eps<=F(2,Qmin)
        assert list(map(F,opt['edge_uniform_bounds']))==[(hi-lo)*abs(int(e['primitive_pair'][1])) for e in row['edges']]
        assert math.gcd(*pair)==1 and eps==max(pair[0]+pair[1]*lo,pair[0]+pair[1]*hi)
        assert min(pair[0]+pair[1]*lo,pair[0]+pair[1]*hi)>=0
        w=list(map(F,opt['positive_weights']));assert all(v>=0 for v in w)
        p=[sum(w[k]*F(row['edges'][k]['polynomial'][j]) for k in range(2)) for j in range(m+1)]
        assert [dot(a,p),dot(b,p)]==pair and dot(C2,p)==0
        integers=list(map(int,opt['integer_polynomial']));scale=F(opt['output_scale'])
        assert scale>0 and [scale*x for x in p]==integers and math.gcd(*integers)==1
        value_lo,value_hi=sorted((pair[0]+pair[1]*zlo,pair[0]+pair[1]*zhi))
        assert 0<value_lo<value_hi<eps<1
        shown=displayed_interval(opt['value']);assert shown[0]<=value_lo<value_hi<=shown[1]
        if (index+1)%10==0:print('verified',index+1,flush=True)
    result=dict(status='passed',cases=len(rows),certified_endpoints=edges_checked,
                integer_lattices=len(rows),positive_primitive_forms=len(rows),telescoper_checks=telescopers,
                primitive_endpoint_forms_above_one=large_edges,farey_denominator_certificates=len(rows),
                method='Independent pole product jets and partial-fraction derivative polynomials; unimodular lattice certificates, exact primal/dual identities, integer lifts, rational zeta bounds.')
    (folder/'verify_four_pole_positive_lattice.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result,flush=True)


if __name__=='__main__':main()
