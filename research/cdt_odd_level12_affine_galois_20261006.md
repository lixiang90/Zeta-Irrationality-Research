# D12 两个真实周期的完整仿射代数闭包与低阶投影障碍

日期：2026-10-06。新全尺度理论稿。固定已经实际审阅的[九生成元真实周期](cdt_odd_level12_generator_cocycle_20261006.md)、[共同整模型](cdt_odd_level12_joint_full_model_20261006.md)及[真实 Bol 算子](cdt_odd_level12_paired_coordinate_20261006.md)。不执行或导入任何冻结数学 producer，不枚举短 words，不扫描参数。本稿证明的是实际函数及其 monodromy 的结构结论，**没有证明新的数值奇 ζ/L 无理性**。

## 1. 实际函数、共同基底与要证明的结论

令 Γ=PSLΓ₁(12)、v 为已证实际 Γ-Hauptmodul，取基域 k=C(v)，导数为 ∂=d/dv。采用
\[
h_Z=f_Z-103680\zeta(3),\qquad
h_L=f_{\sigma,L}+34560\sqrt3L(3,\chi_{12}),
\qquad H_j=B h_j,\quad B=E_2-12E_2(12\tau).
\tag{A1}
\]
这里 h_L 是真正共轭 source 的 primitive。两函数均是实际复解析函数；C 包括它们的数值常数，不假设这些常数为代数数。对 Γ，ε=+1，实际周期是
\[
h_j|_{-2}\gamma-h_j=i\pi^3P_j(\gamma),\quad
P_j(\gamma)\in\mathbf Q[\tau]_{\le2}.
\tag{A2}
\]

令 V 为 normalized Sym² 的三维空间，采用冻结稿的右作用、basis(1,τ,12τ²)和归一80。两周期同时给 affine V⊕V 作用。下文证明：

1. Γ 的双周期仿射表示之复 Zariski 闭包恰为 (Ga⁶)⋊PSL₂，维数9；每个单周期闭包是 Ga³⋊PSL₂。
2. 两实际强迫方程的共同 Picard–Vessiot 场 L，在齐次 Picard–Vessiot 场 K₀ 上是六变量纯超越扩张。
3. H_Z,H_Z′,H_Z″,H_L,H_L′,H_L″ 在 K₀ 上代数独立。它们构成的有理表达式若对全部 Γ 单值不变，必已属于 k。

这排除在**这两个固定源及其低阶 jets**内，用有理或代数规范因子消除全部周期、同时保留目标原函数信息的做法。它不排 thin subgroup 的实际解析叶、新源或新的非代数积分。

## 2. 两个抛物元证明周期类在 C 上独立

若 P(γ)=Q|−2γ−Q 是 quadratic coboundary，γ 是 det1 抛物元且固定有限点 r，则
\[
P(\gamma)(r)=\{(cr+d)^2-1\}Q(r)=0.
\tag{A3}
\]
因为 γr=r、(cr+d)²=1。这对 Q 的任意复系数成立，也适用于把 coboundary 的符号反过来。

使用两个完全确定的实际 Γ 元：
\[
\eta=\begin{pmatrix}1&0\\12&1\end{pmatrix},\quad r_\eta=0,
\qquad x_8=\begin{pmatrix}13&6\\-24&-11\end{pmatrix},
\quad r_8=-1/2.
\]
冻结表准确给
\[
P_Z(\eta)=0,\quad P_L(\eta)(0)=44160,
\tag{A4}
\]
\[
\begin{split}
P_Z(x_8)(-1/2)&=5218560-11819520+6739200=138240,\\
P_L(x_8)(-1/2)&=2819360-6361920+3614880=72320.
\end{split}
\tag{A5}
\]
因此若 aP_Z+bP_L 是任意 C-coefficient quadratic coboundary，先由(A4)得 b=0，再由(A5)得 a=0。两个 cohomology classes 在 **C 上**线性独立，而非仅在 Q 或 Q(√3) 上独立。

整数归一与改用 γ⁻¹把右作用转为左作用，只是固定基变换或 coboundary 符号改变，不影响此判断。下文谈代数群时可用 A_{γ⁻¹} 的标准左 homomorphism；冻结的实际 word 顺序仍是 A_{γδ}=A_δA_γ。

## 3. 双仿射 Zariski 闭包

记 G=PSL₂(C)，作用于 V=Sym²(C²)，中心±I已经除掉。Γ 的 linear image 在 G 中 Zariski dense：T 的所有整数幂闭包含完整 upper root subgroup，η 的幂闭包含完整 lower root subgroup；这两个 root subgroups 生成 G。V 是不可约 G-module，End_G(V)=C。

令 H 是双 affine image 在 (V⊕V)⋊G 中的 Zariski 闭包，N=H∩(V⊕V)。代数群 homomorphism 的像是闭代数子群，因此 H→G 满射。特征0的 additive group 代数子群是 connected 线性子空间；N 是 G-stable。上述基础输入可见 Milne 的 Theorem3.34、Corollary14.33 和 Theorem22.42，固定作者原件及实际阅读范围见[新文献清单](../literature/manifest_cdt_odd_affine_galois_20261006.json)。

若 N≠V⊕V，则 semisimplicity 与 Schur 引理给某个非零 equivariant quotient
\[
\ell:V\oplus V\longrightarrow V,\qquad
\ell(z,l)=az+bl,
\quad \ell(N)=0.
\tag{A6}
\]
将 H 映到 V⋊G，其像 J 仍闭，J→G 满射且 translation kernel 为0。特征0下这个 bijective algebraic-group morphism 是 isomorphism，因此 J 是 G 上一个 algebraic crossed-homomorphism 的图。

这种图必有 affine fixed point：其四维 linear representation 具有 exact sequence 0→V→E→1→0；G reductive 的特征0 finite-dimensional representations semisimple，故有 invariant lift (w,1)。因此图的 translation 是 w−gw，是 coboundary。限制回 Γ 就迫 aP_Z+bP_L 为 coboundary，与§2矛盾。

故 N=V⊕V。再用 H→G 满射，任一个 lift(g,b)都可乘一个 translation 消去b，所以
\[
\boxed{H=(\mathbf G_a^6)\rtimes PSL_2.}
\tag{A7}
\]
所有 graph、image 和 quotient 在这里都是 characteristic0 algebraic groups；未把 discrete Γ 的 H¹ 误称为0。恰是 Γ 上的两个非零独立 classes 迫 algebraic closure 出现完整 translation radical。

投影到任一个 V 因子，立即给单目标 closure Ga³⋊G。H connected，所以任何 finite-index Γ subgroup 的 closure 仍是 H：有限多个 proper closed cosets不能覆盖一个 connected irreducible algebraic group。这将适用于有限代数覆盖，但不分类 Γ 内原点稳定子的 discrete free words。

## 4. 在实际 C(v) 上构造共同双强迫系统

本节补实际 differential-module 接口，不能由一张形式 affine 表直接宣布 differential Galois 群。令 k_v=θ_qv、r_v=k_v′/k_v，按冻结 Bol 证明拉回到 v，有
\[
L_0=\partial^3+3r_v\partial^2+(r_v'+2r_v^2)\partial,
\qquad L_B=B L_0B^{-1}.
\tag{A8}
\]
齐次解是 y₀=B、y₁=Bτ、y₂=12Bτ²。Γ 的实际 transformation 给常数 normalized Sym² matrices；因此 monic L_B 的 coefficients Γ-invariant。冻结稿§6在 finite points 和 cusp 的有限 Laurent pole论证逐项在 v 上成立：Γ无 elliptics，v 是 compact P¹ 的坐标，故 L_B=∂³+a₂∂²+a₁∂+a₀，a_i∈k。

两个 source 仍是同一 Γ 上的 weight4 forms。chain rule θ_q³=k_v³L₀、L₀1=0 给
\[
L_BH_Z=R_Z:=BF_Z/k_v^3\in k,
\qquad L_BH_L=R_L:=BF_{\sigma,L}/k_v^3\in k.
\tag{A9}
\]
weight2+weight4−3·weight2=0 保证 Γ-invariance；有限 Laurent poles保证在 P¹ 上有理。常数 Ξ_Z、Θ 不改变 forcing。这里不用任何数值有理性假设，也没有把 F_L 的 U_p packet 借给 F_Z。

令 C 是 L_B 的三阶 companion matrix，e₃=(0,0,1)^t；令 Y=(∂^iy_j)_{0≤i,j≤2}，u_j=(H_j,H_j′,H_j″)^t。精确构造七维有理系统
\[
\partial\begin{pmatrix}u_Z\\u_L\\1\end{pmatrix}
=\begin{pmatrix}C&0&R_Ze_3\\0&C&R_Le_3\\0&0&0\end{pmatrix}
\begin{pmatrix}u_Z\\u_L\\1\end{pmatrix},
\qquad
\mathcal Y=\begin{pmatrix}Y&0&u_Z\\0&Y&u_L\\0&0&1\end{pmatrix}.
\tag{A10}
\]
Y 可逆：Wronskian为24 B³(τ′)³≠0，其中 factor12来自第三列12Bτ²。于是(A10)是实际 fundamental matrix，不是把formal primitive symbols当成独立函数。

## 5. Regular singular 与 monodromy 的完整核验

在有限非cusp点，τ 是 v 的解析局部 inverse，B、sources 全纯；B 的零引入 apparent poles，但所有列及其有限阶导数至多有限幂增长。在每个 Γ cusp，使用实际 SL₂ scaling A 与真实 cusp width：F|₄A 有 constant 加 holomorphic positive cusp terms。Bol 给
\[
h_j|_{-2}A=\text{degree≤3 polynomial in }\tau_c
 +\text{holomorphic positive cusp series}.
\tag{A11}
\]
其中 degree3项由 source constant决定，degree≤2项包含实际周期。B|₂A 有 ordinary finite-order cusp expansion；原 H_j=B h_j 的 scaling factors恰相消，因此为 finite Laurent factor乘 degree≤3 log polynomial及holomorphic项。齐次 B、Bτ、Bτ² 在同coordinate也为 finite Laurent factor乘 degree≤2 log polynomial。

Γ torsionfree；local v 或1/v在每个cusp是uniformizer。有限次 v-derivatives不会超过有限幂/log增长。故(A10)的整张 fundamental matrix在各sector有 moderate growth，齐次系统与双强迫系统都 regular singular。包含 B-zero 的 apparent points不会增加 monodromy。

因此 Schlesinger 定理适用，differential Galois group是**实际** monodromy 的 Zariski 闭包。Singer 的 Proposition1.3.27与 PV field 定义、Theorem1.3.9/Corollary1.3.21，见[作者原件](../literature/singer2009_differential_galois_lms_author_20261006.pdf)。只读相关页，不声称通读82页。

## 6. 共同齐次场与完整 Ga⁶ translation subgroup

令 K₀=k(Y,1/detY) 是齐次 PV field，L=k(𝒴,1/det𝒴) 是双强迫 PV field；解析 germs 的常数域为 C。齐次 monodromy 恰 Γ 的 normalized Sym² image，closure是 G，所以 Gal(K₀/k)=G。

任意 σ∈Gal(L/k)满足 σY=Yg、σu_j=u_j+Y a_j，g∈G、a_j∈C³；两个Y blocks是**同一个**实际Y，不能为它们独自选择不同g。因此
\[
\operatorname{Gal}(L/k)\subset(V\oplus V)\rtimes G.
\tag{A12}
\]
Γ 的实际 analytic continuation 同时给 u_j→u_j+iπ³Y·coeff(P_j)。80及third-coordinate12是固定共轭基变换；整个 seven-dimensional monodromy与§3的双 affine representation相同。因此(A7)、(A12)及Schlesinger给
\[
\operatorname{Gal}(L/k)=\mathbf G_a^6\rtimes G,
\qquad \operatorname{Gal}(L/K_0)=\mathbf G_a^6.
\tag{A13}
\]
这是当前两 source 的真实 differential Galois 结果，不是 Γ full zero-kernel 的分类。对于 signed M extension不额外推 connected-component外的全部群；本稿已经在 Γ 上证明所需结论。

## 7. 六个低阶 jets 的实际代数独立与投影限制

L由K₀及六个u_j coordinates生成，∂³H_j已由(A9)在这六个coordinates和k中表示，所以没有另需的高阶generators。PV transcendence-degree公式及(A13)给
\[
\operatorname{trdeg}_{K_0}L=6.
\]
六个generators恰因此代数独立：
\[
\boxed{L=K_0(H_Z,H_Z',H_Z'',H_L,H_L',H_L''),
\quad L/K_0\text{为六变量纯超越扩张}.}
\tag{A14}
\]
也可直接核：Ga⁶分别任意平移u_Z,u_L中的三维解Y a_j，detY≠0，故不能有非零polynomial relation。

首先，任何这六个jets和K₀构成的 rational expression 若在完整 translation radical下不变，必属于K₀。再若它对全部Γ analytic continuation不变，闭包密性及(A13)使它在完整 Gal(L/k) 下不变，故准确属于k=C(v)。它的值只由base决定，不包含新的 primitive extension方向。所有有限阶derivatives都由(A9)归约到这六jets，故结果也包括高阶rational differential expressions。

若仅加入K₀的有限代数extension作为 gauge field，六jets的代数独立仍保留：代数coefficients的新relation取field norm/有限conjugates会给K₀上的旧relation。其translation invariant field也只为扩大的gauge field。若在base做有限代数覆盖，§3的finite-index closure与同一moderate-growth论证保留 connected Ga⁶。这些操作仍不能由代数规范因子制造一个保存 primitive信息的全Γ invariant scalar。

此结论只谈指定两source、algebraic gauges/finite covers与rational differential constructions的**完整Γ**不变性。它不排新增源、独立非代数函数、thin subgroup不变目标、成功的Taylor混合格或CDT对非trivial bundles的新评价证明。C包含所有数值周期，故不能从(A14)的functional algebraic independence推出ζ(3)和L(3,χ12)的数值线性无关性。

## 8. 对下一步的影响与审阅状态

完整真实周期现在不仅有integer表，还证明了两个primitive方向的所有六个低阶translation方向都存在于实际Galois群。因而在固定两源内继续寻找全Γ的有理tensor/jet投影，必然丢失primitive信息；新的数值路线应改变实际source/非代数扩张，或分类thin真实稳定子并构造更大的合法map。

本稿不重复执行旧有限证书。§2 arithmetic逐项展示，§3是全尺度代数群证明，§§4–7是实际Bol系统/PV/regular-singular链。helper和low_period均已实际只读全文§§1–8，独推任意C-coefficient coboundary独立、closedimage/semisimple splitting、finite-index connectedclosure、同C(v) Bol forcing与共用Y、Wronskian24B³τ′³、全部cusps moderate growth/Schlesinger、Ga⁶ PV radical、六jets及有限代数gauge/base-cover scope，通过；两人均未执行producer，也未把functional结论转成数值结论。已修唯一LaTeX排版项，数学输入未改变。helper的[实际独审记录](cdt_odd_level12_affine_galois_review_20261006.md)另存；low_period的实际审阅范围在本节外部登记。本稿按此范围冻结，无PY/JSON数学producer。
