"""Exact continuous transport certificates for fixed actual helper tableaux.

Rows use their own proven scales; positive columns need not be constant because
the theorem applied is CDT8.0.1. No n/prime or numerical-period scan is used.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json


def transport(x, rows, masses, max_rate):
    caps = [max(min((k+1)*x, F(1))-min(k*x, F(1)), F(0))
            for k in range(max_rate)]
    caps.append(max(F(1)-max_rate*x, F(0)))
    weights = [[sum(h <= k for h in row) for k in range(max_rate+1)] for row in rows]
    nr, nc = len(rows), len(caps)
    V = nr+nc+2
    src, sink = 0, V-1
    graph = [[] for _ in range(V)]

    def edge(a, b, cap, cost):
        i, j = len(graph[a]), len(graph[b])
        graph[a].append([b, j, cap, cost])
        graph[b].append([a, i, F(0), -cost])
        return a, i, cap

    for i, a in enumerate(masses):
        edge(src, 1+i, a, 0)
    for j, a in enumerate(caps):
        edge(1+nr+j, sink, a, 0)
    pairs = [[edge(1+i, 1+nr+j, F(1), -weights[i][j]) for j in range(nc)]
             for i in range(nr)]
    sent, cost = F(0), F(0)
    while sent < 1:
        dist, previous = [None]*V, [None]*V
        dist[src] = 0
        for _ in range(V-1):
            changed = False
            for a in range(V):
                if dist[a] is None:
                    continue
                for i, (b, rev, cap, value) in enumerate(graph[a]):
                    if cap and (dist[b] is None or dist[b] > dist[a]+value):
                        dist[b] = dist[a]+value
                        previous[b] = a, i
                        changed = True
            if not changed:
                break
        assert dist[sink] is not None
        amount, b = 1-sent, sink
        while b != src:
            a, i = previous[b]
            amount = min(amount, graph[a][i][2])
            b = a
        b = sink
        while b != src:
            a, i = previous[b]
            e = graph[a][i]
            e[2] -= amount
            graph[b][e[1]][2] += amount
            b = a
        sent += amount
        cost += amount*dist[sink]
    flows = [[initial-graph[a][i][2] for a, i, initial in row] for row in pairs]
    potential = [0]*V
    for iteration in range(V):
        changed = False
        for a in range(V):
            for b, rev, cap, value in graph[a]:
                if cap and potential[b] > potential[a]+value:
                    potential[b] = potential[a]+value
                    changed = True
        if not changed:
            break
        assert iteration < V-1
    alpha = [potential[1+i] for i in range(nr)]
    beta = [-potential[1+nr+j] for j in range(nc)]
    assert all(alpha[i]+beta[j] >= weights[i][j] for i in range(nr) for j in range(nc))
    assert all(sum(flows[i]) == masses[i] for i in range(nr))
    assert all(sum(flows[i][j] for i in range(nr)) == caps[j] for j in range(nc))
    dual = sum(masses[i]*alpha[i] for i in range(nr))+sum(caps[j]*beta[j] for j in range(nc))
    assert dual == -cost
    return -cost, alpha, beta, flows, caps


fixed_cases = [
    ("actual_K2_no_inflation_K_rank8", 3, 3, []),
    ("actual_K2_no_inflation_Q_rank11", 3, 6, []),
    ("actual_T4_K_rank9", 4, 3, []),
    ("actual_T4_Q_rank12", 4, 6, []),
    ("actual_T5_K_rank10", 5, 3, []),
    ("actual_T4_and_K2L_K_rank10", 4, 3, [[1, 1, 2]]),
]
certificates = []
for name, R, q, additional in fixed_cases:
    rows = [[]]+[list(range(1, j+1)) for j in range(1, R+1)]+[[1, 1]]+additional+[[1, 1, 1]]
    background = len(rows)-1
    m = background+q
    masses = [F(1, m)]*background+[F(q, m)]
    points = {F(0), F(1)}
    points.update(F(k, m*d) for d in range(1, R+1) for k in range(m*d+1))
    points = sorted(points)
    total, intervals = F(0), []
    for lo, hi in zip(points, points[1:]):
        value, alpha, beta, flow, caps = transport((lo+hi)/2, rows, masses, R)
        endpoints = []
        end_values = []
        for x in (lo, hi):
            v, aa, bb, ff, cc = transport(x, rows, masses, R)
            common_dual = sum(masses[i]*alpha[i] for i in range(len(rows)))+sum(
                cc[j]*beta[j] for j in range(R+1))
            assert v == common_dual, (name, lo, hi, x, v, common_dual)
            end_values.append(v)
            endpoints.append({"x":str(x), "value":str(v), "capacities":[str(a) for a in cc],
                              "flows":[[str(a) for a in line] for line in ff]})
        total += (hi-lo)*sum(end_values)
        intervals.append({"interval":[str(lo),str(hi)],
                          "common_dual_alpha":alpha, "common_dual_beta":beta,
                          "endpoints":endpoints})
    sigma_rows = [sum((F(1, h) for h in row), F(0)) for row in rows[:-1]]+[F(3)]*q
    naive = sum(F(2*i+1)*v for i, v in enumerate(sorted(sigma_rows)))/m**2
    assert naive <= total
    certificate = {
        "case":name, "log_degree":R, "target_rows":q, "actual_total_rank":m,
        "threshold_integer_rates":rows,
        "matrix_scales_by_species":[[str(F(1,h)) for h in row] for row in rows],
        "species_group_masses":[str(a) for a in masses],
        "tau_double":str(total), "comonotone_lower_bound":str(naive),
        "plain_Jensen_rho_necessary":str(F(m,m-1)*total),
        "all_e_zero":True, "full_interval_primal_dual_certificates":intervals,
    }
    certificates.append(certificate)

expected = ["167/64", "340/121", "2597/972", "4937/1728", "1369/500", "1087/400"]
assert [a["tau_double"] for a in certificates] == expected
assert all(F(a["plain_Jensen_rho_necessary"]) > F(29, 10) for a in certificates)
# Exact values are checked by endpoint primal/dual certificates above. This
# printed preview is not used to choose backgrounds or infer irrationality.
here = Path(__file__).resolve().parent
report = here/"cdt_odd_level20_arithmetic_20261006.md"
out = {
    "status":"exact_actual_helper_transport_intervals_passed",
    "report_sha256":hashlib.sha256(report.read_bytes()).hexdigest(),
    "scope":"All fixed cases have exact common-dual certificates on the full x interval.",
    "certificates":certificates,
    "not_claimed":["global optimization over all helpers/gauges/types",
                   "a new numerical irrationality theorem"],
}
(here/"cdt_odd_level20_transport_actual_20261006_verify.json").write_text(
    json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
print(json.dumps({"status":out["status"],"cases":[
    {"case":a["case"],"rank":a["actual_total_rank"],"tau":a["tau_double"],
     "naive_lower":a["comonotone_lower_bound"],"plain_Jensen_rho_necessary":a["plain_Jensen_rho_necessary"]}
    for a in certificates]}))

