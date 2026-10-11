# 第235轮：同一三维源的多图和公开凸性判据

2026-10-08，A。数学程序0。实际读取当前220页CDT原文的相关完整页后，对冻结234的同一
\[
V=\operatorname{span}_{\mathbb Q(u)}\{1,E,J_g\},\quad
E=\operatorname{atanh}\sqrt{3u}/\sqrt{3u},
\quad J_g'+2J_g/(1-4u)=-2E
\]
作一次有界核查。假设g∈Q；实际秩3与holonomicity已付。本文关闭的是下列公开显示公式在既有费用下的入口，不是所有更强CDT或所有联合整模型的no-go。

## 1. 精确的同对象条件

固定u坐标、完整V以及固定Q(u)的Taylor basis。任何共同图φ均须holomorphic D→C、φ(0)=0、φ′(0)≠0，并使完整basis的pullbacks meromorphic。固定有理换基不改变共同meromorphy，故234的全图cap仍适用：
\[
c=|\phi'(0)|\le C_*:=3\pi^3\sqrt2/8<18<e^{7/2}.
\tag{P1}
\]
不要求原点仅有一个前像，允许已付的foreign even-origin叶。

原文§§6–7的literal类型是每一项系数以n^{e_i}乘若干LCM清整，LCM列为若干leading zeros后接同一常数。其费用为τ=τ♭(b)+τ♯(e)。Theorem8.0.1允许任意非负矩阵，并以τ♭♭(b)+τ♯(e)代替；不是把安全upper自由换成较小费用。下文首先以同对象τ≥7/3为输入，最后登记本轮算术证明的实际范围。

Theorem6.0.2要求每张图对全部函数共同meromorphic；按导数严格递增排列，最后一图须log c_l>τ。若未预先知道holonomicity，尚有更强的σ_m门槛；本V已有holonomic连接，可以用放宽版。Theorems7.0.1、7.1.6、7.1.10、7.1.13、7.6.4亦保留positive denominator条件。Theorem8.0.1在已holonomic时要求log c>τ♭♭+τ♯。源rank、关系填点和每张图的共同叶仍须实际支付。

以下全部边界积分首先只对原定理合法的closed-disk图使用，即φ在closed D某邻域holomorphic、完整pullbacks在那里meromorphic；Theorem6.0.2原式的D有overline，text extraction会漏掉。原文Lemma7.4.1允许通过φ_ρ(z)=φ(ρz)、ρ↑1处理open D。此时每个Jensen、BC或Γ下界先在ρ<1的闭盘上证明，再按原判据的径向limit/limsup传递；不把任意open-D函数的点态边界L¹值直接代入Jensen，以免丢掉singular mass。所有导数cap对缩小图仍成立；无有限积分的图不凭发散项产生有用证书。

## 2. Theorem6.0.2：真正的逐层多图也不能绕过门槛

令λ_k=log c_k，λ_0<⋯<λ_l，0=γ_0<⋯<γ_{l+1}=m，
\[
t_k=\gamma_k/m,\qquad w_k=t_{k+1}-t_k,\qquad
\mu_k=\int_{\mathbb T}\log|\phi_k|\,d\mu_{\rm Haar}.
\]
Jensen给μ_k≥λ_k。原文patch函数g在第k块具有分布log|φ_k|、质量w_k。因此对每一对块应用max的凸性，
\[
\iint_{[0,1]^2}\max(g(s),g(t))\,dsdt
\ge\sum_{i,j}w_iw_j\max(\mu_i,\mu_j)
\ge\sum_{k=0}^l(t_{k+1}^2-t_k^2)\lambda_k.
\tag{P2}
\]
后一式是λ_k有序时的精确离散恒等式，故右边等于
λ_l−Σ_{k≥1}t_k²(λ_k−λ_{k−1})。

当前原文(6.0.10)的switch系数确为1/m，已图像核对，并非1/m²。因此完整分子Q₆满足
\[
Q_6\ge\lambda_l+
(m-1)\sum_{k=1}^l t_k^2(\lambda_k-\lambda_{k-1})
\ge\lambda_l.
\tag{P3}
\]
这处理了每层改用另一张图和其实际switch费用，没有把判据替换成单图界的凸组合。只要分母positive，欲令Q₆/(λ_l−τ)<m仍必要λ_l>mτ/(m−1)。取m=3、τ≥7/3，仍要求λ_l>7/2，与(P1)矛盾。

## 3. §§7–8的径向凸性：完整负项尚留下log c

记T(r)=∬log|φ(z)−φ(rw)|、λ=log c。先对w作Jensen，再对z作Jensen，即有
\[
T(r)\ge\int_{\mathbb T}\log|\phi(z)|\ge\lambda,\qquad 0<r\le1.
\tag{P4}
\]
这与外来零点存在与否无关。原文Lemma7.1.4证明T对log r凸且非减。

Theorem7.1.6额外要求末斜率α_l≤m，因而全部
α_k=(T(r_k)−T(r_{k−1}))/log(r_k/r_{k−1})在[0,m]。
其完整分子为
\[
Q_{7a}=T(1)-\frac1m\sum_{k=1}^l
\alpha_k^2\log(r_k/r_{k-1})
\ge T(1)-\sum_k\alpha_k\log(r_k/r_{k-1})
=T(r_0)\ge\lambda.
\tag{P5}
\]
不能违反α_l≤m后仍使用这张显示公式。Theorem7.1.10的连续版本要求Â(1)≤m；其分子是
∫log|φ|+∫Â(1−Â/m)dr/r，亦至少λ。

Theorem7.6.4要求(7.6.5)的线性系统有唯一的非负解s*，且Σs*_h=1；该条件并非自动。它的完整分子恰为
\[
Q_{7b}=\sum_hs_h^*T(r_h)\ge\lambda.
\tag{P6}
\]
原文Theorem8.0.1的(8.0.3)、(8.0.4)、(8.0.5)分别是基本、(P5)、(P6)的同一分子，只更换算术费用。对原先leading-zero类型，Remark8.0.6证明τ♭♭=τ♭；任意矩阵的费用下界须另外付清。因此在τ≥7/3时，这三类完整显示公式都仍必要λ>7/2。

## 4. Binomial metric公式也有一个可证的绝对下界

Theorem7.1.13还使用原生共同收敛盘|u|<R与一张共同图φ，不局限于同一φ的径向缩小。以下核其显示公式(7.1.14)，不扫描metric参数。

固定r>1、η>0、μ∈R（用η代替原文参数λ，以免与log c混淆），置
\[
\Gamma(x)=\max_{0\le v\le1}\{vx-\eta v^r-\mu v\}.
\]
它是凸、非减函数，所有斜率在[0,1]。记
\[
a=\log c,\quad b=\log R<a,\quad \mu\le b,\quad
T=\int_{\mathbb T}\Gamma(\log|\phi|),\quad
q=\Gamma(a),\quad s=\Gamma(b),\quad
 u=\min\{1,((b-\mu)/(\eta r))^{1/(r-1)}\}.
\]
原定理另要求u<1、u≤v_T:=(T−s)/(a−b)≤m；positive denominator给a>τ≥0。Jensen与Γ凸性给T≥q。

令完整显示分子为
\[
N_m(T)=\frac{2\eta}{r+1}+\mu+2T-\frac2m S(T),
\]
\[
S(T)=\frac{(T-s)^2}{2(a-b)}
+us-u^2(b-\mu)\left(\frac12-\frac1{r(r+1)}\right).
\tag{P7}
\]
在q≤T′≤T的区间内，v_{T′}≤v_T≤m，故
\[
N_m'(T')=2-2v_{T'}/m\ge0,\quad
N_m(T)\ge N_m(q).
\tag{P8}
\]
因u<1，s=(r−1)u(b−μ)/r；令v_q=(q−s)/(a−b)，则
\[
S(q)=\frac12v_q^2(a-b)+
 u^2(b-\mu)\frac{r-1}{2(r+1)}\ge0.
\tag{P9}
\]
于是m≥1时N_m(q)≥N_1(q)。

最后用同一个公开定理作严格公式校准，而非替换目标共同图：取m=1、函数f₁=1、零费用τ=0、线性φ_lin(z)=e^a z，保留同样的R=e^b、r、η、μ。常数函数在该盘收敛并在全盘holomorphic；a>0给positive denominator。Γ的凸性及斜率上界给
\[
 u\le v_q\le1,\qquad u<1,
\]
所以Theorem7.1.13的所有特殊条件均成立，积分恰为q，其结论给1≤N_1(q)/a。结合(P8)–(P9)，
\[
\boxed{N_m(T)\ge N_m(q)\ge N_1(q)\ge a=\log c.}
\tag{P10}
\]
这是该显示公式自身的下界；辅助rank1对象只证明(P10)，没有把原目标换到普通点，也没有声称线性φ_lin对实际V合法。因此实际m=3源的binomial界同样必要log c>3τ/2≥7/2，仍被(P1)阻断。

## 5. 算术接口、排除范围和停止判断

234已经支付固定basic basis的费用floor7/3。本文随后实际FULL独立核读B235最终8633 B稿C1–C10；其C3–C9支付任意固定literal e及任意有限非负LCM矩阵的同一floor：p+h的h≠0双层见证和p/2附近的单层见证均是n的p单位，因此乘n^e不删层；每个非rational行必须有slopes≥2，含J行还须至少两列slopes≥1。逐行独立重排不改(8.0.2)，故matrix dominates两列(0,2,2)、(0,0,1)，τ♭♭+τ♯≥7/3。该证据包括全部finite heads与固定basis，不是把某安全upper当必要lower。

与(P3)–(P10)合并，结论精确为：对这个完整V的固定basis、固定u、固定literal powers及有限LCM matrix，不存在共同图、逐层patch、admissible径向斜率、非负s*解或上述binomial参数，使所列公开显示rank上界严格小于3。B对负修正留下的必要费用gap，在本稿由(P5)、(P6)、(P10)实际支付；不要求修改其冻结稿。

这不仅是“单图界平均也失败”。(P3)计入真正switch正项，(P5)计入负平方saving，(P6)使用非负系统解，(P10)计入binomial原生radius与其完整负项。§8.1的Nazarov比较确说明Bost–Charles分子可比rearrangement小，但没有把上述剩余log c成本取消。

没有找到新的有限处正贡献或更小的同对象预算。应停止只增加共同图、division points或这些公开metric参数的优化。这个结论不预领§8脚注32中未显示的一般混合公式、任意新Euclidean metric、随D变化的joint jet lattice、重新选择函数空间/变量、额外有限处解析图或其它CDT定理的排除；若继续，须先付一个确实改变以上预算或分子下界的机制。

来源只用[当前CDT作者PDF](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)的实际完整选页及本轮数学输入；准确读域见literature/truncated_multimap_sources_round235_20261008/lambert_reading_scope.md。没有新增数值无理性或线性无关性定理，数学程序0、参数扫描0、旧producer重跑0，旧234及更早资产不改。最终保存后作者完整复读。
