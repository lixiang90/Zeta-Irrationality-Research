"""Joint root modules: saturated kernels, congruence index and positive lifts.

Every matrix and certificate is exact. No zeta numerical value is used.
"""
import itertools
import json
import math
import sys
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpz_mat, arb, ctx
from growing_positive_moment import shifted_map, dot
from critical_lift_probe import primitive

sys.set_int_max_str_digits(0)


def saturated_kernel(rows):
    A=fmpz_mat(rows);H,U=A.transpose().hnf(transform=True);rank=A.rank()
    assert H==U*A.transpose() and abs(int(U.det()))==1
    assert all(H[i,j]==0 for i in range(rank,H.nrows()) for j in range(H.ncols()))
    K=fmpz_mat([[U[j,i] for j in range(rank,U.nrows())] for i in range(U.ncols())])
    assert not any(A*K)
    return K,U


def rows_of(M):return [[int(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())]


def prime_split(value,limit):
    remain=abs(value);parts=[]
    for p in range(2,limit+1):
        if any(p%j==0 for j in range(2,math.isqrt(p)+1)):continue
        e=0
        while remain%p==0:remain//=p;e+=1
        if e:parts.append([p,e])
    return parts,remain


def joint_matrix(row):
    n,w=row['n'],row['w'];M=shifted_map(n,w);d=w+3
    columns=[];scales=[];polys=[]
    for name in ('lower','upper'):
        H=list(map(fmpq,row[name]['H']))
        for j in range(3):
            P=[fmpq(0)]*j+H
            col,scale=primitive([dot(line,P) for line in M]);assert scale>0
            columns.append(col);scales.append(scale)
            polys.append([p*scale for p in P]+[fmpq(0)]*(d+1-len(P)))
    C=fmpz_mat([[columns[j][i] for j in range(6)] for i in range(4)])
    F=fmpq_mat([[polys[j][i] for j in range(6)] for i in range(d+1)])
    return C,F,scales


def endpoint_lift(row,scales,pair):
    endpoints=[row[name]['primitive_output'] for name in ('lower','upper')]
    B=fmpq_mat([[v[k] for v in endpoints] for k in range(2)])
    alpha=B.inv()*fmpq_mat([[pair[0]],[pair[1]]])
    assert all(x>=0 for x in alpha)
    c=[]
    for block,name in enumerate(('lower','upper')):
        e=row[name]
        q=list(map(fmpq,e['quadratic']));scale=fmpq(e['primitive_scale'])
        c.extend(alpha[block,0]*scale*q[j]/scales[3*block+j] for j in range(3))
    return c


def positive_lp(C,pair):
    """Exact minimum sum coefficients for fixed integer target; all 4-column bases."""
    target=fmpq_mat([[pair[0]],[0],[0],[pair[1]]]);best=None;cost=None
    for support in itertools.combinations(range(6),4):
        B=fmpq_mat([[C[i,j] for j in support] for i in range(4)])
        if not B.det():continue
        x=B.inv()*target
        if any(t<0 for t in x):continue
        total=sum(x,fmpq(0))
        if best is None or total<cost:
            c=[fmpq(0)]*6
            for j,t in zip(support,x):c[j]=t
            best=c;cost=total
    assert best is not None
    # LP dual may be degenerate. Find a 4-column primal basis with valid dual.
    dual=None
    active=[j for j,x in enumerate(best) if x>0]
    for support in itertools.combinations(range(6),4):
        if not all(j in support for j in active):continue
        B=fmpq_mat([[C[i,j] for j in support] for i in range(4)])
        if not B.det():continue
        lam=fmpq_mat([[1,1,1,1]])*B.inv()
        if all(sum((lam[0,i]*C[i,j] for i in range(4)),fmpq(0))<=1 for j in range(6)):
            assert (lam*target)[0,0]==cost;dual=[lam[0,i] for i in range(4)];break
    assert dual is not None
    return best,cost,dual


def probe(row):
    n,w=row['n'],row['w'];C,F,scales=joint_matrix(row)
    assert C.rank()==4
    K,U=saturated_kernel(rows_of(C))
    nuisance=[[int(C[i,j]) for j in range(6)] for i in (1,2)]
    L,V=saturated_kernel(nuisance)
    assert L.ncols()==4 and K.ncols()==2
    CL=C*L
    G=fmpz_mat([[CL[i,j] for j in range(CL.ncols())] for i in (0,3)])
    g1=math.gcd(*(int(x) for x in G))
    g2=math.gcd(*(int(G[0,i]*G[1,j]-G[0,j]*G[1,i]) for i,j in itertools.combinations(range(4),2)))
    smith=[g1,g2//g1];assert smith[1]%smith[0]==0
    _,rough=prime_split(smith[1],8*n)
    # Exact polynomial dimension separates duplicate representations from true telescoping kernels.
    polynomial_rank=F.rank()
    target=row['optimal_pair']
    old_lift=endpoint_lift(row,scales,target)
    new_lift,cost,dual=positive_lp(C,target)
    assert C*fmpq_mat([[x] for x in new_lift])==fmpq_mat([[target[0]],[0],[0],[target[1]]])
    lift_den=math.lcm(*(int(x.denominator) for x in new_lift))
    integer_lift=[int(x*lift_den) for x in new_lift]
    assert math.gcd(*integer_lift)==1
    lifted_output=C*fmpz_mat([[x] for x in integer_lift])
    content=math.gcd(*(int(x) for x in lifted_output));assert content==lift_den
    # A family with arbitrary extra prime power content and fixed primitive output.
    fixed=endpoint_lift(row,scales,[-1,1]);assert all(x>0 for x in fixed)
    fixed_den=math.lcm(*(int(x.denominator) for x in fixed))
    c0=[int(x*fixed_den) for x in fixed]
    kernel=[int(K[i,0]) for i in range(6)];assert math.gcd(*kernel)==1
    multiplier=max(1,max((-kernel[i]+c0[i]-1)//c0[i] for i in range(6)))
    c0=[multiplier*x for x in c0];D=multiplier*fixed_den
    assert C*fmpz_mat([[x] for x in c0])==fmpz_mat([[-D],[0],[0],[D]])
    examples=[]
    for modulus in (101,101**2,1009,1009**2):
        c=[modulus*a+k for a,k in zip(c0,kernel)];assert all(x>0 for x in c)
        input_content=math.gcd(*c)
        assert math.gcd(input_content,modulus)==1
        c=[x//input_content for x in c]
        out=[int(x) for x in C*fmpz_mat([[x] for x in c])]
        gcd=math.gcd(*out);assert gcd%modulus==0
        assert [x//gcd for x in out]==[-1,0,0,1]
        examples.append(dict(modulus=modulus,input_content_before_normalization=str(input_content),
            primitive_input=list(map(str,c)),output_content=str(gcd),primitive_output=[-1,0,0,1]))
    with ctx.workprec(256):
        return dict(n=n,w=w,matrix=rows_of(C),column_scales=list(map(str,scales)),
            polynomial_rank=polynomial_rank,representation_kernel_dimension=6-polynomial_rank,
            genuine_zero_output_polynomial_dimension=polynomial_rank-4,
            saturated_output_kernel=rows_of(K),output_hnf_transform=rows_of(U),
            saturated_nuisance_kernel=rows_of(L),nuisance_hnf_transform=rows_of(V),
            eliminated_target_map=rows_of(G),target_smith_invariants=list(map(str,smith)),
            target_largest_smith_rough_part=str(rough),prime_cutoff=8*n,
            congruence_indices=[dict(modulus=m,index=str(math.prod(m//math.gcd(m,s) for s in smith)))
                                for m in (2,3,5,101,101**2,1009,1009**2)],
            target_pair=target,epsilon=row['epsilon'],
            old_positive_lift=list(map(str,old_lift)),minimum_l1_lift=list(map(str,new_lift)),
            minimum_l1_cost=str(cost),l1_dual=list(map(str,dual)),
            coefficient_cost_improvement=(arb(sum(old_lift,fmpq(0)))/arb(cost)).str(18),
            integer_lift=list(map(str,integer_lift)),integer_lift_output_content=str(content),
            fixed_output_family=dict(base=list(map(str,c0)),base_output_multiplier=str(D),
                kernel=list(map(str,kernel)),examples=examples))


def main():
    folder=Path(__file__).parent
    source=json.loads((folder/'growing_positive_moment.json').read_text())['rows']
    other=json.loads((folder/'growing_positive_ratio_scan.json').read_text())['rows']
    source+=[r for r in other if r['n']==24 and r['w']==48]
    rows=[]
    for r in source:
        result=probe(r);rows.append(result)
        print(r['n'],r['w'],'poly rank',result['polynomial_rank'],
            'target rough',result['target_largest_smith_rough_part'],
            'lift improvement',result['coefficient_cost_improvement'],flush=True)
        (folder/'joint_positive_module.json').write_text(json.dumps(dict(
            scope='Exact joint-module kernels, lattice indices, positive LPs and fixed-output high-content counterexamples; no irrationality claim.',rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
