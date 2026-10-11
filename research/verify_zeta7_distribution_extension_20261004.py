"""Independent x-variable reconstruction and direct determinant checks."""
import hashlib, json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, fmpq_mat, arb, ctx
from b8_hankel import Dpoly

sys.set_int_max_str_digits(0)
BASE=Path(__file__).with_name('zeta7_distribution_extension_20261004.json')

def negative_square(P):
    coeff=[Q(0)]*(2*P.degree()+1)
    for i,c in enumerate(P):coeff[2*i]=c*(-1)**i
    return fmpq_poly(coeff)

def kappa(s,d):
    if d<s-2:return Q(0)
    return math.prod(range(d-s+3,d+1))*Q.bernoulli(d-s+2)/math.factorial(s-1)

def independent_entries(K,N,h):
    D=negative_square(fmpq_poly(Dpoly(K)));W=negative_square(fmpq_poly(Dpoly(N))**8)
    derivative=D.derivative();P=fmpq_poly([0]*7+[1])*W
    H={s:[Q(0)] for s in (3,5,7)}
    for s in H:
        for j in range(1,K+1):H[s].append(H[s][-1]+Q(1,j**s))
    A={s:[] for s in H};B=[]
    for e in range(2*h-1):
        quotient=P//D
        values={s:sum((c*kappa(s,d) for d,c in enumerate(quotient)),Q(0)) for s in H}
        slope=Q(0)
        for j in range(1,K+1):
            rp=P(j)/derivative(j);rm=P(-j)/derivative(-j)
            for s in H:values[s]+=rp*H[s][j]+rm*H[s][j-1]
            slope-=rp+rm
        for s in H:A[s].append(values[s])
        B.append(slope);P*=fmpq_poly([0,0,-1])
    return A,B

def target_ldlt(A,B,h,a,b):
    z=arb(7).zeta();M=[[arb(A[7][i+j]+a*A[5][i+j]+b*A[3][i+j])+z*arb(B[i+j]) for j in range(h)] for i in range(h)]
    for j in range(h):
        d=M[j][j]
        if d<0:return 'negative_pivot'
        assert d>0
        for i in range(j+1,h):
            for k in range(i,h):
                M[k][i]-=M[i][j]*M[k][j]/d;M[i][k]=M[k][i]
    return 'positive'

def main():
    source=BASE.read_bytes();data=json.loads(source);assert data['status']=='finite_exact_and_arb_checks_passed'
    points=0;rows=0;degrees=[]
    with ctx.workprec(20000):
        for ex in data['experiments']:
            K,N,h=ex['K'],ex['N'],ex['h'];A,B=independent_entries(K,N,h)
            z=arb(7).zeta()
            for row in ex['rows']:
                a,b=Q(row['a']),Q(row['b']);ct=Q(row['content'])
                primitive=fmpq_poly([Q(c) for c in row['primitive_coefficients']]);poly=primitive*ct
                assert primitive.degree()==row['degree']
                assert all(c.q==1 for c in primitive) and math.gcd(*(int(c.p) for c in primitive))==1
                aa=[A[7][e]+a*A[5][e]+b*A[3][e] for e in range(2*h-1)]
                # Degree <= h, so h+1 direct rational determinants prove all coefficients.
                for x in range(h+1):
                    direct=fmpq_mat(h,h,[aa[i+j]+x*B[i+j] for i in range(h) for j in range(h)]).det()
                    assert direct==poly(x);points+=1
                value=arb(0)
                for c in reversed(list(primitive)):value=value*z+arb(c)
                assert (1 if value>0 else -1)==row['target_value_sign']
                score=abs(value).log()/K**2
                assert score.overlaps(arb(row['score_ball']))
                status=target_ldlt(A,B,h,a,b)
                assert status==row['relative_ldlt_diagnostic']['status']
                rows+=1
            degrees.append(dict(K=K,h=h,independent_x_variable_entries=4*(2*h-1)))
    out=dict(status='independent_x_variable_checks_passed',source_sha256=hashlib.sha256(source).hexdigest(),
             experiments=degrees,parameter_rows=rows,direct_exact_determinants=points,
             scope='Finite polynomial identity, target value and positive-definiteness checks. No asymptotic claim.')
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
