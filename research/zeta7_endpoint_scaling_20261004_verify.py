"""Independent exact/Arb audit of the three saved rank-two endpoint scales."""
import json, math, sys
from pathlib import Path
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat, arb, arb_poly, ctx
from joint_exact import entries, content
from zeta7_space_extension_probe import polynomial
from zeta7_moment_extension_20261004 import aq, vp
from b8_hankel import Dpoly, mu_monomial

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent;PREFIX='zeta7_endpoint_scaling_20261004'

def ev(p,z):return arb_poly([aq(v) for v in p])(z)
def pref(M,n):return Mat([[M[i,j] for j in range(n)] for i in range(n)])
def ball(v):return v.str(55)

def run(N):
    d=json.loads((ROOT/f'{PREFIX}_N{N}.json').read_text(encoding='utf-8'))
    K,h,q,e=d['K'],d['h'],d['q'],d['corrected_moment']
    f=[Poly([Q(v) for v in p]) for p in d['coefficient_polynomials']]
    aa,bb=entries(K,[(N,8)],h)
    A=Mat([[aa[i+j] for j in range(h)] for i in range(h)])
    B=Mat([[bb[i+j] for j in range(h)] for i in range(h)])
    W,D=Poly(Dpoly(N)**8),Poly(Dpoly(K));corr=[]
    for s in range(2*h-1):corr.append(((W*Poly([0]*s+[1]))//D)[e])
    assert list(map(str,corr))==d['correction_sequence']
    C=Mat([[corr[i+j] for j in range(h)] for i in range(h)])
    assert C.rank()==2 and f[0]==polynomial(A,B)
    head=polynomial(pref(A,h-2),pref(B,h-2));assert head==-f[2]
    ct0,ctT=content(f[0]),content(head)
    assert str(ct0)==d['baseline_content']
    ctx.prec=d['precision_bits']+3000;z=arb(7).zeta()
    base=ev(f[0]/ct0,z);PT=ev(head/ctT,z);detT=ev(head,z);assert base>0 and PT>0
    center=ev(f[1],z)/(2*detT);R=(ev(f[0],z)/detT+center*center).sqrt()
    rows=[];mu=mu_monomial(e);assert vp(mu,q)==-1
    for r in d['cosets']:
        L=int(r['step']);alpha=Q(r['coset_start'])
        F=[f[0]+alpha*f[1]+alpha*alpha*f[2],L*f[1]+2*alpha*L*f[2],L*L*f[2]]
        assert F==[Poly([Q(v) for v in p]) for p in r['coset_coefficient_polynomials']]
        cstar=content(Poly([v for p in F for v in p]));assert str(cstar)==r['all_parameter_content']
        M=L*L*ctT/cstar;assert M.denominator==1 and str(M)==r['integer_M']
        if not r['positive_interval_wider_than_step']:
            assert not 2*R>L;rows.append(dict(label=r['label'],status='width_failure_verified'));continue
        assert 2*R>L
        U=2*R*L*detT/aq(cstar);assert U>PT and U.overlaps((2*R/L)*aq(M)*PT)
        y=Q(r['endpoint_y']);k=(y-alpha)/L
        assert k.denominator==1 and str(k)==r['parameter_k'] and vp(mu-y,q)>=0
        delta=center+R-aq(y);assert 0<delta<L and delta<2*R
        p=f[0]+y*f[1]+y*y*f[2];ct=content(p);extra=ct/cstar
        assert extra.denominator==1 and str(extra)==r['extra_parameter_content']
        pr=p/ct;assert pr==Poly([Q(v) for v in r['primitive_coefficients']])
        assert all(v.denominator==1 for v in pr) and math.gcd(*(int(v) for v in pr))==1
        value=ev(pr,z);assert 0<value<U
        assert value.overlaps(U*(delta/L)*(1-delta/(2*R))/aq(extra))
        for x in (-1,0,1):assert p(x)==(A-y*C+x*B).det()
        full=False
        if r['label']=='baseline_content_protected_step':
            assert p==polynomial(A-y*C,B);full=True
        rows.append(dict(label=r['label'],status='verified',M=str(M),
                         logU_interval=ball(U.log()),logPT_interval=ball(PT.log()),
                         head_gap_interval=ball(U.log()-PT.log()),
                         endpoint_distance_over_L=ball(delta/L),extra_parameter_content=str(extra),
                         actual_minus_baseline=ball(value.log()-base.log()),
                         actual_minus_head=ball(value.log()-PT.log()),
                         independent_full_polynomial=full,exact_determinant_X_checks=[-1,0,1]))
        print('verified K',K,r['label'],'gain',float(value.log()-base.log()),flush=True)
    return dict(N=N,K=K,h=h,q=q,head_full_polynomial_identity=True,baseline_full_polynomial_verified=True,rows=rows)

if __name__=='__main__':
    out=dict(status='independently_verified',cases=[run(N) for N in (3,4,5)])
    (ROOT/f'{PREFIX}_verify.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
