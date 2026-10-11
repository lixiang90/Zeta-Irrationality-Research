"""Exact parametric transportation for two fixed D12 log arrays.

Only k=2 and k=3 occur.  Integral bounded dual potentials enumerate the
complete optimum, with exact endpoint primal flows on every retained piece.
No frozen producer is imported, read or executed.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from collections import deque
from pathlib import Path
import json

REGIONS=[(Q(0),Q(1,3),[(Q(0),Q(1))]*3+[(Q(1),Q(-3))]),
         (Q(1,3),Q(1,2),[(Q(0),Q(1)),(Q(0),Q(1)),(Q(1),Q(-2)),(Q(0),Q(0))]),
         (Q(1,2),Q(1),[(Q(0),Q(1)),(Q(1),Q(-1)),(Q(0),Q(0)),(Q(0),Q(0))])]
CHECKS=[]

def ck(name, actual, expected=True):
    CHECKS.append({"name":name,"passed":actual==expected,
                   "actual":str(actual),"expected":str(expected)})
    if actual != expected:
        raise AssertionError(name)

def duals(cost, rows, col_affine):
    answer=[]
    for tail in combinations_with_replacement(range(4),3):
        v=(0,)+tail
        u=tuple(max(cost[i][j]-v[j] for j in range(4)) for i in range(len(rows)))
        A=sum(rows[i]*u[i] for i in range(len(rows)))+sum(col_affine[j][0]*v[j] for j in range(4))
        B=sum(col_affine[j][1]*v[j] for j in range(4))
        answer.append({"u":u,"v":v,"A":A,"B":B})
    return answer

def primal(rows, cols, cost, u, v):
    # Deterministic exact maxflow on complementary-slack edges.
    r=len(rows); source=0; sink=r+5; n=sink+1
    cap=[[Q(0) for _ in range(n)] for _ in range(n)]
    original=[[Q(0) for _ in range(n)] for _ in range(n)]
    def edge(i,j,value):
        cap[i][j]=value; original[i][j]=value
    for i in range(r): edge(source,1+i,rows[i])
    for j in range(4): edge(r+1+j,sink,cols[j])
    for i in range(r):
        for j in range(4):
            if u[i]+v[j]==cost[i][j]: edge(1+i,r+1+j,Q(1))
    total=Q(0)
    while True:
        parent=[None]*n; parent[source]=source; queue=deque([source])
        while queue and parent[sink] is None:
            at=queue.popleft()
            for nxt in range(n):
                if parent[nxt] is None and cap[at][nxt]>0:
                    parent[nxt]=at; queue.append(nxt)
        if parent[sink] is None: break
        amount=Q(1); at=sink
        while at!=source:
            prev=parent[at]; amount=min(amount,cap[prev][at]); at=prev
        at=sink
        while at!=source:
            prev=parent[at]; cap[prev][at]-=amount; cap[at][prev]+=amount; at=prev
        total+=amount
    flow=[[original[1+i][r+1+j]-cap[1+i][r+1+j] for j in range(4)] for i in range(r)]
    return total,flow

def solve(label, counts, cost, expected_upper):
    m=sum(counts); rows=[Q(a,m) for a in counts]; pieces=[]
    for reg,(lo,hi,col_affine) in enumerate(REGIONS):
        candidates=duals(cost,rows,col_affine)
        points={lo,hi}
        for a in candidates:
            for b in candidates:
                if a["B"]!=b["B"]:
                    x=(b["A"]-a["A"])/(a["B"]-b["B"])
                    if lo<x<hi: points.add(x)
        points=sorted(points); selected=[]
        for left,right in zip(points,points[1:]):
            mid=(left+right)/2
            best=min(candidates,key=lambda z:(z["A"]+z["B"]*mid,z["v"]))
            if selected and selected[-1]["right"]==left and selected[-1]["dual"]==best:
                selected[-1]["right"]=right
            else:
                selected.append({"left":left,"right":right,"dual":best})
        for p in selected:
            left,right,best=p["left"],p["right"],p["dual"]
            endpoint_flows=[]
            for which,x in [("left",left),("right",right)]:
                cols=[A+B*x for A,B in col_affine]
                target=best["A"]+best["B"]*x
                ck(f"{label} r{reg} x{x} dual all inequalities",all(best["u"][i]+best["v"][j]>=cost[i][j] for i in range(len(rows)) for j in range(4)))
                ck(f"{label} r{reg} x{x} dual lower envelope",target,min(z["A"]+z["B"]*x for z in candidates))
                total,flow=primal(rows,cols,cost,best["u"],best["v"])
                ck(f"{label} r{reg} x{x} feasible flow",total,Q(1))
                ck(f"{label} r{reg} x{x} rows",[sum(a) for a in flow],rows)
                ck(f"{label} r{reg} x{x} columns",[sum(flow[i][j] for i in range(len(rows))) for j in range(4)],cols)
                ck(f"{label} r{reg} x{x} nonnegative",all(a>=0 for row in flow for a in row))
                ck(f"{label} r{reg} x{x} primal dual equality",sum(flow[i][j]*cost[i][j] for i in range(len(rows)) for j in range(4)),target)
                endpoint_flows.append(flow)
            pieces.append({"region":reg,"left":left,"right":right,
                           "A":best["A"],"B":best["B"],"row_potential":best["u"],
                           "column_potential":best["v"],"left_flow":endpoint_flows[0],
                           "right_flow":endpoint_flows[1]})
    tau=2*sum(p["A"]*(p["right"]-p["left"])+p["B"]*(p["right"]**2-p["left"]**2)/2 for p in pieces)
    ck(label+" at most certified column upper",tau<=expected_upper)
    return {"m":m,"counts":counts,"cost_matrix":cost,"exact_tau":tau,
            "column_upper":expected_upper,"jensen_threshold":Q(m,m-1)*tau,"pieces":pieces}

cases={
 "k2":solve("k2",[1,3,6,3],[[0,0,0,0],[0,1,1,1],[0,1,2,2],[0,3,3,3]],Q(366,169)),
 "k3":solve("k3",[1,3,6,10,3],[[0,0,0,0],[0,1,1,1],[0,1,2,2],[0,1,2,3],[0,3,3,3]],Q(1146,529))}

def serial(value):
    if isinstance(value,Q): return str(value)
    if isinstance(value,(list,tuple)): return [serial(x) for x in value]
    if isinstance(value,dict): return {k:serial(v) for k,v in value.items()}
    return value

payload={"scope":"Two fixed exact parametric LPs; per-threshold couplings, endpoint primal/dual interpolation.",
         "checks":CHECKS,"passed_count":len(CHECKS),"all_passed":all(x["passed"] for x in CHECKS),"cases":cases}
Path(__file__).with_suffix(".json").write_text(json.dumps(serial(payload),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
for label,data in cases.items():
    print(label,"tau",data["exact_tau"],"Jensen",data["jensen_threshold"],"pieces",len(data["pieces"]))
    for p in data["pieces"]:
        print(" ",p["left"],p["right"],p["A"],p["B"],"dual",p["row_potential"],p["column_potential"])
print(f"{len(CHECKS)} fixed exact checks passed")
