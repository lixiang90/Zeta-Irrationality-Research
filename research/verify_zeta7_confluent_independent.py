"""Independent local polynomial-inverse audit of mu5 triple-pole pencils."""
import hashlib, json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat, arb, ctx

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent

def mu5(e):
    return Q((-1)**e)*Q.bernoulli(2*e+2)*math.prod(range(2*e+3,2*e+6))/24

def harmonic(j,s):return sum((Q(1,k**s) for k in range(1,j+1)),Q(0))

def pole_values(j):
    # Obtained by differentiating J1(j)=j^4 zeta(5,j)-1/(2j)-1/4.
    H5,H6,H7=(harmonic(j-1,s) for s in (5,6,7))
    return [[-j**4*H5-Q(1,2*j)-Q(1,4),Q(j**4),Q(0),Q(0)],
            [2*j*j*H5-Q(5*j**3,2)*H6-Q(1,4*j**3),Q(-2*j*j),Q(5*j**3,2),Q(0)],
            [-H5+Q(35*j,8)*H6-Q(15*j*j,4)*H7-Q(3,16*j**5),Q(1),Q(-35*j,8),Q(15*j*j,4)]]

def independent_entries(K,h,W):
    factors=[Poly([j*j,1]) for j in range(1,K+1)]
    D=Poly([1]);baseD=Poly([1])
    for f in factors:D*=f**3;baseD*=f
    local=[]
    for j,f in enumerate(factors,1):
        E=D//(f**3);g,inv,_=E.xgcd(f**3);assert g==1
        local.append((j,f,inv,pole_values(j)))
    answer=[];P=W
    for s in range(2*h-1):
        quotient=P//D
        values=[sum((c*mu5(e) for e,c in enumerate(quotient)),Q(0)),Q(0),Q(0),Q(0)]
        reconstructed=quotient*D
        for j,f,inv,Js in local:
            part=(P*inv)%(f**3)
            c3=part(-j*j);c2=part.derivative()(-j*j);c1=part.derivative().derivative()(-j*j)/2
            for power,c in enumerate((c1,c2,c3),1):
                reconstructed+=c*(D//(f**power))
                for i in range(4):values[i]+=c*Js[power-1][i]
        assert reconstructed==P
        infinity_coefficient=((P*Poly([0,0,1]))%D)[D.degree()-1]
        assert values[1]==infinity_coefficient
        direct_slope=Q(15,4)*sum((Q(j*j)*P(-j*j)/baseD.derivative()(-j*j)**3 for j in range(1,K+1)),Q(0))
        assert values[3]==direct_slope
        answer.append(values);P*=Poly([0,1])
    return answer

def hermite_S(K):
    D=Poly([1])
    for j in range(1,K+1):D*=Poly([j*j,1])
    M=D**2;S=Poly([0]);dp=D.derivative();dpp=dp.derivative()
    for j in range(1,K+1):
        r=-j*j;factor=Poly([j*j,1])**2;E=M//factor
        g,inv,_=E.xgcd(factor);assert g==1
        a=Q(5*j**3,2)/dp(r)
        b=(-Q(35*j,4)-dpp(r)*a)/(2*dp(r))
        S+=(Poly([a])+b*Poly([j*j,1]))*E*inv
    S%=M;assert S.degree()<2*K
    for j in range(1,K+1):
        r=-j*j
        assert dp(r)*S(r)==Q(5*j**3,2)
        assert dpp(r)*S(r)+2*dp(r)*S.derivative()(r)==-Q(35*j,4)
    return D,S

def hermite_zeta6_checks():
    cases=0;degrees=[]
    for K in (2,4,8):
        D,S=hermite_S(K);M=D**2
        for n in range(3*K+5):
            P=Poly([0]*n+[1])
            direct=independent_entries(K,1,P)[0][2]
            infinity=((P*S)%M)[M.degree()-1]
            assert direct==infinity;cases+=1
        vandermonde=fmpq_mat(2*K,2*K,[Q((-j*j)**s)*(s if derivative else 1)
                     for s in range(2*K) for j in range(1,K+1) for derivative in (False,True)])
        assert vandermonde.rank()==2*K
        degrees.append(dict(K=K,degree_S=S.degree(),confluent_vandermonde_rank=2*K))
    return dict(exact_monomial_cases=cases,interpolant_degrees=degrees)

def content(P):
    return Q(math.gcd(*(int(c.p) for c in P)),math.lcm(*(int(c.q) for c in P)))

def euler_checks():
    for e in range(51):
        mu7=Q((-1)**e)*Q.bernoulli(2*e+2)*math.prod(range(2*e+3,2*e+8))/720
        assert mu7==mu5(e)*Q((2*e+6)*(2*e+7),30)
    for j in range(1,25):
        coefficients=[Q(2,3),Q(7*j*j,15),Q(4*j**4,15)]
        values=[sum((coefficients[k]*pole_values(j)[k][s] for k in range(3)),Q(0)) for s in range(4)]
        assert values==[-j**6*harmonic(j-1,7)-Q(1,2*j)-Q(1,6),Q(0),Q(0),Q(j**6)]
    return dict(exact_monomial_cases=51,exact_simple_pole_cases=24)

def main():
    records=[];detchecks=0;reschecks=0
    with ctx.workprec(16000):
        for filename in ('zeta7_confluent_gram_probe.json','zeta7_confluent_annihilator.json'):
            source=(ROOT/filename).read_bytes();data=json.loads(source)
            selected=[r for r in data['records'] if r.get('positive_candidate_exact') and
                      ((r['K'],r['h']) in ((4,2),(8,4)) or 'annihilator' in filename)]
            for row in selected:
                K,h=row['K'],row['h'];W=Poly([Q(c) for c in row['numerator']])
                coefficient_nonnegative=all(c>=0 for c in W)
                if row.get('status')=='finite_truncated_positive_exact_and_arb_checks_passed':
                    assert not coefficient_nonnegative
                else:
                    assert coefficient_nonnegative
                values=independent_entries(K,h,W)
                assert all(v[1]==v[2]==0 for v in values)
                baseD,S=hermite_S(K);remainder=(W*S)%(baseD**2)
                assert remainder.degree()<=2*K-2*h
                reschecks+=len(values)
                A=fmpq_mat(h,h,[values[i+j][0] for i in range(h) for j in range(h)])
                B=fmpq_mat(h,h,[values[i+j][3] for i in range(h) for j in range(h)])
                primitive=Poly([Q(c) for c in row['primitive_coefficients']]);poly=primitive*Q(row['content'])
                assert content(primitive)==1 and all(c.q==1 for c in primitive)
                assert B.rank()==row['zeta7_slope_rank'] and primitive.degree()==row['degree_polynomial']
                for x in range(h+1):
                    assert (A+x*B).det()==poly(x);detchecks+=1
                value=arb(0);z=arb(7).zeta()
                for c in reversed(list(primitive)):value=value*z+arb(c)
                assert value>0 and value.log().overlaps(arb(row['log_primitive']))
                # Verify all actual target pivots, in addition to the measure proof.
                matrix=[[arb(A[i,j])+z*arb(B[i,j]) for j in range(h)] for i in range(h)]
                for j in range(h):
                    d=matrix[j][j];assert d>0
                    for i in range(j+1,h):
                        for k in range(i,h):
                            matrix[k][i]-=matrix[i][j]*matrix[k][j]/d;matrix[i][k]=matrix[k][i]
                records.append(dict(source=filename,source_sha256=hashlib.sha256(source).hexdigest(),K=K,h=h,
                                    independent_entries=len(values),exact_nuisance_equalities=2*len(values),
                                    direct_polynomial_identity_points=h+1,positive_target_pivots=h,
                                    degree_condition_zeta5_automatic=W.degree()+2*h<=3*K-2,
                                    zeta6_pade_remainder_degree=remainder.degree(),
                                    zeta6_pade_remainder_degree_bound=2*K-2*h,
                                    numerator_coefficients_nonnegative=coefficient_nonnegative,
                                    positivity_scope='positive_measure' if coefficient_nonnegative else 'finite_truncated_gram'))
    result=dict(status='independent_local_inverse_and_arb_checks_passed',records=records,
                total_entries=reschecks,total_direct_determinants=detchecks,euler_checks=euler_checks(),
                hermite_zeta6_checks=hermite_zeta6_checks(),
                scope='Finite verification plus general Euler and residue identities; no asymptotic assertion.')
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2),flush=True)

if __name__=='__main__':main()
