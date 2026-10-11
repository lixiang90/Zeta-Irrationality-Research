# 固定 λ2 第二 Racah、真实交叉块与质量 map：独立全文审阅

2026-10-07，NEW，审阅者 `/root/toric_chow_completion`。本轮504既存输入与全部同行数学 producer 只读，审阅没有执行、import 或 rerun 任何旧/同行程序。本文纯纸面独审，新增数学执行0。原 B6/k3/s5、degree<3n、rank2n 配对整数格不变。

## V1. 实际全文读取和固定版本

实际完整读取作者稿 `research/cdt_odd_paired_cross_racah_injectivity_20261007.md` 十一节、C1–C30，SHA256 `d5401071966ba85d67a53794e29f6a253ecd3da1b6e6ae7cd923883ab7a9d63d`。完整读取候选来源收据 `literature/manifest_cdt_odd_paired_cross_racah_injectivity_20261007.json`，SHA256 `98cb1752215aa78c6c4c59a57cc678f81108785576a41ba2fba1539c7698fc94`，全部字段均已读。候选状态保留为当时实际快照，不要求未来最终收据保持该指纹，也不将未来最终收据读取列成本审阅已完成的读域；后续实际读取独立登记于 NEW 最终收据或主记录，不修改本审阅。

实际完整读取 root 的 `research/cdt_odd_paired_source_radical_response_20261007.md` S1–S6（含 S3b）、S1–S14，读取时物理 SHA256 `10897f75c7a2cb932988a751a25a85dafd79640b715090b7715fc96aeaa37a7a`。这是实际读取快照，不要求 root 未冻结稿未来保持该 SHA。其数学 PY/JSON/guard 未被本审阅者执行，也未被本审阅者静态全文读取。

冻结 `cdt_odd_paired_single_bordered_nonzero_gate_20261006.md` 的 B1–B2 实际 L/J/D 定义和相邻首段已回读；冻结 `cdt_odd_paired_fixed_middle_racah_border_20261006.md` 的 R20 行列式身份本轮作定位读取，全文独审是上一轮已完成的范围，本轮不冒记新的全文读取。

## V2. 完整第二 Racah 正常性的手核

逐项核对 C3–C9 的 folded 权重、Racah 参数和 KS Eq1.2.2。保持终止参数 α+1=−a，将 γ=a+ε、δ=−a−1 的有限有理身份取 ε→0：k=0 的质量仍为1，k>0 的 `(g)_k(1+g/2)_k/(g/2)_k` 极限为 `2 k!`。这得到作者的 `v_k=2(a+1)_k/(-a)_k`，不能把原点质量也乘2。

在 norm 中 α+β−γ+1=1、α−δ+1=1、β+1=2a+2；与额外 n! 合成 `(n!)^3`，故 C9 没有误用上轮三次权重 norm。独立代入 ν0 和 s0 后得到 `J(1)=−(2a+1)!/(2a+2)`，符号与实际 a=5r、p=18r+1 相容。

所有需要除的 factorial/Pochhammer 整数因子最大绝对指标为 `3a+1=15r+1<p`；n=0 空积另算，n≤a 时 `(-a)_n` 无零。C7、C9 的 leading coefficients 和 norms 都是单位，因此完整 J 的每个 leading profile d≤a+1 可逆。这里使用有限有理正交身份和具体单位，不使用有限域 positivity，也不推出任何实际 modified profile 单位。

## V3. 实际 cross 满行秩、右逆及确定尺度

mask `m(u)=Π_{k<r}(u−k²)` 确实包含原点与全部 middle；`C(T,mW)=5J(Tm,W)` 保留实际 λ2。`deg(Tm)<2r`、`deg W<2r`，而实际第二空间仍有 `deg(mW)<3r`。完整 J^[2r] 已证非退化，因此 C^t 单射，原 r×3r 的 C 行秩恰r。结论不需要 actual cross 首r阶 minor 非零，也没有证明 M5 单位。

手核 L1 是对角1的 upper triangular，C15 的 Z+/Z0 满足 L^tZ+=I、L^tZ0=0；C16/C17 提供已证单位右逆及全部2r维 kernel basis。确定尺度 C18 中移列的 `(-1)^r` 与 `det[Z+,Z0]=(-1)^r` 抵消，monic division synthesis 的 block 交换符号为1，得到 `det U=5^{-r} det(J2)^{-1}`。这仅是实际辅助 F_p 上的局部单位规约，不是更换 global S 或免费提供其 archimedean norm。

独立用核第一行 `q1=−Gt` 和 identity pivot 核对 C19–C22：原4r目标的 determinant 与 corank 准确归约到作者3r mixed-boundary gate，列交换符号为 `(-1)^r`。C22 与冻结 R20 的已知 prefactors 相容。只有额外实际 H22=H|ker C 非退化时，才能进一步使用 C23 的 r阶 gate；稿中明确保留这个条件。H22 奇异不表示原 M5 必奇异，C20–C22 仍成立。

## V4. 完整连接、middle 和 contiguous 障碍

逐项核对 C24 Newton 系数的符号：两个 terminating Pochhammer 符号抵消得到正 binomial 系数；C25 的下降递推仅除已证 ell_n 单位。C26 的完整部分为 `5 j_n B_mn`，再准确减去原 middle 的有限 rank 项，C27 在明确两个 Racah bases 中成立；T-basis 改变也必须同步作用于实际 G，不能当作旧 monomial entry 数值。

Racah-I 第j步的 C28 权重在 j≤a 分母仍为单位，support 正好0,…,a−j。支持 squares 两两不同，因为2a<p；Vandermonde 与非零支持权重给完整 moment matrix 的精确秩 a−j+1。j=2r+2 的支持数为3r−1，故3r-profile 奇异。这个全尺度反例只否定所述自然路径的“每步 unit norm”前提，不是否定 actual λ2 M5，也没有排除其他路径。

## V5. 原物理 half-fold 和质量 map

直接展开 C29 的质量 Gram，乘36后使用两条实际 leading-kernel 方程，再用 `C_L+LJ=6F_L`，得到稿中的对称 bilinear identity；恢复 Zz 的条件与 root S3b 一致。没有使用未知 radical Gram 非退化。

物理系数相消为 `L_(i,l)J_(l,j)=T_i(a_l)Q_j(a_l)/S(a_l)`，无额外 κ。p=18r+1 下 c/2=13r+1，`y=5r−l`；reflection-common 节点给 |y|<r 的 η=1/2。非零 middle 的两次各半质量、原点的一次半质量以及 outer 正节点的一次全质量，准确合成为 `F_L(T,Q)=J(TQ)`。原点 halfjet 未被删掉。

完整 J 首r阶单位使 F_L 满行秩。若 Ev=0，则 `Jq=−D^{-1}L^t t`，结合第二 kernel 方程得到 `6F_L^t t=0`；故 t=0，再由 J/Z 单射得 q=z=0。C30 因此是实际 leading radical 上 E 单射的全尺度命题。单射不保证其 restricted finite-field Gram 非退化；稿中保留这一区别，固定 rational source 的无限成功仍未证。

## V6. 一手原件实际读域

本审阅者实际完整文本读取下列页，不将作者读页算入自己的范围，也未把 archive 总页数当作全文阅读：

- 复用 KS 原件 `literature/cdt_paired_pearson_rankone_sources_20261006/koekoek_swarttouw1998_askey_scheme_report98_17.pdf`，SHA `cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`：本轮实际 PDF28–30，3页。核 Eq1.2.2 finite orthogonality、norm 与有限有理参数范围。本审阅者本轮没有 render/view PDF29，不冒记作者的视读。
- NEW 同行归档 Mañas III 原件 `literature/cdt_paired_cross_racah_sources_20261007/manas2021_pearson_III_arxiv2107_02918v2.pdf`，SHA `a6556f2d7b80841b8d0a26eac9a86f6274cf4a9a81af4996205f21ad36251763`：本轮实际 PDF2–3,7–8，4页。核 Hankel/Cholesky 与 shifted Christoffel evaluation 的额外非零前提，没有把这些前提免费用于实际 modified target。
- NEW 同行归档 Oste–Van der Jeugt 原件 `literature/cdt_paired_cross_racah_sources_20261007/oste_vanderjeugt2016_doubling_hahn_racah_arxiv1507_01821v3.pdf`，SHA `2ff7ada189c8e63cd06011f8ab631db37cb36d26b2c6b6e1fd7056f6aa67b158`：本轮实际 PDF23–25，3页。核 Theorem11 Racah-I shifts 与 Proposition12 的实正参数限制；有限域 rank-collapse 使用稿中自足证明。

合计本审阅10数学页，其中7页来自本轮同行新归档，3页来自既存原件。本文没有下载新 PDF、没有新增代码或数学运行、没有扩展辅助 prime unit 表。

## V7. 结论与严格范围

所审固定 d540 全文 C1–C30 通过独立纸面核查：第二完整 Racah 全 profiles 单位、实际 C 满行秩及显式右逆/ker、确定 determinant 尺度、无未知 norm division 的 mixed-boundary gate、明确条件下 r-gate、完整连接与指定 contiguous 路径的秩障碍、实际 half-fold 后的质量 map 单射均成立。

审阅没有证明 H22 正常、mixed kernel 消失、M5 无限 unit、restricted Gram 非退化、固定 source 无限成功、全局费用改进或任何新的 ζ/L/Catalan 无理性/线性无关性定理。原 same-S 算术费用不变。候选来源收据读取是 V1 的实际范围；未来最终来源读取另记 NEW 最终收据或主记录，不追加未来段落到本冻结审阅。
