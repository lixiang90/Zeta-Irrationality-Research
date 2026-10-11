# 完整 F 的全素数幂分母与两层原格 packet

日期：2026-10-06。NEW 全尺度证明；冻结数学稿只读，没有执行/import 旧或同行 producer。本稿保留真实 forcing 与实际 rank10，证明原 ζ(7) 源的 odd-prime 安全列可从11减到8，并在完整五条 F 行上给最高 filtration 的两层原格关系。数值无理性、Lean 验证均未得到。

## 1. 实际源、forcing 及坐标

实际读取了[完整 rank10 稿](cdt_odd_classical_zeta7_full_rank_20261006.md)、[forcing 稿](cdt_odd_classical_zeta7_forcing_20261006.md)和[经典投影稿](cdt_odd_classical_derivative_projection_20261006.md)正文。准确 forcing 是

\[
K H=16x,\quad K=(\theta+1/2)^4-x\theta^4,
\]
\[
L_5F=960x-\tfrac32x\theta^2P_3(\theta)H,
\quad P_3=48\theta^3+80\theta^2+40\theta+5,
\]
\[
L_5=\theta^5-\frac{x}{8}(2\theta+1)
(8\theta^4+16\theta^3+20\theta^2+12\theta+3)
+x^2(\theta+1)^5.
\tag{F1}
\]

960x 不是960/x。设 F(x)=Σfₙxⁿ，其中 fₙ=(Cₙ,₂+cAₙ)/256ⁿ；真目标 c=91440ζ(7)。谈 p-adic valuation 时只在反证假设 ζ(7)∈Q 下使用同一实际 F，或先固定任意 c∈Q。固定初始分母并入 D₀；p∤D₀。其真实微分秩仍为10，forcing 不被当作齐次免费背景。

CDT 原整数 polynomial source 使用原 z 坐标 x=256z：F_z(z)=F(256z)、H_z(z)=H(256z)，θ=z∂z=x∂x。对 odd p，256是 unit，局部 packet、degree 和 valuation 原封保留。本文的全局低 dyadic 费用只在原 z source 中成立；native x 的坐标分母另须全额计费。

## 2. 所有 odd 素数幂的8列安全模型

沿用经典投影稿 V3：

\[
C_{n,2}=-\sum_{i=1}^4\sum_{k=0}^n(i)_4r_{n,i,k}
\sum_{\ell=1}^k(\ell-1/2)^{-i-4}.
\tag{F2}
\]

用该稿 V12 的分解 Rₙ=(2t+n)\mathcal Aₙ(t)^4\mathcal Bₙ(t)^4，

\[
\mathcal A_n(t)=4^n(t+1/2)_n/n!,\qquad
\mathcal B_n(t)=n!/(t)_{n+1},\qquad
\mathcal B_{n,k}=(t+k)\mathcal B_n.
\]

rₙ,ᵢ,ₖ 是 (2t+n)\mathcal Aₙ⁴\mathcal Bₙ,ₖ⁴ 在 t=−k 的 j=4−i 阶 Taylor coefficient。固定 odd p，a=⌊log_p n⌋，b=⌊log_p(2n)⌋；n=0单独整。因为 p≥3，有 b−a∈{0,1}。

独立计数低层：\mathcal Aₙ⁴ 的一个 u 阶 Taylor monomial从四份连续长度 n 的进程中删除合计 u 因子；每层 q=pˢ≤n 原分子至少4⌊n/q⌋个 q 因子，n!⁴分母恰有4⌊n/q⌋。所以该层亏损至多 u。\mathcal Bₙ,ₖ⁴ 的 l 阶 Taylor monomial 的额外分母只用非零距离≤n，亏损至多 la；其常数 (±binom(n,k))⁴ p-integral。线性 (2t+n) 的 v 阶（v=0或1）整，u+l+v=j。因而全部低层合计 valuation≥−ja。若某 harmonic summand 的 v_p(ℓ−1/2)≤a，将它相乘给

\[
v_p\big(r_{n,i,k}(\ell-1/2)^{-i-4}\big)
\ge-[(4-i)+(i+4)]a=-8a.
\tag{F3}
\]

只剩 b=a+1 且 harmonic 真命中 q=pᵇ>n 的情况。2ℓ−1≤2n−1<2q，命中必是 2ℓ−1=q，故 k≥ℓ=(q+1)/2。在 \mathcal Aₙ(−k+u) 的分子进程，序号 m=k−(q+1)/2 位于0,…,n−1，其常数因子为−q/2。四份 \mathcal Aₙ 中这个高层因子出现四次；u 阶 Taylor 删除至多 u 份，q层还余至少4−u≥i个。该层在 n! 或 \mathcal Bₙ,ₖ 的距离分母中不出现。因此

\[
v_p(r_{n,i,k})\ge-(4-i)a+i,
\]
\[
v_p\big(r_{n,i,k}(\ell-1/2)^{-i-4}\big)
\ge-(4-i)a+i-(i+4)(a+1)=-8a-4.
\tag{F4}
\]

低层计数与顶层计数是在同一个整数乘积 monomial 上逐层相加；并未对一个已求和 Taylor coefficient 不合法地再分层估价。所有 monomials、k、i、ℓ 均满足相同最终下界，故其和 F2 也满足。整系数 (i)₄只增加 valuation。得到完整 all-p-power 安全模型

\[
\boxed{v_p(C_{n,2})\ge-4\lfloor\log_p n\rfloor
-4\lfloor\log_p(2n)\rfloor\quad(p\text{ odd}).}
\tag{F5}
\]

Aₙ是已证整数，c 固定有理，因此 p∤D₀ 时同一结论适用 Cₙ,₂+cAₙ 及全部四阶 Euler derivatives。故 odd part 的 Δₙ⁴Δ₂ₙ⁴足够清分母，所需 F positive columns 从旧3个 b=1 加8个 b≈2，改为4个 b=1 加4个 b≈2。这里给安全上界，没有主张 F 的最小公共分母已精确求出。

原 z 的2处仍用旧 V13 的 Δₙ³Δ₂ₙ⁸安全界：固定前缀的2-adic清数 log=O(logN)。它连同 D₀ 是逐 source/graded evaluation 的低阶费用，累计 O(DlogD)=o(D²)，fixed tensor 后同样低于 Dᵈ⁺¹。没有将 native x 中除256ⁿ的 dyadic 主项删除。

## 3. 完整 F 的最高层全 prefix block

固定 odd p∤D₀，全部 0≤n<N 的 prefix 要求 p²>2N+1。F5 给 U=p⁸F 在整个 prefix p-integral；H的已证全层 bound给 p⁴H p-integral。于是实际 F1 严格给

\[
L_5U\equiv0\pmod{p^4,x^N}.
\tag{F6}
\]

此处只将低 valuation forcing 保留为 p⁴误差，没有改变实际完整源或 rank。

记 Q(X)=8X⁴+16X³+20X²+12X+3。定义 rational functions tⱼ(ρ) 由 t₋₁=0、t₀=1及 j≥1 的准确 Frobenius recurrence

\[
(j+\rho)^5t_j(\rho)
=\tfrac18(2j-1+2\rho)Q(j-1+\rho)t_{j-1}(\rho)
-(j-1+\rho)^5t_{j-2}(\rho).
\tag{F7}
\]

对0≤j≤d=p−1，它们在ρ=0的值及一阶参数导数都 p-integral，因为所用全部 j<p 的 leading denominators 是 p-units。tⱼ(0)=Aⱼ/256ʲ由同一 initial t₀=1、t₁=3/8 和递推确定。置

\[
T(x)=\sum_{j=0}^{p-1}t_j(0)x^j,
\quad V(x)=\sum_{j=0}^{p-1}t'_j(0)x^j.
\tag{F8}
\]

T₀=1、V₀=0，degree≤d；不要求最高 A_(p−1) 系数为 unit。

现在逐实际 block n=kp,…,kp+p−1 取 wₖ=Uₖₚ。对j=1，来自前一 block 的系数 (kp)⁵U_(kp−1) 在modp²为0；forcing也在p⁴。对1≤j<p，(kp+j)⁵为 unit，故递推归纳给

\[
U_{kp+j}\equiv w_kt_j(kp)
\equiv w_k\{t_j(0)+kp\,t'_j(0)\}\pmod{p^2}.
\tag{F9}
\]

无需除 wₖ或假定它 unit。k=0的 initial coefficient也由 F6 正确覆盖。归纳不跨过 j=p 的非unit除数，因此没有把边界关系错误延拓为一个 uniform rational quotient。以 s=xᵖ、W(s)=Σwₖsᵏ 写完整 prefix 为

\[
\boxed{U\equiv T(x)W(x^p)+pV(x)\theta_sW(s)
\pmod{p^2,x^N}.}
\tag{F10}
\]

最后 block 可正常截断。所有未知真实 initial/connection 信息完整地留在 wₖ中；没有引入免费齐次 five-dimensional background。F10 用给定 recurrence 覆盖全部 n<N，不是原文某个 p项 endpoint truncation 同余。

## 4. 实际五条 F 行的两层 polynomial relations

令 B=TθV−VθT、Q_T=T²+B；Q_T(0)=1，degree B≤2d−1、degree Q_T≤2d。T 与 Q_T 均 formal p-adic units。置 α=θT/T、β=B/T。F10 的快慢导数严格给

\[
(\theta-\alpha)U\equiv p(T+\beta)\theta_sW\pmod{p^2},
\]

再以 α₂=θQ_T/Q_T−θT/T 作用 θ−α₂，所有慢导数贡献 p²，便有 (θ−α₂)(θ−α)U=0modp²。这里慢导数没有常数偏移；故旧 H 模型的 p/2 correction 在此确实为0，而非被遗漏。

清 Q_TT 后的实际 rows 是

\[
\mathcal M_1=T\theta-\theta T,
\]
\[
\begin{aligned}
\mathcal M_2&=P_2\theta^2+P_1\theta+P_0,\\
P_2&=Q_TT,\quad P_1=-(\theta Q_T)T,\\
P_0&=(\theta Q_T)(\theta T)-Q_T\theta^2T.
\end{aligned}
\tag{F11}
\]

degree≤d、3d，且

\[
\mathcal M_1U\equiv0\pmod{p,x^N},\qquad
\mathcal M_2U\equiv0\pmod{p^2,x^N},
\]
\[
\mathcal M_2=(Q_T\theta-\theta Q_T)\mathcal M_1.
\tag{F12}
\]

最后身份在 polynomial Ore ring 中精确成立；它不使 \mathcal M₁ 的 image 自动提高到p²。\mathcal M₁ 的 left Euler derivatives 到 θ³\mathcal M₁ 的 order至多4；\mathcal M₂ 到 θ²\mathcal M₂ 的 order也至多4。因此全部 rows 支持原五条 (F,θF,…,θ⁴F)，不增加第六条函数。

在原次数≤D source，分别乘 degree≤D−d、D−3d 的 polynomials。按最高 derivative coefficient T、Q_TT 的非零 modp 值依次比较，得到 primitive modp ranks

\[
\boxed{k_{F,1}=4(D-p+2)_+,\qquad
k_{F,2}=3(D-3p+4)_+.}
\tag{F13}
\]

第二层 families 的 modp span 位于第一层：left derivatives of F12 的 multipliers degree≤2d，乘 degree≤D−3d 后仍处第一层 degree≤D−d。此为两个 Smith 阈值，而不是7个额外独立普通 kernel。

## 5. 同一 rank10 格上的可用 floor 账本

在原 z source E_D=⊕_(i=1)^10 Z[z]_(≤D)fᵢ 中，f=(1,H_z,…,θ³H_z,F_z,…,θ⁴F_z)，真实 leading prefix N_D=10(D+1)+O(1)。新 odd 表的 maximal cap为8，Ψₚ=p⁸eval。constant方向 floor8，四条 H方向 floor4，五条 F方向 floor0，baseline floor和为24(D+1)。H原两层关系在第5/6阈值继续提供 k_H,1、k_H,2；F13在第1/2阈值提供 k_F,1、k_F,2。三种 supports分离，nested relations各自保留，因此 capped floor和至少

\[
24(D+1)+k_{H,1}+k_{H,2}+k_{F,1}+k_{F,2}.
\tag{F14}
\]

这不是在旧11列表又同时加3层 baseline 的双计数；8列新安全表与 cap8一并改变。H的两层信用复用[已冻原格证明](cdt_odd_classical_frobenius_smith_20261006.md)，本稿新的信用只来自实际完整 F 行。

其 prime degree-loss积分为 γ_F=4∫₀¹(1−t)dt+3∫₀¹⁄³(1−3t)dt=5/2；与已证 γ_H=11/3 合计 γ=37/6。这个数字只是原 one-variable floor 累计 Σk logp 的 D²系数。必须另外把8列新表的 maximum transport、matching窗口、primitive balanced tensor、HS/arch 归一化逐项接合，才可报告最终 CDT cost。

## 6. 准确新增进展与限制

本稿完成的正输入是：所有 odd primes/全部幂层的 F5，实际完整 F 的 whole-prefix F10，两层原五条 derivative supports 的 F11–F13及同一 rank10 格的 F14。没有删除 forcing，没有将 p-adic unit-root 概念替代 whole-prefix 原格同余，也没有通过换一个 arch-未计费的全局 p-dependent basis 报收益。

新表可能显著改善旧安全费用；但是本文尚未认领新表的最终 τ/κ，没有扩大共同解析叶，也没有证明实际F的最小公共分母、第三及第四Smith层或数值无理性。native-x的dyadic主项尤其不能凭 original-z 的 O(logN) 清数结论忽略。

本文为纯全尺度证明，未执行数学 producer。读到的冻结输入范围为上述三篇全文与原 H Frobenius/Smith 全文；独立审阅和有限证书若后续新增须准确另记，不把本文的手推证明声称为已由 Lean 验证。
