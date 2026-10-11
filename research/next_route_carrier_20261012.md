# 下一载体准入：无穷远二次对数关闭旧混合对象的亚纯地图出口

2026-10-12。本文只继续核第259–261轮已经固定的实际对象，并作下一来源的去重与首命题选择。**没有新的数值无理性或线性无关性定理，没有准入地图、素数、参数或 Padé 扫描。** 新结果是一个全叶局部障碍。父代理已独立全文纸核§§1–6，逐式重算(3)–(6)，并核通过Laurent排除、$c=0$边界和polar-Jensen(7)–(8)；该阅读范围不包括其本人尚未完成的§7尾部，也不表示全文上游或Lean认证。旧归档及其冻结身份未修改。

本次读取了 `docs/LESSONS.md`、`docs/RESEARCH_DIRECTIONS.md`，第259轮 mixed-field、mixed12、gate，第260轮 mixed-analytic，第261轮 gate、characteristic、punctures，以及后文列明的既有 Catalan 混合接触稿。`docs/DIRECTIONS.md` 不存在，实际成果地图为 `RESEARCH_DIRECTIONS.md`。没有继承旧作者的原文全文阅读标签；没有重新核全球新颖性、上游证明或 Lean。

## 1. 要判断的具体出口

仍记
$$
 H=A(a+bB_3+cC_3+dB_4),\qquad a,b,c,d\in\mathbb Q,\quad d\ne0,
$$
$$
 r=1-2s,\qquad t=\frac{1-r^4}{9-r^4},\qquad
 p=t(1-t)(1-9t),
$$
$$
 \mathcal D_t=p\partial_t^2+p'\partial_t+3(-1+3t),\qquad
 \mathcal D_tH=b+\frac{c}{1-t}+dR_4,
 \quad R_4=\frac{(3+r^2)^3}{32r(1+r^2)}.
\tag{1}
$$

第261轮已证明在 $r=\pm\sqrt3$ 的每个到达叶都有非零 $z\log^2z$。在固定 $s$ 的全纯地图接口中，这迫使
$$
 \lambda=\log|\phi'(0)|<\log(11/2)<7/4.
\tag{2}
$$
旧标准 literal type 的任意可用有理基底费用至少 $16/9$。第261轮明确没有排除允许 $s=\phi(z)$ 本身有极点的另一接口。

本次先判断这个例外是否真的存在。具体数值出口是 $\xi_\pm=\zeta(2)\pm2G$。其完整有理反证关系分别有 $b=0,c=\pm d\ne0$，所以不能只核 $c=0$ 的方便子类。

## 2. 新首命题：$c\ne0$ 时所有合法亚纯地图都没有极点

**命题。** 对(1)的任意实际到达解，若 $c\ne0$，则在 $s=\infty$ 具有不可由有限分歧或齐次解取消的二次对数芽。因此，若非恒定亚纯 $\phi:(\mathbb D,0)\to(\mathbb P^1,0)$ 使 $H\circ\phi$ 在圆盘上亚纯，$\phi$ 不可能有极点。此时 $\phi$ 实际全纯，(2)仍适用。

### 2.1 完整局部算子

置
$$
 x=1/r,\qquad v=t-1=\frac{8x^4}{1-9x^4},\qquad \theta_x=x\partial_x.
$$
$x$是 $s=\infty$ 的未分歧局部参数；$v$在这里阶4。先直接展开
$$
 p=v(8+17v+9v^2),\qquad p'=8+34v+27v^2,
$$
于是
$$
 v\mathcal D_t=(8+17v+9v^2)\theta_v^2
 +(17v+18v^2)\theta_v+6v+9v^2.
$$
利用 $\theta_v=(1-9x^4)\theta_x/4$，包括微分该系数产生的项，得到准确恒等式
$$
 \boxed{v\mathcal D_t=
 \frac{1-x^4}{2}\theta_x^2
 +\frac{16x^4}{1-9x^4}\theta_x
 +\frac{48x^4(1+3x^4)}{(1-9x^4)^2}.}
\tag{3}
$$
完整右端是
$$
 \boxed{v\mathcal D_tH=-c+
 \frac{8b x^4}{1-9x^4}
 +\frac{d x(1+3x^2)^3}{4(1+x^2)(1-9x^4)}.}
\tag{4}
$$
因此右端在 $x=0$ 解析，常数恰为 $-c$。$a$只改变齐次解，$b$从阶4开始，$d$从阶1开始，不能取消这个常数。不能把 $dR_4$ 的三阶极点误当成同一个 resonance：乘上 $v$以后它恰为阶1。

### 2.2 不依赖渐近的 Laurent 排除

假设 $H$ 在 $x=0$ 是亚纯 Laurent 芽。若其最低非零指数 $n<0$，(3)左边最低项为 $n^2h_n x^n/2$，其余系数均从阶4开始，不可能匹配(4)的解析右端。故没有负次项。

对解析 $H$，(3)左端的常数为0，(4)常数为 $-c\ne0$，仍矛盾。因此这个局部方程没有任何亚纯解。此论证覆盖所有到达解，不需要知道全局连接常数。

### 2.3 全叶二次对数的准确系数

齐次正则解可取 $U(v)=1+O(v)$，故 $U(x)=1+O(x^4)$。重复指数0的齐次另一个解至多有一次 log。以 $H=U Y$ 使用自伴随恒等式，并把 $t$ 导数完整换成 $x$ 导数：
$$
 \left(\frac{pU^2}{v_x}Y_x\right)_x=v_xU\left(b-\frac c v+dR_4\right).
\tag{5}
$$
其中
$$
 \frac{pU^2}{v_x}=2x(1+O(x^4)),\qquad
 v_xU\left(b-\frac c v+dR_4\right)=-\frac{4c}{x}+O(1).
$$
两次积分给
$$
 \boxed{H(x)=-c\,U(x)\log^2x+O(\log x)+O(1).}
\tag{6}
$$
低阶 log 的解析系数取决于到达路径；最高项 $-c$不变。任意两条到达叶之差是齐次解，只有零次和一次 log，不能消掉(6)。若 $x=\kappa w^e(1+O(w))$，$\kappa\ne0,e\ge1$，最高二次 log 系数变为 $-ce^2$，仍非零。即使 $H$某些导数或乘子有有限极点，也不能将无限局部 monodromy 变成亚纯 Laurent 芽。

若 $\phi$在圆盘某点有阶 $e$ 极点，$x(\phi(z))=1/(1-2\phi(z))$在那里有阶 $e$ 零点；(6)立即使 $H\circ\phi$非亚纯。命题得证。

**范围。** 此命题只用固定实际 $H$与 $c\ne0$。它不排除所有亚纯地图定理，也不排除别的周期载体。固定有理可逆换基若所有新行的 pullback 亚纯，其逆矩阵也亚纯，仍可恢复 $H$，所以不能绕过此结论。

## 3. $c=0$ 不能被免费关闭，也没有获得实现准入

当 $c=0$，(4)从阶1开始。(5)右边解析；选择第一积分常数为0，再除以 $2x$乘解析单位，给一个局部解析 particular 解。齐次部分仍可能保留一次 log。

所以此时 **forcing-only** 不足以证明实际 $H$在无穷远的所有叶都坏。局部解析解存在也不意味着实际全局连接常数为0。若要研究 $1,L(2,\chi_{-3}),G$的较小关系类，第一义务是支付实际所有运输叶的这个连接常数；不是直接把无穷远标记为可填点。

即使某条实际叶可在 $s=\infty$ 填入，第260–261轮已付的四个有限必省略点仍为
$$
 s=(1\pm i)/2,\qquad s=(1\pm\sqrt3)/2.
$$
相应球面四穿孔域与原平面四穿孔域的解析尺度不同，旧两点 Landau 界不能直接照搬；本稿也没有算出足以开启判据的新尺度。此分支不是 $\xi_\pm$ 的完整反证类，不可为那两个目标使用。

## 4. 亚纯坐标的极点会支付什么

下面只给直接可证的解析记账，不冒充一个已经建立的新 arithmetic-holonomy 定理。设 $\phi$亚纯于闭单位盘邻域、边界无零极点、$\phi(0)=0$、$\phi'(0)\ne0$。记
$$
 N_\infty(\phi)=\sum_{\phi\text{ 在 }a\text{ 有极点}}e_a\log(1/|a|).
$$
Jensen 对 $\phi(z)/z$给
$$
 \int_{\mathbb T}\log|\phi(z)|\,d\mu(z)+N_\infty(\phi)
 =\log|\phi'(0)|+N_0^*(\phi)\ge\log|\phi'(0)|.
\tag{7}
$$
极点减少未修正的边界平均；极点计数恰把这份减少加回。对固定外变量再将 Jensen 用于 $\phi(z)-\phi(w)$，积分后同样得到
$$
 J(\phi)+2N_\infty(\phi)\ge\log|\phi'(0)|,
 \quad J(\phi)=\int_{\mathbb T^2}\log|\phi(z)-\phi(w)|.
\tag{8}
$$
对角的对数可积奇性用径向极限处理；本稿只主张满足所列边界条件的公式。(8)是自然双变量 corrected energy 的下界，不是声称原CDT判据只需将 numerator 改成该式。

同时，若 source 系数多项式次数不超过 $D$，则 $\phi^j(f_i\circ\phi)$在地图极点 $a$的 pole order 至多 $e_aD+k_{i,a}$。统一清除全部辅助评价式需要支付随 $D$增长的 polar divisor，而不是一个不随 $D$变化的乘子。其 Jensen 权重有 $D N_\infty(\phi)$主项；固定 $f_i$ 极点另有固定项。加入 slopes 或多变量平衡以后，准确常数仍必须由适用定理重建。

因此，“允许极点后裸 $\phi'(0)$可以更大”不足以构成净收益。既不能从旧全纯定理删去全纯条件，也不能保留旧 $J$、分母费用和任意较大的裸导数拼出矛盾。对 $c\ne0$更早已有第2节的完全局部拒绝，不必为该空地图类继续建立polar-budget公式。

本轮[精确双穿孔覆盖界](next_route_cover_bound_20261012.md)进一步给出所有全纯图的 $\lambda<\log3<10/9$。结合第2节，它也适用于当前 $\xi_\pm$完整反证类的任意合法亚纯地图。自然AP标量前缀模型的[独立费用结算](next_route_ap_cost_20261012.md)为 $32/27$；即便将来建立采用该cap及同一 $\lambda-\tau$ 分母的新定理，正分母仍严格不可能。本稿没有把该自然cap写成全部实际评价格费用的下界。

## 5. 由此得到的下一来源准入条件

对 $\xi_\pm$ 来说，改变地图为亚纯、有限覆盖、固定有理 gauge 或可逆 rebasing 均没有解除旧对象的完整坏芽。一个乘子即使在坏点有零，也只是把 $x^k\log^2x$的指数改变，仍保留无限 monodromy。增加旧纯行只会继续支付已审过的域与分母成本。

真正值得比较的新来源必须交付以下首证书：**在完整反证关系类上，其实际延拓的最高 resonance 类能够在至少一个当前决定性奇点消失，同时原来的指定数值关系仍且仅仍触发一个完整坏芽的消失。** 若继续保留这个二阶 period 模块，首命题可以具体写成：

> 构造真正不同的全局 Eichler/相对周期扩张 $A B_\xi$，识别 canonical cusp 的周期为指定 $\xi_\pm$；在两个 $t=\infty$实 fiber 及允许作为地图极点的 $s=\infty$ fiber，证明所需完整反证类的 resonance 常数为0，并支付剩余一次log的实际连接数据。

仅加一个有理 exact correction 不会改变上述局部 extension obstruction；若新函数仍可经完整有理微分系统恢复旧 $H$，则恢复运算会重新迫出它的域限制。source条件的满足、数值period身份和全处费用都须给实际证书，本稿没有指定一个已满足这些要求的新模形式。**目前没有足够证据准入另一导子或新的参数窗口。**

## 6. 直接 Catalan $M/Z$ 池的去重、指定目标与准确 first gate

这个对象与第259轮模载体不同，可以比较；但“改变零端接触以保留 $\zeta(2)+2G$”本身已经在旧混合contact稿中研究，不能算作本轮发现的新构造。

既有实际矩分解是
$$
 F_j(P,D)=F_j^0(P,D)+4G C_j(P)
   +\frac{\pi^2}{4}(H_j(P)-D_j),
$$
其中 $C_j$ 是无穷远反向Toeplitz系数、$H_j=[t^j]tP/f$ 是零端系数。目标 $\alpha G+\beta\pi^2=u\in\mathbb Q$的精确接触条件是
$$
 H_j-D_j=\mu C_j,\qquad \mu=16\beta/\alpha.
$$
对 $\xi_+=\zeta(2)+2G=2G+\pi^2/6$，恰有 $\mu=4/3$。$\xi_-$对应 $\mu=-4/3$。旧原48N方阵在任意非零 $\mu$下因为合规行空间维数不足而恒为零：raw mixed kernel 为 $36N-1$，filtered-only 为 $40N-1$。不能保留原48N规模而只改 $D$。

旧稿已经给出自洽的缩小配置：$n=44N-1$列、$44N$行池，含 $36N-1$ Jacobi 接触行与 $8N+1$纯D尾行。其完整实际有理关系pencil为
$$
 \mathsf F(\mu,\rho)=
 \begin{pmatrix}R+\mu U+\rho C\\T\end{pmatrix},
 \qquad \rho=4u/\alpha.
\tag{9}
$$
因此正目标 $\xi_+\in\mathbb Q$时应核 **指定** $\mu=4/3,\rho=2\xi_+$，不是 generic $(\mu,\rho)$。旧 all-N second-kind jet rank 给了非零 polynomial maximal minor，实际moment Schur稿给了正尾块与准确的秩条件；它们没有证明每个指定有理关系点都非零，也没有证明新的完整费用被实能量压过。多项式pairs的独立性不替代这一步。

**允许的准确第一关：**在(9)指定 $\mu=4/3$上，证明对每个固定 $\rho\in\mathbb Q\cap(6,8)$存在一个无界 $N$子列，其完整实际输出秩为 $44N-1$。这个有界区间覆盖完整反证情形：$3<\pi<22/7$及Catalan交错级数的 $8/9<G<1$给 $6<2\xi_+<8$。对全部有理 $\rho$成立是更强结果，并非当前目标必须承担的额外义务。可先尝试证明Schur异常谱避开这个区间，或寻找新的全尺度素数机制。generic polynomial 非零、有限 $N$行列式和未知 $\rho$的数值拟合均不足。若改用多个minor，其共同整数预算及实际解析minor界也必须一起进入后续反证。

即使这一关通过，仍要重新付混合Jacobi行的完整整数格、全部素数幂、行尺度与实侧净指数。原纯Catalan Chebyshev valuation lemma、Gram正性和原行列式能量数字不能直接移给新接触行。旧两端contact稿的 dyadic清整只保证一个显式整数子格，没有证明完整本原指数；旧 real-place note也没有得出有利的全 leading gap。

这个 first gate 因而是**旧混合矩资产中的未闭合接口**，不是重开χ−8或给旧构造改名。是否值得投入，应由可望同时改变非零和净费用的新机制决定。若只重复建立 $\mu=4/3$接触恒等式，下一步选择质量没有改善。

## 7. 结算及来源

本轮可保留的新资产是(3)–(6)：$c\ne0$时无穷远的全叶强制二次对数，及“亚纯地图必无极点”的准确范围。它把第261轮未覆盖的一条形式出口在 $\xi_\pm$完整反证类上关闭。它没有给出新 arithmetic-holonomy 费用，没有证明数值目标无理，也没有关闭 $c=0$ 或真正不同的周期源。

本次只写本文。数学producer、CAS、有限n数值、prime/parameter/map扫描、旧脚本、Lean、archive及外Git写均未执行。全部公式为纸面代入、Jensen及局部积分推导。新结果的独立审阅范围见稿头，本轮后续总review可另记，不沿用旧PASS。

直接使用的本地依据：

- [第259轮完整forcing场与实际秩](source_selection_mixed_field_round259_20261010.md)，尤其F6、F8–F10。
- [第259轮实际关系跳变](source_selection_mixed12_round259_20261010.md)及[来源gate](source_selection_gate_round259_20261010.md)。
- [第260轮全部到达叶的复两点障碍](global_review_mixed_analytic_round260_20261010.md)。
- [第261轮联合gate](refined_budget_gate_round261_20261010.md)、[characteristic稿](refined_budget_characteristic_round261_20261010.md)、[punctures稿](refined_budget_punctures_round261_20261010.md)。
- 固定CDT v2原件的既有文本节选：`literature/refined_budget_round261_20261010/characteristic_cdt_v2_physical089_096.txt`，用于核当前定理明确要求 $\phi$全纯；没有从该文本领取未经重建的亚纯版本。
- [两端接触支持障碍与缩小kernel](catalan_mixed_two_end_contact_support_lemma_20261007.md)、[实际moment与Schur条件](catalan_mixed_actual_moment_schur_lemma_20261007.md)、[all-N second-kind jet rank](catalan_mixed_second_kind_jet_rank_20261007.md)、[joint Cauchy与corner接口](catalan_mixed_joint_cauchy_corner_interface_20261007.md)，本次核读了其前述定义、精确分解及定理范围；未声称重新全文复核全部后段估计。

## 8. 本人对本轮覆盖稿的独立复核

本人另全文读了 [next_route_cover_bound_20261012.md](next_route_cover_bound_20261012.md)，并独立打开 [ASVV固定v2原件](https://arxiv.org/pdf/0903.1761v2)的可读网页文本，实际核其 introduction 的密度式、(2.1)曲率规范、(3.1)parameter积分定义及Theorem4.7和证明。没有只依据父代理消息，也没有领取父代理的原文读域。尝试网页截图物理1、2、6页均返回cache miss，未将失败截图计为成功视觉核验；原件的分式系数在文本中可直接核对。

原件曲率为−4，单位盘原点密度为1；$\alpha=0,a=1/2$确实给 $\rho(x)=\pi/[8x(1-x)K(x)K(1-x)]$。因此覆盖稿(1)的factor8、仿射因子 $\sqrt3$及最终 $4\sqrt3/(3\pi)$全部正确。Cauchy–Schwarz积分给 $K(m)^2\le\pi^2/(4\sqrt{1-m})$，两参数相乘后恰得 $\pi6^{1/4}/\sqrt3<44/15<3$；$e^{10/9}$的0–4阶和 $59453/19683>3$也逐项纸核正确。由此(3)的严格界及(4)相对 $32/27$的负分母均通过。

本人核读了AP费用稿的当前全文以确认 $32/27$所指自然balanced标量前缀cap及其有限范围；未重新阅读全部原CDT评价高度证明。覆盖稿将cap计算与未来新定理分开、将正分母门槛与秩矛盾門槛分开、并只把本稿的亚纯扩展用于 $c\ne0$，范围陈述正确。未发现阻断性问题；该复核不构成全球数值目标新颖性审查。
