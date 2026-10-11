"""Exact audit of the general h >= K triple-pole degeneration theorem.

The theorem applies to a common numerator and the full initial monomial
Gram space. It does not apply to arbitrary K-dimensional polynomial spaces.
"""
import json, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat

sys.set_int_max_str_digits(0)

def base_polynomial(nodes):
    D=Poly([1])
    for x in nodes:D*=Poly([x*x,1])
    return D

def hermite_S_and_inverse(nodes,D):
    modulus=D**2;S=Poly([0]);dp=D.derivative();dpp=dp.derivative()
    for x in nodes:
        r=-x*x;factor=Poly([x*x,1])**2;E=modulus//factor
        g,inv,_=E.xgcd(factor);assert g==1
        value=Q(5,2)*x**3/dp(r)
        derivative=(-Q(35,4)*x-dpp(r)*value)/(2*dp(r))
        S+=(Poly([value])+derivative*Poly([x*x,1]))*E*inv
    S%=modulus
    g,U,_=S.xgcd(modulus);assert g==1
    U%=modulus;assert (S*U)%modulus==1
    for x in nodes:
        r=-x*x
        assert U(r)==Q(2,5)*dp(r)/x**3
        assert U.derivative()(r)==dpp(r)/(5*x**3)+Q(7,10)*dp(r)/x**5
    return S,U

def constraint_matrix(nodes):
    K=len(nodes);rows=[]
    for zeta in (5,6):
        for s in range(2*K-1):
            row=[]
            for x in nodes:
                r=-x*x;power=r**s
                row.extend([power*r*r,power*(s+2)*r,power*Q((s+1)*(s+2),2)] if zeta==5 else
                           [Q(0),power*Q(5,2)*x**3,-power*Q(35+20*s,8)*x])
            rows.append(row)
    return fmpq_mat(rows)

def verify_case(nodes):
    nodes=sorted(map(Q,nodes));K=len(nodes)
    assert K>=2 and all(x>0 for x in nodes) and len(set(map(str,nodes)))==K
    D=base_polynomial(nodes);dp=D.derivative();dpp=dp.derivative()
    S,U=hermite_S_and_inverse(nodes,D)
    coefficients=[]
    for x in nodes:
        r=-x*x;C3=Q(2,5)/(x**3*dp(r)**2)
        C2=C3*(-dpp(r)/dp(r)+Q(7,4)/(x*x))
        coefficients.append((Q(0),C2,C3))
    # Normalize the unique zeta6 jet direction by its 2K-1 moment equal to 1.
    checked=0
    for s in range(2*K):
        moment=sum(((-x*x)**s*(Q(5,2)*x**3*C2-Q(35+20*s,8)*x*C3)
                    for x,(_,C2,C3) in zip(nodes,coefficients)),Q(0))
        assert moment==(Q(1) if s==2*K-1 else Q(0));checked+=1
    a,b=nodes[0],nodes[-1]
    q=D//(Poly([a*a,1])*Poly([b*b,1]));p=D*q
    assert q.degree()==K-2 and p.degree()==2*K-2
    p1,p2=p.derivative(),p.derivative().derivative()
    zeta5=sum(((2*r*C2+C3)*p(r)+(r*r*C2+2*r*C3)*p1(r)+r*r*C3*p2(r)/2
               for x,(_,C2,C3) in zip(nodes,coefficients) for r in (-x*x,)),Q(0))
    T=sum((x/((x*x-a*a)*(x*x-b*b)) for x in nodes[1:-1]),Q(0))
    T-=(a+b)/(b*b-a*a)**2+Q(1,4)/(a*b*(a+b))
    assert T<0 and zeta5==Q(2,5)*T
    rank=constraint_matrix(nodes).rank();assert rank==3*K
    return dict(nodes=list(map(str,nodes)),K=K,h=K,coefficient_matrix_rows=4*K-2,
                coefficient_matrix_rank=rank,unique_zeta6_direction_moments_checked=checked,
                endpoint_test_polynomial_degree=p.degree(),strict_negative_obstruction=str(T),
                exact_zeta5_endpoint_test=str(zeta5),
                degree_S=S.degree(),degree_modular_inverse_U=U.degree(),
                exact_modular_inverse_identity=True,
                common_zeta_interpretation='integer nodes' if all(x.q==1 for x in nodes) else 'formal jet equations only')

def single_node_exception():
    nodes=[Q(1)];M=constraint_matrix(nodes);assert M.rank()==2
    W=Poly([21,27,10]);z=Poly([1,1])
    assert W==10*z*z+7*z+4
    # C1=10,C2=7,C3=4. All harmonic constants are H_0=0.
    assert 10-2*7+4==0 and Q(5,2)*7-Q(35,8)*4==0
    constant=10*(-Q(3,4))+7*(-Q(1,4))+4*(-Q(3,16))
    slope=4*Q(15,4)
    assert constant==-10 and slope==15
    return dict(K=1,h=1,constraint_matrix_rank=2,proper_nonzero_kernel_dimension=1,
                positive_numerator=list(map(str,W)),unscaled_target_constant=str(constant),
                unscaled_target_slope=str(slope),primitive_target_polynomial=['-2','3'])

def main():
    cases=[list(range(1,K+1)) for K in range(2,21)]
    cases += [[1,3],[2,5,11],[1,2,4,8],[2,3,7,11,19,23],
              [1,3,7,13,21,31,43,57],[3,8,19,37,61,113],
              [Q(1,2),Q(3,2)],[Q(1,3),Q(2,3),Q(4,3)]]
    rows=[verify_case(nodes) for nodes in cases]
    out=dict(status='general_theorem_finite_exact_checks_passed',scope='General written proof plus finite checks; no irrationality result.',
             cases=rows,total_node_sets=len(rows),total_moment_checks=sum(r['unique_zeta6_direction_moments_checked'] for r in rows),
             single_node_exception=single_node_exception())
    target=Path(__file__).with_suffix('.json');target.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps(dict(status=out['status'],node_sets=out['total_node_sets'],moment_checks=out['total_moment_checks'],
                          consecutive_K_range=[2,20],single_node_exception=out['single_node_exception']),indent=2),flush=True)

if __name__=='__main__':main()
