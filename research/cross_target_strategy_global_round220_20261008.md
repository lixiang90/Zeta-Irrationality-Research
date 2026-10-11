# 第220轮：跨目标载体、真实关系桥与算术 holonomy 投入次序

日期：2026-10-08。身份：round218_dual_audit 独立策略审查；本稿不改旧数学稿、主报告或 manifest。范围有限：比较已经冻结的 Jacobi、Legendre–Eisenstein 与 cyclotomic/polylog 接口，核五项 primary 文献中的必要选目，给出一个新的实际关系桥及其明确失败的现有费用表。**没有新的数值无理性或线性独立定理；固定 Jacobi gate218 仍未通过。**

## 1. 应纠正的投入顺序

CDT 的 direct holonomy theorem 可以直接作用于具有规定分母类型、在同一实际圆盘映射下亚纯延拓的 Q-Taylor functions，并不要求预先构造 Betti/Hodge 实现。其普通细化版 Theorem 7.0.1 在函数已知 holonomic 时要求

\[
\log|\phi'(0)|>\tau(b;e),\qquad
m\leq\frac{J(\phi)}{\log|\phi'(0)|-\tau(b;e)}.
\tag{S1}
\]

要由假设的有理数值关系得到矛盾，关键是该关系是否给出**实际的 Q-germ、同一图下的亚纯延拓、已证明的 Q(x)-秩，以及全 Taylor source 的算术费用**。未给出 holonomicity 时，还须满足原定理中 max\(\{\sigma_m,\tau\}\) 的较强条件。这里的 \(e_i\) 是逐项 \(n^{e_i}\) 分母，不是免费参数。[CDT 固定 v2，Definition 6.0.1、Theorems 6.0.2 与 7.0.1](https://arxiv.org/pdf/2408.15403v2)

因此，先前档案中列出的有理 Betti/Hodge 格、motivic realization 或 source-to-Betti map，只能作为特定方案可能需要的工具，不能被提升为所有 direct CDT 应用的硬门槛。投入次序应先核“目标有理关系 → 实际可延拓 Q-series”；再核全源费用及严格 holonomy quotient。若方案选择通过动机实现获得这一接口，则该实现必须实证；不能因为另一方案不用它而视为自动存在。

CDT 已证明的 \(1,\pi^2,L(2,\chi_{-3})\) 独立性，以及冻结稿中由已知近单位对数定理得到的 dilogarithm 组合，不是本项目新目标的完成。直接复现其映射、trace 或对数包，只有在目标关系进入实际 source 后才有研究收益。

## 2. 冻结接口：已有结构与未兑现收益

|接口|已经付清的内容|尚未付清的决定性内容|本轮判断|
|---|---|---|---|
|固定 Jacobi / positive whole-M|实际非零接口；无约束 exterior 正性和 compact beta-Gram 证书；冻结的联合源预算|实际 Jacobi-restricted、tail-projected 矩阵的下界/零估计，及完整 strict barrier|降级，不能把 unrestricted 证书移植成实际矩阵结论|
|Catalan Legendre rank3|\(x=\lambda(2\tau)\)、实际 \(U\) branch、\(L(U)=1/[16(1-x)]\)、Fuchs connection、带 log16 的 \(G\) endpoint、全源 prime-window flags|有理 \(G\) 是否消掉某个实际单值化障碍；统一 admissible 图与 strict quotient|继续有限接口核验；不凭 rank3 标签晋升|
|\(\zeta(7)\) symmetric-power rank8|正确 oldform \(E_8(\tau)/F^8\)、实际 Bol pullback、log-depth7、一个安全系数包、endpoint 投影|高权全 source 的联合算术改善和 relation-driven filling|降级为工具，不作为当前主攻数值路线|
|便宜对数/polylog padding|若干实际 ODE、秩证书、逐层分母和全源接口|增加的秩能否支付其新积分/共轭费用并改变严格指数|放弃冻结类型中的重复补行；不宣称全部 cyclotomic 方法不可能|

global216 的 \(L_{\rm arith}=-27323/4\) 与 \(U_{\rm mix}\approx-20.85527\) 不可用后续较好看的局部对象替换。round218 中 \(-7799.5\) 的条件性对象与 \(b_0\) 的 \(-2675.5\) 证书也不是可拼接的同一归一化对象；5124 差距未被关闭。以上冻结结论只限制实际已研究构造，不是无理性目标或所有载体的 no-go theorem。

低权全源稿的 \(N=3D\)、source rank \(3D+3\)、output rank \(3D+1\) 和 \(33D^2/4+o(D^2)\) index 上界是真实改进，但没有同时给出可用的 archimedean 严格上界。高权稿的 \(480\,7!d_N^7\) 是指定 Frobenius 系数包；不能把它当作已计算的 rank8 全源联合旗标。秩、log-depth 和 safe denominator 深度一起增加，尚未形成已核验的净 holonomy 收益。

## 3. Legendre 数值关系并未自动补 cusp

采用冻结低权稿的 \(P=x(1-x),F=\theta_3(2\tau)^2,B=F(1-x)\)，实际分支满足

\[
U=\frac{\pi^2F^2}{32B}-\frac{G}{2}F+
\frac{\pi^2B}{48}-\frac B4\widetilde K(\pi F/B).
\tag{S2}
\]

若假设 \(G=g\in\mathbb Q\)，则 \(U+gF/2\) 的初始 Taylor coefficients 确实有理；但它仍有

\[
\frac{\ell^2}{32}+O(1),\qquad
\ell=\log\frac{16}{1-x},
\tag{S3}
\]

这一实际 cusp 障碍。除去 endpoint 的 \(G\) 系数不等于除去整个 cusp。因而“endpoint 识别 + 有理关系”尚不能自动提供 direct CDT 所需的新图。

这是一个具体未付桥，不能被替换为“必须先做 Betti/Hodge”。可能存在更适合的已付 companion、trace、gauge 或其他实际组合；本稿没有否定其存在。但新组合必须给出完整 branch identity、Q-Taylor source 及图，而不能仅消掉一项首阶渐近。

\(\zeta(7)\) 的实际 numerator、rank8 和 log-depth7 同样只是 transport 的完成。把 \(\zeta(7)/\pi^6\) 的投影换成 \(\zeta(7)\) 的有理关系，必须保留 Tate scale；一个有理 de Rham/cohomology class 不会替代实际 endpoint 的这个检查。

## 4. 一个已付的普通 cyclotomic 关系桥

以下是本稿的有限新 paper 构造，目标仍是实际 Catalan 值，而不是复现 \(L(2,\chi_{-3})\) 的既有定理。设

\[
A(x)=\arctan x=\sum_{n\ge1}\frac{\chi_4(n)x^n}{n},\qquad
B(x)=\operatorname{Ti}_2(x)=\sum_{n\ge1}\frac{\chi_4(n)x^n}{n^2},
\tag{S4}
\]

则 \(A'=1/(1+x^2),B'=A/x\)，初始 branches 在 \(x=1\) 都全纯，\(B(1)=G\)。假设 \(G=g\in\mathbb Q\)，定义

\[
S_g(x)=\int_0^x\frac{B(t)-g}{1-t}\,dt.
\tag{S5}
\]

它有实际 Q-Taylor germ；在初始 \(x=1\) leaf 上，分子为零，所以该点可去。与 (S3) 不同，这里目标关系确实消除了新悬挂引入的局部奇点。

有完整有理 connection

\[
1'=0,\quad A'=\frac1{1+x^2},\quad B'=\frac Ax,
\quad S_g'=\frac{B-g}{1-x}.
\tag{S6}
\]

其 Q(x)-秩为4。证明不依赖数值关系：绕 \(i\) 的实际 monodromy 给出 \(\Delta A=\pi\)、\(\Delta B=\pi\log x+C\)。若 \(r_0+r_1A+r_2B=0\)，应用 monodromy 后，\(r_2\ne0\) 会使 \(\log x\) 有理，故 \(r_2=r_1=r_0=0\)。若 \(S_g=r_0+r_1A+r_2B\)，微分并按这三个独立函数比较得 \(r_2'=1/(1-x)\)，与有理函数导数无简单极点残数矛盾。因此 \(1,A,B,S_g\) 在 C(x) 上也独立。

还可付清一个完整实际图，而不只做局部补点。取

\[
\phi_\nu(z)=\tan\frac{\pi\nu z}{2},\qquad \nu=\frac34.
\tag{S7}
\]

它在闭单位圆盘邻域全纯，避开 \(\pm i\)，圆盘中 \(\phi_\nu^{-1}(0)=\{0\}\)、\(\phi_\nu^{-1}(1)=\{2/3\}\)，且 \(A\circ\phi_\nu=\pi\nu z/2\)。于是 \(B\circ\phi_\nu\) 的0点可去；唯一1点沿实段到达初始 \(B(1)=G\) leaf。假设 \(G=g\) 时，\(S_g\circ\phi_\nu\) 也全盘全纯。**这已经给出实际 relation → overconvergent Q-germ，而没有调用 motivic splitting。**

任意其他避开 \(\pm i\) 的图仍不能免除 branch 核验。绕 puncture 后到达另一0前像，\(B\) 可能有 log branch；另一1前像也可能位于 \(B(1)\ne G\) 的 leaf。(S7) 的唯一前像和实路径排除了这些问题，不意味着任意图自动满足它们。

## 5. 全 jet 费用：三种已付表仍不通过普通 gate

对固定 \(g\)，取固定正整数 \(c_g\) 使 \(c_gg\in\mathbb Z\)，以下类型施于 \(c_gS_g\)；固定倍数不改变秩。原系数恒等式是

\[
[x^N]S_g=\frac1N\left(\sum_{k=1}^{N-1}\frac{\chi_4(k)}{k^2}-g\right).
\tag{S8}
\]

因此 (S6) 的一种合法 CDT 类型是

\[
\sigma=(0,1,2,2),\qquad e=(0,0,0,1).
\tag{S9}
\]

两列 staircase widths 为1；外层 \(N\) 是 literal \(n^{e_4}\)。\(\tau_{\rm flat}=27/16\)，而实际 Definition 6.0.1 的

\[
\tau_\sharp(e)=\frac{2}{m^2}
\min_{0\le\xi\le m}\left\{\xi\sum_i e_i+
(\max_i e_i)I_\xi^m(\xi)\right\}
\tag{S10}
\]

给 \(m=4\) 单个 \(e_i=1\) 的费用 \(7/16\)；主文相应 example 的 minimizers 包含 \([2,3]\)。故 **总费用是 \(17/8\)，不是 \(27/16\)**。逐项系数只有一个多项式 \(N\) 分母，不意味着整个多项式 source / jet 无费用。

另有不使用 \(e\) 的安全半宽包：

\[
c_gd_N^2d_{\lfloor N/2\rfloor}\,[x^N]S_g\in\mathbb Z,
\qquad d_M=\operatorname{lcm}(1,\ldots,M),\quad d_0=1.
\tag{S11}
\]

逐 prime-power 证明如下。令 \(h=\max\{a:p^a\le N\}\)。若 \(N\ge2p^h\)，右侧三个 layers 足以清除 \(Nk^2\)。若 \(N<2p^h\)，则 \(d_{\lfloor N/2\rfloor}\) 至少有 \(p^{h-1}\)；\(N,k<N\) 不可能同时是 \(p^h\) 的正倍数，故 \(v_p(N)+2v_p(k)\le3h-1\)。固定 \(g/N\) 同样被包住。对所有素数包括2成立。相应 \(\sigma=(0,1,2,5/2),e=0\) 给

\[
\tau=\frac{3+10+7(5/2)}{16}=\frac{61}{32}.
\tag{S12}
\]

还可用更 aggressive 的 literal 表 \(\sigma=(0,0,0,2),e=(0,1,2,1)\)，其 flat 部分为 \(7/8\)。此时

\[
\tau_\sharp=\frac14\min_{0\le\xi\le4}\{2\xi+I_\xi^4(\xi)\}\ge\frac58.
\tag{S13}
\]

无需计算完整 minimum：\(0\le\xi\le1\) 时，\(I\) 的中间 harmonic integral 至少为 \(\int_2^3 1\,dt+\int_3^4(3/2)\,dt=5/2\)；\(1\le\xi\le2\) 时至少为 \(3-\xi\)，所以 \(2\xi+I\ge4\)；\(\xi\ge2\) 时 \(2\xi\ge4\)。其余两项非负。故这张表的总 \(\tau\ge3/2\)。这个 lower bound 已足够，未宣称完整 sharp minimum。

任何实际共同图都须避开 \(\pm i\)，因为 \(A\) 在二点有不可亚纯的 log branch。该 twice-punctured plane 在0的 conformal radius 是

\[
\rho=\pi F(1/2)^2.
\tag{S14}
\]

可直接用 \(i(2\lambda(i(1+z)/(1-z))-1)\) 的 universal covering 核对：\(\lambda(i)=1/2\)、\(\lambda'=\pi i\lambda(1-\lambda)F^2\) 给原点导数绝对值 \(\rho\)；cover lifting 与 Schwarz lemma 给所有这种图的 \(|\phi'(0)|\le\rho\)。这里使用的是冻结低权稿已核的 lambda/period 归一化，不是把 \(\lambda(2\tau)\) 的 factor2 忘掉。

以下是纯纸面严格界。\(F(1/2)\) 的 hypergeometric coefficients 递减，故

\[
F(1/2)\le1+\frac18+\frac9{256}
 +\frac{25}{256}\sum_{n\ge3}2^{-n}
=\frac{1213}{1024}.
\]

由 \(\pi<22/7\) 和指数级数前六项，

\[
\rho<\frac{32370118}{7340032}
<\frac{5711}{1280}<e^{3/2}.
\tag{S15}
\]

所以 (S9)、(S12)、(S13) 三种**已经付费**的类型，即使使用 a priori holonomic 的较弱条件，仍没有普通 Theorem 7.0.1 的正分母。这不是由一个粗糙图选择造成的；(S14) 对所有实际共同图给必要上界。更不能把未付 \(e\) 的 \(27/16\) 与 \(\log\rho\) 间约0.21的乐观差距当作真实 budget。

限定结论：三张表没有通过普通 single-map gate；没有证明所有联合源、trace、新坐标或更精细 CDT 变体失败。实际全 source 的 cancellations 可能改变费用，但必须重新证明。即使新费用令分母为正，也还必须证明 quotient **严格小于4**；\(\log\rho-\tau\) 的小差距不足以完成该判断。固定整数整体倍数的改善不会改变主指数；literal \(n\) 分母恰是必须计入全 jet 的反例，不能借“多项式因子”免单。

## 6. Primary 文献给予什么，不给予什么

选目限制为五项，没有扩大文献清单。

1. **CDT fixed v2**：直接数值路径的核心是 relation-driven Q overconvergence 与全源 holonomy bound；实际 \(L(2,\chi_{-3})\) proof 包括 trace、分母与独立函数，不能只摘取大映射导数。本稿只把它用于确定入场条件和 (S10) 的费用，未把既有 theorem 当新成果。[218页固定主文](https://arxiv.org/pdf/2408.15403v2)
2. **Brown, Mixed Tate motives over Z**：motivic multiple-zeta basis 和 period map 给组织关系的结构工具；数值 spanning 不等于数值独立性。若没有把实际数值关系提升成所需 motivic relation 的理由，motivic basis 不能证明 \(\zeta(7)\) 无理。[Annals 原文](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf)
3. **Deligne–Goncharov**：\(\mathbb P^1\setminus\{0,\infty,\mu_N\}\) 的 paths 提供适合 Dirichlet/cyclotomic periods 的类别和 branch 语言；规范 de Rham trivialization 本身不是自动的数值分裂。它支持写实际迭代积分载体，未给本项目免费的 rank/denominator gain。[作者公开稿 §5.1–5.2](https://www.math.ias.edu/files/deligne/Tate.pdf)
4. **Brown–Hain**：Bol quotient 与 rational Eichler–Shimura theorem 给 modular-symbol/BGG 类的实际 cohomology bookkeeping。所读 theorem 是 level1；不能据此免证 \(\Gamma_0(4)\) 的具体 source，也没有对 endpoint 关系的数值 injectivity 结论。[作者论文](https://arxiv.org/pdf/1708.00652)
5. **Brown, MMV §7.3**：Eisenstein 的实际 period cocycle 含 odd-zeta coboundary，而其 cohomology class 可在 Tate normalization 后有理。把该 coboundary 忘掉正好会丢失要研究的数值信息；用 class 的有理性替代实际 endpoint 是错误的捷径。[作者稿 Lemma 7.1 与 (7.3)](https://www.ihes.fr/~brown/MMVarchiveV1.pdf)

因此三类方法各有用途：mixed/cyclotomic Tate 整理 path 与 extension；modular symbols/BGG 整理 rational connection 与 cohomology；direct CDT 核实际 Q-series 的算术和分析界。它们不能互相替代未付的数值桥。

## 7. 下一窗口的有限判断

**继续**：把 (S4)–(S7) 作为一个已付 relation bridge 的基准。若主攻新 Catalan 定理，首项任务必须是构造比上述三张表更低成本或具有更好实际 geometry 的**完整 source**，同时保持该目标关系真正补点。交付应至少包含所有 rows/columns、实际 branch、统一图、全 prime-power / jet 费用及严格 quotient；先证明其中决定性的改善，再增加 rank。不要把仅有正分母或“差距很小”作为继续大规模投入的依据。

**有限目标储备**：\(\operatorname{Ti}_2(1/2)\) 等 ordinary rational argument 可以用 \(\int(B-g)/(1-2x)\) 做同类实际悬挂；\(1/2\) 是初始 branch 的普通点，且 (S7) 有唯一相应实前像。分母中新增 \(2^j\) 是整数 numerator，仍须核实际全源与分析预算。本稿没有完整核其无理性文献现状，不能宣称 novelty 或已有无理性；root 的搜索/README 定位也不等于 theorem 阅读。选择它之前先做这一现状核查。

对非主 real Dirichlet \(\chi\)，\(B_s(x)=\sum\chi(n)x^n/n^s\) 满足 \(B_j'=B_{j-1}/x\)，且 \(B_0=\sum_{a=1}^f\chi(a)x^a/(1-x^f)\) 在1可去；因此 ordinary-point suspension 是可审入口。conductorf 的更多 punctures、depths 和可能增加的 rank 都有费用。没有在本轮核完整新目标 source，也不把这个形式入口称为新数值定理。

对 odd \(\zeta(s)\)，\(\operatorname{Li}_s\) 在1仍有 branch：仅减去 \(\zeta(s)\) 的值不能消除 \((1-x)^{s-1}\log(1-x)\) 项。因而 Catalan 的 ordinary-point 补点机制不能未经 monodromy 核验直接搬去 \(\zeta(7)\)。高权 symmetric-power route 暂不再用扩大 rank/log-depth 冒充进展。

**降级**：固定 Jacobi 的 unrestricted exterior 正性、Legendre 的已完成 transport，以及混合 Tate/motive splitting 推测，都保留为准确工具或条件入口。若下一轮没有 actual restricted 零估计、完整联合源费用或真实 filling 的变化，不提升数值目标状态。

**放弃限定操作**：继续重复既有近单位对数 corollary；在冻结便宜 polylog 类型中增加未付积分行；用 endpoint 的单一系数取消宣称全部 cusp 已补；把 motivic splitting conjecture、cohomology class 有理性或 rank 标签当作数值证明。这个判断不扩张为所有 cyclotomic/trace/新坐标路线的禁止。

## 8. Read scope、身份与 run ledger

本轮 FULL 阅读：global216 的6节，round219 source-flags 报告全篇，低权 integral-flags 的7节，CDT mechanism 的7节、odd low-cost 的7节、repository-carriers 的6节。低/高权主稿是在 round219 已 FULL 最终审读的冻结版本；本轮针对上述接口对照，未把作者读冒充独审。身份在本轮再次核 SHA256。主稿低权的独立 FULL receipt 已另存；高权稿由本 agent 作者读、root 独立 FULL 审，不交换角色。

|本地文件（research/）|Bytes|SHA256|
|---|---:|---|
|research_global_review_round216_20261007.md|8957|60119f1598fa41ff07a23223a181735d34c23f9611e796df9ae885b2f9431450|
|cdt_legendre_source_flags_round219_20261008.md|7186|9e705169df37dc88edab27de45d1c6efae9ffdfb24f0a44f52b6355f96bab5af|
|eisenstein_legendre_integral_flags_round219_20261008.md|15599|bc41296fb85c5548adae93d25cde5f9e4983f5d223ada8e6a39cd1b87b765730|
|period_holonomy_cdt_mechanism_20261005.md|16857|27483fbfe9d54e0e2bbe982d6959da4586bd9e7490bbb2b64c5c6301e3478299|
|cdt_odd_low_cost_polylog_20261006.md|12751|9b81a5252d54f32f7c8a502ce5a2550df782cbee88b903c4b3f9bde21e1d2ca2|
|cdt_new_repository_carriers_20261007.md|15074|06593d42003f6d8e22667a86cc437c560ea8559248a8196e7071c989517eb904|
|eisenstein_legendre_catalan_connection_round219_20261008.md|13940|67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39|
|eisenstein_symmetric_power_transport_round219_20261008.md|15514|32910f3ad35dcf3307786b75764ae024a4eaca2d32eec013e482be99e177aaee|

Primary 实读范围（都不是 FULL 全文）：CDT fixed v2 的 Theorem A、完整 Theorem 2.5.1、Definition 6.0.1 / Theorem 6.0.2 输入与费用、单 \(e_i=1\) 的 m4 example、完整 Theorem 7.0.1，以及 §14 末实际关系桥和 §15.1.10 起始相关段；Brown Annals intro Theorem 1.1 / Corollary 1.2 与 §2.2 Definition 2.1 / Remark 2.2；Deligne–Goncharov **91页作者稿** §5.1–5.2 及相邻必要段；Brown–Hain intro Theorem 1.2 / Corollaries 1.3–1.4 与 Proposition 2.2 的 Bol proof；MMV **49页作者稿** 完整 §7.3 Lemma 7.1、(7.3) 及其说明。CDT fixed 主文为218页；未把20页 arithmetic2025/effective2026 当作主文或声称本 agent 读过其全篇。

程序 ledger：数学程序0；数值网格0；symbolic/CAS0；prime scan0；PSLQ0；Lean0；Git0。使用 documentary 文件全文读取、metadata/SHA256、公网 primary 选目浏览和本 NEW Markdown 写入。所有 (S4)–(S15) 的等式、秩与不等式为有限纸面推导。\(\tau_\sharp\) 的完整 aggressive minimum 未求；对其只使用 (S13) 已证明的 lower bound。未改旧稿、main 或 manifest；本稿 final saved author FULL 阅读与外部 hash 单独登记，不在正文自指写入 hash。
