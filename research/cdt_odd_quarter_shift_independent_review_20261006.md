# 四分之一移位模型与两层 packet 的独立审阅

日期：2026-10-06。审阅者 quarter_model_review；本稿为 NEW 证明记录，没有运行、import 或修改冻结数学 producer，没有扫描素数、参数或次数。

实际读取了 [新模型稿](cdt_odd_quarter_shift_full_model_20261006.md)全文 Q1–Q13、§6，以及冻结的 [原 H Frobenius/Smith 稿](cdt_odd_classical_frobenius_smith_20261006.md)、[P₄ 单值证书说明](cdt_odd_classical_spin_monodromy_20261006.md)及[双边端点校准稿](cdt_odd_classical_M4_bilateral_reduction_20261006.md)正文。下述审阅覆盖实际微分模型、精确前缀分母及给定的 split-prime 两层 packet；不审认任何尚未读取的 mixed determinant 成本稿或新数值定理。

## 1. 最小 rank5 与真实 conifold 障碍

取 cₙ=[(3/4)ₙ/(5/4)ₙ]⁴，J=Σcₙxⁿ、θ=x∂ₓ。逐系数递推为

\[
(n+1/4)^4c_n=(n-1/4)^4c_{n-1}\quad(n\ge1).
\]

零次项是 (1/4)⁴。故 K_Q=(θ+1/4)⁴−x(θ+3/4)⁴ 满足 K_QJ=1/256，且 K_Q(x⁻¹⁄⁴y)=x⁻¹⁄⁴[θ⁴−x(θ+1/2)⁴]y。Kummer twist 是 rank1 可逆张量函子，保存四维齐次模的不可约性；冻结输入的 Sp₄ 四维标准模因此给本稿不可约齐次四阶商。

独立核验有理特解排除：0处极点阶 ρ∈−ℕ 的 indicial 因子 (ρ+1/4)⁴ 不为0；1处 gauge 解析非零，indicial roots 0,1,1,2 不容负整数极点；其余有限点 ordinary 不容极点。若有 C(x) 特解 R，则 R 为多项式；最高项 r_dxᵈ 产生不可消的 −(d+3/4)⁴r_dxᵈ⁺¹，与常数 forcing 矛盾。

形式 companion 扩张 0→1→E→E_K→0 映到实际五函数空间，常数线的像非零。任何非零微分核避开常数线，向不可约四维商的像遂为全商且映射单射；它就给 E 的四维补模。这样的补模等价于该非齐次一阶 companion 系统的有理特解，已被排除。故实际 {1,J,θJ,θ²J,θ³J} 恰有 rank5，扩张非分裂，θK_Q 的五阶数也是实际最小阶数。

端点因子再次核为 [Γ(3/4)/Γ(5/4)]⁴=1024π⁴/Γ(1/4)⁸。结合实际读取的双边稿固定 e=1/4 校准，Q3 的两个 L 值系数分别为 Γ(1/4)⁸/(32π⁴)、−Γ(1/4)⁸/(16π⁵)，没有采用未知数值周期的 Galois 共轭。

cₙ=Cn⁻²+O(n⁻³)、C>0 给 J′(x)=−C log(1−x)+O(1)，x→1⁻；积分给 J(x)=J(1)+C(1−x)log(1−x)+O(1−x)。θK_Q 是 Fuchsian 五阶算子。若此实际分支在1的 monodromy 平凡，正规奇点的 moderate-growth 单值解必在1 meromorphic；J(1)有限便使其 holomorphic，进而 J′有界，矛盾。因此实际 monodromy 非零，减去有限端点值也无法消除。此处没有声称单个实轴渐近自动计算完整局部 monodromy 矩阵。

## 2. 精确 J 分母与 H 的 sharp witness

对奇素数 p，q=pʲ、n=kq+r，0≤r<q，长度 q 的两个 arithmetic progressions 各恰有一个 q 的倍数，完整 blocks 相消。若 q≡1(4)，分子、分母计数阈值分别为 (3q+1)/4、(q−1)/4，所以单层损失 δ_q=−1 恰在 [(q−1)/4,(3q+1)/4)。若 q≡3(4)，阈值分别为 (q+1)/4、(3q−1)/4，δ_q=+1 恰在 [(q+1)/4,(3q−1)/4)。于是 v_p(cₙ)=4Σδ_q；q>4n+1 无贡献，2处全部因子为 unit。

对 0≤n≤N，记 M=4N+1。p≡1(4) 的最坏层数≤a=⌊log_pM⌋，n=(pᵃ−1)/4≤N 在每个低层余数都是 (q−1)/4，全部给−1，更高层为0。p≡3(4) 只有偶数层可负，最多 a=⌊log_(p²)M⌋；n=(p²ᵃ−1)/4 在偶层余数为 (q−1)/4，在奇层余数为 (3q−1)/4，恰为正带上端而贡献0。两类同一个实际系数均达到相应上界。因此 Q10 为精确最小公共分母：

\[
D_J(N)=\prod_{p\equiv1(4)}p^{4\lfloor\log_p(4N+1)\rfloor}
\prod_{p\equiv3(4)}p^{4\lfloor\log_{p^2}(4N+1)\rfloor}.
\]

算术级数素数定理给第一类首层 log 和为 M/2+o(M)；其高层及第二类偶层总和 O(√M log²M)。乘4得 logD_J=8N+o(N)。inert prime 并未在全前缀消失，例如 c₂=(7/15)⁴有3⁴分母。

对旧 aₙ=[(n−1)!/(1/2)_(n+1)]⁴，独立重数法是：v_p((n−1)!) 在每层为⌊n/q⌋−1_(r=0)，而奇乘积 1·3·…·(2n+1) 的每层为⌊n/q⌋+1_(r≥(q−1)/2)。2^(n+1) 不影响奇素数。故每层为 −4[1_(r=0)+1_(r≥(q−1)/2)]，两指示互斥。q>2n+1 无贡献。n=(pᵃ−1)/2、a=⌊log_p(2N+1)⌋ 在所有低层余数均为 (q−1)/2，恰达 −4a。2处指数为4[n+1+v₂((n−1)!)]=8n−4s₂(n−1)≥0。故 Q13 精确成立：

\[
D_H(N)=\operatorname{odd}(\operatorname{lcm}(1,\ldots,2N+1))^4,
\qquad \log D_H(N)=8N+o(N).
\]

四条 Euler derivatives 只乘 nⁱ 整数，而 J/H 本身已在各自 source 中，故它们共同前缀分母与原函数相同。此核验没有推出完整 rank10 的 F 分母最优性。

## 3. split-prime whole-prefix packet

下面独立审查根任务给定的新 J 两层公式，未假定其源于晶体 comparison。取 p≡1(4)，prefix 0≤n<N，并要求 p²>4N+1。令 h=(p−1)/4、d=(p−1)/2。上一节全层计数在此窗口只剩首层，故 v_p(cₙ)=−4 恰在 h≤n mod p≤h+d，其余系数 p-integral。设 U=p⁴J，仅在此 prefix 使用。

定义 p-integral 多项式

\[
T(x)=\sum_{j=0}^{d}\left[\frac{(1/2)_j}{j!}\right]^4x^j,
\quad V(x)=\left.\partial_\rho\sum_{j=0}^{d}
\left[\frac{(1/2+\rho)_j}{(1+\rho)_j}\right]^4x^j\right|_{\rho=0}.
\]

j≤d<p 且 (1/2)ⱼ 中最大奇因子为 p−2，所以其全部分母及分子因子都是 p-units，参数导数也 p-integral。T₀=1、V₀=0，degT=d 且最高系数为 p-unit。

每个坏 packet 起点 n₀=h+kp 给准确 ratio

\[
\frac{c_{n_0+j}}{c_{n_0}}
=\left[\frac{(1/2+p(k+1/4))_j}{(1+p(k+1/4))_j}\right]^4
\equiv T_j+p(k+1/4)V_j\pmod{p^2},\quad 0\le j\le d.
\]

带外 U 的系数属于 p⁴；相邻 packets 不重叠，最后一段可按 prefix 截断。置 s=xᵖ，W(s)=ΣU_(h+kp)sᵏ 即得

\[
U\equiv x^h\{TW(s)+pV(\theta_s+1/4)W(s)\}
\pmod{p^2,x^N}.
\tag{R1}
\]

没有从某个 fixed-offset 局部 packet 外推无限 p-integral 级数。

## 4. 两层消元、嵌套与原四行 primitive counts

置 B=TθV−VθT、Q=T²+B、α=h+θT/T、β=xʰB/T。degB≤2d−1、degQ=2d 且最高系数为 p-unit，T₀=Q₀=1。R1 直接给

\[
(\theta-\alpha)U\equiv
p\{(x^hT+\beta)\theta_sW+(\beta/4)W\}\pmod{p^2,x^N}.
\]

再用 α₂=h+θQ/Q−θT/T，慢导数贡献 p²，得到修正项

\[
\{(\theta-\alpha_2)(\theta-\alpha)
-\tfrac p4(Q\theta B-B\theta Q)/(QT^2)\}U\equiv0\pmod{p^2,x^N}.
\]

QθB−BθQ=T(TθB−2BθT)，所以清 QT 即可。实际二阶 polynomial row 的系数为

\[
\begin{aligned}
P_2&=QT,\qquad P_1=-(2hQ+\theta Q)T,\\
P_0&=(h^2Q+h\theta Q)T+(\theta Q)(\theta T)-Q\theta^2T
-\frac p4(T\theta B-2B\theta T).
\end{aligned}
\tag{R2}
\]

令 ℒ₁=Tθ−hT−θT、ℒ₂=P₂θ²+P₁θ+P₀。ℒ₁、θℒ₁、θ²ℒ₁ 支持实际四条 J derivatives、degree≤d，分别把 U 提到 modp；ℒ₂、θℒ₂ 同样支持原四条行、degree≤3d，把 U 提到 modp²。最高 derivative coefficients 分别为 T 与 QT，均 modp 非零，所以在次数≤D 的原 polynomial source 中两类 primitive counts 分别为

\[
k_1=3(D-d+1)_+,\qquad k_2=2(D-3d+1)_+.
\]

准确嵌套为

\[
\overline{\mathcal L_2}=(Q\theta-hQ-\theta Q)\overline{\mathcal L_1}.
\tag{R3}
\]

θℒ₂ 也在 ℒ₁、θℒ₁、θ²ℒ₁ 的 polynomial span 中，其 coefficients degree≤2d；乘 degree≤D−3d 的多项式仍属第一层 degree≤D−d 的 admissible span。因此第二层提高已有 directions 的一个 Smith 阈值，没有被当作额外普通 kernel。R2 的 p/4 修正必要，不能只用两阶乘积。

本文证明这些 whole-prefix 原四行关系和局部 primitive counts，不认领其 tensor/near-balanced determinant、CDT matching maximum、费用积分、解析叶放大或数值无理性结论。那些接口必须在实际同一原格另稿审阅。

## 5. 执行与审阅范围

本稿是独立全尺度推导，未执行任何数学检查脚本。没有有限素数实验，没有 import 同行或冻结 producer。本稿实际审阅的是上述明确四篇 MD 及根任务给出的 R1/R2 公式；没有声称读取任何新 rank10 complete-F packet 或外部未阅原件。此前固定证书中的 Sp₄ 输入作为已冻结证明使用，未重跑其证书。

本轮通过的结论是 rank5 非分裂、Q3 的归一化、J/H 的精确全前缀分母、split-prime R1/R2 与 k₁/k₂；目标数值无理性和线性无关性仍未得到。
