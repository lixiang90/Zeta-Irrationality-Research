"""Exact y-content conductors with rigorous two-dimensional Schur completion.

For each fixed x, old content is protected termwise in the whole quadratic
y pencil.  Candidate y values nearest the certified positivity endpoints
are evaluated with full primitive content, not a relative-norm heuristic.
"""
import json,math,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,arb_poly,ctx
from sympy import primerange
import b8_hankel as b8
from joint_exact import content
from zeta7_joint_lattice_20261004 import vp
from zeta7_moment_extension_20261004 import aq,ball,positive_pivots

sys.set_int_max_str_digits(0)


def main():
    folder=Path(__file__).parent
    d=json.loads((folder/'zeta7_two_moment_partial_20261004_coefficients.json').read_text(encoding='utf-8'))
    coeff=[(r['i'],r['j'],Poly([Q(c) for c in r['polynomial_coefficients']])) for r in d['coefficients']]
    K,N,h,A,B=b8.entries(1);W=Poly(b8.Dpoly(N)**8);D=Poly(b8.Dpoly(K))
    quotients=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    E=[q[47] for q in quotients];F=[q[55] for q in quotients]
    assert F[70]==0 and F[71]==1 and F[72]==-22028
    ctx.prec=16000;z=arb(7).zeta()
    H=arb_mat([[aq(A[i+j])+z*aq(B[i+j]) for j in range(h)] for i in range(h)])
    CE=arb_mat([[aq(E[i+j]) for j in range(h)] for i in range(h)])
    CF=arb_mat([[aq(F[i+j]) for j in range(h)] for i in range(h)])
    cbase=content(coeff[0][2]);basevalue=arb_poly([int(q) for q in coeff[0][2]/cbase])(z)
    base_raw_det=H.det()
    shapes=[(80,40,0,0),(88,32,0,0),(72,36,4,0),(64,32,8,2),
            (56,24,12,7),(48,32,12,7),(64,24,12,4),(64,24,10,7),(56,32,8,7)]
    rows=[]
    primes=list(primerange(2,200))
    for aa,bb,cc,dd in shapes:
        M=2**aa*3**bb*5**cc*7**dd;u=-3*pow(M,-1,17)%17;x=Q(M*u,17)
        Hx=H-CE*aq(x)
        top=arb_mat([[Hx[i,j] for j in range(35)] for i in range(35)])
        pdtop=positive_pivots(top)
        meta=dict(powers=[aa,bb,cc,dd],x=str(x),log_abs_x=ball(aq(x).log()))
        if pdtop['positive_definite'] is not True:
            rows.append(dict(**meta,completion_possible=False,reason='leading35_not_positive'));continue
        U=arb_mat([[Hx[i,j] for j in range(35,37)] for i in range(35)])
        V=arb_mat([[Hx[i,j] for j in range(35,37)] for i in range(35,37)])
        S=V-U.transpose()*top.inv()*U
        a,b,ddr=S[0,0],S[0,1],S[1,1]
        if not a>0:
            rows.append(dict(**meta,completion_possible=False,reason='leading36_not_positive'));continue
        center=b+11014*a
        radius2=a*ddr-b*b+center*center
        if not radius2>0:
            rows.append(dict(**meta,completion_possible=False,reason='negative_completion_discriminant'));continue
        radius=radius2.sqrt();lower,upper=center-radius,center+radius
        ycoeff=[sum((p*x**i for i,jj,p in coeff if jj==j),Poly()) for j in range(3)]
        contents=list(map(content,ycoeff));cx=contents[0]
        n,dn=abs(int(cx.numerator)),int(cx.denominator)
        for p in primes:
            while n%p==0:n//=p
            while dn%p==0:dn//=p
        assert n==dn==1
        for ct in contents:
            de=int(ct.denominator)
            for p in primes:
                while de%p==0:de//=p
            assert de==1
        protect={}
        for p in primes:
            if p==17:continue
            req=int(max(0,max(math.ceil(Q(vp(cx,p)-vp(contents[j],p),j)) for j in [1,2])))
            if req:protect[str(p)]=req
        L=math.prod(int(p)**e for p,e in protect.items());uy=-pow(L,-1,17)%17
        lowk=((lower/aq(Q(L)))-aq(Q(uy,17))).ceil().unique_fmpz()
        highk=((upper/aq(Q(L)))-aq(Q(uy,17))).floor().unique_fmpz()
        assert lowk is not None and highk is not None
        choices=[]
        for label,k in [('lower',int(lowk)),('upper',int(highk))]:
            y=Q(L*(uy+17*k),17)
            if not lower<aq(y)<upper:continue
            assert int((17*y).numerator)%17==16
            if label=='lower':assert aq(y-L)<lower
            else:assert aq(y+L)>upper
            poly=ycoeff[0]+ycoeff[1]*y+ycoeff[2]*y*y;ct=content(poly)
            assert all(vp(ct/cx,p)>=0 for p in primes if p!=17)
            pd=positive_pivots(Hx-CF*aq(y));assert pd['positive_definite'] is True
            value=arb_poly([int(q) for q in poly/ct])(z);assert value>0
            direct_det=(Hx-CF*aq(y)).det()
            assert (direct_det-aq(ct)*value).contains(0)
            ratio=direct_det/base_raw_det
            assert ratio>0
            gain=ct/cbase;n,dn=abs(int(gain.numerator)),int(gain.denominator)
            for p in primes:
                while n%p==0:n//=p
                while dn%p==0:dn//=p
            assert n==dn==1
            choices.append(dict(endpoint=label,y=str(y),log_abs_y=ball(aq(abs(y)).log()),positive_check=pd,
                                log_content_gain_interval=ball(aq(ct/cbase).log()),
                                content=str(ct),content_ratio_to_original_baseline=str(ct/cbase),
                                content_gain_valuations_to_original_baseline={str(p):vp(ct/cbase,p) for p in primes if vp(ct/cbase,p)},
                                content_gain_valuations_to_fixed_x={str(p):vp(ct/cx,p) for p in primes if vp(ct/cx,p)},
                                log_real_determinant_ratio_to_original_baseline_interval=ball(ratio.log()),
                                direct_determinant_and_polynomial_ball_intersect=True,
                                nearest_allowed_inside_endpoint_verified=True,
                                log_primitive_interval=ball(value.log()),log_primitive=float(value.log())))
        rows.append(dict(**meta,completion_possible=True,center_interval=ball(center),radius_interval=ball(radius),
                         y_conductor=str(L),y_conductor_log=math.log(L),protection=protect,
                         fixed_x_content=str(cx),fixed_x_log_content_ratio_to_original_baseline=ball(aq(cx/cbase).log()),
                         fixed_x_content_gain_valuations_to_original_baseline={str(p):vp(cx/cbase,p) for p in primes if vp(cx/cbase,p)},
                         y_coefficient_contents=list(map(str,contents)),choices=choices))
        print('shape',aa,bb,cc,dd,'xlog',float(aq(x).log()),'Llog',math.log(L),'choices',
              [(r['endpoint'],r['log_primitive']) for r in choices],flush=True)
    choices=[dict(powers=r['powers'],x=r['x'],**c) for r in rows for c in r.get('choices',[])]
    best=min(choices,key=lambda r:r['log_primitive']) if choices else None
    out=dict(status='passed',K=K,N=N,h=h,baseline_log_primitive_interval=ball(basevalue.log()),
             original_baseline_content=str(cbase),
             two_tail_correction_matrix=[[0,1],[1,-22028]],
             positivity_formula='leading35 positive; a>0; |y-(b+11014a)|<sqrt(ad-b²+(b+11014a)²)',
             best_positive=best,rows=rows,
             scope='Nine fixed positive x scales and their exact termwise y protection conductors. '
                   'Nearest endpoint integer-conductor choices are finite arithmetic data. '
                   'This does not optimize the full nonlinear p-adic protection set.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('best',best['log_primitive_interval'] if best else None,flush=True)


if __name__=='__main__':main()
