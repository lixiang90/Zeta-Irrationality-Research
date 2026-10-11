"""Finite ideal-closure certificates for all q-integral parameter units.

The rows are monomial multiples of every X coefficient of the determinant.
Modular Smith operations are retained as a reversible operation list so only
the required pure-x certificates need large multiplier vectors.
"""
import json,sys,hashlib,math
from pathlib import Path
from flint import fmpq as Q
from zeta7_all_units_20261004 import valint,valq,modq

sys.set_int_max_str_digits(0)


def reduce(A,p,D,targets):
    rows,cols=len(A),len(A[0]);mod=p**D
    M=[r[:] for r in A];V=[[int(i==j) for j in range(cols)] for i in range(cols)]
    ops=[];diagonal=[]
    for k in range(min(rows,cols)):
        e,r,c=min((valint(M[i][j],p,D),i,j) for i in range(k,rows) for j in range(k,cols))
        if e==D:
            diagonal.extend([D]*(cols-k));break
        M[k],M[r]=M[r],M[k];ops.append(('swap',k,r))
        for matrix in [M,V]:
            for row in matrix:row[k],row[c]=row[c],row[k]
        pe=p**e;inv=pow(M[k][k]//pe,-1,mod)
        M[k]=[(v*inv)%mod for v in M[k]];ops.append(('scale',k,inv))
        assert M[k][k]==pe
        for i in range(k+1,rows):
            if not M[i][k]:continue
            scalar=M[i][k]//pe;assert M[i][k]%pe==0
            M[i]=[(a-scalar*b)%mod for a,b in zip(M[i],M[k])];ops.append(('sub',i,k,scalar))
            assert not M[i][k]
        for j in range(k+1,cols):
            if not M[k][j]:continue
            scalar=M[k][j]//pe;assert M[k][j]%pe==0
            for i in range(rows):M[i][j]=(M[i][j]-scalar*M[i][k])%mod
            for i in range(cols):V[i][j]=(V[i][j]-scalar*V[i][k])%mod
            assert not M[k][j]
        diagonal.append(e)
    if len(diagonal)<cols:diagonal.extend([D]*(cols-len(diagonal)))
    if targets is None:
        conductors=[max(0,max(e-valint(V[i][j],p,D) for j,e in enumerate(diagonal))) for i in range(cols)]
        targets=[min(range(cols),key=lambda i:conductors[i])]
    certificates=[]
    for i in targets:
        conductor=max(0,max(e-valint(V[i][j],p,D) for j,e in enumerate(diagonal)))
        if conductor>=D:
            certificates.append((i,conductor,[]));continue
        R=[0]*rows
        for j,e in enumerate(diagonal):
            numerator=p**conductor*V[i][j]
            assert numerator%p**e==0
            if j<rows:R[j]=(numerator//p**e)%mod
            else:assert e==D and numerator%mod==0
        for op in reversed(ops):
            if op[0]=='swap':_,a,b=op;R[a],R[b]=R[b],R[a]
            elif op[0]=='scale':_,a,u=op;R[a]=R[a]*u%mod
            else:_,a,b,u=op;R[b]=(R[b]-u*R[a])%mod
        image=[sum(R[k]*A[k][j] for k in range(rows))%mod for j in range(cols)]
        assert image==[p**conductor if j==i else 0 for j in range(cols)]
        certificates.append((i,conductor,R))
    return diagonal,certificates


def main():
    shift_degree=int(sys.argv[1]) if len(sys.argv)>1 else 2
    primes=list(map(int,sys.argv[2:])) or [2,3,5,7,11]
    folder=Path(__file__).parent;path=folder/'zeta7_two_moment_partial_20261004_coefficients.json';raw=path.read_bytes();d=json.loads(raw)
    old_monomials=[(r['i'],r['j']) for r in d['coefficients']]
    G=[[Q(r['polynomial_coefficients'][k]) if k<len(r['polynomial_coefficients']) else Q(0)
        for r in d['coefficients']] for k in range(38)]
    ct0=Q(json.loads((folder/'zeta7_joint_lattice_20261004_completion.json').read_text(encoding='utf-8'))['original_baseline_content'])
    shifts=[(a,b) for a in range(shift_degree+1) for b in range(shift_degree+1-a)]
    monomials=sorted(set((i+a,j+b) for i,j in old_monomials for a,b in shifts))
    index={v:i for i,v in enumerate(monomials)};targets=[i for i,(a,b) in enumerate(monomials) if a and not b]
    results=[]
    for p in primes:
        minimum=min(valq(c,p) for row in G for c in row if c);v0=valq(ct0,p);D=v0-minimum;mod=p**D
        oldA=[[modq(c/Q(p)**minimum,p,mod) for c in row] for row in G]
        A=[];row_labels=[]
        for a,b in shifts:
            for k,row in enumerate(oldA):
                if not any(row):continue
                new=[0]*len(monomials)
                for (i,j),value in zip(old_monomials,row):new[index[(i+a,j+b)]]=value
                A.append(new);row_labels.append([k,a,b])
        diagonal,certificates=reduce(A,p,D,targets)
        saved=[]
        for column,conductor,R in certificates:
            i,j=monomials[column];bound=max(0,math.ceil((D-conductor)/i))
            saved.append(dict(i=i,j=j,conductor=conductor,necessary_weight=D-conductor,
                              minimum_x_valuation=bound,multipliers=list(map(str,R))))
        bound=max(c['minimum_x_valuation'] for c in saved)
        result=dict(p=p,target_power=D,coefficient_minimum_valuation=minimum,baseline_content_valuation=v0,
                    rows=len(A),columns=len(monomials),row_labels=row_labels,smith_diagonal_valuations=diagonal,
                    all_unit_minimum_x_valuation=bound,pure_x_certificates=saved,
                    scaled_macaulay_matrix=[[str(v) for v in row] for row in A])
        results.append(result)
        print('shift',shift_degree,'p',p,'matrix',len(A),len(monomials),'all-unit x',bound,flush=True)
        out=dict(status='in_progress',K=40,N=3,h=37,shift_degree=shift_degree,monomials=monomials,
                 source_coefficients_sha256=hashlib.sha256(raw).hexdigest(),results=results,
                 scope='All-unit necessary bounds for q-integral x,y from finitely many ideal multiples. '
                       'The finite Macaulay degree is not asserted to exhaust the protection ideal.')
        Path(__file__).with_name(Path(__file__).stem+f'_d{shift_degree}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    out['status']='passed';Path(__file__).with_name(Path(__file__).stem+f'_d{shift_degree}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
