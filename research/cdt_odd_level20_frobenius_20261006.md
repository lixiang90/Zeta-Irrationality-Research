# level20 的 excellent Frobenius 比值与两层消除

日期：2026-10-06。本稿只研究已有真实 L(3,χ₅) 系统的算术输入。新结果是一个次数 O(p) 的模 p³ Frobenius 比值，以及在 n<p² 的完整最高 packet 上分别提升一层、两层的具体微分算子。它们仍需通过 Smith 过滤、完整素数账本与评价高度转成可用的 CDT 常数；本稿没有新的数值无理性定理。

## 1. 固定输入与原文的适用条件

沿用 [完整模型](cdt_odd_level20_model_20261006.md)、[Hasse 输入](cdt_odd_level20_hasse_20261006.md)，不修改冻结证明。令 K=Q(√5)、χ=χ₅。反证假设 c=L(3,χ)∈Q，排除其分母和固定规范所涉及的有限素数，并取 p≥7、p∤20。以下在 O_{K,𝔭} 完成，p 在 K 中未分歧，因而用 p^j 记录 valuation 层是合法的。

原始文献是 [Beukers, Supercongruences using modular forms, arXiv:2403.03301v3](../literature/beukers2025_supercongruences_modular_v3.pdf)，2025-06-16 版本，共34页。页码均指该固定 PDF 的印刷页：

- p3 定义 excellent lift：s=t^σ=t(q^p)，不是直接 t↦t^p。
- p7 Assumption (II)、Theorem 1.13：t 是 Atkin–Lehner extension 的 integral Hauptmodul；权2形式 Θ 的 character 在 Γ₀(N) 上平凡；Θ 的唯一零轨道在 t 的极点，阶 r≤1；还需 eta product 或 r<1/3。
- p15 Lemma 3.2 是 eta norm identity；p17 Lemma 3.7 给 determinant-p 的 p+1 个商的置换。
- pp20–21 式(6)、Proposition 5.1 给 characteristic polynomial；r 的限制最终用于把比值识别成 degree<p 的通常截断。

这里 A_± 的 character 在 Γ₀(20) 上是非平凡 χ₅；它们也有多个零轨道。直接套 Theorem 1.13 不成立。

采用另一个真实权2 gauge

\[
B=\eta(2\tau)^2\eta(10\tau)^2,\qquad
\Phi=\frac{B}{t(1-t)}.
\]

其 eta 表达式为

\[
\boxed{\Phi=
\eta(\tau)^{-4}\eta(2\tau)^{10}\eta(4\tau)^{-4}
\eta(5\tau)^{-4}\eta(10\tau)^{10}\eta(20\tau)^{-4}.} \tag{1}
\]

它权为2、常数项1、q/t 系数为整数、character 在 Γ₀(20) 上平凡，并在 W₂₀ 下有 multiplier −1。六个原 cusp（分母 c=1,2,4,5,10,20）的阶依次为

\[
(0,3,0,0,3,0).
\]

在 Γ=Γ₀(20)+W₂₀ 的 genus0 商上，只有 t=∞ 的一个零轨道，但阶为 **3**。这恰违反 II(3) 的 r≤1，而不是违反 genus0 或整性要求。

不能靠扩大 Hall extension 自动修复：level20 的 Hall divisors 只有1、4、5、20，extension index至多4；Γ₀(20) 的权2总零阶为36/6=6。任一 holomorphic 权2形式若在该类 extension 上只有一个零轨道，其 orbifold 零阶至少6/4=3/2>1。换 Hauptmodul 不改变这个零阶。A_± 则有 N_± 的两个普通零轨道及 C_± 的两个分歧零轨道：disc(N_-)=37+8√5，Res(N_-,Δ)=−4400+400√5，均非零；共轭式同样非零。本稿选择 B 的 rational gauge Φ，并将 A/Φ=−N√C/5 保留为显式 algebraic factor。

## 2. 超出 r≤1，但保留 O(p) 次数的比值

令 Φ(q)=Σa_nq^n，1/Φ(q)=Σb_nq^n，均属于 Z[[q]]。真实变量为

\[
s(t)=t(q(t)^p),\qquad s(t)\equiv t^p\pmod p.
\]

后一式不能在模 p² 或 p³ 下使用。

仿照 Beukers p20 式(6)，但不使用 r≤1，构造

\[
T_p(X)=\left(1-\frac{\Phi(p\tau)}{\Phi(\tau)}X\right)
\prod_{k=0}^{p-1}\left(p^2-
\frac{\Phi((\tau+k)/p)}{\Phi(\tau)}X\right). \tag{2}
\]

Lemma 3.7 的假设在 Φ 上满足。因此 T_p 的系数是真正 Γ-modular functions，只可能在 Φ 的唯一零轨道 t=∞ 有极点。X^m 的系数次数至多3m。其 q-expansion 整性可由 elementary symmetric roots-of-unity sums、Φ(0)=1 及整数 q↔t 反演直接证明，故 T_p∈Z[t,X]。

式(1)的 Σ_d d e_d=0；eta norm phase因此为1。Lemma 3.2 给

\[
\Phi(p\tau)\prod_{k=0}^{p-1}\Phi((\tau+k)/p)=\Phi(\tau)^{p+1}.
\]

对奇素数，T_p 是 monic degree p+1 polynomial，其根为

\[
x_0=\Phi(\tau)/\Phi(p\tau),\qquad
x_k=p^2\Phi(\tau)/\Phi((\tau+k)/p)\quad(0\le k<p).
\]

定义 **完整 characteristic-polynomial 系数**

\[
G_p(t)=-[X^p]T_p(X,t)\in Z[t],\qquad\deg G_p\le3p. \tag{3}
\]

根之和及实际 Fourier trace 给精确恒等式

\[
G_p(t(q))=\frac{\Phi(q)}{\Phi(q^p)}+
p^2\Phi(q)\sum_{k=0}^{p-1}\frac1{\Phi(\zeta_p^kq^{1/p})}
=\frac{\Phi(q)}{\Phi(q^p)}+p^3\Phi(q)\sum_{j\ge0}b_{pj}q^j.
\]

因而得到全形式级数结论

\[
\boxed{\frac{\Phi(t)}{\Phi(s(t))}\equiv G_p(t)\pmod{p^3},
\qquad \deg G_p\le3p.} \tag{4}
\]

G_p(0)=1+p³，所以 G_p 在原点是 p-adic unit。此证明不把原文的 degree≤p−1 结论挪用到 r=3。G_p 也没有被称为 Φ 的 p 项截断。固定 p=7,11,13 的 mod p³ reduction 实际次数为3(p−1)，但本稿全素数证明只使用安全的3p上界。

模 p 下，Φ(s)≡Φ(t)^p，因此

\[
G_p\equiv\Phi^{1-p}=P_p(t)\pmod p, \tag{5}
\]

其中 P_p 是冻结 Hasse 稿的 degree3(p−1) polynomial。式(4)是对既有 Hasse 输入的真正 p³ 提升，代价是保留 degree O(p) 的完整系数。

## 3. q/t 链式法则与完整 packet

模型中 θ_qt=B√Δ、Δ=C_+C_-，平方根分支在 t=0 取1。令

\[
\vartheta=t\frac d{dt},\quad
g_s(t)=(1-t)\sqrt{\Delta(t)},\quad
S=\theta_q\log t.
\]

于是严格有

\[
\boxed{S=g_s\Phi},\qquad
\boxed{\vartheta s=p s b,\quad b=\frac{S(s)}{S(t)}}. \tag{6}
\]

由(4)

\[
b\equiv\frac{g_s(s)}{g_s(t)G_p(t)}\pmod{p^3}. \tag{7}
\]

所有原点级数均 p-integral，b、g_s、Φ、G_p 的常数项为 unit。

源写作 f_±=u∓√5v，θ_q³u、θ_q³v 是相应 E₄/F₄ oldform 组合。对1≤j<p，divisor sums 的确切分裂给

\[
[q^{pj}]\theta_q^3u=(1+\chi(p)p^3)[q^j]\theta_q^3u,
\quad
[q^{pj}]\theta_q^3v=(\chi(p)+p^3)[q^j]\theta_q^3v.
\]

因 p∤j，除以(pj)³并乘p³给模p³的原源 packet，而非只有模p：

\[
p^3 f_\pm(q)\equiv
(u\mp\sqrt5\chi(p)v)(q^p)
\pmod{p^3,q^{p^2}}. \tag{8}
\]

右边只指内部 degree<p 的 p-integral 截断；不能对含 p-denominator 的完整 f 取 reduction。整数 q↔t 反演把(8)转换到真实 s(t)，并保持 t^{p²} 理想。

令 F_{p,±}(z) 是 (u∓√5χ(p)v)∘q(z) 的 degree<p 截断。周期常数在假定 c∈Q 后为 p-integral，乘p³在本模数下消失。以

\[
R_\pm=N_\pm\sqrt{C_\pm},\quad
Y_\pm=p^3H_\pm,\quad
W_\pm(z)=-\Phi(z)F_{p,\pm}(z)/5,
\]

得到完整前缀关系

\[
\boxed{Y_\pm\equiv R_\pm(t)G_p(t)W_\pm(s(t))
\pmod{p^3,t^{p^2}}.} \tag{9}
\]

W_± 属于 O_{K,𝔭}[[z]]。此处使用 s=t(q(t)^p)，没有把它误换成 t^p。

## 4. 具体的一层与两层算子

暂省略 ±，设

\[
g=R G_p,\quad k=R/g_s,\quad
a_0=\vartheta\log(RG_p),\quad a_1=\vartheta\log(R/g_s),
\quad\nabla_i=\vartheta-a_i.
\]

a_i 为原点 p-integral 的 rational functions。虽然 R、g_s 分别有平方根，其 logarithmic derivatives 是 K(t) 有理函数。令 W_j=ϑ_z^jW(z)。式(6)–(9)及 Euler derivative 保持 t^{p²} 给

\[
\nabla_0Y\equiv p g b W_1(s)
\equiv p k\,g_s(s)W_1(s)
\pmod{p^3,t^{p^2}}, \tag{10}
\]

然后

\[
\boxed{\nabla_1\nabla_0Y\equiv
p^2 k b\left((\vartheta g_s)(s)W_1(s)+g_s(s)W_2(s)\right)
\pmod{p^3,t^{p^2}}.} \tag{11}
\]

右边全部 p-integral。因此在该完整前缀中，∇₀H 的系数至少为−2层，而 ∇₁∇₀H 至少为−1层。这是两种不同权重的整格信息；没有证明两个相同权重的 kernel，也没有得到第三层。

可显式清分母得到 polynomial rows。令 C_o 为另一个 C 因子，则

\[
a_0=\vartheta N/N+\tfrac12\vartheta C/C+\vartheta G_p/G_p,
\quad
a_1=\vartheta N/N+\frac t{1-t}-\tfrac12\vartheta C_o/C_o.
\]

取

\[
D_0=NCG_p,\quad M_0=D_0a_0,
\qquad D_1=N(1-t)C_o,\quad M_1=D_1a_1.
\]

它们的安全次数分别不超过 d₀=3p+4、d₁=5。第一行 L₀=D₀ϑ−M₀ 满足 L₀Y≡0modp。第二行

\[
\boxed{L_2=(D_1D_0\vartheta-D_1\vartheta D_0-D_0M_1)
             (D_0\vartheta-M_0)
       =D_1D_0^2\nabla_1\nabla_0} \tag{12}
\]

是 (H,ϑH,ϑ²H) 上的实际 order2 polynomial row，其三个系数次数不超过6p+13；L₂Y≡0modp²。这种清分母可能有非primitive因子，不能把度数和过滤收益当作免费的 saturation。

## 5. 一个严格限定的一阶障碍

本节只排除 **全形式级数、primitive first-order、polynomial coefficients 的模p² logarithmic lift**。不排除有限 t^{p²} jet，不排除本稿的 order2 composition，也不排除别的 p-adic connections。

用普通 derivative，令 J=t g_s。式(6)给 s'=pJ(s)Φ(s)/(J(t)Φ(t))。置

\[
\Lambda_p=J^{p-1}=[t(1-t)]^{p-1}\Delta^{(p-1)/2}.
\]

由(4)–(5)

\[
s'\equiv p\Lambda_p/P_p\pmod{p^2},\qquad
\boxed{\frac{\Phi'}\Phi\equiv
\frac{G_p'}{G_p}+p\Lambda_p\frac{(P_p')^p}{P_p^{p+1}}
\pmod{p^2}.} \tag{13}
\]

在 P_p 的 generic double root ξ（不在 Δ=0 或 cusp），Λ_p(ξ)≠0，而 P_p' 恰有一阶零。故式(13)的 p 层第二项有 pole p+2。写 G_p=P_p+pG₁ modulo p²，G_p'/G_p 的 p 层最多有四阶 pole；这不能消掉 p+2阶项。

若 D(Φ'/Φ)−M≡0modp² 是全级数关系，D、M∈O_{K,𝔭}[t]，且 D modp非零，则在每个这种 ξ，D₀=Dmodp 的零重数必须至少p+1。比较 p 层时，可在 ξ 的 unramified extension 中选择保留该双根的局部 factored lift P₀=x²U，以及保留 D₀ 零重数的 lift x^mV；U、V 为 unit。原实际 lift 与这些选择之差分别记作 pG₁、pD₁。这使 dlogP₀ 只有简单pole，且 m≥1 时 D₀dlogP₀ 正则；G₁修正的 pole 至多3−m阶（上述4−m的上界仍安全），D₁dlogP₀至多简单pole。若 m≤p，额外 p 层剩余 pole为p+2−m≥2，严格超过两者，不能抵消。对于 A=−RΦ/5，固定 R 的 logderivative 不改变避开 N=0 的 generic poles。

Hasse 的 simple-zero 输入给 generic double roots 数量至少(3p−7)/2；每个 embedding 的 N 最多排除两个。因此相应 primitive 全局一阶提升必须满足

\[
\deg(D\bmod p)\ge(p+1)(3p-11)/2. \tag{14}
\]

该 O(p²) 障碍解释了为何不能简单把旧 O(p) Hasse 一阶算子升级为全局模p²一阶算子。式(11)作用于 Frobenius packet，并采用不同的第二 connection，所以不受此限定障碍阻止。

## 6. 安全的两层 Smith 接口

固定 N<p²、D≥0，在 E_D=O_{K,𝔭}[t]_{≤D}^{⊕3}（秩 n=3(D+1)）上，令 M 是将 row 与 (Y,ϑY,ϑ²Y) 组合后取前 N 项的整系数矩阵。考虑真实 integrality 格

\[
\Lambda=\{v\in E_D:Mv\in p^3O_{K,𝔭}^N\}.
\]

若其 Smith valuations 为 a_i（zero directions 取 a_i=∞），则

\[
[E_D:\Lambda]=\operatorname{Norm}(\mathfrak p)^{\sum_{i=1}^n\max(3-a_i,0)}.
\]

冻结 Hasse 稿给 u₁=2(D−δ_H+1)_+ 个 reduction-independent rows，其输出被 p 整除，δ_H≤(3p+9)/2。新行 L₂ 的最高坐标是 D₁D₀²，其 modp 不是零 polynomial；所以 t^jL₂（0≤j≤D−δ₂，δ₂=6p+13）的 reductions 线性无关。它们输出被 p² 整除，给 u₂=(D−δ₂+1)_+ 个方向。因此

\[
\#\{a_i\ge1\}\ge u_1,\quad \#\{a_i\ge2\}\ge u_2,\qquad
\boxed{[E_D:\Lambda]\le\operatorname{Norm}(\mathfrak p)^{3n-u_1-u_2}.} \tag{15}
\]

u₂方向已经属于第一层 kernel，它只提供额外一层收益，不能把它算成另外两份独立 kernel。此界只使用 N<p² 的 prime window，未覆盖小 p 的更高幂源分母；也没有优化 Q 的公共因子或相对于旧 kernel 的饱和。式(15)是可供后续完整算术账本使用的安全接口，并非最终 CDT τ。

## 7. 验证、限制与下一接口

[独立精确脚本](cdt_odd_level20_frobenius_20261006_verify.py) 和 [证书](cdt_odd_level20_frobenius_20261006_verify.json) 固定 p=7、11、13，不进行目标扫描。以 (Z/p³Z)[r]/(r²−5) 的 pair arithmetic 在每个 n<p² 检验：

- excellent lift s 与 t^p 在 modp³不同而 modp相同；(4)、(6)、(7)、(13) 全前缀成立；
- E/F 完整 source packet 和真实 t-lift 的 modp³关系；
- 两个 embedding 的(10)、(11)、(12)提升；固定样本中 first row不普遍提升两层，second row不普遍提升三层；
- 清分母系数是所称 degree O(p) polynomials。

共107项精确检查。有限证书仅检查规范、坐标及算子，全部合适素数的依据是 §§2–4 的 modular divisor、eta norm、divisor sum 和链式法则证明。

后续应在式(15)的基础上算更精细的 Smith valuations、primitive saturation、次数损耗，并与小素数/高幂层及 CDT Taylor evaluation 高度同算。未经这一步，不能把两层节省直接改写成新的 τ 或新无理性结论。

## 8. 独立审阅范围

helper_tensor_budget 已直接核读 Beukers 固定 v3 的相关页，并独立重推本稿 §§1–4 的所有素数 ratio、source packet、两层 connection、polynomial clearing，以及 §6 的 weighted Smith 接口。其 [独立审阅记录](cdt_odd_level20_frobenius_review_20261006.md) 另给主任务的一变量完整预算；本稿不重复该预算。该审阅没有运行本稿107check脚本，也没有把 §5 的辅助一阶障碍用于预算结论。
