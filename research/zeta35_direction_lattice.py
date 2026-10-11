"""Exact determinant/gcd diagnostics and cross-scale congruence directions.

This is a finite search, not an irrationality proof or an asymptotic theorem.
"""
import json, math
from pathlib import Path
from zeta35_broad_search import Q, coefficient_map, scaled_record, Scorer

ROOT=Path(__file__).parent


def triple(seed,scale,mode):
    N=seed['N']*scale; M=seed['M']*scale
    old=Q(seed['offset']); offset=scale*int(old.floor())+old-int(old.floor())
    i=seed['i']*(scale if mode=='scaled' else 1)
    j=seed['j']*(scale if mode=='scaled' else 1)
    if i==j:return None
    rows=coefficient_map(N,M,j,seed['shape'],seed['spacing'],offset)
    Ai,Bi,Ci=rows[i]; Aj,Bj,Cj=rows[j]
    K=Ai*Bj-Aj*Bi
    U=Ai*Cj-Aj*Ci
    V=Ci*Bj-Cj*Bi
    if K==0:return None
    g=math.gcd(K,U,V)
    return K//g,U//g,V//g


def common_modulus(ts):
    H=math.gcd(*(r[0] for r in ts))
    for i,(_,U,V) in enumerate(ts):
        for _,X,Y in ts[:i]:H=math.gcd(H,U*Y-X*V)
    return H


def gauss(v,w):
    dot=lambda a,b:a[0]*b[0]+a[1]*b[1]
    while True:
        if dot(w,w)<dot(v,v):v,w=w,v
        n=dot(v,v); m=(2*dot(v,w)+n)//(2*n)
        if m==0:return v,w
        w=(w[0]-m*v[0],w[1]-m*v[1])


def directions(H,U,V):
    g=math.gcd(U,H); h=H//g
    assert math.gcd(U,V,H)==1
    r=(-V*pow(U//g,-1,h))%h if h>1 else 0
    v,w=gauss((h,0),(r,g))
    assert abs(v[0]*w[1]-v[1]*w[0])==H
    out=set()
    for m in range(-4,5):
        for n in range(-4,5):
            a,b=m*v[0]+n*w[0],m*v[1]+n*w[1]
            if not a or not b:continue
            d=math.gcd(a,b);a//=d;b//=d
            if b<0:a,b=-a,-b
            # Primitive reduction may lose the full congruence; exclude that.
            if (a*U+b*V)%H==0:out.add((a,b))
    return sorted(out,key=lambda p:p[0]*p[0]+p[1]*p[1])[:12]


def main():
    source=json.loads((ROOT/'zeta35_broad_search_stage3.json').read_text())['records']
    seen=set(); selected=[]
    for r in source:
        s=r['seed']; key=tuple(s[k] for k in ('shape','spacing','offset','M','i','j'))+(r['mode'],)
        if key not in seen:selected.append(r);seen.add(key)
    diagnostics=[]; trials=[]; scorer=Scorer(8192)
    for number,r in enumerate(selected):
        s=r['seed'];mode=r['mode']
        if s['i']==s['j']:continue
        ts=[triple(s,scale,mode) for scale in (1,2,4)]
        if any(t is None for t in ts):continue
        H=common_modulus(ts)
        dirs=directions(H,ts[0][1],ts[0][2])
        gains=[]
        for scale in (1,2,4,8,16):
            t=triple(s,scale,mode)
            if t is None:continue
            K,U,V=t;g=math.gcd(K,s['a']*U+s['b']*V)
            gains.append(dict(N=s['N']*scale,log_g=math.log(g),log_abs_K=math.log(abs(K))))
        diagnostics.append(dict(seed=s,mode=mode,H=str(H),directions=dirs,gains=gains))
        for a,b in dirs:
            assert all((a*U+b*V)%H==0 for _,U,V in ts)
            candidate=dict(s,a=a,b=b)
            levels=[scaled_record(candidate,scale,mode,scorer) for scale in (1,2,4,8,16)]
            candidate.pop('log_L',None)
            if levels[0]['status']=='verified':candidate['log_L']=levels[0]['log_L']
            trials.append(dict(seed=candidate,mode=mode,levels=levels))
        print('lattice',number+1,'H bits',H.bit_length(),'directions',len(dirs),flush=True)
    result=dict(training_scales=[1,2,4],held_out_scales=[8,16],diagnostics=diagnostics,trials=trials)
    (ROOT/'zeta35_direction_lattice.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    valid=[r for r in trials if all(v['status']=='verified' for v in r['levels'])]
    valid.sort(key=lambda r:r['levels'][-1]['log_L'])
    print('trials',len(trials),'all_levels_valid',len(valid))
    for r in valid[:10]:print(r['seed']['a'],r['seed']['b'],[round(v['log_L'],4) for v in r['levels']])


if __name__=='__main__':main()
