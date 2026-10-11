# 显式 \(K_2\) 缺口研究进展：退化判定、整性与 Bloch 端点识别

日期：2026-10-04。承接[上一轮路线报告](odd_zeta_next_routes_progress_20261004.md)，继续当时提出的“候选类非零性—下降—垂直整性—真实调节子”检查。本轮给出固定构造的全局数学证明与精确代数证书，没有进行参数扫描。

**主要推进：原候选 \(T\) 满足整系数 \(4T=0\)；其非零 Catalan 开路径可通过有限 Bloch 链的端点差解释，平均后的类恰为 \(-4[i]\)。** 同时，所选 proper regular 算术模型的全部 codimension 1 tame 检验通过。这个结果完成了候选类的审查，改变了后续几何路线的输入。

ζ(7)、Catalan、固定混合值的无理性仍未证明；没有新增 Lean 形式化。以下结论只针对明确定义的构造及所述引理，不能视为通用方法已成立。

## 1. 原候选的退化有完整证明

上一轮曲线为

\[
C:\quad Y^2=s^8-14s^4+1,\qquad K=\mathbb Q(i,\sqrt2),
\]

两椭圆商 \(x_\pm=s\pm s^{-1},y=Y/s^2\) 上给出
\(S_\pm=\{u_\pm,F_\pm\}\)，拉回总和为 \(T\)。
旧报告只提出候选，并明确未证明非零；它的函数身份与 tame 计算保持有效。

本轮发现 \(T\) 被整个

\[
V_4=\langle(s,Y)\mapsto(-s,Y),\ (s,Y)\mapsto(s^{-1},Y/s^4)\rangle
\]

固定。共同商

\[
R=s^2+s^{-2},\quad W=Y/s^2,\quad
W^2=R^2-16,\quad t=(R+W)/4
\]

是有理曲线，且 \(K(C)/K(t)\) 恰为次数四的 Galois 扩张。
令 \(N\) 为 Milnor \(K_2\) integral transfer。
全部水平 tame 相消使 \(N(T)\) 来自常数
\(\kappa\in K_2^M(K)\)，Galois 公式给
\({\rm res}\kappa=4T\)。
在基点 \(P_0=(0,1)\)，\(u_\pm=1,F_\pm=-1\)，单位特化使
\(\kappa=0\)。因此

\[
\boxed{4T=0\quad\text{在 }K_2^M(K(C))\text{ 中成立。}}
\]

完整证明、原始定理与证书见[退化报告](odd_zeta_k2_descent_20261004.md)。
没有据此声称整系数 \(T=0\)，也没有未经 injectivity 将此关系移到某个指定模型的全局 Quillen \(K_2\)。

该证明推广为预检引理：若有限群 \(H\) 的整个商是 \(\mathbb P^1\)，
无分歧符号 \(\xi\) 被 \(H\) 固定，且有有理点 \(P\)，则

\[
|H|\bigl(\xi-{\rm res}\,{\rm sp}_{P}\xi\bigr)=0.
\]

零特化时即为挠类。往后寻找非恒定绝对周期，应先检查此种对称退化；
非平凡字符本身也不能替代非零证明。

## 2. 整性缺口已经解决，但没有挽救非零性

[整模型与垂直 tame 报告](odd_zeta_k2_vertical_20261004.md)明确使用
\(\mathcal O_K=\mathbb Z[\zeta_8]\) 上两图粘合的 proper 双覆盖。

- 残特征 \(p>3\)：纤维 smooth、几何单分量；所有符号函数为垂直单位。
- 残特征 \(3\)：两分量完整。四个交点的精确局部式
  \(u=Y-s^4+7,\ v=Y+s^4-7,\ uv=-48\)
  给 thickness 一的 regular node；无穷远同样 regular。
- 残特征 \(2\)：对**任意**离散赋值 \(v\)，
  \((\partial_vT)^4=1\)。特征二域没有非平凡四次单位根，故
  \(\partial_vT=1\)，覆盖全部解消分量，不需要遗漏 wild 分量的清单。

只在素数二上取适当正则解消后，所选模型的全部水平、垂直 prime divisor
均 tame 为一。因此 \(T\) 属于以 codimension 1 residue 核定义的无分歧 Milnor 群。
结论没有调用 mixed characteristic Gersten 去指定一个全局 Quillen lift。

对素数三的两分量核验只用于此所选模型，没有擅自推广为任意奇素数 blowup
的所有赋值陈述。素数二部分则确实是全赋值引理。

## 3. 非零 Catalan 信息在端点

令 \(B=(s_0,0)\)，\(s_0=(\sqrt6-\sqrt2)/2\)，
\(\gamma:P_0\to B\) 为原实路径。固定

\[
\eta(f,g)=\log|f|\,d\arg g-\log|g|\,d\arg f.
\]

本轮完整核算分支与实虚边界：

\[
\operatorname{Im}(\log u\,d\log F)
=\eta(u,F)+d(\arg u\log|F|).
\]

两商该边界项在本路径端点都为零，所以

\[
\boxed{\int_\gamma\eta_T=-4G.}
\]

同时 \(T\) 的所有绝对闭合 regulator 周期为零：
可由 \(4T=0\) 得到，也可独立由
\(H^1(C,\mathbb R)^{V_4}=H^1(\mathbb P^1,\mathbb R)=0\) 得到。
因此开路径非零与绝对类退化完全相容。完整分支、闭合 oval 四段相消及
单商修正的 \(\pm\pi\log2\) 边界见[regulator 报告](odd_zeta_k2_regulator_20261004.md)。

简单修补单商 tame 的
\(A_+=2S_+-\{2,(y-4i)/(y+4i)\}\)、
\(A_-=2S_-+\{2,(y-4i)/(y+4i)\}\)
仍被有理商对合 \(x\mapsto-x\) 固定，绝对 regulator 同样为零。
这一具体修补已完成检查，不能继续将它作为非零椭圆候选。

## 4. 端点类的存在、下降与精确识别都已补上

[端点 Bloch 报告](odd_zeta_bloch_boundary_20261004.md)进一步证明：

1. \(T_{\mathbb Q}=0\) 通过 Steinberg 正合性给有限链
   \(\delta\varepsilon_0=u_+\wedge F_++u_-\wedge F_-\)。
2. 对 \(V_4\) 与 \(\sqrt2\mapsto-\sqrt2\) 做八项 formal-chain 平均，
   得到不变链 \(\varepsilon\)，boundary 不变。
3. 在两端逐项取普通函数值，省去 \(0,1,\infty\)；
   一个局部 leading-unit 验证证明端点 boundary 为零。
   因此端点差确实属于 \(B(L)_{\mathbb Q}\)，
   \(L=\mathbb Q(i,\sqrt2,\sqrt3)\)。
4. 端点共轭均落在同一 \(V_4\) 轨道，故平均后的端点差
   \(\beta\) 被 \({\rm Gal}(L/\mathbb Q(i))\) 固定。
   四个固定 \(i\) 的嵌入给其完整 regulator 向量
   \((-4G,-4G,-4G,-4G)\)。
5. Borel–Suslin 全向量单射遂给

\[
\boxed{\beta=-4\,{\rm res}_{L/\mathbb Q(i)}[i]
       \quad\text{在 }B(L)_{\mathbb Q}\text{ 中。}}
\]

这里只使用完整四嵌入，未用高秩群中的单个实值推出类相等；
也不需要整数 Bloch transfer 的归一化选择。
\(\beta\) 因而来自 \(\mathbb Q(i)\) 的经典类。
\(4[i]\) 是一个整数 Bloch cycle，且 \(D(4[i])=4G>0\)，故非挠。
经典类本身早已知道；本轮推进的是它与该固定曲线端点构造的精确联系。

有限链的存在及其平均后的端点类已经识别，但目前仍没有
\(\varepsilon_0=\sum q_j[h_j]\) 的具体五项式清单与长度、高度估计。
这里也未指定规范相对 Quillen \(K_2\) lift 及全部端点 trivialization。

## 5. 对统一研究框架的修正

统一[动机背景](odd_zeta_global_strategy_20261004.md)仍然成立。
本轮结果说明，结构类别、整性与非零周期之后，还须给出能用于无理性的**有理方向和定量预算**。

固定整数类的完整调节子像若为离散格，其非零向量有正的长度下界。
尤其 \(\mathbb Q(i)\) 的秩一 Bloch 调节子格只给整数倍的一个周期；
重复取整数类不自动产生

\[
q_nG-p_n,\quad p_n,q_n\in\mathbb Z,\quad0<|q_nG-p_n|\to0.
\]

一个非零实格的生成元仍可能是有理数。
这个必要区别同样适用于高权奇数 ζ 的 Borel 输入。
本引理仅限固定完整整格；高秩单坐标投影、变化的格及变化的分母需要独立分析。

因此继续统一路线时，应要求一个具体相对族交付：

- boundary、实际端点、分支与纯目标值身份；
- 有理部分以及目标系数的整数化，并逐素数证明成本；
- 全族非零性，以及余项衰减超过清分母增长。

本轮有理商阻碍可在投入高权计算前筛掉对称退化族。
Catalan 权二的 Bloch 识别也给了一个完整示范；
它没有直接提供 ζ(7) 的高权复形识别或近似族。
目前尚无同时满足上述三项的 ζ(7) 或 Catalan 新构造。

## 6. 保存内容与验证

| 新报告 | 已证范围 |
|---|---|
| [对称退化](odd_zeta_k2_descent_20261004.md) | 整系数 \(4T=0\)、有限 Galois 有理商预检引理 |
| [整模型](odd_zeta_k2_vertical_20261004.md) | 所选 proper regular model 全部 codimension 1 tame；二上全赋值 |
| [真实路径](odd_zeta_k2_regulator_20261004.md) | 开路径 \(-4G\)、绝对周期零、单商边界修正 |
| [Bloch 端点](odd_zeta_bloch_boundary_20261004.md) | 端点类存在、平均、下降与 \(-4[i]\) 有理识别；固定整格范围 |

四份报告均配精确 Python/JSON 代数证书。一般 transfer、局部引理、解消及 Borel
定理由书面证明和原始文献支持，有限计算不替代它们。
各关键步骤经过独立只读复核，另保存[端点报告复核记录](odd_zeta_bloch_boundary_20261004_review.md)。

本轮新增 **8 份原始来源 PDF**，包括论文、作者教材/讲义和官方参考快照；
[阅读地图](../literature/k2_gap_reading_map_20261004.md)说明版本及适用范围，
[归档清单](../literature/manifest_k2_gap_20261004.json)记录原始来源、页数及 SHA-256。
PDF 原始字节保存，首页身份已渲染检查；归档不等于证明全文审定。

[交付检查](odd_zeta_k2_gap_delivery_20261004.json)核验报告、证书、PDF、旧冻结稿与本地链接。
旧研究报告及此前归档 PDF 保持原样。

