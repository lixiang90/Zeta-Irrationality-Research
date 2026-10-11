# R₀ positive-cut current 的全角点估计、centering 与实际 compact lift

日期：2026-10-06。NEW 纸面证明。旧数学 MD/PY/JSON/manifest 和同行 producers 全部只读，执行/import 数0。本稿实际全文重读冻结 toric completion、positive-cut period comparison、boundary membrane comparison；当前主报告 §§73–78 和 delivery 的当前 R₀ 状态亦实际核验。采用已固定的 projective regular toroidal refinement，不另换一个方便的紧化。

本稿证明一个 stronger-than-flux 接口：同时把四个 logarithm 减去 \(\pi i\)，得到在每个水平边界方向都消失的 current。其零延拓是实际 compact de Rham lift，且 modulo rational Tate lattice 恰为指定的唯一 family Chow class 的 AJ。它同时证明 canonical relative trace 的边界通量为0。这个构造提供一个明确的 rational lift；不声明旧的任意膜已经具有这个标记，不声明 integral saturation 或新数值无理性。

## F1. 实际对象、分支和要证明的 statement

令 \(D\Subset\{0<|\lambda|<256\}\) 为小 contractible disk，可取包含一段正实 interval，固定 \(\sqrt{x}\)，\(x=\lambda/256\)。记
\[
 \phi(v)=\prod_{i=0}^3{(1+v_i)^2\over v_i},\quad
 U_\lambda=\{\phi=\lambda\}\subset(\mathbf C^*)^4,\quad a=2\pi i.
\]
冻结 toric model 给 smooth proper family \(X_D\to D\)、relative SNC divisor \(E_D\)，以及 \(U_D=X_D\setminus E_D\)。每个 fibre 为 complex threefold。total \(X_D\) 为 complex fourfold。令
\[
 B_i=d\log v_i,\qquad \Delta_i=\delta_{T_i^+},\qquad
 L_i=\log^+v_i,\quad \arg v_i\in(0,2\pi).
\]
positive cut 的 coorientation 是 \(\Delta_i=\delta(\operatorname{Im}v_i)d(\operatorname{Im}v_i)\) near \(v_i>0\)，故
\[
 dL_i=B_i-a\Delta_i.
\]
固定当前的 ordered cup product
\[
 R^+=\sum_{j=0}^3(-a)^j L_j\,
       \Delta_0\wedge\cdots\wedge\Delta_{j-1}
       \wedge B_{j+1}\wedge\cdots\wedge B_3.                 \tag{F1}
\]
empty products 的值是1。四个 positive cuts 在 \(U_D\) 上没有共同交点；所有 partial cuts 与 fibres 横截，已在冻结 positive-class 稿证明。

同时 center 四个 logarithm：
\[
 L_i^c=L_i-a/2=\operatorname{Log}_{(-\pi,\pi)}(-v_i),\qquad
 R^c=\sum_{j=0}^3(-a)^j L_j^c\,\Delta_{<j}\wedge B_{>j}.    \tag{F2}
\]
这不是任意把 current 中的一项常数改掉；它是四个 intrinsic Deligne unit classes \(u(-v_i)\) 的完整 exterior product。其 negative cuts 正好是原 \(v_i\) 的 positive cuts。由于 \(dL_i^c=dL_i\)，
\[
 dR^c=dR^+=B_0\wedge B_1\wedge B_2\wedge B_3
          =:\Omega_Y\quad\hbox{on }U_D.                    \tag{F3}
\]
冻结 derivative 稿已证明 \(\Omega_Y\) 在 \(X_D\) 延为 holomorphic \((4,0)\) form；其 fibre restriction 是0。本稿不再次调用只覆盖 \(\ell=2,3\) 的 DK Lemma4.1。

以下全尺度结论对任意上述 compact parameter disk 和固定有限 regular fan 成立：
\[
 \boxed{\begin{gathered}
 \widetilde R^c\in\mathcal D^3(X_D)\text{ 有规范的局部可积零延拓},\\
 d\widetilde R^c=\Omega_Y,\qquad
 d(\widetilde R^c|_{X_\lambda})=0,\\
 [\widetilde R^c|_{X_\lambda}]
       \bmod H^3(X_\lambda,\mathbf Q(4))=AJ(\Xi_\lambda).
 \end{gathered}}                                          \tag{F4}
\]
“规范”在这里仅指已经固定 F2、fan 与 branches 后，由局部可积 current 的零延拓确定；不是一个未经选择的 integral Betti 标记。

## F2. 所有 surviving cones 的共同坐标结构

取原 \((\mathbf P^1)^4\) grid 上一个 minimum-support stratum \(S\)，令 \(s=|S|\)。其 fixed coordinates 属于 \(0,\infty,-1\)。定义其全局 local parameters
\[
 z_i=v_i\ (0),\qquad z_i=v_i^{-1}\ (\infty),\qquad
 z_i=v_i+1\ (-1).
\]
在这个 neighborhood，
\[
 \phi=c(z,v_{\rm free})\,\chi^\ell,\qquad
 \ell_i=-1\ (0,\infty),\quad \ell_i=2\ (-1),                \tag{F5}
\]
其中 \(c\) 为 holomorphic unit，边界值
\(c_S=(-1)^{p}\prod_{\rm free}(v_i+2+v_i^{-1})\)，
\(p=\#\{i:v_i=-1\}\)。一个 surviving cone \(\tau\) 满足
\(\tau\subset\ker\ell\)；否则对应 orbit 不在 \(\phi\in\mathbf C^*\) 的 graph closure 中。

冻结的 minimum-support 证明给
\[
 2\le s\le4,\quad 1\le r=\dim\tau\le s-1\le3,
 \quad S_-\ne\varnothing,\quad S_p\ne\varnothing,           \tag{F6}
\]
其中 \(S_-=\{i\in S:v_i=-1\}\)，\(S_p=S\setminus S_-\)。
regular cone 的 primitive generators \(n_1,\ldots,n_r\) 可扩充为
\(N_S\simeq\mathbf Z^s\) 的 basis。其 chart 为
\[
 z_i=\prod_{b=1}^r t_b^{n_{b,i}}\ q^{m_i},
 \quad t_b=0\text{ 是 }E_b,\quad q\in(\mathbf C^*)^{s-r}.    \tag{F7}
\]
每个 \(n_{b,i}\ge0\)。minimum support 意味着对每个 \(i\in S\)，至少一个
\(n_{b,i}>0\)；因此在一个 relatively compact orbit/free chart 中，
所有 \(|t_b|<\delta\) 保证所有 \(|z_i|\) 小。

每个 nonzero horizontal ray 满足
\[
 -\sum_{i\in S_p}n_{b,i}+2\sum_{i\in S_-}n_{b,i}=0.
\]
它在非负 cone 中非零，故
\[
 b_b:=\sum_{i\in S_-}n_{b,i}\ge1.                           \tag{F8}
\]
因而
\[
 Z_-:=\prod_{i\in S_-}z_i
      =\Big(\prod_b t_b^{b_b}\Big)\times\text{orbit unit}
\]
在每个水平 normal direction 至少一阶消失。这里采用全部 forced
\(-1\) coordinates 的 product，不把一个只在某些 rays 消失的
coordinate 错用到其余 faces。

\(\ell\) 在 \(M_S\) 中 primitive，因为 \(S_p\ne\varnothing\) 含一个
coefficient \(-1\)。它在 saturated sublattice
\(M_S\cap\tau^\perp\) 中仍 primitive。可把 \(q_0=\chi^\ell\) 作为一个
orbit coordinate。F5 给 \(\phi=cq_0\)。边界上
\(\partial\phi/\partial q_0=c_S\ne0\)，故 \(\phi=\lambda\) 可在 chart
中 holomorphically 解 \(q_0\)。在 compact \(D\) 和 compact orbit/free
annuli 上，shrinking \(\delta\) 后 derivative 与其 inverse 有统一界。
这些均是固定 lattice monomial charts 内的 implicit function theorem，
不引入 nonmonomial blowups 或额外 strata。

## F3. Positive cuts 在 real oriented corners 的统一 angular rank

在 F7 作 real oriented blowup，写
\[
 t_b=\rho_b e^{i\vartheta_b},\qquad 0\le\rho_b<\delta.
\]
orbit/free coordinates 留在固定 compact annuli，角度在有限个 circle
charts 中展开。因为 \(|z_i|<1/2\) 对 \(i\in S_-\)，
\(v_i=-1+z_i\) 的 positive cut 完全不进入该 chart。故一个非空 partial
positive cut 只可能使用 \(S_p\) 里的 coordinates 和 free coordinates。

先在 \(\rho=0\) 的 corner 检验 rank。fixed \(0,\infty\) 的 cut phase
是 lattice character \(\pm e_i\) 的 argument；free cut phase 是其自身
free angle。fibre phase constraint 是
\[
 \arg q_0+\arg c_S(v_{\rm free})=\arg\lambda.               \tag{F9}
\]
对任意 fixed cut subset \(I\subset S_p\)，rows
\(\{\pm e_i:i\in I\}\cup\{\ell\}\) 在 \(M_S\otimes\mathbf R\) 中 independent：
一个未切 \(i\in S_-\) 的 \(\ell_i=2\) 排除了 \(\ell\) 属于这些
coordinate rows 的 span。regular toric coordinate change 是 invertible
integer lattice matrix；因此上述 rows 在全部 toric angular variables
\((\vartheta,\arg q)\) 中有一个非零 integer minor，绝对值至少1。
再加 free cut rows 时，它们形成 identity block；F9 中的 free derivatives
可由这些 rows 消去，或不选对应 free columns。仍有 full row rank。

解掉 \(q_0\) 的 real and imaginary equations 后，这正是 fibre 上剩余
cut phases 的 full rank 条件：independent rows modulo the fibre phase
row，而不是在 ambient space 忘记 fibre constraint。其 cut row 数至多3，
因为至少一个 fixed \(-1\) coordinate 不可切。

靠近 corner，\(c/c_S=1+O(\max_i|z_i|)\)。所有 angular derivatives of
this correction 亦为 \(O(\max_i|z_i|)\)，因为 F7 的 character exponents
固定，\(q\) 留在 compact annuli。q0 elimination 的 angular matrix于是是
边界 full-rank matrix 的 uniformly small perturbation。固定 fan 有有限
多个 cones；proper \(E_D\) 在 compact \(D\) 上可由有限 orbit/free charts
覆盖。因此存在统一常数 \(\delta>0,c_D>0\)，使每个 chart、每个 partial
cut、每个 corner，以及每个参数 \(\lambda\in\overline D\)，均可在某个
angular minor 上取 lower bound \(c_D\)。

这个 statement 也覆盖 face \(\rho_b=\epsilon\) 和任意更多
\(\rho_c=\epsilon\) 的 corners：角度仍保留，所用 minor 没有删掉任何
normal angular variable。uniform constant rank theorem，在有限个 angular
charts 内，把 cut currents 写成 uniformly bounded coarea density 对
剩余 angles 的积分。有限覆盖给统一 multiplicity bound；circle character
的有限 degree 以及同一小 perturbation 排除了随 \(\epsilon\) 增长的
新 sheets。这里的 coarea 是对角变量，不出现 \(1/\rho_b\) 的额外
radial Jacobian。cut phase 的 radial corrections 只具有
\(O(z_i)\,d\rho_b/\rho_b\) 的 logarithmic coefficients。

于是任意 partial-cut delta product 是 real-blowup 上的 uniformly bounded
angular delta current。其余形式估计可统一使用 logarithmic coframe
\[
 d\rho_b/\rho_b,\ d\vartheta_b,\ dq/q,\ d\bar q/\bar q,
 \quad\text{free smooth real forms}.                       \tag{F10}
\]
normal logarithmic volume 为
\(\prod_b(d\rho_b/\rho_b)\,d\vartheta_b\)。如果某项缺少一个 normal radial
direction，其 ordinary volume 更小；下列 upper bounds 仍可用这份
reference measure。此 coarea proof 不只列一个充分条件，而是在全部
surviving cones 中证出了该条件。

## F4. Centered product 的共同 vanishing factor

若 \(i\in S_-\)，则在该 chart
\[
 L_i^c=\operatorname{Log}(1-z_i)=-z_i+O(z_i^2),\qquad
 B_i={dz_i\over-1+z_i}.                                   \tag{F11}
\]
F7 给 \(dz_i=z_i\,d\log z_i\)，故 \(L_i^c\) 以及 \(B_i\) 的 F10 coefficients
都含 factor \(z_i\)。该 coordinate 的 cut \(\Delta_i\) 为0。

令 \(i_0=\min S_-\)。F2 的 term \(j>i_0\) 包含
\(\Delta_{i_0}\) 因而为0。term \(j=i_0\) 的 logarithm \(L_{i_0}^c\)
提供 \(z_{i_0}\)，而其后的全部 forced \(-1\) differentials 提供各自
\(z_i\)。term \(j<i_0\) 的 differentials 包含全部 forced \(-1\) coordinates，
提供其全部 factors。故每个 surviving term 的 logarithmic-frame coefficient
都含同一个 \(Z_-=\prod_{i\in S_-}z_i\)。

其余 centered logs 只有 linear logarithmic growth，所有 remaining dlogs 的
F10 coefficients 有统一界。得到
\[
 |R^c|_{\log,\rm angular}
 \ \le\ C_D\,\prod_{b=1}^r\rho_b^{b_b}
       \left(1+\sum_b|\log\rho_b|\right),\qquad b_b\ge1.    \tag{F12}
\]
这里 \(|\cdot|_{\log,\rm angular}\) 的精确定义是：将每一项以 F10 展开，
并把 F3 的 uniformly transverse delta constraints 通过 angular coarea
积分，剩余 coefficient 的 total variation 由右边控制。它不是把
delta function 当成 pointwise bounded function。任意 smooth test form
拉回到 real blowup，其 F10 coefficients 都 bounded，所以 F12 可用于
current mass 的估计。

## F5. 局部可积零延拓和所有 faces 的消失

对 F12，参考 radial integral 为
\[
 \prod_b\int_0^\delta \rho_b^{b_b}{d\rho_b\over\rho_b}
 \left(1+\sum_b|\log\rho_b|\right)<\infty.                 \tag{F13}
\]
因此 \(R^c\) 作用在任何 smooth compactly supported test form 上均绝对
收敛；有限 atlas 给一个全局 current \(\widetilde R^c\)，等于 \(R^c\)
在 \(U_D\) 上而不给 \(E_D\) 加任何 supported current。这是 locally
integrable extension 的直接定义。没有对 divergent coefficient 作
finite-part choice。

现在用 local exhaustion \(\rho_b\ge\epsilon\)。
在 face \(\rho_b=\epsilon\) 上，任意 smooth test form的 tangential restriction
仍有 uniformly bounded logarithmic coefficients。F12–F13 给
\[
 \left|\int_{\rho_b=\epsilon}R^c\wedge\gamma\right|
 \ \le C_{D,\gamma}\epsilon^{b_b}
        (1+|\log\epsilon|)
        \prod_{c\ne b}\int_\epsilon^\delta
             \rho_c^{b_c-1}(1+|\log\rho_c|)\,d\rho_c
 \ \le C'_{D,\gamma}\epsilon(1+|\log\epsilon|).             \tag{F14}
\]
过度计入多个 logarithms 只使 finite bound 增大。这对 total family 和
每个 fibre 都成立；degree 按对应 test form 调整。pieces 的 corners 是
codimension至少2的边界交接，不是额外的 Stokes faces。可直接用 manifold
with corners 的 oriented boundary chain，或用 uniformly rounded corners；
有限 atlas/partition of unity 把 local face estimates 求和。partition derivatives
仅用于 localization，cut current 的内部 Stokes 由 F3 已含全部 jumps。
当 \(\epsilon\to0\)，F14 消去所有 boundary-supported derivatives。

于是在 total space 的 distribution 意义，
\[
 d\widetilde R^c=\Omega_Y.
\]
在 fibre 同一局部定义并用 F3 的 restriction 为0，得到
\(d\widetilde R^c_\lambda=0\)。这个步骤证明实际 divisor residues和
higher-corner supported derivative 均为0；不只证明 divisorial tame symbol为0。

uniform angular graph representation还证明 \(\widetilde R^c_\lambda\) 是
distribution-valued smooth family：对参数求导时，delta derivatives可在
uniform angular coordinates 中对 smooth test forms 积分分部；q0 implicit
derivatives uniformly bounded，\(\partial_\lambda z_i=O(z_i)\) 保留 F12 中
每个 vanishing factor。每个 finite derivative order 都有同样可积的
radial bound。因此 compact cohomology sections 和下面的 scalar 可按
Gauss–Manin 解释；没有 interchange 一个未控制的 moving-boundary limit。

## F6. 相同的 rational AJ class：显式 flat open Tate correction

每个 summand of \(R^c-R^+\) 在 \(U_D\) 上 closed：
\[
 R^c-R^+=-{a\over2}\sum_{j=0}^3(-a)^j\Delta_{<j}\wedge B_{>j}. \tag{F15}
\]
在 \(\mathbf C^*\) 上，positive cut normalized current 与 logarithmic form
给相同 integral class：
\[
 [\Delta_i]=[B_i/a]=:e_i\in H^1(\mathbf C^*,\mathbf Z).
\]
F3 的 transverse pullbacks 和 exterior products 因此给实际 ordinary cohomology
身份
\[
 \boxed{[R^c-R^+]
 =-{a^4\over2}\sum_{j=0}^3(-1)^j
          e_0\wedge\cdots\wedge\widehat{e_j}\wedge\cdots\wedge e_3
 \in H^3(U_D,\mathbf Q(4)).}                              \tag{F16}
\]
这是 total-space rational class，故其 fibre classes flat。也可在 Chow 层
解释：每个 \(\{-1\}\) 是2-torsion，
\(\{-v_0,-v_1,-v_2,-v_3\}=\{v_0,v_1,v_2,v_3\}\) modulo torsion；
因此 rational Chow/regulator class 没有变化。F16 自身已给完整 cohomological
证明，不依赖积分时忽略 torsion 的口头说法。

冻结 phase-class proof 给指定 family \(\Xi\) 的
\(j^*AJ(\Xi)=[R^+]\) modulo rational \(a^4\)-classes。F16 与 F5 遂给
\[
 j^*[\widetilde R^c_\lambda]=j^*AJ(\Xi_\lambda)
           \quad\bmod H^3(U_\lambda,\mathbf Q(4)).
\]
冻结 derivative 稿已实际证明
\[
 H^3(X_\lambda,\mathbf Q)\hookrightarrow H^3(U_\lambda,\mathbf Q).
\]
用 \(\mathbf Q\)-vector-space tensor exactness，此 injection 亦给
\(H^3(X,\mathbf C)/H^3(X,\mathbf Q(4))\) 到对应 open quotient 的 injection：
对一个 \(\mathbf Q\)-linear injection \(A\hookrightarrow B\)，选择 rational
basis 或取 quotient \(B/A\) 后 tensor，严格有
\(A_{\mathbf C}\cap B_{\mathbf Q}=A_{\mathbf Q}\)；
固定 nonzero scalar \(a^4\) 给同一 statement 的 Tate 版本。
且 \(F^4H^3\) 在 compact/open 均为0。因此 equality of restricted classes
恰推出 F4 的 compact AJ equality。这里没有把任意 coefficient quotient
都设为 exact，也没有调用 integral lattice saturation。

结论：\(r_c=[\widetilde R^c_\lambda]\) 是**具体选定的 actual compact rational
AJ lift**。另一个已完成 admissible cycle 的 lift \(r\) 与它只差
\(a^4q\)，\(q\in H^3(X_\lambda,\mathbf Q)\)；若在同一 total-family primitive
下比较，该差 flat。没有得到旧膜自身已经等于此 current 标记的结论。

## F7. 实际 scalar：centering 不改变 raw pairing

取冻结实际 top form
\(\omega_\lambda=16\sqrt{x}\rho_\lambda\)，LEFT residue convention。
在 fibre complex dimension3，F1/F2 的 terms \(j<3\) 至少含一个
holomorphic dlog；与 \((3,0)\) form \(\omega\) wedge 后为0。因此
\[
 \int_X\widetilde R^c\wedge\omega-\int_U R^+\wedge\omega
 ={a^4\over2}\int_{T_0^+\cap T_1^+\cap T_2^+}\omega.         \tag{F17}
\]
对 \(0<x<1\)，冻结正切积分 proof 给三重 positive cut 上两张
\(v_3=e^{\pm i\alpha}\) sheets。normal-first orientation 相同，
\[
 \omega_+= {i\,d\log v_0d\log v_1d\log v_2
                  \over2\sqrt{\Phi-64x}},\quad
 \omega_-=-\omega_+,\quad \Phi=\prod_{i<3}(v_i+2+v_i^{-1}).
\]
两 sheets 的 absolute integrals 分别 finite，故 F17 的 integral 正好0，
不只是 principal-value cancellation。F5 又保证左边 compact current pairing
绝对定义。因此
\[
 \boxed{Q(r_c,\omega)=\int_X\widetilde R^c\wedge\omega
       =\nu_{\rm cut}=-16a^3W\quad(0<x<1).}                \tag{F18}
\]
这是一个 explicitly marked actual compact lift 的 scalar identity，
不再只是一条 raw open integral identity。对小 complex \(D\) 取相应
branches，F5 的 smooth-family current、F3 的 holomorphic total derivative
和 Gauss–Manin formula使左边是 holomorphic normal-function scalar；
F18 遂按 analytic continuation 成立。可也直接在 triple cut 上使用
\(v_3^\pm\) 的 inverse-pair roots：\(|\lambda|<256\le4\Phi\) 排除了
branch point，LEFT residues仍 opposite。没有用 numerical fit。

total F3 和 frozen LEFT normalization gives
\(\nabla_\theta r_c=16\sqrt{x}\omega\)。因此冻结 compact rank-four
projector/Gram computation实际应用于这个 lift：
\[
 P_4Q(r_c,\omega)=-a^3\sqrt{x}.
\]
它与 F18 完全相容。

真实 \(\Gamma\) 已独立标记且 \(\int_\Gamma\omega=-4i\pi^3y_0\)。
定义实际 rational compact class
\[
 r_{\rm corr}=r_c+{a^4\over8}PD(\Gamma)
\]
时，\(Q(PD(\Gamma),\omega)=\int_\Gamma\omega\)，所以
\[
 \boxed{Q(r_{\rm corr},\omega)
 =-16a^3\left(W-{\pi^4\over16}y_0\right)
 =-16a^3\Psi.}                                           \tag{F19}
\]
这给一项真实 current 加真实闭 cycle 的 explicit marking，
不是把 conifold holomorphy 推成三个 homogeneous coefficients 为0。
其他 compact lifts 仍允许 rational closed periods；此处恰是通过 F2
和 \(\Gamma/8\) 明确选定的 lift。

## F8. 同时完成 canonical boundary flux；不混用 rational splitting

为避免把 F18 与一个任意 rational-horizontal trace 混同，另证明原
\(R^+\) 的 canonical relative flux。

SNC pair 的 relative smooth de Rham complex 可取
\[
 \mathcal A^\bullet_{\rm rel}
 =\{\eta\in\mathcal A_X^\bullet:i_i^*\eta=0\ \forall E_i\}.
\]
这个模型也可直接局部核验。在一个有 \(r\) 个 coordinate hyperplanes
的 polydisk，写 \(\pi_J\) 为把 \(t_j,j\in J\) 置0的 commuting smooth
coordinate projections。若 \(\alpha_i\) 是各 \(E_i\) 上相容的 smooth forms，
\(\alpha_J\) 是其共同 intersection restriction，则
\[
 \sum_{\varnothing\ne J\subset\{1,\ldots,r\}}
       (-1)^{|J|+1}\pi_J^*\alpha_J
\]
是一个 ambient smooth extension：restrict 到 \(E_i\) 时，
\(J\not\ni i\) 与 \(J\cup\{i\}\) 的 terms 两两消去，只余 \(\alpha_i\)。
同一 commuting-projection contraction应用于 higher alternating Cech
degrees，给 ambient forms 到 SNC-intersection forms 的 degreewise exact
augmentation（first kernel正是 \(\mathcal A_{\rm rel}\)）。这可比较
relative mapping cone 与该 kernel complex。

更直接地，radial homotopy vector field在每个 coordinate hyperplane 上
tangent，故其 homotopy operator保持 kernel条件；在 boundary stalk上
contract到一个 \(E\) 中点，constant-pullback在 kernel中为0，因此所有
stalk cohomology为0。在 interior stalk则是 ordinary Poincaré lemma。
该 fine complex所以 resolves \(j_!\mathbf C_U\)，严格计算
\(H^\bullet(X,E)\)，不把 reducible \(E\) 当作 smooth submanifold。
因而 \(\omega\) 定义 canonical relative class \([\omega,0]\)。

可取一个 regular boundary neighborhood \(N\) of the SNC union，
\(N\) topologically deformation retracts到 \(E\)，从而
\(H^2(N,E)=H^3(N,E)=0\)。这里只用 retraction证明 topological cohomology
vanishing，不从一个可能不光滑的 retraction pullback differential forms。
上述 fine relative complex遂给 smooth2-form \(\eta\) on \(N\) 满足
\[
 d\eta=\omega,\qquad i_i^*\eta=0\text{ 对全部 }E_i.
\]
proper relative-SNC family 的 smooth pair trivialization允许固定 \(N\)
和有限 atlas。上述 local homotopies、commuting-projection extensions、
partition of unity和有限 Cech–deRham linear right inverses可全部固定，
应用于 smooth family \(\omega_\lambda\)，给 smooth依赖
\(\lambda\) 的 \(\eta_\lambda\)。这提供任意所需 finite derivative order
的统一界于 compact \(D\)，不需要一个 smooth global retraction。
取 cutoff \(\chi=1\)
near \(E\)，\(\omega_c=\omega-d(\chi\eta)\) compactly supported，代表
\([\omega,0]\)。

一个 smooth form 若对每个 coordinate divisor \(t_b=0\) pullback为0，
其 F10 coefficients 在每个 normal方向都含 \(O(\rho_b)\)，故总为
\(O(\prod_b\rho_b)\)。证明逐项：若该项含 \(dt_b\) 或 \(d\bar t_b\)，
改写 logarithmic coframe提供一个 \(\rho_b\)；若不含该 normal differential，
coefficient在 \(t_b=0\) 消失，real Hadamard lemma给
\(t_b g+\bar t_b h\)。对独立 normal variables重复此分解，得到
product \(\prod_b\rho_b\)，不是只取各个 \(O(\rho_b)\) 的 minimum。

原 \(R^+\) 无 F12 的共同 factor，但其 F10 coefficient仍至多
\(C(1+\sum|\log\rho_b|)\)，而同一 angular coarea bound成立。于是
\(R^+\wedge\eta\) 在所有 faces 上满足 F14（把所有 \(b_b\) 换成1）。
所有 corners 的 total flux uniformly tends to0。degree3 Stokes 的符号
与冻结 boundary comparison相同，得到
\[
 \boxed{B_{\rm canonical}
 :=\lim_{\epsilon\to0}\int_{\partial K_\epsilon}R^+\wedge\chi\eta=0,
 \qquad
 \langle[R^+],[\omega,0]\rangle=\nu_{\rm cut}.}             \tag{F20}
\]
与 F18 相比，这也显示 F16 的 rational open correction对该 canonical
relative top-Hodge pairing为0。不能据此断言它是compact class。

任意 rational horizontal right inverse
\(\sigma:V\to H^3_c(U,\mathbf Q)\) 的 primitive一般不满足
\(\eta|_{E_i}=0\)。故 F20 **不**给 \(B_\sigma=0\)。其不同 trace仍按旧
精确公式登记：rational compact period加 \(B_\sigma\)。
canonical \([\omega,0]\) 和 \(\sigma(\omega)\) 不是同一已证明对象。

## F9. 未 centered 的真实非零 boundary period

这点与 F20 不矛盾，并且阻止把旧 open Tate discrepancy自动升级compact。
以下 independently核验 root 的本轮 local candidate。

在 support \((v_0=-1,v_1=0)\) 上，horizontal ray由
\(2n_0-n_1=0\) 强制为 \((1,2)\)，每个 refinement仍保留这个已有ray。
smooth toric chart可取
\[
 v_0=-1+s,\quad v_1=s^2w,\quad v_2,v_3\text{ free}.
\]
令 \(\Phi=\prod_{i=2,3}(v_i+2+v_i^{-1})\)。fibre equation 为
\[
 F=\Phi(1+s^2w)^2-\lambda(-1+s)w=0,\quad
 w(0)=-\Phi/\lambda,\quad \partial_wF|_{s=0}=\lambda.
\]
free circles取 \(|v_2|=|v_3|=r<1\) 并在 compact annuli中变化；
compact \(D\) 上 \(\Phi\ne0\)、\(\lambda\ne0\)，uniform implicit theorem给
\(|s|<\delta\) 上的 nonzero \(w\)。故
\[
 T^3_\epsilon=\{|s|=\epsilon\}\times\{|v_2|=|v_3|=r\}
\]
bounds实际 \(D^2_s\times T^2\) in \(X_\lambda\)，各 circles CCW。
near \(v_0=-1\) cut \(T_0^+\) 空，仅F1 term \(j=0\) survives：
\[
 R^+=\log^+(-1+s)d\log(s^2w)\wedge d\log v_2\wedge d\log v_3.
\]
对 fixedfree pair，
\[
 \oint_{s}\log^+(-1+s)d\log(s^2w)
 =2a\log^+(-1)=a^2.
\]
\(d\log w\) 为 holomorphic in \(s\) 且在该 disk 上无零，故不贡献 residue。
free两圈各给a，遂
\[
 \boxed{\int_{T^3_\epsilon}R^+=a^4.}                       \tag{F21}
\]
compact closed lift在这个bounding torus上的integral是0。因此旧
\((j^*r-[R^+])/a^4\) 实际具有period \(-1\)，不能属于compact image。
其 relative boundary确实非零，不只是潜在障碍。

centering在这里恰 subtract \(a/2\) 的 \(j=0\) term，得到
\(\operatorname{Log}(1-s)d\log(s^2w)\cdots\)，其 s residue为0。
F12–F14 证明了该局部 cancellation在所有cones/corners同时发生。
root NEW noncompact-Tate-boundary 稿 N1–N12现已实际全文读；
mandatory ray、uniform annuli implicit solution、product orientation、
noncompact conclusion和全centered raw sheet cancellation独核相同。
本稿 F9 用以上直接 chart computation，F2–F5负责该root稿中尚列
conditional的全corner extension。

## F10. 本轮能改变最终 CDT 输入的结果与边界

1. 原来仅有的 actual compact derivative和open regulator comparison，
   现连接到 **explicit centered compact current lift**；不存在需免费
   删除的complex homogeneous scalar gap。F18/F19是这个已标记lift的身份。
2. canonical relative flux现在由所有 surviving cones 的统一 angular
   rank、共同vanishing factors和全部corner estimates严格为0。
3. 未 centered 的 open rational Tate class有真实noncompact boundary
   period，必须保留 F16 的 correction；不能把旧 class本身视为closed
   compact period。其对 canonical top-Hodge trace不贡献 scalar。
4. F19 的 rational cycle marking并非integral normalization；任意旧膜
   仍须通过rational-period ambiguity与此lift比较。未证明denominator
   saturation、全部finite-place/full-rowjet bounds、arithmetic holonomy
   contradiction或任何目标数的新无理性/线性无关性。
5. 证明采用all-scale geometric estimates，没有新增数学producer或数值
   证据充当定理。下一步可对这个明确current marking研究其Betti/jet
   算术packet，而不是继续把自由complex homogeneous correction当未知。

## F11. 实际阅读与来源范围

本稿的 F2–F5、F8 的全corner/coarea/product-factor估计以及 F9 的
local circle computation为独立纸面推导。基础 class/cup/pullback conventions
使用已归档一手来源，不靠二手表述：

* KLM published primary PDF7–12,17在上一轮实际整页读；更早实际读
  PDF1,8–23。本轮为centering另外实际重读PDF8–12，以 unit cup、
  positive/negative branch convention和current product为范围。
* Li published primary上一轮实际PDF4–10；本轮未宣称新的全文阅读。
  unit sector telescope为已实际读的source，不把其epsilon theorem用于
  未满足假设的rawcompactgraph。
* KLII fixed arxiv原件上一轮实际PDF59；更早实际PDF50–61。
  本轮不新套prescribed-pullback theorem以绕过boundary estimates。
* DeligneIII原件此前实际PDF35–41；本轮relative complex的局部证明如
  F8给出，不声称一条未读的general logarithmic-current theorem。
* 本轮 actual全文读冻结 toric completion、positive-cut period comparison、
  boundary membrane comparison以及root NEW noncompact-Tate-boundary
  N1–N12；current main只声称§§73–78，delivery
  只声称current R₀ keys。precise hashes、PDFpages 和receipt另存
  literature/manifest_cdt_odd_R0_positive_cut_boundary_flux_20261006.json。

所有旧/同行数学producer执行/import 数0；原始PDF只供阅读；本轮没有
新网络下载或TLS例外。本文接受后应与root独审以及peer全cone复核一并冻结。

