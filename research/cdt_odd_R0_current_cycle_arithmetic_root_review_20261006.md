# R0 本轮独审：open class、support trace、单初值 dual 模型及完整秩六

日期：2026-10-06。Root 的 NEW 纸面审阅及一个新增完整计秩证明。三个同行证明均实际全文读取，原件关键页另实际核读；没有执行、导入或改动旧/同行数学 producer。Root 自己的消失球稿由另一代理独立审阅，不在这里冒认 root 对自己稿的独立审阅。

## R1. 实际全文审阅的稳定输入及判定

1. [positive-cut class](cdt_odd_R0_compact_positive_cut_class_20261006.md)，SHA256 `094aa342bb462a080c99b525110e8b1738acb58897aa2e4fbe9aa991a521c5d7`：C1–C20、remaining scope及来源全部实际全文读。声明范围通过；没有升级为 compact raw-scalar equality。
2. [boundary membrane comparison](cdt_odd_R0_boundary_membrane_comparison_20261006.md)，SHA256 `2bded7f6e0e6efab5e67f985df38754e5a8b2f99b4e4394d46a6f86a20952c3d`：B1–B25、scope及来源全部实际全文读。已证 support/Stokes/四参数接口通过；B18 仍条件，未核准 flux zero。
3. [actual arithmetic hypotheses](cdt_odd_R0_conifold_actual_arithmetic_hypotheses_20261006.md)，SHA256 `83e5fb5cb3e7cad72440d04e4f75230c895d2865bc68c1565160a6c3b313d567`：A1–A28、scope及来源实际全文读。首次读到 author 尚未修复的一个 `quad` 格式；author 自己修成 `\quad` 后 root 另核最终指纹。未发生数学改动或 producer 重跑。rank-five germ、单初值整化和 no-go 通过；A5 对额外常数1尚不计秩，本稿 R5 补上实际秩六，不更改已冻结稿。

Root 实际读 [消失球归一化](cdt_odd_R0_vanishing_regulator_normalization_20261006.md) 的自己最终稿和该稿独审；其最终输入 SHA 是 `7a254a5d974379a76142aee36120390d5dbd7491c4794d97997976d082cbf296`。新增数学结果仍为指定实际 regulator 的一项 vanishing normalization，而非完整数值身份。

## R2. Intrinsic phase、实际 open AJ 类与 rational open 差额

在单个 unit 上，\(L^+-L^-=2\pi i\chi_{\operatorname{Im}v<0}\)，且
\(d\chi=\delta_{T^-}-\delta_{T^+}\)。用 current cone differential
\(D(A,B,C)=(-dA,-dB,dC-B+A)\)，直接核到
\[
 D(2\pi i\chi,0,0)=\mathcal U^+-\mathcal U^-.
\]
四个不同坐标的 exterior product 的 Leibniz 符号为 \((-1)^j\)，其 third component 与既有 raw positive-cut integral 的 ordered-delta 表达式完全相同。这里 product 在 universal \((\mathbf C^*)^4\) 上定义，未把 positive ray 穿过 cubical 删除值1误当成原 Bloch negative-chain complex。

Actual fibre pullback另经几何核查：若 proper partial cut 的所有 free coordinates derivative 为0，则它们只能为1（−1给 \(\phi=0\)），而 positive coordinates 使 \(\phi\ge256\)，与 \(\sup_D|\lambda|<256\) 矛盾。故全部 positive cut strata 与 fibre transverse，full cut为空。Universal intrinsic class pullback确为文中的具体 current，给真实 \(j^*AJ\Xi=[R^+]\)。没有要求 mixed negative/positive homotopy itself 可在该 fibre 逐项 naive pullback。

Total-space 代表差 \((0,0,S-R^+)\) 的 cone coboundary中，\(F^4D^3=0\) 消去 filtered项，first component给 rational Tate cochain closed。因此 ordinary difference是真正 total-space \(\mathbf Q(4)\) class，fibre restriction flat。这比相同 forcing 更强，但它是 **open** class。

Poincaré–Lefschetz \(H^3(U,\mathbf Q)\simeq H_3(X,E;\mathbf Q)\) 与 relative homology exactness给
\[
 a\in j^*H^3(X,\mathbf Q)\iff\partial A^{\rm rel}=0\in H_2(E,\mathbf Q).
\]
Root 核准这项 kernel/image 条件，而没有假定 \(\partial A^{\rm rel}=0\)。

## R3. Support lemma、两个 trace 与正确 Stokes 符号

Deligne 原始 Proposition8.2.7 给从 smooth proper \(X\) 向 proper \(E\) 的 restriction kernel，可通过 \(\coprod E_i\to E\) 检验。每个 actual rational projective surface 的 \(H^3=0\)，故 \(H^3(X)\to H^3(E)\) 是零映射；不是说 singular \(H^3(E)=0\)。relative exact sequence因此严格给
\[
 H_c^3(U)\twoheadrightarrow H^3(X),\qquad
 \ker j_!=\operatorname{coker}[H^2(X)\to H^2(E)].
\]

Boundary 稿的 \(\sigma\) 是 contractible parameter disk 上 **指定、非canonical** rational horizontal right inverse。其 adjoint \(\tau_\sigma\) rational/horizontal，且 \(\tau_\sigma j^*=\Pi\)。这不假设全局或 Hodge/integral splitting；也不杀掉所有 higher-weight rational open classes。

另一个 canonical support class是实际 holomorphic form的 \([\omega,0]\)。SNC relative smooth-form model可用逐component restriction-zero的fine complex：每个边界stalk的radial homotopy保持所有 components并contract到boundary center，故该complex locally acyclic，计算 \(j_!\mathbf C\)。这个 class可由compact-support form代表，但它未被证明等于 rational-horizontal \(\sigma(\omega)\)。Root 保留两种 trace 的区别。

对任一指定 support representative \(\beta\)，\(\omega-\beta=dk\)。由于 \(R^+\) 的 degree为3、fibre上closed，
\[
 d(R^+\wedge k)=-R^+\wedge dk,
 \qquad \langle[R^+],\beta\rangle=\nu_{\rm cut}+B.
\]
Raw absolute convergence和compact-support integral给 boundary limit存在，不能把其值设0。因此
\[
 \nu_{\rm compact}-\nu_{\rm cut}
 =B_\sigma+(2\pi i)^4Q(\tau_\sigma a,\omega)
\]
对指定 rational trace成立；对 canonical \([\omega,0]\) 则保留 rational **relative** Tate period与相应flux。Root 独核 elliptic puncture 的 exact \(d(\chi/z)\) 反例：raw wedge在near-puncture为0、在annulus绝对收敛，却等 \(-2\pi i f(0)\)，而support trace为0。它正确说明逻辑缺口，不声称本例flux非零。

B20 的 inverseGram恢复必须是 \(-J^{-1}h\)；逐行符号与已冻结矩阵一致。B22 的真实目标四jet向量是
\[
 (2\pi i)^4\int_\Gamma E_j/8
 =-8i\pi^7\theta^j y_0,
\]
不是只求一个任意齐次常数。B18 的全部cone/current Jacobian bounds尚未完成，因此本审阅不接受fluxzero或完整 \(\Gamma/8\) marked equality。

## R4. 单初值 dual germ 的独立核查

对analytic \(f,g\)，代入 \(\theta=-(1-t)D\) 到concomitant得到
\[
 \mathcal C(f,g)(1)=f_0(2g_2-3g_1/2)-g_0(2f_2-3f_1/2).
\]
因此 \(S=\mathcal C(\Psi,g_2)\) 真实满足
\[
 S(1)=2\alpha_0,\qquad
 \theta S=\sqrt{x}g_2/16,\qquad
 S(1-t)=2\alpha_0-\frac1{16}\int_0^t\frac{g_2(u)}{\sqrt{1-u}}du.
\]
\(\alpha_1,\alpha_2\) 的消去是全函数身份；新的非恒定 germ 无条件有理。

令 \(K=(\theta-1/2)^4-x\theta^4\)、\(M=K\theta\)。展开 \(K\) 给
\((1-x)\theta^4-2\theta^3+3\theta^2/2-\theta/2+1/16\)，与五行connection一致。令 \(L=(\theta-1/2)P\)，formal adjoint和Kummer conjugation给
\[
 M=-\sqrt{x}L^*\sqrt{x}^{-1}.
\]
已证明的原extension非分裂及connected \(\mathrm{Sp}_4\)不可约性转到dual后，得
\(0\to1\to\operatorname{Sol}M\to\operatorname{Sol}K\to0\) 非分裂。实际 \(\theta S\ne0\)，orbit span surject到rank4quotient；rank4会提供splitting，所以最小阶严格为5。有限覆盖的非分裂可用有限Galoiscore后平均splitting证明；不会免费降低实际rank。

FR theorem 对 \(g_2\) 用 order4、conifold整数exponents，给 \(D_{n+b_0}^3C_g^{n+1}\)。根逐项核 convolution 的 \(4^{n-1-k}\) 与积分 \(n\) 分母，得到
\[
 16D_{n+b_0}^4(4C_g)^n[t^n]F\in\mathbf Z.
\]
至多三阶导数只读到 \(N+3\) 且factorialratio是整数；故全文的
\[
 \Delta_N=16d_0D_{N+b_0+3}^4(4C_g)^{N+4}
\]
覆盖五行完整prefix。额外1亦被此界整化，但它在实际计秩中不能删除。\((4C_g)^N\) 的 finite-place 指数费用确实保留，未给有效最小 \(C_g\) 或Smithoptimum。

Algebraic differential row消去任一nonzero homogeneous \(g_1\) 会因connected \(\mathrm{Sp}_4\) 杀掉整个 \(P\)层，包括 \(g_0\)。因此新的concomitant不是原模型的免费代数gauge。合法Tate shift \((2\pi i)^4PD\delta\) 对normalized scalar产生 \(+i\pi^3v/8\)，端点和 \(\delta\)-pairing不变，但一阶jet之差超越；与本轮实际消失球稿独立吻合。

最后，\(S=F+2\alpha_0\) 的branch differences及stabilizer对任意constant translation全不变，\(F\) 已有无条件 arithmetic model。故仅用该packet的导数、同一leaf和上述分母/rank数据不能识别目标常数；需要第二端点或真实Betti relation。本no-go限于这些明确输入，不是排除所有CDT方法。

## R5. 新增完整计秩证明：常数1确实给第六行

以下补充是本稿新证明。旧 arithmetic 稿 A5 保守提醒「包含1须另计」，这里把该秩精确算出。

在 \(\mathbf C(x)\) 上令
\[
 \mathcal D=\operatorname{span}(S,u,\theta u,\theta^2u,\theta^3u),
 \qquad u=\sqrt{x}g_2,
\]
\[
 \mathcal N=\operatorname{span}(u,\theta u,\theta^2u,\theta^3u).
\]
R4 的实际最小阶5及4分别给 \(\dim\mathcal D=5\)、\(\dim\mathcal N=4\)。\(\mathcal N\) 是irreducible differential submodule，\(\theta S=u/16\) 给
\[
 0\longrightarrow\mathcal N\longrightarrow\mathcal D
 \longrightarrow1\longrightarrow0.
 \tag{R5.1}
\]
Scalar operator \(M\) 的cyclic derivative module与 \(\operatorname{Sol}M\) local system互为dual；\(S\) 的annihilator实际最小为 \(M\)，所以该identification应用于本 \(\mathcal D\)，不是一个abstract未标记module。R4 的non-split solution sequence的dual正是 (R5.1)，故 (R5.1) 非分裂。

反设常数函数 \(1\in\mathcal D\)。它不可能在 \(\mathcal N\)，否则给irreducible rank4一个rank1trivial submodule。故其quotient像非零。\(\overline S\) 在quotient是horizontal basis；写
\(\overline1=b(x)\overline S\)，flatness给 \(\theta b=0\)，所以 \(b\in\mathbf C^*\)。实际horizontal section \(1/b\in\mathcal D\) 于是给 (R5.1) 的splitting，矛盾。得
\[
 \boxed{1\notin\mathcal D,\qquad
 1,S,u,\theta u,\theta^2u,\theta^3u
 \text{ 在 }\mathbf C(x)\text{ 上线性无关，完整秩恰六。}}
 \tag{R5.2}
\]
这对每个constant translate \(S=F+q\) 同样成立，因为其最小阶与non-split module不变；有限代数覆盖上也保留同一证明。

当 \(\alpha_0\in K\) 时，新增常数1由同一个 \(\Delta_N\) 整化，故六行有完整arithmetic prefix。它仍须用真实rank6记算术holonomy账本，不能把五阶scalarorder记成含1元组的rank5。本新增推导已交 arithmetic 作者独立核module/solution dual方向、非分裂与constantsection论证，确认通过；没有finite math verifier或peer producer执行。

## R6. 当前结构性进展与严格未完成事项

本轮新接口串起来的是：真实 \(\Xi\) 的positive open regulator class；actual rational open Tate discrepancy；全部compactH3的support lifts与指定trace；精确boundaryflux及四jet目标；实际消失球固定一个Tate归一化、剩余三维全纯差；单端点dual完整算术模型及含1实际rank6。

仍未证明actual相对boundary \(\partial A^{\rm rel}=0\)、fluxzero、剩余三periodcoefficients、compactintegrallattice/saturation、有效finitebadprime费用或endpoint-sensitive共同analyticcapacity。没有目标数的新无理性、线性无关性或Lean定理。Goal保持active，不能把这些结构接口记作原数值目标完成。

## R7. Root 实际来源阅读与执行边界

* KLM published [本地23页](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)：本轮 root 实际PDF8–10、12–13、17。Unitproduct、ring、\(p=n\) evaluation、open \(n=p>m\) directR均逐原件核；不冒认本轮全文阅读。
* Li2018 [本地12页](../literature/li2018_integral_regulators_higher_chow_published_20261006.pdf)：root本轮实际PDF8–10，sector identity、exteriorproducts及small-\(\epsilon\) theorem的scope；不扩大该theorem。
* Deligne HodgeIII [本地74页](../literature/deligne1974_hodge_III_primary_20261006.pdf)：root本轮实际PDF35–38，尤其8.2.7、8.2.8原始sequence。此前已视觉读过37；本轮另核整页文本。
* FR [本地12页](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)：root本轮实际PDF2–5、9，geometric无条件版本、\(\mu-1\)、localG basis与有限badprime费用。初次多项合并输出的2–3页被截断，后单独完整重抽取阅读；不把截断页计为已读。
* CDT, *Arithmetic holonomy bounds and effective Diophantine approximation*, fixed arXiv2510.04156v1，[归档20页](../literature/cdt2025_arithmetic_holonomy.pdf)，SHA256 `5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1`：root本轮实际PDF1–4，特别PDF3–4 §2.1、Theorem2.1 的完整 \(\mathbf Q(x)\)-independent元组与分母array。该归档封面copyright2026且arXivv1日期2025-10-05；不混同版本。原 [2024核心论文](https://arxiv.org/abs/2408.15403)本轮只web检索元数据，未冒认本轮重新全文核读。

PDF抽取与hash是只读来源/交付操作；本轮新增数学producer执行0，旧/peer执行或import0，无新PDF下载，无TLS绕过。数学结果由全文纸面推导和独立审阅支撑，文件audit仅查指纹/链接，不是数学或Lean证明。
