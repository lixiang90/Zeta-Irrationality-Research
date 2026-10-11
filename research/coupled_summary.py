"""Collect distinct certified complete-pencil cases and hypothesis status."""
import json
from pathlib import Path

if __name__=='__main__':
    folder=Path(__file__).parent;allrows={}
    def add(K,N,p,value,source):
        key=(K,N,p)
        if key in allrows:
            assert allrows[key]['gauss']==value,(key,allrows[key],value)
            allrows[key]['sources'].append(source)
        else:allrows[key]=dict(K=K,N=N,p=p,gauss=value,sources=[source])
    grid=json.loads((folder/'coupled_grid.json').read_text())
    diagnostics=json.loads((folder/'coupled_diagnostics.json').read_text())
    witnesses={(r['K'],r['N'],r['p']):r for r in diagnostics['specialization_witnesses']}
    for r in grid['rows']:
        if r['crude_certificate']:value=r['constant_valuation']
        else:value=witnesses[r['K'],r['N'],r['p']]['certified_gauss']
        add(r['K'],r['N'],r['p'],value,'grid')
    for name in ['coupled_schur','coupled_scale','coupled_broad','coupled_window']:
        for r in json.loads((folder/(name+'.json')).read_text()):
            assert r['generic_certified']
            add(r['K'],r['N'],r['p'],r.get('gauss',r.get('gauss_valuation')),name)
    law=json.loads((folder/'coupled_candidate_law.json').read_text())
    for r in law['rows']:
        assert r['generic_certified'];add(r['K'],r['N'],r['p'],r['gauss'],'candidate_lower_bound')
    result=dict(unique_certified_cases=len(allrows),grid=grid['summary'],law=law['summary'],
                cases=list(allrows.values()),
                status='Each listed Gauss valuation is certified for that finite case. No uniform conjecture is promoted to a theorem.')
    (folder/'coupled_summary.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:v for k,v in result.items() if k!='cases'}),flush=True)
