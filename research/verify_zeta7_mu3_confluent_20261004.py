"""Independent polynomial-inverse and derivative-recurrence audit."""
import hashlib,json,math,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat as Mat,arb,ctx

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def add(out,s,e,c):
    out.setdefault(s,{})[e]=out.setdefault(s,{}).get(e,Q(0))+c


def derivative_rows(j):
    # Derive coefficients, including Hurwitz zeta derivatives, rather than
    # importing the producer's five hard-coded pole rows.
    symbolic={0:{-1:Q(-1,2),0:Q(-1,2)},3:{2:Q(1)}}
    rows=[]
    for m in range(1,6):
        vals={s:sum((c*Q(j)**e for e,c in terms.items()),Q(0)) for s,terms in symbolic.items()}
        row=[vals.get(s,Q(0)) for s in (0,3,4,5,6,7)]
        row[0]-=sum((row[s-2]*sum((Q(1,k**s) for k in range(1,j)),Q(0)) for s in range(3,8)),Q(0))
        rows.append(row)
        following={}
        for s,terms in symbolic.items():
            for e,c in terms.items():
                if e:add(following,s,e-2,-c*e/(2*m))
                if s:add(following,s+1,e-1,c*s/(2*m))
        symbolic=following
    return rows


def moments(K,h,W):
    factors=[Poly([j*j,1]) for j in range(1,K+1)]
    D=Poly([1])
    for f in factors:D*=f**5
    local=[]
    for j,f in enumerate(factors,1):
        g,inv,_=(D//(f**5)).xgcd(f**5);assert g==1
        local.append((j,f,inv,derivative_rows(j)))
    answer=[];P=W
    for s in range(2*h-1):
        quotient=P//D
        value=[sum((v*Q((-1)**e)*Q.bernoulli(2*e+2)*(2*e+3)/2 for e,v in enumerate(quotient)),Q(0))]+[Q(0)]*5
        reconstructed=quotient*D
        for j,f,inv,Js in local:
            part=(P*inv)%(f**5);der=part
            jets=[]
            for k in range(5):jets.append(der(-j*j)/math.factorial(k));der=der.derivative()
            for m in range(1,6):
                c=jets[5-m];reconstructed+=c*(D//(f**m))
                for a in range(6):value[a]+=c*Js[m-1][a]
        assert reconstructed==P
        assert value[1]==-((P*Poly([0,1]))%D)[D.degree()-1]
        answer.append(value);P*=Poly([0,1])
    return answer


def main():
    source=(ROOT/'zeta7_mu3_confluent_20261004.json').read_bytes();data=json.loads(source)
    rows=[];points=0;equalities=0
    for r in data['records']:
        if r.get('finite_positive_orientation',0)==0:continue
        K,h=r['K'],r['h'];W=Poly([Q(v) for v in r['chosen_numerator']])
        seq=moments(K,h,W)
        assert all(v[a]==0 for v in seq for a in (1,2,3,4));equalities+=4*len(seq)
        A=Mat([[seq[i+j][0] for j in range(h)] for i in range(h)])
        B=Mat([[seq[i+j][5] for j in range(h)] for i in range(h)])
        primitive=Poly([Q(v) for v in r['primitive_coefficients']]);poly=primitive*Q(r['content'])
        assert math.gcd(*(int(v) for v in primitive))==1 and all(v.denominator==1 for v in primitive)
        assert B.rank()==r['target_rank'] and primitive.degree()==r['determinant_degree']
        for x in range(h+1):assert (A+x*B).det()==poly(x);points+=1
        ctx.prec=max(abs(int(v)).bit_length() for v in primitive)+6000;z=arb(7).zeta()
        value=arb(0)
        for v in reversed(list(primitive)):value=value*z+arb(v)
        assert value>0 and value.log().overlaps(arb(r['log_primitive_interval']))
        G=[[arb(A[i,j])+z*arb(B[i,j]) for j in range(h)] for i in range(h)]
        for k in range(h):
            p=G[k][k];assert p>0
            for i in range(k+1,h):
                for j in range(i,h):G[i][j]-=G[i][k]*G[j][k]/p;G[j][i]=G[i][j]
        rows.append(dict(K=K,h=h,moments=len(seq),low_zeta_equalities=4*len(seq),
                        polynomial_identity_points=h+1,positive_target_pivots=h))
    out=dict(status='independent_inverse_recurrence_and_arb_checks_passed',source_sha256=hashlib.sha256(source).hexdigest(),
             records=rows,total_nuisance_equalities=equalities,total_exact_determinants=points,
             scope='Six finite definite candidates; no infinite-scale assertion. Failed K16 case not audited here.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(len(rows),equalities,points,flush=True)


if __name__=='__main__':main()
