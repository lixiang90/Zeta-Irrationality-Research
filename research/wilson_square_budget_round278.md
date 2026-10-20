# 第278轮：双quarter完整费用、实际共同内容与到期裁决

2026-10-20，完成[278一轮任务](wilson_square_budget_charter_round278_20261020.md)。根核实际goal为active、工作树干净、修订18权威账，恢复AGENTS、长期goal、277正式决定、同一W1–W15及独审。上一goal turn完成新来源证明、独审和云端提交，分类为progress；数值总goal仍未实现。

**结论：已对原W9支付全素数幂、伴随商、外a幂、全部前缀及双镜像，得到完整线性安全整数对和精确最小分母桥；安全净率为8+12log2>0。足额完整共同内容未付，一轮窗口按期结束，转279全路线比较。** 该正率不是实际最优分母的下界，不排除所有成功子列。

## 1. 固定实际对象及全部反证

数值目标保持指定 \(L=L(2,\chi_{-8})\)。对象仍为[277 W9](wilson_square_source_round277.md)唯一两quarter、平移n=degree n、原连续双Hahn(1,1,1)测度及实际有理r_n；不换theta、degree比例或目标。

全部实际反证为L=u/v，u∈Z、v>0、gcd=1。若r_n=A_n/d_n既约，则
\[
0<|vd_n(L-r_n)|=|ud_n-vA_n|\in\mathbf Z.
\]
277的全n非零和精确裸率 \(\log|L-r_n|/n\to-2\log\rho\)、\(\rho=(11+5\sqrt5)/2\)经[本轮独立重建I278.1–8](wilson_independent_round278.md)再次支付；全部n!归一、真实权、双镜像同号、统一Stirling及Jensen无遗漏。

因此在预定同一无界子列上，严格负线性净指数等价于 \(\limsup\log d_n/n<2\log\rho\)。临界次指数或其它证明方法没有被此判据排除。

## 2. 伴随多项式和实际二处

[完整算术A278.1–6](wilson_arithmetic_round278.md)及[独立P1–P4](wilson_primitive_round278.md)从monic norm给整数递推
\[
P_{n+1}=(y-\beta_n)P_n-\gamma_nP_{n-1},\quad
\beta_n=(n+1)(2n+3),\quad\gamma_n=n(n+1)^3.
\]
同一差商伴随的两倍V_n也整，V₀=0、V₁=1、同递推。原商精确为 \(-V_n(-a^2)/(2P_n(-a^2))\)，不能丢负号或换另一测度。

对b=4n+1、4n+3，a=b/4、n≥1，W4的k=n项在二处唯一最低，故
\[
\nu_n=4n+2v_2((n+1)!),\quad
v_2q_n(b/4)=-\nu_n,\quad
v_2S_n(b/4)=3-\nu_n.
\]
同一S/q的二赋值为3。再保留全部外a幂，每个U_n(b/4)/16虽为二处半整数，两镜像之和却二处整；完整前缀本来二处整。因此**实际d_n为奇数**。n=0可直接由W9验证，不用于后续n≥1的LCM公式。

q的所有奇处同时由恒等式
\[
a^2q_n(a)=\sum_{k=0}^n\binom nk\binom a{k+1}\binom{a+k}{k+1}
\]
支付：a在每个奇p的Z_p中，泛化二项式p整。于是
\[
B_{n,b}=2^{\nu_n}b^2q_n(b/4)\in2\mathbf Z+1,\qquad
\log B_{n,b}/n\to6\log2+\log\rho.
\]
这只是完整输出中的一个来源整数大小，不是实际d_n下界。

## 3. 全部有理头：Newton矩及全素数幂LCM平方

本轮关键机制由根提出，算术/独审两作者分别从定义重建。令
\[
\mathcal R_k(y)=\prod_{h=1}^k(h^2+y)/(k!)^2,\quad
T_n=\sum_{k=0}^n(-1)^k\binom nk\mathcal R_k/(k+1)^2.
\]
正交性及二项反演给 \(\mu(\mathcal R_k)=(k+1)^2/2\)。同一伴随差商因此是
\[
\mathcal A_k(z)=\tfrac12\sum_{j=1}^k
\prod_{h=j+1}^k(z+h^2)/h^2,\qquad
S_n(a)=-\sum_{k=1}^n(-1)^k\binom nk\mathcal A_k(-a^2)/(k+1)^2.
\]
在z=−a²时，乘积精确化为
\[
(-1)^{k-j}
\frac{\binom{a-j-1}{k-j}\binom{a+k}{k-j}}{\binom kj^2}.
\]
泛化二项式在全部奇p整；且 \((k+1)\binom kj\mid d_{k+1}\)，其中d_m=lcm(1,…,m)。逐p^e的Legendre计数每层是0或1，p^e>k+1时0，所以包含所有高次幂，不仅模p。故
\[
u_n=(\operatorname{odd}d_{n+1})^2,\qquad
C_{n,b}=2^{\nu_n-3}u_nS_n(b/4)\in2\mathbf Z+1.
\]
这支付整个伴随头，不按单项Bernoulli分母或阶乘gross收费。实际商为 \(S/q=8b^2C/(u_nB)\)，从而
\[
U_n(b/4)/16=(b+4)/(2b^3)-32C_{n,b}/(b\,u_nB_{n,b}).
\]
原前缀是 \(\mathcal P_n=\sum_{k<n}(-1)^k[(4k+1)^{-2}+(4k+3)^{-2}]\)，没有删除有限头。

## 4. 完整奇整数对、精确净率及尚未付的信用

取
\[
\ell_n=(\operatorname{odd}d_{4n-1})^2,\qquad
M_n=\ell_n(4n+1)^3(4n+3)^3B_{n,4n+1}B_{n,4n+3}>0.
\]
u_n整除ℓ_n，完整前缀分母整除ℓ_n。定义
\[
X_{n,b}=M_n(b+4)/b^3-64M_nC_{n,b}/(b\,u_nB_{n,b})\in2\mathbf Z+1,
\]
\[
N_n=M_n\mathcal P_n+\tfrac{(-1)^n}{2}
(X_{n,4n+1}+X_{n,4n+3})\in\mathbf Z.
\]
两X之和偶；这同时支付奇处、实际二处取消、两个外a⁻³和全部前缀。精确
\[
r_n=N_n/M_n,\quad g_n=\gcd(M_n,N_n),\quad
d_n=M_n/g_n,\quad A_n=N_n/g_n.
\tag{278.1}
\]
完整共同内容含全部跨镜像、跨prefix和高次幂抵消，不能重复领取局部信用。

LCM渐近和原q精确率给
\[
\log M_n/n\to8+12\log2+2\log\rho,\qquad
\boxed{\log(M_n|L-r_n|)/n\to\kappa:=8+12\log2>0.}
\tag{278.2}
\]
因此任一预定无界子列上精确有
\[
\boxed{\limsup\frac{\log(d_n|L-r_n|)}n
=\kappa-\liminf\frac{\log g_n}n.}
\tag{278.3}
\]
本严格负线性接口的足额完整信用恰为 \(\liminf\log g_n/n>\kappa\)，目前没有此项。278.2证明指定安全输出增长，**不证明最小d_n失败**；278.3也没有将一个未证g当作已付净收益。

## 5. 局部限制、有限诊断与独审

Casoratian
\[
V_nP_{n-1}-V_{n-1}P_n=(n-1)!(n!)^3
\]
控制单镜像的大素数共同内容；规范后可得单镜像gcd(B,C)的upper率≤2。但两镜像共同素数及前缀抵消仍未控制。对p>4n+3，仅在两镜像Q赋值不等时，实际d的赋值等于较大值；赋值相等时不能删掉可能取消。详[本原稿P6–P8及P6a/P6b](wilson_primitive_round278.md)。根独核原恒等式、单镜像估值和以上限定量词，不从gross resultant或单q构造全d的lower。

本原作者执行前说明规范用途后，仅作一次固定n=2精确诊断：P₂=y²−13y+22、V₂=y−10，实际r₂=763653576728237/717219908922825，分母奇。根用Fraction核对已有表格与r₂等式；两位审查者纸核P₂/V₂及有理头规范，不冒称各自重算最终大分数。未重跑producer或增加尺度，该样本没有推广为g的总体率。

根全文核[算术A278.1–23](wilson_arithmetic_round278.md)、[本原P1–P12及增补](wilson_primitive_round278.md)、[独审I278.1–22及交叉读域](wilson_independent_round278.md)。另两作者实际全文独审算术稿；解析作者重建真实非零/率，并独核本原Casoratian增补。作者不自作独审，工具/资产检查不认证数学。

## 6. 到期结算及宏观控制

278一完成轮按期关闭。已付首份完整线性安全费用和精确最小分母桥；未付足额g增长、负净预算或新无理性定理。**feasibility_progress=false，连续未改善2，numeric_admission=false。** 不把本轮临时粗factorial桥设为跨轮已审基线，再用首次安全正upper制造进展重置；局部信用和新文档也不重置计数。

唯一下一动作为[279全路线比较](source_gate_charter_round279_20261020.md)。该具体source若重开，须有同一完整对的足额全尺度内容、实际费用或真实余项机制改变净预算；仅同q的更多局部估值、扩大已关闭参数、固定n2或改名不够。其它χ−8来源的内容不自动移交；没有宣布所有该值/方法不可能。

本轮另发现状态工具曾额外要求“正式复盘后至少两个完成轮”才触发提前复盘，会把277计数1、278计数2误显示为无需复盘。已按协议改为：有新完成轮且连续未改善达到2即触发，正式复盘本身不清计数；同一已处理快照不反复触发。新增三种计数情形的恢复测试，属于组织修复，不算数学进展或新轮。原计数与纠错链保留。

本轮未扩展n/prime/参数扫描、未运行历史producer或Lean构建，也无新一手定理输入或新颖性穷尽声明。文献、形式化与原冻结清单保留；状态账/STATE更新后同步已授权仓库，总goal保持active。
