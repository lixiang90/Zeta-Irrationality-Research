"""Independent residue audits for the congruence and repeated-zero searches."""
import json
from pathlib import Path
from verify_zeta35_broad_search import verify
from zeta35_direction_lattice import triple,common_modulus
from zeta35_broad_search import Scorer,scaled_record

ROOT=Path(__file__).parent


def main():
    rows=[]
    initial=json.loads((ROOT/'zeta35_broad_search_stage1.json').read_text())
    seed=min(initial['records'],key=lambda r:r['log_L'])
    rows.append(dict(group='best_small_order',result=verify(seed)))
    small_scorer=Scorer(8192)
    small_extension=[scaled_record(seed,scale,'fixed',small_scorer) for scale in (2,4,8,16)]
    data=json.loads((ROOT/'zeta35_multiblock_search.json').read_text())
    seen=set()
    for r in data['records']:
        s=r['seed'];key=(s['pattern'],s['offset'])
        if key in seen:continue
        seen.add(key)
        for scale in (1,4):
            result=verify(s,scale,r['mode'])
            rows.append(dict(group='multiblock',pattern=s['pattern'],result=result))
    best=min(data['records'],key=lambda r:r['levels'][-1].get('log_L',float('inf')))
    rows.append(dict(group='multiblock_best_128',result=verify(best['seed'],16,best['mode'])))
    lattice=json.loads((ROOT/'zeta35_direction_lattice.json').read_text())
    best=min(lattice['trials'],key=lambda r:r['levels'][-1].get('log_L',float('inf')))
    rows.append(dict(group='lattice_best_128',result=verify(best['seed'],16,best['mode'])))
    extension=[]; scorer=Scorer(16384)
    for scale in (32,64):
        result=scaled_record(best['seed'],scale,best['mode'],scorer)
        extension.append(result)
        print('extended lattice best',result,flush=True)
    ts=[triple(best['seed'],scale,best['mode']) for scale in (1,2,4,8,16,32,64)]
    H=common_modulus(ts)
    out=dict(status='passed',audit_count=len(rows),rows=rows,
             small_order_extension=small_extension,
             extended_seed=best['seed'],extended_mode=best['mode'],extended_levels=extension,
             common_modulus_through_512=str(H))
    (ROOT/'verify_zeta35_search_extensions.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('audits passed',len(rows),'common modulus',H,flush=True)


if __name__=='__main__':main()
