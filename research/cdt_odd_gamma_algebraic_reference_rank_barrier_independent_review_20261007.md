# 同叶整代数参考族与 CDT 秩比较：正式独立全文审查

2026-10-07，审阅者 `/root/masked_racah_finalize`，作者 `/root`。实际 FULL 读取 `research/cdt_odd_gamma_algebraic_reference_rank_barrier_20261007.md` 的全部六节、A1–A15 与公式 A1–A16；审查对象 SHA `d38ca46ee63aebf626309955a6347f40d3c018c42db810b827e20430d3c483a3`，11145 bytes。本审稿为唯一 NEW 正式独审，不修改旧 596 冻结记录，不执行、import、重跑或创建任何数学 producer，不运行或扩展 prime 表。

## V1. 准确读取的直接输入与原件

本轮已实际 FULL 读取冻结 `cdt_odd_gamma_connection_projection_20261007.md` G1–G19（SHA `0bb53d928dbc925dadce1e7dd2c4a1bdd148af0e7c81be4659070aeb893fff44`，18401 bytes）和 `cdt_odd_gamma_lift_holonomy_reference_gate_20261007.md` H1–H20（SHA `78eb5777b649336c7906174878f1b5504e34dd012409fdcbb96e13d1390710c7`，13537 bytes）。前者校准实际原 lift，后者支付 ordinary μ 点的每分支非零 forcing、全 jet rank10 以及原整数坐标的 uniform D_n^9。没有用本轮同行未审稿替代这些冻结条件。

独审时另实际 FULL 读 CDT 固定 v2 原件 `literature/cdt2024_l2_chi_minus3.pdf` 的 PDF66、67、68、69，四个 distinct 页；物理原件 218 页、4517169 bytes、SHA `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。逐式核 Definition6.0.1、Theorem6.0.2、Cor6.0.14 及 Remark6.0.12 的固定系数缩放/limiting 接口。没有新下载或 render 原件，没有继承他人的页数；不声称 CDT 全文218页已读。一次先选择了20页的另一篇既有 CDT 文件，读取越界后改用上述正确固定原件；没有改动文件，该文献定位错误不是数学运行。

## V2. μ 的实际遗漏与规范参考 germ

A1 的局部项 λ_μ(t−μ)^4 log(t−μ)，λ_μ≠0，在齐次差于 μ ordinary point 解析这一冻结条件下，所有 transported branches 首项相同。若 φ 在 z0 达到 μ 且零阶为 h≥1，局部 t−μ=c(z−z0)^h(1+O(z−z0))，log 项留下非零 hλ_μc^4(z−z0)^(4h)log(z−z0)，不可能成为 meromorphic germ。因此含 F_u 的 target-admissible holomorphic maps 的确 omit μ。主稿没有把这个性质无条件传给删掉 F_u 的其他投影。

对规范 G_k=(1−At)^(k/q)，绕 μ 的 Fourier argument 用全部 q 个迭代 loop：矩阵 (exp(2πijk/q))_(j,k) 可逆且有理系数单值，故每个 scalar coefficient 必为0。这证明实际 C(t) 独立；任何选出的 m≤q 行也独立，不只是宣称代数扩张 degree=q。A3 的阶一微分式符号准确。φ omit μ 后 1−Aφ 无零，单连通盘上规范 log 存在且起点为0，所建 pullback 正是 Taylor germ 的全盘 holomorphic 延拓。

## V3. 完整全有限处整模型

约分 k/2^s=k'/2^(s')，k' odd。n≥1 时 numerator 的 n 个 factors 全 odd，(−A)^n 的2-adic valuation为20n，分母为2^(s'n)n!，所以

\[
v_2([t^n]G_k)=(20-s')n-v_2(n!)=(19-s')n+s_2(n).
\]

s'≤19 时全部非负，n0 coefficient=1，k0 行为常数，所有边界都已包括。此处 A 的符号只改变 coefficient 符号，不改变 valuation。

odd p 上 k/2^s∈Z_p；固定 n，以非负整数 a_h p-adically 趋近它。binomial polynomial 在 Q_p 上连续，除 n! 仅有固定 valuation，而整数 binom(a_h,n) 的极限仍在闭集 Z_p。故不是仅在2处证明整性；真正得到 Z[[t]]。s19/q524288 与 s4/q16 的 claimed ranks 均符合此范围。

## V4. 相同 m 和相同 partition 的 CDT 比较

CDT Theorem6.0.2 明确允许 u_j=m；零 column 与 e=0 给 τ_flat=τ_sharp=0，且参考函数 holonomic，因而 conformal 条件为 ρ>0。Cor6.0.14 对参考 family 给 J≥mρ。target 用同一个 J、同一个 m 且 τ_T≥0、ρ>τ_T，得到 J/(ρ−τ_T)≥mρ/(ρ−τ_T)≥m，含 τ_T=0 的等号边界。分子无穷或未满足原解析/limiting 条件的 maps 不构成 strict contradiction。

多 map 的式 A9 正是 PDF67 的完整 numerator：patched increasing-rearrangement double integral，加 (1/m)Σγ_k² log derivative ratios。参考与 target 使用相同的 m、全部 maps 及同一个 partition，故 Theorem6.0.2 给 N_(φ,γ)≥mρ_l；没有省略 gap terms。选 q16 的 first ten 行与包含 F_u 的 frozen rank10 family，于是 A7 的任何非负 CDT 费用排除结论成立；它不要求更小的 denominator cap 已被证明。

## V5. 高 rank 坐标缩放两边同时支付

B=2^max(0,s−19) 给 v2(AB)≥s+1，原全 prime binomial proof 遂使所有 tilde G_k(x)=(1−ABx)^(k/q) 整 Taylor。ψ=φ/B 正确保留 tilde G_k∘ψ=G_k∘φ；ρ_ψ=ρ_φ−logB，J(ψ)=J(φ)−logB，因为两个 log-radius 同时移相同常数，其 max 也移此常数。

CDT 在新 x 坐标零费用参考 family 上给 J(φ)−logB≥m(ρ−logB)，准确整理为 A12：J≥mρ−(m−1)logB。所有 maps 同除 B 时 patched g 减 logB，derivative ratios 保持，因此 A13 的完整 multi-map 式亦成立。τ_T≥logB 是作者明确给出的充分排除条件，满足 mτ_T≥(m−1)logB；未宣称最优或必要，不把 s>19 的原 t Taylor 免费视为整。

## V6. 有限 polynomial 放大的量词、rank 与原费用

degree≤d 的九个实际 jet 的 monomials 数为 binomial(d+9,9)；Q[t] coefficients 不增加 Q(t) span。逐个 index≤d 给该数≤(d+1)^9，整数 d≥1 有 d+1≤2^d，从而 m≤2^(9d)。主稿只使用真实独立 rows 的 rank upper，包含1和F_u 使 m≥2并保留 omission；不声称所有 monomials 独立。

每个 jet 的 frozen fixed-multiplier/D_n^9 模型，在 degree≤d convolution 中由 D_(n_i)|D_n 得 fixed-multiplier/D_n^(9d) 模型；Q[t] shifts 的非负指数同样保持。finite tensor/module closure保证 holonomic。对 first row1 和其余 m−1 行，9d 个 width1 columns 均 u_j=1，PDF66 的公式准确给 τ_T=9d(1−m^(−2))；这是已支付 uniform safe 账本，不是最小费用。

取 s=ceil(log2m)，B≤m；因此 logB≤logm≤9dlog2。log2<3/4 可由严格凸函数1/x 在[1,2]的 trapezoid 上界得出；m≥2 给 9d(1−m^(−2))≥27d/4，遂 A16 严格成立。任意大但 fixed finite d、真实 m、fixed u、含 F_u 的该类 family，均被同一已付费 comparison 排除。不外推到删 F_u 的 projection、所有 tensor 或新的算术 arrays。

## V7. 审查结论与边界

全部 A1–A15、A1–A16 已实际逐式纸面检查，通过，无正文数学修订请求。新成果是：在同一 forced-omission leaf/interface 内，原 rank10 family 的 strict CDT 余量受任何非负费用的参考比较阻止；保留 F_u 的上述 finite polynomial amplification 配合 current uniform 模型也无法逃出。它没有证明任何 ζ/L/Catalan 数值无理性，没有把参考 rank 当 target rank，没有宣称通用方法不可能。

本正式审稿完成后由审阅者实际 FULL 自读全部 V1–V7；数学 producer 创建/执行/import/rerun、prime-table运行/扩展、Lean 均0。直接 primary actual FULL 四页，下载0，render0。最终主稿仍须作者收审后实际 FULL 回读及其单向 FINAL 来源收据；本审稿不 pin 任何未来或互相 receipt。
