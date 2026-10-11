# 互补四分之一源：Γ-free 临界周期目标与完整素数层

日期：2026-10-06。本轮NEW纯证明；仅只读上一轮冻结模型、bilateral校准与原稿，不执行或import旧数学producer。没有新的数值无理性定理。

## 1. 新的有理初值源及精确临界周期

令θ=x∂ₓ，定义
\[
A(x)=\sum_{n\ge0}\left[\frac{(1/4)_n}{(3/4)_n}\right]^4x^n,
\quad J(x)=\sum_{n\ge0}\left[\frac{(3/4)_n}{(5/4)_n}\right]^4x^n,
\quad C_a=\left[\frac{\Gamma(a+1/2)}{\Gamma(a)}\right]^4.
\tag{A1}
\]
J是[上一轮实际rank5源](cdt_odd_quarter_shift_full_model_20261006.md)，A是其互补shift。两者在1绝对收敛。冻结[双边反射](cdt_odd_classical_M4_bilateral_reduction_20261006.md)的T(e)、M₀、M₁在共同全纯带−1/2<Re e<1满足
\[
\cos^4(\pi e)T(e)+\sin^4(\pi e)T(1/2-e)
=M_0-\frac{M_1}{2\pi}\sin(2\pi e).
\tag{A2}
\]
e=−1/4合法，不是跨越Gamma极点的形式代入。Gamma recurrence和一次移位给
\[
T(3/4)=T(-1/4)-C_{1/4}^{-1}.
\]
代入A2，即
\[
T(-1/4)=2M_0+M_1/\pi+\tfrac12C_{1/4}^{-1}.
\]
结合已证T(1/4)=2M₀−M₁/π，准确端点为
\[
\boxed{A(1)=\tfrac12+C_{1/4}(2M_0+M_1/\pi),
\quad J(1)=C_{3/4}(2M_0-M_1/\pi).}
\tag{A3}
\]
Γ(5/4)=Γ(1/4)/4给C_(1/4)C_(3/4)=1/256。因此实际有理初值函数
\[
Q(x)=(A(x)-\tfrac12)J(x),\qquad Q(0)=\tfrac12,
\]
有完全消去Γ规范的端点
\[
\boxed{Q(1)=\frac{4M_0^2-M_1^2/\pi^2}{256}
=4L(f_8,2)^2-\frac{16}{\pi^2}L(f_8,3)^2.}
\tag{A4}
\]
这是明确的新可研究数值目标，而不是证明它无理。A4是项目已有经典输入的严格推论，未主张文献首创。这里Γ消去发生在真实函数的乘积，不以未知周期作数值Galois操作。

## 2. 实际微分模型：不把上界当最小秩

A满足
\[
K_AA=1/256,\qquad K_A=(\theta-1/4)^4-x(\theta+1/4)^4.
\tag{A5}
\]
准确gauge K_A(x^(1/4)y)=x^(1/4)P₄y；P₄=θ⁴−x(θ+1/2)⁴。冻结P₄ connectedSp₄输入保持不可约四阶商。常数forcing无C(x)有理特解：0处根1/4不容负整数极点；1处gauge解析非零、根0,1,1,2不容负整数；其它有限点ordinary。多项式最高项在K_A中产生−(d+1/4)⁴a_dx^(d+1)，不能等于常数。

同上一轮实际kernel/不可约商证明，{1,A,θA,θ²A,θ³A}因此恰rank5、扩张非分裂。native x中A本身有有理Taylor系数；齐次gauge的四次覆盖不减实际rational-variable秩。

两个真实rank5系统的25个乘积
\[
1;\quad \theta^iA,\theta^jJ\ (0\le i,j\le3);\quad
(\theta^iA)(\theta^jJ)\ (0\le i,j\le3)
\tag{A6}
\]
在Q(x)上构成明确derivation-closed生成空间：各θ⁴通过A5和既有K_Q消去，θ乘积用Leibniz rule。这先给25行安全上界；本轮另建[完整19行模型](cdt_odd_quarter_product_rank19_interface_20261006.md)，用相反Kummer gauge与对称乘积准确删去六个反对称方向，逐行写出有理微分闭包，得到Q最小阶数≤19。**未证明实际最小秩19、完整两个扩张的PVradical或Q的cyclic秩；不能在CDT中把19当已证独立函数数。** 端点Γ消去也不证明两个实际扩张分裂。

## 3. A的准确素数幂计数及最小前缀分母

写 a_n=[Π_(k=0)^(n−1)(4k+1)/(4k+3)]⁴。对奇素数p、q=pʲ、n=kq+r，0≤r<q，完整长度q blocks相消。q≡1(mod4)时，numerator/denominator首次命中序号为(q−1)/4、(3q−3)/4，所以单层
\[
\delta_q^A(n)={\bf1}_{r\ge(q+3)/4}-{\bf1}_{r\ge(3q+1)/4}
=+1\quad\text{恰在 }[(q+3)/4,(3q+1)/4).
\tag{A7}
\]
q≡3(mod4)时，首次序号为(3q−1)/4、(q−3)/4，故
\[
\delta_q^A(n)={\bf1}_{r\ge(3q+3)/4}-{\bf1}_{r\ge(q+1)/4}
=-1\quad\text{恰在 }[(q+1)/4,(3q+3)/4).
\tag{A8}
\]
v_p(a_n)=4Σ_jδ_(pʲ)^A(n)，q>4n−1无贡献，n=0各层零，v₂(a_n)=0。特别所有p≡1(mod4)处，A的**全部无限Taylor系数**都p-integral；这里不是只在p²窗口内得出整性。

对N≥1置M=4N−1、b_p=⌊log_pM⌋。p≡3(mod4)只有奇数j层可负，故最大亏损≤4⌈b_p/2⌉。若有负层，取最大奇数s≤b_p及n=(pˢ+1)/4≤N。每个较低奇数层q的余数是(q+1)/4，恰在负带左端；每个较低偶数层余数是(3q+1)/4，恰为正带右端，因此贡献零。高层无命中。这一实际系数达到所有许可负层，给精确最小公共分母
\[
\boxed{D_A(N)=\prod_{p\equiv3(4)}p^{4\lceil\lfloor\log_p(4N-1)\rfloor/2\rceil},
\quad D_A(0)=1.}
\tag{A9}
\]
AP-PNT及高幂小项给logD_A(N)=8N+o(N)。A只有inert奇层的分母，J既有split全部层/inert偶层；此互补结构不是双方每层分母成本自动相消。

## 4. 乘积的全部地方与真实conifold

Q的n≤N系数是有限有理convolution。无穷多p²>4N+1的whole-prefix窗口里，每个素数只在其中一个因子有首层亏损−4，另一因子p-integral。因此Q的全部系数亏损至多−4，不能按两个任意p⁴分母粗称−8。但首层现在覆盖两类odd primes，密度恢复为1，必须付全量费用。

一般prefix可安全用2D_A(N)D_J(N)清全部Q系数：各因子index≤N，A−1/2只需固定2。于是log安全分母≤16N+o(N)，2处仅固定分母2，没有dyadic指数主项。此为明确的可认证bound，不是Q最小公共分母或mixed determinant最优費。相关Euler derivatives只乘整数，不增加分母。

另可证明最小prefix分母的准确主率。设D_Q(N)为q₀,…,q_N的最小公共分母。对p²>4N+1：若p≡1(4)，J的首次亏损在h=(p−1)/4，A的全部系数p-integral；q_h的唯一亏损项为(A₀−1/2)j_h=j_h/2，其余卷积项整，故v_p(q_h)=−4。若p≡3(4)，A的首次亏损在h=(p+1)/4，J在整个prefix整；q_h的唯一亏损项为a_hJ₀=a_h，同样v_p(q_h)=−4。凡h≤N的这些素数均必须进入D_Q(N)。除至多O(√N)个小素数及区间端点外，这覆盖全部odd p≤4N。PNT给logD_Q(N)≥16N+o(N)，结合上述安全上界得到
\[
\boxed{\log D_Q(N)=16N+o(N).}\tag{A10}
\]
这只是准确指数主率，不声称已给D_Q(N)的每个高幂指数，也不等于原19行整格的CDT transport费用。

Q在1有限并有非零真实log²项。令t=1−x，convergentFuchsian local expansions给A=A(1)+C_(1/4)tlogt+analyticterms及higher tᵏlogt；J同理系数C_(3/4)。A−1/2不改log。于是Q的t²log²t系数为C_(1/4)C_(3/4)=1/256≠0。完整有限乘积是regular-singular tensor系统的解，局部log²monodromy不能由一个纯analytic项或其它单log项消去。减去Q(1)常数因而不赋予一个filledconifold叶。

另稿准确识别全部 arithmetic-initial、原点全纯的Sym²P₄ homogeneous背景为二维，并证明其中没有代数常数校正能取消Q的双log；该否定只限这个明确的背景空间。下一项必要工作是19行模型的actual rank与原整评价的混合Smith信用，或其它新的inhomogeneous周期源。A4同时给具体Γ-free目标；它没有消去conifold branch，也不能据此认领新数值无理性。

本轮 current_full_source 实际全文独审原 §§1–4，通过 A2–A9、真实完整prefix费用与conifold；root实际全文独审新19行接口及其全部素数层和双log障碍。最终19行链接和限定范围另记于本轮root review。未执行旧或peer producer，没有有限checks或Lean声明。
