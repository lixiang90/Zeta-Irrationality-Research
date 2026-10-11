# 第239轮独立算术：实际one-hole余子式的两层整格与固定素数内容

2026-10-08，Dual/C。对同一真实填点源，在假设g₀=𝔱∈Q下，新增全尺度结论
\[
\boxed{\mathcal A_D\le
\left(\frac{21}{2}-\log12\right)D^2+o(D^2).}
\tag{A1}
\]
证明覆盖所有候选缺行h=m,…,2m，因而覆盖未知actual selector；没有将generic g、任意最大minor或Gram平方和代入实际费用。此upper需要同一合法图的真实metric严格比较，尚无新的数值无理性结论。数学程序0。

## 1. 固定实际对象与原生费用

令m=D+1、N=3m。冻结238已经自足证明，真实g₀=2I(1/4)=𝔱对应
\[
f=(1,F,b_gJ_{g_0}),\quad F=uE,\quad
E=\sum_{n\ge0}\frac{3^n}{2n+1}u^n,\quad
J_g=S(g-2I),\ S=\sqrt{1-4u},\ I'=E/S.
\tag{A2}
\]
仅在g₀∈Q假设下固定正整数b_g，使b_gg₀∈Z。取L_D=Z[u]_{\le D}³及完整Taylor系数评价T_N。尾矩阵K_m有行r=0,…,2m、列s=0,…,m−1：
\[
K_E(r,s)=\mu_{r+s}=\frac{3^{r+s}}{2(r+s)+1},
\quad K_J(r,s)=j_{r+s+1}(g_0),
\tag{A3}
\]
其中j_n=[uⁿ]J_g。删第h行的未乘b_g子式记δ_h；所有δ_h不全为零。actual h_*是最大非零下标，h_*∈[m,2m]，完整实际pivot为
\[
\eta_D=\det T_{V_D}=\pm b_g^m\delta_{h_*},\qquad
\mathcal A_D=-\log|\eta_D|.
\tag{A4}
\]
238的正moment仅支付全阶非零与selector。下文局部整格的结论适用于每个固定有理g；用于A4时始终取同一真实g₀，未改变源或target。

冻结234完整卷积保留全部头：
\[
S=\sum s_nu^n,\quad s_0=1,\ s_n=-2\mathrm{Cat}_{n-1}\in Z;
\quad S^{-1}=\sum B_nu^n,\ B_n=\binom{2n}n,
\]
\[
I_n=\frac1n\sum_{j=0}^{n-1}
\frac{3^j B_{n-1-j}}{2j+1},\qquad
b_gD_ND_{2N-1}j_n\in Z\quad(0\le n\le N).
\tag{A5}
\]
S及S⁻¹是整数Taylor单位。gS整项不带增长素数残差，但不意味着particular J、δ的分母或其值已免费消失。

## 2. 中间素数窗口的完整两层结构

取素数p>3、p∤b_g，
\[
2m<p\le3m=N,\quad
k=(p-1)/2,\quad h=k+1,\quad
L=N-p,\quad G=k-m\ge0.
\tag{A6}
\]
这里N<3p/2、p²>2N−1。整个prefix中内奇分母只能有一个p，即2j+1=p；外积分分母只能有一个p，即n=p。全部原系数深度至多p²。唯一双极点来自I_p，且
\[
p^2I_p\equiv3^kB_k=(-3)^k\pmod p.
\]
所以对P=c+bF+a(b_gJ)，完整0,…,N输出满足
\[
p^2T_N(P)\equiv
-2b_g(-3)^k u^p S\,a
\pmod{(p,u^{N+1})}.
\tag{A7}
\]
F只有simple pole，gS全整，未丢掉任何finite head。S常数项1，故深层kernel恰为
\[
a_0,\ldots,a_L\in pZ_p,\qquad
[L_D\otimes Z_p:\Lambda_2]=p^{L+1}.
\tag{A8}
\]
其它a_j、b、c仍自由。此kernel上的T_N至多simple pole；所有n<h的原系数均p整，所以后层residue只能落在h,…,N，共N−h+1个输出。这先给安全upper；以下证明全部输出确实onto。

在relative rows0,…,N−h，按三段0,…,m−1；m,…,k−1；k,…,N−h分块：

* b的m列给pF≡3^ku^h，第一段是单位identity。
* 将低a_j写成pA_j，j=0,…,L。它们给p²J的A7残差，在最后一段形成S的下三角Toeplitz矩阵，diagonal为−2b_g(−3)^k，故单位；第一、二段为0。
* 若G>0，取自由高列a_(m−1−s)，s=0,…,G−1。这些下标均>L。其整个剩余J coefficient下标<p，故只用第一simple residue：
  \[
  pJ_g\equiv3^ku^h\mathscr A(u)\pmod{(p,u^p)},\quad
  u\mathscr A'+\left(\frac12+\frac{2u}{1-4u}\right)\mathscr A=-2,
  \quad\mathscr A_0=-4.
  \tag{A9}
  \]
  消去第一段b后，gap rows r=m+i给b_g3^k\mathscr A_(1+i+s)。

冻结236 J7–J8的完整纸证给
\[
H_G=(\mathscr A_{1+i+s})_{0\le i,s<G},\quad
\det H_G=
2^{3G^2+G}
\frac{\prod_{j=0}^{G-1}(j!)^2}
{\prod_{i,s=0}^{G-1}(2i+2s+3)}.
\tag{A10}
\]
p>4G−1在A6自动成立，故H_G是p单位；G=0无gap、无Hankel除法。三段选中的列数正为m+G+L+1=N−h+1，最后用低列清除高列的尾部，得到整个simple map满秩。

于是最大完整整值prefix格Λ_p={P:T_N(P)∈Z_p^(N+1)}的**精确**index为
\[
\boxed{[L_D\otimes Z_p:\Lambda_p]
=p^{L+1+N-h+1}=p^{2N-3k}.}
\tag{A11}
\]
p=2m+1时G=0，同式仍成立。证明未使用实正性推Fp unit，而以A10的完整rational determinant证明。b_g全程为固定p单位。

A11只饱和同一完整prefix整值格的local index；它没有把局部index当作actual δ的精确valuation，更不排除该δ的numerator content另有收益。

## 3. 全prime powers的CRT安全upper

fallback取完整row尺度
\[
q_E=D_{2N-1},\quad q_J=D_ND_{2N-1},
\quad \Gamma_{\rm row}
=Z[u]_{\le D}\times q_EZ[u]_{\le D}\times q_JZ[u]_{\le D}.
\tag{A12}
\]
它覆盖2、3、全部prime powers及全部原生输出。

对高窗口N<p≤2N−1，采用已FULL复读的236 J3–J9：最大prefix local index为p^(N−k)，而fallback为p^(2m)。对A6中间窗口，fallback为p^(3m)，用A11代替。固定p|3b_g留在fallback，D充分大时不落入两个窗口。各窗口均为整系数有限congruence kernel，CRT交成一个实际full-rank Γ_D⊂L_D，T_NΓ_D全整。其index为
\[
\begin{aligned}
I_D={}&m(\log q_E+\log q_J)\\
&-\sum_{N<p\le2N-1}(k-m)\log p
-\sum_{2m<p\le3m}3(k-m)\log p ,
\end{aligned}
\tag{A13}
\]
窗口中排除固定坏prime的有限项；N=3m。中间p=2m+1的gain为0，无边界遗漏。

PNT加partial summation给fallback15m²+o(m²)，高窗口gain15m²/4+o(m²)，中间gain3m²/4+o(m²)。所以
\[
\boxed{I_D\le\frac{21}{2}m^2+o(m^2)
=\frac{21}{2}D^2+o(D^2).}
\tag{A14}
\]
此全primepower-safe模型比冻结45/4改善3/4；不是最优全prime lower。236/237只改变截止O(1)时的主项同样保持。两窗口local index已付饱和不表示其它prime或actual content已最优。

## 4. 所有μ-Cauchy minor的整数内容

固定任意h及其任意Laplace展开项；从剩余2m行选m行
0≤r_0<…<r_(m−1)≤2m。μ-block的Cauchy exact formula为
\[
U_{\boldsymbol r}:=\det(\mu_{r_i+j})_{i,j=0}^{m-1}
=
\frac{
3^{\sum_i r_i+\binom m2}
2^{m(m-1)}
V(\boldsymbol r)\prod_{j=0}^{m-1}j!
}{
\prod_{i,j=0}^{m-1}(2r_i+2j+1)
}.
\tag{A15}
\]
两组Cauchy差值均递增，符号为正。由整数binomial basis，
\[
\frac{V(\boldsymbol r)}{\prod_{j=0}^{m-1}j!}
=\det\left(\binom{r_i}{j}\right)_{i,j=0}^{m-1}\in Z.
\tag{A16}
\]
故V不是可抛掉的普通实Vandermonde；它支付第二份factorial整除。

固定素数p的Legendre和式直接给
\[
2\sum_{j=0}^{m-1}v_p(j!)
=\frac{m^2}{p-1}+O_p(m\log m).
\]
分母全部奇数，因此
\[
v_2(U_{\boldsymbol r})
\ge m(m-1)+2\sum_jv_2(j!)
\ge2m^2-O(m\log m).
\tag{A17}
\]
对3，Σr_i+binom m2≥m(m−1)。每一行的m个奇分母为step2 progression；对3^a至多m/3^a+1个，全部分母≤6m−1。所以
\[
\sum_{i,j}v_3(2r_i+2j+1)
\le\frac{m^2}{2}+O(m\log m).
\]
A16的双factorial抵消这项主率，得到
\[
\boxed{v_3(U_{\boldsymbol r})\ge m^2-O(m\log m).}
\tag{A18}
\]
所有常数均对r、h一致，不需要critical h=2m，也不依g的generic评值。

## 5. J-minor的固定素数损失只为低阶

A5在n≤N覆盖每个原生b_gj_n。对固定p=2或3，
\[
v_p(b_gj_n)\ge
-\lfloor\log_pN\rfloor-\lfloor\log_p(2N-1)\rfloor.
\tag{A19}
\]
因此任何m阶native J-block determinant只损O(m log m)的固定p深度。对δ_h作μ/J全部Laplace展开，每项都由A17/A18和A19给同一个valuation lower；相加或相消只能提高valuation。零子式的valuation按+∞理解。故对**每个**0≤h≤2m，
\[
\boxed{
v_2(b_g^m\delta_h)\ge2m^2-O(m\log m),\qquad
v_3(b_g^m\delta_h)\ge m^2-O(m\log m).
}
\tag{A20}
\]
特别适用于A4的未知actual h_*。这是完整rational coefficient内容证明，没有从μ正性、余子式绝对值upper或若干小D证据推出Fp行为。

## 6. 内容必须进入actual fee，而非从raw index免费扣费

令i_p=v_p[L_D:Γ_D]。实际jump matrix T_(V_D)在Γ_D上全整，故
\[
v_p(\eta_D)+i_p\ge0.
\tag{A21}
\]
对p≠2,3用−v_pη_D≤i_p；对2、3直接用A20。Γ_D在固定2、3沿用fallback，i_2,i_3=O(m log m)。rational product formula给
\[
\begin{aligned}
\mathcal A_D
&=-\sum_pv_p(\eta_D)\log p\\
&\le I_D-(2\log2+\log3)m^2+O(m\log m)\\
&\le\left(\frac{21}{2}-\log12\right)D^2+o(D^2).
\end{aligned}
\tag{A22}
\]
这证明开头A1。它使用同一nonzero actual pivot的固定prime内容，并非改Γ后以index减少宣布intrinsic fee改变。237同flag抵消恒等式仍成立；Γ只是提供其它全部prime的合法upper。

若仅用固定2、3正内容，却未覆盖其余prime powers，就不能得到A22。若仅用实处Chebyshev小量，则只给𝓐_D的lower，方向与本upper不同。此处两者没有混用。

## 7. 有界方向与执行范围

237直接filtered BC桥允许以A22为同源actual arithmetic upper，故可用
\[
\tau_{\rm upper}
=\frac29\left(\frac{21}{2}-\log12\right)
=\frac73-\frac29\log12 .
\tag{A23}
\]
它严格改善原literal7/3及安全κ45/4换算5/2。但仍需在真实目标假设下给同一合法共同图的λ、J(1)，或完整凸曲线J(r)，并证明
\[
\frac{21}{2}-\log12
<\frac92\lambda-\frac32J(1)+C_R .
\]
derivative cap只是upper，不能当存在达到cap的合法图；本轮算术改善不等于strict margin已付。goal仍是新的真实ζ/L数值结论，没有以辅助lemma重定义成功。

Root随后重新利用234已付的全部合法共同图界。本人实际完整选读冻结A234的§4.2/A13–A16；在其同一holomorphic φ、F∘φ meromorphic条件下，
\[
|\phi'(0)|\le C_E=\frac{2\pi}{3}
\mathbf K(1/9)\mathbf K(8/9),\qquad
\mathbf K(x)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-x\sin^2\theta}}.
\]
自含Cauchy–Schwarz与tan θ换元给
\[
\mathbf K(x)^2\le\frac\pi2
\int_0^{\pi/2}\frac{d\theta}{1-x\sin^2\theta}
=\frac{\pi^2}{4\sqrt{1-x}}.
\]
两式相乘可把旧松cap收紧为
\[
\boxed{|\phi'(0)|\le\frac{\pi^3}{2^{7/4}}.}
\tag{A24}
\]
它只需要E的实际frame，J标记只进一步限制图。参数x与modulus√x没有互换，A14的导数规范确给系数2π/3。

这个新upper使当前A22不足以证明**basic r=1**的strict gate：J(1)≥λ令其右侧至多3λ≤3log(π³/2^(7/4))，而
\[
\frac{21}{2}-\log12>
3\log\left(\frac{\pi^3}{2^{7/4}}\right).
\tag{A25}
\]
无需浮点程序即可核方向：π³<32、2^(7/4)>16/5给cap<10；e³>13>12给左侧>15/2，e^(5/2)>4169/384>10给3log10<15/2。改善确实跨过旧松cap的必要门槛，却跨不过这个较紧界。A25不是actual 𝓐_D的lower：更低actual费用仍可能存在；也未控制凸C_R或其它方法，不能升级为全联合费用/目标no-go。

中间窗口的安全两层upper由C独立先推，Root独立提出exact gap/Hankel饱和补强后C逐式核；固定2、3的内容接口由Packet/B提出，C独立给出A15–A22完整valuation推导。保留这些协调事实，不把收到结论代替实际证明。第240轮正式全局复盘并执行止损门槛，不自动延长到无收益素数优化。

本轮实际FULL读取238 one-hole稿、236完整联合整格稿、234完整卷积稿和237独立metric桥；确切身份另存同目录dual scope。没有新增primary检索/下载、数学程序、小D exact、prime/parameter scans或旧producer。仅NEW239数学稿与scope，旧稿、main、manifest不改。保存后实际FULL作者复读，最终bytes/hash另报。

