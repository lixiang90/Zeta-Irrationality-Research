# 配对消头整格的独立审核

日期：2026-10-06。审阅者 conifold_arithmetic_hypothesis。NEW 独审；不改作者或任何冻结输入。

## R1. 实际读取与准确范围

实际全文读 final research/cdt_odd_paired_head_free_integral_lattice_20261006.md，I1–I25，SHA5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b。此前亦实际全文读 a4c53b 候选，并指出 I25 应限 sqrt(8n)<p≤6n；最终作者仅修该 domain，已再次全文核最终版本。

实际全文读 literature/manifest_cdt_odd_paired_head_free_integral_lattice_20261006.json，SHA6d2d7deddd4837840d5b33c535659523196cbe3e59ec021fb4189bcc6878bb84。旧 primitive 稿 P1–P9 本轮实际全文读，SHA93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8。本文不冒称实际重读 receipt 所列 Brown/Monien PDF；没有新增 primary PDF，本文使用的整数代数步骤已逐项纸面核。

## R2. 完整整数基与 saturation

I3 的连续节点 evaluation 前 2n 列是 lower triangular diagonal1；后 n 列全零，故整数 split surjective。I5 的 cardinal Newton 展开由 binomial 乘积身份及 (1−1) 的求和核过；其系数均整数，degree 与节点身份正确。

逐 pair primitive row (q_m,−p_m) 的 gcd 为1，所以约束 C 到 Z^n 满射。其 kernel 等于指定有理子空间与原整数值格之交，不留 torsion。I8 的 G_m=p_m L_m+q_m L_m' 与后 n 个 Newton vectors 是准确完整基；Bezout 补全给 GL₃ₙ(Z)，并没有把 raw pair 的巨大 gcd 当免费整格。

Raw pair 向量逐列为 g_m G_m；故 index 正是 ∏g_m。d_j=(6n+1)! binom(6n+j,j−1) 逐项核过；至少 6n²log n 的 raw index 与 raw Gram 的 index² 因子同时出现，不能单独制造净余量。

## R3. 范数与 primitive exterior identity

由 I5，||L_j||₁=binom(2n,j)≤4^n；p_m,q_m≤C_n=binom(8n,2n−1) 给实际 Newton 基的 Hadamard 界。Stirling 的 log C_n/n=16log2−6log3，故 I13 主项18log2−6log3正确。它是指定 Newton metric 的 upper bound。

I15 的准确 covolume 身份也通过。C 整数满射意味着 row wedge primitive；Hodge star 给与 kernel 同理性子空间的 primitive integer wedge。两者仅差符号，平方 Euclidean norms 分别是 det(CCᵀ) 与 kernel 基的 Gram determinant，故没有漏掉 gcd 或 saturation 常数。I16 的 binomial inner product 是 Vandermonde 身份。

Evaluation metric 下各 pair 支持分离，covolume 为 ∏sqrt(p_m²+q_m²)。I18 相邻 d 的 ratio 求和后 multiplicity 为 min(j,2n−j)；其 Riemann integral 在0端可积。用 F''=log核得 I=112log2+18log3−49log7，正性可直接由 integrand 取得。作者明确不把这个不同 metric 的 lower bound 当 actual arithmetic/analytic lower cost。

第一 pair p₁=1,q₁=C_n；任何完整基的 pair-coordinate gcd 为1，至少一列有非零 P(2n)≥C_n。Newton evaluation ℓ1≤2^(2n−1)，因此 I20 的单列高度下界正确，但不能升级为总 n² 费用下界。

## R4. 实际局部秩与全部 finite-place 接口

I21 去掉唯一 p 后的 factorial reduction 等于−(z)₃ᵣ。vp g_m=1，primitive constraints modp 无格损失。负评价 kernel 为 H Q 且 Q reflection-even；degree<3r 的差在4r节点消失，得到准确 rank floor(5r/2)。在 p=9r+1 odd prime 时 r 偶数，此式就是5r/2。它不证明 weighted image form 或 weak jet nondegenerate。

I23 的实际 saturated basis S 是整数；两次 Cauchy–Binet 把 common 2n-minor Gauss 界传给 det(SᵀB_NS)。S 的 maximal-minor gcd1 不令 Gram 自身的 Gauss valuation 变0。

从 falling-factorial numerator 到 monomial 的变换整数 unitriangular，除每个所选 row/column 的 i!。无需实际 Plücker 支持时最大扣除确为2Σ_{i=n}^{3n−1}vp(i!)，不是 first2n 项。I25 必须限 sqrt(8n)<p≤6n，最终已如此修；该域的 residue F bounds用于全部2n阶 minors，Laplace 展开与 min-plus 下界兼容。更小 p 采用 stated entry-wise denominator bound，p>6n 由长 harmonic 的单 p 分母被 W 中三次 binomial carry 清除。fixed rational source D^(2n) 在 finite 与 arch 两侧均明付。

这些是安全 bound，不是 content equality；本文未独算新的 LP 主率或 strict margin。

## R5. 审核结论与执行审计

Final I1–I25 全尺度纸面审核通过。完整整数基、所有 finite places 的 direct-summand、raw index、指定 metric 的上/下界、准确 primitive Plücker/covolume 以及 common-minor 整化接口均成立；无限非零、最优 content 与匹配解析净余量仍未证。

本文数学 producer 新建/执行为0；旧或同行 producer 执行、import、重跑为0。仅实际源文读取、保存本文与 SHA256；不以 receipt 中作者的 PDF scope 冒充审阅者自身阅读。本独审不替代本文作者自己的 auxiliary first-jet 论文；该作者稿由 root/quarter/toric 另独审。
