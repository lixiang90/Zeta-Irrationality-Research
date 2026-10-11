# 第248轮：增长整数矩阵与相对周期的实际首关

2026-10-10，C独立纸核。当前证据不足以恢复K5或χ−7标量源的默认费用优化，也不足以把M₀,₁₀升为已投影数值源。新增一个同对象外国窗口Schur判据，精确说明怎样把旧upper变成真实饱和或宏观内容收益；未证明该余块所需的全尺度性质。数学执行0；主目标仍是新的数值定理。

## 1. 四接口留在同一对象

固定 D_m(t)=∏_{j=1}^m(t+j)，R_n=D_n⁴/D_{5n}，h=3n，S_n=(5n)!/(n!)⁴，F_n=∏_{i<h}(i!)²。

| 实际对象与数值出口 | 完整周期投影 | 关系点无限非零 | primitive与实处首关 |
|---|---|---|---|
| K5，X=3ζ(3)+ζ(5)，Q_n=det[U_T(t^{i+j}R_n)] | U=(3/2)B∘∂(t·)+(1/24)B∘∂³(t·)，整个商部/简单极点只有1、X，已付 | 241每个有理q的无界非零作为已付输入；本轮不重审241 | 同一Q̃=S_n^hQ/F_n全系数upper1511/60；独立完整−6和strict净差额未付 |
| 非对称χ−7，Y=L(2,χ−7)，Qχ,n=det[Vχ,T(t^{i+j}R_n)] | 全字符平移Bernoulli空间只有1、Y，已付 | 未付；μχ>0不能去掉R_n(iy)复相位 | 同一absolute-Heine leading转移已付；fixed7、外国区及其余全prime净费未付；−6仍依原输入 |
| 对称χ−7，R_n(t)R_n(−t) | ±全部简单极点与商部仍只有1、Y，已付 | 正Gram支付每个n,h非零 | 外场变为|R_n|²，不能借非对称费用或−6 |
| 原M₀,₁₀，I_n=∫F^nω，拟投影后隔离ζ(7) | 十一通道已付，实际六通道/目标隔离未付 | 原正积分不支付投影后det非零 | 完整目标分母及投影后实处模式未付 |

1009/40−1/24=1511/60是所选完整费用证书upper；242的36/5只约束所选upper函数积分。243首层kernel、s=1目标系数秩都不是实际费用lower。χ−7的175/4也只是外国窗口upper。这些支持资源止损，不是数学no-go。

Tang pinned Criterion给整数多项式在非零有理点的|P(q)|≥den(q)^(−deg P)，Assembly明确需要算术、实处、prime-edge三个节点。FstarDefs给完整−6命题和有限点输入的精确定义，不等于本轮已认证其证明。README亦引用Fauzan的ζ(5)结果；本轮不重认证该原证明/Lean，更不从单值无理推出X无理或全球新颖。

## 2. 新首证书：外国窗口的实际余矩阵

**G1（完整Gauss首层饱和判据）。** n≥2，取
\[
35n/2<p<35n,\quad J=\lceil p/7\rceil,\quad
k=5n-J+1,\quad r=h-k=J-2n-1.
\]
此时p>5n、p≠7、0<k<h。令
\[
\Psi=D_{5n}/D_{J-1},\qquad
K_{n,J}=R_n\Psi^2=\frac{D_n^4\Psi}{D_{J-1}},
\]
\[
C_{n,J,p}(T)=
[V_{\chi,T}(t^{a+b}K_{n,J})]_{0\le a,b<r}\in M_r(\mathbb Z_p[T]).
\tag{G1}
\]
对同一Q̃χ,n，
\[
g_p(\widetilde Q_{\chi,n})=-2k
\iff\det C_{n,J,p}(T)\not\equiv0\pmod p.
\tag{G2}
\]
这不以泛型多项式非零代替某固定有理q的非零。

证明：244完整分解是
\[
M=W-\chi(p)p^{-2}\sum_{j=J}^{5n}j\lambda_jv_jv_j^t,
\quad W\in M_h(\mathbb Z_p[T]),\
v_j=((-j)^i)_{i<h},\
\lambda_j=\operatorname{Res}_{-j}R_n.
\]
取degree<k的Lagrange基ℓ_j，在−J,…,−5n上为单位值基，再取Ψt^a，0≤a<r。节点差均p单位，Ψ首一，故这是degree<h的完整Z_p单位基。合同变换给
\[
\begin{pmatrix}p^{-2}D+A&B\\B^t&C\end{pmatrix},
\quad D=-\chi(p)\operatorname{diag}(j\lambda_j)\in GL_k(\mathbb Z_p),
\quad A,B,C\text{整}.
\]
原子在交叉/底块严格为零；C恰为(G1)，不是任取ambient minor。剩余极点j<J有7j<p，故头p整；商部degree仍≤5n−1<p−1，Bernoulli和fixed7也p整。

在Q_p(T)的Gauss DVR中，顶块逆为p²D⁻¹+O(p⁴)，det估值−2k；实际Schur
\[
Z=C-B^t(p^{-2}D+A)^{-1}B\in M_r(\mathcal O_G),
\qquad\overline Z=\overline C.
\]
基变换与S_n^h/F_n在此均p单位。若Q≠0，精确地
\[
g_p(\widetilde Q_{\chi,n})=-2k+\ell_{n,p},\qquad
\ell_{n,p}=g_p(\det Z)\ge0.
\tag{G3}
\]
剩余域为F_p(T)，所以ℓ=0当且仅当det C模p非零。证明完毕。

完整目标系数亦明示为
\[
[T]C_{ab}=-[t^{-2}]t^{a+b}K_{n,J}
=\sum_{n<j<J}j\lambda_j\Psi(-j)^2(-j)^{a+b}.
\tag{G4}
\]
剩余节点/权重均p单位，但签名不正；Vandermonde满秩不证明方形Hankel minor满秩，更不证明完整仿射det非零。

若(G2)在宏观子窗成立，旧−2k在该处成为真实饱和；其它窗口仍可能有正内容，不能单窗推出全源no-go。要节省leading费用，须支付实际ℓ≥nη(p/n)+o(n)，或正比例rank defect/更深内容，连同整个外国区、fixed7及其余窗口。单有det C≡0只给ℓ≥1，其证书收益总计O(n)，不改变n²率；宏观收益才是∫η(x)dx。

本窗口S_n为p单位，实际节点各出现一次。242强head依赖的S_n整数矩p^s整除在这里没有正s，不能免费移植W≥p。本轮只支付降维和精确判据，没有解det C的全尺度问题，也不据此启动下一层优化。在本轮所核244原稿中，此余det没有被支付；不宣称已穷尽全部历史文献。

## 3. 对称正Gram的能量方向

**G2（同测度比较）。** 设
\[
G_0=[\int y^{i+j}\mu_\chi(y)dy],\quad
G_{\rm sym}=[\int y^{i+j}|R_n(iy)|^2\mu_\chi(y)dy].
\]
二者正定，且非对称矩的相位不改变绝对det：
\[
|Q_{\chi,n}(Y)|^2\le\det G_0\,\det G_{\rm sym}.
\tag{G5}
\]
证明：在L²(μχ)用两组向量y^i、overline{R_n(iy)}y^i。完整块Gram正半定，Schur补给Gsym−C*G0⁻¹C≥0，取det即得；指数尾支付全部矩。

因此G5只给det Gsym≥实际|Qχ,n(Y)|²/det G0；已知|Qχ,n(Y)|的upper本身不能代入右侧当作lower。这个比较不提供可用的对称源小upper或−6证书。对称源真正支付非零，下一证书却须独立重算外场归一化和净费用；再证明正性不改变预算。

## 4. 原相对周期的更早门槛

实际FULL复读240原F、ω的cubical式与Euler排除，并读Brown2012所用coaction完整页和Brown2014 PDF34–35。后者本配置的低权消失仍标experimental；Theorem11.2要求两个完整cellular boundary divisors，不能凭配置名称用于原n≥7非cellular奇异除子。

十一通道中首式仍是
\[
D_3I_n^{\mathfrak m}=\zeta_3^\ell\otimes
(c_3+c_{23}\zeta_2^{\mathfrak m}
+2c_{33}\zeta_3^{\mathfrak m}
+c_{223}(\zeta_2^{\mathfrak m})^2),
\]
\[
D_3I_n^{\mathfrak m}\in
\mathbb Q\zeta_3^\ell\otimes\zeta_2^{\mathfrak m}
\iff c_3=c_{33}=c_{223}=0.
\tag{G6}
\]
(G6)全n成功后尚有两个Tate禁通道；六通道也不自动给纯ζ7。固定对角Euler失败是严格限定的结构排除，不反驳(G6)，也不排除非对角relative telescope。

可接受的首证书仍是一份作用于原相对类的可终止cut/telescope：明确boundary motivic lift，给递推及全部非负整数例外，用motivic初段归纳禁止坐标。一般GM容器、数值初段或另一η的parity均不符合。所读记录没有这个证书，也没有已匹配而廉价的新relative projector；保持条件后备，不为抽象container再开窗口。

## 5. 下一窗口与判停

这几类不凭当前资产回主线。K5须有新的全宏观Gauss机制和同对象实处完整认证，1/24局部省不足。χ−7若安排一轮纸面准入，唯一具体问题是(G1)完整仿射det的全尺度饱和或线性内容；没有宏观预算希望就停，单层/rank结果不自动续窗。M₀,₁₀只在原relative投影首证书出现后恢复。

CDT所读§15.1.10明确近似式生成函数不自动为G函数；§15.2.2有效局部自由仍是Question。不能用形式ΣQ_n(T)z^n把n²费用改成有限lcm-slope，也不能把计划中的adelic一般化当已付多place收益。同一标量Gauss内容已计所有p；新增place须有额外实际关系点估值或完整G-germ/图，不能重复计已有整内容。

未得新数值定理，未认证全球新颖性。精确实际读域见新dual_reading_scope.md；数学/CAS/扫描/Lean0，外仓库写0，新增GET0。

