#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
b=8 位势不等式 Table7 证书发射器（镜像 mo271 scripts/gen_table2.py）。

输入：research/table7_final.txt（Table 7）、research/partition7.json（认证分区）。
输出：Zeta7Formal/Zeta7/Table7/{Data,U*,I*,All}.lean —— 最终定理
  `potential_ineq_le_two : ∀ t : ℝ, 0 < t → t ≤ 2 → 2 * Uρ8 t - Vfield8 t ≤ M0_8`。

适配点（相对 b=6 版）：系数 6→8、12→16、α=1/40、qm8=7/5000、qp8=9/6250、
M0_8 = -6.4；模板引理内联于 Table7/Data.lean（Apery 同名文件是死代码）。
"""
from fractions import Fraction as Fr
import math, json, os, sys

sys.set_int_max_str_digits(10**7)
AL = Fr(1, 40)
QM8, QP8 = Fr(7, 5000), Fr(9, 6250)
M0 = Fr(-127, 20)   # -6.35
WORST = [Fr(-10**9), None]
OUT = 'Zeta7Formal/Zeta7/Table7'
os.makedirs(OUT, exist_ok=True)

TABLE = []
for line in open('research/table7_final.txt', encoding='utf-8'):
    line = line.strip().rstrip(',')
    if line.startswith('('):
        x, y, z = (int(v) for v in line.strip('()').split(','))
        TABLE.append((Fr(x, 10**12), Fr(y, 10**12), Fr(z, 10**12)))
A = [t[0] for t in TABLE]; B = [t[1] for t in TABLE]; C = [t[2] for t in TABLE]
N16 = sum(C)
assert N16 == Fr(39, 40), N16

def lean(q):
    if q.denominator == 1:
        return f"({q.numerator} : ℝ)"
    return f"({q.numerator} / {q.denominator} : ℝ)"

LOG2_LO, LOG2_HI = Fr(6931471803, 10**10), Fr(6931471804, 10**10)  # 与 Zeta7.log_le_of_pow_two_upper 的十进制一致
PI_LO = Fr(314159265358979323846, 10**20)  # = mathlib Real.pi_gt_d20 的可证下界
PI_HI = Fr(314159265358979323847, 10**20)  # = mathlib Real.pi_lt_d20 的可证上界

def log_core(y, m=12):
    k = 0; yy = y
    while yy < 1: yy *= 2; k += 1
    while yy >= 2: yy /= 2; k -= 1
    x = (yy - 1) / (yy + 1)
    s = Fr(0); xp = x
    for j in range(m):
        s += xp / (2 * j + 1); xp *= x * x
    rem = 2 * xp / ((2 * m - 1) * (1 - x * x))
    return k, 2 * s, rem

def log_upper(y):
    k, c, r = log_core(y)
    return k, c + r - k * LOG2_LO

def log_lower(y):
    k, c, r = log_core(y)
    return k, c - r - k * LOG2_HI

def sqrt_squeeze(q, prec=10**14):
    s = Fr(math.isqrt((q.numerator * prec * prec) // q.denominator), prec)
    while s * s > q: s -= Fr(1, prec)
    while (s + Fr(1, prec)) ** 2 <= q: s += Fr(1, prec)
    return s, s + Fr(1, prec)

def series_atan_lower(x, kk):
    s = Fr(0); xp = x
    for i in range(kk):
        s += xp / (2 * i + 1) if i % 2 == 0 else -xp / (2 * i + 1)
        xp *= x * x
    return s

def series_atan_upper(x, kk):
    s = series_atan_lower(x, kk)
    return s + xp_next(x, kk)

def xp_next(x, kk):
    xp = x
    for _ in range(kk):
        xp *= x * x
    return xp / (2 * kk + 1)

class Emitter:
    def __init__(self): self.lines = []; self.n = 0
    def fresh(self, b):
        self.n += 1; return f"{b}{self.n}"
    def emit(self, s): self.lines.append("  " + s)

def emit_log_upper(E, argl, y):
    k, u = log_upper(y)
    h = E.fresh("hL")
    E.emit(f"have {h} : Real.log {argl} ≤ {lean(u)} := by")
    E.emit(f"  refine (Zeta7.log_le_of_pow_two_upper (by norm_num : (0:ℝ) < {argl}) {k} 11 (by norm_num)).trans ?_")
    E.emit(f"  simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num")
    return h, u

def log_lower_cert(y):
    # y ≥ 1 的下界证书值：与 emit_log_lower 完全一致（y = 2^s·y'，y' ∈ [1,2)）。
    assert y >= 1, y
    s = 0; yp = Fr(y)
    while yp >= 2: yp /= 2; s += 1
    _, c, r = log_core(yp)
    return c - r + s * LOG2_LO, s, yp

def emit_log_lower(E, argl, y):
    # y ≥ 1 的下界：把 y 写成 2^s * y'，y' ∈ [1,2)，log y = s·log2 + log y' ≥ s·LOG2_LO + (c − rem)。
    l, s, yp = log_lower_cert(y)
    h = E.fresh("hL")
    E.emit(f"have {h} : {lean(l)} ≤ Real.log {argl} := by")
    E.emit(f"  have h1 := Apery.log_ge_artanh (by norm_num : (1:ℝ) ≤ {lean(yp)}) 12")
    E.emit(f"  have h2 : Real.log {argl} = ↑({s} : ℕ) * Real.log 2 + Real.log {lean(yp)} := by")
    E.emit(f"    have e : {argl} = 2 ^ {s} * {lean(yp)} := by norm_num")
    E.emit(f"    rw [e, Real.log_mul (by positivity) (ne_of_gt (by norm_num)), Real.log_pow]")
    E.emit(f"  have h3 := Real.log_two_gt_d9")
    E.emit(f"  simp only [Finset.sum_range_succ, Finset.sum_range_zero] at h1")
    E.emit(f"  have hs : (0:ℝ) ≤ ↑({s} : ℕ) := by norm_num")
    E.emit(f"  rw [h2]; nlinarith [h1, mul_le_mul_of_nonneg_left h3.le hs]")
    return h, l

def emit_atan_lower(E, x):
    x = Fr(x); h = E.fresh("hA")
    if x > 1:
        hu, qu = emit_atan_upper(E, 1 / x)
        q = PI_LO / 2 - qu
        E.emit(f"have {h} : {lean(q)} ≤ Real.arctan {lean(x)} := by")
        E.emit(f"  rw [Zeta7.arctan_eq_pi_div_two_sub (by norm_num)]")
        E.emit(f"  have := Real.pi_gt_d20")
        E.emit(f"  have e : (1:ℝ) / {lean(x)} = {lean(1/x)} := by norm_num")
        E.emit(f"  rw [e]; linarith [{hu}]")
        return h, q
    if x > Fr(1, 2):
        w = sqrt_squeeze(1 + x * x)[1]; y = x / (1 + w)
        hy, qy = emit_atan_lower(E, y)
        q = 2 * qy
        E.emit(f"have {h} : {lean(q)} ≤ Real.arctan {lean(x)} := by")
        E.emit(f"  have hw : Real.sqrt (1 + {lean(x)} ^ 2) ≤ {lean(w)} := Apery.sqrt_le_of_sq_le (by norm_num) (by norm_num)")
        E.emit(f"  have := Zeta7.arctan_ge_half (by norm_num) hw")
        E.emit(f"  have e : {lean(x)} / (1 + {lean(w)}) = {lean(y)} := by norm_num")
        E.emit(f"  rw [e] at this; linarith [{hy}]")
        return h, q
    kk = 8
    q = Fr(math.floor(series_atan_lower(x, 2 * kk) * 10**15), 10**15)  # arctan_ge_partial k 求和 range(2k)
    E.emit(f"have {h} : {lean(q)} ≤ Real.arctan {lean(x)} := by")
    E.emit(f"  refine le_trans ?_ (Apery.arctan_ge_partial (by norm_num) (by norm_num) {kk})")
    E.emit(f"  simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num")
    return h, q

def emit_atan_upper(E, x):
    x = Fr(x); h = E.fresh("hA")
    if x > 1:
        hl, ql = emit_atan_lower(E, 1 / x)
        q = PI_HI / 2 - ql
        E.emit(f"have {h} : Real.arctan {lean(x)} ≤ {lean(q)} := by")
        E.emit(f"  rw [Zeta7.arctan_eq_pi_div_two_sub (by norm_num)]")
        E.emit(f"  have := Real.pi_lt_d20")
        E.emit(f"  have e : (1:ℝ) / {lean(x)} = {lean(1/x)} := by norm_num")
        E.emit(f"  rw [e]; linarith [{hl}]")
        return h, q
    if x > Fr(1, 2):
        w = sqrt_squeeze(1 + x * x)[0]; y = x / (1 + w)
        hy, qy = emit_atan_upper(E, y)
        q = 2 * qy
        E.emit(f"have {h} : Real.arctan {lean(x)} ≤ {lean(q)} := by")
        E.emit(f"  have hw : {lean(w)} ≤ Real.sqrt (1 + {lean(x)} ^ 2) := Apery.le_sqrt_of_sq_le (by norm_num) (by norm_num)")
        E.emit(f"  have := Zeta7.arctan_le_half (by norm_num) (by norm_num) hw")
        E.emit(f"  have e : {lean(x)} / (1 + {lean(w)}) = {lean(y)} := by norm_num")
        E.emit(f"  rw [e] at this; linarith [{hy}]")
        return h, q
    kk = 8
    q = Fr(math.ceil(series_atan_lower(x, 2 * kk + 1) * 10**15 + 1), 10**15)  # arctan_le_partial k 求和 range(2k+1)
    E.emit(f"have {h} : Real.arctan {lean(x)} ≤ {lean(q)} := by")
    E.emit(f"  refine le_trans (Apery.arctan_le_partial (by norm_num) (by norm_num) {kk}) ?_")
    E.emit(f"  simp only [Finset.sum_range_succ, Finset.sum_range_zero]; norm_num")
    return h, q

# ---------- U 点证书 ----------
def U_bound_terms(p):
    res = []
    for j in range(16):
        a, b = A[j], B[j]; m = (a + b) / 2
        if a <= p <= b:
            arg = (b - a) / 4; k, u = log_upper(arg); res.append(('in', None, arg, u))
        elif p >= b:
            s = sqrt_squeeze((p - a) * (p - b))[1]; arg = (p - m + s) / 2; k, u = log_upper(arg)
            res.append(('right', s, arg, u))
        else:
            s = sqrt_squeeze((p - a) * (p - b))[1]; arg = (m - p + s) / 2; k, u = log_upper(arg)
            res.append(('left', s, arg, u))
    return res

def emit_U_lemma(name, p):
    E = Emitter(); terms = U_bound_terms(p)
    UB = sum(C[j] * terms[j][3] for j in range(16))
    E.lines.append(f"lemma {name} : Uρ8 {lean(p)} ≤ {lean(UB)} := by")
    E.emit("rw [Uρ8_eq]")
    E.emit("rw [" + ", ".join(f"aρ8_{j+1}, bρ8_{j+1}, cρ8_{j+1}" for j in range(16)) + "]")
    hs = []
    for j in range(16):
        case, s, arg, u = terms[j]; a, b = A[j], B[j]
        if case == 'in':
            argl = f"(({lean(b)} - {lean(a)}) / 4)"
        elif case == 'right':
            argl = f"(({lean(p)} - ({lean(a)} + {lean(b)}) / 2 + {lean(s)}) / 2)"
        else:
            argl = f"((({lean(a)} + {lean(b)}) / 2 - {lean(p)} + {lean(s)}) / 2)"
        hl, _ = emit_log_upper(E, argl, arg)
        h = E.fresh("hU")
        if case == 'in':
            E.emit(f"have {h} : Uω {lean(a)} {lean(b)} {lean(p)} ≤ {lean(u)} := Uω_le_inside (by norm_num) (by norm_num) {hl}")
        elif case == 'right':
            E.emit(f"have {h} : Uω {lean(a)} {lean(b)} {lean(p)} ≤ {lean(u)} := Uω_le_right (by norm_num) (by norm_num) (by norm_num) (by norm_num) {hl}")
        else:
            E.emit(f"have {h} : Uω {lean(a)} {lean(b)} {lean(p)} ≤ {lean(u)} := Uω_le_left (by norm_num) (by norm_num) (by norm_num) (by norm_num) {hl}")
        hs.append(h)
    E.emit("linarith [" + ", ".join(hs) + "]")
    return "\n".join(E.lines), UB

# ---------- V 点证书 ----------
def emit_V_lemma(name, p):
    E = Emitter()
    slo, shi = sqrt_squeeze(p)
    if slo <= 0:
        slo = Fr(1, 10**14)
    while slo * slo > p:
        slo -= Fr(1, 10**15)
    l1 = log_lower_cert(1 + p)[0]
    k2, l2 = log_upper(p + AL * AL)
    E.lines.append(None)
    hl1, _ = emit_log_lower(E, f"(1 + {lean(p)})", 1 + p)
    hl2, _ = emit_log_upper(E, f"({lean(p)} + (1 / 40) ^ 2)", p + AL * AL)
    hA1, A1 = emit_atan_lower(E, 1 / shi)
    hA2, A2 = emit_atan_upper(E, AL / slo)
    Plo = PI_LO + A1 - 8 * A2
    pos = Plo >= 0
    sfac = slo if pos else shi
    v = l1 - 8 * AL * l2 - 2 + 16 * AL + 2 * sfac * Plo
    E.lines[0] = f"lemma {name} : {lean(v)} ≤ Vfield8 {lean(p)} := by"
    body = [
        f"  have hp : (0 : ℝ) < {lean(p)} := by norm_num",
        f"  have hs1 : {lean(slo)} ≤ Real.sqrt {lean(p)} := Apery.le_sqrt_of_sq_le (by norm_num) (by norm_num)",
        f"  have hs2 : Real.sqrt {lean(p)} ≤ {lean(shi)} := Apery.sqrt_le_of_sq_le (by norm_num) (by norm_num)",
        f"  have e1 : (1 : ℝ) / {lean(shi)} = {lean(1/shi)} := by norm_num",
        f"  have e2 : (1 / 40 : ℝ) / {lean(slo)} = {lean(AL/slo)} := by norm_num",
    ]
    lemma = "Vfield8_ge_of_bounds_pos" if pos else "Vfield8_ge_of_bounds_neg"
    tail = [
        f"  have hA1' : {lean(A1)} ≤ Real.arctan (1 / {lean(shi)}) := by rw [e1]; exact {hA1}",
        f"  have hA2' : Real.arctan ((1 / 40) / {lean(slo)}) ≤ {lean(A2)} := by rw [e2]; exact {hA2}",
        f"  have := {lemma} hp (by norm_num) hs1 hs2 {hl1} {hl2} hA1' hA2' (by norm_num)",
        f"  linarith",
    ]
    return "\n".join([E.lines[0]] + body + E.lines[1:] + tail), v

# ---------- Data.lean ----------
data_lines = ["import Mathlib", "import Zeta7.PotentialIneq8", "import Apery.Certificates",
              "", "namespace Zeta7", ""]
for j in range(16):
    data_lines.append(f"lemma aρ8_{j+1} : aρ8 {j+1} = {lean(A[j])} := by norm_num [aρ8, table7]")
    data_lines.append(f"lemma bρ8_{j+1} : bρ8 {j+1} = {lean(B[j])} := by norm_num [bρ8, table7]")
    data_lines.append(f"lemma cρ8_{j+1} : cρ8 {j+1} = {lean(C[j])} := by norm_num [cρ8, table7]")
data_lines.append("""
/-- Certified upper bound for `log y`（镜像 Apery.log_le_of_pow_two_upper，b 无关抄录）。 -/
lemma log_le_of_pow_two_upper {y : ℝ} (hy : 0 < y) (k m : ℕ) (hk : 1 ≤ 2 ^ k * y) :
    Real.log y ≤ 2 * ∑ j ∈ Finset.range m, (1 / (2 * (j : ℝ) + 1)) *
        ((2 ^ k * y - 1) / (2 ^ k * y + 1)) ^ (2 * j + 1) +
      2 * ((2 ^ k * y - 1) / (2 ^ k * y + 1)) ^ (2 * m + 1) /
        ((2 * m + 1) * (1 - ((2 ^ k * y - 1) / (2 ^ k * y + 1)) ^ 2)) - k * 0.6931471803 := by
  have h1 := Apery.log_le_artanh hk m
  have h2 : Real.log (2 ^ k * y) = k * Real.log 2 + Real.log y := by
    rw [Real.log_mul (by positivity) hy.ne', Real.log_pow]
  have h3 := Real.log_two_gt_d9
  have hk0 : (0 : ℝ) ≤ k := Nat.cast_nonneg k
  nlinarith [mul_le_mul_of_nonneg_left h3.le hk0]

lemma arctan_eq_pi_div_two_sub {x : ℝ} (hx : 0 < x) :
    Real.arctan x = Real.pi / 2 - Real.arctan (1 / x) := by
  rw [one_div, Real.arctan_inv_of_pos hx]; ring

lemma arctan_ge_half {x w : ℝ} (hx : 0 ≤ x) (hw : Real.sqrt (1 + x ^ 2) ≤ w) :
    2 * Real.arctan (x / (1 + w)) ≤ Real.arctan x := by
  rw [Apery.arctan_eq_two_mul_arctan hx]
  have hs : 0 ≤ Real.sqrt (1 + x ^ 2) := Real.sqrt_nonneg _
  refine mul_le_mul_of_nonneg_left (Real.arctan_strictMono.monotone ?_) (by norm_num)
  exact div_le_div_of_nonneg_left hx (by linarith) (by linarith)

lemma arctan_le_half {x w : ℝ} (hx : 0 ≤ x) (hw0 : 0 ≤ w) (hw : w ≤ Real.sqrt (1 + x ^ 2)) :
    Real.arctan x ≤ 2 * Real.arctan (x / (1 + w)) := by
  rw [Apery.arctan_eq_two_mul_arctan hx]
  refine mul_le_mul_of_nonneg_left (Real.arctan_strictMono.monotone ?_) (by norm_num)
  exact div_le_div_of_nonneg_left hx (by linarith) (by linarith)

/-- V₈ 下界模板（括号非负）。 -/
lemma Vfield8_ge_of_bounds_pos {p slo shi l1 l2 A1 A2 : ℝ} (hp : 0 < p) (hslo : 0 < slo)
    (hs1 : slo ≤ Real.sqrt p) (hs2 : Real.sqrt p ≤ shi) (hl1 : l1 ≤ Real.log (1 + p))
    (hl2 : Real.log (p + (1 / 40) ^ 2) ≤ l2) (hA1 : A1 ≤ Real.arctan (1 / shi))
    (hA2 : Real.arctan ((1 / 40) / slo) ≤ A2)
    (hP : 0 ≤ 3.14159265358979323846 + A1 - 8 * A2) :
    l1 - 8 * (1 / 40) * l2 - 2 + 16 * (1 / 40) + 2 * slo * (3.14159265358979323846 + A1 - 8 * A2) ≤ Vfield8 p := by
  rw [Vfield8_eq hp]
  have hsp : 0 < Real.sqrt p := Real.sqrt_pos.mpr hp
  have hshi : 0 < shi := hsp.trans_le hs2
  have hm1 : Real.arctan (1 / shi) ≤ Real.arctan (1 / Real.sqrt p) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hsp hs2)
  have hm2 : Real.arctan ((1 / 40) / Real.sqrt p) ≤ Real.arctan ((1 / 40) / slo) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) hslo hs1)
  have hpi := Real.pi_gt_d20
  have hPle : 3.14159265358979323846 + A1 - 8 * A2 ≤
      Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p) := by linarith
  have hprod : 2 * slo * (3.14159265358979323846 + A1 - 8 * A2) ≤
      2 * Real.sqrt p * (Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p)) :=
    mul_le_mul (by linarith) hPle hP (by positivity)
  have hl2' : 8 * (1 / 40) * Real.log (p + (1 / 40) ^ 2) ≤ 8 * (1 / 40) * l2 :=
    mul_le_mul_of_nonneg_left hl2 (by norm_num)
  linarith

/-- V₈ 下界模板（括号非正）。 -/
lemma Vfield8_ge_of_bounds_neg {p slo shi l1 l2 A1 A2 : ℝ} (hp : 0 < p) (hslo : 0 < slo)
    (hs1 : slo ≤ Real.sqrt p) (hs2 : Real.sqrt p ≤ shi) (hl1 : l1 ≤ Real.log (1 + p))
    (hl2 : Real.log (p + (1 / 40) ^ 2) ≤ l2) (hA1 : A1 ≤ Real.arctan (1 / shi))
    (hA2 : Real.arctan ((1 / 40) / slo) ≤ A2)
    (hP : 3.14159265358979323846 + A1 - 8 * A2 ≤ 0) :
    l1 - 8 * (1 / 40) * l2 - 2 + 16 * (1 / 40) + 2 * shi * (3.14159265358979323846 + A1 - 8 * A2) ≤ Vfield8 p := by
  rw [Vfield8_eq hp]
  have hsp : 0 < Real.sqrt p := Real.sqrt_pos.mpr hp
  have hshi : 0 < shi := hsp.trans_le hs2
  have hm1 : Real.arctan (1 / shi) ≤ Real.arctan (1 / Real.sqrt p) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hsp hs2)
  have hm2 : Real.arctan ((1 / 40) / Real.sqrt p) ≤ Real.arctan ((1 / 40) / slo) :=
    Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) hslo hs1)
  have hpi := Real.pi_gt_d20
  have hPle : 3.14159265358979323846 + A1 - 8 * A2 ≤
      Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p) := by linarith
  have hprod : 2 * shi * (3.14159265358979323846 + A1 - 8 * A2) ≤
      2 * Real.sqrt p * (Real.pi + Real.arctan (1 / Real.sqrt p) - 8 * Real.arctan ((1 / 40) / Real.sqrt p)) := by
    calc 2 * shi * (3.14159265358979323846 + A1 - 8 * A2)
        ≤ 2 * Real.sqrt p * (3.14159265358979323846 + A1 - 8 * A2) :=
          mul_le_mul_of_nonpos_right (by linarith) hP
      _ ≤ _ := mul_le_mul_of_nonneg_left hPle (by positivity)
  have hl2' : 8 * (1 / 40) * Real.log (p + (1 / 40) ^ 2) ≤ 8 * (1 / 40) * l2 :=
    mul_le_mul_of_nonneg_left hl2 (by norm_num)
  linarith

end Zeta7
""")
open(f"{OUT}/Data.lean", "w", encoding='utf-8').write("\n".join(data_lines))
print("Data.lean written", flush=True)

# ---------- 分区整理 ----------
cells_json = json.load(open('research/partition7.json', encoding='utf-8'))
raw = [(Fr(c['l']), Fr(c['r'])) for c in cells_json]
# 强制切分点：qm8/qp8 + 全部表端点（保证 ucase 分类精确）
SPLIT = {QM8, QP8} | set(A) | set(B)
cells = []
for (l, r) in raw:
    marks = sorted(p for p in SPLIT if l < p < r)
    bounds = [l] + marks + [r]
    for i in range(len(bounds) - 1):
        cells.append((bounds[i], bounds[i+1]))
cells = sorted(set(cells))
# 按 V 的局部 Lipschitz 细分：宽 cell 的端点混合松弛 ~ width * V'(t)；
# V'(t) ≈ P(√t)/√t ≤ 30 on (0, 0.05]，≤ 4 on (0.05, 2] —— 限宽 5e-4 / 5e-3。
def cell_width_cap(t):
    return Fr(1, 2000) if t <= Fr(1, 20) else Fr(1, 200)
refined = []
for (l, r) in cells:
    cap = cell_width_cap(r)
    if r - l <= cap:
        refined.append((l, r))
    else:
        nseg = int((r - l) / cap) + 1
        for i in range(nseg):
            refined.append((l + (r - l) * i / nseg, l + (r - l) * (i + 1) / nseg))
cells = sorted(set(refined))

# 自适应再细分：以发射器风格的 cell 界（mono: 2U(r)−V(l)；anti: 2U(l)−V(r)；
# const: 2U(l)−V(相应端)）为目标 < −6.40，违反者二分。
import functools
@functools.lru_cache(maxsize=None)
def Upoint(p):
    terms = U_bound_terms(p)
    return sum(C[j] * terms[j][3] for j in range(16))
@functools.lru_cache(maxsize=None)
def Vpoint(p):
    return emit_V_lemma("tmp", p)[1]
TARGET = Fr(-127, 20)   # -6.35（真峰 -6.3678 + 细分松弛 0.013 + 余量）
def cell_bound(l, r):
    a1, b1 = A[0], B[0]
    if r <= a1:
        return 2 * Upoint(l) - Vpoint(r), 'anti'
    if l >= b1:
        return 2 * Upoint(r) - Vpoint(l), 'mono'
    return 2 * Upoint(l) - Vpoint(max(l, min(r, QM8)) if r <= QM8 else l), 'const'
for _round in range(24):
    bad = []
    for (l, r) in cells:
        if l == QM8 and r == QP8:
            continue
        bnd, _ = cell_bound(l, r)
        if bnd > TARGET:
            bad.append((l, r, bnd))
    if not bad:
        break
    newcells = []
    badset = {(l, r) for (l, r, _) in bad}
    for (l, r) in cells:
        if (l, r) in badset:
            m = (l + r) / 2
            newcells += [(l, m), (m, r)]
        else:
            newcells.append((l, r))
    cells = sorted(set(newcells))
    print(f"  adaptive round {_round}: {len(bad)} violating, worst {float(max(b for _,_,b in bad)):.4f}, cells -> {len(cells)}", flush=True)
# Vstar cell
cells = [(l, r) for (l, r) in cells if not (QM8 <= l and r <= QP8)]
cells.append((QM8, QP8))
cells = sorted(cells)
pts = sorted({l for (l, _) in cells} | {r for (_, r) in cells})
pts = [p for p in pts if p != QM8 or True]
# pts[0] 应为 0：补 (0, first] cell
first = cells[0][0]
if first > 0:
    cells = [(Fr(0), first)] + cells
    pts = [Fr(0)] + pts
pts = sorted(set(pts))
N = len(cells)
print(f"cells: {N}, points: {len(pts)}", flush=True)

# ---------- U / V 点证书 ----------
CH = 40
used_pts = pts
UB = {}
nU = (len(used_pts) + CH - 1) // CH
for c in range(nU):
    chunk = used_pts[c*CH:(c+1)*CH]
    lines = ["import Zeta7.Table7.Data", "", "set_option maxHeartbeats 4000000", "",
             "namespace Zeta7", "", "open Apery (Uω)", ""]
    for i, p in enumerate(chunk):
        idx = c*CH + i
        txt, ub = emit_U_lemma(f"U_pt_{idx}", p)
        UB[idx] = ub
        lines += [txt, ""]
    lines += ["end Zeta7", ""]
    open(f"{OUT}/U{c:02d}.lean", "w", encoding='utf-8').write("\n".join(lines))
print("U files:", nU, flush=True)

json.dump({'UB': {str(k): str(v) for k, v in UB.items()},
           'pts': [str(p) for p in pts], 'cells': [[str(l), str(r)] for l, r in cells]},
          open('research/table7_progress.json', 'w', encoding='utf-8'))
print("PART1_DONE", flush=True)

# ---------- V 点证书 + I_k + 组装（第二部分） ----------
VB = {}
pt_idx = {p: i for i, p in enumerate(pts)}
nI = (N + CH - 1) // CH
STAR_EMITTED = {}
for c in range(nI):
    lo, hi = c*CH, min((c+1)*CH, N)
    imports = set()
    for k in range(lo, hi):
        imports.add(f"Zeta7.Table7.U{(k)//CH:02d}")
        imports.add(f"Zeta7.Table7.U{(k+1)//CH:02d}")
    lines = [f"import {m}" for m in sorted(imports)] + ["import Zeta7.Table7.Data", "",
             "set_option maxHeartbeats 4000000", "", "namespace Zeta7", "", "open Apery (Uω)", ""]
    for k in range(lo, hi):
        l, r = cells[k]
        i_l, i_r = pt_idx[l], pt_idx[r]
        # V 证书
        if r <= QM8:
            vname = f"V_pt_{k}"
            txt, v = emit_V_lemma(vname, r)
            lines += [txt, ""]
            vcase = 'right'
        elif l >= QP8:
            vname = f"V_pt_{k}"
            txt, v = emit_V_lemma(vname, l)
            lines += [txt, ""]
            vcase = 'left'
        else:
            assert l == QM8 and r == QP8, (l, r)
            vcase = 'star'
            E = Emitter()
            slo_m, shi_p = sqrt_squeeze(QM8)[0], sqrt_squeeze(QP8)[1]
            l1v = log_lower_cert(1 + QM8)[0]
            k2, l2v = log_upper(QP8 + AL * AL)
            hl1, _ = emit_log_lower(E, f"(1 + qm8)", 1 + QM8)
            hl2, _ = emit_log_upper(E, f"(qp8 + (1 / 40) ^ 2)", QP8 + AL * AL)
            hA1, A1 = emit_atan_lower(E, 1 / shi_p)
            hA2, A2 = emit_atan_upper(E, AL / slo_m)
            Plo = PI_LO + A1 - 8 * A2
            assert Plo < 0
            v = l1v - 8 * AL * l2v - 2 + 16 * AL + 2 * shi_p * Plo
            star = [f"lemma Vstar8_ge : {lean(v)} ≤ Vstar8 := by",
                    f"  unfold Vstar8",
                    f"  have hs1 : {lean(slo_m)} ≤ Real.sqrt qm8 := Apery.le_sqrt_of_sq_le (by norm_num) (by norm_num)",
                    f"  have hs2 : Real.sqrt qp8 ≤ {lean(shi_p)} := Apery.sqrt_le_of_sq_le (by norm_num) (by norm_num)",
                    f"  have hsqp : 0 < Real.sqrt qp8 := sqrt_qp8_pos",
                    f"  have e1 : (1 : ℝ) / {lean(shi_p)} = {lean(1/shi_p)} := by norm_num",
                    f"  have e2 : (1 / 40 : ℝ) / {lean(slo_m)} = {lean(AL/slo_m)} := by norm_num"] + E.lines + [
                    f"  have hm1 : Real.arctan (1 / {lean(shi_p)}) ≤ Real.arctan (1 / Real.sqrt qp8) := Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left zero_le_one hsqp hs2)",
                    f"  have hm2 : Real.arctan ((1 / 40) / Real.sqrt qm8) ≤ Real.arctan ((1 / 40) / {lean(slo_m)}) := Real.arctan_strictMono.monotone (div_le_div_of_nonneg_left (by norm_num) (by positivity) hs1)",
                    f"  rw [e1] at hm1; rw [e2] at hm2",
                    f"  have hpi := Real.pi_gt_d20",
                    f"  have hPle : {lean(Plo)} ≤ Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40) / Real.sqrt qm8) := by linarith [{hA1}, {hA2}]",
                    f"  have hprod : 2 * {lean(shi_p)} * {lean(Plo)} ≤ 2 * Real.sqrt qp8 * (Real.pi + Real.arctan (1 / Real.sqrt qp8) - 8 * Real.arctan ((1 / 40) / Real.sqrt qm8)) := by",
                    f"    calc 2 * {lean(shi_p)} * {lean(Plo)} ≤ 2 * Real.sqrt qp8 * {lean(Plo)} := mul_le_mul_of_nonpos_right (by linarith) (by norm_num)",
                    f"      _ ≤ _ := mul_le_mul_of_nonneg_left hPle (by positivity)",
                    f"  have hl2' : 8 * (1 / 40) * Real.log (qp8 + (1 / 40) ^ 2) ≤ 8 * (1 / 40) * {lean(l2v)} := mul_le_mul_of_nonneg_left {hl2} (by norm_num)",
                    f"  linarith", ""]
            lines += star
        VB[k] = v
        ul, ur = UB[i_l], UB[i_r]
        a1, b1 = A[0], B[0]
        if r <= a1:
            ucase, ub = 'anti', ul
        elif l >= b1:
            ucase, ub = 'mono', ur
        else:
            assert a1 <= l and r <= b1, (l, r, a1, b1)
            ucase, ub = 'const', ul
        if 2 * ub - v > WORST[0]:
            WORST[0] = 2 * ub - v
            WORST[1] = (k, str(l), str(r), float(ub), float(v), ucase, vcase)
        assert 2 * ub - v <= M0, (k, l, r, float(2 * ub - v))
        L = [f"lemma I_{k} : ∀ t : ℝ, {lean(l)} < t → t ≤ {lean(r)} → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by",
             f"  intro t h1 h2",
             f"  have hU : Uρ8 t ≤ {lean(ub)} := by"]
        if ucase == 'anti':
            L += [f"    refine le_trans (Uρ8_antitoneOn (show {lean(l)} ∈ Set.Iic (aρ8 1) by rw [aρ8_1]; exact Set.mem_Iic.mpr (by norm_num)) (show t ∈ Set.Iic (aρ8 1) by rw [aρ8_1]; exact Set.mem_Iic.mpr (by linarith)) h1.le) U_pt_{i_l}"]
        elif ucase == 'mono':
            L += [f"    refine le_trans (Uρ8_monotoneOn (show t ∈ Set.Ici (bρ8 1) by rw [bρ8_1]; exact Set.mem_Ici.mpr (by linarith)) (show {lean(r)} ∈ Set.Ici (bρ8 1) by rw [bρ8_1]; exact Set.mem_Ici.mpr (by norm_num)) h2) U_pt_{i_r}"]
        else:
            mem_l = "(by rw [aρ8_1])" if l == A[0] else "(by rw [aρ8_1]; norm_num)"
            L += [f"    have e1 := Uρ8_of_mem (t := t) (by rw [aρ8_1]; linarith) (by rw [bρ8_1]; linarith)",
                  f"    have e2 := Uρ8_of_mem (t := {lean(l)}) {mem_l} (by rw [bρ8_1]; norm_num)",
                  f"    rw [e1, ← e2]; exact U_pt_{i_l}"]
        L += [f"  have hV : {lean(v)} ≤ Vfield8 t := by"]
        if vcase == 'right':
            L += [f"    have hq : {lean(r)} ≤ (7 / 5000 : ℝ) := by norm_num",
                  f"    refine le_trans {vname} (Vfield8_antitoneOn (show t ∈ Set.Ioc 0 qm8 from ⟨by linarith, by show t ≤ (7 / 5000 : ℝ); linarith⟩) (show {lean(r)} ∈ Set.Ioc 0 qm8 from ⟨by norm_num, by show {lean(r)} ≤ (7 / 5000 : ℝ); norm_num⟩) h2)"]
        elif vcase == 'left':
            L += [f"    have hq : (9 / 6250 : ℝ) ≤ {lean(l)} := by norm_num",
                  f"    refine le_trans {vname} (Vfield8_monotoneOn (show {lean(l)} ∈ Set.Ici qp8 from Set.mem_Ici.mpr (by show (9 / 6250 : ℝ) ≤ {lean(l)}; norm_num)) (show t ∈ Set.Ici qp8 from Set.mem_Ici.mpr (by show (9 / 6250 : ℝ) ≤ t; linarith)) h1.le)"]
        else:
            L += [f"    exact le_trans Vstar8_ge (Vfield8_ge_Vstar h1.le h2)"]
        L += [f"  show _ ≤ -6.35", f"  linarith", ""]
        lines += L
    lines += ["end Zeta7", ""]
    open(f"{OUT}/I{c:02d}.lean", "w", encoding='utf-8').write("\n".join(lines))
print("I files:", nI, flush=True)

# ---------- 组装 ----------
lines = [f"import Zeta7.Table7.I{c:02d}" for c in range(nI)] + ["import Zeta7.PotentialIneq8",
         "", "namespace Zeta7", ""]
def build(lo, hi):
    if hi - lo == 1:
        return f"I_{lo}"
    mid = (lo + hi) // 2
    name = f"J_{lo}_{hi}"
    left = build(lo, mid); right = build(mid, hi)
    lines.append(f"lemma {name} : ∀ t : ℝ, {lean(cells[lo][0])} < t → t ≤ {lean(cells[hi-1][1])} → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by")
    lines.append(f"  intro t h1 h2")
    lines.append(f"  rcases le_or_gt t {lean(cells[mid-1][1])} with h | h")
    lines.append(f"  · exact {left} t h1 h")
    lines.append(f"  · exact {right} t h h2")
    lines.append("")
    return name
top = build(0, N)
lines += [f"theorem potential_ineq_le_two : ∀ t : ℝ, 0 < t → t ≤ 2 → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := {top}", "",
          "/-- 全 t 的位势不等式：(0, 2] 由分割证书，[2, ∞) 由尾部。 -/",
          "theorem potential_ineq : ∀ t : ℝ, 0 < t → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by",
          "  intro t ht",
          "  rcases le_or_gt t 2 with h | h",
          f"  · exact potential_ineq_le_two t ht h",
          f"  · exact potential_ineq_tail8 (le_of_lt h)", "", "end Zeta7", ""]
open(f"{OUT}/All.lean", "w", encoding='utf-8').write("\n".join(lines))
print("All.lean written; cells:", N, flush=True)
print("WORST_EMITTER_BOUND =", float(WORST[0]), flush=True)
print("WORST_CELL =", WORST[1], flush=True)
print("EMIT_DONE", flush=True)
