"""Full integer-parameter extra-content classification on one saved coset.

An affine Macaulay identity bounds all parameter gcds. Exact p-adic balls
classify simultaneous quadratic roots, including arbitrarily high units.
"""
import hashlib,itertools,json,math,sys,time
from pathlib import Path
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat as Mat,fmpz_mat as ZMat

sys.set_int_max_str_digits(0)
ROOT=Path(__file__).parent


def setup():
    names=['zeta7_two_moment_partial_20261004_coefficients.json','zeta7_endpoint_budget_20261004.json']
    source={n:(ROOT/n).read_bytes() for n in names}
    packet=json.loads(source[names[0]]);budget=json.loads(source[names[1]])
    r=next(r for r in budget['rows'] if r['powers']==[64,24,10,7])
    x=Q(r['x']);a=Q(r['coset_start']);L=Q(r['coset_step']);cs=Q(r['all_parameter_content'])
    c=[(d['i'],d['j'],Poly([Q(v) for v in d['polynomial_coefficients']])) for d in packet['coefficients']]
    f=[sum((p*x**i for i,j,p in c if j==jj),Poly()) for jj in range(3)]
    pol=[(f[0]+a*f[1]+a*a*f[2])/cs,L*(f[1]+2*a*f[2])/cs,L*L*f[2]/cs]
    F=[[int(pol[j][e]) for j in range(3)] for e in range(max(q.degree() for q in pol)+1)]
    assert all(v.denominator==1 for p in pol for v in p)
    assert math.gcd(*(v for row in F for v in row))==1
    return source,r,F


def constant_certificate(F,degree):
    rows=[];labels=[]
    for i,row in enumerate(F):
        for shift in range(degree-1):
            rows.append([0]*shift+row+[0]*(degree-2-shift));labels.append((i,shift))
    A=ZMat(rows);H,U=A.hnf(transform=True);assert U*A==H
    indices=[i for i in range(H.nrows()) if any(H[i,j] for j in range(H.ncols()))]
    assert len(indices)==degree+1
    B=Mat([[Q(H[i,j]) for j in range(H.ncols())] for i in indices]);inv=B.inv()
    d=math.lcm(*(int(inv[0,j].denominator) for j in range(degree+1)))
    witness=[sum((d*inv[0,j]*Q(U[indices[j],i]) for j in range(degree+1)),Q(0)) for i in range(len(rows))]
    assert all(w.denominator==1 for w in witness)
    witness=[int(w) for w in witness]
    assert [sum(w*row[j] for w,row in zip(witness,rows)) for j in range(degree+1)]==[d]+[0]*degree
    return dict(degree=degree,constant=str(d),identity_multipliers=[dict(X_coefficient=i,k_power=shift,multiplier=str(w))
               for (i,shift),w in zip(labels,witness) if w])


def factor_small(d):
    factors={}
    for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97):
        e=0
        while d%p==0:d//=p;e+=1
        if e:factors[p]=e
    assert d==1,'unfactored constant'
    return factors


def root_balls(F,p,e):
    modulus=p**e;visits=0
    def recurse(r,power,level):
        nonlocal visits
        visits+=1
        if visits>250000:raise RuntimeError('root-tree bound reached')
        all_divisible=True
        for a,b,c in F:
            A=(a+b*r+c*r*r)%modulus
            B=(power*(b+2*c*r))%modulus
            C=(power*power*c)%modulus
            if A or B or C:all_divisible=False
            # If the fixed value has smaller valuation than every possible
            # correction, no continuation of this entire ball can be a root.
            def vp(v):
                if not v:return e
                n=0
                while v%p==0:v//=p;n+=1
                return n
            if vp(A)<min(vp(B),vp(C)):return []
        if all_divisible:return [(r,level)]
        assert level<e
        answer=[]
        for digit in range(p):answer.extend(recurse(r+digit*power,power*p,level+1))
        if len(answer)==p and all(lev==level+1 for _,lev in answer):
            expected={r+digit*power for digit in range(p)}
            if {v for v,_ in answer}==expected:return [(r,level)]
        return answer
    roots=recurse(0,1,0)
    # Every returned ball satisfies the congruences for all its integers.
    for r,level in roots:
        step=p**level
        for k in (r,r+step,r+2*step):
            assert all((a+b*k+c*k*k)%modulus==0 for a,b,c in F)
    return dict(exponent=e,root_cosets=[dict(residue=str(r),modulus_exponent=level) for r,level in roots],tree_visits=visits)


def main():
    sources,r,F=setup();certs=[constant_certificate(F,d) for d in (2,3,4,5)]
    certificate=certs[-1];factors=factor_small(int(certificate['constant']))
    fd=math.gcd(*(a+b*k+c*k*k for a,b,c in F for k in (0,1,2)))
    assert fd in (1,2)
    local=[];combinations=1
    for p,e in factors.items():
        levels=[root_balls(F,p,k) for k in range(1,e+1)]
        options=1+sum(len(l['root_cosets']) for l in levels)
        combinations*=options
        local.append(dict(p=p,max_exponent=e,levels=levels,local_options=options))
        print('prime',p,'bound',e,'root counts',[len(l['root_cosets']) for l in levels],flush=True)
    out=dict(status='all_integer_coset_content_classes_passed',input_sha256={n:hashlib.sha256(v).hexdigest() for n,v in sources.items()},
             selected_powers=r['powers'],x=r['x'],coset_start=r['coset_start'],coset_step=r['coset_step'],
             all_parameter_content=r['all_parameter_content'],normalized_coefficient_rows=F,
             fixed_divisor=fd,constant_certificates=certs,constant_factorization={str(p):e for p,e in factors.items()},
             local_classes=local,total_crt_classes=combinations,
             scope='All integer parameters in one fixed-x saved y coset; not all x,y and not an asymptotic result.')
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print('CRT classes',combinations,flush=True)


if __name__=='__main__':main()
