"""Primitive affine charts: a genuine existence bound via unbiased rounding.

Fix u_j=1, impose local linear congruences on the remaining coordinates, and
write u=a+zV. Then every integer z gives a primitive admissible hyperplane.
The exact integer-valued quadratic fixed divisor and an Arb upper bound
certify an existence statement for this entire family.
"""
import argparse
import json
from math import gcd, prod
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpz_mat, fmpq_poly, nmod_mat, arb, ctx
from arithmetic_subspaces import (integer_pencil, adjugate_coefficients, rational_metric,
                                 radical, congruence_kernel, normal_result, adjugate_conditions)
from sympy import primerange


def affine_chart(m, j, conditions):
    cols = [k for k in range(m) if k != j]; n = m-1
    L = fmpz_mat([[int(i == k) for k in range(n)] for i in range(n)])
    a = fmpz_mat(1, n)
    for p, R in conditions:
        d = R.ncols()
        C = nmod_mat(d, n, [int(R[k,i]) for i in range(d) for k in cols], p)
        b = nmod_mat(d, 1, [-int(R[j,i]) % p for i in range(d)], p)
        Cnew = C*nmod_mat(n, n, [int(x) % p for x in L.transpose().entries()], p)
        rhs = b-C*nmod_mat(n, 1, [int(x) % p for x in a.entries()], p)
        aug = nmod_mat(d, n+1, [int(Cnew[i,k]) if k < n else int(rhs[i,0])
                                    for i in range(d) for k in range(n+1)], p)
        rr, rank = aug.rref(); z = [0]*n
        for i in range(rank):
            pivot = next(k for k in range(n+1) if rr[i,k])
            if pivot == n:
                return None
            z[pivot] = int(rr[i,n])
        a += fmpz_mat(1, n, z)*L
        L = (congruence_kernel(Cnew, p)*L).hnf()
    return cols, a, L


def evaluate(poly, z):
    result = arb(0)
    for c in reversed(list(poly)):
        result = result*z+arb(c)
    return result


def chart_result(K, A, B, det, coefficients, dual, j, conditions, label,
                 condition_kind='ambient_radical', uniform_content=1, chart_override=None):
    m = A.nrows(); n = m-1
    chart = affine_chart(m, j, conditions) if chart_override is None else chart_override
    if chart is None:
        return None
    cols, a, L = chart
    Hss = fmpz_mat(n, n, [dual[r,c] for r in cols for c in cols])
    reduced, T = (L*Hss*L.transpose()).lll(rep='gram', gram='exact', transform=True)
    L = T*L
    assert reduced == L*Hss*L.transpose() and abs(T.det()) == 1
    full_a = [1 if k == j else int(a[0,cols.index(k)]) for k in range(m)]
    V = fmpq_mat(n, m, [0 if k == j else int(L[i,cols.index(k)]) for i in range(n) for k in range(m)])
    av = fmpq_mat(1, m, full_a)
    fixed = 0; trace_coefficients = []; matrices = []
    for H in coefficients:
        M = V*H*V.transpose(); b = V*H*av.transpose(); c = (av*H*av.transpose())[0,0]
        matrices.append(M)
        values = [c]
        values += [M[i,i]+2*b[i,0] for i in range(n)]
        values += [2*M[i,i] for i in range(n)]
        values += [2*M[i,k] for i in range(n) for k in range(i+1,n)]
        assert all(x.q == 1 for x in values)
        for value in values:
            fixed = gcd(fixed, abs(int(value.p)))
        trace_coefficients.append(sum((M[i,i] for i in range(n)), fmpq(0))/4)
    assert fixed > 0
    if condition_kind=='adjugate_kernel':
        assert fixed % (uniform_content*prod(p for p,R in conditions)) == 0
    trace = fmpq_poly(trace_coefficients)
    jj = fmpq_poly([A[j,j], B[j,j]])
    bits = max(abs(int(c.p)).bit_length() for P in [det, trace, jj] for c in P)+600
    # The constrained continuous minimizer is G*e_j/G_jj. This avoids
    # inverting the high-height approximate adjugate, and lets Arb certify
    # fractional parts for a sharper unbiased-rounding bound.
    Li = fmpq_mat(L).inv()
    r0 = fmpq_mat(1,n,[A[k,j]-a[0,i]*A[j,j] for i,k in enumerate(cols)])*Li
    r1 = fmpq_mat(1,n,[B[k,j]-a[0,i]*B[j,j] for i,k in enumerate(cols)])*Li
    with ctx.workprec(bits):
        zeta = arb(7).zeta()
        dv, jv, tv = evaluate(det,zeta), evaluate(jj,zeta), evaluate(trace,zeta)
        assert dv > 0 and jv > 0 and tv > 0
        coarse_bound = (dv/jv+tv)/fixed
        alpha=[]; lowers=[]; variances=[]; unresolved=0
        for i in range(n):
            x=(arb(r0[0,i])+arb(r1[0,i])*zeta)/jv
            near=int(x.mid().floor().unique_fmpz())
            for candidate in [near,near+1]:
                if r0[0,i]==candidate*A[j,j] and r1[0,i]==candidate*B[j,j]:
                    x=arb(candidate)
            floor=x.floor().unique_fmpz()
            if floor is None:
                unresolved+=1; floor=int(x.mid().floor().unique_fmpz()); variance=arb(1)/4
            else:
                theta=x-int(floor); variance=theta*(1-theta)
            alpha.append(x); lowers.append(int(floor)); variances.append(variance)
        def metric_entry(i,k):
            return evaluate(fmpq_poly([M[i,k] for M in matrices]),zeta)
        variance_cost=sum((variances[i]*metric_entry(i,i) for i in range(n)),arb(0))
        bound=(dv/jv+variance_cost)/fixed
        log_bound = bound.log()
        bound_ball = (log_bound/K**2).str(30)
        score = float((log_bound/K**2).mid())
        coarse_score=float((coarse_bound.log()/K**2).mid())
        coarse_ball=(coarse_bound.log()/K**2).str(30)
        # Conditional-expectation selection. The final witness is checked
        # independently against the rigorous existence bound below.
        deviations=[]; integers=[]
        for i in range(n):
            x=alpha[i]; lower=lowers[i]
            cross=sum((metric_entry(i,k)*deviations[k] for k in range(i)),arb(0))
            costs=[2*(v-x)*cross+metric_entry(i,i)*(v-x)**2 for v in [lower,lower+1]]
            chosen=lower if costs[0].mid()<=costs[1].mid() else lower+1
            integers.append(chosen); deviations.append(arb(chosen)-x)
    sub_u = a+fmpz_mat(1,n,integers)*L
    u = [1 if k == j else int(sub_u[0,cols.index(k)]) for k in range(m)]
    witness = normal_result(u, A, B, coefficients, K, label, conditions, True,
                            condition_kind,uniform_content)
    assert all(t['preserved_after_saturation'] for t in witness['local'])
    assert all(fmpq(c).q == 1 and int(fmpq(c).p) % fixed == 0 for c in witness['poly'])
    with ctx.workprec(max(bits, 200)):
        pv = evaluate(fmpq_poly([fmpq(c) for c in witness['poly']]), arb(7).zeta())/fixed
        assert pv > 0
        below_bound = pv <= bound
    return dict(chart_coordinate=j, label=label, index=str(abs(L.det())), fixed_divisor=str(fixed),
                condition_kind=condition_kind,
                existence_score=score, existence_score_ball=bound_ball,
                coarse_existence_score=coarse_score, coarse_existence_score_ball=coarse_ball,
                unresolved_fractional_parts=unresolved,
                witness_below_existence_bound=below_bound, witness=witness,
                affine_point=full_a, lattice_rows=[[int(L[i,k]) for k in range(n)] for i in range(n)],
                trace_quarter_poly=[str(c) for c in trace])


def run(K, N, m, model='radical'):
    A,B,_ = integer_pencil(K,N,m)
    det,H = adjugate_coefficients(A,B); dual,_ = rational_metric(A,B)
    candidates = []; diagnostics=[]; uniform=1
    kind='ambient_radical' if model=='radical' else 'adjugate_kernel'
    if model=='radical':
        for p in primerange(3,2*K+5):
            R,d = radical(A,B,p)
            if 0 < d < m-1:
                candidates.append((p,R))
        candidates.sort(key=lambda pair:(pair[1].ncols(),-pair[0]))
    else:
        uniform,candidates,diagnostics=adjugate_conditions(H,m,K)
    selected = candidates[:2 if model=='radical' else 3]
    jobs = [('unconstrained',[])]+[(f'{model}_{p}',[(p,R)]) for p,R in selected]
    if len(selected)>=2:
        jobs.append((f'joint_{model}',selected))
    rows=[]
    prefix='affine_subspaces' if model=='radical' else 'affine_adjugate'
    output=Path(__file__).with_name(f'{prefix}_K{K}_N{N}_m{m}.json')
    for label,conditions in jobs:
        feasible=[j for j in range(m) if affine_chart(m,j,conditions) is not None]
        assert feasible
        for j in sorted({feasible[0],feasible[-1]}):
            row=chart_result(K,A,B,det,H,dual,j,conditions,label,kind,uniform)
            rows.append(row)
            data=dict(K=K,N=N,m=m,h=m-1,condition_model=model,adjugate_content=str(uniform),
                      constraint_diagnostics=diagnostics,
                      selected_constraint_rows=[dict(p=p,rows=[[int(R[j,i]) for j in range(m)]
                                                              for i in range(R.ncols())]) for p,R in selected],rows=rows)
            output.write_text(json.dumps(data,indent=2),encoding='utf-8')
            print(json.dumps(dict(K=K,m=m,label=label,j=j,bound=row['existence_score'],
                                  witness=row['witness']['score'],verified=row['witness_below_existence_bound'])),flush=True)
    return data


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--K',type=int,default=12)
    p.add_argument('--N',type=int,default=1);p.add_argument('--m',type=int)
    p.add_argument('--model',choices=['radical','adjugate'],default='radical')
    args=p.parse_args();run(args.K,args.N,args.m or args.K-args.N+1,args.model)
