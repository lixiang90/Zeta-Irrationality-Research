"""Exact root-module deformations: target indices, positive rays and collisions.

Column normalization is always recorded. Large-prime rank drops are not
identified with improvements in the primitive zeta form.
"""
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpz_mat, arb, ctx
from growing_positive_moment import shifted_map, dot, mul, node, eval_poly
from critical_lift_probe import primitive, cross
from joint_positive_module import saturated_kernel, rows_of, prime_split
from farey_cone_optimizer import optimize

sys.set_int_max_str_digits(0)


def root_block(n, starts, infinity, M):
    roots=([0] if not infinity else [])+[r for s in starts for r in (s,s+1)]
    assert len(set(roots))==len(roots)
    assert starts[0]>=(0 if infinity else 1)
    assert all(b>=a+2 for a,b in zip(starts,starts[1:]))
    H=[fmpq(1)]
    for r in roots:H=mul(H,[-fmpq(node(n,r)),fmpq(1)])
    columns=[];scales=[]
    for j in range(3):
        c,s=primitive([dot(line,[fmpq(0)]*j+H) for line in M])
        columns.append(c);scales.append(s)
    return dict(starts=list(starts),infinity=infinity,nodes=roots,H=list(map(str,H)),
                columns=columns,scales=list(map(str,scales)))


def divisor(rows):
    r=len(rows);m=len(rows[0])
    return math.gcd(*(int(fmpz_mat([[row[j] for j in js] for row in rows]).det())
                      for js in itertools.combinations(range(m),r)))


def valuation(x,p):
    assert x
    v=0
    while x%p==0:x//=p;v+=1
    return v


def mod_rank(rows,p):
    a=[[int(x)%p for x in line] for line in rows];r=0
    for j in range(len(a[0])):
        k=next((k for k in range(r,len(a)) if a[k][j]),None)
        if k is None:continue
        a[r],a[k]=a[k],a[r];inv=pow(a[r][j],-1,p)
        a[r]=[x*inv%p for x in a[r]]
        for k in range(len(a)):
            if k!=r:
                v=a[k][j];a[k]=[(x-v*y)%p for x,y in zip(a[k],a[r])]
        r+=1
        if r==len(a):break
    return r


def positive_rays(C):
    """Enumerate every extreme ray of {c>=0:A c=0}, A rank two."""
    A=[[int(C[i,j]) for j in range(6)] for i in (1,2)]
    rays={}
    for k in (1,2,3):
        for js in itertools.combinations(range(6),k):
            B=fmpz_mat([[line[j] for j in js] for line in A])
            if B.rank()!=k-1:continue
            if k==3:v=cross([A[0][j] for j in js],[A[1][j] for j in js])
            elif k==2:
                line=next(line for line in A if any(line[j] for j in js))
                v=[line[js[1]],-line[js[0]]]
            else:v=[1]
            if all(x<=0 for x in v):v=[-x for x in v]
            if not all(x>0 for x in v):continue
            g=math.gcd(*map(int,v));v=[int(x)//g for x in v]
            c=[0]*6
            for j,x in zip(js,v):c[j]=x
            out=[int(x) for x in C*fmpz_mat([[x] for x in c])]
            assert out[1:3]==[0,0] and any(out)
            g=math.gcd(*out);pair=[out[0]//g,out[3]//g]
            rays[tuple(c)]=dict(input=c,output_content=str(g),pair=pair)
    return list(rays.values())


def module(n,w,blocks,global_lo,global_hi):
    columns=[c for b in blocks for c in b['columns']]
    C=fmpz_mat([[c[i] for c in columns] for i in range(4)])
    assert C.rank()==4
    A=[[int(C[i,j]) for j in range(6)] for i in (1,2)]
    L,U=saturated_kernel(A);CL=C*L
    G=fmpz_mat([[CL[i,j] for j in range(4)] for i in (0,3)])
    s1=math.gcd(*map(int,G));delta=divisor(rows_of(G));s2=delta//s1
    dc=divisor(rows_of(C));da=divisor(A)
    assert dc==da*delta and s2%s1==0
    common=len(set(blocks[0]['nodes'])&set(blocks[1]['nodes']))
    degrees=[len(b['nodes']) for b in blocks]
    intersection=max(0,min(degrees)+3-(sum(degrees)-common))
    polynomial_rank=6-intersection
    rays=positive_rays(C)
    for ray in rays:
        a,b=ray['pair'];bound=max(a+b*global_lo,a+b*global_hi)
        assert bound>0
        # A positive summand is a rigorous lower bound on the actual form.
        r=0
        while True:
            y=node(n,r);poly=fmpq(0)
            for j,c in enumerate(ray['input']):
                block=blocks[j//3]
                poly+=c*fmpq(block['scales'][j%3])*y**(j%3)*eval_poly(list(map(fmpq,block['H'])),y)
            if poly>0:break
            assert poly==0;r+=1
        t=n+1+r;x=2*t+n
        term=poly*fmpq(math.prod(x*x-(n+2*j)**2 for j in range(1,n+1)),
                      math.prod((t+j)**7 for j in range(n+1)))/int(ray['output_content'])
        ray.update(upper_bound=str(bound),first_node=r,first_term=str(term))
    best=min(rays,key=lambda z:fmpq(z['upper_bound'])) if rays else None
    lows=[(-fmpq(a,b),i) for i,z in enumerate(rays) for a,b in [z['pair']] if b>0]
    highs=[(-fmpq(a,b),i) for i,z in enumerate(rays) for a,b in [z['pair']] if b<0]
    wedge=None
    if lows and highs:
        lo,li=max(lows);hi,ui=min(highs);assert lo<hi
        assert lo<=global_lo and hi>=global_hi
        opt=optimize(Fraction(str(lo)),Fraction(str(hi)))
        a,b=opt['pair'];E=max(a+b*global_lo,a+b*global_hi)
        wedge=dict(lower=str(lo),upper=str(hi),lower_ray=li,upper_ray=ui,
                   width=str(hi-lo),farey_pair=list(opt['pair']),local_epsilon=str(opt['epsilon']),
                   global_upper_bound=str(E))
    with ctx.workprec(192):
        return dict(n=n,w=w,blocks=blocks,matrix=rows_of(C),
                    polynomial_rank=polynomial_rank,common_root_count=common,
                    nuisance_kernel=rows_of(L),nuisance_hnf_transform=rows_of(U),
                    target_map=rows_of(G),target_smith=list(map(str,[s1,s2])),
                    output_determinantal_divisor=str(dc),nuisance_determinantal_divisor=str(da),
                    rough_s1=str(prime_split(s1,8*n)[1]),rough_s2=str(prime_split(s2,8*n)[1]),
                    log_s1_per_n=(arb(s1).log()/n).str(15),
                    rays=rays,best_ray=(rays.index(best) if best else None),wedge=wedge)


def main():
    folder=Path(__file__).parent
    source=json.loads((folder/'growing_positive_moment.json').read_text())['rows']
    source+=json.loads((folder/'growing_positive_ratio_scan.json').read_text())['rows']
    result=dict(scope='Finite root deformations and forced modular collisions; exact certificates, no irrationality claim.',cases=[],collisions=[])
    for n,w in ((8,8),(16,16),(24,24),(24,48)):
        row=next(r for r in source if r['n']==n and r['w']==w);M=shifted_map(n,w)
        lo=fmpq(row['lower']['endpoint']);hi=fmpq(row['upper']['endpoint'])
        original=[root_block(n,row[name]['starts'],row[name]['infinity'],M) for name in ('lower','upper')]
        records=[dict(label='baseline',certificate=module(n,w,original,lo,hi))]
        for k,name in enumerate(('lower','upper')):
            base=row[name]['starts'];infinity=row[name]['infinity']
            for i in range(len(base)):
                for shift in (-2,-1,1,2):
                    starts=base[:];starts[i]+=shift
                    if starts[0]<(0 if infinity else 1) or any(b<a+2 for a,b in zip(starts,starts[1:])):continue
                    blocks=original[:];blocks[k]=root_block(n,starts,infinity,M)
                    cert=module(n,w,blocks,lo,hi)
                    records.append(dict(label=f'{name}:{i}:{shift:+}',certificate=cert))
        baseline=records[0]['certificate'];wedge=baseline['wedge']
        assert fmpq(wedge['lower'])==lo and fmpq(wedge['upper'])==hi
        fixed_lower=min([fmpq(1)]+[fmpq(baseline['rays'][wedge[key]]['first_term'])/
                         abs(baseline['rays'][wedge[key]]['pair'][1]) for key in ('lower_ray','upper_ray')])
        result['cases'].append(dict(n=n,w=w,global_lower=str(lo),global_upper=str(hi),
                                   fixed_parameter_integer_form_lower_bound=str(fixed_lower),records=records))
        print('neighbors',n,w,len(records),'rough s2 count',sum(r['certificate']['rough_s2']!='1' for r in records),flush=True)
        if w==n and n in (8,16):
            for p in (101,1009):
                for e in (1,2):
                    starts=original[0]['starts'][:];starts[-1]+=p**e
                    other=root_block(n,starts,True,M)
                    cert=module(n,w,[original[0],other],lo,hi)
                    C=cert['matrix'];A=[C[i] for i in (1,2)]
                    data=dict(p=p,e=e,certificate=cert,rank_mod_p=mod_rank(C,p),nuisance_rank_mod_p=mod_rank(A,p),
                              smith_valuations=[valuation(int(s),p) for s in cert['target_smith']])
                    result['collisions'].append(data)
                    print('collision',n,p,e,'ranks',data['rank_mod_p'],data['nuisance_rank_mod_p'],
                          'v',data['smith_valuations'],'two sided',cert['wedge'] is not None,flush=True)
        (folder/'root_module_deformation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')


if __name__=='__main__':main()
