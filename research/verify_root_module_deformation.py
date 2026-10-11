"""Independent Fraction reconstruction and integer certificate verification."""
import itertools
import json
import math
import sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import sympy as S
from verify_discrete_positive_cone import independent_map, dot, mul

sys.set_int_max_str_digits(0)
independent_map=lru_cache(None)(independent_map)


def node(n,r):return 4*r*(3*n+2+r)


def det(A):
    if len(A)==1:return A[0][0]
    return sum((-1)**j*A[0][j]*det([row[:j]+row[j+1:] for row in A[1:]]) for j in range(len(A)))


def minors(A):
    return math.gcd(*(int(det([[row[j] for j in js] for row in A]))
                      for js in itertools.combinations(range(len(A[0])),len(A))))


def rankmod(A,p):
    A=[[int(x)%p for x in row] for row in A];rank=0
    for j in range(len(A[0])):
        pivot=next((i for i in range(rank,len(A)) if A[i][j]),None)
        if pivot is None:continue
        A[rank],A[pivot]=A[pivot],A[rank];v=pow(A[rank][j],-1,p)
        A[rank]=[x*v%p for x in A[rank]]
        for i in range(rank+1,len(A)):
            k=A[i][j];A[i]=[(x-k*y)%p for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==len(A):break
    return rank


def vp(x,p):
    v=0
    while x%p==0:x//=p;v+=1
    return v


def evalpoly(P,x):
    s=F(0)
    for a in reversed(P):s=s*x+a
    return s


def verify(c,lo,hi):
    n,w=c['n'],c['w'];M=independent_map(n,w);cols=[];polys=[]
    assert 5*n-2*w>=1
    for block in c['blocks']:
        starts=block['starts'];assert all(b>=a+2 for a,b in zip(starts,starts[1:]))
        assert starts[0]>=(0 if block['infinity'] else 1)
        roots=([0] if not block['infinity'] else [])+[r for s in starts for r in (s,s+1)]
        assert roots==block['nodes']
        H=[F(1)]
        for r in roots:H=mul(H,[-node(n,r),1])
        assert H==list(map(F,block['H']))
        for j in range(3):
            P=[F(0)]*j+H;out=[dot(line,P) for line in M]
            den=math.lcm(*(x.denominator for x in out));out=[int(x*den) for x in out]
            g=math.gcd(*out);scale=F(den,g);col=[x//g for x in out]
            assert col==block['columns'][j] and scale==F(block['scales'][j]) and scale>0
            cols.append(col);polys.append([x*scale for x in P])
    C=[[col[i] for col in cols] for i in range(4)];assert C==c['matrix']
    A=[C[1],C[2]];L=S.Matrix(c['nuisance_kernel']);U=S.Matrix(c['nuisance_hnf_transform'])
    assert abs(U.det())==1 and S.Matrix(A)*L==S.zeros(2,4)
    assert (U*S.Matrix(A).T)[2:,:]==S.zeros(4,2) and U[2:,:].T==L
    G=(S.Matrix(C)*L)[[0,3],:];assert G==S.Matrix(c['target_map'])
    gg=[[int(x) for x in G.row(i)] for i in range(2)]
    s1=math.gcd(*(x for row in gg for x in row));s2=minors(gg)//s1
    assert [s1,s2]==list(map(int,c['target_smith']))
    dc,da=minors(C),minors(A)
    assert dc==int(c['output_determinantal_divisor']) and da==int(c['nuisance_determinantal_divisor'])
    assert dc==da*s1*s2
    for key,value in (('rough_s1',s1),('rough_s2',s2)):
        for p in range(2,8*n+1):
            while value%p==0:value//=p
        assert value==int(c[key])
    common=len(set(c['blocks'][0]['nodes'])&set(c['blocks'][1]['nodes']))
    degs=[len(b['nodes']) for b in c['blocks']]
    assert c['polynomial_rank']==6-max(0,min(degs)+3-sum(degs)+common)
    # Independently enumerate all supports of extreme rays (at most three columns).
    expected=set()
    for k in (1,2,3):
        for js in itertools.combinations(range(6),k):
            a=[A[0][j] for j in js];b=[A[1][j] for j in js]
            if k==3:v=[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
            elif k==2:
                if a[0]*b[1]!=a[1]*b[0]:continue
                line=a if any(a) else b;v=[line[1],-line[0]]
            else:
                if any(a+b):continue
                v=[1]
            if all(x<0 for x in v):v=[-x for x in v]
            if not all(x>0 for x in v):continue
            g=math.gcd(*v);full=[0]*6
            for j,x in zip(js,v):full[j]=x//g
            expected.add(tuple(full))
    assert expected=={tuple(r['input']) for r in c['rays']}
    for r in c['rays']:
        v=r['input'];out=[sum(x*y for x,y in zip(row,v)) for row in C]
        content=math.gcd(*out);a,b=r['pair']
        assert out==[content*a,0,0,content*b] and content==int(r['output_content'])
        assert max(a+b*lo,a+b*hi)==F(r['upper_bound'])>0
        P=[sum(v[j]*(polys[j][k] if k<len(polys[j]) else 0) for j in range(6)) for k in range(w+4)]
        index=r['first_node'];assert all(evalpoly(P,node(n,j))==0 for j in range(index))
        t=n+1+index;x=2*t+n
        first=evalpoly(P,node(n,index))*F(math.prod(x*x-(n+2*j)**2 for j in range(1,n+1)),
                                          math.prod((t+j)**7 for j in range(n+1)))/content
        assert first==F(r['first_term'])>0
    if c['rays']:
        assert F(c['rays'][c['best_ray']]['upper_bound'])==min(F(r['upper_bound']) for r in c['rays'])
    lower=[(-F(r['pair'][0],r['pair'][1]),i) for i,r in enumerate(c['rays']) if r['pair'][1]>0]
    upper=[(-F(r['pair'][0],r['pair'][1]),i) for i,r in enumerate(c['rays']) if r['pair'][1]<0]
    if lower and upper:
        l,li=max(lower);u,ui=min(upper);z=c['wedge']
        assert z and F(z['lower'])==l and F(z['upper'])==u and l<=lo<hi<=u
        assert F(z['width'])==u-l and z['lower_ray']==li and z['upper_ray']==ui
        a,b=z['farey_pair'];assert math.gcd(a,b)==1 and min(a+b*l,a+b*u)>0
        assert max(a+b*l,a+b*u)==F(z['local_epsilon'])
        assert max(a+b*lo,a+b*hi)==F(z['global_upper_bound'])
    else:assert c['wedge'] is None
    return C


def rational_mod(x,m):return x.numerator*pow(x.denominator,-1,m)%m


def raw_block(starts):
    H=[F(1)]
    for s in starts:
        for r in (s,s+1):H=mul(H,[-node(8,r),1])
    return [[dot(row,[F(0)]*j+H) for j in range(3)] for row in independent_map(8,8)]


def eq(starts,m):
    B=raw_block(starts)
    return [rational_mod(det([B[i] for i in (1,2,k)]),m) for k in (0,3)]


def main():
    folder=Path(__file__).parent;data=json.loads((folder/'root_module_deformation.json').read_text())
    intervals={};count=0;ray_count=0
    for case in data['cases']:
        key=(case['n'],case['w']);lo,hi=F(case['global_lower']),F(case['global_upper']);intervals[key]=(lo,hi)
        for rec in case['records']:
            c=rec['certificate'];verify(c,lo,hi);count+=1;ray_count+=len(c['rays'])
        base=case['records'][0]['certificate'];z=base['wedge']
        assert F(z['lower'])==lo and F(z['upper'])==hi
        fixed_lower=min([F(1)]+[F(base['rays'][z[key]]['first_term'])/abs(base['rays'][z[key]]['pair'][1])
                                for key in ('lower_ray','upper_ray')])
        assert fixed_lower==F(case['fixed_parameter_integer_form_lower_bound'])>0
        print('verified neighbors',key,len(case['records']),flush=True)
    for rec in data['collisions']:
        c=rec['certificate'];C=verify(c,*intervals[(c['n'],c['w'])]);p=rec['p'];e=rec['e']
        assert rankmod(C,p)==rec['rank_mod_p']==3 and rankmod([C[1],C[2]],p)==2
        assert [vp(int(x),p) for x in c['target_smith']]==rec['smith_valuations']==[0,e]
        count+=1;ray_count+=len(c['rays'])
    h=json.loads((folder/'root_rank_hensel.json').read_text());p=h['p'];base=h['base'];B=raw_block(base)
    assert eq(base,p)==[0,0]
    pivot=rational_mod(B[1][0]*B[2][1]-B[1][1]*B[2][0],p)
    assert pivot==h['nuisance_pivot']!=0
    # Derivatives via differentiated factors, independent of finite differences.
    jac=[];M=independent_map(8,8)
    for j in range(4):
        dH=[F(1)]
        for k,s in enumerate(base):
            u,v=node(8,s),node(8,s+1);du,dv=4*(26+2*s),4*(26+2*(s+1))
            factor=[du*v+u*dv,-du-dv,0] if k==j else [u*v,-u-v,1]
            dH=mul(dH,factor)
        dB=[[dot(row,[F(0)]*k+dH) for k in range(3)] for row in M]
        deriv=[]
        for k in (0,3):
            rows=[B[i] for i in (1,2,k)];drows=[dB[i] for i in (1,2,k)]
            value=sum(det([drows[t] if t==r else rows[t] for t in range(3)]) for r in range(3))
            deriv.append(rational_mod(value,p))
        jac.append(deriv)
    assert jac==h['jacobian_columns'];a,b=h['unknown_indices'];J=[[jac[a][0],jac[b][0]],[jac[a][1],jac[b][1]]]
    assert J==h['jacobian_minor'] and det(J)%p==h['jacobian_determinant_mod_p']!=0
    next_starts=base
    for rec in h['rows']:
        e=rec['e'];m=p**e;starts=rec['residue_starts'];assert starts==next_starts and eq(starts,m)==[0,0]
        assert sorted(x%m for x in rec['integer_starts'])==sorted(x%m for x in starts)
        c=rec['certificate'];C=verify(c,*intervals[(8,8)]);count+=1;ray_count+=len(c['rays'])
        assert rankmod(C,p)==rankmod([C[1],C[2]],p)==2
        assert [vp(int(x),p) for x in c['target_smith']]==rec['smith_valuations']==[e,e]
        assert eq(starts,m*p)==rec['next_equations']
        next_starts=starts[:]
        for j,d in zip((a,b),rec['next_digits']):next_starts[j]+=m*d
        assert eq(next_starts,m*p)==[0,0]
    short=json.loads((folder/'root_short_lift_scan.json').read_text());p=short['p'];R=short['R']
    modM=[[rational_mod(x,p) for x in row] for row in independent_map(8,8)]
    pair=[[(node(8,r)*node(8,r+1))%p,(-node(8,r)-node(8,r+1))%p,1] for r in range(R+1)]
    solutions=[];ranks={};tested=0
    for t in itertools.combinations(range(R-2),4):
        starts=[x+i for i,x in enumerate(t)];P=[1]
        for s in starts:P=[x%p for x in mul(P,pair[s])]
        B=[[sum(row[k+j]*x for k,x in enumerate(P))%p for j in range(3)] for row in modM]
        rank=rankmod(B,p);ranks[str(rank)]=ranks.get(str(rank),0)+1;tested+=1
        if rank==2 and rankmod([B[1],B[2]],p)==2 and all(any(B[i][j] for i in range(4)) for j in range(3)):
            solutions.append(starts)
    assert tested==short['tested'] and ranks==short['rank_counts'] and solutions==short['solutions']
    assert len(short['records'])==len(solutions)
    for rec,starts in zip(short['records'],solutions):
        c=rec['certificate'];assert rec['starts']==c['blocks'][0]['starts']==starts
        second=starts[:];second[-1]+=p;assert c['blocks'][1]['starts']==second
        C=verify(c,*intervals[(8,8)]);assert int(c['target_smith'][0])%p==0
        count+=1;ray_count+=len(c['rays'])
    result=dict(status='all exact certificate checks passed',modules=count,positive_extreme_rays=ray_count,
                hensel_levels=len(h['rows']),independent_jacobian=True,independent_bounded_root_search=tested,
                scope='Independent raw maps, saturated kernels, determinantal divisors, all positive rays, first terms and Hensel steps; modular search frequency claims are reproducible experiments.')
    (folder/'verify_root_module_deformation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result,flush=True)


if __name__=='__main__':main()
