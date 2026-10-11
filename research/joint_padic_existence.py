"""Selected mixed-depth, mixed-prime affine existence budgets."""
import json
from pathlib import Path

from arithmetic_subspaces import integer_pencil, adjugate_coefficients, rational_metric
from affine_subspace_existence import chart_result
from padic_subspace_flags import identity, integral_coefficients, advance, lattice_chart, rows


def run():
    K=24;N=1;m=24
    A,B,_=integer_pencil(K,N,m)
    det,H=adjugate_coefficients(A,B);g,F=integral_coefficients(H)
    dual,_=rational_metric(A,B)
    data=dict(K=K,N=N,m=m,adjugate_content=str(g),charts=[])
    output=Path(__file__).with_name('joint_padic_existence_K24_N1_m24.json')
    for depths in [(2,1,1),(3,1,2),(2,2,2),(3,3,2)]:
        for strategy in ['radical','isotropic']:
            if depths[1]==1 and strategy=='isotropic':
                continue
            T=identity(m);steps=[]
            for p,depth in zip([3,7,17],depths):
                for level in range(1,depth+1):
                    T,record=advance(F,T,p,strategy)
                    record.update(level=level)
                    steps.append(record)
            label=strategy+'_'+('_'.join(map(str,depths)))
            result=chart_result(K,A,B,det,H,dual,0,[],label,'higher_padic',g,
                                chart_override=lattice_chart(T,0))
            result.update(ambient_lattice_rows=rows(T),depths=depths,strategy=strategy,steps=steps)
            data['charts'].append(result)
            output.write_text(json.dumps(data,indent=2),encoding='utf-8')
            print(json.dumps(dict(label=label,bound=result['existence_score'],witness=result['witness']['score'],
                                  relative_divisor=str(int(result['fixed_divisor'])//g),index=result['index'])),flush=True)
    return data


if __name__=='__main__':
    run()
