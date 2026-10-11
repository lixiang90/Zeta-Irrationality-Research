# Level12 实际共轭周期的有限 Fourier/Bernoulli 独立核对

日期：2026-10-06。本文新增，是对 [source period](cdt_odd_level12_source_period_20261006.md) §§2–5及其新 producer 规范的实际只读限定核对。没有执行该 producer，没有素数/参数扫描，没有新的无理性定理。以下有理数均以固定有限求和及手算重推，不依赖该 producer 的执行结果。

## 1. 实际 source 与共轭符号

令 χ=χ₁₂，r=√3，κ=24r=12√12。χ在1、11取+1，在5、7取−1。原 source 为

\[
 F_-=aG_1+bG_2+cG_3+d(E_χ-\kappa F_χ),
\]

而代数系数共轭 σ:r↦−r 给

\[
 F_\sigma=aG_1+bG_2+cG_3+d(E_χ+\kappa F_χ).
\tag{R1}
\]

这里只作用于 q 系数中已给的代数数，没有对未知 L 值规定一个 Galois 作用。

γ=[[7,2],[24,7]] 的 determinant1、下左entry24≡0 mod12、χ(7)=−1，M=γW₁₂=[[24,−7],[84,−24]]、M²=−12I。三 G 在 W 下anti，character C+ 在 W 下plus；γ保持 trivial部分、反号整个character部分。故 Fσ|M=−Fσ。用于 M endpoint 的真实 source 是 R1 的加号，不是原减号 source。

原稿式(6)的 quadratic 与这个 source 相符：若 fσ=θq⁻³Fσ 且两端constant0，则 Bol给 fσ+R_M fσ(Mτ) 是 degree≤2 polynomial；M²central使它位于 Sym²M 的一维 +eigenspace。canonical polynomial为 1+12(7τ−2)²，在 cusp2/7取1。因此 λσ 的有限 endpoint计算应使用 q=ρ₇² 和 R1，保留原稿的两端constant/pole抵消条件。

## 2. 普通 Lambert kernel 与三个 oldscale Tate 数

对1≤a≤6，有限 cot Fourier恒等式为

\[
 \cot(\pi a/7)=\frac17\sum_{m=1}^6(7-2m)\sin(2\pi am/7).
\tag{R2}
\]

另由 Bernoulli Fourier identity

\[
 \sum_{n\ge1}\frac{\sin(2\pi nx)}{n^3}
 =\frac{2\pi^3}{3}B_3(x),\quad
 B_3(x)=x^3-\frac32x^2+\frac12x,
\tag{R3}
\]

得到普通 T(q)=Σn⁻³qⁿ/(1−qⁿ) 的 imaginary finite part

\[
 \mathcal T(h)=\frac1{21}\sum_{m=1}^6
 (7-2[mh^{-1}]_7)B_3(m/7).
\tag{R4}
\]

B₃ 的六值为 (15,15,6,−6,−15,−15)/343，直接有限点积给

\[
 \mathcal T(h)=(12,4,0,0,-4,-12)/343.
\tag{R5}
\]

在 canonical q=ρ²处，E₄(jτ)的正次数 primitive 为240j⁻³T(qʲ)，故

\[
 G_1:\quad240\{\mathcal T(2)-\mathcal T(3)/12\}=960/343,
\]
\[
 G_2:\quad30\mathcal T(4)-10\mathcal T(5)=40/343,
\]
\[
 G_3:\quad(80/9)\mathcal T(6)-(20/3)\mathcal T(1)=-80/147.
\tag{R6}
\]

这些是普通 Lambert 的六 phase；不能将下一节的 χ-generating polynomial 的其它 phases代入 R6。

## 3. χE 与 scaledχF：Gauss 因子及 550/1029

χ-generating rational function

\[
 e_χ(z)=\frac{z-z^5-z^7+z^{11}}{1-z^{12}}
\]

在 canonical q=ρ²满足

\[
 e_χ(\rho^{2n})=\rho^n-\rho^{3n}+\rho^{4n}-\rho^{6n}.
\tag{R7}
\]

这是先在 z=ρⁿ中写 eχ(z)=z²−z³+z⁴−z⁵，再代入 z=ρ²ⁿ所得；n≡0 mod7时可去值同为0。R3于是给 Eχ primitive 的 Tate数

\[
 \mathcal E=\frac23\{B_3(1/7)-B_3(3/7)+B_3(4/7)-B_3(6/7)\}=12/343.
\tag{R8}
\]

primitive even χ 的真实 Gauss sum为 τχ=2√3=√12，并且

\[
 \chi(n)=\frac1{\sqrt{12}}\sum_{a=1}^{12}\chi(a)\cos(2\pi an/12).
\]

R3及 χ-even 的 a↦12−a配对使 χ-twisted sine sum 的因子为 2π³/(3√12)。Lambert imaginary kernel有额外1/2，cot Fourier有1/7；乘κ=12√12后总因子为

\[
 \frac{\kappa}{3\sqrt{12}\,7}=\frac47.
\tag{R9}
\]

因为 canonical h=2的inverse为4，权向量为 w=(−1,5,−3,3,−5,1)。内层四项是

\[
 I_m=B_3(\{1/12+m/7\})-B_3(\{5/12+m/7\})
     -B_3(\{7/12+m/7\})+B_3(\{11/12+m/7\}).
\tag{R10}
\]

m=1、2、3的四 arguments 依次是

\[
 (19,47,61,5)/84,\quad(31,59,73,17)/84,\quad(43,71,1,29)/84.
\]

用 B₃(n/84)=n(2n−84)(n−84)/(2·84³)直接手算，三个 signed numerator sums是156744、193032、84672，分母1185408。因此

\[
 (I_1,I_2,I_3)=(311/2352,383/2352,1/14),\quad I_{7-m}=-I_m,
\]
\[
 \sum_mw_mI_m=-2\frac{311}{2352}+10\frac{383}{2352}-6\frac1{14}
 =\frac{275}{294}.
\tag{R11}
\]

最后 R9给

\[
 \boxed{\mathcal F=\frac47\frac{275}{294}=\frac{550}{1029},\qquad
 \mathcal E+\mathcal F=\frac{586}{1029}.}
\tag{R12}
\]

这是 scaled κFχ 的 Tate数；不是 unscaled Fχ 的数。原 C−自身的 finite imaginary是 E−F=−514/1029，而真实 σsource/M-period使用 R12 的 E+F，二者均正确但作用不同。

## 4. 线性消去与非零目标

∞constant0与 ζ₃-free条件为

\[
 23d=143a+8b+7c/9,\qquad c=-99a-9b,\qquad d=(66a+b)/23.
\tag{R13}
\]

将 R6、R12代入完整 σsource Tate数后得到

\[
 \frac{960a}{343}+\frac{40b}{343}-\frac{80c}{147}+\frac{586d}{1029}
 =\frac{28164a+2434b}{483}.
\tag{R14}
\]

整数 direction (a,b,c,d)=(1217,−14082,6255,2880)的三约束直接核对为

\[
 -174031+112656-4865+66240=0,
\]
\[
 -133870+140820-6950=0,
\]
\[
 (3504960-1689840-3502800+1687680)/1029=0.
\tag{R15}
\]

目标 coefficient d=2880非零；真实 σsource endpoint 的 real part为−κdL₃χ/2=−34560√3L(3,χ₁₂)，与原稿的 λσ=−Θ相符。这里核对 source period身份，不证明 L₃χ无理性。

## 5. Radial limit 与限定审核范围

普通 Lambert regularization的 bound≤1/2适用于7|n的 pole terms：对 x=εn>0，(eˣ−1)⁻¹−x⁻¹∈[−1/2,0]。对7∤n不减x⁻¹，而以有限 root phases得到一个统一常数 bound。两部分乘n⁻³后均可 dominated convergence，不能将≤1/2的句子扩为所有phase。

有限 polynomial K_h 的严格 identity是

\[
 (1-x^h)K_h(x)-x^h\equiv-\Phi_7(x)/7\pmod{x^7-1}.
\tag{R16}
\]

所以它在非平凡7阶 roots上为0；x=1处另用真实 radial finite part−1/2。此点与字符 Eχ的 R7在 x=1可去不同。原稿的 ordinary/χ pole抵消使用 κL(4,χ)=(115/3)ζ(4)及∞zero，保留两 source整体后才取实际 radial limit。

本次实际只读审核包括原稿 §§2–5和 producer 的有限 E/F/Bernoulli规范，重推 R1–R16，通过。未运行其68checks，未在本次复核原稿 §§6–8 的非 eigen Laurent完整中间L值、双embedding整模型、Γ/Hauptmodul与filled leaves；这些数学输入应由其各自独审承担。特别不把 genus0、真实period或本固定 finite sum 当成已完成CDT预算。
