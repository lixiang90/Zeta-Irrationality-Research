# 第247轮A/C dyadic两源与实际五行模型独立审阅

2026-10-10，B。结论：以下两个最终数学稿在各自明示范围内 **PASS，无必要数学修订**。本人实际FULL读取保存稿及author scopes，独立纸核关键恒等式；数学程序/CAS/Lean/扫描0，没有改作者稿、246/245、main、policy或manifest。

## 实际FULL目标身份

|冻结数学稿|bytes|SHA256|
|---|---:|---|
|research/chi7_dyadic_two_period_source_round247_20261010.md|9308|ed85200e7b75f24d0f7e7ffa523ba16a3196fd199012657567e15f8d90d04017|
|research/dyadic_chi7_eisenstein_source_round247_20261010.md|12786|2cc22522b952f4b9c6587c9ebdf0e25d4a2a078afcf6221ff8dbf6f9b8c6079c|

A scope2396/1c2cf3d8d08366c218bb7ad895364b42d0e30cefc8302d5ae289ebcb77bc98e6、source selection2015/3d1ed360dba0944e67ae6f5075391899fa5f2550ecd4a1786a0f11b2a7a3fc15及C scope5549/a32ac3e0c59c4c876828bc9f34b0c64c35ca8e2d38824bc8deca3724dc9d7ea5也本人FULL读。详细本人primary读域另记本轮packet_review_scope.md，不将作者更广旧稿/文献阅读转记为本人。

## A：全系数、Fricke及所有声明的有限部分

D8的两种完整系数分别为\((e_n-8[2\mid n]e_{n/2})/n^2\)、\((a_n-[2\mid n]a_{n/2})/n^2\)。第二种无额外4分母，chain rule的4已消掉primitive系数的1/4；d_N²覆盖所有素数幂。普通导数的“先截断/先微分”区别正确。

D9先以已付u degree-one及cusp divisor得到Laurent degree bound，再用三系数确定
\[
E_1/f=-7-\frac8{7u}.
\]
不是有限头推无限身份。f的S因子\(i7\sqrt7\tau^3\)给E₀/E₁正确交换；oldform q²的所有三次因子保留，D10正确。两次微分
\(\Theta^2[\tau I(-1/(14\tau))]=h(-1/(14\tau))/(196\tau^3)\)
精确消一次导数项。D6/D7支付两个affine斜率；W₁₄²=id支付常数。因此D11两个完整Fricke身份、D12 eigencombination及D13只有减号fixed-point强制值都通过重算。A₊的Fricke因子与乘积even性也正确，未冒称已付代数坐标或全图。

D14的奇数项贡献\(-7L_3/(8a)\)，减pole后全部项的常数为Y/2；余项统一有界，支配收敛合法。D15 finite rational kernels减pole后统一有界，其β Fourier权重对r↔7−r对称，使用B₂正确。我重算h=1,2的两个有限系数55/2058、−137/2058，得到D16的pole \(\mathfrak gL_3/(8a)\)与119π²/2744。R的residue-periodic求和应使用csc²而非直接B₂；保存稿已正确处理，其非实项的三角恒等式给0。L₃的绝对收敛Euler product正、Gauss sum非零，所以两个额外cusp pole真实存在；同时删除它们的常数组合只能为0。该结论限固定两源/pole方向，没有关闭另加Tate项或完整period projectors。

## C：actual algebraic forcing、rank5与两叶区别

D3的Z是实际eta模单位，native q产品整数；mod2 subgroup给index3。cusp0处u pole2、Z pole1，任意C(u)函数在此valuation为偶数，故Z不在C(u)，prime degree给完整field C(u,Z)。Q下降可按稿内有限未知系数的Q线性系统完成；选择分母非零是避开一个真线性子空间，不需要finite q-fit认证。minimal式给δZ规则及有限5×5 connection；框架行数与实际独立秩保持分开。

同一x=u/(1+7u)坐标下，整数逆级数及δ=x(1−7x)∂x保持完整prefix，不调用N之后的原系数；1,Z,Z²整数，S_g、T_g用固定b d_N²安全清分母。没有把该安全类型当最优联合格。

canonical cusp0的eta身份全部chain constants正确。独立展开h的两个w⁻²项相消，留下h=1/(7w)+O(1)；δ=kϑ、k(0)=−1/2给forcing首项4w/7。normalized方程的n² pivot及所列majorant支付收敛analytic particular。完整齐次basis为A(w²)、A(w²)logw，可由原A、τA和精确Fricke身份核得。因此
\[
\Delta_0 S_g=-2i\sqrt7(Y/2-g)A(w^2)
\]
是整个返回芽身份，而非leading极限。g=Y/2在实际cusp cover填平；x−1/7=−w²+O(w⁴)、首奇项4w/7与Z∼1/(8w)保留，故没有免费base填点。

cusp1/2的实际γ与scaling计算给A∼π/(√7a)、S_g最高log²系数\(-343L_3/(8\sqrt7\pi^3)\ne0\)。holomorphic driver/f的最多simple pole、u的simple pole使normalized forcing analytic；double-zero indicial递推支付完整收敛最高层，不只asymptotic标签。u∞的fiber ramification2+1与degree3一致。同值bad叶存在没有被换成每个合法图必到该叶。

S_g不在meromorphic field block；模该rank3 block的非零cyclic quotient被原不可约order2算子杀，故秩恰2，实际full frame秩5。无需forcing本身cyclic生成全部field。g∈Q下合法type(0,0,0,2,2)给τ32/25；已存完整CDT Theorem2.5.1允许对先验holonomic行使用该较弱threshold。稿内图与strict quotient只是明确待付条件，没有领取capacity、能量、目标无理性或最小LCD。

## 收据边界

此次不重新审A的全部CDT/novelty检索，不继承C所读218–220全章节；新primary仅完整读其所用Loeffler六页text、Stein degeneracy选段，以及已有CDT物理16–20完整选段。采用冻结246明示u divisor/不可约输入并在本轮实际FULL读246源。单源canonical去常数的非D-finite障碍不能外推到相关dyadic差分；本收据不修改B已冻该证明。

两稿均得到可复核的新函数资产，但完整共同图、所有返回叶的关系投影、同对象无限非零及strict预算仍未付。本收据不是新数值定理。保存后实际FULL自读，最终identity另报。
