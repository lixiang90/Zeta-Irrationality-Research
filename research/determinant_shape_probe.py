"""Exact determinant recurrences and target-lattice shape diagnostics.

No zeta evaluations and no asymptotic inference from finite shape data.
"""
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq, fmpq_mat, fmpq_poly

from critical_lift_probe import output_map
from growing_head_quotient import kernel_polynomial


def raw_matrix(n, head):
    out,_=output_map(n,head=head)
    return fmpq_mat([[out[k][i] for i in range(4)] for k in (0,3,5,7)])


def determinant_formula(n, head):
    m=n//2
    assert n==2*m and m>=1 and 0<=head<7*m
    return fmpq((-1)**(m+head)*2**(11+8*head)*math.factorial(head)**8
                *math.factorial(m+head)*math.factorial(7*m-head-1),
                math.factorial(m)**8*math.factorial(n)**28)


def transfer_matrix(N, head):
    z=fmpq_poly([0,1])
    kernels=[]
    leading=[]
    for i in range(8):
        primitive,content=kernel_polynomial(N,head,i)
        k=fmpq_poly([a*content for a in primitive])
        kernels.append(k)
        leading.append(k[i+4])
    columns=[]
    for j in range(4):
        p=z**j*(z-N*N)**8
        for i in reversed(range(8)):
            p-=kernels[i]*(p[i+4]/leading[i])
        assert p.degree()<=3
        columns.append([p[i] for i in range(4)])
    Q=fmpq_mat([[columns[j][i] for j in range(4)] for i in range(4)])
    return Q,kernels,leading


def head_matrix(n,head):
    primitive,content=kernel_polynomial(n,head,0)
    kernel=[fmpq(x*content) for x in primitive]
    c=(n+2*head+2)**2
    T=fmpq_mat(4,4)
    for j in range(4):
        T[j,j]-=c
        if j<3:
            T[j+1,j]+=1
        else:
            for i in range(4): T[i,j]-=kernel[i]/kernel[4]
    return T


def transfer_check(N):
    Q,kernels,leading=transfer_matrix(N,0)
    predicted=fmpq(2**64*N**36*(N-1)**28,math.prod(7*N-2*r for r in range(1,9)))
    assert Q.det()==predicted
    # Check all coefficients, not only the determinant.
    assert raw_matrix(N-2,1)==raw_matrix(N,0)*Q*fmpq(1,4**7)
    jets=fmpq_mat([[sum((k[d]*math.comb(d,r)*(N*N)**(d-r)
                         for d in range(r,k.degree()+1)),fmpq(0))
                    for k in kernels] for r in range(8)])
    assert jets.det()==2**64*N**36*(N-1)**28
    return dict(N=N,transfer_determinant=str(predicted),jet_determinant=str(jets.det()),
                complete_transfer_identity=True)


def recurrence(N):
    head=N-3
    Q,_,_=transfer_matrix(N,head)
    assert Q.det()==fmpq(2**64*(head+1)**8*N**36*(N-1)**28,
                         math.prod(7*N-2*head-2*r for r in range(1,9)))
    T=head_matrix(N,head)*head_matrix(N,head+1)*head_matrix(N,head+2)
    C=Q.inv()*T
    R=C.transpose()*(4**5*(N*(N-1))**5)
    previous=raw_matrix(N-2,N-2).transpose()*fmpq(math.factorial(N-2)**5,4**(N-2))
    current=raw_matrix(N,N).transpose()*fmpq(math.factorial(N)**5,4**N)
    assert current==R*previous
    balanced=fmpq_mat([[R[i,j]*fmpq((N-2)**(2*j),N**(2*i)) for j in range(4)] for i in range(4)])
    return dict(N=N,coefficient_recurrence=[list(map(str,row)) for row in R.tolist()],
                balanced_recurrence=[list(map(str,row)) for row in balanced.tolist()],
                all_four_period_columns_verified=True)


def limiting_recurrence():
    z=fmpq_poly([0,1])
    kernel=fmpq_poly([-3,-76,-154,-28,5])
    def multiplication(p):
        cols=[(z**i*p)%kernel for i in range(4)]
        return fmpq_mat([[cols[j][i] for j in range(4)] for i in range(4)])
    Q=multiplication((z-1)**8)
    T=multiplication((z-9)**3)
    R=(Q.inv()*T).transpose()*4**5
    expected=fmpq_poly([27,1])*fmpq_poly([-3125,17973501862,573091,1])
    assert R.charpoly()==expected
    return dict(matrix=[list(map(str,row)) for row in R.tolist()],
                characteristic_polynomial_coefficients=list(map(str,expected.coeffs())),
                factorization='(X+27)*(X^3+573091*X^2+17973501862*X-3125)')


def gauss(gram):
    def dot(v,w):
        return sum((v[i]*gram[i][j]*w[j] for i in range(2) for j in range(2)),fmpq(0))
    a,b=[1,0],[0,1]
    steps=0
    while True:
        if dot(b,b)<dot(a,a): a,b=b,a
        r=dot(a,b)/dot(a,a)
        if abs(r)<=fmpq(1,2): break
        rounded=r+fmpq(1,2)
        k=int(rounded.numerator)//int(rounded.denominator)
        b=[b[i]-k*a[i] for i in range(2)]
        steps+=1
        assert steps<10000
    assert abs(a[0]*b[1]-a[1]*b[0])==1
    return a,b,dot(a,a),dot(b,b),steps


def shape(n):
    dn=math.lcm(*range(1,n+1))
    A=raw_matrix(n,n).transpose()*fmpq(dn**7*math.factorial(n)**5,4**n)
    m=n//2
    determinant=fmpq((-1)**m*2**11*dn**28*math.factorial(3*m)*math.factorial(5*m-1),
                      math.factorial(m)**8)
    assert A.det()==determinant
    assert all(A[i,j].denominator==1 for i in range(4) for j in range(4))
    B=A.inv()
    G=[[sum((B[i,k]*B[j,k] for k in range(4)),fmpq(0)) for j in (0,3)] for i in (0,3)]
    minors=[A[i,1]*A[j,2]-A[i,2]*A[j,1] for i,j in itertools.combinations(range(4),2)]
    gcd_minors=math.gcd(*(int(x) for x in minors))
    target_index=abs(int(determinant))//gcd_minors
    assert abs(int(determinant))==gcd_minors*target_index
    detG=G[0][0]*G[1][1]-G[0][1]**2
    assert detG==sum((x*x for x in minors),fmpq(0))/determinant**2
    rho=G[0][1]/G[0][0]
    transverse2=detG/G[0][0]
    a,b,first2,second2,steps=gauss(G)
    for v in (a,b,[1,0],[0,1],[2,-3]):
        direct=sum((v[i]*G[i][j]*v[j] for i in range(2) for j in range(2)),fmpq(0))
        assert direct==G[0][0]*(v[0]+rho*v[1])**2+transverse2*v[1]**2
    positive=all(B[0,j]>0 for j in range(4))
    slopes=[B[3,j]/B[0,j] for j in range(4)] if positive else []
    with ctx.workprec(192):
        log=lambda x:(arb(x).log()/n).str(20)
        rates=dict(det_A=log(abs(determinant)),covolume=(arb(detG).log()/(2*n)).str(20),
                   first_minimum=(arb(first2).log()/(2*n)).str(20),
                   second_minimum=(arb(second2).log()/(2*n)).str(20),
                   longitudinal=(arb(G[0][0]).log()/(2*n)).str(20),
                   transverse=(arb(transverse2).log()/(2*n)).str(20),
                   shape_ratio=(arb(second2/first2).log()/(2*n)).str(20))
        if positive: rates['slope_width']=log(max(slopes)-min(slopes))
    return dict(n=n,rates=rates,constant_inverse_row_positive=positive,
                det_A=str(determinant),metric_determinant=str(detG),
                longitudinal_squared=str(G[0][0]),transverse_squared=str(transverse2),
                rational_center=str(rho),first_minimum_squared=str(first2),second_minimum_squared=str(second2),
                reduced_basis=[list(map(str,a)),list(map(str,b))],gauss_steps=steps,
                nuisance_minor_gcd=str(gcd_minors),integral_target_image_index=str(target_index),
                slope_interval=[str(min(slopes)),str(max(slopes))] if positive else None)


def main():
    cases=[]
    for n in (2,4,6,8,12,16):
        heads=sorted(set((0,1,n//2,n,2*n,7*n//2-2,7*n//2-1)))
        for head in heads:
            actual=raw_matrix(n,head).det()
            predicted=determinant_formula(n,head)
            assert actual==predicted
            cases.append(dict(n=n,head=head,determinant=str(actual)))
    transfers=[transfer_check(N) for N in (4,6,8,12,16)]
    recurrences=[recurrence(N) for N in (4,6,8,12,16,24,32)]
    limit=limiting_recurrence()
    rows=[]
    for n in (4,8,16,24,32,48,64,96):
        row=shape(n);rows.append(row)
        print(json.dumps(dict(n=n,rates=row['rates'],positive=row['constant_inverse_row_positive'])),flush=True)
    with ctx.workprec(192):
        D=28+arb(3).log()*fmpq(3,2)+arb(5).log()*fmpq(5,2)
        beta=7+3*arb(3).log()+5*arb(2).log()
        kappa=D-2*beta
        lo=fmpq(10123576813076657727664936,10**25)
        hi=fmpq(10123576813076657727664937,10**25)
        x=arb((lo+hi)/2,(hi-lo)/2)
        phi=8*x*x.log()-(x-1)*(x-1).log()+(x+2)*(x+2).log()-8*(x+1)*(x+1).log()
        spectral_kappa=14+fmpq(3,2)*arb(3).log()+phi
        constants=dict(determinant_exponent=D.str(24),coefficient_upper_exponent=beta.str(24),
                       covolume_decay_lower=kappa.str(24),
                       spectral_covolume_decay=spectral_kappa.str(23),
                       sufficient_shortest_vector_exponent_threshold=(7+fmpq(3,2)*arb(3).log()).str(23))
    result=dict(scope='Exact determinant identities; finite lattice shapes do not prove asymptotic nondegeneracy.',
                determinant_checks=cases,transfer_checks=transfers,shape_cases=rows,constants=constants,
                recurrence_checks=recurrences,limiting_recurrence=limit)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(checks=len(cases),transfers=len(transfers),constants=constants)),flush=True)


if __name__=='__main__': main()
