# R₀ 非线性与射影函数域稿的独立实际审阅

日期：2026-10-06。审阅者：`toric_chow_completion`。本文为 NEW 只读同行稿的独立审阅记录；未修改作者稿、旧数学稿或任何同行 producer，也未执行、import 或重跑这些 producer。

## 1. 最终对象与真实阅读范围

实际全文阅读并逐项手核 [同行最终稿](cdt_odd_R0_nonlinear_projective_invariant_field_20261006.md)，包括 N1–N27、三个定理、N10a 及全部范围限定。最终 SHA256：

`ec6ad8fedb27a1eea5fcbcdc8afed0b58a4e13cf6a393568c8274c9d16afd59b`。

亦实际全文读 [作者最终来源收据](../literature/manifest_cdt_odd_R0_nonlinear_projective_invariant_field_20261006.json)，SHA256：

`b76e6d36b85f3e93c12c92cf0856a46b49a89270e304803f1d3561b5de47d17d`。

初始候选 `6d4df372fa64fe4ca79d5c95a5bed6d3d63ea77ea8e20ef51799e5ae4ef1df58` 也曾全文读。其 N26 将一个固定 q 的 complex constant 错写为不属于固定 q 的函数域；quarter 独审发现该错误。本文依据修订后的最终全文作出结论，保留修订记录，不把错误版本记作通过。最终稿改为 uniform q-free recovery 命题，并分别证明 W 与 y₀ 不属于实际函数域；这两项修订已实际全文复读。

本轮实际阅读 [Singer 作者原件](../literature/singer2009_differential_galois_lms_author_20261006.pdf) PDF1、13–14、17、20、26，原件82页、SHA256 `c805d45ed54e0e6734b4d7f125c197364b9eccab2a7e09a8c26c3bf63cf5db96`。实际核读范围为 Theorem1.3.9、Corollary1.3.10、Proposition1.3.20/Corollary1.3.21、Schlesinger Proposition1.3.27 及 regular-singular local group；没有声称全文82页阅读。其余具体表示计算为本次独立手核，未冒称 Singer 原文已有 R₀ 结论。

当前权威主报告 §§85–93 本轮已实际全文读。NEW [模8稿](cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md) SHA256 `a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc` 本轮实际全文独核，并另存 [独审](cdt_odd_R0_origin_orbit_mod8_independent_review_20261006.md)，SHA256 `14766f8cb92e52dd180a5668d2b7d78c0f49963580b60768c3bf9c53cd0edd7c`。冻结 exterior、Betti、real、holonomy 稿的此前全读独审属于历史输入，本轮不重复登记为新全文阅读。

## 2. 实际稳定子与六维轨道

N4 的实际向量为 `(e+d)∧p`，其中 p 为非零 oriented Lagrangian bivector。比较 quotient 与 V 部分，确切得到 `MP=P`、`det(M|P)=1`、`a+Md−d∈P`。一次 constant translation conjugation 后，connected stabilizer 是

\[
H_P=P_{\rm add}\rtimes(\operatorname{SL}_2\ltimes\operatorname{Sym}^2P),
\qquad \dim H_P=2+3+3=8.
\]

PV 基本矩阵可逆，固定全部九行等价于固定此实际向量；Singer 的 Galois 对应适用于任何 closed subgroup，不要求 H normal。因此 `L_q=E^{H_q}` 正确，且没有把 L_q 本身误认为 PV 扩张。完整 H 的 negative Kummer component 可由 determinant −1 的 plane stabilizer 与合适 translation 构造；它排除 `sqrt(x)` 留在 `L_q∩E^{G°}` 的可能。有限代数 base extension 不改变 connected group，加入 sqrt 后以连通群论证，未加入时保留 component 判断，范围一致。

N12 的 ambient invariant 计算通过：当 `p∧p≠0` 时，`a↦a∧p` 在四维空间上可逆，translation invariants 与 b 无关。Sp4 在 primitive 五空间的 Lie 像是 so5；其 kernel 同时杀 primitive bivectors 与不变辛 bivector，故杀全部二次外幂，而四维 gl Lie 作用的 kernel 为零。维数相等及 connectedness 给 SO5 全像。非零 quadratic levels 传递，得到 rational invariant field `C(Q)` 与 polynomial ring `C[Q]`。

实际 p 可分解，故 Q=0；b 属于二维 `V∧p`。非零 null bivector 的底空间维数4，加完整二维 translation fibre，恰为单一六维 orbit，实际 invariant field 为 C。合法 actual rational extension 仍受此结论限制；nullcone 上未定义的 0/0 不构成输出。有限 tensor、product 和 contractions 的 coordinates 仍属于原 L_q。

## 3. 群生成的全尺度证明

N14–N15 的关键 Lie 证明已逐 block 手核。若 nilpotent X 不保持 P，其 lower symmetric block C 非零。减去已有 upper block 与 traceless diagonal 后，用 sl2 brackets 消去 scalar diagonal 项，并生成完整 irreducible lower Sym² 模。Upper/lower brackets 给全部四维 diagonal block，连同两个三维 symmetric block 得到 sp4 的十维 Lie algebra。

Affine closure 与 translation V 的交集已含非零 P，且受满 Sp4 投影作用；标准四维模不可约，交集必为全部 V。故 connected closure 为 `Ga4⋊Sp4`，不是仅得 Sp 投影。此证明不依赖具体 d，也未遗漏 source column 或有限 local cover：unipotent powers 的 Zariski closure 含同一完整 one-parameter subgroup。

## 4. 有理微分函数与有限代数根的不同处理

有理函数 f 同时受实际 H 与适当 local monodromy power 固定；若该 power 的 projection 不保持 P，上节给满 connected group，故 f 降到 finite algebraic base。原式的 coefficients 必须固定，不额外输入目标 q。Translation `(q'−q)g₀` 把 Φ(q) 送到 Φ(q')，故一个已降到 base 的固定公式对全 q 给相同整个函数。一个 nonzero PV denominator 在 automorphism 下仍非零，不会在别的 q 变成 identically undefined。

N18–N19 没有把 algebraic root z 当作 PV 元素。z 在 E 上的 monic minimal polynomial 是其在 L_q 上某个 polynomial 的有限组 irreducible factors 之一。Connected H 在这一有限集合上的 rational action 必为恒定，因而固定各 coefficients。若 local continuation 经 finite cover 固定 z，则 transformed minimal polynomial 仍有同一 root，monic uniqueness 使 local power 固定 coefficients。群生成论证遂使 coefficients 降到 finite base，z 仅给 base 的有限代数 branches。

Uniform root comparison 另要求同一个 defining extension/germ 与相同 continuation 规则。连续 family 中 simple branch 不能在固定有限 roots 间跳变；irreducible characteristic-zero polynomial 可 separable 化。按 q 另选不同 root 属于额外离散数据。最终稿没有偷换为“任意 q-dependent root selection 都同值”。

## 5. 三个实际 punctures 的分类

Origin 的全部 transported planes 均不等于 `ker N₀²`，这是本轮模8稿的真实 cycle-period/Kummer 输入，已独核；并非假定 canonical conifold plane 有有理 Betti coordinates。J4 的唯一 invariant two-plane 为 `ker N₀²`，故全部 transported origin branches 都适用第3–4节。Odd Kummer sign 在 finite even cover 被消去；regular nilpotent 不因正倍数而改变稳定 plane。Origin 定理1及 projective affine charts 的结论通过。

Conifold 的 Lagrangian plane invariant 当且仅当包含 vanishing vector v。若不包含，transvection lower block 非零，得到满群与 q-blind output；若包含，完整 paired packet 在该 branch 对每个 q holomorphic，所有合法 rational expressions 对全 q meromorphic。允许 poles 是 CDT 的实际条件；pole order、holomorphic lattice 或 root ramification 另属费用，最终稿没有混淆。

Infinity 的 full J5 是冻结实际 Stieltjes 输入。令 D|V=N∞、De=b，则 `b∉N∞V`，否则可调 e 得 J4⊕J1，矛盾。若 P 不稳定，仍得满群。若 P 稳定，则 P 为 `ker N∞²`，位于 `N∞V`；从 D 减去 H 中同一 Sp projection 后得 pure translation `b+N∞d`，其在 V/P 的像非零。Q_P 对该 quotient 的 SL2 作用不可约，已有 P translations，故交集为全部 V。

此 stable case 的 closure 准确为 `V_add⋊Q_P`，不是 full Sp4。其 fixed field 可保留五个 homogeneous primitive mixed coordinates J，但完整 translation radical 已固定输出，因此仍完全丧失 q。有限 algebraic output 的 minimal-polynomial coefficients 同样 translation invariant。最终稿准确保留了这种区别。

## 6. N26 修订与新增 reference 的确切含义

对实际 homogeneous difference `d_q=h+qg₀−W`，flat symplectic contractions给

\[
C\bigl(y_0,C(d_q,g_1)g_2-C(d_q,g_2)g_1\bigr)
=-2(q-\alpha_0)/\pi^2.
\]

在 q=α₀ 处，d 为 y₀ 加 g₁/g₂ 部分：后两项由 isotropy 不贡献，前者两项对称相消；variation 用 `c(g₀∧g₁∧g₂)=−2v` 与 `C(y₀,v)=1/π²` 得到所示斜率。尺度与符号通过。

对于每个固定 q，右边当然是 complex constant，属于 C(x)。最终稿正确声称不存在一个只从 F(q) 用同一 q-free formula 给出这整个非零斜率 family；否则 origin 定理使其全 q 同值。实际 W 不属于 L_q 的证明独立于常数 family：H 含完整 P translations，任一非零 a 改变 W 为 W+a。实际非零 y₀ 不被 Q_P 固定，因为 SL2 在 P 与 V/P 均无 fixed vectors，故 V 的 fixed subspace 为零。PV 对应给二者各不属于 L_q。

N26 是真实新增 reference 接口，仍需共同算术 germ。单独 α₀ 代数只确定一个 period ratio，不提供 W、y₀、canonical conifold basis 的共同 all-place coefficients。最终稿没有把 origin 的各自良好 normalization 当作免费的 conifold 比较。

## 7. Rational disk 共同域与明确保留的 root 分支缺口

N10a 定理3的 coefficients 明确限定 C(x)，φ 为列明的 nonconstant holomorphic disk map，target t=1−x，canonical germ 在 t=0。若所有 outputs 已 q-blind，共同域显然成立；否则选一个 sensitive output。任何 origin preimage 的 positive winding 会由定理1迫其 q-blind，矛盾，故该 map 避开 origin。Holomorphic map 无 infinity preimage；列明的 meromorphic 扩展用定理2另排除 infinity pole。

每个 conifold arrival branch 若 plane 不含 v，也会迫 sensitive output q-blind；所以必须含 v，完整 F(q) 对全 q 都在该 branch 填回且 local loop trivial。Punctured disk 的 loops 由 small preimage loops 生成；open disk 时每个 loop 落在一个只含有限 preimages 的 compact subdisk。这样 whole packet 对全 q 单值并填回，fixed rational functions 只产生允许的 poles。分母非零由 translation automorphism 控制。没有依据 arbitrary nonlocal-word 分类来偷证本定理。

N27 的 finite 或 infinite linear differential-span rank 相同，也直接来自 translation field automorphism 固定 C(x) 并交换 θ；未因此声称新 ratio 必 D-finite、rank=9/10 或继承原 species/denominators。

Finite algebraic roots 不属于这个共同域定理：ordinary discriminant zero 会给新的 q-dependent branchpoints。原三个 punctures 的 minimal-polynomial 结论不删除此剩余可能。任何尝试利用这些新的 branchpoints，都还须给 finite actual holonomic rank、完整算术 germ、所有 places/embeddings 与真正 boundary hypotheses。审阅不新增 finite-isogeny 或一般 holonomic-root 定理。

## 8. 结论、范围与执行记录

最终 `ec6ad8…fd59b` 全文声明范围独审通过：实际八维 connected stabilizer、六维 orbit、ambient/actual invariant fields、局部生成 lemma、有限 roots 的 minimal-polynomial interface、三个 punctures 的 nonlinear 分类、rational disk 共同域及实际 rank 参数不变。

这一通过不意味着获得新的无理性或超越性。新的 independent periods、非代数 gauges/积分变换、带 jump 的局部 height 理论、任意 nonlocal-word quotient 分类与 ordinary discriminant roots 仍在本文范围外。原含1十行 `τ=329/50`、`a=8sqrt(2)` 和全部 places 预算仅适用于原 packet，不免费赋给新 rational outputs。

本独审不下载新 PDF、不执行数学 producer；既存 Singer 六页的只读抽取/hash 不属于数学 producer。全部 old/peer mathematical producer execution/import/rerun 为0。本独审作者保存后实际全文回读并冻结；review SHA 在父任务收据另登记，以避免自引用 hash。
