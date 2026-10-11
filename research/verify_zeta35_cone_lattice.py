"""Independent residue audit of positive cone certificates, without zeta values.

Unlike the producer's basis-wise product series, this expands each complete
numerator and divides its Taylor series by the complete local denominator.
"""
import json
import math
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly


def direct_image(N,M,shift,coeffs):
    assert all(v>=0 for v in coeffs) and any(coeffs)
    p=Poly()
    y=Poly([-shift,N,1])
    for c in reversed(coeffs):
        p=p*y+c
    for k in range(1,M+1):
        p*=Poly([-k*(N+k),N,1])
    D=Poly([1])
    for j in range(N+1):
        D*=Poly([j,1])**5
    assert p.degree()<=D.degree()-2
    deriv=[p]
    for _ in range(4):
        deriv.append(deriv[-1].derivative())
    total=[Q(0)]*6;constant=Q(0)
    H=[Q(0)]*6
    for j in range(N+1):
        if j:
            for s in range(1,6):
                H[s]+=Q(1,j**s)
        E,rem=divmod(D,Poly([j,1])**5);assert not rem
        ed=[E]
        for _ in range(4):
            ed.append(ed[-1].derivative())
        num=[deriv[k](-j)/math.factorial(k) for k in range(5)]
        den=[ed[k](-j)/math.factorial(k) for k in range(5)]
        local=[]
        for k in range(5):
            local.append((num[k]-sum((den[i]*local[k-i] for i in range(1,k+1)),Q(0)))/den[0])
        for s in range(1,6):
            total[s]+=local[5-s]
            constant-=local[5-s]*H[s]
    assert total[1]==total[2]==total[4]==0
    return [total[5],total[3],constant]


def main():
    root=Path(__file__).parent
    lattice=json.loads((root/'zeta35_cone_lattice.json').read_text(encoding='utf-8'))['rows']
    cones=json.loads((root/'zeta35_positive_cone.json').read_text(encoding='utf-8'))['cases']
    audits=[]
    for N in (10,20,40,80):
        record=max((r for r in lattice if r['N']==N),key=lambda r:r['d'])
        case=next(c for c in cones if c['N']==N and c['d']==record['d'])
        M=record['M'];shift=case['shift'];degree=record['d']
        a,c=Q(record['a']),Q(record['c'])
        lo,hi=Q(record['lower']),Q(record['upper'])
        for side,scale in zip(('lower','upper'),record['endpoint_normalizations']):
            ray=case['endpoints'][side]['ray'];p=[Q(0)]*(degree+1)
            p[ray['i']]+=Q(ray['u'])*Q(scale);p[ray['j']]+=Q(ray['v'])*Q(scale)
            ra,rc=Q(ray['a']),Q(ray['c'])
            assert direct_image(N,M,shift,p)==[ra,3*ra,rc]
            assert (ra>0 if side=='lower' else ra<0)
            assert -rc/ra==(lo if side=='lower' else hi)
        p=[Q(v) for v in record['positive_polynomial_coefficients']]
        assert direct_image(N,M,shift,p)==[a,3*a,c]
        bound=a*(hi if a>=0 else lo)+c
        assert bound==Q(record['strict_error_upper']) and bound>0
        exclusion=int((1/bound).floor())+1
        assert str(exclusion)==record['rational_denominator_at_least']
        exponent=0
        while bound<Q(1,10**(exponent+1)):
            exponent+=1
        audits.append(dict(N=N,d=degree,independent_residue_checks=3,
                           uses_zeta_evaluation=False,
                           strict_error_less_than_10_to_minus=exponent,
                           rational_denominator_at_least=str(exclusion)))
        print('verified without zeta digits',N,degree,'L < 10^-'+str(exponent),flush=True)
    (root/'verify_zeta35_cone_lattice.json').write_text(json.dumps(dict(status='passed',audits=audits),indent=2),encoding='utf-8')


if __name__=='__main__':
    main()
