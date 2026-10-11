"""Independent checks of flag inclusions, fixed divisors and final values."""
import json
from functools import reduce
from math import gcd, lcm
from pathlib import Path

from flint import fmpq, fmpq_mat, fmpq_poly, fmpz_mat, nmod_mat, arb, ctx
from arithmetic_subspaces import integer_pencil, adjugate_coefficients, saturated_kernel, valuation
from joint_exact import evaluate_primitive_ball, content, entries
from mixed_subspaces import determinant_matrices
from padic_subspace_flags import integral_coefficients, identity, restrict, matrix_content, residual_forms, rows

ROOT=Path(__file__).parent


def evalp(P,x):
    y=arb(0)
    for c in reversed(list(P)):
        y=y*x+arb(c)
    return y


def polynomial(u,H):
    u=fmpq_mat(1,len(u),u)
    return fmpq_poly([(u*T*u.transpose())[0,0] for T in H])


def main():
    K=24;N=1;m=24;n=m-1
    A,B,_=integer_pencil(K,N,m);det,H=adjugate_coefficients(A,B);g,F=integral_coefficients(H)
    totals=dict(flag_steps=0,affine_families=0,exact_witness_polynomials=0,
                finite_difference_divisors=0,independent_arb_bounds=0,forced_pole_records=0)
    all_charts=[]
    for prefix in ['padic_subspace_flags','isotropic_subspace_flags','joint_padic_existence']:
        data=json.loads((ROOT/f'{prefix}_K24_N1_m24.json').read_text())
        assert int(data['adjugate_content'])==g
        prev={}
        for step in data.get('flags',[]):
            p=step['p'];T=fmpz_mat(step['lattice_rows']);old=prev.get(p,identity(m))
            exponent,L,Q=residual_forms(F,old,p)
            assert rows(L)==step['residual_row_basis'] and [rows(q) for q in Q]==step['residual_form_basis']
            d=step.get('isotropic_dimension',0)
            if d:
                E=nmod_mat(step['isotropic_rows'],p)
                assert E.rank()==d and all(not E*q*E.transpose() for q in Q)
            inclusion=fmpq_mat(T)*fmpq_mat(old).inv()
            assert all(x.q==1 for x in inclusion.entries())
            assert abs(inclusion.det())==p**(L.nrows()-d)
            assert valuation(matrix_content(restrict(F,T)),p)==step['exponent_after']
            assert exponent==step['exponent_before']
            if p in [3,17] and len(Q)==1 and L.nrows()==2:
                q=Q[0]
                assert all((nmod_mat(1,2,[a,b],p)*q*nmod_mat(2,1,[a,b],p))[0,0]
                           for a in range(p) for b in range(p) if a or b)
            if p==7 and step['step']==2:
                assert len(Q)==1 and Q[0].rank()==7
            prev[p]=T;totals['flag_steps']+=1
        all_charts+=data['charts']
    unique=set();better=[]
    for row in all_charts:
        j=row['chart_coordinate'];cols=[k for k in range(m) if k!=j]
        L=fmpq_mat(row['lattice_rows']);T=fmpq_mat(row['ambient_lattice_rows'])
        av=fmpq_mat(1,m,row['affine_point']);Ti=T.inv()
        V=fmpq_mat(n,m,[0 if k==j else L[i,cols.index(k)] for i in range(n) for k in range(m)])
        assert av[0,j]==1 and all(x.q==1 for x in (av*Ti).entries())
        assert all(x.q==1 for x in (V*Ti).entries())
        assert abs(L.det())==abs(T.det())==int(row['index'])
        D=0;Mlist=[]
        for hk in H:
            M=V*hk*V.transpose();b=V*hk*av.transpose();c=(av*hk*av.transpose())[0,0]
            Mlist.append(M)
            # Gcd of actual values at a finite-difference determining set.
            values=[c]
            values.extend(c+M[i,i]+2*b[i,0] for i in range(n))
            values.extend(c+4*M[i,i]+4*b[i,0] for i in range(n))
            values.extend(c+M[i,i]+M[k,k]+2*M[i,k]+2*b[i,0]+2*b[k,0]
                          for i in range(n) for k in range(i+1,n))
            for x in values:
                assert x.q==1
                D=gcd(D,abs(int(x.p)))
        assert D==int(row['fixed_divisor']);totals['finite_difference_divisors']+=1
        w=row['witness'];u=w['normal'];uv=fmpq_mat(1,m,u)
        # Stored normals use first-nonzero-positive sign normalization.
        assert reduce(gcd,map(abs,u),0)==1 and abs(u[j])==1
        coordinates=fmpq_mat(1,n,[u[k]*u[j]-av[0,k] for k in cols])*L.inv()
        assert all(x.q==1 for x in coordinates.entries())
        assert all(x.q==1 for x in (uv*Ti).entries())
        P=polynomial(u,H);C=saturated_kernel(u)
        assert P==fmpq_poly([fmpq(x) for x in w['poly']])
        assert P==determinant_matrices(C*A*C.transpose(),C*B*C.transpose())
        ct,lv,bits=evaluate_primitive_ball(P)
        assert str(ct)==w['content'] and int(ct)%D==0
        bits=max(bits,max(abs(int(x.p)).bit_length() for hk in H for x in hk.entries())+800)
        with ctx.workprec(bits):
            z=arb(7).zeta();jj=arb(A[j,j])+z*arb(B[j,j])
            star=fmpq_mat(1,n,[A[k,j]-av[0,k]*A[j,j] for k in cols])*L.inv()
            slope=fmpq_mat(1,n,[B[k,j]-av[0,k]*B[j,j] for k in cols])*L.inv()
            total=evalp(det,z)/jj
            for i in range(n):
                alpha=(arb(star[0,i])+z*arb(slope[0,i]))/jj
                floor=alpha.floor().unique_fmpz()
                if floor is None:
                    close=int(alpha.mid().floor().unique_fmpz())
                    candidate=next(v for v in [close,close+1]
                                   if star[0,i]==v*A[j,j] and slope[0,i]==v*B[j,j])
                    variance=arb(0)
                else:
                    theta=alpha-int(floor);variance=theta*(1-theta)
                total+=variance*evalp(fmpq_poly([M[i,i] for M in Mlist]),z)
            bound=total/D
            assert abs(bound.log()/K**2-arb(row['existence_score_ball']))<arb('1e-27')
            assert evalp(P,z)/D<=bound
            assert abs(lv/K**2-arb(w['score_ball']))<arb('1e-27')
            if lv/K**2<arb('0.747563909116364061456044642939'):
                better.append(tuple(u))
        unique.add(tuple(u));totals['affine_families']+=1
        totals['independent_arb_bounds']+=1;totals['exact_witness_polynomials']+=1
        if totals['affine_families']%10==0:
            print('verified affine families',totals['affine_families'],flush=True)
    # Squarefree self-adjoint generator is a certificate of no common zeros.
    cert=json.loads((ROOT/'residual_etale_certificate_K24_p17_level3.json').read_text())
    flags=json.loads((ROOT/'padic_subspace_flags_K24_N1_m24.json').read_text())
    flag=next(r for r in flags['flags'] if r['p']==17 and r['step']==3)
    Q=[nmod_mat(q,17) for q in flag['residual_form_basis']]
    R=nmod_mat(cert['base_form'],17);M=nmod_mat(cert['generator'],17)
    assert R==Q[0] and R*M==Q[1] and R.det()
    cp=M.charpoly();assert list(map(int,cp))==cert['characteristic_polynomial']
    assert cp.gcd(cp.derivative()).degree()==0
    change=nmod_mat(cert['power_coefficients'],17);assert change.det()
    current=R
    for k in range(9):
        combination=sum((q*int(change[k,i]) for i,q in enumerate(Q)),nmod_mat(9,9,17))
        assert current==combination;current=current*M
    forced=json.loads((ROOT/'forced_pole_subspaces.json').read_text())
    controls=json.loads((ROOT/'forced_pole_degree_controls.json').read_text())
    scaled=[]
    for row in forced['rows']+controls['rows']:
        P=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])
        ct,lv,bits=evaluate_primitive_ball(P);assert ct==1
        with ctx.workprec(160):
            assert abs(lv/row['K']**2-arb(row['score_ball']))<arb('1e-27')
        # Independent full-matrix determinant evaluations at degree+1 points
        # prove polynomial proportionality, using the surviving-pole degree
        # bound. Clearing entry denominators keeps memory use bounded.
        if row['label']=='scaled_block' or (row['K']==24 and row['roots']==[2]):
            k,nn,hh=row['K'],row['N'],row['h']
            aa,bb=entries(k,[(nn,6),(2*nn,2)],hh)
            den=lcm(*(int(x.q) for x in aa+bb))
            ai=fmpz_mat(hh,hh,[int(aa[i+j]*den) for i in range(hh) for j in range(hh)])
            bi=fmpz_mat(hh,hh,[int(bb[i+j]*den) for i in range(hh) for j in range(hh)])
            d=k-2*nn;assert P.degree()==d and bi.rank()==d
            base=ai.det();assert base and P(0)
            print('checking full Hankel evaluations',k,'points',d+1,flush=True)
            for x in range(1,d+1):
                assert (ai+bi*x).det()*P(0)==base*P(x)
                if x%20==0:
                    print('Hankel evaluation',k,x,flush=True)
            assert base/P(0)>0
            scaled.append(k)
        totals['forced_pole_records']+=1
    result=dict(totals=totals,unique_hyperplanes=len(unique),
                hyperplanes_better_than_original=[list(u) for u in sorted(set(better))],
                etale_no_common_zero_certificate=True,independent_scaled_determinants=scaled,
                best_existence_score=min(r['existence_score'] for r in all_charts),
                best_witness_score=min(r['witness']['score'] for r in all_charts))
    (ROOT/'padic_subspaces_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
