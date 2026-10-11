"""Saturated full numerator lattices for mu5 triple-pole pure zeta7 pencils.

The HNF transform proves saturation; LLL and bounded combinations seek
finite truncated-positive candidates. Every accepted candidate is evaluated
after its complete polynomial content is removed.
"""
import hashlib, itertools, json, math, random, sys, time
from fractions import Fraction
from pathlib import Path
from flint import fmpq as Q, fmpz_mat as ZM, fmpq_mat as QM, fmpq_poly as Poly, arb, ctx
from zeta7_confluent_gram_probe import coefficient_sequences

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent
OUT=Path(__file__).with_suffix('.json')

def primitive_vector(v):
    g=math.gcd(*(abs(int(x)) for x in v))
    if not g:return None
    v=tuple(int(x)//g for x in v)
    if next(x for x in reversed(v) if x)<0:v=tuple(-x for x in v)
    return v

def integer_constraints(seqs,h,d):
    rows=[]
    for z in (1,2):
        for s in range(2*h-1):
            row=[seqs[z][s+e] for e in range(d+1)]
            denominator=math.lcm(*(int(c.q) for c in row))
            integers=[int(c*denominator) for c in row]
            g=math.gcd(*(abs(c) for c in integers))
            if g:integers=[c//g for c in integers]
            rows.append(integers)
    return ZM(rows)

def saturated_kernel(M):
    H,U=M.transpose().hnf(transform=True)
    assert U*M.transpose()==H and abs(U.det())==1
    rank=M.rank();zero_rows=[i for i in range(H.nrows()) if all(not H[i,j] for j in range(H.ncols()))]
    assert len(zero_rows)==M.ncols()-rank
    B=ZM([[U[i,j] for j in range(U.ncols())] for i in zero_rows])
    assert B*M.transpose()==ZM(B.nrows(),M.nrows())
    C,T=B.lll(transform=True)
    assert T*B==C and abs(T.det())==1
    return H,U,B,C,T

def entries(seqs,h,v):
    return [[sum((seqs[z][s+e]*c for e,c in enumerate(v)),Q(0)) for s in range(2*h-1)] for z in (0,3)]

def signature(aa,bb,h):
    z=arb(7).zeta();M=[[arb(aa[i+j])+z*arb(bb[i+j]) for j in range(h)] for i in range(h)]
    signs=[]
    for j in range(h):
        pivot=M[j][j]
        if pivot.contains(0):return None
        signs.append(1 if pivot>0 else -1)
        if len(signs)>1 and signs[-1]!=signs[0]:return signs
        for i in range(j+1,h):
            for k in range(i,h):
                M[k][i]-=M[i][j]*M[k][j]/pivot;M[i][k]=M[k][i]
    return signs

def content(P):return Q(math.gcd(*(int(c.p) for c in P)),math.lcm(*(int(c.q) for c in P)))

def evaluate(K,h,seqs,v,coordinates,origin):
    aa,bb=entries(seqs,h,v);sig=signature(aa,bb,h)
    if sig is None or len(sig)!=h:return None
    orientation=1 if all(s==1 for s in sig) else -1 if all(s==-1 for s in sig) else 0
    if not orientation:return None
    if orientation<0:
        v=tuple(-c for c in v);coordinates=[-c for c in coordinates]
        aa=[-c for c in aa];bb=[-c for c in bb]
    A=QM(h,h,[aa[i+j] for i in range(h) for j in range(h)])
    B=QM(h,h,[bb[i+j] for i in range(h) for j in range(h)])
    if B.det():P=(-(B.inv()*A)).charpoly()*B.det()
    else:
        vals=QM(h+1,1,[(A+x*B).det() for x in range(h+1)])
        V=QM([[Q(x)**e for e in range(h+1)] for x in range(h+1)])
        sol=V.inv()*vals;P=Poly([sol[e,0] for e in range(h+1)])
    ct=content(P);primitive=P/ct
    assert all(c.q==1 for c in primitive) and content(primitive)==1
    value=arb(0);z=arb(7).zeta()
    for c in reversed(list(primitive)):value=value*z+arb(c)
    assert value>0
    return dict(origin=origin,numerator=list(map(str,v)),lattice_coordinates=coordinates,
                numerator_height_bits=max(abs(c).bit_length() for c in v),degree_numerator=max(i for i,c in enumerate(v) if c),
                numerator_coefficients_nonnegative=all(c>=0 for c in v),truncated_gram_positive=True,
                slope_rank=B.rank(),degree_polynomial=P.degree(),content=str(ct),
                primitive_coefficients=list(map(str,primitive)),score_ball=(value.log()/K**2).str(40),
                score=float((value.log()/K**2).mid()),log_det_ball=(value.log()+arb(ct).log()).str(40),
                log_content_ball=arb(ct).log().str(40))

def baselines(K,h):
    rows=[]
    for name in ('zeta7_confluent_annihilator.json','zeta7_confluent_gram_probe.json'):
        for r in json.loads((ROOT/name).read_text(encoding='utf-8'))['records']:
            if (r['K'],r['h'])==(K,h) and r.get('positive_candidate_exact'):
                rows.append(dict(source=name,score=r['normalized_log_primitive'],
                                 numerator_height_bits=max(abs(int(x)).bit_length() for x in r['numerator']),
                                 numerator=r['numerator']))
    return rows

def run(K,h,random_count=256):
    d=3*K-1;seqs=coefficient_sequences(K,d+2*h-2)
    M=integer_constraints(seqs,h,d);H,U,B,C,T=saturated_kernel(M);rank=M.rank();n=C.nrows()
    vectors=[[int(C[i,j]) for j in range(C.ncols())] for i in range(n)]
    combinations=[]
    for i in range(n):
        co=[0]*n;co[i]=1;combinations.append((co,'LLL_basis'))
    for i in range(n):
        for j in range(i+1,n):
            for sign in (-1,1):
                co=[0]*n;co[i]=1;co[j]=sign;combinations.append((co,'LLL_pair'))
    rng=random.Random(20261004+100*K+h)
    for _ in range(random_count):
        co=[0]*n
        for i in rng.sample(range(n),min(n,rng.randint(2,5))):co[i]=rng.choice((-2,-1,1,2))
        combinations.append((co,'bounded_sparse_LLL_combination'))
    if n==2:
        centers={Fraction(a,b) for a in range(-2,3) for b in (1,2)}
        cq=QM(C);left_inverse=cq.transpose()*(cq*cq.transpose()).inv()
        for base in baselines(K,h):
            vv=[Q(c) for c in base['numerator']]+[Q(0)]*(d+1-len(base['numerator']))
            co=QM(1,d+1,vv)*left_inverse
            assert all(co[0,i].q==1 for i in range(2))
            if co[0,1]:centers.add(Fraction(int(co[0,0]),int(co[0,1])))
        for ratio in sorted(centers):
            for denominator in range(1,33):
                numerator=(ratio.numerator*denominator)//ratio.denominator
                for offset in (-1,0,1):
                    combinations.append(([numerator+offset,denominator],'two_dimensional_projective_neighbor'))
    seen=set();accepted=[];tested=0
    for co,origin in combinations:
        raw=[sum(co[i]*vectors[i][j] for i in range(n)) for j in range(d+1)]
        v=primitive_vector(raw)
        if v is None or v in seen:continue
        seen.add(v);tested+=1
        # Adjust coordinates for the primitive orientation exactly.
        g=math.gcd(*(abs(x) for x in raw));orientation=1 if raw==[g*x for x in v] else -1
        if any(x%g for x in co):
            # Primitive division stays in the saturated lattice; recover coordinates.
            # Solve C^T z = v using an exact Gram left inverse.
            cq=QM(C);vq=QM(1,d+1,[Q(x) for x in v]);sol=vq*cq.transpose()*(cq*cq.transpose()).inv()
            assert all(sol[0,i].q==1 for i in range(n));coords=[int(sol[0,i]) for i in range(n)]
        else:coords=[orientation*x//g for x in co]
        assert all(sum(coords[i]*vectors[i][j] for i in range(n))==v[j] for j in range(d+1))
        r=evaluate(K,h,seqs,v,coords,origin)
        if r is not None:accepted.append(r)
    accepted.sort(key=lambda r:r['score'])
    result=dict(K=K,h=h,degree_limit=d,constraint_rank=rank,lattice_rank=n,
                saturated_lattice_proof='Zero rows of U in U M^T=H, det U=+-1; LLL transform determinant +-1.',
                integer_constraint_matrix=[[str(M[i,j]) for j in range(M.ncols())] for i in range(M.nrows())],
                hnf_transform=[[str(U[i,j]) for j in range(U.ncols())] for i in range(U.nrows())],
                hnf_rows=[[str(H[i,j]) for j in range(H.ncols())] for i in range(H.nrows())],
                saturated_basis=[[str(B[i,j]) for j in range(B.ncols())] for i in range(B.nrows())],
                reduced_basis=[[str(C[i,j]) for j in range(C.ncols())] for i in range(C.nrows())],
                lll_transform=[[str(T[i,j]) for j in range(T.ncols())] for i in range(T.nrows())],
                tested_primitive_candidates=tested,positive_candidates=len(accepted),
                positive_coefficient_candidates=sum(r['numerator_coefficients_nonnegative'] for r in accepted),
                baseline=baselines(K,h),best_candidates=accepted[:12])
    print(K,h,'rank',rank,'dim',n,'tested',tested,'positive',len(accepted),'best',accepted[0]['score'] if accepted else None,flush=True)
    return result

def main():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--extend',action='store_true');args=parser.parse_args()
    cases=[(4,2),(4,3),(6,3),(6,4),(8,4),(8,6),(12,6),(12,9),(16,8),(24,12)]
    out=json.loads(OUT.read_text(encoding='utf-8')) if args.extend else dict(
        status='running',scope='Finite saturated numerator lattices and bounded candidate search; no asymptotic theorem.',records=[])
    existing={(r['K'],r['h']) for r in out['records']};out['status']='running'
    with ctx.workprec(16000):
        for K,h in cases:
            if (K,h) in existing:continue
            out['records'].append(run(K,h));OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='finite_lattice_and_arb_checks_passed';OUT.write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__':main()
