# 经典奇ζ导数源的四阶超几何几何入口、真实五阶秩与渐近

日期：2026-10-06。本轮新结果。只读[冻结经典导数投影](cdt_odd_classical_derivative_projection_20261006.md)；没有执行/import冻结或同行producer。本文给具体微分模块、精确单值群和实际积分渐近，不给新的数值无理性结论。四阶几何对象本身已见文献，新增的是它与本项目真实经典源的精确外平方及forcing接口。

## 1. 真实五阶算子恰是四阶超几何模块的外平方商

令x=256z、θ=x d/dx。经典源的齐次generating算子为

\[
 L_5=\theta^5-\frac{x}{8}(2\theta+1)
 (8\theta^4+16\theta^3+20\theta^2+12\theta+3)
 +x^2(\theta+1)^5.\tag{P1}
\]

**结构定理。**设V₄为

\[
 \boxed{P_4=\theta^4-x(\theta+1/2)^4}\tag{P2}
\]

的四维局部解空间，V₅为L₅解空间。对两个V₄解y、ỹ，

\[
 \boxed{w=x(y\widetilde y'-y'\widetilde y)\in V_5.}\tag{P3}
\]

六维外平方经(P3)的完整输出秩是5；其核是一维symplectic invariant。因而V₅是V₄外平方的primitive五维商，不能把四阶入口当作真实L₅秩免费降到4。

以下给完整系数证明。把P₄化为普通导数monic式D⁴+a₃D³+a₂D²+a₁D+a₀，准确系数为

\[
\begin{aligned}
a_3&=2(4x-3)/[x(x-1)],\\
a_2&=(29x-14)/[2x^2(x-1)],\\
a_1&=(5x-1)/[x^3(x-1)],\\
a_0&=1/[16x^3(x-1)].
\end{aligned}\tag{P4}
\]

它们满足完整CY2恒等式

\[
a_3''-2a_2'+\tfrac32a_3a_3'-a_2a_3+\tfrac14a_3^3+2a_1=0.\tag{P5}
\]

令Y=yỹ′−y′ỹ、U=Y‴+a₃Y″+a₂Y′+a₁Y。由四阶companion的六个外平方minors直接消元，得

\[
U''+\tfrac32a_3U'+(a_2+\tfrac14a_3^2)U
-4a_0Y'-2(a_0'+a_3a_0)Y=0.\tag{P6}
\]

将w=xY代入，(P6)的六个普通导数系数逐个等于(P1)monic系数。另用完整6×6 exterior companion检验六个minor均被(P1)消去；输出行及其前四次协变导数组成的5×6矩阵秩准确为5。这验证实际module map，不只检验一个CY条件或几个Taylor项。[新外平方证书](cdt_odd_classical_spin_pullback_20261006_verify.py)首次单次16项通过，[JSON](cdt_odd_classical_spin_pullback_20261006_verify.json)保留全部系数、指数及输入pins。

Almkvist–Zudilin [原始论文](https://arxiv.org/abs/math/0402386) §§2–3给四/五阶外平方机制；Almkvist [Yifan Yang pullback论文](https://arxiv.org/abs/math/0612215)给一般降阶背景。本稿(P4–P6)从本项目真实companion独立推出，不依赖文献的一条印刷公式替代整个module验证。

## 2. 实际A序列来自两个真实Frobenius周期的Wronskian

四阶regular解为

\[
y_0(x)={}_4F_3(1/2,1/2,1/2,1/2;1,1,1;x)
=\sum_{n\ge0}\binom{2n}{n}^4(x/256)^n.\tag{P7}
\]

取Frobenius解y₁=y₀logx+B，其中

\[
B(x)=8\sum_{n\ge0}\binom{2n}{n}^4
(H_{2n}-H_n)(x/256)^n.\tag{P8}
\]

这里(P8)由ρ-导数准确给出，没有赋值于未知ζ。于是

\[
w_0=x(y_0y_1'-y_0'y_1)
=y_0^2+x(y_0B'-y_0'B),\qquad w_0(0)=1.\tag{P9}
\]

由(P3)它解L₅；L₅在0的indicial是r⁵，analytic power-series解由constant唯一递推。因此

\[
\boxed{\sum_{n\ge0}A_nz^n=w_0(256z).}\tag{P10}
\]

这不仅给formal相似性，而是实际A源与周期的whole-germ恒等式。

Frobenius算术也有完整接口。令

\[
Y(\rho,z)=z^\rho\sum_{n\ge0}
256^n\left[\frac{(1/2+\rho)_n}{(1+\rho)_n}\right]^4z^n.
\tag{P11}
\]

P₄Y=ρ⁴z^ρ，故ρ⁰至ρ³系数给四个真解。以Δₙ=lcm(1,…,n)记LCM；de-log regular部分bⱼ(z)的第n系数满足

\[
\Delta_n^j[z^n]b_j\in\mathbf Z\quad(0\le j\le3).\tag{P12}
\]

证明：写Fₙ(ρ)=4ⁿ(1/2+ρ)ₙ/n!、Gₙ(ρ)=n!/(1+ρ)ₙ。Gₙ的degree-j Taylor项由j个k⁻¹乘积组成，故Δₙʲ清分母。Fₙ的每个degree-j项是从n个偶倍奇数因子中删除j个后除以n!：对odd p每层pᵃ≤n原odd progression至少有⌊n/pᵃ⌋个倍数，删除j个至多损失j层；pᵃ>n没有n!分母。对p=2，剩余2^(n+j)已经清v₂(n!)≤n。故Fₙ同样满足Δₙʲ清分母；卷积及取(FₙGₙ)⁴保持此界。这里的bⱼ是在z归一的logz分解，避免把log256额外当作rational initial value。

(P12)是背景regular部分的算术接口，不证明它们是独立的免费Q[[z]] horizontal solutions；删去logz后，其实际Dfinite秩、共同全纯叶与CDT数组成本还须核算。

## 3. 单值群准确为Sp₄；五阶商的实际秩是5

Beukers–Heckman [原始论文](https://math.uchicago.edu/~drinfeld/Hypergeometric_motives/Beukers-Heckman.pdf) Proposition 3.2、Theorem 3.5给本参数的Levelt模型。α=(1/2)⁴、β=(1)⁴没有integer cross-difference；可取

\[
A=\begin{pmatrix}0&0&0&-1\\1&0&0&-4\\0&1&0&-6\\0&0&1&-4\end{pmatrix},\qquad
B=\begin{pmatrix}0&0&0&-1\\1&0&0&4\\0&1&0&-6\\0&0&1&4\end{pmatrix},\tag{P13}
\]

分别h∞=A、h₀=B⁻¹、h₁=A⁻¹B。它们保持唯一到scale的nondegenerate alternating form

\[
J=\begin{pmatrix}0&1&0&-5\\-1&0&1&0\\0&-1&0&1\\5&0&-1&0\end{pmatrix}.\tag{P14}
\]

N₀=logB=(B−I)−(B−I)²/2+(B−I)³/3及N₁=A⁻¹B−I属于单值群Zariski closure的Lie algebra。固定有理commutator closure准确dimension10，且每个元素满足NᵀJ+JN=0。因此该Lie algebra是整个sp₄，closure是connected Sp₄。

在外平方的J-contraction kernel上直接限制A、B，得到primitive5维表示；由这两个确定矩阵生成的完整associative algebra维数25，故该表示绝对不可约。这样(P3)中的一维kernel必须是唯一invariant line；V₅准确是不可约五维primitive外平方（connected群SO₅）。任何非零L₅解，包括真实A，都没有order<5的rational scalar annihilator。有限代数cover保留connected群，所以也没有通过有限pullback免费降秩。

[新单值群证书](cdt_odd_classical_spin_monodromy_20261006_verify.py)首次单次19项全通过；[JSON](cdt_odd_classical_spin_monodromy_20261006_verify.json)存完整J、Lie basis、primitive矩阵及代数维数。闭包是在固定有限维matrix algebra内进行，不是有限group-word样本推无限群分类。

P₄在0、1的indicial分别r⁴和r(r−2)(r−1)²；L₅分别r⁵和r²(r−1)(r−2)²。conifold primitive单值确为Jordan(2,2,1)，而不是只据local exponent猜Jordan。因此这个rank5 module不等价于rank2非平凡单幂的Sym⁴：后者非平凡unipotent只有一条Jordan5链，或identity有五个fixed directions。

## 4. 这里有真实几何，但整周期格尚未搬运完成

对|x|<1，三次Euler积分严格给

\[
y_0(x)=\pi^{-3}\int_{[0,1]^3}
\frac{dt_1dt_2dt_3}{
\sqrt{t_1t_2t_3(1-t_1)(1-t_2)(1-t_3)(1-xt_1t_2t_3)}}.
\tag{P15}
\]

逐项展开最后平方根，三个Beta积分与展开系数合给四个(1/2)ₙ/n!。故π³y₀是明确algebraic double-cover family的实际积分；不由这一affine积分独自声称已构造光滑compact CY resolution。

更强的几何识别已有原始文献：Bönisch–Klemm–Scheidegger–Zagier [作者PDF](https://people.mpim-bonn.mpg.de/zagier/files/preprints/ADEK.pdf) §2.1 Table 1第一行给aᵢ=1/2、µ⁻¹=256，镜像为P⁷中四个quadrics；§2.4.2给explicit one-parameter quotient和resolution。因此(P2)就是该mirror CY threefold family的Picard–Fuchs模块。本文实际读Table 1及相关构造页；未独立重建整个resolution或其integral symplectic周期basis。

Levelt的GL₄(Z)格证明topological monodromy有显式integral lattice；它不能直接代替CDT要求的所有源系数、de Rham comparison、forcing extension、奇点模型与finite-place预算。尤其primitive外平方格的饱和和rank4周期格到实际A/C源的有理comparison必须另算。这是当前完整整模型的明确缺口。

## 5. 真实ζ(7)forcing接入同一几何module的twist

新[forcing spin接口](cdt_odd_classical_zeta7_forcing_spin_20261006.md)给actual germ

\[
H(x)=\sum_{n\ge1}\frac{(n-1)!^4}{(1/2)_{n+1}^4}x^n,
\quad[(\theta+1/2)^4-x\theta^4]H=16x.\tag{P16}
\]

其齐次module与P₄通过quadratic twist及contiguity同构；它仍保留16x非齐次项。实际C₂=ΣCₙ,₂(x/256)ⁿ满足

\[
L_5C_2=960x-\tfrac32x\theta^2
(48\theta^3+80\theta^2+40\theta+5)H.\tag{P17}
\]

forcing稿还证明Kr=16x无C(x)有理特解：0、1没有负整数indicial root，其余有限点ordinary，故r须polynomial；最高degree与constant均不可能。结合已证齐次K不可约，实际H闭包包含trivial一维且非零quotient是rank4，故H实际秩恰为5；若extension split，trivial投影给被排除的有理特解。因此该forcing extension确实非split。完整C₂/F₂的inhomogeneous derivative closure仍只有安全上界10，而不是已证明最小秩10。root实际全文审核新增pole/degree、quotient及split投影证明，以及原coefficient recurrence、twist、Bézout逆和closure；没有把齐次contiguity当作非齐次特解。

另一[forcing排除证明](cdt_odd_classical_zeta7_forcing_20261006.md)已排除整个hypergeometric particular class；所有rational-initial特解仍保留坏素数p⁴带并转移真实ζ(5)carrier。无hypergeometric特解并不等价于一般differential extension非split。这一整体结构需要下一步计算，而不是删除forcing后直接套CDT。

## 6. 正的渐近定理：这些经典形式本身并不指数趋零

对冻结经典源

\[
R_n(t)=256^n(2t+n)
\left[\frac{\Gamma(t)}{\Gamma(t+1/2)}\right]^4
\left[\frac{\Gamma(t+n+1/2)}{\Gamma(t+n+1)}\right]^4,
\quad F_{n,r}=\sum_{m\ge0}R_n^{(2r)}(m+1/2),\ r\ge1,
\tag{P18}
\]

有全固定r渐近

\[
\boxed{F_{n,r}\sim\frac{256^n}{n}\,S_r,\quad
S_r=\sum_{m\ge0}\left.\frac{d^{2r}}{dt^{2r}}
\left[\frac{\Gamma(t)}{\Gamma(t+1/2)}\right]^4
\right|_{t=m+1/2}>0.}\tag{P19}
\]

证明完整保留半整数求和及derivative normalization。compact t-sets上Gamma ratio的Stirling给nRₙ/256ⁿ→φ(t)⁴及全部固定导数，φ=Γt/Γ(t+1/2)。对disk |u−t|≤t/2、t≥1/2，Euler Beta给

\[
|\phi(u)|\le\phi(t/2),\quad
\left|\frac{\Gamma(u+n+1/2)}{\Gamma(u+n+1)}\right|
\le(n+t/2)^{-1/2}.
\]

后一式用Gamma的log-convexity：Γ(a+1/2)²≤Γ(a)Γ(a+1)，故Γ(a+1/2)/Γ(a+1)≤a⁻¹/²（a>0）。于是

\[
|nR_n(u)/256^n|
\le\frac{n(n+3t)}{(n+t/2)^2}\phi(t/2)^4
\le3\phi(t/2)^4\le972t^{-2}.
\tag{P20}
\]

最后界可从φ(a)=a⁻¹Γ(a+1)/Γ(a+1/2)≤a⁻¹(a+1/2)^1/2及a≥1/4得到φ(a)⁴≤9a⁻²；此时(P20)甚至可改善为108t⁻²，保留972安全界。Cauchy给

\[
|nR_n^{(2r)}(t)/256^n|
\le972(2r)!2^{2r}t^{-2r-2}.\tag{P21}
\]

它支配全部m求和，故可交换n-limit与sum。φ(t)⁴的四次Euler Beta积分再给

\[
\boxed{S_r=\pi^{-2}\int_{[0,1]^4}
\frac{\prod_i u_i^{-1/2}(1-u_i)^{-1/2}}{1-U}
(\log U)^{2r}\,du_1du_2du_3du_4,\quad U=\prod_i u_i.}\tag{P22}
\]

非negative integrand在interior严格positive；(P21)或直接boundary估计保证finite，因此Sᵣ>0。这是真正的positive connection period接口，不是有限n数值拟合。

(P19)纠正任何未经证明的“Apéry外观意味着Fₙ,ᵣ/Aₙ→0”推断：这些F本身以256ⁿ/n增长。本文不宣称已算Aₙ leading connection constant，因而不以此认领F/A的数值limit，也不把Sᵣ私自替换成纯ζ(2r+3)。若想产生small forms，必须消去实际Sᵣ连接周期并记录新目标、完整整格及成本。

还有直接的analytic consequence。对实x↑1，Abelian比较aₙ=Sᵣ/n+o(1/n)给
\[
\sum_{n\ge0}F_{n,r}(x/256)^n
\sim-S_r\log(1-x)\longrightarrow+\infty.\tag{P23}
\]
证明只需将n≥N的误差夹于ε/n，有限initial sum有界，再用Σxⁿ/n=−log(1−x)。所以z=1/256对这个实际germ不可去；ζ的有理性假设没有改变其真实数值函数，不能单凭该假设赠送一个去conifold的解析叶。这不排避开该点的其他合法CDT地图或不同corrector源。

## 7. 研究推进与实际审阅

本轮得到新的具体几何路线：同一CY rank4、primitive exterior rank5、twisted rank4 forcing与positive real connection integrals。它为全oddζ导数源提供统一候选对象，超出旧level12单幂框架；不声称全部oddζ或Catalan已经归入同一完整证明。

下一可核任务是完整C₂/F₂的inhomogeneous extension的split/minimalrank、primitive integral lattice与源comparison，以及实际Sᵣ连接矩阵的几何表达。H的rank5与非split缺口已补，但不能把它代替完整目标。随后才谈共同analytic leaf、finite-place预算和CDT严格差额。现有hypergeometric/整数校正族的失败不能替代这些待做证明。

本稿两个新固定producer分别首次16、19项全通过；未运行任何冻结或同行producer。conjugate_projection实际全文只读独审本稿§§1–7/P1–P23及两份新PY/JSON，通过完整module、Frobenius算术、Levelt/Sp₄/primitive链和全r渐近/Abelian结论；它另实际核读BH PDF7–10与CY作者表/构造页，不认领整resolution/格重建。helper_tensor_budget实际只读独审§6/P18–P23，独推Beta/Cauchy归一及Abelian范围，通过；它未审其它spin部分。hash由[本轮审阅记录](cdt_odd_spin_corrector_review_20261006.md)明确登记。经典forcing两份新稿root实际全文/PY/JSON读审，未将这些19/16项说成数值或Lean验证。
