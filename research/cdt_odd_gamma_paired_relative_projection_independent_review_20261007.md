# paired-relative projection 的实际全文独立纸审

2026‑10‑07。审阅者 `/root/masked_racah_finalize`。本审仅审核指定新稿，不创建、执行、导入、重跑数学 producer，不运行 guard 或素数表；不修改604项旧冻结记录。

## V1. 对象、实际阅读和最终 fingerprint

实际 FULL 读取被审稿 [paired-relative projection](cdt_odd_gamma_paired_relative_projection_20261007.md)，全部8节、P1–P27，物理18952bytes，SHA `cefd8f209a63bb344577fee0354076305e0e683c8189a1c63747b509262fc6a1`。审阅没有把候选的 formal operator order 或 ambient PV field dimension 当作 scalar function rank。

实际 FULL 回读三份直接冻结输入：

- [dual relation extension](cdt_odd_gamma_dual_relation_extension_20261007.md)，全部7节/D1–D17、公式D1–D30，SHA `f8e36b1bf0b605d73574e556bc9cc382a944a07523b74dc5d12a5b64446208ab`。
- [unramified forcing split](cdt_odd_gamma_unramified_forcing_split_20261007.md)，全部10节/U1–U34，SHA `611485070e8364a2b2905ea60654eac12770b8bb76d3b8d2c6f929b356de37ac`。
- [tensor Taylor projection](cdt_odd_gamma_tensor_taylor_projection_20261007.md)，全部10节/T1–T28，SHA `0a9eb062f5ca02f3337a9532457a01b6b8904e064b2ff1ebf187b302388adc9e`。

Authority 使用 immutable [carry–Cartier–split–algebraic audit](cdt_odd_delivery_carry_cartier_split_algebraic_20261007.json)，SHA `44521a432fd71bdfef7e10a0d3ac63d636878b32aabfad5b293d8276a9fdf4a7`。本审没有人工 FULL 重审604项，也未借这一 audit 的阅读域为本审增加页数。全文旧总报告为 mutable 汇总，不作为 formal pin。

## V2. P1–P9：普通点完整 jump 的有理初值与比例

P2 的一步 coefficient recurrence 正确，实际 `h_1=3840` 与 `L1=−h_1t` 一致。冻结 dual D9–D13 的 tail estimate 确在任意 `c<q<radius R` 上给完整 analytic `C_Rf_0−B_R`，所以P3不是仅首项连接。各半数及 fifths 与0的 difference 均非integer；GM实际PDF2的无共同根 modZ criterion支付 irreducibility。

对 ordinary rational `μ≠0,c`，原L的普通9阶首系数 `μ⁹(1−Λμ)` 非零；canonical ordinary initial basis `v_i` 的递推只除有理非零数。冻结 dual 的 Green form 在 `D` jets 中的矩阵在Q(t)、ordinary initial basis与D初值间的 triangular转换也在GL9(Q)，故P5的 `G_μ∈GL9(Q)`，不存在未支付的 Betti comparison 常数。

完整 residue identity `ℬ(v_i,χ_R)=2πi Res_μ v_iR dt/t` 中每个 residue只用 finite rational jet；非退化 pairing于是使 `χ_R/(2πi)` 的9个 initial coordinates全部有理。两条完整 solutions若成常数比例，选第一条一个非零 initial coordinate便得到P8的 `λ∈Q`。沿相同返回路径作相同 invertible continuation不改比例。这里没有把返回MUM basis的全部 entries宣称有理，也不把 algebraic μ 的结果免费降至Q。

P9的 stronger linear-row论证亦成立：若 `χ_2=q(t)χ_1`，其所有 continuations使 multiplication by q 送 irreducible solution space V 到V，故 `q^jχ_1∈V` 对全部j成立。有限维给constant polynomial关系，强制q locally、继而 globally constant。两条genuine jumps为非零与允许λ0的边界已分别标清。

## V3. P10–P14：确切 scalar invariant 域，而非一个假设的 K-automorphism

`R_2−λR_1` 有理且仅有同一 ordinary pole μ，P4恰消该唯一新增完整jump；split U19–U21遂给唯一 `Z=T+a f_0`，`a=−T(0)∈Q`，而 `C_2−λC_1=a`。P11的sign与Z定义一致。

P12分支 `a≠0` 时由 `f_0=(Z−T)/a` 确得 `k=Q(t)(f_0)`，`a=0` 时 `k=Q(t)`。原齐次系统在μ ordinary，所以 `T_μ` 固定全部homogeneous germs、χ1以及Z；因此其所有iterations把B1送到 `B1+nχ1`。即使 `T_μ(K)` 不等于K，ambient germ/PV field中的 continuation仍可迭代，此处正文已正确明定义 “invariants among K”。

假设B1在k代数后，同一个非零polynomial因coefficients fixed具有无限不同roots，矛盾。对任意 quotient `F=p(B1)/q(B1)` 的 μ‑invariance，P13使 `p(X)−Fq(X)` 在ambient field有无限不同roots，故其全部coefficients为0；取q一个非零coordinate得 `F∈k`。所有continued denominators仍是非零germs，因为 continuation是可逆field automorphism；没有删除可能的meromorphic poles。反向k显然fixed。P14的全部finite-degree polynomial/product/quotient因此已证，无需把B1、B2假设为独立形式变量。

此部分严格仅分类两个 undifferentiated scalar germs生成的域；没有借无限translation为单个μ-loop的fulljet/tensor场作不当分类。

## V4. P15–P24：真实 nonsplit 配对、数值 relation 后的 rank collapse 与 Q 下降

P16由 `L1=−h_1t` 直接验证，并准确保持两个forcing的同一个μ pole5及非零χ5。P17的 `C_2=ζ5−1`、`B1−B2=f_0−1` sign一致。后者有整数Taylor且nonrational，因为其conifold jump为ψ非零；它没有使用ζ5有理性作新branch filling。B1在Q(t)(f0)上transcendental还真正给 `{1,B1,B2}` rank3。

P18沿冻结 dual D26–D28的all-layer carry证明支付所有primes及prime powers，固定N只为实际B5而非整PV field。新integer correction保持同一cap；单独输出f0−1确为cap0，但任意 `Q(t)(f0)` quotient不能免费领取这一cap，正文已保留该限制。

`F_i=B_i−u_i f0` 下 `Z_u=T+(a−u_2+λu_1)f0`。若完整c‑jump分别消失，P3及ψ≠0给 `u_i=C_i`，P11遂使该coefficient为0。P21只用same μ translation便得全部scalar invariants在Q(t)，不需另用Taylor、O9或最高weight theorem。P22的校准rank2、F2=F1+1与f0−1不属于该relation-filled二scalar场的断言一致。

P23的rational下降自足且正确：无限coefficient equations的row space在有限Q向量空间中由有限个rows张成，solution kernel定义在Q。现有complex denominator vector的常数coordinate非零，遂Q kernel内也有一个该coordinate非零向量；其product numerator仍在Q[t]。在P12/P19 scalar field内，Q-Taylor给T0 fixed，加c fixed后原三点全部monodromy fixed，PV property给C(t)，再P23给Q(t)。这一scope没有取消新增pole或arithmetical endpoint的费用。

## V5. P25–P27：真正付费的 regular-singular extension 与全部 finite generators

P25是一条具体9+s维 companion extension，包含原fundamental homogeneous列和particular jet列；没有把minimal scalar order同新增constants的数目混用。

P26的local gauge是本稿重要新证明。原regular-singular block在每一local coordinate（含∞的 `x=1/t`）有 meromorphic invertible Fuchsian gauge，β_i因rational forcing及meromorphic gauge只有finite pole order。令 `\tilde e=x^{-M}e`，则 `e=x^M\tilde e`，确得到右侧 `x^Mβ_i` 以及新diagonal `−M/x`。选 `M≥max poleorderβ_i−1`，全部entries最多simple pole，准确证明ordinary任意high poles、0/c及∞均regular-singular。此变化并不声称整数格免费保持。

Singer实际PDF19–20的Schlesinger Proposition1.3.27适用于P26所付的完整extension；PDF13–14的PV Fundamental Theorem/Cor1.3.10给full fixed field C(t)。P27要求每个新增ordinary generator和c的完整fixed，加 genuine Q-Taylor的0 fixed；sphere relation再支付∞。表达式新生meromorphic poles不改变PV connection monodromy。于是全部finite tensor/rational/fulljet/Green/inverse expressions若满足这些强条件确降到Q(t)。本文没有把仅μ-fixed或selected projection改称满足P27，也没有否定保留其它generator的relative新base方案。

## V6. Primary 实际页域与 documentary 范围

本 formal review 另外 actual FULL 读取：

1. [Golyshev–Mellit固定v1](../literature/cdt_gamma_connection_sources_20261007/golyshev_mellit2009_gamma_structures_arxiv0902_2003v1.pdf)，PDF1–3，3distinct页，核actual irreducibility criterion。
2. [Singer author lecture](../literature/singer2009_differential_galois_lms_author_20261006.pdf)，PDF13–14、19–20，4distinct页，核PV fixed field、regular-singular definitions与Schlesinger Proposition1.3.27。实际原件82物理页，未声称全文82页或source作者所读的10–20全部页。

Assigned review的primary范围为7distinct页；其余本轮own modular manuscript的58页另行记录，personal合计65distinct local primary PDF页（文件不同，页域无重复）。本审没有继承source作者BH三页或17页读域，也没有新download/render/producer/prime或任何Lean操作。唯一新PDF为own modular任务的Bertolin–Waldschmidt20页，不用于P1–P27的数学证明。

## V7. 审阅结论

**PASS，未发现需改正文的数学项。** 已actual FULL审全部P1–P27与上述三份完整冻结输入，逐纸核local rational jump vector、λ有理、arbitrary scalar rational μ固定域、nonsplit校准与relation后collapse、Q descent、local Fuchsian gauge及全部generator/PV边界。

新增成果为限定但真实的scalar fixed-field分类与rational extension的全loop边界；不等于ζ5/ζ7/κ/Catalan的新无理性、LI或形式化定理。作者仍须actual FULL收读本审并最后FULL自读unchanged主稿，随后闭合单向FINAL receipt；本审不pin future receipt、mutable总报告或互相receipt。审阅者保存后亦实际全文回读本审，再发送最终SHA。
