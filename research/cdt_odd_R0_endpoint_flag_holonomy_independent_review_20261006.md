# Endpoint flag / arithmetic holonomy 独立审阅

日期：2026-10-06。NEW 全文独审。旧稿与同行数学 producer 均只读，未执行、import 或 rerun。

## I1. 实际对象与来源

实际全文读 `research/cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.md` 最新候选 SHA256
\[
\texttt{af728ecbebe3ac4827f7388706d4c5892896437e625e1bf4a0671b949bff28b5}.
\]
H1–H10 全文实际审阅，含最新 H4 人工把 q 放入常数系数不属 period 提取的说明，以及 H7/H8 闭单位盘邻域/径向缩盘 boundary 条件。实际全文读其 NEW source receipt，未执行 manifest。

本轮为此独审实际读 primary：

- `literature/cdt2025_arithmetic_holonomy.pdf`，SHA \(\texttt{5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1}\)：完整 PDF3–8，Theorem2.1、denominator type、number-field norm、§2.3 的 \(O_K\) evaluation module、slopes、Lemma2.9 和 finite-place heights。
- `literature/cdt2024_l2_chi_minus3.pdf`，SHA \(\texttt{84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771}\)：完整 PDF99–103、105、122–124，(7.3.7)、(7.3.14)–(7.3.16)、Lemma7.4.1、Theorem8.0.1 与 Remark8.0.6。没有声称本轮读完218页或 §§6–8 的完整全部证明。

冻结 exterior 与 real Betti 两稿上一轮已实际全文独审；本轮又读 exterior E1–E3/E10，核 \(\Phi(q)=\Phi_h+q\Phi_0\)、\(P_c=\langle g_1,g_2\rangle\)、\(v=g_1+\tfrac34g_2\)、\(C(y_0,v)=1/\pi^2\) 的归一化。输入 Galois group 与 actual rank 的完整既有证明保持冻结只读。

## I2. 强 linear no-go 全尺度证明

H2 的 kernel lemma 正确：任何 connected \(G_a^4\rtimes\operatorname{Sp}_4\)-stable 子空间若在 primitive5 quotient 有非零像，该像为全5；非零二向量 p 不可能令全部 \(a\wedge p\) 为零，translations 产生 bottom4 的一个非零向量，再由不可约性得全4，故 kernel=全9。不是仅依 composition factor 宣称。

H3 的 \(P_c\ne\ker N_0^2\) 严格成立：后者包含于 \(\ker N_0^3=y_0^\perp\)，而 \(v\in P_c\)、\(C(y_0,v)\ne0\)。奇 loop 的 quotient eigenvalue−1；偶 loop 的 fixed decomposable wedge 强迫 plane invariant，进而 \(N_0\)-stable，single Jordan4 的唯一二维 stable plane 与 \(P_c\) 不同。因而每个 q、每个非零 finite loop 都有实际 nonzero primitive quotient jump。

对有限代数 cover 上 algebraic row R，\(\operatorname{ev}_R\) 的 kernel 为相应 finite-index differential-Galois/monodromy closure stable：R 已在 base field 中，被该群固定。若输出 local meromorphic，kernel 包含上述 primitive jump，故全9。fundamental matrix invertible，迫 R=0。这核清了 analytic zero-function kernel、actual solution vector 与 pointwise numerical value 的区别。导数经 rational connection 仍是 row，故微分 closure、algebraic gauge、加独立常数及有限次 integration 的声明都在正确范围。H4 通过。

## I3. 半径、cut term 与 metric 费用

H5 中每个保留 coordinate row 为 actual 九空间的非零 row，故其 canonical origin branch 非 meromorphic；与 conifold \(t=0\) 的 \(|t|<1\) 全纯性结合，Cauchy–Hadamard 半径恰1。不是九行平均半径或有限系数拟合。fixed holomorphic multiplier 只能乘非零 jump，不能在开 cut 上杀掉；primary Lemma7.4.1 的 pole-removal 与 subharmonic scalar 条件确实不能用最高一层 log 消失取代。

H6 是带明确 hypothesis 的 metric lemma：若全部辅助向量 norm ratios 在 \(e^{\pm O(\log D)}\) 内，则 determinant degree 与 rD 个 heights 的变化是 \(O(D\log D)\)，不给 D² 主项。固定 logweight 的结论只对注明的 polynomial-log cutoff 范围成立；作者保留极端 D-dependent weights 的新证明要求。\(r\,d[k\log(-\log r)]/dr\to0\) 与 powerweight atom 的区别正确，没有泛称所有 parabolic 理论均无效。

## I4. species、数域与 q=0 reference

十行 rows species \(0,6,6,6,6,6,7,7,7,7\) 对应六列 cutoff1 和一列 cutoff6，得
\[
\tau=7-(6+36)/100=329/50.
\]
primary Remark8.0.6 对 nested columns 确给更细 species 同值。固定 indexshift 的 \(\epsilon\) 处理与固定 scalar 整化不贡献主项。将 \(f(Cs)\) 与 map \(\phi/C\) 配对，确实同时把 \(\log C\) 从 numerator 的 Bost–Charles integral 和 denominator 的 conformal size 中减去；不是仅在 denominator 支付。H14 是带完整 meromorphy 及 positive denominator 的条件 inequality。

H8 逐 embedding 的 weighted slopes 与 primary \(O_K\) model/height normalization 一致。用 \(y_j=u_jb_j\)，degree 主项 \(mA/2+\sum u_j^2b_j\)，arch height \(-m^2L/2+mA\)，finite height \((m^2\sigma_m+\sum u_j^2b_j)/2\)；相减严格给 \(10(L-329/50)\le A\)。有限 places 的 LCM valuation 是 \(O(\log n)\)，scale C 已支付全部 unknown bad primes，没有把单一 complex embedding 的结论冒充超越性。

q0 reference 是 actual \(F(0)\) 的无条件 rational G-packet，仍有 rank10，并非 toy。若某 map family 同时适用于 q0 与 actualq，则上述 inequality 已对 q0 成立，common-domain 数据不能给只排斥 actualq 的矛盾。规范 conifold fillability 与 infinity obstruction 均 q-blind；H4 已堵住 canonical origin linear single-valued enlargement。这个 no-go 没有覆盖未构造的不同 transported word 或更高/nonlinear packet。H9 的条件与剩余突破范围正确。

## I5. 结论与边界

H1–H10 全文声明范围通过。本稿实际提供当前 scalar CDT 路线的明确 linear 障碍与精确预算；不证明所有统一框架都不可能，不宣称 α0 或 ζ/L/Catalan 无理性。最高 log flag 仍是有意义的 actual marking 数据，但与 meromorphic filling 是两种不同条件。

本人同时实际全文读 root NEW denominator 稿，仅做纸面校核矩阵、all-n recurrence 与 conditional odd-place interface；其正式独审由其他代理负责，本文件不重复登记为另一篇独立 proof review。本轮没有运行任何数学 producer，也没有新增 PDF。

