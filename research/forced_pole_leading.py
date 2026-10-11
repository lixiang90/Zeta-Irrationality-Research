"""Exact leading coefficient of D_N^6 D_M^2 with a polynomial tail block."""
import json
from pathlib import Path
from math import lcm, prod
from flint import fmpq, fmpq_poly, fmpq_mat, fmpz_mat
from joint_exact import Dcache, moment, entries


ROOT=Path(__file__).parent


def mu(P):
    return sum((c*moment(i) for i,c in enumerate(P)),fmpq(0))


def run():
    data=json.loads((ROOT/'forced_pole_subspaces.json').read_text())
    records=[]
    for row in data['rows']:
        if row['label']!='scaled_block' and not (row['K']==24 and row['roots']==[2]):
            continue
        K,N,h=row['K'],row['N'],row['h'];M=2*N;L=K-M;s=h-L
        t=fmpq_poly([0,1]);weight=fmpq_poly(Dcache(N))**6*Dcache(K)
        tail=fmpq_mat(s,s,[mu(weight*t**(i+j)) for i in range(s) for j in range(s)])
        pole_det=(-1)**(L*(L-1)//2)*prod(
            fmpq(j**6)*Dcache(N)(-j*j)**6*Dcache(M)(-j*j) for j in range(M+1,K+1))
        predicted=tail.det()*pole_det
        P=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])
        aa,bb=entries(K,[(N,6),(M,2)],h)
        den=lcm(*(int(x.q) for x in aa))
        a0=fmpz_mat(h,h,[int(den*aa[i+j]) for i in range(h) for j in range(h)])
        constant=fmpq(a0.det(),den**h)
        assert predicted*P[0]==P[L]*constant
        assert tail.det()>0 and P.degree()==L
        # Also check every entry of the cross and polynomial blocks by
        # multiplying the original exact rational moment Hankel matrix.
        poles=fmpq_poly(Dcache(K)//Dcache(M))
        C=fmpq_mat(h,h,[ (t**i if i<L else poles*t**(i-L))[j]
                        for i in range(h) for j in range(h)])
        A=fmpq_mat(h,h,[aa[i+j] for i in range(h) for j in range(h)])
        B=fmpq_mat(h,h,[bb[i+j] for i in range(h) for j in range(h)])
        ca=C*A*C.transpose();cb=C*B*C.transpose()
        assert C.det()==1
        assert all(not cb[i,j] for i in range(h) for j in range(h) if i>=L or j>=L)
        assert all(ca[L+i,L+j]==tail[i,j] for i in range(s) for j in range(s))
        cross_weight=fmpq_poly(Dcache(N))**6*Dcache(M)
        assert all(ca[i,L+j]==mu(cross_weight*t**(i+j)) for i in range(L) for j in range(s))
        certificate=dict(K=K,N=N,M=M,h=h,pole_dimension=L,tail_dimension=s,
                         tail_determinant=str(tail.det()),pole_determinant=str(pole_det),
                         leading_coefficient=str(predicted),full_polynomial_match=True,
                         all_cross_and_tail_entries_verified=True)
        records.append(certificate)
        print(json.dumps({k:v for k,v in certificate.items() if k not in
                          ['tail_determinant','pole_determinant','leading_coefficient']}),flush=True)
    (ROOT/'forced_pole_leading_certificates.json').write_text(json.dumps(records,indent=2),encoding='utf-8')
    return records


if __name__=='__main__':
    run()
