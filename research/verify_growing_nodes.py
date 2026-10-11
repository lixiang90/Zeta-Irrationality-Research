"""Independent finite checks for full integer-valued spaces and new nodes."""
import json,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,fmpz_mat
from sympy import Poly,Symbol,Rational,oo,primerange
from rational_square_nodes import node_list,product,entries_nodes,pole
from growing_integer_space import basis,coordinates,lattice_index
from joint_exact import entries_from_polynomial,Dcache,content
from two_prefix_outer import vp


def check_poly(row):
    K,N,M,h=(row[k] for k in ('K','N','M','h'));nodes=node_list(K,row['kind'])
    if 'Q' in row:W=product(nodes[:N])**8*fmpq_poly([fmpq(c) for c in row['Q']])**2
    else:W=product(nodes[:N])**6*product(nodes[:M])**2
    aa,bb,_=entries_nodes(nodes,W,h)
    P=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])*fmpq(row['content'])
    den=math.lcm(*(int(c.q) for c in aa+bb));scale=den**h
    for x in range(h+1):
        A=fmpz_mat(h,h,[int(den*(aa[i+j]+x*bb[i+j])) for i in range(h) for j in range(h)])
        assert A.det()==P(x)*scale
    return dict(K=K,kind=row['kind'],label=row['label'],specializations=h+1)


def index_formula(N,L):
    num=math.prod(math.comb(L,k) for k in range(1,L+1))
    num*=math.prod((j-i)*(2*N+L+1+i+j) for i in range(L+1) for j in range(i+1,L+1))
    den=fmpq(math.factorial(L)**(2*L)*2**(L-1),math.prod(math.factorial(2*i) for i in range(1,L)))
    value=fmpq(num)/den;assert value.q==1
    return int(value)


def half_local(K,N,M,p):
    ns=node_list(K,'half');h=K-M;W=product(ns[:N])**6*product(ns[:M])**2
    aa,bb,T=entries_nodes(ns,W,h);groups={}
    for a in ns[M:]:
        r=int(a.p)*pow(int(a.q),-1,p)%p;c=min(r,p-r);groups.setdefault(c,[]).append(a)
    bs=[];weights=[]
    for c,ls in sorted(groups.items()):
        part=product(ls);v=T//part;assert v*part==T
        if len(ls)==2:
            bs.extend([v,v*fmpq_poly([ls[-1]**2,1])]);weights.extend([-8,0])
        else:
            assert len(ls)==1;bs.append(v);weights.append(-1 if c==0 else 0)
    C=fmpq_mat(h,h,[b[j] for b in bs for j in range(h)]);assert vp(C.det(),p)==0
    count=0
    for values in (aa,bb):
        H=fmpq_mat(h,h,[values[i+j] for i in range(h) for j in range(h)]);H=C*H*C.transpose()
        for i in range(h):
            for j in range(h):
                if H[i,j]:assert 2*vp(H[i,j],p)>=weights[i]+weights[j]
                count+=1
    assert sum(weights)==4*p-8*K+3
    return dict(K=K,N=N,M=M,p=p,entries_checked=count,lower=sum(weights))


def main():
    folder=Path(__file__).parent;nodes=[];spaces=[];checks=[];root_rows=[];x=Symbol('t')
    for K in (24,48,96):
        rows=json.loads((folder/f'rational_square_nodes_K{K}.json').read_text())['rows'];nodes+=rows
        N,L=K//24,K//8
        data=json.loads((folder/f'growing_integer_space_K{K}_L{L}_integer.json').read_text());spaces+=data['rows']
        assert index_formula(N,L)==int(data['translated_block_lattice']['index'])
        assert abs(int(fmpz_mat(data['lll_transform']).det()))==1
        for r in data['rows']:
            Q=fmpq_poly([fmpq(c) for c in r['Q']]);assert Q[L]==1
            cc=coordinates(Q/math.factorial(L)**2);assert all(v.q==1 for v in cc)
        r=next((r for r in data['rows'] if r['label']=='lll'),data['rows'][1]);Q=fmpq_poly([fmpq(c) for c in r['Q']])
        P=Poly(sum(Rational(int(c.p),int(c.q))*x**i for i,c in enumerate(Q)),x)
        intervals=P.intervals(eps=Rational(1,10**8));positive=P.count_roots(0,oo)
        assert positive==L and all(m==1 and a>0 for (a,b),m in intervals)
        root_rows.append(dict(K=K,L=L,label=r['label'],positive_roots=int(positive),
                              intervals=[[str(a),str(b)] for (a,b),m in intervals],
                              scaled_min=float(intervals[0][0][0]/K**2),scaled_max=float(intervals[-1][0][1]/K**2)))
    extra=[]
    for kind in ('half','dense_half'):
        extra+=json.loads((folder/f'growing_integer_space_K24_L3_{kind}.json').read_text())['rows']
    for K in (24,48,96):
        extra+=json.loads((folder/f'retained_prefix_space_K{K}.json').read_text())['rows']
        extra+=json.loads((folder/f'growing_congruence_space_K{K}.json').read_text())['rows']
    extra+=json.loads((folder/'growing_space_vertical_shifts.json').read_text())['rows']
    for r in extra:
        K,N,M=(r[k] for k in ('K','N','M'));L=M-N;Q=fmpq_poly([fmpq(c) for c in r['Q']]);assert Q[L]==1
        retained=r.get('retained',0);fixed=fmpq_poly(Dcache(N+retained)//Dcache(N));R=Q//fixed;d=L-retained
        assert R*fixed==Q and all(v.q==1 for v in coordinates(R/math.factorial(d)**2))
        if 'modulus' in r:assert all(int(u)%r['modulus']==0 for u in r['parameters'])
    for r in nodes+spaces+extra:
        P=fmpq_poly([fmpq(c) for c in r['primitive_polynomial']]);assert content(P)==1 and P.degree()==r['degree']
    for K,kind in [(24,'half'),(24,'dense_half'),(48,'half')]:
        checks.append(check_poly(next(r for r in nodes if r['K']==K and r['M']==K//6 and r['kind']==kind)))
    for K,label in [(24,'naive'),(48,'lll')]:checks.append(check_poly(next(r for r in spaces if r['K']==K and r['label']==label)))
    for K,label in [(24,'modulus_60'),(48,'retained_4_lll')]:checks.append(check_poly(next(r for r in extra if r['K']==K and r['label']==label)))
    checks.append(check_poly(next(r for r in extra if r['K']==24 and r['kind']=='dense_half' and r['label']=='naive')))
    # Integer-node engine agrees exactly, entry by entry, with the old engine.
    W=fmpq_poly(Dcache(1))**6*fmpq_poly(Dcache(4))**2
    aa,bb,T=entries_nodes(node_list(24,'integer'),W,20)
    assert (aa,bb)==entries_from_polynomial(24,W,20)
    # Integer-valued triangular basis, including negative integer inputs.
    ivchecks=0
    for i in range(13):
        q=basis(i)
        for a in range(-30,31):assert q(-a*a).q==1;ivchecks+=1
        assert q(-i*i)==1 and all(q(-a*a)==0 for a in range(i))
    # Complementary shifts: the coefficient of Z(a)-Z(1-a) is positive.
    paired=[]
    for q in (3,4,6):
        for K in (4,8,12):
            ns=[fmpq(j)+a for j in range(K//2) for a in (fmpq(1,q),fmpq(q-1,q))]
            D=product(ns);deriv=D.derivative();weights=[]
            for i,a in enumerate(ns):
                c=fmpq(1 if i%2==0 else -1,2)*a**6/deriv(-a*a)
                assert c>0;weights.append(str(c))
            paired.append(dict(q=q,poles=K,positive_weights=weights))
    # The observed sharp exterior valuation for pure half nodes is recorded
    # as finite evidence, not asserted as a theorem for all K.
    exterior=[]
    for r in nodes:
        if r['kind']!='half':continue
        K,M=r['K'],r['M'];ct=fmpq(r['content'])
        for p in primerange(K+M+1,2*K):
            actual=vp(ct,p);bound=4*p-8*K+3
            assert actual==bound,(K,M,p,actual,bound)
            exterior.append(dict(K=K,M=M,p=int(p),valuation=actual))
    result=dict(node_records=len(nodes),space_records=len(spaces),additional_space_records=len(extra),integer_value_checks=ivchecks,
                integer_engine_entries=2*len(aa),full_polynomial_checks=checks,
                independent_integer_determinants=sum(r['specializations'] for r in checks),
                root_certificates=root_rows,paired_shift_certificates=paired,half_exterior_checks=exterior,
                half_local_bases=[half_local(24,1,4,29),half_local(24,1,4,47),half_local(48,2,8,59)])
    (folder/'growing_nodes_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['paired_shift_certificates','half_exterior_checks','root_certificates']}
                    |dict(roots=[{k:r[k] for k in ['K','L','positive_roots','scaled_min','scaled_max']} for r in root_rows],half_exterior_count=len(exterior))),flush=True)


if __name__=='__main__':main()
