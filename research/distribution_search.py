"""Nonmonotone root multiplicities, exact content, rigorous Arb evaluation.

At scale m a shape b assigns b_i to every j in ((i-1)m, im].
The beam search is finite exploration, not a global optimization certificate.
"""
import argparse,json,time,math
from pathlib import Path
from flint import fmpq,fmpq_poly,arb,ctx
from joint_exact import (Dcache,entries,entries_from_polynomial,determinant,
                         determinant_pole_split,evaluate_primitive_ball,experiment)

FOLDER=Path(__file__).parent

def trim(b):
    b=list(b)
    while b and b[-1]==0:b.pop()
    return tuple(b)

def numerator_poles(K,shape,m):
    assert K%24==0 and K==24*m and len(shape)*m<=K
    W=fmpq_poly([1]);T=fmpq_poly([1]);bottom=1
    for j in range(1,K+1):
        b=shape[(j-1)//m] if (j-1)//m<len(shape) else 0
        factor=fmpq_poly([j*j,1])
        if b:
            W*=factor**b;bottom*=j**b
        else:T*=factor
    return W,T,bottom

def run_shape(K,shape,h=None,origin=0):
    h=h or K;m=K//24;shape=trim(shape)
    W,T,bottom=numerator_poles(K,shape,m)
    assert origin>=0 and int(origin)==origin
    W*=fmpq_poly([0,1])**origin
    aa,bb=entries_from_polynomial(K,W,h)
    P=determinant_pole_split(aa,bb,T,h)
    assert 0<=P.degree()<=min(h,T.degree())
    ct,logball,bits=evaluate_primitive_ball(P)
    qdet=fmpq(1)
    for i in range(1,h):qdet*=fmpq(2,math.factorial(2*i))
    S=fmpq(math.factorial(K),bottom)**(2*h)*qdet**2
    with ctx.workprec(160):
        J=logball/K**2;A=-arb(ct*S).log()/K**2;R=J-A
        result=dict(K=K,h=h,shape=list(shape),scale=m,origin=origin,numerator_degree=W.degree(),
                    surviving_poles=T.degree(),degree=P.degree(),score=float(J.mid()),
                    score_ball=J.str(30),score_per_lambda=float((J*K/h).mid()),
                    arithmetic_ball=A.str(30),real_ball=R.str(30),
                    content_log_ball=arb(ct).log().str(30),precision_bits=bits,
                    strictly_positive=bool(J>0))
    return result,P

def prefix_shape(profile):
    return trim([sum(b for N,b in profile if N>=j) for j in range(1,max(N for N,b in profile)+1)])

def verify_engine():
    checks=[]
    for profile,h in [([(1,8)],23), ([(1,3),(2,2),(3,1)],24), ([(1,2),(3,2)],21)]:
        shape=prefix_shape(profile);W,T,_=numerator_poles(24,shape,1)
        aa,bb=entries_from_polynomial(24,W,h)
        assert (aa,bb)==entries(24,profile,h)
        P=determinant_pole_split(aa,bb,T,h)
        assert P==determinant(aa,bb,h)
        old,Pold,*_=experiment(24,profile,h)
        new,Pnew=run_shape(24,shape,h)
        assert P==Pold==Pnew and abs(new['score']-old['score'])<1e-14
        checks.append(dict(profile=profile,h=h,score=new['score']))
    # A shape with gaps: the old max-root shortcut would give the wrong pole count.
    shape=(2,0,3,0,1);W,T,_=numerator_poles(24,shape,1)
    aa,bb=entries_from_polynomial(24,W,24)
    assert T.degree()==21
    assert determinant_pole_split(aa,bb,T,24)==determinant(aa,bb,24)
    checks.append(dict(shape=shape,surviving_poles=T.degree()))
    (FOLDER/'distribution_engine_checks.json').write_text(json.dumps(checks,indent=2))
    print('engine checks '+json.dumps(checks),flush=True)

def beam_search(args):
    out=FOLDER/'distribution_search24.json'
    rows=json.loads(out.read_text()) if out.exists() else []
    cache={tuple(r['shape']):r for r in rows}
    prior=[r for r in json.loads((FOLDER/'layer_joint_search24.json').read_text()) if r['h']==24]
    seeds=set()
    for M in [8,9,10,11,12]:
        subset=[r for r in prior if sum(n*b for n,b in r['profile'])==M]
        seeds.update(prefix_shape(r['profile']) for r in sorted(subset,key=lambda r:r['score'])[:2])
    seeds.update([(8,),(6,3),(6,3,1)])
    start=time.time();best=min((r['score'] for r in rows),default=1e9)
    def evaluate(shape):
        nonlocal best
        shape=trim(shape)
        if shape not in cache:
            r,_=run_shape(24,shape);cache[shape]=r;rows.append(r)
            if r['score']<best:
                best=r['score'];print('BEST '+json.dumps(r),flush=True)
            if len(rows)%20==0:
                out.write_text(json.dumps(rows,indent=2))
                print(f'{len(rows)} cases, {time.time()-start:.1f}s',flush=True)
        return cache[shape]
    for shape in sorted(seeds):evaluate(shape)
    rounds=[]
    for depth in range(args.rounds):
        # Two winners per total degree preserve several different cost budgets.
        selected=[]
        for M in [8,9,10,11,12]:
            selected+=sorted((r for r in rows if sum(r['shape'])==M),key=lambda r:r['score'])[:2]
        jobs=set()
        for r in selected:
            b=r['shape']+[0]*(args.roots-len(r['shape']))
            for i in range(args.roots):
                if not b[i]:continue
                for j in range(args.roots):
                    if i==j:continue
                    c=b[:];c[i]-=1;c[j]+=1;jobs.add(trim(c))
        for shape in sorted(jobs):evaluate(shape)
        leader=min(rows,key=lambda r:r['score'])
        rounds.append(dict(round=depth+1,unique_cases=len(rows),best_shape=leader['shape'],score=leader['score']))
        out.write_text(json.dumps(rows,indent=2))
        print('ROUND '+json.dumps(rounds[-1]),flush=True)
    summary=dict(rounds=rounds,cases=len(rows),roots=args.roots,
                 negative_cases=sum(r['score']<0 for r in rows),
                 nonmonotone_cases=sum(any(a<b for a,b in zip(r['shape'],r['shape'][1:])) for r in rows),
                 best=sorted(rows,key=lambda r:r['score'])[:12])
    (FOLDER/'distribution_search_summary.json').write_text(json.dumps(summary,indent=2))
    print('SUMMARY '+json.dumps({k:v for k,v in summary.items() if k!='best'}),flush=True)

def refine(args):
    prior=json.loads((FOLDER/'distribution_search24.json').read_text())
    chosen=sorted(prior,key=lambda r:r['score'])[:args.top]
    # Include best genuinely nonmonotone shape even if outside the shortlist.
    non=[r for r in prior if any(a<b for a,b in zip(r['shape'],r['shape'][1:]))]
    if non:chosen+=sorted(non,key=lambda r:r['score'])[:2]
    out=FOLDER/f'distribution_search{args.K}.json'
    rows=json.loads(out.read_text()) if out.exists() else []
    done={tuple(r['shape']) for r in rows}
    for row in chosen:
        shape=tuple(row['shape'])
        if shape in done:continue
        start=time.time();r,_=run_shape(args.K,shape)
        rows.append(r);done.add(shape);out.write_text(json.dumps(rows,indent=2))
        print(json.dumps(r)+f' seconds={time.time()-start:.1f}',flush=True)

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--K',type=int,default=24)
    ap.add_argument('--rounds',type=int,default=3);ap.add_argument('--roots',type=int,default=7)
    ap.add_argument('--top',type=int,default=6);ap.add_argument('--verify',action='store_true')
    args=ap.parse_args()
    if args.verify:verify_engine()
    elif args.K==24:beam_search(args)
    else:refine(args)
