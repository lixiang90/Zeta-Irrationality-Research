"""Independent finite checks of the moment-threshold and rank lemmas."""
import json
from pathlib import Path
from flint import fmpq as Q, fmpq_poly, nmod_mat
import zeta35_mixed_moments as mixed
from zeta35_target31 import primes_to
from zeta35_target31_scan import entries

def mu5(e):
    return Q(-1)**e*Q.bernoulli(2*e+2)*(2*e+3)*(2*e+4)*(2*e+5)/24

def nu(e):return mu5(e)-3*mixed.mu3(e+1)

def integral(q,p):return int(q.denominator)%p!=0

def mod(q,p):
    assert integral(q,p)
    return (int(q.numerator)*pow(int(q.denominator),-1,p))%p

def main():
    primes=[p for p in primes_to(101) if p>=5]
    for p in primes:
        assert all(integral(mu5(e),p) for e in range(2*p-3))
        assert not integral(mu5(2*p-3),p)
        assert all(integral(nu(e),p) for e in range(p-3))
        assert not integral(nu(p-3),p) and integral(p*nu(p-3),p)
    K,N,h,A5,B=mixed.original.entries(1)
    A3=mixed.shifted_mu3_entries(1)
    hh,Anew,Bnew=entries(K,N,6)
    assert hh==h and Bnew==B and Anew==[x-3*y for x,y in zip(A5,A3)]
    W=fmpq_poly(mixed.original.Dpoly(N)**6)
    DK=fmpq_poly(mixed.original.Dpoly(K))
    qs=[(W*fmpq_poly([0]*e+[1]))//DK for e in range(2*h-1)]
    ranks=[]
    for p in primes:
        r=2*h+6*N-K+2-p
        if not 0<=r<=h: continue
        seq=[]
        for q in qs:
            value=sum((q[k]*nu(k) for k in range(p-3,q.degree()+1)),Q(0))
            seq.append(mod(p*value,p))
        observed=nmod_mat([[seq[i+j] for j in range(h)] for i in range(h)],p).rank()
        assert observed==r,(p,r,observed)
        ranks.append(dict(p=p,predicted=r,observed=observed))
    result=dict(status='passed',moment_threshold_primes=primes,high_part_ranks=ranks,
        generic_entries_match_original_mixed=True,
        scope='finite checks supporting separately written elementary proofs; not a Lean formalization')
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
