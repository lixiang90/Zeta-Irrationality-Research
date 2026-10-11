"""All-unit necessary content bounds by modular coefficient-lattice identities.

This does not sample x units.  Smith reduction over Z/p^D Z constructs
explicit coefficient combinations isolating every parameter monomial modulo
p^D.  It applies to x,y that are p-integral.  Certificates are independently
checked by modular matrix multiplication before saving.
"""
import json,sys,hashlib,math
from pathlib import Path
from flint import fmpq as Q

sys.set_int_max_str_digits(0)


def valint(n,p,cap):
    if not n:return cap
    if p==2:return min(cap,(n&-n).bit_length()-1)
    v=0
    while n%p==0:n//=p;v+=1
    return min(v,cap)


def valq(q,p):
    if not q:return None
    n,d=abs(int(q.numerator)),int(q.denominator);v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v


def modq(q,p,mod):
    n,d=int(q.numerator),int(q.denominator)
    assert d%p
    return n*pow(d,-1,mod)%mod


def reduce(A,p,D):
    rows,cols=len(A),len(A[0]);mod=p**D
    M=[r[:] for r in A]
    U=[[int(i==j) for j in range(rows)] for i in range(rows)]
    V=[[int(i==j) for j in range(cols)] for i in range(cols)]
    diagonal=[]
    for k in range(cols):
        e,r,c=min((valint(M[i][j],p,D),i,j) for i in range(k,rows) for j in range(k,cols))
        if e==D:
            diagonal.extend([D]*(cols-k));break
        M[k],M[r]=M[r],M[k];U[k],U[r]=U[r],U[k]
        for matrix in [M,V]:
            for row in matrix:row[k],row[c]=row[c],row[k]
        pe=p**e;inv=pow(M[k][k]//pe,-1,mod)
        M[k]=[(v*inv)%mod for v in M[k]]
        U[k]=[(v*inv)%mod for v in U[k]]
        assert M[k][k]==pe
        for i in range(k+1,rows):
            if not M[i][k]:continue
            assert M[i][k]%pe==0
            scalar=M[i][k]//pe
            M[i]=[(a-scalar*b)%mod for a,b in zip(M[i],M[k])]
            U[i]=[(a-scalar*b)%mod for a,b in zip(U[i],U[k])]
            assert not M[i][k]
        for j in range(k+1,cols):
            if not M[k][j]:continue
            assert M[k][j]%pe==0
            scalar=M[k][j]//pe
            for i in range(rows):M[i][j]=(M[i][j]-scalar*M[i][k])%mod
            for i in range(cols):V[i][j]=(V[i][j]-scalar*V[i][k])%mod
            assert not M[k][j]
        diagonal.append(e)
    assert all(M[i][j]==(p**diagonal[i] if i==j and i<cols and diagonal[i]<D else 0)
               for i in range(rows) for j in range(cols))
    certificates=[]
    for i in range(cols):
        conductor=max(0,max(e-valint(V[i][j],p,D) for j,e in enumerate(diagonal)))
        multipliers=[]
        for j,e in enumerate(diagonal):
            numerator=p**conductor*V[i][j]
            assert numerator%p**e==0
            multipliers.append(numerator//p**e)
        R=[sum(multipliers[j]*U[j][k] for j in range(cols))%mod for k in range(rows)]
        # This is the certificate used later.  Its entries are ordinary
        # integers and the matrix A is integral modulo the target power.
        image=[sum(R[k]*A[k][j] for k in range(rows))%mod for j in range(cols)]
        expected=[(p**conductor)%mod if j==i else 0 for j in range(cols)]
        assert image==expected
        certificates.append((conductor,R))
    return diagonal,certificates


def main():
    folder=Path(__file__).parent
    path=folder/'zeta7_two_moment_partial_20261004_coefficients.json';raw=path.read_bytes();data=json.loads(raw)
    monomials=[(r['i'],r['j']) for r in data['coefficients']]
    G=[[Q(r['polynomial_coefficients'][k]) if k<len(r['polynomial_coefficients']) else Q(0)
        for r in data['coefficients']] for k in range(38)]
    baseline=json.loads((folder/'zeta7_joint_lattice_20261004_completion.json').read_text(encoding='utf-8'))
    ct0=Q(baseline['original_baseline_content'])
    results=[]
    for p in list(map(int,sys.argv[1:])) or [2,3,5,7,11,13]:
        minimum=min(valq(c,p) for row in G for c in row if c)
        v0=valq(ct0,p);D=v0-minimum;mod=p**D
        A=[[modq(c/Q(p)**minimum,p,mod) for c in row] for row in G]
        diagonal,certificates=reduce(A,p,D)
        constraints=[]
        for (i,j),(conductor,R) in zip(monomials,certificates):
            constraints.append(dict(i=i,j=j,conductor=conductor,necessary_weight=D-conductor,
                                    multipliers=list(map(str,R))))
        bound=max(0,max(math.ceil((D-c['conductor'])/c['i']) for c in constraints if c['i'] and not c['j']))
        ybound=max(0,max(math.ceil((D-c['conductor'])/c['j']) for c in constraints if c['j'] and not c['i']))
        result=dict(p=p,baseline_content_valuation=v0,coefficient_minimum_valuation=minimum,target_power=D,
                    smith_diagonal_valuations=diagonal,all_unit_minimum_x_valuation=bound,
                    all_unit_minimum_y_valuation=ybound,constraints=constraints,
                    scaled_coefficient_matrix=[[str(v) for v in row] for row in A],
                    statement='For p-integral x,y, full old-content protection implies '
                              'i*v_p(x)+j*v_p(y)>=necessary_weight for every stored constraint. '
                              'No restriction on any unit digits is imposed.')
        results.append(result)
        print('p',p,'D',D,'Smith range',min(diagonal),max(diagonal),'all-unit x bound',bound,'y',ybound,flush=True)
        out=dict(status='in_progress',K=40,N=3,h=37,monomials=monomials,results=results,
                 source_coefficients_sha256=hashlib.sha256(raw).hexdigest(),
                 scope='All-unit necessary constraints for p-integral x,y. These identities are '
                       'not asserted for parameters with negative p-adic valuations.')
        Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed';Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
