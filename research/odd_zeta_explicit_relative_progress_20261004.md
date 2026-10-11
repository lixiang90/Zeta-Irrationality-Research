# 显式端点与高权矩消元：本轮研究进展

日期：2026-10-04。承接[上一轮 K₂ 缺口研究](odd_zeta_k2_gap_progress_20261004.md)，保存原报告与论文原件。
本轮完成四条可继续使用的数学输入：Catalan 的四项显式链与整系数 \(T=0\)；
两类纯 ζ(7) 近似在指定参数区间的真实本原预算排除；
普通 Rodrigues 族的实际非零性及精确指数；
一个同时消去多阶对数矩的显式整数候选。

**这些是本项目内部推导与复核的结果，不声称全球新颖；ζ(7)、Catalan 及固定混合值的新无理性证明仍未得到。没有新增 Lean 形式化。**
有限精确证书验证代数输入；全尺度结论依靠各报告中的书面证明。

## 1. 原 Catalan 曲线的缺口：从存在性变成四项公式

[显式 Steinberg 报告](odd_zeta_explicit_steinberg_20261004.md)保留
\(K=\mathbb Q(i,\sqrt2)\) 与原曲线 \(C:Y^2=s^8-14s^4+1\) 上的函数 \(u_\pm,F_\pm\)。
在有理商
\[
R=s^2+s^{-2},\quad W=Y/s^2,\quad
W^2=R^2-16,\quad t=(R+W)/4
\]
上引入
\[
\rho_+=-i\frac{t+i}{t-i},\qquad
\rho_-=-i\frac{t-i}{t+i},\qquad \rho_+\rho_-=-1.
\]
直接代数给
\[
F_\pm=-\frac{u_\pm-\rho_\pm}{1-\rho_\pm u_\pm},
\qquad
(1-\rho_\pm/u_\pm)(1-\rho_\pm u_\pm)=-2\rho_\pm.
\]

因此原符号 \(T=\{u_+,F_+\}+\{u_-,F_-\}\) 在**整系数 Milnor \(K_2(K(C))\)** 中已满足
\[
\{u_\pm,F_\pm\}=\{\rho_\pm,2\},\qquad
\boxed{T=\{-1,2\}=0.}
\]
这是上一轮 \(4T=0\) 的加强，来自直接 Steinberg 关系，毋须再消去未知 torsion。
它也使总符号在任何离散赋值下的 tame 为 1；该陈述没有自动给出一个指定整模型上的规范 Quillen lift。

在有理 pre-Bloch 群中，实际四项链为
\[
\boxed{\varepsilon_0=
-[\rho_+/u_+]-[\rho_+u_+]
-[\rho_-/u_-]-[\rho_-u_-],\quad
\delta\varepsilon_0=
u_+\wedge F_++u_-\wedge F_-.}
\]
它本身已有原两 involution 的对称性，无需八次平均。
只有 \(\rho_\pm\) 等辅助函数降到有理商；四个链参数仍在 \(K(C)\)，没有把原曲线改判为 genus zero。

在原实路径 \(P_0=(0,1)\to B=((\sqrt6-\sqrt2)/2,0)\) 上，
令 \(A=2+\sqrt3\)，有
\[
\varepsilon_0(P_0)=-4[-i],\qquad
\varepsilon_0(B)=-[A]-[A^{-1}]-[i]-[-i].
\]
八个列明且非退化的五项关系直接把端点差化为
\(\boxed{-4[i]}\)；有理身份不再依赖 Borel 注入来识别它。
整系数端点 cycle 及其有限 torsion 关系另在报告中处理，没有把有理等式当成整系数消 torsion。

Bloch–Wigner 实 primitive 与分支兼容的完整复 Li₂ primitive 均已写出。
实际开放积分仍为 \(\int_\gamma\eta_T=-4G\)，闭路调节子为零，两者相容。
这解释了固定曲线为何能承载 Catalan，却不能仅凭闭路类产生无理性：
我们已得到精确周期身份，尚未得到随尺度变化的小整数形式。

## 2. 新的纯 ζ(7) 与 Catalan 积分族：先核真实分母

[cyclotomic Mellin 报告](odd_zeta_cyclotomic_mellin_20261004.md)定义
\[
J_k(P)=\frac1{(k-1)!}\int_0^1
\frac{(-\log t)^{k-1}P(t)}{1+t^2}\,dt.
\]
整数除法 \(P=(1+t^2)Q+A+Bt\) 精确给
\[
J_k(P)=A\beta(k)+
B\frac{2^{k-1}-1}{2^{2k-1}}\zeta(k)
+\sum_m\frac{Q_m}{(m+1)^k}.
\]
因此 \(P(i)=A+iB\) 决定纯目标或污染；“积分为正”不能替代这个检查。
对于 \(P_n=t^{an}(1-t)^{bn}\)，纯 ζ 余类是
\((2a-b)n\equiv2\pmod4\)，纯 β 余类是 \((2a-b)n\equiv0\pmod4\)。
部分参数根本不存在纯 ζ 子列，结论只沿存在的子列陈述。

对有理项约分后的真实分母 \(M_n\)，报告逐素数证明了线性移动窗口
\[
\frac{(a+b)n}{h+1}<p<\frac{an}{h},\qquad hb<a
\]
内的精确赋值 \(v_p(\text{有理项})=-k\)：
β 方向用所有 \(h\ge1\)，原 ζ 方向用 \(h\ge2\)。
相关非零交错部分和只产生有限个固定坏素数，最终离开窗口。
这给全部尺度的实际分母下界，非有限试算或统一 LCM 粗估。

若有理项为 \(r/M\) 已约分，目标系数为 \(BC/D_0\)，整数对
\((MBC,-D_0r)\) 的完整 gcd \(g\) 满足
\(g\mid D_0|BC|\)。
因此已允许全部约分，而不是假定 content 很小。
把真实分母下界、积分 Laplace 指数和这一 gcd 引理合并，得到：

| 具体族 | 已严格排除的固定整数参数 | 排除内容 |
|---|---|---|
| \(t^{an}(1-t)^{bn}\)，纯 \(G\)（\(k=2\)） | \(a\ge4b>0\) | 完整约分后的整数线性形式指数发散 |
| 同族的纯 ζ(7) 子列（\(k=7\)） | \(a\ge4b>0\) | 同上；只沿存在的纯目标子列 |
| \(tR(t^2)\)，\(R=u^{an}(1-u)^{bn}\)，纯 ζ(7) | \(a\ge2b>0\) | 同上；已按 \(u\) 次数计费 |

第三行利用
\[
2^kJ_k(tR(t^2))=
I_k(R)=\frac1{(k-1)!}\int_0^1
\frac{(-\log u)^{k-1}R(u)}{1+u}\,du
\]
优化变量预算，ζ(7) 系数准确为 \(63R(-1)/64\)。
在边界比值 \(a/b=4\) 和 \(2\)，净下界分别由严格有理对数界认证，随后用分段单调性覆盖整个区间。

**这些是具体族的排除定理，不是所有单核方法的不可行定理。**
平衡参数 \(a=b\)、小比值、带符号多项式、尺度组合和更高极点均未排除。
另有非负整数分子的统一 LCM 障碍 \(\liminf D^{-1}\log J_k\ge-\log4\)，
但它只控制安全乘子；不能取代具体族的真实分母及 gcd 证明。

## 3. 普通 Rodrigues：实际非零，但指数没有改善

[相对族审计](odd_zeta_relative_family_audit_20261004.md)给出
\[
R_{n,A}(u)=\frac1{n!}\frac{d^n}{du^n}
[u^{(A+1)n}(1-u)^n],\qquad A\ge1.
\]
它有整数系数，消掉 \(n\) 个普通矩，
\(R_{n,A}(-1)\ne0\)，并经 parity 化生成纯 \(1+\mathbb Q\zeta(7)\) 或纯 \(1+\mathbb QG\) 的线性形式。
尽管分子有变号，完全单调的真实积分权与分部积分仍证明两个目标积分严格为正。

但固定 \(A,k\) 时
\[
\boxed{\lim_{n\to\infty}\frac1n\log I_k(R_{n,A})
=A\log A-(A+1)\log(A+1).}
\]
它恰为原二项式的绝对指数。高阶导数中的 \(u^{-n}\) 抵消新增 \(u^n\)；
普通矩消元不能自动改善含对数端点的积分预算。
标准乘子后的失败已严格证明；这一带符号族的完整本原 content 仍待研究。

这个 Rodrigues 整族不能靠增加普通正交阶数改善上述指数。
下一步可优先处理多个对数阶或改变整个 mixed 函数系统；
这里没有排除所有其他普通正交构造。

## 4. 多阶对数矩的实际整数候选

[log-moment 候选报告](odd_zeta_log_moment_candidate_20261004.md)已构造
\[
R_{n,q}(u)=
\sum_{r=0}^{qn}(-1)^r
\binom{qn}{r}\binom{n+r}{n}^{q}u^r,\qquad q,n\ge1.
\]
其 Mellin 函数有完全显式的因式：
\[
\boxed{\int_0^1u^{z-1}R_{n,q}(u)\,du=
\frac{(-1)^{qn}(qn)!}{(n!)^q}
\frac{\prod_{j=1}^n(z-j)^q}{\prod_{r=0}^{qn}(z+r)}.}
\]
逐极点留数证明它成立；分子零阶直接证明
\[
\int_0^1u^m(-\log u)^jR_{n,q}(u)\,du=0,
\qquad 0\le m<n,\ 0\le j<q.
\]
反向次数论证证明该矩问题一维，\(R(0)=1\) 给唯一整数归一化。
因此现在有可计算、可证明的具体对象，无需先假设某个泛用“完美性”定理。

欧氏除法给严格纯 ζ(7) 形式
\[
I_7(R_{n,q})=\frac{63B}{64}\zeta(7)+S,
\qquad B=R_{n,q}(-1)>0,\quad S\in\mathbb Q.
\]
没有低阶 ζ 污染。对 ζ(7)，必须区分：

- \(q=6\)：只消 \(\log^0,\ldots,\log^5\) 矩，不能截断最高 \(\log^6\) 项；
- \(q=7\)：完整消去前 \(n\) 个目标对数矩，得到精确尾项
  \[
  I_7(R_{n,7})=\frac{(-1)^n}{6!}
  \int_0^1\frac{u^n(-\log u)^6R_{n,7}(u)}{1+u}\,du.
  \]

尾项身份还没有证明实际非零或净衰减。
安全界 \(|I_k|\le B/(n+1)^k\)（\(q\ge k\)）不足，
因为 \(B\ge\binom{2n}{n}^{q}\) 已指数大。
多项式本原、矩问题唯一、目标系数非零，都不能替代指定端点值非零。

## 5. 深方法如何落实为下一阶段的任务

本轮[新增文献地图](../literature/explicit_relative_reading_map_20261004.md)保存五份原始 PDF。
Fischler–Rivoal 的 mixed polylog Padé 同时控制多个函数、无穷远消零和奇点端点；
Prévost–Sorokin 的循环函数系统在低权实现真正的 Apéry 逼近；
Krattenthaler–Rivoal 的 Catalan 工作说明实际分母可以显著优于粗 LCM，
仍须检查最终净预算。这些提供具体机制，而非全部奇 ζ 的统一无理性定理。
来源及版本均在阅读地图中逐条链接，不能把不同 Padé 问题的唯一性移植到这里。

据此下一阶段按如下依赖继续：

1. **先解决 \(q=7\) 具体端点值。** 从 Mellin 因式或 Cauchy transform 推导独立的积分/轮廓表达，证明其非零；不能预设 ζ(7) 无理。
2. **在同一表达中比较指数。** 同时认证余项、目标系数 \(B\) 的实际增长，再用整数值多项式及逐素数估值分析 \(S\) 的最小分母和完整 gcd。
3. **如单核预算不能闭合，改变 mixed 函数系统。** 引入多变量积分或循环 polylog 条件，先证明新问题唯一、真实端点投影纯净和算术成本，后谈目标无理性。

原 ζ(5) 方法的多项式消元与二次尺度预算仍是对照，
见[前阶段路线报告](odd_zeta_next_routes_progress_20261004.md)；
本轮线性 Mellin 输入没有自动填补其 ζ(7) 版本的所有缺口。
动机与调节子帮助识别周期、控制边界；真正剩余的跨越是
**在已纯化目标上同时取得实际非零与约分后趋零的整数形式**。

## 6. 文件、证书与冻结范围

| 分支 | 书面证明 | 精确证书 |
|---|---|---|
| 四项链、\(T=0\)、实与复 primitive | [报告](odd_zeta_explicit_steinberg_20261004.md) | [脚本](odd_zeta_explicit_steinberg_20261004_verify.py)／[JSON](odd_zeta_explicit_steinberg_20261004_verify.json) |
| 真实分母窗口及本原排除 | [报告](odd_zeta_cyclotomic_mellin_20261004.md) | [脚本](odd_zeta_cyclotomic_mellin_20261004_verify.py)／[JSON](odd_zeta_cyclotomic_mellin_20261004_verify.json) |
| 普通 Rodrigues 与独立 log 矩核查 | [报告](odd_zeta_relative_family_audit_20261004.md) | [脚本](odd_zeta_relative_family_audit_20261004_verify.py)／[JSON](odd_zeta_relative_family_audit_20261004_verify.json) |
| 多阶 log 矩候选及唯一性 | [报告](odd_zeta_log_moment_candidate_20261004.md) | [脚本](odd_zeta_log_moment_candidate_20261004_verify.py)／[JSON](odd_zeta_log_moment_candidate_20261004_verify.json) |

[独立复核记录](odd_zeta_explicit_relative_review_20261004.md)注明检查范围与限制。
[交付检查](odd_zeta_explicit_relative_delivery_20261004.json)核报告、证书、本地链接、
新增原始 PDF 的签名、页数、SHA-256 与首页身份，以及此前冻结材料的散列不变。
没有参数扫描；没有把有限样本、视觉检查或散列完整性当作数学定理。

