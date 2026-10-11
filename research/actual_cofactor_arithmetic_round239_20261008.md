# 第239轮：actual cofactor的全有限分母与固定2、3内容

2026-10-08，Packet/B，数学程序0。对238同一selected cofactor，纸证全prime分母Q_m及共同整数内容因子C_m，得到
\[
\limsup_{D\to\infty}\frac{\mathcal A_D}{D^2}
\le\frac{21}{2}-\log12.
\]
这是严格改善45/4的真实费用upper，跨越旧宽cap的门槛；本轮新的紧all-map cap仍使这项safe bound不足以认证basic BC严格余量。没有取得新数值定理，也不从upper不足推出最优联合费用no-go。

## 1. 同一真实source与全部候选hole

固定真实目标g₀=𝔱=2I(1/4)，在关系假设g₀∈Q下取固定正整数b_g，使b_gg₀∈Z。沿238原生源
\[
f=(1,uE,b_gJ_{g_0}),\quad
E=\sum_{n\ge0}\frac{3^nu^n}{2n+1},\quad
J_g=S(g-2I),\quad S=\sqrt{1-4u},\quad I'=E/S.
\tag{A1}
\]
令m=D+1、N=3m。238已全阶支付0,…,N完整jet单射，以及
\[
K_m(r,s)=\big(\mu_{r+s},j_{r+s+1}(g_0)\big),\quad
\mu_l=\frac{3^l}{2l+1},\quad 0\le r\le2m,\ 0\le s<m.
\]
δ_h为删第h行的2m阶det，h_*=max{h:δ_h≠0}，m≤h_*≤2m。实际ordinary graded费用恰为
\[
\mathcal A_D=-\log|\mathcal D_{h_*}|,\qquad
\mathcal D_h=b_g^m\delta_h.
\tag{A2}
\]
以下界统一作用于所有m≤h≤2m；不换最大绝对值minor，不用Σδ²，不假设critical prefix perfect。

235完整卷积给
\[
I_n=\frac1n\sum_{j=0}^{n-1}
\frac{3^j}{2j+1}\binom{2(n-1-j)}{n-1-j}.
\tag{A3}
\]
记d_t=lcm(1,…,t)，q_E=d_(2N−1)、q_J=d_Nd_(2N−1)。包括所有素数幂、0阶头和固定g分母在内，q_E清uE的0,…,N prefix，q_J清b_gJ_g的完整prefix。2、3绝不从分母账中免费删去。

## 2. 两个实际prime窗口给完整Q_m

首先重核middle window：p>3、p∤b_g，
\[
2m<p\le N=3m,\quad
k=(p-1)/2,\quad \ell=N-2k,\quad M=N-k,\quad r=k-m.
\tag{A4}
\]
此时N<3p/2，p²>2N−1；内奇分母仅p，外积分分母仅n=p。A3的唯一双层源为I_p，binom(p−1,k)≡(−1)^k，故全部0,…,N输出满足
\[
p^2T_N(c,b,a)
\equiv-2b_g(-3)^k u^pS\,a\pmod{(p,u^{N+1})}.
\tag{A5}
\]
这里T_N评价c+b(uE)+a(b_gJ_g)，全部三组degree≤m−1；E、c没有双层，原生gS头已整。因S₀=1，deep kernel恰为a₀,…,a_(ℓ−1)≡0 modp，index p^ℓ。

在该kernel选a=pα+u^ℓ a_hi，deg α<ℓ。此后输出仅simple p层，且n<h=(p+1)/2全部整。除去单位3^k u^h，后层residue恰为
\[
b+b_g u^\ell a_{\rm hi}A
-2b_g(-1)^k u^kS\alpha
\quad\bmod u^M,
\]
\[
uA'+\left(\frac12+\frac{2u}{1-4u}\right)A=-2,\qquad A_0=-4.
\tag{A6}
\]
high a的原J下标至多N−ℓ=p−1，所以只用A₀,…,A_(k−1)，其2j+1<p，归约没有隐藏p分母。

后层onto的三段证明：b覆盖0,…,m−1；若r>0，取high a的列m−1,m−2,…,m−r，清掉b段后在m,…,k−1形成H_r=(A_(1+i+j))。这些列都≥ℓ，因为m−r−ℓ=r。236全r Jacobi公式给
\[
\det H_r=
2^{3r^2+r}
\frac{\prod_{j=0}^{r-1}(j!)^2}
{\prod_{i,j=0}^{r-1}(2i+2j+3)}.
\tag{A7}
\]
本窗口k≤(3m−1)/2，故p>4r−1；A7严格为p单位。最后α的S₀=1 triangular block覆盖k,…,M−1，长度ℓ。r=0没有gap，直接用b和α；该边界也onto。因此整个原source的最大整数值格满足
\[
[L_D\otimes Z_p:\Lambda_{D,N,p}]
=p^{\ell+M}=p^{2N-3k}.
\tag{A8}
\]
这是完整tuple的两层kernel，不是两个rank相加却遗漏后层。

在第二窗口N<p≤2N−1、p∤3b_g，236已付完整simple residue，给精确local index p^(N−k)。当前N=3m、D=m−1：若r'=N−h−D=2m−k≤0，b单独覆盖全部active输出；若1≤r'≤m，才用同A7且p>4r'−1的Jacobi单位。因此包括全部此窗口，不调用负尺寸Hankel，也不缩短输出。

据此定义对所有p的非负整数
\[
e_m(p)=
\begin{cases}
2N-3k,&2m<p\le N,\ p\nmid3b_g,\\
N-k,&N<p\le2N-1,\ p\nmid3b_g,\\
m\big(v_p(d_N)+2v_p(d_{2N-1})\big),&\text{其它p},
\end{cases}
\qquad Q_m=\prod_p p^{e_m(p)}.
\tag{A9}
\]
两个window的fallback分别为3m、2m；A8及236证明这些替换均不增index。其它prime，包括2、3、p|b_g及其全部powers，保留完整fallback；有限badprime不改变leading rate。

local kernel/row lattice经CRT形成完整jet整格Γ_m，index恰为Q_m：两个窗口用上述exact kernel，其它prime用fallback row lattice。取Γ_m的整数基变换B，det B=±Q_m，T_square B全整。因此任一full-column Taylor square的det分母都由Q_m清除；238常数列identity遂给
\[
\boxed{\mathcal N_h:=Q_m\mathcal D_h\in Z
\quad\text{对每个 }m\le h\le2m.}
\tag{A10}
\]
这包含全部finite heads；不能只清一个tail entry便声称A10。

PNT、partial summation与log d_t=t+o(t)给base 15m²。middle gain为
∫_(2m)^(3m)[3m−(6m−3p/2)]dp=(3/4)m²；
第二window gain为(15/4)m²（236完整计算）。固定端点/坏prime仅O(m log m)，故
\[
\boxed{\log Q_m=\frac{21}{2}m^2+o(m^2).}
\tag{A11}
\]

## 3. Cauchy–Vandermonde使每个候选cofactor都有固定内容

令F_m=∏_(j=0)^(m−1)j!。对任意m个不同非负整数rows r₁<⋯<r_m≤2m，μ-block的exact minor为
\[
\det(\mu_{r_i+j})=
3^{\sum_i r_i+m(m-1)/2}\,
2^{m(m-1)}
\frac{V(r_1,\ldots,r_m)F_m}
{\prod_{i=1}^m\prod_{j=0}^{m-1}(2r_i+2j+1)}.
\tag{A12}
\]
这是Cauchy determinant的直接代入。更重要的是
\[
\frac{V(r_1,\ldots,r_m)}{F_m}
=\det\big(\binom{r_i}{j}\big)_{i=1,\ldots,m;\ j=0,\ldots,m-1}
\in Z.
\tag{A13}
\]
所以不能只保留explicit 2幂而丢掉整数Vandermonde的全部powers。

2处A12分母全奇：
v₂(μ-minor)≥m(m−1)+2v₂(F_m)。
3处，Σr_i≥m(m−1)/2；对固定i，odd arithmetic progression的3^a倍数至多ceil(m/3^a)。令t₃=floor(log₃(6m−1))，便有
\[
v_3(\mu\text{-minor})\ge m(m-1)+2v_3(F_m)
-m\sum_{a=1}^{t_3}\left\lceil\frac m{3^a}\right\rceil .
\tag{A14}
\]
这里没有从实处正性推Fp unit，而是完整rational Cauchy式的valuation。

沿两个species作Laplace展开。每项另一半是b_gJ的m×m minor，所有entries由q_J清，故其p估值≥−m v_p(q_J)。定义明确整数
\[
L_2=m(m-1)+2v_2(F_m)-m v_2(q_J),
\]
\[
L_3=m(m-1)+2v_3(F_m)
-m\sum_{a=1}^{t_3}\left\lceil\frac m{3^a}\right\rceil
-m v_3(q_J).
\tag{A15}
\]
所有Laplace项均满足v₂≥L₂、v₃≥L₃，相加不会降低估值。这统一覆盖每个候选hole，无论它是不是actual h_*。因此
\[
c_2=\max(0,e_m(2)+L_2),\quad
c_3=\max(0,e_m(3)+L_3),\quad C_m=2^{c_2}3^{c_3}
\]
严格给
\[
\boxed{C_m\mid\mathcal N_h\quad(m\le h\le2m).}
\tag{A16}
\]
C_m是可证的共同内容因子，不冒称全部numerator的最大gcd。q_J已清固定g分母，b_g的额外valuation只帮助；所有2/3 prime powers由A12–A16处理，未排除这些prime。

Legendre factorial公式给
2v₂(F_m)=m²+O(m log m)，
2v₃(F_m)=m²/2+O(m log m)。
A14中的sum=m/2+O(log m)，而固定p处v_p(q_J)、e_m(p)/m均为O(log m)。因此
\[
L_2=2m^2+O(m\log m),\qquad
L_3=m^2+O(m\log m),\qquad
\boxed{\log C_m=(\log12)m^2+O(m\log m).}
\tag{A17}
\]
该credit不与window savings重叠：window primes随m增长，2、3处Q_m费用只有O(m log m)。也不是把同metric整格index改变冒称intrinsic变化；A16直接控制actual rational determinant的整数内容。

## 4. 真正的actual费用upper与仍未付的图预算

238证明selected δ_(h*)非零。故𝓝_(h*)是被C_m整除的非零**整数**，无须从别的minor选值或远离polynomial roots：
\[
|\mathcal D_{h_*}|\ge C_m/Q_m,\qquad
\boxed{\mathcal A_D\le\log Q_m-\log C_m,\quad
a:=\limsup\mathcal A_D/D^2\le21/2-\log12.}
\tag{A18}
\]
此界同时保留m log b_g与全部prime账，没有免费删除固定row尺度。它改善45/4约3.235，且不同于238 Chebyshev得到的费用lower。

冻结全部共同图cap C*=3π³√2/8。确有
\[
21/2-\log12<3\log C^*.
\tag{A19}
\]
可不用数值程序核：π>31/10、√2>7/5给C*>31/2；e<11/4且√e<5/3给e^(21/2)<(11/4)^10(5/3)<12(31/2)^3。因此确跨过**旧宽upper**给出的门槛，安全有效fee为(2/9)(21/2−log12)；不能据此称当前所有已付解析门槛已经打开。

单BC图的足够严格比较仍须实际
3λ>𝓙+2(21/2−log12)/3，
λ=log|φ′(0)|且𝓙为**同一合法共同图**的真实metric energy。C*只是upper，Jensen下界不是energy equality。

Root本轮指出234已付A15还保留更紧的exact all-map式，本人独立纸核其Cauchy–Schwarz改善。记𝐊(x)=∫₀^(π/2)(1−xsin²θ)^(-1/2)dθ；原生E的全图cover给
\[
|\phi'(0)|\le C_E=\frac{2\pi}{3}\mathbf K(1/9)\mathbf K(8/9).
\]
CS及tanθ代换直接给𝐊(x)²≤π²/[4√(1−x)]，故
\[
\boxed{C_E\le C_{\rm tight}:=\pi^3/2^{7/4},\qquad
3\log C_{\rm tight}<21/2-\log12.}
\tag{A20}
\]
后一比较亦可纸核：π<√10、log3<2log2、log10<5/2、log2>2/3给
9logπ+log3−(13/4)log2<125/12<21/2。
这些log界来自有限指数级数与e<11/4，无数学程序。

因此在该单BC显示入口中，𝓙≥λ使3λ−𝓙≤2log C_tight，小于2(21/2−log12)/3；**当前safe upper不能产生严格预算**。这仅关闭用此upper继续主张已获strict margin的gate，不证明实际a达到该upper，也不排除更小的真实selected费用或另一个已完整支付的判据。固定内容改进仍有效，但本轮不再追其它prime层或宣布成功；没有新数值无理性。

实际FULL输入与执行域见 literature/actual_cofactor_arithmetic_sources_round239_20261008/packet_reading_scope.md。数学程序0、扫描0、旧producer0、新primary0；只保存NEW239稿及scope，不改238、旧稿、main或manifest。保存后实际FULL作者复读，final身份另报。
