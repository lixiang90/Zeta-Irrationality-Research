# 四分之一移位的真实 rank5 模型及精确全前缀分母

日期：2026-10-06。新研究稿；不修改此前冻结的数学输入。

本稿把已校准的 T(1/4) 端点变成一个有有理 Taylor 系数的实际源，证明它的微分闭包恰为 rank5，并精确给出全部素数幂的最小前缀分母。同时把旧 forcing H 的分母上下界提升为等式。这些结论提供新的 CDT 输入；没有声称一个新的数值无理性定理，也没有 Lean 形式化验证。

## 1. 实际源、投影与规范

置 θ=x d/dx，定义
\[
c_n=\left[\frac{(3/4)_n}{(5/4)_n}\right]^4
=\left[\prod_{k=0}^{n-1}\frac{4k+3}{4k+5}\right]^4,
\qquad J(x)=\sum_{n\ge0}c_nx^n.
\tag{Q1}
\]
空积为1。这是实际有理系数的 \({}_5F_4(1,(3/4)^4;(5/4)^4;x)\)，并非只选了一个未知常数作为背景。Gamma 商渐近给
\[
c_n=Cn^{-2}(1+O(n^{-1})),\qquad
C=\left[\frac{\Gamma(5/4)}{\Gamma(3/4)}\right]^4>0.
\tag{Q2}
\]
故 J(1) 的定义绝对收敛。

沿用[冻结双边比较稿](cdt_odd_classical_M4_bilateral_reduction_20261006.md)的
\[
T(e)=\sum_{n\ge0}\left[\frac{\Gamma(n+1/2+e)}{\Gamma(n+1+e)}\right]^4,
\quad f_8=\eta(2\tau)^4\eta(4\tau)^4.
\]
该稿的全解析反射关系及已校准 M₀、M₁ 给
\[
T(1/4)=32L(f_8,2)-\frac{64}{\pi}L(f_8,3).
\]
另一方面 T(1/4)=[Γ(3/4)/Γ(5/4)]⁴J(1)。由 Γ(1/4)Γ(3/4)=π√2 和 Γ(5/4)=Γ(1/4)/4，比例因子恰为 1024π⁴/Γ(1/4)⁸。因此
\[
\boxed{J(1)=\frac{\Gamma(1/4)^8}{32\pi^4}L(f_8,2)
-\frac{\Gamma(1/4)^8}{16\pi^5}L(f_8,3).}
\tag{Q3}
\]
这是给定实际源的精确端点投影，不是关于两个未知周期自动施加数值 Galois 共轭。没有主张该恒等式在已有超几何文献中从未出现。

## 2. 四阶非齐次方程、最小秩及非分裂性

Q1 逐系数满足 (n+1/4)⁴c_n=(n−1/4)⁴c_(n−1)，n≥1。于是
\[
K_Q=(\theta+1/4)^4-x(\theta+3/4)^4,
\qquad \boxed{K_QJ=1/256.}
\tag{Q4}
\]
齐次方程与真实 P₄=θ⁴−x(θ+1/2)⁴ 的关系准确为
\[
K_Q(x^{-1/4}y)=x^{-1/4}P_4y.
\tag{Q5}
\]
[冻结单值群证明](cdt_odd_classical_spin_monodromy_20261006.md)已经证明 P₄ 的 connected monodromy 为 Sp₄、其四维标准模不可约。有限四次 cover 保持 connected Sp₄；Q5 的 Kummer twist 不改变不可约性。因此 K_Q 在 C(x) 上绝对不可约。没有把四次 cover 当成降低 CDT 秩的理由。

K_QR=1/256 没有 C(x) 有理解：在0，负整数 Laurent 阶 ρ 的最高极点因子是 (ρ+1/4)⁴，非零；在1，Q5 的局部解析且非零 gauge 给 P₄ 的 indicial roots 0,1,1,2，不容负整数极点；其余有限点是 ordinary，也不容有理特解的极点。故 R 必须是多项式。若最高项 r_dx^d 非零，K_QR 的 x^(d+1) 项为 −(d+3/4)⁴r_d，非零，不能等于常数。R=0也不解方程。

现在实际微分空间由 {1,J,θJ,θ²J,θ³J} 生成，Q4 给稳定性。可以把五维形式 companion 扩张映到实际函数空间；其四维商是上述不可约齐次模。若此映射有非零核，由于实际常数1非零，核与常数线相交为0，且其向四维商的像只能是全部商；这会给 companion 扩张的一个齐次补空间。标准非齐次 companion 扩张的此类补空间等价于一个有理特解，已被前段排除。因此五个实际函数独立，得到
\[
\boxed{\dim_{\mathbb C(x)}\langle1,J,\theta J,\theta^2J,\theta^3J\rangle=5,}
\quad 0\longrightarrow\mathbf1\longrightarrow E_J\longrightarrow E_{K_Q}\longrightarrow0
\text{ 非分裂}.
\tag{Q6}
\]
θK_Q 是 J 的五阶湮灭算子，最小阶数也是5。减去任意有理常数只改变有理 forcing，不改变实际空间 E_J；若只假设 J(1) 有理，也不能自动删掉四维背景。

## 3. 每个素数幂层的准确计数

固定奇素数 p，q=p^j，写 n=kq+r，0≤r<q。长度 q 的 numerator 和 denominator arithmetic progressions 各有一个 q 的倍数，完整 blocks 相消。

若 q≡1 (mod4)，numerator 在一个 block 中首次命中的零基序号为 (3q−3)/4，denominator 为 (q−5)/4。计数的余数阈值分别是 (3q+1)/4 和 (q−1)/4，故
\[
\delta_q(n)={\bf1}_{r\ge(3q+1)/4}-{\bf1}_{r\ge(q-1)/4}
=-1\quad\text{恰在 }(q-1)/4\le r<(3q+1)/4.
\tag{Q7}
\]
其余余数给0。最小此类 q 为5，所以这两个序号均合法。

若 q≡3 (mod4)，对应首次命中序号为 (q−3)/4 和 (3q−5)/4。因此
\[
\delta_q(n)={\bf1}_{r\ge(q+1)/4}-{\bf1}_{r\ge(3q-1)/4}
=+1\quad\text{恰在 }(q+1)/4\le r<(3q-1)/4,
\tag{Q8}
\]
其余给0。准确 valuation 为
\[
\boxed{v_p(c_n)=4\sum_{j\ge1}\delta_{p^j}(n).}
\tag{Q9}
\]
q>4n+1 时无命中，和有限。p=2 时每个 Q1 因子都是2-unit，故 v₂(c_n)=0，全部 n 同时成立。

## 4. 最小公共前缀分母的闭式

令 D_J(N) 是使所有 c_n，0≤n≤N，整数化的最小正整数，M=4N+1。对 p≡1 (mod4)，各幂层只有 Q7 的非正损失，故
\[
v_p(D_J(N))\le4\lfloor\log_p M\rfloor.
\]
置 a=⌊log_p M⌋。若 a≥1，取 n=(p^a−1)/4≤N。对全部 j≤a，p^(a−j)≡1 (mod4)，所以 n mod p^j=(p^j−1)/4，每层恰给−1；更高层没有命中。这个单个实际系数达到 −4a，证明上界恰等。

对 p≡3 (mod4)，奇数 j 的 Q8 非负，偶数 j 的 Q7 至少−1。因此
\[
v_p(D_J(N))\le4\lfloor\log_{p^2}M\rfloor.
\]
令 a=⌊log_(p²) M⌋，若 a≥1，取 n=(p^(2a)−1)/4≤N。较低偶数幂层余数是 (q−1)/4，损失−1；较低奇数幂层的 p^(2a−j)≡3 (mod4)，余数是 (3q−1)/4，准确落在 Q8 的上端点，损失0。更高层也0，故达到−4a。于是完整精确公式是
\[
\boxed{D_J(N)=
\prod_{p\equiv1\ (4)}p^{4\lfloor\log_p(4N+1)\rfloor}
\prod_{p\equiv3\ (4)}p^{4\lfloor\log_{p^2}(4N+1)\rfloor}.}
\tag{Q10}
\]
N=0时均为空积1。因为 Euler 导数只将第 n 项乘整数 n^i，而 J 本身已在基中，Q10 也是整个 Q6 五函数的最小公共前缀分母。

不能将 inert 素数完全删掉。例如 c₂=(7/15)⁴有3⁴分母，来自 q=9 的偶数层。只有 p²>4N+1 的 whole-prefix 窗口内，p≡3 (mod4) 的全部前缀系数才是 p-integral。

由算术级数素数定理 θ₁(M):=Σ_(p≤M,p≡1(4))log p=M/2+o(M)，所有 split 的 j≥2 项和所有 inert 偶数层都是 O(√M log²M)。于是
\[
\boxed{\log D_J(N)=2(4N+1)+o(N)=8N+o(N).}
\tag{Q11}
\]
首层 split 素数密度1/2，但这不把完整成本降为4N：它们的分母范围到4N+1而非2N+1。Q11 是 row-wise 前缀率，尚不是 CDT mixed evaluation determinant 的最优算术费。

## 5. 同轮补齐原 H 的精确分母

真实旧源 H(x)=Σ_(n≥1)a_nx^n，其中 a_n=(n−1)!⁴/(1/2)_(n+1)⁴。沿用[冻结共同叶算术稿](cdt_odd_classical_lambda_leaf_arithmetic_20261006.md)§5.1 已证明的全 q=p^j 计数
\[
v_p(a_n)=-4\sum_{j\ge1}\left(
{\bf1}_{n\bmod p^j\ge(p^j-1)/2}+{\bf1}_{n\bmod p^j=0}\right).
\tag{Q12}
\]
当 q>2n+1 时该层为0，n≥1、q≥3 时两指示互斥。因而 p 的最坏 denominator exponent ≤4⌊log_p(2N+1)⌋。取 a=⌊log_p(2N+1)⌋≥1，n=(p^a−1)/2≤N。因 p^(a−j) 为奇数，全部低层余数是 (p^j−1)/2，恰每层损失4，更高层没有命中。冻结稿同时给 v₂(a_n)=8n−4s₂(n−1)≥0，故
\[
\boxed{D_H(N)=\operatorname{odd}(\operatorname{lcm}(1,\ldots,2N+1))^4,\qquad
\log D_H(N)=8N+o(N).}
\tag{Q13}
\]
这里 H₀=0。n≤N 前缀与四条 Euler derivatives 的公共分母也是 Q13；原 z 坐标 H(256z) 在奇素数 valuation 不变，在2处仍整，故同一等式适用。此处精确 witness 关闭了旧稿只有4N≤logD_H≤8N的缺口，不改写旧冻结稿，且仍不宣称完整目标 F 的最优分母已得。

## 6. 解析叶与下一项必要接口

三点0,1,∞以外 Q4 ordinary。J 在0的 canonical germ 全纯，因此一周绕0固定 J 及其所有 Euler derivatives；在共同 λ 覆盖的 cyclic quotient 填0可下降为一张真实函数盘。其 omit1/unique simple0 类的 native-x capacity≤16 复用冻结[共同叶稿](cdt_odd_classical_lambda_leaf_arithmetic_20261006.md)的精确覆盖证明；这里只证明此合法类的存在，没有分类所有可填 conifold branches。

Q2 同时给 J'(x)=−C log(1−x)+O(1)，x→1−；误差来自 n c_n−C/n=O(n⁻²)，求和有界。θK_Q 是 Fuchsian 超几何算子，解在1有 moderate growth；若此实际解的局部 monodromy 平凡，则它单值且 meromorphic，而有限 J(1) 又迫其 holomorphic，与导数的 logarithmic divergence 矛盾。因此 J 在1有非零真实 monodromy；相应展开含非零 (1−x)log(1−x) 项。减去其端点常数不会消除此 monodromy。一个有理端点假设因而不够把该点直接填进共同解析叶。

新方向相较原 rank10 目标有较低实际秩和无2-denominator，但 Q11 仍有不可回避的全prefix率8。下一步必须在同一五函数、polynomial source lattice及全部graded evaluations中证明 split 素数的可计量 Smith 信用，并明确任何放大的叶确实杀掉真实 conifold 周期。没有这些接口，不能从 Q3 或 special-fiber 的 motivic factorization 直接认领 CDT 数值矛盾。

本稿纯全尺度证明；有限 rational 检查若另列，不能代替 Q6、Q10、Q13 或共同叶证明。独立审核范围将在新交付记录中列明。
