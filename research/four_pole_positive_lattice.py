"""Exact output lattices and coefficient-positive derivative cones.

SciPy proposes LP faces; every accepted endpoint has exact primal/dual checks.
The derivative certificate is sufficient, not necessary for half-line positivity.
"""
import json, math, itertools, sys
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
from flint import fmpq as Q, fmpq_mat, fmpz_mat, fmpq_poly, arb, ctx
from critical_lift_probe import output_map, harmonic_table, primitive
from joint_positive_module import saturated_kernel, rows_of
from farey_cone_optimizer import optimize

sys.set_int_max_str_digits(0)


def dot(a,b):return sum((x*y for x,y in zip(a,b)),Q(0))


def maps(n,m,s):
    assert 2*m<=4*n+2
    _,local=output_map(n,4,tuple(range(0,2*m+1,2)))
    H=harmonic_table(n,s);r=s-4;norm=math.factorial(n)**4
    C2=[];a=[];b=[]
    for col in range(m+1):
        C2.append(norm*sum((local[k][col][2] for k in range(n+1)),Q(0)))
        b.append(norm*math.comb(s-1,3)*sum((local[k][col][4] for k in range(n+1)),Q(0)))
        a.append(-norm*sum((math.comb(j+r-1,r)*local[k][col][j]*H[k][j+r]
                           for k in range(n+1) for j in range(1,5)),Q(0)))
    # u=t-1. Positive coefficients certify the derivative on all t>=1.
    q=fmpq_poly([1])
    for k in range(n+1):q*=fmpq_poly([k+1,1])
    x=fmpq_poly([n+2,2]);polys=[]
    for j in range(m+1):
        T=x**(2*j)
        for ell in range(r):T=((4+ell)*q.derivative()*T-q*T.derivative())/(ell+1)
        polys.append(T)
    B=[[p[i] for p in polys] for i in range(max(len(p) for p in polys))]
    return C2,a,b,B


def lattice(C2,a,b,n,s):
    constraint,_=primitive(C2)
    K,U=saturated_kernel([constraint])
    D=math.lcm(*range(1,n+1))**s
    M=fmpz_mat([[int(x*D) for x in line] for line in (a,b)])
    assert all((x*D).denominator==1 for line in (a,b) for x in line)
    G=M*K
    rank=G.rank()
    H,V=G.transpose().hnf(transform=True)
    g1=math.gcd(*(int(x) for x in G))
    g2=math.gcd(*(int(G[0,i]*G[1,j]-G[0,j]*G[1,i]) for i,j in itertools.combinations(range(G.ncols()),2)))
    return dict(constraint=list(map(str,constraint)),saturated_kernel=rows_of(K),
                kernel_unimodular=rows_of(U),clearing_scale=str(D),target_map=rows_of(G),
                image_hnf=rows_of(H),image_unimodular=rows_of(V),rank=rank,
                smith=list(map(str,[g1,g2//g1])) if rank==2 else [str(g1)])


def coordinates(C2,a,b):
    m=len(a)-1
    E=[]
    for j in range(1,m+1):
        e=[Q(0)]*(m+1);e[j]=1;e[0]=-C2[j]/C2[0];E.append(e)
    T=[x/dot(b,E[0]) for x in E[0]]
    V=[[e[k]-dot(b,e)*T[k] for k in range(m+1)] for e in E[1:]]
    pivot=next(i for i,v in enumerate(V) if dot(a,v))
    A=[x/dot(a,V[pivot]) for x in V[pivot]]
    S=[T[k]-dot(a,T)*A[k] for k in range(m+1)]
    Z=[[v[k]-dot(a,v)*A[k] for k in range(m+1)] for i,v in enumerate(V) if i!=pivot]
    basis=[A,S]+Z
    for i,p in enumerate(basis):
        assert dot(C2,p)==0 and dot(a,p)==(i==0) and dot(b,p)==(i==1)
    return basis


def dual_feasible_basis(cons):
    """Rational phase I: find lambda>=0 with sum lambda_i*cons_i=e_0."""
    count=len(cons);dim=len(cons[0])
    columns=cons+[[Q(int(i==j)) for i in range(dim)] for j in range(dim)]
    A=fmpq_mat([[col[i] for col in columns] for i in range(dim)])
    target=fmpq_mat([[int(i==0)] for i in range(dim)])
    basis=list(range(count,count+dim))
    costs=[Q(0)]*count+[Q(-1)]*dim
    for iteration in range(10000):
        M=fmpq_mat([[A[i,j] for j in basis] for i in range(dim)])
        inv=M.inv();x=list(inv*target);table=inv*A
        reduced=[costs[j]-sum((costs[basis[i]]*table[i,j] for i in range(dim)),Q(0)) for j in range(count+dim)]
        entering=next((j for j in range(count+dim) if j not in basis and reduced[j]>0),None)
        if entering is None:
            assert sum((costs[basis[i]]*x[i] for i in range(dim)),Q(0))==0
            for i in range(dim):
                if basis[i]<count:continue
                assert x[i]==0
                M=fmpq_mat([[A[k,j] for j in basis] for k in range(dim)]);table=M.inv()*A
                swap=next(j for j in range(count) if j not in basis and table[i,j])
                basis[i]=swap
            return basis,iteration
        leaving=min((i for i in range(dim) if table[i,entering]>0),
                    key=lambda i:(x[i]/table[i,entering],basis[i]))
        basis[leaving]=entering
    raise RuntimeError('rational phase I pivot limit')


def endpoint(B,basis,sign):
    # Coordinates are output constant a, target coefficient b, then zero-output directions.
    coeff=[[dot(line,p) for p in basis] for line in B]
    cons=[[row[0]]+row[2:] for row in coeff]
    rhs=[-sign*row[1] for row in coeff]
    keep=[i for i in range(len(cons)) if any(cons[i]) or rhs[i]]
    A=np.array([[float(x) for x in cons[i]] for i in keep]);v=np.array([float(rhs[i]) for i in keep])
    scales=np.maximum(np.max(np.abs(A),axis=1),np.abs(v));scales[scales==0]=1
    A/=scales[:,None];v/=scales
    colscale=np.max(np.abs(A),axis=0);colscale[colscale==0]=1
    A/=colscale
    objective=np.zeros(A.shape[1]);objective[0]=1/colscale[0]
    lp=linprog(objective,A_ub=-A,b_ub=-v,bounds=[(None,None)]*len(objective),method='highs',
               options={'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    dim=len(objective)
    active=[]
    if lp.success:
        active=[keep[i] for i in range(len(keep)) if abs(lp.ineqlin.residual[i])<1e-7]
        active.sort(key=lambda k:abs(lp.ineqlin.marginals[keep.index(k)]),reverse=True)
    def repair(chosen):
        # Exact simplex on the dual. Bland's rule handles degeneracy. A dual
        # feasible basis may have an infeasible primal vertex after float search.
        chosen=list(chosen)
        for iteration in range(5000):
            M=fmpq_mat([cons[i] for i in chosen]);inv=M.inv()
            sol=list(inv*fmpq_mat([[rhs[i]] for i in chosen]))
            dual=list(inv.transpose()*fmpq_mat([[int(i==0)] for i in range(dim)]))
            assert all(x>=0 for x in dual)
            entering=next((i for i in range(len(cons)) if dot(cons[i],sol)<rhs[i]),None)
            if entering is None:return chosen,sol,dual,iteration
            alpha=list(fmpq_mat([cons[entering]])*inv)
            candidates=[j for j in range(dim) if alpha[j]>0]
            assert candidates,'infeasible primal certificate'
            leaving=min(candidates,key=lambda j:(dual[j]/alpha[j],chosen[j]))
            chosen[leaving]=entering
        return None
    phase1=[0]
    def candidates():
        yield from itertools.islice(itertools.combinations(active,dim),3000)
        chosen,phase1[0]=dual_feasible_basis(cons)
        yield chosen
    for chosen in candidates():
        M=fmpq_mat([cons[i] for i in chosen])
        if not M.det():continue
        unit=fmpq_mat([[int(i==0)] for i in range(dim)])
        dual=list(M.transpose().inv()*unit)
        if any(x<0 for x in dual):continue
        fixed=repair(chosen)
        if fixed is None:continue
        chosen,sol,dual,pivots=fixed
        assert sol[0]==sum((x*rhs[i] for x,i in zip(dual,chosen)),Q(0))
        coordinates=[sol[0],Q(sign)]+sol[1:]
        p=[sum((coordinates[i]*basis[i][j] for i in range(len(basis))),Q(0)) for j in range(len(basis[0]))]
        positive=[dot(line,p) for line in B]
        assert all(x>=0 for x in positive) and any(positive)
        pair,scale=primitive([sol[0],Q(sign)])
        return dict(status='certified',sign=sign,constant=str(sol[0]),endpoint=str(-sol[0]/sign),exact_pivots=pivots,phase1_pivots=phase1[0],
                    polynomial=list(map(str,p)),active=list(chosen),dual=list(map(str,dual)),
                    coordinate_solution=list(map(str,coordinates)),primitive_pair=list(map(str,pair)),
                    primitive_scale=str(scale),derivative_coefficients=list(map(str,positive)))
    return dict(status='uncertified_numeric_candidate',active=active,lp_value=float(lp.fun))


def probe(n,m,s):
    C2,a,b,B=maps(n,m,s)
    result=dict(n=n,m=m,s=s,map=list(map(lambda row:list(map(str,row)),[C2,a,b])),
                lattice=lattice(C2,a,b,n,s))
    basis=coordinates(C2,a,b);result['coordinate_basis']=[list(map(str,p)) for p in basis]
    edges=[endpoint(B,basis,sign) for sign in (1,-1)];result['edges']=edges
    if all(e['status']=='certified' for e in edges):
        lo,hi=map(lambda e:F(e['endpoint']),edges)
        assert lo<hi
        if lo<0:return result
        opt=optimize(lo,hi);pair=opt['pair'];epsilon=opt['epsilon']
        # Positive combination of endpoint kernels realizes the chosen output exactly.
        weight0=(Q(pair[0])+Q(str(hi))*pair[1])/Q(str(hi-lo))
        weight1=(Q(pair[0])+Q(str(lo))*pair[1])/Q(str(hi-lo))
        assert weight0>=0 and weight1>=0
        p=[weight0*Q(edges[0]['polynomial'][j])+weight1*Q(edges[1]['polynomial'][j]) for j in range(m+1)]
        assert dot(C2,p)==0 and dot(a,p)==pair[0] and dot(b,p)==pair[1]
        ints,input_scale=primitive(p)
        with ctx.workprec(max(abs(x).bit_length() for x in pair)+512):
            value=arb(pair[0])+arb(pair[1])*arb(s).zeta()
            assert value>0 and value<arb(Q(str(epsilon)))
            result['optimized']=dict(lower=str(lo),upper=str(hi),width=str(hi-lo),
                pair=list(map(str,pair)),epsilon=str(epsilon),value=value.str(30),
                farey_left=list(map(str,opt['left'])),farey_right=list(map(str,opt['right'])),
                minimum_internal_denominator=str(opt['Q']),
                edge_uniform_bounds=[str(Q(str(hi-lo))*abs(int(e['primitive_pair'][1]))) for e in edges],
                positive_weights=list(map(str,[weight0,weight1])),integer_polynomial=list(map(str,ints)),
                output_scale=str(input_scale),input_height_bits=max(abs(x).bit_length() for x in ints),
                log_epsilon_per_n=(arb(Q(str(epsilon))).log()/n).str(20))
    return result


def main():
    rows=[]
    cases=[(n,m,7) for n in (2,4,8,12) for m in (2,3,4,6,8) if m<=2*n+1]
    cases += [(8,m,s) for s in (5,9) for m in (2,4,6,8)]
    cases += [(n,m,7) for n in (3,5) for m in (2,4)]
    cases += [(n,m,7) for n in (16,24,32) for m in (2,4,8,12)]
    cases += [(16,8,s) for s in (5,9)]
    for n,m,s in cases:
        row=probe(n,m,s);rows.append(row)
        print(n,m,s,[e['status'] for e in row['edges']],row.get('optimized',{}).get('pair'),flush=True)
        Path(__file__).with_suffix('.json').write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
