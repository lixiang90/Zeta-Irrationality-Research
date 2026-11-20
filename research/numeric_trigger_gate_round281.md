# 第281轮独立竞争：Z₅图周期的纯目标正Gram与实际端点速率

2026-10-20，作者 `/root/numeric_trigger_281`，唯一写本文件。子代理 goal 工具返回 null，未另建 goal；根的实际运行状态由根核定。已运行状态工具，读 AGENTS、长期 goal、修订21的 STATE、281章程、279正式比较、280结算及周期竞争稿；初始工作树为空。随后定向检索到已有 canonical W₇ 变形，实际读其 V1–V15 及原215范围，避免重复领取旧结论。本稿没有参数、素数、系数或图族扫描。

**决定：没有数值实施准入。** Z₅ 给一个不同且真实的正收敛纯 ζ7 周期；取 Symanzik 多项式本身为坐标后，确能构造全规模正定、只有一个条目含 ζ7 的实际 Gram。它没有280的固定jet秩障碍。然而，同一对象的 Schur 余项有全规模多项式下界，裸指数率恰0；所有本原整系数线性输出也不可能取得严格负线性或二次指数。正性和纯目标投影不支付余项速度。此范围不排一切次指数方法，也不排不同有理权。

## N281.1 目标、完整反证和实际新输入

保持指定实目标 ξ=ζ(7)∉Q；完整反证是 ξ=u/v，u∈Z、v>0、gcd(u,v)=1。最终若使用线性整数输出 A_m ξ+B_m，须同一预定无界子列上实际非零，并对每个固定 v 有 v|A_m ξ+B_m|→0。严格负指数是充分接口；不能把不同归一化的行列式大小和本原系数费用拼合。

一手输入是 [Brown–Schnetz, arXiv:1208.1890v2 §1.1，(1.1)–(1.2)、Theorem1.1](https://arxiv.org/html/1208.1890v2#S1.SS1)：Z_n 有2n条边，其正取向 projective period 为 ∫Ω/Ψ²，收敛且等于

\[
4\frac{(2n-2)!}{n!(n-1)!}
\left(1-\frac{1-(-1)^n}{2^{2n-3}}\right)\zeta(2n-3).
\]

因此 **Z₅ 是10边、6顶点、5 loop、实9维单形上的 period**，不是 canonical W₇，也不是其形式指数13的密度：

\[
I=\int_\Delta\frac{d\alpha}{\Psi(\alpha)^2}
=c\xi,\qquad c=\frac{441}{8},\quad
\Delta=\{\alpha_e\ge0:\ \sum_e\alpha_e=1\}.
\tag{N1}
\]

这里 dα 是正取向的九维 Lebesgue 单形测度，体积1/9!，与 Ω 在 sum=1 图上的归一一致。纯目标系数441/8由上式 n=5 直接算出。本稿不重证外部的 period 评价及全部收敛定理。

为完全固定图，取 C₇(1,2) 删顶点0。原始定义和“decompleted C_n(1,2) 是 zigzag”实际对照 [Yeats, A few c₂ invariants of circulant graphs, §1 Definition1.1、§3首段](https://intlpress.com/site/pub/files/_fulltext/journals/cntp/2016/0010/0001/CNTP-2016-0010-0001-a003.pdf)。顶点1,…,6，标边

\[
\begin{split}
(a_1,\ldots,a_5)&=((1,2),(2,3),(3,4),(4,5),(5,6)),\\
(b_1,\ldots,b_5)&=((1,3),(2,4),(3,5),(4,6),(6,1)).
\end{split}
\tag{N2}
\]

实际 Ψ 定义为 ∑_T∏_(e∉T)α_e，T 遍历该图的 spanning trees；每个系数为1，degree5。等价的有限矩阵证书是

\[
\Psi=\det(C\operatorname{diag}(a_1,\ldots,a_5,b_1,\ldots,b_5)C^t),
\quad
C=\begin{pmatrix}
-1&-1&0&0&0&1&0&0&0&0\\
0&-1&-1&0&0&0&1&0&0&0\\
0&0&-1&-1&0&0&0&1&0&0\\
0&0&0&-1&-1&0&0&0&1&0\\
1&1&1&1&1&0&0&0&0&1
\end{pmatrix}.
\tag{N3}
\]

前五条链边是 spanning tree，五行是 fundamental cycles。Cauchy–Binet 的非零平方 minors 恰为 complementary spanning trees，均为1；故 N3 自足核对了所用 Ψ，而非一个未指明的图积分。

## N281.2 不靠cohomology猜想的纯目标正Gram

令 S=∑α_e，实际 projective 坐标 t=Ψ/S⁵；在 Δ 上 t=Ψ。由于 Ψ 是 squarefree degree5 且系数1的 monomial 子和，

\[
0<t\le e_5(\alpha)\le S^5/5!=1/120
\quad(\alpha\in\Delta^\circ).
\tag{N4}
\]

取正有限测度 dµ=Ψ⁻²dα，并记 µ_k=∫t^k dµ。关键不是说“图只有一个 period”，而是以下真实消分母身份：

\[
\mu_0=c\xi,\qquad
\boxed{\mu_k=\int_\Delta\Psi^{k-2}d\alpha\in\mathbf Q\quad(k\ge2).}
\tag{N5}
\]

µ₁ 没有被假设有理；必须跳过一次幂。固定 m≥1，基为

\[
p_0=1,\quad p_i=t^{i+1}\ (1\le i\le m),\qquad
G_m=(\langle p_i,p_j\rangle)=
\begin{pmatrix}c\xi&b_m^t\\b_m&H_m\end{pmatrix},
\tag{N6}
\]

其中 b_i=µ_(i+1)、H_ij=µ_(i+j+2)，全属Q。t 在开单形上非恒定，像包含非空实区间，dµ 在其上为严格正密度。因此任何非零基多项式的平方积分正，**G_m 对全部 m 正定，rank=m+1；H_m 也正定**。这是全规模实际非零，不从形式函数秩或有限样本推出。

ζ7 系数矩阵恰为 c e₀e₀ᵗ，rank1。N5 的全部背景已真正移除，不调用“单一 masterperiod”猜想。Schur 补给

\[
\det G_m=\det H_m(c\xi-r_m)>0,\qquad
r_m=b_m^tH_m^{-1}b_m\in\mathbf Q,
\tag{N7}
\]
\[
E_m:=c\xi-r_m=
\min_{q\in\operatorname{span}(t^2,\ldots,t^{m+1})}
\int_\Delta|1-q(t)|^2d\mu>0.
\tag{N8}
\]

这确实给同一纯 ξ 的有理逼近，不是把图 period 表示误算成逼近。又取 x=t/T、T=1/120 及 P_m(x)=(1−x)^m(1+mx)。它在[0,1]介于0与1，constant为1、linear系数0，且对 x>0 收敛到0。由有限测度的 dominated convergence，E_m→0。这里没有给指数速度。

## N281.3 全素数幂的合法算术上界（不是本原费用lower）

对 k≥2，Ψ^(k−2) 是整系数 homogeneous polynomial，degree D=5(k−2)。单项 α^a 的实际积分是

\[
\int_\Delta\alpha^a d\alpha=\frac{\prod_{e=1}^{10}a_e!}{(D+9)!}.
\]

对每个 prime power q=p^j，其分母 factorial layer 为

\[
\left\lfloor\frac{D+9}{q}\right\rfloor
-\sum_e\left\lfloor\frac{a_e}{q}\right\rfloor
=\left\lfloor\frac{9+\sum_e(a_e\bmod q)}q\right\rfloor\le9.
\]

q>D+9 时 layer 为0。记 ℓ_N=lcm(1,…,N)，则

\[
\ell_{5k-1}^{\,9}\mu_k\in\mathbf Z\quad(k\ge2),\qquad
L_m=\ell_{10m+9}^{\,9}
\tag{N9}
\]

支付 N6 全部有理条目，包括小素数和高幂。以(8L_m)^(m+1)可安全清整 detG 的 ξ 多项式。它只有 exp(O(m²)) 上界，不是 actual primitive lower；原 determinant 的小 detH 不能在除完整 content 后再当免费余项。

## N281.4 实际推前权给全规模零裸指数

此证明直接针对 N6–N8，不重跑旧215的 x=1 变形。取 e=b₅，它在一条 cycle 上，故存在 avoiding e 的 spanning tree。令 α_e=1−r，其余9条边 α_f=r u_f，u∈Δ₈ 的固定紧内集 U。按 e 是否在 complementary tree monomial 中分拆，精确有

\[
\Psi=r^4((1-r)A(u)+rB(u)),\qquad A(u)>0,
\tag{N10}
\]

A、B 是非负系数 polynomial。U 上 A 一致有正 lower，A、B、导数一致有界；小 r 时 ∂Ψ/∂r 与 r³ 双边可比，Ψ 与 r⁴ 双边可比。单形体积是 r⁸dr du。因此 t=Ψ 的 pushforward 测度，在一个固定(0,δ)上满足严格 measure inequality

\[
\boxed{\int f(t)d\mu\ge c_0\int_0^\delta f(t)t^{-3/4}dt}
\quad\text{对每个非负可测 }f.
\tag{N11}
\]

这是对 U 这一正体积角区作变量替换得到的 lower；没有把一个角区当整个积分的精确 asymptotic。

对任意 degree≤N、P(0)=1 的实 polynomial，端点 Christoffel inequality 给

\[
\int_0^1P(x)^2x^{-3/4}dx\ge c_1(N+1)^{-1/2}.
\tag{N12}
\]

为避免外借未核公式，这里给完整证明。对 α>−1，置

\[
q_j(x)=\frac{x^{-\alpha}}{j!}
\frac{d^j}{dx^j}\bigl(x^{j+\alpha}(x-1)^j\bigr).
\]

j 次分部积分（两端低于j阶的边界项均为0）给 q_j 对所有低于j的 polynomial 正交；其 leading coefficient 为 Γ(2j+α+1)/(j!Γ(j+α+1))。再对 q_j 自身分部积分并用 beta integral，得

\[
\int_0^1q_j^2x^\alpha dx=\frac1{2j+\alpha+1},\qquad
q_j(0)=(-1)^j\frac{(\alpha+1)_j}{j!}.
\]

把 P 展开为 q_j 基并用 Cauchy–Schwarz，左侧至少是

\[
\left[\sum_{j=0}^N(2j+\alpha+1)
\left(\frac{(\alpha+1)_j}{j!}\right)^2\right]^{-1}.
\]

α=−3/4 时，Gamma ratio 的 Stirling 界给 (1/4)_j/j!≤C(j+1)^(−3/4)，上方和≤C′√(N+1)，证 N12。缩放 x=t/δ，代 N11 和 N8（N=m+1），得到

\[
\boxed{c_2(m+2)^{-1/2}\le E_m\le I,\qquad
\lim_{m\to\infty}\frac{\log E_m}{m}=0.}
\tag{N13}
\]

这里放宽了 P′(0)=0 约束，只会降低最小值，所以 lower 对实际空间依然合法。N13 也给 log E_m/m²→0；没有主张 E_m 恰与 m^(−1/2) 同阶。

## N281.5 完整本原输出不能借 detH 获得负指数

任何从 N7 清分母并除全内容所得非零 primitive integer polynomial，仍是

\[
Q_m(X)=A_mX+B_m=A_m(X-r_m/c),\quad A_m\in\mathbf Z\setminus\{0\}.
\]

在实际 ξ 处，N13 严格给

\[
|Q_m(\xi)|=\frac{|A_m|}{c}E_m
\ge\frac{c_2}{c}(m+2)^{-1/2}.
\tag{N14}
\]

所以**所有无界子列、全部共同内容约分后**，liminf m⁻¹ log|Q_m(ξ)|≥0，也没有负二次指数。费用理想化为0也不能得到原严格指数接口。这个结论比从 N9 的正安全 upper 宣称 no-go 强，且范围明确；它不否定用完全不同的次指数准则进一步分析 actual A_m，也不证明全部图 period 方法不可行。

## N281.6 宏观决定、最小可查问题与实际读域

与279/280竞争后的准确收益是：Z₅ 的正实积分避开未正则化复有理平方发散；N5 避开 ζ3/ζ5 背景；N6 无界实际正秩，故不是固定jet改标签。但 N13–N14 立即拒绝**该固定 Ψ polynomial Gram 的严格指数数值实施**。不把纯投影、正定、全素数 safe cap 或新的 no-go 登记为完整可行性改善，不重置停滞。

若根需保留此几何方向的最小来源任务，首问题应是一个**真实不同权的 period 下降证书**，不再是多算 polynomial degree：例如先固定

\[
\rho=\int_\Delta\frac{d\alpha}{1+\Psi(\alpha)}
\tag{N15}
\]

（对应下一类基向量 Ψ²/(1+Ψ) 与1的配对），只核其实际 rational-form reduction 是否落入 Q+Qξ、并保存其全部新增 relative-period 边界。N1 的单个 period 评价、抽象 cohomology 有限维或280秩不能支付 N15；一个 rho 身份也不足保证完整矩阵纯化。**没有这样的新下降证据前，本稿不建议启动有理极点 Gram、扫描参数或另开数学实现。** N15 只是精确、有限的最小来源核查对象，不是已准入候选；若其他独立竞争已给更短的已付新机制，应优先它。本竞争不因“尚未排除”争取下一轮预算。

新外部输入的实际读域：Brown–Schnetz v2 HTML §1.1–1.3（尤其式1.1–1.2和Theorem1.1），及 §1.2中的单值 generating series 定义；未通读 §3–5 的证明。Yeats2016 PDF 实际读物理 pp.1–3中 circulant 定义、图 period 定义及 pp.8的 §3首段/图2说明；未核其 c₂ 定理或完整24页。网页定位结果中的其它预印本、批评文章、社媒和“新无理性”主张均未输入证明。N2–N14 为本文给出的自足专项推导，作者不将自己的推导计作独立复核，交根及另一代理审阅。
