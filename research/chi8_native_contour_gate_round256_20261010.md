# 第256轮：native Q 全sheet实际生成芽与contour首关

日期：2026-10-10。对象严格沿用第255轮冻结的 `a=1/√2`、参数在 `+1` 的单圈 `T`、`3+T`、`N(i,j)=a^i(3+T)M_a(i,j)`，以及第255轮整数单项式接触prototype。本文只支付实际解析载体；没有新数值无理性/线性无关性定理，不预领整数模型、energy、Frobenius或实际非零。

## 1. 实际读取与结论边界

本轮先FULL读取冻结255的Root架构稿、A Catalan比较稿、B holonomy稿、进展报告及manifest，逐一定位同一对象。其NEW逐字副本与哈希见 `literature/native_chi8_sources_round256_20261010/contour_reading_scope.md`。下文解析证明自含，不调用Catalan论文的实位正性/energy/奇素数结论，也未运行数学程序、finite-head扫描、CAS或参数/prime/map搜索。

本次肯定结论是：存在一个与全部指标、全部n无关的固定双变量芽域，以及在该芽域上同一次实际合法参数继续。其返回值逐项为完整N数组；普通Z是另一个明确的实际伴随积分。所有F由这同一对实际芽的有限线性取系数得到。二者的支持不同，不能混成同一条正测度曲线。全前缀整数费用首关由本轮另一份算术工作判定；本文不把解析成功等同于整个256首关通过。

## 2. 原始全数组与Stieltjes消分母

令 `dμ(t)=|t|dt/√(1−t²)`，`−1<t<1`，初始平方根取正，且

\[
m_i=\int_{-1}^{1}t^i\,d\mu(t),\qquad
m_{2\ell}=\frac{2}{(2\ell+1)c_\ell},\quad m_{2\ell+1}=0,
\quad c_\ell=4^{-\ell}\binom{2\ell}{\ell}.
\]

因此 `m₀=2`，`m₋₁=0`，以及 `(d+1)m_d=d m_{d−2}` (`d≥2`)。对 `|u|<1` 定义实际积分

\[
M_u(i,j)=\int_{-1}^{1}\int_0^1
 \frac{t^i s^j}{1-uts}\,ds\,d\mu(t)
=\sum_{k\ge0}\frac{u^k m_{i+k}}{j+k+1}.
\]

Stieltjes函数与完整芽是

\[
S(r)=\int\frac{d\mu(t)}{1-rt}
=\frac{2\arcsin r}{r\sqrt{1-r^2}},\quad S(0)=2,
\]
\[
\mathcal G_u(z,w)=\int\!\int
\frac{d\mu(t)ds}{(1-zt)(1-ws)(1-uts)},
\qquad
H_u(z,w):=\mathcal G_u(uz,w)=\sum_{i,j\ge0}u^i M_u(i,j)z^iw^j.
\]

原始域 `|u|,|z|,|w|<1` 的紧子集上几何级数绝对一致可积；这是实际全数组，而非仅形式递推。先积掉t，有精确除差公式

\[
H_u(z,w)=\int_0^1
 \frac{zS(uz)-sS(us)}{(z-s)(1-ws)}\,ds.
\tag{2.1}
\]

其中 `z=s` 为除差的可去点。置 `r=us`，再置 `r=sinθ`，初始端点 `φ=arcsin u`，得到本轮关键共同载体

\[
\boxed{\quad
\mathscr H(u,\phi;z,w)=
\int_{0\to\phi}
\frac{uzS(uz)\cos\theta-2\theta}
 {(u-w\sin\theta)(uz-\sin\theta)}\,d\theta .\quad}
\tag{2.2}
\]

初始 `0<u<1` 时，(2.2)逐步换元于(2.1)，所以 `H_u=𝓗(u,arcsin u)`。一般初始复邻域由解析恒等原理给出同一等式。这里 `S(uz)` 始终是小r主芽；将端点φ继续而不把它重新选成主arcsin，正是实际参数sheet。

## 3. 固定小芽域、显式单圈及全部polar-divisor

取固定开放矩形与芽域

\[
\Omega=\{-1/8<\Re\theta<7\pi/8,\ |\Im\theta|<1/4\},
\qquad |z|,|w|<1/32,
\]
并在参数回路的邻域使用 `2/3<|u|<9/8`。这些常数与i、j、n无关。

写 `r₀=1/8`。端点φ从 `π/4` 沿实轴走到 `π/2−r₀`，然后走

\[
\phi=\pi/2+r_0e^{i\vartheta},\quad -\pi\le\vartheta\le0,
\]
最后从 `π/2+r₀` 沿实轴到 `3π/4`。参数回路为 `u=sinφ`。两条实轴段在u平面互相反向，中段满足

\[
u-1=\cos q-1=-2\sin^2(q/2),\quad q=r_0e^{i\vartheta}.
\]

`sin(q/2)/(q/2)` 在 `|q|≤r₀` 无零，故中段对 `u=1` 的绕数为+1；又 `|u−1|≤cosh(r₀)−1<1/32`，对0和−1绕数为0。这是255已指定的正向单圈T的显式代表，不是新sheet word。全端点路径位于Ω的紧子集，初末参数都等于a，初末φ分别为 `π/4,3π/4`。

以下实际核清(2.2)在整个共同域的所有潜在极点。

1. `|uz|<9/256<1/16`，故小r的 `S(uz)` 无分支点。令 `α=arcsin(uz)` 为小芽，则 `|α|≤|uz|/√(1−|uz|²)<1/8`，`cosα≠0`。
2. `sinθ=uz` 的所有解为 `α+2kπ` 或 `π−α+2kπ`。Ω内唯一可能解为α；第二类均在Ω外。分子是 `2α cosθ/cosα−2θ`，在θ=α精确为0。分母 `uz−sinθ` 在该点为单零，故商共同解析可去，而不只是逐系数消除。其延拓值为

\[
\frac{2(1+\alpha\tan\alpha)}
 {\cos\alpha\,(u-wuz)}.
\]

在α=0时该值也正常，为 `2/u`。局部解析整除给出与u,z,w共同的解析函数。
3. Ω上 `|sinθ|≤cosh(1/4)<4/3`，所以 `|w sinθ|<1/24`，而 `|u|>2/3`。因此 `u−w sinθ` 的模严格大于5/8。它不能提供隐藏极点。
4. 换元已经约掉原先的 `√(1−r²)`：积分核没有 `1/cosθ` 因子。跨过θ=π/2完全合法。对数起点θ=0在z=0时也是上述同一可去点。

Ω是凸、单连通域。因此(2.2)可取从0到φ的直线段；也可用Ω中任意同端点路径，二者相同。被积核在Ω及整个芽域共同解析，故积分是共同解析函数。参数回路避开实际分支点±1和0，端点φ有合法解析提升；沿此提升(2.2)是原始 `H_u` 的解析继续。它避免了在原始实区间积分中直接穿过 `1−uts=0` 的非法操作。

对芽域任意固定紧子盘，例如 `|z|,|w|≤1/64`，全部端点/积分路径取自Ω的固定紧子集；解析延拓后的核一致有界、路径长度一致有界。故求导、Cauchy取系数与实际继续可交换，对全i,j同时成立，无需逐指标选择回路。

返回a后的两个实际芽因此是

\[
H_{old}(z,w)=\mathscr H(a,\pi/4;z,w),\qquad
H_{new}(z,w)=\mathscr H(a,3\pi/4;z,w),
\]
\[
\boxed{\mathcal N(z,w)=3H_{old}(z,w)+H_{new}(z,w)
=\sum_{i,j\ge0}N(i,j)z^iw^j.}
\tag{3.1}
\]

这是一个共同实际双变量芽。沿回路使用u^i归一化不改变255固定的a^i方向：u^i单值，初末都为a^i。因此(3.1)的每个系数精确为 `a^i(3+T)M_a(i,j)`。`3+T` 的有理单值项乘4，不能当成幂等投影。

## 4. 起点period与全finite heads的实际支付

令 `Y=L(2,χ₋₈)`，其中奇数上的χ依次为 `1,1,−1,−1`（模8），偶数为0，`E=1+√2`。由(2.2)在z=w=0，

\[
H_{old}(0,0)=\frac2a\int_0^{\pi/4}\frac\theta{\sin\theta}\,d\theta
=4Y-\frac\pi{\sqrt2}\log E.
\]

此恒等式可自含核：分部积分得到 `I(α)=α log tan(α/2)−∫₀^α log tan(θ/2)dθ`；对 `0<θ≤π/4`，Abel取极限的傅里叶式为 `log tan(θ/2)=−2Σ_{k odd} cos(kθ)/k`。积分后绝对收敛的正弦级数给 `−2Σ_{k odd}sin(kπ/4)/k²=−√2Y`，且 `tan(π/8)=E⁻¹`。Abel极限可在积分内通过：`|1−ρe^{iθ}|≥cθ` (`ρ≥1/2`)，对数由 `C+|logθ|` 控制，分母 `1+ρe^{iθ}` 在该小区间离0有界。

将新积分的 `π/4..3π/4` 段用θ与π−θ配对，得到

\[
H_{new}(0,0)-H_{old}(0,0)
=\frac{2\pi}{a}\log E.
\]

故 `N(0,0)=16Y`。直接初始积分亦给 `M_u(0,1)=φ²/u²`；同一合法继续给新φ，所以 `N(0,1)=3π²/2`。Stieltjes值 `S_old(a)=π`、`S_new(a)=−3π`，因此bar S₀=0。它们都是同一实际继续的值，并非自由选择的period starts。

设 `μ_i=a^i m_i∈Q`，`U_i=a^i(3+T)S_i(a)`，其中 `S_i(u)=Σ u^k m_{i+k}`。在原始实际域中，积核代数恒等式给

\[
S_i(u)=u^{-i}\Big(S(u)-\sum_{k<i}u^km_k\Big),
\quad
M_u(i,j)-uM_u(i+1,j+1)=m_i/(j+1).
\]

逐式沿上述共同芽继续，返回a并作用3+T，便得

\[
U_i=-4\sum_{k<i}\mu_k,\quad U_0=0,
\qquad N(i,j)-N(i+1,j+1)=\frac{4\mu_i}{j+1}.
\tag{4.1}
\]

两个边界的完整递推为

\[
N(1,0)=8,\qquad
dN(d,0)=(d-1)a^2N(d-2,0)+a^2U_{d-2}-U_d\quad(d\ge2),
\tag{4.2}
\]
\[
(d-1)a^2N(0,d)=(d-2)N(0,d-2)+\frac8{d-1}
\quad(d\ge2).
\tag{4.3}
\]

为避免仅引用形式递推，给出其初始实际域证明。(4.2)未bar版本由 `(d+k+1)m_{d+k}=(d+k)m_{d+k−2}` 在绝对收敛的原始级数逐项求和得到。`uM_u(1,0)=(u²−1)S(u)+2`，因两边在0为0，且导数均为 `(S(u)−2)/u`。对(4.3)，令 `I_d(u)=∫₀^u v^dS(v)dv=u^{d+1}M_u(0,d)`；

\[
\frac{d}{dv}\big[v^{d-1}(v^2-1)S(v)\big]
=[(d-1)v^d-(d-2)v^{d-2}]S(v)-2v^{d-2}.
\]

积分从0到u后除以u^{d−1}即得初始式，再沿共同实际继续作用3+T，得到(4.2)–(4.3)。所有常数项在bar后乘4。

由(4.1)可写全finite heads，而无需任何截断假设：

\[
N(i,j)=N(i-j,0)-4\sum_{h=1}^j\frac{\mu_{i-j+h-1}}h
\quad(i\ge j),
\tag{4.4}
\]
\[
N(i,j)=N(0,j-i)-4\sum_{h=j-i+1}^j
\frac{\mu_{h-(j-i)-1}}h
\quad(i<j).
\tag{4.5}
\]

结合边界starts及递推，确切得到

\[
\boxed{N(i,j)=R_{ij}
+16Y\,a^{i-j}c_{(i-j)/2}
+\frac32\pi^2\,a^{i+1-j}c_{(j-i-1)/2},\quad R_{ij}\in\mathbb Q.}
\tag{4.6}
\]

约定c的下标非非负整数时该项为0。非零period系数的a幂均为偶数，所以系数为Q；R由(4.1)–(4.5)完整定义。有理性及完整有限项已支付，但本文没有据此宣称共同分母是exp(O(H))；一般递推清分母可能过贵，必须另证。

## 5. 普通Z的支持与actual F全数组

初始 `x=at` 将native旧积分的支持变成 `[-a,a]`，测度为 `2|x|dx/√(1−2x²)`。新sheet的(2.2)继续跨过θ=π/2，不能解释为这区间上的同一正测度。另一方面，接触消ζ(2)伴随明确是

\[
Z(i,j)=\int_{[0,1]^2}\frac{x^is^j}{1-xs}\,dxds,
\quad
\mathcal Z(z,w)=\int_{[0,1]^2}
\frac{dxds}{(1-zx)(1-ws)(1-xs)}.
\tag{5.1}
\]

`1/(1−xs)` 在角点(1,1)可积；其总积分ζ(2)有限。因此同一 `|z|,|w|<1/32` 的紧子盘可用 `(1−δ)⁻²/(1−xs)` 支配。全双变量展开、求导及取系数均合法，且

\[
Z(i,i)=\zeta(2)-H_i^{(2)},\qquad
Z(i,j)=\frac{H_i-H_j}{i-j}\quad(i\ne j).
\tag{5.2}
\]

这由 `Σ_{k≥0}[(k+i+1)(k+j+1)]⁻¹` 的实收敛求和/望远镜直接得到；全部finite heads明示。Z实际支持包含 `(a,1]`，本文保留(5.1)为独立伴随分量，不冒称可沿原conic正曲线吸收。

对任意有限多项式P,D，定义 `𝓛_P h=Σ_i p_i[z^i]h`。实际生成行是

\[
\mathcal F_{P,D}(w)=\mathcal L_P\mathcal N(z,w)
-9\mathcal L_D\mathcal Z(z,w)
=\sum_{j\ge0}F_j(P,D)w^j.
\tag{5.3}
\]

这是同一实际N/Z芽对的有限连续线性操作。每个j、每个degree及每个prototype n均用相同contour与相同芽域；不需要先固定j再重新选择sheet。若需要对prototype的r与j同时生成，令 `𝓕_n(v,w)=Σ_{r=0}^{n−1}v^r𝓕_{P_r,D_r}(w)`，得到实际双变量芽，其v只是有限行索引的生成记号，不改变参数、包或投影方向。它在上述同一w域与任意有限v域解析；本文不给其n增长范数或energy保证。

由(4.6)与(5.2)，F的π²系数精确为

\[
\frac32[x^j]\Big(\frac{xP(x)}{\sqrt{1-2x^2}}-D(x)\Big).
\tag{5.4}
\]

所以真实接触 `xP/√(1−2x²)−D=O(x^L)` 对每个 `j<L` 消掉π²，完整F属于 `Q+QY`。没有删掉任何finite head或只留下period层。

冻结prototype仍为 `n≥1,0≤r<n`：

\[
P_r(x)=2^nx^{2r},\qquad
D_r(x)=\sum_{\ell=0}^{n-r-1}
2^{n-\ell}\binom{2\ell}{\ell}x^{2r+1+2\ell}\in\mathbb Z[x].
\]

接触余项为 `O(x^{2n+1})`，因此全部raw `0≤j<2n` 都是实际 `Q+QY` 值。even `j=2s` 的Y系数为 `16·2^n·2^{-(r-s)}c_{r-s}` (`r≥s`；否则0)，三角对角线为 `16·2^n`。此period系数det不是实际关系点det非零证明。

## 6. 与free-start以及剩余首关的准确接口

全数组(4.6)还给自由替换start Y→g的形式差

\[
\mathcal N^{[g]}(z,w)-\mathcal N^{[Y]}(z,w)
=\frac{16(g-Y)}{(1-zw)\sqrt{1-z^2/2}}.
\]

实际contour及第四节傅里叶恒等式选定的是Y；不能由上述差式声称任意g都具有同一几何period、正性或energy下界。

本轮解析首关通过：一条明确单圈、一块固定全芽域、一个共同N双变量contour与一个明确Z伴随，支付了全部数组和finite heads，且未换成局部截断载体。它只回答“这些数组确实是同一实际继续的周期值”。剩余必须是完整前缀的exp(O(H))级整数模型、全部row-scale及之后的实际非零/严格预算证书。若只有通用H!级清分母，256总首关仍应停止；若算术首关成功，也不自动产生新数值定理，更不能套用Catalan正测度energy。
