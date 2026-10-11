"""Complete two-variable Hensel exclusions with explicit frontier caps.

The starting residues include every unit pair.  Hence empty lifting trees
exclude ALL higher unit digits at a valuation pair.  A capped tree is marked
unresolved.  Large y valuations are treated separately by an exact x-only
fiber once every y term is beyond the content threshold.
"""
import json,sys,math
from pathlib import Path
from flint import fmpq as Q
from zeta7_all_units_20261004 import valq,modq

sys.set_int_max_str_digits(0)


def lift(coeff,p,a,b,v0,roots0,cap=4096,x_only=False):
    weighted=[]
    for i,j,cs in coeff:
        if x_only and j:continue
        for k,c in enumerate(cs):
            if c:weighted.append((i,j,k,c*Q(p)**(i*a+j*b)))
    m=min(valq(c,p) for i,j,k,c in weighted);D=v0-m
    if D<=0:return dict(status='protected_for_all_units',depth=D,normalization=m)
    modulus=p**D
    rows={}
    for i,j,k,c in weighted:
        c=c/Q(p)**m
        if valq(c,p)>=D:continue
        rows.setdefault(k,[]).append((i,j,modq(c,p,modulus),valq(c,p)))
    def evaluate(u,v,r):
        mod=p**r;up=[pow(u,i,mod) for i in range(11)];vp=[pow(v,j,mod) for j in range(3)]
        out={}
        for k,terms in rows.items():
            active=[(i,j,c) for i,j,c,e in terms if e<r]
            if active:out[k]=sum(c*up[i]*vp[j] for i,j,c in active)%mod
        return out
    def derivative(u,v):
        du={};dv={}
        for k,terms in rows.items():
            du[k]=sum(c*i*pow(u,i-1,p)*pow(v,j,p) for i,j,c,e in terms if not e and i)%p
            dv[k]=sum(c*j*pow(u,i,p)*pow(v,j-1,p) for i,j,c,e in terms if not e and j)%p
        return du,dv
    roots=[(u,v) for u,v in roots0 if not any(evaluate(u,v,1).values())]
    maximum=len(roots)
    if not roots:return dict(status='excluded_all_units',depth=D,normalization=m,obstruction_layer=1,maxbranches=0)
    for r in range(1,D):
        power=p**r;new=[]
        for u,v in roots:
            residual={k:c//power for k,c in evaluate(u,v,r+1).items()}
            du,dv=derivative(u%p,v%p)
            equations=[(du.get(k,0),dv.get(k,0),residual.get(k,0)) for k in set(rows)|set(residual)]
            if x_only:
                choices=[(aa,0) for aa in range(p) if all((z+x*aa)%p==0 for x,y,z in equations)]
            else:
                choices=[(aa,bb) for aa in range(p) for bb in range(p)
                         if all((z+x*aa+y*bb)%p==0 for x,y,z in equations)]
            new.extend((u+power*aa,v+power*bb) for aa,bb in choices)
        roots=new;maximum=max(maximum,len(roots))
        if not roots:return dict(status='excluded_all_units',depth=D,normalization=m,obstruction_layer=r+1,maxbranches=maximum)
        if len(roots)>cap:
            return dict(status='unresolved_frontier_cap',depth=D,normalization=m,reached_layer=r+1,
                        branches=len(roots),maxbranches=maximum,frontier_examples=[[str(u),str(v)] for u,v in roots[:4]])
    assert all(not any(evaluate(u,v,D).values()) for u,v in roots)
    return dict(status='protected_root_classes',depth=D,normalization=m,classes=len(roots),
                roots=[[str(u),str(v)] for u,v in roots],maxbranches=maximum)


def main():
    p=int(sys.argv[1]) if len(sys.argv)>1 else 2
    cap=int(sys.argv[2]) if len(sys.argv)>2 else 4096
    folder=Path(__file__).parent
    d=json.loads((folder/'zeta7_two_moment_partial_20261004_coefficients.json').read_text(encoding='utf-8'))
    coeff=[(r['i'],r['j'],[Q(c) for c in r['polynomial_coefficients']]) for r in d['coefficients']]
    v0=valq(Q(json.loads((folder/'zeta7_joint_lattice_20261004_completion.json').read_text(encoding='utf-8'))['original_baseline_content']),p)
    bounds=json.loads((folder/'zeta7_all_units_20261004_macaulay_d8.json').read_text(encoding='utf-8'))
    lower=next(r['all_unit_minimum_x_valuation'] for r in bounds['results'] if r['p']==p)
    local=json.loads((folder/'zeta7_joint_lattice_20261004.json').read_text(encoding='utf-8'))
    info=next(r for r in local['results'] if r['p']==p);upper=info['termwise_protection_minimum_x_valuation']
    terms=[(r['i'],r['j'],r['v']) for r in info['coefficient_content_valuations']]
    face_map={tuple(tuple(s) for s in f['support']):f['unit_roots'] for f in info['faces']}
    rows=[];excluded_a=[]
    for a in range(lower,upper):
        bcut=max(0,max(math.ceil((v0-v-i*a)/j) for i,j,v in terms if j))
        candidates=[]
        for b in range(bcut):
            weights=[v+i*a+j*b for i,j,v in terms];m=min(weights)
            support=tuple((i,j) for (i,j,v),w in zip(terms,weights) if w==m)
            roots=face_map.get(support,[])
            if roots:candidates.append((b,roots))
        cases=[]
        for b,roots in candidates:
            ans=lift(coeff,p,a,b,v0,roots,cap)
            cases.append(dict(b=b,**ans))
        # For every b>=bcut all y terms are automatically integral at the
        # required level.  Test all x units once, with y=0.
        ans=lift(coeff,p,a,bcut,v0,[(u,1) for u in range(1,p)],cap,x_only=True)
        cases.append(dict(b_range=[bcut,'infinity'],**ans))
        excluded=all(c['status']=='excluded_all_units' for c in cases)
        if excluded:excluded_a.append(a)
        rows.append(dict(a=a,y_cutoff=bcut,initial_candidate_pairs=len(candidates),
                         all_y_valuations_excluded=excluded,cases=cases))
        print('p',p,'a',a,'cases',len(cases),'excluded',excluded,
              {s:sum(c['status']==s for c in cases) for s in sorted(set(c['status'] for c in cases))},flush=True)
        out=dict(status='in_progress',K=40,N=3,h=37,p=p,branch_cap=cap,starting_all_unit_bound=lower,
                 excluded_x_valuations=excluded_a,rows=rows,
                 scope='All higher units at each fully excluded valuation pair are covered. '
                       'Capped pairs remain unresolved. The parameter domain is v_p(x),v_p(y)>=0. '
                       'Valuations below the starting bound are excluded by independent Macaulay certificates.')
        Path(__file__).with_name(Path(__file__).stem+f'_p{p}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    true_lower=next((a for a in range(lower,upper) if a not in excluded_a),upper)
    out['status']='passed';out['certified_all_unit_minimum_x_valuation']=true_lower
    Path(__file__).with_name(Path(__file__).stem+f'_p{p}.json').write_text(json.dumps(out,indent=2),encoding='utf-8')


if __name__=='__main__':main()
