# 双极点路线的真实费用、解析残差与提高零点阶数的修复

日期：2026-10-06。本轮NEW。目标仍是新的特殊值无理性/线性无关性，不以布局归约或文件审计替代该目标。本轮得到全尺度结构引理及费用证书，尚未得到新的数值定理。

## R1. 当前真实输入与上一轮分类

上一轮是progress：已冻结[真实混合目标身份及H9](cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md)，SHA e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463。它证明旧三重零点布局的无穷非零子序列，未证明费用和匹配解析界。本轮重新实际全文读取该稿，实际读取[Lai原件](../literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf)PDF7–14、18–22；累计root实际读1–14、18–23，不称全文25页独验。原件SHA仍838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58，未重下载或改动。

NEW工作分别为[算术主稿](cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md)、[解析主稿](cdt_odd_mixed_double_pole_analytic_decay_20261006.md)、[真实整格比较稿](cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md)。这些稿的已证范围以各自终稿和独审为准；本稿独立证明下面的通用非零布局及精确连续费用模型。旧冻结稿全部保留。

## R2. 三重零点的真实解析限制

旧H9有R_n(t)=((6n)!)²/((2n)!)³·S_n(t)³/(t)_(6n+1)²，S_n=(t−2n)_(2n)，h=3n。对s5，实际泛函为4aΣ(RP)''−bΣ(RP)'''。前2n个整数处二阶导数消失，但

\[
 (RP)'''(m)=R'''(m)P(m)\ne0\quad(1\le m\le2n)
\]

一般成立。因此向右移到Re t=2n+1/2的积分只能表示尾和；全部泛函还含−bΣ_{m≤2n}R'''(m)P(m)。其在degree<3n空间的bilinear correction恰rank2n：所有R'''(m)非零，2n个不同节点的evaluation columns独立。原论文weight4衰减不能通过fixed higher-derivative kernel免费移植。

保留左contour Re t=1/2可得完整全尺度安全界 |J_n,s|≤C^(3n)3^(−9n²)，固定s,a,b时B_safe=9log3。这个界覆盖有限残差；未证明它是最佳衰减。详见NEW解析稿。

## R3. 对全部固定s≥4恢复轮廓移动的通用布局

令k=s−1≥3，整数B>k，d=B−k，h=dn，定义
\[
 R_{n;k,B}(t)=\frac{(Bn)!^2}{(2n)!^k}
 \frac{S_n(t)^k}{(t)_{Bn+1}^2}.
 \tag{R3.1}
\]
对degP,Q<h，deg(RPQ)≤−4；全部series绝对收敛。R在m1..2n的零阶k严格大于s−2，因此相关两种导数均消失，移动到Re t=2n+1/2没有这组有限残差。

部分分式系数仍有真实目标投影：
\[
 W_j=\binom{Bn}{j}^2\binom{2n+j}{j}^{k},\quad
 C_j=(k+2)H_j-kH_{2n+j}-2H_{Bn-j},
\]
\[
 U_j=-(s-1)a(s-3)!H_j^{(s-2)}-b(s-2)!H_j^{(s-1)},
\]
\[
 V_j=C_jU_j+(s-1)![X-aH_j^{(s-1)}-bH_j^{(s)}].
\tag{R3.2}
\]
用L_X(P)=Σ_jW_j(U_jP'(−j)+V_jP(−j))及J_X=detL_X(t^(i+j))/∏i!²。R3.2无条件定义Q[X]有理多项式；只有候选关系aζ(s−1)+bζ(s)=c成立时，X=c评价等于实际解析级数。ΣA1,j=0消去较低ζ值，不能把形式多项式身份误作数值关系已成立。

## R4. 通用布局无穷非零及归一化费用

取n=2m，素数p=(B+k)m+1，p>max(s+1,|b|)，q=dm，h=2q。j<p部分在H9的p-scaled Hermite basis上缩放p^(s−4)后均在pZ_p。其余j=p+l、0≤l<q满足
\[
 W_{p+l}\in\mathbf Z_p^\times,\quad C_{p+l}=2/p+O(\mathbf Z_p),\quad
 H_{p+l}^{(v)}=p^{-v}+O(\mathbf Z_p).
\tag{R4.1}
\]
证明Wunit直接用Lucas。Bn=2Bm=p+(B−k)m−1，故第一个binomial模p为binom(q−1,l)；第二个为binom(4m+l,l)。q−1<p且4m+l≤(B−k+4)m−1<p，后者来自k≥3。Bn<2p、2n+Bn<2p也由k≥3成立，所有调和数只有一个p-denominator；HBn−j的上限q−1−l<p，所以C的leading是(k+2−k)/p。

在节点0..q−1的Hermite basis P_l=p²E_l、Q_l=pF_l上，E_l values1/derivative0，F_l values0/derivative1。节点差均小于p，未缩放E,F是Z_p-unimodular basis。Taylor移p及R4.1给p^(s−4)Gram模p blocks
\[
 (s-2)!bW_{p+l}
 \begin{pmatrix}-(s+1)&s\\s&-(s-1)\end{pmatrix}.
\tag{R4.2}
\]
det为−((s−2)!bW)²unit。因此任意X∈Z_p的实际det非零；Dirichlet给无穷p≡1 mod(B+k)。这是对通用布局的全尺度非零证明，未用有限枚举。

**归一化不能省略。** scaledbasis determinant valuation3q，故monomialdet的exact valuation是−h(s−1)。若h≥p，factorial normalization再减2Σ_{i<h}v_p(i!)；由于h<2p，此项为2(h−p)_+。B≤3k的布局没有这个额外项，B>3k须明确计入。s5的B5/6/8均满足前者。

在p>s+1时Schur elimination可进一步读actual elementary exponents：q份−s、q份−(s−2)，因此旧H9s5的−5/−3确实比s4的−4/−2多付费用。它是指定auxprime上的真实局部等式，单一p每n只给O(nlogn)，不据此断言全素数n²费用下界。

## R5. 全素数minor模型与可证明算术费用

NEW算术稿严格自证全部prime的归一化Gauss bounds。大primep>sqrt((B+2)n)按ρmodp拆form；令
\[
 q_\rho=\lfloor(Bn-\rho)/p\rfloor,\quad
 w_\rho=2\lfloor Bn/p\rfloor-2q_\rho
 +k\lfloor(2n+\rho)/p\rfloor-k\lfloor2n/p\rfloor.
\]
对m-minor可用
\[
 F_{s,\rho}(m)=m^2+(w_\rho-s-1)m
 +(s-1)(m-2q_\rho)^+
 +1_{m=1}1_{p>\max(Bn-\rho,2n+\rho)},
\tag{R5.1}
\]
且m>2(qρ+1)时minor为0。Tail entries的界是i+j+w−s，head entries为i+j+w−1；tailrank≤2q迫额外s−1的credit。换integer shift basis和Cauchy–Binet保留所有minors。ρ0还可加强rank/content，但它只改连续模型的lower-order项。

**这些都是安全下界，不是真实valuation下界的最优性声明。** Signed common multiplier保留正valuation信用，对整个J(X)的Gauss coefficients同时有效；不能把normalization或改变非unimodularbasis当免费降费用。

## R6. 精确连续优化：无需由有限n猜全尺度

设x=p/n，u=ρ/p，A=floor(B/x)，C=floor(2/x)，q=floor(B/x−u)，w=2·1_{u>{B/x}}+k·1_{u≥1−{2/x}}。每个u类的凸函数F(m)允许0≤m≤2(q+1)。其marginal
\[
 \Delta_m=2m+w-s-2+(s-1)1_{m>2q}
 +e(1_{m=1}-1_{m=2}),
\tag{R6.1}
\]
非递减，其中e是R5.1的exceptional indicator。最小总费用在约束平均m=d/x下由排序marginals填充精确得到，不是启发式greedy。每个类的x·measure由0、B−Ax、(C+1)x−2、x四个有序阈值的差给出。

在floor及阈值次序固定的interval中，各marginal整数不变，capacity是x的affine函数；累计capacity达到d的点再把interval细分，所得
\[
 g_{s,k,B}(x)=x\min\int_0^1F_u(m_u)du
 +x\lfloor d/x\rfloor(\lfloor d/x\rfloor+1)-2d\lfloor d/x\rfloor
\tag{R6.2}
\]
严格affine。Floor breakpoints是B/j、2/j、d/j；两个内部阈值交叉在(B+2)/j。代码列全这些breakpoints，再解每个capacity=d affine根；因此分段积分是有限精确有理计算。离散residue数与连续measure仅差O(1)，在x≥ε上cost/rank修正也O(1)，不改变PNT求和的n²率。

用完成平方、0≤w≤k+2及方差≤(k+2)²/4，得到
\[
 g_{s,k,B}(x)\ge-ds-\frac{(k+2)^2+4}{16}x.
\tag{R6.3}
\]
所以未计算的0<x<ε尾积分至少−dsε−((k+2)²+4)ε²/32。小primep≤sqrt((B+2)n)使用普适entry界，仅贡献O_s(n^(3/2)logn)；p>Bn系数为整数。PNT及R6.2/3从而给整个Gauss common multiplier的全尺度费用上界，适用于任意固定integera,b和形式X，非有限n实验。

## R7. 旧布局升weight的精确模型损失63/4

在旧B6,k3,d3模型，所有固定s≥4有
\[
 g_s(x)=g_4(x)-(s-4)T(x),\quad
 T(x)=\begin{cases}3,&0<x\le9/2,\\12-2x,&9/2\le x\le6.\end{cases}
\tag{R7.1}
\]
证明F_s−F4=−(s−4)min(m,2q)。当A=floor6/x≥2，ceil3/x≤A，所有类都有tailcap至少A；填充到m≤A的tail marginal至多2A−1，任何head marginal至少4A−3。故s4的最优分配全部在tail，且总资源3/x可填满；提高s只使tail更便宜，此分配仍最优，损失3(s−4)。A1时，逐类q1的w0/3、q0的w2(exception1)或5；所有tail costs至多1，所有head costs至少2，故先填满tail。Tail平均capacity=2(6/x−1)，因此加权损失min(3,12−2x)。这证明R7.1，且
\[
 \int_0^6T(x)dx=63/4.
\]
它是**这个minor下界模型**每增加一weight的费用率损失，绝不等同actual最优分母费用下界。

根NEW[旧布局精确producer](cdt_odd_double_pole_residue_lp_20261006.py)首次执行一次，[证书](cdt_odd_double_pole_residue_lp_20261006.json)对ε1/100给每个s1200段精确有理积分。含严格尾界的safeA满足A4<30.409、A5<46.159、A7<77.659；A_s之间正好多63/4(s−4)。Source适用性来自R5–R7纸面证明，不能只凭这些数值宣布一个算术定理。

## R8. 修复零点后的匹配界与本轮判别

NEW解析稿独立证明恢复布局的G、全尺度uniform bound及sech determinant。令
\[
 G_{k,B}(y)=(k+2)\log(y^2+4)-(B+2)\log(y^2+(B+2)^2)
 +(k+2)y\arctan(2/y)-2y\arctan((B+2)/y)
 +2B\log B-2k\log2.
\]
对0<λ=G'(y*)<2π，c1=G(y*)−y*λ、κ=2π−λ，global tangent自G''单次变号得到。Degreeh归一化后
\[
 \log|J_{n,s}|\le-\beta n^2+O(n\log n),\quad
 \beta=d^2\log(2\kappa/\pi)-dc_1.
\tag{R8.1}
\]
s5/k4、y*=1时κ=6atan(1/2)−2atan(1/(B+2))且c1=6log5−(B+2)log((B+2)²+1)+2BlogB−8log2。根另NEW[恢复布局producer](cdt_odd_restored_zero_layout_lp_20261006.py)首次执行一次，[证书](cdt_odd_restored_zero_layout_lp_20261006.json)用ε1/20给如下严格算术界。表中β区间由[NEW独立区间核验](cdt_odd_double_pole_budget_certificate_verify_20261006.py)及[证书](cdt_odd_double_pole_budget_certificate_verify_20261006.json)固定，π用Machin公式、atan交错级数、log用atanh级数严格有理包围；不把floating orientation作证明。

|s5四重零点布局|rank|safe算术A上界|已证解析β严格区间|
|---|---:|---:|---:|
|B5|n|17.834|(7.642,7.643)|
|B6|2n|35.939|(17.476,17.477)|
|B8|4n|81.249|(43.029,43.030)|

**这组已取得的界没有β>A，不能推出无理性。** A列只是安全上界；比较失败不证明真实算术成本较大，也不排除更好的equilibrium measure、不同整格、不同y*或新布局。Nonzero已补，重零点修复已补，fullprime比较已落成可检验的具体数值门槛。

## R9. 本轮进展、缺口和下一步

本轮完成：旧H9的全prime/形式Gauss算术框架；高阶导数crossing的真实校正；所有固定s≥4可恢复轮廓移动且保留无穷非零的新布局；原布局63/4的精确bound-model损失；三个s5布局的严格费用/衰减比较。没有新的经典特殊值无理性或线性无关性结论，没有外部Lean认证。

下一步优先研究真正能改变n²项的接口：恢复布局的equilibrium能量；不同length/zero/pole比例及未付费的paired-isotropic lattice；或比当前residue-minor模型更强的整格共同content。固定prefactor和纯基变换若同付allplace费用，不能凭表面归一化改变margin。所有旧R0方法的no-go范围继续保持，不扩大成对全部CDT路线的禁止。

根本轮自己NEW数学producer三个，各首次执行一次；不导入、执行或重跑旧及同行producer；其他同行数学producer执行数以各自收据为准。文件来源审计、PDF抽文本和网页检索不是数学producer。最终冻结/独审/来源计数另补主进展报告，goal仍active。
