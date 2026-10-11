# 第230轮 Root 完整残差接口独立纸审

2026-10-08，A。数学条件与边界降维 **PASS**。本收据不把8个有限案例升级为无限子族，未运行数学程序，未改目标。

## 1. 实际读取身份与范围

实际FULL读取 Root 最终正文 q2_residue_nonzero_gate_round230_20261008.md：3866B，SHA256 38ddebf4c572452af2679f04bd31e215d1d021fc063ace77d318bf5e9e56aa37（较此前3546B版新增完整多项式局部LCD段，最终版再FULL读取）；producer probe_q2_residue_round230_20261008.py：3429B，SHA256 05cb7ad4f351bbe3f340e549080aa6901f1ac805e3fa40e05b0cca2e8eb024bf；以及229分母稿全文。JSON35763B，SHA256 f28f4af112017b13e4bdd8b675ae2c3b7a1b86fde1868956b6363a5101ff8b24，只读metadata、完整8行rank表和d1,p5的全部三块矩阵；**未FULL打印/逐项重算全部JSON**。Root报告唯一producer运行exit0；本独审复跑0。

## 2. 条件引理与有限表

在L<p≤2(L−m)+1，A/B均p整且a至多简单p极点。逐个下行乘p确给p^mW(g)∈Z_(p)，gA项模p消失。若完整栈[B;paᵀ]的模p行列式为单位，便有v_pW(g)=−m，结论对全部g∈Z_(p)同时成立。若有无界d,p子族，固定有理Θ的分母只排除有限个p；该条件足以支付相应无限非零。**无界子族仍未付。**

新增完整多项式陈述 **PASS**：在Z_(p)[X]中直接有p^mW(X)=det[B;pXA+paᵀ]。其约化为同一残差常数。若该常数非零，则v_p([X⁰]W)=−m；按下行多线性，j次项须选j个pXA行，更强地v_p([X^j]W)≥j−m（零系数照v_p(0)=∞）。故非恒定系数至少少一阶，全部系数的最小局部分母恰p^m。该结论不声称其它素数的最优费用或全局严格净收益。

producer的尾递推、独立有限和、全池s/r方向、全部有限头、Fraction模p整性检查和有限域Gauss消元都与正文相符。JSON八行rank完全对应正文表。首案例手核：B的左2×2块det=4，paᵀ右2×2块det=2，所以完整det=3 (mod5)，非零；E模p退化不能妨碍该栈满秩。

一个运行措辞限定：producer的status=PASS是无条件打印，未assert full==required_rank。它确有尾公式、素数/窗口、整性及零列下界assert；8案例满秩由**实际rank输出及正确消元算法**支付，不能说PASS标签单独断言了该性质。本独审未另算其它7例，也不要求为此重跑或改冻结producer。

## 3. p=4d+1边界的独立公式核对

设k=2d，γ=2(−1)^k∈F_p^×。偶矩递推和binom(p−1,k)≡(−1)^k给

\[
p\,m_{2(k+j)}\equiv\gamma c_j\pmod p,\qquad0\le j\le d.
\]

对l=k+t、1≤t≤d+1，令q_t=pQ_l、r_t=pR_l，模p递推为

\[
(2t-1)q_t=(2t-2)q_{t-1}+\gamma c_{t-1},\quad
(2t-1)r_t=(2t-2)r_{t-1}+q_{t-1}-q_t.
\]

初值q_0=r_0=0。逐项代入（或用C(z)=(1−z)^(−1/2)的系数卷积）得到

\[
q_t=\gamma\sum_{j=0}^{t-1}\frac{c_j}{2(t-j)-1},
\qquad
r_t=-\gamma\sum_{j=0}^{t-1}\frac{c_j}{[2(t-j)-1]^2}.
\]

所有这些分母模p为单位。将后一式与a的完整奇v头项相减，正、负t两种范围都合成

\[
(pa)_{m+u,s}
=-\gamma\sum_{j=0}^{u}
\frac{c_j}{[2(d-s-u+j)-1]^2},\qquad0≤u,s≤d.        \tag{R}
\]

前m个源列的pa为0。令C_(u,v)=c_(u−v)（u≥v，否则0），其对角为1；(R)就是−γCV，其中V_(u,s)=1/[2(d−s−u)−1]²。因此原残差栈非零，恰等价于正文列出的B初始Hankel块与V两个有限域行列式非零。V的全部整数分母为非零奇数、绝对值<p。转置方向不改变非零性；卷积只移除单位标量及detC=1。

该降维正确，没有调用普通Cauchy公式处理平方，也未由有理数域非零推出F_p非零。p≡1 mod4无限确能提供无界候选，但**这两个有限域引理仍缺**。正文保留的非零/整模型严格收益/数值定理边界准确，无必要数学修正。

本收据保存后实际FULL自读；本任务数学运行0，文档JSON选取仅读取，不执行producer、CAS或扫描。
