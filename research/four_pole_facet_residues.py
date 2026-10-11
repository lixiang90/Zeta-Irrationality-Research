"""Intrinsic residue budget and exact facet-lattice simplex formulation."""
import json,sys,math,itertools
from pathlib import Path
from flint import fmpq as Q,fmpq_mat,fmpz_mat
from four_pole_positive_lattice import maps,dot
from four_pole_minimal_lifts import floor

sys.set_int_max_str_digits(0)
def qgcd(values):
    den=math.lcm(*(int(x.denominator) for x in values));num=math.gcd(*(int(x*den) for x in values))
    return Q(num,den)
def main():
    root=Path(__file__).parent
    def keyed(file):return {(r['n'],r['m'],r['s']):r for r in json.loads((root/file).read_text())['rows']}
    source=keyed('four_pole_positive_lattice.json');geos=keyed('four_pole_buffer_geometry.json')
    cover=keyed('four_pole_height_cover.json');boundary=keyed('four_pole_boundary_fibers.json')
    charts=json.loads((root/'four_pole_residue_sections.json').read_text())['charts'];out=dict(status='in_progress',rows=[])
    for key,geo in geos.items():
        n,m,s=key;d=m-2;C2,a,b,B=maps(n,m,s);Z=fmpz_mat(geo['zero_basis']);A=fmpq_mat(B)*fmpq_mat(Z)
        chart=next(c for c in charts if tuple(c[k] for k in ('n','m','s'))==key and c['chart_sign']==1)
        W=fmpz_mat(chart['unimodular_completion']);J=fmpz_mat([[W[i,j+1] for j in range(2)] for i in range(m+1)])
        facets={};models=[]
        for simplex in boundary[key]['boundary_simplexes']:
            sign=simplex['sign'];I=simplex['active'];lam=list(map(Q,simplex['positive_dual']))
            rho=[qgcd([A[i,j] for j in range(d)]) for i in I];assert min(rho)>0
            weights=[x*y for x,y in zip(lam,rho)];kappa=qgcd(weights);coins=[int(x/kappa) for x in weights]
            D=fmpz_mat([[int(A[i,j]/rr) for j in range(d)] for i,rr in zip(I,rho)])
            assert all((A[i,j]/rr).denominator==1 for i,rr in zip(I,rho) for j in range(d))
            assert all(sum(coins[i]*int(D[i,j]) for i in range(d+1))==0 for j in range(d))
            minors=[int(fmpz_mat([[D[i,j] for j in range(d)] for i in range(d+1) if i!=omit]).det()) for omit in range(d+1)]
            index=math.gcd(*minors);assert index>0
            model=dict(sign=sign,active=I,positive_dual=list(map(str,lam)),row_steps=list(map(str,rho)),
                       weight_unit=str(kappa),primitive_positive_weights=list(map(str,coins)),
                       facet_lattice=[[int(D[i,j]) for j in range(d)] for i in range(d+1)],
                       maximal_minors=list(map(str,minors)),saturation_index=str(index),index_bits=index.bit_length())
            models.append(model);facets[sign]=(I,lam,rho,kappa,coins,D)
        cases=[];previous={tuple(c['pair']):c['status'] for c in boundary[key]['cases']}
        for candidate in cover[key]['candidates']:
            pair=list(map(int,candidate['pair']));sgn=1 if pair[1]>=0 else -1
            I,lam,rho,kappa,coins,D=facets[sgn];w=list(map(int,candidate['image_coordinates']))
            p=list(J*fmpz_mat([[x] for x in w]));vals=[dot(B[i],p) for i in I]
            n0=[floor(x/rr) for x,rr in zip(vals,rho)];delta=[x-rr*j for x,rr,j in zip(vals,rho,n0)]
            assert all(0<=x<rr for x,rr in zip(delta,rho))
            budget=dot(lam,delta);r=Q(candidate['raw_endpoint_slack']);assert dot(lam,vals)==r
            M=(r-budget)/kappa;assert M.denominator==1 and M==sum(c*j for c,j in zip(coins,n0))
            status='excluded_by_negative_residue_budget' if M<0 else 'necessary_budget_passes'
            if candidate['covered']:assert M>=0
            cases.append(dict(pair=candidate['pair'],residue_budget=str(budget),slack=str(r),
                              integer_budget=str(M),status=status,previous_status=previous.get(tuple(candidate['pair']),'positive_integer_lift_at_k1')))
        newly=sum(c['integer_budget'].startswith('-') and c['previous_status']=='unresolved' for c in cases)
        row=dict(n=n,m=m,s=s,models=models,cases=cases,
                 summary=dict(excluded=sum(c['status']=='excluded_by_negative_residue_budget' for c in cases),newly_excluded=newly))
        out['rows'].append(row)
        print('facet model',key,'indices',[r['index_bits'] for r in models],row['summary'],flush=True)
    out['status']='passed';Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')

if __name__=='__main__':main()
