# R₀ 全奇素数模型、真实 PF 收敛与 C16 前缀：独立全文审阅

日期：2026-10-06。NEW 纸面独审。全部旧/同行数学 MD、PY、JSON、manifest 只读；没有执行、import 或重跑数学 producer。本稿与此前自身 orbit verifier 首次执行记录分开，本独审的数学 producer 数为0。

实际全文读 [fixed-fan smooth model](cdt_odd_R0_toric_odd_prime_smooth_model_20261006.md)，冻结 SHA
`bde766ee2c7825c9b7a3de7bb77ee4a2b42983a51ab2fc8f6bd28c9cb16e323d`；实际全文读 [all-odd arithmetic interface](cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.md)，最终冻结 SHA
`439a21b2bdf35eeffcbf46e016b35e6ad3b11b635baa8e4148d6533741f6dc5a`。
先读45b3候选；作者补强A3 relative PD双复形与A14a/b literal ε转换后，已再次实际全文回读上述439a最终候选。没有修改任何冻结输入。

**独审结论：S2–S8 的全奇素数几何、A2–A6 的 rational GM 与 actual G4/G5 generic radius、A7 的完整 C16 前缀及 A8 的有限素数多项式扰动均通过。** 全奇素数的第四条件由这两份 NEW 证明闭合；旧冻结 D14 的历史条件性表述不改写。没有获得新的特殊值无理性，也没有把本例整数 de Rham cohomology 宣称为无挠。

## I1. Fixed fan 的整数构造，而非从复光滑推好约化

本独审回读冻结 toric 稿 §§2–8 的数学内容，及其最后来源段；源参数为
\[
 \phi=\prod_{j=0}^3(1+v_j)^2/v_j,\qquad
 R=\mathbf Z[1/2],\qquad
 S=\operatorname{Spec}R[\lambda,\lambda^{-1},(\lambda-256)^{-1}].
\]
每个 grid normal parameter 在完整 stratum 邻域上是同一个全局坐标。局部公式 \(\phi=c\prod z_i^{e_i}\) 中 \(e_i=-1,2\)，且 c 是整数 chart 上的单位。既存 regular coherent fan 保持原整数 lattice；其 chart 是
\[
 \operatorname{Spec}R[\tau^\vee\cap M],
\]
与自由 coordinate stratum 的乘积。regular cone 的 rays 可补成原 lattice 整数基底，所以其 chart smooth over R，并非只在 \(\mathbf Q\) 上 nonsingular。face localization 和原 global normal parameters 给 glue；不存在依赖某个 residue characteristic 的新扇形。

coherence 给 projective monomial modification；每个 cone contained in 一个 \(\ell\) half-space，故 \(\phi\) 或 \(\phi^{-1}\) 在整个 chart 上 regular，得到无 indeterminacy 的 f。proper source 的 closed graph 给 f projective。这一段不假定 normalization 随任意 base change 可交换，而是直接在 R 上使用同一 monoid schemes。

## I2. 所有边界角点的 primitive character 和 relative SNC

surviving 非零 cone 满足 \(\ell|_\tau=0\)。minimum original support 的全部 normal coordinates 都正，迫其同时含一个 pole coefficient −1 和一个 zero coefficient +2；故 \(2\le s\le4\)、\(1\le r\le s-1\le3\)。regularity 给 \(N_\tau\) saturated。

original 某个 coordinate vector 的 \(\ell\) value 是 −1，其在 \(N/N_\tau\) 上仍是 −1。因此 quotient character primitive，能用 determinant ±1 的整数 torus basis 把 f 化成最后一项 projection：
\[
 D_{A,\tau}^{\circ}
 \simeq U_R^{4-s}\times\mathbf G_m^{s-r-1}\times\mathbf G_{m,\lambda}.
\]
minimum support 使所有原 z_i 在这整个 orbit 为0，所以删去的 z_i=±1 没有删 orbit 点；这里确是全局产品，不是忽略了 étale torus twisting 的局部 statement。

在全部 residue fields，最后 torus coordinate q 的 derivative 是单位 c_A。该 orbit tangent 上的 Jacobian minor 已为单位，故 full ambient tangent 的 df 也满射；结合 r 个 normal coordinates，可取保留它们的 relative étale chart。因此 f smooth，r 个 boundary components 形成 relative SNC。r2/r3 corners 都由同一 proof 覆盖；不存在需额外逐点试验的 arithmetic component。

## I3. Odd-characteristic interior 与几何连通

在 interior，精确整数公式
\[
 \partial_{v_j}\log\phi=(v_j-1)/(v_j(1+v_j))
\]
分母都是单位。在每个奇特征，全部 derivatives 同时为0当且仅当所有 v_j=1，值为256；这是已从 S 删除的点。256 对所有奇素数均为单位。于是与 I2 合起来，\(\mathcal X/S\) everywhere projective smooth，relative dimension3。

S7 的 connectedness 也实际手核：固定前三个坐标，第四个满足
\[
 v_3^2+(2-A)v_3+1=0,
 \qquad A=\lambda/\Phi,
 \qquad \operatorname{disc}=\lambda(\lambda-4\Phi)/\Phi^2.
\]
代入0和−1说明两个被删 coordinate divisors 已自动避开。代数闭域无限，可选自由值令某个 \(\lambda-4\Phi=0\) 点的 v_0≠1；该点 derivative 非零，所以其某 irreducible divisor 的 order为1。discriminant 不是 square；char≠2 的 monic quadratic 不可约，整个 interior fibre integral。proper smooth fibre 的任一三维 component 不能全部落在有限个 dimension≤2 的 boundary strata 中，所以都遇到这个 irreducible interior，迫只有一个 component。这不是把 complex connectedness 免费传到 mod p。

S9 保留整数 de Rham locally-free 的缺口是准确的历史范围；新 A 稿通过 rational crystalline route 绕开它，不改 S9。

## I4. Primary rational crystalline 结论及 relative de Rham comparison

本独审实际全文读 Morrow 12页、Bhatt–de Jong 10页，而非只读 search abstract。Morrow Proposition2.1 给 proper smooth smooth-varieties higher direct image after tensor \(\mathbf Q_p\) 为 isocrystal，Proposition3.2 给 rational base change/Frobenius，Proposition6.1 给各 formal enlargement 的 crystalline realization，Corollary6.2 识别为 convergent F-isocrystal。

Morrow PDF4–5 的 finite projective after inverting p、有限 resolution 和 clearing p denominators 处理了 Tor。这里既无 p>i 条件，也不要求实际 integer cohomology torsion-free。不能反过来将其结论登记成 integral local-freeness。

Bhatt–de Jong 的 primary Theorem3.6/Corollary3.8 写的是 \(\Sigma=\operatorname{Spec}\mathbf Z_p\) 版本。A3 明确把相对 A 版本作为同一 proof 的推导，而非冒称原定理的文字已给本例。该推导成立：relative smooth polynomial/étale A-algebras 上的 PD Poincaré calculation 只用 relative variables；其 PD ideal 是已有 canonical divided powers 的 (p)。各 Čech intersections 上用 \(\Omega^\bullet_{\widehat X/A}\)，proper formal functions 沿 p-adic ideal 给完成后的 derived hypercohomology。最终补强稿还具体构造 \(D(q)\) 和双复形：PD variable 的 \(d z^{[n+1]}=z^{[n]}dz\) 给无需除n的 column contraction；各slot相对differentials用BdJ Example2.16的cosimplicial cut homotopy处理正次数row。étale chart及p-adic completion与这些finite slot formulas相容，两个谱序列确给同一个relative complex。故
\[
 R\Gamma_{\rm crys}(X_0/A)
 \simeq R\Gamma(\widehat X,\Omega^\bullet_{\widehat X/A}).
\]
不把 \(\Omega^\bullet_{X/W}\) 换成 relative complex，也不无条件交换 integral cohomology 与 arbitrary base change。

该比较 functorial 于 base diagonal 两次 pullback；最终稿明记 \(I/I^{[2]}=\Omega^1_{A/W}\)，其 HPD first-order difference 与 de Rham base-differential filtration 的 connecting map相同，即实际 Gauss–Manin。反演 p 后才取 rational realization；formal completion 与 actual algebraic GM 相容。S2–S8 的 proper smooth lift 在每个 odd p 均满足这里的 hypotheses。

## I5. Ambient convergence 真正传到 actual P/G4

回读实际 mirror/residue 稿全文及冻结 Yukawa Y1–Y10，另实际读 BK primary PDF6–7、16–17、19：该 family 是真实 compact quotient 的 resolution，PF参数是 q=1/x，canonical form 与 \(\omega=\sqrt x\eta\) 的 gauge由真实 dense-open 留数给出。Y8a 的共同 degree-one resolution 证明 cohomological \(P\omega=0\)，不是只由一条 Γ scalar period 推断。

这个 characteristic-zero algebraic identity 张量 \(\mathbf Q_p\) 仍是 actual X 的 identity。无需 mirror graph 本身在每个 odd p 好约化，也无需 integer Π 在晶体模型中实现。cyclic rank4 的非零 determinant 在 characteristic zero base extension 下不变。

在 Gauss generic disk \(t=\xi+s\)、\(|s|_p<1\)，residue \(\bar\xi\) 超越，故 t、1−t 为单位。convergent Taylor comparison 给 ambient rational horizontal fundamental matrix。dual、connection-stable submodule 和 quotient 可限制该 horizontal trivialization；没有要求它们先拥有 integer Frobenius stable lattice。

square-root cover 在 odd p 有 invertible Jacobian \(2\sqrt x\)。generic disk 的 binomial square root 属于 \(\mathbf Z_p[[s/(1-\xi)]]\)，故该 disk 的单值 lift有radius1。其上 actual cyclic span 与 dual scalar period system 的 P 相同。

companion basis、root G4 derivative basis 的比较是 rational gauge。任何非零 denominator 或 determinant 去掉固定 p 幂后 reduction 是非零 polynomial，超越 residue 避开它的所有零；gauge 和 inverse 在整开盘 analytic。固定 p-denominator 影响 norm，不改变 convergence radius。于是 G4 的 FR 第(iv)条对所有 odd p成立。它的其余三条来自 root 已冻 exact rational G4 和 square-zero residue，未假定 p2。

## I6. G5 正结论：源积分不冒用 μ4

root 的 actual source system为
\[
 \delta y=G_4y+\frac u{16}(0,0,t,t^2)^T,
 \qquad \delta u=\frac{7t}{2(1-t)}u.
\]
source initial vector在 G5(0) kernel，G5(0)²=0。

手核 exact trace为 \(\operatorname{tr}(G_4/t)=6/(1-t)\)。因此 normalized generic fundamental matrix满足
\[
 \det Y_4(\xi+s)=((1-\xi)/(1-\xi-s))^6,
\]
无零；adjugate 给 inverse 也radius1。rank-one源的normalized factor是 \((1-s/(1-\xi))^{-7/2}\)，在odd p系数integral。上右块准确是
\[
 Y_4(s)\int_0^s Y_4(z)^{-1}
  \frac1{16}(0,0,1,\xi+z)^T
  (1-z/(1-\xi))^{-7/2}dz.
\]
integration 除 n+1 只增 \(O(\log n)\) valuation，保留radius1。这是 G5 的 explicit proof，不假定 higher-Chow class 的 integral Frobenius，不把 h 当 homogeneous g。

FR μ4 product96给odd exponents3及p3 exponent5；μ5 product2500给通常4、p3 exponent5、p5 exponent8。整初值均在 residue kernel，所以使用的是 normalized holomorphic Levelt factor U(t)c，不需 shearing/Laurent denominator。A2 的 extra \(3^{2\lfloor\log_3n\rfloor}\) 和 A3 的 extra \(3^{\lfloor\log_3n\rfloor}5^{4\lfloor\log_5n\rfloor}\) 全部正确，n0按1。

## I7. Paired 九行及 strict C16 前缀

本轮实际补读冻结 exterior E1–E3、E7/E7a、E10 的完整目标和 contraction identity。它的 four pure rows准确是
\[
 Z_j=F_1\theta^jg_2-F_2\theta^jg_1
       -2q\theta^j(g_1+\tfrac34g_2),
 \qquad F_i=-\frac1{16}\int_0^t g_i(u)/\sqrt{1-u}\,du.
\]
five mixed rows是 \(\sqrt{1-t}\) 乘两个 homogeneous jets 的保留 minors。没有换目标；rank9/含1 rank10 使用已冻实际 orbit theorem。

g 的 odd D三、F 的odd D四，故 Z 是 D七；mixed 是D六。每个乘积两个g因子的extra p3最多
\(P_3(N)=3^{4\lfloor\log_3(N+6)\rfloor}\)。paired公式不需要 h 的μ5界，故无需把A3的p5extra带到这份packet中。

dyadic function \(b(n)=2n+2v_2(n!)-\lfloor n/2\rfloor\) 非减且superadditive：floor difference非零只在a,b都odd，此时binomial even，仍有 \(b(a+b)\ge b(a)+b(b)\)。F 至多付固定3次二进制幂，q项固定1次，最多两组三阶jets总index shift≤6；square-root三项卷积也用同一superadditivity。因此 root safe \(b(N+6)+4\) 可用，且
\[
 b(N+6)+4\le \tfrac72N+25\le4N+25.
\]
取 fixed d0 使 d0q在 \(\mathcal O_K\) 中，则所有 \(0\le n\le N\) 同时由
\[
 2^{25}d_0\,16^N P_3(N)D_{N+6}^{7}
 \quad\hbox{或}\quad
 2^{25}d_0\,16^N P_3(N)D_{N+6}^{6}
\]
整化 Z/mixed。D是full LCM，额外包含的2-powers无害。固定 contraction、1/16、3/4 与g2初值因子由上述常数覆盖；没有把两个 prefix 费用错误乘成16^{2N}。这是全部places的strict前缀，保留finite shifts、P3和所有K embeddings。

## I8. Polynomial factor 的 slopes 费用，不能删除它的精确存在

本独审实际读 CDT archived primary PDF3–8，尤其PDF7的
\(\#V_D=m(D+1)\)、\(V_D\subset\{0,\ldots,(m+\epsilon)D\}\)，及PDF6–8的filtered evaluation/degree/main-term proof。

对 m10、Taylor截断 N=O(D)，P3(N)的log为O(logD)。把auxiliary integral lattice统一乘 P3(N) 改变normalized degree至多 \(10(D+1)\log P3(N)=O(D\log D)\)；每个 graded evaluation height增加O(logD)，只有O(D)个非零grade，仍是O(DlogD)。固定 shifts 可同样付多项式factor；d0和固定2幂是O(D)。因而这个NEW perturbation proof足够，且是o(D²)；并未声称P3不存在或直接满足Theorem2.1的纯LCM精确定义。

最终A14a/b的第二条literal route亦独核：任意 \(0<\varepsilon\le1\)，n≥2/ε时 \(\lfloor\varepsilon n\rfloor\ge\varepsilon n/2\)、n+6≤7n，故两个3-adic floorlogs差不超过 \(\lceil\log_3(14/\varepsilon)\rceil\)。smalln时n+6≤8/ε由同一固定3幂覆盖。因此真正整除
\[
 P_3(n)\mid3^{4\lceil\log_3(14/\varepsilon)\rceil}
 D_{\lfloor\varepsilon n\rfloor}^{4}
\]
成立，并未把P3当作必整除n⁴。n≥6/ε时n+6≤floor((1+ε)n)，其余有限n用固定LCM补足。于是对每个ε，six cutoff1和one cutoff6的原列乘1+ε，再增four cutoff1 ε列，确是literal species；
\[
 \tau_\varepsilon=(1+\varepsilon)329/50+3.96\varepsilon
 =6.58+10.54\varepsilon\longrightarrow329/50.
\]
固定dε不影响主项。rational parameter可直接逐ε用printedTheorem2.1，L>329/50时选ε足够小再取极限；K版本按all-place slopes保持全部embeddings。这也单独支撑A15，无需把strict P3模型口头改成纯LCM。

实际species是 \((0,6,6,6,6,6,7,7,7,7)\)。其weighted sum为
\[
 \tau=\frac{6\cdot35+7\cdot64}{100}=329/50.
\]
scale16的真实变量替换同时把conformal log和Bost integral减 \(\log16\)，所以A15的两项scale费用一致。只有all-embedding meromorphic pullbacks与原定理的analytic hypotheses满足时才得该不等式；未给合格domain的存在或capacity numerical contradiction。

同一q0 rational reference也满足同一packet/模型，这是value-blind domain路线的限制；此处不把C16和rank10当新数值无理性。actual target \(q=\pi^2(R_0-M_0)/16\) 的代数性也不与 \(R_0-M_0\) 的有理性等同。

## I9. Actual-read及版本记录

* S稿全文实际读，SHA bde766；其source receipt实际全文读，SHA `bcf77395a646e8d120e6322c622d7c56bdbe1e16c0bbd13a8ed5cae22f1ca737`。
* A稿45b3候选实际全文读并逐节手核；补强后的439a最终版再次实际全文回读，新增relativePD双复形/HPD及A14a/b逐项独核。其NEW source receipt实际全文读，status FROZEN，pin与本文439a一致；receipt SHA `775149ca7c34a3f80fedf8a0a59e65bfa08edf76273ce0562b0f42486aeccb88`。本文按439a冻结。
* 旧toric §§2–8全部数学内容及最后source段回读；初次批量输出尾部截断，仅据实际收到范围登记，不冒记该批量调用全文。mirror全文实际回读；Yukawa Y1–Y10另行补读完整。
* [Morrow author primary](../literature/morrow_higher_direct_images_crystalline_author_20261006.pdf)，12页全部实际读，SHA `9d7bb24587a99edbdfa707c62c2590d0e469e931c937cb99fbe3f14af2f0c009`。第一次text输出GBK编码失败未输出正文，改为UTF8后完整12页读取；这是source读取，无数学producer。
* [Bhatt–de Jong author primary](../literature/bhatt_dejong2011_crystalline_derham_author_20261006.pdf)，10页全部实际读，SHA `6c66ed20334f5ce8d96c9af9c0523d69c9f50f776b8b5169300b461f0558e669`。
* [BK primary](../literature/bonisch_klemm_scheidegger_zagier_alternate_author_url_20261006.pdf)，actual PDF6–7、16–17、19，SHA `f124aab462ae953eff9a2c9df28cff63e1b63adad792a572a1c608226fdfac83`。未声称本轮阅读全文。
* [FR published primary](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)，actual PDF6–8，SHA `c36b46c110aa378caba371897b7ab45959941d10f8d61311496868bcd004dc68`。
* [CDT archived primary](../literature/cdt2025_arithmetic_holonomy.pdf)，actual PDF3–8，另随关键词定位读PDF9、11、14、16；SHA `5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1`。filename含2025而页脚copyright2026，不把filename当发布年份。
* root D1–D11 本人上一NEW独审已实际全文手核，最终fea017复读；本轮只回读D10–D14及执行/来源段，未重跑probe/symbolic producer。
* 本人没有重复下载这些PDF；新增Morrow/Bhatt–deJong由arith按verifiedTLS归档。未实际重读Katz本轮primary页，不冒记其source scope。

此独审不证明integer crystalline torsion-freeness、all-odd integral motivic completion、conifold integral nearby-cycle normalization、value-sensitive analytic map、CDT数值反证或Lean。它验证的是NEW全奇素数/全部阶 arithmetic模型及其明确适用范围。
