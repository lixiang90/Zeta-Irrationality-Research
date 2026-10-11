"""Bounded independent-scale and z=x-3y search, using the saved exact pencil."""
import json,math,sys
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,arb_poly,ctx
import b8_hankel as b8
from joint_exact import content
from zeta7_moment_extension_20261004 import aq,ball,positive_pivots

sys.set_int_max_str_digits(0)


def center(v):
    v%=17
    return v-17 if v>8 else v


def main():
    folder=Path(__file__).parent
    d=json.loads((folder/'zeta7_two_moment_partial_20261004_coefficients.json').read_text(encoding='utf-8'))
    coeff=[(r['i'],r['j'],Poly([Q(c) for c in r['polynomial_coefficients']])) for r in d['coefficients']]
    def polynomial(x,y):
        xp=[x**i for i in range(11)];yp=[y**j for j in range(3)]
        return sum((p*xp[i]*yp[j] for i,j,p in coeff),Poly())
    K,N,h,A,B=b8.entries(1);W=Poly(b8.Dpoly(N)**8);D=Poly(b8.Dpoly(K))
    quotients=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    E=[q[47] for q in quotients];F=[q[55] for q in quotients]
    ctx.prec=16000;z=arb(7).zeta()
    H=arb_mat([[aq(A[i+j])+z*aq(B[i+j]) for j in range(h)] for i in range(h)])
    CE=arb_mat([[aq(E[i+j]) for j in range(h)] for i in range(h)])
    CF=arb_mat([[aq(F[i+j]) for j in range(h)] for i in range(h)])
    RE=H.inv()*CE;RF=H.inv()*CF
    tEE=(RE*RE).trace();tEF=(RE*RF).trace();tFF=(RF*RF).trace()
    baseline=polynomial(Q(0),Q(0));c0=content(baseline)
    basevalue=arb_poly([int(q) for q in baseline/c0])(z)
    candidates={}
    xscales=[(64,32),(64,40),(72,32),(72,36),(72,40),(80,24),(80,28),(80,32)]
    yscales=[(a,b) for a in [48,64,80,96] for b in [24,32,40]]
    for a,b in xscales:
        Mx=2**a*3**b;x=Q(Mx*center(-3*pow(Mx,-1,17)),17)
        for c,e in yscales:
            My=2**c*3**e;uy=center(-pow(My,-1,17))
            for shift in [-1,0,1]:
                y=Q(My*(uy+17*shift),17)
                candidates[(str(x),str(y))]=dict(kind='independent_scales',x_power2=a,x_power3=b,y_power2=c,y_power3=e,y_integer_shift=shift)
    for a,b in [(64,40),(72,32),(72,36),(80,24)]:
        M=2**a*3**b;y=Q(M*center(-pow(M,-1,17)),17)
        for shift in [-3,-2,-1,0,1,2,3]:
            zz=Q(M*shift);x=3*y+zz
            candidates[(str(x),str(y))]=dict(kind='z_coordinate',M_power2=a,M_power3=b,z_multiple=shift,z_value=str(zz))
    rows=[]
    for (sx,sy),meta in candidates.items():
        x,y=Q(sx),Q(sy)
        assert int((17*x).numerator)%17==14 and int((17*y).numerator)%17==16
        assert (x-3*y).denominator%17
        tr=aq(x)**2*tEE+2*aq(x)*aq(y)*tEF+aq(y)**2*tFF
        if tr<1:pd=dict(positive_definite=True,proof='relative_square_trace_below_one')
        else:
            pd=positive_pivots(H-CE*aq(x)-CF*aq(y))
            if 'pivot_interval' in pd:pd['pivot_interval']=str(arb(pd['pivot_interval']).str(80))
        poly=polynomial(x,y);ct=content(poly)
        value=arb_poly([int(q) for q in poly/ct])(z)
        if pd['positive_definite'] is True:assert value>0
        rows.append(dict(**meta,x=sx,y=sy,z=str(x-3*y),trace_relative_square_interval=ball(tr),
                         positive_check=pd,log_content_gain_interval=ball(aq(ct/c0).log()),
                         log_abs_primitive_interval=ball(abs(value).log()),log_abs_primitive=float(abs(value).log())))
    positive=[r for r in rows if r['positive_check']['positive_definite'] is True]
    best=min(positive,key=lambda r:r['log_abs_primitive'])
    out=dict(status='passed',K=K,N=N,h=h,tested_count=len(rows),positive_count=len(positive),
             baseline_log_primitive_interval=ball(basevalue.log()),best_positive=best,
             relative_geometry=dict(trace_unit47=ball(tEE),trace_cross=ball(tEF),trace_unit55=ball(tFF),
                  trace_correlation_interval=ball(tEF/(tEE*tFF).sqrt()),
                  projected_trace_unit47=ball(tEE-tEF*tEF/tFF)),rows=rows,
             scope='Bounded explicit independent powers of 2 and 3, centered p17 representatives '
                   'with three y shifts, plus seven z-coordinate shifts. '
                   'Every value uses full exact polynomial content. No optimality claim.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('tested',len(rows),'positive',len(positive),'best',best['kind'],best['log_abs_primitive_interval'],flush=True)


if __name__=='__main__':main()
