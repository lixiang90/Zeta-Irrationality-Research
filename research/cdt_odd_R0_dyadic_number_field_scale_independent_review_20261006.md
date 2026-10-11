# R₀ 的 \(8\sqrt2\) 数域缩放：独立全文审阅

日期：2026-10-06。NEW 独审，和已冻结 C16/A/S review 分开。全部旧/同行数学文件只读；本独审无数学 producer 创建、执行、import 或重跑。

实际全文读 [数域缩放补充](cdt_odd_R0_dyadic_number_field_scale_supplement_20261006.md) 初稿7af55；指出其最后 reference 的“同一个 \(L=\mathbf Q(\sqrt2)\)”与一般 \(L=K(\sqrt2)\) 不一致。作者在未冻 NEW 稿修正为 \(\mathbf Q\to\mathbf Q(\sqrt2)\to\) actual 同一个 \(K(\sqrt2)\)。已再次实际全文回读最终 SHA

5a800387513a2f6593087991d5371dbfca47eb8c6c1b74971fe13e3965f4c2b3。

**K1–K14 的有限位整化、所有 embeddings 的 source 比较、rank/degree 费用、完整预算和条件类内 product-formula 最优性均通过。** 这是另一份付清数域费用的整模型，不删除已冻 C16 证明的历史范围；没有数值无理性反证。

## J1. 真正使用的是更强 dyadic 纸面界

已有全阶界为
\[
 b(n)=2n+2v_2(n!)-\lfloor n/2\rfloor,\qquad
 b(n+6)+4\le\tfrac72n+25 .
\]
先选 fixed rational integer d0，使 d0q在 \(\mathcal O_K\) 中。paired rows 对每个2-place、按 \(v_2(2)=1\) 归一，都有
\[
 v_2(d_0c_n)\ge-\tfrac72n-25.
\]
这来自每项 convolution/derivative 的全阶证明，不是由较弱 \(16^n\) 前缀倒推。原 \(D^{7}\)/\(D^{6}\)、\(P_3(n)=3^{4\lfloor\log_3(n+6)\rfloor}\) 费用继续保留。

令 \(L=K(\sqrt2)\)、\(a=8\sqrt2\)。\(a^2=128\) 说明 a是非零代数整数，对任意2-place有 \(2v_2(a)=7\)，所以即使ramification index改变，归一化valuation仍为7/2。odd-place则 \(2v_p(a)=v_p(128)=0\)。据此
\[
 2^{25}d_0a^nP_3(n)D_{n+6}^{s}c_n\in\mathcal O_L,
 \qquad s=7\text{ 或 }6
\]
是所有 finite valuations 分别非负的结论。它不是仅在一个2-adic embedding成立，也不是平均 norm 的结论。

前缀用 \(a^N\) 也合法：\(a^{N-n}\) 为algebraic integer；\(P_3(n)\mid P_3(N)\)、\(D_{n+6}\mid D_{N+6}\)，故同一个前缀整化因子覆盖全部 \(n\le N\)。q未获得免费整性。

## J2. Literal ε species仍支付小素数和shift

K5沿用已独核 A14a/b 的真实整除转换：固定ε后，用fixed dε清除finite shift和P3；six cutoff1列、one cutoff6列乘1+ε，再加four cutoff1 ε列。每个
\[
 \widehat f_i(s)=2^{25}d_0d_\varepsilon f_i(a s)
\]
的coefficients是这些LCM的algebraic-integer numerator，常数1行乘同一fixed scalar仍是integer。其
\[
 \tau_\varepsilon=(1+\varepsilon)329/50+3.96\varepsilon
 \longrightarrow329/50
\]
通过。固定dε无D²主项；不能把这个ε转换说成精确P3因子本来不存在。

在每一个固定finite place，LCM的valuation是O(logn)，P3也如此；因此变换后的series在开单位盘收敛。这里“subexponential”指各固定p-adic norm，不指global rational denominator的增长。

## J3. 所有复嵌入的source与两个符号

g1、g2、Fi的coefficients为有理数，因此对任意 \(\sigma:L\hookrightarrow\mathbf C\)，
\[
 \sigma f(q)=f(q_\sigma),\qquad
 q_\sigma=\sigma q,\qquad
 a_\sigma=\sigma a=\pm8\sqrt2.
\]
非实际选定period的qσ仍是需要检查的conjugate analytic packet，不能用实际一个embedding的period图像替它们作证。

必须实际选 \(\phi_\sigma\) 使该qσpacket的pullback meromorphic，并满足原holonomy theorem的boundary/radial-limit hypotheses。取
\[
 \psi_\sigma=\phi_\sigma/a_\sigma
\]
才有exact source identity
\[
 \widehat f_i^\sigma(\psi_\sigma)
 =2^{25}d_0d_\varepsilon f_i(q_\sigma)(\phi_\sigma).
\]
source参数和canonical germ都吻合，包括a的负号嵌入。没有只用 \(|a_\sigma|\) 忽略参数符号。

每个σ的绝对值均为 \(2^{7/2}\)。derivative log及Bost–Charles double integral都减
\(\rho=(7/2)\log2\)。两个边同时付费正确。finite maps取identity，不能额外加正conformal size。

## J4. Rank保持10；扩域的weights不能重复计容量

已有实际rank证在 \(\mathbf C(t)\) 上给nine rows rank9、含1rank10，且每个fixedq都成立。限制scalars到L(t)、或作invertible L-rational change \(t=a s\)，保持这些独立函数和holonomicity。这里没有额外函数被制造。

用所有complex embeddings逐个计数时可取 \(w_\sigma=1/[L:\mathbf Q]\)；将complex conjugate pair合并并给权2/[L:Q]是等价约定。任意K-embeddingτ恰有[L:K]个extensions，所以
\[
 \sum_{\sigma|K=\tau}w_\sigma=1/[K:\mathbf Q].
\]
这就是K11。integer auxiliary lattice的Z-rank虽乘field degree，normalized Arakelov degree也除该degree，有效holonomy rank仍10。K已经含sqrt2时没有第二份extension收益；没含时也不能把rank10自动记成20。

## J5. 实际预算、有限条件类内最优性及reference

在全部 arithmetic/analytic hypotheses都满足、\(L_\rho>329/50\)时，先取fixedε使 \(L_\rho>\tau_\varepsilon\)，应用all-place inequalities再取ε→0，得到
\[
 10(L_\rho-329/50)\le A_\rho,\quad
 A_\rho=\sum_\sigma w_\sigma I(\phi_\sigma)-\rho,\quad
 L_\rho=\sum_\sigma w_\sigma\log|\phi_\sigma'(0)|-\rho.
\]
与rational C16版之差精确是 \(\log16-\rho=\tfrac12\log2\)。这仍是假设有合格全部σmaps后的holonomy约束，未构造新的capacity反证。

K14的product formula亦通过。对非零algebraic scale b，若每个2-place要求 \(v_2(b)\ge7/2\)，每个odd-place要求 \(v_p(b)\ge0\)，按 \(\sum_{v|p}[L_v:\mathbf Q_p]/[L:\mathbf Q]=1\) 归一，则平均arch logcost至少ρ；a达到该下界。该条件类最优性不证明actual coefficients必须具有该下界，也不排除改变整数模型后更低费用。

纠正后的reference argument现在严格在同一field：f0定义于Q，经a变换定义于Qsqrt2，再baseextend到actual同一L=Ksqrt2。它仍有相同rank10和费用。若map family对q共同，在reference上使用完全相同L-σmaps和weights，也已强制同一预算。因此扩域/缩放改进不能单凭共同domain排除actual q代数。这个限制只在共同domain假设下适用；不否定另一份value-sensitive domain的可能性。

## J6. 阅读、修订和执行

* 7af55初稿实际全文读、独核，发现samefield文字问题并通知作者/root；5a800最终稿再次实际全文读，修正段和其余全文均确认，无旧稿更改。
* all-odd A稿最终439a全文独核、S稿bde766全文独核，记录见已冻 [A/S independent review](cdt_odd_R0_all_odd_radius_independent_review_20261006.md)，SHA b2cb52c650e517ed3aff06e554747e77f21ef8aea1d22e5c078529a837ca09ef。
* 本轮实际CDT archived primary PDF3–8：normalized local weights、rank m(D+1)、VD线性截断及slopes主项。此补充未新增PDF下载，也未冒记又阅读全文。
* 最终source Get-Content/hash首次自动审批deadline超时，命令未启动；工具明确允许retryonce，重试后已成功实际全文读取。这是源文件读取，数学producer执行数仍0。

本独审不证明actual q代数/超越、不将 \(\pi^2(R_0-M_0)\) 与 \(R_0-M_0\) 的有理性等同、不把扩域degree当新rank、不声称actual denominator最优。没有新的ζ/L/Catalan数值定理或Lean。
