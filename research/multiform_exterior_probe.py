"""Common integral four-form basis and exact exterior elimination costs."""
import itertools
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq, fmpq_mat

from critical_lift_probe import cross, output_map


def positive_basis_bound(n):
    """Rational upper bound for all four positive sums, no zeta evaluation."""
    cutoff=10*n
    scale=math.lcm(*range(1,n+1))**7*math.factorial(n)**5
    partial=sum((fmpq(scale*math.prod(t-j for j in range(1,n+1))
                      *math.prod(t+n+j for j in range(1,n+1))*(2*t+n)**6,
                      math.prod((t+j)**7 for j in range(n+1)))
                 for t in range(n+1,cutoff)),fmpq(0))
    exponent=5*n+1
    prefactor=scale*fmpq(cutoff+2*n,cutoff)**(2*n)*fmpq(2*cutoff+n,cutoff)**6
    tail=prefactor*(fmpq(1,cutoff**exponent)+fmpq(1,(exponent-1)*cutoff**(exponent-1)))
    return partial+tail,cutoff


def reduced_target_basis(rows, values, n, exact_bound):
    inverse=fmpq_mat(rows).inv()
    v=[[inverse[i,j] for j in range(4)] for i in (0,3)]
    gram=[[sum((v[i][k]*v[j][k] for k in range(4)),fmpq(0)) for j in range(2)] for i in range(2)]
    def dot(a,b):
        return sum((a[i]*gram[i][j]*b[j] for i in range(2) for j in range(2)),fmpq(0))
    first,second=[1,0],[0,1]
    steps=0
    while True:
        if dot(second,second)<dot(first,first):
            first,second=second,first
        ratio=dot(first,second)/dot(first,first)
        if abs(ratio)<=fmpq(1,2):
            break
        rounded=ratio+fmpq(1,2)
        m=int(rounded.numerator)//int(rounded.denominator)
        second=[second[i]-m*first[i] for i in range(2)]
        steps+=1
        assert steps<10000
    assert abs(first[0]*second[1]-first[1]*second[0])==1
    costs=[]
    for a,b in (first,second):
        u=[a*v[0][j]+b*v[1][j] for j in range(4)]
        assert all(sum((u[i]*rows[i][j] for i in range(4)),fmpq(0))==target
                   for j,target in enumerate((a,0,0,b)))
        costs.append(sum(abs(x) for x in u))
    mu=max(costs)
    squared_second=dot(second,second)
    with ctx.workprec(max(abs(x).bit_length() for pair in (first,second) for x in pair)+512):
        exact_values=[(arb(a)+arb(b)*arb(7).zeta()).str(22) for a,b in (first,second)]
        lower=arb(squared_second).sqrt()
        upper=arb(mu)
        assert upper<=2*lower
        assert arb(exact_bound)>=max(values)
        rational_triangle=mu*exact_bound
        return dict(output_basis=[list(map(str,first)),list(map(str,second))],
                    determinant=str(first[0]*second[1]-first[1]*second[0]),gauss_steps=steps,
                    l1_cost_upper=str(mu),l2_second_minimum_squared=str(squared_second),
                    l2_first_minimum_squared=str(dot(first,first)),
                    metric_determinant=str(gram[0][0]*gram[1][1]-gram[0][1]**2),
                    log_l1_cost_upper_per_n=(upper.log()/n).str(18),
                    log_l1_second_minimum_lower_per_n=(lower.log()/n).str(18),
                    rational_triangle_bound=str(rational_triangle),
                    certified_triangle_bound=arb(rational_triangle).str(22),
                    actual_values=exact_values)


def probe(n):
    out,local=output_map(n,head=n)
    dn=math.lcm(*range(1,n+1))
    rational_scale=fmpq(math.factorial(n)**5,4**n)
    common=rational_scale*dn**7
    # Verify the stronger local arithmetic statement, not just final integrality.
    local_checks=0
    for pole in local:
        for col in pole:
            for k in range(1,8):
                assert (col[k]*rational_scale*dn**(7-k)).denominator==1
                local_checks+=1
    rows=[[out[k][i]*common for k in (0,3,5,7)] for i in range(4)]
    assert all(a.denominator==1 for row in rows for a in row)
    rows=[[int(a) for a in row] for row in rows]
    det=fmpq_mat(rows).det()
    assert det
    exact_bound,cutoff=positive_basis_bound(n)
    candidates=[]
    for support in itertools.combinations(range(4),3):
        c=cross([rows[i][1] for i in support],[rows[i][2] for i in support])
        result=[sum(c[j]*rows[i][k] for j,i in enumerate(support)) for k in range(4)]
        assert result[1]==result[2]==0
        if result[0]==result[3]==0:
            continue
        g=math.gcd(result[0],result[3])
        pair=[result[0]//g,result[3]//g]
        cost=fmpq(sum(abs(x) for x in c),g)
        candidates.append(dict(support=list(support),primitive_pair=list(map(str,pair)),
                               coefficients=list(map(str,c)),output_content=str(g),
                               effective_multiplier_l1=str(cost)))
    independent=[]
    for i,j in itertools.combinations(range(len(candidates)),2):
        a,b=map(int,candidates[i]['primitive_pair'])
        c,d=map(int,candidates[j]['primitive_pair'])
        if a*d-b*c:
            cost=max(fmpq(candidates[i]['effective_multiplier_l1']),fmpq(candidates[j]['effective_multiplier_l1']))
            independent.append((cost,i,j))
    assert independent
    cost,i,j=min(independent)
    precision=max(abs(a).bit_length() for row in rows for a in row)+512
    with ctx.workprec(precision):
        periods=[arb(1)]+[arb(k).zeta() for k in (3,5,7)]
        values=[sum((arb(a)*x for a,x in zip(row,periods)),arb(0)) for row in rows]
        assert all(v>0 for v in values)
        for candidate in candidates:
            a,b=map(int,candidate['primitive_pair'])
            # Candidate coefficients can be much larger than the common basis.
            with ctx.workprec(max(abs(a).bit_length(),abs(b).bit_length())+512):
                v=arb(a)+arb(b)*arb(7).zeta()
                assert not v.contains(0)
                candidate['primitive_value']=v.str(22)
                candidate['log_abs_value_per_n']=(abs(v).log()/n).str(18)
        logs=[(v.log()/n).str(18) for v in values]
        logcost=(arb(cost).log()/n).str(18)
        target_basis=reduced_target_basis(rows,values,n,exact_bound)
        if n==32:
            assert fmpq(target_basis['rational_triangle_bound'])<fmpq(2,10**58)
    return dict(n=n,local_integrality_checks=local_checks,common_scale=str(common),
                integer_basis=[[str(x) for x in row] for row in rows],determinant=str(det),
                common_form_log_values_per_n=logs,candidates=candidates,
                best_independent_candidate_pair=[i,j],effective_pair_cost=str(cost),
                log_effective_pair_cost_per_n=logcost,
                target_second_minimum=target_basis,
                basis_bound=dict(cutoff=cutoff,upper=str(exact_bound)),
                note='The pair is optimal only among these four cofactor candidates, not among all rational combinations.')


def saddle_certificate():
    lo=fmpq(10123576813076657727664936,10**25)
    hi=fmpq(10123576813076657727664937,10**25)
    poly=lambda x:(x-1)*(x+1)**8-x**8*(x+2)
    assert poly(lo)<0<poly(hi)
    with ctx.workprec(192):
        x=arb((lo+hi)/2, (hi-lo)/2)
        phi=8*x*x.log()-(x-1)*(x-1).log()+(x+2)*(x+2).log()-8*(x+1)*(x+1).log()
        assert phi < arb(fmpq(-77824,10000))
        return dict(root_interval=[str(lo),str(hi)],phi=phi.str(23),
                    decay_exponent=(-7-phi).str(23),coefficient_height_upper_exponent=(7+11*arb(2).log()).str(23))


def main():
    rows=[]
    for n in (4,8,16,24,32):
        row=probe(n);rows.append(row)
        print(json.dumps({k:row[k] for k in ('n','common_form_log_values_per_n','log_effective_pair_cost_per_n')}),flush=True)
    result=dict(scope='Exact finite integral bases and four cofactor candidates; no global optimization claim.',
                saddle=saddle_certificate(),rows=rows,
                local_integrality_checks=sum(r['local_integrality_checks'] for r in rows))
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result['saddle']),flush=True)


if __name__=='__main__':main()
