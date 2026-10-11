# 九阶实际 MUM 系统的 Gamma 连接行、奇 ζ 投影与 Taylor 模块缺口

日期：2026-10-07。本稿为唯一 NEW 纸面主稿；580 条冻结记录、旧 producer、guard 与素数表全部只读。未创建或执行数学 producer，未 import/rerun 旧或同行数学文件。本稿的 Gamma 连接公式使用已有定理，不宣称首次发现 Gamma-class 现象，也不宣称任何新数值无理性。

## 一、保留原对象的九阶齐次系统

上一轮最终稿 `cdt_odd_period_extension_relation_leaf_20261007.md` E11–E17 中的 U 取参数

\[
 a=(\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12,
       \tfrac15,\tfrac25,\tfrac35,\tfrac45),\qquad r=9.
\]

其实际 ζ(5) quasi-period 仍为指定的 \(G(w)=-P(\theta_w)U(w)/380928\)，原 source 仍是 \(\alpha\zeta(4)+\beta\zeta(5)\)。这里没有把它改成一个任意 Gamma period。Kerr 2026 Theorem 4.11 的几何解释有 Hodge-cycle/defined-over-Q 假设；本稿只使用实际微分方程和 Frobenius/monodromy 定理。

**G1（同一 U 的齐次部分）。** 令 \(z=1/w\)、\(D_z=z\partial_z\)。实际 particular 满足

\[
 L_z U(1/z)=1,\qquad L_z=D_z^9-z\prod_{a_i\in a}(D_z+a_i).
 \tag{G1}
\]

所以以下 rank-nine homogeneous system 是原 U 的实际齐次系统；连接系数属于这个系统，却不自动等于原 ordinary endpoint 的 \(\zeta(5)\) quasi-period。

**G2（变量缩放与整 fundamental period）。** 取

\[
 \Lambda=2^{10}5^5=3200000,\quad z=\Lambda t,\quad c=\Lambda^{-1},
 \qquad L_t=D^9-\Lambda t\prod_i(D+a_i).
\]

有限反射点为 \(t=c\)，不是原 ordinary endpoint \(z_0=-3125/1024\)。在这个整数坐标中

\[
 f_0(t)=\sum_{n\ge0}h_nt^n,\qquad
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}
 =\binom{2n}{n}^{5}\binom{5n}{n,n,n,n,n}\in\mathbb Z.
 \tag{G2}
\]

缩放把所有有限奇点的位置一起改变；不能只领取整性而保留未缩放的 conformal radius。

**G3（完整 Frobenius 解与正则部分）。** 固定正实路径 \(0<t<c\) 上的实 \(\log t\) 分支，定义

\[
 \Phi(s,t)=t^s\sum_{n\ge0} A_n(s)t^n,\quad
 A_n(s)=\Lambda^n\frac{\prod_i(a_i+s)_n}{(1+s)_n^9},
 \qquad L_t\Phi=s^9t^s.
 \tag{G3}
\]

一律用系数而非未除 factorial 的导数：

\[
 \phi_j=[s^j]\Phi(s,t),\qquad
 \eta_j=[s^j]\bigl(t^{-s}\Phi(s,t)\bigr).
\]

\(\phi_0,\ldots,\phi_8\) 是完整齐次 Frobenius basis；\(\eta_j\in\mathbb Q[[t]]\)，且

\[
 \phi_j=\sum_{k=0}^j\frac{(\log t)^k}{k!}\eta_{j-k},\quad
 \eta_0=f_0,\quad \eta_j(0)=0\ (j>0).
 \tag{G4}
\]

对 \(j>0\)，\(\phi_j\) 与 \(\eta_j\) 不可互换：前者的 leading term 是 \((\log t)^j/j!\)，后者是正则 Taylor germ。

## 二、完整反射连接行及明确的 ζ(5)、ζ(7) 目标

**G4（所用定理及非零跳跃）。** 本参数的 \(a_i-1\) 全非整数。Bloch–Vlasenko Proposition 26，结合其 Definition 22，给出沿上述固定路径的全部 Frobenius constants。反射点的 local exponents 是

\[
 0,1,\ldots,7,\quad 8-\sum a_i=\tfrac72.
 \tag{G5}
\]

故 local monodromy \(T_c-I\) 为 rank one 的反射，非 unipotent transvection。令
\(\psi=(T_c-I)\phi_0\)。它非零：若 \(\phi_0\) 同时被 \(T_c\) 固定和被 MUM \(T_0\) 固定，其线便对完整三点 monodromy 不变，与该 hypergeometric system 的 irreducibility 矛盾。归一化使 \(\kappa_0=1\)。于是

\[
 (T_c-I)\phi_j=\kappa_j\psi\quad(0\le j\le8).
 \tag{G6}
\]

**G5（全连接行的 exact generating function）。** 未缩放 \(z\) 坐标中，定理给出 \(\Gamma(1+s)^9\prod_i\Gamma(a_i)/\prod_i\Gamma(a_i+s)\)。由于 \(t^s=\Lambda^{-s}z^s\)，在本稿整数坐标中必须乘 \(c^s\)。因此

\[
 \kappa(s):=\sum_{j\ge0}\kappa_js^j
 =\Lambda^{-s}\frac{\Gamma(1+s)^9\prod_i\Gamma(a_i)}
                         {\prod_i\Gamma(a_i+s)}
 =\frac{\Gamma(1+s)^{15}}{\Gamma(1+2s)^5\Gamma(1+5s)}.
 \tag{G7}
\]

最后等式来自二倍、五倍 Gamma multiplication：
\(\Gamma(1/2+s)/\Gamma(1/2)=2^{-2s}\Gamma(1+2s)/\Gamma(1+s)\)，以及四个 fifth 参数乘积为 \(5^{-5s}\Gamma(1+5s)/\Gamma(1+s)\)。因此 \(\log\Lambda\) 的消失来自明确的变量缩放，不是略掉未知常数。

G7 给出全部 nine-dimensional homogeneous connection **行**，即 \(\kappa_0,\ldots,\kappa_8\)；高于8的项属于 Frobenius extensions，不能称为 rank-nine 内的新齐次解。若写 \(\psi=\sum w_i\phi_i\)，完整反射矩阵还有列 \(w\)，且 \(T_c=I+w\kappa^{\mathsf T}\)、\(\kappa^{\mathsf T}w=-2\)。本稿不声称已经单独求出 \(w\) 或整个 0-to-infinity connection matrix。Golyshev–Mellit 提供一般 Gamma/Vandermonde monodromy matrices；无需未经检查地套用其 \((-1)^r\) 坐标约定。

**G6（显式展开）。** Euler 常数项因 \(15-10-5=0\) 消失。标准 log-Gamma Taylor formula 给出

\[
 \log\kappa(s)=\sum_{m\ge2}\ell_ms^m,\qquad
 \ell_m=\frac{(-1)^m}{m}(15-5\cdot2^m-5^m)\zeta(m).
 \tag{G8}
\]

例如 \(\ell_2=-15\zeta(2)\)、\(\ell_3=50\zeta(3)\)、\(\ell_4=-345\zeta(4)/2\)、\(\ell_5=654\zeta(5)\)、\(\ell_6=-2655\zeta(6)\)、\(\ell_7=11250\zeta(7)\)、\(\ell_8=-195945\zeta(8)/4\)。指数展开后

\[
 \begin{aligned}
 \kappa_0&=1,&\kappa_1&=0,&\kappa_2&=-15\zeta(2),&\kappa_3&=50\zeta(3),\\
 \kappa_4&=\tfrac{435}{4}\zeta(4),\\
 \kappa_5&=654\zeta(5)-750\zeta(2)\zeta(3),\\
 \kappa_6&=1250\zeta(3)^2-\tfrac{9405}{16}\zeta(6),\\
 \kappa_7&=11250\zeta(7)-9810\zeta(2)\zeta(5)
                   +\tfrac{10875}{2}\zeta(3)\zeta(4).
 \end{aligned}\tag{G9}
\]

\(\kappa_8\) 以及全部后续系数由 G7/G8 完整确定，不需要数值 recognition。G9 所列纯化简使用 \(\zeta(2)^2=5\zeta(4)/2\)、\(\zeta(2)\zeta(4)=7\zeta(6)/4\)、\(\zeta(2)^3=35\zeta(6)/8\)。这是可检查的新目标接口；没有证明这些组合的无理性。

**G7（真正的 relation-filled homogeneous row）。** 对 \(1\le j\le8\)、固定 \(u\in\mathbb Q\)，

\[
 F_{j,u}=\phi_j-u\phi_0,\qquad
 (T_c-I)F_{j,u}=(\kappa_j-u)\psi.
 \tag{G10}
\]

若数值假设 \(\kappa_j=u\) 成立，消去的是完整实际跳跃；由 G5，反射不变的齐次解均在 \(c\) holomorphic，因此此 row 确实填去这个 conifold branch。尤其 \(j=5\) 是 G9 的 unscaled 混合 ζ 目标，而不是 \(\zeta(5)/(2\pi i)^5\) 的假设。

但 \(F_{j,u}\) 在起点0仍含 \((\log t)^j/j!\)；\(u\phi_0\) 不能改变它。有限覆盖 \(t=v^h\) 只把最高 log 系数乘 \(h^j\)。它不属于 \(\mathbb Q[[t]]\)，不能把以下 \(\eta\) 分母 cap 或 CDT Taylor theorem 移植给它。改在 ordinary point 展开又需要证明全部 Taylor coefficients rational，并支付其完整 connection constants；数值假设 G10 单独不提供此项。

## 三、Tate 与实结构投影的费用

**G8（纯 odd 行确可构造，但常数域不同）。** 记 \(q=2\pi i\)、\(\widehat\phi_j=q^{-j}\phi_j\)、\(\widehat\kappa_j=q^{-j}\kappa_j\)。偶 log-Gamma 系数 \(\ell_{2m}/q^{2m}\in\mathbb Q\)。令

\[
 E(s)=\exp\!\left(-\sum_{m\ge1}\ell_{2m}(s/q)^{2m}\right)
       \in\mathbb Q[[s^2]].
\]

头两项为 \(E_2=-5/8\)、\(E_4=121/384\)。因 \(\widehat\kappa_1=0\)，下列确为完整 homogeneous period rows：

\[
 \begin{aligned}
 Y_5&=\widehat\phi_5-\tfrac58\widehat\phi_3,
 &(T_c-I)Y_5&=\frac{654\zeta(5)}{q^5}\psi,\\
 Y_7&=\widehat\phi_7-\tfrac58\widehat\phi_5
                       +\tfrac{121}{384}\widehat\phi_3,
 &(T_c-I)Y_7&=\frac{11250\zeta(7)}{q^7}\psi.
 \end{aligned}\tag{G11}
\]

若补上 \(E_4\widehat\phi_1\)、\(E_6\widehat\phi_1\) 等完整卷积 terms，其跳跃为0，因此不影响 G11。至 weight7，去掉偶 exponential 后的 odd exponential 还未产生两个或三个 odd weights 的 weight5/7 混合项；weight9 开始会有 \(\zeta(3)^3\)，不能宣称所有 odd coefficients 从此自动纯化。

**G9（不能免费回到 Q-Taylor/原 target）。** G11 中的 rational coefficients 是对这个 Tate-normalized complex period basis 而言；basis 自身含 \(q^{-j}\) 且有 log terms。其有理 Betti lattice、Gamma comparison 与 integral index 须另行指定，不能直接宣布它就是 \(\mathbb Q[[t]]\) 的函数族。\(\zeta(5)\in\mathbb Q\) 并不推出 \(\zeta(5)/q^5\in\mathbb Q\)。奇数次 normalized constants 是纯虚数；取实部会使其值消失，乘 \(i\) 后仍支付 \(\pi^{-5}\) 或 \(\pi^{-7}\)。raw basis 中纯化的乘子含 \(\zeta(2)\)、\(\zeta(4)\)，不是 Q coefficients。G11 是真实的 Gamma/Tate 结构，不是原 source 的免费新无理性证明。

## 四、正则 Taylor functions 的真实 rank 与全部有限处分母

**G10（剥离 log 的精确 monodromy 公式）。** 在 conifold loop 上 \(\log t\) 不跳跃，因为该小 loop 不绕0。由 G4/G6 的逆三角变换得到

\[
 (T_c-I)\eta_j
   =\psi\sum_{k=0}^j\kappa_{j-k}\frac{(-\log t)^k}{k!}
   =:\psi H_j(\log t),\qquad 0\le j\le8.
 \tag{G12}
\]

\(H_j\) 的 degree 恰为 \(j\)，leading coefficient 为 \((-1)^j/j!\)，无任何未知 connection 常数。即使 \(u=\kappa_j\)，

\[
 (T_c-I)(\eta_j-u\eta_0)
 =\psi\{H_j(\log t)-u\}\ne0\quad(j\ge1).
 \tag{G13}
\]

所以完整 \(\phi\) row 的 relation-fill 在取 analytic parts 后确实失效，而不是缺了一项形式注释。

**G11（新的可用函数秩接口）。** 对任意 \(0\le d\le8\)，

\[
 \{1,\eta_0,\eta_1,\ldots,\eta_d\}
 \quad\text{在 }\mathbb C(t)\text{ 上线性无关；秩为 }d+2.
 \tag{G14}
\]

证明：设 \(r_*(t)+\sum_{j=0}^d r_j(t)\eta_j(t)=0\)，其中 \(r\in\mathbb C(t)\)。在所有 rational coefficients 无 pole 的普通点取 germ，并沿固定路径绕 conifold，G12 给
\(\psi\sum r_j(t)H_j(\log t)=0\)。非零 \(\psi\) 可在 meromorphic germ 域中消去。\(\log t\) 对 \(\mathbb C(t)\) 超越：若满足有限次 polynomial equation，则沿0反复 continuation 的 \(\log t+2\pi iN\) 会在普通点给无穷多个根，矛盾。因此最高 log 系数首先强制 \(r_d=0\)，降阶依次给全部 \(r_j=0\)，最后 \(r_*=0\)。故这也是实际 \(\mathbb Q(t)\)-rank，而非矩阵 minors 的 rank。

更一般地，G12 还证明在此 fixed analytic-part package 中，唯一 conifold-invariant 的 \(\mathbb C(t)\)-linear combination 是 rational-function row本身。允许 rational 变基或假设某一个 \(\kappa_j\in\mathbb Q\)，均不改变这个结论。

**G12（holonomic 性）。** 将 \(t^{-s}L_tt^s\) 写为 \((D+s)^9-\Lambda t\prod_i(D+s+a_i)\)，对 s 逐阶取系数，得到 \(\eta_j\) 的有限 triangular inhomogeneous differential system over \(\mathbb Q(t)\)。每个 \(\eta_j\) 均 holonomic；也可用有限 log-Kummer tensor 和 G4 说明。这里仅说实际 scalar functions holonomic，不把其共同 minimal first-order system rank 与 G14 混同。

**G13（all-prime LCM cap）。** 令 \(D_N=\operatorname{lcm}(1,\ldots,N)\)。从实际系数有

\[
 \frac{A_n(s)}{h_n}
 =\frac{\displaystyle\prod_i\prod_{\ell=0}^{n-1}
          (1+s/(a_i+\ell))}
        {\displaystyle\prod_{\ell=1}^n(1+s/\ell)^9}.
 \tag{G15}
\]

每个 numerator reciprocal 是 \(2/(2\ell+1)\) 或 \(5/(5\ell+k)\)，分母皆 \(\le5n\)。denominator factors 的 negative-binomial coefficients 是整数，且每次 degree contribution 消耗同样数量的 \(\ell^{-1}\)。每个 s-degree-j term 共恰 j 个 reciprocal，因此

\[
 D_{5n}^{\,j}[s^j]A_n(s)\in\mathbb Z
 \quad(n\ge1,\ 0\le j\le8).
 \tag{G16}
\]

这支付了 prime2、prime5 及所有其他有限处，未仅对 auxiliary progression 主张整性。因为使用 \([s^j]\) 而非 \(\partial_s^j\)，没有遗落 factorial。该 cap 是明确安全 upper bound，不是最小费用定理。

**G14（已支付的 CDT flat 参数）。** 对 G14 的完整 fixed basis，按 \(1,\eta_0,\eta_1,\ldots,\eta_d\) 排序，取 \(m=d+2\)、\(e=0\)，用 d 个 width5 的嵌套 LCM columns，使 \(\eta_j\) 激活前 j columns。row sums 为

\[
 \sigma=(0,0,5,10,\ldots,5d),\qquad
 \tau^\flat=\frac{5}{(d+2)^2}\sum_{j=1}^d j(2j+3)
 =\frac{5d(d+1)(4d+11)}{6(d+2)^2}.
 \tag{G17}
\]

例如 d5 给实际函数秩7、\(\tau=775/49\)；d7 给秩9、\(\tau=1820/81\)；d8 给秩10、\(\tau=129/5\)。这些按固定 CDT v2 Definition 6.0.1/Theorem 6.0.2 计算；若改 basis、变 coordinate 或只选一部分 rows，须重新算整个 array。holonomic hypothesis 可使 Corollary 6.0.14 的 derivative 门槛从 \(e^{\sigma_m}\) 放宽到 \(e^\tau\)，但不会取消实际单值 meromorphic pullback 条件。

## 五、为何 rational de Rham quotient 不能直接删掉 MUM 链

**G15（全局 irreducibility）。** Golyshev–Mellit 的 hypergeometric criterion 给出本 rank-nine system 在 \(\mathbb C(t)\) 上 irreducible：P 的 roots 为0，Q 的 roots为 \(-a_i\)，差值均非整数。MUM 点的 log filtration 是一个局部 monodromy flag，并非自动的全局 rational differential submodule。

**G16（rational differential projection 的精确限制）。** 对本 irreducible scalar operator L，任一非零齐次解的 minimal annihilator over \(\mathbb C(t)\langle D\rangle\) 是 L（up to units）：若它同时被某个 lower-order operator annihilate，右 gcd 给 L 的非平凡 right factor，与 irreducibility 矛盾。因此 rational differential operator 若 annihilate 某个非零齐次 period，就 annihilate 全部 L-solutions，除非它并不真正 annihilate而只是映射到另一系统。

所以不能用一个未经支付的 rational projector，杀掉 \(\phi_1,\ldots,\phi_8\) 的 log chains同时保留 \(\phi_0\) 的同一全局 period system。换到 \(\eta\) 确能得 Taylor germs，却属于显式 log-Kummer/extension construction，具有 G12 的 polynomial jump、G14 的实际函数秩和 G16 的分母账本。它不是对 rank-nine module 免费取一个低秩 quotient。

**G17（起点与单值条件不可分开）。** G10 在 conifold 真填 branch，却不能以0作为 rational Taylor 起点；G14/G16 在0提供真正 rational Taylor族，却由 G12/G13 不能借单一 \(\kappa_j=u\) 填该 branch。取 ordinary起点的 \(\phi_j-u\phi_0\) 需要其完整 comparison matrix 令所有 Taylor coefficients rational，不是只有函数值或一个连接 coefficient rational。

若拟应用 CDT v2 Corollary 6.0.14，须构造实际 holomorphic mapping \(\varphi:(\mathbb D,0)\to(\mathbb C,0)\)，使所选所有 function pullbacks meromorphic于 \(\mathbb D\)，且

\[
 \log|\varphi'(0)|>\tau,
 \qquad m>
 \frac{J(\varphi)}{\log|\varphi'(0)|-\tau},\quad
 J(\varphi)=\iint_{\mathbb T^2}
       \log\max(|\varphi(z)|,|\varphi(w)|)\,d\mu(z)d\mu(w).
 \tag{G18}
\]

所用 boundary/integrability 或 limiting hypotheses 与原定理一致。这里 \(\varphi\) 本身 holomorphic，meromorphic 的是函数 pullbacks。G18 是 contradiction 所需的严格接口；本稿没有找到满足全部条件的 relation-dependent leaf，也没有把大 radius 的一个标量函数当成所需 m 个独立函数。

## 六、本轮得到与仍缺的具体信息

**G18（可以直接继续的目标）。** G9 的 \(\kappa_5\)、\(\kappa_7\) 是原九阶系统的真实 unscaled connection constants。\(\kappa_j=u\in\mathbb Q\) 确导致 G10 的 homogeneous branch-fill，比 ordinary endpoint−u 多了一项可检验的 monodromy事实。G11 展示 pure odd Tate rows，却不能删掉 normalization费用。

**G19（尚未闭合之处）。** 要由这些连接行证明新数值无理性，仍须构造一个同时满足 rational Taylor、保留这条 relation-dependent branch-fill、完整 \(\mathbb Q(t)\)-rank 与 all-prime caps 的实际 extension/subsystem。G12–G14 已给出具体阻碍：在当前 analytic-part package 内，即使允许 rational function变基，任何非 rational row均不能填 conifold；其最高 log degree 不依赖 \(\kappa_5\) 或 \(\kappa_7\) 的值。可能的新对象必须超出这一个 package，例如另行构造并校准的 dual/relative extension；不能仅改写其 basis。相应 geometric projection、完整 constants、Taylor整性与实际 leaf 都尚未证。

本轮结果不替换原 \(\alpha\zeta(4)+\beta\zeta(5)\) source、不移植旧 whole-S费用、不证明 ζ(7)、Catalan 或任何其他新常数的无理性。得到的是全反射连接行、两个明确混合ζ目标、可核 pure-Tate rows，以及新的实际函数 rank/cap/branch obstruction接口。

## 七、原件、实际页域与证据边界

新增 primary archives（正常 TLS、certificate验证保留，无重复下载）：

1. [Bloch–Vlasenko, Gamma functions, monodromy and Frobenius constants, arXiv1908.07501v2](https://arxiv.org/pdf/1908.07501v2)，43页。文件 `literature/cdt_gamma_connection_sources_20261007/bloch_vlasenko2020_gamma_frobenius_arxiv1908_07501v2.pdf`，SHA256 `d8f04d9d6477c2da86cc05516d8a865fbb582e44b1e280749b690f707cc43994`。本轮本人实际 FULL PDF1–4、15–21，共11页；其中15–20支持 G4–G7；21的数值 examples不用于本稿定理。
2. [Golyshev–Mellit, Gamma Structures and Gauss's Contiguity, arXiv0902.2003v1](https://arxiv.org/pdf/0902.2003v1)，10页。文件 `literature/cdt_gamma_connection_sources_20261007/golyshev_mellit2009_gamma_structures_arxiv0902_2003v1.pdf`，SHA256 `239c64b8bab41b12bc2a41d8eb3630d2935e04365bf6a3b9919193793551fc20`。本人本轮实际 FULL PDF1–10，共10页，特别2的 irreducibility/反射及8–9的 monodromy matrices。
3. [NIST DLMF 5.7, Gamma series](https://dlmf.nist.gov/5.7)，本轮实际读网页与5.7.3/5.7.4公式；另正常TLS存 `literature/cdt_gamma_connection_sources_20261007/nist_dlmf_5_7_gamma_series_20261007.html`，SHA256 `c0e07097dba1e3ec7006bb0fcd06e45d24d5b0a058062aeacc8749dfd54b3309`。仅用于标准 Gamma Taylor，网页不计PDF页数。

已有 primary，本轮重新实际 FULL读取：Kerr2020 `kerr2020_unipotent_extensions_arxiv2008_03618v1.pdf` PDF1–5、16–18、23–25，共11页；Kerr2026 `kerr2026_three_vignettes_arxiv2602_04128v1.pdf` PDF8–11，共4页；固定 CDT v2 `cdt2024_l2_chi_minus3.pdf` PDF66–69，共4页。本人本轮 distinct primary PDF页数为 **40**，不是归档53页的全读，也不继承上轮68页或同行读域。

已实际全文读上轮 period-extension 最终稿 E1–E24，以及 authority main §§176–180/current-progress。本稿所有算式为纸证；documentary PDF/text读写与hash不算数学 producer。仅 source connection行已计算；完整 Γ/Barnes0-to-infinity comparison的其余 rows、可用 relation-leaf与新数值结论均明确保留为未证。
