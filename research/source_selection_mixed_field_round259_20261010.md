# 第259轮：唯一 mixed χ−3/χ−4 来源的完整场与半平移降场

2026-10-10；field 子任务，纯纸面证明，数学程序0。唯一候选始终为 CDT 的 A=A₃、B=B₃、C=C₃ 与 B₄=Σχ−4(n)qⁿ/[n²(1+qⁿ)]，目标数值行 (1,L(2,χ−3)/2,ζ(2)/4,G/2)。本稿没有改变 filter、character 或目标，没有新数值定理。

核心结果：表面的共同 level 是24，其 χ12 cover 确是 genus1；但该具体 forcing 具有额外半平移对称，最小 forcing 场实际为 genus0 的 Q(s)，s=q+Z[[q]] 且 q(s)∈sZ[[s]]。给出明确 rational forcing，完整 all-prefix 整模型，并为反证中的单一关系 H 证明实际 bare rank3。完整全纯图、全部返回支路和严格 holonomy 仍待支付；不借 CDT 的14行、旧 τ 或旧 energy。

## F1. 原件、旧资产与去重范围

固定 CDT [arXiv:2408.15403v2](https://arxiv.org/abs/2408.15403v2)，本地218页 PDF；本轮实际读物理159–163、89–90、122–124页。Eisenstein 规范用 Stein 原件物理99–102页，尤其 Theorem5.8；eta character、Ligozat、Sturm 用 Allen 等 [固定v1](https://arxiv.org/abs/1901.10511v1) 的物理1–3页、Theorems1.2、1.4、1.5。本轮保存相关原件/节选于 literature/source_selection_round259_20261010/field_*，准确 scope 另存。

旧 [level12 paired coordinate](cdt_odd_level12_paired_coordinate_20261006.md) 的 §§2–4 本轮实际全文读核，其 genus0 character 参数与全阶整数递推可复用。其 pure L(3,χ12) source、周期、rank4、W/M 叶和停止的预算不移交。本轮也全文读了旧 joint-full-model 与 candidates5/8/12；前者是 ζ3/L3χ12 的 weight4 source，后者的level24 tensor是weight4三重 primitive，均不是当前 weight3 dyadic B₄。固定关键词检查没有识别到本候选已停止的同源证书；这是列明旧文件范围的去重，不是全库或文献首次性声明。

## F2. 实际 level、Eisenstein source 和两个 eta 恒等式

令 δ=q d/dq，χ₃=χ−3，χ₄=χ−4，χ12=χ₃χ₄。采用

\[
 E_{k,α,β}=c_0+\sum_{n\ge1}\sum_{d\mid n}α(n/d)β(d)d^{k-1}q^n,
 \quad c_0=0\ (\operatorname{cond}α>1).
\]

直接逐项微分 dyadic Lambert series 得

\[
 f_4:=δ^2B_4=E_{3,χ_4,1}(τ)-8E_{3,χ_4,1}(2τ)
 \in M_3(Γ_0(8),χ_4).                                      \tag{F2.1}
\]

A∈M₁(Γ₀(6),χ₃)。所以普通共同群为 Γ₀(24)，不能把 lcm(3,4) 当成12；dyadic scale 必须计入。以下 eta identities 有完整证明：

\[
 A=\frac{η_2^6η_3}{η_1^3η_6^2},\qquad
 f_4=\frac{η_1^4η_4^8}{η_2^6},\qquad
 h:=\frac{f_4}{A^3}=\frac{η_1^{13}η_4^8η_6^6}{η_2^{24}η_3^3}.       \tag{F2.2}
\]

对 A 的 eta 式，指数和2，两 Newman 和为0、0，character由 (−16/3,d) 得 χ₃；在 Γ₀(6) 的 cusp denominators1,2,3,6，Ligozat orders依次0,1,0,0。它是 holomorphic form，constant、q项为1、3，与 A 相同；weight1、index12 的 Sturm bound为1，差的起始order至少2迫恒零。

对 f₄ 的 eta 式，指数和6，两和24、24，character由 (−2¹⁰,d) 得 χ₄；Γ₀(8) 的 denominators1,2,4,8，orders依次1,0,1,1。它是 holomorphic form，前四系数（含constant）为0,1,−4,8。F2.1 直接 divisor sums 给同样0,1,−4,8。weight3、index12 的 Sturm bound为3，故差的起始order至少4迫恒零。这里是三个固定系数的纸面 Sturm 证明，不是执行有限头拟合或 scan。

h 的 weight0，level24两和24、72，character χ12；q-leading1，h∈qZ[[q]]。A 的 reciprocal 是 formal integer unit，所以这也直接由 f₄/A³ 的全阶整数性得到。η在上半平面无零，所有三式均无内部零极。

## F3. 表面完整模场：degree8 和 genus1 都确实付清

固定 CDT 的底参数

\[
 t=x_6=\frac{η_1^4η_6^8}{η_2^8η_3^4}=q+Z[[q]],\qquad q(t)\in tZ[[t]].
\]

Γ₀(6)的PSL index12，Γ₀(24) index48。令 j₂₄=j(24τ)。在 Γ₀(6) 中，j₂₄ 的 generic stabilizer恰 Γ₀(24)：j(24γτ)=j(24τ) 导致 diag(24,1)γdiag(1/24,1)∈±SL₂(Z)，亦即24|c。对一个开集等式，涉及的 SL₂(Z) 元素由离散性为同一元素；反向显然。因此

\[
 F_0=Q(t,j_{24})=Q(X_0(24)),\qquad [F_0:Q(t)]=4.
\]

Q下降由各函数的 rational q-expansion 和 t 所指 rational cusp，亦可在modular-function Galois closure中以实际 stabilizer直接取 fixed field。v=t²⁴j₂₄∈Z[[t]]，故1,v,v²,v³是四条 integer field basis。

取 E=kerχ12∩Γ₀(24)。矩阵 (5,1;24,5) 的 χ12(5)=−1，h非零，故

\[
 F=F_0(h)=Q(X(E)),\quad[F:F_0]=2,\quad[F:Q(t)]=8.                \tag{F3.1}
\]

八条真正 independent 且全部 Z[[t]] 的完整背景可取

\[
 1,v,v^2,v^3,h,vh,v^2h,v^3h.                                  \tag{F3.2}
\]

Γ₀(24)无elliptic points。完整 cusp widths及 lower-right parabolic entries为

|c|1|2|3|4|6|8|12|24|
|---|---:|---:|---:|---:|---:|---:|---:|---:|
|width|24|6|8|3|2|3|1|1|
|1+cw|25|13|25|13|13|25|13|25|

八个 character都+1，所以 E doublecover 在所有 cusp和内部均不分歧。Γ₀(24) 的genus=1+48/12−8/2=1；E有index96、16 cusps、genus=1。同样不能仅因 genus1 断言其图或本方法失败。以下更便宜的具体 forcing 对称说明完整 F3.1 不是本对象的最低场费用。

## F4. 唯一 cusp0 的完整 odd germ 支付额外 γ12 作用

mixed 子任务从固定218稿的实际 reciprocity 证明了：w=−1/(24τ)，q₀=e²πⁱʷ，

\[
 T(w)=θ_{-3}(8w)+\tfrac12θ_{-3}(4w),\quad
 C_4(w)=\frac{π^2}8-2D(q_0^3)+\tfrac12D(q_0^6),
\]
\[
 D(r)=\sum_{m\ge1}\frac{r^m}{m^2(1+r^{2m})},\quad
 B_4-G/2=iτC_4(w),\quad A=\frac{iT(w)}{2\sqrt3τ}.                 \tag{F4.1}
\]

本 field 稿不继承 mixed 的未读原文 FULL；这里独核 F4.1 之后的场论链。D 的偶数系数是其半index系数的1/4，因为展开的 multipliers 2k+1 都 odd。因此 −2D(r)+D(r²)/2 仅有 odd powers，constant π²/8 不影响 δ_w²。直接两次 chain rule 得

\[
 h=-\frac{\sqrt3}{24}\frac{δ_w^2 C_4(w)}{T(w)^3}
   =\frac{2\sqrt3}9q_0^3+\cdots.                              \tag{F4.2}
\]

T 只含 q₀⁴ powers，T(0)=3/2。故完整 h(−q₀)=−h(q₀)，不是最高项近似。γ12=(1,0;12,1) 把 w 送 w−1/2，遂

\[
 h(γ_{12}τ)=-h(τ).                                           \tag{F4.3}
\]

初始 cusp 邻域的恒等式由 analytic continuation/identity theorem 延及 H。Γ₀(24)在Γ₀(12)中index2，γ12处在非平凡coset，因此二者生成Γ₀(12)。F2.2 在前一群的 χ12 作用和 F4.3 完整确定在后一群的 character

\[
 ψ(γ)=χ_{12}(d)(-1)^{c/12},\qquad γ\in Γ_0(12).                \tag{F4.4}
\]

ψ的确是 homomorphism：c_product/12≡c₁/12+c₂/12 (mod2)，因为 a₂,d₁ odd；d_product≡d₁d₂ (mod12)。ψ(−I)=1。

## F5. 精确半平移共轭；真正 genus0 native 整坐标

记 Γ12=kerχ12⊂Γ₀(12)，P=(1,1/2;0,1)。对 c=12k，

\[
 PγP^{-1}=\begin{pmatrix}a+c/2&b+(d-a)/2-c/4\\c&d-c/2\end{pmatrix}\in Γ_0(12).
\]

全部项整数，det1，反向 P⁻¹ 同样正规化Γ₀(12)。在 units mod12上，χ12(d−6k)=χ12(d)(−1)ᵏ，故

\[
 Γ_ψ:=\kerψ=P^{-1}Γ_{12}P.                                  \tag{F5.1}
\]

旧已付 character 参数为

\[
 h_{12}=\frac{η_1^3η_4η_6^2}{η_2^2η_3η_{12}^3},\quad
 v_{12}^2=(h_{12}+6)/(h_{12}+2),\quad v_{12}(∞)=1,
\]
\[
 u=(v_{12}-1)/2,
 \quad x_{12}=1/h_{12}=\frac{u(1+u)}{1-2u-2u^2},
 \quad Q(X(Γ_{12}))=Q(u).                                   \tag{F5.2}
\]

其实际 branch characters由全部 cusp loops确定，不是只取一个 formal root。新的唯一坐标为

\[
 \boxed{s=-u(τ+1/2)=-u(-q)=(1-v_{12}(τ+1/2))/2.}              \tag{F5.3}
\]

F5.1–F5.2 给 Q(X(Γψ))=Q(s)，不是 genus0 的抽象猜测。x12为leading q整数eta式，F5.2的关系等价

\[
 u+u^2=x_{12}-2x_{12}u-2x_{12}u^2.
\]

每个新系数系数都是1，其他项只用既有整数，所以 u(q)∈qZ[[q]]，leading1；q↦−q、u↦−u不破坏整性。leading1的逐系数反演同样不需除法，因此

\[
 s(q)\in q+q^2Z[[q]],\qquad q(s)\in s+s^2Z[[s]].              \tag{F5.4}
\]

作为交叉校准，Γψ在Γ₀(12)上的cusp characters按c=1,2,3,4,6,12为(−,+,−,+,+,+)：只有0、1/3两个cusps branch，故index48、10cusps、genus0，与明确参数吻合。

## F6. t(s) 的明确 degree4；h 的最低场恰 Q(s)

旧 eta cusp数据给

\[
 t=\frac{x_{12}(1+2x_{12})}{(1+3x_{12})(1+6x_{12})}.
\]

该 identity 的严格证书为：两边在 X₀(12)均只有simple zeros于∞、1/6与simple poles于1/2、1/4；eta无内部零极，ratio constant，leading q coefficient1定constant1。半平移正规化Γ₀(12)，其在x12上的Möbius为−x12/(1+6x12)：它固定∞ cusp（x12=0），交换0与1/2（∞、−1/6），leading sign−确定该式。把 F5.2–F5.3 代入，r=1−2s，得到

\[
 \boxed{t(s)=\frac{1-r^4}{9-r^4}
 =\frac{s(1-s)(1-2s+2s^2)}{(1-s+s^2)(1+2s-2s^2)}.}            \tag{F6.1}
\]

此 degree正好4，无约消，亦等于[Γ₀(6):Γψ]=48/12。其两个branch fibers为s=1/2→t=1/9及s=∞→t=1，两处e4。四个 t=0 fiber为0,1,(1±i)/2，四个 poles为(1±√3)/2、(1±i√3)/2。

h已在Γψ单值，所以 Q(t,h)⊂Q(s)。F4.2 与 t−1/9∼c q₀⁴，c≠0，给 h 的非零leading exponent3/4，local inertia为4；故[Q(t,h):Q(t)]≥4。上界由F6.1为4，所以

\[
 \boxed{Q(t,h)=Q(s),\quad[Q(s):Q(t)]=4.}                      \tag{F6.2}
\]

这对完整 bad germ 的对称有实际含义，不能将表面degree8场强制收作最小费用。F3的 E→Γψ 商degree2；它仍是原completelevel24 character curve，不等于本文forcing的最小compact curve。

## F7. h(s) 的完整 rational identity，非有限头拟合

F2.2的 h 在Γ₀(24)按c=1,2,3,4,6,8,12,24的Ligozat orders为

\[
 (3,-6,1,0,0,0,1,1).                                       \tag{F7.1}
\]

它在 H 内无零极。Γψ→Γ₀(12)的 cusp表与 F5.3给 h 在 P¹s 的完整 divisor：zeros为s=0,1（各1）、1/2（3）、∞（1），poles为(1±√3)/2（各3）。例如Γ₀(24)在c2的width6，而Γψ的相应width3，下降时order−6除e2成为−3；c0的width24和c3的width8已相同，故3、1不改。其余cusp对应(1±i)/2、(1±i√3)/2，order0。

因此相同divisor的 rational expression只差constant；q-leading1以及s-leading1定constant为1：

\[
 \boxed{h(s)=\frac{s(1-s)(1-2s)^3}{(1+2s-2s^2)^3}
          =\frac{2(1-r^2)r^3}{(3-r^2)^3}.}                   \tag{F7.2}
\]

这支付整个 rational forcing，而不是几个 Taylor coefficients。在未shift旧u底上，E→Q(u)degree2且h的γ12 anti作用迫h∉Q(u)，所以Q(u,h)=F；{1,h}给两条完整 integer背景。它是合法但比 F6.2更贵的同对象选择。

## F8. 实际 holonomicity 与三 forcing 都在同一 Q(s)

CDT算子 D_t=p(t)∂t²+p′(t)∂t+3(−1+3t)，p=t(1−t)(1−9t)。实际periodsolution是 A、τA；Wronskian为 A²/(2πi δt)。因为 coefficient p′，p·Wronskian constant；t=q+…、A=1+…定 δt=pA²。chain rule因此给任意 B_j

\[
 D_t(A B_j)=\frac{δ^2B_j}{p A^3}.
\]

故

\[
 D_t A=0,\quad D_t(AB_3)=1,\quad D_t(AC_3)=\frac1{1-t},
 \quad D_t(AB_4)=\frac hp=\frac{(3+r^2)^3}{32r(1+r^2)}.         \tag{F8.1}
\]

把 t(s)完整代入，∂t=(t_s)⁻¹∂s，得到真正 Q(s)[∂s] order2算子及 rational forcing。monic化的 forcing仍在Q(s)，只可能新增有限 rational pole。这是 actual holonomicity，不是把 q-series本身称D-finite。

该homogeneous module在Γψ上的actual solution span为(A,τA)，其monodromy是χ₃ twist的标准二维representation。Γψ是SL₂(Z)有限指数子群；再取kerχ₃仍有限指数，包含两个独立unipotent powers，Zariski closure含SL₂。因此homogeneousmodule over C(s)不可约。有限原点的rational apparent poles不改变该结论。

## F9. 反证中单一 H 的实际最小秩3；不冒称原九germs独立

假设 a+bL₃/2+cζ₂/4+dG/2=0，a,b,c,d∈Q，非平凡，定义

\[
 H=A(a+bB_3+cC_3+dB_4).
\]

已证 CDT三项LI使d≠0。其D_t forcing b+c/(1−t)+dh/p非零，因为h∉Q(t)（F6.2）。F8给导数闭包上界3且1位于闭包。

先证 H∉C(s)，这一点不靠已删除的cusp0 log。若H是rational function of s，则 f=H/A 是Γψ上meromorphic weight−1、characterχ₃的form。Bol身份给 δ²f=bδ²B₃+cδ²C₃+df₄，这是所有cusps都 holomorphic 的 weight3 form（前三来源的modularity在CDT161页）。在整个Γ₀(12)上，f₄的实际character是χ₃(d)ψ(γ)=χ₄(d)(−1)^(c/12)；故在Γψ上它恰为χ₃(d)，这是h不变和A³变换给出的twisted equality。不能将raw Dirichlet equality χ₄(d)=χ₃(d)错误推广到Γψ中不属于Γ₀(8)的元素，例如(5,2;12,5)∈Γψ而χ₄(5)=1、χ₃(5)=−1。

内部若f有pole阶m，δ²增加到m+2，不能被holomorphic source容许。任一 cusp取实际scaling和width，f|-1σ有有限 Laurent expansion；Bol identity将δ² f的slash送到该 expansion 的二阶导数。每个负 Fourier项乘上非零 (n/width)²，故所有负项必须消失。constant项可以存在，但f已是全compact holomorphic negative-weight form，必为0。具体地 y^{−1/2}|f| 在Γψ下不变且在每个cusp趋0；若非零，其正最大值在内部取得，而在f非零处 log|f|−(log y)/2 的Euclidean Laplacian为1/(2y²)>0，严格subharmonic不能在内部取最大。于是forcing0，矛盾。故H∉C(s)。

对 actual derivative closure V，K·1⊂V，V/K·1的非零 cyclic module被不可约order2 homogeneousoperator消去，所以其rank恰2。结合上界得

\[
 \boxed{\dim_{Q(s)}V=3,\quad\{1,H,\vartheta_sH\}\text{实际独立},
 \quad\vartheta_s=s\partial_s.}                            \tag{F9.1}
\]

同样论证对任意固定d≠0的rational coefficient组合成立；不需其数值关系真实存在。该结果只用于反证中的单一H，不主张1,A,A′,AB₃,(AB₃)′,AC₃,(AC₃)′,AB₄,(AB₄)′全部九germs独立。

## F10. 完整 all-N 整模型；原始 type与 conditional holonomy 成本

每个j≤N，B₃/B₄的 coefficient是 Σn|j χ(n)(−1)^{j/n−1}/n²，分母整除d_N²；C₃也是同一bound。A∈Z[[q]]，固定整数C₀清关系系数后，卷积只用index≤N。因此 C₀d_N²[H(q)]_j∈Z。F5.4的integer composition仍只用q-degree≤j≤N，得到

\[
 C_0d_N^2[H(s)]_j\in Z,\quad
 C_0d_N^2[\vartheta_sH(s)]_j\in Z\quad(0\le j\le N).           \tag{F10.1}
\]

所有prime powers均已由literal lcm支付，没有只计square-free primes。θs仅乘j，不加ordinary-derivative index shift。采用实际普通 Taylor tuple (1,C₀H,C₀θsH)，固定scalar不改变rank，常数项也为整数；其真实safe type为两相同列

\[
 b_{\bullet,1}=b_{\bullet,2}=(0,1,1)^t,\qquad e=(0,0,0).
\]

固定 CDT v2 Remark8.0.6（物理123页）对该嵌套unit-column standing型给τflatflat=τflat=Σh(bh−bh·uh²/m²)，uh为每列的zero-prefix长度。这里m3、bh1、uh1、两列，所以τflatflat=2(1−1/9)=16/9；也等于[2(2·2−1)+2(2·3−1)]/3²。e0使τsharp0（Theorem7.0.1后物理90页亦明确此情形）。此表从F10.1直接算出，不从旧χ7或CDT14借值。若未来的解析证书仅需一个fixed rational polynomial清已证有限poles，它只产生有限index shift和fixed scalar，不改变渐近type；若需非polynomial gauge、再增rank或aux primitives，必须重付，本文不预贴费用。

使用的严格形式为固定 CDT v2 Theorem7.0.1、(7.0.3)（物理89–90页；亦Theorem8.0.1、(8.0.3)，物理123页）：φ:(D,0)→(C,0) holomorphic，三个实际普通Taylor芽沿同一φ分别为disk上的meromorphic functions，原Theorem6.0.2其余standing assumptions均满足，且已知holonomic使只需λ=log|φ′(0)|>τ时，m≤J/(λ−τ)，J=∫T²log|φ(z)−φ(w)|。因此rank3严格矛盾要求3(λ−16/9)>J。对这样的holomorphic φ，固定w的Jensen先给∫Tlog|φ(z)−φ(w)|≥log|φ(w)|；再对φ(z)/z用Jensen，得到J≥λ。故必要条件为λ>8/3。此门槛仅对应未加convexity修正的(7.0.3)；不排其它更精细criteria。这里τ是本对象已付原始coefficient type的值，普通Taylor rank及type已付，而全部共同meromorphic graph、其boundary/radius standing与极点处理尚未付；没有certify任何map或strict numerical inequality。

## F11. 下一首证书与本轮边界

新s的额外integer inverse和rationalforcing不是原level12 pure L3的坐标更名：原sourceweight4/third primitive，本sourceweight3/second primitive；额外ψ来自当前f₄的完整odd坏芽。借旧u函数域不借旧L3 periods或预算，也不以未识别旧记录宣称首次性。

下一首证书必须核当前s在同一relation H解析leaf上的全部cusps、t=0四fiber与t∞四fiber、branch-return monodromy和θsH poles，明确哪些点由关系填、哪些必须省略/ramify/clear。F4.1完整cusp0 identity与s=1/2局部parameter能填唯一canonical cusp；不能据此断言所有Γψ translates或全部 compact P¹s 上H单值。源空间的rationalforcing与holonomicity也不会自动给一个足够大的holomorphic图。

没有构造Padé/matrix、没有CAS/prime/maps/参数/数值扫描、没有执行旧producer或Lean。没有新的ζ/L数值定理。本稿的source admission界限是：最低场、真实bare关系rank、完整formal整模型已付，整体解析图和strict预算未付。是否值得继续应由第260轮全局复盘按这些实际缺口决定。
