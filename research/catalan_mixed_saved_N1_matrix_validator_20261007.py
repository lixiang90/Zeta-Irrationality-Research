"""Independent read-only FLINT check of two saved N=1 JSON certificates.

This script never imports or executes either producer, and never rebuilds
Jacobi polynomials, moments, sections, or the original matrix entries.
Only the saved finite matrices and their recorded transformations are checked.
No output files are written.
"""
import hashlib
import json
from pathlib import Path

import flint
from flint import nmod_mat

HERE = Path(__file__).resolve().parent
FIRST = HERE / "cdt_mixed_actual_moment_pencil_N1_20261007.json"
SECOND = HERE / "cdt_mixed_N1_observability_20261007.json"


def read(path):
    raw = path.read_bytes()
    obj = json.loads(raw.decode("utf-8"))
    return obj, dict(path=str(path), bytes=len(raw),
                     sha256=hashlib.sha256(raw).hexdigest())


x, xr = read(FIRST)
y, yr = read(SECOND)
assert x["modulus"] == y["modulus"] == 101
assert x["N"] == y["N"] == 1
assert y["input_sha256"] == xr["sha256"]
assert not x["actual_relation_assumed"] and not x["periods_approximated"]
assert y["historical_producer_runs"] == 0
assert y["previous_producer_rerun"] is False
pmod = 101


def matrix(data, rows, cols):
    assert len(data) == rows and all(len(row) == cols for row in data)
    # FLINT's tolist() returns nmod scalars; normalize these computed values.
    assert all(z == int(z) for row in data for z in row)
    data = [[int(z) for z in row] for row in data]
    assert all(type(z) is int and 0 <= z < pmod for row in data for z in row)
    return nmod_mat(data, pmod)


def sub(mat, r0, r1, c0, c1):
    return nmod_mat([row[c0:c1] for row in mat.tolist()[r0:r1]], pmod)


def assert_equal(computed, saved, rows, cols):
    assert computed == matrix(saved, rows, cols)


E0, E1, CF = [matrix(x["matrices"][key], 44, 43)
              for key in ("E0", "E1", "CF")]
cr = x["component_ranks"]
assert (E0.rank(), E1.rank(), CF.rank()) == (cr["E0"], cr["E1"], cr["CF"])
C1 = sub(CF, 0, 35, 9, 43)
T0 = sub(E0, 35, 44, 0, 9)
T1 = sub(E0, 35, 44, 9, 43)
assert C1.rank() == cr["CF_residual"] == 34
assert (T0.rank(), int(T0.det())) == (
    cr["tail_first9"]["rank"], cr["tail_first9"]["determinant"])
assert sub(CF, 0, 35, 0, 9) == nmod_mat(35, 9, pmod)
assert sub(CF, 35, 44, 0, 43) == nmod_mat(9, 43, pmod)
assert sub(E1, 35, 44, 0, 43) == nmod_mat(9, 43, pmod)

# Inspect all saved row arrays for the claimed finite support and labels;
# do not regenerate their defining polynomials or moment entries.
assert len(x["rows"]) == 44
for index, row in enumerate(x["rows"]):
    for key in ("P", "D0", "D1"):
        vals = row[key]
        assert vals and len(vals) <= 65
        assert all(type(z) is int and 0 <= z < pmod for z in vals)
    if index < 35:
        assert row["kind"] == "Jacobi" and row["degree"] == index + 9
        assert all(z == 0 for z in row["P"][:19])
        assert all(z == 0 for key in ("D0", "D1") for z in row[key][:20])
    else:
        assert row["kind"] == "pure_D_tail" and row["tail"] == index - 35
        assert row["P"] == [0] and row["D1"] == [0]
        assert all(z == 0 for z in row["D0"][:54 + index - 35])

tests = []
assert [(z["mu"], z["gamma"]) for z in x["evaluations"]] == [
    (mu, gamma) for mu in (1, 2, -1) for gamma in (0, 1, -1)]
for entry in x["evaluations"]:
    mu, gamma = entry["mu"], entry["gamma"]
    value = E0 + E1 * mu + CF * gamma
    square = sub(value, 0, 43, 0, 43)
    rank, det = value.rank(), int(square.det())
    assert rank == entry["full_pool"]["rank"] == 43
    assert square.rank() == entry["selected_square"]["rank"] == 43
    assert det == entry["selected_square"]["determinant"]
    tests.append(dict(mu=mu, gamma=gamma, rank=rank, square_det=det))

# Recompute only exact linear-algebra transformations from saved E matrices.
Tinv = T0.inv()
W = Tinv * T1
S0 = sub(E0, 0, 35, 9, 43) - sub(E0, 0, 35, 0, 9) * W
S1 = sub(E1, 0, 35, 9, 43) - sub(E1, 0, 35, 0, 9) * W
for name, computed, nr, nc in (
    ("tail_inverse", Tinv, 9, 9), ("W", W, 9, 34),
    ("S0", S0, 35, 34), ("S1", S1, 35, 34), ("C1", C1, 35, 34)):
    assert_equal(computed, y[name], nr, nc)
chosen, extra = y["selected_C1_rows"], y["extra_row"]
assert chosen == list(range(34)) and extra == 34
Csel = matrix([C1.tolist()[i] for i in chosen], 34, 34)
Cinv = Csel.inv()
assert_equal(Cinv, y["C1_inverse"], 34, 34)
A = Cinv * matrix([S0.tolist()[i] for i in chosen], 34, 34)
B = Cinv * matrix([S1.tolist()[i] for i in chosen], 34, 34)
Cextra = matrix([C1.tolist()[extra]], 1, 34)
v = matrix([S0.tolist()[extra]], 1, 34) - Cextra * A
zero1 = matrix([S1.tolist()[extra]], 1, 34) - Cextra * B
can = y["canonical"]
assert_equal(A, can["A"], 34, 34)
assert_equal(B, can["B"], 34, 34)
assert_equal(v, [can["v"]], 1, 34)
assert_equal(zero1, [can["extra_S1"]], 1, 34)
assert zero1 == nmod_mat(1, 34, pmod) and v.rank() == 1
cyclic = []
assert [r["mu"] for r in y["records"]] == [1, 2, -1, 0]
for record in y["records"]:
    mu = record["mu"]
    J = A + B * mu
    assert_equal(J, record["matrix"], 34, 34)
    orbit, current = [], v
    for _ in range(34):
        orbit.append(current.tolist()[0])
        current = current * J
    O = matrix(orbit, 34, 34)
    assert_equal(O, record["observability_matrix"], 34, 34)
    rank, det = O.rank(), int(O.det())
    assert rank == record["gaussian"]["rank"] == 34
    assert det == record["gaussian"]["determinant"]
    cyclic.append(dict(mu=mu, rank=rank, cyclic_det=det))

print(json.dumps(dict(scope="saved N=1 matrices only; no producer rerun",
                     flint_version=flint.__version__, first=xr, second=yr,
                     first_keys=list(x), second_keys=list(y),
                     parameters=x["parameters"],
                     component_ranks={k: v for k, v in cr.items() if k != "tail_first9"},
                     tail_rank=T0.rank(), tail_det=int(T0.det()),
                     first_evaluations=tests,
                     selected_C1_rows=chosen, extra_row=extra,
                     S0_rank=S0.rank(), S1_rank=S1.rank(),
                     v_nonzero=True, extra_S1_zero=True, cyclic=cyclic),
                 ensure_ascii=False, indent=2))
