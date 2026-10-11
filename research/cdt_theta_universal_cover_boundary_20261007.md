# Θ 三阶实际载体的全部共同映射界：三穿孔球面与精确 universal-cover 常数

2026-10-07。隔离 NEW 研究稿。本文不改已定稿的 `cdt_theta_analytic_geometry_20261007.md`，也不改 main、manifest、原仓库或旧 producer。本文只处理 S37–S40 的同一个三阶 Θ 载体；全 s 家族由并行独立稿处理。证明不以有限 prime 样本、浮点 quadrature 或文件 hash 代替数学。没有得到新的数值无理性或 LI 定理。

实质结论为：任何允许这一完整六维实际空间共同 meromorphic pullback 的 CDT 映射，不论其 arctan lift 是否 injective，都满足

\[
 |\varphi'(0)|\le C:=\frac{\Gamma(1/4)^4}{4\pi^2}
 <\frac{3971}{896}<e^{3/2}.
 \tag{U1}
\]

结合任意 full Q(x) basis 的必要费用 \(\tau\ge97/72\) 与 \(J\ge\log|\varphi'(0)|\)，此实际 Θ 三阶载体不能在任何上述共同映射上给 CDT rank 矛盾。该结论扩展了此前只对 slit leaf 或 injective arctan lift 的限制；仍然严格限定这一载体。

## 1. 实际载体及共同 meromorphic 条件强制的省略点

固定 \(\theta=x\partial_x\)，从0正规化实际枝

\[
 R(x)=\log\frac{1+x^2}{1+x},\quad
 P=\theta^2D,\quad Q=\theta D,
\]
\[
 R'=\frac{2x}{1+x^2}-\frac1{1+x},\quad
 P'=-\frac{R}{1-x^2},\quad Q'=P/x,\quad D'=Q/x,
\]
\[
 R(0)=P(0)=Q(0)=D(0)=0,\qquad
 F_u'=(D-u)/(1-x),\quad F_u(0)=0.
 \tag{U2}
\]

这里 \(D=A-B/2\)，\(\Theta=D(1)\)，正是 [桥接稿 S37–S40](cdt_weight4_space_germ_bridge_20261007.md) 的实际对象。仅在 \(\Theta=u\in\mathbb Q\) 的同一个假设下讨论 CDT 的 Q-Taylor 输入。由已 FULL 读取并纸核的 [算术稿 T4/T6/T27](cdt_theta_rank_arithmetic_20261007.md)，

\[
 V=\langle1,R,P,Q,D,F_u\rangle_{\mathbb Q(x)},\qquad
 \dim V=6,
\]
\[
 \text{任意有效 full basis fixed-type 阵列均有}\qquad
 \tau\ge\frac{97}{72}.
 \tag{U3}
\]

U3 是本文调用的已证明 companion theorem，而非重新从数值 rank 或自然基上界推断。它允许任意 rational basis、0处有限 Laurent poles、完整 rational tails、任意固定 \(N^e\)，以及非负 \(\tau^\sharp\)。最新有效 e=0 safe cap 为 [另一稿 N13](cdt_new_repository_carriers_20261007.md) 的 \(191/72\)，这个可行上界不改变 U3 的必要下界。

若某个 full Q(x) basis 在同一个 \(\varphi\) 下共同 meromorphic，则以 inverse rational basis matrix（系数再与 \(\varphi\) 复合）恢复 U2 的各项，特别得到 \(R\circ\varphi\) meromorphic。这一步允许变基矩阵在某些点有 poles；meromorphic 函数的有限和与乘积仍是 meromorphic。对非恒定 \(\varphi\)，分母 rational function 与它复合不会恒等为零。

令 \(q(x)=(1+x^2)/(1+x)\)。任何 transported branch 都有同一个微分

\[
 d(R\circ\varphi)=\frac{d(q\circ\varphi)}{q\circ\varphi}.
 \tag{U4}
\]

若 \(\varphi(z_0)=i\) 或 \(-i\)，local multiplicity 为 \(k\ge1\)，则 \(q\circ\varphi\) 有 order k 的零点，U4 在 \(z_0\) 的 residue 为 k。若 \(\varphi(z_0)=-1\)，则 residue 为 −k。若允许 \(\varphi\) meromorphic 且在 \(z_0\) 有 order k 的 pole，由 \(q(x)\sim x\) 得同一个 residue −k。但 meromorphic 函数的导数在每个 isolated point 的 residue 都为0（逐项微分其 Laurent series 即证）。因此

\[
 \boxed{\varphi\text{ 必全纯，且 omit }-1,i,-i.}
 \tag{U5}
\]

这是真实 logarithm 的必要条件，不以一个 D-finite equation 的 apparent singularity 代替它。后文只使用较弱条件 omit ±i，故忽略 −1 或 transported 0/1 约束只会放大允许映射类。特别不推断任意 transported branch 在0或1自动可去。

## 2. 三穿孔球面的曲率与 elliptic parameter 记号

写 \(\Omega_{01}=\mathbb C\setminus\{0,1\}\)。全文采用 Gaussian curvature −4：

\[
 \rho_{\mathbb D}(z)=\frac1{1-|z|^2},\qquad
 \rho_{\mathbb H}(\tau)=\frac1{2\operatorname{Im}\tau}.
 \tag{U6}
\]

若采用 curvature −1，所有 density 同时乘2，cover derivative 的比值不变。ASVV 的 [§2 与 Theorem 4.7](https://arxiv.org/html/0903.1761v1) 明确使用 \(\Delta\log\rho=4\rho^2\)，其 upper-half-plane pullback 也明确为 U6；不能把这套 convention 与 curvature −1 density 混用。

为避免 modulus 与 parameter 的 factor 错误，定义

\[
 \mathcal K(m)=\int_0^1\frac{dt}{\sqrt{(1-t^2)(1-mt^2)}},
 \quad K_*:=\mathcal K(1/2).
 \tag{U7}
\]

这里 m 是 parameter。DLMF 的 modulus 记号满足 \(\mathcal K(m)=K(\sqrt m)\)，所以 \(K_*=K(1/\sqrt2)\)，不是 \(K(1/2)\) 的 modulus 值。定义见 [DLMF 19.2.4、19.2.8](https://dlmf.nist.gov/19.2)。

ASVV 的 \(a=1/2\) Schwarz map 为

\[
 \tau(m)=i\frac{\mathcal K(1-m)}{\mathcal K(m)}.
 \tag{U8}
\]

它将 upper m-half-plane conformally 映到 ideal triangle

\[
 \Delta=\{\tau\in\mathbb H:0<\operatorname{Re}\tau<1,
                  |\tau-1/2|>1/2\},
\]

三顶点对应 \(m=0,1,\infty\) 的 \(\tau=\infty,0,1\)。[ASVV Lemma 4.1](https://arxiv.org/html/0903.1761v1) 给这一 precise triangle theorem。取 inverse \(\Lambda:\Delta\to\mathbb H\)，由三条 geodesic sides 的 Schwarz reflection 延拓到 \(\mathbb H\)。[Sugawa 的原始稿 printed p.48、PDF page 10](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1042-4.pdf) 明确证明/调用这一延拓为 \(\mathbb H\to\Omega_{01}\) 的 universal covering，并给局部等距公式

\[
 \rho_{01}(\Lambda(\tau))|\Lambda'(\tau)|
       =\frac1{2\operatorname{Im}\tau}.
 \tag{U9}
\]

这是本文使用的标准 global uniformization theorem。其 theta-function 表示为

\[
 \Lambda(\tau)=\frac{\vartheta_2(0,e^{\pi i\tau})^4}
                    {\vartheta_3(0,e^{\pi i\tau})^4},\qquad
 \Lambda(i)=\frac12,
 \tag{U10}
\]

分别见 [DLMF 23.15.6](https://dlmf.nist.gov/23.15.E6) 与 [23.17.1](https://dlmf.nist.gov/23.17.E1)。本文只依赖上述公开的 triangle/universal-cover theorem，不把有限 series 的局部 inverse 当作全局覆盖证明。

## 3. 完整 Wronskian 计算与精确 density

为自行检查 U8/U9 的因子，令 \(U(m)=\mathcal K(m)\)、\(V(m)=\mathcal K(1-m)\)。二者满足

\[
 m(1-m)y''+(1-2m)y'-\frac14y=0.
 \tag{U11}
\]

例如对 U，在 \(|m|<1\) 将 integral 作 binomial expansion，系数为 \((\pi/2)c_n^2\)，\(c_n=\binom{2n}{n}/4^n\)。recurrence \((n+1)^2c_{n+1}^2=(n+1/2)^2c_n^2\) 逐项给 U11；V 由 \(m\mapsto1-m\) 给同一方程，随后 analytic continuation。令 \(W=V'U-VU'\)，则 Abel identity 给

\[
 W'= -\frac{1-2m}{m(1-m)}W,
 \qquad W=\frac{c}{m(1-m)}.
\]

常数也可直接从 integral 核出。\(U(0)=\pi/2\)、U′ 在0有界；代 \(t=\sin\theta\)、再代 \(u=\tan\theta\)，有

\[
 V(m)=\int_0^\infty\frac{du}{\sqrt{(1+u^2)(1+mu^2)}}.
\]

对 \(0<m<1\)，在 \([0,1]\)、\([1,m^{-1/2}]\)、\([m^{-1/2},\infty)\) 分段估计得 \(V(m)=O(1+|\log m|)\)。对 derivative 代 \(v=\sqrt m\,u\)，

\[
 mV'(m)=-\frac12\int_0^\infty
  \frac{v^2\,dv}{\sqrt{m+v^2}(1+v^2)^{3/2}}
  \longrightarrow-\frac12.
\]

dominated convergence 的上界为可积函数 \(v/(1+v^2)^{3/2}\)，其 integral 为1。因此 \(mW\to-\pi/4\)，从而

\[
 \boxed{\tau'(m)=-\frac{i\pi}{4m(1-m)\mathcal K(m)^2}.}
 \tag{U12}
\]

这也与 ASVV Theorem 4.7 proof 的 exact derivative 一致。在 \(m=1/2\)，U8 给 \(\tau=i\)，U12 给 \(\tau'=-i\pi/K_*^2\)。U9 遂给

\[
 \rho_{01}(1/2)=\frac{|\tau'(1/2)|}{2\operatorname{Im}i}
               =\frac{\pi}{2K_*^2}.
 \tag{U13}
\]

只用 U13 已足够；作为独立 primary check，ASVV Corollary 4.11 直接给同一值 \(8\pi^2/\Gamma(1/4)^4\)。再取 affine map

\[
 T(x)=\frac{x+i}{2i}:\Omega:=\mathbb C\setminus\{-i,i\}
                      \longrightarrow\Omega_{01},
 \quad T(0)=1/2,
 \quad |T'(0)|=1/2.
\]

由 conformal covariance，

\[
 \boxed{\rho_\Omega(0)=\frac{\pi}{4K_*^2}.}
 \tag{U14}
\]

另一个独立 convention check 是 [Herron–Lindquist §2.C.2、Fact 2.13](https://arxiv.org/pdf/2011.11016)：其 curvature −1 记号有 \(\lambda_{\mathbb D}(0)=2\) 与 \(1/\lambda_{01}(-1)=\Gamma(1/4)^4/(4\pi^2)\)。Möbius \((x-i)/(x+i)\) 在0值 −1、derivative 模2，故 \(\lambda_\Omega(0)=2/C\)，再除2正好等于 U14。

## 4. 对所有 disk maps 的 sharp bound，及一个显式极值 cover

令 \(p:\mathbb D\to\Omega\) 是 universal cover，\(p(0)=0\)。U6 与 local isometry 给

\[
 |p'(0)|=\frac{\rho_{\mathbb D}(0)}{\rho_\Omega(0)}
         =\frac{4K_*^2}{\pi}=:C.
 \tag{U15}
\]

对任何 holomorphic \(f:\mathbb D\to\Omega\)、\(f(0)=0\)，simply connected disk 的 covering lift 唯一给 \(f=p\circ h\)、\(h:\mathbb D\to\mathbb D\)、\(h(0)=0\)。Schwarz lemma 给 \(|h'(0)|\le1\)，故

\[
 \boxed{\sup_{f:\mathbb D\to\Omega, f(0)=0}|f'(0)|=C.}
 \tag{U16}
\]

该 proof 完全不要求 f injective，也不要求 arctan lift injective。对于在 closed unit disk 的邻域全纯的映射，仍有同一 upper bound；极值以 radial shrinking 任意接近。

更明确地，取

\[
 c(z)=i\frac{1+iz}{1-iz}=\frac{i-z}{1-iz},\qquad
 \Phi(z)=2i\Lambda(c(z))-i.
 \tag{U17}
\]

c 是 disk 到 upper half plane 的 conformal map，\(c(0)=i\)、\(c'(0)=-2\)。U12 给 \(\Lambda'(i)=iK_*^2/\pi\)，故 Φ 是省略 ±i 的 universal cover，\(\Phi(0)=0\)、\(\Phi'(0)=4K_*^2/\pi>0\)。\(\Phi_\rho(z)=\Phi(\rho z)\) 在 \(|z|<1/\rho\) 全纯，导数为 \(\rho C\)。这确立 omission class 的 sharpness；并不声称 \(\Phi_\rho\) 自动是 U2 的有效共同映射。Θ 实际空间还要求 omit −1，并满足 transported 0/1 的枝条件。

## 5. Gamma 值的自含积分推导

由 U7，对0≤t≤1作 substitution

\[
 x=\frac{\sqrt2\,t}{\sqrt{1+t^2}},\qquad
 dx=\frac{\sqrt2\,dt}{(1+t^2)^{3/2}},
\]
\[
 1-x^2=\frac{1-t^2}{1+t^2},\qquad
 1-x^2/2=\frac1{1+t^2},
\]

得到

\[
 K_* =\sqrt2\int_0^1\frac{dt}{\sqrt{1-t^4}}
      =\frac{\sqrt2}{4}B(1/4,1/2).
\]

Euler beta identity、reflection identity 与 half value 分别见 [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1)、[5.5.3](https://dlmf.nist.gov/5.5.E3)、[5.4.6](https://dlmf.nist.gov/5.4.E6)。因此

\[
 B(1/4,1/2)=\frac{\Gamma(1/4)\sqrt\pi}{\Gamma(3/4)},\qquad
 \Gamma(1/4)\Gamma(3/4)=\pi\sqrt2,
\]
\[
 \boxed{K_* =\frac{\Gamma(1/4)^2}{4\sqrt\pi},\qquad
 C=\frac{4K_*^2}{\pi}=\frac{\Gamma(1/4)^4}{4\pi^2}.}
 \tag{U18}
\]

这核定了 requested constant，约为4.3768796（此小数仅是 primary source 的说明值；后面的严格比较不依赖它）。

## 6. 比 \(C<5\) 更强的纯有理证书

定义 \(c_n=\binom{2n}{n}/4^n\)。由 binomial expansion 与 Wallis integral recurrence，

\[
 K_*=\int_0^{\pi/2}(1-\tfrac12\sin^2\theta)^{-1/2}d\theta
     =\frac\pi2\sum_{n\ge0}c_n^2\,2^{-n}.
 \tag{U19}
\]

交换 sum/integral 可由 \(\sin^2\theta/2\le1/2\) 的 uniform convergence，或正项 monotone convergence 证明；\(\int_0^{\pi/2}\sin^{2n}\theta d\theta=(\pi/2)c_n\) 由一次 integration by parts 递推。展开亦与 [DLMF 19.5.1](https://dlmf.nist.gov/19.5.E1) 完全一致。

令 \(S=2K_*/\pi\)。因为 \(c_{n+1}/c_n=(2n+1)/(2n+2)<1\)，\(c_3=5/16\)，

\[
 S\le1+\frac18+\frac9{256}
          +\frac{25}{256}\sum_{n\ge3}2^{-n}
   =\frac{1213}{1024}<\frac{19}{16}.
 \tag{U20}
\]

为连 \(\pi<22/7\) 也纸面闭合，

\[
 0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=\frac{22}{7}-\pi.
\]

等式的多项式除法是

\[
 \frac{x^4(1-x)^4}{1+x^2}
 =x^6-4x^5+5x^4-4x^2+4-\frac4{1+x^2};
\]

其中 \(4/(1+x^2)\) 的积分为π，多项式部分的积分为22/7。于是

\[
 C=\pi S^2<\frac{22}{7}\frac{361}{256}
       =\frac{3971}{896}<\frac{5711}{1280}
       =\sum_{j=0}^{5}\frac{(3/2)^j}{j!}<e^{3/2}.
 \tag{U21}
\]

唯一中间有理差为 \(5711/1280-3971/896=267/8960>0\)。特别 \(3971/896<5\)。全部 inequalities 是有理运算、正项尾界和一个显式正积分，不需要 Γ 的小数计算。

## 7. 同一六维 Θ full carrier 的 all-map CDT 边界

令 φ 为 CDT 允许的 nonconstant 映射，\(\varphi(0)=0\)、\(\varphi'(0)\ne0\)，在 closed unit disk 的邻域满足共同 meromorphic pullback。由 U5 它在 disk 内全纯且 omit ±i，所以

\[
 L:=\log|\varphi'(0)|\le\log C<\frac32.
 \tag{U22}
\]

若 φ 在 circle 上全纯，双边界量

\[
 J(\varphi)=\iint_{\mathbb T^2}
       \log|\varphi(z)-\varphi(w)|\,d\mu(z)d\mu(w)
\]

满足 \(J\ge L\)。确切地，对固定 w，Jensen 应用于 \(z\mapsto\varphi(z)-\varphi(w)\)，给 inner mean 至少 \(\log|\varphi(w)|\)；再对 \(\varphi(w)/w\) 应用 Jensen，给 outer mean 至少 \(\log|\varphi'(0)|\)。边界零点只给可积 logarithmic singularities；可先取半径 <1 再取 limit。若所允许更一般边界导致 \(J=+\infty\)，它亦不能产生所需有限 rank 上界。

对于 \(m=6\)，CDT 的 positive denominator 为 \(L-\tau>0\)，其 rank 上界严格小于真实 rank6的必要条件是

\[
 \frac{J}{L-\tau}<6
 \quad\Longrightarrow\quad
 \tau<L-\frac J6\le\frac56L.
 \tag{U23}
\]

U3/U22 却给

\[
 \tau-\frac56L>
 \frac{97}{72}-\frac54=\frac7{72}>0.
 \tag{U24}
\]

等价地，任何这种 rank 矛盾至少需要

\[
 L>\frac65\frac{97}{72}=\frac{97}{60}>\frac32,
\]

与 U22 冲突。故

\[
 \boxed{\text{此三阶 Θ 六维 full carrier，任意 full Q(x) basis、
 任意实际共同 CDT map，均不能给 CDT rank 矛盾。}}
 \tag{U25}
\]

该 theorem 不只针对 arctan-lift injective subclass；basis 后的取消也由恢复 R 的 U4/U5 支付。本文没有由此证明所有 maps 均有 \(L-\tau\le0\)：必要费用97/72仍低于 \(\log C\)，所以这里只封住完整 rank contradiction 门槛。本文也不排除新的不同 carrier、真实 quotient 子空间或新的周期实现。

## 8. β 的边界仍保留，不能外推 U25

对桥接稿的 β(4) 六维 full space，S22 仅给 \(\tau\ge11/9\)。同样的 omission pair upper bound 与 \(J\ge L\) 只迫使可能的 rank 矛盾满足

\[
 L>\frac65\frac{11}{9}=\frac{22}{15},\qquad
 e^{22/15}<|\varphi'(0)|\le C.
 \tag{U26}
\]

lower endpoint 约4.335，upper endpoint 约4.377；这些小数只是解释剩余范围。U21 的 \(\log C<3/2\) 并不能推出 \(\log C\le22/15\)。因此本文不宣称 all β maps no-go，也未证明这段必要范围内有满足全部 transported branch/J/finite denominator 条件的 β map。此前 injective arctan-lift subclass 的 sharp size π 及其失败结论仍是更窄映射类的结果。

## 9. 来源、全文阅读与独立核对的准确范围

本轮实际 FULL 读取桥接稿 S1–S40、算术稿 T1–T27、已定稿几何稿 G1–G26；这些是 carrier、necessary arithmetic 和此前 map 范围的内部输入。本文 U4/U5、U11–U24 的积分、Wronskian、normalization、universal lift、理性证书及 rank 比较均逐式纸核。两名独立子审分别核了原始 universal-cover/curvature normalization 与 Gamma/rational certificate；二者都确认 U18 无额外 factor2。随后 root 实际 FULL 读取本稿最终九节 U1–U26，独立数学审阅确认 PASS；作者在完成引用、范围说明及此收据后再次 FULL 回读。这个收据不把独立 s3 检查外推到全 s。

实际 primary 阅读范围为：ASVV 0903.1761 的 §2、§3、Lemma 4.1、Theorem 4.7 及其 proof、Corollary 4.11；Sugawa 1042-4 的 printed p.47–48 相关 Hempel/covering 段；Herron–Lindquist 的 §2.C.2、Fact 2.13；DLMF 所链接的 elliptic、beta、reflection、half value 和 modular-function formulas。没有声称 FULL 读取这三篇外部原论文的所有页，也没有直接读取1968年 Agard 原文；本文用实际看到的 primary presentation 与自行重推代替未经核验的记忆。

所用网页/PDF 已实际下载到
`literature/cdt_theta_universal_cover_sources_20261007/`：
`asvv_0903.1761v1.html`、`sugawa_1042-4.pdf`、
`herron_lindquist_2011.11016.pdf`、DLMF 19.2/19.5/5.12/5.5/5.4/23.15/23.17 的 HTML。
其逐文件 URL、actual bytes 和 SHA256 记录在同目录 `source_receipts.json`；同目录 `reading_scope.md` 逐项区分节选读取、公式查看、完整归档及子审的额外交叉核对。归档是来源留存，hash 只认证文件，没有数学证明功能。保存、阅读和写后 FULL 回读以外，没有运行旧数学 producer、PSLQ、Lean、prime pool 扩表或浮点 quadrature。
