"""Canonical shortest targets, direction changes, and denominator-only bounds."""
import json
import math
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from flint import arb, ctx, fmpq, fmpq_mat

from determinant_shape_probe import raw_matrix, gauss
from multiform_exterior_probe import positive_basis_bound


def probe(n,smith=False):
    scale=fmpq(math.lcm(*range(1,n+1))**7*math.factorial(n)**5,4**n)
    A=raw_matrix(n,n).transpose()*scale
    B=A.inv()
    G=[[sum((B[i,k]*B[j,k] for k in range(4)),fmpq(0)) for j in (0,3)] for i in (0,3)]
    a,b,l1,l2,steps=gauss(G)
    if a[1]<0 or (a[1]==0 and a[0]<0):a=[-x for x in a]
    cost=sum((abs(a[0]*B[0,j]+a[1]*B[3,j]) for j in range(4)),fmpq(0))
    E,_=positive_basis_bound(n)
    bound=E*cost
    detG=G[0][0]*G[1][1]-G[0][1]**2
    assert 3*l1*l1<=4*detG
    assert cost*cost<=4*l1
    denominator=math.lcm(*(int(B[i,j].denominator) for i in (0,3) for j in range(4)))
    assert l1*denominator**2>=1
    row=dict(n=n,canonical_shortest_vector=list(map(str,a)),first_norm_squared=str(l1),
             rational_upper_bound=str(bound),target_inverse_denominator=str(denominator))
    with ctx.workprec(160):
        row['upper_bound_decimal']=arb(bound).str(18)
        row['denominator_log_per_n']=(arb(denominator).log()/n).str(18)
    if smith:
        S=smith_normal_form(sp.Matrix([[int(A[i,j]) for j in range(4)] for i in range(4)]),domain=sp.ZZ)
        invariants=[abs(int(S[i,i])) for i in range(4)]
        assert all(invariants[i+1]%invariants[i]==0 for i in range(3))
        assert math.prod(invariants)==abs(int(A.det()))
        assert invariants[-1]%denominator==0
        row['smith_invariants']=list(map(str,invariants))
    return row


def main():
    rows=[probe(n,n in (4,8,16,24,32)) for n in range(2,34,2)]
    transitions=[]
    for previous,current in zip(rows,rows[1:]):
        a,b=map(int,previous['canonical_shortest_vector'])
        c,d=map(int,current['canonical_shortest_vector'])
        determinant=a*d-b*c
        transitions.append(dict(n=previous['n'],next_n=current['n'],determinant=str(determinant),changed=bool(determinant)))
    extra=[probe(n,True) for n in (48,64)]
    with ctx.workprec(160):
        lo=fmpq(10123576813076657727664936,10**25)
        hi=fmpq(10123576813076657727664937,10**25)
        x=arb((lo+hi)/2,(hi-lo)/2)
        phi=8*x*x.log()-(x-1)*(x-1).log()+(x+2)*(x+2).log()-8*(x+1)*(x+1).log()
        alpha=-7-phi
        kappa=14+fmpq(3,2)*arb(3).log()+phi
        gamma=alpha+kappa/2
    result=dict(scope='Finite direction changes do not prove infinitely many changes. Bounds allow zero forms.',
                unconditional_form_decay=gamma.str(23),rows=rows,transitions=transitions,extra_arithmetic_cases=extra)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(decay=result['unconditional_form_decay'],transitions=len(transitions),
                          changed=sum(t['changed'] for t in transitions),
                          denominator_rates=[dict(n=r['n'],rate=r['denominator_log_per_n']) for r in rows+extra if 'smith_invariants' in r],
                          last_bound=rows[-1]['upper_bound_decimal'])),flush=True)


if __name__=='__main__':main()
