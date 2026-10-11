# 第257轮：完整实际能量与新内容的同对象净结算

2026-10-10。上一轮256归档已完成，本轮实际解析manifest并核100/100当前pins及main/policy身份；上一goal turn分类progress。原总目标仍active，没有新数值定理。本稿固定a=1/√2、Y=L(2,χ−8)、3+T、全P/D prototype、全部raw j<2n及selected-even determinant，结算256准入的一次净可行性检验。

## 1. 真实进展不能混成数值出口

本轮两项完整新证书都成立。实际单圈差可实折叠，得到全部i,j的

\[
N(i,j)=4N_{old}(i,j)+4\pi\int_a^1\frac{x^{i-j}}{\sqrt{2x^2-1}}dx.
\tag{R1}
\]

原heads和ordinary Z没有删除。令T_n=2^(−n)F_n，则完整actual Y处的三标签实测度表示是

\[
\begin{aligned}
(T_n)_{rs}={}&16\int_0^a\int_0^1
\frac{x^{2r+1}y^{2s}}{\sqrt{1-2x^2}(1-x^2y^2)}dy\,dx\\
&+4\pi\int_a^1\frac{x^{2r-2s}}{\sqrt{2x^2-1}}dx\\
&-9\int_0^1\int_0^1
\frac{x^{2r+1}C_{n-r-1}(x^2)y^{2s}}{1-xy}dy\,dx,
\end{aligned}
\tag{R2}
\]

C_m(u)=Σ_(l=0)^m binom(2l,l)u^l/2^l。这里标签O/J/Z须保留：J的列变量是x^(−2)，Z的行函数带负号和n相关截断。正测度不使此式成为同函数Gram。对全部标签的共同有限测度ν，完整Andreief为detT_n=(1/n!)∫detf·detg dν^n。

另一方面，原native全数组的更强前缀清整证书是

\[
\boxed{\widetilde q_H=2^{3\lfloor H/2\rfloor+1}d_{H+1}^2},
\qquad d_m=\operatorname{lcm}(1,\ldots,m).
\tag{R3}
\]

它同时清R、Y/ζ(2)系数和ordinary Z heads的完整矩形，含所有prime powers。minus完整头的binomial双和、plus even/odd逐层两分母界及全diagonal heads给证明，不借有限n/prime样本。若单独用π²记未乘9的ordinary Z，其δ/6需另付固定3；contact后的9Z及N的π²系数已经覆盖。

## 2. 同一个整数多项式的真实全内容改进

H=2n−1，q_old=2^(4n−1)d_(2n)^3，而\widetilde q=2^(3n−2)d_(2n)^2。固定整数row content κ_n=2^(n(n+1)/2)只用一次。全部整数filters同样有

\[
C_{n,E}^{new}(T)=\frac{\widetilde q^n}{\kappa_n}\Delta_{n,E}(T)\in\mathbb Z[T],
\]
\[
C_{n,E}^{old}(T)=\underbrace{[2^{n+1}d_{2n}]^n}_{M_n}C_{n,E}^{new}(T).
\tag{R4}
\]

所以M_n确实整除旧完整模型的每个coefficient，ALL n、ALL integer filters。它不是最大primitive content，也不是单纯换单位所得新数值定理。它改善的是此前对同一primitive多项式的上界证书。

令Π_n为selected-even同一det的positive-leading primitive多项式，ℓ_n为其leading。由target coefficient (16·2^n)^n，完整安全leading费用为

\[
\log\ell_n\le2n\psi(2n)+\left(\frac72n^2+\frac32n\right)\log2,
\quad\psi(m)=\log d_m.
\tag{R5}
\]

若仅作标准PNT换算，leading upper从6+(9/2)log2降到4+(7/2)log2，二次阶省2+log2。清整scalar本身leading为4+(5/2)log2，不能与ℓ费混用；另一个native行尺度的同乘积κ不能再扣。以上是全模型的真实改善，尚非实际最优费用。

## 3. 完整actual上界与新费用的精确合并

三标签模型的列变量η全在[0,2]。monic Chebyshev列变换给

\[
|\det g|\le n^{n/2}2^{n-1-n(n-1)/2}.
\]

Z行完整截断高度给|f_r|≤2^(n−r)，从而|detf|≤n!2^(n(n+1)/2)。其正负二次指数恰抵消。ν总质量可取

\[
M=16+2\sqrt2\pi\log(1+\sqrt2)+\frac32\pi^2.
\]

于是同一个actual Y处，全部n≥1有

\[
|2^{-n^2}\Delta_n(Y)|\le M^n n^{n/2}2^{2n-1}.
\tag{R6}
\]

这是目标处的实际upper，不是free-start量词。把(R3)的完整整数模型还原，得到

\[
|\Pi_n(Y)|\le\frac{\widetilde q^n}{\kappa_n}
2^{n^2}M^n n^{n/2}2^{2n-1},
\]
\[
\boxed{\log|\Pi_n(Y)|\le
2n\psi(2n)+\left(\frac72n^2-\frac12n-1\right)\log2+
n\log M+\frac n2\log n.}
\tag{R7}
\]

若Π_n(Y)=0，log按−∞理解，未由upper领取非零。无需PNT，(R7)已是exact fee/actual安全估计；沿同一标准ψ(2n)=2n+o(n)标尺，其leading为正的4+(7/2)log2。因此这两份证书的**合并upper不能给无理性矛盾**。正upper不意味着真实Π_n(Y)有正指数或全部方法no-go，可能有更强取消；本轮未控制它。

谱式也完全匹配。Δ_n(Y)=(16·2^n)^n∏_j(Y−λ_j(K_n))，故(R6)给

\[
\prod_j|Y-\lambda_j(K_n)|\le
M^n n^{n/2}2^{-2n-1}.
\tag{R8}
\]

(R5)+(R8)正好回到(R7)，没有遗漏16^n或2^(n²)。这份谱积upper的n²项为0；与新ℓ费仍不构成strict。若Y=u/v有理且Π_n(Y)非零，才有|Π_n(Y)|≥v^(−n)。实际无界非零和负二次limsup仍均未付。

## 4. 普通Vandermonde或逐块非零不能免费补缺口

同一个row basis的exact upper Toeplitz关系为

\[
D_r/2^n=\sum_{k=r}^{n-1}b_{k-r}x^{2k+1},\quad
U_{rk}=b_{k-r},\quad b_l=\binom{2l}{l}/2^l,
\]
\[
T_n=N_n-9U_nZ_n,\qquad \det U_n=1.
\tag{R9}
\]

U_n^(−1)系数来自sqrt(1−2z)，为−2^(−l)binom(2l,l)/(2l−1)（l≥1），只有dyadic分母。这是同对象有理row变换，primitiveΠ_n不变，不提供额外免费费减。

mixed O/Z row vectors在相同t=x²>0分别是v(t)与−√t U_nv(t)。n≥2时最后两行的v与Uv子式为

\[
\det\begin{pmatrix}t^{n-2}&t^{n-2}+t^{n-1}\\t^{n-1}&t^{n-1}\end{pmatrix}
=-t^{2n-2}\ne0.
\tag{R10}
\]

用n−2个O节点合流到0并取标准除阶乘的导数列，得到e_0,…,e_(n−3)，故混合alternant在O/Z两节点相等时仍可非零。这个ALL-n证书只排除未经证明的全node Vandermonde因子和从纯sector借双容量的捷径，不证明真实det不能更小。J-only也有反序Vandermonde固定符号(−1)^(n(n−1)/2)，不能代替整式非零。

增加n时，原旧block还有一个精确障碍：令b_r=b_(n−r)、z_s=Z(2n+1,2s)∈Q，則

\[
(T_{n+1})_{0:n,0:n}=T_n-9bz^t.
\tag{R11}
\]

所以当前actual det不是一个fixed正moment matrix的普通principal-minor链。其rational rank-one修改及完整bordered determinant须一起支付。目标coef16L子块不变不推出下一actual det非零；本稿未领取相邻coprimality或∞nonnull。

## 5. 投入结算与下一结构方向

本轮有实质progress：完整实际实表示、ALL-n actual上界、全prefix分母减层和whole-polynomial内容。它们已经同尺度结算，仍未给所需数值出口。当前default monomial prototype停止投入；保留完整carrier和新算术证书。不得因本轮新content再次自动加prime/Frobenius、参数/maps/sheetwords或换向量窗口。停止是机会成本决定，不是χ−8全方法不可能。

下一258转回统一框架的来源选择：检查一个假设的数值有理关系，是否能在**完整最小函数族**中消掉整个非meromorphic local monodromy，并带来可量化的共同解析域增益。候选须同时交付真实period投影、函数独立性和全prefix费用；只增加germ/jet数量或消掉一个本已允许的meromorphic极点不准入。优先考察真实不同cyclotomic通道的多源机制，但不能从它们单独无理或函数代数独立直接宣称目标数值线性无关。此轮不提前构造新参数或新的Padé实例。

258是一次有界的跨架构准入判断：若不能给明确的关系敏感monodromy和共同域增益，直接否决相应来源选择，而不是继续局部搜索。它保留原数值目标，未将成功改定义为抽象引理。正式clock仍last256，本轮完成后计数1，下一260、最迟264；连续2轮核心停滞提前。没有新数值无理性/线性无关性定理，原goal active。
