"""Try to lift finite-window LP duals to full discrete positivity certificates."""
import json
from pathlib import Path
import sympy as S
from flint import fmpq, arb, ctx
from discrete_positive_cone_probe import shifted_map, generators, dot


def certificate(row,which):
    n,w=row['n'],row['w'];d=w+3
    M=shifted_map(n,w)
    edge=row[which];r=fmpq(edge['endpoint'])
    a,b=map(fmpq,edge['dual_auxiliary'])
    functional=[M[0][j]+a*M[1][j]+b*M[2][j]+r*M[3][j] for j in range(d+1)]
    gens=generators(n,d,'extreme_window')
    polys=[gens[j][0] for j in edge['support']]
    node=lambda k:(3*n+2+2*k)**2-(3*n+2)**2
    common=[k for k in range(13) if all(dot(p,[node(k)**j for j in range(d+1)])==0 for p in polys)]
    infinity=all(p[-1]==0 for p in polys)
    columns=[[node(k)**j for j in range(d+1)] for k in common]
    if infinity: columns.append([0]*d+[1])
    H=S.Matrix(d+1,len(columns),lambda i,j:columns[j][i])
    target=S.Matrix([S.Rational(str(x)) for x in functional])
    try:
        solution,params=H.gauss_jordan_solve(target)
    except ValueError:
        return dict(verified=False,reason='No supported positive-measure representation',common_nodes=common,infinity=infinity)
    assert params.rows==0
    assert H*solution==target
    good=all(x>=0 for x in solution)
    return dict(verified=good,common_nodes=common,infinity=infinity,weights=list(map(str,solution)))


def main():
    folder=Path(__file__).parent
    rows=json.loads((folder/'discrete_positive_full_window.json').read_text())['rows']
    results=[]
    for r in rows:
        lower=certificate(r,'lower');upper=certificate(r,'upper')
        results.append(dict(n=r['n'],w=r['w'],lower=lower,upper=upper))
        print(r['n'],r['w'],'global duals',lower['verified'],upper['verified'],
              'nodes',lower.get('common_nodes'),upper.get('common_nodes'),flush=True)
    (folder/'discrete_positive_global_certificate.json').write_text(json.dumps(dict(
        scope='A verified nonnegative moment representation certifies all integer nodes, not just the finite generator window.',
        rows=results),indent=2),encoding='utf-8')


if __name__=='__main__':main()
