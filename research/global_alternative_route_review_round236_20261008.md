# 第236轮：替代周期路线的首个数值门槛

2026-10-08。独立路线复盘，作者 /root/round218_lambert_carrier。数学程序、参数扫描、旧 producer 复跑均为0；旧数学稿、主日志、manifest 和外部仓库只读。本稿不研究已关闭的固定三维 scalar 表，也不研究新 c4 源的参数。

## 1. 判断与选择

在这里比较的替代路线中，最可信的重构对象是 **一个固定 cellular 七重积分族的真实 ζ(7) 投影**。理由是已有低权 primary 同时给出实际数值投影、投影后的指数率和作用于投影系数的算术对称性；它没有把“周期属于某个几何空间”当成严格小整数。不过，高权族本身尚未取得这些桥，不能宣布准入数值证明。

近期行动可先允许本轮提出的同源联合 jet 格做**一个有界接口检查**：它改变 degree-D 整模型，区别于继续调整固定 scalar LCM 表。其 prime-window 指数收益必须进入同一个完整 jet 格及解析 minor 才有意义；不是新的 τ，也不能继承另一个投影的衰减。若这个桥未付，转到下文指定的 cellular ζ(7) 投影门槛，不再为 conifold 单常数或椭圆 ratio 追加容量优化轮次。

这项选择要求证明 ζ(7) 的新性质，或比本项目已采用的 ζ(5) 无理性基准更强的线性无关性。原文建议的“ζ(5)、ζ(7) 至少一个无理”在该基准下不算新成功出口。本文不重新认证那份 ζ(5) 基准，也不宣称文献整体已接受它。

## 2. 各路线距离实际结论的第一道缺口

| 路线及真实目标 | 已有可靠接口 | 首个未证核心引理；本轮处理 |
|---|---|---|
| R0 conifold / compact normal function | 指定 higher-Chow family 的 regulator 微分；真实 PF、端点 concomitant；dual germ 可只检测一个初值 | 目标敏感的第二端点或完整标记比较。dual 为 \(F+q\)，所有跳跃不随 \(q\) 改变；不恢复单常数 CDT 攻击 |
| 五个 Mukai Fano 的 Apéry extensions | 原文 Theorem 1.1 和具体 THNF；V12 的 \((\zeta(3)/6)A-B\) 真正消去完整跳跃 | 新 ζ/L 的实际 connection coefficient、整数初值与严格关系增益。已算实例是 ζ(2)、ζ(3)、Tate/已知临界 L 通道，不能按几何维数免费推广 |
| conductor15 非 CM 椭圆 ratio | \(r=30L(E,2)/[\pi L(E,\chi_{-4},1)]\) 的明确评价；rank5 counterterm、全素数 half-width 模型及 native 关系补点 | 同一完整函数包的有效 common map/严格能量预算。foreign µ lift 和原 σ 的 log² 仍在；ratio 的无理性也不自动等于单独 \(L(E,2)\) 的无理性 |
| Deligne–Drinfeld | 当前源的 formal Lie algebra 生成/自由性；奇权 real holonomy 的非零 depth-one 系数 | 实际数值关系到目标敏感整源及严格估计。非零系数只用 ζ(n)>0，不能排除 ζ(n) 是正有理数 |
| Catalan/ζ mixed moments | 正 tail、完整 Schur 消元、全列 period-coefficient rank | 假设数值关系处的真实 maximal minor 非零及同 minor 费用。generic 多项式非零不排除真实点落在 determinantal locus |
| cellular \(M_{0,10}\) | 原文给出固定七重积分和低阶数值分解；低权 \(M_{0,8}\) 有真实投影/次主指数机制 | 全尺度数值投影、ζ(5) 消元后的无限非零及投影指数。rank4 的 motivic 描述在该段明确是 experimental；有条件保留 |

这些缺口不是笼统的 Hodge 先决条件。CDT 的直接 rank 定理本身并不要求先造 Betti/Hodge packet；但选择 regulator 作为数值源时，若实际标记或 connection identity 未付，就尚未给出所需 Q-germ 与关系敏感解析性质。

conifold 的限制可以直接检验。冻结 dual 身份是 \(S(1-t)=2\alpha_0+F(t)\)，\(F\in\mathbb Q[[t]]\)。对每个代数 \(q\)，\(F+q\) 的非恒定系数、局部跳跃及共同亚纯图完全相同。因而只采用这些资料的判据若排除某个代数常数，也会排除无条件算术实例 \(F\)。需要增加目标敏感的第二项，不能用“normal function 非平坦”补这个缺口。相应原始 scalar 的真实 Tate–Betti vanishing-period shift 还保持端点、改变超越 jet，故单端点值没有免费固定算术 germ。

## 3. 一个可改变行动的精确判断：删除附带周期会损失最快指数

Brown–Zudilin 当前 v3 的对称 \(M_{0,8}\) 族满足实际数值分解
\[
 I_n=2I'_n+4\zeta(2)I''_n,\qquad
 I'_n=Q_n\zeta(5)-P_n,\quad I''_n=Q_n\zeta(3)-\widehat P_n.
 \tag{A1}
\]
原文 PDF5 给出三根的实际连接：
\[
 \chi(\lambda)=4\lambda^3-2368\lambda^2-188\lambda+1,\qquad
 \lim |I_n|^{1/n}=\lambda_1,\quad
 \lim |I'_n|^{1/n}=\lim |I''_n|^{1/n}=|\lambda_2|.
 \tag{A2}
\]
这里采用 primary 已陈述的 asymptotic connection，不把仅有 characteristic polynomial 当成 connection 的证明；本人没有复跑其 telescoping 软件。

以下比较只需纸算。因为
\[
 \chi(0)>0,\quad
 \chi(1/192)=-76799/1769472<0,\quad
 \chi(-1/12)=95/432>0,\quad
 \chi(-1/10)=-971/250<0,
 \tag{A3}
\]
再由 \(\chi(1)<0\) 与正无穷处正号，三个不交区间分别给全部三个实根。因此
\[
 0<\lambda_1<1/192,\qquad 1/12<|\lambda_2|<1/10.
 \tag{A4}
\]
令 \(d_n=\operatorname{lcm}(1,\ldots,n)\)。由 \(\log d_n=n+o(n)\)，
\[
 \lim\frac1n\log(d_n^5|I_n|)=5+\log\lambda_1<0,\qquad
 \lim\frac1n\log(d_n^5|I'_n|)=5+\log|\lambda_2|>0.
 \tag{A5}
\]
第一不等式使用 \(e<11/4\)、\((11/4)^5<192\)；第二使用 \(e>2\)、\(2^5>12\)。故完整正积分乘这个因子仍趋零，**目标 ζ(5) 投影乘同一个因子却指数增长**。这个结论不需要把原文 PDF5 的 experimental 全分母观察升级成本文的整性定理；即使另行支付该因子的整性，它也不会救出投影。

这是实际已分析族中的严格反例：不能把全 period stack 的最小积分衰减交给删除周期后的数值 channel。它直接限制 mixed-moment、Schur 和更高维 normal-function 方案的预算移植。正积分、formal projection 与真实 projected value 的指数需要分别付清。[当前原文](https://arxiv.org/abs/2210.03391v3)

同文 Theorem 1 的有效无限近似指数为0.86；作者明确不据此推出无理性。PDF20 的五个连续最大值 LCM 及额外分母优化还有明确 experimental/待证明措辞；本文只复核结构，不将整套 factorial savings 认证为我们可直接采用的最优模型。

## 4. 固定七重积分的精确替代门槛

原文 PDF29 指定配置 \((10,2,4,1,6,3,8,5,9,7)\)。写
\[
 D=(t_3-t_1)t_3t_5(t_5-t_2)(t_7-t_2)(t_7-t_4)(1-t_4)(1-t_6),
\]
\[
 I_n=\int_{0<t_1<\cdots<t_7<1}
 \left(\frac{t_1\prod_{j=1}^{6}(t_{j+1}-t_j)(1-t_7)}D\right)^n
 \frac{dt_1\cdots dt_7}{D}.
 \tag{A6}
\]
这不是重新选择参数族。作者提出数值分拆 \(I_n=I'_n+\zeta(2)I''_n\)，其中 \(I'_n\) 属于 \(1,\zeta(5),\zeta(7)\) 通道，\(I''_n\) 属于 \(1,\zeta(3),\zeta(5)\) 通道。其全尺度、完整算术与指数证明不能从低权结果领取。

列出的有限评价给
\[
 I'_1=\frac{75}{4}\,61\,\zeta(7)-900\zeta(5)-220,\qquad
 I'_2=\frac{75}{4}\,52921\,\zeta(7)-783459\zeta(5)-\frac{6021219}{32}.
 \tag{A7}
\]
仅在这些明示评价上，纸面消元得到
\[
 261153 I'_1-300 I'_2
 =\frac{4052475}{4}\zeta(7)-\frac{8037855}{8},
 \qquad 61\cdot261153-300\cdot52921=54033\ne0.
 \tag{A8}
\]
这证明有限头的 ζ(7) channel 可被观察；没有证明其实际值非零、无限非零或严格小性，更没有独立重证原七重积分的两项评价。

下一项**唯一准入 lemma**可明确为：对这个固定族构造全 \(n\) 的实际数值 identities
\[
 I'_n=a_n\zeta(7)+b_n\zeta(5)+c_n,\qquad
 I''_n\in\mathbb Q+\mathbb Q\zeta(3)+\mathbb Q\zeta(5),
 \tag{A9}
\]
并给出可追溯的投影函数/递推证书，不能以 MZV period-map injectivity 取代它。只有该 lemma 过门，才考虑 \(b_{n+1}I'_n-b_nI'_{n+1}\) 的 actual connection、无限非零与完整整数化。A8 不排除最终零。若只能得到“至少一个 ζ(5)、ζ(7) 无理”，在本项目基准下立即停止；不把它当新目标。

该对象与222–227固定交错分式包不同：这里的候选收益来自实际几何数值投影、次主渐近及作用于系数的对称性，而不是给同一三周期包换参数。但是否真有更小费用尚未证明，也不保证比原包更强。

## 5. 对237联合格提案的独立评价

有理固定基的 scalar prefix LCD 与完整 degree-D polynomial-source jet 格是不同对象。若
\[
 T_{D,N}:\mathbb Q[u]_{\le D}^{\,m}\longrightarrow\mathbb Q^{N+1},
 \quad (P_i)\longmapsto
 \bigl([u^n]\sum_iP_i f_i\bigr)_{0\le n\le N},
 \tag{A10}
\]
则真正整系数域是 \(T_{D,N}^{-1}(\mathbb Z^{N+1})\)。在完整 cutoff 的 \(T_{D,N}\) 已证单射时，这个域才是离散的全秩格；有核时须先商去 \(\ker T_{D,N}\)，在像格中计费，不能将无限的 Q-kernel 当作有限 index 收益。逐行清分母所得整数子模的像给其中一个子格；卷积中跨行 cancellation 可使整值像格严格变大。因此已关闭固定 scalar/Literal array 并不免费关闭这个 degree-D 格，也不能把其 index saving 免费反填到 scalar τ。

这为一个有界联合格检查提供合理性。它须先支付所有素数幂、全部源列、完整 cutoff 和与解析 determinant 的传递。在此之前，窗口上的 \(N^2/4+o(N^2)\) 收益只是一段 index 信息；不是净预算，也不是数值无理性。本稿没有 FULL 审读尚在收束的 B236 联合格证明，故不登记其数学 PASS。

因此优先级是：允许237检查真正的新整模型接口；以 same-object transfer 为停止线。该检查若不能给实际 determinant/holonomy 的完整成本，就停止该对象，转到A9的一项固定 cellular 源重构。不要自动追加六轮 prime/content/容量调参，也不要恢复已经失去关系敏感性的 conifold constant source。

## 6. 来源与结论边界

本人实际 FULL 复读222、228、232正式 review；FULL 读 conifold arithmetic、R0 regulator derivative、elliptic counterterm、period-extension relation-leaf、mixed-moment Schur 五份数学记录。首轮批量输出中的 Cauchy/Betti-flag 文件发生合并截断，只作定位，未登记本轮 FULL。当前 DD 实际读取本地 introduction 全文和 holonomy lines422–553，官方网页核对象，不冒称全论文或 fresh Git 状态。

Primary 实际选读：Brown–Zudilin当前 v3 PDF1–5、17–20、27–30（13页）；Koutschan–Zudilin v1 PDF1–6（全6页）；GKS v3 PDF1–4、27–30（8页）。Kerr2026只有本轮官方 abstract/version locator；未重新读其正文，不把其条件定理作为新输入。原件复用，不重复下载。精确身份及新选段见 [个人scope](../literature/global_review_sources_round236_20261008/lambert_reading_scope.md)。

本轮新纸证是A3–A5的实际投影指数损失判断和A8有限头消元；它们约束下一步行动，不证明新数值无理性/LI。没有从未检索到论文推全球新颖性，没有将 formal Lie freedom、很一般 regulator 非零、generic minor 非零或 positive Gram 视为真实目标点非零。
