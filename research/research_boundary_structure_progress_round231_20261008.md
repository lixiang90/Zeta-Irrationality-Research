# 第231轮进展：边界算术结构与耦合点值缺口

本轮状态：**progress**。已证明边界Hankel的参数反序与半阶Schur归约，
平方Cauchy的有限域Gaudin/微分插值核，以及正则化解析矩阵的非零结构。
**尚未得到原实际行列式的无限非零，也没有新的数值无理性/线性无关性定理。**
ζ/L 的真实目标隔离和完整净算术收益仍是原目标的必要部分，未被辅助Θ族替代。

第230轮的完整残差和固定八例精确输出已实际保存，故上一轮分类为progress。
本轮没有重跑它们或扩大参数扫描；推进依据是新纸面结构与定向primary核对。

## 1. 初始边界块出现了明确的Fermat商条件

对素数p=4d+1、m=d+1、k=2d，同一边界初始块A₀/B₀满足

\[
JA_0J=A_0,\qquad JB_0J=-B_0-4H_kA_0,
\qquad\det A_0=2^{-d(2d+1)}.
\]

这来自完整参数反序，绝非实数正性或有限样本的外推。按J的正/负
特征空间分块，维数分别a=ceil(m/2)、b=floor(m/2)，已得到

\[
\frac{\det B_0}{\det A_0}
=\lambda^{a-b}\det(\lambda^2I_b-S),\qquad
\lambda=-2H_k=4q_p(2).
\]

S是由实际交叉块组成的b阶矩阵，尚未证明其剩余行列式为unit。
当p≡1(mod8)、m奇时，满秩必要求q_p(2)≠0，也就是相应素数为底数2的
non-Wieferich素数。它是一个新增的必要算术条件；目前没有展示该同余类
的实际Wieferich反例，更没有证明所有边界失败。p≡5(mod8)、m偶没有
维数强制的线性因子，这条子族仍可研究。

查到并实际选读的[Ding2019，Theorem1.1](https://doi.org/10.1016/j.crma.2019.05.007)
与[Graves–Weiss2025 v1，Introduction/Theorems1–3](https://arxiv.org/abs/2503.19144v1)
仍以abc假设给non-Wieferich的增长或算术级数结果，不能替本项目支付
所需的无条件无界子族。所选文献的条件结论也不支付S与另一边界块的单位性。

详见 [参数反序及精确Schur块](q2_boundary_hankel_reflection_round231_20261008.md)；
Root另存了 [独立反序/调和因子推导](q2_boundary_symmetry_independent_round231_20261008.md)。

## 2. 平方Cauchy块变成了一个确切的有限域微分核

同一第二块H_(i,j)=1/(d+i+j)的普通Cauchy行列式是p单位。
Borchardt身份把det(H^[2])≠0等价于per(H)≠0。现在已用节点插值在Fp
直接证明其Gaudin行列式身份，进一步得到

\[
\operatorname{per}(H)=0\quad\Longleftrightarrow\quad
\exists f\ne0,\ \deg f\le d:\quad
P f'-P'f\in Q\mathbf F_p[x],
\]

其中Q(x)=∏_(i=0)^d(x−i)、P(x)=Q(x−1/2)。还把未知多项式次数降到d−1，
得到等价的对偶节点条件。真正缺口是排除这个特定半单位平移的核，
并使它与第一块的单位条件在同一无界素数子族上相交。

一个手算Fp5反例已排除“P/Q是不相交的x^p−x因子，所以永久和非零”
的泛化推断；反例不是当前半单位平移对象，不能拿来宣布实际H失败。
现成的binomial-root永久和简积公式也未匹配当前算术节点。
详见 [Gaudin与半单位平移核](q2_boundary_squared_cauchy_gaudin_round231_20261008.md)。

## 3. 解析正则化支付了相关矩阵，但保留真实点值缺口

令a=1/4、h_a(x)=log(x/a)/(x−a)>0。通过分离幂谱带与
squared-Cauchy系数的同号minor，已证明正则化的完整2m函数族
[h_a x^s; f_(d,s)]具有Chebyshev性质，相应实际矩Γ_d可逆。
它保留原f_(d,s)，没有把投影替换成另一组任意正函数。

由完整线性系统唯一构造monic degree m多项式P_m，给出精确关系

\[
\mathcal W_d(\Theta)=(-2)^m\det\Gamma_d\,P_m(1/4).
\]

因此所需实际非零现在等价于这个耦合点值非零。Γ_d的可逆性
**不证明**P_m(1/4)≠0。扩展函数族的幂谱带会交叠，不能免费套用
更大指标的正常性；标量正交多项式的相邻非共零结论也不能移给P_m。

对于固定正测度h_aν的标量正交多项式q_m，三项递推确实证明相邻
q_m(a)不能同时为零，故初始signed B块在每两个相邻尺度至少一项
实数非零。这是一个已付的无界子块结论；它不支付原W或modp单位性。

正则化的算术内容亦已明确：

\[
K=\int h_{1/4}\,d\nu=\frac{8\pi}{3\sqrt3},\qquad
\int x^n h_{1/4}\,d\nu=(1/4)^nK+
\frac12\sum_{j=0}^{n-1}(1/4)^{n-1-j}B_j.
\]

所以新增π周期的矩系数为rank1，有限头是有理数。这是完整周期账，
没有支付更好的全部素数费用、严格收益或新的四项数值线性无关。

此外，原f_(d,s)可写成同一固定Stieltjes函数F₀的精确Taylor余项，
为下一次寻找固定Hankel/Padé表达提供入口；该表达与Kronecker无限非零桥
尚未证明，不能把函数非有理性直接当本W的无限非零。

完整证明见 [正则化基与真实Christoffel点值](q2_christoffel_positive_basis_round231_20261008.md)。

## 4. 下一轮提前作全局复盘

上次正式复盘228；默认节奏原为234。本轮发现了隐藏的prime无穷性条件
及耦合点值条件，因而把下一次正式复盘**提前到232**，距228正好4轮。
231没有重置计数，也没有把辅助结构引理定义成最终成果。

复盘将比较四个真实接口：ζ/L目标的周期隔离、同一完整整模型、
解析收益与实际无限非零。重点判断边界有限域路线、正则化/固定余项路线
是否值得继续，或者应回到更直接的ζ/L源函数。
不默认引入abc等未付假设，不追加扫描，不先优化尚未闭合对象的费用常数。

## 5. 文献与验证范围

新primary与实际选读范围存入
[231文献库目录的Root记录](../literature/finite_field_projection_sources_round231_20261008/root_reading_scope.md)，
另有B/C/A各自的source记录。下载全文不等于阅读全文；所选文献只支持
被核对的公式或适用条件。本轮没有重审整个OpenAI仓库或运行Lean。

数学程序0、旧producer复跑0、Git操作0、Lean构建0。
新数学稿经Root完整审读及交叉纸核；具体范围见
[Root独审记录](research_round231_root_math_check_20261008.md)。
另有 [反序/Gaudin独审](research_round231_symmetry_gaudin_review_20261008.md) 和
[正则化基独审](research_round231_christoffel_positive_basis_review_20261008.md)。
归档仅核230manifest身份、main保留前缀、231新文档及本报告链接。
