"""Specialization witnesses and a labelled deformation diagnostic at p=43."""
import json,time
from pathlib import Path
from flint import nmod_mat
from sympy import factorint
from fractions import Fraction
from coupled_pencil import normalized_pencil
from coupled_schur import counts
from distribution_modular import smith_mod

if __name__=='__main__':
    folder=Path(__file__).parent;grid=json.loads((folder/'coupled_grid.json').read_text())
    prior=json.loads(Path(__file__).with_suffix('.json').read_text()) if Path(__file__).with_suffix('.json').exists() else {}
    cache={(r['K'],r['N'],r['p'],r['delta']):r for r in prior.get('deformations',[])}
    witnesses=[]
    for row in grid['special']:
        K,N,p=row['K'],row['N'],row['p'];h=K-N;d=normalized_pencil(K,N,p,6)
        for x in range(1,8):
            matrix=nmod_mat(h,h,[(d['A'][i][j]+x*d['B'][i][j])%p for i in range(h) for j in range(h)],p)
            determinant=int(matrix.det())
            if determinant:break
        assert determinant and row['exact_gauss']==d['tropical']
        witnesses.append(dict(K=K,N=N,p=p,x=x,det_mod_p=determinant,
                              certified_gauss=d['tropical'],constant_valuation=row['constant_valuation']))
    deformed=[]
    for K,N,p in [(128,16,43),(176,22,59),(158,18,53),(248,31,83)]:
        exceptional_delta=(-129*pow(128,-1,p))%p
        deltas=sorted({0,1,2,p,exceptional_delta}) if p in [43,59] else [0,1,p]
        for delta in deltas:
            if (K,N,p,delta) in cache:
                deformed.append(cache[K,N,p,delta]);continue
            d=normalized_pencil(K,N,p,8,harmonic_deformation=delta)
            ss,censored,_=smith_mod(d['A'],p,8);assert not censored
            row=dict(K=K,N=N,p=p,delta=delta,original_functional=(delta==0),
                     tropical=d['tropical'],smith_counts=counts(ss),smith_sum=sum(ss),
                     B_min=d['B_min'],generic_certified=d['B_min']>=max(ss))
            deformed.append(row);print('DEFORMATION '+json.dumps(row),flush=True)
    constants=[]
    for q in [2,3,4]:
        H=sum((Fraction(1,j**7) for j in range(1,q+1)),Fraction(0))
        constants.append(dict(q=q,harmonic=str(H),numerator_factors={str(p):v for p,v in factorint(H.numerator).items()}))
    out=dict(specialization_witnesses=witnesses,harmonic_constants=constants,deformations=deformed,
             warning='Nonzero delta changes the functional. It is a sensitivity experiment, not a zeta(7) construction or a proof of causation.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print('WITNESSES '+json.dumps(witnesses),flush=True)
