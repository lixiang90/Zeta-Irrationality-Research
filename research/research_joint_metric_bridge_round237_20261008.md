# 第237轮：联合整格进入holonomy的桥成立，实际费用由首项行列式决定

2026-10-08。上一轮236是progress；本轮继续同一个数值目标，不重置正式全局复盘计数。**仍没有新的ζ/L值无理性或线性无关性定理。** 本轮填补了236指定的度量传递缺口，并证明一个会改变下一步行动的精确格变换不变量。

## 1. 保留真实源与问题

固定有理数g及正整数b_g，b_gg为整数。取

\[
f=(1,uE,b_gJ_g),\quad
E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
S=\sqrt{1-4u},\quad J_g=S(g-2I),\quad I'=E/S,\quad I(0)=0.
\]

采用234–236已付的真实连接值，关系目标保持为

\[
t=\frac52L(2,\chi_{-3})-\frac{\pi\log3}{3\sqrt3}.
\]

本轮没有替换成Clausen目标、没有证明t无理，也没有以文献搜索缺失认证新颖性。236的完整联合模型仍是

\[
L_D=\mathbb Z[u]_{\le D}^3,\qquad
T_N(P)=[P\cdot f]_{0,\ldots,N},\qquad N=3D+C_0.
\]

三维源实际微分闭合：若F=uE、K=b_gJ_g，则

\[
F'=\frac1{2(1-3u)}+\frac F{2u},\qquad
K'=-\frac{2b_g}uF-\frac2{1-4u}K.
\]

采用CDT Theorem3.2.8（Shidlovsky），可选固定C_0，使全部实际vanishing jumps不超过N。这里没有宣称3D+2这个单纯数量匹配截断已单射。已付的Q(u)-rank3保证完整源评价单射；不是有限头实验独立性。

## 2. 直接BC桥：不用另付CRT基高度

先对一般m维独立、微分闭合的有理芽证明。设L_D=Z[u]≤D^m，Γ_D⊂L_D是full-rank子格，且所有0至N=mD+O(1) jets整数，N覆盖全部实际过滤阶。设φ:(D,0)→(C,0)为CDT的BC度量适用的holomorphic map，φ'(0)≠0、全部pullback亚纯，λ=log|φ'(0)|，并要求下面J有限：

\[
J=\iint_{\mathbb T^2}\log|\phi(z)-\phi(w)|\,d\mu(z)d\mu(w).
\]

以CDT §7.3的O(1)_φ度量赋给每一行多项式，取正交直和。在原文的Laurent section约定中，用P↦u^{-D}P将Z[u]≤D识别为Z[1/u]≤D；formal section u^{-D}(P·f)的过滤阶仍是ord(P·f)。不额外引入一个Dλ项。

若ℓ_D=log[L_D:Γ_D]，CDT的arithmetic Hilbert–Samuel式及同实处度量的covolume定义给

\[
\widehat{\deg}\,\Gamma_D=\frac m2 JD^2-\ell_D+o(D^2). \tag{1}
\]

令V_D为实际过滤阶集合，|V_D|=m(D+1)。Γ与L有同一Q-span及同一R-span，故各阶实处子空间和商度量相同。CDT Lemma7.4.1的估计因此对Γ完全相同：

\[
h_\infty(\psi_D^{(n)})\le-n\lambda+DJ+o(D),\qquad
\sum_{n\in V_D}h_\infty(\psi_D^{(n)})
\le\left(-\frac{m^2}2\lambda+mJ\right)D^2+o(D^2). \tag{2}
\]

第二式使用|V_D|和V_D⊂[0,mD+O(1)]；这还给Σn=m²D²/2+O(D)。CRT整数基的坐标大小不进入(2)：实处规范是在原来的整个系数空间上固定，商度量只依其子空间。

在有限处，Γ^(n)=Γ∩{ord≥n}是饱和子格，Γ^(n)/Γ^(n+1)无扭。全部相关jets整意味着其首项评价是到Z的同态，所以每个p的算子范数≤1，即h_p≤0。不能只要求单个选中jet整数而漏掉其他实际过滤阶。

采用CDT Lemma7.2.13的filtered slopes inequality，目标graded lattice为固定Z、norm1，得

\[
\frac{m^2}2\lambda\le\frac m2J+
\limsup_{D\to\infty}\frac{\ell_D}{D^2}.
\]

若κ是右侧index主项的已证upper，则

\[
\boxed{m\lambda\le J+\frac{2\kappa}m},\qquad
\boxed{m\le\frac J{\lambda-2\kappa/m^2}}
\quad\text{（第二式须分母为正）。} \tag{3}
\]

这证明236提出的rank3费用2κ/9是合法的充分upper，但前提是同一格、全部实际首项、上述实处度量及零估计已经一并支付。没有从raw index定义τ后直接调用不同的CDT模板。

开放disc内的亚纯pole通过固定ρ<1缩图处理：有限多个pole由h_ρ(z)、h_ρ(0)=1清除；固定ρ时其费用为O_ρ(1)，全阶求和为O_ρ(D)。先D→∞，再ρ→1，λ_ρ→λ、J_ρ→J。这里采用原文7.4.1/7.3.17脚注的limit，未把任意有极点的映射当作无需修正的meromorphic BC map；φ本身仍holomorphic，pullbacks允许meromorphic。

## 3. 更准确的格变换不变量

上述index判据丢掉了可能为负的有限处高度。保留这些高度后，得到更强且自含的结论。

固定同一完整Q过滤及同一实处度量，Γ⊂L为任意full-rank整数子格。令

\[
L^{(n)}=L\cap V^{(n)},\qquad \Gamma^{(n)}=\Gamma\cap V^{(n)}.
\]

每个实际jump n的graded商rank1；把Gr_nΓ识别为Gr_nL中的子格，记其index为s_n。逐层有限商的exact sequence给

\[
\prod_{n\in V_D}s_n=[L:\Gamma]. \tag{4}
\]

若原primitive graded generator的首项为β_n∈Q×，新generator首项为±s_nβ_n。固定目标Z_p的norm1给

\[
h_p(\psi_{\Gamma}^{(n)})
=h_p(\psi_L^{(n)})-v_p(s_n)\log p.
\]

故

\[
\boxed{\sum_nh_{\rm fin}(\psi_\Gamma^{(n)})
=\sum_nh_{\rm fin}(\psi_L^{(n)})-\log[L:\Gamma].} \tag{5}
\]

与此同时实处evaluation heights完全相同，degree也恰减log[L:Γ]。在**精确**filtered slopes inequality两边，这个变化抵消。它不否定(3)，但说明更大的整数格只是可能提供一个更好的upper认证，不能独自改变这个完整过滤的内在算术费用。

定义

\[
\mathcal A_D:=\ell_D+\sum_nh_{\rm fin}(\psi_\Gamma^{(n)})
=\sum_nh_{\rm fin}(\psi_{L_D}^{(n)}). \tag{6}
\]

这个量可以为负；不能在取upper时无理由截成非负。对所有实际jump rows的square Taylor矩阵T_{V_D}，以标准全部m(D+1)系数列定义，完整评价单射及flag给

\[
\boxed{\mathcal A_D=-\log|\det T_{V_D}|.} \tag{7}
\]

证明：嵌套饱和整过滤可取兼容的primitive Z基，换基矩阵在GL_M(Z)中；按jump顺序的evaluation矩阵为三角矩阵，diag为β_n。因此det为±∏β_n，product formula给Σ_p log|β_n|_p=−log|β_n|。这不是任选满秩minor、generic rank或某几个有限头。V_D必须是实际过滤阶，跳阶允许存在。

将(6)代回(1)–(2)，若a是limsup A_D/D²的upper，真实基本BC判据是

\[
\boxed{m\lambda\le J+2a/m}. \tag{8}
\]

Γ全jet整只证明A_D≤ℓ_D。236的raw index节省仍是有效上界认证的改善，但尚不证明a改善到足够小。

## 4. 当前预算结论与范围

236保守完整CRT模型κ=45/4，在m=3的(3)中给2κ/9=5/2，比旧固定类型费用7/3更高。**这个保守upper不能得到新矛盾，也不能据此排除所有联合格或本源的真实算术费用。** finite negative heights可能让a严格小于κ。

单图基本BC式要排除rank3，必须实际证明a<(9λ−3J)/2，并付相应图及J的严格值。由Jensen得J≥λ，沿用已付共同图cap λ≤log C*、C*=3π³√2/8，得到这套基本判据的必要门槛

\[
a<3\log C^*.
\]

此处不将该必要门槛扩大为任意新metric、多图或mixed-period determinant的通用no-go，也不把既有7/3的模板下界自动转成a的下界。

本轮(4)–(7)仅针对完整full-rank源、固定普通rank-one目标graded lattices和相同实处度量。改变source subspace、真实周期投影、目标格或metric须重算；balanced tensor限制不在该无条件不变量的范围内。

## 5. 第238轮的可检验首关

不再以“更大的CRT格”作为独立突破目标。238优先对这个实际三维源证明全尺度的实际jump行列式公式/估计，或证明其有效费用下界已超过能够利用的图门槛。不能用0,…,3D+2方阵代替T_{V_D}而不付非零和真实jumps。

可以从c行的polynomial jets消去后剩余两species的Toeplitz/Hankel块开始，但必须保留全部gS及finite heads，并在任何perfectness或Jacobi匹配前证明所用minor确实对应实际flag。只在精确费用仍有严格可能余量时才细化相关prime层；不恢复basis、energy或有限样本扫描。

238若不能推进这个all-scale实际行列式接口，则按236决定停止当前模型的优化，转固定M0,10数值周期投影。后备准备稿不给实验rank4或有限头赋予全n身份。正式全局复盘仍计划242，窗口240–244；本轮真实核心进展不触发无进展战术停止，也不以战术检查重置正式计数。

## 6. 来源与验证

数学依据为当前CDT作者220页PDF：Theorem3.2.8、§7.2的covolume/filtered slopes、§7.3的BC metric/Hilbert–Samuel、完整Lemma7.4.1证明。原始选页文本与关键degree/slopes原件PNG保存于literature/joint_lattice_metric_sources_round237_20261008。Root实际FULL读50–54及96–110，视觉核95/104；95除图内内容外不声称本轮整页文本FULL。采用既有BC原文定理，不声称独立重证arithmetic Hilbert–Samuel或Shidlovsky。

两条独立纸面审阅确认(3)与(4)–(7)；最终完整稿及独审另存并列入本轮manifest。这些是由标准斜率方法与格论给出的本项目结构引理，不声称一般Arakelov理论的新原创定理。数学计算程序、参数扫描、Git修改、Lean构建均0。文件读取、PDF选页文本保存和来源归档属于记录操作，不冒充数学计算验证。
