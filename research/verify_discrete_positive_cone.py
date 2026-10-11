"""Independent Fraction checks, including a direct-factor partial-fraction map.

Does not import the optimizer, its arithmetic engine, or evaluate zeta.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import math


def mul(a,b,cap=None):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if cap is None or i+j<cap:c[i+j]+=x*y
    return c if cap is None else c[:cap]


def dot(a,b):return sum((x*y for x,y in zip(a,b)),F(0))


def independent_map(n,w):
    d=w+3;origin=(3*n+2)**2
    out=[[F(0)]*(d+1) for _ in range(8)]
    for j in range(n+1):
        inverse=[F(1)]
        for k in range(n+1):
            if k!=j:
                inverse=mul(inverse,[F((-1)**r*math.comb(6+r,r),(k-j)**(7+r)) for r in range(7)],7)
        x=n-2*j
        head=[F(1)]
        for ell in range(1,n+1):head=mul(head,[x*x-(n+2*ell)**2,4*x,4],7)
        base=mul(inverse,head,7)
        y=[x*x-origin,4*x,4];power=[F(1)]
        for i in range(d+1):
            jet=mul(base,power,7)
            for k in range(1,8):
                c=jet[7-k]
                out[k][i]+=c
                out[0][i]-=c*sum((F(1,t**k) for t in range(1,j+1)),F(0))
            power=mul(power,y,7)
    assert all(x==0 for k in (1,2,4,6) for x in out[k])
    return [out[k] for k in (0,3,5,7)]


def polynomial(n,d,tag):
    p=[F(0)]*tag['power']+[F(1)]
    node=lambda k:(3*n+2+2*k)**2-(3*n+2)**2
    for a,b in tag.get('node_pairs',[]):
        assert a>=0 and (b==a+1 or (b==a and tag['type']=='squares'))
        p=mul(p,[node(a)*node(b),-node(a)-node(b),1])
    return p+[F(0)]*(d+1-len(p))


def main():
    folder=Path(__file__).parent
    rows=json.loads((folder/'discrete_positive_full_window.json').read_text())['rows']
    globals_=json.loads((folder/'discrete_positive_global_certificate.json').read_text())['rows']
    result=[]
    for row,glob in zip(rows,globals_):
        n,w=row['n'],row['w'];d=w+3;M=independent_map(n,w)
        endpoint_polys={}
        for name in ('lower','upper'):
            edge=row[name];cert=glob[name]
            assert cert['verified']
            polys=[polynomial(n,d,tag) for tag in edge['generator_tags']]
            weights=list(map(F,edge['weights']));assert all(x>0 for x in weights)
            P=[sum(weights[i]*polys[i][j] for i in range(len(polys))) for j in range(d+1)]
            assert P==list(map(F,edge['polynomial']))
            output=[dot(line,P) for line in M]
            assert output==list(map(F,edge['output']))
            assert output[1]==output[2]==0 and output[3]*edge['sign']>0
            r=F(edge['endpoint']);assert -output[0]/output[3]==r
            c3,c5=map(F,edge['dual_auxiliary'])
            functional=[M[0][j]+c3*M[1][j]+c5*M[2][j]+r*M[3][j] for j in range(d+1)]
            nodes=[(3*n+2+2*k)**2-(3*n+2)**2 for k in cert['common_nodes']]
            mu=list(map(F,cert['weights']));assert all(x>=0 for x in mu)
            for j in range(d+1):
                rhs=sum((mu[k]*y**j for k,y in enumerate(nodes)),F(0))
                if cert['infinity'] and j==d:rhs+=mu[-1]
                assert functional[j]==rhs
            assert dot(functional,P)==0
            endpoint_polys[name]=(P,output[3])
        lo=F(row['lower']['endpoint']);hi=F(row['upper']['endpoint']);a,b=row['optimal_pair']
        alpha=(a+hi*b)/(hi-lo);beta=(a+lo*b)/(hi-lo)
        assert alpha>=0 and beta>=0 and alpha+beta>0 and b
        Plo,blo=endpoint_polys['lower'];Phi,bhi=endpoint_polys['upper']
        lift=[alpha*x/blo+beta*y/(-bhi) for x,y in zip(Plo,Phi)]
        assert [dot(line,lift) for line in M]==[a,0,0,b]
        epsilon=F(row['epsilon']);assert epsilon==max(a+lo*b,a+hi*b)
        assert math.gcd(a,b)==1
        union_lo=max(F(c['lo']) for c in row['head_budget_checks'])
        union_hi=min(F(c['hi']) for c in row['head_budget_checks'])
        assert union_lo<=lo<hi<=union_hi
        result.append(dict(n=n,w=w,global_endpoint_certificates=2,
            integer_form_lift_verified=True,
            all_head_budget_width_improvement=str((union_hi-union_lo)/(hi-lo)),
            epsilon=str(epsilon)))
        print('Independent certificates passed',n,w,flush=True)
    (folder/'verify_discrete_positive_cone.json').write_text(json.dumps(dict(
        scope='Independent direct-factor Fraction partial fractions, global positive dual identities, exact integer-output lifts; no zeta numerics.',
        rows=result),indent=2),encoding='utf-8')


if __name__=='__main__':main()
