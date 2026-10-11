# 第245轮：CM源的实际函数秩与两个非分裂扩张

2026-10-10，A。固定常数g，沿244定义取F、S_g=G+gF及H_g。本稿证明C7在C(z)上的实际函数秩恰为7；加入常数1后恰为8。H_g的实际cyclic阶数也恰为7。对固定g∈Q及目标假设g=X/1104∈Q均成立；native补点不降低这些秩。此为函数与连接的结构结论，未付共同图的全叶条件、严格费用或数值无理性。数学程序0。

## 1. 固定输入与底层不可约性

实际FULL读取244冻结稿global_cm_log_trigger_round244_20261009.md，6783 B / SHA256 187cbbd9bda470a07691dc2c962dd5054144e6c65a6542491498bb9342456d9c，六节C1–C7。取
\[
 \theta=z\partial_z,\quad L=\theta^3-8z(2\theta+1)^3,\quad
 J=8z(2\theta+1)-\theta/46,\quad z_0=1/4096.
\]
244已给LF=0、LS_g=JF以及H_g'=S_g/(1-4096z)。本稿的秩证明与g的数值无关，只用g是常数。

令x=64z，则L变成θ³−x(θ+1/2)³，是三阶超几何算子，α=(1/2,1/2,1/2)、β=(1,1,1)。[Beukers–Heckman原文](https://math.uchicago.edu/~drinfeld/Hypergeometric_motives/Beukers-Heckman.pdf)式(2.5)、Propositions3.2–3.3给出：两组指数的指数化参数没有交集时，单值化表示不可约。本例参数分别全为−1和全为1，故L的三维局部系统及对应C(z)微分模块不可约。

这里用的是实际现行算子。若F满足低于三阶的非零有理系数方程，F的全部单值化分支也满足它；这些分支在L解空间中生成非零不变子空间，依不可约性只能是全部三维，却不能装入低阶方程的解空间。因此
\[
 \dim_{\mathbb C(z)}\langle F,\theta F,\theta^2F\rangle=3.
 \tag{R1}
\]

## 2. 六行连接及原点残差

写f=(F,θF,θ²F)ᵀ，s=(S_g,θS_g,θ²S_g)ᵀ。完整系统为
\[
 \theta\binom f s=
 M(z)\binom f s,\qquad
 M=\begin{pmatrix}A&0\\B&A\end{pmatrix},
 \tag{R2}
\]
\[
 A=\begin{pmatrix}
 0&1&0\\0&0&1\\
 {8z\over1-64z}&{48z\over1-64z}&{96z\over1-64z}
 \end{pmatrix},\quad
 B=\begin{pmatrix}0&0&0\\0&0&0\\
 {8z\over1-64z}&{16z-1/46\over1-64z}&0
 \end{pmatrix}.
\]
这些有理矩阵不依赖g。M在0全纯，N=M(0)的作用按列基e₁,…,e₆有
\[
 Ne_3=e_2,\quad N^2e_3=e_1-e_6/46,\quad
 N^3e_3=-e_5/46,\quad N^4e_3=-e_4/46,\quad N^5=0.
\]
直接从R2又得rankN=4，故N的Jordan型恰为(5,1)。齐次三行A(0)是单个三阶nilpotent块；两份齐次模块直和的原点Jordan型为(3,3)。

## 3. 残差确实决定这里的log链

为避免以残差猜单值化，给出局部解析gauge。设M=N+Σ_(j≥1)M_jz^j，求T=I+Σ_(k≥1)T_kz^k使Y=T Z、θZ=NZ。递推为
\[
 (kI-\operatorname{ad}N)T_k
   =\sum_{j=1}^k M_jT_{k-j}.
 \tag{R3}
\]
adN nilpotent，所以左端对每个k≥1可逆，逆为有限和
\[
 (kI-\operatorname{ad}N)^{-1}
   =\sum_{r=0}^{8}{(\operatorname{ad}N)^r\over k^{r+1}},
 \qquad \|(kI-\operatorname{ad}N)^{-1}\|\le C/k .
\]
取任意小ρ使||M_j||≤Kρ^(−j)，R3的系数由标量解析级数(1−z/ρ)^(−CK)控制。因此T实际收敛且T(0)=I可逆，局部基本解为T(z)exp(N logz)。原点单值化共轭于exp(2πiN)，其块长就是(5,1)。

同论证给齐次A系统块长3。任意有理gauge在穿孔邻域单值，故保留单值化的Jordan型。于是R2不可能有理地分裂为两份L的直和：
\[
 0\longrightarrow M_F\longrightarrow M_6
  \longrightarrow M_F\longrightarrow0
 \quad\hbox{在C(z)上非分裂。}
 \tag{R4}
\]
用函数列的连接或其对偶模块均得同一判断；对偶保留不可约性、可分裂性及Jordan块长。R3同时说明所用长度5是付清的局部log结构，不是形式阶数计数。

## 4. 从非分裂模块到实际六函数独立

将R2视为六个形式符号的微分模块M₆，代入实际六函数得微分同态ev。前三符号生成不可约M_F，商模块也是由L定义的不可约M_F。R1说明ker(ev)与前三符号子模块交为0。

若ker(ev)非零，其像在不可约商模块中必为全部商。交为0又使该kernel到商的投影为同构，故M₆为前三符号与kernel的直和，构成R4所禁止的有理分裂。因而kernel为0，得到
\[
 \dim_{\mathbb C(z)}
 \langle F,\theta F,\theta^2F,S_g,\theta S_g,\theta^2S_g\rangle=6 .
 \tag{R5}
\]
这一步将抽象连接的非分裂性与实际选定芽连接起来；不以抽象六维系统的存在代替实际独立性。

## 5. H的普通点极点强制增加一维

令Y为R5的六函数列，Y'=A_6(z)Y，其中A₆=M/z。A₆在z₀是普通矩阵。若H_g=r(z)Y，r为有理行向量，微分并用R5得
\[
 r'+rA_6=b(z),\qquad
 b=(0,0,0,(1-4096z)^{-1},0,0).
 \tag{R6}
\]
b在z₀有非零simple pole。若r在此有阶数m≥1的pole，r'的最高阶为m+1，系数−m r_(−m)非零；rA₆至多阶m，不能抵消，而右端至多阶1。矛盾。于是r在z₀全纯，左端也全纯，仍与b的pole矛盾。

所以H_g不在六函数的有理线性包中：
\[
 \boxed{\operatorname{rank}_{\mathbb C(z)} C7=7.}
 \tag{R7}
\]
即使目标g使实际S_g(z₀)=0，R6的完整连接源b仍非零。native某个解的残差取消，与存在一个对整个六行模块有效的有理primitive不同。因此R7也覆盖目标g。

还有实际最小阶数结论：由H_g'恢复S_g；由LS_g=JF恢复F模块中的非零元素JF，其[z]系数为8−8/46=180/23。不可约性使这个非零元素的微分生成模块为全部M_F。故H的cyclic模块包含R5六行及H本身，而C7又给七维闭包，所以其维数和最小scalar微分方程阶数均恰为7。这里由实际独立性及cyclic生成证明阶数，没有把闭包维数直接当最小阶。

## 6. 若共同源含常数1，实际秩为8

R5六维模块没有trivial一维子模块：其子、商均为不可约rank3的M_F。任何trivial子模块投影到商，像或为0而落在M_F内，或为整个rank3商；两种都不可能。因此1不在六函数的有理线性包中。

若1=rY+c(z)H_g，微分并用R7给c'=0及
\[
 r'+rA_6=-c\,b.
\]
若c为非零常数，R6的普通点pole论证再次禁止这个方程；若c=0，则1已在六行包中，同样矛盾。故
\[
 \boxed{\operatorname{rank}_{\mathbb C(z)}(1,C7)=8.}
 \tag{R8}
\]
对有理g，上述独立性当然也在Q(z)成立。R8是包含实际常数函数的共同源判断，不是宣称H的scalar阶数为8。

## 7. 已付接口与终止边界

本稿支付底层不可约性、六行实际非分裂/独立、H的第七维、actual cyclic order7，以及加入1的实际rank8。证明对任意常数g成立；g∈Q只用于244的有理系数和整模型，目标关系只用于native log补点。

它未证明全部transported叶满足同一CM关系，也未付合法大图、严格holonomy余量、最优integer types或完整jet normality。244的安全prefix模型已经覆盖七行；Root另行提出的更紧算术模型没有在此被预先独审或当作必要成本。函数秩也不代替无界尺度的数值行列式非零证书，不提供任何混合目标的新无理性定理。

实际来源、选读身份与执行账见本轮alternative_reading_scope.md。数学程序、CAS、素数/参数扫描、Lean、git操作均0；只有既存PDF的文本抽取与NEW文档读写。保存后实际FULL作者复读本稿。

