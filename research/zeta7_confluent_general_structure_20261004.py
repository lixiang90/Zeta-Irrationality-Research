"""Generic odd-kernel repeated-pole endpoint obstruction: exact checks."""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat

sys.set_int_max_str_digits(0)

def coefficients(s,m):
    # J_q zeta(s+l,x) coefficient = A[q][l] x^(s-1-2(q-1)+l).
    A={1:[Q(1)]}
    for q in range(1,m):
        old=A[q];new=[Q(0)]*(q+1)
        for l,c in enumerate(old):
            new[l]-=Q(s-1-2*(q-1)+l,2*q)*c
            new[l+1]+=Q(s+l,2*q)*c
        A[q+1]=new
    return A

def coefficient(s,A,q,zeta,x):
    l=zeta-s
    return Q(0) if l<0 or l>=len(A[q]) else A[q][l]*x**(s-1-2*(q-1)+l)

def highest(s,k,x):
    return Q(math.prod(range(s,s+k)),2**k*math.factorial(k))*x**(s-1-k)

def base_D(nodes):
    D=Poly([1])
    for x in nodes:D*=Poly([x*x,1])
    return D

def functional(s,A,zeta,nodes,C,p):
    derivatives=[p]
    for _ in range(len(C[0])-1):derivatives.append(derivatives[-1].derivative())
    out=Q(0)
    for x,cs in zip(nodes,C):
        r=-x*x
        for q,c in enumerate(cs,1):
            for pole in range(1,q+1):
                order=q-pole
                out+=c*coefficient(s,A,pole,zeta,x)*derivatives[order](r)/math.factorial(order)
    return out

def endpoint_value(nodes):
    a,b=nodes[0],nodes[-1]
    out=sum((x/((x*x-a*a)*(x*x-b*b)) for x in nodes[1:-1]),Q(0))
    return out-(a+b)/(b*b-a*a)**2-Q(1,4)/(a*b*(a+b))

def coefficient_matrix(s,r,nodes):
    K=len(nodes);m=r-s+1;A=coefficients(s,m);rows=[]
    for zeta in range(s,r):
        for n in range(2*K-1):
            row=[]
            for x in nodes:
                rr=-x*x
                for q in range(1,m+1):
                    value=Q(0)
                    for pole in range(1,q+1):
                        order=q-pole
                        if order<=n:value+=coefficient(s,A,pole,zeta,x)*math.comb(n,order)*rr**(n-order)
                    row.append(value)
            rows.append(row)
    return fmpq_mat(rows)

def verify(s,r,nodes):
    nodes=sorted(map(Q,nodes));K=len(nodes);k=r-s;m=k+1
    assert s>=3 and s%2==r%2==1 and k>=2 and k%2==0 and K>=2
    D=base_D(nodes);dp=D.derivative();dpp=dp.derivative();T=endpoint_value(nodes);assert T<0
    a,b=nodes[0],nodes[-1];q=D//(Poly([a*a,1])*Poly([b*b,1]));p=D*q
    layers=[]
    for kk in range(k,0,-2):
        target=s+kk;mm=kk+1;A=coefficients(s,mm);cs=[]
        for x in nodes:
            rr=-x*x;am1=highest(s,kk-1,x);cm=Q(1)/(am1*dp(rr)**2)
            lower=cm*(-dpp(rr)/dp(rr)-Q(kk+1-2*s,4)/(x*x))
            cs.append([Q(0)]*(mm-2)+[lower,cm])
        for n in range(2*K):
            test=Poly([0]*n+[1]);actual=functional(s,A,target-1,nodes,cs,test)
            assert actual==(Q(1) if n==2*K-1 else Q(0))
        obstruction=functional(s,A,target-2,nodes,cs,p)
        factor=Q(2*(kk-1),target-2)
        assert obstruction==factor*T and obstruction<0
        layers.append(dict(target=target,maximum_pole=mm,normalized_moments_checked=2*K,
                           endpoint_factor=str(factor),exact_endpoint_value=str(obstruction)))
    M=coefficient_matrix(s,r,nodes);rank=M.rank();assert rank==K*m
    return dict(base_odd_value=s,target_odd_value=r,nodes=list(map(str,nodes)),K=K,h=K,
                maximum_pole=m,matrix_rows=M.nrows(),matrix_columns=M.ncols(),matrix_rank=rank,
                endpoint_T=str(T),recursive_layers=layers)

def coefficient_checks():
    checked=0
    for s in (3,5,7):
        A=coefficients(s,12)
        for k in range(1,12):
            for x in (Q(1),Q(2),Q(7,3)):
                assert coefficient(s,A,k+1,s+k,x)==highest(s,k,x)
                assert coefficient(s,A,k+1,s+k-1,x)==highest(s,k-1,x)*Q(k+1-2*s,4)/(x*x)
                checked+=2
    # Specific mu3 fifth-pole coefficients supplied by the root derivation.
    A=coefficients(3,5);x=Q(3)
    expected={3:{4:-Q(9,8)/x,5:Q(3,2)},
              4:{4:-Q(3,16)/x**3,5:-Q(3,4)/x**2,6:Q(5,4)/x},
              5:{4:-Q(9,128)/x**5,5:-Q(9,32)/x**4,6:-Q(5,16)/x**3,7:Q(15,16)/x**2}}
    for pole,vals in expected.items():
        for zeta,v in vals.items():assert coefficient(3,A,pole,zeta,x)==v
    return dict(highest_two_coefficient_identities=checked,mu3_specific_coefficients_checked=9)

def main():
    shape_pairs=[(s,r) for s in (3,5) for r in (7,9,11)]
    node_sets=[list(range(1,K+1)) for K in range(2,9)]
    node_sets += [[1,3],[2,5,11],[1,2,4,8]]
    rows=[verify(s,r,nodes) for s,r in shape_pairs for nodes in node_sets]
    out=dict(status='general_endpoint_theorem_exact_checks_passed',scope='General written theorem plus finite exact checks; no irrationality result.',
             coefficient_checks=coefficient_checks(),records=rows,total_cases=len(rows),
             total_recursive_layers=sum(len(v['recursive_layers']) for v in rows),
             total_normalized_moments=sum(sum(l['normalized_moments_checked'] for l in v['recursive_layers']) for v in rows))
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','coefficient_checks','total_cases','total_recursive_layers','total_normalized_moments')},indent=2),flush=True)

if __name__=='__main__':main()
