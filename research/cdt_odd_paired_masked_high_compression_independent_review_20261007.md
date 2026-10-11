# 第四 Racah 与真实 high 压缩：独立全文审阅

日期：2026-10-07，NEW，审阅者 `/root/scaled_root_finalize`。实际完整阅读最终候选 [主稿](cdt_odd_paired_masked_high_compression_20261007.md) 九节 M1–M24，物理 SHA256 `bd107ba87fe707be5d8dc969b29949b05a4afd91e32baef4e41e5f9d4775bb1f`；此前 b61c、56a7 候选也已全文读。作者在 primary 公式范围段补充以下手核，并将短和的最大指标与含零项的项数准确区分；全部 M1–M24 数学公式不变。此前529冻结记录不动。本独审没有数学 producer 执行/import/rerun，没有辅助素数数据。审阅者本轮另有经 root 授权的 mirror/root FIRST1 一次，独立记录于其稿和来源收据，不挪作本算术稿的验证。

结论：最终候选的全部结构恒等式和限定障碍通过本次独立纸面核查；没有证明 actual D_high、restricted-H 或原固定 M5 非零。特别检查了 complete L、twice-masked Φ 和 actual high 压缩三者的区别。

## V1. 实際原件读取与第四族范数

实际完整文本读取：Chu1998 PDF1、10–12四页；KS报告 PDF28–29两页；Krattenthaler2101.04225v1 PDF1–4四页；Li–Long–Tu2103.08858v2 PDF18–19两页。共12 distinct primary pages，其中新 Chu 原件4页。未称这些 PDF 全文读完，未下载重复原件，也不继承作者额外 Li1–5 读域。

沿冻结 restricted-H 的实际输入：middle-vanishing m 与 high basis mP̃_(r+j) 保持原对象。complete D 的折叠 outer mass 为 S³，乘一次 m 在 k=r 时给 λ*=−r(2r−1)!/[(4r)!³(6r)!³]。相邻比为 [(x−4r)/(x+6r+1)]³·[(x+r+1)/(x+r)]·[(x+2r)/(x+1)]，准确给 M4。

KS Eq1.2.1 的 α+β+1=−14r−1、三个下参数均−4r；Eq1.2.2 norm 的 α+β−γ+1、α−δ+1、β+1 均−10r，另含 n!，分母 α+β+2=−14r。M 的 α+1=−N 分支给 (10r+1)_(4r)(2r+1)_(4r)/(6r+1)_(4r)²。故 M6–M7 的核、leading coefficient、n0 及所有 norm 因子准确。非空积最大绝对值14r<p，终止内无0，所以 M8–M9 的完整 L 正常性成立。

这不控制 Φ=D(m²·)：多乘一个 m 改变权重。它也不控制对第三族 high directions 的压缩；作者没有将 complete normality 当 restricted normality。

## V2. Christoffel 符号与限定 ordinary-Racah 障碍

Krattenthaler Theorem1 的 finite-window Christoffel identity，取 variables −b_i、修改多项式 ∏(u−b_i)，将 evaluation determinant 转置，给 (-1)^(rd)∏_(n<d)ω_n det[p_(d+j)(b_i)]/V_b。其符号亦可用 r=d=1 的 identity μ1−bμ0=−μ0p1(b) 直接核。最高 degree d+r−1≤4r，所用旧 norms 与 leading coefficients 均已有单位证明。有限代数身份的有理单位约化合法；不需要 Φ 正常，也不需要书面 theorem 的无限序列假设越过此窗口。

M11 的 r-node determinant 对完整2r Phi Gram 等价，不能推出它在只有 r 个 P̃_high 方向上的 compression非退化。outer支集外的 real-sign 说法不适用于 Fp，稿中保持该限制。

M12 的 twice mask prefactor、summand 和 M15 的7/7 reduced ratio 逐因子一致。r≥2 时其六个不同根位置在 F 中不会相撞；r≥4 时4r个实际 edges 多于交叉多项式最大degree12。普通同 quadratic-grid Racah 的 ratio 至多5/5，若全部边相等必为同一有理函数，与 reduced7/7次数矛盾。限定 r≥4、指定同 grid、正常非零 node ratios 的范围准确；没有否定小 r 拟合、其他超几何族、Christoffel gate 或实际 M5。

## V3. Whipple 平移、完整公式与印式范围

独立从 actual summand 乘 F_l 检查：F_l 在 x<l 为0，x=l+j 后终止长度 n=4r−l。x=l 的原 summand times F_l(l) 为

\[
\frac{(-4r)_l^3(r+1)_l^2(2r)_l^2(2r+l)_l}
{(6r+1)_l^3(r)_l^2 l!},
\]

用 (2r)_l(2r+l)_l=(2r)_(2l)、(r+1)_l/(r)_l=(r+l)/r，准确等于 M17 的 σ_l，没有遗失 well-poised factor。

Chu PDF11 Eq4.12 取 a=2r+2l、b=c=−4r+l、d=r+1+l、e=2r+l、n=4r−l。fourth upper 为1+a−d−e=−r；下参数为r+l、1+l、b+c−a−n=−14r+l。prefactor 展开成 factorial 为 (6r+l)!³(14r−l)!/[(2r+2l)!(10r)!³]，正好 M17–M18。新4F3的最大求和指标为 min(r,4r−l)，包含指标0，故项数为 min(r,4r−l)+1≤r+1；所有有限分母单位。其值可能相消，作者没有声称 T_l unit。

balanced4F3 的上下和差1准确；Chu Eq4.13 的额外 Dougall 条件在当前差13r−l，处于9r,…,13r，模p也非0，故不能套 factorial evaluation。

Li PDF18 印 Eq26 的 fourth upper a 在其后明确 c+d=1 的研究特殊化才与一般正确1+a−c−d相同。作者按独立审阅意见明确补充了印式范围与可手核的 counterexample：a2、c=d1、e=f1/2、g−1时，left7F6=99/100；Gamma ratio=24/25；printed uppera的4F3=17/16，product51/50；correct upper1的4F3=33/32，product99/100。各有限分母正常，n1时在 rhs下参数−2的pole前已终止。此手算只审计印刷 general formula，不是 actual辅助素数实验，也不否定该文满足c+d1的后续特殊化。当前新 proof 完整依赖 Chu Eq4.12，未依赖该印式错误。

## V4. actual 高块与 reciprocal 第五幂的准确范围

两组 shifted Newton 展开 M20 由4F3系数与 (-x)_l(x+2r)_l 的 monic product 自证；degree≤4r 的全部 triangular diagonals单位。product P̃_(r+i)P̃_(r+j) degree≤4r−2，故 M21 用同一 Φ 的 Newton moments 给全部 actual D_high entries，未拼不同权重的 norm。

E_eval 的4r+1 outer squares 互异、third leading coefficients单位，故完整 evaluation matrix单位。v=S^−1m、z=S³m² 均 nodewise单位，v²/z=S^−5。将 J=Et diag(v)E、P=Et diag(z)E 直接求完整 inverse，得 J^−1G5J^−1=P^−1；这是 M23，不除任何 principal block。J 在第三正交 basis 中 diagonal，Jacobi principal complementary minor identity 给 det P_I=detP det(P^−1)_(Ic,Ic)，准确得到 M24 的 ∏η_j^−2 prefactor，无符号遗漏。

目标 normality 等价于具体3r+1-dimensional outer fifth-power spectral-complement Gram normality，但它不同于原 M5 左上 r阶第五幂 block。有限处全 evaluation/unit metric 不提供任何 global degree/basis/height 免费变化，也不使其 principal minor自动非零。

## V5. 审阅通过与未证范围

通过：第四单mask cubic Racah完整profiles单位；twice-mask complete Phi leading Gram 的 off-support Christoffel formula；指定普通Racah shortcut在r≥4的严格障碍；所有 Newton moments 的准确短Whipple balanced4F3 formula；actual high压缩与outer第五幂spectral补块的determinant duality。印刷Whipple general formula范围问题已在最终新稿准确记录，未改旧原件。

未证：M11 的off-support determinant unit、D_high unit、H|kerC unit、固定第五幂种子处的 actual M5 无限 unit、fixed rational source 无限成功、actual higherSmith替代、足够同对象strict margin或新ζ/L/Catalan无理性/LI。完整 normality、合法超几何变换、完整 reciprocal metric都不升级这些结论。本审不是 Lean，也没有新增有限 unit 实验。

最后来源收据须在作者实际全文读本审、最终主稿回读后另作一向闭合；本审不提前声明这些未来读取已经完成。
