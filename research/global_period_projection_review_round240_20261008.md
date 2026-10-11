# 第240轮：固定 M₀,₁₀ 周期投影的首证书与精确 Euler 障碍

2026-10-08，C。目标仍是新的 ζ/L 数值结论。本轮重审原 F、ω 与十一通道 motivic ambient，核对239的 D₃判据，并对一个新的一手奇维 primitive 机制作同对象检验。结果是：该机制不能直接移植；原 ω 的全 n D₃证书仍未支付，亦未被反驳。数学程序、参数扫描均0。

## 1. 固定原对象与真正要证明的命题

令 0<t₁<⋯<t₇<1，固定
\[
D=(t_3-t_1)t_3t_5(t_5-t_2)(t_7-t_2)(t_7-t_4)(1-t_4)(1-t_6),
\]
\[
F=\frac{t_1(t_2-t_1)(t_3-t_2)(t_4-t_3)(t_5-t_4)(t_6-t_5)(t_7-t_6)(1-t_7)}D,
\quad\omega=\frac{dt_1\cdots dt_7}D,\quad I_n=\int F^n\omega.
\tag{C1}
\]
配置为 (10,2,4,1,6,3,8,5,9,7)。237已付全 n 收敛及十一通道 motivic 包含性；本轮实际 FULL 复读该稿，未把其一般 mixed Tate 容器升级为秩四。

以 z_j=ζ(j) 的 motivic 版本记，ambient 基为
\[
1,z_2,z_3,z_2^2,z_5,z_2z_3,z_3^2,z_2^3,z_7,z_2z_5,z_2^2z_3.
\]
Brown 2012 的 infinitesimal coaction 是 derivation，偶 ζ 在左 unipotent 因子为0，奇 ζ primitive。因此239的式子准确为
\[
D_3I_n^{\mathfrak m}
=z_3^\ell\otimes
\big(c_3(n)+c_{23}(n)z_2^{\mathfrak m}
+2c_{33}(n)z_3^{\mathfrak m}
+c_{223}(n)(z_2^{\mathfrak m})^2\big).
\tag{C2}
\]
其它七通道在 D₃下为0。由 motivic 基独立性，
\[
D_3I_n^{\mathfrak m}\in
\mathbb Q z_3^\ell\otimes z_2^{\mathfrak m}
\iff c_3(n)=c_{33}(n)=c_{223}(n)=0.
\tag{C3}
\]
这不使用数值 period map injectivity；也没有证明原 I_n 满足左边。即便全 n 证出(C3)，z₂²、z₂³两个禁止 Tate 坐标仍须另付。

长度3 cut 公式能检验已获得的标准 iterated-integral words；它本身不将高 pole 的 Fⁿω 转成全部 n 有效的 words。需要 relative reduction 连同边界项及 motivic lift，或一个确实作用在原相对类上的 projector。数值 I₀ 的有限头公式不能认证这些 motivic 坐标。Brown 2014 PDF34的本配置消失现象仍标为 experimental；其 Theorem11.2 的 cellular-divisor 假设不能从本配置名称领取。238已证明标准对偶同余观察不到全部五个禁止通道，并给同 F、不同 η 的精确反例；本轮没有将它误写为原 ω 的反例。

## 2. 新 primary 的奇维机制究竟是什么

本轮新增 Tosi 的 arXiv:2601.00346v2（2026-03-19）。实际读完整 PDF1–3、6–9，特别 Lemma9 的完整证明。其对象是
\[
\xi_l=\int_{[0,1]^l}\frac{dx_1\cdots dx_l}
{\prod_{i=1}^{l-1}(1-x_ix_{i+1})};
\]
论文明确把它限定为所有参数函数 fᵢ=1的族，并指出严格的 cellular 配置解释只在 l 偶数时成立。该对象不能只因 l=7 或在同一 M₀,₁₀就当作(C1)。

其 primitive 有一个可直接核查的微分解释。设
\[
Q_{\rm adj}=\prod_{i=1}^{l-1}(1-x_ix_{i+1}),\quad
V_{\rm alt}=\sum_{i=1}^l(-1)^{i+1}x_i\partial_{x_i},\quad
\omega_{\rm adj}=Q_{\rm adj}^{-1}dx_1\cdots dx_l.
\]
每个 xᵢxᵢ₊₁的 V_alt 权重为0，故 V_alt(Q_adj)=0；其 divergence 是1或0，分别对应 l 奇或偶。Cartan公式于是给
\[
d(\iota_{V_{\rm alt}}\omega_{\rm adj})
=\begin{cases}\omega_{\rm adj},&l\text{ 奇};\\0,&l\text{ 偶}.\end{cases}
\tag{C4}
\]
这正是 Lemma9 的显式 primitive，而不是从 Grothendieck period conjecture 推出。本文采用并纸核(C4)；未读其全部闭式求值证明，也不将该论文的 conjectural interpretation 当作定理。来源：[Tosi v2](https://arxiv.org/abs/2601.00346v2)。

## 3. 原 ω 的完整 cubical 形式

取 xᵢ=tᵢ/tᵢ₊₁，1≤i≤6，x₇=t₇。正 Jacobian 为 t₂⋯t₇。定义
\[
\begin{aligned}
q_1&=x_1x_2,&q_2&=x_2x_3x_4,&q_3&=x_2x_3x_4x_5x_6,\\
q_4&=x_4x_5x_6,&q_5&=x_4x_5x_6x_7,&q_6&=x_6x_7,\\
Q&=\prod_{j=1}^6(1-q_j),&&P=x_2x_4x_6.
\end{aligned}
\]
逐因子代换给 D=t₃²t₅²t₇²Q，因此原对象精确变为
\[
\boxed{\omega=\frac P Q\,dx_1\cdots dx_7,\qquad
F=\frac{x_1x_2^2x_3x_4^2x_5x_6^2x_7\prod_{i=1}^7(1-x_i)}Q.}
\tag{C5}
\]
这是原 ω，不是另选的η，也未用有限数值头推断坐标。

令 a=(a₁,…,a₇)∈ℂ⁷，
\[
V_a=\sum_i a_ix_i\partial_{x_i},\quad
w_j=\sum_{i\in\operatorname{supp}q_j}a_i,\quad
A(a)=\sum_i a_i+a_2+a_4+a_6.
\]
由(C5)及 volume divergence 得完整身份
\[
\frac{\mathcal L_{V_a}(F^n\omega)}{F^n\omega}
=(n+1)A(a)-n\sum_i\frac{a_ix_i}{1-x_i}
+(n+1)\sum_j\frac{w_jq_j}{1-q_j}.
\tag{C6}
\]
没有遗漏 volume、P 或 F 的贡献。顶形式闭合，故左端也等于 d(ι_V(Fⁿω))/(Fⁿω)。

**C5（固定对角 Euler primitive 的精确排除）。**
对 n=0，若 d(ι_Vω)=cω，其中 c 为常数，则 c=0，且
\[
V=b(-x_1\partial_{x_1}+x_2\partial_{x_2}-x_3\partial_{x_3})
\tag{C7}
\]
为全部可能的 V。对每个整数 n≥1，若
d(ι_V(Fⁿω))=cFⁿω 且 c 常数，则 V=0、c=0。

证明：在 Laurent torus 中，六个 1−qⱼ是不同的 irreducible divisors。若(C6)是常数，在每个 divisor 的 generic point，其余分母均可避开；n=0时对应 pole 的系数迫 wⱼ=0。六个线性条件依次为
\[
a_1+a_2=0,\ a_2+a_3+a_4=0,\
a_2+a_3+a_4+a_5+a_6=0,\
a_4+a_5+a_6=0,\
a_4+a_5+a_6+a_7=0,\ a_6+a_7=0.
\]
由第三减第二得 a₅+a₆=0，第四得 a₄=0，第五得 a₇=0，第六得 a₆=0，继而 a₅=0，余下恰为(C7)。此时 Σaᵢ=−b，P 权重为 b，故 A(a)=0，c=0。六 binomial 的 exponent vectors 均 primitive且不同，这也直接验证所用 irreducibility与generic-pole分离。

n≥1时，先在各 1−xᵢ的 generic point 看(C6)。它们与全部 1−qⱼ及其它 1−xₖ不同；系数 −naᵢ必须为0，所以所有 aᵢ=0。证明完毕。

作为直接校准，Tosi 的 V_alt 对原 ω 给
\[
\frac{\mathcal L_{V_{\rm alt}}\omega}{\omega}
=-2-\frac{q_2}{1-q_2}-\frac{q_3}{1-q_3}
-\frac{q_4}{1-q_4},
\tag{C8}
\]
并非1。保留原 Q 的唯一非零 Euler方向(C7)在 ω 上闭合，乘 F 后又有
\[
V(F)/F=b\left(\frac{x_1}{1-x_1}
-\frac{x_2}{1-x_2}+\frac{x_3}{1-x_3}\right),
\]
不是常数。这说明两个具体失配：原密度的 numerator 消去 divergence；真实参数函数又引入单坐标 pole。

此结论仅排除该坐标上的固定对角 Euler contraction/parity 方法，甚至逐 n 的常数 eigenform亦失败。它不排除非对角 rational vector field、relative-boundary projector、完整 coaction cancellation或更强 contiguity。尤其它没有证明(C3)为假；也不能从一个 absolute exact primitive 的不存在推断 relative period 的禁止坐标非零。

## 4. 投入判断：先支付什么，不能互借什么

| 路线 | 已付结构 | 首个未付证书与本轮判断 |
|---|---|---|
| 固定 M₀,₁₀ | 全 n 真实积分、十一通道、(C2)–(C3)，以及本轮(C5)–(C8) | 全 n 原 relative 类的 D₃右因子只落 weight2；仍是 conditional reserve。没有理由从 Euler 方法失配回到 generic秩四或有限头扫描。 |
| 同 cellular 包的混合 determinant | 若六通道已付，可形式消 ζ₅ | 必须指定真实 ζ₇系数并证明无限非零、完整分母与投影后次主渐近；全 I_n正性/衰减不能迁移。当前不能作为已付纯 ζ₇源。 |
| Catalan integer-period projection迁移至 c₄ | 236实际源码已读的 integer contact、全pool格、独立非消失及同对象实界 | 新 c₄矩阵仍须全entry周期身份、实际整数 nuisance-kernel 与保留目标rank；旧 G seeds/二次费用不可继承。保留真正增长的mixedkernel入口，停止固定背景填branch的旧提案。 |

239实际 selected-cofactor 全尺度 upper的改进仍是成果，但其安全费用
21/2−log12不能跨过239已付固定共同BC证书类的紧全图门槛。该判断不是 actual费用lower或全部CDT no-go；本轮不再延长原源的无界 prime优化。本文仅复核239最终门槛稿的实际范围，没有冒充另一次全部局部整格证明。

相较一般 motive/rank论述，下一项有价值的输入必须改变原函数的精确周期通道或实际整数投影。对本 M₀,₁₀仅接受一份可终止的原 relative telescope/cut证书：展示边界的 motivic lift、全部非负整数例外和足够的 motivic 初段，才能用已证递推归纳全 n。未得到它，就降为条件后备。新的 whole-functional 机制须由其真实原件与函数身份单独认证，本文没有预领尚未读的其它候选。

目标未完成：没有新的 ζ₇、c₄或其它 ζ/L 数值无理性结论；既有数值定理也不作为本轮成功目标。

## 5. 实际阅读与运行范围

本轮 FULL 读237固定源准备稿、238投影准入稿、239门槛稿及236本人的 Catalan比较冻结稿；完整选读 Brown2012 PDF8–11、Brown2014 PDF34–35、Brown–Zudilin v3 PDF29–30。后者两页的有限头不用于认证原 ω 的 motivic 坐标。

新 primary 只保存 Tosi v2一份PDF，实际 FULL 读三个TXT选段，合计物理PDF1–3、6–9；不声称FULL整篇36页。初始网页曾落到v1，发现版本差异后不采用其公式；最终采用已存v2及其日期/更正声明。未重新读取外仓库源码或认证当前remote，Catalan架构依据本轮FULL复读的236原始阅读报告。数学运行、扫描、旧producer、Git/Lean执行均0；文档抽取三次，不计数学运行。最终保存作者FULL复读与身份另报；不冒充独审。精确版本见[本人scope](../literature/global_review_sources_round240_20261008/dual_reading_scope.md)。
