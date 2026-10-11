# 第251轮：实际正处盈余门槛与双覆盖族的全参数能量障碍

2026-10-10，B，纸证。固定当前实际 \(K=\mathbb Q(\sqrt2)\) 源、真实假设 \(g=g_+\in K\)、完整 \((1,7bB_{+,g},7bE\delta B_{+,g})\)，不换坐标、行或列池。本轮不证明全正处合法图的排除，也没有新的数值定理。新证书是：第250轮导数无界的 entire \(Q_+\) 双覆盖族，**全部参数的同对象 BC 盈余都小于6**；因此该族中任何可能实际合法的图仍达不到必要8。完整源的所有合法图是否满足同一上界，仍须更强的 period/fiber 证书。

## 1. 全部实际图的准确接口

令 \(\mathcal A_+\) 是所有 \(\phi:(\mathbb D,0)\to(\mathbb C,0)\)、\(\phi'(0)\ne0\)，使上述实际完整三行拉回 single-valued meromorphic 的图。有限处清 pole 已付；不是只让某个代数 double cover 拉回。记
\[
\lambda_\phi=\log|\phi'(0)|,\qquad
J_\phi=\iint_{\mathbb T^2}\log|\phi(z)-\phi(w)|\,d\mu(z)d\mu(w).
\]
对一般 open-disc 图，采用径向极限；若 \(J=+\infty\)，它不能支付严格正盈余。由第250轮同负图的整数背景及全负叶界，当前 safe array 的 strict 入口要求
\[
\delta_\phi:=3\lambda_\phi-J_\phi>32/3-\lambda_->8,\qquad
\lambda_\phi>4.
\tag{E1}
\]
\(\tau=16/9\) 与两嵌入平均均保持，数域 rank仍3。没有把这些 safe 必要条件扩成其它整型或 all-place 判据的必要下界。

置
\[
F_\phi(z,w)=\frac{\phi(z)-\phi(w)}
{\phi'(0)(z-w)},\qquad F_\phi(0,0)=1.
\]
对 \(0<r<1\) 两次 Jensen 及
\(\iint\log|z-w|=0\) 给
\[
\mathcal O_{\phi,r}:=\iint\log|F_\phi(rz,rw)|\ge0,\qquad
J_{\phi(r\cdot)}=\lambda_\phi+\log r+\mathcal O_{\phi,r}.
\]
\(\log|F_\phi|\) 是 plurisubharmonic，故这些径向均值单调，极限得到
\[
\boxed{J_\phi=\lambda_\phi+\mathcal O_\phi,\quad
\mathcal O_\phi\ge0,\quad \delta_\phi=2\lambda_\phi-\mathcal O_\phi.}
\tag{E2}
\]
因此真正覆盖 \(\mathcal A_+\) 的关闭证书须证明
\[
\boxed{\mathcal O_\phi\ge2\lambda_\phi-8
\quad\text{对每一实际合法 }\phi\text{，在 }\lambda_\phi>4\text{ 时}.}
\tag{E3}
\]
正向准入则必须给一个 actual 共同图使反向严格号成立，并支付与负图组合的完整 (E1)。普通补支的点集或裸导数并不决定 \(\mathcal O_\phi\)：它是整个 boundary Haar fiber 分布的同对象量。

## 2. primary Nazarov 的方向不能代替 (E3)

本轮实际 FULL 读取既存 current 作者 PDF物理123–130页完整 TXT，包括完整 Theorem8.0.1 statement及 §8.1 energy principle、Proposition8.1.13 和证明。所用结论是
\[
J_\phi\le \iint\log\max(|\phi(z)|,|\phi(w)|)
=\int_0^1 2t\,(\log|\phi|)^*(t)\,dt.
\tag{E4}
\]
这是 \(J\) 的**上界**，可在一个已认证合法图上帮助证明正盈余，但不能直接证明 \(\delta=3\lambda-J\) 的 upper；把 rearrangement 大当作实际失败证书，方向错误。本文不使用该命题关于 equality 的额外刻画，也不领取 §8.2完整 proof、未知 map 的数值积分或任意矩阵费用优化。

本轮没有付 actual 正处覆盖的全部填叶/周期稳定子分类。即使另知 \(Q_+\circ\phi\) 有全纯 square root，也不能据此把 \(\mathcal A_+\) 换成某个猜测参数族。

## 3. 250双覆盖族的完整差值分解

令
\[
\alpha=(7-4\sqrt2)/2\in(0,1),\quad
\beta=\sqrt{1-\alpha^2},\quad x=\operatorname{arsinh}(\alpha/\beta).
\]
故 \(\beta\sinh x=\alpha,\ \beta\cosh x=1\)、
\(Q_+(t)=(t-\alpha)^2+\beta^2\)。250的 entire cosh 图恰可改写为
\[
\phi_M(z)=\alpha-\beta\sinh(x+Mz),\qquad M>0,
\quad \phi_M(0)=0,\quad \phi_M'(0)=-M.
\tag{E5}
\]
它保留全部 \(Q_+\) double-cover 条件，导数 \(M\) 无界，但从未被认证为 actual \(B_{+,g}\) 的合法图。其差值是完整身份
\[
\phi_M(z)-\phi_M(w)=
-2\beta\sinh\!\left(\frac M2(z-w)\right)
\cosh\!\left(x+\frac M2(z+w)\right).
\tag{E6}
\]
写 \(z=e^{i(u+v)},w=e^{i(u-v)}\)。这个 degree2 torus homomorphism保持 product Haar measure；\(z-w=2ie^{iu}\sin v,\ z+w=2e^{iu}\cos v\)。因此
\[
J_M=\log(2\beta)+
\mathbb E_v Q(M|\sin v|)+\mathbb E_v P_x(M|\cos v|),
\tag{E7}
\]
其中
\[
Q(R)=\mathbb E_u\log|\sinh(Re^{iu})|,
\quad P_x(R)=\mathbb E_u\log|\cosh(x+Re^{iu})|.
\]
这是实际 BC double integral，不是比较两个 radius lower bounds。零点的 logarithmic singularities可积；下列 Jensen 身份亦直接确认 (E7) 有限。

## 4. 全 \(M\) 的线性 fiber penalty 与严格盈余 upper

\(\sinh z\) 的非零零点恰为 \(\pm i\pi k\)、\(k\ge1\)，皆 simple；除去原点后 Jensen 精确给
\[
Q(R)=\log R+
2\sum_{k\ge1}\log^+\frac{R}{\pi k},\qquad R>0.
\]
只取 \(k\le R/(2\pi)\)，每项至少 \(\log2\)，得到全 \(R\) 不等式
\[
Q(R)\ge\log R+2\log2\left\lfloor\frac{R}{2\pi}\right\rfloor.
\tag{E8}
\]
同时 \(\cosh x\ne0\)，对整个圆盘的 subharmonic 均值给
\(P_x(R)\ge\log\cosh x=-\log\beta\)。用
\[
\mathbb E|\sin v|=2/\pi,\quad
\mathbb E\log|\sin v|=-\log2,\quad \lfloor u\rfloor\ge u-1,
\]
其中 log 均值可自含核：sin/cos 的均值相同，而 \(\sin2v=2\sin v\cos v\) 给 \(I=\log2+2I\)。联 (E7)–(E8) 得完整 all-parameter 下界
\[
\boxed{J_M\ge\log M-2\log2+\frac{2\log2}{\pi^2}M.}
\tag{E9}
\]
故
\[
\delta_M\le 2\log M+2\log2-\frac{2\log2}{\pi^2}M
\le 2\log\frac{2\pi^2}{\log2}-2<6.
\tag{E10}
\]
中间 supremum 由一阶导数精确取得于 \(M=\pi^2/\log2\)，没有参数搜索或数值程序。最后严格号也纯纸证：\(\log2>1/2,\pi^2<10\)，所以 \(2\pi^2/\log2<40\)；\(e>65/24>27/10\) 给 \(e^4>51>40\)。若需独立支付 \(\pi^2<10\)，正积分
\[
0<\int_0^1\frac{u^4(1-u)^4}{1+u^2}\,du
=22/7-\pi
\]
给 \(\pi<22/7\)、\((22/7)^2<10\)。

于是，即使将来某个 \(\phi_M\) 被认证属于 \(\mathcal A_+\)，它仍严格达不到必要 \(\delta_+>8\)。裸导数 \(M\to\infty\) 没有预算收益：同对象 fiber penalty至少线性增长。

## 5. 为什么该证明不自动覆盖 actual 正源

若同轮作者完整证明 \(Q_+\) 两根的**全部 transported 到达叶**皆坏，则任何 actual 正图都先得到下面的部分代数提升；这承认了新正处结构接口，但仍不等于全正处 period/energy 分类。本稿冻结时不以未亲读的同伴最终稿代替证明输入。所有满足 \(\phi(0)=0\)、\(y^2=Q_+(\phi),y(0)=1\) 的图确可完整参数化为
\[
w=\frac{\phi-\alpha+y}{\beta}\in\mathcal O(\mathbb D)^\times,\quad
w(0)=e^{-x},\quad
h=-\log(w/e^{-x}),\quad h(0)=0,
\]
\[
\boxed{\phi=\alpha-\beta\sinh(x+h),\qquad
\phi'(0)=-h'(0).}
\tag{E11}
\]
非零性由 \((\phi-\alpha+y)(y-\phi+\alpha)=\beta^2\)，单连通性支付 logarithm。线性 \(h=Mz\) 只是一族；任意 holomorphic \(h\) 的 boundary Haar pushforward不保留 §3 的 rotation/separation公式。不能把 \(h'(0)\) 代入 (E9) 并冒称对所有 \(h\) 成立。

不过剩余全 \(h\) energy 关可精确写成三个非负项。令
\[
U_h=(h(z)-h(w))/2,\quad V_h=(h(z)+h(w))/2,\quad
\Psi_h=\frac{h(z)-h(w)}{h'(0)(z-w)}.
\]
因为 \(\phi'(0)=-h'(0)\)、\(\beta\cosh x=1\)，完整 difference identity给
\[
F_\phi(z,w)=
\Psi_h(z,w)\frac{\sinh U_h}{U_h}
\frac{\cosh(x+V_h)}{\cosh x}.
\]
三个因子在双盘全纯且原点值1（\(U=0\) 取可去值），各自径向log均值非负。故
\[
\boxed{\mathcal O_\phi=\mathcal O_h+\mathcal S_h+\mathcal C_h,\quad
\mathcal O_h,\mathcal S_h,\mathcal C_h\ge0.}
\tag{E13}
\]
\(\mathcal S_h\) 记录 \(h(z)-h(w)=2\pi ik,\ k\ne0\) 的fiber，\(\mathcal C_h\) 记录 \(h(z)+h(w)=-2x+i\pi(2k+1)\)，\(\mathcal O_h\) 是 \(h\) 本身的collision overflow。全实际类所缺的具体下界是
\(\mathcal O_h+\mathcal S_h+\mathcal C_h\ge2\log|h'(0)|-8\)。
Jensen目前只给各项非负，尚未把它们联系到全部实际 \(h\) 的 derivative；这就是不可跳过的同对象能量接口。

更重要的是，实际源还有其它 \(E\)-根、cusp0 的 transported 叶和全部 affine period 通道；(E11) 不支付它们。只知道某个 subgroup 稳定 source 不等于知道全部 actual 稳定子，也不等于给了所有合法图的 energy upper。没有从普通填点条件 \(q=0,M=0\) 免费取得全-cover reduction。

正处 quadratic 背景也不是第250轮的免费整数行。置 \(a=7-4\sqrt2\)，它在唯一2-adic place为unit，规范 \(v_2(2)=1\)。\(y_0=1,v_2(y_0)=0\)。对 \(n\ge1\)，
\[
y_n=[t^n]\sqrt{1-at+t^2}
=\sum_{k=\lceil n/2\rceil}^n
\binom{1/2}{k}\binom{k}{n-k}(-a)^{2k-n}.
\]
\(v_2\binom{1/2}{k}=-2k+s_2(k)\)。令 \(r=n-k>0\)，binary digit subadditivity给其它项相对 \(k=n\) 的估值差至少
\(2r+s_2(k)-s_2(n)\ge2r-s_2(r)\ge1\)。因此唯一最深项不能抵消：
\[
\boxed{v_2(y_n)=-2n+s_2(n).}
\tag{E12}
\]
深度 \(2n-s_2(n)=n+v_2(n!)\) 严格递增，因此对每个 \(N\ge1\)，完整 \(0,\ldots,N\) prefix在此place所需最小规范清分母深度恰为 \(2N-s_2(N)=2N-O(\log N)\)。不能用fixed scalar变成整数背景或直接领取正 \(J_+\ge2\lambda_+\)。这只记录完整背景的实际finite费用障碍，不把该深度直接当 \(\tau\)，也不推出所有联合模型的最优费用。

一个真实但无收益的子类是 native \(q\)-chart：若 \(\phi=t(q(z))\)、\(q:\mathbb D\to\mathbb D\)、\(q(0)=0\)，native 完整源合法，且 \(t'(0)=1\) 与 Schwarz 给 \(c_\phi\le1\)。于是 (E2) 给 \(\delta_\phi\le0\)。并非每个 actual 合法图都被证明有这个 \(q\)-lift；特别不能继承245失败源的 lifting theorem。

## 6. 本关结论与停止条件

已付实际统一接口 (E2)–(E3)、Nazarov的正确方向、部分cover的完整 holomorphic 参数化和全 \(h\) 的三项fiber分解、quadratic 背景的全 \(n\) dyadic深度，以及所有 \(M>0\) 的同对象 strict 阻碍 (E10)。未付的是 \(\mathcal A_+\) 全覆盖的 period-stabilizer→fiber-overflow 下界，或一个完整合法图的反向 strict 证书。本文不把族的 upper-profile 失败写成 actual Gauss lower/no-go，不关闭整个双多叶方法。

本轮没有支付当前唯一准入目标：尚无 actual \(\delta_+>8\) 图，亦无覆盖全部 actual 图的 \(\delta_+\le8\) 证明。因而不能据此再开同源 prime、map、参数、Bloch常数或局部叶续轮；252正式复盘应按既定规则结束本源默认投入，除非其它同轮作者真的付清这个唯一核心证书。本文的新族能量 lemma是复盘资产，不是新的延长许可。

本轮数学/CAS/Lean/interval/prime/map/parameter/word程序0，新 GET0、外 Git mutation0、旧producer及旧文件写0。primary actual读域、冻结输入与保存后 FULL 作者复读身份另登记；没有上游全文认证或新数值无理性/LI结论。
