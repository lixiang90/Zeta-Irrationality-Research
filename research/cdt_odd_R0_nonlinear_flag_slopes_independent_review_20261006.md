# R₀ 非线性函数域与完整跳跃评价界：独立全文审阅

日期：2026-10-06。审阅人：quarter_actual_rank。本稿 NEW，仅写本次独审；全部旧稿、同行稿、数学脚本、JSON 与来源 manifest 保持只读。没有执行、import、重跑任何旧或同行数学 producer，本人本轮 NEW 数学 producer 也是 0。以下为纸面核验，不是有限搜索或数值实验。

## I1. 审阅对象、最终输入与阅读历史

已实际完整读取以下最终正文，输出均无截断：

1. [非线性稿](cdt_odd_R0_nonlinear_projective_invariant_field_20261006.md)，N1–N12，含 N26、N10a、N27；SHA256 **ec6ad8fedb27a1eea5fcbcdc8afed0b58a4e13cf6a393568c8274c9d16afd59b**。
2. [旗标与跳跃稿](cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.md)，G1–G11 全文；SHA256 **aeec82c8aa5a69b6e6ed8ada331ccca5846417d42c0d3a7591ac966b2f9b2d25**。

对应最终来源收据为：

- literature/manifest_cdt_odd_R0_nonlinear_projective_invariant_field_20261006.json，SHA **b76e6d36b85f3e93c12c92cf0856a46b49a89270e304803f1d3561b5de47d17d**。
- literature/manifest_cdt_odd_R0_logarithmic_flag_slopes_reduction_20261006.json，SHA **f55d8f15ce967f864cf85b5b6fa1971dc98369aada6829cbf7f9e4ceb8e060ac**。

非线性初候选 6d4df372 曾把参数常数 \(\mathcal J(q)\) 的 uniform recovery 写成 fixed-q field nonmembership。本独审指出：基域是 \(\mathbf C(x)\)，每个固定 q 的常数本来就在基域。作者仅修订未冻结 NEW 稿，最终 N26 正确区分这两件事，并另用稳定子证明 W、y₀ 各不在 \(\mathcal L_q\)。最终稿还新写 N10a 的 rational disk 共同域和 N27 的实际微分秩。初稿已全文读；一次最终组合输出截断后按段补读，最后又独立完整输出并阅读全文 ec6，未把截断算作完整阅读。

旗标初候选 0d4ec96 的 cut 条件尚未保证 thin-cut bank 积分趋于 trace。本人与 root 分别指出该缺口。最终稿 aeec 增列有限 piecewise-C¹ arcs/节点、compact subarc 上 bank 解析延拓或明确的 thin-cut L¹ 收敛，且先细管后 endpoint circles 取极限。最终全文回读确认修补已经进入假设和证明。上述错误与修订均留有记录，没有改写任何旧冻结稿。

实际当前基线主报告 §§85–93 已读取，SHA 为 1e0161b49ee96adae6cc30e9e7c89ca667b81877fd484919b86e7fd38e105f4c。基线 366 份冻结输入是归档数字，并不表示本次重新核验全部输入。实际模 8 证明 a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc 是本人另稿全尺度证明，原文与同行独审记录分别存在。

## I2. 非线性稿的实际稳定子与 invariant field

对实际 \(w=(e+d)\wedge p\)，p 是非零 Lagrangian decomposable bivector。Sp 部分固定 p 当且仅当 MP=P 且 \(\det M|_P=1\)；affine 部分须 \(a+Md-d\in P\)。平移共轭移除 d 后稳定子恰
\[
H^\circ=P_{\rm add}\rtimes Q_P,\qquad
Q_P=\operatorname{SL}_2\ltimes\operatorname{Sym}^2P.
\]
其维数 2+6=8，实际轨道维数 14−8=6；这不是九空间 generic vector 的稳定子。原 fundamental matrix 可逆使固定九行函数等价于固定 w，PV 对应可用于 \(k(F(q))=\mathcal E^{H_q}\)，无需误称中间域自身为 PV。完整稳定子的负 Kummer component 固定 w 但翻转 \(\sqrt x\)，所以其与 connected fixed field 的交只剩 k。这些核算通过。

在 ambient 九空间，\(a\mapsto a\wedge p\) 于 \(p\wedge p\ne0\) 时可逆，故 rational translation invariant 与 b 无关。Sp₄ 在 primitive 五空间的 Lie 作用注入 so₅，二者维数同为 10，得到 SO₅；非零 quadratic level 的传递性给
\[
\mathbf C(\mathcal W)^{G^\circ}=\mathbf C(Q),\qquad
\mathbf C[\mathcal W]^{G^\circ}=\mathbf C[Q].
\]
实际 null orbit 的 p 非零而 Q=0，b 落在二维 \(V\wedge p\)；Sp 和 translations 合起来传递，actual invariant field 是常数。Q 恒零或 0/0 因此不给 actual 参数信息。Polynomial 版本从 dense open 恒等式与 nonisotropic line 的 even polynomial 同样成立。N12/N13 没有将 ambient invariant 直接冒认 actual invariant。

## I3. 群生成、finite roots 与三个真实 punctures

N4 的关键 Lie lemma 可直接核验。相对于 \(P\oplus P^*\)，X 的 lower symmetric block C 非零恰等于 XP 不稳定 P。已有 traceless diagonal 和 upper symmetric blocks 可减去；sl₂ 对 remaining lower C 的非平凡不可约 Sym² 作用产生全部 pure lower blocks。Upper/lower 的 brackets 再给 scalar diagonal 及完整 sp₄。Generated affine closure 的 translation intersection 已含 P，且为满 Sp₄ 稳定；V 不可约使其等于 V。因而 N15 的 closure 是完整 \(G^\circ\)，没有仅由维数猜群。

若 rational output 在 finite local cover 上亚纯，某个正 even unipotent power固定它；它亦被 actual H 固定。以上生成使其来自 finite base，并固定 \(a=(q'-q)g_0\) translation。因此同一个不外加 q 的有理公式给全 q 同一函数。所有分母的非零性随 automorphism 保持，不能只在某参数把 identically-zero denominator 解释成输出。

Finite algebraic roots 的 N6 论证正确没有假定 root 在 PV 域。Root 的 PV-minimal polynomial 是 H 固定 defining polynomial 的有限 irreducible factors 之一，connected H 不能非平凡置换这些 factors；局部 continuation 固定 root 则固定其 monic minimal polynomial。其 coefficients 故被 H 和局部 u 固定，归约到 finite base。结论是 root algebraic over base，及固定、连续 branch-selection 的 q-blindness；不将任意外加 q-dependent finite branch 选择纳入。

原点调用真实 allword 模 8 障碍，任何 transported P 都不等于 regular J₄ 的唯一 invariant two-plane \(\ker N_0^2\)，故 N15 对所有路径和有限 cover 成立。Conifold 的 Lagrangian plane 稳定 transvection 当且仅当包含 vanishing vector v：否则 covector 在 P 上非零且映到 P 外；包含时 restriction 是 identity。Bad plane 给 q-blind rational output；good plane 则完整 paired packet 对全 q 全纯。这是 meromorphy 分类，不是 pole order 或 arithmetic lattice 的免费分类。

Infinity 的 full J₅ 要单独处理。源 column \(b\notin N_\infty V\)，否则可 split 出 J₁。若 P 不稳定则满群生成；若 P 稳定，P=\(\ker N_\infty^2\subset N_\infty V\)，subtract H 内相同 Sp Lie element 后出现 P 外 pure translation。Q_P 在 V/P 上的 sl₂ 作用不可约，生成全 V。此时 closure 准确为 \(V_{\rm add}\rtimes Q_P\)，不是满 Sp₄ affine 群。留下的 primitive five-row quotient 不含 q，因此可亚纯 output 仍 q-blind。N24 的限制是必要的，最终稿保留了它。

## I4. Fixed-q constants、实际 rank 与 disk 共同域的范围

N26 的 flat concomitant 计算给
\[
\mathcal J(q)=-2(q-\alpha_0)/\pi^2.
\]
它对每个 fixed q 是基域常数，不能据此声称其不在 \(\mathcal L_q\)。最终稿只排除 single q-free reference-independent formula 的 uniform recovery：否则 origin meromorphy 和 N17 会令非零斜率 family 恒定。另证 W 不被 P-add translations 固定；Q_P 在 V 上无 fixed vector排除 y₀。这两个 actual nonmembership 证明独立于常数 family，正确。

N10a 对 coefficients 在 \(\mathbf C(x)\) 的有限 rational outputs，及列明的 nonconstant holomorphic disk map，证明共同 meromorphic domain。若有 sensitive output，origin preimage 会由定理 1 强迫其 q-blind，故不能存在；每个 conifold arrival plane必须 good，否则同样矛盾。Good planes让完整 F(q) 对全 q 填平；disk 去掉离散 preimages 的 loops 在每个 compact subdisk 由 small loops 生成，故全部 F(q) 同时单值，再取 rational outputs。Denominator automorphism 保持非零。φ 的边界估计另核；finite algebraic coefficient covers 另列。

N27 由 fix k、commute θ 的 translation 同构，给 actual derivative spans 全 q 等秩，有限或无限均成立；没有把新 ratio 的秩误记为 9/10。Finite roots 的 ordinary discriminant locus 可随 q 变化，**不在这个共同域定理内**。任意非局部 word 的 scalar quotient 也未逐一分类，all-place 整模型与 holonomic rank更不会从旧 packet 免费继承。最终稿的正面边界与费用限制准确。

## I5. 完整 jump 的 Cauchy 界与 D² 条件

最终 G3 的 cut 几何和 bank convergence 足以使用有限 smooth exhaustion。固定 n 后，小节点圈积分为 \(O(\varepsilon^{1-\alpha}(1+|\log\varepsilon|)^k)\)，因为 b≠0，\(z^{-n-1}\) 在 b 附近有界。先 thin bank tubes 再节点圈，外圈另用径向 L¹ 极限，得到 exact formula
\[
c_n=(2\pi i)^{-1}\int_{\partial D}Fz^{-n-1}dz+
(2\pi i)^{-1}\sum_\Gamma\int_\Gamma JFz^{-n-1}dz.
\]
符号由 cut boundary orientation定义，无漏 ordinary poles：若有须另加 residues。每个固定 n 的 identity 先成立，不交换 n→∞ 与 endpoint limit。G5 的 \(\rho^{-n-1}\) bound 直接。

Source unit ball 上 outer ≤M_D、full-jump ≤\(C_\Gamma M_De^{-\sigma D}\) 的 **uniform** 条件给
\[
\log\|\mathrm{ev}_{D,n}\|\le\log M_D+
(n\log\rho^{-1}-\sigma D)^++O_\Gamma(1).
\]
这是 log(1+Ceᵘ) 的精确 positive-part inequality；单个 vector 的 highest-log cancellation 不能代替 full operator bound。对 r(D+1) 个 distinct indices，至少约 rD/2 个 ≥rD/2，节省 \(\sum\min(an,\sigma D)\) 至少是正文 G8 的 D² 下界；multiplicity≤k 时将 ar/2 换为 ar/(2k)。这是条件全尺度计数，不是 R₀ 已验证的 σ>0。

## I6. Fixed log metric 与真正 arithmetic descent

G9 是列明的双向 norm 比较假设。固定 packet rank 和 log weights、\(|\log r_D|\le D^B\) 令每个 singular log 变化 O(logD)，在 rank O(D) 的 source/graded target 总费用 O(DlogD)。Line O(D) 的 Bost–Charles metric保持不变是必要限制；degree-growing tensor、nilpotent order、new polynomial packet 不在此结论内。该 bound 没有制造 G6 的 e⁻σD。

W₉ differential module本身与 q 无关，module-functorial semisimple exponents/Deligne weights/irregular slopes因此全 q 相同；\(\det e^{N\log z}=1\) 本身不改 power exponent。Marked section 的最高 nilpotent flag cancellation 仍可能成为未来新定理输入，但不是现成 module slope。

Endpoint hyperplane 的 descent lemma 是纯线性代数充要条件：若实际 Taylor covector \(a=\ell_B C\)，则 ker a 由 K 定义 iff \([a]\in\mathbf P(W_K^\vee)(K)\)，即所有 normalized ratios 在 K。整数 Betti row不自动给 Taylor row下降；假设 \(\alpha_0\in K\) 只固定在 \(\Phi_h,\Phi_0\) 上一项 ratio，未控制九空间全 projective row。固定 K-row 还需 fixed denominator/all-place operator height，也不自动产生 σ>0。G11 的 actual R₀ 成立性、G6 的 actual full-jump抑制均保留未证。

## I7. 实際一手原页与证据边界

本人本轮实际读取的 primary PDF 页如下；不是作者 scope 的复制，也不是全文 PDF 阅读：

| Primary | 本人 actual PDF pages | SHA256 |
|---|---|---|
| Singer，LMS lectures | 13、14、17、20、26 | c805d45ed54e0e6734b4d7f125c197364b9eccab2a7e09a8c26c3bf63cf5db96 |
| Bost–Chambert-Loir，Analytic curves | 18、38、39、40 | e04ad5408eb19d5da826363c0a775c36f9387fe72da8f81bc39e8733b1ec48f9 |
| André，Slope filtrations | 6、7、70、71 | ef147278d1472d2a0f2dbacd4c660bbc040b6f99431677c23f4e44dfa32d17a9 |
| Bost，Evaluation maps | 15、16、17 | 46e5d09078d6e1ca1d20a5f811a3d27dafeb51fffc5867c541ba17416e504e9a |
| CDT，effective holonomy author 2026 | 5、6、7、8 | 368cc0af5584049a76c7cef0fd78886524143ee3935f56cfc2e35fb9bee22796 |

Singer 支持 PV correspondence、connected fixed field、torsor 和 regular-singular monodromy closure；specific R₀ stabilizer/Lie lemma是新稿自证。BCL 18/38–40确有 K-linear evaluation、A-analytic formal germ/all-place height；Bost 15–17 的 parabolic 指 Liouville/null-boundary，不能与 nilpotent flag weights混称。André 6–7 定义 regular differential slope，70–71定义 arithmetic hermitian lattice；不同 category不自动产生 degree。CDT 本人明确读取的是 receipt 所列 effective-author 文件 5–8：Lemma2.9 的完整 error、operator unit-ball、rank-one graded maps与D²预算均吻合。

所有页为本地 primary 字节的实际读取；TLS acquisition 由各作者已冻结来源收据登记，本人本轮没有下载这些 PDF，也不把 metadata/search snippet 当定理。对来源收据已实际读其完整内容；nonlinear receipt 的 pending 状态后来改为 final freeze仅 metadata，最终 SHA单独复核。只读 fitz text extraction、Get-Content/Get-FileHash不是数学 producer。

## I8. 独审结论

两份最终正文在其明确范围内通过纸面独审。新增已证是实际 six-dimensional orbit/stabilizer/invariant fields、有限 roots 的 minimal-polynomial接口、原三个 punctures 的 nonlinear分类、rational disk共同域，以及 complete-jump Cauchy/positive-part界、条件 D²计数、fixed-log低阶费用和 projective row下降lemma。

R₀ 的 uniform σ>0、actual comparison ratios、new all-place packet及 matched height/energy仍未完成。Finite roots 的新 ordinary branchpoints、独立 reference的共同 arithmetic germ与 jump-aware holonomy仍是明确边界。此独审不登记新的 ζ/L/Catalan 无理性、超越性、线性无关性或 Lean结果。

本文完成实际全文回读与最终 SHA后冻结只读；root main/delivery/audit由 root另行更新。
