"""Independent exact determinant comparisons and rigorous value enclosures."""
import json,time
from pathlib import Path
from flint import fmpq_poly,fmpq,arb,ctx
from joint_exact import entries,determinant,determinant_tail_split,determinant_interpolation,evaluate_primitive_ball,experiment

if __name__=='__main__':
    start=time.time();rows=[];folder=Path(__file__).parent
    for K,profile,h in [(8,[(1,2),(2,3)],8),(12,[(1,3),(2,3)],12),
                        (12,[(1,8)],15),(16,[(1,2),(2,4)],12)]:
        aa,bb=entries(K,profile,h)
        assert determinant(aa,bb,h)==determinant_interpolation(aa,bb,h)
        assert determinant_tail_split(aa,bb,K,max(n for n,b in profile),h)==determinant_interpolation(aa,bb,h)
    for file in sorted(folder.glob('joint_cache_K*_N*.json')):
        data=json.loads(file.read_text());r=data['result'];K=r['K']
        P=fmpq_poly([fmpq(c) for c in data['poly']]);ct,lv,bits=evaluate_primitive_ball(P)
        assert str(ct)==data['content']
        with ctx.workprec(160):
            score=lv/(K*K)
            assert score>0
            assert abs(float(score.mid())-r['score'])<1e-12
            row=dict(source=file.name,score_ball=score.str(30),precision_bits=bits)
        rows.append(row);print(json.dumps(row),flush=True)
    for K in [24,48,72]:
        m=K//24
        r,*_=experiment(K,[(m,3),(2*m,3)],K)
        rows.append(r);print(json.dumps(r)+f' elapsed={time.time()-start:.1f}',flush=True)
    (folder/'joint_validation.json').write_text(json.dumps(rows,indent=2))
