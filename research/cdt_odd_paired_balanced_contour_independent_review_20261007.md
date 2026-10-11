# balanced-contour D1–D18 的独立 FULL 纸面审阅

日期：2026-10-07。审阅者 `/root/source_pencil_finalize`。被审唯一 NEW 主稿 `research/cdt_odd_paired_balanced_contour_20261007.md`，actual FULL读取九节，SHA256 `f86cbe2e7fe3ba171b2e6a6f4bad83f678dc5b7a09ad2041350f3087b7c0f330`。结论：**PASS，无实质修订请求**。本审阅不是数值证明、producer或prime实验；旧580冻结记录只读，不执行/import/rerun数学producer，不修改旧文件。

## V1. 实际对象与正常化匹配

实际 FULL回读冻结 head-free lattice I1–I25、coupled Gram C1–C23、exact phase F1–F18，以及 kernel-jet content Q1–Q22的完整八节。lattice I4/I8的 cardinal polynomials、primitive pair约束和完整基与 D2准确一致；degree<3n、rank2n及实际ξ=αζ4+βζ5均保留。D3的竖线自下而上有 dz=i dx，故1/(2πi)恰转为已冻结 dx/(2π)，没有phase或2π遗漏。

尤其 D4正确以 R自己的三阶零计算：低 G_m一般不被S整除，G_m/S可有head极点。D5不需要把低列误称为S整除多项式。只在ξ=c∈Q的假设下积分与原有理B_n(c)识别；形式变量X的任意值没有被赋予轮廓period。

## V2. 残数、配对与必要充分绕数

独立取w=z−j：πcotπz=w^−1+O(w)，二导主部2w^−3，三导主部−6w^−4；K=6βw^−4−8αw^−3+O(1)。R=C_n S′(j)^3 d_j^−2 w^3+O(w^4)，故唯一可能simple residue是6βC_n S′(j)^3p(j)q(j)/d_j²。α项正则，其他Taylor项不能再贡献w^−1。这核实D4/D5的6β，而非6β/2π或一个错号。

2n为偶数，S′(m′)=−S′(m)。原paired values相同，故D7的pair residual准确相反。差cycle以Γ−Γ_R定义，残数定理和1/(2πi)给D8。用degree≤2n−1的d_mL_m+d_m′L_m′可独立指定每个t_m，且β≠0、a_m≠0。因此若整段bilinear form相同，各w_m−w_m′分别必须为0；反向由D8立即成立。D9是真正必要充分，限定head-only、紧支闭cycle及避极点条件，未被夸大成任意路径同值。

## V3. 无限竖线与nonhead跨越

独立核实固定n的度数：R的分子degree6n、分母degree12n+2，因此R=O(|z|^−6n−2)；pq degree≤6n−2，乘积O(|z|^−4)。在该有限宽strip的上下horizontal边，cot二/三导有uniform指数e^−2π|Im z|。所以horizontal integrals趋0且两vertical绝对收敛。两侧之间仅有全部heads，其配对残数和0，D10 exact同period成立；没有未经证明的n-dependent左侧主率。

对positive nonhead，h=Rpq正则；6βw^−4取h'''/3!、−8αw^−3取h''/2!，准确给βh'''−4αh''。negative denominator poles另有R二阶pole，D11没有冒充那里也适用。所有pole跨越的条件在D9/D11严格分开。

## V4. Hermitian商Gram与精确phase证书

D12是实际同一原basis的total-variation Hermitian Gram。非平凡弧段上密度除discrete zeros外非零，多项式非零不可能在弧段几乎处处消失，因此PΓ>0。由complex measure的Cauchy–Schwarz得||PΓ^−1/2 B(PΓ^−1/2)^t||≤1，transpose没有被误换为adjoint。

令U=[L,K_0] unimodular、E=U^−t前d列、C=L^tBL，则B=ECE^t。C_d(T)=q ww^t的唯一singular value是|q|Σ|w_I|²。Cauchy–Binet/Jacobi给Σ|w_I|²=det(E^tPΓ^−1E)=det(K_0^tPΓK_0)/detPΓ，从而准确推出D14：|q|=QΓΘΓ,d。该证明只使用冻结F1–F4的有限complex Gram身份，不依赖其后S-factor叙述。K_0实整数，Hermitian kernel Gram里的K_0^t正确；ν0的空det约定一致。

B与primitive整数kernel完全没变，因此q的全有限处整模型无需新坐标费用；PΓ的全部解析费用仍须重新估。D15由同一q的两个精确表达相除而来，右侧可以无增益，正文明确保留；不能同时把同一个商改善作为额外phase和kernel两次扣除。

## V5. 凸平均的方向

在固定实际补基U中，Schur quotient的quadratic form是对kernel变量y取infimum。故P_Q(Σa_jP_j)≽Σa_jP_Q(P_j)，方向正确。logdet既Loewner monotone又concave，给logQ(\bar P)≥Σa_jlogQ(P_j)≥min logQ(P_j)。因此D17准确排除这一positive-Gram凸平均操作超过最优单曲线bound；它没有排除复干涉或不同rows的独立representation。

## V6. 完整费用与定理量词

D18将同一q的非零整数lower Q^q_(n,d)/(DM)^d与D14比较，符号正确。冻结kernel-content的safe A_q(λ)=32λ−1−13λ²/4（λ∈[3/2,2]）属于actual原q，fixed(DM)^d保留。实际应用仍在已经证明无限适用的n=4r子列、真实ξ=c假设及adaptive actual rank上进行；没有给7r/顶阶无限非零或strict analytic margin的新声明。39.6875为安全upper预算，未被当成actual最小cost或方法no-go。

## V7. 本人实际primary读取与适用条件

本审阅 actual FULL读取新增Vartanian–Zhou固定v1 PDF1–8，文件 `literature/cdt_paired_contour_deformation_sources_20261007/vartanian_zhou2019_rational_rhp_arxiv1912_00500v1.pdf`，SHA256 `0729a0ef7aaf008d7854c365afc8669ccef8330bfd66511aa05def8d40c7df4f`。首次合并输出page5有截断，本人随后另单独完整读page5，才计1–8共8页。没有读或声明读343页全文。

PDF1/3的有限固定K及循环pole sequence、PDF7的positive probability measure与real analytic external field/growth conditions、PDF8的real rational inner product与正文保留条件一致。它们未覆盖当前随n增长pole集合、complex cot period及paired约束。被审稿未套用后文未读的asymptotic theorem，仅将它作为后续RHP机制的primary定位，适用边界诚实。

本审阅新增下载0、数学producer创建/执行/import/rerun0、prime扩表0。个人本轮研究Γ主稿实际primary40页，加本审阅8页，总48 distinct；这一总数不是同行累计，也不继承上一轮68页。唯一formalreview实际作者FULL回读后才交root；本稿不pin未来audit或同行receipt。
