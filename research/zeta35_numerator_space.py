"""Exact coefficient maps for higher-dimensional positive numerator spaces."""
import math
from flint import fmpq as Q, fmpq_poly as Poly, arb, ctx
from zeta35_integer_poles import mul_trunc


def coefficient_map(N,M,d,shift=0):
    assert N%2==0 and 2*M+2*d<=5*N+3
    P=Poly([1])
    for k in range(1,M+1):
        P*=Poly([-k*(N+k),N,1])
    H=[[Q(0)] for _ in range(6)]
    for s in range(1,6):
        for j in range(1,N+1):
            H[s].append(H[s][-1]+Q(1,j**s))
    rows=[[Q(0),Q(0),Q(0)] for _ in range(d+1)] # zeta5,zeta3,constant
    local_cert=[]
    for j in range(N+1):
        local=[sum((P[i]*math.comb(i,k)*Q(-j)**(i-k)
                    for i in range(k,len(P))),Q(0)) for k in range(5)]
        for l in range(N+1):
            if l!=j:
                local=mul_trunc(local,[Q((-1)**k*math.comb(k+4,4),(l-j)**(5+k)) for k in range(5)])
        factor=[Q(-j*(N-j)-shift),Q(N-2*j),Q(1),Q(0),Q(0)]
        for power in range(d+1):
            rows[power][0]+=local[0]
            rows[power][1]+=local[2]
            rows[power][2]-=sum((local[5-s]*H[s][j] for s in range(1,6)),Q(0))
            if power==0:
                local_cert.append(list(local))
            local=mul_trunc(local,factor)
    return rows


def combine(rows,p):
    return [sum((p[i]*rows[i][j] for i in range(len(p))),Q(0)) for j in range(3)]


def primitive(A,C):
    den=math.lcm(int(A.denominator),int(C.denominator))
    ai,ci=int(A*den),int(C*den)
    g=math.gcd(ai,ci)
    assert g
    return ai//g,ci//g


def evaluate(A,C):
    ai,ci=primitive(A,C)
    ctx.prec=max(abs(ai).bit_length(),abs(ci).bit_length())+256
    L=ai*(3*arb(3).zeta()+arb(5).zeta())+ci
    for _ in range(6):
        if not L.contains(0):
            break
        ctx.prec*=2
        L=ai*(3*arb(3).zeta()+arb(5).zeta())+ci
    assert L>0
    return dict(a=str(ai),c=str(ci),log_L=float(L.log()),log_interval=L.log().str(24))
