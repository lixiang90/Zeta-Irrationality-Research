# 第273轮：固定 Abel 来源的差商清头与实际阶乘内容

2026-10-20，`primitive_mechanism_273`。本分工先核 goal 工具为 null、工作树干净，实际读取273任务、STATE、长期goal、271完整对象及272结算/来源证书。只读与纸证；没有 m、prime、参数或 CAS 扫描，未改旧稿和状态账。

数值目标仍为 \(Y=4\beta(5)-3\beta(4)\)，反证范围仍为全部实际 \(Y=u/v\)。固定271的唯一 \(p_i,R_m,M_m,Q_m\)，不改节点、比例或投影。所需最终收益是同一 \(\lambda_mQ_m(Y)\) 的严格负二次率。本分工首命题仅为：是否存在全尺度机制把272完整商部所付 \(d!\) 替换为 \(\exp(O(m))\)，并因此证明实际旧内容，而不凭“可能有大 gcd”重开。取得或否定该机制后交根作宏观决定；本稿不自行重开旧窗口。

**结论：存在这样的完整清头机制。** 原核先按固定阶数不超过3的整数极点作部分分式，再对整数值来源作固定阶差商，得到完整矩阵安全倍数 \(\widehat S_m=\exp(O(m))\)。它消掉旧安全倍数中的阶乘增长，给同一实际旧内容 \(\log g_m\ge12m^2\log m-O(m^2)\)。新安全倍数的剩余本原内容和严格负二次率尚未支付，故没有新无理性定理。

## 1. 不能从整数值直接推商部整数值

即使分母只有一个整数零点，整数值也不被通常多项式除法保留：
\[
 U(q)=\binom q2\in\operatorname{Int}(\mathbf Z),\qquad
 \frac{U(q)}q=\frac{q-1}{2}\notin\operatorname{Int}(\mathbf Z).
\tag{P1}
\]
所以272保留商部费用的警告正确。下述结论付一个明确 LCM 倍数；它不声称有理除法免费。

记 \(d_N=\operatorname{lcm}(1,\ldots,N)\)。对整数 \(a\) 定义多项式算子
\[
 T_aU(q)=\frac{U(q)-U(a)}{q-a}.
\]
若 \(U\in\operatorname{Int}(\mathbf Z)\)、\(\deg U\le N\)，在整数中心a作Newton展开
\(U(q)=\sum_{r\le N}c_r\binom{q-a}{r}\)，\(c_r\in\mathbf Z\)。恒等式
\[
 \frac1{q-a}\binom{q-a}{r}
 =\frac1r\binom{q-a-1}{r-1}\quad(r\ge1)
\]
遂给
\[
 d_N T_aU\in\operatorname{Int}(\mathbf Z),\qquad
 d_N^s T_a^sU\in\operatorname{Int}(\mathbf Z).
\tag{P2}
\]
第二式是有限次迭代，不需要普通导数整性。由归纳或Taylor展开，
\[
 T_a^sU=
 \frac{U(q)-\sum_{j=0}^{s-1}U^{(j)}(a)(q-a)^j/j!}{(q-a)^s}.
\tag{P3}
\]
它恰为 \(U(q)/(q-a)^s\) 的完整多项式商部。

因此若proper有理核只有整数极点且极点阶数至多固定r，
\[
 R(q)=\sum_a\sum_{s=1}^r\frac{c_{s,a}}{(q-a)^s},
 \qquad A c_{s,a}\in\mathbf Z,
\]
则 \(RU\) 的完整多项式商部满足
\[
 A d_N^r\operatorname{Pol}(RU)\in\operatorname{Int}(\mathbf Z).
\tag{P4}
\]
极点数只增加有限和的项数，**不增加差商迭代次数r**。这正是避免按全部极点逐次除法所付巨额费用的原因。

## 2. 同一 Abel 核满足全部假设

沿272的坐标，置
\[
 n=2m-1,\quad d=6m-2,\quad E=2d=12m-4,\quad D=E-3=12m-7,
\]
\[
 q=t+m-\tfrac12,\qquad L_0=d_{4m-3},\qquad C=8L_0^2.
\]
272 H11已证同一 \(f_i(q)=p_i((q+1/2)^2)\) 满足
\[
 Cf_i\in\operatorname{Int}(\mathbf Z),\qquad \deg f_i\le d.
\tag{P5}
\]
所以 \(U_{ij}=C^2 f_if_j\) 是次数至多E的整数值多项式。

原 \(R_m(t)\) 的极点在此坐标恰为
\(a_k=m-k-1\in\mathbf Z\)，\(0\le k\le n\)，阶数至多3；核仍proper，degree为−3。平移斜率为1，所以部分分式系数仍是271的 \(a_{s,k}\)。271 B1、B7给
\[
 2^{6n}a_{3,k}\in\mathbf Z,\qquad
 L_0g_k\in\mathbf Z,\qquad 2L_0^2h_k\in\mathbf Z,
\]
其中 \(a_{2,k}=a_{3,k}g_k\)、\(a_{1,k}=a_{3,k}h_k\)。这些式子覆盖全部k；左节点也可由反射获得。因此
\[
 A_R=2^{6n+1}L_0^2,
 \qquad A_Ra_{s,k}\in\mathbf Z\quad(s=1,2,3).
\tag{P6}
\]
这里使用的是原核的实际中央二项式/调和和公式；没有仅从半整数与整数交错便推断整性。

设 \(H_{ij}\) 是同一 \(F_{ij}=R_mP_iP_j\) 的完整多项式商部。平移不改变proper与polynomial的唯一分解。由P4–P6，
\[
 \boxed{J_mH_{ij}(q)\in\operatorname{Int}(\mathbf Z),\qquad
 J_m=C^2A_Rd_E^3=2^{6n+7}L_0^6d_E^3.}
\tag{P7}
\]
此处 \(H_{ij}(q)\) 表示把原商部写在q坐标中；其次数至多D。P7付整个商部，包含所有系数和交叉项，不只是最高项或一个minor。

三重整数零仍属于271完整移线/投影的证据链；本次商部改进直接使用的是**三重极点的固定阶数**及其已付部分分式分母。并未把三重零当作 \(\operatorname{Int}(\mathbf Z)\) 中可免费相除的因子。

## 3. 半步平移、Euler头、有限头及全部素数幂

次数至多D的整数值多项式半步平移后，由Vandermonde恒等式及
\(4^r\binom{-1/2}{r}\in\mathbf Z\)，乘 \(4^D\) 即仍整数值。原坐标 \(q=t+m-1/2\) 因而给
\[
 J_m4^DH_{ij}(t)\in\operatorname{Int}(\mathbf Z).
\]
Newton微分公式
\[
 \frac d{dt}\binom tr
 =\sum_{j=1}^r\frac{(-1)^{j-1}}j\binom t{r-j}
\]
说明再乘 \(d_E^2\) 清两次微分。交错Abel泛函满足
\(\mathcal E(\binom tr)=(-1)^r/2^{r+1}\)；故保守统一倍数
\[
 J_m4^Dd_E^2 2^{D+1}
 =\boxed{\widehat S_m
 =2^{48m-19}L_0^6d_E^5}
\tag{P8}
\]
清全部 \(\mathcal E(H_{ij}'')\)。P8没有声称2处最优；可按实际二导次数略减常数，但不改变下述指数阶和决策。

同一完整乘积在右半节点 \(0\le k<m\) 的proper主部已由271投影固定为
\(A_{3,k}=a_{3,k}\delta_{ik}\delta_{jk}\)、\(A_{2,k}=3A_{3,k}\)、\(A_{1,k}=0\)；左半节点由反射配对，第二层可改变符号。因而所有proper系数由 \(2^{6n}\) 清整。实际有限调和头为271 A2；其中奇分母至多 \(2n-1=4m-3\)，幂数至多5，所以
\[
 2^{6n}L_0^5
\]
已清全部有限头，包括所有小素数和高次幂。此倍数整除P8：\(48m-19\ge6n\) 对所有 \(m\ge1\) 成立，且 \(L_0^5\mid L_0^6\)。目标矩阵B也由 \(2^{6n}\) 清整。因此对271原来的带符号 \(A_m,B_m\)，严格有
\[
 \boxed{\widehat S_mA_m,\ \widehat S_mB_m\in M_m(\mathbf Z).}
\tag{P9}
\]
无需再乘272的 \(d_{4m}^5\)。P8的逐素数完整赋值是
\[
 v_p(\widehat S_m)=(48m-19){\bf1}_{p=2}
 +6\lfloor\log_p(4m-3)\rfloor
 +5\lfloor\log_p(12m-4)\rfloor.
\tag{P10}
\]
当对应上界小于p时该项为0。此公式是安全倍数本身的赋值，不冒充最小 \(\lambda_m\) 的实际赋值。

## 4. 同一对象的实际旧内容得到全尺度下界

保持271的首一 \(Q_m=\det(A_m+ZB_m)/\det B_m\) 及其最小整数倍数 \(\lambda_m\)。由P9，
\[
 \widehat\Lambda_m=|\det(\widehat S_mB_m)|,
 \qquad \widehat\Lambda_mQ_m\in\mathbf Z[Z],
\]
所以 \(\lambda_m\mid\widehat\Lambda_m\)，特别 \(\lambda_m\le\widehat\Lambda_m\)。原272安全倍数与内容记为
\[
 S_m^{\rm old}=2^{12m+2}(d!)^2L_0^4d_{4m}^5,
 \qquad g_m^{\rm old}=\frac{|\det(S_m^{\rm old}B_m)|}{\lambda_m}.
\]
全部对象未变，因此
\[
 \boxed{g_m^{\rm old}\ge
 \frac{|\det(S_m^{\rm old}B_m)|}{\widehat\Lambda_m}
 =\left(\frac{S_m^{\rm old}}{\widehat S_m}\right)^m.}
\tag{P11}
\]
这是实际内容的保证，不是把源的局部gcd当成完整det内容。由Stirling与 \(\log d_N=O(N)\)，
\[
 \log S_m^{\rm old}=12m\log m+O(m),\qquad
 \log\widehat S_m=O(m),
\]
故
\[
 \boxed{\log g_m^{\rm old}\ge12m^2\log m-O(m^2).}
\tag{P12}
\]
它付掉的是272指定旧清整中人为多付的阶乘部分；不把这笔内容再从 \(\widehat S_m\) 的预算重复扣一次，也不声称新安全族已经本原。

对实际评价，\(\lambda_m\le\widehat S_m^m|\det B_m|\) 给
\[
 |\lambda_mQ_m(Y)|\le\widehat S_m^m\det M_m.
\tag{P13}
\]
结合272.10的既有实处upper及标准 \(\log d_N=N+o(N)\)，可得有限二次率安全上界
\[
 \limsup_{m\to\infty}m^{-2}\log|\lambda_mQ_m(Y)|
 \le 86+48\log2+12\log6>0.
\tag{P14}
\]
P14改变旧 \(O(m^2\log m)\) 的完整安全包络，但不是严格负率。P12也不证明 \(\det M_m\)、\(|Q_m(Y)|\) 的非负二次率，或最优 \(\lambda_m\) 的下界。

## 5. 去重与交付范围

本地定向rg和实际选读242的整数值完整商部处理、270算术稿、271独审及272两稿：242已有不同K5核在有限连续评价点上控制完整商部/Newton费用；270已有另一核的完整头；272 H13–H14已有固定次数微分与Euler整性。固定阶整数节点差商本身是初等恒等式，不宣称首次发现。此次新增适配是：把**本Abel核已付的三层部分分式**与**本Hermite来源的整数值证书**结合，第一次在本证据链中支付P7–P10的完整 \(\exp(O(m))\) 矩阵清整，并由同一首一Q推出P11–P12的实际旧内容。以上去重仅限所述实际读域，不是全仓库或文献穷尽。

本稿提供能够改变原障碍的全尺度实证，供273正式宏观资源比较判断是否给一次有界重开。没有获得严格负本原二次预算；没有改总目标、没有新数值定理，也没有否定全部Abel方法。作者纸证与根独核应分别记账，本稿不把作者自读计为独审。
