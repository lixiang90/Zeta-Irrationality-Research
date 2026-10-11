## 214. 一般 N 的第二类系数秩、实际矩阵判据与全局路线调整

2026-10-07。本轮取得新的结构性证明和同对象的算术改进，尚未取得新的 ζ/L 数值无理性或线性无关性定理。根据用户“每 4～8 轮俯瞰全局”的要求，现固定每 6 个完成的研究轮次回顾；本轮已提前进行[全局回顾](research_global_review_round214_20261007.md)，下次常规回顾为第 220 轮，协议保存在[研究导航文件](research_navigation_protocol.md)。

**一、一般 N 的周期系数秩已证明。** 主要混合模型有 n=44N−1，36N−1 个 Jacobi 方向和 8N+1 个纯 D 尾方向。新的[Schur 稿](catalan_mixed_actual_moment_schur_lemma_20261007.md)证明实际 Z 矩阵严格全正，全部允许 D 空间的矩映射可逆，给出精确尾部消元、实际核的图表达和最大子式恒等式。多项式对独立与实际矩阵满秩不再混同。

[第二类 jet 秩稿](catalan_mixed_second_kind_jet_rank_20261007.md)进一步证明完整 C 映射秩 44N−1，接触子空间上的残差 C1 秩 m=36N−2，对每个 N≥1 都成立。核心证明把假想系数依赖转为

\[
\Phi(z)\Lambda(z)-\Pi(z)=O(z^{58N}),\qquad
\Phi(z)=\frac{(1-z)^{6N}}{\sqrt{1-z^2}}.
\]

由 Phi 的一阶微分方程构造的多项式度数至多 58N−2，零阶至少 58N−1，因而恒零。这会迫使有理函数 Pi/Lambda 的对数导数在 z=−1 有留数 −1/2，与有理函数的整数阶数矛盾。它是全部 N 的纸面证明，不是从有限秩外推。

于是每个固定 mu 都有一个最大子式，在形式关系参数 gamma 中次数恰为 m，最高系数非零；至多 m 个复例外值。实际 mu 斜率也满秩。**仍不能据此排除反证关系给出的固定有理例外点。**

**二、剩余非零性已化为具体算子问题。** 标准形为

\[
\begin{bmatrix}v\\A+\mu B+\gamma I_m\end{bmatrix},\qquad
\Delta_N^{\rm obs}(\mu)=
\det\begin{bmatrix}v\\v(A+\mu B)\\\cdots\\v(A+\mu B)^{m-1}\end{bmatrix}.
\]

对固定 mu，观测行列式非零等价于整个池对全部复 gamma 满列秩。若仅需固定反证关系点，可证明较弱的无限 N 非零。Phi 方程只控制 C 核，不含实际 M0/Z0 的非齐次信息；它本身不足以证明 v 循环。原指定的删除一条尾行方阵也不同于整个池满列秩。

两次新的有界 producer 各执行一次：首先保存 N=1、模 101 的完整实际有理 pencil；第二次只读第一个已存 JSON，保存尾消元与循环矩阵。独立审核从原定义检查源代码，并从全部已存矩阵重算变换与观测幂。对 mu=1,2,−1,0，观测行列式模 101 为 100,71,29,32，均非零。因此这四个固定 mu 在 **N=1 对所有复 gamma** 的整个 44×43 池满秩。这不推广到任意 mu 或全部 N。准确审核与验证器范围见[有限证书记录](catalan_mixed_N1_saved_certificate_review_20261007.md)。

**三、有限处已对新行重新证明，原 Chebyshev 非零证书不能迁移。** [全有限处稿](catalan_mixed_jacobi_moment_finite_places_20261007.md)证明 4^d J_d∈Z[t]，使用实际逐行 dyadic 标量、全部小素数与高次幂 entry cap，并在完整原始列池上实施联合剪切后转回滤波列。对同一 red 对象，原安全下界为

\[
\liminf n^{-2}\log|\Delta_{\rm red}|
\ge-7849/3872
\]

（限于非零的反证有理行列式）。这是安全分母费用，不是最优或必要费用。旧标量的正改进必须在实处同时计入，不能凭改变归一化创造矛盾。

[尺度素数稿](cdt_mixed_jacobi_prime_content_20261007.md)证明 N=p 的许多 Jacobi 行已有 p 内容，原 p² 前导模板会消失；单个尺度素数只能给 O(N log N)，不能填补 N² 缺口。[完整内容因子稿](cdt_mixed_jacobi_primitive_content_20261007.md)给出全部素数和 powers 的精确 Newton 系数 gcd，避免交换 min 与 prime-power 求和。进一步，大奇素数的内容由两组半区间剩余类的交集精确给出。

仅用 65N<p<88N 的素数就产生真实 +529/4·N² 改进：这些素数不在原矩核分母范围，而每个有 T_p=44N−(p+1)/2 条 Jacobi 行带 p 内容。PNT 求和给出同一 red 对象新的安全下界

\[
\liminf n^{-2}\log|\Delta_{\rm red}|
\ge-15169/7744.
\]

这里未声称所有内容因子的渐近已经求出，也未声称整个接触格已有 primitive 基。

**四、实处缺口已经量化，下一步不能继续只看小余项。** [实处稿](catalan_mixed_jacobi_real_place_interface_20261007.md)精确移除所选纯 D 尾，保留完整实际 D_mu，给出残差 Gram 外积及 beta 因子。Jacobi Rodrigues 推导揭示 t=0 的拼接多项式；高阶余项虽然小，这个拼接项和 D_mu 尚未消除，不能把余项的衰减当完整行列式界。

同一 red 归一化下，当前 trace AM–GM 界为

\[
\limsup N^{-2}\log|\Delta_{\rm red}|
\le G_*+18t_*,\quad G_*\simeq598.8475,
\quad t_*:=\limsup N^{-1}\log\mathfrak T_N(\mu).
\]

原算术界需 t*<−251.297；上述实际内容区间改进把门槛改为 (−15169/4−G*)/18≈−243.95。这样的 trace 估计仍未证明。若另在 primitive Jacobi 行上重新应用原安全 cap，全部内容因子的理论收益至多 1872 log2·N²；这个收益不能再与同源的原 red 区间改进相加。故单独优化内容因子也不足以使当前粗 trace 比较成功。此为粗界的局限，不是完整行列式的不可能性证明。

新的[带权列接口](catalan_mixed_weighted_column_interface_20261007.md)直接以 monic shifted Jacobi 多项式作行列式不变的列变換，积分分部后保留实际 P−(3/2)D_mu 的双重积分，给完整的有限 Hadamard 界。它提供下一步可操作入口，尚无有利 N² 主项。主要投入改为精确残差外积/带权 Schur 的联合结构；并行用实际 M0/Z0 递推研究循环性。停止扩大 N=1 参数网格及 content-only 扫描。

**五、全局方向与退出条件。** 本轮把 β4、ζ7 非交错/交错模型、完整空间 holonomy 和非线性 wheel 路线放在同一“已证明接口—决定性缺口”表中。旧 β4 的无限非零已付但费用、衰减相差很大；ζ7 的投影与整模型已具体化，但非零和比较仍缺。特定固定类型的完整 holonomy 载体已有严格门槛，可逆变基或继续提高权重不能救该类型。它们不排除跨类型联合格或新函数载体。不同载体只在能写出具体有理 Taylor 芽、完整目标分支与整模型时升级。

接下来两轮若仍只得到一般秩或行范数，没有实际关系点非零或联合 N² 比较的新信息，就降低当前参数路线优先级，改支撑/核或载体。第 220 轮必须再次全局回顾；遇关键界或反例提前进行。

**审核、文献与当前进展。** 本轮新结构稿得到独立数学纸审，量词与未完成条件逐项列明；不是 Lean 形式化验证。新增两份 primary PDF 已存 literature，实际读取分别为 Derevyagin–Zhedanov 物理页 1～5、Baratchart–Yattselev 物理页 1～8，均非全文。前者假设矩行列式非零，后者要求弧外节点、固定 Jacobi 指数与 admissible family；不能直接支付当前缺口。精确范围与原 Catalan 两节源文件存档见[文献读取记录](../literature/cdt_mixed_second_kind_source_scope_20261007.md)。没有运行旧 producer、旧 guard、历史 prime scan、PSLQ 或 Lean；仓库同步已经完成，本轮未重复维护。最终指纹及执行、审阅范围见[本轮归档](../literature/manifest_cdt_mixed_moment_rank_global_review_20261007.json)。目标继续 active：已增加一般 N 的秩定理与真实算术收益，尚无新的数值无理性或线性无关性结论。
