"""Exact derivative/boundary-jet audits; no asymptotic irrationality claim."""
import json
import math
from pathlib import Path

from flint import arb, ctx, fmpq, fmpq_mat

from critical_lift_probe import harmonic_table, output_map, primitive
from growing_head_quotient import kernel_polynomial


def rising(k, p):
    return math.factorial(k+p-1)//math.factorial(k-1)


def rank(rows):
    if not rows or not rows[0]:
        return 0
    return fmpq_mat(rows).rref()[1]


def derivative_rows(n, head, w, max_order):
    out, local = output_map(n, head=head, degrees=tuple(range(0, 2*(w+4), 2)))
    harmonic = harmonic_table(n, 7+max_order)
    constants = [out[0]]
    for p in range(1, max_order+1):
        constants.append([-sum(((-1)**p*rising(k,p)*local[j][col][k]*harmonic[j][k+p]
                               for j in range(n+1) for k in range(1,8)), fmpq(0))
                          for col in range(w+4)])
    return out, local, constants


def check(n, head, w, h):
    out, local, constants = derivative_rows(n, head, w, 2*h)
    kernels = [kernel_polynomial(n,head,i)[0] for i in range(w)]
    jet_matrix = []
    checks = 0
    for p in range(1, 2*h+1):
        row = []
        for polynomial in kernels:
            # R = S(t)-S(t+1): S's coefficients are prefix sums of R's.
            d = [fmpq(0)]*8
            boundary = fmpq(0)
            for j in range(n+1):
                for k in range(1,8):
                    d[k] += sum((local[j][col][k]*polynomial[col]
                                 for col in range(len(polynomial))), fmpq(0))
                if j<n:
                    boundary += sum(((-1)**p*rising(k,p)*d[k]/(j+1)**(k+p)
                                     for k in range(1,8)), fmpq(0))
            assert all(x==0 for x in d)
            output = sum((constants[p][col]*polynomial[col]
                          for col in range(len(polynomial))), fmpq(0))
            assert output == boundary
            row.append(output)
            checks += 1
        jet_matrix.append(row)
    ordinary = rank(jet_matrix[:h])
    even = rank(jet_matrix[1::2])
    base = [out[k] for k in (0,3,5,7)]
    joint_ordinary = rank(base+constants[1:h+1])
    joint_even = rank(base+constants[2::2])
    assert ordinary == min(h,w)
    assert joint_ordinary == 4+ordinary
    assert joint_even == 4+even
    if w>=2*h:
        assert even == h
    # One seed's even derivatives: its newest zeta column is nonzero.
    seed = 0
    assert out[7][seed] != 0
    weights = list(range(3,8+2*h,2))
    forms = []
    for p in range(h+1):
        row = [constants[2*p][seed]]
        row += [rising(k-2*p,2*p)*out[k-2*p][seed]
                if 1<=k-2*p<=7 else fmpq(0) for k in weights]
        forms.append(row)
    rank_zeta = rank([row[1:] for row in forms])
    rank_all = rank(forms)
    assert rank_zeta == rank_all == h+1
    return dict(n=n,head=head,w=w,h=h,domain_dimension=w+4,
                ordinary_jet_rank=ordinary,even_jet_rank=even,
                joint_ordinary_rank=joint_ordinary,joint_even_rank=joint_even,
                simultaneous_even_formal_kernel=w-even,
                boundary_identity_checks=checks,
                one_seed_rows=h+1,one_seed_zeta_rank=rank_zeta,
                one_seed_augmented_rank=rank_all)


def primitive_basis_probe(n,head):
    out,_=output_map(n,head=head)
    rows=[]
    ints=[]
    for col in range(4):
        pair,scale=primitive([out[k][col] for k in (0,3,5,7)])
        ints.append([fmpq(x) for x in pair])
        with ctx.workprec(max(abs(x).bit_length() for x in pair)+384):
            value=arb(pair[0])+sum((arb(pair[j])*arb(k).zeta()
                                   for j,k in enumerate((3,5,7),1)),arb(0))
            assert value>0
            rows.append(dict(degree=2*col,coefficients=list(map(str,pair)),
                             scale=str(scale),positive_value=value.str(20),
                             log_value_per_n=(value.log()/n).str(16),
                             log_height_per_n=(arb(max(abs(x) for x in pair)).log()/n).str(16)))
    det=fmpq_mat(ints).det()
    assert det and det.denominator==1
    return dict(n=n,head=head,rank=4,determinant=str(det),rows=rows)


def main():
    rows=[]
    for n,head in ((2,0),(4,0),(4,4),(8,8)):
        for w in (1,2,4,6):
            if 7*n-2*head-2*w<1:
                continue
            for h in (1,2,3):
                row=check(n,head,w,h)
                rows.append(row)
                print(json.dumps(row),flush=True)
    basis=[primitive_basis_probe(n,n) for n in (4,8,16,24)]
    result=dict(scope='Exact finite ranks and boundary identities. General statements are proved separately in the report.',
                rank_cases=rows,boundary_checks=sum(r['boundary_identity_checks'] for r in rows),
                primitive_four_form_bases=basis)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(dict(cases=len(rows),boundary_checks=result['boundary_checks'],
                          basis_log_values=[dict(n=r['n'],rates=[x['log_value_per_n'] for x in r['rows']]) for r in basis])),flush=True)


if __name__=='__main__':
    main()
