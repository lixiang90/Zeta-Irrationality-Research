# 第248轮独立数学审阅：原椭圆源 cap 与 Fricke 商源

2026-10-10，B。两份最终稿均实际 FULL 阅读并逐项纸核；结论 **PASS，无必要数学修正**。本文是唯一合并收据，不修改作者稿或既有 B 主稿/scope。它不认证新数值定理，也不认证未完成的商源全叶或严格预算。

## 1. 最终读取身份与原源 cap

- Root：research/dyadic_elliptic_uniform_cap_round248_20261010.md，全部七节，8699 B，SHA256 ae596e99d2d477a766746c0392ff6938070d70fcc5fff85acc066ec5c947d72c。最终保存版再次 FULL 读；此前草稿审阅不替代这个身份。
- A：research/chi7_fricke_quotient_source_round248_20261010.md，全部六节/Q1–Q18，12413 B，SHA256 a95eda931df3fcf8042376b5a49d66bb60f8622f2772e3548178a176a853912b。FULL 读后独立核以下具体数学；并重新核保存身份一致。

Root 的五行两列数组、τ32/25 和整数 rank3 子源的 J≥3λ 正确，严格入口确需 λ>16/5。f14 两 congruence sums24、字符参数196为平方；四 cusp orders 均1，故实际 ω=f14 dq/q 全纯无零、native leading1。t 的完整 divisor 给 degree2，W-invariance先支付真正商坐标；y anti、其完整 pole orders先给四次空间，五个正确头项才确定 whole quartic。本人手算这些五项，没有数学程序。

quartic→Weierstrass 消元及 inverse 精确；隐式偏导 F_U=2y、F_t=V 给 ω=−dX/Y，没有遗漏2πi或未定 isogeny 倍数。正实 oval 给 a；从负实轴经 branch1到正实轴的路径两端同到 infinity，确是闭曲线，给 a/2−ib。反向/共轭给所需 a/2+ib。只需这两个 period 在完整 lattice 内，不需假定为 primitive basis。

两 quartic 积分比较、κ分解、a²<80/13、b²<200/47、R²<1590/611<25/9 均独立核定。逐 imaginary row 再逐 real node 的 covering bound 正确。Bloch证明中可对 (h′−α)/(3α) 用零点 Schwarz；Rouché 在半径1/3给真实 image disk M/12，适用 multivalent。field normalization lift、真实 x-pole fiber 的遗漏、Abel lift 及 z′0=φ′0 衔接无缺口。因此所有原完整五行共同图 c<20；联能量门槛只关闭 **原 x、已付数组、基本单实处判据**。更优联合整型、不同源/坐标或其它判据未被排除。

## 2. 商源 exact gauge、forcing 与实际 rank

A 的 Q3–Q10：eta 字符/四 cusp divisor、W 商 degree-one、Q± simple roots 与全部 ramification、真实 quadratic field 全部成立。独立核加减 Q5 得 A1A2/f14=Q0/t、(A1²−2A2²)/f14=−y/t；native sign不能省略。Q8 中 u 的 finite rational formula 已付微分身份和首项，v=ut 来自整个 eta product，Z 来自 f14³=f1 f1(2τ)，不是有限系数猜测。

取 d=δlogu、k=A+/A1、ℓ=δlogk。拉回并 gauge 原方程确给
\[
p_1=-\delta\log d-2\ell,\qquad
p_0=-d^2V+(\delta d/d)\ell+\ell^2-\delta\ell.
\]
实际 Wronskian A+²δτ=a+Q+/(2πi y) 给显示 p1；全 Γ 与 W 的常数矩阵返回使唯一 monic operator 在 y↦−y 下不变，因此 p0∈K(t)。先有 invariance，再取 trace，未错误替换原方程。

对 B_g=A+(I+−g)，乘积的 δI 交叉项因 p1=δlogG0−2δlogA+ 精确消去，故
\[
\mathcal L_+B_g=A_+h_+/G_0^2.
\]
代入 Q7/Q10 得 Q13 的完整有界 algebraic expression；Γ 与 W 的权/字符相消令 forcing 在 K(t)。native首项非零，g不改变 forcing。

Q14 的全 Γ affine polynomial不是只援引 W：两次 Bol 微分给 Pγ″=0，字符平方1使 B0(γτ)=B0+ A+Pγ。对任意 g 再加 g(A+−A+∘γ)，确属 homogeneous span。T、U14 实际返回无共同 invariant line，故二阶 operator 不可约。坏 cusp 的非零 log² 给 B_g 非 rational；实际 cyclic quotient rank2，完整三行 rank3。非恢复证明的微分稳定直和投影确令 Lz=0，而非错误声称所有 rational coefficients 的 homogeneous module 元素原本都被 L 杀。log² 不能来自 rational r 加齐次 z，结论对每个固定 g 正确。

## 3. 整模型、共轭与未付准入

t=q+整数高项，formal inverse q(t) 亦整；完整 d_N² 清 R、D，故固定7b支付所有 primes/powers 的 B_g prefix，δ-jets 不索取超出prefix的项。普通 derivatives 必保留 shifted cutoff。这个安全整模型不是最优 primitive 内容或同对象净能量。

K=Q√2 的系数共轭实际把 A+、I+、Q+ 变成对应减号。g=g+ 不支付 σ(g)=g−；若同时要求两 canonical返叶补点，差给 π² algebraic，确与已知 transcendence 矛盾。这是双方免费补点的障碍，不是 g+∉K 的新定理。

商源改变实际 species，原 genus1 cap 不能直接搬到 t。仍缺全部 Γ 周期多项式的目标关系控制、全部 transported到达叶的共同合法性、另一 embedding 的实际图，以及同对象全有限处/实处严格预算。没有凭 rational forcing/rank3 宣称准入；不自动启动图或素数续轮。

## 4. 本人实际 primary 读域

本轮 FULL 读出版社所存 alternative_eta_quotient_theorems_pdf11.txt 完整物理11页（印页835），2730 B，SHA256 1b29e52c8e2fafef77f01dfa8f7b937dda39937a57f9a94778685eacbc199f7b，含 Theorems2.4/2.5 的全部条件：采用其明确转述的 Ono eta-character/cusp-order statements，未读上游 Ono 完整证明或该论文全文。

另 FULL 读 Root 的 root_savitt_newman_statement_selected.md 规范化记录，1696 B，SHA256 b66e130948ca3b3841a0d813ccaf6a8843ac9949ea0e613ba1f7c49042d3d741。这是本人阅读记录文件，不冒称本人重新打开 Savitt 原PDF或确认其全部证明；实际独核 eta 条件另由上述出版社完整 theorem page支付。

旧 CDT 五页/247数学输入的本人 FULL 读域见冻结 B248 packet_reading_scope.md（4674 B/SHA256 566c13e517d80c9b4e1fe0982d2c9159aed5e76aaedc8ab1dea48a5d8650bd90）。采用标准 Frobenius、monodromy不可约性、genus1 Abel universal cover与π² transcendence；没有冒称对这些通用定理的新证明或完整 primary 复审。

数学程序/CAS/Lean/interval/prime/parameter/map scan 均0，无新增GET、无旧文件/main/policy/manifest/external Git写入。只保存本 NEW 收据，保存后本人实际 FULL 复读并报 bytes/SHA；两份目标保持冻结。

## 5. 正式全局报告的追加独立范围审查

随后实际 FULL 读 research/research_global_review_round248_20261010.md，全部四节，7851 B，SHA256 0efe88842e82a1b6cec326a9d753ace0187ebc53a6b049b399e42879b9a825c1；工具核保存身份一致。结论 **PASS，无须修改**。

报告准确把全图 cap 限于原 x、完整五行、当前五行两列安全数组与基本单实处入口；没有将安全费用当最优算术下界。新商的真坐标、actual rank3/nonrecovery/rational forcing/prefix 是已付资产，全叶、共轭图及严格全place预算仍标未付。K 系数共轭不被偷换为未知周期共轭，也没有将双 canonical 补点矛盾误当 g+∉K 已证。其它后备的有限层/条件证书没有被当成宏观收益或新数值定理。

唯一249–250准入明确要求生成元周期系数与完整数域/全部嵌入预算，未重复分配原图或素数优化窗口；两轮不缩小核心缺口即停止，252正式复盘、248重置与目标active/新数值false一致。该决定不预领准入成功。

本追加审查针对完整报告的结论范围和上述本人数学审阅输入；历史路线表、C新Schur原推导、仓库 fresh metadata、其它同伴的文献读域是报告所引用的已登记输入，本人不以此次范围审查冒称重审其全部证明、仓库或下载程序。不新增 primary、不运行数学程序、不写任何其它文件；现有 B 主稿与 scope 及三份目标保持冻结。
