# 真实 conifold 算术假设稿的实际全文独立审阅

日期：2026-10-06。审阅者：toric_chow_completion。NEW 纸面独审；旧/同行数学 MD/PY/JSON/manifest 只读，没有执行、import 或改写任何 mathematical producer。

## 1. 固定版本与审阅结论

实际全文审阅：
[主稿](cdt_odd_R0_conifold_actual_arithmetic_hypotheses_20261006.md)，17526bytes，SHA256 83e5fb5cb3e7cad72440d04e4f75230c895d2865bc68c1565160a6c3b313d567。

核 A1–A28 与 §§A1–A12。结论：**在作者明确的输入与声明范围内通过**。正结果是实际 dual germ仅要求一个初值、non-split rank5最小性、五行全部前缀整化，以及真实 Tate-lift/gauge/constant-translation 限制。它不证明数值无理性，不识别 actual compact scalar与 \(\Psi\)，也不把五行 packet与另加常数1后的CDT模型混同。

## 2. 实际读取的冻结输入和 primary

本次实际全文读 [中心算术稿](cdt_odd_conifold_arithmetic_center_20261006.md)，SHA256 10c1e882a7cc75b2f8b6be82ed6c241ec3900db07109ff144c041cc734f3e7b0；核其 conifold coefficient recurrence、三个 canonical germs、local G-basis 与 geometric FR scope。没有运行它的旧 PY/JSON verifier。

[Kummer 接口](cdt_odd_R0_kummer_period_interface_20261006.md)已在本轮前序独审实际全文读，SHA256 803b3eced9825fe5f40005728430188e36c4a8cd123d41223972cceb23c2e172，采用其 actual rank5/non-split 及完整 conifold log projection；[Yukawa 稿](cdt_odd_R0_Yukawa_scalar_interface_20261006.md) final SHA256 172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15 已逐式独审并另存冻结 review。本审阅采用已核准的 concomitant、actual node period和PD/cup convention。

冻结正切稿本轮已实际全文读；主报告 §§68–72 和delivery的全部R₀新状态亦实际读，确认 raw/compact comparison仍未完成。

本次实际整页读：
[FR published 原件](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)，PDF2、3、4、5、9，12页原件143655bytes，SHA256 c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68。PDF2–3明确 geometric因子乘积及无条件定理，PDF4 local Nilsson–G basis，PDF9 finite bad-prime \(C^{n+1}\) 费用。还实际全文读 [原FR receipt](../literature/manifest_cdt_odd_conifold_arithmetic_20261006.json)。没有宣称读完12页原件。

[KLM published 原件](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf) PDF13–14本次实际全文页读；SHA256 8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9。PDF13（printed386）明确 \(p=n=4\) cohomological factor为1、Tate ambiguity为 \(H^3(X,\mathbf Q(4))\)，膜因子为 \((2\pi i)^4\)。PDF18–19只采用前序任务已实际读的scope，不认领本次重新读取。

本次没有新下载PDF；Python fitz只用于整页抽取和hashlib元数据，非数学producer。

## 3. Endpoint concomitant 与单初值 dual germ

令 \(t=1-x\)。实际 \(\theta f(1)=-f_1\)、\(\theta^2f(1)=2f_2-f_1\) 代入 Euler concomitant，含 \(1-x=t\) 的两项在analytic germs中趋零，得到
\[
 \mathcal C(f,g)(1)=
 f_0(2g_2-\tfrac32g_1)-g_0(2f_2-\tfrac32f_1).
\]
所以 A5 配对矩阵正确；其 radical为 \(g_1+\tfrac34g_2\)。Actual node首项 \(-\pi^2t\) 与已核 \(b=3a/4\) 给
\[
 g_\delta=-\pi^2(g_1+\tfrac34g_2)
\]
为完整local germ身份，非仅两个Taylor coefficients的拟合：三初值唯一递推和analytic vanishing period已固定余项。

对 \(S=\mathcal C(\Psi,g_2)\)，端点为 \(2\alpha_0\)，而全函数concomitant身份给
\[
 \theta S=\sqrt{x}g_2/16.
\]
因此
\[
 S(1-t)=2\alpha_0-\frac1{16}
             \int_0^t g_2(u)(1-u)^{-1/2}\,du.
\]
\(g_2=t^2+O(t^3)\) 给nonconstant首项 \(-t^3/48\)。所有nonconstant coefficients为有理数，constant为 \(2\alpha_0\)，故A10的全部coefficient algebraicity等价成立。这里确实只消去 \(\alpha_1,\alpha_2\)，没有免费改变原 \(\Psi\) 的格。

## 4. A4 的 adjoint、non-split 和实际最小阶

独立算
\[
 L=(\theta-\tfrac12)P,\quad
 L^*=-P(\theta+\tfrac12),\quad
 \sqrt{x}\theta\sqrt{x}^{-1}=\theta-\tfrac12.
\]
于是
\[
 -\sqrt{x}L^*\sqrt{x}^{-1}
 =\{(\theta-\tfrac12)^4-x\theta^4\}\theta
 =K\theta=M.
\]
A12顺序正确；不是把非commutative operator factors颠倒。Formal adjoint的solution duality通过Lagrange concomitant，Kummer gauge再作rank1 twist，所以冻结 \(L\) 的non-split extension确实变为
\[
 0\to\mathbf C\cdot1\to\operatorname{Sol}(M)
       \xrightarrow{\theta}\operatorname{Sol}(K)\to0.
\]
Kernel准确为常数；局部antiderivative给onto；quotient由connected \(\mathrm{Sp}_4\) 输入绝对不可约。

\(\theta S\ne0\)，故其monodromy span在quotient上满四维。若span只有四维，就与kernel不交并给invariant complement，违反non-split；故span五维。任意order≤4 rational scalar annihilator的solution space不能包含该五维orbit，因此最小阶恰5。对每个 \(F+q\) 相同，证据不依赖constant取值。

Finite-cover部分也通过：先取Galois core，使cover monodromy为normal finite-index subgroup；quotient仍不可约。若存在subgroup-equivariant splitting，有限quotient共轭平均给原群equivariant splitting，矛盾。这里可以除有限degree，因为在characteristic0；不产生免费integral splitting。

A15五行等于 \(S,16\theta S,16\theta^2S,16\theta^3S,16\theta^4S\)，故其 \(\mathbf C(x)\)-线性独立由上述最小阶直接成立。主稿未借此计算另加常数1的更大packet；本独审也不扩大该rank5结论。

## 5. A6 的完整五行 all-prefix 整化

FR定理不能仅由“有理Taylor解”应用。这里真正几何 \(P\)、local Nilsson–G basis和algebraic initial normalization给 \(g_2\) 本身为G-function；它直接解order4的 \(P\)，不需要用去log部分的order16安全上界。Conifold整数exponents使 \(b=1\)，因此
\[
 D_{n+b_0}^3C_g^{n+1}[t^n]g_2\in\mathbf Z
\]
正当，有限bad-prime指数项仍保留。

卷积中的 \(k\le n-1\) 系数可由
\[
 D_{n-1+b_0}^3(4C_g)^n
\]
共同整化：它包含每个 \(D_{k+b_0}^3C_g^{k+1}4^{n-1-k}\) 的分母。积分再除 \(16n\)，\(n\mid D_{n+b_0}\)，故A19全 \(n\ge1\) 成立；\(n=0\) 是零项。不是有限前缀检验。

\(\sqrt{1-t}\) 的全部coefficients可由 \(4^n\) 安全整化（\(n\ge1\) 时 numerator \(\binom{2n}{n}/(2n-1)=2\,\mathrm{Catalan}_{n-1}\) 为整数）。所以 \(u=\sqrt{1-t}g_2\) 有相应 \(D^3\) 卷积界。前三次 \(\theta=-(1-t)\partial_t\) 只付整数derivative ratios、读到 \(N+3\)；主稿
\[
 \Delta_N=16d_0D_{N+b_0+3}^{4}(4C_g)^{N+4}
\]
覆盖五行所有 \(0\le n\le N\)。\(S\) 的constant由 \(d_0\alpha_0\in\mathcal O_K\) 支付。固定shifts不改变主率，\(C_g^N\)确实改变主率，因此A21的 \(4+\log(4C_g)\) 安全界正确。未求effective最小 \(C_g\)、Smith或CDT optimum。

## 6. A7 的 finite-algebraic differential gauge no-go

主稿dual projection使用actual \(g_2\) 及derivatives。\(g_2\) 作为不可约rank4系统的nonzero solution不能algebraic；因此这不是 \(\overline{\mathbf Q}(x)\) 内免费gauge。有限cover保持connected \(\mathrm{Sp}_4\)，也不能改变这一点。

若algebraic-coefficient scalar differential row \(T\) 杀nonzero \(g_1\)，在其有限代数coefficient field上右除以 \(P\)，得 \(T=QP+R,\ \operatorname{ord}R<4\)。若 \(R\ne0\)，就是该cover上的order<4 annihilator，违背最小四阶；故 \(R=0\)。因此 \(T\) 杀全部 \(\ker P\)，尤其 \(g_0\)。A22通过，且其实仅 \(Tg_1=0\) 已足够。

该结论限制的是algebraic differential row及所有initial coefficients的消去；不排除作者新建dual/tensor packet并另行支付分母费用。主稿已正确分清两者。

## 7. A9 的 actual δ-lift scale 与 normalization 盲区

采用真实compact node sphere \(\delta\) 和KLM的
\[
 r\mapsto r+(2\pi i)^4\operatorname{PD}\delta .
\]
PD-first cup约定使scalar shift确为actual \(\int_\delta\omega\)。所以
\[
 -\frac{(2\pi i)^4}{16(2\pi i)^3}
          (-\pi^2v)
 =\frac{i\pi^3}{8}v.
\]
A26因子和正号正确。它保持endpoint、holomorphic conifold germ与forcing，但改变一阶jet的已知transcendental量。两种许可lifts不可能同时Taylor algebraic。

Middle intersection alternating给 \(\delta\cdot\delta=0\)，故这个shift还保持与 \(\delta\) 的regulator evaluation。Derivative、端点及一个vanishing normalization因此不足以标记所有jets。该证据使用actual integral sphere及rational Tate ambiguity，独立于尚未证明的compact/raw scalar equality。Dual projection确实看不见该shift，因为 \(\mathcal C(v,g_2)=0\)。

## 8. A10 的 target尺度与constant-translation 限制

若 \(R_0-M_0\) 是nonzero algebraic，则 \(\alpha_0=\pi^2(R_0-M_0)/16\) 已知transcendental；若差为零才有 \(\alpha_0=0\)。所以“差有理”不能一概推出本稿single-jet arithmetic hypothesis。将整个dual germ除 \(\pi^2\) 也不合法：首个nonconstant coefficient成为 \(-1/(48\pi^2)\)，已非algebraic。

\(F\) 自身无条件为rational-coefficient G-function。每个algebraic \(F+q\) 都有同样rank5、相同nonconstant coefficient bound和branch differences；constant在continuation中相消。因此一个只依赖这些共同数据的criterion不能独自排除实际 \(2\alpha_0\) 为某个algebraic constant。该限定没有扩大为“任何CDT或global marking方法不可能”的声明；真正需要额外endpoint/Betti relation或值敏感period packet。

本稿只给统一safe denominator bound，未声称constant translate下所有finite-place Smith矩阵或所有norm budgets逐项相同。保留这一scope后A28及作者提出的必要额外数据通过。

## 9. 最终状态

独审通过A4 non-split dual最小阶、A6全五行全prefix整化、A7 finite-algebraic gauge no-go、A9 actualδ许可lift尺度、A10 constant-blindness，以及其余A1–A28的纸面身份。

本次未运行peer/旧producer，没有数值samples、PSLQ、Lean或新的无理性/线性无关性定理。Actual source page范围和冻结输入已逐项区分；本review自己的全文回读不冒认另一份独审。下一仍须标记actualcompactlift、保留端点敏感关系并核更大packet与原格费用。

