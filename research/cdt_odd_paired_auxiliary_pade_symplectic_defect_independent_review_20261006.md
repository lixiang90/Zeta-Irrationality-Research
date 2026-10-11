# 实际辅助素数 Padé 辛缺陷稿的独立审阅

2026-10-06；审阅者 `/root/toric_chow_completion`。NEW 审阅稿，不修改被审数学文件或旧 pins；全部旧/同行 producers 执行、import、重跑为0。

## V1. 实际全文与原件读取范围

实际全文读取 [被审稿](cdt_odd_paired_auxiliary_pade_symplectic_defect_20261006.md) 十节、D1–D25，SHA `452d0271f294b304f3b8bd2a65b343ae5e8b1af128267750e7c9118862066be2`。其 NEW PY `0000ef0f9b98659874603579fc9cf60d1ed5572940f1c150ab007fdd1fa84504` 与完整 NEW JSON `e751f6c57b27ccf4624bd12b27827bd3edbcfb3e9413d08162238cef2ec7bef7` 均逐项静态全文读，不执行/import。实际全文读取当时的作者 receipt `2f6f331bae4c99ea18dbc9e1c11a953b8b0fa2982bd062fb10a5949abe742f7c`；它是候选状态的真实读取快照，不以之后作者的状态更新替代此次读取。

随后作者只更新 receipt 的 reviewed/frozen 状态及准确 review confirmations；审阅者实际完整补读最终 receipt `f0502fc3539c08c95aa979c502eb5bda26d8c467734eb406e58ac68304d417da`，主数学、PY、JSON 哈希不变。

另实际完整回读冻结 [CRT structure](cdt_odd_paired_auxiliary_units_structure_20261006.md)，SHA `dcc6d4d670dbcc3960936d3ee1b21a877f73c03e2ba65c479c9d550e0624a8a5`，包括 U14–U28 的真实 bounded-kernel 接口、U21 的 descending-coefficient determinant 归一化及 U5/U6 的 middle weights。

本轮审阅者实际读取作者已正常 TLS 归档的两份原件：Beckermann–Labahn PDF1–15（分1–7和8–15两个完整无截断输出），D'Andrea–Krick–Szanto PDF1–8（一个完整无截断输出）。合计23 distinct PDF页；审阅者新增PDF下载0，不能与作者下载数重复计。准确路径、hash、阅读页与出处另存 NEW review receipt。

## V2. actual graph index 与 shifted-degree 证明通过

D3–D6 的 row graph bases 确实生成全部 congruence module，determinants 是 P 与 P²。critical bounds 的和为 N 与2N，每个 symplectic coordinate pair 的 bounds 之和都是 N。

D8 的 row cancellation 每次使 `2ν·sdeg+LP` 严格下降；非零 polynomial vector 的该量有固定下界，所以终止，且每步 unimodular、不需目标 Gram pivot。D9 选最大 leading position 的同-degree 项，可排除整体最高项消去。shifted leading matrix 为三角，故 det-degree=sumδ+sum b；critical sumδ=0。strict negative 部分的 Hilbert function 是 Σmax(0,−δ)，更一般累积维数恢复 δ multiset，degree defect 因而与约化路径无关。上述证明自足，不依赖假定所有 intermediate profiles 正常。

## V3. 辛自对偶与实际 corank 等价通过

手算 B_0 J B_0^T=PJ，matrix 情形使用真实 numerator symmetry，scalar 情形同样成立。β=vJw^T/P 是 graph module 上 polynomial-valued unimodular alternating form。paired bounds 给 degβ_ij≤δ_i+δ_j。由于 form determinant 非零，至少一个 determinant product 非零；每项迫 δ_i+δ_σ(i)≥0，而全部和为0，所以每个和恰0，δ multiset 确为 (−d,d) 或 (−d₂,−d₁,d₁,d₂)。这个 matching argument 不以未知 Gram 非退化为输入。

frozen U23/U27 的 degree cutoffs 正好是被审 D6 的严格负 shifted-degree 条件。bounded A、B 均 degree<N，从 T 或 (T,Q) 唯一恢复，排除了前分量零而后分量非零的 bounded vectors。因此 corankG₀=d、corankM₅=d₁+d₂，以及所给全部 actual kernel basis 成立。它将未知 gate 准确缩成三个非负整数；未证明它们在无穷 p=18r+1 上为0。

## V4. principal subresultant 的 normalization 与实际环境因子通过

独立核 D18 的 elimination：P-rows 的最高 e−1 columns 为 unit triangular；剩余 g-rows 经消去后是 rem_P(u^j g)，原 j descending，与冻结 U21 的余式矩阵转置相差 row reversal，sign 为 (−1)^{e(e−1)/2}。因此 D19 的 index4r+1 和 scalar exact sign 正确，包括 padded g 实际 degree 较低的情形。

原件 D'Andrea–Krick–Szanto PDF3 明确保留 deg(g)<N−1 的 padded monic definition；PDF4–5 的 PRS/reconstruction 对非零 subresultant 和节点上的 denominator 有明确条件。其结论不能把 gcd(P,g)=1 升成所有 principal coefficients 非零。被审稿保留这一界线。

环境 scalar Gram 的 Vandermonde-square/productP′ sign 为 (−1)^{N(N−1)/2}，productg=(-1)^N2^{r−N}R^{-6}，故 D22 通过。matrix 两 channels 的 Vandermonde 四次方与 productP′² 抵消，localdet=−3(2−χ)S^{-4}，nonmiddle 共4r+1点，故 D23 通过。D24 正是 principal Jacobi complement，无新 sign；未知 complementary target minor 没有删去。环境全维 unit 不等于目标截断 unit，也没有产生新的 finite-place 费用信用。

## V5. p37 真实 nonperfect 中间 profile 与有限探针范围通过

独立手算 r2,p37 的 S(0)=28、inverse4，以及 ratio 表；Σ μ_k s_k⁵=148≡0，Σ k² μ_k s_k⁵≡12。因此同一真实 moment sequence 的 size1 determinant 为0，而原 scalar size2 determinant=−12²=4。这个反例保留 middle，不是 toy weights；它反驳所有 intermediate Hankel profiles 均 unit 的过强 perfectness 假设，亦不反驳原目标在该 prime 非零。

PY 静态核读确认：real nodes 构造 numerator，与冻结 U15 在0和非零平方节点的不同 P′ scalar 相容；weak-Popov algorithm 保留 graph，所用 negative-degree corank 与纸面 formula 对接。完整 JSON 为五个此前已研究的 r=1,2,4,6,7，共14 scalar profiles与42 matrix profiles；actual target 和 nearby diagnostics 明确区分。有限表不扩成全 r、无穷 prime 或 nonzero theorem。审阅者未运行该程序。

## V6. 文献边界、审阅结论与本轮研究进展

实际 BL PDF9–10 的 normality/perfectness 与 controllable data 定义、PDF11–14 的 Mahler degree equivalence，以及 PDF14–15 Theorem6.1 的 nonzero stepping 条件都保留显式 prerequisites。所读 PDF1–15 支持跨 singular subproblem 的算法框架，但审阅者没有称已读 PDF16–31 的完整 nonperfect algorithm，也没有用它替代本稿自足 D8–17。

实际 DKS PDF1–8 的 rational interpolation 公式同样保留非零 numerator 与节点 denominator 条件；未称读PDF9–14。两篇原件均不承诺当前真实 χ 与 critical profile 的 normality。

**按实际读域通过。** 本稿提供 actual scalar/matrix target 的两整数辛缺陷与 fixed principal coefficient 接口，及一个真实 intermediate nonperfectness 反例。无限 simultaneous unit、same-object strict margin、特殊值无理性仍未证。审阅者本轮无新增数学 producer；自身另一份 jet 稿恰1次首次运行与这里的 peer 静态审阅分开登记。本文保存后全文回读，来源 receipt 单独 pin，不修改旧或被审文件。
