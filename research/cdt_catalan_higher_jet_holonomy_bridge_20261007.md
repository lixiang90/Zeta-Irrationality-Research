# Catalan outer-log 的完整有限 Hasse-jet 模型与 holonomy 投影边界

2026-10-07。只新增本稿；旧620冻结稿、旧producer/guard及源仓库均未改动或执行。研究目标是把已有 Catalan 两分支 Hardy 核保留，只改变 outer measure，并辨明有限 jet 能否真正消去低周期。本文得到完整真实 moment 系统、全素数指数规模清分母、一个实际满秩低周期核和精确的 flat-splitting 反例；没有新 β(4) 无理性或 \(1,G,\beta(4)\) 的数值线性无关性结论。

## 1. 参数化同一实际积分

令 \(f(t)=\sqrt{1-t^2}\)、\(a(t)=\operatorname{artanh}t\)，固定偶数 \(\ell=2m-2\ge2\)。已有解析迁移使用

\[
\rho_m(t)=\frac{a(t)^\ell}{(\ell+1)!},\qquad
F^{(m)}_{rj}=M^{(m)}(P_r,j)-\frac32Z^{(m)}(D_r,j).
\tag{H1}
\]

保持原整数 Chebyshev \(P_r,D_r\)、contact、raw column pool 与整数 filter。引入真正复参数（不是把周期任意变成形式变量）

\[
M_z(i,j)=\int_{-1}^1\!\int_0^1
\frac{|t|t^is^j e^{za(t)}}{f(t)(1-ts)}\,ds\,dt,
\quad
Z_z(i,j)=\int_0^1\!\int_0^1
\frac{t^is^j e^{za(t)}}{1-ts}\,ds\,dt.
\tag{H2}
\]

它们在 \(|\operatorname{Re}z|<1\) 全纯。端点 \(t=\pm1\) 被 \(u^{-(1+|\operatorname{Re}z|)/2}(1+|\log u|)\) 支配；任意固定阶参数导数只增加固定 log 幂，仍可积。\(Z\) 的支配更弱。由 Hasse 系数约定 \([z^k]\)，

\[
M^{(m)}(i,j)=\frac{[z^\ell]M_z(i,j)}{\ell+1},
\qquad Z^{(m)}(i,j)=\frac{[z^\ell]Z_z(i,j)}{\ell+1}.
\tag{H3}
\]

这是完整两个 measure 同时改动的 mixed object。它仍满足已有解析迁移的实处估计

\[
\log|\Delta_N^{(m)}|
\le (\tfrac12\log2-2.290939875)n^2+O_m(n\log(n+2)),\quad n=48N.
\tag{H4}
\]

H4 沿用该稿实际有限非负 measure 证明；本文未重算原数值证书。

## 2. 外矩的闭合变形和首次低周期

定义真实正半轴矩

\[
A_i(z)=\int_0^1\frac{t^ie^{za(t)}}{f(t)}dt,
\quad B_i(z)=\int_0^1t^ie^{za(t)}dt.
\]

对 \(t^if(t)e^{za(t)}\) 分部积分，端点确为零（\(i=0\) 的左端单独保留），得到

\[
A_1=1+zA_0,\qquad
(i+1)A_{i+1}=iA_{i-1}+zA_i\quad(i\ge1).
\tag{H5}
\]

置 \(u=\sqrt{(1-t)/(1+t)}\)，则

\[
A_0(z)=2\int_0^1\frac{u^{-z}}{1+u^2}du
=2\sum_{k\ge0}\beta(k+1)z^k,
\tag{H6}
\]

该展开在 \(|z|<1\) 绝对局部一致成立。\(k=0\) 的 \(\beta(1)=\pi/4\) 由通常交错积分解释。

记 \(\mu_i(z)=\int_{-1}^1|t|t^ie^{za(t)}dt/f(t)\)。则

\[
\mu_i=A_{i+1}(z)+(-1)^iA_{i+1}(-z),
\quad \mu_{-1}=A_0(z)-A_0(-z),
\quad \mu_0=2+z\mu_{-1},
\]
\[
(i+1)\mu_i=i\mu_{i-2}+z\mu_{i-1}\quad(i\ge1).
\tag{H7}
\]

这里 \(\mu_{-1}\) 是可积的 sign/f moment，不引入不存在的 \(t^{-2}\) 积分。特别地

\[
\frac{[z^\ell]\mu_0}{\ell+1}
=\frac4{\ell+1}\beta(\ell).
\tag{H8}
\]

H2 的 diagonal shift 给

\[
M_z(i,j)-M_z(i+1,j+1)=\frac{\mu_i(z)}{j+1}.
\tag{H9}
\]

已有起始周期是 \(M^{(m)}(0,0)=4\beta(\ell+2)\)。因此得到精确身份

\[
\boxed{M^{(m)}(1,1)=4\beta(2m)-\frac4{2m-1}\beta(2m-2).}
\tag{H10}
\]

尤其 \(M^{(2)}(1,1)=4(\beta(4)-G/3)\)。这是一条新的实际 carrier 身份，既可考虑纯 \(\beta(4)\)，也可把 \(\beta(4)-G/3\) 或 \(1,G,\beta(4)\) 作为目标。H10 本身不证明任何目标无理。由于新 Catalan 稿已证明 \(G\notin\mathbb Q\)，在仅假设 \(\beta(4)\in\mathbb Q\) 时，该单个 \(M^{(2)}(1,1)\) 反而无理；仅校准 (M(0,0)) 不能启动原 rational determinant 论证。这不是对完整 mixed \(F\) 的不可能性断言，后者可能另有实际相消。

对 \(t^i(1-t^2)e^{za(t)}\) 分部积分给

\[
B_1=(1+zB_0)/2,
\qquad (i+1)B_i=(i-1)B_{i-2}+zB_{i-1}\quad(i\ge2).
\tag{H11}
\]

若 \(\eta(k)=\sum_{v\ge1}(-1)^{v-1}/v^k\)，则

\[
B_0(z)=1+\sum_{k\ge1}2^{1-k}\eta(k)z^k.
\tag{H12}
\]

证明可先令 \(t=\tanh a\)。对 \(k\ge1\)，分部积分把 \(\int_0^\infty a^k\operatorname{sech}^2a\,da\) 改成 \(k\int_0^\infty a^{k-1}(1-\tanh a)da\)，再用 \(1-\tanh a=2/(e^{2a}+1)\)。Abel 正则化后逐项积分，得到 \(k!2^{1-k}\eta(k)\)；\(k=1\) 的条件收敛由同一正积分极限处理。

## 3. 完整 (M/Z) 数组的有限 jet 模块

以下没有遗漏 \(i<j\) 的边界，也没有靠有限 prime 表。记

\[
T=M_z(0,0),\ U=M_z(0,1),\quad
V=Z_z(0,0),\ W=Z_z(1,0),\ X=Z_z(0,1).
\]

对 \(K_d^-=M_z(d,0), K_d^+=M_z(0,d)\)，H7 的有限移位与 telescoping 给

\[
K_0^-=K_0^+=T,\quad K_1^+=U,\quad
K_1^-=zT+\mu_{-1}+\mu_0,
\]
\[
dK_d^-=(d-1)K_{d-2}^-+zK_{d-1}^-+\mu_{d-2}+\mu_{d-1},
\]
\[
(d-1)K_d^+=(d-2)K_{d-2}^++zK_{d-1}^+
 +\frac{\mu_0}{d-1}+\frac{\mu_{-1}}d\quad(d\ge2).
\tag{H13}
\]

例如第二条递推的剩余 series 是 \(\sum_{u\ge2}(\mu_{u-2}-\mu_u)\)，另有 \(z(K_{d-1}^+-\mu_0/d)\) 和 \(u=0,1\) 的真实边界；H7 的 \(2\mu_1-z\mu_0=\mu_{-1}\) 恰给所显示的最后一项。因为 \(\mu_i(z)\to0\) 在 compact substrip 一致成立，telescoping 尾确实趋零。

对 \(L_d^-=Z_z(d,0),L_d^+=Z_z(0,d)\)，H11 给

\[
L_0^-=L_0^+=V,\quad L_1^-=W,\quad L_1^+=X,
\]
\[
dL_d^-=(d-2)L_{d-2}^-+zL_{d-1}^-+B_{d-2}+B_{d-1},
\]
\[
dL_d^+=(d-2)L_{d-2}^++zL_{d-1}^+
 +\frac{B_0}{d-1}+\frac1d\quad(d\ge2).
\tag{H14}
\]

最后一个 (1/d) 来自 \(2B_1-zB_0=1\)。\(Z_z(i,j)-Z_z(i+1,j+1)=B_i(z)/(j+1)\)。故 H13/H14 和 diagonal shift 无歧义生成所有 \(i,j\ge0\)。

**完整有限模块定理。** 固定 \(\ell\)，所有 H3 的矩属于下列实际周期生成元的 \(\mathbb Q\)-span：

\[
\mathscr P_\ell=\left\{1,\beta(1),\ldots,\beta(\ell+1),
\eta(1),\ldots,\eta(\ell),
[z^k]T,[z^k]U,[z^k]V,[z^k]W,[z^k]X:0\le k\le\ell\right\}.
\tag{H15}
\]

这是至多 \(7\ell+7\) 个实际生成元；不声称最小基或数值独立。按 jet 阶归纳时，所有 \(zK_{d-1}\) 都降一阶，H5/H7/H11/H13/H14 构成有限 triangular extension，而不是每个 \(N\) 另猜一套高权周期。

配对 \(\pm t\) 还给准确的 top-period 删除/保留规则：

\[
\frac{T(z)+T(-z)}2=A_0'(z)+A_0'(-z),
\quad [z^{2j}]T=4(2j+1)\beta(2j+2).
\tag{H16}
\]

所以 H15 中目标 \([z^\ell]T\) 可以无条件换成 \(4(\ell+1)\beta(\ell+2)\)。其余 seed jets 仍是显式真实积分，尚未被假定为有理或已命名 beta 值。

## 4. 全素数整模型：固定 jet 无 factorial \(n^2\log n\) 障碍

给出可复核的 generating-function 表，避免从逐次除 \(d\) 得到过粗的 \(H!\) 付款。写

\[
a(x)=\operatorname{artanh}x,\quad f(x)=\sqrt{1-x^2},\quad
h(x,z)=f(x)^{-1}e^{za(x)}.
\]

对 \(\mathcal A=\sum_{i\ge0}A_ix^i,\mathcal B=\sum_{i\ge0}B_ix^i\)，

\[
\mathcal A=h\left(A_0+\int_0^x f(u)^{-1}e^{-za(u)}du\right),
\quad
\mathcal B=\frac{e^{za(x)}}x\int_0^x
\frac{e^{-za(u)}(B_0+u)}{1-u^2}du.
\tag{H17}
\]

这里 \(x^{-1}\) 是 removable；\(\mu(x)=\sum_{i\ge0}\mu_ix^i\) 正是

\[
\mu(x)=\frac{\mathcal A(x,z)-A_0(z)+A_0(-z)-\mathcal A(-x,-z)}x.
\tag{H18}
\]

令 \(\mathcal K^-=\sum_{d\ge0}K_d^-x^d,\ \mathcal K^+=\sum_{d\ge0}K_{d+1}^+x^d\)。

\[
\mathcal K^-=h\left(T+\int_0^x
 \frac{h(u,z)^{-1}((1+u)\mu(u)+\mu_{-1})}{1-u^2}du\right),
\]
\[
\mathcal K^+=h\left(U+\int_0^x\frac{h(u,z)^{-1}}{1-u^2}
 \left[-\frac{\mu_0\log(1-u)}u
 +\frac{\mu_{-1}(-\log(1-u)-u)}{u^2}\right]du\right).
\tag{H19}
\]

对 \(\mathcal L^- =\sum_{d\ge0}L_d^-x^d,\ \mathcal L^+=\sum_{d\ge0}L_{d+1}^+x^d\)，

\[
\mathcal L^-=e^{za(x)}\left(V+\int_0^x\frac{e^{-za(u)}}{1-u^2}
 \left[(1+u)\mathcal B(u)+W-zV-B_0\right]du\right),
\]
\[
\mathcal L^+=\frac{e^{za(x)}}x\int_0^x\frac{e^{-za(u)}}{1-u^2}
 \left[X-B_0\log(1-u)-\frac{\log(1-u)}u-1\right]du.
\tag{H20}
\]

各式可直接求导核回 H5/H11/H13/H14，所有显示的 \(u^{-1},u^{-2}\) 皆由分子 Taylor 零阶支付。没有负幂积分 regularization。

**整系数界。** 令 \(D_R=\operatorname{lcm}(1,\ldots,R)\)。对 \(0\le i,j<H\)，在 H15 的自由生成系统中选择由 H17–H20/diagonal reduction 定义的 coefficient arrays，则

\[
Q_{\ell,H}:=2(\ell+1)\ell!\,2^{12(H+\ell+4)}D_{H+4}^{\ell+4}
\tag{H21}
\]

事实上，\(Q_{\ell,H}/2\) 已同时使 \(M^{(m)}(i,j)\)、\(Z^{(m)}(i,j)\) 的形式系数为整数。因外面的 (2) 已支付 (3/2)，相同 Q 使全部真实 mixed raw entries、整数 Chebyshev contractions 与整数 column filters 的系数为整数。

证明如下。\(f^{\pm1}\) 的第 \(v\) 个 Taylor 系数由 \(2^{2v+2}\) 清分母；\((1-u^2)^{-1},(1\pm u)^{-1}\) 的系数为整数。固定 \(z\)-degree \(k\le\ell\) 的 \(e^{\pm za(u)}\) 系数是 \(a(u)^k/k!\)，在 prefix \(v\le H+4\) 由 \(\ell!D_{H+4}^k\) 清分母。相乘时参数阶的总和至多 \(\ell\)，因此不是每因子另付 \(\ell\) 层；\(\ell!/\prod k_i!\) 是整数。一个 formal integration 只增加 \(D_{H+4}\) 一层；(log(1-u)) 也只增加一层。H17–H20 任一路径至多两重 integration；log source 至多再一层，最后 diagonal finite tail 除 (j+1) 至多一层，总指数至多 \(\ell+4\)。最多四个 \(f^{\pm1}\) factors 在同一 coefficient 路径上出现；H18 与 H19 的 removable shifts 至多移动固定四阶。\(2^{12(H+\ell+4)}\) 同时支付这些 dyadic factors 及 H12 的 \(2^{1-k}\)。H3 的 \(\ell+1\) 及 mixed (3/2) 已列在 Q 中。该证明对每个素数及所有 \(p^e\) 同时成立。

故 \(\log Q_{\ell,H}=O_\ell(H)\)，而非 \(O_\ell(H\log H)\)。当原 \(H=65N\asymp n\)，

\[
Q_{\ell,H}^{n}\Delta_N^{(m)}\in\mathbb Z[\mathscr P_\ell]
\tag{H22}
\]

作为实际周期代入的整数系数多项式成立。它不是“在只假设 \(\beta(2m)\) 有理时 determinant 已有理”的断言；未消掉的 seed periods 仍在。H21 是一个安全但很粗的 \(n^2\) 费用；没有继承原 Catalan 的优化全原列池费用或非零种子。

## 5. 固定 jet 不等于 \(O(n\log n)\) 费用或常秩坏空间

令 \(h_d(z)=[x^d]h(x,z)\)。这是 H5 齐次传播的完整 coefficient kernel。它满足

\[
h_0=1,\ h_1=z,\quad dh_d=(d-1)h_{d-2}+zh_{d-1}.
\tag{H23}
\]

对每个奇素数 \(p>k\ge1\)，有精确局部身份

\[
\boxed{v_p([z^k]h_{kp}(z))=-k.}
\tag{H24}
\]

因为 \([z^k]h_{kp}=[x^{kp}]f^{-1}a(x)^k/k!\)，所有奇分母在 \(kp<p^2\) 内至多有一个 \(p\)。出现 valuation (-k) 需要 \(k\) 个 artanh 指数全为 \(p\) 的正奇倍数；总次数 (kp) 强迫恰为 \(p,\ldots,p\)，并且 \(f^{-1}\) 取常数项。唯一最低项是 \(1/(k!p^k)\)，其他项 valuation 至少 (-k+1)，不能抵消。比如 \(h_5=(89z+30z^3+z^5)/120\)。H24 反驳“固定 jet 阶数只可能增加固定坏素数/多项式尺度分母”的一般断言；它不是对最终 determinant 费用的下界，后者还可能通过 alternation/rank 节省。

还有一个实际 full-rank 低周期核。H5 可写成 \(A_d=h_dA_0+c_d(z)\)，其中 \(c_d\in\mathbb Q[z]\) 且 parity 为 \(d-1\bmod2\)。从 H6 得

\[
\mu_{2j}^{(2)}:=\frac{[z^2]\mu_{2j}}3
=\frac43[z]h_{2j+1}(z)\,G+r_j,\quad r_j\in\mathbb Q.
\tag{H25}
\]

又 \(c_{2j+1}'(0)=0, A_0(0)=\pi/2\)，所以

\[
[z]h_{2j+1}=\frac2\pi A_{2j+1}'(0)
=\frac1\pi\int_0^1\frac{s^j\operatorname{artanh}\sqrt s}{\sqrt{1-s}}ds.
\tag{H26}
\]

因此对任意 \(n\ge1\)，矩阵

\[
C_n=\left(\frac43[z]h_{2(i+j)+1}\right)_{0\le i,j<n}
\tag{H27}
\]

严格正定：它是正、内部非零、有限 measure \(\frac4{3\pi}\frac{\operatorname{artanh}\sqrt s}{\sqrt{1-s}}ds\) 下的 monomial Gram。于是同一个低周期 \(G\) 在真实 outer Hankel moment 系统中有 rank \(n\)，并非只有一个坏方向。

H27 不断言原 mixed Catalan raw matrix 的 \(G\)-coefficient 已满秩；它精确否定“seed/jet 类型固定，所以污染 rank 必为 (O(1))”这一步。若某种常秩 border 只能对 nuisance coefficient 增加 rank≤k 的 correction，则要消掉 H27 必须 \(k\ge n\)。固定 jet 类型也可能需要每行一套 (O(n)) auxiliary coordinates；其完整 determinant energy/格费用不能自动标成 \(O(n\log n)\)。

## 6. 有理投影的正确接口与 flat extension 的限制

H15/H21 首次把 outer-log 原对象的完整 coefficient arrays 固定下来。任意有限 row/column pool 上，以实际 seed periods 为自由符号记录足够条件（不假定独立）。若目标是 \(\theta=aG+b\beta(4)\)，\(b\ne0\)，先利用 H16 等已证实际身份合并生成元，把 raw matrix 写为

\[
F=C_0+G C_G+\beta(4)C_4+\sum_\nu p_\nu C_\nu,
\quad C_\bullet\in M_{n\times R}(\mathbb Q).
\]

定义真正的有理 column kernel

\[
K_N=\bigcap_\nu\ker C_\nu\ \cap\ \ker(bC_G-aC_4)\subset\mathbb Q^R.
\tag{H28}
\]

若允许的 endpoint/filter column subspace 为 \(W_N\subset\mathbb Q^R\)，则得到 \(n\) 个单目标 columns 且目标 coefficient 非退化的充分充要形式条件是

\[
\operatorname{rank}(C_4|_{K_N\cap W_N})=n.
\tag{H29}
\]

清分母后可取整数 columns，得到 \(Q_0+Q_1\theta\) 的真实 matrix。H29 的 sufficiency 由挑 \(n\) 个 image basis；necessity 是目标 coefficient 的实际 rank。这个条件不要求 \(p_\nu\) 数值独立，因此是可靠的充分消元准则。若只选纯 \(\beta(4)\)，令 \(a=0,b=1\)。若选 \(\beta(4)-G/3\)，令 \(a=-1/3,b=1\)。消元所需 primitive lattice index/height 必须另算；H21 支付的是输入数组，不支付任意 Smith-kernel basis 的额外高度。

尤其，只在原 \(n\times n\) filtered matrix 上作可逆 rational row/column 变基，不可能消掉一个原来非零的 formal nuisance coefficient：\(A C_\nu B=0\iff C_\nu=0\)。若 \(W_N\) 仍恰是原 \(n\)-维 filter column space，H29 满 rank 会强迫该整段空间已处于 \(K_N\)。因此“保留同一个 full determinant，只换可逆 finite-jet basis”不是新的周期消除机制。需要证明原 contact 确实给新 arrays 所需身份，或增大/改变 allowed pool，并同步给出新的 Hardy/energy 与全原格预算。

还可给出一个范围明确的 flat-splitting 反例。函数

\[
f(x)^{-1},\quad f(x)^{-1}a(x),\ldots,
f(x)^{-1}\frac{a(x)^\ell}{\ell!}
\tag{H30}
\]

构成 twisted Kummer Hasse tower。去掉平方根符号的二重 cover 上，绕 \(x=1\) 的局部 monodromy 是一个大小 \(\ell+1\) 的 regular unipotent Jordan block \(\exp(-2\pi iN)\)。它的 commutant 是 \(\mathbb C[N]\)，只有幂零局部环中的两个 idempotents 0、1。因此这个真实 jet local system 没有非平凡 horizontal direct summand，更没有把 top graded piece有理地分裂成直接因子的 flat projector。

该证明不排除 unipotent quotient（quotient 确实存在），不排除非水平 rational rows、额外相对 chains、tensor/Green integrations或针对 H28 的增长整数投影。它只排除把“固定高阶 logarithm module”自动拆成互不耦合的低周期与高 beta factor；period evaluation是否下降到某 quotient，仍须完整实际边界比较，不能由抽象 quotient alone 得到。

## 7. CDT 接口、目标新颖性与精确缺口

CDT 固定 v2 的 Theorem 7.0.1（PDF/印刷89–90页）要求 \(m\) 个真正 \(\mathbb Q[[x]]\) 芽、\(\mathbb Q(x)\)-线性独立、完整 denominator types，以及共同 map 上全部芽的 meromorphic continuation；在 holonomic 情形，仍须 \(\log|\varphi'(0)|>\tau\)。其给出的 rank bound 用同一 \(\tau\) 与 double boundary integral比较。H15 是真实有限周期生成系统，不是这些条件的替代；H22 的多周期整数多项式也不是有理 Taylor 芽。

因此可推进的具体路线是 H28/H29：在原完整 raw pool 中找满足目标关系的真实 integer kernel，证明 target image rank；再寻找同一关系使全部 monodromy/endpoint coefficient 消失的实际 germ，并证明完整 arithmetic type 与 strict holonomy ratio。不能把 H30 的 module dimension 或 \(T_\ell=4(\ell+1)\beta(\ell+2)\) 的单个值身份直接特化为数值 LI。

本轮 primary 检索实际打开 [Lai–Zhou 2021 v2](https://arxiv.org/abs/2103.00904)、[Zudilin 2019 v2](https://arxiv.org/abs/1804.09922) 与 [Talla Waffo 2026 v4](https://arxiv.org/abs/2602.16761)。前两份摘要给出的都是集合中至少一个 even beta 无理；2026文的摘要讨论显式多项式及归一化 ratio representations，未给单独 \(\beta(4)\) 或 \(1,G,\beta(4)\) 的 LI 定理。本轮检索没有核到 \(\beta(4)-G/3\) 无理或这组三值 LI 的 primary 定理，但这不能作为全球新颖性证明。本文没有改去重述 critical L-values 的 Lindemann/Baker 后果，也不把已知 Catalan 结论冒充新目标。

已证：H5–H20 完整变形/有限 jet arrays；H21–H22 全素数指数规模输入整模型；H10 的准确 mixed-beta scalar；H24 的高 jet 分母层；H27 的实际 rank \(n\) 低周期核；H28/H29 的可检验目标投影；H30 的 flat-splitting 限定反例。仍缺：H29 对原 allowed full pool 的成功与指数预算、真实单关系 meromorphic 芽、无限非零和足够严格的算术/解析差额。因此没有新的 ζ/L 数值无理性、LI 或形式化验证。

## 8. 实际读取与验证范围

实际全文读三份指定新稿：`catalan_higher_even_beta_analytic_transfer_20261007.md`、`catalan_higher_even_beta_period_projection_20261007.md`、`cdt_beta_single_period_confluent_integral_model_20261007.md`；读取已有 `period_holonomy_cdt_mechanism_20261005.md` 与 `period_holonomy_target_projection_20261005.md` 的前175/170行，及新仓库阅读稿前160行；用 rg 去重 outer-log、Hasse jet、holonomy 与 extension 结果。

源仓库只读 Catalan `build/sections/foundations.tex` 完整434行（提交按父任务已同步状态 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`，本文没有自行再次确认checkout）。未读新仓库 Deligne–Drinfeld 原章节；本稿不把其 Lie 结构当作数值输入。

按 PDF skill，用 bundled Python/pypdf 只读已存 `literature/cdt2024_l2_chi_minus3.pdf`：实际显示/阅读 PDF3、60、61、89、90、92、93、99共8页；60–61是定位途中显示的 discrepancy/large deviations，89–90核 Theorem7.0.1、92–93核 convexity refinements、99核其 evaluation module。定位扫描只输出匹配页号，不计为全文阅读。没有新增/下载文献PDF、渲染或改写PDF；本轮新原件下载数0。

全部数学推导为纸面证明；shell只执行读取、rg、只读PDF文本提取及本稿的文字转义修正，没有针对本稿执行数学producer、旧guard、prime扩表、Lean或数值拟合。读取的第一次默认工具被本机 deny-read ACL 初始化故障拒绝，随后以批准的 `require_escalated` 只读继续；本稿在授权工作区创建，未要求修改ACL或源repo。本文全素数身份是纸面推导，不称机器形式验证。

root已对本稿八节H1–H30作独立全文纸面数学审查并通过，重点重新推导四个border递推、全部generating functions/removable shifts、全素数cap、满秩Gram与投影/flat-splitting范围；仅请求修正两处literal mathcal和参数变量拼写。作者收审后完成这些排版修订，并最终全文回读。另应root要求，作者全文审查其 cdt_beta4_prime_newton_polygon_20261007.md 及N11–N23输入，用一段全新内存Fraction/mod23检查核p23 Pfaffian/gcd chain与n2判别式，J1–J15均通过；该独审没有执行旧程序，也不改变本稿H1–H30的纯纸面证明性质。
