# level20 Cartier 源的精确消去：有界慢方程与积分坐标的右因子障碍

日期：2026-10-06。本文只新增，不修改或重跑冻结报告。新的全尺度输入是：保留真实周期载体后，Cartier primitive 满足一个次数不随 p 增长的四阶非齐次慢方程；三阶算子确实精确消去周期项。不过，该方程的算子有右因子 θ，拉回快变量后仍不含原始积分坐标。因此这条复合消元路线尚未给出新增 primitive S3 行。本文没有排除其它 actual-packet 混合关系，没有降低已有 CDT 成本，也没有得到新的数值无理性定理。

## 1. 真实函数、周期载体及 prefix 的范围

沿用 [完整模型](cdt_odd_level20_model_20261006.md)、[真实目标积分](cdt_odd_level20_target_integral_20261006.md) 与 [Cartier 核](cdt_odd_level20_cartier_kernel_20261006.md)。令 K=Q(√5)，θ=t d/dt，ε=χ₅(p)，并以 ε=1 选择负下标、ε=−1 选择正下标。写

\[
A_\varepsilon=A^{(\varepsilon)},\quad
f_\varepsilon=f^{(\varepsilon)},\quad
H_\varepsilon=A_\varepsilon(f_\varepsilon-\varepsilon\Theta),
\qquad \Theta=-5\sqrt5\,L(3,\chi_5)/16.
\tag{S1}
\]

定义实际未平移源

\[
\boxed{K_\varepsilon(t):=A_\varepsilon(t)f_\varepsilon(t)
       =H_\varepsilon(t)+\varepsilon\Theta A_\varepsilon(t).}
\tag{S2}
\]

这里 Kε 的字母表示函数，不能与数域 K 或固定原始 source 格混淆。它的原点值为0；fε 的原始 q 系数由 θq³fε=Vε、fε(∞)=0 唯一确定。不在 (S2) 中删去 ΘAε，也不将 Aε 当成此前 H 的共同 weight0 解析叶上的免费函数。

Cartier 稿已证明，对所有排除固定坏素数的 p 及每个好 place，

\[
R_p(t)=P_p(t)/D_\varepsilon(t),\qquad
D_\varepsilon=(1-t)N_\varepsilon C_\varepsilon,
\quad\deg D_\varepsilon=5,\quad\deg P_p\le5,
\quad P_p(0)=1+\varepsilon p^3.
\tag{S3}
\]

Pp 是 integral polynomial，Dε(0)=1。使用该稿明确的 k-linear relative-Cartier 识别，正规目标积分 I_H=∫(H₋−H₋(0))dt/t 的前缀缩放

\[
Y=p^3H_-,\qquad Z=p^4I_H
\]

在 N≤p² 的 integral prefix 中满足

\[
Z\equiv J_{p,\varepsilon}(t^p)\pmod{p,t^N},
\qquad
\theta J_{p,\varepsilon}\equiv R_pK_\varepsilon\pmod{p,t^p},
\quad J_{p,\varepsilon}(0)=0.
\tag{S4}
\]

如果使用 exact Frobenius 参数 s=t(q(t)^p)，则 s≡t^p (mod p)，所以同样有 Z≡Jp,ε(s) (mod p,tᴺ)。这是模 p 的 prefix 身份；不是模 p³ 身份，不是无界全级数整性。1,…,p−1 均为 unit，使 J 在 degree<p 的范围内唯一。

## 2. 三阶算子精确消去周期载体

令模型三阶算子为 L3,ε，并写其 Euler 规范

\[
E_\varepsilon=t^3L_{3,\varepsilon}
 =\theta^3+b_2\theta^2+b_1\theta+b_0,
\qquad \overline U_\varepsilon=t^3U_\varepsilon.
\tag{S5}
\]

模型给出精确 char0 恒等式 L3,εHε=Uε、L3,εAε=0。因此

\[
\boxed{E_\varepsilon K_\varepsilon=\overline U_\varepsilon\in K(t).}
\tag{S6}
\]

(S6) 是同一个算子作用于 (S2) 后的真实消去，使用实际 Aε 的齐次方程，不是假设 Θ=0。它甚至不需要未知周期的有理性假设；当讨论原始 H source 的算术格时才使用该假设。

定义一个随 p 取实际 Hecke 核的 char0 辅助 primitive

\[
\boxed{\Xi_p(t)=\int_0^t R_p(u)K_\varepsilon(u)\,du/u.}
\tag{S7}
\]

Kε(0)=0，故这是原点全纯芽，Xi_p(0)=0。其 degree<p 的 Taylor 系数在好 place integral：Kε 的此段系数只涉及 q-index<p 的 n⁻³，整数双向坐标与 R_p 的整系数不引入 p 分母，末次积分的1,…,p−1亦均为 unit。由 (S4) 的唯一性，

\[
\boxed{\Xi_p\bmod(p,t^p)=J_{p,\varepsilon}.}
\tag{S8}
\]

Xi_p 的无界级数不因此变为 p-integral；本文只使用上述 prefix。结合 θXi_p=R_pKε 与 (S6)，有精确四阶慢方程

\[
\boxed{\left[E_\varepsilon\circ M_{D_\varepsilon/P_p}\circ\theta\right]\Xi_p
       =\overline U_\varepsilon.}
\tag{S9}
\]

M 表示乘法算子，顺序不能交换。相同等式在原点把全部项还原为 integral prefix 后，对 J 模 (p,tᵖ) 成立。

## 3. 固定 degree≤47 的完整清分母

以下次数界由模型的有理式给出，对所有好 p 成立。令 C_opp 是模型 R_gauge=Aε/S 分母中的另一 C 因子；它与 Dε 的 own C 不同。设置

\[
\Lambda_\varepsilon=(1-t)N_\varepsilon C_{opp},\qquad
B_\varepsilon=\Lambda_\varepsilon^3\Delta^3,
\qquad\deg B_\varepsilon=27,
\quad B_\varepsilon(0)=1.
\tag{S10}
\]

写 j=θlog(Aε/S)、qproj=t²Q。Euler gauge 展开为

\[
b_2=-3j,\qquad b_1=3(j^2-\theta j)+4qproj,
\]
\[
b_0=-j^3+3j\theta j-\theta^2j-4qproj\,j+2\theta qproj.
\tag{S11}
\]

j 的分母整除 Λε；θj、θ²j 的分母分别整除 Λε²、Λε³。qproj=tQ₈/[(1−t)²Δ²]，θqproj 的分母整除 (1−t)³Δ³。因此 Bεbᵢ 都是 K[t] 中的多项式。模型的 Ubar 分母整除 (1−t)³Δ，也被 Bε 清掉。

gauge Aε/S 在∞为有限非零值，j=O(t⁻¹)；qproj=O(t⁻¹)、Ubar=O(1)。所以 bᵢ 在∞有界，

\[
\deg(B_\varepsilon b_i)\le27,
\qquad \deg(B_\varepsilon\overline U_\varepsilon)\le27.
\tag{S12}
\]

置 m=Dε/Pp、d=degPp≤5。逐次 Euler 微分给

\[
\theta^jm=Q_j/P_p^{j+1},
\qquad\deg Q_j\le5+jd\quad(0\le j\le3).
\tag{S13}
\]

将 (S9) 左乘 BεPp⁴，全部 order≤4 的系数和 forcing 都成为多项式。因为每项 θʲm 的 numerator 再乘 Pp^(3−j) 后的次数≤5+3d，得到

\[
\boxed{\deg\{
\text{全部 polynomial operator coefficients 与 forcing}\}
\le27+\max(5+3d,4d)\le47.}
\tag{S14}
\]

最高 θ⁴ 系数为 BεDεPp³，其常数项 Pp(0)³ 是好 place 的 unit。故该慢变量 polynomial 行本身 primitive；这不能代替快变量实际整格中的 content 分析。未使用素数样本拟合 degree，也没有把某个 p 的多项式截断冒充 (S14)。

## 4. 为什么这条方程仍没有新的积分坐标

直接展开左侧算子，

\[
E_\varepsilon\circ M_m\circ\theta
=m\theta^4+(3\theta m+b_2m)\theta^3
 +(3\theta^2m+2b_2\theta m+b_1m)\theta^2
\]
\[
\hspace{15mm}
 +(\theta^3m+b_2\theta^2m+b_1\theta m+b_0m)\theta.
\tag{S15}
\]

zeroth Xi coefficient 恰为0。这是精确右因子 θ；左乘任何清分母都不改变它。

用 s=t(q(t)^p)、b=S(s)/S(t) 记 exact Frobenius pullback，已有

\[
\theta_ts=psb,\qquad
\theta_s=(pb)^{-1}\theta_t.
\tag{S16}
\]

(S15) 的最右 θs 因而替换为 (pb)⁻¹θt；所有 product-rule 项只改变其左侧系数，不能产生 zeroth Z 项。于是任何由这条复合 ODE 拉回并清左分母得到的行，仍以 θt 为右因子。

在实际 rank5 source 中有精确关系

\[
\theta_t Z=pY-p^4H_0,
\quad\theta_t^2Z=p\theta_tY,
\quad\theta_t^3Z=p\theta_t^2Y.
\tag{S17}
\]

再用原始 Euler 模型消去 θt³Y，所有 order4 项都回到 constant 与三个 H jets。沿实际 pole-clearing gauge g=Δ² 清掉 rational coefficient 后，这仍是 constant、gH、gθH、gθ²H 四个旧坐标；I_H 坐标严格为0。

因此，(S9) 本身不能给一个在新增 integral 坐标上非零的 primitive S3 输入。它也不能仅凭形式上的 order4 被计为第四个独立方向。旧行在 p⁴ 缩放中本来的 baseline shift 必须保留。

这并不证明任何纯 H special-packet S3 行都不存在：所得旧坐标行的实际 valuation、独立性仍可能需要研究。它也不排除具有非零 zeroth Z coefficient 的不同混合方程。本节排除的严格范围只是「先用 (S6) 消去载体，再将 (S9) 直接拉回」所自动声称的新 integral-coordinate 收益。

## 5. 模 p 身份不能经慢微分自动升级到 S3

(S8)、(S4) 只确定 Z 的 mod p 前缀。写 Z=J(s)+pE(t)，其中 E 的前缀 integral。运用 θs=(pb)⁻¹θt 时，误差 pE 的一个慢微分已可能变成 b⁻¹θtE，不再带 p；迭代三、四次更加不能保留未经证明的 p³。

若先清掉所有 p 分母，所得 primitive content 又必须重新除去。不能同时保留「慢导数的额外 p」和「原始 polynomial 行的 primitive 性」这两个相互冲突的记账。固定次数≤47 并不补足未知的模 p²/p³ lift。

特别是 full-formal universal W 的已知 S2/S3 排除与这里的 actual degree<p source 是两个不同对象。本稿没有将 universal 排除套到 actual packet，也没有以有限 leading rows 的 kernel 代替完整 prefix 的消除条件。

## 6. 更强的 zeroth 耦合条件，以及 char0 层的确定障碍

可以把下一问题从反复微分改写为实际 de Rham exactness。对每个 ε，在 char0 考虑

\[
W_{K,\varepsilon}=\operatorname{span}_{K(t)}
 (1,K_\varepsilon,\theta K_\varepsilon,\theta^2K_\varepsilon).
\tag{S18}
\]

(S6) 与 Ubar≠0 给 closed rank≤4；模型已证的 cusp log³ 在加减 homogeneous A 时仍存在，故实际 rank=4。这里的 W_K 不被认定为 W_H 的同一实际函数子空间；两个不同平移必须分别解释，不能免费增加 A 方向。

若要把 Xi_p 写成上述四个实际函数的 rational combination，设

\[
\Xi_p=r_0+r_1K_\varepsilon+r_2\theta K_\varepsilon
             +r_3\theta^2K_\varepsilon,
\qquad r_i\in K(t).
\tag{S19}
\]

由实际 rank4 与 (S6)，θXi=R_pK 的充分必要条件是下列固定四方程，另要求候选表达式在原点全纯、值为0：

\[
\theta r_0+\overline U_\varepsilon r_3=0,
\qquad\theta r_1-b_0r_3=R_p,
\]
\[
r_1+\theta r_2-b_1r_3=0,
\qquad r_2+\theta r_3-b_2r_3=0.
\tag{S20}
\]

它是一个具体的 rational integration 问题，包含 constant forcing，也保留实际 R_p。同期新增的 [实际 cohomology 证明 §2–4](cdt_odd_level20_cartier_cohomology_20261006.md) 已对整个六维空间 R=P/Dε、degP≤5 证明：每个非零 R 在 char0 的实际 rank4 模内都 non-exact。故 (S20) 在 char0 没有满足 (S19) 的 rational 解；并不需要只试有限次数的 ansatz。这是比单纯右因子更强的 char0 障碍。

其证明从实际 G、G′、G″ 的匹配得到 −L3,ε* b=R/t。所有 rational b 必须在0、1各有至少二阶零、四个 Δ 根各有至少一阶零、N 的两个根最多有简单极点，迫使∞growth≥6；而 adjoint 在∞的首系数是 −(d−2)³，右边 O(t⁻¹) 迫 growth≤2。这个真实 local-divisor 矛盾同时适用于 Kε 与正规 H primitive。本文只读独立核对了该稿 §2–4，不把它的共同叶或分母预算一并纳入本稿的新审阅范围。

root 正在另稿证明实际 Hecke 源的三维全 p 结构；[固定 Hecke 证书](cdt_odd_level20_hecke_space_20261006.json) 的有限好素数与 Krylov rank 不在本稿中充当其全素数证明。即使缩到三维，其 char0 类仍由上述六维 injectivity 保持 non-exact；缩维的作用是使实际模 p 问题具有固定有限输入，不能自动改变这一 char0 障碍。

在 mod p 的实际截断 source 上，(S20) 型 module 身份仍是安全的充分输入；char0 的必要性与无解不能直接变成实际 mod p 有限 jet 的必要性或无解。若模 p 中取得随 p 改变的 rational 解，还必须证明：其次数与 poles 在全 p 下可控；原点积分常数正确；slow jets 可由 fast target 的实际高层 packet 实现；lift 至所需 p 层后有非零 I_H 坐标；清分母与除共同 content 后仍 primitive；实际 leading minor 上的 Smith threshold 超过原 baseline。本文没有证明这些额外条件。

## 7. 核验及明确未完成之处

本稿的 (S6)、(S9)、(S14)、(S15) 是全尺度代数证明。[配套最小 symbolic 脚本](cdt_odd_level20_cartier_source_elimination_20261006_verify.py) 与 [JSON](cdt_odd_level20_cartier_source_elimination_20261006_verify.json) 新执行62项检查，只核 Euler gauge 展开、复合乘法算子、rational exactness 系数匹配与原点/次数的形式上界，不计算新的 Hecke 素数，不执行冻结 producer，不把样本当成 all-p identity。

low_period_closure 已独立复核 (S6)、(S9) 的算子顺序、right-factor pullback、实际 (S17) 消元后 I_H 坐标为0，以及 mod p 不能通过除 p 的慢微分升级到 S3；该消息审阅未覆盖 degree47 细节。root 已对实际正文 §1–7 作完整只读独审，通过 Euler 规范、Λ³Δ³清分母、∞次数界、degree47、原点unit、right-factor范围及 char0／modp 区分；两位均未运行本稿 producer。完整 rank5、共同 cover、Cartier fixed divisor/整性与旧 Smith 收益分别沿用此前独立报告，不在此重复声明新证明。

已经得到的是一个有界实际源方程和明确的路线障碍。新增 mixed Cartier primitive S3、其 balanced tensor 接合以及严格 holonomy 矛盾仍未完成。
