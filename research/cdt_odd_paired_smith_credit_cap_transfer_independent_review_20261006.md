# 真配对格 Smith 信用与 cap 转移的正式独立审阅

2026-10-06，审阅者 /root/conifold_arithmetic_hypothesis。NEW 独审稿。本次所有旧/同行 mathematical producer 仅读，无执行、import、rerun。本文不把作者有限证书的 PASS 当全尺度定理。

## V1. 实际读取和精确版本

实际完整读取 quarter 新主稿 [Smith credit transfer](cdt_odd_paired_smith_credit_cap_transfer_20261006.md) 的 **sections S1–S10，equations S1–S17**，最终数学 SHA：

8b7368457b4e147e16a3de12e62db330ebaccc3b7da0faaa6e725842885d37b0。

实际完整读取 root 新 [CRT 整模型](cdt_odd_paired_residue_crt_integral_model_20261006.md) 的 sections1–6、R1–R21，SHA：

3265da7c600ef8c1624f4208448ec35d75e32d71d92d78f4576b2cfdd5cfbd33。

实际完整静态读 quarter NEW PY，SHA378962de4c7f87851dc2e942318277b92d66b24814af00db43f9df009331711d；其 NEW JSON SHAcf308c972e1279686684a641acc58a4a5c1d3d8382bce14c4ae5990c5d175e7f。JSON 初次 pretty 全输出、随后合并 compact 全输出均发生截断，未把它们称完整阅读；再分批完整显示并实际读取全部94 graph records、全部76 affine records及所有 metadata，最后两组输出均未截断。这里没有逐条手工重算94个 matrix rank。

本轮还实际读冻结 dual 稿 D1–D11所在的首110行，核准确 complementary-minor identity；冻结 budget稿含B13–B19的实际113行，核 small-x tail、uniform-PNT和whole-X transfer；冻结 combined review的Q6–Q7及其邻接实际41行，核以前安全费用和不交窗口。未冒称本轮全文重新读取这些旧稿、旧JSON或旧来源。

候选 quarter source receipt cb474624e3d458083a8c6907875b7108589b832f1f5cf17ce52a44f37e0cd8b5 已实际全文读。作者随后更新其尚未冻 receipt，本文不把未来最终状态提前列为已读，不嵌入其最终SHA，避免独审与来源收据循环。最终数学/PY/JSON已分别物理核 hash。

本独审没有新增PDF下载、PDF页面读取或外部源码；不能借用作者6页primary阅读作为本人阅读。本审阅者另外一个自有 operator 项目恰1次首次PASS364checks，与本次同行审阅数学执行0分开计。

## V2. Primitive weighted 图与第一层下界通过

实际 C 的每个 pair gcd1且 supports不交，连续 Newton evaluation为GL，故满射/kernel饱和。乘 j! 后列为两个整数节点上的 falling products；modp的 j≥p列确为0，首p列是全部p residues的可逆evaluation。这里p≤n保证真 head覆盖所有residues，并没有扩充degree<2n的自由源空间。

p²>8n保证所有相应factorial端点小于p²。写N=6n+1=hp+e、k=lp+r，则

\[
v_p(d_{k+1})=h+\mathbf1_{r\ge p-e}.
\]

若镜像carry不同，真实primitive row只有较高carry节点的系数modp非零。因此每个offcenter mixed block的rank至多1，原两coordinates预算为2；fixed residue不mixed且rank至多1，给rank≤p−M。Smith总和至少非零第一层个数，得到

\[
\delta_p\ge n-p+M.
\]

没有把p>n时的0/1 Smith结论延伸至p≤n；未知更高层只能增强下界。

精确 mixed 数 S8 是两个 reflection intervals 中 lower<τ≤upper 的数目；fixed点不mixed。p<n时除p=n例外不可能p|2n；通常 z+1=nZ、τ=nT−1，各正部误差≤1。若p|N，actual carry全同而continuous nT=1，仍O(1)；p=n时actual M=1、continuous d=0。故S4完整包含跳点而不删除未付例外prime。

## V3. 全prime真实 CRT 容量输入独核通过

R5通过各monic Q_r的unit resultants给GL_M(Z_p) CRT，local monic step-Newton basis到evaluation准确为 p^j j!binom(l,j)。其像是integer-coefficient polynomial像，不能偷换为普通integer-valued函数的全自由像。

Reflection同时保留inner长度a+1与outer长度a，offcenter的实际lift序为l↦L−1−l，centerloop长度偶。因而R11/R12是同一C!的真实direct-sum normal form。所有j!保留，ragged cutoff不补不存在的高jet。

Baseline加和R17可按a奇偶直接核：a=2u给pW_u+(b/2)w_u；a=2u+1给pW_u+((p+b)/2)w_u。其中w_j=j+v_p(j!)、W_u=Σ_{j<u}w_j，恰等于first-n factorial的valuation总和。p2与p>2n的极端亦包含。

p²>8n时mixed offcenter block一侧primitive coefficients为units，另一侧恰带p，且L<p令j!为unit。因此column weights强侧j、弱侧j+1，最便宜L列费用 floor(L²/4)，比baseline floor((L−1)²/4)多floor(L/2)。这自足证明R19，而无需任何未知Schur unit或Gram正常性。

R20 exact mixed counts和R21给S14–S15的同一capacity。x∈[1/4,1]时权重≤4，τ仅差1，或p|N时nT=1；b=0即p|n的边界同样包含，故额外信用的归一化误差uniform O(1)。S8现在是有已证CRT输入的定理；producer输出中的原条件历史保持不改是准确记录。

## V4. Whole-X转移与正费用方向通过

Primitive complementary minors给

\[
T_p=\sum_{i<3n}v_p(i!)-\delta_p.
\]

冻结B18来自实际S两侧Cauchy–Binet、指定Newton factorial除法和monomial共同minor下界，给whole-X Gauss valuation≥Λ_p−2T_p；另有entry bound−10n。因此在n/2<p≤n，δ0=n−p，S2降低T_safe至少M，合法新下界正是

\[
\max(-10n,\Lambda_p-2T_p^{safe}+2M).
\]

它针对整个形式X polynomial，不假设a,b为p-units，也不借specialized determinant非零。固定有理source或固定rational X的清分母分别付exp(O(n))，没有算免费gauge。

逐prime取旧合法界与新界最大，得到同一signed Q_n，D_A(X)/Q_n∈Z[X]；positive content亦保留。与已付n<p≤2n及3n<p≤6n两个window不交，Γ未在finite place再扣一次。

## V5. Cap后的精确收益独核通过

依S9把inner/outer tents加到12个实际raw affine段，再与−10取max。9个非零gain段及其crossing根与静态源码、全部76保存段吻合。源码先枚举floor boundaries，再加入所有min/max和cap crossing roots；在一个闭affine段只用端点核差，足以证明整个段，不以中点抽样推断完整区间。

独立手算三个正window的积分：

\[
\frac{32}{455175}+\frac{16}{79475}=\frac{16}{58905},
\]
\[
\frac1{100}+\frac9{1100}+\frac4{3971}+\frac1{722}
=\frac1{55}+\frac1{418}=\frac{43}{2090},
\]
\[
\frac1{8092}+\frac{23}{10404}+\frac1{252}.
\]

其总和为121537/4476780。安全费用 subtraction亦手核：共同分母17925027120满足旧分母104824720乘171、新gain分母4476780乘4004，两个numerators之差

\[
4624049789\cdot171-121537\cdot4004
=790225879771.
\]

故S3

\[
A_{\rm first}^{safe}
=\frac{790225879771}{17925027120}
\]

是已证明更便宜的安全上界。原raw在cap下的未列tent不能按裸面积积分。

## V6. M4和所有subhalf隐藏信用通过

在1/2<x<2/3，a=3的capacity只多一个inner tent，即length4 mixed block M4。直接核raw+4d_in在三个inner peak14/27、14/25、14/23的最大值分别为

\[
-280/27,\quad-314/25,\quad-330/23,
\]

全部严格小于−10，故这一额外layer在当前transfer中收益为0，不否定其实际Smith信用。

在[1/4,1/2]，静态完整piece覆盖中的所有weighted gain确为0；结合原raw literal rows、floor权重和全部affine crossing的完整纸面枚举证明，这不是有限prime/参数观察。x≤1/4的全尺度封口不用这76段：实际pairs总数n，Σfloor(L/2)≤n/2，因此e_cap≤1/2；加上冻结B13

\[
g_{\rm raw}+2e_{\rm cap}
\le-4/x+3+x/4
\le-207/16<-10.
\]

所以全部subhalf无遗漏tail收益。这里的0只针对这个明确safe bound模型；不能称actual cost lower或未来方法no-go。

## V7. PNT、finite验证与结论边界

Uniform O(1) residue/factorial/tent误差对p/n≥1/4有限types成立；p≤sqrt(8n)保留旧all-n界，费用O(n^(3/2)log n)。bounded piecewise-affine test function经θ和step/Riemann逼近给S13的liminf方向。例外小n及所有端点由实际finite valuation界覆盖，PNT没有替代整化。

Own peer certificate恰首次1PASS，94 graph cases/76 affine pieces；我只静态读，无执行/import。Graph有限检查不能证全n rank或高Smith；affine proof需S14真CRT前提。源码和JSON保留当时conditional字样，而最终正文在actual读root定理后解除，此历史无矛盾。

本次正式独审数学范围全部通过，无要求修订。已证是同一个D_A的whole-X信用和更便宜safe upper；无限auxiliary simultaneous units、determinant无限nonzero、strict margin和任何ζ/L数值新定理均仍未补。S17提出support-dependent Λ_IJ关联估计，准确保留为尚未兑现的下一接口。

本NEW独审全文自读后冻结；旧/同行producer执行、import、rerun为0，新PDF/外部源码为0。
