# 原 annihilator 的反射方向与连续—离散 graph 缺陷

2026-10-07，NEW，作者 /root/scaled_root_finalize。Authority 为主报告 §§176–180 与 delivery_phase_kernel_content SHA959e24af83f2124da40079aa70fade144425f6d15e5e990e455f1ec5a088264d。580 旧冻结记录（575数学、5guards）只读。本轮纯纸证，数学producer创建、execute、import、rerun，辅助prime扩表及Lean均0。唯一NEW主稿。本稿证明原真实cot轮廓的反射身份和真实核的相位方向平衡，再把所需source方向估计精确约化为同一个P、B、V的加权graph缺陷；没有证明足够strict margin。

## 1. 实际读域、原对象与本轮新增内容

本轮actual FULL读：relative-spectrum R1–R29/all9节、exact-phase F1–F18/all7节、primitive-kernel K1–K18/all8节、coupled C1–C23、mixed-node entropy S1–S27/all10节、Hasse arithmetic J1–J18/all7节。总稿实际读 §§176–180。Audit完整JSONparse、header/current_progress/580计数字段及物理SHA；不称本人逐条人工全文读或逐一物理审计全部580记录。一次重复组合读取有工具总输出截断，不把那次重复的省略段算新的全文读域；前述完整读域来自本轮完整显示的读取。未读/执行旧数学程序或数值结果。本稿无需新增primary定理，新增PDF/HTML/code下载及实际PDF新读页均0。

固定原数值源
\[
\xi=\alpha\zeta(4)+\beta\zeta(5),\quad
\alpha,\beta\in\mathbf Q,\quad\beta\ne0,\quad m=2n,
\]
原饱和整数值basis为
\[
g=(G_1,\ldots,G_n,f_{2n},\ldots,f_{3n-1}),\qquad
f_i(z)=\binom{z-1}{i}.
\tag{D1}
\]
所有g_i有实系数。原竖线为z=c_n+ix、c_n=2n+1/2，记
\[
\rho_n(x)=\frac{R_n(c_n+ix)\mathscr K(c_n+ix)}{2\pi},\quad
R_n(z)=\frac{(6n)!^2}{(2n)!^3}
\frac{S_n(z)^3}{(z)_{6n+1}^2},\quad
S_n(z)=\prod_{a=1}^{2n}(z-a),
\]
\[
\mathscr K(z)=-4\alpha(\pi\cot\pi z)''
-\beta(\pi\cot\pi z)'''.
\tag{D2}
\]
本稿用 \(\mathscr K\) 表示cot源，以K表示primitive核basis；两者不同。令w=|\rho_n|、\(\tau=\rho_n/w\)，零密度处按反射对称选modulus1的值，它们不影响积分。冻结coupled C3给所有以下原列、有限线性组合的绝对积分收敛。真实Grams准确为
\[
B_{ij}=\int_{\mathbf R}g_i(z)g_j(z)\rho_n(x)\,dx,\quad
P_{ij}=\int_{\mathbf R}g_i(z)\overline{g_j(z)}w(x)\,dx>0,
\]
\[
V=24\sum_{j=0}^{6n}W_jv_jv_j^t>0,\quad
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad v_j=g(-j).
\tag{D3}
\]
所有算术、连续与离散量保留同一原basis。主要新定理是D4–D12的真实反射、selfadjoint involution与radical等范数方向；D16–D22给同模型phase/source两个graph的精确对齐身份，D23–D26给量化信用接口。高phase块可逆和足够小的加权缺陷尚未证明。

## 2. 原cot源使P与phase compression实对称

实系数rational R_n及cot的实反射性给
\[
\boxed{\rho_n(-x)=\overline{\rho_n(x)},\quad
w(-x)=w(x),\quad\tau(-x)=\overline{\tau(x)}
\quad\text{a.e.}}
\tag{D4}
\]
这里并非只使用整数矩阵B的实性。源在原竖线上更具体为
\[
\mathscr K(c_n+ix)
=\operatorname{sech}^2(\pi x)
\{8i\alpha\pi^3\tanh(\pi x)
+2\beta\pi^4[1-3\tanh^2(\pi x)]\}.
\tag{D5}
\]
此式由cot周期和直接求导得到，亦与本轮FULL读F14一致。β≠0保证非恒零；α=0可能的两个实零点只影响零测集。竖线上R_n没有零极点。对所有原列有 \(g_i(c_n-ix)=\overline{g_i(c_n+ix)}\)。在D3换x为−x，正Gram每项变为自身共轭，B亦然。因P本为Hermitian、B本为symmetric，得到
\[
\boxed{P\ \text{real symmetric SPD},\quad
B\ \text{real symmetric},\quad
T=P^{-1/2}BP^{-1/2}\ \text{real symmetric},\quad\|T\|\le1.}
\tag{D6}
\]
其singular values准确为实eigenvalues的绝对值。P的cross block仍可非零；实性不等于low/high正交，也不推出高B块正定。结论对真实ξ处的每个n成立，不先假设ξ有理。合理改形后的非对称轮廓应重新核P实性，不能免费沿用D6。

## 3. 相位反射的selfadjoint involution与真实核等范数分解

取 \(\mathcal H=L^2(wdx)\)，inner product linear-first，
\(\langle f,h\rangle=\int f\overline h\,w\,dx\)，
\(\mathcal F=\operatorname{span}_{\mathbf C}\{g_i(c_n+ix)\}\)。
定义
\[
J_0f(x)=\overline{f(-x)},\quad
\mathcal Af(x)=\overline{\tau(x)}\,\overline{f(x)},\quad
\boxed{\mathcal U=\mathcal A J_0,\quad
\mathcal Uf(x)=\overline{\tau(x)}f(-x).}
\tag{D7}
\]
D4使J0为antiunitary conjugation；A也为antiunitary conjugation。U是linear unitary，而且
\(\mathcal U^2f(x)=\overline{\tau(x)}\overline{\tau(-x)}f(x)=f(x)\)，
所以U selfadjoint、U²=I。这里两个conjugation的乘积一般未必involution；D4在这一验证中不可省略。

J0逐一固定原g_i，并保持F。亦保持实际高子空间
\(\mathcal H_n=\operatorname{span}\{f_{2n},\ldots,f_{3n-1}\}\)
和其P-正交补 \(\mathcal E_n=\mathcal F\ominus\mathcal H_n\)；
原high=共同S_n乘degree<n的所有多项式，未换一个任意large-spectrum空间。
因为A=U J0且J0F=F，AF=UF。置
\[
\mathcal C=\Pi_{\mathcal F}\mathcal U|_{\mathcal F},\qquad
\boxed{\mathcal W=\ker\mathcal C
=\mathcal F\cap(\mathcal U\mathcal F)^\perp
=\mathcal F\cap(\mathcal A\mathcal F)^\perp.}
\tag{D8}
\]
以e=P^−1/2g取J0固定的正交frame。D7给
\(\langle e_i,\mathcal Ue_j\rangle=\int e_i e_j\tau\,w=T_{ij}\)；
linear-first convention使operator坐标本为overline(T)，但D6使它恰T。
因此D8正是原全部bilinear moments消失的annihilator，
不是只对若干测试点为0。若ξ=c有理，primitive K对应的complex span恰W，
\(\dim_{\mathbf C}\mathcal W=\nu=m-\operatorname{rank}B\)。

设 \(\Pi_\pm=(I\pm\mathcal U)/2\)，它们为真实全Hilbert空间中±1通道的orthogonal projections。
任意h,k∈W有 \(\langle h,\mathcal Uk\rangle=0\)，故
\[
\boxed{\langle\Pi_+h,\Pi_+k\rangle
=\langle\Pi_-h,\Pi_-k\rangle
=\tfrac12\langle h,k\rangle,\qquad
\|\Pi_\pm h\|^2=\tfrac12\|h\|^2.}
\tag{D9}
\]
证明可直接用Π± selfadjoint及Π±²=Π±；由于W⊂F、Π_F Uk=0，cross项为0。尤其两个通道中各有ν维的真实核像，\(\sqrt2\Pi_\pm|_{\mathcal W}\)各为isometric embedding。这是具体原源给的方向约束；不是一般bilinear annihilator的默认正负分解。

对实系数的实际kernel polynomial h，J0h=h，D9还给明确通道函数
\[
\boxed{\Pi_\pm h(x)
=\tfrac12\{h(c_n+ix)\pm\overline{\tau(x)}
\overline{h(c_n+ix)}\}.}
\tag{D10}
\]
它们一般不在原polynomial span F。离散V只定义在原polynomials上；不能直接给D10的两个通道赋负整数evaluation再用W_j。更不能把±通道当作原low/high。相位平衡本身未估连续核Gram或relative source norm。

## 4. 原low/high phase block与kernel graph

用上述实际P-正交分解F=E_n⊕H_n，在两者各选J0固定的orthonormal frame。以下transpose/adjoint均在这个frame中，矩阵实，亦可按Hermitian convention统一写*。C的真实块为
\[
\mathcal C=
\begin{pmatrix}C_{EE}&C_{EH}\\C_{HE}&C_{HH}\end{pmatrix},\quad
C_{EH}=C_{HE}^*,\quad\|\mathcal C\|\le1.
\tag{D11}
\]
此变换同时施于原B、P、V。它不声称还是整数基；ratio与真实J的身份在此不变，而原q的整性仍在原格计费。一般性P剪切不会给C_HH非零；V_high evaluation单位也不会给它非零。

**Graph定理。** 仅在实际C_HH可逆时定义
\[
G=-C_{HH}^{-1}C_{HE},\qquad
D_E=C_{EE}-C_{EH}C_{HH}^{-1}C_{HE},\quad
\mathcal Z=\ker D_E\subset E_n.
\tag{D12}
\]
逐块解Ch=0给准确双射
\[
\boxed{\mathcal W=\{e+Ge:e\in\mathcal Z\},\quad
\dim\mathcal Z=\nu,\quad \|e+Ge\|^2=\|e\|^2+\|Ge\|^2.}
\tag{D13}
\]
这不是先选一个自由graph作为kernel；Z由原phase Schur complement确定。若ν=0，为空graph并按空det convention处理。

记 \(s=\sigma_{\min}(C_{HH})>0,\ \epsilon=\|C_{HE}\|\)。有
\[
\|G\|\le\epsilon/s,\quad
C_{HE}C_{EH}+C_{HH}^2\preceq I_{H_n},
\quad\boxed{\epsilon^2\le1-s^2,\quad
\|G\|\le\sqrt{1-s^2}/s.}
\tag{D14}
\]
中间式来自C²≤I的HH block，使用selfadjoint reflection；这是具体的phase conditioning到low/high泄漏的安全比较。只有固定s>0时泄漏一般仍固定量级；若昂贵source高谱指数级大，固定泄漏不能自动提供n²信用。

C_HH singular时，正确解为
\[
h_H=-C_{HH}^\dagger C_{HE}e+\eta,\quad
\eta\in\ker C_{HH},\quad C_{HE}e\in\operatorname{ran}C_{HH},
\]
并另满足 \(C_{EE}e+C_{EH}h_H=0\)。这里η由剩余phase方程约束，不能删除。D13–D14在这个分支不被免费延伸；本文没有证明原每个n的高phase块可逆。

## 5. 原离散source的最小能量graph与exact缺陷

在同一P-orthonormal decomposition定义actual relative source operator
\(\mathcal R=P^{-1/2}VP^{-1/2}\)（不同正交frame只作unitary similarity），其quadratic form为
\[
v(h)=24\sum_{j=0}^{6n}W_j|h(-j)|^2
=\langle\mathcal Rh,h\rangle,\qquad
\mathcal R=
\begin{pmatrix}R_{EE}&R_{EH}\\R_{HE}&R_{HH}\end{pmatrix}>0.
\tag{D15}
\]
本式h(-j)指同一h的原polynomial延拓，不对全Hilbert任意函数定义evaluation。R_HH严格正定。准确source Schur与source-minimizing graph为
\[
S_E=R_{EE}-R_{EH}R_{HH}^{-1}R_{HE}>0,\qquad
G_V=-R_{HH}^{-1}R_{HE}.
\tag{D16}
\]
对所有e∈E_n、h_H∈H_n完成平方，
\[
\boxed{v(e+h_H)=
\langle S_Ee,e\rangle+
\|R_{HH}^{1/2}(h_H-G_Ve)\|^2.}
\tag{D17}
\]
source的有限原节点、权重24及全部W_j在两项中完整保留。此Schur投影以原P为规范，并非只改P后留下旧V。

若实际phase高块可逆，将D13代入并定义
\[
\boxed{\Delta=G-G_V
=-C_{HH}^{-1}C_{HE}+R_{HH}^{-1}R_{HE},}
\]
\[
N_{\mathcal Z}=(S_E+\Delta^*R_{HH}\Delta)|_{\mathcal Z},
\qquad A_{\mathcal Z}=(I+G^*G)|_{\mathcal Z}.
\tag{D18}
\]
限制表示在Z选orthonormal frame后压缩；不要求G保持Z。phase graph可以有很大的高分量，但若它与source最小能量graph对齐，其加权Δ仍小。D17证明真正需要比较的是Δ，单独估G的坐标大小可能损失这一相消。

实际P-normalized kernel source \(R_K\)的eigenvalues准确是这两个positive forms的generalized eigenvalues：
\[
\boxed{R_K\sim_{\rm unitary}
A_{\mathcal Z}^{-1/2}N_{\mathcal Z}A_{\mathcal Z}^{-1/2},
\quad
\det R_K=\frac{\det N_{\mathcal Z}}{\det A_{\mathcal Z}}.}
\tag{D19}
\]
证明：取Z的orthonormal frameQ，实际核map \(\begin{pmatrix}I\\G\end{pmatrix}Q\)有continuous Gram \(Q^*(I+G^*G)Q\)、source Gram \(Q^*(S_E+\Delta^*R_{HH}\Delta)Q\)。按其continuous Gram正交化即得R_K；primitive K与这frame相差可逆ν×ν基变换，两Gram det同乘|det|²，ratio不变。没有任意核height费。

D19是同一个真实kernel的精确方向接口。它不假定primitive kernel位于所有large relative eigenvalues的低补空间，也不将P_high diagonal bound换成E_n上未经证明的同一bound。

## 6. 全尺度compression upper及真正n²门槛

以下量均为原模型可独立核验的operator norm：
\[
\sigma_E=\|S_E\|,\quad
\delta=\|R_{HH}^{1/2}\Delta\|,\qquad
b_n=\sigma_E+\delta^2>0.
\tag{D20}
\]
可只在真实Z上取norm得到更强版本；全E_n norm给安全uniform bound。D19及A_Z≥I得
\[
\boxed{R_K\preceq b_n I_\nu,\qquad
\log\det R_K\le\nu\log b_n-\log\det A_{\mathcal Z}.}
\tag{D21}
\]
第一式在P-normalized核frame中成立；N_Z≤b_nI，A_Z^−1≤I。第二式保留continuous graph norm，较只用νlogb_n更精确。ν0两项为空，信用0。

也可给一个无需source Schur逆精度的较粗graph比较。令r_E=||R_EE||、r_H=||R_HH||，t=||G||。positive source的Cauchy–Schwarz给
\[
\boxed{R_K\preceq \widehat b(t)I,\quad
\widehat b(t)=\max_{0\le u\le t}
\frac{(\sqrt{r_E}+\sqrt{r_H}u)^2}{1+u^2}
=\begin{cases}
\dfrac{(\sqrt{r_E}+\sqrt{r_H}t)^2}{1+t^2},
&t<\sqrt{r_H/r_E},\\
r_E+r_H,&t\ge\sqrt{r_H/r_E}.
\end{cases}}
\tag{D22}
\]
r_E>0，边界相接。任一实际graph vector的u=||Ge||/||e||≤t，故不需要独立最大化未匹配source/cot量。D14给合法t upper，却不证明r_E、r_H足够便宜。D21允许Δ相消；D22把它丢掉，不能用两者分别扣两次信用。

本轮FULL读relative R4–R5已证，在同一个原P,V上
\[
\lambda_n(\mathcal R)\ge a_n
=c(n+2)^{-C}e^{a_*n},\quad
a_*=\tfrac{17}{2}-6\log3+2\log2>\tfrac{13}{4}.
\tag{D23}
\]
因而0≤ν≤n有eν(R)≥a_n^ν。在有理假设的无限适用n=4r上，actualν≤n/2，冻结R6精确
\[
|J_\nu|=H_\nu\mathcal L_K\Theta_d,\quad
\mathcal L_K=\det R_K/e_\nu(R),\quad0<\mathcal L_K\le1.
\tag{D24}
\]
D21–D24给新的可量化方向比较
\[
\boxed{-\log\mathcal L_K\ge
\nu\log(a_n/b_n)+\log\det A_{\mathcal Z}.}
\tag{D25}
\]
右端可为负；仍有通用0下界，不能把未知Δ删去宣称正信用。
特别若同一无限子列C_HH可逆，ν/n→κ>0且
\[
\log(\sigma_E+\delta^2)\le b\,n+o(n),\quad b<a_*,
\]
则
\[
\boxed{\liminf n^{-2}(-\log\mathcal L_K)
\ge\kappa(a_*-b)
+\liminf n^{-2}\log\det A_{\mathcal Z}
\ge\kappa(a_*-b)>0.}
\tag{D26}
\]
如果ν=o(n)，仅固定指数差不保证正n²主率。若source Schur指数b_s、weighted defect指数b_δ分别受控，D20中b可取max(b_s,2b_δ)加o(1)；不把未加权Δ norm直接当δ。本文尚未给原模型所需的高phase可逆、σ_E或δ上界。

## 7. 相位平衡和phase高块单位仍不足：限定Hilbert例子

本节只检查上面哪些一般条件无法推出D26，不是原cot、paired source或所有研究方法的no-go。取n为4的倍数、m=2n、ν=n/2、d=3n/2，在finite Hilbert空间选orthonormal u_1,…,u_d、v_1,…,v_ν及额外w_1,…,w_ν。F为u/v span，J0为该frame的coefficient conjugation。定义selfadjoint unitary
\[
Uu_i=u_i,\quad Uv_a=w_a,\quad Uw_a=v_a,\quad A=UJ_0.
\tag{D27}
\]
U与J0 commute，A为conjugation，C=Π_FU|F=diag(I_d,0ν)，W=span(v)。每个v在U±通道恰各半范数。任选高H_n⊂span(u)维数n，则C_HH=I、G=0。取P=I、positive source R=M_nI_m，M_n=e^{an}、a>a_*；这满足至少n个指数relative通道。可是
\[
\boxed{\Theta_d=1,\quad
\mathcal L_K=\frac{M_n^\nu}{\binom m\nu M_n^\nu}
=\binom m\nu^{-1},\quad
-\log\mathcal L_K\le2n\log2=o(n^2).}
\tag{D28}
\]
source Schur仍M_nI，缺陷Δ=0。因此相位平衡、实际graph可逆甚至单位、large relative spectrum共存时，也必须估源的cheap Schur方向。例子没有原cot密度、原g、W_j或算术内容，不能据它排除实际更强结论。其用途是防止从D9或D14单独跳到D26。

## 8. 同一个首次jet的费用与仍未闭合的实际条件

设 \(\mathfrak c_n=-\log\mathcal L_{K_n}\)、\(\mathfrak p_n=-\log\Theta_{d_n}\)。
本轮FULL读entropy S4与Hasse arithmetic J16/J18给
\[
\log H_{\nu_n}\le
[-22/3-2\gamma+\kappa_n(\Theta+17/2)]n^2+o(n^2),
\quad \gamma\ge1.455845,\quad\Theta=K_3<11557/400,
\]
\[
|J_{\nu_n}(c)|\ge
\exp[-(A_{\rm full}-5\kappa_n^2/4)n^2-o(n^2)],\quad
A_{\rm full}<40.314517427,\quad\kappa_n=\nu_n/n.
\]
因此真正充分的same-object条件仍为
\[
\boxed{\liminf\left[
\frac{\mathfrak c_n+\mathfrak p_n}{n^2}
-A_{\rm full}+\frac54\kappa_n^2+\frac{22}{3}
+2\gamma-\kappa_n(\Theta+\tfrac{17}{2})
\right]>0.}
\tag{D29}
\]
D25提供了 \(\mathfrak c_n\) 的新原块表达式，并未使D29成立。Γ/head费用全部在同一已读Hν中计一次，source extraction在S4中已支付；相对ratio不再独立扣同一Γ。固定source/input分母准确为(DM)^(2n−ν)，费O(n)而非被遗漏。κ0时图信用为空，仍需独立phase/full determinant处理，不能把ν=n/2的收益套给全部adaptive阶。

若转为primitive商q，则用其自身整模型；不能除去a_V后沿用jet成本。最新authority的q安全费用635/16以及source-content信息不能作为R_K upper：后者还含连续P_K。同行本轮正在证明unit-W节点的核valuation约束；在正式全文阅读与审查前，本稿不把聊天lemma当已冻结数学输入。即使它成立，其离散整除/内容lower也须与连续核norm同对象比较，不能直接推出本稿σ_E或δ上界。

## 9. 精确未闭合处与可核的下一目标

本轮已经无条件证明的是原cot源的P/T实对称、phase-reflection selfadjoint involution、D9–D10的真实radical等范数方向，以及D17的同原源完成平方。实际C_HH可逆时D13/D19/D25全部是等式或安全全尺度不等式。三个尚未得到的具体原模型结论为：

1. 实际高phase压缩C_HH的非零与conditioning；它涉及 \(\int S_n^2p q\,d\mu\)，正high Gram及负节点评价unit均不能代替。
2. 原P-orthogonal低空间上的source Schur normσ_E。原整数低列的source diagonal或左Hardy bound不能无偿搬到P-orthogonal低列；high投影同时改变source。
3. 实际phase graph与source最小能量graph的weighted缺陷δ。需比较C_HH^−1C_HE与R_HH^−1R_HE的同方向相消，单独dim计数或primitive height不够。

若第1项失败，应先研究D14后述含ker C_HH的解空间，不删η；若第2项指数太大，应直接在真实Z上估detN_Z/ detA_Z，不能以全E上坏norm反推实际不可能。D9的两个通道一般非原polynomial，源evaluation无法免费施加；可考虑原合法contour共同变形，但新P、phase和K的continuous Gram需要同时重算。

这些是具体、可逐式纸核的原对象门槛，不是声称已经得到新ζ/L/Catalan无理性、LI、Lean或strict gap。唯一NEW稿待实际FULL交叉独审、收审后作者最终全文回读和单向FINAL来源收据；580旧冻结字节保持不变。
