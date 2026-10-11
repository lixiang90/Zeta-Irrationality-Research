"""Fixed exact certificates for endpoint-pure type-I/type-II duality.

Three prescribed dual examples, one other rational endpoint, and two
ordinary highest-log Padé examples. No numerical zeta evaluation or scan.
"""
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
import json
import sympy as S


def zero(x):
    assert S.cancel(S.expand(x)) == 0, x


def primitive(c, r):
    c, r = S.Rational(c), S.Rational(r)
    D = S.ilcm(c.q, r.q)
    v = [int(D*c), int(D*r)]
    g = gcd(abs(v[0]), abs(v[1]))
    v = [x//g for x in v]
    if v[0] < 0:
        v = [-x for x in v]
    return v


def rational_part(P, q, a, u):
    Q, rem = S.div(P, u+a, u)
    assert S.Poly(rem, u).degree() <= 0
    rat = sum(c/S.Integer(r+1)**q for (r,), c in S.Poly(Q, u).terms())
    return S.Rational(rat), S.Rational(rem)


def eta_interval(q, K=256):
    # Positive Euler differences are <=1, so the omitted tail is <=2^-K.
    total = Fraction(0)
    cumulative = 0
    for i in range(K):
        cumulative += comb(K, i)
        weight = Fraction((1 << K)-cumulative, 1 << K)
        total += (-1)**i*weight/Fraction((i+1)**q)
    return total, total+Fraction(1, 1 << K)


def catalan_interval(K=64):
    total = Fraction(0)
    cumulative = 0
    for i in range(K):
        cumulative += comb(K, i)
        weight = Fraction((1 << K)-cumulative, 1 << K)
        total += (-1)**i*weight/Fraction((2*i+1)**2)
    return total, total+Fraction(1,1 << K)


def target_ball(rat, q, vec):
    lo, hi = eta_interval(q)
    r = Fraction(int(rat.p), int(rat.q))
    c = Fraction((1 << (q-1))-1, 1 << (q-1))
    scale = Fraction(vec[0])/c
    left, right = scale*(lo+r), scale*(hi+r)
    assert left*right > 0
    sign = 1 if left > 0 else -1
    lower_abs = left if sign > 0 else -right
    exp = lower_abs.numerator.bit_length()-lower_abs.denominator.bit_length()
    if lower_abs < Fraction(2)**exp:
        exp -= 1
    assert lower_abs >= Fraction(2)**exp
    return {'Euler_terms':256, 'primitive_sign':sign,
            'primitive_absolute_value_at_least_power_of_two':exp,
            'primitive_value_strictly_exceeds_one':lower_abs > 1}


def original(s, q, u):
    return S.expand(sum((-1)**r*S.binomial(q*s, r)*S.binomial(s+r, s)**q*u**r
                        for r in range(q*s+1)))


def cauchy_det(s, q):
    d = s*q
    num = S.prod(j-i for i in range(d) for j in range(i+1, d))
    num *= S.prod((j-i)**(q*q) for i in range(s) for j in range(i+1, s))
    den = S.prod((m+r+1)**q for m in range(d) for r in range(s))
    return (-1)**(s*q*(q-1)//2)*S.Rational(num, den)


def main():
    u,w = S.symbols('u w')
    dual = []
    for n,q,a in [(2,3,1),(2,7,1),(3,7,1),(2,7,2)]:
        s = n-1
        d = q*s
        labels = [(j,r) for r in range(s) for j in range(1,q+1)]
        C0 = S.Matrix([[S.Rational(1,(m+r+1)**j) for j,r in labels]
                       for m in range(d)])
        C1 = S.Matrix([[S.Rational(1,(m+r+2)**j) for j,r in labels]
                       for m in range(d)])
        C = a*C0+C1
        v = S.Matrix([S.Rational(1,(m+1)**q) for m in range(d)])
        b = -C.inv()*v
        assert C*b+v == S.zeros(d,1)
        zero(C0.det()-cauchy_det(s,q))
        assert C.det() != 0
        A = [S.Integer(0)]*(q+1)
        for bi,(j,r) in zip(b,labels):
            A[j] += (u+a)*bi*u**r
        A[q] += 1
        for j in range(1,q+1):
            A[j] = S.expand(A[j])
            zero(A[j].subs(u,-a)-(1 if j==q else 0))
        M = 1/w**q+sum(bi*(a/(w+r)**j+1/(w+r+1)**j)
                        for bi,(j,r) in zip(b,labels))
        assert all(S.cancel(M.subs(w,m+1)) == 0 for m in range(d))

        R = original(s,q,u)
        P = S.Poly(R,u).monic().as_expr()
        for j,r in labels:
            zero(sum(c/S.Integer(k+r+1)**j for (k,),c in S.Poly(P,u).terms()))
        T = S.zeros(d)
        for m in range(d-1):
            T[m,m+1] = 1
        for m in range(d):
            T[d-1,m] = -S.Poly(P,u).nth(m)
        assert C1 == T*C0
        zero(T.charpoly(u).as_expr()-P)
        zero(C.det()/C0.det()-(-1)**d*P.subs(u,-a))
        rat_new = S.Rational(sum(bi/S.Integer(r+1)**j for bi,(j,r) in zip(b,labels)))
        rat_old, B = rational_part(R,q,a,u)
        zero(rat_new-rat_old/B)
        assert B == R.subs(u,-a) > 0
        row = {'n_typeI':n,'s_typeII':s,'q':q,'a':a,'ordinary_moments_zero':d,
               'matrix_and_endpoint_constraints':'passed',
               'Mellin_zeros':'passed','confluent_Cauchy_determinant':'passed',
               'companion_determinant_identity':'passed','target_duality':'passed',
               'R_at_minus_a':str(B),'typeI_rational_part':str(rat_new),
               'A_polynomials':[str(A[j]) for j in range(1,q+1)]}
        if a==1:
            cq=S.Rational(2**(q-1)-1,2**(q-1))
            new_vec=primitive(cq,rat_new)
            old_vec=primitive(B*cq,rat_old)
            assert new_vec==old_vec
            row.update({'canonical_primitive_identity':'passed',
                        'primitive_coefficients':[str(x) for x in new_vec],
                        'target_coefficient_bits':new_vec[0].bit_length(),
                        'exact_value_certificate':target_ball(rat_new,q,new_vec)})
        dual.append(row)

    ordinary=[]
    for s in [1,2]:
        k=7
        H=S.Matrix([[S.Rational(1,(m+r+1)**k) for r in range(s)] for m in range(s)])
        v=S.Matrix([S.Rational(1,(m+s+1)**k) for m in range(s)])
        p=-H.inv()*v
        P=u**s+sum(p[r]*u**r for r in range(s))
        assert H.det()>0
        assert all(sum(c/S.Integer(m+r+1)**k for (r,),c in S.Poly(P,u).terms())==0
                   for m in range(s))
        assert S.Poly(P,u).count_roots(0,1)==s
        D=int(S.ilcm(*[c.q for c in S.Poly(P,u).all_coeffs()]))
        assert S.Poly(D*P,u).get_domain() == S.ZZ
        rat,B=rational_part(P,k,1,u)
        ratio=S.Rational(rat/B)
        vec=primitive(S.Rational(63,64),ratio)
        Q=S.expand(D*P)
        S_int,B_int=rational_part(Q,k,1,u)
        assert B_int.q==1
        M=int(S_int.q)
        s_num=int(S_int.p)
        h=gcd(abs(63*M*int(B_int)),abs(64*s_num))
        sign_B=1 if B_int>0 else -1
        full_vec=[sign_B*63*M*int(B_int)//h,sign_B*64*s_num//h]
        assert full_vec==vec
        ball=target_ball(ratio,k,vec)
        assert ball['primitive_sign']==1
        ordinary.append({'s':s,'weight':'(-log u)^6/6!',
                         'monic_P':str(P),'minimal_coefficient_multiplier':str(D),
                         'P_at_minus_one':str(B),'orthogonality_and_Sturm':'passed',
                         'integer_Q_at_minus_one':str(B_int),
                         'reduced_rational_part_numerator':str(s_num),
                         'reduced_rational_part_denominator':M,
                         'complete_target_content':h,
                         'complete_primitive_interface':'passed',
                         'normalized_rational_part':str(ratio),
                         'primitive_coefficients':[str(x) for x in vec],
                         'target_coefficient_bits':vec[0].bit_length(),
                         'exact_value_certificate':ball})

    # Complete coefficient-level filtering of one extra integer node.
    q=7
    P=original(1,q,u)
    R=(u+2)*P
    r1,B1=rational_part(R,q,1,u)
    r2,B2=rational_part(R,q,2,u)
    rp,Bp=rational_part(P,q,1,u)
    zero(B2)
    zero(B1-Bp)
    zero(r1-r2-rp)
    # Prescribed Catalan s=1 example; all-scale positivity is a proof in the note.
    Pg=u-S.Rational(1,9)
    Qg=9*Pg
    Tg,Bg=S.div(Qg,u+1,u)
    Sg=sum(c/S.Integer(2*r+1)**2 for (r,),c in S.Poly(Tg,u).terms())
    zero(sum(c/S.Integer(2*r+1)**2 for (r,),c in S.Poly(Pg,u).terms()))
    assert Bg==-10 and Sg==9
    loG,hiG=catalan_interval()
    lo_value,hi_value=10*loG-9,10*hiG-9
    assert 0 < lo_value < hi_value < 1
    assert lo_value > Fraction(1,8) and hi_value < Fraction(1,4)
    Z3,Z5=S.symbols('Z3 Z5')
    zero(4*S.Rational(3,4)*Z3+S.Rational(16,15)*S.Rational(15,16)*Z5
         -(3*Z3+Z5))
    data={'status':'fixed_exact_mixed_pade_certificates_passed',
          'endpoint_typeI_duality':dual,'highest_log_ordinary_Pade':ordinary,
          'extra_integer_node':{'q':q,'P_degree':7,
             'R_formula':'(u+2)P(u)','R_at_minus_two':'0',
             'J1_R_minus_J2_R_equals_J1_P':'passed',
             'old_R_at_minus_two':str(P.subs(u,-2))},
          'Catalan_Markov':{'s':1,'moment_formula':'1/(2m+1)^2',
             'monic_P':str(Pg),'integer_Q':str(Qg),'B':'-10','S':'9',
             'M':1,'complete_content':1,'primitive_coefficients':['10','-9'],
             'orthogonality_and_primitive_interface':'passed',
             'Euler_terms':64,'strict_value_bounds':['1/8','1/4'],
             'strictly_positive_and_less_than_one':True},
          'fixed_combination':{'target':'3*zeta(3)+zeta(5)',
             'positive_weight':'4*w3+(16/15)*w5',
             'rational_moment_formula':'4/(m+1)^3+16/(15*(m+1)^5)',
             'exact_eta_to_zeta_identity':'passed',
             'not_claimed':'primitive decay or irrationality'},
          'no_zeta_values_numerically_evaluated':True,
          'not_proved':['irrationality','full-family primitive decay',
                        'ordinary-highest-log actual denominator asymptotics',
                        'numerical independence of Li_7(-1/2) and zeta(7)']}
    dest=Path(__file__).with_suffix('.json')
    dest.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':data['status'],'file':str(dest)}))


if __name__=='__main__':
    main()
