"""Combine complete fixed-divisor enumerations with independent Arb bounds."""
import json
from pathlib import Path
from flint import fmpq, fmpq_mat, fmpq_poly, fmpz_mat, arb, arb_mat, ctx
from sympy import factorint
from directional_congruence import Family, root_lattice, metric, lattice_round, matrix_rows
from directional_congruence_audit import arb_metric
from joint_exact import content, entries_from_polynomial, determinant
from block_pencil_fixed_divisor import gcdq


def main():
    folder=Path(__file__).parent;fam=Family();A0,b0=metric(24,1,3);ct0=content(fam.det([0,0,0]));rows=[]
    with ctx.workprec(6000):
        A,b,minimum=arb_metric(fam)
        for tag in ('K24_full','K24_root30'):
            data=json.loads((folder/f'directional_fixed_divisor_{tag}.json').read_text());G=fmpq(data['fixed_divisor'])
            B=fmpz_mat(data['basis']);assert B==root_lattice(fam.E,data['moduli'])
            u,U,_,_=lattice_round(B,A0,b0,20)
            ub=arb_mat(3,3,list(U.entries()));gram=ub*A*ub.transpose();epsilon=sum((gram[i,i] for i in range(3)),arb(0))/4
            premium=arb(ct0/G).log()/576;gain=20*((minimum+epsilon)/20).log()/576
            ratio=ct0/G;assert ratio.q==1
            # Recompute every gcd-changing witness through the original moment
            # engine, independent of the cached convolution evaluator.
            witness_contents=[]
            for witness in data['gcd_changes']:
                z=witness['z'];ui=[sum(int(B[i,j])*z[i] for i in range(3)) for j in range(3)]
                Q=fam.polynomial(ui);aa,bb=entries_from_polynomial(24,fam.polynomial(ui)**2*fmpq_poly([1,1])**8,20)
                original=determinant(aa,bb,20);assert original==fam.det(ui)
                c=content(original);assert str(c)==witness['content'];witness_contents.append(c)
            assert gcdq(witness_contents)==G
            rows.append(dict(tag=tag,index=str(abs(int(B.det()))),points=data['points'],
                fixed_divisor=str(G),prime_losses={str(p):int(e) for p,e in factorint(int(ratio.p)).items()},
                minimum_ball=minimum.str(35),rounding_ball=epsilon.str(35),premium_ball=premium.str(35),
                real_existence_gain_ball=gain.str(35),relative_trace_certificate_ball=(premium+gain).str(35),
                ideal_relative_trace_certificate_ball=(premium+20*(minimum/20).log()/576).str(35),
                reduced_basis=matrix_rows(U),witnesses_independently_checked=len(witness_contents)))
    path=folder/'directional_fixed_summary.json';path.write_text(json.dumps(dict(rows=rows),indent=2),encoding='utf-8')
    print(json.dumps([{k:v for k,v in r.items() if k not in ['fixed_divisor','reduced_basis']} for r in rows],indent=2),flush=True)


if __name__=='__main__':main()
