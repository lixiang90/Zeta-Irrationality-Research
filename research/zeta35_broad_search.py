"""Broad exact search for a FIXED non-axis combination a*zeta(3)+b*zeta(5).

No continued-fraction selection from target intervals is used. Positive
rational-function sums are aligned by two nonnegative numerator coefficients.
"""
import argparse,json,math,time,heapq
from pathlib import Path
from functools import lru_cache
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx

ROOT=Path(__file__).parent
SHAPES=('all5','center1','centerquarter','centerhalf','outerhalf','outerquarter','ends5','center3')


def orders(N,shape):
    if shape=='all5':return [5]*(N+1)
    if shape=='center1':return [5 if j==N//2 else 3 for j in range(N+1)]
    if shape=='centerquarter':return [5 if abs(2*j-N)<=N//4 else 3 for j in range(N+1)]
    if shape=='centerhalf':return [5 if abs(2*j-N)<=N//2 else 3 for j in range(N+1)]
    if shape=='outerhalf':return [3 if abs(2*j-N)<=N//2 else 5 for j in range(N+1)]
    if shape=='outerquarter':return [3 if abs(2*j-N)<=N//4 else 5 for j in range(N+1)]
    if shape=='ends5':return [5 if j in (0,N) else 3 for j in range(N+1)]
    if shape=='center3':return [3 if j==N//2 else 5 for j in range(N+1)]
    raise ValueError(shape)


def mul(a,b,n):
    return [sum((a[j]*b[k-j] for j in range(k+1)),Q(0)) for k in range(n)]


@lru_cache(maxsize=256)
def coefficient_map(N,M,d,shape,spacing,offset,extra_blocks=()):
    offset=Q(offset)
    half=offset.denominator==2
    assert offset.denominator in (1,2)
    es=orders(N,shape)
    assert N%2==0 and sum(es)%2==1
    assert all(0<=v<=M for v in extra_blocks)
    assert 2*(M+sum(extra_blocks))+2*d<=sum(es)-2
    center=2*offset+spacing*N
    z0=(M+1)*(M+center+1)
    P=Poly([1])
    for block in (M,)+tuple(extra_blocks):
        for k in range(1,block+1):P*=Poly([-k*(center+k),center,1])
    poles=[offset+spacing*j for j in range(N+1)]
    H=[[Q(0)] for _ in range(6)]
    for s in range(1,6):
        if half:
            for k in range(int(max(poles).floor())+1):H[s].append(H[s][-1]+Q(2**s,(2*k+1)**s))
        else:
            for k in range(1,int(max(poles))+1):H[s].append(H[s][-1]+Q(1,k**s))
    rows=[[Q(0)]*3 for _ in range(d+1)]
    unwanted=[[Q(0)]*3 for _ in range(d+1)]
    for j,pole in enumerate(poles):
        e=es[j]
        local=[sum((P[i]*math.comb(i,k)*Q(-pole)**(i-k) for i in range(k,len(P))),Q(0)) for k in range(e)]
        for l,other in enumerate(poles):
            if l!=j:
                local=mul(local,[Q((-1)**k*math.comb(k+es[l]-1,k))/(other-pole)**(es[l]+k) for k in range(e)],e)
        factor=([Q(pole*(pole-center)-z0),Q(center-2*pole),Q(1)]+[Q(0)]*e)[:e]
        for power in range(d+1):
            cs=[Q(0)]*6
            for s in range(1,e+1):cs[s]=local[e-s]
            rows[power][0]+=(31 if half else 1)*cs[5];rows[power][1]+=(7 if half else 1)*cs[3]
            hindex=int(pole.floor())+1 if half else int(pole)
            rows[power][2]-=sum((cs[s]*H[s][hindex] for s in range(1,e+1)),Q(0))
            for k,s in enumerate((1,2,4)):unwanted[power][k]+=cs[s]
            local=mul(local,factor,e)
    assert all(v==0 for r in unwanted for v in r)
    den=math.lcm(*(int(c.denominator) for r in rows for c in r))
    ints=[[int(c*den) for c in row] for row in rows]
    g=math.gcd(*(abs(c) for row in ints for c in row))
    return tuple(tuple(c//g for c in r) for r in ints)


def directions(bound):
    values={(a,b) for a in range(-bound,bound+1) if a for b in range(1,bound+1) if math.gcd(a,b)==1}
    for c in (24,32,48,64,96,128,256):
        values.update(((1,c),(-1,c),(c,1),(-c,1)))
    return sorted(values)


class Scorer:
    def __init__(self,bits):
        ctx.prec=bits;self.prec=bits;self.z3=arb(3).zeta();self.z5=arb(5).zeta();self.theta={}
    def value(self,a,b,q,c):
        bits=max(abs(q).bit_length(),abs(c).bit_length())+384
        if bits>self.prec:
            ctx.prec=bits;self.prec=bits;self.z3=arb(3).zeta();self.z5=arb(5).zeta();self.theta={}
        key=(a,b)
        if key not in self.theta:self.theta[key]=a*self.z3+b*self.z5
        L=q*self.theta[key]+c
        assert L>0,(key,q,c,self.prec)
        return float(L.log())


def aligned(rows,i,j,a,b):
    Ai,Bi,Ci=rows[i];Aj,Bj,Cj=rows[j]
    Ti=b*Bi-a*Ai;Tj=b*Bj-a*Aj
    if i==j:
        if Ti:return None
        u,v=1,0
    else:
        if Ti*Tj>=0:return None
        u,v=abs(Tj),abs(Ti)
    AA=u*Ai+v*Aj;CC=u*Ci+v*Cj
    assert AA%b==0
    q=AA//b
    if not q:return None
    g=math.gcd(q,CC)
    return q//g,CC//g


def stage1(bound=16,N=8,maxdegree=6):
    start=time.perf_counter();dirs=directions(bound);scorer=Scorer(2048)
    best={v:[] for v in dirs};family_best={};count=0;maps=0;counter=0
    for shape in SHAPES:
        for spacing in (1,2,3):
            for offset in (Q(0),Q(N//2),Q(1,2),Q(N+1,2)):
                maxM=(sum(orders(N,shape))-4)//2
                for M in range(maxM+1):
                    d=min(maxdegree,(sum(orders(N,shape))-2-2*M)//2)
                    if d<1:continue
                    rows=coefficient_map(N,M,d,shape,spacing,offset);maps+=1
                    for a,b in dirs:
                        for i in range(d+1):
                            for j in range(i,d+1):
                                pair=aligned(rows,i,j,a,b)
                                if pair is None:continue
                                q,c=pair;score=scorer.value(a,b,q,c);count+=1
                                rec=dict(a=a,b=b,N=N,M=M,i=i,j=j,shape=shape,spacing=spacing,offset=str(offset),
                                         log_L=score,q=str(q),c=str(c))
                                counter+=1;heap=best[(a,b)]
                                item=(-score,counter,rec)
                                if len(heap)<2:heapq.heappush(heap,item)
                                elif score<-heap[0][0]:heapq.heapreplace(heap,item)
                                fkey=(a,b,shape,spacing,str(offset))
                                if fkey not in family_best or score<family_best[fkey]['log_L']:
                                    family_best[fkey]=rec
        print('stage1',shape,'maps',maps,'forms',count,'seconds',round(time.perf_counter()-start,1),flush=True)
    records=[v[2] for heap in best.values() for v in heap]
    identities={tuple(r[k] for k in ('a','b','shape','spacing','offset','M','i','j')) for r in records}
    for r in family_best.values():
        identity=tuple(r[k] for k in ('a','b','shape','spacing','offset','M','i','j'))
        if identity not in identities:records.append(r);identities.add(identity)
    out=dict(scope='finite exact positive rational-function scan, fixed non-axis target directions',
             N=N,bound=bound,direction_count=len(dirs),map_count=maps,form_count=count,
             seconds=time.perf_counter()-start,records=records)
    (ROOT/'zeta35_broad_search_stage1.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('top',[(r['a'],r['b'],r['shape'],r['M'],r['i'],r['j'],round(r['log_L'],4)) for r in sorted(records,key=lambda r:r['log_L'])[:12]],flush=True)


def scaled_record(seed,scale,mode,scorer):
    N=seed['N']*scale;M=seed['M']*scale
    oldoffset=Q(seed['offset']);offset=scale*int(oldoffset.floor())+oldoffset-int(oldoffset.floor())
    i=seed['i']*(scale if mode=='scaled' else 1);j=seed['j']*(scale if mode=='scaled' else 1)
    if 2*M+2*j>sum(orders(N,seed['shape']))-2:return dict(status='degree_exceeds_bound',scale=scale)
    rows=coefficient_map(N,M,j,seed['shape'],seed['spacing'],offset)
    pair=aligned(rows,i,j,seed['a'],seed['b'])
    if pair is None:return dict(status='positive_alignment_unavailable',scale=scale)
    q,c=pair
    score=scorer.value(seed['a'],seed['b'],q,c)
    return dict(status='verified',scale=scale,N=N,M=M,i=i,j=j,offset=str(offset),log_L=score,
                coefficient_bits=max(abs(q).bit_length(),abs(c).bit_length()))


def stage2():
    start=time.perf_counter();source=json.loads((ROOT/'zeta35_broad_search_stage1.json').read_text())
    scorer=Scorer(4096);out=[]
    for k,seed in enumerate(source['records']):
        for mode in ('fixed','scaled'):
            r=scaled_record(seed,2,mode,scorer)
            out.append(dict(seed=seed,mode=mode,levels=[r]))
        if (k+1)%4000==0:print('stage2 seeds',k+1,'seconds',round(time.perf_counter()-start,1),flush=True)
    verified=[r for r in out if r['levels'][-1]['status']=='verified']
    verified.sort(key=lambda r:r['levels'][-1]['log_L'])
    candidates=verified[:48]
    selected_ids={id(r) for r in candidates}
    # Also preserve the best recipe for every direction; direction-specific
    # improvement is not rejected just because another direction starts smaller.
    seen=set()
    for r in verified:
        key=(r['seed']['a'],r['seed']['b'],r['seed']['shape'],r['seed']['spacing'],Q(r['seed']['offset']).denominator)
        if key not in seen and id(r) not in selected_ids:
            candidates.append(r);selected_ids.add(id(r))
        seen.add(key)
    # Group identical coefficient maps so the exact-arithmetic cache is useful.
    work=sorted(candidates,key=lambda r:(r['seed']['shape'],r['seed']['spacing'],
                r['seed']['offset'],r['seed']['M'],r['mode'],r['seed']['j']))
    for k,r in enumerate(work):
        r['levels'].append(scaled_record(r['seed'],4,r['mode'],scorer))
        if (k+1)%2000==0:print('stage2 scale4',k+1,'seconds',round(time.perf_counter()-start,1),flush=True)
    counts={}
    for r in out:
        status=r['levels'][0]['status'];counts[status]=counts.get(status,0)+1
    for r in candidates:
        r['seed'].pop('q',None);r['seed'].pop('c',None)
    (ROOT/'zeta35_broad_search_stage2.json').write_text(json.dumps(dict(
        scale2_count=len(out),scale2_status_counts=counts,scale4_candidates=candidates,
        seconds=time.perf_counter()-start),indent=2),encoding='utf-8')
    good=[r for r in candidates if r['levels'][-1]['status']=='verified']
    good.sort(key=lambda r:r['levels'][-1]['log_L'])
    print('best scale4',[(r['seed']['a'],r['seed']['b'],r['seed']['shape'],r['seed']['M'],r['mode'],
                         [round(r['seed']['log_L'],4)]+[round(v['log_L'],4) for v in r['levels'] if v['status']=='verified']) for r in good[:12]],flush=True)


def stage3():
    source=json.loads((ROOT/'zeta35_broad_search_stage2.json').read_text())
    records=[r for r in source['scale4_candidates'] if r['levels'][-1]['status']=='verified']
    records.sort(key=lambda r:r['levels'][-1]['log_L'])
    selected=records[:32];seen=set()
    for r in records:
        key=(r['seed']['shape'],r['seed']['spacing'],Q(r['seed']['offset']).denominator,r['mode'])
        if key not in seen and r not in selected:selected.append(r)
        seen.add(key)
    scorer=Scorer(8192)
    for k,r in enumerate(selected):
        for scale in (8,16):r['levels'].append(scaled_record(r['seed'],scale,r['mode'],scorer))
        print('stage3',k+1,(r['seed']['a'],r['seed']['b']),
              [round(v['log_L'],4) if v['status']=='verified' else v['status'] for v in r['levels']],flush=True)
        (ROOT/'zeta35_broad_search_stage3.json').write_text(json.dumps(dict(records=selected[:k+1]),indent=2),encoding='utf-8')


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--stage',type=int,default=1);p.add_argument('--bound',type=int,default=16)
    args=p.parse_args()
    if args.stage==1:stage1(args.bound)
    elif args.stage==2:stage2()
    else:stage3()
