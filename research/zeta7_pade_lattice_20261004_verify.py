"""Independent saturated-kernel and primitive-polynomial verification."""
import hashlib, json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as QM, fmpz_mat as ZM, arb, ctx
from verify_zeta7_confluent_independent import independent_entries
from sympy import Poly as SP, Symbol, Rational, oo

sys.set_int_max_str_digits(0)
SOURCE=Path(__file__).with_name('zeta7_pade_lattice_20261004.json')

def content(P):return Q(math.gcd(*(int(c.p) for c in P)),math.lcm(*(int(c.q) for c in P)))

def integer_constraints(values,h,d):
    rows=[]
    for z in (1,2):
        for s in range(2*h-1):
            row=[values[s+e][z] for e in range(d+1)]
            denominator=math.lcm(*(int(c.q) for c in row));v=[int(c*denominator) for c in row]
            g=math.gcd(*(abs(c) for c in v))
            rows.append([c//g for c in v] if g else v)
    return ZM(rows)

def positivity(W):
    t=Symbol('t');p=SP.from_list([Rational(str(c)) for c in reversed(list(W))],t)
    factors=p.sqf_list()[1]
    all_roots=sum(int(f.count_roots(0,oo)) for f,_ in factors)
    odd_roots=sum(int(f.count_roots(0,oo)) for f,m in factors if m%2)
    first=next(c for c in W if c)
    return dict(positive_real_roots_count=all_roots,odd_multiplicity_positive_roots=odd_roots,
                first_nonzero_coefficient_sign=1 if first>0 else -1,
                global_nonnegative_on_halfline=bool(first>0 and odd_roots==0),
                halfline_sign_changes=bool(odd_roots>0))

def explicit_zeta5_basis(K,h,M):
    F=Poly([1])
    for j in range(1,K+1):F*=Poly([j*j,1])**3
    degree=3*K-2*h-2
    assert degree>=0
    A0=Poly([F[i+2] for i in range(F.degree()-1)])
    A1=Poly([F[i+1] for i in range(F.degree())])
    polys=[Poly([0]*e+[1]) for e in range(degree+1)]+[A0,A1]
    E=ZM([[int(p[j]) for j in range(3*K)] for p in polys])
    M5=ZM([[int(M[i,j]) for j in range(M.ncols())] for i in range(2*h-1)])
    assert E*M5.transpose()==ZM(E.nrows(),M5.nrows())
    H,U=M5.transpose().hnf(transform=True);assert abs(U.det())==1
    zero=[i for i in range(H.nrows()) if all(not H[i,j] for j in range(H.ncols()))]
    saturated=ZM([[U[i,j] for j in range(U.ncols())] for i in zero])
    assert E.hnf()==saturated.hnf() and E.rank()==3*K-2*h+1
    return dict(low_degree_limit=degree,explicit_integer_basis_rank=E.nrows(),
                complete_saturated_zeta5_kernel_hnf_matched=True)

def main():
    raw=SOURCE.read_bytes();data=json.loads(raw);assert data['status']=='finite_lattice_and_arb_checks_passed'
    verified=[];entries_count=coefficients_count=direct_count=0
    with ctx.workprec(20000):
        for r in data['records']:
            K,h,d=r['K'],r['h'],r['degree_limit']
            maximum=d+2*h-2;probe_h=(maximum+3)//2
            seqs=independent_entries(K,probe_h,Poly([1]));assert len(seqs)>maximum
            M=integer_constraints(seqs,h,d)
            stored=ZM([[int(c) for c in row] for row in r['integer_constraint_matrix']]);assert M==stored
            coefficients_count+=M.nrows()*M.ncols()
            U=ZM([[int(c) for c in row] for row in r['hnf_transform']])
            H=ZM([[int(c) for c in row] for row in r['hnf_rows']])
            B=ZM([[int(c) for c in row] for row in r['saturated_basis']])
            C=ZM([[int(c) for c in row] for row in r['reduced_basis']])
            T=ZM([[int(c) for c in row] for row in r['lll_transform']])
            assert abs(U.det())==1 and U*M.transpose()==H
            zero=[i for i in range(H.nrows()) if all(not H[i,j] for j in range(H.ncols()))]
            assert len(zero)==r['lattice_rank']==M.ncols()-M.rank()
            assert B==ZM([[U[i,j] for j in range(U.ncols())] for i in zero])
            assert T*B==C and abs(T.det())==1
            assert B*M.transpose()==ZM(B.nrows(),M.nrows())
            checked=[]
            for index,best in enumerate(r['best_candidates'][:3]):
                W=Poly([Q(c) for c in best['numerator']]);coords=best['lattice_coordinates']
                assert all(sum(int(C[i,j])*coords[i] for i in range(C.nrows()))==W[j] for j in range(d+1))
                assert content(W)==1 and all(c.q==1 for c in W)
                values=[[sum((seqs[s+e][z]*W[e] for e in range(W.degree()+1)),Q(0)) for z in range(4)] for s in range(2*h-1)]
                if index==0:assert values==independent_entries(K,h,W)
                assert all(v[1]==v[2]==0 for v in values);entries_count+=len(values)
                A=QM(h,h,[values[i+j][0] for i in range(h) for j in range(h)])
                Bx=QM(h,h,[values[i+j][3] for i in range(h) for j in range(h)])
                primitive=Poly([Q(c) for c in best['primitive_coefficients']]);P=primitive*Q(best['content'])
                assert content(primitive)==1 and all(c.q==1 for c in primitive)
                for x in range(h+1):assert (A+x*Bx).det()==P(x);direct_count+=1
                z=arb(7).zeta();value=arb(0)
                for c in reversed(list(primitive)):value=value*z+arb(c)
                assert value>0 and (value.log()/K**2).overlaps(arb(best['score_ball']))
                G=[[arb(A[i,j])+z*arb(Bx[i,j]) for j in range(h)] for i in range(h)]
                for j in range(h):
                    pivot=G[j][j];assert pivot>0
                    for i in range(j+1,h):
                        for k in range(i,h):G[k][i]-=G[i][j]*G[k][j]/pivot;G[i][k]=G[k][i]
                checked.append(dict(score_ball=best['score_ball'],degree_numerator=W.degree(),numerator_height_bits=best['numerator_height_bits']))
            verified.append(dict(K=K,h=h,constraint_rank=M.rank(),saturated_lattice_rank=C.nrows(),
                                 explicit_zeta5_basis=explicit_zeta5_basis(K,h,M),
                                 best_candidates_verified=checked,best_halfline_positivity=positivity(Poly([Q(c) for c in r['best_candidates'][0]['numerator']]))))
    out=dict(status='independent_hnf_kernel_polynomial_and_arb_checks_passed',source_sha256=hashlib.sha256(raw).hexdigest(),
             records=verified,independent_constraint_coefficients=coefficients_count,
             independent_target_moments=entries_count,direct_exact_determinants=direct_count,
             scope='All saved saturated lattice certificates and top three candidates per lattice are verified. Bounded search counts are producer records.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','source_sha256','independent_constraint_coefficients','independent_target_moments','direct_exact_determinants')},indent=2),flush=True)
    print(json.dumps([(r['K'],r['h'],r['best_halfline_positivity']) for r in verified],indent=2),flush=True)

if __name__=='__main__':main()
