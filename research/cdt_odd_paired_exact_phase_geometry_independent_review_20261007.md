# exact phase geometry：独立全文纸面审查

2026-10-07，NEW，审查者 /root/source_pencil_finalize，作者 /root。被审稿为 `research/cdt_odd_paired_exact_phase_geometry_20261007.md`，物理 SHA `735150b725bfc590f471a9ed0fca97bc8226b6860118b7a88dcbbaea09ffb1c4`。本人已实际 FULL 读七节 F1–F18，并实际 FULL 回读冻结 coupled C1–C23 与 primitive-kernel K1–K18；本轮 authority 为572旧记录只读的 delivery_kernel_profiles，SHA `313ad01a4abe88dd8a8193561b30232dfa131c8832d126af18390eafc8514e72`。没有创建、执行、import、rerun数学producer或扩prime表。

结论：纸面检查 PASS，无实质修订请求。检查的是恒等式、量词和实际 phase 的识别；正文并未证明足够的 n² phase 损失或新特殊值无理性。

## R1. 同一原核商和正确的 complex Gram

沿 actual-rank 对象 B=ECEᵀ，U=[L,K] 为 unimodular real整数矩阵，C 非奇异且 q=detC≠0。原 P 变换约定为 RᵀP conjugate(R)，故在实U下 UᵀPU 的 inverse 左上块确为 EᵀP^−1E。block inverse 给 G=P_Q^−1；detU²=1 给 detG=detP_K/detP，ν0空det也一致。

F=P^−1/2E 是真正的 complex column matrix。C_d(T)=qwwᵀ 中 w 为 F 的全部最大 minors。对 complex w，(wwᵀ)(wwᵀ)*=||w||²ww*，因此唯一非零 singular value 为||w||²，不是|wᵀw|。Cauchy–Binet给||w||²=det(F*F)=detG。故 F3–F4 的 exact identity

Θ_d=|q|detP_K/detP

是对 actual d 个非零 singular values 的乘积；full detT=0 时仍严格为正，且没有忽略 primitive 整数格因素。首次 jet 的冻结身份 J_ν=q det(KᵀVK) 因而准确给 F6。a_V 的整数因子不能免费删除，正文保留此点及 q/jet 的两种不同整模型。

## R2. 非零全谱与 antilinear 坐标

Q_F=FG^−1/2 有 Q_F*Q_F=I，Q_Fᵀconjugate(Q_F)=I。右 transpose 是 coisometry，不是一般 complex inverse；T=Q_F T_Q Q_Fᵀ 的所有非零 singular values 与 T_Q 完全相同。因此 F5 比 determinant 粗界强，但不把它当新的算术 source。

采用 linear-first ⟨f,h⟩=∫f conjugate(h)dν，A f=conjugate(τ)conjugate(f) 为 antilinear isometric involution。直接代入得到 ⟨e_i,Ae_j⟩=T_ij。若 f=Σx_j e_j，则 ΠAf 的第i坐标是 Σ conjugate(T_ij)conjugate(x_j)，即 conjugate(T)conjugate(x)。其平方的坐标是 conjugate(T)T=T*T，因为 T symmetric。这验证了稿中的 conjugation，不能改写成未经核对的 T conjugate(x)。两个 orthonormal frames 的 cross-Gram 给 principal-angle cosines，ν个真实 zero singular values 对应直角；F8 的 spectrum准确。

## R3. 去核 trace、尺度和 min–max

δ_i=1−σ_i²∈[0,1)，TrD^r−ν=Σδ_i^r。finite d 和正项 Tonelli 展开给 F9。每项都减同一ν而不是只在r1减，避免对实际核制造无穷 phase 信用。

M_R≤(d/2)H_R≤(d/2)(1+logR) 对任何R成立；m=2n且 R(n) polynomial gives O(nlogn)。这限制的是该 truncated certificate 的保证量，不能反推实际−logΘ_d至多O(nlogn)。稿中已明确两者区别。F11 layer-cake 在每个σ>0下直接成立，排除ν个zero后积分有限；s=nt的变量替换无缺失因子。若 actual (kerT)^⊥ 中存在ℓ维 exponentially contracted subspace，先对 d维非零 restriction 使用 min–max，确给ℓ个**非零**小 singular values。没有把已存在的kernel算入指数压缩。

## R4. 原 measure、S⁵ 和 cot phase

冻结 C1 原 S=∏_(j1..2n)(z−j)、R∝S³；抽出 g_i=S u_i 后真实 density 为 RK S²，而 total variation 是 |RK||S|²。f↦Sf 确实是相应两个 Hilbert spaces 间的 isometry，保持同一 B/P/T，没有把原复杂 measure 换成正 measure。

在 z=2n+1/2+iny 上，S factors 实部依序为 r+1/2、r0..2n−1；rising factors 实部为2n+1/2+j、j0..6n。故 F13 的两个 arctan sums 权重恰为5和−2，并且 K 是同一原 αζ4+βζ5 source。

独立按 d/dz=−i d/dx、πcotπ(1/2+ix)=−iπt 求导：第二导数=−2iπ³st，第三导数=−2π⁴s(1−3t²)。代入 −4α第二导数−β第三导数，严格给 F14。α0情况下 K 的零点在 fixed x，不落入固定 ε≤y≤M 大n区域；|argK|≤π 的选择足够使 argK/n 为O(1/n)。稿中没有假定 phase 全球连续principal argument或抹掉零点。

midpoint sums在第一个区间t∈[0,2]对 y≥ε 光滑，第二rising sum额外末项只O(1)；所以 F15 的 uniform compact误差成立。负半轴的 conjugation/固定π差不影响 n主率。该 phase 是 density phase，basis u_i 的自身 phase 不在 Φ 中，不能据此单独声称整个 Gram 谱指数小。

## R5. stationary point 与 primary 范围

对 Φ 分别求导给

Φ'=(7/2)log(y²+4)−(5/2)log(y²)−log(y²+64)，

Φ''=[100y²−1280]/[y(y²+4)(y²+64)]。

因此 Φ' 到8/√5下降，之后上升且从−50/y²+O(y^−4)负值趋0，y0极限+∞。在y²2、3的整数比较分别为6^7>2^5·66²和7^7<3^5·67²；唯一 positive stationary 在(√2,√3)，F17 的幂方程正确。没有执行 root 数值搜索。

本人本轮实际完整文本读 Deaño 固定 v1 PDF1–7七页、Garcia–Putinar AMS PDF1–5五页，共12 distinct页；两份是root已下载的原件，本人没有重复下载。Deaño的 Theorems2.1、2.2、2.4 限定 linear V、[-1,1] 和 λ<λ0；Remark2.5确实写明 omitted Hankel determinant estimates。正文引用其启发并拒绝直接移植，准确。AMS的§2.1 conjugation与§2.2双线性kernel convention支持上述语义，但实际 finite-Gram 证明已自足；没有把原paired空间当标准Hardy model space。PDF4的Deaño图页只按完整文本读域记录，不声称目读了图中数值实验。

这12页属于本人的本轮相位独审读域；与本人另一个 period-extension 主稿已读56页不重复，合计68 distinct primary页。归档整本34、31页不等于本人本轮全文读。没有继承root的读页作为自己的读页。

## R6. 最终量词

F18在同一有理性假设、真实无限 actual-rank 子列、已合法的 q 整模型下比较 |q|与 Q_(n,d)/(DM)^d。把 exact F4代入，严格负 limsup 的充分性正确；fixed费用、真实核方向、相位均保留。该条件目前尚未被证。本文既没有由 source-rank推出 CDT函数rank，也没有把 oscillatory density 的存在当已经跨过算术预算的证据。

被审 main hash 在完成本审查时仍须物理核对；本文件作者 actual FULL 回读后才单向收据，不 pin未来audit或同行receipt。572旧记录只读，本文仅作新稿正式独立纸面审查。
