# 第224轮：固定三周期jet的真实Fourier核与三频率非退化入口

2026-10-08。只研究222固定R_n和223固定连续三行Δ。新增的是一个不靠未计算n-operator的**精确普通积分接口**：Δ等于显式核K_r在π、3π、5π三个点的连续三行行列式，乘一个已知非零常数。六重卷积在微分前非负；微分后的核正性、三阶Chebyshev性或多模式主渐近尚未证明。**本稿没有证明Δ无限非零，没有新的数值定理。**

## 1. 固定归一化及整个函数

记n为非负偶数，

\[
R_n(t)=\frac{\prod_{j=1}^n[(t-j)(t+n+j)]^3}
{\prod_{k=0}^n(t+k)^6},\quad
F_{n,k}(v)=v^6R_n(-k+v),\quad
S_n(v)=\sum_{k=0}^n(-1)^kF_{n,k}(v).
\]

S_n在|v|<1全纯且为偶函数。令s_(j,n)=Σ_(k=0)^n(−1)^k c_(j,k,n)，于是

\[
([v^4]S_n,[v^2]S_n,[v^0]S_n)=(s_{2,n},s_{4,n},s_{6,n}),
\]

\[
(A_{3,n},A_{5,n},A_{7,n})
=(\tfrac32s_{2,n},\tfrac{15}4s_{4,n},\tfrac{189}{32}s_{6,n}).\tag{Q1}
\]

以上是实际pole jets；本稿的S_n不是223增长稿用ε平移原数值和的另一个参数函数。

定义

\[
\mathcal A_n(z)=\left(\frac{\sin\pi z}{\pi}\right)^6R_n(-z).
\tag{Q2}
\]

R_n(−z)的全部极点位于z=0,…,n，阶数≤6，正好由sin⁶消除，故A是整个函数。实轴所有固定阶导数均为O_n((1+|x|)⁻⁶)。对足够大|z|，有

\[
|\mathcal A_n(z)|\le C_n e^{6\pi|\Im z|}|z|^{-6}.
\tag{Q3}
\]

常数允许依赖n；这不是n增长估计。另由R_n(−n−t)=R_n(t)可得A_n(n−z)=A_n(z)。

## 2. 实际Fourier支持与有限和的六阶误差

采用未归一化、负号的Fourier约定

\[
\widehat{\mathcal A}_n(\xi)=
\int_{\mathbb R}\mathcal A_n(x)e^{-i\xi x}\,dx.
\tag{Q4}
\]

该普通绝对积分存在且连续。它与DLMF的正号/√(2π)约定有固定换算，以下所有2π常数都按Q4计算。

**支持lemma。** \(\widehat{\mathcal A}_n(\xi)=0\) 当|ξ|≥6π。

证明：ξ≥6π时将实轴积分向下移到Im z=−Y。A整个，固定Y时右左外边由|Re z|⁻⁶消失。由Q3，在Y足够大时，水平线积分绝对值≤C_n e^{−(ξ−6π)Y}Y⁻⁵，故Y趋无穷时为0；ξ=6π也由Y⁻⁵归零。ξ≤−6π向上移同理。这是对本整个函数的直接轮廓证明，不把未经核定的Paley–Wiener假设当作输入。

令

\[
\mathcal P_n(v)=\sum_{k\in\mathbb Z}(-1)^k\mathcal A_n(k-v).
\tag{Q5}
\]

任意有界复v集合上，和及固定v导数一致绝对收敛。其为2周期、1反周期的整个函数。又在|v|<1/2，

\[
\mathcal P_n(v)-
\left(\frac{\sin\pi v}{\pi v}\right)^6S_n(v)
=\left(\frac{\sin\pi v}{\pi}\right)^6
\sum_{k\notin\{0,\ldots,n\}}(-1)^kR_n(v-k)
=O_n(v^6).\tag{Q6}
\]

在|v|<1/2内，R_n(v−k)可能有极点只在k=0,…,n且v=0；这些k已被排除，故右侧和在小v盘全纯。无限尾有k⁻⁶统一界。Q6明确支付外侧项，不是假定有限和等于双边和；它们只在本目标的0、2、4 jets上完全相同。

## 3. 恰三个候选odd modes及固定jet矩阵

对2周期P取系数(1/2)∫₀²P(v)e^(−iπℓv)dv。偶ℓ因反周期性为0；对奇ℓ，交换绝对收敛和并令x=k−v后，每个实x被两个长度2的区间覆盖，得到系数恰为\(\widehat{\mathcal A}_n(-\ell\pi)\)。由上节支持lemma，只有ℓ=±1,±3,±5可能保留。连续同周期函数的Fourier系数唯一性给精确身份；采用的是[DLMF1.8的系数/唯一性](https://dlmf.nist.gov/1.8)，条件已实际核读。

对偶n，由A关于n/2的对称和实性，\(\widehat A_n(j\pi)\)在奇j处为实数，并且正负频率相同。定义**cos系数**

\[
\mathcal B_{j,n}=2\widehat{\mathcal A}_n(j\pi),\quad j=1,3,5.
\]

则

\[
\boxed{\mathcal P_n(v)=
\mathcal B_{1,n}\cos\pi v+
\mathcal B_{3,n}\cos3\pi v+
\mathcal B_{5,n}\cos5\pi v.}\tag{Q7}
\]

这不宣称每个mode在每个n非零。“三个”是已支付的固定频率上限及可逆jet坐标；不是由三个saddle标签获得的秩定理。

Q6与
\((\pi v/\sin\pi v)^6=1+\pi^2v^2+(8/15)\pi^4v^4+O(v^6)\)
给

\[
s_{6,n}=\sum_j\mathcal B_{j,n},\quad
\frac{s_{4,n}}{\pi^2}=\sum_j(1-j^2/2)\mathcal B_{j,n},
\quad
\frac{s_{2,n}}{\pi^4}=\sum_j(8/15-j^2/2+j^4/24)\mathcal B_{j,n}.
\tag{Q8}
\]

三个j²为1、9、25。列顺序(s₂/π⁴,s₄/π²,s₆)的反向矩阵行列式为
\((9-1)(25-1)(25-9)/48=64\)，所以正向坐标det为1/64。具体可解出

\[
\begin{aligned}
\mathcal B_{1,n}&=s_{2,n}/(8\pi^4)+11s_{4,n}/(48\pi^2)+841s_{6,n}/960,\\
\mathcal B_{3,n}&=-3s_{2,n}/(16\pi^4)-7s_{4,n}/(32\pi^2)+79s_{6,n}/640,\\
\mathcal B_{5,n}&=s_{2,n}/(16\pi^4)-s_{4,n}/(96\pi^2)+s_{6,n}/1920.
\end{aligned}\tag{Q9}
\]

与Q1的三个κ相乘，连续三行的实际Δ满足

\[
\boxed{\Delta_r=\frac{8505\pi^6}{4}
\det[\mathcal B_{j,2r+2h}]_{h=0,1,2; j=1,3,5}.}\tag{Q10}
\]

这与Root消息中独立csc推导的cos系数及常数一致；本文没有把尚未FULL读的Root224主稿登记为独审输入。若用单侧Fourier幅度而非cos系数，常数应为17010π⁶，不能混用两种B归一化。

## 4. 六重正卷积及实际微分核

令n=2r，中心变量x=z−r。由Gamma反射或原有限乘积重组，

\[
\mathcal A_{2r}(r+x)=
\frac{\Gamma(3r+1+x)^3\Gamma(3r+1-x)^3}
{\Gamma(r+1+x)^9\Gamma(r+1-x)^9}
=P_r(x)^3h_r(x)^6,\tag{Q11}
\]

\[
P_r(x)=\prod_{a=r+1}^{3r}(a^2-x^2),\qquad
h_r(x)=\frac1{\Gamma(r+1+x)\Gamma(r+1-x)}.
\]

r=0时P空积1。实际核读[DLMF5.12.E5](https://dlmf.nist.gov/5.12.E5)的完整条件Re a>0；取a=2r+1、b=2x，由beta–Gamma换算、偶延拓及t↦t/2得到

\[
h_r(x)=\int_{\mathbb R}w_r(t)e^{ixt}\,dt,\quad
w_r(t)=\frac{2^{2r-1}}{\pi(2r)!}
\cos^{2r}(t/2)\,\mathbf1_{[-\pi,\pi]}(t)\ge0.\tag{Q12}
\]

先在|Re x|<r+1用beta表达，再由两侧整个性延到全部复x。r=0给w₀=1/(2π)的box核，是常数核校准，不丢端点。

本稿*表示**普通未归一化卷积**(f*g)(t)=∫f(t−s)g(s)ds；与DLMF1.14局部含1/√(2π)的记号不同。Fubini直接给

\[
U_r=w_r^{*6}\ge0,\qquad
h_r(x)^6=\int U_r(t)e^{ixt}\,dt,\qquad
\operatorname{supp}U_r\subset[-6\pi,6\pi].
\]

U_r连续且有界变差：w_r是有界compact BV函数，卷积的变差满足Var(w_r*w_r^{*5})≤Var(w_r)‖w_r^{*5}‖₁，连续性由L¹平移连续和另一有界因子给出。因此下述反演满足点处的连续/BV条件，不仅是形式变换。

为了支付全部微分边界，用反射式
\(h_r(x)=\sin\pi x/[\pi x\prod_{a=1}^r(a^2-x^2)]\)
（整数点均取可去值），可得实轴h_r=O_r(|x|⁻²ʳ⁻¹)。因此x^q h_r(x)^6∈L¹对全部0≤q≤12r+4成立。普通Fourier反演及逐项导数的绝对积分给

\[
U_r\in C^{12r+4}(\mathbb R).
\]

这里核读了[DLMF1.14的反演及卷积条件](https://dlmf.nist.gov/1.14)，并逐一转换本稿符号。定义显式、r依赖的算子和核

\[
\mathcal D_r=\prod_{a=r+1}^{3r}(a^2+\partial_t^2)^3,
\qquad K_r=\mathcal D_rU_r\in C^4(\mathbb R).\tag{Q13}
\]

D阶数为12r。U及其所需导数在支撑外为0，端点按C^(12r+4)接为0；12r次普通分部积分没有Dirac项或遗漏边界，故

\[
\mathcal A_{2r}(r+x)=\int K_r(t)e^{ixt}\,dt,
\quad
\widehat{\mathcal A}_{2r}(\xi)=e^{-ir\xi}2\pi K_r(\xi).
\tag{Q14}
\]

K为真实偶、实、compact C⁴核，支持在[−6π,6π]。这也是Q2的直接支持证明的另一个一致实现，没有借未计算的n-operator。

## 5. 真正三点核det与正性缺口

在j=1,3,5处，e^(−irjπ)=(−1)^r。因此

\[
\mathcal B_{j,2r}=4\pi(-1)^r K_r(j\pi),
\qquad
\boxed{\Delta_r=136080\pi^9(-1)^{r+1}
\det[K_{r+h}(j\pi)]_{h=0,1,2; j=1,3,5}.}\tag{Q15}
\]

目标从三列Taylor jets准确化为**同一实际核的三个固定采样点**。若能证明r方向的三点严格Chebyshev性，Q15立即给相应Δ非零；目前未证明它。只证明K_r在三个点分别非零或同号也不够，三行仍可能线性相关。

非负的是U_r。D_r含二阶微分，不能自动保留非负性，更不能把不同r的三点取值当正Gram矩阵。本文没有宣称K_r为正测度、TP核或variation-diminishing。算子因子a²+∂²本身不是一般非负函数的positivity-preserving map，例如足够窄的正Gaussian在0处会给负值；特定U_r若具有额外结构，需要另证。这里不从一般反例推出实际K_r一定变号。

Q9/Q15是C上的可逆解析坐标。π²是非代数常数，**不是Q上或代数数域上免费的CDT source shear**；不能把223的分母12/26、arith τ或G定义费用直接分配给这些Fourier列。它们用于证明原有有理Δ非退化，数论归一化仍回到Q1。

已付222有限Δ₀>0说明这三个mode序列的最初三行不退化；这只是同一个有限证书的等价重述，不证明tail rank3、每个mode无限非零或Δ无限非零。

## 6. 单mode主项障碍与可审查的充分入口

Q7/Q8显示：若一个主mode占优，例如B₁,₂ᵣ，则实际S的共同主振幅为
\((\pi v/\sin\pi v)^6\cos\pi v\)，而不应漏掉公共prefactor。它的三个jet形成固定向量；连续三行纯主项恰rank1。两个主mode最多rank2。任何只认证一列A₇或一个共同cos主项的渐近，都没有付Q10的三列det。首项det为0也不能据此证明实际Δ=0；较小mode或幅度层可能决定它。

一个完全不依赖n-operator的充分lemma如下。置k_(j,r)=K_r(jπ)。若能在同一实际核上证明

\[
k_{j,r}=d_j\lambda_j^r r^{\alpha_j}(1+O(r^{-1})),\quad
j=1,3,5,
\]

其中d_j、λ_j均非零，三个λ_j两两不同，则

\[
\det[k_{j,r+h}]\sim
\left(\prod_j d_j\lambda_j^r r^{\alpha_j}\right)
\prod_{i<j}(\lambda_j-\lambda_i)\ne0.
\tag{Q16}
\]

证明是按每列主尺度归一化，三行极限为(1,λ_j,λ_j²)，其Vandermonde非零。因此足够大r的Δ全部非零。此lemma只是一个充分接口：本稿没有给这些实际渐近、非零Stokes常数或严格轮廓；不能用formal saddle方程或不同支撑半径下界支付它。

相比223已有的I指数上界，这里新增的是Q12–Q15的真实kernel和全部边界，以及精确三个odd modes。下一步若采用这条直接路径，只需选一个明确任务：证明这三点K-family的非退化，或对三个实际积分给足Q16的严格多模式渐近。不继续声称正卷积本身已经解决目标，也不扫描n/参数来猜符号。若只重复模式数或旧安全增长界，则没有新增的无限非零进展。

## 7. 来源、actual读取及运行账

本稿固定对象及κ来自本人已actual FULL读的222数学包11908B/`35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`；223 holonomic稿11517B/`54eb60ab2835832855cd268c5dfb4318f2c25019a4589cf713483460fa00866a`与223报告8464B/`6ee2aa403fdd73e32b6d5cc82f3611b49e4ef231b0b5b3f646e7937fa57f1edd`均在上一任务实际FULL读。没有修改这些输入，也没有借本人的作者读冒称独审。

本轮primary actual完整选读：DLMF1.8的E4系数及连续同周期Fourier唯一性；E14及其C²、f和|f″|可积的完整条件另作比较，本稿Q7实际采用直接unfold+唯一性。DLMF1.14(i)的Fourier定义、连续性、反演E3/E4及卷积E5的完整相关条件；DLMF5.12的E1 beta–Gamma身份、E5及Re a>0条件。本人没有FULL读三大网页全部章节或Nielsen/Titchmarsh原书，也没有采用搜索定位到的其他hypergeometric论文定理。来源存于[literature224目录](../literature/pade_direct_structure_sources_round224_20261008)，官方HTML3份和实际FULL读的短TEX5份；下载不等于整页FULL读取。详细identity见[dual记录](../literature/pade_direct_structure_sources_round224_20261008/dual_reading_scope.md)。

本任务数学程序/CAS/矩阵或Fourier数值/积分/参数或素数扫描/PSLQ/Lean均**0**。Q1–Q16为纸面推导；工具仅primary网页、公式下载、文档读写及bytes/hash。没有运行223 telescoping、222有限程序或Git操作。最终保存后作者须actual FULL复读全部正文，最终bytes/SHA另报；自己稿的作者读不代替同行独立审阅。Root224 csc稿若另需独审，须实际FULL读其最终保存版本后另立收据。
