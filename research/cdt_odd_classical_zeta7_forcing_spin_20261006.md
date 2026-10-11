# 经典ζ(7)：forcing接入同一四阶超几何模块的twisted扩张

日期：2026-10-06。新纯Markdown正接口，不运行producer、不改变冻结输入。使用[经典导数源](cdt_odd_classical_derivative_projection_20261006.md)的真实forcing；不同于[hypergeometric特解障碍](cdt_odd_classical_zeta7_forcing_20261006.md)，这里研究forcing自身的actual differential module。证明forcing的实际秩恰为5、扩张非split，以及完整ζ(7)目标的安全秩上界10；不声称完整目标的最小秩、geometric realization或新数值定理。

## 1. 一个明确的actualforcing函数与四阶非齐次方程

令x=256z、θ=x d/dx，定义实际analytic germ

\[
 H(x)=\sum_{n\ge1}a_nx^n,\qquad
 a_n=\frac{(n-1)!^4}{(1/2)_{n+1}^4}.
 \tag{S1}
\]

该式在|x|<1收敛，因为a_(n+1)/a_n=n⁴/(n+3/2)⁴趋于1。a1=256/81；对n≥2有(n+1/2)⁴a_n=(n−1)⁴a_(n−1)。逐系数严格给

\[
 \boxed{K H=16x,\qquad K=(\theta+1/2)^4-x\theta^4.}
 \tag{S2}
\]

x的一阶系数为(3/2)⁴a1=16，H0=0。没有采用某个formal characteristic solution代替该实际germ。等价显式表达是

\[
 H(x)=\frac{256x}{81}\,{}_5F_4
 \left(1,1,1,1,1;\frac52,\frac52,\frac52,\frac52;x\right).
 \tag{S3}
\]

这里只是同一actual power series的重新表达；其最小阶数在第4节由实际模块证明，不由这个超几何写法直接推出。

## 2. ζ(7)非齐次源的forcing完全由H给出

以C₂(x)=Σ C_n,2(x/256)ⁿ。设旧五阶算子在x坐标为

\[
 L_5=\theta^5-\frac{x}{8}(2\theta+1)
 (8\theta^4+16\theta^3+20\theta^2+12\theta+3)
 +x^2(\theta+1)^5.
 \tag{S4}
\]

冻结forcing是G_n=−384n²(48n³+80n²+40n+5)256ⁿa_n。原generating equation初值项245760z必须保留，因此严格有

\[
 \boxed{L_5C_2(x)=960x-\frac32x\theta^2
       (48\theta^3+80\theta^2+40\theta+5)H(x).}
 \tag{S5}
\]

它对真实线性形式生成函数F₂=C₂+91440ζ(7)A(x/256)仍成立，因为L5A=0。没有赋值或Galois作用于未知ζ(7)。

## 3. 齐次K的exactcontiguous接口

定义

\[
 P_-=\theta^4-x(\theta-1/2)^4,\qquad
 P_+=\theta^4-x(\theta+1/2)^4.
 \tag{S6}
\]

若KH=0，设v=x^(1/2)H，则P−v=0。因此homogeneous K在二次coverQ(x,√x)上与P−通过gauge等价；在Q(x)上可表为P−的quadratic character twist。

令T=(θ−1/2)⁴。对P−v=0，θ⁴v=xTv；θ与T交换，且T x=x(θ+1/2)⁴。因而

\[
 \theta^4Tv=T\theta^4v=TxTv=x(\theta+1/2)^4Tv,
 \qquad P_+(Tv)=0.
 \tag{S7}
\]

这个solution map没有kernel：若Tv=0且P−v=0，则θ⁴v=0。局部v是log(x)的degree≤3 polynomial；而Tv=0的局部solutions是x^(1/2)乘degree≤3的log polynomial。这两个spaces只交0。也可用θ⁴与(θ−1/2)⁴这两个coprime constant-coefficient polynomials的Bézout identity立即推出v=0。

两个regular-point solution spaces均dimension4，故T是isomorphism。更明确，选择U(X),V(X)∈Q[X]满足U(X)X⁴+V(X)(X−1/2)⁴=1；在P−solution上

\[
 v=\{U(\theta)x+V(\theta)\}\,Tv.
 \tag{S8}
\]

这给rational differential inverse，不仅是注入的solution map。因此K的齐次module是同一P+四阶超几何module的quadratic twist。这个P+恰是root的新spin/exterior-minor模型入口；(S6–S8)本身不依赖该外幂证书执行或几何解释。

实际H满足KH=16x，仍是rank4齐次module的非齐次extension。不能把(S7)对齐次solutions的isomorphism当作它的forcing特解，也不能丢掉16x。gauge后实际v满足P−v=16x^(3/2)，不是P−v=0。

## 4. forcing的实际秩5、非split扩张与完整目标的安全上界

先严格排除微分方程(S2)的有理函数特解。这与第1份forcing稿的有理差分/超几何特解排除是两个不同命题。

**命题。**不存在r(x)∈C(x)满足Kr=16x。

证明：K在x=0的Euler indicial是(ρ+1/2)⁴。若r在0有极点，最低Laurent指数ρ是负整数，该系数非零，而右端16x没有负次项，矛盾。在x=1，置u=x−1，写

\[
 K=(1-x)\theta^4+2\theta^3+\frac32\theta^2
       +\frac12\theta+\frac1{16}.
 \tag{S9a}
\]

作用于u^ρ的最低项u^(ρ−3)系数为

\[
 -\rho(\rho-1)(\rho-2)(\rho-5).
 \tag{S9b}
\]

所有根为非负整数0、1、2、5，故负整数极点同样不可能。其他有限点的最高普通导数系数为(1−x)x⁴，非零；若有极点，最高导数产生唯一最低Laurent项，不能等于analytic右端。因此r没有任何有限极点，是多项式。若degree d≥1，−xθ⁴r产生非零最高项−d⁴r_d x^(d+1)，而其余项degree≤d；它不能等于degree1的16x。常数r满足Kr=r/16，也不可能。命题得证。

[实际spin/单值群证明](cdt_odd_classical_spin_pullback_20261006.md)第3节给P+的connected Zariski单值群Sp₄，故其四阶微分模块绝对不可约，且有限代数cover后仍不可约。由第3节的exact contiguity及quadratic twist，齐次K模块也在C(x)上绝对不可约。这一步使用实际单值群证明，不用“order4”本身代替不可约性。

由(S2)，H、θH、θ²H、θ³H、x的Q(x)-span对θ稳定：θx=x、θ⁴H可用K H=16x消去。故actual forcing closure维数≤5。

令W_H为H生成的实际微分函数模块，扩标量到C(x)。因为KH=16x，它包含一维trivial模块C(x)·x。商W_H/(C(x)·x)由实际bar H循环生成，且被K消去；若bar H=0，则H∈C(x)，与上面的有理特解排除矛盾。因此这个商是非零的不可约K模块商，维数恰为4。严格得到

\[
 \boxed{\dim_{\mathbf Q(x)}W_H
        =\dim_{\mathbf C(x)}W_H=5.}
 \tag{S9c}
\]

Q(x)维数不超过5，而C(x)维数已是5，故两者相等。这里的W_H是实际函数及其导数的模块；若改用horizontal solution fiber，需要相应取对偶，不能混用两个约定。

扩张

\[
 0\longrightarrow\mathbf C(x)\,x\longrightarrow W_H
 \longrightarrow K_{\mathrm{hom}}\longrightarrow0
 \tag{S9d}
\]

非split。若存在与θ交换、在C(x)·x上为identity的投影π，则π(H)∈C(x)，且Kπ(H)=π(KH)=16x，给被排除的有理特解。这是微分扩张非split的证明，不把“无超几何序列特解”误用成该结论。

由(S5)，C₂、θC₂、…、θ⁴C₂再加这五个H方向构成θ-stable实际span；高阶forcing derivatives由(S2)归约。于是

\[
 \boxed{\operatorname{rank}_{\mathbf Q(x)}
       \langle C_2,\theta C_2,\ldots\rangle\le10.}
 \tag{S9}
\]

固定numeric ζ(7)的实际F₂同样有C(x)-closure≤10；假设ζ(7) rational则同一Q(x)-model可用。这里没有证C₂或F₂的actualrank为10，也没有证完整目标扩张是否split。原L5的实际五阶齐次部分与本节实际rank5 forcing仍需作为完整模型一起核算；两个rank5模块的存在不能自动把特定目标germ的最小阶数加成10。

该接口把ζ(7)forcing定位为同一超几何/VHS候选的twisted非齐次扩张，给下一步monodromy、connection constants、geometric period和整模型的具体目标。尚未有真实regular叶、共同capacity、CDT成本矛盾或ζ(7)无理性结论。

## 5. 实际审阅状态

纯Markdown，无producer与finitechecks。root实际全文审核系数recurrence、exact contiguity/Bézout、安全closure以及第4节新增的有理微分特解排除、actual rank5和非split证明，通过；未执行任何producer。helper_tensor_budget实际只读第4节(S9a–d、S9)，独核两个indicial、全部有限pole/多项式degree排除、条件于已证Sp₄不可约输入的quotient rank4、actual rank5与split投影矛盾，通过；未重新审阅Sp₄、几何或capacity。本文现冻结。

旧冻结源及新spin证书均未执行/import。新增结论依赖已证明的实际Sp₄单值群，而不是有限Taylor样本。完整C₂/F₂ rank、完整扩张、整周期格、真实regular叶与CDT数值差额仍未闭合。
