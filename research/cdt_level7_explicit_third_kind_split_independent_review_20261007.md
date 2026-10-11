# Level 7 显式第三类周期分解的独立审查

审查结论：纸面证明通过。新分解保留实际算子、Fourier 起点与相对 cusp 积分，明确补齐第三类代表、第二类系数和端点常数三个缺口；没有据此得到新的数值无理性定理。

日期：2026-10-07。审查者：`/root`。实际全文读取 [主稿](cdt_level7_explicit_third_kind_split_20261007.md) 的八节、T1–T28；另实际读取冻结 `cdt_odd_level7_polynomial_extension_classes_20261007.md` §§1–4/E1–E18，核验所引用的算子、forcing 商空间和全部整数 polynomial forcing 的 D_n²模型。主稿初读物理大小19679bytes。数学审查不以文档 SHA 或程序编译替代证明。

## 1 原算子与整数载体

由 L1=−2t−4t²、r_B=t−t²，严格有

\[
 -r_B/3+L(-1/6)=t^2.
\]

因此 B₂=−B/3−1/6+A/6 的 forcing 和 zero constant 同时正确。Bρ=B₃−B₂的 forcing 是 t³−t²=−t r_B，属于 tZ[t]。旧稿 E12–E13 使用 integral q(t)、A、S 与 integral-unit 分母，故 D_n²[tⁿ]Bρ∈Z 对所有素数和所有 n 成立；没有因 T6 中的三分之一而漏掉新的固定费用。

L(AE)=pAS⁻²D²E 与 S²/A=f(1−t)(1−28t)/t 逐项给 D²(B_R/A)=fR/[t(1−t)]。这核对了 2πi 和算子变量，得到

\[
 h_2=ft/(1-t)=-f/3+D^2(-1/(6A)),\quad
 h=-ft+h_2.
\]

## 2 完整局部数据和代数留数

有理 r 表达式 T11 直接核对所有 poles：ρ只在 r=−7 的 CM−7 轨道有二阶 poles；h₂只在 P(r)=0 的两个 CM−3 轨道有三阶 poles；h 同时有两类。ρ、h₂的两 cusp native 零阶2，h 的零阶3，与 q²、q³起项一致。

CM−3 处 G=−1/(6A) 只有一个 simple principal part，二次导后只留下 δ⁻³项。故 h₂的 δ⁻²、δ⁻¹完全为零。这足以核证 second-kind 身份，而非只核 pole order。

CM−7 的 indicial resonant constant 是14。z=1/t 在 τ−w 中零阶2，乘完整 affine v₀/A 后给 coefficient (τ−w̄)/(7A_w(w−w̄))。微分两次时必须保留 δ⁻¹；T17 的符号和 1/(28π²A_w) 正确。

以 (2πi)²ρ(X−τY)dτ 为 differential，留数是 (X−w̄Y)/(7A_w(w−w̄))。主稿明确列出的 BF comparison 使用 w̄−w，而不是 w−w̄，及 first period 2πiA_w，故最终代数留数是 −η′/7。这里审查数学代入和 normalization，不把同行的 PDF 图像目读计为 root 本轮 fresh PDF 阅读。

非零向量留数不能来自全球 meromorphic weight−1 Bol 二次导，也不能由加 holomorphic cusp form 或有限 cover 消去。这个 non-Bol 结论不等价于数值无理性。

## 3 全部相对边界和积分符号

沿 τ=iy，D=−∂y/(2π)，因此 I(D²G)=[yg′−g]₀∞。Fricke 给 A(iy)=A(i/(7y))/(√7y)，于是 G(iy)在∞趋−1/6，在0为−√7y/6加指数小 error。前者的边界是+1/6，后者是0；导数 error 没有漏掉有限常数。

由 h₂和f的 cusp vanishing，积分普通收敛，无须引入 regularization。故

\[
 I(h_2)=1/6-\kappa/3,\qquad
 C_3=I(\rho)+1/6-\kappa/3.
\]

I(ρ)=−I(ft)<0，M₁=1/6−κ/3−C₃>0。主稿最后版的这一符号正确。0<I(h₂)<κ/27 给 9/20<κ<1/2；C₃上界和 I(ρ)的严格范围也由真实正积分核得出。没有使用已撤回的另一口头下界。

## 4 完整周期身份和使用范围

T26 由 B₂、Bρ的实际 affine shear 直接得到完整 σ-jump，常数 1/6 并非只有端点数值。Q-span{1,κ,C₃}=Q-span{1,κ,I(ρ)} 及对应关系系数变换正确。

第三类代表的 uniqueness 依赖相同完整 poles、cusp vanishing 和 [q]ρ=0；差除以 f 在 compact X₀(7) 上 holomorphic，故为常数。这排除了旧第三类 kernel 分解的 cusp ambiguity，没有把未知 cusp correction 免费忽略。

q_w=−e⁻ᵖⁱᐟ√⁷处有真二阶 pole，故 q-series radius<1。Cauchy–Hadamard 给某个系数 subsequence 指数增长；对任意固定 s，c_n/nˢ不能趋0。普通 Dirichlet series 没有收敛右半平面，因此 I(ρ)不能直接命名为通常 L(ρ,2)。该排除不否定将来与别的 L 值建立独立身份的可能。

本例 weight3/k1 不满足所引用 BF even-k CM Tate结论；有非零 cusp form f，也不满足 cusp cohomology vanishing 假设。主稿没有用 expected 的 k1 Rankin comparison 代替已证明定理。

## 5 审查状态

T1–T28 的数学证明通过；作者已核正 T1 align 中的行分隔格式并更新收审状态。root 已最终全文回读19710bytes版本，数学结论一致。root 没有执行数学 producer、prime 表、guard 或 Lean。本审查是独立纸面复核，不是形式化验证。

剩余目标为真实 I(ρ)的算术 comparison 或达到严格 CDT 余量的载体，而非再重复已补齐的分解三个问题。应先支付这些全局接口再声称目标值无理。
