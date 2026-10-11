"""Independent Fraction/SymPy verification of joint-module certificates."""
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path
import sympy as S
from verify_discrete_positive_cone import independent_map, dot

sys.set_int_max_str_digits(0)


def q(x):return S.Rational(str(x))


def primitive_column(values):
    den=math.lcm(*(x.denominator for x in values))
    integers=[int(x*den) for x in values];g=math.gcd(*integers)
    return [x//g for x in integers],F(den,g)


def kernel_certificate(A,U,K):
    assert abs(U.det())==1 and A*K==S.zeros(A.rows,K.cols)
    rank=A.rank();H=U*A.T
    assert H[rank:,:]==S.zeros(A.cols-rank,A.rows)
    assert K==U[rank:,:].T


def verify_module(row,source):
    n,w=row['n'],row['w'];M=independent_map(n,w)
    cols=[];polys=[]
    for name in ('lower','upper'):
        H=list(map(F,source[name]['H']))
        for j in range(3):
            P=[F(0)]*j+H
            col,scale=primitive_column([dot(line,P) for line in M])
            cols.append(col);polys.append([q(scale*x) for x in P]+[S.Integer(0)]*(w+4-len(P)))
    C=S.Matrix.hstack(*(S.Matrix(col) for col in cols));assert C==S.Matrix(row['matrix'])
    P=S.Matrix.hstack(*(S.Matrix(col) for col in polys));assert P.rank()==row['polynomial_rank']
    U=S.Matrix(row['output_hnf_transform']);K=S.Matrix(row['saturated_output_kernel'])
    kernel_certificate(C,U,K)
    A=C[[1,2],:];V=S.Matrix(row['nuisance_hnf_transform']);L=S.Matrix(row['saturated_nuisance_kernel'])
    kernel_certificate(A,V,L)
    G=(C*L)[[0,3],:];assert G==S.Matrix(row['eliminated_target_map'])
    d1=math.gcd(*(int(x) for x in G))
    d2=math.gcd(*(int(G[:,list(ij)].det()) for ij in itertools.combinations(range(4),2)))
    smith=list(map(int,row['target_smith_invariants']));assert smith==[d1,d2//d1]
    rem=smith[-1]
    for p in range(2,8*n+1):
        while rem%p==0:rem//=p
    assert rem==int(row['target_largest_smith_rough_part'])
    target=S.Matrix([row['target_pair'][0],0,0,row['target_pair'][1]])
    x=S.Matrix(list(map(q,row['minimum_l1_lift'])));lam=S.Matrix([list(map(q,row['l1_dual']))])
    assert all(t>=0 for t in x) and C*x==target
    assert all(t<=1 for t in lam*C)
    assert sum(x)==q(row['minimum_l1_cost'])==(lam*target)[0]
    c=S.Matrix(list(map(int,row['integer_lift'])));content=int(row['integer_lift_output_content'])
    assert C*c==content*target and math.gcd(*(int(t) for t in c))==1
    old=S.Matrix(list(map(q,row['old_positive_lift'])));assert all(t>=0 for t in old) and C*old==target
    family=row['fixed_output_family'];base=S.Matrix(list(map(int,family['base'])));k=S.Matrix(list(map(int,family['kernel'])))
    D=int(family['base_output_multiplier']);assert all(x>0 for x in base)
    assert C*base==D*S.Matrix([-1,0,0,1]) and C*k==S.zeros(4,1)
    assert math.gcd(*(int(x) for x in k))==1
    for example in family['examples']:
        m=example['modulus'];v=m*base+k
        g=math.gcd(*(int(x) for x in v));assert math.gcd(g,m)==1
        c=S.Matrix(list(map(int,example['primitive_input'])));assert c==v/g
        assert all(x>0 for x in c) and math.gcd(*(int(x) for x in c))==1
        content=int(example['output_content']);assert content%m==0
        assert C*c==content*S.Matrix([-1,0,0,1])
    return C,L


def verify_congruence(row,module,source):
    C=S.Matrix(module['matrix']);L=S.Matrix(module['saturated_nuisance_kernel'])
    m=row['modulus'];G=S.Matrix(module['eliminated_target_map']);Z=S.Matrix(row['change_of_lattice_basis'])
    A=G.row_join(-m*S.eye(2));U=S.Matrix(row['augmented_hnf_transform'])
    assert abs(U.det())==1 and (U*A.T)[2:,:]==S.zeros(4,2)
    assert Z==(U[2:,:].T)[:4,:]
    expected=math.prod(m//math.gcd(m,int(s)) for s in module['target_smith_invariants'])
    assert abs(Z.det())==expected==int(row['index'])
    basis=(L*Z).T;T=S.Matrix(row['lll_transform']);B=S.Matrix(row['reduced_basis'])
    assert abs(T.det())==1 and B==T*basis
    outputs=(C*B.T).T
    assert all(x%m==0 for x in outputs) and outputs[:,[1,2]]==S.zeros(4,2)
    # Independent complete enumeration of the stated finite search box.
    B=[[int(x) for x in B.row(i)] for i in range(4)]
    outputs=[[int(x) for x in outputs.row(i)] for i in range(4)]
    lo=F(source['lower']['endpoint']);hi=F(source['upper']['endpoint'])
    count=0;zeros=0;best=None;directions=set();radius=row['radius']
    for z in itertools.product(range(-radius,radius+1),repeat=4):
        if not any(z) or next(x for x in z if x)<0:continue
        v=[sum(z[i]*B[i][j] for i in range(4)) for j in range(6)]
        out=[sum(z[i]*outputs[i][j] for i in range(4)) for j in range(4)]
        if not any(out):zeros+=1
        if all(x<=0 for x in v):v=[-x for x in v];out=[-x for x in out]
        if any(x<0 for x in v):continue
        count+=1;g=math.gcd(*out);assert g>0 and g%m==0
        a,b=out[0]//g,out[3]//g;directions.add((a,b))
        bound=max(a+b*lo,a+b*hi)
        if best is None or bound<best:best=bound
    assert count==row['positive_vectors'] and zeros==row['zero_output_vectors']
    assert len(directions)==row['distinct_primitive_outputs']
    assert (best is None and row['best'] is None) or best==F(row['best']['rational_upper'])


def verify_polygon(poly,module):
    vertices=[tuple(map(F,p)) for p in poly['vertices']]
    base=list(map(int,module['fixed_output_family']['base']));K=module['saturated_output_kernel']
    for v in vertices:
        assert all(base[i]+K[i][0]*v[0]+K[i][1]*v[1]>=0 for i in range(6))
        assert sum(base[i]+K[i][0]*v[0]+K[i][1]*v[1]==0 for i in range(6))>=2
    all_vertices=set()
    for i,j in itertools.combinations(range(6),2):
        A=S.Matrix([K[i],K[j]])
        if not A.det():continue
        v=A.inv()*S.Matrix([-base[i],-base[j]])
        if all(base[k]+K[k][0]*v[0]+K[k][1]*v[1]>=0 for k in range(6)):
            all_vertices.add(tuple(F(str(x)) for x in v))
    assert set(vertices)==all_vertices
    area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(vertices,vertices[1:]+vertices[:1]))/2
    assert area==F(poly['area']) and area>0


def main():
    folder=Path(__file__).parent
    sources=json.loads((folder/'growing_positive_moment.json').read_text())['rows']
    sources+=json.loads((folder/'growing_positive_ratio_scan.json').read_text())['rows']
    modules=json.loads((folder/'joint_positive_module.json').read_text())['rows']
    for row in modules:
        source=next(r for r in sources if (r['n'],r['w'])==(row['n'],row['w']))
        verify_module(row,source);print('Verified module',row['n'],row['w'],flush=True)
    congruences=json.loads((folder/'joint_positive_congruence_probe.json').read_text())['rows']
    for row in congruences:
        module=next(r for r in modules if (r['n'],r['w'])==(row['n'],row['w']))
        source=next(r for r in sources if (r['n'],r['w'])==(row['n'],row['w']))
        verify_congruence(row,module,source)
    fibers=json.loads((folder/'joint_positive_fiber.json').read_text())['rows']
    for row in fibers:
        module=next(r for r in modules if (r['n'],r['w'])==(row['n'],row['w']))
        verify_polygon(row,module)
    result=dict(scope='Independent direct-factor Fraction outputs, unimodular kernel certificates, exact LP duals, all bounded-search points and fiber vertices.',
        modules=len(modules),fixed_output_modulus_examples=4*len(modules),
        congruence_lattices=len(congruences),bounded_vectors_checked=sum(r['checked_up_to_sign'] for r in congruences),
        positive_fiber_polygons=len(fibers),all_checks_passed=True)
    (folder/'verify_joint_positive_module.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(result,flush=True)


if __name__=='__main__':main()
