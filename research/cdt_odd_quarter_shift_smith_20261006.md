# 四分之一移位原 rank5 格的 split-prime 两层信用

日期：2026-10-06。新证明，沿用[实际模型及精确分母](cdt_odd_quarter_shift_full_model_20261006.md) Q1–Q13；不运行或改动任何旧冻结数学脚本。

本稿对同一五函数基 f=(1,J,θJ,θ²J,θ³J)、native x 坐标、整数 polynomial sources 和普通 arch metric，闭合 split 素数的 whole-prefix 同余到原格 Smith determinant 的接口。全前缀分母不是满密度 Δ_(4N)^4；必须保留 residue-class 费用。本稿给出可认证上界，未证明最优 CDT 费用，也没有新无理性定理。

## 1. 实际 whole-prefix packet

固定 p≡1 (mod4)，令 h=(p−1)/4、d=(p−1)/2。全范围 0≤n<N 要求
\[
\boxed{p^2>4N+1.}\tag{S1}
\]
实际模型的 Q7–Q9 表明 c_n 的 valuation 为−4恰在 h≤n mod p≤h+d，带外为0。令 U=p⁴J，U 的全部所需 coefficients p-integral。对 n₀=h+kp 和 j≥0，准确比值是
\[
\frac{c_{n_0+j}}{c_{n_0}}
=\left[\frac{(1/2+p(k+1/4))_j}{(1+p(k+1/4))_j}\right]^4.
\tag{S2}
\]
只用 j≤d 的带内区间；其中各因子 p-unit。定义有限多项式
\[
T(x)=\sum_{j=0}^d\left[\frac{(1/2)_j}{j!}\right]^4x^j,
\quad V(x)=\left.\partial_\rho\sum_{j=0}^d
\left[\frac{(1/2+\rho)_j}{(1+\rho)_j}\right]^4x^j\right|_{\rho=0}.
\tag{S3}
\]
T、V∈Z_(p)[x]、T₀=1、V₀=0，degT=d 且 top coefficient modp非零。以实际 w_k=p⁴c_(h+kp) 定义所需有限慢 series W(s)，s=xᵖ。S2 的一阶 Taylor 展开与带外 U∈p⁴ 一起给
\[
\boxed{U\equiv x^h\{T(x)W(x^p)+pV(x)(\theta_s+1/4)W(s)\}
\pmod{p^2,x^N}.}\tag{S4}
\]
W 的高阶延拓可任取；前缀以外不声称 p⁴J 整。用 Euler derivatives 保持同一 xⁿ 评价行和同一截断。

## 2. 两层原格 polynomial relations

一阶关系为
\[
\mathcal L_1=T\theta-hT-\theta T,
\quad\mathcal L_1U,\ \theta\mathcal L_1U,\ \theta^2\mathcal L_1U\equiv0\pmod{p,x^N}.
\tag{S5}
\]
置 B=TθV−VθT、Q=T²+B。因 B 的 x^(2d) 项相消，degB≤2d−1，Q 的 top coefficient 是 T_d²，p-unit。将 z=U/(x^hT)、r=V/T，S4 给
\[
z=W+p r(\theta_s+1/4)W\pmod{p^2}.
\]
θW(xᵖ)=pθ_sW，快慢分离严格保留到 p²，于是
\[
(1+\theta r)\theta^2z-(\theta^2r)\theta z
-\frac p4(\theta^2r)z\equiv0\pmod{p^2,x^N}.
\tag{S6}
\]
这里1+θr=Q/T²是 formal p-adic unit。回代 z、清分母后得到 degree≤3d 的实际 polynomial source
\[
\begin{aligned}
\mathcal L_2&=P_2\theta^2+P_1\theta+P_0,\\
P_2&=QT,\\
P_1&=-(2hQ+\theta Q)T,\\
P_0&=(h^2Q+h\theta Q)T+(\theta Q)(\theta T)-Q\theta^2T
-\frac p4(T\theta B-2B\theta T).
\end{aligned}\tag{S7}
\]
实际清分母只需 QT：使用 QθB−BθQ=T(TθB−2BθT)，消去表面上的更高分母。S6 也可直接乘 T³ 后作 conjugation 推出 S7，不依赖这个局部除法。
\[
\mathcal L_2U,\ \theta\mathcal L_2U\equiv0\pmod{p^2,x^N},
\qquad\overline{\mathcal L_2}=(Q\theta-hQ-\theta Q)\overline{\mathcal L_1}.
\tag{S8}
\]
因此第二层的 modp 向量属于第一层的 polynomial span；θℒ₂ 对 ℒ₁、θℒ₁ 的表达亦只增至 degree2d 的 multipliers，乘 degree≤D−3d 的 polynomial 后仍在第一层许可的 degree≤D−d 中。没有把两层算作五个互相独立的普通 kernel。

## 3. 同一实际 square evaluation matrix

取 E_D=⊕_(i=1)^5 Z[x]_(≤D)f_i，R=5(D+1)。实际 rank5 derivation-closed 系统的 Shidlovsky 评价 flag 给 N_D=5(D+1)+O(1) 及 R 个 leading rows V_D⊂[0,N_D)。取满足 S1 的 split p，Ψ_p=p⁴eval_(V_D) 为整矩阵。

constant source 有 D+1 个方向且 image⊂p⁴；其它四 rows 只用安全 p⁴ prefix分母。因此 baseline Smith floors 和为4(D+1)。S5 的三个 relation families，乘 degree≤D−d polynomials，按最高 derivative coefficient T 依次比较，modp primitive rank为 k₁=3(D−d+1)₊；其 Ψ_p image⊂p。S7 的两个 families 同理 primitive rank k₂=2(D−3d+1)₊，image⊂p²。constant support与四个 J supports分离，S8保留嵌套。

阈值1至少 D+1+k₁，阈值2至少 D+1+k₂，阈值3/4各至少D+1。故原 square leading determinant 的 capped Smith floors β_i≤4 满足
\[
\boxed{\sum_i\beta_i\ge4(D+1)+k_1+k_2.}\tag{S9}
\]
每个 local relation 的 p-unit系数只用于同一原格 DVR 证明；没有换一个未经 arch norm 计费的新全局基。

## 4. residue-class baseline及全部其它地方

固定 ε>0，b=4+ε。Q10 的 split part 被四个 restricted LCM columns
\[
\Delta^+_{\lfloor bn\rfloor},\qquad
\Delta^+_M=\prod_{p\equiv1\ (4)}p^{\lfloor\log_pM\rfloor}
\tag{S10}
\]
所清，有限 initial项由固定整数处理。inert part 的 log≤O(√n log²(n+2))，对完整 N_D 前缀的统一整数因子也只有此量；即使对每个 polynomial source column全额计费，其 evaluation height 的主阶仍为 o(D²)，tensor归一后也是小项。split 小素数的 j≥2 层同样 O(√N_D log²N_D)，属于小项。p=2 的全部 coefficients 是2-unit，Euler derivatives/source polynomials都整，没有删除任何本来存在的 dyadic 主项。

这里可直接沿 CDT 第八节的 prime sums 保留 p≡1 (mod4)，不需要假定 restricted LCM 是原定理自动列出的普通 LCM 型。按该节原逐 prime height 证明，AP prime number theorem 使同一 leading/degree integral乘密度1/2。Shidlovsky flag与source/arch metric均不变。等价地，本段是明确对底层 prime height估计的限定推广，全部非 split 地方的 o(D²) 控制已给出；不是只据一个密度口号减半。

普通 full-density 表为 constant四个0 columns、其余四 species 各四个 b columns。normalized degree u∈[0,1]均匀，positive species总质量4/5，给每个 threshold t 的最大transport payoff
\[
M_b(t)=4\min(4/5,(1-t/b)_+).
\tag{S11}
\]
上界来自可成功 degree质量与 positive species质量；将 positive species放入最高的 degree区间达到此上界，species内部可等分，故这是 maximum而非下界。于是
\[
\tau_b=2\int_0^bM_b(t)dt=\frac{96b}{25},
\qquad\tau_b^{\rm split}=\frac{48b}{25}.
\tag{S12}
\]
对 b↓4，baseline为192/25；它已经包括 full-prefix率8和实际rank5 balanced transport之间的差异。

## 5. 真实 balanced determinant信用及结论范围

[冻结DVR/near-balanced桥](cdt_odd_level20_balanced_smith_bridge_20261006.md)的 saturated primitive restriction证明可用 S9 的 cap4，tensor floors和至少 dR^(d−1)[4(D+1)+k₁+k₂]，restriction损失≤4dc，其中 c/R^d→0。actual balanced leading rows在 V_D^d中，故此为真实 source/graded evaluation信用。

ν=(0,4,4,4,4)、s=4。sorted θ=(0,1/b,1/b,1/b,1/b)，all-active matching窗口 a₀=b。S5信用只支撑 p≤2D，S7只支撑 p≤2D/3，两者均在 p≤(2−δ)D 内的同一 baseline全active窗口。原最大transport在此恰为16/5；原 pure matrix baseline也恰是4−4/5=16/5，因而允许直接扣掉 S9 的信用，没有从不相容的费用表扣kernel维数。固定 ε、tensor dimension、strict margin/tolerance后取 D→∞，再取 tensor/tolerance极限与δ↓0。

小素数条件 p²>bN_D 只删 o(D²)信用，AP prime sums给
\[
\gamma=\frac12\left[3\int_0^2(1-t/2)dt
+2\int_0^{2/3}(1-3t/2)dt\right]=\frac{11}{6}.
\tag{S13}
\]
沿冻结桥实际核对过的 HS/source/arch normalization，最终 finite cost折扣为2γ/5²=11/75。故此限定普通 metric 的可认证输入满足
\[
\boxed{\kappa_{\varepsilon}=\frac{48(4+\varepsilon)}{25}-\frac{11}{75},
\qquad \lim_{\varepsilon\downarrow0}\kappa_{\varepsilon}=\frac{113}{15}.}
\tag{S14}
\]
同一合法共同 φ 因而给 5(ρ−κ_ε)≤J_φ（此处 J_φ 指 ordinary Jensen，勿与函数 J 混淆）。S14 是一个证明得到的上界，不是最优费用的必要下界，不能据它排除所有 improved lattices。

已认证的 omit1/unique simple0 native-x λ-leaf 类有 ρ≤log16<3，而 κ_ε>7。因此**这份完整且改进后的输入不能产生 CDT 数值矛盾**。只把 J(1) 假为有理也不消除其真实 conifold monodromy，不能补一个未经证明的 filled leaf。可继续研究 higher Smith阈值、其它源的真实抵消周期或另一个全解析叶；本稿不以这些尚未证明的改进作为既得结果。

## 6. 核验范围

whole-prefix、local relations及原格primitive counts由新[独立审阅](cdt_odd_quarter_shift_independent_review_20261006.md)实际核验；该审阅未认领本稿§§4–5的費用。后来另建[费用独审](cdt_odd_quarter_shift_cost_independent_review_20261006.md)实际读本稿全文、旧balanced桥和原CDT PDF122–124/129–131/140–143，通过 restricted所有地方、小项、maximum、matching、原格balanced信用及ordinary HS归一化。它未执行producer或读取JSON，不让其审阅范围包含有限检查次数。

新[有限脚本](cdt_odd_quarter_shift_smith_20261006_verify.py)及[证书](cdt_odd_quarter_shift_smith_20261006_verify.json)由根首次单次执行，24项全通过：抽象 S6–S8 identities；p=5/13/17的实际多block prefixes；N=0..96精确最小分母及全列明奇素数valutation；积分和常数。它只 import标准库/SymPy，不执行旧或同行数学代码。所有全 p/full-scale 结论仍依赖本稿及模型的证明，有限样本不是替代。当前同一原格费用是可认证上界，没有新数值无理性/Lean定理。
