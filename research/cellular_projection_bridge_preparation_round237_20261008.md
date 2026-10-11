# 第237轮后备：固定 M₀,₁₀ 的全 n 周期投影桥

日期：2026-10-08。仅准备后备接口，不改变第236轮确定的联合格主任务。数学程序、参数扫描均为0。

## 1. 固定实际积分与已证的全 n 输入

取 Brown–Zudilin v3 物理PDF29页的配置
\[
\sigma=(10,2,4,1,6,3,8,5,9,7),\qquad
\mathcal S=\{0<t_1<\cdots<t_7<1\}.
\]
令
\[
D=(t_3-t_1)t_3t_5(t_5-t_2)(t_7-t_2)(t_7-t_4)(1-t_4)(1-t_6),
\]
\[
F=\frac{t_1(t_2-t_1)(t_3-t_2)(t_4-t_3)(t_5-t_4)
(t_6-t_5)(t_7-t_6)(1-t_7)}{D},\quad
\omega=\frac{dt_1\cdots dt_7}{D},\quad I_n=\int_{\mathcal S}F^n\omega.
\tag{B1}
\]
这里 n 是积分参数，标记点数始终为10。Brown 2014 §10.2.6将此配置列在收敛配置中；§5.1说明等参数给出全部基本 cellular 积分，且收敛判据是紧化后实胞腔有限距离边界无极点。因而 I₀ 有限，所有 n≥0 是合法实际周期。以下也给出直接控制：
\[
F=\frac{t_1}{t_3}\frac{t_2-t_1}{t_3-t_1}
\frac{t_3-t_2}{t_5-t_2}\frac{t_4-t_3}{t_5}
\frac{t_5-t_4}{t_7-t_4}\frac{t_6-t_5}{t_7-t_2}
\frac{t_7-t_6}{1-t_6}\frac{1-t_7}{1-t_4}.
\tag{B2}
\]
八个因子在 \(\mathcal S\) 中均严格介于0和1。因此
\[
0<I_n\le I_0,\qquad I_n\longrightarrow0,\qquad
\sum_{n\ge0}I_n z^n
=\int_{\mathcal S}\frac{\omega}{1-zF}\quad(|z|<1).
\tag{B3}
\]
最后两式分别由支配收敛和支配几何级数得到。这是全 n 的实际正周期及生成积分恒等式；没有给出所投影周期的非零或有效指数，也没有宣布生成函数具有某个已付 CDT 类型。

## 2. 一般 motivic 定理确实给实际恒等式，但只有较大空间

Brown 2014 Theorem8.1/Corollary8.2（物理PDF25–26）适用于这些收敛有理顶形式：每个 \(F^n\omega\) 的 motivic 周期是权重≤7的 motivic MZV 的有理线性组合。应用 period 同态，立刻得到实际积分的同一恒等式；这个方向无需假设 period 同态单射。

Brown 2012 Theorem1.1和Zagier公式及其 motivic lift（Theorems4.1、4.3）将该空间在这些小权重中化成
\[
\mathcal B_{\le7}=
(1,\zeta_2,\zeta_3,\zeta_2^2,\zeta_5,\zeta_2\zeta_3,
\zeta_3^2,\zeta_2^3,\zeta_7,\zeta_2\zeta_5,\zeta_2^2\zeta_3).
\tag{B4}
\]
这里 \(\zeta_j=\zeta(j)\)。具体地，Hoffman \(\{2,3\}\) 基在权重5、7分别有2、3个字，均为单个3夹在若干2中，由Zagier公式化成相应奇ζ乘偶ζ通道；权重6的两字由纯偶ζ公式和
\(2\zeta(3,3)=\zeta_3^2-\zeta_6\)
处理。纯偶ζ均为有理倍的 \(\zeta_2\) 幂。相同恒等式在 motivic 层成立，且与各权重的 Hoffman 基维数一致；所以可用其 motivic 版本定义坐标。**不据此宣称(B4)中实际数值线性独立。**

由此支付一个准确的全 n 结论：
\[
I_n=\sum_{b\in\mathcal B_{\le7}}c_b(n)\,b,\qquad c_b(n)\in\mathbb Q,
\quad n\ge0.
\tag{B5}
\]
这是存在性；Theorem8.1的证明还明确指出非有效性，不能从它推出分母界、系数高度或所需显式坐标。

所有有理顶形式的极点仅在固定紧化的边界上。各 n 的极点支撑之并为有限个边界分量，且由收敛性与实胞腔边界无共同分量。因此它们可放进一个固定相对 mixed Tate 周期对象。这个观察只支付共同容器；**容器的秩四或所需分次维数并未计算**。特别地，不能把乘以非恒定 F 当作相对上同调的免费端同态：\(d(F\eta)=F\,d\eta+dF\wedge\eta\)。

## 3. 最早尚未支付的投影引理

所要的六通道实际恒等式是
\[
I_n=U_n\zeta_7+V_n\zeta_5+W_n
+\zeta_2(\widetilde U_n\zeta_5+\widetilde V_n\zeta_3+\widetilde W_n),
\quad U_n,\ldots,\widetilde W_n\in\mathbb Q,
\quad \text{全部 }n\ge0.
\tag{B6}
\]
一个明确、充分且可核的 uniform motivic 证书，是(B5)的五个坐标
\[
c_{\zeta_3}(n)=c_{\zeta_2^2}(n)=c_{\zeta_3^2}(n)
=c_{\zeta_2^3}(n)=c_{\zeta_2^2\zeta_3}(n)=0
\quad(n\ge0).
\tag{B7}
\]
(B7)等价于相应 motivic 六通道包含性，并蕴含(B6)。没有 period injectivity 时，不宣称(B7)是实际(B6)的必要条件。

一般权重定理没有给(B7)。Brown 2014 PDF34将同一配置的“中间消失”标为 experimental。其Theorem11.2与Corollary11.3的已证明消失机制，要求极点除子 cellular；PDF35明确指出标记点数≥7的基本积分的极点除子一般不再 cellular，并把进一步推广留为问题。故不能把 nmarks=5,6 的 Apéry 情形证明直接搬到本配置。

即使证出权重3、4、6全消失，也还须处理权重7中 \(\zeta_2^2\zeta_3\) 的单独通道。权重5本来就是(B6)允许的两通道。要再升级到 v3 结尾展示的 rank4 模型，还需要权重5和7中的耦合：
\[
V_n=-3R_n,\quad \widetilde V_n=2R_n,\qquad
U_n=\frac{75}{4}Q_n,\quad \widetilde U_n=-9Q_n.
\tag{B8}
\]
v3 PDF29将 rank4 的底层 motive 标为 experimental，并在结尾叙述两线性形式的分解；该例展示 n=0,1,2，而没有在这些页给出覆盖全部 n 的相对上同调、系数递推或约化证书。本轮定位全文相关措辞并阅读结尾，没有找到可直接移植到此配置的已证明 uniform certificate。因此(B6)、更强(B8)保留为需要明确证明的桥，不把有限头宣布为定理；也不把原文展望改写成已有数值无理性结果。

这里“令 ζ₂=0”只能指已证明 motivic 恒等式的坐标投影。若(B6)已支付，分别对两部分应用 period 得到实际数
\[
I'_n=U_n\zeta_7+V_n\zeta_5+W_n,\quad
I''_n=\widetilde U_n\zeta_5+\widetilde V_n\zeta_3+\widetilde W_n,\quad
I_n=I'_n+\zeta_2 I''_n.
\tag{B9}
\]
这不是在原数值积分中将非零的 ζ₂ 任意置零。(B3)的正性不推出 \(I'_n\ne0\)。

## 4. 可终止的全 n 证书与新目标边界

下一次若启动此后备任务，只接受以下一种明确证书，而不是更多有限头：

* 对固定相对对象计算出(B7)所需的分次/子空间消失；或
* 给出可逐式验证的有理形式约化/contiguity 恒等式，对全部 n 将禁止通道的 motivic 坐标控制住。

后一种可做成一个完全明确的有限验证引理。设 \(v_n\) 为(B4)的11维 motivic 坐标，若有同一个已证明关系
\[
\sum_{j=0}^{r}a_j(n)v_{n+j}=0,\qquad a_j(n)\in\mathbb Q(n),
\tag{B10}
\]
且所有整数 n≥n₀ 上 \(a_r(n)\) 有定义并非零，那么禁止坐标在一个连续 r 项初段为零就通过归纳全部为零；n<n₀和整数奇异点必须另付。积分层的(B10)需展示 rational-form telescope、相对边界项为零及其 motivic lift，而不能由实数期望关系或有限数据猜测推出。这条归纳引理是已证明的；具体(B10)在本配置仍未构造。单说“periods/holonomic”不给上述可核边界与整数例外。

证明(B6)以后仍未得到新数值定理。若要指定 ζ₇，可形成
\[
V_{n+1}I'_n-V_nI'_{n+1}
=(V_{n+1}U_n-V_nU_{n+1})\zeta_7
+V_{n+1}W_n-V_nW_{n+1}.
\tag{B11}
\]
这支付形式消元，尚须目标系数在无限多个 n 非零、实际清分母后非零、完整系数高度与投影后的真实渐近。用不同参数子族也须付同样条件。全积分 \(I_n\) 的快衰减不可移植到 \(I'_n\)：v3 的已分析 M₀,₈ 例恰须转用次主渐近，第236轮已纸面核了这个区别。

“ζ₅、ζ₇至少一个无理”在项目采用的 ζ₅ 基准下不是新目标。后备入口必须明确支付指定 ζ₇ 的(B11)，或对 \(1,\zeta_5,\zeta_7\) 更强的真实线性独立输出。也不能从共同 mixed Tate 容器、motivic 秩或系数存在性继承第235–236轮缺失的完整整格/度量预算。

## 5. 范围与结论

本轮正向资产是(B1)–(B5)的全 n 实际周期输入、十一通道的准确 ambient theorem，以及(B7)/(B10)这一可终止的最早桥。结论支持把此配置保留为237联合格检查失败后的有限后备，**不恢复参数优化，也不预领六通道或秩四**。若不能给出(B7)的实际 cohomological/contiguity 证书，应停止把本配置当作已有纯 ζ₇ source。

实际源读取与身份见
[alternative_reading_scope.md](../literature/joint_lattice_metric_sources_round237_20261008/alternative_reading_scope.md)。
主来源：[Brown 2014 author PDF](https://www.ihes.fr/~brown/IrratModuliMotivesv8.pdf)，
[Brown 2012 author PDF](https://www.ihes.fr/~brown/MTZ.pdf)，
[Brown–Zudilin v3](https://arxiv.org/abs/2210.03391v3)。
只对已列完整选页负责，不声称 FULL 读三份整篇论文；数学程序0，无新PDF下载，无旧稿/主进展/manifest修改。
