# R₀：真实紧致 rank-four 扇区、Yukawa 常数与 scalar regulator 的精确接口

日期：2026-10-06。NEW 纯证明稿。所有旧稿与 peer mathematical producer 只读；未执行、导入或改动任何旧/同行数学脚本。本文独立计算 cup pairing 的常数，**不使用待核的 KLM scalar-current equality 反求常数**。它不宣称新的数值无理性定理，也不将 regulator derivative 的候选视为完成。

## 1. 固定对象、规范与结论

令

\[
 \theta=x\partial_x,\qquad
 P=\theta^4-x(\theta+\tfrac12)^4,\qquad
 y_0=\sum_{n\ge0}\frac{(1/2)_n^4}{(n!)^4}x^n,
 \qquad P W=\frac{\sqrt{x}}{16}.
 \tag{Y1}
\]

采用冻结实际几何

\[
 V_x=\{F_x=1-x\prod_{j=0}^3(1-u_j^2)=0\},\quad
 \Omega_x=\frac{du_0\wedge du_1\wedge du_2\wedge du_3}{F_x},
 \quad \eta_x=\operatorname{Res}_{V_x}\Omega_x .
\]

**左留数约定**是 \(\Omega_x=dF_x/F_x\wedge\eta_x\)。在覆盖 \(x=s^2\) 上固定

\[
 \omega=s\,\eta_x .
 \tag{Y2}
\]

全部 \(\theta\) 微分在此覆盖上进行，\(\theta=(s/2)\partial_s\)。这不把平方根覆盖当成免费的整模型操作。

设 \(X_x=Y_{256x}\) 为已构造的 smooth proper toric family 的光滑三维纤维；在 \(x\ne0,1,\infty\) 上工作。本文的两个配对是

\[
 Q_{\rm raw}(\alpha,\beta)
       =\int_{X_x}\alpha_{\rm an}\wedge\beta_{\rm an},\qquad
 Q_{\rm dR}=(2\pi i)^{-3}Q_{\rm raw}.
 \tag{Y3}
\]

第二式固定了 Tate trace 的规范，即代数 \(c_1(\mathcal O(1))\) 的 Betti 比较含 \(2\pi i\)。以下一直按 **第一个参数在前** 的 cup 顺序；交换两参数会变号。

本稿证明，在实际紧致四维 CY sector \(\mathbb V\) 中，

\[
 \boxed{
 Q_{\rm raw}(\omega,\nabla_\theta^3\omega)
 =-\frac{(2\pi i)^3}{16(1-x)},\qquad
 Q_{\rm dR}(\omega,\nabla_\theta^3\omega)
 =-\frac1{16(1-x)}.}
 \tag{Y4}
\]

这里不假设整个 open \(H^3(V_x)\)，或整个 \(H^3(X_x)\)，都是 rank four。§2 构造的是有理紧致投影；没有给 integral trace/saturation。

进一步，**如果**真正 compact regulator lift 的投影 \(r\) 满足

\[
 \nabla_\theta r=c\sqrt{x}\,\omega
 \tag{H}
\]

（\(c\) 是已由实际 current 确认的常数），则标量
\(\nu_{\rm raw}=Q_{\rm raw}(r,\omega)\)、
\(\nu_{\rm dR}=Q_{\rm dR}(r,\omega)\) 满足

\[
 \boxed{
 P\nu_{\rm raw}=-\frac{c(2\pi i)^3}{16}\sqrt{x},
 \qquad
 P\nu_{\rm dR}=-\frac c{16}\sqrt{x}.}
 \tag{Y5}
\]

所以 \(c=+16\) 时，恰当规范是

\[
 \boxed{\widehat\nu=-\frac{\nu_{\rm raw}}{16(2\pi i)^3}
                    =-\frac{\nu_{\rm dR}}{16},
        \qquad P\widehat\nu=\frac{\sqrt{x}}{16}.}
 \tag{Y6}
\]

它与 \(W\) 的 **inhomogeneous scalar equation** 完全同型；仍只能推出
\(\widehat\nu-W\in\ker P\)。本稿不删除 (H) 的条件，也不将这个齐次差自动置零。

## 2. 真正紧致 sector 与有理 projector

冻结 mirror 稿已在 function fields 上证明 degree-64 quotient

\[
 M_\psi/\Gamma\dashrightarrow V_{\psi^8},\qquad
 |\Gamma|=64,\quad x=\psi^8 ,
\]

并在固定 ambient order 下证明

\[
 p^*\omega=64\,\omega_M.
 \tag{Y7}
\]

采用 BKΣZ primary 的实际 smooth compact mirror \(\mathcal W_\psi\)：它是该 quotient 的 CY resolution，\(h^{2,1}=1\)，故 \(H^3(\mathcal W_\psi,\mathbb Q)\) rank four。其 canonical form 的真实 PF 是 half-four 方程；native normalized parameter 为 \(q=\psi^{-8}=1/x\)。这里所采用的 **compact PF 输入** 是 primary PDF6 Eq2.1、PDF7 Table1、PDF19 Eq2.39–2.40：该 compact family 的全部 canonical-form periods 满足 \(P_q\)，而不只是旧 \(\Gamma\) 的一个 scalar period 满足它。

更明确地，primary form 按它的 ambient order 为
\(\Omega_{\rm BK}=\epsilon(2\psi)^4\omega_M
                =16\epsilon\psi^4\omega_M\)，
\(\epsilon\in\{1,-1\}\) 是两个 ambient orientation 的固定差。
因此在共同 birational compact model 上
\[
 \omega=4\epsilon x^{-1/2}\Omega_{\rm BK},\qquad
 P_x[x^{-1/2}h(1/x)]
      =-x^{1/2}(P_qh)(1/x).
 \tag{Y7a}
\]
对 \(\mathcal W\) 的每个 compact flat cycle 应用 (Y7a)，mirror 的 full-period 非退化比较给出真正 **cohomological** \(P_x[4\epsilon x^{-1/2}\Omega_{\rm BK}]=0\) 在 \(H^3(\mathcal W)\) 中。下面通过共同 resolution 把它搬到 \(X\)，不假设 \(X\) 的额外三维 cycles 来自 mirror。raw constant form scale 不改变 PF，但会改变 Yukawa；本稿不从这个 scale 跳步读取常数。

在所需有限代数覆盖及非空 smooth base 上，取 graph 的共同 smooth proper resolution

\[
 X \xleftarrow{\,a\,} Z \xrightarrow{\,b\,}\mathcal W ,
 \tag{Y8}
\]

两映射都是 birational，degree one。Graph resolution 在 characteristic zero 存在，随后 spread 并收缩 base；它不需要声明整个 compact family 的完整整格已经计算。

在 \(Z\) 上，实际 dense-open 留数比较给
\[
 a^*\omega=4\epsilon x^{-1/2}b^*\Omega_{\rm BK}.
 \tag{Y8a}
\]
两边都是 global holomorphic three-forms，故 dense-open 等式延伸为全局等式。Pullback 与 Gauss–Manin 相容，所以
\[
 a^*(P_x\omega)
 =P_x\{4\epsilon x^{-1/2}b^*\Omega_{\rm BK}\}
 =b^*P_x\{4\epsilon x^{-1/2}\Omega_{\rm BK}\}=0.
\]
用 \(a_*a^*=\operatorname{id}\)，得到 \(P_x\omega=0\) 在 **整个 compact \(H^3(X)\)** 中。这个步骤使用 mirror 的 full PF 与 degree-one pullback 单射；没有从旧 \(\Gamma\) 的一个 scalar period 推出它。

定义

\[
 i=a_*b^*:R^3\pi_{\mathcal W*}\mathbb Q\longrightarrow
               R^3\pi_{X*}\mathbb Q,\qquad
 i^*=b_*a^* .
\]

下面的短证明保证这里不是任意选择一个 abstract PF submodule。Proper degree-one projection formula 给
\(a_*a^*=b_*b^*=\operatorname{id}\)，以及 \(a^*,b^*\) 对 middle cup pairing 的 isometry。Birational pullback 对 holomorphic three-forms 是同构。因 (Y7)，\(b^*\) 的 canonical form 与 \(a^*\omega\) 在共同 dense open 上相同（按已固定 scale），因而在 \(Z\) 上相同。故

\[
 T=(1-a^*a_*)b^*
\]

杀掉这个 Hodge-line section。所有图对应的 pullback/pushforward 都与 Gauss–Manin 相容，所以 \(T\) 也杀掉它的全部 derivatives。实际 half-four PF 的绝对不可约性及 rank four 输入说明这些 derivatives 的 span 为整个 \(R^3\pi_{\mathcal W*}\mathbb Q\otimes\mathcal O\)。因此 \(T=0\)，即

\[
 b^*H^3(\mathcal W)\subset a^*H^3(X),\qquad i^*i=1.
 \tag{Y9}
\]

于是

\[
 \boxed{\Pi=i\,i^*=a_*b^*b_*a^*}
 \tag{Y10}
\]

是实际 algebraic-correspondence 定义的 horizontal rational orthogonal projector。
其 image \(\mathbb V\) rank four，含 \(\omega\)，cup pairing 非退化。这个 construction 的 Hodge line 和 cyclic span 不随共同 resolution 改变，故所得 orthogonal projector 唯一；在 finite cover 上的 deck transformations 保持该 cyclic span，投影因而下降到原 smooth base 的有理 local system。

这证明 **有理 compact projection 的存在和一份具体对应公式**。它没有证明：

* graph correspondence 在已选 integral lattice 中的 matrix 或 saturation；
* \(\Pi\) 是 integral projector；
* 全部 open/boundary classes 都属于这个四维 sector。

有限 degree-64 map \(M_\psi\to\mathcal W_\psi\) 与 (Y8) 的 degree-one birational maps 也不能混用；前者 cup trace 有实际 degree，而后者在 (Y9) 才是 isometry。

## 3. Flat pairing、完整 cyclic matrix 与 self-duality

记 \(E_j=\nabla_\theta^j\omega\)，\(0\le j\le3\)。把 (Y1) 展开为

\[
 P=(1-x)\theta^4-2x\theta^3-\frac{3x}{2}\theta^2
                      -\frac x2\theta-\frac x{16}.
 \tag{Y11}
\]

在 \(\mathbb V\) 内 \(P\omega=0\)。设
\[
 p_3=-\frac{2x}{1-x},\quad p_2=-\frac{3x}{2(1-x)},\quad
 p_1=-\frac{x}{2(1-x)},\quad p_0=-\frac{x}{16(1-x)}.
\]
则 \(E_4=-p_3E_3-p_2E_2-p_1E_1-p_0E_0\)。

对 (Y3) 任一 pairing，Hodge type 与 Griffiths transversality 给
\(Q(E_0,E_0)=Q(E_0,E_1)=Q(E_0,E_2)=0\)。令 \(Y=Q(E_0,E_3)\)。
Flatness 依次给

\[
 Q(E_1,E_2)=-Y,\quad Q(E_1,E_3)=-\theta Y,\quad
 2\theta Y=-p_3Y .
\]

因此

\[
 Y=\frac{\kappa}{1-x},\qquad
 Q(E_2,E_3)=-\theta^2Y-p_3\theta Y-p_2Y
          =\frac{\kappa x}{2(1-x)^2}.
 \tag{Y12}
\]

也就是说，按 \(E_0,E_1,E_2,E_3\) 的顺序，

\[
 J=\begin{pmatrix}
 0&0&0&Y\\
 0&0&-Y&-\theta Y\\
 0&Y&0&\kappa x/[2(1-x)^2]\\
 -Y&\theta Y&-\kappa x/[2(1-x)^2]&0
 \end{pmatrix},
\]
\[
 \boxed{
 J^{-1}=\frac1\kappa
 \begin{pmatrix}
 0&x/2&x&-(1-x)\\
 -x/2&0&1-x&0\\
 -x&-(1-x)&0&0\\
 1-x&0&0&0
 \end{pmatrix}.}
 \tag{Y13}
\]

Pfaffian 为 \(-Y^2\)，故 \(\kappa\ne0\) 时确实非退化。
取 \(Q_{\rm dR}\) 后，§5 将独立得到 \(\kappa=-1/16\)，所以整个 matrix 已是明确的 rational function matrix。

若 \(\alpha\in H^3_{\rm dR}(X)\)，令
\(v_j=Q_{\rm dR}(\alpha,E_j)\)，则投影还有精确 cyclic 表达式

\[
 \boxed{\Pi\alpha=-\sum_{j=0}^3 (J^{-1}v)_jE_j.}
 \tag{Y14}
\]

这与 (Y10) 同一 orthogonal projector，不是只在 open cohomology 的 field restriction 上拟出的投影。每个 \(E_j\) 的平方根 scale 在 (Y14) 中相消；但 (Y14) 的有理 matrix 仍不等于一个已标定的 integral Betti projector。

Euler formal adjoint采用 measure \(dx/x\)，即 \(\theta^*=-\theta\)。直接有
\[
 [x(\theta+\tfrac12)^4]^*
 =(-\theta+\tfrac12)^4x=x(\theta+\tfrac12)^4,
 \qquad \boxed{P^*=P}.
 \tag{Y15}
\]
这里没有把 monic operator \(P/(1-x)\) 误作同一个 self-adjoint operator。

## 4. Scalar concomitant 的符号

对 scalar functions \(h,k\)，定义

\[
\begin{aligned}
\mathcal C_0(h,k)={}&
 \frac x2(h\theta k-\theta h\,k)
 +x(h\theta^2k-\theta^2h\,k)\\
 &-(1-x)(h\theta^3k-\theta^3h\,k)
 +(1-x)(\theta h\,\theta^2k-\theta^2h\,\theta k).
\end{aligned}
 \tag{Y16}
\]

直接 integration-by-parts / (Y15) 给
\[
 \theta\mathcal C_0(h,k)=(Ph)k-h(Pk).
 \tag{Y17}
\]
所以对两个 homogeneous periods 它为常数。也可从 (Y13) 看出
\[
 (\ h,\theta h,\theta^2h,\theta^3h\ )J^{-1}
   (\ k,\theta k,\theta^2k,\theta^3k\ )^T
   =\mathcal C_0(h,k)/\kappa .
 \tag{Y18}
\]

这里的 **dual sign** 很重要。采用 Poincaré dual convention
\[
 \int_\gamma\alpha=\int_X\operatorname{PD}(\gamma)\wedge\alpha,\qquad
 \gamma\cdot\delta=\int_X
       \operatorname{PD}(\gamma)\wedge\operatorname{PD}(\delta).
 \tag{Y19}
\]
对 \(\gamma,\delta\) 的 compact-sector 投影，period vector 的列坐标是
\(-J\) 乘其 Poincaré-dual 的 basis coordinates。因此 (Y18) 是

\[
 \boxed{\mathcal C_0(h_\gamma,h_\delta)/\kappa_{\rm raw}
       =-Q_{\rm raw}(\Pi\operatorname{PD}\gamma,
                     \Pi\operatorname{PD}\delta).}
 \tag{Y20}
\]

这正是随后确定负号的一步，不能把 contravariant solution pairing 和 covariant cup pairing 混同。

## 5. 用真实 node 和 Picard–Lefschetz 独立确定 \(\kappa\)

### 5.1. 真实 vanishing three-sphere 的首项

Toric 稿已证明全部 surviving boundary strata 上的 family map smooth，interior 唯一 critical point 是 \(v_j=1\)，对应 \(u_j=0,x=1\)。它的 Hessian 非退化。因此 \(X\) 的 proper degeneration 在这里恰有一个 ordinary quadratic critical point，不另有 boundary critical points。

令 \(f(u)=1-\prod_j(1-u_j^2)=\sum_j u_j^2+O(|u|^4)\)。
对实 \(x>1\) 接近1，\(F_x=x(f-\tau)\)，\(\tau=(x-1)/x>0\)。
取 real Morse coordinates \(u=z+O(|z|^2)\)，其 Jacobian 在0为 \(+1\)，并给 vanishing \(S^3\) 取 real outward-boundary orientation。
左 residue
\[
 \operatorname{Res}\frac{dz_0\wedge\cdots\wedge dz_3}
                          {\sum z_j^2-\tau}
\]
在 radius \(\sqrt\tau\) 的 real sphere 上，是其 oriented area form 除以 \(2\sqrt\tau\)。因 area \(S^3_{\sqrt\tau}=2\pi^2\tau^{3/2}\)，真正的 vanishing period 满足

\[
 g(x):=\int_{\delta_x}\omega
 =\pi^2(x-1)+O((x-1)^2).
 \tag{Y21}
\]

这只需要首项；不以 canonical hypergeometric normalization 猜测 node period。
令 \(t=1-x\)，则
\[
 g=a\,t+b\,t^2+O(t^3),\qquad a=-\pi^2 .
 \tag{Y22}
\]

### 5.2. 实际 closed torus 与 PL coefficient

冻结 mirror 稿给真正 compact three-torus \(\Gamma_x\subset V_x\subset X_x\)，其 fixed-orientation period 是

\[
 h(x):=\int_{\Gamma_x}\omega=-4i\pi^3 y_0(x).
 \tag{Y23}
\]

冻结 conifold analysis 给 \(y_0\) 的整个 log branch 为 rank one，首个 \(t\log t\) 系数 \(1/\pi^2\)。于是
\[
 h(t)=H(t)+c\,t\log t+O(t^2\log t),\qquad c=-4i\pi ,
 \tag{Y24}
\]
其中 \(H\) analytic。

本稿采用 positive anticlockwise monodromy。Picard–Lefschetz 的 sign 为
\((-1)^{n(n+1)/2}\)，这里 total complex dimension \(n=4\)，所以是 \(+1\)：
\[
 T\gamma=\gamma+(\gamma\cdot\delta)\delta .
 \tag{Y25}
\]
实际 primary 为 Movasati author text §6.6 Theorem6.3，特别明确 anticlockwise path 和 \(H_{n-1}\) 的 intersection-order convention；\(n=4\) 不能误填 relative dimension3。

由 (Y22)–(Y24)，continued period 的 jump 为
\[
 (Th-h)(t)=2\pi i\,c\,t+O(t^2)
          =8\pi^2t+O(t^2)=-8g(t).
\]
配合 (Y25) 和 \(g\ne0\)，得到真正 compact intersection number

\[
 \boxed{\Gamma\cdot\delta=-8.}
 \tag{Y26}
\]

在 \(H^3(X)\) 上 \(T-1\) 的 image 是 \(\mathbb Q\,\operatorname{PD}\delta\)。
这个 operator 在 \(\mathbb V\) 上非零，因为其 P4 monodromy 是实际非零 transvection。投影 (Y10) 与 \(T\) 相容，故 \(\operatorname{PD}\delta\in\mathbb V\)。
因此
\[
 Q_{\rm raw}(\Pi\operatorname{PD}\Gamma,\operatorname{PD}\delta)
 =\Gamma\cdot\delta=-8 .
 \tag{Y27}
\]
这里不假设 \(\Gamma\) 没有额外 compact/open sector，也不先假设 \(\delta\) 是某 chosen lattice 的 primitive generator。

### 5.3. Concomitant 的真正极限

两个 period 都在 \(\ker P\)。Rank-one jump 还说明 \(h\) 的 log coefficient 是 \(g\) 的常数倍。
把 \(P\) 改写为 \(t\)-derivatives：

\[
\begin{aligned}
 P={}&t(1-t)^4\partial_t^4
 +(1-t)^3(2-8t)\partial_t^3
 +\tfrac12(1-t)^2(29t-15)\partial_t^2\\
 &+(1-t)(4-5t)\partial_t-\tfrac1{16}(1-t).
\end{aligned}
 \tag{Y28}
\]

\(P(g\log t)\) 的 \(t^{-1}\) 系数为 \(2b-3a/2\)；analytic part 不产生负次幂。
故
\[
 b=3a/4.
 \tag{Y29}
\]

在 (Y16) 中代入 \(g=a t+(3a/4)t^2+O(t^3)\)，
\(h=H(t)+(c/a)g\log t\)。由于 \(\theta=-(1-t)\partial_t\)，log 项各 contribution 的极限依次为
\[
 0,\quad -ca,\quad +ca,\quad +ca.
\]
而 analytic \(H\) 的 contribution 是
\(H(0)(-3a/2+2b)=0\)；其余 analytic terms 趋于0。
于是
\[
 \boxed{\mathcal C_0(h,g)=ca=4i\pi^3.}
 \tag{Y30}
\]

最后 (Y20)、(Y27) 给
\[
 \frac{4i\pi^3}{\kappa_{\rm raw}}=8,\qquad
 \boxed{\kappa_{\rm raw}=\frac{i\pi^3}{2}
       =-\frac{(2\pi i)^3}{16},\quad \kappa_{\rm dR}=-\frac1{16}.}
 \tag{Y31}
\]
这完成 (Y4)。推导只使用真正 node/torus/intersection 和 compact cup pairing，没有使用本轮尚待核的 regulator integral equality。

## 6. 真正 scalar normal-function 方程的条件推导

现在只假定 (H)，在局部 simply connected smooth base 选 actual compact regulator 的 lift，先用 (Y10) 投影。因为 \(\omega\in\mathbb V\)，未投影 lift 与投影 lift 的 scalar pairing 相同；extra orthogonal compact sectors 不进入该 scalar。

令 \(\nu=Q(r,E_0)\)。Hodge zeros 与 (H) 依次给
\[
 \theta\nu=Q(r,E_1),\quad
 \theta^2\nu=Q(r,E_2),\quad
 \theta^3\nu=Q(r,E_3),
\]
\[
 \theta^4\nu=Q(r,E_4)+c\sqrt{x}\,Q(E_0,E_3).
\]
因此对 **monic** operator \(P/(1-x)\)，
\[
 \frac{P}{1-x}\nu=c\sqrt{x}\,Y.
\]
乘回 actual leading factor，才得到
\[
 \boxed{P\nu=(1-x)c\sqrt{x}\,Y=\kappa c\sqrt{x}.}
 \tag{Y32}
\]
将 (Y31) 代入便是 (Y5)。少乘 \(1-x\) 会错误留下 conifold pole；少计 \(1/16\) 会错误放大 source。

如果 toric current 的实际证明最终给 \(c=+16\)，则 (Y6) 严格成立，而且
\[
 P\{\nu_{\rm raw}+16(2\pi i)^3W\}=0 .
 \tag{Y33}
\]
若别的 current/Tate convention 给相反 sign 或不同 constant，应把实际 \(c\) 代回 (Y5)，而不是修改已固定的 (Y31)。本稿不把冻结 toric §8 中尚带问号的负号候选当成事实。

## 7. 现在已填的接口与仍未填的部分

本文无条件的新增部分（以已核准 mirror/toric 几何输入为基础）是：

* 实际 rational compact rank-four projector (Y10)/(Y14)，以及完整 cyclic cup matrix；
* fixed-left-residue / raw-cup / Tate-trace 规范下的 exact Yukawa (Y31)；
* 包含 formal self-duality、contravariant sign、leading factor 的完整 scalarization formula (Y32)。

从真正 regulator 到 \(W\) 仍需两项独立实际输入：

1. KLM current 与 completion 在 compact family 中的真正 derivative (H)，含 \(c\) 的 sign/Tate convention。不能直接将 DK 只陈述 \(\ell=2,3\) 的 Lemma4.1 用在我们的非regular \(\ell=4\) compactification。
2. 确定 (Y33) 的 **实际 homogeneous period**。唯一非零 family Chow class 不等于指定 current representative、flat Betti lift 或 actual cube/tube marking；同一个 inhomogeneous PF equation 不消除这个差。

本稿还没有标定 projector 的完整 integral correspondence matrix、trace/saturation、fibre conifold nearby-cycle lift，或 CDT 全 place 费用。不能以 (Y31) 的有理常数、或 (Y6) 的 Tate 除法，宣称这些算术操作都是免费。

## 8. Primary 来源、实际阅读与执行边界

* 冻结输入：[actual mirror/residue/tube 稿](cdt_odd_R0_relative_cycle_mirror_20261006.md)，SHA256 \(43009e569bba25b6f819f0e5f1de0b96fa2db57e1a73817e8b087d294a059912\)；[toric completion 稿](cdt_odd_R0_toric_completion_20261006.md)，SHA256 \(abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0\)。另实际全文读 Kummer interface，核对 P4W 和完整 log coefficient 输入。
* BKΣZ, *D-brane masses at special fibres of hypergeometric families of Calabi–Yau threefolds, modular forms, and periods*，[本地79页 primary](../literature/bonisch_klemm_scheidegger_zagier_alternate_author_url_20261006.pdf)：本轮 actual read PDF6–12、14–17、19，核对 full compact PF、Table1、pairing/period/form conventions、真实四quadrics quotient 和 compact resolution。PDF10 Eq2.11 的 pairing order、Eq2.14 的 positive convention 与 Eq2.6/2.8 的 leading period expansion 需要谨慎协调；本文不从那里照搬 \(\kappa=16\) 或其 sign，而按 (Y19) 独立计算。
* Doran–Kerr, *Algebraic K-theory of toric hypersurfaces*，[本地 published204页](../literature/doran_kerr2011_algebraic_K_toric_published_20261006.pdf)：本轮 actual read PDF66–75、79–83。PDF73–74 Definition4.1/Corollary4.5 使用 **monic** PF，\(g=Y\) 的条件是实际 rank \(r=n\)；PDF74 Remark4.4 明确指出 constant \(\kappa\) 需要额外精确信息。PDF79–80 Lemma4.1 已陈述范围是 \(\ell=2,3\)。本文重推 rank4 scalarization，而不扩大该 lemma。
* Movasati, *A Course in Hodge Theory, With Emphasis on Multiple Integrals*, author-hosted version dated2021-04-27，[official author PDF](https://w3.impa.br/~hossein/myarticles/hodgetheory.pdf)，[本轮保存](../literature/movasati2021_course_hodge_theory_author_20261006.pdf)，380页，SHA256 \(69830ec409ccd1172f1ec348dad2f6bed59fe4f18342c1a4fab37b0659c85182\)。本轮实际读 PDF1,54,57–58,82,93–95,131–133；PDF95另作视觉核查。Theorem6.3 的 anticlockwise homological PL sign 是本文 (Y25) 的来源；额外若干基础页没有扩大为完整 book 审阅。正常 curl TLS 下载成功，未绕过证书。

本文是新的纸面数学推导；没有创建或运行 mathematical verifier，没有数值 PSLQ 或 Lean claim。后续独审应尤其检验 (Y20) 的 dual sign、(Y29) 的 analytic cancellation、degree-one projector proof 与 (Y31) 的 raw/Tate 区分。
