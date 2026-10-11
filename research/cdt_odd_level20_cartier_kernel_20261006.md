# level20 目标积分的有界 Cartier–Hecke 核

日期：2026-10-06。本文新建，不改冻结稿。正结论是一个全素数结构输入：正规目标积分的最高 packet 被一个固定次数≤5的 rational kernel 控制。该核来自真实 weight4 Hecke 作用，不依靠扫描素数或假设未知 Smith rank。其 primitive 仍含明确的 ΘA 项；本稿没有消去该项，也没有证明新的 S3/S4 收益或数值无理性定理。

## 1. 固定实际形式与正确的正反号

取 \(r=\sqrt5\)、\(K=\mathbf Q(r)\)、\(\chi=\chi_5\)，沿原点规范分支使用 [完整模型](cdt_odd_level20_model_20261006.md) 与 [Frobenius稿](cdt_odd_level20_frobenius_20261006.md) 的

\[
\Delta=C_+C_-,\quad C_\pm=1-(6\pm2r)t+(6\pm2r)t^2,
\]

\[
N_-=1-(6+r)t+(1+r)t^2,\quad N_+=\sigma(N_-),
\quad A_\pm=-N_\pm\sqrt{C_\pm}\,\Phi/5.
\tag{C1}
\]

最后一式是 A 的实际分支；模型的 A₋/S gauge 才有另一因子 \(\sqrt{C_+}\) 在分母，不能把两个下标混用。另令

\[
S=\theta_q\log t=(1-t)\sqrt\Delta\,\Phi,
\quad\theta_q=q\,d/dq.
\tag{C2}
\]

由既有 η-unit \(t=\eta_1^3\eta_4\eta_5\eta_{20}^3/(\eta_2^4\eta_{10}^4)\)，

\[
S=\{3E_2(\tau)-8E_2(2\tau)+4E_2(4\tau)+5E_2(5\tau)
        -40E_2(10\tau)+60E_2(20\tau)\}/24.
\tag{C3}
\]

η指数的和为0，故 quasimodular anomaly 消去；logarithmic derivative 在各 cusp 有有限常数项。因此 \(S\in M_2(\Gamma_0(20),1)\)，\(S(0)=1\)。t 的 Fricke invariance 给 \(S(W_{20}\tau)=20\tau^2S(\tau)\)。

统一用 determinant-normalized slash：

\[
\mathcal W_N f(\tau)=N^{-k/2}\tau^{-k}f(-1/(N\tau)).
\]

已有真实关系是

\[
\mathcal W_{20}S=S,\quad\mathcal W_{20}A_-=-A_-,
\quad\mathcal W_{20}A_+=A_+.
\tag{C4}
\]

所以 \(F_{old}=A_-S\in M_4(\Gamma_0(20),\chi)\) 的 Fricke eigenvalue 为−1。

## 2. Hecke–Fricke 交换：不要求 cusp 或 newform

对 \(p\nmid N\)，取标准算术 Hecke 规范

\[
T_p^\chi f=\chi(p)p^{k-1}f(p\tau)+p^{-1}\sum_{j=0}^{p-1}f((\tau+j)/p).
\tag{C5}
\]

定义 \(\alpha_\infty=\operatorname{diag}(p,1)\)、\(\alpha_j=\begin{pmatrix}1&j\\0&p\end{pmatrix}\)、\(w_N=\begin{pmatrix}0&-1\\N&0\end{pmatrix}\)。则 \(T_p^\chi=p^{k/2-1}(\chi(p)[\alpha_\infty]+\sum_j[\alpha_j])\)。两项 \(\alpha_\infty w_N=w_N\alpha_0\)、\(\alpha_0w_N=w_N\alpha_\infty\) 直接互换。

对 j≠0，唯一选择 \(\ell\in\{1,\ldots,p-1\}\) 使 \(Nj\ell\equiv-1\pmod p\)。令

\[
\gamma=\begin{pmatrix}(1+Nj\ell)/p&j\\N\ell&p\end{pmatrix}\in\Gamma_0(N).
\]

直接乘矩阵得 \(\alpha_jw_N=\gamma w_N\alpha_\ell\)，且 detγ=1、χ(γ)=χ(p)。\(\mathcal W_N f\) 的 character 是 χ⁻¹。代入 coset 和，得到对所有 holomorphic \(M_k(\Gamma_0(N),\chi)\) 成立的

\[
\boxed{\mathcal W_NT_p^\chi=\chi(p)T_p^{\chi^{-1}}\mathcal W_N.}
\tag{C6}
\]

本模型 χ²=1，故右边的 Hecke space 不变。\(T_pF_{old}\) 的 Fricke eigenvalue 为 \(-\chi(p)\)。

原始输入：[Mocanu 作者原件](../literature/mocanu_atkin_lehner_theory_author.pdf) p6 Proposition4.1 给 double-coset 保持全部 holomorphic Mₖ，p7 Proposition4.2 的证明明确给 character Hecke 的上述 Fourier 系数规范；其 GL slash 用 det^(k−1)，不可在该算术 Tₚ上再乘一次本稿的 det^(k/2) 书写因子。正规化对照：[Weinstein 官方讲义](../literature/weinstein_modular_forms_intro_bu.pdf) p15 §4.4 说明非平凡 character 的 newform eigenvalues 被 χ(p)⁻¹扭转；[Box 的论文](https://link.springer.com/article/10.1007/s40993-021-00276-8) Lemma3.17(d) 给对应 Atkin–Lehner/Hecke 矩阵关系。后两者的具体表述不是本稿全 Mₖ 交换式的直接代用；上面的矩阵证明不需要 AS 是 cusp form 或 newform。另见独立的 [primary-input 审核](cdt_odd_level20_cartier_primary_input_20261006.md)。

## 3. 显式固定分母与 degree5 的全素数 kernel

置 \(\varepsilon=\chi(p)\)。定义

\[
A^{(\varepsilon)}=\begin{cases}A_-,&\varepsilon=1,\\A_+,&\varepsilon=-1,\end{cases}
\]

N^(ε)、C^(ε) 同下标，\(F_{den}^{(\varepsilon)}=A^{(\varepsilon)}S\)。其 eigenvalue 与 \(T_pF_{old}\) 同为−ε。因此

\[
\boxed{R_p(t):=\frac{T_p(A_-S)}{A^{(\varepsilon)}S}\in K(t).}
\tag{C7}
\]

原因是 character、weight 与 Fricke eigenvalue 全部相消，ratio 下降到已证 genus0 的 Fricke quotient。若 ε=−1仍用 A₋S 作分母，ratio 会 anti-invariant，不能直接宣称属于 K(t)。

全尺度 pole bound 可以显式清分母。已证 Φ 的零 divisor 只有 t=∞ 的两个 cusps，各阶3；由 (C1)、(C2)，

\[
F_{den}^{(\varepsilon)}
=-\frac15(1-t)N^{(\varepsilon)}C^{(\varepsilon)}
     \sqrt{C^{(-\varepsilon)}}\,\Phi^2.
\tag{C8}
\]

在 X₀(20) 上的全部零为：N 的两个普通 quotient 根各两个 lifts、各阶1；own C 的两个 branch、各阶2；other C 的两个 branch、各阶1；t=1的两个 cusps、各阶1。总阶4+4+2+2=12，与 weight4、index36 的 valence 相符。t=0、∞处 Fden 为 unit；特别是 t∞ 的表面 t⁶ 因子正与 Φ²的 zero6抵消。

分子 holomorphic。因为 ratio Fricke-invariant，在 other C branch 处其 pole 阶必须偶数，而 Fden 仅一阶零，所以没有 pole；等价地分子至少一阶消失。own C 的二阶零只容许 quotient t 上的一阶 pole；N 两根与 t1也至多 simple pole。故固定多项式

\[
\boxed{D^{(\varepsilon)}(t)=(1-t)N^{(\varepsilon)}(t)C^{(\varepsilon)}(t),
\quad\deg D^{(\varepsilon)}=5,\quad D^{(\varepsilon)}(0)=1}
\tag{C9}
\]

清掉所有 finite poles。∞处 ratio 有限，所以

\[
\boxed{R_p=P_p/D^{(\varepsilon)},\quad P_p\in K[t],\quad\deg P_p\le5.}
\tag{C10}
\]

这是固定 divisor 证明，对全部好 p 成立，并非从几个素数计算拟合出次数界。

## 4. p-integrality 与原点 unit

在好 place，A、S的全部 q coefficients integral；(C5) 的 q-expansion 是

\[
[q^n]T_pF=a_{pn}+\varepsilon p^3a_{n/p}
\]

（约定非整数 index 的项为0），因而分子全 q-series integral。分母 S A^(ε) 的 constant 为−1/5，是 unit。ratio 原点的全部 q coefficients integral；整数互逆 q↔t 与 D^(ε)(0)=1使 P_p=D^(ε)R_p 的全部 coefficients integral。因此对每个好 \(\mathfrak p\mid p\)，

\[
P_p\in O_{K,\mathfrak p}[t],\quad\deg P_p\le5,
\qquad\boxed{P_p(0)=R_p(0)=1+\varepsilon p^3\equiv1\pmod p.}
\tag{C11}
\]

这里只排除固定规范中的有限坏素数，不要求 p-dependent denominators。

## 5. relative Cartier 与新积分的真实 packet

令 residue field 为 k。split place 时 k=Fₚ，inert place 可为 Fₚ²。本文明确采用 **k-linear p-extraction**

\[
\mathfrak C_t\left(\sum a_nt^n\right)=\sum a_{pn}t^n,
\quad\mathfrak C_q\left(\sum a_nq^n\right)=\sum a_{pn}q^n.
\tag{C12}
\]

这是 relative Cartier 的 Frobenius-twisted target 识别，或 absolute Cartier 后作 σₚ-linearization；不是把 absolute Cartier 的 \(a_{pn}^{1/p}\) 无故写成 \(a_{pn}\)。[Katz 原件](../literature/katz1973_padic_modular_forms.pdf) PDF p47／印刷p115 Lemma3.6.1 明确把 Cartier 的值域置于 Frobenius twist。这里 q↔t、S具有 Fₚ coefficients，所以该识别与坐标转换相容。inert place 的 σₚ(r)=χ(p)r 不应再额外加到 (C12) 的 k-linear operator 上。

一形式的 Cartier 坐标相容性，应用于 A₋dt/t=A₋S dq/q，给

\[
\mathfrak C_t(A_-)(t(q))\,S(q)=\mathfrak C_q(A_-S)(q).
\tag{C13}
\]

weight4 Hecke q-expansion 的额外项含 p³，故

\[
\boxed{\mathfrak C_t(A_-)=R_p(t)A^{(\varepsilon)}(t)\pmod p.}
\tag{C14}
\]

现在使用 [正规目标积分稿](cdt_odd_level20_target_integral_20261006.md) 的 I_H、Y=p³H₋、Z=p⁴I_H，并只在 n<p² 的 integral prefix 上 reduction。已有真实源 packet 给

\[
Y\equiv A_-(t)F_{p,\varepsilon}(t^p)\pmod{p,t^{p^2}},
\tag{C15}
\]

其中 Fₚ,ε 是实际 f₋（ε=1）或 f₊（ε=−1）经 q(t) 后的 degree<p 截断。由逐系数正规积分，存在唯一 \(J_{p,\varepsilon}\in tk[t]/(t^p)\) 满足

\[
Z\equiv J_{p,\varepsilon}(t^p)\pmod{p,t^{p^2}},
\quad\vartheta J_{p,\varepsilon}
=\mathfrak C_t(A_-)F_{p,\varepsilon}\pmod{t^p}.
\tag{C16}
\]

唯一性来自1,…,p−1都是unit，且取零积分常数。不能把 J 的 slow-variable primitive 当成未正规化的 logt；其 constant 为0。

## 6. 必须保留的真实周期污染与下一限定接口

反证假设 L(3,χ₅)∈Q后，Θ及其真实系数共轭属于K；记 \(H^{(\varepsilon)}=A^{(\varepsilon)}(f^{(\varepsilon)}-\varepsilon\Theta)\)。由 (C14)、(C16) 得到明确的 bounded-kernel reduction

\[
\boxed{\vartheta J_{p,\varepsilon}
\equiv\frac{P_p}{D^{(\varepsilon)}}
 \{H^{(\varepsilon)}+\varepsilon\Theta A^{(\varepsilon)}\}
\pmod{p,t^p}.}
\tag{C17}
\]

所有 terms 都是实际形式或真实周期。\(\Theta A^{(\varepsilon)}\) 不能丢掉：A是weight2 carrier，本身没有此前 H 的 G=⟨T,W₂₀⟩ weight0 下降与共同 full-disk leaf；增加它或积分它，需要重证 actual rank、monodromy、cover 与完整分母。不能把 (C17) 直接简化成一个仅含 H 的廉价 Cartier primitive。

已经闭合的进展是：无限 p 的 integral packet 归约到两个固定分母、次数≤5的核空间以及明确的 period carrier。是否能利用其中的真实 de Rham 关系产生 pI_H 与三个 g-target blocks 的新增 primitive S2/S3/S4 行，仍需证明其完整 prefix 消除、共同 content、次数与 Smith 独立性；本稿不假设该收益。

## 7. 核验与范围

[新最小代数脚本](cdt_odd_level20_cartier_kernel_20261006_verify.py) 与 [证书](cdt_odd_level20_cartier_kernel_20261006_verify.json) 核固定 η权、Fricke coset 矩阵、显式 D 的次数与原点值、两种符号下因子平方及 Hecke constant。没有计算未知周期、没有扫描 p、没有重跑冻结 producer。全素数 modularity、divisor pole bound、relative Cartier 归约与 period-term 限制由本稿证明给出。
