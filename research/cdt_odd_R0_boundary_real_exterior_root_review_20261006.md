# R₀ 全角点、实结构和端点外积的 root 独立审阅

日期：2026-10-06。NEW 纸面审阅。root 实际全文读取下列三份作者稿，并实际回读所有终稿变动；旧/同行数学 producer 的执行、import、rerun 数均为0。本文不是对自己 authored 的局部边界稿作独立审阅；那一稿另有 quarter 的实际终稿全文独审。

## 1. 最终审阅对象与判定

* [全角点 centered compact current](cdt_odd_R0_positive_cut_boundary_flux_20261006.md)，最终 SHA256 3fabdbfa3f4c0fd17e50db268b86cfe8c7d752f71a462bcdf0ebaeb1faa3d150。初稿实际全文读 F1–F11；终稿 F6 的 rational quotient 说明、F8 的 fine relative complex/primitive 构造又实际全部回读。**通过**。
* [实结构与实际剩余周期](cdt_odd_R0_real_Betti_normalization_20261006.md)，最终 SHA256 dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f。实际全文读 R1–R45，另实际回读终稿 §§9–11。**通过**。
* [实际 exterior packet](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md)，最终 SHA256 b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef。初稿实际全文读（组合输出首段截断后另完整读取 E1–E7）；终稿新增 E7a、E20.3 和 E11 奇偶 cover 限定另全部实际回读。**通过**。

这些是全尺度纸面证明的内部独立审阅，没有 Lean、形式化内核证书或新数值无理性 claim。结论涉及指定 rational model 与 explicit lift；integer saturation 和有效全部 place 费用仍未完成。

## 2. 全角点延拓的关键链条独核

F2 的 minimum support 保证每个非零 horizontal ray 同时有 pole coordinate 和 forced \(-1\) coordinate，其 lattice identity 是
\[
 2\sum_{i\in S_-}n_{b,i}=\sum_{i\in S_p}n_{b,i}>0.
\]
因此 \(b_b=\sum_{S_-}n_{b,i}\ge1\) 对**每条** surviving ray 成立，而不是只在某个 divisor generic point 成立。

F3 对实际 fibre cut 的 angular rank 已核：fixed \(0,\infty\) cut characters 与 \(\ell\) independent，因至少一个未切 forced \(-1\) coordinate 的 \(\ell\)-coefficient 为2；free cut rows形成 identity block。regular toric lattice matrix 不改变 rank。解 \(\phi=cq_0=\lambda\) 后，这就是 modulo fibre phase 的 full rank。\(c/c_S=1+O(z)\) 及其 angular derivatives 保持统一小扰动，所以在 finite atlas/compact parameter disk 中可取统一 coarea bound。该 coarea 只沿角变量，不给额外 radial negative power；delta 的 radial components 在 logarithmic frame 至多 bounded。

F4 的共同因子更强于“挑一个 forced coordinate”：令 \(i_0=\min S_-\)，ordered product 中 \(j>i_0\) term 因空 cut 为零，\(j=i_0\) 的 centered log 给 \(z_{i_0}\)，其它 forced differentials 给全部剩余 \(z_i\)；\(j<i_0\) 的 dlogs 已含全部 forced \(z_i\)。故所有 surviving terms 均含 \(\prod_{S_-}z_i\)。这使 radial measure 被
\[
 \prod_b\rho_b^{b_b-1}d\rho_b\,
 (1+\sum_b|\log\rho_b|)
\]
控制，可积。所有 \(\rho_b=\epsilon\) faces 对任意 smooth test form 的作用均为 \(O(\epsilon(1+|\log\epsilon|))\)，所以零延拓没有任何 boundary-supported derivative。此证明同时处理 total space 与实际 fibres，得 \(d\widetilde R^c=\Omega_Y\) 和 fibrewise closedness。

F6 的 ordinary rational correction 可独立从 \([a\Delta_i]=[B_i]\) 逐项核为
\[
 [R^c-R^+]=-\frac{a^4}{2}\sum_j(-1)^j
 e_0\wedge\cdots\wedge\widehat e_j\wedge\cdots\wedge e_3.
\]
不同 degrees 的 product 符号与原 ordered KLM cup 一致。它是 OPEN Tate class，不需属于 compact image。compact AJ restriction injection 则用真正的 rational linear injection：
\(A_{\mathbf C}\cap B_{\mathbf Q}=A_{\mathbf Q}\)；
因此 centered extension 的 open regulator 身份确实决定其 compact AJ class。

F17 的最后 constant term 为 \(a^4/2\) 倍 triple-cut top-form integral。两实际 sheets 的 LEFT residues opposite，normal-first orientation 相同，且逐 sheet 绝对收敛；故它为零。由此
\[
 Q(r_c,\omega)=-16a^3W,\quad
 Q(r_c+a^4PD\Gamma/8,\omega)=-16a^3\Psi.
\]
这是 specific chosen lift 的精确 scalar 身份。加项数值亦核：
\(a^4(-4i\pi^3)/8=-8i\pi^7
 =16a^3\pi^4/16\)。
没有由 conifold holomorphy 猜其三个 homogeneous coefficients 为零。

F8 已补足 SNC fine kernel 模型：commuting coordinate projections 的 inclusion-exclusion 延拓和 higher Cech contraction 给 exact augmentation；radial homotopy 保持每个 divisor 的 pullback-zero 条件，boundary stalk cohomology 为0。故 kernel fine complex 确计算 relative cohomology。regular neighborhood 的 topological retract只用于 \(H^{2,3}(N,E)=0\)，不用于 nonsmooth pullback forms；于是有 smooth relative primitive。它在每个 logarithmic normal direction 都含 \(\rho_b\)，用 Hadamard decomposition 对独立 variables 迭代给**乘积** bound。旧 raw current 对它的所有 face flux 为零。结论只给 canonical \((\omega,0)\)，不冒认任意 rational horizontal splitting 的 flux 也为零。

## 3. 原开放障碍与 explicit compact marking 的一致性

root authored 的 [局部边界稿](cdt_odd_R0_noncompact_Tate_boundary_period_20261006.md)，最终 SHA 00d1cb69f8cf783b842dd5c53331368bcf95fddf69135e80f614c4f0598372c1，证明一个 actual compact bounding torus 的 \(R^+\)-period 为 \(a^4\)。其 [quarter 独审](cdt_odd_R0_noncompact_Tate_boundary_period_independent_review_20261006.md) 已实际全文读，最终 SHA 652483276ee0e98787e792822243c3842aa1b2dec27594fbf144aee570fec5b6。

因此未 centered 的 open discrepancy 对所有 compact lifts 都非compact；不能将其 relative boundary 再列为“也许待证为零”。F16 改变的是 open representative，消去此 obstruction，所以 F4/F19 与这个反例没有冲突。F20 的 canonical trace zero也不要求其 ordinary class compact。

本轮 actual marked identity 已完成。对其它旧膜/任意 lift，仍存在 rational compact ambiguity；这是选择比较，不能再将它描述为此 explicit centered lift 的 scalar gap。

## 4. Real proof 的 sign、剩余真实周期与正性独核

complex threefold 的 conjugation degree 为−1，故 raw cup 的 \(B\) involution anti-symplectic，且 \(BPD\gamma=-PD(c_*\gamma)\)。真实 sphere 的 antipodal \(S^3\) map degree+1，Γ的三个 CCW contours各翻向给−1，遂 \(PD\delta\) 是 minus、\(\Pi PD\Gamma\) 是 plus。rank4 的两 rational eigenspaces 各维2；再施 δevaluation zero 的 plus-space是维1。真实 real average 只加 rational compact Tate class，合法性不依赖原 open discrepancy compact。

物理 monodromy 使用 single-valued algebraic \(\eta=\omega/\sqrt{x}\) 的算子
\((\theta+1/2)^4-x(\theta+1)^4\)，origin eigen−1、infinity eigen+1，traces −4/+4。PL rank-one trace给 \(\delta\cdot M_0\delta=-8\)，所以 signed \(U_0=-M_0\) 才给+8。R26 的 cycle
\(\gamma_L=-(M_0-M_0^{-1})\delta-2\Gamma\)
是 actual integral transport combination，不能称 \(U_0\) physical loop。其 V-projection 非零由 \(N^2\delta\ne0\) 核准。

Frobenius basis 的 concomitant matrix直接核 \(C(f_0,f_3)=-1,C(f_1,f_2)=1\)。由
\[
 C(g,g_{U_0})=a(2b_1-b_2^2)+a^3/6
\]
和 raw \(\kappa=-a^3/16\) 的 dual sign得
\(2b_1-b_2^2=-4\pi^2/3\)。R34 正确。Abelian \(t\log t\) coefficient为 \((b_2+8\log2)^2/4\)：\(a_n\sim1/(\pi^2n^2)\)、\(\operatorname{Li}_2(1-t)\) 的该 coefficient为1；其余 \(O(n^{-3})\) series 有连续 first derivative，不影响此项。conifold holomorphy遂确定 \(b_2=-8\log2\)。

R40 的 positive half-integer tail 与 R35 完全相同。R41 的 n0 contribution 恰 \(16\pi^2\log^22+\pi^4/3\)，其余严格正，tail \(O(n^{-4})\)，故实际 endpoint lower bound成立。origin log² coefficient \(\pi^2/4\) 超越，只证明此 Nilsson normalization 的成本；不能推出 conifold Taylor coefficients非代数。任意 real+δ lift 的 remaining Q-line仍存在，与已明确选择的 F19 lift完全相容。

## 5. 外积完整计秩、D七和局部解析数据独核

五阶 actual extension 非分裂，homogeneous connected group是 Sp4。其 translation kernel是标准 irreducible 四模的 stable additive subgroup，只能0或全；0会使 reductive representation split，故实际为 Ga4。第三 wedge 的 symplectic primitive kernel有 exact factors 4和 \(\chi\cdot5\)。实际 wedge 的非零 primitive quotient 与 translation-generated bottom使 orbit span恰9。coordinate relation必须杀全部 orbit，从而为0；scalar012在 bottom 非零且 translation不能留下 quotient-only kernel，故 minorder9。无 trivial factor，常数1确为第十行；finite covers同样保持 connected group。

实际 \(c_B\) matrix 逐列核为
\[
 \begin{pmatrix}t&0&0&0\\-x&t&0&0\\x/2&0&t&0\\0&x/2&x&t\end{pmatrix},
\]
其 determinant \(t^4\)，inverse 的 apparent poles必须保留，不能称 original integer lattice不变。用 exact concomitant identities另证
\[
 Z_j=F_1\theta^jg_2-F_2\theta^jg_1-2\alpha_0\theta^jv.
\]
\(F_j\) 全前缀付 \(D^4\)，乘 homogeneous jets 再付 \(D^3\)，四 Z 行得到 \(D^7\)；五 mixed rows为 \(D^6\)。coefficient-by-coefficient convolution的指数依赖 indices总和，保留 \(C^{N+12}\)，没有免费删固定坏素数或付错误 \(C^{2N}\)。此改进需 hypothesis \(\alpha_0\in K\)，并非 \(R_0-M_0\in K\) 的同义式。canonical endpoint \((0,2\alpha_0,-\alpha_0,\alpha_0/4)\) 用 v的前三 coefficients核准。

Conifold transvection固定该 wedge iff \(v\in P_\gamma\)，与q无关。raw jet minors可以有 \(t^{-1},t^{-2}\) apparent poles，须额外 \(\ell(\gamma(h+qg_0))=0\)。t²regularization与辛收缩的新九行tuple都清除这些 poles，才具有 fixed iff fillable 的 q-blind criterion。目前没有实际 word证明 raw tuple新增 value-sensitive filled branch。

真实 Stieltjes积分缩放给四维 crosspolytope体积 \(2/3\)，所以 \(B(-R)\sim\log(256R)^4/(384R)\)。log⁴迫 actual infinity J5，三平面含 nonzero quotient不能是其唯一 invariant三flag；因此任何有限 cover的 infinity branches都不可填。

Origin的 semisimple projector \(p_+\) 是 local monodromy 数据，未作为免费 arithmetic gauge。contraction gives \(c(\Phi_0)=-2v\)，actual cup给 \(C(y_0,v)=1/\pi^2\ne0\)，且 actual \(p_+\Phi(\alpha_0)\) 是 \(y_0\wedge g_1\wedge g_2\) 的倍数，所以
\[
 N_0^3p_+\Phi(q)=0\quad\Longleftrightarrow\quad q=\alpha_0.
\]
这是 actual endpoint-sensitive highest-log relation，而非已构造的填点或 capacity increase。E30 对 transported origin的潜在 criterion已经明确仅在 even cover杀掉 Kummer sign后使用；odd loop mixed quotient不 fixed。

## 6. 同行互审终稿也已实际全文回读

* [全角点 independent review](cdt_odd_R0_positive_cut_boundary_flux_independent_review_20261006.md)，最终 SHA 7cfbcce37c932b1ecd8b734ceaf8993d1c383798ee25c59958c6fb857b731b16。root实际全文读 I1–I9，与作者稿的全cone、allface、AJ、scalar和canonicalrelative接口逐项相符；其本轮没有新增原件页阅读的限定保留。
* [外积与 real 双稿 independent review](cdt_odd_R0_endpoint_sensitive_exterior_packet_independent_review_20261006.md)，最终 SHA 0ff0e13e00142733e81587bcc11e2b1bcbd3040e057b4d6b613ea8a8c9f940d0。root实际全文读 I1–I9，涵盖两个最终主稿全部数学、D七、E30 even-cover补强、真实physicalsign与positivecost；其原件FR/KLM actual页范围另精确登记。
* quarter 的 root局部边界稿独审已在§3登记，root同样实际全文读终稿。root自己 authored 的局部定理不冒认 self-independent-review。

两份新 literature receipts也已由root实际全文读，其 primary SHA/版本与无新PDF/无producer scope一致。全角点 receipt 的 root局部稿 fb91af… pin是实际早期阅读snapshot，已明确写成“before final root freeze”；它不是对root终稿SHA的未来断言。后续排版修订和终稿00d1cb…独审已另记录，历史snapshot不改。

## 7. 原件、执行与尚缺输入

本轮 root实际原件页：KLM published PDF8–12；Deligne HodgeIII PDF37–41；FR published PDF2–5、9。PDF text只读；本轮新数学不使用有限验证器。网页另核 KLM primary与Deligne Numdam元数据；没有新增PDF。

本轮真正新增接口是 actual rational marked compact regulator identity、canonical raw flux zero、explicit noncompact open Tate period、实际 real-compatible剩余 cycle，以及目标敏感外积和D七安全阵列。下一步必须在这个真实完整元组上计算 local \(p_+,N_0\) 的原 Betti/deRham格 comparison，并证明可用于 CDT 的 endpoint-sensitive analytic estimate、有效 C 和全 place 费用。尚无数值无理性/线性无关性、integral saturation 或 Lean结论。
