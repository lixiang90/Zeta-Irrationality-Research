# 第265轮正式来源选择：指定组合的共同系数向量

2026-10-13。上一goal turn为progress：264完成真实index下界、leading-box桥和稳定窗口停止决定。本轮按两轮停滞规则提前正式比较全路线。**没有新的数值无理性定理，也没有候选通过完整净预算准入。** 下一步选择不同原生来源的一轮系数向量核查，不恢复已闭Frobenius或旧参数窗口。

## 1. 全路线的最终接口与机会成本

| 来源 | 最短未付接口 | 本轮资源决定 |
| --- | --- | --- |
| ζ(5)上游基线 | 不是新数值目标 | 保留形式化与可迁移机制 |
| ζ(7)旧Gram/整数格 | 同参数本原负指数、实际无界非零 | 不扩大已闭参数；新wheel插入另核下文 |
| K5固定3:1组合 | 完整内容及实能量；当前安全费用1511/60仍不足 | 不借scalar超几何定理重跑K5 |
| logmoment/Markov | actual根分母异常内容，或正测度Padé的完整成本 | 无新的已匹配内容身份，不扩精度 |
| 已知CDT周期推论 | 尚不能隔离新的指定数值 | 不替代goal |
| 奇权/CM/Fricke | 背景恢复、全叶域、同对象成本 | 旧停止范围保留 |
| χ−8 RV/native | actual无限非零和严格净预算 | 不由另一来源的失败自动恢复 |
| mixed标准/标量AP | 已有准确限定障碍 | 关闭 |
| mixed actual整数格 | index-only已排除；intrinsic负graded仍缺 | 263–264窗口保持关闭；下文否定两个免费转接 |
| 新原生来源 | 固定目标的全系数模型及实际预算 | 比较Catalan滤波、wheel、Mellin与M₀,₈；只选择一项源核查 |

此表依据[成果地图](../docs/RESEARCH_DIRECTIONS.md)、[263复盘](research_global_review_round263_20261013.md)及[264结算](research_round264_report_20261013.md)的现行范围。未重跑全部历史producer。K5、CM、原M₀,₁₀相对类与下文M₀,₈不是同一来源，费用或非零不能跨行移用。

## 2. Catalan自然滤波：保守清整确实增长

[Eskandari v1](https://arxiv.org/pdf/2609.26354v1)的实际对象为
$$
 \widetilde J_{n,m}=\int_{[0,1]^2}\psi^n(1-16\psi)^m d\nu
 =\widetilde u_{n,m}G-\widetilde v_{n,m},
 \quad \psi=\frac{xy(1-x)(1-y)}{1-xy},
$$
$$
 d\nu=\frac{dx\,dy}{\sqrt{x(1-y)}(1-xy)},\quad
 D_{n,m}=16^n d_{2n+2m}^{\,2},\quad d_N=\operatorname{lcm}(1,\ldots,N).
$$
原式(2.9)清除完整两坐标；$16^m$ 的滤波节省已经包含在这个模型中。总质量为 $8G<\infty$。这里只讨论原论文选用的偶 $m$、$m/n\to\alpha\in[0,\infty)$。

最大值 $c=\theta^{-5}$、$\theta=(1+\sqrt5)/2$ 在 $x=y=\theta^{-1}$ 取得；沿对角线 $\psi=u^2(1-u)/(1+u)$ 遍历 $[0,c]$。内部正密度保证每个非零值附近都有正测度质量。对 $\log t+\alpha\log|1-16t|$，左区间临界点为 $1/[16(1+\alpha)]$，右区间严格递增。故sup为
$$
 M(\alpha)=\max\left\{
 \frac{\alpha^\alpha}{16(1+\alpha)^{1+\alpha}},\quad
 c(16c-1)^\alpha\right\},\qquad0^0=1.
$$
偶 $m$ 没有符号抵消。在一个最大点的正质量邻域取下界，再缩邻域，与总质量乘sup的上界相合，得到原件upper的加强：
$$
 \lim\frac1n\log\widetilde J_{n,m}=\log M(\alpha).
$$
最大点避开 $0$ 和 $1/16$；$\alpha=0$ 可用 $c$ 附近，因此不漏掉 $m=o(n)$。由PNT，实际自然清整指数为
$$
 \delta(\alpha)=\log16+4(1+\alpha)+\log M(\alpha)
 \ge4(1+\alpha)+\alpha\log\alpha-(1+\alpha)\log(1+\alpha).
$$
右侧二阶导数为 $1/[\alpha(1+\alpha)]$，在 $\alpha=1/(e^4-1)$ 取全域最小值 $\log(e^4-1)>0$。因此这个整个偶滤波/有限比率域的**自然清整形式实际增长**，非failed upper。额外本原gcd及其他signed滤波不在排除范围；若通过gcd救济，须在拟用无界子列上重新支付实际指数。

该源两坐标仅为 $1,G$，$\zeta(2)\pm2G\in\mathbb Q$ 并不使其评价有理。原自然滤波已在本库[内容研究](odd_zeta_content_geometry_20261004.md)登记；几何新标签或另计 $16^m$ 不提供新准入。Viola–Marcovecchio的不同contour/group摘要尚缺完整target-vector预算，不据两页摘要恢复优化。

## 3. 原生wheel的增长插入：完整投影和收敛均失败

[Brown–Schnetz v3](https://arxiv.org/html/2402.06757v3)给W₇的正密度
$$
 d\mu=26(\Psi^{-2}+60S\Psi^{-3}+360S^2\Psi^{-4})|\Omega|,
 \quad \int d\mu=24024\zeta(7).
$$
固定唯一自然插入 $f=S/\Psi$。设 $J_j=\int S^j\Psi^{-j-2}|\Omega|$。原Theorem62及归一化给，对 $0\le j\le4$，
$$
 J_j=\frac{924}{(j+1)(2j+1)!}
 \sum_{r\ge1}\frac{\prod_{\ell=1}^j(r^2-\ell^2)}{r^{11}}.
$$
代入 $M_m=26(J_m+60J_{m+1}+360J_{m+2})$，逐项多项式展开得
$$
 M_1=143(3\zeta(5)-14\zeta(7)+21\zeta(9)-10\zeta(11)),
$$
$$
 M_2=\frac{143}{30}(\zeta(3)-15\zeta(5)+77\zeta(7)-155\zeta(9)+92\zeta(11)).
$$
两个nuisance坐标的子式 $21\cdot92-(-10)(-155)=382\ne0$。所以在这个明确**系数消元模型**中，degree≤2 polynomial insertion消掉ζ9、ζ11后只能退回constant $M_0$；不假设这些数值有理线性无关。

无界Gram另有直接收敛障碍。七个rim同时缩小为 $\rho$，spokes留在固定正box，轮矩阵为一个秩6的正cycle Laplacian加正 $O(\rho)$ 对角项，故 $\Psi\asymp\rho$、$S\asymp1$。径向volume为 $\rho^6d\rho$，$M_m$的最高正项为
$$
 C\int_0^\varepsilon\rho^{2-m}\,d\rho.
$$
因此 $M_3$ 起发散。所有degree≥3 polynomial insertion亦不能通过抵消较低degree来恢复绝对收敛。这个插入不准入；不否定有界插入、其他wheel或新增相对边界。旧矩阵平移的全叶障碍已在[独立旧证据](cdt_wheel7_rational_deformation_germ_obstruction_20261007.md)保存。

Brown2026的多参数Mellin criterion本身是真方法，但period ambient维数至少二不隔离ζ7；需要同来源完整投影和transfinite预算，不能用原M₀,₁₀或wheel nuisance代替目标。[一手入口](https://arxiv.org/abs/2604.20741v1)

## 4. 当前intrinsic minor：两个免费内容转接不成立

沿用mixed实际 $g_{i,k}=s^kf_i$、$f=(1,J,\theta J)$、$M=3(D+1)$，实际jumps $V_D=\{v_0<\cdots<v_{M-1}\}$。完整differential Wronskian有自含恒等式
$$
 [s^{\nu_D}]\det(\partial_s^r g_{i,k})
 =\prod_{i<j}(v_j-v_i)\det T_{V_D},\quad
 \nu_D=\sum v_j-\binom M2=O(D).
$$
证明：Taylor/Cauchy–Binet展开中，greedy row flag使任何非零row basis逐个不小于 $v_j$，最低总和只由 $V_D$ 给出；falling factorial行列式正是Vandermonde。零估计还给 $v_j-j=O(1)$，所以Vandermonde除回 $\prod_{r<M}r!$ 后只差 $\exp(O(D\log D))$，不能领取导数factorials为新内容。

Abel只控制基本周期解的Wronskian，不控制这些多项式乘子分量列。仅 $D=0$ 已有 $\det T_{\{0,1,2\}}=j_1j_2$，随齐次初值 $a$ 变化，而forcing和基本Abel恒等式不变；这拒绝直接转接，不提供负graded信用。

另一个直接positive Stieltjes猜想也可反证。规范 $d=1,c=\epsilon=\pm1$、$a=-\epsilon\zeta(2)/4-G/2$，清整常数 $C_0>0$。由[实际算子](source_selection_mixed_field_round259_20261010.md) F8及 $t(s)=s-4s^2+11s^3+\cdots$，递推得
$$
 j_1/C_0=3a+\epsilon+1,\quad j_2/C_0=3a+2\epsilon+2,\quad
 j_3/C_0=6a+(10\epsilon+17)/9.
$$
只用 $3/2<\zeta(2)<7/4$、$8/9<G<1$，即得ε+时 $j_1<0<j_2$，ε−时 $j_1=j_2<0<j_3$。故不存在非零实数b、常数c及 $[0,\infty)$ 上正测度μ，使 $bJ(s)+c=\int d\mu(x)/(1-sx)$ 成为native芽恒等式。这里仅排除同号Taylor正矩约定；这些符号不排除 $1+sx$ 约定、其他支持或signed/complex/Nikishin新结构。

以上是新可核边界，而非满足[264负graded债务](joint_budget_bridge_round264.md)的新机制；不重开当前mixed窗口。

## 5. 更直接的不同来源：M₀,₈的固定3:1投影

[Brown–Zudilin v3](https://arxiv.org/pdf/2210.03391v3)的canonical两部分满足
$$
 I_n=2I'_n+4\zeta(2)I''_n,\quad I'_n=Q_n\zeta(5)-P_n,\quad
 I''_n=Q_n\zeta(3)-\widehat P_n.
$$
因此对固定目标 $X=3\zeta(3)+\zeta(5)$，有实际两坐标
$$
 E_n=I'_n+3I''_n=Q_nX-R_n,\quad R_n=P_n+3\widehat P_n.
 \tag{B1}
$$
这是原文可容许八参数 $I(\mathbf a)$ 族的精确投影，不是数值拟合。它不等于K5 rational kernel或原M₀,₁₀十一通道，也不靠ζ3、ζ5分别无理推出X无理。

固定原文§11参数 $a=(8,16,10,15,12,16,18,13)$；对应
$$
 p=(15,14,16,29,18,13,12)n,\quad q=(15,12,10,8,16)n.
$$
原PDF式(17)的binomial双和支持为 $16n\le k_1\le28n$、$18n\le k_2\le26n$，所有summands正、外符号 $(-1)^n$。故此归一化 $Q_n\in\mathbb Z\setminus\{0\}$；费用必须使用 $\log|Q_n|$，换符号须同时换整套向量。

**正性和精度不可借。** $I'_n$ 是Betti行替换，不是已付的正积分。对称族已有交错符号公式，不能从 $I_n>0$ 宣布投影全n正。代数上
$$
 E_n=\left(1-\frac3{2\zeta(2)}\right)I'_n+rac3{4\zeta(2)}I_n.
 \tag{B2}
$$
若采用原文§11报告的两实际渐近率 $-31.55296934\ldots$、$-66.05784567\ldots$，则 $I_n/I'_n\to0$、$E_n/I'_n\to1-3/(2\zeta(2))>0$。于是实际E最终非零且保持较慢的第一率；这是**以上述asymptotic connection为输入的条件结算**，本轮未独立认证其区间或证明。它只支付实际目标处非零；不声称任意有理q处无条件非零。

原文公布ζ5栏费用定位值 $84-34.39425186=49.60574814\ldots$ 比较该率仍差约 $18.05277880n$。完整 $\widehat P_n$ 模型未付；PDF20式(28)明标experimental，不能升级为本轮全primepower证书。这些数字是作者报告的预算定位，不是本原费用lower或本项目认证精确常数。

同一Σ₇ factorial symmetry作用于canonical $I',I''$，因此有望审**完整向量** $(Q_n,R_n)$ 的内容，而非只贴ζ5一栏的清整。该共同向量是目前未完成的具体source接口。定向检索与236/237相应稿没有找到它的完整本原审计；不是穷尽归档或全世界文献的声明。

## 6. 正式决定与下一轮唯一首问题

上述候选没有足够已证净预算，因此不登记数值实施准入。唯一下一任务为[M₀,₈完整向量核查](m08_target_vector_charter_round266_20261013.md)，**最多一轮来源验证**：从原double-Barnes及下降积分定义Q、P、P̂，建立全部prime powers的共同安全模型，核Σ₇对 $(Q,P+3P̂)$ 的完整内容是否真有改变上述量级缺口的机制。原实验式和ζ5单栏费用不作输入。

选择它的理由是已明确1、X两坐标，且只有一个目标primitive算术接口；wheel还新增发散和全周期投影缺口，mixed Wronskian仍需从头识别actual selector和signed内容。若266只给旧单栏上界、局部节省或无足够机制，结束这个源核查，不扩5040 orbit参数搜索、不自动转优化窗口。这个有限来源验证不是给263–264改名，也不是宣称X已获准证明。

本轮完成正式复盘last265；连续未改善数值可行性计数保留为5，不因新结构和来源识别重置。默认下一正式复盘269、最迟273；当前核查窗口在266到期更早。总goal保持active。

## 7. 实际读域与独审

主代理全文读成果地图，读263/264结算及236相关替代来源范围；旧长批输出有截断，不据其领取全文标签。实际核BZ本地32页v3的物理7、10、20、28–29页、第一页版本及primary HTML中(4)、Betti分量、group与§11；本地SHA `5a2e45566925a2de55067ca40b599bb4e8f89475a1ffc5cd506dbe896c3a1636`，原件[保留](../literature/brown_zudilin_cellular.pdf)。HTML自动编号和PDF不同，以说明所用版本为准。

另读Eskandari v1的(2.9)、§4–5、wheel v3 Definition61/Theorems62–65，以及259 F6–F9的实际算子。三位新上下文子代理分别只读源、旧停止范围与primary选段；主代理独立重建Laplace/凸下界、wheel五项多项式与corner power-count、Wronskian/符号边界、M₀,₈投影和支持。保存后两位审阅者全文复读本稿与266任务说明：graded_mechanism独核Catalan、wheel、BZ；odd_sources独核mixed边界及目标投影，补足前者自撰Wronskian段不能自计独审的范围。按复核限定了Stieltjes的 $1-sx$ 约定及可容许八参数族，未发现其他阻断项。审阅不认证作者数值常数区间，不重证整篇BZ分解或全部引用文献，不继承FULL/Lean标签。无CAS、数学producer、素数/参数/地图或Padé扫描；文献和形式化字节保留。
