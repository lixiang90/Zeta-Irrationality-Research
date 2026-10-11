"""Exact certificates for enlarged positivity cones; floating LP only proposes supports.

All endpoint certificates use rational partial fractions and nonnegative generators.
Finite ansatz cones are not the cone of all nonnegative polynomials.
"""
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.optimize import linprog
from flint import fmpq, fmpq_mat, arb, ctx
from critical_lift_probe import output_map, primitive, cross
from farey_cone_optimizer import optimize


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),fmpq(0))


def mul(a,b):
    out=[fmpq(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out


def shifted_map(n,w):
    d=w+3
    out,_=output_map(n,head=n,degrees=tuple(range(0,2*d+1,2)))
    origin=(3*n+2)**2
    return [[sum((out[k][j]*math.comb(i,j)*(-origin)**(i-j)
                  for j in range(i+1)),fmpq(0)) for i in range(d+1)]
            for k in (0,3,5,7)]


def cubic_certificate(n):
    M=fmpq_mat(shifted_map(n,0)); I=M.inv()
    U=[I[j,0] for j in range(4)]; V=[I[j,3] for j in range(4)]
    assert all(u>0 for u in U)
    ratios=[v/u for u,v in zip(U,V)]
    direction=1 if ratios[3]>ratios[0] else -1
    assert all(direction*(ratios[i+1]-ratios[i])>0 for i in range(3))
    # Coefficient of y^(i+j-1) in V' U - V U':
    derivative=[fmpq(0)]*5
    for i in range(4):
        for j in range(i): derivative[i+j-1]+=(i-j)*(V[i]*U[j]-V[j]*U[i])
    assert all(direction*c>0 for c in derivative)
    return dict(n=n,U=list(map(str,U)),V=list(map(str,V)),
        ratios=list(map(str,ratios)),derivative=list(map(str,derivative)),
        full_discrete_lower=str(min(ratios)),full_discrete_upper=str(max(ratios)),
        certified_equal_to_shifted_coefficient_cone=True)


def generators(n,d,kind):
    # y=(2t+n)^2-(3n+2)^2, node r corresponds to t=n+1+r.
    node=lambda r: fmpq((3*n+2+2*r)**2-(3*n+2)**2)
    gens=[]; seen=set()
    def add(p,tag):
        p=list(p)+[fmpq(0)]*(d+1-len(p))
        key=tuple(map(str,p))
        if key not in seen:
            seen.add(key);gens.append((p,tag))
    for j in range(d+1): add([0]*j+[1],dict(type='monomial',power=j))
    if kind=='monomial': return gens
    if kind=='extreme_window':
        # Complete extreme-ray root patterns whose node indices are <=12.
        # Extra monomials remain included to simplify baseline comparisons.
        for odd in (0,1):
            for k in range((d-odd)//2+1):
                for starts in itertools.combinations(range(odd,12),k):
                    if any(b<a+2 for a,b in zip(starts,starts[1:])): continue
                    p=[fmpq(0),fmpq(1)] if odd else [fmpq(1)]
                    for r in starts: p=mul(p,[node(r)*node(r+1),-node(r)-node(r+1),fmpq(1)])
                    add(p,dict(type='pairs',power=odd,node_pairs=[[r,r+1] for r in starts]))
        return gens
    # Each block is positive on the specified support and monic.
    # Include single blocks anywhere in a finite window, and consecutive blocks.
    starts=range(0,9)
    for degree_blocks in range(1,min(d//2,4)+1):
        for start in starts:
            p=[fmpq(1)]; factors=[]
            for k in range(degree_blocks):
                r=start+2*k
                if kind=='squares':
                    a=b=node(r)
                else:
                    a,b=node(r),node(r+1)
                p=mul(p,[a*b,-a-b,fmpq(1)])
                factors.append([r,r if kind=='squares' else r+1])
            for j in range(d-len(p)+2):
                add([0]*j+p,dict(type=kind,power=j,node_pairs=factors))
    return gens


def exact_simplex(vals,support,sign):
    """Three equality constraints, exact primal simplex with Bland's rule."""
    target=fmpq_mat([[0],[0],[sign]])
    def matrix(S): return fmpq_mat([[vals[j][k] for j in S] for k in (1,2,3)])
    good=False
    if len(support)==3:
        B=matrix(support)
        if B.det(): good=all((B.inv()*target)[i,0]>=0 for i in range(3))
    if not good:
        for S in itertools.combinations(range(min(12,len(vals))),3):
            B=matrix(S)
            if B.det() and all((B.inv()*target)[i,0]>=0 for i in range(3)):
                support=list(S);good=True;break
    assert good
    for step in range(10000):
        B=matrix(support); inv=B.inv(); x=inv*target
        assert all(x[i,0]>=0 for i in range(3))
        dual=fmpq_mat([[vals[j][0] for j in support]])*inv
        reduced=[v[0]-sum((dual[0,i]*v[k] for i,k in enumerate((1,2,3))),fmpq(0)) for v in vals]
        entering=next((j for j,r in enumerate(reduced) if r<0),None)
        if entering is None: return support,step
        direction=inv*fmpq_mat([[vals[entering][k]] for k in (1,2,3)])
        positive=[i for i in range(3) if direction[i,0]>0]
        assert positive, 'Unbounded exact positivity LP would contradict positivity.'
        leaving=min(positive,key=lambda i:(x[i,0]/direction[i,0],support[i]))
        support[leaving]=entering
    raise RuntimeError('Exact simplex iteration cap')


def endpoint(M,gens,sign,lo,hi):
    # Minimize a0 for a7=sign; add nuisance rows and center at known midpoint
    # exactly BEFORE floating conversion to avoid catastrophic cancellation.
    vals=[[dot(row,p) for row in M] for p,_ in gens]
    # Exact row preconditioning is essential: nuisance coefficient rows are
    # nearly dependent in ordinary floating precision.
    pivot=fmpq_mat([[M[k][j] for j in range(3)] for k in (1,2,3)])
    inv=pivot.inv()
    transformed=inv*fmpq_mat([[v[k] for v in vals] for k in (1,2,3)])
    rhs=inv*fmpq_mat([[0],[0],[sign]])
    rhs_scale=max(abs(rhs[i,0]) for i in range(3))
    costs=[v[0]-sum((M[0][i]*transformed[i,j] for i in range(3)),fmpq(0))
           for j,v in enumerate(vals)]
    # Per-column scaling bounds all input entries, then row equilibration.
    raw=[[transformed[i,j] for j in range(len(vals))] for i in range(3)]+[costs]
    row_scale=[max(abs(x) for x in row) or fmpq(1) for row in raw]
    col_scale=[max(abs(raw[i][j]/row_scale[i]) for i in range(4)) for j in range(len(vals))]
    mat=np.array([[float(F(str(raw[i][j]/row_scale[i]/col_scale[j])))
                   for j in range(len(vals))] for i in range(4)])
    # Normalize target a7 to the same scale as its row; solve homogeneous ray.
    target=[float(F(str(rhs[i,0]/rhs_scale/row_scale[i]))) for i in range(3)]
    # Scale the whole right hand side; this does not change the optimizing ray.
    target_scale=max(map(abs,target))
    target=[x/target_scale for x in target]
    result=linprog(mat[3],A_eq=mat[:3],b_eq=target,bounds=(0,None),
                   method='highs',options={'dual_feasibility_tolerance':1e-9,
                                           'primal_feasibility_tolerance':1e-9})
    support=[] if not result.success else [j for j,x in enumerate(result.x) if x>1e-8]
    support,exact_steps=exact_simplex(vals,support,sign)
    # Exact reconstruction is valid even for a numerically inaccurate proposal.
    if len(support)==3:
        weights=cross([vals[j][1] for j in support],[vals[j][2] for j in support])
    elif len(support)==2:
        row=1 if any(vals[j][1] for j in support) else 2
        weights=[vals[support[1]][row],-vals[support[0]][row]]
    else: weights=[fmpq(1)]
    if all(x<0 for x in weights): weights=[-x for x in weights]
    assert all(x>0 for x in weights)
    v=[sum((a*vals[j][k] for j,a in zip(support,weights)),fmpq(0)) for k in range(4)]
    assert v[1]==v[2]==0 and sign*v[3]>0
    rational_endpoint=-v[0]/v[3]
    # Exact LP dual: a0 + d3*a3 + d5*a5 + endpoint*a7 >=0 on all rays.
    # If rank3, solve the two auxiliary dual variables from two active rays.
    dual_verified=False; dual=None; slacks=[]
    for i,j in itertools.combinations(support,2):
        B=fmpq_mat([[vals[k][1],vals[k][2]] for k in (i,j)])
        if not B.det(): continue
        dual=B.inv()*fmpq_mat([[-vals[k][0]-rational_endpoint*vals[k][3]] for k in (i,j)])
        slacks=[v[0]+dual[0,0]*v[1]+dual[1,0]*v[2]+rational_endpoint*v[3] for v in vals]
        dual_verified=all(s>=0 for s in slacks)
        break
    polynomial=[sum((a*gens[j][0][k] for j,a in zip(support,weights)),fmpq(0)) for k in range(len(M[0]))]
    pair,scale=primitive([v[0],v[3]])
    return dict(endpoint=str(rational_endpoint),sign=sign,
        support=support,weights=list(map(str,weights)),
        generator_tags=[gens[j][1] for j in support],
        polynomial=list(map(str,polynomial)),output=list(map(str,v)),
        primitive_output=pair,primitive_scale=str(scale),
        dual_verified=dual_verified,
        dual_auxiliary=None if dual is None else [str(dual[0,0]),str(dual[1,0])],
        negative_dual_slacks=sum(s<0 for s in slacks),exact_simplex_steps=exact_steps)


def run(n,w,kind,old):
    M=shifted_map(n,w); gens=generators(n,w+3,kind)
    lo=fmpq(old['lower_bound']); hi=fmpq(old['upper_bound'])
    lower=endpoint(M,gens,1,lo,hi); upper=endpoint(M,gens,-1,lo,hi)
    newlo=fmpq(lower['endpoint']); newhi=fmpq(upper['endpoint'])
    assert lo<=newlo<newhi<=hi
    opt=optimize(F(str(newlo)),F(str(newhi)))
    oldopt=optimize(F(str(lo)),F(str(hi)))
    with ctx.workprec(256):
        out=dict(n=n,w=w,kind=kind,generator_count=len(gens),
            lower=lower,upper=upper,
            width_ratio=str((newhi-newlo)/(hi-lo)),
            width_improvement=(arb(hi-lo)/arb(newhi-newlo)).str(14),
            log_width_per_n=(arb(newhi-newlo).log()/n).str(14),
            optimal_pair=list(opt['pair']),epsilon=str(opt['epsilon']),
            epsilon_arb=arb(fmpq(str(opt['epsilon']))).str(16),
            old_epsilon=str(oldopt['epsilon']),
            epsilon_improvement=(arb(fmpq(str(oldopt['epsilon'])))/arb(fmpq(str(opt['epsilon'])))).str(14),
            minimum_internal_denominator=str(opt['Q']))
    return out


def main():
    folder=Path(__file__).parent
    oldrows=json.loads((folder/'positive_head_cone.json').read_text())['rows']
    rows=[]; cubics=[]
    for n in (2,4,6,8,12,16,24,32,48,64):
        cubics.append(cubic_certificate(n))
        print('cubic equal cones',n,flush=True)
    for n,w in ((4,2),(4,4),(8,2),(8,4),(8,8),(16,4),(16,8),(24,8)):
        old=next(r for r in oldrows if r['n']==n and r['w']==w)
        for kind in ('monomial','squares','pairs'):
            row=run(n,w,kind,old);rows.append(row)
            print(json.dumps({k:row[k] for k in ('n','w','kind','generator_count','width_improvement','epsilon_improvement')}),
                  'dual',row['lower']['dual_verified'],row['upper']['dual_verified'],flush=True)
        (folder/'discrete_positive_cone_probe.json').write_text(json.dumps(
            dict(scope='Exact finite positivity certificates and finite cone optima when dual_verified; no asymptotic irrationality claim.',
                 cubic_certificates=cubics,rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__': main()
