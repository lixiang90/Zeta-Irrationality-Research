# R0 的正实 logarithm cuts、真实 Stieltjes 周期与有理 tube 修正

日期：2026-10-06。本稿是新的纸面数学推导。旧 MD/PY/JSON/manifest 均只读；没有执行、导入或重跑冻结或同伴的数学 producer。结论是开放模型上一个精确 current 积分与真实 relative-period 的比较；本稿不把未经 admissible completion 的 graph current 宣称为紧化 Chow 类的 regulator。

## 1. 已核验输入和实际结论

使用冻结稿 [真实相对链与 mirror](cdt_odd_R0_relative_cycle_mirror_20261006.md) §§2–4,8 的实际对象与 LEFT residue convention：

\[
 \theta=x\partial_x,\qquad P_4=\theta^4-x(\theta+\tfrac12)^4,
 \qquad \phi(v)=\prod_{j=0}^3(v_j+2+v_j^{-1}),\quad\lambda=256x,
\]
\[
 X_x^*=\{\phi=256x\}\subset(\mathbb C^*)^4,
 \quad \Omega_x=\frac{16\,d\log v_0\wedge\cdots\wedge d\log v_3}{\phi-256x},
 \quad\omega_x=\sqrt{x}\operatorname{Res}_{X_x^*}\Omega_x.
\]

固定 \(0<x<1\) 和 \(\sqrt{x}>0\)。冻结的实际 Stieltjes integral 为

\[
 B(x)=\int_{(0,\infty)^4}\frac{d\log v_0\cdots d\log v_3}{\phi-256x},
 \quad W(x)=\sqrt{x}B(x),\quad P_4W=\sqrt{x}/16.
\]

令 \(R_4^+\) 为下面明确定义的正实切 logarithmic symbol current。按逐个坐标的 complex orientation 及 current normal-first convention 定义 exhaustion pairing。本稿证明

\[
 \boxed{\nu_{\rm cut}(x):=\int_{X_x^*}R_4^+\wedge\omega_x
       =-16(2\pi i)^3W(x).} \tag{1}
\]

这是全部 \(0<x<1\) 上的精确身份，不是数值拟合。其 current integral 绝对收敛。

对冻结稿实际闭三环面 \(\Gamma_x\) 和正向 Leray tube \(T\Gamma_x\)，定义

\[
 \nu_{\rm corr}:=\nu_{\rm cut}+\frac{(2\pi i)^4}{8}\int_{\Gamma_x}\omega_x.
\]

则进一步有

\[
 \boxed{\nu_{\rm corr}
 =-16(2\pi i)^3\left(W-\frac{\pi^4}{16}y_0\right)
 =-\frac{(2\pi i)^3}{8}\sqrt{x}\int_{8C-T\Gamma_x}\Omega_x.} \tag{2}
\]

其中 \(C=[-1,1]^4\) 是旧 \(u\) 坐标中的真实整相对 cube，\(y_0={}_4F_3(\tfrac12^4;1^3;x)\)。式 (2) 标明所需膜修正的有理系数恰为 \(1/8\)，没有把它当成 integral primitive cycle。

## 2. 正实切及三个方向的符号

取 logarithm branch \(\arg v\in(0,2\pi)\)。其 cut 为 \(v>0\)。在 cut 附近写 \(v=a+ib\)，\(a>0\)，则从 \(b<0\) 到 \(b>0\)，log 的跳跃为 \(-2\pi i\)。因此，作为分布，

\[
 d[\log^+v]=d\log v-2\pi i\delta_T,\qquad
 \delta_T=\delta(b)\,db. \tag{3}
\]

这规定 coorientation，不能另凭“实轴向右”猜 current 的方向。令

\[
 R_4^+=\log^+v_0\,d\log v_1\wedge d\log v_2\wedge d\log v_3
 -2\pi i\log^+v_1\,\delta_{T_0}\wedge d\log v_2\wedge d\log v_3
\]
\[
 \hspace{7mm}+(2\pi i)^2\log^+v_2\,\delta_{T_0}\wedge\delta_{T_1}\wedge d\log v_3
 -(2\pi i)^3\log^+v_3\,\delta_{T_0}\wedge\delta_{T_1}\wedge\delta_{T_2}. \tag{4}
\]

这里把各 delta factor 全部放在 differential factors 前面。对前三个坐标，delta wedge 与剩余实切体积的排列是

\[
 db_0\wedge db_1\wedge db_2\wedge da_0\wedge da_1\wedge da_2.
\]

相对于 complex orientation \(da_0\wedge db_0\wedge da_1\wedge db_1\wedge da_2\wedge db_2\)，排列 \([1,3,5,0,2,4]\) 有六次逆序，符号为正。因此三重 cut 的最后一项按 \((a_0,a_1,a_2)\) 的正向体积积分；不能将单个 cut 的 tangent orientation 简单相乘后漏掉 normal 排列。

在 complex dimension 3 的 \(X_x^*\) 上，\(\omega_x\) 为 \((3,0)\) form。式 (4) 前三项每项还含至少一个 holomorphic \(d\log v_j\)，与 \(\omega_x\) wedge 后为零。唯有最后一项存活，故

\[
 \nu_{\rm cut}=-(2\pi i)^3
       \int_{T_0\cap T_1\cap T_2}\log^+v_3\,\omega_x. \tag{5}
\]

四个 positive cuts 的 fibre intersection 为空，因为正实 orthant 上 \(\phi\ge256>256x\)。因此这里没有漏掉第四 cut 上的内部积分项。不过 compact boundary 上的 face currents 和 Bloch homotopy 尚未处理，见 §6。

## 3. 两张真实 sheet 的 LEFT 留数

对 \(v_0,v_1,v_2>0\) 设

\[
 \Phi=\prod_{j=0}^2(v_j+2+v_j^{-1})\ge64,\qquad
 a=\frac{256x}{\Phi}\in(0,4).
\]

fibre 方程给出两张互不相交的 sheet

\[
 v_3=e^{\pm i\alpha},\quad0<\alpha<\pi,\qquad
 \cos\alpha=\frac a2-1=\frac{128x}{\Phi}-1,
 \quad\sin\alpha=\frac{16\sqrt{x}\sqrt{\Phi-64x}}{\Phi}. \tag{6}
\]

LEFT residue 的定义为 \(\Omega_x=(d(\phi-256x)/(\phi-256x))\wedge\eta_x\)。因 \(dv_3\) 移过前三个坐标产生负号，得到

\[
 \eta_x=-\frac{16\,d\log v_0\wedge d\log v_1\wedge d\log v_2}
                    {\Phi(v_3-v_3^{-1})}.
\]

所以

\[
 \omega_+=\frac{i\,d\log^3 v}{2\sqrt{\Phi-64x}},\qquad
 \omega_-=-\frac{i\,d\log^3 v}{2\sqrt{\Phi-64x}}. \tag{7}
\]

正实切 branch 上 \(\log^+v_{3,+}=i\alpha\)、\(\log^+v_{3,-}=i(2\pi-\alpha)\)。按 §2 已固定的两个 sheet 的 cut orientations 相加，恰得

\[
 \boxed{\log^+v_{3,+}\,\omega_++\log^+v_{3,-}\,\omega_-
       =\frac{(\pi-\alpha)\,d\log^3v}{\sqrt{\Phi-64x}}.} \tag{8}
\]

sheet projection 在整个正实三维域均无 branch point；\(a<4\) 保证没有遗漏合并 sheet。

## 4. 一个初等全尺度积分给出因子 16

固定前三个 positive coordinates，直接积分第四个变量：

\[
 \int_0^\infty\frac{dv_3/v_3}{\Phi(v_3+2+v_3^{-1})-256x}
 =\frac1\Phi\int_0^\infty\frac{dv_3}{v_3^2+(2-a)v_3+1}.
\]

由 \(2-a=-2\cos\alpha\)，complete-square 积分给出

\[
 \frac{1}{\Phi\sin\alpha}
 \left[\arctan\frac{v_3-\cos\alpha}{\sin\alpha}\right]_{0}^{\infty}
 =\frac{\pi-\alpha}{\Phi\sin\alpha}.
\]

代入 (6) 并乘 \(\sqrt{x}\)，得到

\[
 \boxed{W(x)=\frac1{16}\int_{(0,\infty)^3}
                  \frac{(\pi-\alpha)\,d\log^3v}{\sqrt{\Phi-64x}}.} \tag{9}
\]

原四维 integrand 非负，Tonelli 可用；它经 \(v=(1+u)/(1-u)\) 化为有限 cube 上 \((1-x\prod(1-u_j^2))^{-1}\)，其值被 \((1-x)^{-1}\) 控制，故 (9) 绝对收敛。还须检验两张 sheet 分别的绝对收敛，不能仅凭 (8) 合并后非负省略这一步。其 absolute densities 相加为

\[
 |\log^+v_{3,+}\,\omega_+|+|\log^+v_{3,-}\,\omega_-|
 =\frac{\pi\,d\log^3v}{\sqrt{\Phi-64x}}
 \le\frac{\pi\,d\log^3v}{\sqrt{1-x}\sqrt{\Phi}}.
\]

最后一个 integral 分离成三个 \(\int_0^\infty dv/[\sqrt v(1+v)]=\pi\)，故两张 sheet 的 absolute norm 总和至多 \(\pi^4/\sqrt{1-x}<\infty\)。因此未合并的 raw current pairing 也绝对收敛，其 exhaustion limit 独立于顺序。由 (5),(8),(9) 即得 (1)。在 \(x\) 的任意 compact subinterval of \((0,1)\) 上，同一 cube bound 允许解析延拓和参数微分；故也有

\[
 P_4\nu_{\rm cut}=-(2\pi i)^3\sqrt{x}. \tag{10}
\]

## 5. 真实闭周期修正、Tate 因子和 conifold 值

冻结的实际三环面和 tube 满足

\[
 \int_{\Gamma_x}\omega_x=-4i\pi^3y_0(x),\quad
 \sqrt{x}\int_{T\Gamma_x}\Omega_x=8\pi^4y_0(x),\quad
 \sqrt{x}\int_C\Omega_x=16W(x).
\]

直接代入，不改变任何 residue/chain orientation：

\[
 \frac{(2\pi i)^4}{8}\int_{\Gamma_x}\omega_x=-8i\pi^7y_0,
 \quad-16(2\pi i)^3W=128i\pi^3W.
\]

于是 (2) 成立。若将 \(\Gamma_x/8\) 放入 rational Tate-period ambiguity，这正是把 \(W\) 变为 canonical conifold holomorphic germ

\[
 \Psi=W-\pi^4y_0/16.
\]

此处 \(1/8\) 是实际计算出来的有理 membrane coefficient，而 \(8C-T\Gamma_x\) 是整相对链。没有从 rational 修正推出 integral saturation。

冻结的 conifold identity 给出

\[
 \boxed{\lim_{x\to1^-}\nu_{\rm corr}(x)
 =-(2\pi i)^3\pi^2(R_0-M_0).} \tag{11}
\]

相同 forcing (10) 对 \(\nu_{\rm corr}\) 仍成立。这是新核准的 Tate-normalized analytic comparison；不是 \(R_0-M_0\) 的无理性或非零定理。

## 6. 对实际 compact regulator 比较的贡献与剩余缺口

KLM published §5.6 的 ordinary cohomological normalization 为 \((-2\pi i)^{p-n}\)，本例 \(p=n=4\) 时此因子为 1；膜修正为 \((2\pi i)^4\delta_\zeta\)。所以 (2) 的 Tate 因子与原始公式相容，未偷除 \((2\pi i)^3\) 当有理 gauge。

然而本稿没有证明如下 stronger statement：

\[
 \int_{Y_x}AJ(\Xi_x)\wedge\omega_x=\nu_{\rm cut}
 \quad\text{或}\quad\nu_{\rm corr}
 \quad\text{作为已经标记的具体 lift。}
\]

已唯一存在的 family Chow 类 \(\Xi\) 不能自动固定 its precycle、Bloch homotopy、topological membrane 和 closed-period lift。raw graph closure 在若干 compact boundary components 上共享 coordinate zeros/poles，仍须验证 cubical multi-face admissibility；rotating logarithmic cuts 不替代这项验证。直接 boundary pushforward 与 holomorphic 3-form 的 pairing 确实按 restriction/type 消失，但 Bloch homotopy 及 membrane 可留下 closed period。

本稿因此将新接口精确化为：

1. 所需 raw open integral 已严格比较完毕，系数为 \(-16(2\pi i)^3\)。
2. 所需 canonical conifold period correction 是实际 \(\Gamma_x/8\)，其与旧整 relative chain 的关系由 (2) 固定。
3. actual compact regulator 的 derivative、cup normalization 可以另行独核；forcing 一致至多说明其标量与 (1) 相差 homogeneous PF solution，不能把该解设成零。
4. 要升级为 actual marked regulator equality，尚须构造/比较 admissible completed precycle 与其 membrane，或给出能唯一确定全部 homogeneous correction coefficients 的真实 Betti 归一化条件。

没有新增 numerical theorem、完整 integral model、算术 holonomy contradiction 或 Lean formalization。本轮不运行数学 producer。

## 7. 实际来源阅读

* [冻结真实相对链与 mirror](cdt_odd_R0_relative_cycle_mirror_20261006.md)：root 本轮完整实际阅读 §§1–13，核准 C、Γ、tube、φ、LEFT residue 和参数反演。
* Kerr–Lewis–Müller-Stach, *The Abel–Jacobi map for higher Chow groups*, Compositio Math.142(2006)374–396，[本地 published 原件](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，DOI [10.1112/S0010437X05001867](https://doi.org/10.1112/S0010437X05001867)。root 本轮实际读 PDF1–2,10–14,18–19；§5.3–5.7 核准 current 公式、moving 的条件、Tate factor、膜和 period ambiguity；§6–7 核准 extension/current 比较不等于本例 precycle 比较。未宣称阅读全文。

正实 logarithm phase 的分布公式 (3)、三重 orientation、sheet 留数和积分 (6)–(9) 是本稿独立推导，并非把论文的负实 cut 公式不加说明地直接搬用。
