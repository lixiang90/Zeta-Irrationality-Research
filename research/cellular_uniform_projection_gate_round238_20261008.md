# 第238轮：cellular 全 n 投影的有界准入检查

2026-10-08。固定第237轮 M₀,₁₀ 配置
(10,2,4,1,6,3,8,5,9,7)及其 F、ω、\(I_n=\int_{\mathcal S}F^n\omega\)。
数学程序/扫描0，旧资产不改。本轮**没有证明新的禁止坐标恒零**。下列两条精确负向引理关闭“直接套一般Gauss–Manin或自对偶就得到六通道”的推断，并明确还须什么证书。

## 1. 标准对偶关系看不见全部五个禁止坐标

复用237已经支付的 motivic 十一通道基，记
\[
\mathcal B_{\le7}^{m}=
(1,\zeta_2^m,\zeta_3^m,(\zeta_2^m)^2,\zeta_5^m,
\zeta_2^m\zeta_3^m,(\zeta_3^m)^2,(\zeta_2^m)^3,
\zeta_7^m,\zeta_2^m\zeta_5^m,(\zeta_2^m)^2\zeta_3^m).
\tag{U1}
\]
需要消掉的五通道为
\[
\zeta_3^m,\quad(\zeta_2^m)^2,\quad(\zeta_3^m)^2,\quad
(\zeta_2^m)^3,\quad(\zeta_2^m)^2\zeta_3^m.
\tag{U2}
\]
本轮实际FULL读 Brown 2014物理PDF27–28。Lemma8.4的前提包括底/顶分次各一维；结论是对偶周期在 unipotent 映射π下、**再模掉权重≤6**的同余。π杀掉ζ₂；引理只控制最高权重部分，不是一条全部数值周期的等式。

令Q为这条引理所用的观测：
\[
Q:\mathcal H_{\le7}\xrightarrow{\pi}\pi\mathcal H_{\le7}
\longrightarrow \pi\mathcal H_{\le7}/\pi\mathcal H_{\le6}.
\tag{U3}
\]
在(U1)中，权重<7的元素在最后一步消失；权重7的
\(\zeta_2^m\zeta_5^m\)及\((\zeta_2^m)^2\zeta_3^m\)
在第一步消失。因此Q只保留ζ₇方向，且(U2)全部在kerQ中。
**对任意n给周期加上任意五个禁止通道的有理组合，(U3)所观察的周期数据均不改变。**

这证明，即使先额外支付该配置的自对偶识别和Lemma8.4全部前提，仅凭其约化后的周期关系仍不能证明237所需的任何一项禁止坐标为零。这里不声称任意增加通道仍属于同一个已计算的具体motive；正是那种额外的类/分次信息尚未支付。自对偶的分次维数对称性也不等于分次消失。本结论只限定该对偶同余的证明能力；不排除进一步的全上同调计算、representation projector或更强的实际恒等式。

## 2. 一般Gauss–Manin输入也不强制六通道：同F的精确反例

这里检验的是从“一般M₀,₁₀周期容器与移动极点Gauss–Manin”直接推出六通道的逻辑，不是反驳指定ω。

在同一实胞腔置
\[
x_i=t_i/t_{i+1}\ (1\le i\le6),\qquad x_7=t_7.
\]
此映射将\(\mathcal S\)双射到(0,1)⁷，正Jacobian给
\(dx_1\cdots dx_7=dt_1\cdots dt_7/(t_2\cdots t_7)\)。
取另一个实际有理顶形式
\[
\eta=\frac{dt_1\cdots dt_7}
{(t_4-t_1)t_2t_3t_5t_6t_7}
=\frac{dx_1\cdots dx_7}{1-x_1x_2x_3}.
\tag{U4}
\]
它的极点也只在紧化边界，积分绝对收敛。逐项非负几何级数或三次纤维积分给
\[
\int_{\mathcal S}\eta
=\int_{(0,1)^3}\frac{dx_1dx_2dx_3}{1-x_1x_2x_3}
=\sum_{k\ge0}\frac1{(k+1)^3}=\zeta_3.
\tag{U5}
\]
纤维积分依次为
\(-\log(1-x_1x_2)/(x_1x_2)\)、\(\operatorname{Li}_2(x_1)/x_1\)、\(\operatorname{Li}_3(1)\)；
这是标准迭代积分恒等式，同样给motivic周期ζ₃ᵐ，四个多余单位区间的周期为1。无需period injectivity，也未据数值恒等式猜测某个motivic坐标。

沿用原来的同一个F定义
\[
\widetilde I_n=\int_{\mathcal S}F^n\eta,\qquad
\widetilde{\mathcal I}(z)=\int_{\mathcal S}\frac{\eta}{1-zF}.
\tag{U6}
\]
由237的0<F<1及(U5)，全部n收敛，\(|z|<1\)时生成积分合法。它有相同移动超曲面 \(1-zF=0\)，并在加入η固定极点后的共同相对代数de Rham对象中具有一般Gauss–Manin连接。每个系数仍是权重≤7的MZV周期；然而其n=0的禁止ζ₃ᵐ坐标恰为1。

这是一个**精确解析/motivic反例**，证明一般周期容器、同F的移动超曲面和Gauss–Manin存在性不是六通道包含性的充分条件。使用n=0是反驳该无条件推断，绝非用有限头认证原序列的全n投影。η与ω的固定极点除子/类不同，所以它不否定原配置可能有特殊投影；恰说明那一特殊相对对象或类的约化信息必须显式支付。

## 3. 原文已经给的递推存在性，与尚未给的证书

本轮实际FULL读 Brown 2014物理PDF13–14。§4直接研究
\[
\mathcal I(z)=\int_{\mathcal S}\frac{\omega}{1-zF}.
\tag{U7}
\]
其 relative Gauss–Manin对象保留实胞腔边界；存在
\(D_{\rm rel}\in\mathbb Q[z,\partial_z]\)
使该相对类为零，配对水平relative周期后得到
\(D_{\rm rel}\mathcal I=0\)，所以原实际序列有P-recursive关系。这是原文的一般存在性，**本轮没有把它包装为新的小秩或显式递推成果**。

原文也明确区分去掉相对边界后的absolute对象：relative→absolute的kernel为constant connection，absolute算子只给
\[
D_{\rm abs}\mathcal I=P(z),\qquad P(z)\in\mathbb C[z].
\tag{U8}
\]
这个边界period-valued右端并非已知的有理多项式。将absolute reduction当作无边界homogeneous telescope会遗漏数据；把P用足够多导数消掉虽可得更大齐次算子，也不消灭其禁止周期坐标。

自对偶在此节给递推系数的反射
\[
p_i(n)=c\,p_{r-i}(-r-1-n)
\tag{U9}
\]
（适当符号和非零有理c），不是禁止坐标恒零。生成形式的对偶还交换z与1/z及两组边界，不是原点Taylor芽的免费同号投影。

实际可核的下一证书必须至少包含：

1. 具体relative reduction或telescope，含全部边界，使所导关系在固定motivic系数包中成立；只有数值递推而没有这个lift时，不能以未知的数值周期独立性比较十一通道系数。
2. 给出实际阶数、系数及全部非负整数奇异点；末项系数在归纳范围内非零，例外逐一处理。
3. 对禁止坐标支付相应有限初段的**motivic**约化，再由该已证关系归纳全n。

237的递推归纳引理只在这些证书已经给出时有效。本轮没有构造D_rel的具体形式，没有检查其整数奇异点，也没有完成上述motivic初段。因此未从原文的存在性预领五坐标消失或rank4；不以继续保存文献代替该缺口。

## 4. 行动结论与数值目标

本轮支付(U3)的五坐标不可见引理与(U4)–(U6)的同F精确反例。它们关闭“只凭自对偶/标准Gauss–Manin就够”的直接提案；**正向uniform六通道投影仍无进展**。不启动参数或递推阶数扫描，也不自动再延长六轮。

若原实际flag/费用任务停止而选择cellular后备，首任务仍只能是上一节的一份具体relative证书，或直接计算原类的禁止分次；当前资产不足以宣布纯ζ₇ source。即使完成六通道，指定ζ₇还须真实消ζ₅后的无穷非零、完整整格与投影次主渐近预算；不能把全I_n的正性/主衰减或“ζ₅、ζ₇至少一个无理”作为新数值目标出口。此稿不改变237–238主任务和236正式复盘计数。

实际读域与冻结源身份见
[alternative_reading_scope.md](../literature/actual_flag_sources_round238_20261008/alternative_reading_scope.md)。
主来源：[Brown 2014 author PDF](https://www.ihes.fr/~brown/IrratModuliMotivesv8.pdf)。
本轮仅新增完整选读物理PDF13–14、27–28；237的基与固定积分沿用其已核身份，无新PDF下载、数学程序或旧文件修改。
