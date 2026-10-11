# 同一配对构造：主率、全素数费用与有限域 normality 的根独审

日期：2026-10-06。本文件是对三份同行 NEW 数学稿的实际纸面独审；root 自己的 primitive gcd 主率稿另由 quarter 独审，不将自审计为独立复核。所有旧及同行数学程序只读，未 execute/import/rerun。

## 1. 最终输入与实际读取

以下最终主稿的数学正文均实际完整读取、输出无截断：

|同行主稿|最终 SHA256|本轮读取说明|
|---|---|---|
|`cdt_odd_paired_plucker_energy_rate_20261006.md`|`01c87202a292f9d977f58098bd609e99f9b6aa1b6701e9fff7c036bda7e2515a`|初稿全文，修订稿全文，最终 E1–E8 及公式 E1–E26 再次全文回读。|
|`cdt_odd_paired_all_prime_budget_20261006.md`|`55278a0ed68b645fc5cb2f3089563e49c30e608ace9de511cc80d37609b712dc`|前版 `98cf2cef92b2ff5594eba17da406443e0632c5677a1dd9e917afed8fe78bccf5` 全文 B2–B22；最终两处新增 B15 coarse60、B18 gcd 接合及周围文本实际补读。未声称最终全部字节又逐行重读。|
|`cdt_odd_paired_auxiliary_units_structure_20261006.md`|`dcc6d4d670dbcc3960936d3ee1b21a877f73c03e2ba65c479c9d550e0624a8a5`|候选全部数学与最终格式修订稿 §1–11、U1–U35 两次完整实际阅读。|

静态全文读取作者已经保存的源与证书：解析 failed-v1 PY `cd43f0cd2965be81f0ad9f077771322f849f4460e2ed5f29d1ea29e29011f129`；单独 v2 PY `ce447f4de73324241725208131be73aea61ef5c5fe44ee044f72fa076b88f3e1`、JSON `49e3cb42c8c9ddbc8c4ab71b70bee4ebbbf693f4921615330d0a4dbc40b748d8`；预算 PY `01b4970d7d634f2dc5376bce974d3755e7694c1f8a6defec68230aa86f784a95`、JSON `7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b`；结构 PY `b445ebd6b1d52eb1a73fbc4aa003542aa7fb11f9f6ab2551e06fa2ed9a5910c5`、JSON `cc3417ecff851db9aa7a0b37cf38d7e13f114cb8db8e2dab67de643cbdd0e884`。预算全部50仿射段、结构全部40案例表均实际完整静态读取。这不声称人工重算全部有限表或重新执行程序。

本轮 root 独立来源实际读域为 Rimányi–Varchenko PDF1–8 共8页；Dominici、Rosengren root 只核元数据/摘要，不称全文或正文阅读。NIST 5.4(ii)/5.4.19、5.7(ii)/5.7.6、27.12 的相关官方网页结论实际读取；保存三个原始 HTML，不称完整 markup 全文阅读。来源适用条件另见结构稿 §9 与本轮 receipt。未新增外部仓库源码、Lean 编译或核验。

## 2. 解析主定理：完整基的费用已经匹配

保持原 B6/k3/s5、ambient degree<3n、实际 rank2n 饱和 paired Newton 格及固定目标 ξ=aζ(4)+bζ(5)，b≠0。根独核确认：

1. 高块准确为 Δ(z)∏S(z)/∏(2n+k)!；低块为逐镜像节点选择的 Cauchy determinant。κ 的分母含 **(j−1)!²**，且每项共同含 Γ_n^{-1}。
2. 有限 Laplace/L² 展开常数是一个 binom(2n,n)，选择和的粗化另付4^n，两者只属 O(n)。没有删掉 n² 阶 symmetric degree。
3. 真实 Hardy 核积分为2π/(δ_i+δ_j)，Loewner determinant 单调与完整 Cauchy product 给统一负能量 c_H=9log3−8log2−4>0.3423。正 Gram 仅给原复 determinant 上界，不证明其非零。
4. 高 Vandermonde 用精确实恒等式 `(1+y²)(1+y'²)−(y−y')²=(1+yy')²`，可去掉此前多余因子2。此修订只改变纸面安全上界；既有首次 β0 区间证书保持原参数定义，无需重跑。
5. L_n^n、Z_H、κ²、F_n^{-2} 的 n²logn 系数依次4、5、−4、−5，完全消去。共同 weight 的 uniform midpoint/Stirling 误差、固定 cot 导数指数尾、所有 factorial 与基增长均付费。
6. 两个 saddle 的唯一性和无机器 β0>7.1 证明通过。v2 rational certificate 只认证两根与 β0 数值，未替代所有 n 的 E2 纸面证明。

因此同行的全尺度定理通过：

\[
\log|D_{A,n}(\xi)|\le-\beta_Hn^2-2\log\Gamma_n+O_{a,b}(n\log(n+2)),
\quad\beta_H>8.59403839512558.
\]

与 root 最终 gcd 稿的 γ∈[1.455845,1.457795] 接合，得到同一对象的 limsup≤−β_H−2γ，严格主率 **β_H+2γ>11.50572839512558**。quarter 对该 gcd 稿全数学、源与证书的独审已实际读取：`cdt_odd_paired_primitive_gcd_rate_independent_review_20261006.md` SHA `9257bbfcf1f52916b460497ed0cb9a14425040382006a4b0b39646f44a718ad2`。root 不把自己 gcd 命题再记一次独立核验，也不把 Γ 的同一信用重复当有限 place content。

## 3. 全素数形式整模型：安全费用界确为全部系数的界

预算 B4–B16 数学核准。入口 −10n floor(log_p8n) 为实际整数值基的整 entry 界；p>6n 的独立 integrality 包括6n..8n 的 carry，不能省略。大素数模型只在√8n<p≤6n；小素数费用 O(n^{3/2}logn) 另付。

真实 rank2n monomial-minor 共界 Λ 经两侧 Newton 转换付 `2Σ_{i=n}^{3n−1}v_p(i!)`，没有借低 degree 的 factorial。signed ℓ_p 保留正 valuation，整个 D_A(X)/Q_n∈Z[X]；未称 Q_n 为 actual primitive content。

连续模型的 max(g_raw,−10) 是两个合法 valuation lower bounds 取强者。0<x≤1/4 恰为−10，避免未经支付的 −1/x 积分；47 base breakpoints、capacity/cap 根给50全覆盖仿射段。PNT 与 uniform O(1) 整数 allocation 误差正确转成全尺度 liminf，而不是有限 n 拟合。

\[
\liminf n^{-2}\log Q_n\ge-\frac{1085983123}{24190320},
\quad A_{\rm pair}^{\rm safe}\in[44.893,44.894).
\]

coarse60 的素数幂尾 O(√n logn) 核准；新 bound-model 安全费用改善>15.106。此费用上界仍高于目前解析下界，**既未得到正 margin，也不能反过来证明 actual cost 必高或整个方法失败**。

B17–B22 的进一步接口通过：T_p=max(e_I−v_p(u_I)) 是实际 wedge denominator，整数 unitriangular falling 转换不改变它；全素数桥可强化为 max(−10n,Λ−2T_p)。当前证书没有计算 T_p 主率，不能先扣其收益。ψ=(t^p−t)/p 的双层 binomial 基在 degree<3n<p² 范围有 p-unit leading ratio，确为 GL(Z_p) 整数值换基；ψ(a+pY)≡ψ(a)−Y、pψ'≡−1 的 leading-jet 接口合法。实际 full rank/Smith 提升尚未证明，不能免费替代旧 minor 费用。

## 4. 辅助矩阵：全尺度结构已证，截断非退化仍是实质缺口

结构稿的 p=18r+1、n=4r 真 half jet 和 middle multiplicity 完整保留。U7 Wilson 符号、U10 full/middle coefficients、U12 交叉项、U29 residue 负号、U30 单一有限域 power-sum 指数逐项纸面核准。

P S=u^{9r+1}−u 给 squarefree 互素因式与真正 middle CRT projector χ。U18 分子 g,c,h 和 U20 inverse 经 χ=0/1 两支独立核对正确；这是整个 CRT 代数的 perfectness，不是截断 Gram 的 nonzero。

U21 高 descending 余式 coefficient 到 Laurent 矩的矩阵是 diagonal1 下三角，故 scalar 和 matrix determinant 恒等式 U22/U26 没有漏行反序符号、scalar 或 normalization。U23 与 U27/U28 给原两 determinant 为零的精确 degree-profile 条件。该转换把无限 unit 缺口明确落成 profile(r,3r) 的有限域 Padé normality；没有证明 normality 本身。

middle scalar Gram 的 rank 恰为r；joint middle 也恰为r，随尺度增长，不能当有界秩扰动。逐点 Pearson 最小 class full5 / actual7（r≥2）的证明核准：内部零点数足以强制 polynomial identity，互素性给上端点根阶5，实际 flux 再加至6，下端点加1，真实两跳变再各加1；所需根在 F_p 互异，相关比值均为 unit。最高 coefficient83/9、101/9 在 U1 素数上非零。该最低 class 限于指定全局 pointwise polynomial Pearson pair，不排除 rational gauge、新 lattice、矩阵正交多项式或新的表示。

自有 structure first-only probe 的40素数19..1621、最大 joint dimension360，全 G0/M5 unit，是有限证据。它未验证本稿全部 CRT/Pearson 纸面命题，未证明无穷 unit。Selberg/Hahn 文献的具体权重、指数范围及 balanced 条件尚未匹配，不能直接借乘积公式。

## 5. 执行与进展判定

本轮各作者 NEW 数学执行合计5：root gcd1成功、quarter 原 v1 首次1失败（数学 assertions 后遇输出大整数字符串限制，保留源码、无 JSON、不记 PASS）加不同 v2 首次1成功、toric budget1成功、arithmetic structure1成功。成功4、失败1；任何旧/同行 execute/import/rerun0、Lean0。静态独审和文件指纹检查不是数学程序执行或形式化认证。

本轮属于有全尺度纸面命题和交叉审阅的研究进展。尚需至少两项独立 gate：无限辅助 Padé normality/nonzero；同一 determinant 上足够便宜的 actual 全素数费用或更强解析界。当前没有新的 ζ(7)、ζ/L 奇数值、Catalan 无理性或线性无关性定理。

下一轮优先由 B21–B22 真整数值 ψ 模型证明实际 residue/jet rank 与 Smith 层，争取 n² 级全素数节省；同时对保留 χ 的 U23/U27 研究 explicit determinant/normality。仅扩大有限 prime 表、删除 middle、重复 common gcd 或挪用 restored-k4 energy 均不填补上述 gate。
