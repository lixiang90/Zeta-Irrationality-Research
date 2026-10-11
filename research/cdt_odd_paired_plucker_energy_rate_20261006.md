# 同一配对饱和格的 Cauchy–Hardy 分解与严格解析主率

日期：2026-10-06。NEW 未冻结主稿，quarter_actual_rank。本文为原三重零点、rank2n 的实际配对格证明全尺度解析上界，不借完整3n determinant、恢复四重零点布局或其能量。无限非零与算术主率不在本文的完成范围。

## E1. 实际全文输入与主结论

本轮实际完整读取下列冻结输入，输出均无截断：

- `cdt_odd_paired_head_free_integral_lattice_20261006.md`，I1–I25，SHA `5b7947c8d26747ca0eb7abac8b3ed5b7cbbe0828170ffe74d7ac51215b1fef5b`。
- `cdt_odd_paired_head_free_analytic_plucker_root_20261006.md`，R1–R16，SHA `cf341860474546dc0d5a2a630ae73f6bbf50426fa7ee8c100975c6a2b1688e38`。

保持该稿的 R_n、S_{2n}、右线 c_n=2n+1/2、K=-4a q''-b q'''，a,b 为固定整数、b≠0；实际目标 ξ=aζ(4)+bζ(5)。D_{A,n}(ξ) 始终按 I8 的完整整数值饱和基 G_1,…,G_n,f_{2n},…,f_{3n-1} 取值。

记

\[
b_j=\binom{6n+j}{j-1},\quad
\beta_m=\gcd(b_m,b_{2n+1-m}),\quad
\Gamma_n=\prod_{m=1}^n\beta_m.
\tag{E1}
\]

**主定理。** 存在只依赖 a,b 的常数 C，使每个 n≥1 都有

\[
\log|D_{A,n}(\xi)|\le
-\beta_H n^2-2\log\Gamma_n+C n\log(n+2),
\tag{E2}
\]

log0=-∞。这里 β_H=β_0+(1/2)log2+c_H，

\[
c_H=9\log3-8\log2-4,
\]
\[
\beta_0=-\left[M_0+M_1+\frac12\log2
+176\log2-21\log3-49\log7+\frac{15}2\right],
\tag{E3}
\]

M_0、M_1 是 E5 定义、E6 明确求取的两个一变量最大值。β_0 保留早先 high-pair factor2 的安全基线，便于沿用原首次证书；E19 的准确平方恒等式随后省掉该因子，再增加 (1/2)log2。独立纸面短界给 β_0>7.1、c_H>0.3423，所以 E2 确实是正的 n² 衰减。另一个 NEW 有理区间证书给

\[
7.90523839512558\le\beta_0\le7.90523839512559,
\quad \beta_H>8.59403839512558.
\tag{E4}
\]

此界已经支付完整基的 archimedean 增长和实际所有 factorial。Γ_n 是同一饱和基的共同因子，并非多除一次 raw (6n+1)!。若独立另证 γ=lim n^{-2}logΓ_n 存在，E2 直接给 limsup n^{-2}log|D_A(ξ)|≤-β_H-2γ。本文此处不使用尚未独审的新 gcd 主率稿。

## E2. Cardinal 低块与高 Newton 块的准确分解

S=S_{2n}，j'=2n+1-j。冻结基的 identity 为

\[
L_j(z)=\frac{S(z)}{(z-j)S'(j)},\qquad
G_m(z)=S(z)\left(\frac{\kappa_m}{z-m}
+\frac{\kappa_{m'}}{z-m'}\right),
\tag{E5}
\]
\[
\kappa_j=\frac{b_j}{\beta_m S'(j)}
=\frac{(-1)^j(6n+j)!}
{(6n+1)!\,\beta_m\,(j-1)!^2(2n-j)!},
\quad j\in\{m,m'\}.
\tag{E6}
\]

这里 S'(j)=(-1)^j(j-1)!(2n-j)!；分母有 **(j-1)!²**。阶段消息曾漏写该平方，写稿前已纠正；不能使用那个 shorthand 计算主率。令 \widetildeκ_j=β_m|κ_j|，真实展开中每项共同包含 Γ_n^{-1}。

高块恰为

\[
f_{2n+k}(z)=\frac{S(z)\prod_{v=1}^k(z-2n-v)}{(2n+k)!},
\quad0\le k<n.
\]

所以任意 n 个 column z_B 上的高块 determinant 准确等于

\[
\frac{\Delta(z_B)\prod_{j\in B}S(z_j)}{F_n},
\quad F_n=\prod_{k=0}^{n-1}(2n+k)!.
\tag{E7}
\]

这来自 monic degrees0,…,n-1 的 unitriangular 转换，不漏额外 Schur polynomial。低块多线性展开选每个 mirror pair 一个节点 a_m∈{m,m'}；其剩余矩阵是 1/(z_j-a_m)。Cauchy identity 为

\[
\det\left[\frac1{z_j-a_i}\right]
=(-1)^{n(n-1)/2}
\frac{\Delta(a)\Delta(z)}{\prod_{i,j}(z_j-a_i)}.
\tag{E8}
\]

因此 R16 的 n²–2n² symmetric-degree 费用已被精确转成低块 Cauchy 相互作用；并未将它扔掉或按 fixed kernel 处理。

## E3. 实际复 determinant 到同一基的正包络

记

\[
W_n(x)=\frac{|R_n(c_n+ix)K(c_n+ix)|\,|S(c_n+ix)|^2}{2\pi},
\quad L_n=\sup_{x\in\mathbf R}W_n(x),
\tag{E9}
\]

以及高块的正 partition

\[
Z_{H,n}=\frac1{n!}\int_{\mathbf R^n}
|\Delta(c_n+ix)|^2\prod_j W_n(x_j)\,dx_j.
\tag{E10}
\]

对一个选择 a=(a_1,…,a_n)，低块正 Gram 为

\[
\mathsf M_C(a)_{ij}=\int_{\mathbf R}
\frac{W_n(x)\,dx}{(c_n+ix-a_i)(c_n-ix-a_j)}.
\tag{E11}
\]

全部积分绝对收敛：K 指数衰减，R、S 和固定阶多项式仅给有限次幂增长；c_n-a_i≥1/2。冻结 R6 的 finite determinant 展开与 L² triangle inequality，按 n 个 low 和 n 个 high columns 做 Laplace 展开，给全 n 的精确上界

\[
|D_A(\xi)|\le
\binom{2n}{n}\frac{Z_{H,n}}{F_n^2\Gamma_n^2}
\left(\sum_{a_m\in\{m,m'\}}
\prod_m\widetilde\kappa_{a_m}\,
\sqrt{\det\mathsf M_C(a)}\right)^2.
\tag{E12}
\]

说明常数：每个固定 column partition 的 L² norm² 含 (n!)²/(2n)!=binom(2n,n)^{-1}；相同 norm 的 binom(2n,n) 个 partitions 在 triangle 后给 E12 的一个 binomial，而不是遗漏或多出 n²阶 combinatorial fee。

E12 保留真实选择节点的 κ 与对应 Cauchy Gram 的匹配，可继续优化；目前取统一上界。正 Gram 只给上界，未证明实际复 D_A(ξ) 非零。

## E4. Hardy 核准确支付低块的 n²相互作用

令 δ_i=c_n-a_i>0。partial fractions 与 ∫δ/(δ²+x²)dx=π 给

\[
\int_{\mathbf R}\frac{dx}{(\delta_i+ix)(\delta_j-ix)}
=\frac{2\pi}{\delta_i+\delta_j}.
\tag{E13}
\]

各 kernel 乘积为 O(x^{-2})，所以无需 principal value。W_n≤L_n 给 Hermitian Loewner inequality，再用 positive definite Gram 的 determinant monotonicity，得

\[
\det\mathsf M_C(a)\le L_n^n\mathcal H_n(a),
\quad
\mathcal H_n(a)=
(2\pi)^n\prod_i\frac1{2\delta_i}
\prod_{i<j}\left(\frac{\delta_j-\delta_i}{\delta_j+\delta_i}\right)^2.
\tag{E14}
\]

节点均不同，所以 unweighted Gram positive definite，Cauchy determinant formula 给最后的准确身份。排序后 δ_1<⋯<δ_n 是 {1/2,3/2,…,2n-1/2} 的子集，因此 δ_i≥i-1/2、δ_j<2n，且∏(2δ_i)^{-1}≤1。ratio 随较小 δ 减小、较大 δ 增大而增大，所以

\[
\log\mathcal H_n(a)\le n\log(2\pi)
+2\sum_{i=1}^n(n-i)
\log\frac{2n-i+1/2}{2n+i-1/2}
=-c_Hn^2+O(n).
\tag{E15}
\]

最后是 smooth Riemann sum，误差 uniform in a；

\[
2\int_0^1(1-t)\log\frac{2-t}{2+t}\,dt
=4-9\log3+8\log2=-c_H.
\]

这项是真实 Hardy Gram 的负能量，不能用 lattice gcd1 替代。没有假定一支撑 equilibrium、所有选点相同或选择展开没有 cancellation。

此外 b_{m'}>b_m，|S'(m')|=|S'(m)|，所以 \widetildeκ_{m'}>\widetildeκ_m。E12–15 于是给

\[
|D_A(\xi)|\le
\binom{2n}{n}4^n e^{-c_Hn^2+O(n)}
\frac{Z_{H,n}L_n^n}{F_n^2\Gamma_n^2}
\prod_{j=n+1}^{2n}\widetilde\kappa_j^2.
\tag{E16}
\]

组合费 log binom(2n,n)+nlog4=O(n)。这是 main theorem 使用的统一选择 bound；E12 比 E16 更精细，E15 不宣称 optimal node energy。

## E5. 右线共同 weight 的全尺度估计

令

\[
J_A(y)=\int_0^A\log\sqrt{v^2+y^2}\,dv
=\frac A2\log(A^2+y^2)-A+y\arctan(A/y)
\quad(y>0),
\]

J_A(0)=AlogA-A。固定变量 z=n(2+1/(2n)+iy)。Stirling 与实际 root-product Riemann sums 给

\[
W_n(ny)\le C_{a,b}n^{4n+C}(1+|y|)^C e^{nQ(y)},
\]
\[
Q(y)=12\log6-6\log2-6+7J_2(y)-2J_8(y)-2\pi|y|.
\tag{E17}
\]

这里 7J2−2J8 来自 |R| 中3J2−2(J8−J2)，加上实际 |S|² 的2J2；没有换成 k4 的 R。

误差均 uniform：S 的 scaled 正根距为 (v+1/2)/n、v0..2n-1，log√(u²+y²) 单调，midpoint sum 的 endpoint error至多 O(log(n+2)+log(1+|y|))；denominator 的根在2..8附近，离0有固定距离，额外 endpoint 同阶。prefactor 的 Stirling error亦 O(log(n+2))。K(c_n+inx) 沿 half-integer line 是 fixed hyperbolic derivatives，|K|≤C_{a,b}e^{-2πn|x|}。由这些逐项估计可取一个固定 C，而非隐藏 n-dependent norm。

Q(y)=-2π|y|-2log|y|+O(1) 在无穷远，故 L_n 满足

\[
\log L_n\le4n\log n+nM_0+O_{a,b}(\log(n+2)),
\quad M_0=\max_{y\in\mathbf R}Q(y).
\tag{E18}
\]

为高块，准确恒等式 (1+y²)(1+y'²)-(y-y')²=(1+yy')²≥0 给 |y-y'|²≤(1+y²)(1+y'²)，因此

\[
Z_{H,n}\le
\frac{n^{n(n-1)}}{n!}
\left[\int_{\mathbf R}W_n(x)
\left(1+\frac{x^2}{n^2}\right)^{n-1}dx\right]^n,
\]
\[
\log Z_{H,n}\le
5n^2\log n+M_1n^2
+O_{a,b}(n\log(n+2)),
\quad M_1=\max_y\{Q(y)+\log(1+y^2)\}.
\tag{E19}
\]

积分上界：对 F=Q 或 Q+log(1+y²)，在一个固定 compact 中 F≤maxF；外侧 F≤maxF-|y|，固定 polynomial factor 被指数尾吸收。因而 Laplace 上界只付 O(logn)，未以有限 n 拟合替代所有 n 的收敛。

## E6. 准确 factorial 与基增长配对，n²logn 全消去

定义

\[
h(t)=(6+t)\log(6+t)-2t\log t
-(2-t)\log(2-t)-6\log6+2.
\tag{E20}
\]

对 j=n+1,…,2n，E6 的精确 factorial 给

\[
\log\widetilde\kappa_j=-(2n-1)\log n+nh(j/n)+O(\log(n+2)),
\]
\[
2\sum_{j=n+1}^{2n}\log\widetilde\kappa_j
=-4n^2\log n+2n^2\int_1^2h(t)dt+O(n\log(n+2)),
\]
\[
2\log F_n=5n^2\log n
+2n^2\int_2^3(u\log u-u)du+O(n\log(n+2)).
\tag{E21}
\]

t=2 端点使用0!=1、0log0=0。Stirling 误差对全部非负整数阶乘一致；h 在该端点有可积导数，所以乘上 n 后的 Riemann 误差至多 O(nlogn)。这里始终是实际 I8 基系数，没有另加一个独立取最大的 Newton covolume 费用。

共同 n²logn 分别为：low weight L_n^n 的4，high partition的5，κ product的−4，F_n^{-2}的−5，合计0。剩下

\[
2\int_1^2h(t)dt-2\int_2^3(u\log u-u)du
=176\log2-21\log3-49\log7+\frac{15}2.
\tag{E22}
\]

E16–22 证明 E2。若把 (j-1)!² 漏掉，或把 high factorial免费换成 first2n factorial，这个取消及常数都会错误。

两个 maxima 可明确认证。对 y>0，

\[
Q'(y)=7\arctan(2/y)-2\arctan(8/y)-2\pi,
\quad Q''(y)=-\frac{14}{4+y^2}+\frac{16}{64+y^2}.
\tag{E23}
\]

在0<y≤1，Q''≤-51/20；F_1=Q+log(1+y²) 满足 F_1''≤-11/20。两者在0+的导数均π/2。atan(1/2)≥11/24、atan(1/8)≤1/8、π<22/7，给 Q'(1)+1<0。Q''<0 至 y<√416，在该区间 y≥1 时 F_1'≤Q'(1)+1<0；对 y≥√416，用 Q'≤14/y-2π、2y/(1+y²)≤2/y 也得 F_1'<0。因此 M0、M1 各由 (0,1) 内唯一 root 达到：

\[
7\arctan(2/y_0)-2\arctan(8/y_0)=2\pi,
\]
\[
7\arctan(2/y_1)-2\arctan(8/y_1)+\frac{2y_1}{1+y_1^2}=2\pi.
\tag{E24}
\]

M0=Q(y0)，M1=Q(y1)+log(1+y1²)。这是一变量、唯一 saddle 的明确计算，不是未知 high-degree module rate。

## E7. 无机器的正衰减界，以及 NEW 常数证书的真实历史

Q(0)=12log3-28log2-4。E23 与 log(1+y²)≤y² 给

\[
M_0\le Q(0)+\frac{5\pi^2}{102},
\quad M_1\le Q(0)+\frac\pi2-\frac{11}{40}.
\]

于是

\[
\beta_0\ge49\log7-\frac{241}2\log2-3\log3
-\frac{5\pi^2}{102}-\frac\pi2+\frac{31}{40}>7.1.
\tag{E25}
\]

最后不需数学程序：log2<347/500、log3<1099/1000、log7>389/200，由 log x=2Σ_{k≥0}z^{2k+1}/(2k+1)、z=(x-1)/(x+1) 的前三项及 geometric remainder 给；log3=log2+log(3/2)，log7=2log2+log(7/4)。π<22/7 由正积分 ∫₀¹ x⁴(1-x)⁴/(1+x²)dx=22/7-π。代入 E25 的有理 lower bound 准确为

\[
\frac{71}{10}+\frac{826}{2186625}>\frac{71}{10}.
\]

同一 log series取前五项，直接清分母可得 log3>1.09861、log2<0.693148，故 c_H>0.342306>0.3423。log2 的前三项下界又严格大于0.693，所以 (1/2)log2>0.3465；这两项加上 β_0 证书下界给 E4 的严格 β_H 下界。

数值细化另由自有 NEW exact Fraction 程序处理，旧/同行程序均未 execute/import/rerun：

1. `cdt_odd_paired_plucker_energy_rate_20261006_verify.py` 首次执行一次。两个 root bracket 与 7<β0<8 的数学 assertions 已经过；随后 Python4300-digit整数字符串限制使输出序列化失败，exit1，**未生成JSON，不记PASS**。源保留不改、不重跑。
2. 单独 `cdt_odd_paired_plucker_energy_rate_20261006_verify_v2.py` 首次执行一次，成功生成同名JSON。只将输出巨大内部 Fraction 改成分母10^14的 outward rational rounding，原数学算法与80项 atan/log区间、72次root bisection不变。程序自身校验舍入 containment；原失败源不被import或execute。

本人数学执行总数为 **2：failed1+NEW-v2-success1**，不能抹去失败或称只有1次。v2 只认证 E24 两根和 E3 常数，未证明 E2 的所有 n、非零或算术 margin；E2 的纸面证明及 E25 独立存在。其输出为 y0∈[0.49369430476462,0.49369430476463]、y1∈[0.83271861497492,0.83271861497493]，β0 的严格外舍区间见 E4。

## E8. 更精细的匹配能量仍可继续，但不能偷换完成范围

E12–14 保留准确 finite-n 优化项

\[
\left(\sum_{a_m\in\{m,m'\}}
\prod_m\widetilde\kappa_{a_m}\sqrt{\mathcal H_n(a)}\right)^2.
\tag{E26}
\]

每项的 n² 能量保留 2∫h(t)dλ(t)，以及准确的 Hardy 相互作用

\[
\iint\log\left|\frac{(2-t)-(2-u)}{(2-t)+(2-u)}\right|d\lambda(t)d\lambda(u).
\]

λ 在每个 mirror pair 中选一个节点，fold 约束使极限密度≤1，λ 加其反射为 [0,2] 上的 Lebesgue 测度。E15 是这项准确能量的统一放宽。本文没有声称已经求出优化后的极限 supremum 或 equality，也没有把 symmetric degree 记成 O(n)。

这一 strict analytic rate 是同一 actualsat lattice 的新结论。要得到新的特殊值定理，还必须在同一 D_A 上证明无限 nonzero，并给足够便宜的 all-prime primitive polynomial cost。一个辅助素数的有限样本、positive Gram upper bound、Γ 的 archimedean共同因子均不自动完成这些条件。没有新的ζ/L/Catalan无理性、线性无关性或Lean定理；本文暂未冻结，交root实际全文独审。
