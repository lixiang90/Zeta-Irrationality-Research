# 四二次曲面 conifold 周期的校准文献与 M₄ 的实际五阶扩张

日期：2026-10-06。NEW 文献核查及纯证明。冻结 rank10、spin、connection_moments、lambda 输入均只读；未运行或 import 任何旧或同行 producer。本文不给 ζ(7) 的数值无理性定理。

## 1. 统一规范与本轮确切结果

沿用冻结 [connection_moments](cdt_odd_connection_moments_20261006.md) 的规范

\[
 \Phi(t)=\left[\frac{\Gamma(t)}{\Gamma(t+1/2)}\right]^4,
 \quad T(\epsilon)=\sum_{n\ge0}\Phi(n+1/2+\epsilon),
 \quad M_j=(-1)^j T^{(j)}(0).
 \tag{C1}
\]

齐次 CY 算子为

\[
 P=\theta^4-x(\theta+1/2)^4,\qquad \theta=x\frac d{dx},
 \quad y_0(x)=\sum_{n\ge0}\frac{(1/2)_n^4}{n!^4}x^n,
 \quad x=256z.
 \tag{C2}
\]

本轮文献检索找到了 BKΣZ 之后的真正原始工作：Bönisch 的 2023 年博士论文，以及 Bönisch–Golyshev–Klemm 的 2025 年固定 v1。其 fibering 方法给出了更完整的混合周期积分机制。不能把“已证明属于模形式的周期”与“本规范下的完整整周期矩阵、每个校准常数均已证明”合并成一句话。

本文独立证明一个可直接使用的正接口：M₄ 是下面明确五阶、非分裂扩张的真实边界值，而非只能泛称一个尚未描述的对数插入。

\[
 Z_4(x)=\left.\partial_\epsilon^4\left(x^\epsilon
       \sum_{n\ge0}\Phi(n+1/2+\epsilon)x^n\right)\right|_{\epsilon=0},
 \quad PZ_4=24\pi^2,\quad Z_4(1)=M_4.
 \tag{C3}
\]

其实际最小标量微分方程阶数是 5，见 §6。这没有把原 ζ(7) 的 actual rank10 系统降为 rank4，也没有给这个新扩张免费算术或解析信用。

## 2. BKΣZ 原件与所谓新版本

本轮另存的作者站 DbranesCYandMFs.pdf 与已有 ADEK.pdf **SHA256 完全相同**，都是 79 页作者快照。其新文件名为 [alternate_author_url](../literature/bonisch_klemm_scheidegger_zagier_alternate_author_url_20261006.pdf)。不能把不同 URL 或搜索引擎的抓取日期当成修订版或固定期刊版。arXiv 2203.09426 的 submission history 此次只列 v1。

原件 PDF 8–9 页给 MUM Frobenius/周期规范，PDF 26–27 页给 conifold 矩阵及 level8 个案，PDF 33–37 页 §4 给 Kuga–Sato 对应。在 PDF 36 页 (4.16) 中，三形式被拉回为模形式乘 dτ dz₁ dz₂；PDF 37 页 (4.28) 的文字保留乘法常数的范围。因此它证明的是周期对应的实质几何输入，不应据此把整张数值矩阵当成已完成的整 Betti 基校准。

已有 connection_moments M12–M14 已严格辨明：在同一 CY Frobenius 定义下 M₁=w₊/4；RWZ 固定 v2 PDF13 (30) 给

\[
 M_0=\pi^2 y_0(1)=16L(f_8,2),\qquad
 f_8(\tau)=\eta(2\tau)^4\eta(4\tau)^4.
 \tag{C4}
\]

此处没有从 (C4) 猜出 M₁ 或 M₄。root 本轮另行保存了 [Bailey–RWZ 合流的实际证明](cdt_odd_bailey_M1_period_20261006.md)，本文作者已实际全文独审，并实际核 McCrorie PDF32–34 (A.1) 与 RWZ v2 PDF13–14 (31)，得到

\[
 M_1=64L(f_8,3),\qquad w_+=4M_1=256L(f_8,3).
 \tag{C4a}
\]

本文不重复其证明；(C4a) 校准此 Frobenius 连接数值，但仍不声称完整整 Betti 基矩阵或 M₄ 已求值。

## 3. 找到的后续 fibering 原始文献

### 3.1 Bönisch 2023 年博士论文

新存 [99 页固定博士论文](../literature/bonisch2023_modularity_special_rank4_motives_thesis_20261006.pdf)，Bonn 博士答辩日期 2023-09-01，封面 June 2023；DNB 存档的网页日期不构成新论文年份。

实际读取 PDF87–96（印刷79–88），其中：

- PDF87/印刷79 的 Theorem12：十二个 hypergeometric CY family 的 w±、e± 为相关 newform 的周期/拟周期；包括 half⁴。
- PDF91/印刷83 的 Table6.2：half⁴ 的 rank3 fibering indices 为 half³，参数 (k,l,β)=(1,1,1)，拉回 level 为 16。这个 level16 形式需要与 level8 newform 经实际 old/twist 关系比较，不能直接改标为 f₈。
- PDF92–93/印刷84–85 的 Theorem13：引入 f、meromorphic partner F 及带非零留数的 g，周期类在合适的一维 Tate 格模下给出 a±。非零留数的 integral 只能在保留该格及所选 contour 的意义下使用。
- PDF94–95/印刷86–87 的 Theorem14：b,c,d 为 CM 点间的、必要时正则化的积分。书面详细证明的主例是 quintic；其它 family 使用同一有限 monodromy/cohomology 程序。本文实际读取定理及正文，但未执行这些外部程序或重新校准其全部周期格。
- PDF96/印刷88 的 Table6.3 明列为 numerical height identities。half⁴ 行的 −3log2 不能当作一个已证明的 M₄ 求值公式。

因此这是比早期“完整矩阵数值识别”更强的可用来源，但它没有在读到的原页上给本项目 M₄ 的 critical L-value 闭式。

### 3.2 Bönisch–Golyshev–Klemm 2025 固定 v1

新存 [Fibering out Calabi–Yau motives, arXiv2510.03939v1](../literature/bonisch_golyshev_klemm2025_fibering_calabi_yau_motives_v1_20261006.pdf)，11 页，实际全文读取。§§2–4 的详细主例为 quintic。

PDF7 的 Theorem1 把 w±、e±、a± 及明确缩放的 cocycle 对应到 f₅₀、F₅₀、g₅₀。其中 f₅₀=5f₂₅−20f₂₅(2τ)，不能沿用 2023 lecture 中未带 5 的记号。PDF8–9 的 Theorem2 给 b,c,d 的 CM open contour 及减去的实际奇部，保留 g₅₀ 留数导致的路径差。

PDF10 AppendixA 第一行再次给 half⁴→half³ 的 (1,1,1) fibering 和 level16。其余 family 可类比，但本文不把主例 Theorem1 的所有缩放常数自动迁移到 half⁴。PDF9 Outlook 对 height/L′ 关系仍使用 conjectural/numerical 的范围，explicit algebraic correspondence 的更多细节也留作后续工作。

这篇论文值得作为下一步真实 cycle transport 的方法输入：固定 fibre map，追踪实际 monodromy-invariant contour combinations，按留数规范减去奇部，再比较同一规范的形式与周期。它没有允许略去 contour、缩放、Tate 格，或将本项目 ε⁴ 扩张自动当作其 rank4 mixed period matrix。

## 4. 其它本轮保存文献的准确作用域

- [2023 IHES lecture](../literature/bonisch_2023_fibering_mirror_quintic_20261006.pdf)，27 页。实际全文读。PDF20–22 是上述 quintic 后续论文的前身：pure block 有证明路径，nonzero-residue/mixed height 仍称 work in progress。它不是四二次曲面 M₄ 的证明。
- [Candelas–de la Ossa–McGovern 2025 固定期刊版](../literature/candelas_de_la_ossa_mcgovern2025_weight4_ratios_journal_20261006.pdf)，39 页；另存 [arXiv2410.07107v2](../literature/candelas_de_la_ossa_mcgovern2025_weight4_ratios_v2_20261006.pdf)，43 页。实际读期刊 PDF1–5、12、17–18、23、25、33–39；v2 只核封面及版本元数据。期刊 PDF12 对 BKΣZ 个案证明作背景说明；PDF2、23、25 明确当前数值/Padé identities 及 continuation 的 conjectural 范围。因此不能用它补本 M₁/M₄ 的校准证明。
- [Katz–Klemm–Schimannek–Sharpe 2024 期刊存档](../literature/topological_strings_noncommutative_resolutions2024_20261006.pdf)，88 页含大学封面。实际读 PDF44–47/期刊43–46 的四二次曲面两 MUM、Γ-class 和 integral brane charge 规范，以及相关命中段落。它有实际整规范输入；此次未发现该段给 conifold M₁/M₄ 的 exact modular L-value 比较。没有认领全篇审阅。
- [Golyshev 2023 arXiv2308.10813v1](../literature/golyshev2023_l_derivatives_biextensions_v1_20261006.pdf)，10 页。实际读 PDF1–7 的假设、DLD motivic theorem 和 biextension 构造；其 L′ 比较明确是 numerical evidence。所列七个非共振原 family 不包含 half⁴，所以连其假设也不能直接全套到本 M₄。

检索没有找到某证明，只是本轮读取范围的结果；不是不存在这种证明的定理。全部 PDF 的固定来源、页数、SHA256、实际 read scope 与下载失败记录保存在 [新 manifest](../literature/manifest_cdt_odd_classical_conifold_calibration_20261006.json)。

## 5. 四二次曲面的精确 fibering 入口

BGK AppendixA half⁴ 行可直接逐系数独立验证：

\[
 y_0(x)=\frac1{2\pi i}\oint_{|t|=1/2}
 \frac1{1-t}\,
 {}_3F_2\left(\tfrac12,\tfrac12,\tfrac12;1,1;
                     \frac{x}{4t(1-t)}\right)\frac{dt}{t},
 \qquad |x|<1.
 \tag{C5}
\]

展开 rank3 函数后第 n 项为

\[
 \frac{(1/2)_n^3}{n!^3}\left(\frac x4\right)^n
 \frac1{2\pi i}\oint t^{-n-1}(1-t)^{-n-1}dt
 =\frac{(1/2)_n^3}{n!^3}\left(\frac x4\right)^n\binom{2n}{n}
 =\frac{(1/2)_n^4}{n!^4}x^n.
 \tag{C6}
\]

在该圆上 |4t(1−t)|≥1，任意 |x|≤r<1 时展开绝对一致收敛，故交换积分和求和合法。x=1 涉及 pinch；真正连接周期必须像 BGK §3 那样处理 transported cycles，而不能把整个圆上的一次形式值等同全部继续分支。这条公式是全 x 的证明，不是若干 n 的检查。

## 6. M₄ 的 actual rank5、非分裂接口

在 |x|<1 的一个固定 log x 分支上定义

\[
 \mathcal S(\epsilon,x)=x^\epsilon
      \sum_{n\ge0}\Phi(n+1/2+\epsilon)x^n,
 \qquad Z_j=\left.\partial_\epsilon^j\mathcal S\right|_0.
 \tag{C7}
\]

Gamma 函数的递推给 n≥1 的全尺度恒等式

\[
 (n+\epsilon)^4\Phi(n+1/2+\epsilon)
 =(n-1/2+\epsilon)^4\Phi(n-1/2+\epsilon).
\]

所以每一非首项均在 P 下精确相消，而首项留下

\[
 \boxed{P\mathcal S=\epsilon^4\Phi(1/2+\epsilon)x^\epsilon.}
 \tag{C8}
\]

对 ε 求导，PZ_j=0（0≤j≤3），且 Φ(1/2)=π² 给

\[
 PZ_4=24\pi^2,\qquad
 (\theta P)Z_4=0,\qquad
 \theta P=\theta^5-x(\theta+1)(\theta+1/2)^4.
 \tag{C9}
\]

故 order≤5。单绕 x=0 的实际继续只有 x^ε 乘 e^{2πiε}，从而

\[
 Z_j\longmapsto\sum_{k=0}^j\binom jk(2\pi i)^{j-k}Z_k.
 \tag{C10}
\]

Z_j 的 log^j x 最高系数都是 Φ(n+1/2) 的幂级数，即 π²y₀(x)≠0。因此 Z₀,…,Z₄ 以不同最高 log 次数在 C 上线性无关，Z₄ 的五个局部 monodromy translates 张成它们。任何阶数 d 的 rational scalar ODE 在普通点的解空间只有 d 维，故 actual order≥5。结合 (C9)，Z₄ 的最小阶数恰为 5。

更精确地，θP 的解层通过 P 投影到常数解层，kernel 为 P 的四维齐次层。若此扩张分裂，其 x=0 monodromy 将是四阶齐次 MUM block 与一维常数 block 的直和，nilpotency length 至多4；(C10) 实际为 length5，矛盾。因此该真实扩张非分裂。这个论证不需猜测 PV 群、数值拟合或额外 Sp₄ 假设。

还可直接核 rational particular 的障碍：P 在 0 的 indicial 为 ρ⁴，在 1 的 leading indicial 为 −ρ(ρ−1)²(ρ−2)；其它有限点 ordinary。这些均不允许 rational particular 有有限极点。若 R 为 polynomial，最高项 r_d x^d 在 PR 中给 −(d+1/2)⁴ r_d x^{d+1}，对所有 d≥0 不为零，故 PR=24π² 无 rational 解。这只排这个明确 P 的 rational particular，并非全部周期或扩张方法。

最后，对于 ε 的充分小 compact 圆，Γ ratio 的 uniform Stirling 界给 Φ(n+1/2+ε)=O(n⁻²)，Cauchy 公式保证任意固定 ε 导数的同类一致可和界。故 x→1⁻ 的边界值可与四次 ε 导数交换；x^ε 的 log x 在该极限消失，得到

\[
 \boxed{Z_4(1)=T^{(4)}(0)=M_4>0.}
 \tag{C11}
\]

这是新正接口：后续应比较 **实际 θP 扩张** 与模形式/正则化 integral 的 regulator 数据，而不是把 M₄ 直接放入原四维齐次周期列表。M₄ 是否有精确 L-value/height 表述、该扩张的完整整模型及允许解析叶仍需另外证明。

## 7. 证书与审核范围

新增同名 `_verify.py/json` 仅做固定 symbolic 检查：Gamma recurrence 对应的 rational ratio、(C6) 二项式关系、ε⁰至ε⁴ forcing、P 的 ordinary coefficients 与两个 indicial、θP 左乘次序、(C10) Jordan chain。程序不作数值拟合、prime/参数扫描或外部 producer 调用。正文全尺度证明不由有限检查替代。作者仅首次执行一次，17 项全部通过；无执行失败或再次运行。

root 已实际阅读全文及本稿的新 PY/JSON（只读，未执行）；其独立数学审阅重点为 §§5–6 的固定圆一致展开、全尺度 Gamma 递推、五个实际 log branches、Jordan length5 与非分裂、rational particular 的有限极点及无穷远障碍、ε 一致收敛和端点。文献 §§2–4 仅读本稿所准确列出的原件阅读范围与报告，没有重新阅读全部八份原件，因此不登记为八份原件的独立全文审阅。

helper_tensor_budget 已实际只读 §6/C7–C11，独立核对全尺度 Gamma 递推、forcing 常数24π²、五个实际继续分支与最小阶5、Jordan5 的非分裂、rational particular 障碍以及 uniform ε 的端点求导；没有审本稿文献 §§2–4，也未执行 producer 或认领完整整模型。

root 新 Bailey 稿由作者另作实际全文独审，其记录与本稿的审阅分别记载，互不替代。本稿至此冻结；新双边级数的 M₄ 归约另稿保存，不在冻结正文中追加。
