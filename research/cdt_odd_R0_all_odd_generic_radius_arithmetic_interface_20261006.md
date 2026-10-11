# Actual R0 全奇素数 generic radius 与显式九行整模型

日期：2026-10-06。NEW 全尺度纸面证明。旧/同行数学 MD/PY/JSON/manifest 全部只读，未执行、import 或重跑 producer。本稿连接本轮整数 toric 模型、actual compact Picard–Fuchs 和 rational convergent Gauss–Manin；不修改 root 已冻结 D14 的条件性历史范围。

## A1. 精确输入与新结论

令 \(t=1-x,\ w=1-t,\ \delta=t\,d/dt\)。actual 算子为
\[
 P=\theta_x^4-x(\theta_x+\tfrac12)^4,\qquad
 Pg_i=0,\quad Ph=\sqrt{1-t}/16,
\]
conifold Taylor 初值 \(g_0,g_1,g_2,h\) 分别为
\((c_0,c_1,c_2)=(1,0,0),(0,1,0),(0,0,1),(0,0,0)\)。

输入为：

1. 本轮 toric 新稿 S2–S8 的同一 fixed-fan scheme 在 \(\mathbf Z[1/2]\) 上 projective smooth，基底删除 \(x=0,1,\infty\)，全部奇素数及 boundary corners 已逐 stratum 证明。
2. 冻结 Yukawa Y7a–Y10 的真正 cohomological PF：原始 compact algebraic form \(\eta\) 在 \(H^3\) 中，\(\omega=\sqrt x\,\eta\) 的 cyclic span rank4，且 \(P\omega=0\)。这不是一个 period 数值的 scalar PF 猜测。
3. 冻结 root 有效分母 D1–D6 的 actual G4/G5 matrices、square-zero residues、整初值及全尺度 dyadic 界
\[
 2^{b(n)}c_n\in\mathbf Z_2,\qquad
 b(n)=2n+2v_2(n!)-\lfloor n/2\rfloor\le 7n/2.
 \tag{A1}
\]
4. 本稿实际核读的 Morrow rational crystalline/convergent comparison、Bhatt–de Jong crystalline/de Rham comparison 和 Fischler–Rivoal Theorem3。

下面证明 G4 和 G5 在每个奇素数的 Gauss generic point 上基本解矩阵均收敛于半径1开盘。因此对全部 \(n\ge0\)，g 的整数模型为
\[
 2^{b(n)}(D_n^{\rm odd})^3
 3^{2\lfloor\log_3 n\rfloor}c_n(g_i)\in\mathbf Z;
 \tag{A2}
\]
h 的独立模型为
\[
 2^{b(n)}(D_n^{\rm odd})^4
 3^{\lfloor\log_3 n\rfloor}5^{4\lfloor\log_5 n\rfloor}
 c_n(h)\in\mathbf Z.
 \tag{A3}
\]
这里 \(D_n=\operatorname{lcm}(1,\ldots,n)\)，\(D_0=1\)，n=0 的 logarithmic factors 按1处理。A2/A3 不再带未证明 generic-radius 条件；它们使用上述本轮完整模型证明，不从 characteristic-zero 几何推断好约化。

## A2. 为什么 rational crystalline 定理不需要 integral de Rham free

实际全文读 Morrow 十二页原件。Proposition2.1 给 proper smooth \(f:X_0\to S_0\)、smooth varieties over perfect \(k\) 的
\[
 R^i f_{\rm crys*}\mathcal O_{X_0/W}\otimes\mathbf Q_p
\]
为 isocrystal；Proposition3.2 给 rational base change 与 Frobenius isomorphism；Corollary6.2 识别它为 Ogus convergent F-isocrystal。该结论没有要求 integral \(H^i_{\rm dR}\) locally free 或 crystalline torsion-free，也没有 \(p>i\) 条件。

Morrow 的论证实际处理 Tor：PDF4–5 先证明 rational module projective，再由有限 resolution/clearing p denominators 使所有 base-change obstruction 被一个 p 幂杀掉。不能倒过来将这个 rational 结论当作 integral cohomology free。我们只需要 rational differential equation 的收敛性，故 p3 的可能 torsion 不构成该定理的额外假设。

Katz PDF23 的简化几何 F-crystal 版本明确要求 de Rham locally free；本稿使用更一般的 rational 定理补该接口，并不删改 Katz 假设。Katz 后段 \(p>i\) 是 Mazur divisibility 的附加条件，也不约束 Morrow 的 rational Frobenius。

## A3. relative lift 的 comparison 与 actual Gauss–Manin

为避免将 absolute \(\Omega^\bullet_{X/W}\) 误作 relative \(\Omega^\bullet_{X/A}\)，说明比较的具体相对形式。

取 smooth affine base 的 p-adically completed smooth lift \(A/W(k)\)，并将实际 proper smooth family 完成在该 base 上，记 \(\widehat X/A\)。其 special fibre 为 \(X_0/S_0\)。在每个 relative smooth affine chart，晶体计算用 relative smooth polynomial/étale A-algebra 的 p-adic PD hull；理想 \((p)\) 已有 compatible canonical divided powers，故该 hull 正是 smooth lift 的 p-adic completion。PD de Rham resolution 在这里使用 \(\Omega^\bullet_{\widehat X/A}\)，而非 absolute differentials。

Bhatt–de Jong 原件 PDF2–9 的 Lemmas2.4,2.13–2.17、Theorem2.12/3.6 和 Corollary3.8 实际证明 affine PD-hull calculation、functorial Čech descent 和 proper formal-functions algebraization，且不假设各 \(H^i\) free。其纸面 theorem 用 \(\Sigma=\operatorname{Spec}\mathbf Z_p\) 表述；本处相对 A 版本须自证，不能把印刷 Cor3.8直接称为相对 theorem。

具体相对 lemma 的证明如下。对 \(\widehat X\) 中一个 smooth affine lift \(B\)，取相对 polynomial/étale chart，构造
\[
 D(q)=\widehat{\operatorname{PD}}\,
 \left(B^{\widehat\otimes_A(q+1)}
       \longrightarrow B/pB\right)\quad(q\ge0),
\]
所有 tensor 和 forms均相对于 A。q=0 的 PD ideal为(p)，已具有 canonical divided powers，故 \(D(0)=B\)。q>0 的 diagonal differences给 p-adically completed PD polynomial variables；对 étale chart由 unique étale lifting得到同样描述。

这些 lift对象在相对 crystalline topos 中的 filtered union 是 effective epimorphism，因为 smooth B的 infinitesimal lifting property局部提升任意 PD thickening。其 q次自交正是D(q)。准凝聚 structure crystal 的 mod p^e transition maps surjective，故 \(R^1\lim\) 为0，Čech–Alexander complex \(D(\bullet)\) 算 crystalline cohomology；这就是BdJ Lemma2.4的相对A版本，证明只用 topos descent与surjective transitions。

考虑双复形
\[
 C^{q,j}=\Omega^j_{D(q)/A}.
\]
各列的 relative PD Poincaré lemma直接成立：一个 PD variable z的 forms有 \(d z^{[n+1]}=z^{[n]}dz\)，正次数 contracting homotopy将 \(z^{[n]}dz\) 送到 \(z^{[n+1]}\)，没有除n；有限多个 variables取tensor并p-adic完成。这使每列与 \(\Omega^\bullet_{B/A}\) quasi-isomorphic。

各正次数行 homotopic zero也只需基环无关的combinatorics。对 relative polynomial \(B=A[T_1,\ldots,T_r]\)，第q项 \(\Omega^1\) 的生成元是各slot的 \(dT_i(e)\)，cosimplicial map将它送到 \(dT_i(f(e))\)。BdJ Example2.16的 homotopy把第e生成元在 \([q]\to[1]\) 的cut j前保留、cut后送0；两端evaluation分别0与identity，故给显式contracting homotopy。Exterior powers、tensor coefficient crystal与p-adic completion保留这一cosimplicial homotopy（它是module maps的有限逐项formula）。对étale chart，relative cotangent bundle从polynomial chartbase change，故homotopy继承；Zariski descent处理一般smooth B。由双复形的两谱序列，\(\Omega^\bullet_{B/A}\)与relative crystalline complex quasi-isomorphic。

最后用相容的有限affine Čech覆盖 glue到proper \(\widehat X\)。proper formal-functions将此p-adically completed hypercohomology与actual proper algebraic lift的completed de Rham complex识别。因此有 functorial derived identity
\[
 R\Gamma_{\rm crys}(X_0/A)\simeq
 R\Gamma(\widehat X,\Omega^\bullet_{\widehat X/A}).
 \tag{A4}
\]
取 \(H^3\) 后再 invert p 可与 Morrow Proposition6.1 的 coherent rational realization 比较；没有声称先取 cohomology 再 arbitrary integral base change 总无 Tor。

连接也被确定：取base第一PD对角包 \(A(1)\)，两 projection p1,p2 的 crystalline base change给 \(\epsilon:p_1^*H^3\to p_2^*H^3\)。其 \(\epsilon(h\otimes1)-1\otimes h\bmod I^{[2]}\) 位于 \(H^3\otimes_A I/I^{[2]}\)，且 \(I/I^{[2]}=\Omega^1_{A/W}\)。A4 的逐chart functorial comparison与两 projection相容；在同一个Čech/de Rham代表上该差就是lift沿base变化的first differential。把 \(\Omega^\bullet_{X/W}\) 按base differentialdegree过滤的transitivity sequence取connecting map，得到完全相同的formula，这正是relative de Rham Gauss–Manin。晶体cocycle保证它integrable。故本例真正 \(H^3_{\rm dR}(\widehat X/A)[1/p]\) 是 rational convergent F-isocrystal 的实现，不是仅具有同样秩的另一个 equation。

在 generic fibre，proper coherent comparison 将这个完成后相对 de Rham 模块与 actual algebraic GM 完成相同。所需基底本身 smooth over \(\mathbf Z_p\)，原 toric模型 projective smooth，因此上述比较 hypotheses 对每个 odd p成立。

## A4. Gauss generic disk、actual P 和有理 gauge

固定任意奇素数 p。取 perfect residue field k 包含一个在 \(\mathbf F_p\) 上超越的元素 \(\bar\xi\)，并在相应 Gauss valued extension 中取单位 lift \(\xi\)。此时
\[
 t=\xi+s,\qquad |s|_p<1,\qquad
 |\xi|_p=|1-\xi|_p=1.
 \tag{A5}
\]
它是 smooth base 的 generic residue disk；本稿并未将退化中心 t=0 当作 smooth point。

Convergent isocrystal 的 diagonal Taylor comparison 在所有这样的开盘收敛；限制到该 disk 并固定中心 fibre 的 basis，便得到 ambient \(H^3\) 的水平基本解，半径至少1。它的 dual、horizontal submodules 与 quotients 同样收敛：horizontal trivialization 把这些子空间识别成中心 fibre 的固定向量子空间，再限制或取商即可。这里不要求 submodule 自身先拥有 integral Frobenius lattice。

actual \(\eta\) 属于原 compact \(H^3_{\rm dR}\)。\(\omega=\sqrt x\,\eta\) 的 square-root cover 在 odd p 下 finite étale，因为 x 在基底上为单位且 \(2\sqrt x\) 是单位。A5 盘上的 square root 可唯一选 lift，二项展开属于 \(\mathbf Z_p[[s/(1-\xi)]]\)，半径1。这就是真正 Kummer twist，不是免费除 Tate period。

冻结 Y8a–Y10 在 characteristic zero 的 cohomological \(P\omega=0\) 和 cyclic rank4 是 Q 上的代数对应身份。张量 \(\mathbf Q_p\) 后仍成立；本稿不需要相关 mirror correspondence 自身拥有 mod p degree-one good reduction，ambient 是 S模型的 actual X。由 \(\omega,\nabla_\theta\omega,\nabla_\theta^2\omega,\nabla_\theta^3\omega\) 的 cyclic sector得到 actual rank4 differential module；period scalar 解属于它的 dual，因而继承上述 generic convergence。

G4 是 P 的同一个 exact rational derivative basis，并非 abstract representation 的维数推测。任意比较 gauge 的每个非零 rational denominator 经除去固定 p 幂后，reduction为非零 polynomial；\(\bar\xi\) 超越使它及 determinant 在 A5 盘上无零。故 gauge 与 inverse 都 analytic 半径1，不改变 solvability radius。fixed p-denominators 影响 lattice norm，但不影响这个 convergence 结论。

因此 actual G4 满足 FR Theorem3 第(iv)条，对每个 odd p都成立。其(i)–(iii)条由 exact G4 rational matrix 全部在 \(\mathbf Z[1/2]\) 且唯一有限非零 pole t=1、G4(0)²=0 给出。未使用 \(p=2\) 的 étale square-root 或 good reduction。

## A5. G5 的 source 不需 higher-Chow integral Frobenius

root exact expansion 为
\[
 \delta y=G_4(t)y+\frac{u}{16}(0,0,t,t^2)^T,\qquad
 u=(1-t)^{-7/2},\qquad
 \delta u=\frac{7t}{2(1-t)}u.
 \tag{A6}
\]
这定义 actual G5 homogeneous extension。源列在 t=0 消失，G5(0)²=0；所有 coefficients 在 \(\mathbf Z[1/2]\)，唯一有限非零 pole为1。

在 A5 generic disk，令 Y4 为中心 normalized 的 G4 基本解。由 exact matrix
\[
 \operatorname{tr}(G_4/t)=6/(1-t)
\]
得到
\[
 \det Y_4(\xi+s)=
 \left(\frac{1-\xi}{1-\xi-s}\right)^6,
 \tag{A7}
\]
盘内无零，故 adjugate formula 给 \(Y_4^{-1}\) 同样收敛半径1。

源的 normalized fundamental factor
\[
 U_1(s)=\left(1-\frac{s}{1-\xi}\right)^{-7/2}
\]
在每个 odd p系数 p-integral、半径1。变参数公式的上右块为
\[
 Y_4(s)\int_0^s Y_4(z)^{-1}
 \frac1{16}(0,0,1,\xi+z)^T\,U_1(z)\,dz.
 \tag{A8}
\]
被积函数收敛半径1。积分将第n项除以 \(n+1\)，其 p-adic valuation 至多 \(O(\log n)\)，不改变半径。因此 A8 与 Y4、U1 组成 G5 半径1的 normalized invertible fundamental matrix。

这证明 source h 的 FR 第(iv)条；它并未将 regulator normal function 宣称为 integral crystalline higher-Chow object。也没有对 inhomogeneous h 直接套 μ4 定理。

## A6. FR μ4/μ5 的所有小奇素数费用

实际读 published FR PDF6–8 Theorem3，公式为
\[
 v_p(\operatorname{den} U_n)\le
 \bigl(\mu-1+v_p((\mu-1)!)+\beta_\mu\bigr)
 \lfloor\log_p n\rfloor,\quad
 \beta_\mu=\min\{\mu-1,v_p\prod_{j=1}^\mu{\mu\choose j}\}.
 \tag{A9}
\]
μ4 的 product为96；故 p≥5 exponent3，p3 exponent
 \(3+1+1=5\)。g0/g1/g2 的 actual G4 初值为
\((1,0,0,0),(0,1,0,0),(0,0,2,0)\)，在 residue kernel 且 integral，所以是 Levelt holomorphic factor U(t) 乘这个初值。由 A9 得全odd A2。

μ5 的 product为2500，故 p≥7 exponent4，p3 exponent
\(4+1+0=5\)，p5 exponent \(4+0+4=8\)。h 的 G5 初值 \((0,0,0,0,1)\) 也在 residue kernel且 integral。结合 dyadic A1得 A3。3和5的 extra factors 都是 polynomial in n，不是新的 exponential bad-prime C。

这些边界不要求任何 shearing 初值分母，使用的是已固定 exact G4/G5，而非 FR 的“所有足够大 primes”存在性替代。

## A7. 实際九行、C16 和完整 prefix

用冻结 exterior 的 paired coordinates：
\[
 Z_j=F_1\theta_x^jg_2-F_2\theta_x^jg_1
       -2q\,\theta_x^j(g_1+\tfrac34g_2),\quad 0\le j\le3,
\]
\[
 F_i(t)=-\frac1{16}\int_0^t \frac{g_i(u)}{\sqrt{1-u}}\,du,
 \tag{A10}
\]
及五个 independent mixed \(\sqrt{1-t}\,(g_1\wedge g_2)\) jet coordinates。其 actual rank9/with1 rank10 已在冻结 exterior 全尺度证明。本节不更换目标或 rank。

g 的 odd LCM三次，积分 F 多一次，所以 four Z odd LCM七次，mixed odd LCM六次。每个乘积有两个 g factors的 p3 extra，故统一留
\[
 P_3(N)=3^{4\lfloor\log_3(N+6)\rfloor}.
 \tag{A11}
\]
固定最多三阶 derivatives 的 coefficients 是 integer polynomial combinations 及 index shift，mixed 总移位至多6。

dyadic b(n) 对乘积的卷积 superadditive，根稿已经给同尺度四Z/五mixed 界 \(2^{b(N+6)+O(1)}\)。可直接核：
\[
 b(a+b)-b(a)-b(b)=2v_2{a+b\choose a}
 -\{\lfloor(a+b)/2\rfloor-\lfloor a/2\rfloor-\lfloor b/2\rfloor\}\ge0.
\]
当花括号1时 a,b均odd且 binomial even；其余case显然。平方根系数费用 \(2^{2n}\le2^{b(n)}\)，积分16和除n由 b递增吸收，加一个固定 \(2^4\)足够。因此可保守使用 fixed \(B=25\)，因为
\[
 b(n+6)+4\le 7n/2+25\le4n+25.
\]

对 \(q\in K\)，选 fixed positive integer \(d_0\) 使 \(d_0q\in\mathcal O_K\)。所有 N≥0 的完整前缀都有
\[
 \boxed{2^{25}d_0\,16^N\,P_3(N)D_{N+6}^{\,7}
          [t^n]Z_j(q)\in\mathcal O_K\quad(0\le n\le N),}
 \tag{A12}
\]
\[
 \boxed{2^{25}d_0\,16^N\,P_3(N)D_{N+6}^{\,6}
          [t^n]M_i\in\mathcal O_K\quad(0\le n\le N).}
 \tag{A13}
\]
原 canonical mixed columns的固定 source1/16、g2初值2与 contraction factors 都由固定2幂覆盖。这个有理 C16 模型涵盖全部 places；它保留 P3 和 finite shifts，没有把 p3 polynomial cost删除。

本 paired 模型本身不需要 h 的 μ5 分母界：A10 已精确消去不需要的 source jets。A3是另外完成的实际正结论，不以把 h 当 g 来取得九行收益。

## A8. P3 对 CDT 主项的严格费用

strict coefficients A12/A13 比纯 LCMspecies多 P3。不能直接冒称它们无修改满足 CDT2025 Theorem2.1 的精确纯LCM定义。

但原 CDT slopes proof允许显式核有限-place lattice perturbation。对 degree D auxiliary空间，rank \(r_D=10(D+1)\)、Taylor截断 N=O(D)；\(\log P_3(N)=O(\log D)\)。将每个 coefficient lattice乘此 common integer使实际 arithmetic constraints integral，两 lattice的 index绝对值至多 \(P_3(N)^{O(r_D)}\)，故 normalized Arakelov degree的变化为 \(O(D\log D)\)。同样每个 relevant graded local height只多 \(O(\log D)\)，共有 O(D)项，所以总和也是 \(O(D\log D)=o(D^2)\)。这些 statements在 K 下用 normalized local weights同样成立，固定 \(d_0,2^{25}\) 只贡献 O(D)。

还可给 literal Theorem2.1 的独立转换，避免只凭主项语言删掉实际分母。取任意 \(0<\varepsilon\le1\)。对每个 n≥0，
\[
 3^{4\lfloor\log_3(n+6)\rfloor}
 \mid 3^{4\lceil\log_3(14/\varepsilon)\rceil}
       D_{\lfloor\varepsilon n\rfloor}^{\,4}.
 \tag{A14a}
\]
若 n≥2/ε，\(\lfloor\varepsilon n\rfloor\ge\varepsilon n/2\) 且 n+6≤7n，因此 floorlog差至多 \(\lceil\log_3(14/\varepsilon)\rceil\)；n<2/ε则n+6≤8/ε，同一fixed3幂直接覆盖。D0按1。式A14a是真正的整数整除，不把P3当作被n⁴整除。

fixed index shift n+6也可付清：n≥6/ε时 \(D_{n+6}\mid D_{\lfloor(1+\varepsilon)n\rfloor}\)，其余有限n由fixed \(D_{\lceil6/\varepsilon\rceil+6}\) 覆盖。故对每个ε存在显式fixed \(d_\varepsilon\)（可以取上述fixed3幂乘 \(D_{\lceil6/\varepsilon\rceil+6}^{\,7}\)），使 actual coefficients of \(2^{25}d_0d_\varepsilon f_i(16s)\) 满足 literal species：六列 nonconstant cutoff1 的 b=1+ε，一列 pure cutoff6 的 b=1+ε，加四列 nonconstant cutoff1 的 b=ε。其
\[
 \tau_\varepsilon=(1+\varepsilon)\frac{329}{50}
       +4\varepsilon(1-1/100)\longrightarrow329/50.
 \tag{A14b}
\]
固定 \(d_\varepsilon\) 不贡献D²。对 rational parameter可以逐ε直接用 CDT2025 Theorem2.1；all-place K slopes版本也保留全部embeddings。若下面 L>329/50，先选ε使L>τε，取得界后令ε趋0。这与前述explicit lattice perturbation给同一极限，而且每个ε的arithmetichypotheses是原定理的literal format。

所以 D² 主项仍是先前十行的
\[
 (\sigma_i)=(0,6,6,6,6,6,7,7,7,7),\qquad
 \tau=329/50,
 \tag{A14}
\]
而 rational scale C16 的费用是 \(\log16\)。对全部embeddings实际 meromorphic pullbacks及合适 boundary regularity的映射 \(\phi_\sigma\)，记
\[
 A=\sum_\sigma w_\sigma I(\phi_\sigma)-\log16,\quad
 L=\sum_\sigma w_\sigma\log|\phi_\sigma'(0)|-\log16.
\]
当 \(L>329/50\)，原 slopes inequalities加上述 o(D²) comparison给
\[
 \boxed{10(L-329/50)\le A.}
 \tag{A15}
\]
所有 K embeddings 与有限 places仍为必要条件；本稿没有以单一 complex embedding 判 α超越。

这确实将未知 bad-prime C替换为 complete explicit C16 + polynomial factor，然而同一个 q=0 actual rank10 rational reference也满足同一模型。若 analytic map/domain 对 q共同，A15在 q=0已强制，故费用优化仍不能产生对 actual q 的反证。最高log旗标不能填平 canonical origin，有限cover no-go仍成立；新的数值结果尚需 genuinely value-sensitive meromorphic domain或另一个完整packet。

## A9. 来源、指纹与执行记录

本轮实际全文读 toric NEW S稿、Morrow12页；实际讀 Bhatt–de Jong PDF1–9（先1,7–9后补2–6，PDF10 references未计作本轮读）、Katz PDF3–6,9–12,23–24、FR published PDF6–8。冻结 Yukawa Y7a–Y10/Y27 与 root exact G4/G5 初值实际回读；root D1–D11 full dyadic proof由 quarter独审，本人不冒记又完整独审。

- Morrow，author PDF：literature/morrow_higher_direct_images_crystalline_author_20261006.pdf，12页，SHA256 9d7bb24587a99edbdfa707c62c2590d0e469e931c937cb99fbe3f14af2f0c009。首次 curl失败因 Windows revocationservice offline，未绕过TLS；随后 Python urllib默认证书验证同URL正常成功。
- Bhatt–de Jong，author PDF：literature/bhatt_dejong2011_crystalline_derham_author_20261006.pdf，10页，SHA256 6c66ed20334f5ce8d96c9af9c0523d69c9f50f776b8b5169300b461f0558e669；正常默认TLS。
- Fischler–Rivoal published：12页，SHA256 c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68。
- Katz，35页，SHA256 b885d13a652d87763c5864eb22238f0695613a3dab774507e2ba570a487eca1a。

完整新source receipt另存NEW manifest。新数学producer执行数0，旧/同行数学producer执行/import/rerun数0。归档/fitz读取/公式页渲染属于source处理，不验证数学identity。

结论为A2/A3的all-n全部奇素数模型、A12/A13 complete explicit九行前缀和A15定量holonomy费用。目标 \(q=\alpha_0=\pi^2(R_0-M_0)/16\) 的代数性与 \(R_0-M_0\) 有理/代数不等价；没有新特殊值无理性、线性无关性或Lean结论。
