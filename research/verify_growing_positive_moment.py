"""Independent Fraction verification of growing-degree root and moment certificates."""
from fractions import Fraction as F
import json
import math
import itertools
from pathlib import Path
from verify_discrete_positive_cone import independent_map, mul, dot


def ev(p,x):
    value=F(0)
    for c in reversed(p):value=value*x+c
    return value


def determinant3(B):
    return (B[0][0]*(B[1][1]*B[2][2]-B[1][2]*B[2][1])
            -B[0][1]*(B[1][0]*B[2][2]-B[1][2]*B[2][0])
            +B[0][2]*(B[1][0]*B[2][1]-B[1][1]*B[2][0]))


def verify(row):
    n,w=row['n'],row['w'];d=w+3;M=independent_map(n,w)
    node=lambda r:(3*n+2+2*r)**2-(3*n+2)**2
    lifts={};edges=[]
    for name in ('lower','upper'):
        e=row[name];assert e['global_optimal']
        starts=e['starts'];assert all(b>=a+2 for a,b in zip(starts,starts[1:]))
        assert starts[0]>=(0 if e['infinity'] else 1)
        roots=([0] if not e['infinity'] else [])+[j for a in starts for j in (a,a+1)]
        assert roots==e['nodes']
        H=[F(1)]
        for j in roots:H=mul(H,[-node(j),1])
        assert H==list(map(F,e['H']))
        q=list(map(F,e['quadratic']));assert all(x>0 for x in q)
        P=mul(H,q);assert P==list(map(F,e['polynomial']))
        output=[dot(line,P) for line in M];assert output==list(map(F,e['output']))
        assert output[1]==output[2]==0
        c3,c5=map(F,e['dual_auxiliary']);r=F(e['endpoint']);mu=list(map(F,e['dual_weights']))
        assert all(x>=0 for x in mu)
        assert -output[0]/output[3]==r
        for j in range(d+1):
            rhs=sum((mu[i]*node(k)**j for i,k in enumerate(roots)),F(0))
            if e['infinity'] and j==d:rhs+=mu[-1]
            assert M[0][j]+c3*M[1][j]+c5*M[2][j]+r*M[3][j]==rhs
        scale=F(e['primitive_scale']);pair=e['primitive_output']
        assert scale>0 and [scale*output[k] for k in (0,3)]==pair
        assert math.gcd(*pair)==1
        t=n+1
        while ev(P,node(t-n-1))==0:t+=1
        x=2*t+n
        first=scale*ev(P,node(t-n-1))*F(math.prod(x*x-(n+2*j)**2 for j in range(1,n+1)),
                                      math.prod((t+j)**7 for j in range(n+1)))
        assert first>1
        B=[[dot(line,[F(0)]*j+H) for j in range(3)] for line in M]
        common=math.lcm(*(x.denominator for line in B for x in line))
        integer=[[int(x*common) for x in line] for line in B]
        contents=[math.gcd(*(line[j] for line in integer)) for j in range(3)]
        integer=[[line[j]//contents[j] for j in range(3)] for line in integer]
        minor0=determinant3([integer[k] for k in (0,1,2)])
        minor7=determinant3([integer[k] for k in (3,1,2)])
        gcd=math.gcd(minor0,minor7)
        assert F(-minor0,minor7)==r and abs(minor7)//gcd==abs(pair[1])
        lifts[name]=(P,output[3])
        edges.append(dict(sign=e['sign'],first_term_gt_one=True,first_term=str(first),
                          joint_minor_gcd=str(gcd),final_denominator=str(abs(pair[1]))))
    a,b=row['optimal_pair'];lo=F(row['lower']['endpoint']);hi=F(row['upper']['endpoint'])
    alpha=(a+hi*b)/(hi-lo);beta=(a+lo*b)/(hi-lo)
    assert alpha>=0 and beta>=0 and alpha+beta>0 and b!=0
    p,blo=lifts['lower'];q,bhi=lifts['upper']
    p=p+[F(0)]*(d+1-len(p));q=q+[F(0)]*(d+1-len(q))
    lift=[alpha*x/blo-beta*y/bhi for x,y in zip(p,q)]
    assert [dot(line,lift) for line in M]==[a,0,0,b]
    assert F(row['epsilon'])==max(a+lo*b,a+hi*b)
    assert math.gcd(a,b)==1
    return dict(n=n,w=w,global_certificates=2,positive_integer_lift_verified=True,edges=edges)


def verify_arithmetic_record(record):
    B=record['primitive_column_matrix']
    delta1=math.gcd(*(x for row in B for x in row))
    delta2=math.gcd(*(B[i][a]*B[j][b]-B[i][b]*B[j][a]
                     for i,j in itertools.combinations(range(4),2)
                     for a,b in itertools.combinations(range(3),2)))
    delta3=math.gcd(*(determinant3([B[i] for i in rows]) for rows in itertools.combinations(range(4),3)))
    smith=[delta1,delta2//delta1,delta3//delta2]
    assert smith==list(map(int,record['smith_invariants']))
    v=[B[1][1]*B[2][2]-B[1][2]*B[2][1],B[1][2]*B[2][0]-B[1][0]*B[2][2],B[1][0]*B[2][1]-B[1][1]*B[2][0]]
    content=math.gcd(*v);assert content==int(record['elimination_vector_content'])
    output=[sum(x*y//content for x,y in zip(line,v)) for line in B]
    assert math.gcd(*output)==int(record['primitive_input_output_content'])
    assert smith[-1]%math.gcd(*output)==0
    def split(value):
        rest=abs(value)
        for p in range(2,record['prime_cutoff']+1):
            while rest%p==0:rest//=p
        return rest
    assert split(smith[-1])==int(record['largest_smith_rough_part'])
    assert split(int(record['joint_minor_gcd']))==int(record['joint_gcd_rough_part'])
    assert split(int(record['final_denominator']) if 'final_denominator' in record else abs(int(record['zeta7_minor']))//int(record['joint_minor_gcd']))==int(record['denominator_rough_part'])


def verify_neighbors(folder):
    sources=json.loads((folder/'growing_positive_moment.json').read_text())['rows']
    sources+=json.loads((folder/'growing_positive_ratio_scan.json').read_text())['rows']
    rows=json.loads((folder/'growing_positive_arithmetic_neighbors.json').read_text())['rows'];count=0
    for r in rows:
        n,w=r['n'],r['w'];d=w+3;M=independent_map(n,w)
        source=next(x for x in sources if x['n']==n and x['w']==w)
        lo=F(source['lower']['endpoint']);hi=F(source['upper']['endpoint'])
        node=lambda j:(3*n+2+2*j)**2-(3*n+2)**2
        for rec in r['records']:
            e=rec['best'];H=[F(1)]
            starts=e['starts'];assert starts[0]>=(0 if e['infinity'] else 1)
            assert all(b>=a+2 for a,b in zip(starts,starts[1:]))
            for j in e['nodes']:H=mul(H,[-node(j),1])
            expected=([0] if not e['infinity'] else [])+[j for a in starts for j in (a,a+1)]
            assert expected==e['nodes']
            q=list(map(F,e['quadratic']));assert all(x>0 for x in q)
            P=mul(H,q);assert P==list(map(F,e['polynomial']))
            out=[dot(line,P) for line in M];assert out==list(map(F,e['output']))
            scale=F(e['primitive_scale']);a,b=e['primitive_output']
            assert [scale*x for x in out]==[a,0,0,b] and math.gcd(a,b)==1
            assert F(rec['upper_bound'])==max(a+b*lo,a+b*hi)
            t=n+1
            while ev(P,node(t-n-1))==0:t+=1
            x=2*t+n
            first=scale*ev(P,node(t-n-1))*F(math.prod(x*x-(n+2*j)**2 for j in range(1,n+1)),math.prod((t+j)**7 for j in range(n+1)))
            assert first==F(rec['arithmetic']['first_term']) and first>1
            count+=1
    return count


def main():
    folder=Path(__file__).parent;rows=[]
    for source in ('growing_positive_moment','growing_positive_ratio_scan'):
        inputs=json.loads((folder/(source+'.json')).read_text())['rows']
        for r in inputs:
            if not r.get('full_cone_optimal'):continue
            result=verify(r);rows.append(result)
            print('Verified',r['n'],r['w'],'both global endpoints, first terms, minors and integer lift',flush=True)
            (folder/'verify_growing_positive_moment.json').write_text(json.dumps(dict(
                scope='Independent Fraction direct-factor residue expansion and positive moment identities; no zeta approximation.',
                rows=rows),indent=2),encoding='utf-8')
    arithmetic=json.loads((folder/'growing_positive_arithmetic.json').read_text())['rows']
    for r in arithmetic:
        for e in r['edges']:verify_arithmetic_record(e)
    neighbors=verify_neighbors(folder)
    output=dict(scope='Independent Fraction direct-factor residues, all positivity identities, determinant-divisor Smith checks, and neighbor bounds; no zeta approximation.',
                rows=rows,smith_and_prime_support_checks=sum(len(r['edges']) for r in arithmetic),
                neighbor_winner_checks=neighbors)
    (folder/'verify_growing_positive_moment.json').write_text(json.dumps(output,indent=2),encoding='utf-8')
    print('Additional checks:',output['smith_and_prime_support_checks'],'Smith records and',neighbors,'neighbor winners',flush=True)


if __name__=='__main__':main()
