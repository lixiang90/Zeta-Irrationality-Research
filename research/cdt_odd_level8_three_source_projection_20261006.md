# Level8 三个真实源：纯 L3 与 Tate-free 周期的精确分离

日期：2026-10-06。本文新增一个比此前 pure-character level32 更低的 level8 目标源；它借助 trivial-character Eisenstein oldforms，故不属于此前 unmixed ansatz。没有证明 L(3,χ8) 无理。下述有限线性分类覆盖明确的三个源，不能外推为所有 level8 模形式或所有 CDT 实现的界。

## 1. 三个实际模形式及原点常数

采用[完整 D8 嵌入审计](cdt_odd_level8_mixed_embedding_20261006.md)的固定归一化：r=√2，κ=16r，E4 常数为1，Eχ8 常数为11/2，Fχ8 常数为0。令

\[
 G_1=E_4(τ)-64E_4(8τ),\quad
 G_2=E_4(2τ)-4E_4(4τ),\quad
 C_-=E_χ-κF_χ,
 \quad C_+=E_χ+κF_χ.
 \tag{A1}
\]

G1、G2 属于 M4(Γ0(8))，C± 属于 M4(Γ0(8),χ8)。在 Γ=kerχ8 上它们是同一 level8 的实际 weight4 sources。归一化 Fricke 满足

\[
 E_4(jτ)|W_8=64j^{-4}E_4((8/j)τ),\quad
 E_χ|W_8=κF_χ,\quad F_χ|W_8=κ^{-1}E_χ.
\]

故 G1、G2、C− 都是 W8-anti，C+ 为 W8-plus。对 a,b,d∈Q 取

\[
 F_-=aG_1+bG_2+dC_-,\quad F_σ=aG_1+bG_2+dC_+.
 \tag{A2}
\]

它们的 ∞ 常数均为 −63a−3b+11d/2。因此 q 全纯的三次 primitive f−、fσ 具有真正 modular source 的充要条件是

\[
 d=(126a+6b)/11.
 \tag{A3}
\]

以下始终保留 A3，primitive 取 f(0)=0，不先删去一个非零常数再冒称三次导数是模形式。

## 2. 原始周期和共轭 lift 的完整端点

divisor sums 的 Dirichlet 级数以及同一 Mellin identity 给

\[
 L(G_1,3)=-105ζ(3),\quad L(G_2,3)=-15ζ(3)/2,
 \quad L(C_-,3)=8rL(3,χ_8),\quad L(C_+,3)=-8rL(3,χ_8).
 \tag{A4}
\]

每个 W-anti 部分的中间 L2 为0。A3 又使两端常数消去，所以

\[
 f_-+8τ^2f_-(W_8τ)=ξ(1+8τ^2),
\]
\[
 ξ=Aζ(3)+8rdL(3,χ_8),\qquad A=-105a-15b/2.
 \tag{A5}
\]

系数 σ 只作用 r↦−r，不对 ζ3/L3 作作用。取冻结稿中的 γ=(3,1;8,3)，M=γW8。由于 χ8(3)=−1，Fσ|M=−Fσ。A3 给 ∞ 与 M∞=1/3 的常数0，故完整 Bol/Eichler cocycle 是

\[
 f_σ+R_Mf_σ=λ_M q_M,
 \quad R_Mh=(24τ-8)^2h(Mτ)/8,
 \quad q_M=1+8(3τ-1)^2.
 \tag{A6}
\]

没有独立的一次项：M²=−8I 的 weight−2 polynomial +1 eigenspace 是一维。

令 T(q)=Σ q^n/[n³(1−q^n)]，ρ=exp(2πi/3)。三个 primitives 是

\[
 g_1=240T(q)-30T(q^8),\quad
 g_2=30T(q^2)-15T(q^4),\quad
 c_+=e_χ(q)+κT_χ(q),
 \tag{A7}
\]

其中 eχ 为 Eχ 的去常数三次 primitive，Tχ=Σχ8(n)q^n/[n³(1−q^n)]。这些公式直接由 divisor sums 得到。

冻结的实际 radial finite-parts 给 T(ρ)=−ζ3/2+2iπ³/243、eχ(ρ)=4iπ³/81、κTχ(ρ)=−8rL3χ8+23iπ³/108。由此三源的 imaginary π³ 系数为

\[
 20/9,\quad -10/27,\quad 85/324.
\]

divergent 1/ε 系数以 ζ4/(81ε) 为单位分别为945/4、45/4、−165/8，其 a,b,d 组合由 A3 恒为0。这是整个实际 radial limit，不是只取某个形式 finite part。于是

\[
 \boxed{λ_M=ψ+iπ^3 C,\quad
 ψ=Aζ(3)-8rdL(3,χ_8),\quad C=(115a-5b)/22.}
 \tag{A8}
\]

## 3. 一个新的低层数 pure-L3 入口

令 a=1,b=−14,d=42/11。A3 成立且 A=0，因此

\[
 F_-^{pure}=G_1-14G_2+\frac{42}{11}C_-,\quad
 ξ=\frac{336}{11}\sqrt2\,L(3,χ_8).
 \tag{A9}
\]

这个 source 在 level8 已完成 ∞constant、中间 L2 与 ζ3 contamination 的实际消去。其 q 系数乘11后在 Z[√2]，三次 primitive 以11·lcm(1,…,n)³安全整数化。所有 q 系数的理由是 divisor sums；这不是从有限 jet 猜分母。

若待反证的 L3χ8∈Q，ξ∈K且 σξ=−ξ 是合法的代数数域共轭。此时共轭 lift 的真实周期为

\[
 \boxed{λ_M=-ξ+\frac{185}{22}iπ^3.}
 \tag{A10}
\]

因此这一模型只留下明确 Tate 周期障碍，已消除此前 ξ/ψ 的 ζ3 trace mismatch。它仍不能用一个 scalar modular prefactor 直接下降 M 的二次商：冻结稿的 T-periodic 论证对 λM≠σξ 同样适用。

可取 rational weight2 prefactor B0=E2(τ)−8E2(8τ)，它在 Γ0(8) 为 W8-anti。因此 B0(f−−ξ) 在原 W8 的实际 canonical α 下降。第二 embedding 必须另处理 A10：例如合法的 ramified map、加入额外真实源或周期 projection。实际 t-holonomic 模型、两 embedding 完整叶、成本与严格 holonomy 余量尚未构造。不能把上述安全 q 分母直接当作已完成 t 整模型。

## 4. 一个 Tate-free 的混合目标及兼容性限制

令 a=1,b=23,d=24。它给

\[
 ξ=-\frac32\{185ζ(3)-128\sqrt2L(3,χ_8)\},\quad C=0.
 \tag{A11}
\]

这次 M 的真正端点无 π³ 项。但 ξ+ψ=−555ζ3。若假 ξ∈K 且又将 ψ 设为 σξ，则 TraceK/Q(ξ)=−555ζ3∈Q，与 Apéry 的已知 ζ3 无理性矛盾。因此，即使去掉 Tate 部分，ψ也不能成为该假定代数ξ的共轭。若只假 ξ∈Q，则 ψ=−ξ−555ζ3 无理；没有这里的假设时不声称 ψ 无理。

“pure-L3”和“Tate-free”在此明确三源 family 中不能同时实现非零源：在 A3 下的两条件矩阵为

\[
 \begin{pmatrix}-105&-15/2\\115/22&-5/22\end{pmatrix},
 \qquad\det=2775/44\ne0.
 \tag{A12}
\]

故 A=0=C 强制 a=b=d=0。A12只分类 A1，不排其它 level8 cusp forms、不同 Fricke lifts、更高 level 或额外独立 primitives。它也指出下一个正接口应增加一个有独立 Tate coefficient 的实际源，而不是在这两个自由参数上继续搜寻。

## 5. 算术范围与新证书

同名 NEW [_verify.py](cdt_odd_level8_three_source_projection_20261006_verify.py)/[JSON](cdt_odd_level8_three_source_projection_20261006_verify.json) 只核本次预先指定 family 的精确 Fricke、constant、critical finite-parts线性系数、divergence cancellation和两点投影；不执行旧 producer、不扫 primes/参数。全 coefficient integerization、Mellin/Bol 与 actual endpoint convergence 由正文和冻结原件证明承担。尚无新的奇数 ζ/L 数值无理性定理，也不以 A11 这个新候选取代原目标。
