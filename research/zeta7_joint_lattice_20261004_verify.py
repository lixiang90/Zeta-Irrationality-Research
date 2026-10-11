"""Independent checks of initial faces, successful Hensel fibers and resultants."""
import json,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from flint import fmpq as Q,fmpq_poly as Poly,fmpq_mat

sys.set_int_max_str_digits(0)


def val(q,p):
    if not q:return 10**9
    n,d=abs(int(q.numerator)),int(q.denominator);v=0
    while n%p==0:n//=p;v+=1
    while d%p==0:d//=p;v-=1
    return v


def main():
    folder=Path(__file__).parent;raw=(folder/'zeta7_two_moment_partial_20261004_coefficients.json').read_bytes()
    d=json.loads(raw);cs=[(r['i'],r['j'],Poly([Q(c) for c in r['polynomial_coefficients']])) for r in d['coefficients']]
    local=json.loads((folder/'zeta7_joint_lattice_20261004.json').read_text(encoding='utf-8'))
    face_checks=0
    for info in local['results']:
        p=info['p'];terms=info['coefficient_content_valuations']
        for face in info['faces']:
            a,b=F(face['witness']['a']),F(face['witness']['b'])
            weights=[F(t['v'])+t['i']*a+t['j']*b for t in terms]
            assert [[t['i'],t['j']] for t,w in zip(terms,weights) if w==min(weights)]==face['support']
            roots=[]
            for u in range(1,p):
                for v in range(1,p):
                    image=[0]*38
                    for term in face['initial_polynomials']:
                        scalar=pow(u,term['i'],p)*pow(v,term['j'],p)%p
                        for k,c in enumerate(term['X_coefficients']):image[k]=(image[k]+scalar*c)%p
                    if not any(image):roots.append([u,v])
            assert roots==face['unit_roots'];face_checks+=1
    fibers=json.loads((folder/'zeta7_joint_lattice_20261004_fibers.json').read_text(encoding='utf-8'))
    fiber_checks=0
    for info in fibers['results']:
        p=info['p'];v0=next(r['baseline_content_valuation'] for r in local['results'] if r['p']==p)
        for row in info['rows']:
            if row['protected'] is not True:continue
            x=Q(p**row['a']*row['x_unit'])
            for root in row['roots']:
                y=Q(p**row['b']*int(root))
                polynomial=sum((pol*x**i*y**j for i,j,pol in cs),Poly())
                assert min(val(c,p) for c in polynomial if c)>=v0
                fiber_checks+=1
    resultants=json.loads((folder/'zeta7_joint_lattice_20261004_resultants.json').read_text(encoding='utf-8'))
    resultant_checks=0
    for row in resultants['results']:
        k,l=row['X_coefficients'];RR=Poly([Q(c) for c in row['resultant_coefficients']])
        for x in [Q(-1),Q(0),Q(1,2)]:
            left=[sum((pol[k]*x**i for i,jj,pol in cs if jj==j and k<=pol.degree()),Q(0)) for j in range(3)]
            right=[sum((pol[l]*x**i for i,jj,pol in cs if jj==j and l<=pol.degree()),Q(0)) for j in range(3)]
            c,b,a=left;f,e,d=right
            syl=fmpq_mat([[a,b,c,0],[0,a,b,c],[d,e,f,0],[0,d,e,f]])
            assert syl.det()==RR(x);resultant_checks+=1
    out=dict(status='passed',source_coefficients_sha256=hashlib.sha256(raw).hexdigest(),
             initial_face_and_unit_root_checks=face_checks,exact_full_content_fiber_point_checks=fiber_checks,
             independent_sylvester_resultant_checks=resultant_checks,
             scope='Checks the saved faces and successful fibers exactly. Completeness of the face '
                   'enumeration follows from the separate interval argument; higher-unit absence '
                   'and global optimality are not asserted.')
    Path(__file__).with_name('zeta7_joint_lattice_20261004_verified.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(out,flush=True)


if __name__=='__main__':main()
