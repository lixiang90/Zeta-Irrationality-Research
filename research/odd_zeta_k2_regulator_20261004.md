# Catalan 长度二端点积分：绝对 regulator 归零与非零 Bloch 端点类

日期：2026-10-04。独立审计冻结的 [椭圆商报告](E:/kimi-build/zeta5/research/odd_zeta_cover_elliptic_quotients_20261004.md) 中 (9)、(11)，不改变其脚本和结论。本文固定 real regulator 的微分为

\[
\eta(f,g)=\log|f|\,d\arg g-\log|g|\,d\arg f.
\]

闭合周期常用的归一化是 `(2π)⁻¹∫η`；下文所有积分先不除 `2π`，以免把这个常数混入 Catalan 恒等式。

本轮可以完整证明：原符号 `T` 的绝对 real regulator 为零；原来的 `G` 却是选定符号代表的开放路径积分，准确为 `∫γη_T=−4G`。进一步，在 `T⊗Q=0` 的 transfer 结论上，可以非显式构造有限 Steinberg 链；其经对称平均后的 Bloch 端点差，在 `L=Q(i,√2,√3)` 上准确等于 `−4[i]`。这解释了非零端点信息的所在，但没有给出非零椭圆 K₂ 类、算术整模型输入或无理性证明。

## 1. 固定曲线、函数和路径

记 `a=√2`、`b=√3`、`K=Q(i,a)`。在

\[
C:\quad Y^2=s^8-14s^4+1
\]

上考虑 `σ(s,Y)=(−s,Y)`、`τ(s,Y)=(1/s,Y/s⁴)` 和超椭圆对合 `ι(s,Y)=(s,−Y)`。两个商的共同纵坐标是 `y=Y/s²`：

\[
E_+: x=s+s^{-1},\quad y^2=x^4-4x^2-12;
\qquad
E_-: x=s-s^{-1},\quad y^2=x^4+4x^2-12.
\]

函数仍采用冻结报告的归一化：

\[
u_+=\frac{x+a}{x-a},\quad r_+=\frac{i x(6-x^2)}a,
\quad F_+=\frac{y-r_+}{y+r_+};
\qquad
u_-=\frac{x-ia}{x+ia},\quad r_-=\frac{x(x^2+6)}a,
\quad F_-=\frac{y-r_-}{y+r_-}.
\]

写 `S±={u±,F±}`、`T=π₊*S₊+π₋*S₋`，并写 `η_T` 为相同显式符号代表的两项 `η` 之和。冻结报告已精确检查 `T` 在所有水平点的 tame 均为 `1`。

取

\[
P_+=(0,1),\qquad s_0=\frac{a(b-1)}2=\sqrt{2-\sqrt3},
\qquad B_+=(s_0,0),
\]

`γ` 是从 `P₊` 到 `B₊`、`s∈[0,s₀]`、`Y≥0` 的原实路径。其投影端点为 `E₊:(ab,0)=(√6,0)`、`E₋:(−a,0)`。`logu±` 从基点取值 `0` 沿这条路径连续延拓。原已认证的真值相消给

\[
G=\frac i4(I_++I_-),\qquad
I_\pm=\int_{\pi_\pm\gamma}\log u_\pm\,d\log F_\pm. \tag{1}
\]

此处 (1) 是此前已证的固定积分恒等式，不是通过 regulator 非零或 `G` 无理性推出来的。

## 2. 复 primitive 与 real regulator 的必要边界项

任取连续分支 `logu=A+iψ`、`logF=B+iφ`，其中 `A=log|u|`、`B=log|F|`。直接展开给

\[
\boxed{\operatorname{Im}(\log u\,d\log F)
=\eta(u,F)+d(\arg u\cdot\log|F|).} \tag{2}
\]

所以一般不能把 `logu dlogF` 的虚部直接称为 regulator 微分，必须核算两端的 `ψB`。标准闭合 K₂ pairing、tame 与局部环的关系，以及 `η(h,1−h)=dD(h)`，可见 [Dokchitser–de Jeu–Zagier，math/0405040v2，§3](https://arxiv.org/pdf/math/0405040v2)。`D` 是 Bloch–Wigner dilogarithm。

本路径上的符号和分支可以完全控制：

| 商 | 路径内的 `u` | 路径内的 `F` | 连续分支与端点 |
|---|---|---|---|
| E₊ | `u₊>1`，实正 | `|F₊|=1` | `argu₊=0`；`argF₊` 从 `π` 降至 `0` |
| E₋ | `|u₋|=1` | `F₋<−1`，实负 | `argu₋=2arctan(a/|x|)` 从 `0` 升至 `π/2`；`argF₋=π` |

证明所需的符号事实如下。E₊ 的 `x` 从 `+∞` 降至 `√6`、`y>0`；`r₊=−ik`，`k=x(x²−6)/a>0`，故 `F₊=(y+ik)/(y−ik)`。在无穷远 `k/y→∞`，在分支点 `k/y→0`，故上表的相位连续。

E₋ 的 `x` 从 `−∞` 升至 `−a`，`r₋<0`，而

\[
y^2-r_-^2=-\tfrac12(x^2+2)^2(x^2+6)<0.
\]

于是 `|r₋|>y`、`F₋=(y+|r₋|)/(y−|r₋|)<−1`。在两端 `F₋→−1`，所以 `log|F₋|→0`。E₊ 的 `log|F₊|` 沿路径恒为零；E₋ 的边界乘积也在两端为零。由 (2) 得

\[
\boxed{R:=\int_\gamma\eta_T
=\operatorname{Im}(I_++I_-)=-4G.} \tag{3}
\]

端点单位值准确为

\[
\begin{array}{c|cccc}
&u_+&F_+&u_-&F_-\\\hline
P_+&1&-1&1&-1\\
B_+&2+\sqrt3&1&i&-1.
\end{array} \tag{4}
\]

其中 `F₊(B₊)=1` 必须用曲线局部参数判断：`y=t`、`x=√6+O(t²)`、`r₊=O(t²)`，所以 `(t−r₊)/(t+r₊)→1`；不能直接把 `0/0` 当值。

复恒等式 (1) 的分支仍有实际意义。若把 `logu₊` 整体增加 `2πim`，则 `∫dlogF₊=−iπ`，`I₊` 增加 `2π²m`。这不改变 (3) 的虚部，却改变 (1) 的复表达。E₋ 的 `∫dlogF₋=0`。因此 (1) 必须保持基点 `logu±=0` 的归一化；(3) 则使用无分支的实微分和已核算的边界项。

## 3. 全部绝对 real regulator 周期都为零

`σ` 在两个商上都把 `x` 变为 `−x`，同时保留 `y`；`τ` 保留 E₊ 的 `x`，把 E₋ 的 `x` 变为 `−x`。每次 `x→−x` 都使相应 `u`、`F` 同时变逆。因此 `σ*T=τ*T=T`，且显式实微分本身满足

\[
\sigma^*\eta_T=\tau^*\eta_T=\eta_T.
\]

共同商是有理圆锥：

\[
D=C/V_4:\quad W^2=R_0^2-16,
\qquad R_0=s^2+s^{-2},\quad W=Y/s^2,
\]

\[
t=(R_0+W)/4,\qquad R_0=2(t+t^{-1}),\quad W=2(t-t^{-1}). \tag{5}
\]

原路径在这个商上从 `t=∞` 走到 `t=1`，仍是开放路径；商的 genus 为零本身不把它变成闭合周期。

所以 `H¹(C(C),R)^V₄≅H¹(P¹(C),R)=0`。另一方面 `T` 的水平 tame 为 `1`，使每个被删点的小环积分为零；局部对数奇性是可积的，regulator 类属于整条光滑射影曲线的 `H¹`。该类既在零不变子空间内，就必须为零。结论是

\[
\boxed{\int_\Gamma\eta_T=0\quad\text{对每条闭合一周类 }\Gamma.} \tag{6}
\]

这个独立证明只用曲线对称性与 tame，不需要先证明 `T` torsion。若采用根分支已证的更强 `4T=0`，real regulator 杀 torsion 也立即给 (6)。

为使下面的 Steinberg 链入口自足，这里列出 `4T=0` 的标准代数论证。`K(C)/K(t)` 是 V₄ 的次数 `4` 扩张；令 `N` 为 Milnor K₂ transfer。restriction–transfer 给 `res N(T)=Σg*gT=4T`。residue–transfer 兼容使 `N(T)` 在 `K(t)` 的全部有限点 tame 为 `1`；有理函数域的 Bass–Tate 正合列迫使 `N(T)` 来自常数 `c∈K₂(K)`。于是 `4T=res c`。在 `P₊` 特化时 (4) 给 `T(P₊)=0`，故 `c=0`，得 `4T=0`。此处用的是函数域 Milnor K₂ 及单位特化，不把它擅自提升为某个指定整模型 Quillen K₂ 类。transfer、residue 与特化的标准依据是 [Rost，Chow Groups with Coefficients，Theorem 1.4、R1c/R3b/R3d、Proposition 2.2](https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf)。

## 4. 明确闭合实路径：非零端点项在四段中相消

令 `P₋=(0,−1)`、`B₋=(−s₀,0)`。`ι*η_T=−η_T`，而 `σ*η_T=η_T`。四条保持原方向的路径及积分为

\[
\begin{array}{c|c|c}
\text{路径}&\text{端点}&\int\eta_T\\\hline
\gamma&P_+\to B_+&R\\
\iota\gamma&P_-\to B_+&-R\\
\iota\sigma\gamma&P_-\to B_-&-R\\
\sigma\gamma&P_+\to B_-&R.
\end{array}
\]

因此实 oval 的闭合链可取

\[
\Gamma=\gamma-\iota\gamma+\iota\sigma\gamma-\sigma\gamma,
\qquad \partial\Gamma=0,\qquad\int_\Gamma\eta_T=0. \tag{7}
\]

`γ−ιγ` 虽然连接两层的基点，但其边界为 `P₋−P₊`，不是闭合 cycle，积分为 `2R=−8G`。

由 (6) 可取全局实 primitive `Φ`，在有限奇点按连续极限延拓，令 `Φ(P₊)=0`。于是

\[
\Phi(B_+)=\Phi(B_-)=-4G,\qquad \Phi(P_-)=-8G,
\]

\[
\sigma^*\Phi=\Phi,\qquad \iota^*\Phi=-\Phi-8G. \tag{8}
\]

这些端点常数解释 (3) 与 (6) 如何同时成立。相对实上同调 `H¹(C,{P₊,B₊};R)` 中的 `[η_T,0]` 位于 `H⁰({P₊,B₊})/H⁰(C)` 所给的一维端点部分，且与 `γ` 的 pairing 为 `−4G`。这是完整的相对实上同调结论；单靠它不能指定相对 motivic K₂ lift 所需的代数端点 trivialization。

## 5. 修正单商 tame 的简单候选仍然没有绝对椭圆 regulator

在两个 E± 上同取

\[
v=\frac{y-4i}{y+4i},\qquad
A_+=2S_+-\{2,v\},\qquad A_-=2S_-+\{2,v\}. \tag{9}
\]

`y=4i` 的相应两点上 `ordv=2`，`y=−4i` 的两点上 `ordv=−2`，因为 `y²+16=(x²∓2)²`；没有其他有限零极点。在 E₊，`tame S₊` 分别为 `2,1/2`；在 E₋ 则相反。`tame{2,v}=2^ordv`，所以 (9) 的全部水平 tame 都为 `1`。共同拉回满足 `π₊*A₊+π₋*A₋=2T`。

但是 `κ:(x,y)↦(−x,y)` 同时反转 `u,F`、保留 `v`，故 `κ*A±=A±`。其商 `E±/κ` 为 genus `0`，`κ` 在 `H¹(E±)` 上作用为 `−1`。因此两个修正类的绝对 real regulator 也都为零。这个恒定 tame 修正并未制造新的非零椭圆候选。

开放路径的修正则可精确计算。在两条投影上 `|v|=1`，连续 `argv=−2arctan(4/y)` 从 `0` 降到 `−π`，故

\[
\int\eta(2,v)=-\pi\log2.
\]

若 `R±=∫π±γη(S±)`，则

\[
\int\eta(A_+)=2R_++\pi\log2,\qquad
\int\eta(A_-)=2R_--\pi\log2. \tag{10}
\]

两项相加正好为 `−8G`。忽略这两个相反的 `πlog2` 边界贡献，会错误识别单商的真实积分。

## 6. 可证明的有限 Steinberg 链与端点 Bloch kernel 引理

本节只在有理系数工作。对于任意域 `F`，以 `P₂(F)_Q` 表示由 `[h]`、`h∈F\{0,1}` 生成、再模去五项关系的 pre-Bloch 群，并采用

\[
\delta[h]=h\wedge(1-h),\qquad
\mathcal B(F)_Q=\ker\delta.
\]

此方向与 GL 的 `(1−h)∧h` 相反，相应地本报告使用 `dD(h)=η(h,1−h)`；不混用两种符号方向。Matsumoto 正合性表示 `K₂(F)_Q` 是外平方除以这些 Steinberg 元素。可见 [Goncharov–Levin，alg-geom/9508008v4，§1.6 的 Bloch–Suslin 正合列](https://arxiv.org/pdf/alg-geom/9508008v4)；与 K₃ 的精确联系由 [Suslin，Theorem 5.2](https://www.maths.dur.ac.uk/users/herbert.gangl/Suslin_K3_Bloch_group.pdf) 给出。

令 `F=K(C)`，并在外平方中写

\[
w=(\pi_+^*u_+)\wedge(\pi_+^*F_+)
+(\pi_-^*u_-)\wedge(\pi_-^*F_-).
\]

`T⊗Q=0` 表示存在一个实际有限、但本文没有显式求出的自由链

\[
\varepsilon_0=\sum_{\ell=1}^m q_\ell[h_\ell],\quad q_\ell\in\mathbb Q,
\qquad\delta\varepsilon_0=w. \tag{11}
\]

这里只是有限代数存在命题，不依赖任何 Beilinson 猜想，也不要求先算出 `hℓ`。

**端点 kernel 引理。** 设 `P` 的剩余域为 `L`，`w` 的各符号两项均在 `P` 为单位，且单位特化 `w(P)=0` 在 `Λ²L×_Q` 中成立。对满足 (11) 的任意有限自由链，按逐项取值定义

\[
\varepsilon_P=\sum_{h_\ell(P)\notin\{0,1,\infty\}}q_\ell[h_\ell(P)].
\]

则 `δε_P=0`，所以它给一个 `B(L)_Q` 的类。这里不是声称“省去 0,1,∞”总能在整系数 pre-Bloch 群上定义规范特化；我们只证明这个特定有限链的有理 kernel 性质。

证明：选局部参数 `t`，对 `h=t^m a`、`a` 为单位，取 leading-unit evaluation `λ_t(h)=a(P)`。这是 `F×→L×` 的乘法映射。若 `m>0`，则 `λ_t(h)∧λ_t(1−h)=a(P)∧1=0`；若 `m<0`，它为 `a(P)∧(−a(P))=0`，最后一步使用有理系数杀掉 `−1` 的 torsion。若 `m=0` 而 `h(P)=1`，第一因子为 `1`，仍为零。其余情况正好为 `δ[h(P)]`。把 `Λ²λ_t` 应用于 (11) 就得到 `δε_P=w(P)=0`。证毕。

在本问题中取 `L=Q(i,a,b)`。由 (4)，`w(P₊)=0`，而

\[
w(B_+)=(2+b)\wedge1+i\wedge(-1)=0
\quad\text{在有理外平方中}.
\]

因此定义

\[
\beta=\varepsilon_{B_+}-\varepsilon_{P_+}\in\mathcal B(L)_Q. \tag{12}
\]

Bloch–Wigner 函数在 `0,1,∞` 连续取值 `0`，(11) 又给 `dD(ε)=η_T`。沿路径分段积分、在有限零极点取连续极限，即得

\[
\boxed{D(\beta)=-4G.} \tag{13}
\]

这已经给一个非显式的真正数域 Bloch 类：`G=Σk≥0[(4k+1)⁻²−(4k+3)⁻²]>0`，所以其 regulator 非零。这里使用严格的正项恒等式，而非数值精度或把 `G>0` 当作 `T≠0` 的证据。

## 7. 后续补上的身份：有限对称平均后，端点类准确等于 −4[i]

本节记录与根分支交叉复核后补上的身份；完整平均、下降及后续预算分析另见 [端点 Bloch 类报告](E:/kimi-build/zeta5/research/odd_zeta_bloch_boundary_20261004.md)。身份的范围是有理 Bloch 群。令 `aFlip` 为 `K/Q(i)` 的非平凡元素；它把 `a` 变为 `−a`，同时使 `u±,F±` 都变逆。`w` 因而在 `V₄` 和 `aFlip` 下不变。它们可交换，故将 (11) 的自由链替换为

\[
\varepsilon=\frac18\sum_{g\in V_4\times\langle aFlip\rangle}g\varepsilon_0 \tag{14}
\]

后，仍有 `δε=w`，且链在这个有限群下 literal invariant。每个函数仍属于 `K(C)`，因此没有 `b` 系数。

把 (12) 中的链取为 (14)。记 `bFlip` 把 `b` 变为 `−b`。端点的精确 Galois 作用为

\[
aFlip(B_+)=\sigma B_+,\qquad
bFlip(B_+)=\sigma\tau B_+,
\]

因为 `aFlip(s₀)=−s₀`、`bFlip(s₀)=−1/s₀`。`P₊` 的坐标是有理数；在 `aFlip` 下系数与端点链的固定性由 (14) 保证，在 `bFlip` 下链无 `b` 系数且 `P₊` 本身固定。注意这里没有声称 `στ(P₊)=P₊`。

逐项端点评价与这些作用相容，`0,1,∞` 也保持为应省去的值，故 `β` 在 `Gal(L/Q(i))` 下 literal invariant，当然也在 `B(L)_Q` 中不变。

`L` 有四对复嵌入；可以选取全部四个固定 `i`、独立改变 `a,b` 符号的嵌入作代表。于是 (13) 和不变性给其 **全部四个** regulator 坐标为

\[
(-4G,-4G,-4G,-4G).
\]

`[i]` 是有理 Bloch cycle，因为 `i` 为 torsion，`i∧(1−i)=0` 于有理外平方；`D(i)=ImLi₂(i)=G`。`res[i]` 在上述四个嵌入的 regulator 都是 `G`。Borel–Suslin 的全部 regulator 向量在 `B(L)_Q` 上是单射，故

\[
\boxed{\beta=-4\operatorname{res}_{L/\mathbb Q(i)}[i]
\quad\text{于 }\mathcal B(L)_Q.} \tag{15}
\]

此处的单射是无条件定理，精确表述可见 [Neumann–Yang，math/9712225v1，§2 的 Borel theorem](https://arxiv.org/pdf/math/9712225v1)。同节 Proposition 2.1 还直接给有理 Galois descent；证明 (15) 本身无需选择 Bloch transfer 的整系数归一化。不能只在 rank `4` 的 Bloch 群上用一个实坐标相等推出类相等；这里确实使用了全部四个坐标。

因此，满足平均条件的选择虽然没有显式五项证书，其端点差在有理 Bloch 群中已经与已知 cyclotomic 类唯一识别。这个身份与 `T` 在函数域 K₂ 中 torsion 完全相容：非零信息出现在一条 Steinberg null-homotopy 的两个端点，绝对曲线 regulator 仍为零。

## 8. 结论的实际范围与下一步输入

本轮完成的是固定 Catalan 积分的精确归属：一个绝对 regulator 为零的符号代表仍有非零开放路径 primitive；对称平均的有限 Steinberg 链把这一端点差送到 `−4[i]`。这不是新造非零椭圆周期，也不是证明非零代数 K₂ 类或无理性。

相对 real 上同调已经完整。若要进一步把它记成某个指定的 `K₂(C,{P₊,B₊})` 类，仍需给出曲线 Quillen K₂ lift 和端点 trivialization；本文没有把函数域符号、自由 Steinberg 链和规范相对 motivic lift 混为一件事。有限链 (14) 的存在也未给其长度、高度、分母或随尺度变化的可控制构造。

可继续推进的具体入口是把 (11) 显式化：在有理商坐标 (5) 上给有限 Steinberg 分解，记录端点求值及五项关系，并估计其算术成本。任何新的非零绝对椭圆 K₂ 候选必须避开 (9) 的 `κ` 不变性及 `T` 的整个 V₄ 不变性；仅把单商 tame 修成 `1` 不够。即使找到这样的候选，也须独立证明其目标周期身份和整数近似预算。

[独立精确脚本](E:/kimi-build/zeta5/research/odd_zeta_k2_regulator_20261004_verify.py) 与 [JSON](E:/kimi-build/zeta5/research/odd_zeta_k2_regulator_20261004_verify.json) 已运行通过。它们核商坐标、V₄ 平均、函数反转、八点的修正 tame jets、端点局部值、Galois 点作用、(2) 的实虚展开和 (7) 的闭合边界/积分符号，不数值计算 `G`，也不替代 transfer、Matsumoto、Borel–Suslin 等定理证明。

## 9. 本轮直接使用的 primary 版本

- Goncharov–Levin，*Zagier's conjecture on L(E,2)*，`alg-geom/9508008v4`，1997-06-15；§1.6 Bloch–Suslin 正合列，Theorem 1.2/1.5 说明椭圆 K₂ 的正确范围。[PDF](https://arxiv.org/pdf/alg-geom/9508008v4)。
- Rost，*Chow Groups with Coefficients*，Documenta Mathematica 1 (1996), 319–393；Theorem 1.4、R1c/R3b/R3d、Proposition 2.2。[作者 PDF](https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf)。
- Dokchitser–de Jeu–Zagier，*Numerical verification of Beilinson's conjecture for K₂ of hyperelliptic curves*，`math/0405040v2`，2005-05-04；§3 的 tame、closed-cycle regulator 和 Bloch–Wigner primitive。发表于 Compositio Math.142 (2006), 339–373。[v2 PDF](https://arxiv.org/pdf/math/0405040v2)。
- Suslin，*K₃ of a field, and the Bloch group*，Trudy Mat.Inst.Steklov.183 (1990), 180–199；英文 Proc.Steklov Inst.Math.183 (1991), 217–239，Theorem 5.2。[英文原件 PDF](https://www.maths.dur.ac.uk/users/herbert.gangl/Suslin_K3_Bloch_group.pdf)。
- Neumann–Yang，*Rationality problems for K-theory and Chern–Simons invariants of hyperbolic 3-manifolds*，Enseign.Math.(2)41 (1995), 281–296；`math/9712225v1`，1997-12-04；§2 Borel theorem 和 Proposition 2.1。[arXiv PDF](https://arxiv.org/pdf/math/9712225v1)，[作者公开 PDF](https://www.math.columbia.edu/department/neumann/preprints/cs2.pdf)。
