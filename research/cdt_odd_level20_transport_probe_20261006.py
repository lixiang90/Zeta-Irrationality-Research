from fractions import Fraction as F
from collections import namedtuple
from pathlib import Path
import hashlib
import json

def transport(x,q):
    m=q+5
    masses=[F(1,m)]*5+[F(q,m)]
    caps=[x,min(2*x,F(1))-x,max(min(3*x,F(1))-min(2*x,F(1)),F(0)),max(F(1)-3*x,F(0))]
    ws=[[0,0,0,0],[0,1,1,1],[0,1,2,2],[0,1,2,3],[0,2,2,3],[0,3,3,3]]
    V=12; src=0; sink=11
    graph=[[] for _ in range(V)]
    def edge(a,b,cap,cost):
        i=len(graph[a]);j=len(graph[b])
        graph[a].append([b,j,cap,cost]);graph[b].append([a,i,F(0),-cost])
        return a,i,cap
    pairs=[]
    for i,a in enumerate(masses):edge(src,1+i,a,0)
    for j,a in enumerate(caps):edge(7+j,sink,a,0)
    for i in range(6):
        p=[]
        for j in range(4):p.append(edge(1+i,7+j,F(1),-ws[i][j]))
        pairs.append(p)
    sent=F(0);cost=F(0)
    while sent<1:
        dist=[None]*V;dist[src]=0;prev=[None]*V
        for _ in range(V-1):
            changed=False
            for a in range(V):
                if dist[a] is None:continue
                for i,e in enumerate(graph[a]):
                    b,rev,cap,c=e
                    if cap and (dist[b] is None or dist[b]>dist[a]+c):
                        dist[b]=dist[a]+c;prev[b]=(a,i);changed=True
            if not changed:break
        assert dist[sink] is not None
        amount=1-sent;b=sink
        while b!=src:
            a,i=prev[b];amount=min(amount,graph[a][i][2]);b=a
        b=sink
        while b!=src:
            a,i=prev[b];e=graph[a][i]
            e[2]-=amount;graph[b][e[1]][2]+=amount;b=a
        sent+=amount;cost+=amount*dist[sink]
    flow=[[initial-graph[a][i][2] for a,i,initial in p] for p in pairs]
    pot=[0]*V
    for k in range(V):
        changed=False
        for a in range(V):
            for b,rev,cap,c in graph[a]:
                if cap and pot[b]>pot[a]+c:pot[b]=pot[a]+c;changed=True
        if not changed:break
        assert k<V-1
    alpha=[pot[1+i] for i in range(6)]
    beta=[-pot[7+j] for j in range(4)]
    assert all(alpha[i]+beta[j]>=ws[i][j] for i in range(6) for j in range(4))
    assert sum(masses[i]*alpha[i] for i in range(6))+sum(caps[j]*beta[j] for j in range(4))==-cost
    assert all(sum(flow[i])==masses[i] for i in range(6))
    assert all(sum(flow[i][j] for i in range(6))==caps[j] for j in range(4))
    return -cost,alpha,beta,flow,caps,masses

certificates=[]
for q in (3,6):
    m=q+5
    pts={F(0),F(1),F(1,3),F(1,2)}
    pts.update(F(k,m*d) for d in (1,2,3) for k in range(m*d+1))
    pts=sorted(pts);total=F(0);segments=[]
    for lo,hi in zip(pts,pts[1:]):
        val,alpha,beta,flow,caps,masses=transport((lo+hi)/2,q)
        ends=[]; endpoint_flows=[]
        for t in (lo,hi):
            vv,aa,bb,ff,cc,mm=transport(t,q)
            dual=sum(mm[i]*alpha[i] for i in range(6))+sum(cc[j]*beta[j] for j in range(4))
            assert vv==dual,(q,lo,hi,t,vv,dual)
            ends.append(vv)
            endpoint_flows.append({
                "x":str(t),"value":str(vv),"capacities":[str(v) for v in cc],
                "flows":[[str(v) for v in line] for line in ff]})
        total+=(hi-lo)*(ends[0]+ends[1])
        segments.append({
            "interval":[str(lo),str(hi)],
            "common_dual_alpha":alpha,"common_dual_beta":beta,
            "endpoints":endpoint_flows})
    expected=F(257,96) if q==3 else F(1039,363)
    assert total==expected
    certificates.append({
        "target_rows":q,"actual_total_rank":m,
        "matrix":[["0","0","0"],["1","0","0"],["1","1/2","0"],
                  ["1","1/2","1/3"],["1","1","1/3"]]+[["1","1","1"]]*q,
        "species_group_masses":[str(F(1,m))]*5+[str(F(q,m))],
        "tau_double":str(total),"all_e_zero":True,
        "full_interval_primal_dual_certificates":segments})
here=Path(__file__).resolve().parent
report=here/"cdt_odd_level20_arithmetic_20261006.md"
out={
    "status":"exact_transport_all_intervals_passed",
    "report_sha256":hashlib.sha256(report.read_bytes()).hexdigest(),
    "definition":"CDT fixed v2 Theorem8.0.1 (8.0.2), balanced continuous transport",
    "scope":"Primal endpoint flows and one common feasible dual prove each entire interval.",
    "certificates":certificates,
    "not_claimed":["global optimum across other backgrounds or gauges",
                   "new numerical irrationality or capacity contradiction"]}
(here/"cdt_odd_level20_transport_20261006_verify.json").write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":out["status"],
    "fixed_tau_double":[{"rank":a["actual_total_rank"],"tau":a["tau_double"],
                        "segments":len(a["full_interval_primal_dual_certificates"])}
                       for a in certificates]}))

