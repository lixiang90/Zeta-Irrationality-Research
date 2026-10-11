"""NEW DISTINCT guarded FIRST1 supported-weighted transfer certificate.
Only [1/4,2] is updated.  Frozen487 combined bounds are literal data.
No old/peer mathematical file is read/imported/executed; no prime table.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import traceback

OUT = Path(__file__).with_suffix('.json')
with OUT.open('x', encoding='utf-8') as first:
    json.dump({'status': 'RUNNING_FIRST1', 'rerun_allowed': False}, first)

BASELINE_LITERAL = '''
1/4 27/106 -560 136
27/106 47/184 -136 28
47/184 8/31 -136 28
8/31 7/27 608 -164
7/27 89/343 230 -66
89/343 20/77 230 -66
20/77 6/23 1924 -506
6/23 5/19 -136 28
5/19 4/15 -98 18
4/15 7/26 562 -158
7/26 3/11 198 -60
3/11 8/29 -120 24
8/29 64/231 518 -152
64/231 7/25 518 -152
7/25 2/7 168 -54
2/7 47/161 -434 120
47/161 41/140 -112 26
41/140 5/17 -112 26
5/17 8/27 -78 16
8/27 14/47 462 -144
14/47 79/265 180 -60
79/265 97/325 180 -60
97/325 3/10 1480 -448
3/10 4/13 -98 22
4/13 14/45 422 -138
14/45 6/19 152 -54
6/19 8/25 -66 12
8/25 55/171 384 -132
55/171 14/43 384 -132
14/43 1/3 126 -48
1/3 40/117 -312 100
40/117 35/102 -78 20
35/102 8/23 -78 20
8/23 7/20 336 -124
7/20 130/371 136 -54
130/371 20/57 136 -54
20/57 6/17 1048 -374
6/17 5/14 -78 20
5/14 4/11 -50 10
4/11 7/19 302 -118
7/19 3/8 112 -48
3/8 8/21 -66 16
8/21 23/60 270 -112
23/60 7/18 270 -112
7/18 2/5 90 -42
2/5 33/80 -220 84
33/80 29/70 -60 18
29/70 5/12 -60 18
5/12 8/19 -36 8
8/19 14/33 230 -104
14/33 110/259 98 -48
110/259 134/315 98 -48
134/315 3/7 728 -316
3/7 4/9 -50 14
4/9 14/31 202 -98
14/31 6/13 78 -42
6/13 8/17 -28 4
8/17 37/78 176 -92
37/78 14/29 176 -92
14/29 1/2 60 -36
1/2 13/25 -136 64
13/25 23/44 -36 12
23/44 8/15 -36 12
8/15 7/13 144 -84
7/13 41/76 66 -42
41/76 20/37 66 -42
20/37 6/11 436 -242
6/11 5/9 -36 12
5/9 4/7 -18 2
4/7 7/12 122 -78
7/12 3/5 50 -36
3/5 8/13 -28 8
8/13 28/45 102 -72
28/45 7/11 102 -72
7/11 2/3 36 -30
2/3 19/27 -78 48
19/27 17/24 -24 10
17/24 5/7 -24 10
5/7 8/11 -10 0
8/11 14/19 78 -64
14/19 31/42 40 -36
31/42 37/50 40 -36
37/50 3/4 240 -184
3/4 4/5 -18 6
4/5 14/17 62 -58
14/17 6/7 28 -30
6/7 8/9 -6 -4
8/9 19/21 48 -52
19/21 14/15 48 -52
14/15 1 18 -24
1 15/14 -32 28
15/14 14/13 -32 28
14/13 12/11 -32 28
12/11 8/7 -10 4
8/7 7/6 32 -44
7/6 74/63 20 -30
74/63 20/17 20 -30
20/17 6/5 88 -110
6/5 5/4 -10 4
5/4 4/3 -2 -6
4/3 7/5 22 -38
7/5 3/2 12 -24
3/2 8/5 -6 0
8/5 5/3 14 -32
5/3 7/4 14 -32
7/4 2 6 -18
2 16/7 -8 12
16/7 8/3 -1 -4
8/3 3 8 -28
3 11/3 -2 -2
11/3 4 1 -13
4 5 1 -13
5 6 12 -68
'''


def af(m=0, b=0): return F(m), F(b)
def add(a, b): return a[0]+b[0], a[1]+b[1]
def mul(k, a): return F(k)*a[0], F(k)*a[1]
def sub(a, b): return add(a, mul(-1, b))
def value(a, x): return a[0]*x+a[1]
def root(a, b):
    m, c = sub(a, b)
    return None if m == 0 else -c/m
def integral(a, l, r): return a[0]*(r*r-l*l)/2+a[1]*(r-l)
def encode(a): return {'slope':str(a[0]), 'intercept':str(a[1])}
def inside(cuts, lo, hi, a, b):
    x=root(a,b)
    if x is not None and lo<x<hi: cuts.add(x)
def alpha(w,q,Q,lam,eta):
    return min(w*r+4*max(0,r-2*q)+2*max(0,r-Q)-lam*r-eta*(r>Q)
               for r in range(2*q+3))


def candidates(x):
    Q,h,a=int(F(3)/x),int(F(6)/x),int(F(2)/x)
    c,t,rr,xx=af(-h,6),af(a+1,-2),af(-Q,3),af(1)
    u=min((c,t),key=lambda z:value(z,x))
    FF=mul(a,min((u,mul(F(1,2),t)),key=lambda z:value(z,x)))
    if value(c,x)<=value(t,x):
        counts=[(0,h,c),(2,h-1,sub(t,c)),(5,h-1,sub(xx,t))]
    else:
        counts=[(0,h,t),(3,h,sub(c,t)),(5,h-1,sub(xx,c))]
    bounds=[]
    for lam in range(3,12):
        for eta in range(3):
            bb=add(sub(af(0,2*lam-10),mul(2-eta,rr)),mul(2,FF))
            for w,q,count in counts:
                assert value(count,x)>=0
                bb=add(bb,mul(alpha(w,q,Q,lam,eta),count))
            bounds.append((f'lambda{lam}_eta{eta}_supported',bb))
    return [Q,h,a],bounds


try:
    frozen=[]
    for line in BASELINE_LITERAL.strip().splitlines():
        lo,hi,m,b=line.split()
        frozen.append((F(lo),F(hi),af(int(m),int(b))))
    assert len(frozen)==113
    assert frozen[0][0]==F(1,4) and frozen[-1][1]==6
    assert all(frozen[i][1]==frozen[i+1][0] for i in range(112))
    # Updating [1/4,2] only.  No computation of old [2,6] budget is done.
    base=[(lo,min(hi,F(2)),bb) for lo,hi,bb in frozen if lo<2]
    initial={F(1,4),F(2)}
    for lo,hi,_ in base: initial.update((lo,hi))
    for k in (2,3,6):
        for j in range(1,25):
            cut=F(k,j)
            if F(1,4)<cut<2: initial.add(cut)
    initial=sorted(initial)
    branch=[]
    for lo,hi in zip(initial,initial[1:]):
        x=(lo+hi)/2
        h,a=int(F(6)/x),int(F(2)/x)
        c,t=af(-h,6),af(a+1,-2)
        pieces=(c,t,mul(F(1,2),t))
        cuts={lo,hi}
        for i,aa in enumerate(pieces):
            for bb in pieces[i+1:]: inside(cuts,lo,hi,aa,bb)
        branch.extend(zip(sorted(cuts),sorted(cuts)[1:]))
    rows=[]
    paid=F(0)
    checks=0
    for lo,hi in branch:
        mid=(lo+hi)/2
        matches=[bb for l,r,bb in base if l<mid<r]
        assert len(matches)==1
        old=matches[0]
        floors,bounds=candidates(mid)
        allbounds=[('frozen487_combined',old)]+bounds
        distinct=list(dict.fromkeys(bb for _,bb in allbounds))
        cuts={lo,hi}
        for i,aa in enumerate(distinct):
            for bb in distinct[i+1:]: inside(cuts,lo,hi,aa,bb)
        cuts=sorted(cuts)
        for l,r in zip(cuts,cuts[1:]):
            x=(l+r)/2
            label,new=max(allbounds,key=lambda item:value(item[1],x))
            for _,other in allbounds:
                assert value(new,l)>=value(other,l)
                assert value(new,r)>=value(other,r)
                checks+=2
            dg=sub(new,old)
            area=integral(dg,l,r)
            assert area>=0
            checks+=1
            paid+=area
            rows.append({'lo':str(l),'hi':str(r),'floors_Q_h_a':floors,
                         'old':encode(old),'winner':label,'new':encode(new),
                         'gain':encode(dg),'area':str(area)})
    assert rows[0]['lo']=='1/4' and rows[-1]['hi']=='2'
    assert all(rows[i]['hi']==rows[i+1]['lo'] for i in range(len(rows)-1))
    manual=integral(af(6,-4),F(2,3),F(19,27))+integral(af(-48,34),F(19,27),F(17,24))
    assert manual==F(1,216) and paid>=manual
    merged=[]
    for row in rows:
        signature=tuple((k,json.dumps(v,sort_keys=True)) for k,v in row.items() if k not in ('lo','hi','area'))
        if merged and merged[-1][0]==signature and merged[-1][1]['hi']==row['lo']:
            rr=merged[-1][1]
            rr['hi']=row['hi']; rr['area']=str(F(rr['area'])+F(row['area']))
        else: merged.append((signature,row.copy()))
    A487=F(68678357676574195925297901887,1702339643838709841383978560)
    result={'status':'PASS','execution_count':1,'first_only':True,'rerun_allowed':False,
            'runs':{'new_successful_first':1,'failed':0,'rerun':0,'old_peer_execute_import':0},
            'scope':'NEW supported-weighted transfer closed affine update [1/4,2] only; frozen487 baseline literals; no old whole-window rerun or prime samples',
            'domain':['1/4','2'],'unchanged_places':'p<n/4, p>2n, and p2<=8n retain frozen487 allplace bounds',
            'baseline_literal_rows':113,'baseline_rows_used':len(base),'new_safe_candidates':27,
            'initial_cells':len(initial)-1,'branch_cells':len(branch),'arrangement_cells':len(rows),
            'merged_rows':len(merged),'endpoint_area_checks':checks,'manual_paid_window':'1/216',
            'baseline_A487':str(A487),'new_paid_gain':str(paid),'new_signed_scale_A':str(A487-paid),
            'decimals_information_only':{'paid_gain':float(paid),'new_signed_scale_A':float(A487-paid)},
            'not_proved':['Actual Gram Smith equality','Infinite target nonzero','Strict margin','New special-value theorem'],
            'closed_certificate_rows':[rr for _,rr in merged]}
    OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','arrangement_cells','merged_rows','endpoint_area_checks','new_paid_gain','new_signed_scale_A','decimals_information_only')}))
except Exception:
    OUT.write_text(json.dumps({'status':'FAILED_PRESERVED_FIRST1','rerun_allowed':False,'traceback':traceback.format_exc()},indent=2),encoding='utf-8')
    raise
