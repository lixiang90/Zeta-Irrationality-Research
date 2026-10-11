# 真实周期、完整整模型与算术 holonomy：本轮新目标与结论

日期：2026-10-05。当前研究扩大到有理点二重对数、对数乘积、六分点 trigamma、一般剩余类 Lerch 系统及周期系数 polylog；ζ(7)、Catalan 和此前记录保持冻结。

本轮闭合了两个数值目标族的分类/独立性结论，并证明几个连接真实周期与整模型的结构引理。数值结论是 CDT 已知定理的实际推论，尚未证明新的单个导子 \(L\) 值、ζ(7) 或 Catalan 无理，也未确认这些推论在全球文献中的首次性；本轮没有新增 Lean 形式化。

## 1. 原论文真正可迁移的链条

采用 [CDT arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2)，[固定原件](../literature/cdt2024_l2_chi_minus3.pdf)，218 页。作者站当前 220 页文件另存为 [新快照](../literature/cdt_l2_chi_minus3_author_20261005.pdf)，不混用其页码与旧 v2。另读 [2025 年 20 页短稿](../literature/cdt2025_arithmetic_holonomy.pdf)。

成功证明的核心不是“一个周期函数是 holonomic”，而是以下实际接口：
\[
\text{假定数值关系}
\Longrightarrow\text{有理系数且消去特定坏支的真实芽}
\Longrightarrow
\begin{cases}
\text{同一组实际独立函数}\\
\text{全部系数分母阶梯}\\
\text{合法单值叶/覆盖与解析积分}
\end{cases}
\Longrightarrow
J<m(\log|\varphi'(0)|-\tau).
\tag{1}
\]
最后的严格反向不等式与算术 holonomy 的秩上界冲突。

[机制审计](period_holonomy_cdt_mechanism_20261005.md) 把 Theorem C 的整个链具体化为 Hadamard 有理芽、真实 trace 对称化、六个额外积分、七个 pure 函数与最终 17 个实际独立函数。全部分母不是一个统一 \(L_n^2\)：对称化支付 \(L_{2n}^2\)，积分另支付序号 \(n\)，fine 参数为
\[
\tau=\frac{1032659}{242760},\qquad
\frac{10}{\log(256\cdot1287/2516)-\tau}
=16.1032097\ldots<17.
\tag{2}
\]
原文的函数独立性、合法解析叶及 \(J<10\) 是已证外部输入；本项目核了真实函数身份、完整整数公式、阶梯以及严格数值余量，未冒称重新证明原文解析积分。

## 2. 一个确实得到无理性与四项独立性的新项目目标族

对整数 \(N\ge10^6\)，令 \(\ell_j=\log(1+1/j)\)，以及
\[
\begin{split}
\Phi_N={}&
\operatorname{Li}_2\left(\frac{N+2}{(N+1)^2}\right)
+\operatorname{Li}_2\left(\frac{N+1}{N(N+2)}\right)
-\operatorname{Li}_2\left(\frac1{N(N+1)}\right)\\
&-\operatorname{Li}_2\left(\frac1{N+1}\right)
-\operatorname{Li}_2\left(\frac1{N+2}\right).
\end{split}
\tag{3}
\]
实际实五项恒等式证明
\[
\Phi_N=\ell_N\ell_{N+1}.
\tag{4}
\]
全部参数在 \((0,1)\)，两变量微分及零边界确定常数为零，没有遗留 \(\pi^2\) 或分支修正。

由 CDT Theorem C 和严格条件 \(1/(N+1)<10^{-6}\)，得到
\[
\boxed{\Phi_N\notin\mathbb Q,\qquad
1,\ell_N,\ell_{N+1},\Phi_N\ \text{在 }\mathbb Q\text{ 上线性无关}.}
\tag{5}
\]
这实际处理了无穷多个五项有理点二重对数目标。未指定其中某个单独 Li2 值无理；未证明 \(\log2\log3\) 或三个 log 的乘积无理。

更一般，对正整数 \(m,n\ge2\)，只要 \(0<|m/n-1|<10^{-6}\)，将 (3) 中的五参数替换为
\((n+1)/(n(m+1)),(m+1)/(m(n+1)),1/(mn),1/(m+1),1/(n+1)\)
也得到四项独立。详细证明及阈值见 [机制稿 §2](period_holonomy_cdt_mechanism_20261005.md)。

## 3. 第二个闭合族：全部六分点 trigamma 与有理对数积分

置 \(T_n=\psi_1(n/6)\)。写 \(n=r+6q\)，\(1\le r\le6\)，则实际收敛级数给
\[
T_n=C_n+a_r\zeta(2)+\frac92 b_rL(2,\chi_{-3}),\quad
C_n=-36\sum_{j=0}^{q-1}(r+6j)^{-2},
\]
\[
a=(12,4,3,4,12,1),\qquad b=(5,1,0,-1,-5,0).
\tag{6}
\]
对任意有限有理组合 \(T=C+A\zeta(2)+B L(2,\chi_{-3})\)，
由 CDT Theorem A 有
\[
T\in\mathbb Q\Longleftrightarrow A=B=0.
\tag{7}
\]
任意目标列表与 1 的 \(\mathbb Q\)-秩，恰等于 1 加上其两行 \((A,B)\) 坐标矩阵的秩。因此所有这些组合的有理关系与无理性都可完全判定。

例子包括 \(1,T_1,T_2\) 线性无关，但
\(T_1-5T_2+8T_6=0\)，\(T_7=T_1-36\)。
[投影与整格稿](period_holonomy_target_projection_20261005.md) 还证明六残数整数投影的 Smith 因子为 \((1,18)\)，纯 \(L\) 滤波格为 \(L/8\,\mathbb Z\)，并处理端点平移的全部有理分母。固定投影指标不能控制非单射投影后单行 content 的增长。

这个分类进一步给出一个实际积分族。任取 \(P(t)=\sum_{k=0}^d p_k t^k\in\mathbb Q[t]\)，定义
\[
I(P)=\int_0^1\frac{P(t)(-\log t)}{1-t^6}\,dt
=\frac1{36}\sum_{k=0}^d p_kT_{k+1}.
\tag{8}
\]
在 1 端的 \(-\log t\) 消去分母的一阶零；有限求和与绝对收敛级数允许逐项积分。令 \(r_k\) 是 \(k+1\) 的 \(1,\ldots,6\) 余类，则
\[
I(P)\in\mathbb Q
\Longleftrightarrow
\sum_kp_ka_{r_k}=0
\quad\text{且}\quad
\sum_kp_kb_{r_k}=0.
\tag{9}
\]
其有理值由 (6) 的 \(C_{k+1}\) 精确计算。两个实际正积分对照为
\[
I(t-t^3)=\frac14L(2,\chi_{-3})\notin\mathbb Q,\qquad
I(1-t^6)=1.
\tag{10}
\]
这说明真正决定无理性的是完整周期坐标；余项/积分正性单独不能代替它。任意有限列表的 \(I(P)\) 与 1 的秩也由同一个两行矩阵完全给出。

## 4. 本轮最关键的整模型结果：秩 3 商与真实秩 6 整商

为 (3) 五参数定义实际函数
\(F(z)=\sum_i\epsilon_i\operatorname{Li}_2(r_i z)\)，\(\epsilon=(1,1,-1,-1,-1)\)。
[完整模型稿](period_holonomy_dilog_model_20261005.md) 证明：
- \(1,zF',F\) 的实际微分循环秩为 3；
- 保留五个 log 和五个 Li2 的共享常数来源，具有真正秩 11 的整数 Betti 单值化格；
- 其 de Rham 秩 3 投影的复核为 8 维，却只有 5 维核能从指定来源的有理 Betti 格下降；
- 因此，兼容该来源与投影的 Betti 商至少为秩 6，且下界由一个具体有理 de Rham/整 Betti 商达到。

后者有六个真正独立的有理系数芽
\[
1,\quad g_b,\quad g_c,\quad g_d-2g_a,\quad g_e+g_a,\quad F,
\qquad g_i=-\log(1-r_i z).
\tag{11}
\]
证明保留了额外比较常数 \(\log r_i\)，并精确利用
\(\log N,\log(N+1),\log(N+2)\) 的有理独立性；它不是对形式符号计数。
这个秩下界限定于所给来源，不是所有可能实现的普遍最小秩，也不是六个端点数值已独立。

完整算术与几何还得到：
\[
D=N(N+1)^2(N+2)
\tag{12}
\]
是全部参数的最小公共分母；所有标记边界的坏碰撞素数支持为
\[
N(N+1)(N+2)(N^2+N-1)(2N+3)(N-1)(N^2-2).
\tag{13}
\]
仅清 \(D\) 会漏掉真实模素数的边界碰撞。好素数对数连接、整 Betti 来源、全部坏支持与全素数 Taylor 成本已分别构造/列出；坏纤维上的全局整 log 延拓仍需另证。

令 \(A_i=Dr_i\)、\(T_k=\sum_i\epsilon_iA_i^k\)。投影行的真实整坐标前缀分母为
\[
\operatorname{lcm}_{k\le n}\frac{k^2}{\gcd(k^2,T_k)};
\]
完整 11 行恰为 \(L_n^2\)，兼容秩 6 商恰为
\[
\operatorname{lcm}_{k\le n}\frac{k^2}{\gcd(k,T_k)}.
\tag{14}
\]
但三者的公共分母增长指数均为 2。因为 \(T_1=N^2+N-1\)，
除它的固定有限个素数外，\(T_{p^h}\equiv T_1\not\equiv0\pmod p\)
强制所有最高平方分母。原坐标三者的增长指数均为 \(\log D+2\)。
故本族的投影 content 不改善固定 \(N\) 的公共前缀指数；fine 行成本仍要单独计算。

这把“真实投影”与“完整整模型”连接到了可检验的数学断言，也给出了不兼容压缩的具体来源。

## 5. 正例与一般目标模型：哪些接口已经统一

[三级 Dirichlet 整模型稿](period_holonomy_integral_models_20261005.md) 构造
\[
H_j(s)=\sum_{n\ge1}\frac{\chi_{-3}(n)}{n^j}
       \left(\frac{s}{1+s}\right)^n,\quad j=1,2.
\]
其真实微分秩和 Betti 整格均为 3：根单位对数是有理倍 \(2\pi i\)，因此这里可以完整清整。还给出唯一几何坏素数 3 的两次 blowup、全 \(\mathbb Z\) 的 proper regular 曲面与 SNC 约化边界；没有将其重数 2 的坏纤维误称 reduced/semistable，也未将曲面 regular 性误当成已建坏素数整 log 连接。

整数坐标变换及其整数逆，在每个尺度精确保留前缀分母：
\[
\delta_{H_j}(n)
=\left(L_n/3^{v_3(L_n)}\right)^j.
\tag{15}
\]
但它不保留序号 \(n^e\) 的逐项类型；在 \(n=p+1\) 真实出现新的一层 \(p\) 分母。按全部自然类型和排列核算，拉回前后最优自然三行预算都是 \(25/18\)，并没有拉回的额外收益。

[一般投影稿](period_holonomy_target_projection_20261005.md) 另给任意模数的 Lerch 系统
\(F_{a,j}(z)=\sum_{n\ge0}z^n/(mn+a)^j\)。
含 \(t\) 个非零残数的二阶滤波具有实际循环秩 \(2t+1\)；端点即使为零，函数秩仍可以很大。旧函数空间内的有理滤波不能真正删除 \(z=1\) 的 monodromy。共同整数前缀格用同余 Smith 数据处理，不能先逐行约掉 content 再忽略联合格。

还有一个跨全部权和模数的实际周期系数系统：非零整数周期序列 \(c(n)\) 的
\[
G_j(x)=\sum_{n\ge1}\frac{c(n)}{n^j}x^n,\qquad
\theta G_j=G_{j-1},\quad G_0\in\mathbb Q(x).
\]
其实际循环秩为 \(j+1\)，可用 \(L_n^j\) 整数化，真实前缀由全部 gcd 给出。代数覆盖加单项权重将原 Lerch 行转成此系统，能真实改变某些边界；三级字符模型是一个明确兼容整 Betti 格的实例。一般模数的低 de Rham 秩仍不自动给低秩 Betti 有理商，也不自动给无理性反证。

在模 6 的整数滤波中，还可以把纯周期要求与实际域改善一起计算：只要求纯 \(L\) 时像为 \(L/8\,\mathbb Z\)；若还要求 \(\sum c_r=0\) 从而真实消去 \(x=1\) 分支，则完整饱和格的像恰为 \(L/4\,\mathbb Z\)。这一固定指数 2 已证明，不是新增的渐近收益。它展示了如何在同一整格中计算“纯目标且保留所需解析域”的共同代价。

## 6. 研究方向据此收紧

本轮已经闭合的数值结论，是 (5)、(7)、(9)；新的结构结论是完整来源的秩 6 商、精确坏边界与全内容、整数坐标前缀不变而 fine 类型改变，以及一般实际周期系统的循环秩。它们有正文全尺度证明，不靠有限实例猜测。

目前统一框架最实质的未闭接口仍是：**假定一个尚未知数值关系，能否产生一个新有理芽，并实际消去哪项坏 monodromy。** 在上述原始 polylog 系统中，它们本来就有理系数；减掉一个假定有理端点常数不改变函数秩、正次数分母或延拓域，不能触发反证。这点现已由常数剪切引理明确证明。

后续应优先考察原文 §15 提到的多个两-log 乘积的共同 Hermite–Padé/过收敛系统，而不是把三个 log 直接 Hadamard 相乘：原文现有预算已出现 \(e^3>16\) 障碍。具体新目标必须先给出数值关系到规范正则芽的映射，再核其 Betti/de Rham 整比较、全部系数阶梯和合法解析叶；达到这个入口后才计算严格余量。三级、更多导子角色及椭圆周期都可纳入，尚未有完整输入者保留为待证对象。

本轮既有正例又有严格的模型限制，足以作为这些新系统的校准标准；没有把周期猜想或形式纯化当成解决全部奇数 ζ / Catalan 的定理。

## 7. 交付、文献与验证

四份技术稿及配套精确证书：
[CDT 机制](period_holonomy_cdt_mechanism_20261005.md)，
[目标投影与整格](period_holonomy_target_projection_20261005.md)，
[三级整模型](period_holonomy_integral_models_20261005.md)，
[五项完整模型](period_holonomy_dilog_model_20261005.md)。
[总览积分分类证书](period_holonomy_progress_20261005_verify.json)
独立核 (8)–(10) 的实际有理坐标；[书面审阅](period_holonomy_review_20261005.md)
记录各人的明确审查范围，[交付审计](period_holonomy_delivery_20261005.json)
记录文件散列、原件冻结与本地链接。

[本轮文献地图](../literature/period_holonomy_reading_map_20261005.md)
新增两份原始 PDF、234 页：Maximon/NIST 的二重对数原始论文，以及 CDT 作者站的 220 页单独快照；另存 DLMF 5.15、25.12 与 Stacks 01OF 三份原始 HTML。
固定来源、页数、SHA-256 与首页视觉身份见
[PDF manifest](../literature/manifest_period_holonomy_20261005.json)、
[网页 manifest](../literature/manifest_period_holonomy_web_20261005.json)。
已有 64 份原始 PDF 及此前研究/证书保持原字节，未替换固定 CDT v2。

[上一轮本原预算与正测度接口](odd_zeta_primitive_routes_progress_20261005.md)
及其全部旧报告冻结。本轮证明、直接推论、外部定理和仍缺条件均已分开。

