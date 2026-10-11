# 真实 conifold 初值假设：一个单端点 dual 算术模型及其严格局限

日期：2026-10-06。NEW 全尺度纸面推导。旧数学 MD/PY/JSON/manifest 均只读；没有创建、执行或 import 数学 producer。本文不声明新的数值无理性或线性无关性，也不把 analytic cut scalar 等同于尚未标记的 compact regulator scalar。

## A1. 对象、来源与问题

沿 [conifold 算术中心稿](cdt_odd_conifold_arithmetic_center_20261006.md) 的实际正实分支，取
\[
 P=\theta^4-x(\theta+\tfrac12)^4,\quad \theta=x\partial_x,
 \quad t=1-x,
 \quad\Psi=W-\frac{\pi^4}{16}y_0,
 \quad P\Psi=\frac{\sqrt{x}}{16}.
\]
\(\Psi\) 在 \(t=0\) 全纯，且
\[
 \Psi(1-t)=h(t)+\alpha_0g_0(t)+\alpha_1g_1(t)+\alpha_2g_2(t),
 \qquad
 \alpha_0=\frac{\pi^2}{16}(R_0-M_0).
 \tag{A1}
\]
这里 \(h,g_0,g_1,g_2\in\mathbf Q[[t]]\) 为冻结 C3 的 canonical germs：\(Ph=\sqrt{x}/16\)，\(Pg_j=0\)，前三 Taylor coefficients 分别是零和三个单位向量。因此
\[
 g_0=1+O(t^3),\quad g_1=t+O(t^3),\quad
 g_2=t^2+\frac54t^3+O(t^4).
\]
本文实际完整读取上述稿、[Kummer 接口](cdt_odd_R0_kummer_period_interface_20261006.md)、[Yukawa 稿](cdt_odd_R0_Yukawa_scalar_interface_20261006.md)及[正实切比较](cdt_odd_R0_positive_cut_period_comparison_20261006.md)，并实际读取主记录 §§64、68–72。

原六行中心模型要求三个 \(\alpha_j\) 同属 number field；一个具体数值关系没有自动给这三项。本稿证明可以构造一个不同的 rank-five dual 模型，只需 \(\alpha_0\) 一个数据；同时精确说明此投影为何还没有产生数值矛盾，以及哪些真实 Betti 歧义不能忽略。

## A2. 在原 Taylor 坐标上计算 concomitant

采用冻结 Yukawa §4 已核准的 Euler concomitant
\[
\begin{aligned}
 \mathcal C(f,g)={}&\frac x2(f\theta g-\theta f\,g)
   +x(f\theta^2g-\theta^2 f\,g)\\
 &-(1-x)(f\theta^3g-\theta^3f\,g)
   +(1-x)(\theta f\,\theta^2g-\theta^2f\,\theta g).
\end{aligned}
\tag{A2}
\]
其全函数身份为
\[
 \theta\mathcal C(f,g)=(Pf)g-f(Pg).
 \tag{A3}
\]
若 \(f=f_0+f_1t+f_2t^2+O(t^3)\) 与 \(g=g_0+g_1t+g_2t^2+O(t^3)\) 均全纯，因 \(\theta=-(1-t)\partial_t\)，
\[
 \theta f(1)=-f_1,\qquad\theta^2f(1)=2f_2-f_1.
\]
含 \(1-x=t\) 的两项极限为零，故实际端点公式是
\[
 \boxed{\mathcal C(f,g)(1)=
       f_0(2g_2-\tfrac32g_1)-g_0(2f_2-\tfrac32f_1).}
 \tag{A4}
\]
没有分别求 \(W\) 和 \(y_0\) 的发散端点导数。

这也证明三维 holomorphic homogeneous 空间的配对矩阵（顺序 \(g_0,g_1,g_2\)）为
\[
 \begin{pmatrix}0&-3/2&2\\3/2&0&0\\-2&0&0\end{pmatrix}.
 \tag{A5}
\]
特别地，\(g_1,g_2\) 张成 isotropic plane。其 radical 恰由
\[
 v=g_1+\frac34g_2=t+\frac34t^2+O(t^3)
 \tag{A6}
\]
生成。冻结实际 node/PL 稿的 vanishing period 因 log 必须消去的关系及首项 \(-\pi^2t\)，恰为 \(g_\delta=-\pi^2v\)；这在下面用于真实 Betti 歧义，不把有理 \(v\) 当成未经标记的 integral period。

## A3. 一个未知初值已足够的真正 dual germ

定义新的实际函数
\[
 S(x)=\mathcal C(\Psi,g_2)(x).
 \tag{A7}
\]
(A3)–(A4) 精确给
\[
 \boxed{S(1)=2\alpha_0,\qquad\theta S=\frac{\sqrt{x}}{16}g_2.}
 \tag{A8}
\]
两个未知初值 \(\alpha_1,\alpha_2\) 完全消失。因为 \(\mathcal C(g_1,g_2)=\mathcal C(g_2,g_2)=0\)，也可直接从 (A1) 得到同一结论。以真正 conifold Taylor 坐标写成
\[
 \boxed{S(1-t)=2\alpha_0+F(t),\qquad
 F(t)=-\frac1{16}\int_0^t\frac{g_2(u)}{\sqrt{1-u}}\,du
       \in t^3\mathbf Q[[t]].}
 \tag{A9}
\]
因此 \(F(t)=-t^3/48+O(t^4)\)。这里是收敛的 analytic primitive；\(g_2\) 的 G-function 性和 \(\sqrt{1-t}^{-1}\) 的收敛代数展开使积分合法。

由 (A9) 得到精确等价：
\[
 \boxed{S(1-t)\text{的全部 Taylor coefficients 是代数数}
        \iff\alpha_0\in\overline{\mathbf Q}.}
 \tag{A10}
\]
若 \(\alpha_0\in K\)，则全部 coefficients 已在同一个 number field \(K\)。这确实把真实 cut scalar 的三个初值要求降到一个初值，但构造的是新的 dual germ，而非原 \(\Psi\) 的免费有理 gauge。

## A4. 明确 rank-five 方程、dual 身份和最小性

设 \(u=\sqrt{x}g_2\)。用 \(\sqrt{x}\theta\sqrt{x}^{-1}=\theta-1/2\)，有
\[
 Ku=0,\qquad K=(\theta-\tfrac12)^4-x\theta^4,
 \qquad MS=0,\quad M=K\theta.
 \tag{A11}
\]
原 \(L=(\theta-1/2)P\) 对 Euler measure \(dx/x\) 的形式 adjoint 为
\(L^*=-P(\theta+1/2)\)，因为 \(P^*=P\)。因而
\[
 \boxed{M=-\sqrt{x}L^*\sqrt{x}^{-1}.}
 \tag{A12}
\]
这是 Kummer twist 后真正的 dual equation。形式 adjoint 的 Lagrange concomitant 给一个非退化 flat pairing，将解空间识别为 dual；它不是把同阶数当作 local systems 同构。

冻结 [Kummer 接口](cdt_odd_R0_kummer_period_interface_20261006.md) §4 已全尺度证明 \(L\) 的 extension 非分裂，且齐次 rank-four 层绝对不可约。故 dual 后再作 Kummer twist 的 (A11) 也非分裂，解 local system 有准确的 non-split exact sequence
\[
 0\longrightarrow\mathbf C\cdot1\longrightarrow
     \operatorname{Sol}(M)\xrightarrow{\theta}
     \operatorname{Sol}(K)\longrightarrow0.
 \tag{A13}
\]
其中 \(\operatorname{Sol}(K)\) 仍不可约。因 \(\theta S=u/16\ne0\)，其 monodromy orbit span 在四维 quotient 上非零，因而满射。若此 span 只有四维，它与常数核没有交集，给 invariant complement，违背非分裂；所以其维数恰五。任一四阶或更低的 scalar annihilator 必有包含该 orbit 的解空间，亦不可能。因此
\[
 \boxed{\operatorname{ord}_{\min}S=5.}
 \tag{A14}
\]
同一论证对每个 \(F+q\)、\(q\in\mathbf C\) 成立，因为其 \(\theta\)-image 不变且非零。最小性并不依赖 \(\alpha_0\) 非零或非代数。

这个结论也在有限代数覆盖上保留：rank-four 齐次层的 connected \(\mathrm{Sp}_4\) 使其覆盖后仍绝对不可约。若 (A13) 在有限覆盖上分裂，取 Galois core 后对有限 quotient 平均 splitting，便得到原基上的 splitting（特征零可除 degree），矛盾。这只是最小 scalar order；不把含常数 1 的更大 CDT 竞争模型自动记成秩五。

## A5. 原坐标上的完整五行系统

取五行
\[
 (S,u,\theta u,\theta^2u,\theta^3u).
 \tag{A15}
\]
由 \(K=(1-x)\theta^4-2\theta^3+\frac32\theta^2-\frac12\theta+\frac1{16}\)，实际有理 connection 为
\[
 \theta S=\frac u{16},\qquad
 \theta^4u=\frac{2\theta^3u-\frac32\theta^2u+
          \frac12\theta u-\frac1{16}u}{1-x}.
 \tag{A16}
\]
其余三条为 derivative shift。以 \(t=1-x\) 作 algebraic coordinate change，除去 \(\theta=-(1-t)D\) 后就是 \(\mathbf Q(t)\) 上的五行有理系统；没有使用 \(\pi\) 作 gauge。

(A15) 的五行在 \(\mathbf C(x)\) 上独立：否则为 \(S\) 得到阶数小于五的 scalar annihilator，与 (A14) 冲突。若研究还需常数 1 作为额外竞争函数，要另行核证其更大实际模型和格；(A14) 不能用于漏掉这一项。

## A6. 单初值条件下的全尺度 prefix 整模型

本稿实际读取 [Fischler–Rivoal 出版原件](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf) PDF2–5、9。Thm1–2 的 geometric 定义允许 PF factors 的乘积，并在 geometric 情形无条件给 \(D_{bn+b_0}^{\mu-1}C^{n+1}\)；PDF9 说明有限坏素数的 \(C^{n+1}\) 不能删除。

\(g_2\) 本身是 \(P\) 的真实 holomorphic solution，前三初值有理。冻结中心稿的 local Nilsson–G basis / algebraic normalization 论证适用于 \(\beta=0\)，故它是阶四 geometric equation 的 G-function。conifold exponents \(0,1,1,2\) 给 \(b=1\)。存在固定整数 \(b_0\ge0,C_g\ge1\)，使
\[
 D_{n+b_0}^{3}C_g^{n+1}[t^n]g_2\in\mathbf Z.
 \tag{A17}
\]
令 \(a_j=\binom{2j}{j}/4^j\)，则 (A9) 的第 \(n\ge1\) 个 coefficient 是
\[
 [t^n]F=-\frac1{16n}\sum_{k=0}^{n-1}
       ([t^k]g_2)\frac{\binom{2(n-1-k)}{n-1-k}}{4^{n-1-k}}.
 \tag{A18}
\]
每个 summand 可由 \(D_{n-1+b_0}^3(4C_g)^n\) 整化；积分的 \(n\) 再由 \(D_{n+b_0}\) 支付，故
\[
 \boxed{16D_{n+b_0}^{4}(4C_g)^n[t^n]F\in\mathbf Z.}
 \tag{A19}
\]
这直接核出额外一个 lcm exponent 的代价，而非仅援引未知阶数的 tensor 分母。

若 \(\alpha_0\in K\)，选正整数 \(d_0\) 使 \(d_0\alpha_0\in\mathcal O_K\)。在实际 \(t\) 坐标中，对 (A15) 的全部五行、全部 \(0\le n\le N\)，可共同采用
\[
 \boxed{\Delta_N=16d_0D_{N+b_0+3}^{4}(4C_g)^{N+4}.}
 \tag{A20}
\]
理由如下：\(S\) 用 (A9),(A19)；\(u=\sqrt{1-t}g_2\) 的 algebraic coefficients 由 \(4^n\) 安全整化，卷积用相同 \(D^3\)。至多三次 \(\theta=-(1-t)D\) 是整数系数多项式乘 derivative 的组合，仅需读到原序列的 \(N+3\) 项，derivative factorial ratios 为整数。(A20) 比所需界更大，覆盖全部项。

因此获得真正的 arithmetic prefix，而主率安全上界为
\[
 \log\Delta_N\le(4+\log(4C_g))N+o(N).
 \tag{A21}
\]
固定 \(b_0,d_0,16\) 不改变主率，\((4C_g)^N\) 改变主率。该界没有证明最小 \(C_g\)、good-prime Smith savings 或完整 CDT optimum；当前不能从 (A21) 宣称数值矛盾。

## A7. 此投影没有免费保留原模型的整数格

式 (A7) 的 coefficients 含实际 \(g_2,\theta g_2,\theta^2g_2,\theta^3g_2\)。它们并非 \(\overline{\mathbf Q}(x)\) 中的函数；绝对不可约 \(P\) 的 nonzero solution 不可能是 algebraic solution。因此 (A7) 不是原 \(\Psi\) 模型的 algebraic gauge。把旧原点 finite-place savings、叶容量或 Betti lattice 无改变地赋予 (A15) 没有依据。

本稿是对新 dual germ 自身直接建立 (A16),(A20)，而非先做未经证明的整数 tensor quotient。若欲把 \(\Psi\) 的所有几何优势搬到新 dual 系统，需在实际 tensor/current 的原格中比较 (A7) 的 evaluation map、kernel、saturation 与全部 finite places。

还有一个严格的有限代数 gauge 限制。若一个 algebraic-coefficient scalar differential operator \(T\) 杀 \(g_1\)，则 \(g_1\) 的 homogeneous differential Galois orbit span 是整个四维 \(\ker P\)；\(T\) 也杀所有 \(g_j\)。等价地，右除以 \(P\) 后的余项阶小于四，杀非零 \(g_1\) 就违背其最小四阶，余项必为零。故
\[
 Tg_1=Tg_2=0\Longrightarrow Tg_0=0.
 \tag{A22}
\]
同一结论对有限代数覆盖成立（connected \(\mathrm{Sp}_4\) 保留）。因此一个真正 algebraic differential row 若想在所有 \(\alpha_1,\alpha_2\) 上消去这两项，也会消去 \(\alpha_0\)。本稿使用新的 dual tensor pairing，避开这一限制的同时必须支付 (A20)，不能称为免费三jet消去。

## A8. 单个端点不足以使原 germ 算术：完整反例

对任一 \(a\in\overline{\mathbf Q}\)，两个真实 analytic solutions
\[
 f=h+ag_0,\qquad f^\sharp=h+ag_0+\pi g_1
 \tag{A23}
\]
均满足 \(Pf=\sqrt{x}/16\)，在 conifold 全纯，且端点值都为 \(a\)。第一个所有 Taylor coefficients 代数，第二个一次系数为 \(\pi\)，已知超越，故不算术。这是完整全函数 counterexample，并非只核几个 coefficient。它证明 forcing、全纯性和单个端点代数性不足以给原 C5 六行整模型。

(A23) 不声称其任意 complex flat translate 都是原 family Xi 的许可 Betti lift。下面给原 Xi 本身许可范围内的更强证据。

## A9. 真正允许的 Tate–Betti lift 也保持端点、改变超越 jet

KLM published §5.6（本稿实际读 PDF13，印刷386）给本例 \(p=n=4\) 的 precise ambiguity 为
\[
 r\ \longmapsto\ r+(2\pi i)^4\operatorname{PD}\gamma,
 \qquad\gamma\in H_3(X_x,\mathbf Q),
 \tag{A24}
\]
因为 \(F^4H^3=0\)。取冻结实际 node 稿已构造的 integral vanishing sphere \(\delta\)，其 period 是
\[
 \int_\delta\omega=-\pi^2v(t),
 \quad v=t+\tfrac34t^2+O(t^3)\in\mathbf Q[[t]].
 \tag{A25}
\]
对固定规范
\[
 \widehat\nu=-\frac{Q_{\rm raw}(r,\omega)}{16(2\pi i)^3},
\]
(A24) 导致真实的 scalar shift
\[
 \boxed{\widehat\nu\longmapsto\widehat\nu+
      \frac{i\pi^3}{8}v(t).}
 \tag{A26}
\]
直接计算符号和因子：\(-[(2\pi i)^4/(16(2\pi i)^3)](-\pi^2v)=i\pi^3v/8\)。它仍满足相同 inhomogeneous forcing，仍在 conifold 全纯（若原 lift 全纯），且端点值完全相同。一阶 Taylor coefficients 的差却是 \(i\pi^3/8\)，已知超越；两者不可能都具有 algebraic Taylor coefficients。

此外 middle intersection 为 alternating，\(\delta\cdot\delta=0\)，所以这个许可 shift 也保持与 \(\delta\) 的 regulator pairing。即使 derivative、exact Yukawa、单端点值与一个 \(\delta\)-normalization 全部给定，也没有排除此歧义。必须增加真实 Betti marking，不能把 scalar algebraicity 视为 AJ quotient class 的无标记性质。

对 (A7) 的 dual projection，这个歧义确实消失，因为 \(\mathcal C(v,g_2)=0\)；这与其只检测 \(\alpha_0\) 的性质一致。此处是实际许可 lift 的论证，独立于尚未完成的 \(\widehat\nu=\Psi\) 比较。没有假定该比较已成立。

## A10. 目标常数、Tate 尺度及投影的准确 no-go

\(R_0-M_0\in\mathbf Q\) 不推出 \(\alpha_0\) 代数：若差为非零代数数，(A1) 使 \(\alpha_0\) 是 \(\pi^2\) 的非零代数倍数，因而已知超越。若差为零，则 \(\alpha_0=0\)，但那是另一个未证数值关系。不能在一个无理性反证里事先选择差非零或零。

本稿单初值条件适合的直接目标是
\[
 \alpha_0=\frac{\pi^2}{16}(R_0-M_0)
 \quad\text{或等价地}\quad \pi^2(R_0-M_0),
 \tag{A27}
\]
其新数值无理性仍未证明。把 (A7) 整体除以 \(\pi^2\) 后，非恒定 Taylor coefficients 已含 \(1/\pi^2\)；(A20) 立即失效，不能因常数项变为 \((R_0-M_0)/8\) 而宣称得到有理 arithmetic germ。

更关键的限制是 (A9) 的 \(F\) 本身无条件就是有理 coefficient G-function。任意 \(q\in\overline{\mathbf Q}\) 的 \(F+q\) 均有同样 order five、同样 nonconstant Taylor coefficients、同样 local branch differences。对任何 continuation loop \(\gamma\)，
\[
 \gamma(F+q)-(F+q)=\gamma F-F;
 \tag{A28}
\]
所以 scalar branch stabilizer 及所有局部 log/pole 取消完全不随常数平移改变。只用这些数据、rank-five 与本稿 uniform finite-place bound 的 CDT 判据，不能把某个 \(q\) 单独排除：\(F\) 已是这些条件的无条件算术实例。

这不是对所有利用 global normalization 的 CDT 方法作不可能性结论。它准确指出下一项必要数据：必须保留至少一个与实际 \(\alpha_0\) 有关的第二端点/Betti relation，或一个更大的真实 period packet 中的关系；只有 derivative、同一 analytic leaf 和单个常数项的 arithmetic implication 不足以制造数值矛盾。

## A11. 进一步的真实候选与可审查的下一步

1. 用实际 Betti/de Rham 格标记 conifold 三jet向量，再研究 \(1,\alpha_0,\alpha_1,\alpha_2\) 的有理关系。这个候选要求证明其实际表示与完整费用；目前没有其数值线性无关性结论，也没有声称更小子列已证。
2. 在保留端点敏感数据的 tensor packet 内使用 \(\Psi\wedge g_1\wedge g_2\)。它严格等于 \(h\wedge g_1\wedge g_2+\alpha_0g_0\wedge g_1\wedge g_2\)，故同样消去两个初值，但 \(\alpha_0\) 在这里不只是 constant translate。需计算真正 wedge representation、实际最小 cyclic rank、finite-place tensor lattice及 local0 marking；本稿不把暂定9或10充当已证秩。
3. 对新 dual packet (A15) 独立求有效 \(C_g\) 和 good-prime Smith data，并核新中心 analytic capacity。可以用来量化投影预算；应同时保留 (A28) 的值盲区，不能把此预算本身报成新数值定理。
4. 将 actual compact scalar 与 \(\Psi\) 的剩余三维 holomorphic period 差全部标记。A9 表明一条 vanishing pairing 条件不够；需要三维真实 Betti normalization / integral nearby-cycle comparison。完成后才可把 A3 的 \(\alpha_0\) 解释为那个指定 compact lift 的端点数据。

这些任务服务于原 ζ/L 特殊值目标；本文没有将 success 改为 dual arithmetic structure。实际新结果是 A8–A10 的单初值 dual 闭包、全尺度 rank/整化，以及 A22–A26 对免费原 gauge 与无标记单端点论证的严格限制。

## A12. 阅读、执行与审查范围

本稿实际阅读的 primary：

* [Fischler–Rivoal 2017 published](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)，PDF2–5、9；已冻结 SHA `c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68`。geometric unconditional denominators、local Nilsson G basis、有限 bad-prime exponential。来源原收据是 [冻结 FR manifest](../literature/manifest_cdt_odd_conifold_arithmetic_20261006.json)，没有重新下载、没有修改。
* [KLM 2006 published](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，PDF13–14、18–19；§5.6 读实际 membrane / Tate period ambiguity，§6–7 读 extension comparison。不声称该 actual Xi 的 completed precycle 已等于 raw positive graph。

A2 采用已证明 concomitant 身份，本文独立计算 analytic endpoint；A4 采用已冻结 non-split/absolute-irreducibility 输入，独立计算 adjoint/Kummer conjugation并证明实际最小阶；A6 对全部 \(n,N\) 纸面整化；A9 使用真实 node period与 primary Tate ambiguity。没有有限样本、PSLQ、mathematical verifier或 Lean claim。本文自己回读不冒认独立审阅；root或其他代理的独审另行记录。
