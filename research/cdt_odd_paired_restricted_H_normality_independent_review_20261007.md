# 掩膜第三 Racah 与 restricted-H：独立全文审阅

日期：2026-10-07。审阅者 `/root/scaled_root_finalize`。实际完整读取作者候选 [主稿](cdt_odd_paired_restricted_H_normality_20261007.md) 八节 H1–H27，候选物理 SHA256 `074f55c5d83547b6b9a301cd515d1b676a5c3a2723a40e9101cb45e48b7f703f`。另实际全文读冻结 [cross 稿](cdt_odd_paired_cross_racah_injectivity_20261007.md) C1–C30 与冻结 [middle 稿](cdt_odd_paired_fixed_middle_racah_border_20261006.md) R1–R30，以核实际输入、halfjet 与已证 D/E 单位。此次静态审阅没有执行、import 或 rerun 任何数学 producer，没有辅助素数扩表或 Lean。

结论：在所注明的有限域实际模型和 p=18r+1 素数条件下，H6–H27 的结构定理通过本次独立纸面检查。没有从完整 normality 推出 restricted-H unit，没有新数值无理性或线性无关性定理。

## 1. 新第三族的质量与 norm 因子逐项核对

实际完整文本阅读 Koekoek–Swarttouw 原件 PDF28–29 共2 distinct页；[本地原件](../literature/cdt_paired_pearson_rankone_sources_20261006/koekoek_swarttouw1998_askey_scheme_report98_17.pdf) 170页、SHA256 `cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`，未称全文读完，未重复下载。

H4 的 m(k²)=k(k−r+1)_(2r−1) 由逐个 (k−j)(k+j) 直接成立；k=r 时 m=r(2r−1)!，S(r²)^−1=−(4r)!(6r)!，故 w_* 准确为作者负号。H5 的两个 successive ratios 与 H6 的 v_(x+1)/v_x 逐项一致；删除 middle 后 k≥r≥1，不存在遗留原点 half-mass。

Eq1.2.1 中的 α+β+1=6r+1、β+δ+1=γ+1=6r+1、γ+δ+1=2r，准确给 H8。Eq1.2.2 的权重分子有 (-4r)_x、两份 (6r+1)_x、(2r)_x、(r+1)_x，分母有 (6r+1)_x、两份 (-4r)_x、(r)_x、x!；逐项 cancel 后正好 H6。

同式 n-norm 的三项 α+β−γ+1、α−δ+1、β+1 分别为 1、1、10r+2，连同 n! 得 (n!)³(10r+2)_n；分母 α+β+2=6r+2、α+1=−4r 及另外两份 6r+1。M 的 α+1=−N 分支给 (-10r−1)_(4r)(2r+1)_(4r)/(-4r)_(4r)²。因此 H12 的 n0 常量和每个非零 n 的范数均与原件一致，没有借用旧两族公式或 g=0 误极限。

H9 的 Newton product 消去 x 参数；最高项由 (-n)_n(-1)^n/n!=1，给 H10。所有终止内分母单位，最大正指标 14r+1<p；ν0 中负因素绝对值≤10r+1<p。单位 norm 与单位 leading coefficients 的三角 congruence 给 H14 全 leading profiles 非退化。该论证是有限有理正交身份的合法参数特化，不含有限域 positivity。

## 2. degree<2r 的实际 C、右逆与完整 kernel

H15 使用原 C 的 5 complete−middle；m 在全部实际 middle（包括0）为0，故 C(T,mW)=5J_m(TW) 确实准确。以 degree<r 的 J_m Gram 作子块可逆，给 actual C 在 degree Q<2r 已满行秩和 H17 的右逆。这里仅除已证 J_r，而没有除实际 unknown cross-leading minor。

H18 后半列 mP̃_r,…,mP̃_(2r−1) 与全部 T-degree<r 正交；前半列用右逆消去 C。按 m 作 Euclidean division，前半列具有独立余数 u^j，后半列具有 degree r,…,2r−1 的独立商，准确组成 2r-dimensional ker C。

为检查 H19 的符号，采用 (remainder degree<r, quotient degree<2r) coordinates，monic synthesis determinant1。U 的前 r columns R 在余数块为0；第二 r columns K_low 的余数为 I。交换这两组列的符号为 (−1)^(r²)=(−1)^r；商的两个对角块分别 J_r^−1/5 和三角 P̃_r,…,P̃_(2r−1) leading coefficients。因此作者给出的 det U 和已证单位 prefactors 全部准确。

H20 的 middle evaluation 在 K_low 上正好为 distinct-square Vandermonde，在 K_high 上为0，故准确正合且实际 middle 在 ker C 上的更新秩准确 r。H21 保留 e0 的原点半质量；该单位 middle-only 项与完整 D 的和可能相消，作者没有把它升级为 H22 单位。

## 3. 2r boundary 的符号、determinant 与 kernel

H22 的 M0 只是 G=0 诊断，没有代替实际第五幂 G。U congruence 后首2r block [[0,I],[I,H11]] determinant(−1)^r，其 inverse 下右 block0，故 H23 的 determinant 与 corank 正确，无须实际 H invertible。

独立从 bordered matrix [[0,C,0],[Ct,D,V],[0,Vt,−E^−1]] 检查：消去 −E^−1 给 (−1)^r det(E)^−1 det M0；消去已知 D 得负 cross 的 2r Schur block。再以 diag(−I,I) congruence 得 H24 的正 cross。与 H23 合并后两次 (−1)^r cancel，正好得到 H25 的 det U² det E det D prefactor。−B_H 后再同一 congruence 给 H26；总维数2r为偶数，det 不变。

H27 的第一行给 C D^−1(Ct t−Vz)=0；第二行给 z=EVt q；于是 Hq=Ct t。反向由 ker C 的 annihilator=im Ct 和 Ct 单射恢复唯一 t,z。q0 迫 z0，再迫 t0，确为 kernel 等价。该 radical 是 Hq∈im Ct，而不是仅 ker H∩ker C，作者没有漏掉混合核。

## 4. 审阅通过的范围

通过：第三完整 masked-cross Racah 族全 profiles 单位；actual C 的 degree<2r 满行秩；known-unit 低度右逆、完整 kernel、确定 determinant scale；真实 middle 正合列及其秩；restricted-H 等价于无第五幂种子的 2r 已知 boundary。

仍未证明：boundary determinant 非零、D_high 压缩正常性、H|ker C unit、actual M5 在固定第五幂种子处 unit、无限 actual determinant 非零、固定有理 source 无限成功或特殊值无理性。完整 J_m 与完整 D 的正常性不自动控制 ker C 上的压缩；H22 unit 只是进一步 r-gate 的充分条件。此审阅没有增加实验性 unit 数据，也不构成 Lean 形式化。

本报告针对上述候选 SHA 的实际全文；最终作者回读、主稿是否保持该 SHA，以及 root 实际全文复核由各自最后收据记录，不在这里提前声明。
