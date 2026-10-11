"""Additional finite search with repeated and nested numerator zero blocks."""
import json,math,time
from pathlib import Path
from zeta35_broad_search import Q,orders,coefficient_map,aligned,directions,Scorer

ROOT=Path(__file__).parent
PATTERNS=('double','triple','half','threequarter')


def blocks(M,pattern):
    if pattern=='double':return (M,)
    if pattern=='triple':return (M,M)
    if pattern=='half':return (M//2,)
    if pattern=='threequarter':return (3*M//4,)
    raise ValueError(pattern)


def evaluate(seed,scale,mode,scorer):
    N,M=8*scale,seed['M']*scale
    extra=tuple(v*scale for v in seed['extra_blocks'])
    i,j=(seed['i'],seed['j']) if mode=='fixed' else (seed['i']*scale,seed['j']*scale)
    if 2*(M+sum(extra))+2*j>sum(orders(N,seed['shape']))-2:
        return dict(status='degree_exceeds_bound',N=N)
    rows=coefficient_map(N,M,j,seed['shape'],seed['spacing'],Q(seed['offset']),extra)
    pair=aligned(rows,i,j,seed['a'],seed['b'])
    if pair is None:return dict(status='positive_alignment_unavailable',N=N)
    q,c=pair
    return dict(status='verified',N=N,log_L=scorer.value(seed['a'],seed['b'],q,c),
                coefficient_bits=max(abs(q).bit_length(),abs(c).bit_length()))


def main():
    start=time.perf_counter(); scorer=Scorer(4096); dirs=directions(24)
    maps=forms=0; retained={}; global_best=[]
    for shape in ('all5','centerhalf','centerquarter','center1'):
        for spacing in (1,2):
            for offset in (Q(0),Q(1,2)):
                for pattern in PATTERNS:
                    for M in range(1,12):
                        extra=blocks(M,pattern)
                        if not all(extra):continue
                        d=min(4,(sum(orders(8,shape))-2-2*(M+sum(extra)))//2)
                        if d<1:continue
                        rows=coefficient_map(8,M,d,shape,spacing,offset,extra);maps+=1
                        for a,b in dirs:
                            for i in range(d+1):
                                for j in range(i,d+1):
                                    pair=aligned(rows,i,j,a,b)
                                    if pair is None:continue
                                    q,c=pair; score=scorer.value(a,b,q,c);forms+=1
                                    key=(a,b,shape,spacing,str(offset),pattern)
                                    if key not in retained or score<retained[key]['log_L']:
                                        retained[key]=dict(a=a,b=b,N=8,M=M,i=i,j=j,extra_blocks=extra,
                                            shape=shape,spacing=spacing,offset=str(offset),pattern=pattern,log_L=score)
        print('multiblock',shape,'maps',maps,'forms',forms,flush=True)
    level16=[]
    work=sorted(retained.values(),key=lambda s:(s['shape'],s['spacing'],s['offset'],s['M'],s['extra_blocks'],s['j']))
    for seed in work:
        for mode in ('fixed','scaled'):
            level=evaluate(seed,2,mode,scorer)
            level16.append(dict(seed=seed,mode=mode,levels=[level]))
    valid=[r for r in level16 if r['levels'][-1]['status']=='verified']
    valid.sort(key=lambda r:r['levels'][-1]['log_L'])
    chosen=valid[:64]; seen=set(); chosen_ids={id(r) for r in chosen}
    for r in valid:
        s=r['seed'];key=(s['pattern'],s['shape'],s['spacing'],s['offset'],r['mode'])
        if key not in seen and id(r) not in chosen_ids:chosen.append(r);chosen_ids.add(id(r))
        seen.add(key)
    for n,r in enumerate(chosen):
        for scale in (4,8,16):r['levels'].append(evaluate(r['seed'],scale,r['mode'],scorer))
        print('multiblock finalist',n+1,[round(v['log_L'],3) if v['status']=='verified' else v['status'] for v in r['levels']],flush=True)
    result=dict(map_count=maps,form_count=forms,direction_count=len(dirs),retained_count=len(retained),
                scale2_count=len(level16),scale2_valid=len(valid),scale2_min_log=valid[0]['levels'][0]['log_L'],
                seeds_best=sorted(retained.values(),key=lambda r:r['log_L'])[:20],records=chosen,
                seconds=time.perf_counter()-start)
    (ROOT/'zeta35_multiblock_search.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    good=[r for r in chosen if all(v['status']=='verified' for v in r['levels'])]
    good.sort(key=lambda r:r['levels'][-1]['log_L'])
    print('best',[(r['seed'],[v['log_L'] for v in r['levels']]) for r in good[:3]])


if __name__=='__main__':main()
