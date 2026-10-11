# 真正 Q(x) polylog 分母主稿的独立全文审查

2026-10-07，NEW，审阅者 /root。被审稿 [rational polylog cap](cdt_odd_paired_rational_polylog_cap_20261007.md) 的实际物理 SHA256 为 `51ec9a76c83c612407d4c28e4017867a1db7a27a85b0f2727aabedf4701d351c`。本人本轮实际完整阅读其六节、R1–R17；不是只读摘要、hash 或同行结论。结论：限定范围内 PASS，未请求数学修改。

## 1. Laurent 尾部与精确抵消响应

R4 的固定有理函数 Laurent 展开在有限坏素数以外具有整个无限尾部的 p 整性；最低 Laurent 次数是固定整数。因此 N=kp+s 的每个非零卷积项都只有有限正 Ξ 指标，且指标总和不超过 N−h_*。当 p 足够大时它们小于 p²；若有 k 个被 p 整除的指标，其中任一个达到 2p，总和至少 (k+1)p，留下的固定 Laurent 下界不能补足。这个排除确实涵盖在 0 有有限极点的变基。

最高系数非恒定时，固定非零、非零次 Laurent 系数 a_(j,s) 提供 N=jp+s 的唯一 j 极点层，残数 β^j a_(j,s) 非零。低次项没有 j 个极点，故 R6 的精确估值 −5j 成立。

最高系数恒定且 j≥2 时，不能分别断言旧 witness 不抵消。本人重新列出 N=(j−1)p+s 的最低层：最高 j 次项有 j 个选择非极点位置的排列，系数 j a_j Ξ_s；低 j−1 次项系数为 a_(j−1,s)。它们合起来正是 H_s=(j a_j Ξ+a_(j−1))_s。Ξ 非有理函数确保 H 非恒定，因此存在固定 s≠0 的非零响应。s≤0 时 Ξ_s=0，仍由 Laurent 项给同一公式。R8–R9 对应精确 −5(j−1)，并未漏掉同阶抵消。

j=1 且最高系数恒定的例外必须保留：N=p 的估值为 −5，固定 N=p+s、s≠0 的位置没有同样极点。R10 和后续 N^e 例外没有被 degree≥2 结论吞并。

## 2. Prefix 下界及有限 LCM 的必要费用

R11 的固定 k,s 对每个大素数给一个前 N 系数的分母因子 p^(5k)，再由 θ((N−s)/k)∼N/k 得 R12 的 liminf≥5。这里只是 prefix 分母的必要下界，不是 upper，也不是 τ 的定义。

R6/R9 的 shifted index 不被 p 整除；任何固定 N^e 在该处均不付 p。每个固定 LCM(bN+c) 在大 p 时最多付一个 p，并且能付 p 的 slope 必须 b≥1/k。精确 −5k 至少需要 5k 个这样的 factors，总 slope 至少 5。固定 offsets、integer scaling 和有限坏素数不破坏此结论；变基及 cap 均先固定，不能随 witness prime 变化。

## 3. 实际 full basis 与 CDT 费用定义

由 Ξ 的幂在 C(x) 上独立，degree≤1 的 Q(x) 空间恰有维数 2。任意实际 full basis 至多两条 independent rows 可绕过 degree≥2 的 slope≥5 界。另一方面 V_n 严格正定使每个实际 d-principal polynomial 的最高系数 det(V_I)>0；实际模块有 degree d 元素，所以任意 full Q(x) basis 至少一条 degree d row。这补足 q=1 和 q=2 情况，未把 matrix rank 与函数模块维数混同。

本人本轮实际文本全文读 [固定 CDT v2 原件](../literature/cdt2024_l2_chi_minus3.pdf) PDF66–69 四页，218 页版本，SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。核对 Definition6.0.1、Theorem6.0.2 的 (6.0.3)–(6.0.9)、Remark6.0.12、Corollary6.0.14 和 BasicRemark6.0.17。column-step 条件的 σ_i 确实非降，τ^flat=q^−2 Σ(2i−1)σ_i。因此 q≥3 的下界 5(1−4/q²)、q=1 的 5 和 q=2 的 15/4 均正确；τ^sharp≥0。标准 slit 的 conformal radius4 使这些 full-basis 类型不满足所选定理的正分母门槛。该结论只排除正文指定的 finite module、finite-LCM/N^e 类型与标准 slit leaf，没有扩大到所有 period 实现或所有 holonomy 方法。

## 4. Branch、端点及真实校准

有理函数变基不能删除非恒定 polynomial-in-Ξ row 的 translation monodromy；多次绕行形成无限多个 Ξ+kv，最高次数比较迫使 invariant row 的正次数部分为零。实际 invariant part 为 W∩Q(x)，维数至多1，未假定 W 包含常数。

变基的端点正则及 U(1) 条件独立于分母证明。xΞ 经 1/x 变成 Ξ 的校准保留 x↑1 的同一 ξ，并在 0 正则；它确实把 flat cap 从至少5降到0，但引入 e=5。直接按原文 m=1 的定义，I^1_ξ(ξ)=(1−ξ)²/2，τ^sharp=e。原文 m=2 的 e=(0,1) 为3/4，齐次性给 e=(0,5) 的15/4。R17 没有把 flat 改善当作 total margin。

## 5. 本轮读域与结论

本人还实际完整读上一轮 [module bridge](cdt_odd_paired_compound_period_module_bridge_20261007.md) 及其 [独审](cdt_odd_paired_compound_period_module_bridge_independent_review_20261007.md)，核对 R1–R2 所用实际 polynomial module 及非有理函数前提。旧记录均只读。本审查不新增、执行、import 或 rerun 数学 producer；不扩 prime 表。

R6、R8、R12、R14–R17 在明确量词及实际源 ξ=αζ(4)+βζ(5)、β≠0 下通过。结论是分母接口与该标准实现的范围障碍，不是新 ζ/L/Catalan 数值无理性或线性无关性，不是 Lean 验证，也没有解决其他路线的 strict analytic margin。
