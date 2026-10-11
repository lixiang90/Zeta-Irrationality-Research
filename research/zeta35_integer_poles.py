"""Exact target alignment in a positive integer-pole rational-function family."""
import argparse
import json
import math
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx


def mul_trunc(a,b):
    return [sum((a[j]*b[i-j] for j in range(i+1)),Q(0)) for i in range(5)]


def run(N,r,verbose=True):
    M=int(r*N)
    assert N%2==0 and Q(r)*N==M and 0<=2*M+2<=5*N+3
    P=Poly([1])
    for k in range(1,M+1):
        P*=Poly([-k*(N+k),N,1])
    H=[[Q(0)] for _ in range(6)]
    for s in range(1,6):
        for j in range(1,N+1):
            H[s].append(H[s][-1]+Q(1,j**s))
    base=[];linear=[]
    for j in range(N+1):
        local=[sum((P[i]*math.comb(i,k)*Q(-j)**(i-k)
                    for i in range(k,len(P))),Q(0)) for k in range(5)]
        for l in range(N+1):
            if l!=j:
                local=mul_trunc(local,[Q((-1)**k*math.comb(k+4,4),(l-j)**(5+k)) for k in range(5)])
        base.append([Q(0)]+[local[5-s] for s in range(1,6)])
        yl=mul_trunc(local,[Q(-j*(N-j)),Q(N-2*j),Q(1),Q(0),Q(0)])
        linear.append([Q(0)]+[yl[5-s] for s in range(1,6)])
    C=[sum((row[s] for row in base),Q(0)) for s in range(6)]
    Y=[sum((row[s] for row in linear),Q(0)) for s in range(6)]
    assert C[1]==C[2]==C[4]==0 and Y[1]==Y[2]==Y[4]==0
    assert C[3]-3*C[5]!=0
    lam=-(Y[3]-3*Y[5])/(C[3]-3*C[5])
    coeff=[[linear[j][s]+lam*base[j][s] for s in range(6)] for j in range(N+1)]
    A=Y[5]+lam*C[5]
    assert Y[3]+lam*C[3]==3*A and A!=0
    B=-sum((coeff[j][s]*H[s][j] for j in range(N+1) for s in range(1,6)),Q(0))
    # Independently evaluate the partial-fraction identity at three points.
    for x in (Q(M+1),Q(M+2),Q(1,2)):
        actual=P(x)*(x*(x+N)+lam)/math.prod((x+j)**5 for j in range(N+1))
        rhs=sum((coeff[j][s]/(x+j)**s for j in range(N+1) for s in range(1,6)),Q(0))
        assert actual==rhs
    cutoff=(M+1)*(M+N+1)
    positive=lam>-cutoff
    den=math.lcm(int(A.denominator),int(B.denominator))
    ai,bi=int(A*den),int(B*den)
    divisor=math.gcd(ai,bi);ai//=divisor;bi//=divisor
    ctx.prec=max(abs(ai).bit_length(),abs(bi).bit_length())+512
    L=ai*(3*arb(3).zeta()+arb(5).zeta())+bi
    if positive:
        assert L>0
    row=dict(N=N,M=M,r=float(r),lambda_value=str(lam),lambda_over_N2=float(lam/N**2),
             raw_theta_coefficient=str(A),raw_constant=str(B),
             integerizing_factor=str(Q(den,divisor)),
             positivity_at_all_integer_summands=positive,
             primitive_theta_coefficient=str(ai),primitive_constant=str(bi),
             log_abs_integer_form=float(abs(L).log()),
             log_interval=abs(L).log().str(25),
             positive_integer_form=bool(L>0),
             base_ratio=str(C[3]/C[5]) if C[5] else None)
    if verbose:
        print('N',N,'M',M,'lambda/N2',round(row['lambda_over_N2'],6),
              'positive',positive,'logL',round(row['log_abs_integer_form'],6),flush=True)
    return row


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--maxN',type=int,default=32);args=p.parse_args()
    rows=[]
    path=Path(__file__).with_suffix('.json')
    for N in range(2,args.maxN+1,2):
        for r in (1,2):
            rows.append(run(N,r))
            path.write_text(json.dumps(dict(scope='finite exact scan; no asymptotic claim',rows=rows),indent=2),encoding='utf-8')
