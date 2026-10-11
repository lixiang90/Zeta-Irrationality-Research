# 实际反不变强迫实结构稿：独立全文纸面审查

2026-10-07。审阅者 /root/masked_racah_finalize；作者 /root/scaled_root_finalize。唯一 NEW 正式独审。被审最终稿为 research/cdt_odd_gamma_anti_forcing_real_projection_20261007.md，SHA256 fe200cc00791575957ac5e96109728b80aa6aefed1b7bc2e2f5a403652d96095，24812 bytes，九节 R1–R29。本人实际 FULL 读取全部正文后，独立核查下列证明；无正文纠错请求，结论 PASS。PASS 指本稿明确范围内的结构证明，并非任何新常数的无理性或线性无关性。

## 1. 实际读取的输入与所审对象

**V1。** 本轮实际 FULL 读取被审稿全部九节，以及三份冻结直接输入：

- research/cdt_odd_gamma_connection_projection_20261007.md，SHA0bb53d928dbc925dadce1e7dd2c4a1bdd148af0e7c81be4659070aeb893fff44，18401 bytes，七节 G1–G19。
- research/cdt_odd_gamma_quadratic_antiinvariant_extension_20261007.md，SHAc0a492603f559ed92b08fb685f79284ab3daf5feb9e10c52daf2ae1ea101ba27，26211 bytes，十节 A1–A29、公式 A1–A49。
- research/cdt_odd_gamma_dual_relation_extension_20261007.md，SHAf8e36b1bf0b605d73574e556bc9cc382a944a07523b74dc5d12a5b64446208ab，18371 bytes，七节 D1–D17、公式 D1–D30。

以上读取都是完整最终正文，没有执行其中提及的 producer、WZ notebook、guard 或数学结果文件。原件读取与指纹范围见第八节。未声称本轮重审全部 612 冻结记录。

## 2. 共轭方向与积分收敛的逐式检查

**V2。** R1–R5 保留了同一整数坐标、完整 Frobenius basis、系数列上的反射矩阵与指定 bridge。由 dt/t-adjoint 的 D*=-D、参数关于 1/2 对称，完整输入 D3–D8 的 Green pairing 给 S、d=16π⁸/5、v=-2Sκ/d 与 κᵗv=-2；此处不需要把 Frobenius basis 当成 Betti 整格。

正向小环从 c 左侧出发，第一半环位于下半平面。故 lower path 接 upper path 的逆向为正向环；沿 upper boundary 的反射差确为

\[
\phi_j^- -\phi_j^+=\kappa_j\psi^+,
\qquad \psi^+=f_0^- -f_0^+=-2i\operatorname{Im}f_0^+.
\]

实系数和实初始 germs 给 lower=conjugate upper，所以各虚部均为 κ_j 倍同一方向，R8–R9 的符号通过。P∈tR[t] 在 0 抵消 dt/t 的简单极点，完整 basis 至多有限 log；c 的 7/2 指数使 solutions bounded；b 的 w 只有平方根零点。这些给 R10 的实际 improper 收敛及半圆积分趋零。对实 P 取虚部后，J_c=-2iβ 的全分量身份 R12 通过，范围确限实强迫与该 bridge。

## 3. 实比较矩阵、完整 MUM 门与有理分裂

**V3。** 本人完整检查冻结 A3–A6 的 rational image：ordinary b 的半整数指数在施行九阶算子后必须使 q 在 b 消失至少九阶；0、c 的负整数指数及其余 ordinary poles 均不允许；∞最高项使 degree 精确增加一，故商恰九维并有 [t]至[t⁹] 的有理 basis。完整 A17–A21 同时使用实际 finite generating loops 和 ∞ moderate growth，将全部九个比较 gate 的 kernel 证明为该 rational split image。被审稿 R13–R14 因而没有漏付全局分支。

R12 使 real comparison 的零空间恰与 complex comparison 的实零空间一致；九维性遂给 R16 的实同构。逐行复矩阵转换

\[
M=\begin{pmatrix}I_8&i\kappa_{<8}\\0&-2i\end{pmatrix}N
\]

准确，故 det M=-2i det N，而非另一个相位。完整 MUM fixed space 为 C f₀，R19–R21 的全部八个条件 I₀… I₇=0 不依赖所减 u。实 P 时 I₀=0 已迫 β=0，再迫 J_c=0，故 R22–R23 的完整填 MUM 迫分裂成立。有理 P 的 q 为有理，来自唯一 triangular 解，未从 real comparison inverse 免费推出。

## 4. 真实反射实形式与实际十行秩

**V4。** h_j=2(-1)ʲI₈₋ⱼ 与 Sκ 的分量逐项给 Im h=-dβv；κᵗv=-2 给 Im η=2dβ。z=h-2C_Pe₀ 满足 κᵗRe z=0，且

\[
T\overline z=\overline z-2id\beta v=z.
\]

所以 fixed real space 正好为八维 +1 方向和一维纯虚 -1 方向，R25–R27 无符号错误。它是实形式而非免费有理格，R13 的边界明确。

拉回的 index-two subgroup 通过乘 ordinary b-loop 得到与原群相同的 monodromy image，R14 的 irreducibility 不是一般 finite-cover 断言。对任意实 nonsplit P，R22 保证指定完整 MUM jump 非零；其 orbit 因不可约张成九维 homogeneous space。rational-coefficient order≤8 算子不能杀全部九个 independent ordinary solutions，故 R28 的十行实际函数秩通过。相同 orbit 与 Ore division 给 minimal scalar order 恰十，而不是仅由存在十阶方程推断。

## 5. 完整线性微分投影与较少门的边界

**V5。** 任一有理线性微分算子 A 若杀该完整 jump，continuation 使它杀全部九维 homogeneous space。按 L_pb 右除后的余式阶数小于九，必须为零，故 A=UL_pb，且 AF=U(wP) 为有理函数。此论证也覆盖 A=0，不排除 nonlinear tensor、换 base 或不同 leaf。constant Euler polynomial 的特例在 r₋ 为 ordinary scalar equation，无法同时含有 f₀ 的非零反射 jump，R18 对任意 degree 的论证通过。

R32 的实 codimension 逐项来自 N 的独立行及共同 β：只有至少一个所选 κ_i 非零时才多一个条件；没有声称全部 odd κ 非零。R33 的 Q⁹ 交 real kernel、R35 的低 log 空间和 R38 的 rational line 条件均准确保留 arithmetic gap。特别 I₇=1、其余前七项零且 β=0 给 h₁=-2、h₀=2C_P，故完整跳跃 -4πif₀ 的符号正确。正 Euler measure 又使 β(t²)/β(t) 严格处于 (c,b)，但其有理性没有被证明；R39 的 degree-two 接口通过。

## 6. 全有限处 Taylor 与 CDT 费用

**V6。** q-layer 在 q|m 时 C_q(m)=0，避免将两个独立最差估计误加；q>n≥m 时 floor 表达随 index 单调。因此 D_n⁹ h_n/(m⁹h_m) 的全部 primes 整性成立。w 的整数 Catalan Taylor、整数代换 x(1-x) 与 δ 的整数 Taylor multiplier 同时保留 fixed P/u 分母及有限阶 jets，R40–R41 未使用辅助素数表。

本人实际核 CDT v2 PDF66–69。十行按九个 width-one columns 的 whole-array 计算 σ=(0,9,…,9)，e=0，τᵇ=9(1-10⁻²)=891/100。holonomic 情形允许导数门槛 e^τ，但仍须实际 meromorphic 全 pullbacks。R42 是安全预算 upper，不是最小费用或 strict-margin。正文明确保留 canonical branch 与其他 transported germs 的区别，没有把一条 MUM gate 分类推成所有映射必须遗漏该点。

## 7. 审查结论与保留的缺口

**V7。** 全部 R1–R29 在所述范围通过。本轮实质加强是：实强迫下指定完整 MUM 填洞已迫 rational split；全 signed real nonsplit 类的实际十行秩；杀该完整 jump 的 rational differential projections 只输出 rational functions；以及较少比较条件的准确 Q-intersection 接口。比较同构、positive moments、低 log line 和 rank10 都不推出新 ζ/L/C_P 无理性，正文对此没有越界。无修改请求。

## 8. 实际原件页域与最终自读纪律

**V8。** 本独审实际 FULL text 读取既有 Golyshev–Mellit arXiv0902.2003v1 PDF1–3，SHA239c64b8bab41b12bc2a41d8eb3630d2935e04365bf6a3b9919193793551fc20，171695 bytes、10归档页；PDF2 的 irreducibility、pseudoreflection、unique Jordan block 与原参数相匹配。实际 FULL text 读取既有 CDT v2 PDF66–69，SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771，4517169 bytes、218归档页，用于第六节精确 array 接口。独审 primary scope 为七个不同 PDF 页；和本轮本人 Koutschan–Zudilin PDF1–6 合并，个人本轮共十三个不同 PDF 页，不继承作者或以前轮次的页数。

Gamma 行及 Green 常数另依本轮实际 FULL 冻结 G/D 正文，并核其明列的有限代数式；未冒称重新读取 Bloch–Vlasenko 全文或原命题页。本轮没有新下载用于此 review，也没有 render、数学 producer 创建/execute/import/rerun、prime 扩表、guard 或 Lean 执行。审稿保存后须实际 FULL 审阅者回读并核验最终字节，才发送指纹；不 pin 同行收据、mutable 总稿或未来 audit。
