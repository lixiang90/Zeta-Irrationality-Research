"""Exact bounded two-dimensional positive fibers of the six-column map."""
import json
from fractions import Fraction as F
from pathlib import Path


def cross(o,a,b):return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])


def polygon(base,K):
    vertices=set()
    for i in range(6):
        for j in range(i+1,6):
            a,b=K[i];c,d=K[j];det=a*d-b*c
            if not det:continue
            x=F(-base[i]*d+b*base[j],det);y=F(-a*base[j]+base[i]*c,det)
            if all(base[k]+K[k][0]*x+K[k][1]*y>=0 for k in range(6)):vertices.add((x,y))
    vertices=sorted(vertices);assert len(vertices)>=3
    lower=[];upper=[]
    for p in vertices:
        while len(lower)>=2 and cross(lower[-2],lower[-1],p)<=0:lower.pop()
        lower.append(p)
    for p in reversed(vertices):
        while len(upper)>=2 and cross(upper[-2],upper[-1],p)<=0:upper.pop()
        upper.append(p)
    hull=lower[:-1]+upper[:-1]
    area=sum(a[0]*b[1]-a[1]*b[0] for a,b in zip(hull,hull[1:]+hull[:1]))/2
    assert area>0
    return hull,area


def main():
    folder=Path(__file__).parent
    modules=json.loads((folder/'joint_positive_module.json').read_text())['rows'];rows=[]
    for row in modules:
        base=list(map(int,row['fixed_output_family']['base']));K=row['saturated_output_kernel']
        vertices,area=polygon(base,K)
        rows.append(dict(n=row['n'],w=row['w'],vertices=[[str(x),str(y)] for x,y in vertices],
            area=str(area),vertex_count=len(vertices)))
        print(row['n'],row['w'],'positive fiber vertices',len(vertices),flush=True)
    (folder/'joint_positive_fiber.json').write_text(json.dumps(dict(
        scope='For fixed target C*base, nonnegative integer lifts of m times the target are integer points in m times this rational polygon.',
        rows=rows),indent=2),encoding='utf-8')


if __name__=='__main__':main()
