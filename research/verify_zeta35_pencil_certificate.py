"""Replay certificates without using their generator's elimination algorithm."""
import argparse,json
from pathlib import Path
from flint import fmpq_mat
import zeta35_mixed_moments as mixed
from zeta35_local_layers import vp_int
from zeta35_pole_cancellation import val

def verify(n):
    path=Path(__file__).with_name(f'zeta35_pencil_certificate_n{n}.json')
    data=json.loads(path.read_text());K,N,h,aa,bb=mixed.original.entries(n);a3=mixed.shifted_mu3_entries(n)
    originals={a:fmpq_mat([[aa[i+j]-a*a3[i+j] for j in range(h)] for i in range(h)]) for a in (0,3)}
    B=fmpq_mat([[bb[i+j] for j in range(h)] for i in range(h)])
    detcache={};verified=[]
    for cert in data['rows']:
        p,L,s=cert['p'],cert['precision'],cert['scale'];modulus=p**L
        def matrix(M):
            answer=[]
            for i in range(h):
                row=[]
                for j in range(h):
                    q=M[i,j]*p**s
                    row.append(int(q.numerator)*pow(int(q.denominator),-1,modulus)%modulus)
                answer.append(row)
            return answer
        mats=[matrix(originals[cert['a']]),matrix(B)]
        for k,op in enumerate(cert['operations']):
            w,pivot_i,pivot_j=op['pivot']
            for M in mats:
                M[k],M[pivot_i]=M[pivot_i],M[k]
                for row in M:row[k],row[pivot_j]=row[pivot_j],row[k]
                for i,factor in enumerate(map(int,op['row_factors']),start=k+1):
                    if factor:
                        for j in range(h):M[i][j]=(M[i][j]-factor*M[k][j])%modulus
                for j,factor in enumerate(map(int,op['column_factors']),start=k+1):
                    if factor:
                        for i in range(h):M[i][j]=(M[i][j]-factor*M[i][k])%modulus
        a,b=mats
        assert all(a[i][j]==0 for i in range(h) for j in range(h) if i!=j)
        assert [vp_int(a[i][i],p,L)-s for i in range(h)]==cert['constant_layers']
        assert b==[[int(x) for x in row] for row in cert['transformed_B_scaled_mod_pL']]
        bounds=[[min(vp_int(a[i][j],p,L),vp_int(b[i][j],p,L))-s for j in range(h)] for i in range(h)]
        assert bounds==cert['entry_bounds']
        u,v=cert['row_weights'],cert['column_weights']
        assert all(u[i]+v[j]<=bounds[i][j] for i in range(h) for j in range(h))
        assert sum(u)+sum(v)==cert['lower']
        witness=cert['specialization_witness']
        if witness:
            key=(cert['a'],witness['x'])
            if key not in detcache:detcache[key]=(originals[key[0]]+key[1]*B).det()
            assert val(detcache[key],p)==cert['lower']
        verified.append(dict(p=p,a=cert['a'],lower=cert['lower'],sharp=witness is not None))
    result=dict(n=n,status='independent_replay_passed',cases=len(verified),rows=verified)
    Path(__file__).with_name(f'verify_zeta35_pencil_certificate_n{n}.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print('verified',n,len(verified),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('n',type=int,nargs='+')
    for n in parser.parse_args().n:verify(n)
