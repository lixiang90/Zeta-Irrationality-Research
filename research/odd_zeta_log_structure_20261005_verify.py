"""Fixed exact certificates for the confluent JP/Cauchy/polylog bridge.

No period evaluation, parameter search, or irrationality assertion.
"""
from pathlib import Path
import json
import sympy as S


def zero(expr):
    assert S.cancel(S.expand(expr)) == 0, expr


def candidate(n, q, z):
    return S.expand(sum((-1)**r*S.binomial(q*n, r)*S.binomial(n+r,n)**q*z**r
                        for r in range(q*n+1)))


def theta(expr, z):
    return S.cancel(z*S.diff(expr,z))


def op_shift(expr, shift, z):
    return S.cancel(theta(expr,z)+shift*expr)


def scalar_L(expr, n, q, z, theta_fn):
    lhs = expr
    for _ in range(q+1):
        lhs = theta_fn(lhs)
    rhs = expr
    for _ in range(q):
        rhs = S.cancel(theta_fn(rhs)+(n+1)*rhs)
    rhs = S.cancel(theta_fn(rhs)-q*n*rhs)
    return S.cancel(lhs-z*rhs)


def correction(R, j, z):
    return S.expand(sum(c*sum(z**(r-l)/S.Integer(l)**j for l in range(1,r+1))
                        for (r,),c in S.Poly(R,z).terms() if r>0))


def main():
    z,w,e = S.symbols('z w e')
    out = []
    for n,q in [(1,2),(1,3),(1,7)]:
        N=n*q
        R=candidate(n,q,z)
        zero(scalar_L(R,n,q,z,lambda f:theta(f,z)))
        R1=(-1)**N*S.factorial(N)/S.factorial(n)**q
        zero(R.subs(z,1)-R1)
        assert R1 != 0
        C=(-1)**N*S.factorial(N)/S.factorial(n)**q
        M=C*S.prod((w-j)**q for j in range(1,n+1))/S.prod(w+r for r in range(N+1))
        zero((w+N+1)*(w-n)**q*M.subs(w,w+1)-w**(q+1)*M)
        source=S.cancel((e+N+1)*(n-e)**q*M.subs(w,e+1))
        assert all(S.diff(source,e,j).subs(e,0)==0 for j in range(q))
        assert S.diff(source,e,q).subs(e,0) != 0
        root_count=int(S.Poly(R,z).count_roots(0,1))
        assert root_count==N and S.gcd(R,S.diff(R,z))==1

        sj=[None]+[correction(R,j,z) for j in range(1,q+1)]
        Q,B=S.div(R,1+z,z)
        rat=sum(c/S.Integer(r+1)**q for (r,),c in S.Poly(Q,z).terms())
        zero(sj[q].subs(z,-1)-rat)
        assert B==R.subs(z,-1)>0

        A=S.zeros(q+1)
        A[1,0]=-1/(z*(z-1))
        for j in range(2,q+1):
            A[j,j-1]=-1/z
        T=S.eye(q+1)
        for j in range(1,q+1):
            T[j,0]=-sj[j]
            T[j,j]=R
        Bmat=S.simplify((T.diff(z)+T*A)*T.inv())
        rR=S.cancel(S.diff(R,z)/R)
        expected=S.zeros(q+1)
        expected[1,0]=rR*sj[1]-S.diff(sj[1],z)-R/(z*(z-1))
        expected[1,1]=rR
        for j in range(2,q+1):
            expected[j,0]=rR*sj[j]-S.diff(sj[j],z)-sj[j-1]/z
            expected[j,j-1]=-1/z
            expected[j,j]=rR
        for entry in Bmat-expected:
            zero(entry)

        rank_det = None
        scalar_log_basis = []
        if q in [2,3]:
            rows=[]
            row=S.zeros(1,q+1)
            row[0,0]=-sj[q]
            row[0,q]=R
            for j in range(q+1):
                rows.append(row)
                row=S.simplify(row.diff(z)+row*A)
            actual=S.cancel(S.Matrix.vstack(*rows).det(method='domain-ge'))
            b=S.cancel(sj[q]/R)
            theta_b=b
            for _ in range(q):
                theta_b=theta(theta_b,z)
            claimed=S.cancel(R**(q+1)/z**(q*(q+1)//2)
                               *(1/(z-1)-(-1)**q*theta_b))
            zero(actual-claimed)
            assert actual != 0
            rank_det=str(S.factor(actual))

            L=S.symbols('L')
            v=S.symbols('v1:'+str(q+1))
            def formal_theta(expr):
                val=z*S.diff(expr,z)+S.diff(expr,L)
                val-=S.diff(expr,v[0])/(z-1)
                for j in range(1,q):
                    val-=S.diff(expr,v[j])*v[j-1]
                return S.cancel(S.expand(val))
            for j in range(q):
                gj=(-1)**j*sum(L**(j-l)/S.factorial(j-l)*(R*v[l]-sj[l+1])
                               for l in range(j+1))
                zero(scalar_L(gj,n,q,z,formal_theta))
                scalar_log_basis.append({'j':j,'L_gj_identity':'passed'})

        out.append({'n':n,'q':q,'N':N,'R':str(R),'R_at_one':str(R1),
                    'R_minus_one':str(B),'scalar_polynomial_ODE':'passed',
                    'Mellin_shift_recurrence':'passed',
                    'epsilon_source_order_exact':q,
                    'interior_roots_Sturm':root_count,
                    'polylog_rational_gauge_identity':'passed',
                    'target_rational_part_at_minus_one':str(rat),
                    'D_jet_cyclic_determinant':rank_det,
                    'log_normalized_scalar_solutions':scalar_log_basis})

    data={'status':'fixed_exact_structure_certificates_passed',
          'cases':out,'no_period_values_computed':True,
          'not_a_computational_claim':['strong remainder asymptotics',
           'all-n endpoint nonzero','integer primitive decay','irrationality']}
    dest=Path(__file__).with_suffix('.json')
    dest.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'status':data['status'],'file':str(dest)}))


if __name__=='__main__':
    main()
