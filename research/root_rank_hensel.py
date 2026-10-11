"""Smooth p-adic rank-two locus, lifted to positive paired-root generators."""
import itertools
import json
from pathlib import Path
from root_module_deformation import *
from root_modular_rank_search import mulmod


def block_mod(M,starts,m):
    H=[1]
    for s in starts:
        a,b=node(8,s)%m,node(8,s+1)%m
        H=mulmod(H,[a*b%m,-a-b,1],m)
    return [[sum(int(row[k+j].numerator)*pow(int(row[k+j].denominator),-1,m)*v
                 for k,v in enumerate(H))%m for j in range(3)] for row in M]


def equations(M,starts,m):
    B=block_mod(M,starts,m)
    return [int(fmpz_mat([B[i] for i in (1,2,k)]).det())%m for k in (0,3)]


def main():
    folder=Path(__file__).parent;p=67;M=shifted_map(8,8)
    row=next(r for r in json.loads((folder/'growing_positive_moment.json').read_text())['rows'] if r['n']==8)
    lo=fmpq(row['lower']['endpoint']);hi=fmpq(row['upper']['endpoint'])
    starts=[3,9,17,43];assert equations(M,starts,p)==[0,0]
    B=block_mod(M,starts,p);pivot=(B[1][0]*B[2][1]-B[1][1]*B[2][0])%p
    assert pivot
    f=equations(M,starts,p*p);jac=[]
    for j in range(4):
        moved=starts[:];moved[j]+=p;g=equations(M,moved,p*p)
        jac.append([((b-a)%(p*p))//p for a,b in zip(f,g)])
    unknown=next(js for js in itertools.combinations(range(4),2)
                 if (jac[js[0]][0]*jac[js[1]][1]-jac[js[1]][0]*jac[js[0]][1])%p)
    a,b=unknown;J=[[jac[a][0],jac[b][0]],[jac[a][1],jac[b][1]]]
    det=(J[0][0]*J[1][1]-J[0][1]*J[1][0])%p;invdet=pow(det,-1,p)
    rows=[]
    for e in range(1,5):
        modulus=p**e;assert equations(M,starts,modulus)==[0,0]
        actual=sorted(starts)
        for j in range(1,4):
            while actual[j]<actual[j-1]+2:actual[j]+=modulus
        second=actual[:];second[-1]+=modulus
        cert=module(8,8,[root_block(8,actual,True,M),root_block(8,second,True,M)],lo,hi)
        values=[valuation(int(x),p) for x in cert['target_smith']]
        assert min(values)>=e
        data=dict(e=e,residue_starts=starts[:],integer_starts=actual,certificate=cert,smith_valuations=values)
        f=equations(M,starts,modulus*p);rhs=[-x//modulus%p for x in f]
        delta=[(J[1][1]*rhs[0]-J[0][1]*rhs[1])*invdet%p,
               (-J[1][0]*rhs[0]+J[0][0]*rhs[1])*invdet%p]
        data.update(next_equations=f,next_digits=delta);rows.append(data)
        starts[a]+=modulus*delta[0];starts[b]+=modulus*delta[1]
        print('Hensel',e,actual,'v',values,'rays',len(cert['rays']),'wedge',bool(cert['wedge']),flush=True)
    result=dict(scope='Smooth rank-two locus gives arbitrary p-power uniform divisibility, not small primitive forms.',
                p=p,base=[3,9,17,43],nuisance_pivot=pivot,jacobian_columns=jac,unknown_indices=list(unknown),
                jacobian_minor=J,jacobian_determinant_mod_p=det,rows=rows)
    (folder/'root_rank_hensel.json').write_text(json.dumps(result,indent=2),encoding='utf-8')


if __name__=='__main__':main()
