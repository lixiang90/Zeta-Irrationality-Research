"""Two-moment p=17 repair with joint old-prime protection parameters.

The bivariate determinant is reconstructed exactly.  This is a bounded
experiment in a restricted two-moment family, not a no-go theorem.
"""
import json,math,sys,hashlib
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat,arb,arb_mat,arb_poly,ctx
from sympy import primerange
import b8_hankel as b8
from joint_exact import determinant,content
from zeta7_moment_extension_20261004 import aq,vp,positive_pivots,ball

sys.set_int_max_str_digits(0)


def centered(x,p):
    x%=p
    return x-p if x>p//2 else x


def main():
    K,N,h,A,B=b8.entries(1)
    W=Poly(b8.Dpoly(N)**8);D=Poly(b8.Dpoly(K))
    quotients=[(W*Poly([0]*s+[1]))//D for s in range(2*h-1)]
    E=[q[47] for q in quotients];F=[q[55] for q in quotients]
    rankE=fmpq_mat([[E[i+j] for j in range(h)] for i in range(h)]).rank()
    rankF=fmpq_mat([[F[i+j] for j in range(h)] for i in range(h)]).rank()
    assert(rankE,rankF)==(10,2)
    samples=[[determinant([a-x*e-y*f for a,e,f in zip(A,E,F)],B,h)
              for y in range(rankF+1)] for x in range(rankE+1)]
    Ix=fmpq_mat([[Q(x)**j for j in range(rankE+1)] for x in range(rankE+1)]).inv()
    Iy=fmpq_mat([[Q(y)**j for j in range(rankF+1)] for y in range(rankF+1)]).inv()
    intermediate=[[sum((samples[x][y]*Ix[i,x] for x in range(rankE+1)),Poly())
                   for y in range(rankF+1)] for i in range(rankE+1)]
    coeff=[[sum((intermediate[i][y]*Iy[j,y] for y in range(rankF+1)),Poly())
            for j in range(rankF+1)] for i in range(rankE+1)]
    assert all(not coeff[i][j] for i in range(rankE+1) for j in range(rankF+1) if i+j>rankE)
    def polynomial(x,y):
        return sum((coeff[i][j]*x**i*y**j for i in range(rankE+1) for j in range(rankF+1)),Poly())
    for x,y in [(Q(-1),Q(1,2)),(Q(2,3),Q(-3,5))]:
        assert polynomial(x,y)==determinant([a-x*e-y*f for a,e,f in zip(A,E,F)],B,h)
    coefficient_packet=dict(K=K,N=N,h=h,moments=[47,55],
                            coefficients=[dict(i=i,j=j,polynomial_coefficients=list(map(str,coeff[i][j])))
                                          for i in range(rankE+1) for j in range(rankF+1) if coeff[i][j]])
    coefficient_text=json.dumps(coefficient_packet,indent=2)
    coefficient_path=Path(__file__).with_name(Path(__file__).stem+'_coefficients.json')
    coefficient_path.write_text(coefficient_text,encoding='utf-8')
    c0=content(coeff[0][0])
    ctx.prec=16000;z=arb(7).zeta()
    H=arb_mat([[aq(A[i+j])+z*aq(B[i+j]) for j in range(h)] for i in range(h)])
    CE=arb_mat([[aq(E[i+j]) for j in range(h)] for i in range(h)])
    CF=arb_mat([[aq(F[i+j]) for j in range(h)] for i in range(h)])
    Hi=H.inv();RE=Hi*CE;RF=Hi*CF
    tEE=(RE*RE).trace();tEF=(RE*RF).trace();tFF=(RF*RF).trace()
    rows=[]
    for a in [0,16,32,48,64,80]:
        for b in [0,8,16,24,32,40]:
            M=2**a*3**b
            x=Q(M*centered(-3*pow(M,-1,17),17),17)
            y=Q(M*centered(-pow(M,-1,17),17),17)
            assert (int((17*x).numerator)%17,int((17*y).numerator)%17)==(14,16)
            poly=polynomial(x,y);ct=content(poly);gain=ct/c0
            tr=aq(x)**2*tEE+2*aq(x)*aq(y)*tEF+aq(y)**2*tFF
            pd=positive_pivots(H-CE*aq(x)-CF*aq(y))
            if tr<1:assert pd['positive_definite'] is True
            val=arb_poly([int(q) for q in poly/ct])(z)
            if pd['positive_definite'] is True:assert val>0
            numerator_left,denominator_left=abs(int(gain.numerator)),int(gain.denominator)
            for p in primerange(2,200):
                while numerator_left%p==0:numerator_left//=p
                while denominator_left%p==0:denominator_left//=p
            row=dict(power2=a,power3=b,scalar_M_log=math.log(M),moment47_correction=str(x),
                     moment55_correction=str(y),trace_relative_square_interval=ball(tr),
                     relative_norm_certified=bool(tr<1),positive_check=pd,
                     content_gain_valuations={str(p):vp(gain,p) for p in primerange(2,200) if vp(gain,p)},
                     unfactored_content_gain_numerator=str(numerator_left),
                     unfactored_content_gain_denominator=str(denominator_left),
                     log_content_gain_interval=ball(aq(gain).log()),
                     log_abs_primitive_interval=ball(abs(val).log()),log_abs_primitive=float(abs(val).log()))
            rows.append(row)
    positive=[r for r in rows if r['positive_check']['positive_definite'] is True]
    best=min(positive,key=lambda r:r['log_abs_primitive'])
    data=dict(status='passed',K=K,N=N,h=h,p=17,rank_moment47=rankE,rank_moment55=rankF,
              exact_interpolation_shape=[rankE+1,rankF+1],exact_interpolation_cross_checks=[['-1','1/2'],['2/3','-3/5']],
              coefficient_file=coefficient_path.name,
              coefficient_file_sha256=hashlib.sha256(coefficient_text.encode()).hexdigest(),
              relative_square_unit_intervals=dict(moment47=ball(tEE),cross=ball(tEF),moment55=ball(tFF)),
              positive_count=len(positive),tested_count=len(rows),best_positive=best,rows=rows,
              scope='Finite restricted two-moment centered CRT family M=2^a3^b only. '
                    'All members retain both p=17 principal-part cancellation conditions. '
                    'The experiment is not an optimal protection lattice computation.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    print('positive',len(positive),'/',len(rows),'best',best['power2'],best['power3'],
          best['log_abs_primitive_interval'],'contentgain',best['log_content_gain_interval'],flush=True)


if __name__=='__main__':main()
