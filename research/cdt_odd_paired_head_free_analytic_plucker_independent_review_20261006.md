# 配对空间真实解析与加权Plücker接口：独立审阅

日期：2026-10-06。quarter_actual_rank。NEW 独审；所有旧/同行数学文件只读。数学 producer 执行、import、重跑均0，外部Lean0。审阅通过下述范围，没有新的特殊值数值定理。

## J1. 实际全文读取与来源范围

实际完整读取 root 新稿 `research/cdt_odd_paired_head_free_analytic_plucker_root_20261006.md` R1–R6、全部公式R1–R16，输出无截断，SHA **cf341860474546dc0d5a2a630ae73f6bbf50426fa7ee8c100975c6a2b1688e38**。本审未运行任何数学producer。

实际完整重读冻结整数格输入 `research/cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md`，SHA93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8。自身新整数格稿是作者输入、并非自身独审自身；最终作者全文回读的候选 `research/cdt_odd_paired_head_free_integral_lattice_20261006.md` SHA5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b。其I25在同行独审后明确限制sqrt8n<p≤6n，其余p>6n另有integrality证明；所有索引与norm区分保留。

本轮实际读取两份primary PDF：

| 原件 | SHA256 | 本审实际读取 |
|---|---|---|
| `literature/brown2026_mellin_transfinite_diameter_arxiv2604_20741v1_20261006.pdf` | fcbcc22ee7504b9e057c534c0e5fae3f3812af8548d132cd2018ce4857a20bef | PDF7–10、21–24，8页；原件34页 |
| `literature/monien2009_hankel_dirichlet_arxiv0901_1883v1_20261006.pdf` | 2c75a17ba33a84e95269601ebb218fdbf8fdbf249882f8b22b49e0c86fb5d7ef | PDF1–3，3页；原件12页 |

实际完整原页文本已读，未凭abstract或同行scope冒認全文。两PDF由root本轮归档，本审仅只读，无自身下载或TLS例外。Saff PDF本审未读取，其equilibrium建议不是R1–R16证明输入。Lai上轮的读取页不计为本轮再次读取。

Brown PDF8明确real/nonnegative form与real generators等P1–P3，Lemma3.2才保证真实Gram正定；PDF9 Proposition3.5是一般module Vandermonde identity。PDF21–23区分nonzero hypothesis、整化与period-span≥2；尤其PDF22 Corollary7.3和PDF23 Lemma7.8并非直接证明任意指定多项线性无关。Monien PDF2–3 Theorem2.1及Lemma2.3是正系数Dirichlet系列的多节点平方Vandermonde，不投影成仅含1与本轮ξ。Root的来源边界与这些实际页一致。

## J2. 同一目标、积分与严格total-variation Gram

R3的实际整数值格基det未再除first2n factorial，形式X关系与实际ξ严格区分。X-leading矩阵24ΣW ev⊗ev在配对空间上positive definite，degree恰2n；此不保证指定rational specialization非零。

R4两pair的R''' factorial numerator相同而sign相反，P(m)/d_m条件恰消去整个bilinear finite head。故右线R5只在实际ξ或候选关系成立时识别目标det。所有g degree≤3n−1，degreeR g_i g_j≤−4，K在半整数竖线上指数衰减，所需全部moments和det integrand绝对可积。有限区间展开后dominated limit合法，R6平方是普通复bilinear determinant，不偷换成Hermitian或ordinary Vandermonde。

R8独立核准：先对R6取绝对值，得到∫|detg|²∏|dμ|/r!；Hermitian Andreief恰等于det(SᵀMS)，S真实整数。M positive definite由nonzero polynomial在直线上的有限zeros及K非恒零保证。此正包络是upper bound；其非零不推出原complex/signed det非零。因此不能将Brown P1/P2套到人工包络后证明实际目标nonzero。

## J3. Mandatory高indices、加权Plücker与全n预算

实际S的low/high block diag(A,I_n)成立，因为G全部degree<2n且kernel基是f_(2n)..f_(3n−1)。任何nonzero 2n-minor必须包含全部这n个high indices，再从low2n选n个，数量binom2n,n；这不是任意size2n Hankel的first-indices模型。

R10由Cauchy–Binet严格给Σ|u_I|²=detSᵀS，即原Newton-Euclidean covol²，finite gcd1来自真实饱和性。R11的rectangular determinant展开与每个Hermitian minor identity符号/normalization正确。

在L²(ν^⊗r/r!)中triangle inequality给R12：

\[
|D_A(\xi)|\le
\left(\sum_I|u_I|\sqrt{\det M_{I,I}}\right)^2.
\]

Cauchy–Schwarz给R13，finite maximum给R14的2logbinom2n,n。其组合费O(n)，允许actual同一I的Plücker与analytic minor配对研究，不免费将两个不同norm的最大值拼接。R15恰是I13的Newton fee乘2，尚未声称任何det衰减主率。

## J4. Degree与禁止错误预算继承的范围

每个V_I最高homogeneous项是(∏i!⁻¹)det(z_j^i)，非零，故除Δ后最高总degree恰Σi−r(r−1)/2。Mandatory high sum=n(5n−1)/2，low选n的sum在n(n−1)/2与n(3n−1)/2间；减去2n(2n−1)/2，准确为n²到2n²。Lower terms并未消失，所以不能声称每一项都有minimum degree n²。

这些symmetric factors、actual Plücker坐标与right-line measure都可改变n²能量。以ordinary size2n Vandermonde替换实际det，或将fullsize3n determinant小界当所有2n minors的小界，均不成立；root diagonal反例充分。恢复四重zero的k4空间具有不同R及degree，不能给此paired-space免费预算。

## J5. 审阅结论

R1–R16的实际same-target identity、absolute convergence、total-variation Gram、mandatory support、weighted全n bounds及degree结论通过。本审未发现需改root数学项。

已证的是可执行的真实解析/整格接口。Restricted specialization无限nonzero、各I的实际解析n²率、足够便宜的signed arithmetic content以及正margin均仍待证。没有新ζ/L/Catalan无理性、线性无关性或Lean认证。本文作者完整最终回读后冻结，来源receipt另保存，不改旧稿或同行稿。
