# b=8 三段表 Lean 文件生成器（镜像 mo271 gen_lean_inner.py / gen_inner_sum.py / gen_lean_outer.py）
# 数据源：research/b8_tables.json（b8_tablegen.py 精确管道产出，已校准）
# 产出：Zeta7Formal/Zeta7/Growth/{InnerTable,InnerSum,OuterTable}.lean
# b=8 平移点（相对 mo271 生成器）：
#   * inner 可采性断言 -2q-6 -> -2q-8（新 kloI，Norm.lean 第 131 行）；
#   * inner_table_k 陈述 -6 -> -8；
#   * OuterTable 的 max 项 13/10 -> 29/20；
#   * namespace Apery -> Zeta7，import 路径 Zeta7.Growth.*。
import json, math, os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FORMAL = os.path.join(ROOT, 'Zeta7Formal', 'Zeta7', 'Growth')

# ccount / cvLo / cvHi / psiR / bcoef / Jc_fast（mo271 table.py 前缀，b-无关）
exec(open(os.path.join(ROOT, 'Zeta5-mo271', 'scripts', 'growth', 'table.py'))
     .read().split('def Ein')[0])

d = json.load(open(os.path.join(HERE, 'b8_tables.json')))
P_IN = d['b8_inner']['pieces']    # [x0, x1, k, a, b]
P_OUT = d['b8_outer']['pieces']   # [x0, x1, a, b]
al = Fr(3, 40)

def lit(r):
    r = Fr(r)
    if r.denominator == 1:
        return f"({r.numerator} : ℝ)" if r >= 0 else f"(({r.numerator}) : ℝ)"
    return f"(({r.numerator}) / {r.denominator} : ℝ)"

def q_lit(r):
    r = Fr(r)
    return f"({r.numerator})" if r.denominator == 1 else f"({r.numerator}/{r.denominator})"

def lin_of(fn, x0, x1):
    xa = x0 + (x1 - x0) / 3
    xb = x0 + 2 * (x1 - x0) / 3
    ya, yb = fn(xa), fn(xb)
    a = (yb - ya) / (xb - xa)
    b = ya - a * xa
    return a, b

def linexpr(a, b):
    return f"({lit(a)} * x + {lit(b)})"

CC = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

HEADER = [
    "import Mathlib",
]

OPTS = [
    "set_option linter.unusedSimpArgs false",
    "set_option linter.unusedTactic false",
]

def cc_lemmas(q, qq, x0, x1):
    L = []
    L.append(f"  have hf0 : (0 : ℝ) ≤ x - (({q} : ℕ) : ℝ) := by norm_num; linarith")
    L.append(f"  have hf1 : x - (({q} : ℕ) : ℝ) < 1 := by norm_num; linarith")
    L.append(f"  have hg0 : (0 : ℝ) ≤ 3 / 40 * x - (({qq} : ℕ) : ℝ) := by norm_num; linarith")
    L.append(f"  have hg1 : 3 / 40 * x - (({qq} : ℕ) : ℝ) < 1 := by norm_num; linarith")
    for (i, j) in CC:
        fn = lambda x, i=i, j=j: ccount(x - q, al * x - qq, i, j)
        ca, cb = lin_of(fn, x0, x1)
        L.append(f"  have e{i}{j} : ccount (x - (({q} : ℕ) : ℝ)) (3 / 40 * x - (({qq} : ℕ) : ℝ)) {i} {j} = {linexpr(ca,cb)} := by")
        L.append(f"    rw [cc{i}{j} hf0 hf1 hg0 hg1]; (try simp only [min_def, max_def]); (try split_ifs) <;> (push_cast at *; linarith)")
    return L

# ---------------- InnerTable.lean ----------------
def inner_piece(idx, x0, x1, k, a, b):
    x0, x1, a, b = Fr(x0), Fr(x1), Fr(a), Fr(b)
    k = int(k)
    q = math.floor(x0)
    qq = math.floor(al * x0)
    mu = math.floor(Fr(37, 20) * x0)
    assert -2 * q - 8 <= k <= 8 * q + 20, (idx, x0, q, k)
    L = []
    L.append(f"theorem inPiece_{idx} (x : ℝ) (h1 : {lit(x0)} ≤ x) (h2 : x < {lit(x1)}) :")
    L.append(f"    Ein x ({k}) = {lit(a)} * x + {lit(b)} := by")
    L.append(f"  rw [Ein_expand ({k}) (q := {q}) (q' := {qq}) (μ := {mu}) (by norm_num; linarith) (by norm_num; linarith)")
    L.append(f"    (by norm_num; linarith) (by norm_num; linarith) (by norm_num; linarith) (by norm_num; linarith) (by linarith)]")
    L += cc_lemmas(q, qq, x0, x1)
    L.append("  simp only [Fin.sum_univ_three]")
    L.append("  rw [e00, e01, e02, e10, e11, e12, e20, e21, e22]")
    L.append("  simp only [bIn, bcoef, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,")
    L.append("    Matrix.head_cons, Matrix.tail_cons, psiR_eq, lrow, toNat_cast_q]")
    L.append("  push_cast")
    L.append("  norm_num")
    L.append("  ring")
    return "\n".join(L)

out = HEADER + ["import Zeta7.Growth.TableGen", ""] + OPTS + ["",
    "/-! 由 `gen_lean_b8.py` 生成：`Ê_in` 在 `[3, 20]` 上的分段（b=8，131 段）。 -/", "",
    "namespace Zeta7", ""]
for idx, (x0, x1, k, a, b) in enumerate(P_IN):
    out.append(inner_piece(idx, x0, x1, k, a, b))
    out.append("")
out.append("end Zeta7")
open(os.path.join(FORMAL, 'InnerTable.lean'), 'w', encoding='utf-8').write("\n".join(out))
print("InnerTable:", len(P_IN), "pieces")

# ---------------- InnerSum.lean ----------------
ts = [p[0] for p in P_IN] + [P_IN[-1][1]]
out = HEADER + ["import Zeta7.Growth.InnerTable", ""] + OPTS + ["set_option maxHeartbeats 4000000", "",
    "/-! 由 `gen_lean_b8.py` 生成：`Ê_in` 在 `[3, 20]` 上的表（b=8）。可采性界用新 kloI：`-2q-8`。 -/", "",
    "namespace Zeta7", ""]
out.append("def tInL : List ℚ := [" + ", ".join(q_lit(t) for t in ts) + "]")
out.append("def kInL : List ℤ := [" + ", ".join(str(p[2]) for p in P_IN) + "]")
out.append("def aInL : List ℚ := [" + ", ".join(q_lit(p[3]) for p in P_IN) + "]")
out.append("def bInL : List ℚ := [" + ", ".join(q_lit(p[4]) for p in P_IN) + "]")
out.append("")
out.append("noncomputable def tIn (i : ℕ) : ℝ := ((tInL.getD i 0 : ℚ) : ℝ)")
out.append("def kIn (i : ℕ) : ℤ := kInL.getD i 0")
out.append("noncomputable def gIn (i : ℕ) (x : ℝ) : ℝ := ((aInL.getD i 0 : ℚ) : ℝ) * x + ((bInL.getD i 0 : ℚ) : ℝ)")
out.append("")
out.append(f"theorem tIn_mono : ∀ i < {len(P_IN)}, tIn i < tIn (i + 1) := by")
out.append("  intro i hi")
out.append("  interval_cases i <;> simp only [tIn, tInL, List.getD_cons_succ, List.getD_cons_zero] <;> norm_num")
out.append("")
out.append(f"theorem inner_table : ∀ i < {len(P_IN)}, ∀ x ∈ Set.Ico (tIn i) (tIn (i + 1)), Ein x (kIn i) = gIn i x := by")
out.append("  intro i hi x hx")
out.append("  interval_cases i")
for idx in range(len(P_IN)):
    out.append(f"  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢")
    out.append(f"    push_cast at hx ⊢")
    out.append(f"    have := inPiece_{idx} x (by linarith [hx.1]) (by linarith [hx.2])")
    out.append(f"    linarith")
out.append("")
out.append(f"theorem inner_table_k : ∀ i < {len(P_IN)}, ∀ x ∈ Set.Ico (tIn i) (tIn (i + 1)),")
out.append("    -2 * (⌊x⌋₊ : ℤ) - 8 ≤ kIn i ∧ kIn i ≤ 8 * (⌊x⌋₊ : ℤ) + 20 := by")
out.append("  intro i hi x hx")
out.append("  interval_cases i")
for idx, (x0, x1, k, a, b) in enumerate(P_IN):
    q = math.floor(Fr(x0))
    assert -2 * q - 8 <= int(k) <= 8 * q + 20
    out.append(f"  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢")
    out.append(f"    push_cast at hx")
    out.append(f"    rw [nat_floor_of_bounds (q := {q}) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]")
    out.append(f"    norm_num")
out.append("")
out.append("end Zeta7")
open(os.path.join(FORMAL, 'InnerSum.lean'), 'w', encoding='utf-8').write("\n".join(out))
print("InnerSum written")

# ---------------- OuterTable.lean ----------------
def outer_piece(idx, x0, x1, a, b):
    x0, x1, a, b = Fr(x0), Fr(x1), Fr(a), Fr(b)
    q = math.floor(x0)
    qq = math.floor(al * x0)
    mu = math.floor(Fr(37, 20) * x0)
    L = []
    L.append(f"theorem outPiece_{idx} (x : ℝ) (h1 : {lit(x0)} ≤ x) (h2 : x < {lit(x1)}) :")
    L.append(f"    Eout x = {lit(a)} * x + {lit(b)} := by")
    L.append(f"  rw [Eout_expand (q := {q}) (q' := {qq}) (μ := {mu}) (by norm_num; linarith) (by norm_num; linarith)")
    L.append(f"    (by norm_num; linarith) (by norm_num; linarith) (by norm_num; linarith) (by norm_num; linarith) (by linarith)]")
    L += cc_lemmas(q, qq, x0, x1)
    fn = lambda x: max(Fr(0), Fr(29, 20) * x - 2)
    ca, cb = lin_of(fn, x0, x1)
    L.append(f"  have em : max 0 (29 / 20 * x - 2) = {linexpr(ca,cb)} := by")
    L.append(f"    (try simp only [max_def]); (try split_ifs) <;> linarith")
    L.append("  simp only [Fin.sum_univ_three]")
    L.append("  rw [e00, e01, e02, e10, e11, e12, e20, e21, e22, em]")
    L.append("  simp only [bGO, bcoef, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,")
    L.append("    Matrix.head_cons, Matrix.tail_cons, GO, Finset.sum_range_succ, Finset.sum_range_zero]")
    L.append("  norm_num")
    L.append("  ring_nf")
    return "\n".join(L)

out = HEADER + ["import Zeta7.Growth.TableGen", ""] + OPTS + ["set_option maxHeartbeats 4000000", "",
    "/-! 由 `gen_lean_b8.py` 生成：`Ê_out` 在 `[20/37, 3]` 上的表（b=8，14 段）。 -/", "",
    "namespace Zeta7", ""]
for idx, (x0, x1, a, b) in enumerate(P_OUT):
    out.append(outer_piece(idx, x0, x1, a, b))
    out.append("")
ts = [p[0] for p in P_OUT] + [P_OUT[-1][1]]
out.append("def tOutL : List ℚ := [" + ", ".join(q_lit(t) for t in ts) + "]")
out.append("def aOutL : List ℚ := [" + ", ".join(q_lit(p[2]) for p in P_OUT) + "]")
out.append("def bOutL : List ℚ := [" + ", ".join(q_lit(p[3]) for p in P_OUT) + "]")
out.append("noncomputable def tOut (i : ℕ) : ℝ := ((tOutL.getD i 0 : ℚ) : ℝ)")
out.append("noncomputable def gOut (i : ℕ) (x : ℝ) : ℝ := ((aOutL.getD i 0 : ℚ) : ℝ) * x + ((bOutL.getD i 0 : ℚ) : ℝ)")
out.append("")
out.append(f"theorem tOut_mono : ∀ i < {len(P_OUT)}, tOut i < tOut (i + 1) := by")
out.append("  intro i hi")
out.append("  interval_cases i <;> simp only [tOut, tOutL, List.getD_cons_succ, List.getD_cons_zero] <;> norm_num")
out.append("")
out.append(f"theorem outer_table : ∀ i < {len(P_OUT)}, ∀ x ∈ Set.Ico (tOut i) (tOut (i + 1)), Eout x = gOut i x := by")
out.append("  intro i hi x hx")
out.append("  interval_cases i")
for idx in range(len(P_OUT)):
    out.append(f"  · simp only [tOut, tOutL, gOut, aOutL, bOutL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢")
    out.append(f"    push_cast at hx ⊢")
    out.append(f"    have := outPiece_{idx} x (by linarith [hx.1]) (by linarith [hx.2])")
    out.append(f"    linarith")
out.append("")
out.append("end Zeta7")
open(os.path.join(FORMAL, 'OuterTable.lean'), 'w', encoding='utf-8').write("\n".join(out))
print("OuterTable:", len(P_OUT), "pieces")
