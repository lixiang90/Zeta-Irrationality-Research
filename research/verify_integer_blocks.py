"""Verification of block scans, asymptotic certificates and parameter pencils."""
import json,math
from fractions import Fraction as F
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpz_mat
import mpmath as mp
from integer_blocks import polynomials,scalar,ilog
from integer_block_budget import geometry,lines_for,tail,real_lower,profiles
from two_prefix_budget import linval
from joint_exact import entries_from_polynomial,determinant_pole_split,content,Dcache
from two_prefix_outer import vp
from restart_obstruction_certificate import outward_decimal


def check_poly(K,N,blocks):
    selected,W,T=polynomials(K,N,blocks);h=T.degree();aa,bb=entries_from_polynomial(K,W,h)
    P=determinant_pole_split(aa,bb,T,h)
    return check_values(K,N,h,aa,bb,P,dict(blocks=blocks))


def check_values(K,N,h,aa,bb,P,extra):
    den=math.lcm(*(int(c.q) for c in aa+bb));scale=den**h
    for x in range(h+1):
        mat=fmpz_mat(h,h,[int(den*(aa[i+j]+x*bb[i+j])) for i in range(h) for j in range(h)])
        assert mat.det()==P(x)*scale
    return dict(K=K,N=N,h=h,specializations=h+1,**extra)


def main():
    folder=Path(__file__).parent;rows=[]
    for name in ('integer_blocks_K24.json','integer_blocks_K48.json','integer_blocks_K96.json','integer_blocks_two.json'):
        rows+=json.loads((folder/name).read_text())['rows']
    checks=0
    for row in rows:
        K,N,h=(row[k] for k in ('K','N','h'));assert row['degree']==h and row['score']>0
        S=scalar(K,N,row['blocks'],h);assert S==fmpq(row['scalar']);ct=fmpq(row['content'])
        for local in row['local']:
            assert vp(S*ct,local['p'])==local['actual']>=local['lower'];checks+=1
    summaries=[]
    for K in (24,48,96):
        rs=[r for r in rows if r['K']==K and len(r['blocks'])==1]
        N=K//24;comparisons=[]
        for L in sorted({r['blocks'][0][1] for r in rs}):
            same=[r for r in rs if r['blocks'][0][1]==L];base=next(r for r in same if r['blocks'][0][0]==N)
            assert all(r['score']>=base['score']-1e-13 for r in same)
            shifted=min((r for r in same if r['blocks'][0][0]>N),key=lambda r:r['score'])
            comparisons.append(dict(L=L,prefix_score=base['score'],best_shift=shifted['blocks'][0][0],
                                    best_shifted_score=shifted['score']))
        summaries.append(dict(K=K,comparisons=comparisons))
    pencils=[]
    for K in (24,48,96):pencils+=json.loads((folder/f'integer_block_pencils_K{K}.json').read_text())['rows']
    for row in pencils:
        P=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']]);assert content(P)==1
        K,N,h=(row[k] for k in ('K','N','h'));ct=fmpq(row['content']);S=fmpq(row['scalar'])
        for p in (2,3,5,7):assert vp(S*ct,p)>=-8*h*ilog(p,4*K+12*N+4)-h*vp(fmpq(720),p)
    certs=[check_poly(24,1,[(2,3)]),check_poly(48,2,[(3,6)]),check_poly(24,1,[(1,2),(4,1)])]
    for K in (24,48):
        row=next(r for r in pencils if r['K']==K and r['s']==K//24 and r['u']==-1)
        N,L,h=(row[k] for k in ('N','L','h'));Q=fmpq_poly([fmpq(c) for c in row['numerator']])
        aa,bb=entries_from_polynomial(K,Dcache(N)**8*Q**2,h)
        P=fmpq_poly([fmpq(c) for c in row['primitive_polynomial']])*fmpq(row['content'])
        certs.append(check_values(K,N,h,aa,bb,P,dict(s=row['s'],u=-1)))
    budgets=json.loads((folder/'integer_block_budget.json').read_text())['rows'];piece_count=0;real_checks=[]
    for row in budgets:
        alpha=F(row['alpha']);blocks=[tuple(map(F,b)) for b in row['blocks']];s=F(row['test_s'])
        cuts=geometry(alpha,blocks,row['cutoff']);total=F(0)
        for l,r,name,a,b in row['pieces']:
            l,r,a,b=map(F,(l,r,a,b));x=(l+r)/2
            cl,cr=next((l0,r0) for l0,r0 in zip(cuts,cuts[1:]) if l0<x<r0)
            candidates=lines_for(alpha,blocks,cl,cr);assert candidates[name]==(a,b)
            assert all(a*t+b<=linval(v,t) for v in candidates.values() for t in (l,r))
            total+=a*(1/l-1/r)+b*(1/l**2-1/r**2)/2;piece_count+=1
        T,_=tail(alpha,blocks,row['cutoff'],row['tail_end']);A=total+T;B=real_lower(alpha,blocks,s)
        assert outward_decimal(A)==row['A_interval'] and outward_decimal(A+B)==row['gap_interval']
        with mp.workdps(60):
            conv=lambda x:mp.mpf(x.numerator)/x.denominator
            root,sel,norm=profiles(alpha,blocks);lam=1-alpha-sum(L for a,L in blocks);lm,sm=conv(lam),conv(s)
            def J(c,t):
                y=mp.sqrt(t)
                return c*mp.log(t+c*c)-2*c+2*y*mp.atan(c/y) if t else 2*c*(mp.log(c)-1)
            def V(t):return 2*mp.pi*mp.sqrt(t)+J(mp.mpf(1),t)-sum(v*J(conv(a),t) for a,v in root.items())
            C=-2*lm+sum(2*v*conv(a)*lm*(1-mp.log(conv(a))) for a,v in norm.items())+3*lm**2-2*lm**2*mp.log(2*lm)
            numeric=lm*lm*(mp.log(sm*sm)-mp.mpf('1.5'))-lm*mp.quad(V,[0,sm*sm])/(sm*sm)+C
            assert abs(numeric-conv((B.lo+B.hi)/2))<mp.mpf('1e-35')
            real_checks.append(str(numeric))
    # Algebraic integer-valued identity with generalized binomial coefficients.
    integer_checks=0
    def binom(n,k):return F(math.prod(n-i for i in range(k)),math.factorial(k))
    for a in range(1,13):
        for L in range(1,9):
            for x in range(-15,16):
                value=F(math.prod(j*j-x*x for j in range(a+1,a+L+1)),math.factorial(L)**2)
                assert value==(-1)**L*binom(x-a-1,L)*binom(x+a+L,L) and value.denominator==1
                integer_checks+=1
    result=dict(block_records=len(rows),block_prime_checks=checks,pencil_records=len(pencils),
                pencil_small_prime_checks=4*len(pencils),integer_value_checks=integer_checks,
                full_polynomial_certificates=certs,integer_determinants=sum(c['specializations'] for c in certs),
                envelope_pieces_checked=piece_count,real_cross_checks=real_checks,comparisons=summaries)
    (folder/'integer_blocks_validation.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('real_cross_checks','comparisons')}),flush=True)


if __name__=='__main__':main()
