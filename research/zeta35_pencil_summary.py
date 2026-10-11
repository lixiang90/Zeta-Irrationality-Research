"""Summarize verified finite pencils and test a proposed large-prime formula."""
import json
from pathlib import Path
from flint import nmod_mat

def main():
    root=Path(__file__).parent;rows=[]
    for n in (1,2,3):
        data=json.loads((root/f'zeta35_pencil_certificate_n{n}.json').read_text())
        check=json.loads((root/f'verify_zeta35_pencil_certificate_n{n}.json').read_text())
        assert check['status']=='independent_replay_passed' and check['cases']==len(data['rows'])
        K,N,h=40*n,3*n,37*n
        for c in data['rows']:
            p=c['p'];layers=c['constant_layers'];k=sum(v<0 for v in layers);z=h-k
            residual=[[int(x)//p**c['scale']%p for x in row[k:]]
                      for row in c['transformed_B_scaled_mod_pL'][k:]]
            rank=nmod_mat(residual,p).rank() if z else 0
            det=int(nmod_mat(residual,p).det()) if z else 1
            formula=None
            if 2*p>K+N:
                d=max(h-p,0);q=min(N+1,max(K+1-p,0));cap=h-d
                r=max(2*h+6*N-K+2-(2 if c['a']==0 else 1)*p,0)
                formula=-7*d-min(cap,q+r)
                assert formula==c['lower']
                if c['a']==3:
                    assert rank==z
                    assert sum(v for v in layers if v<0)==c['lower']
            rows.append(dict(n=n,p=p,a=c['a'],negative_dimension=k,residual_dimension=z,
                residual_X_rank=rank,residual_X_determinant_mod_p=det,
                certified_content_valuation=c['lower'],candidate_formula=formula,
                formula_scope='finite agreement only; arbitrary-n formula unproved'))
    out=dict(status='finite_summary_checks_passed',total=len(rows),
             formula_cases=sum(r['candidate_formula'] is not None for r in rows),rows=rows)
    (root/'zeta35_pencil_summary.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('total',len(rows),'formula cases',out['formula_cases'])

if __name__=='__main__':main()
