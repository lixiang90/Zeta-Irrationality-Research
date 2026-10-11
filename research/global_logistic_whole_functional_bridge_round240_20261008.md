# 第240轮：有限 ζ 组合的 logistic 全泛函投影

2026-10-08，Root。新纸面引理；数学程序、参数扫描、Lean 构建均为0。本稿把新的一手构造扩展为明确的数值投影接口，不宣称得到任何新的数值无理性定理。

## 1. 来源身份与适用范围

本轮新检索到 Qian Tang 的 [zeta2-zeta3-linear-independence](https://github.com/dtq1997/zeta2-zeta3-linear-independence)。保存版本为 commit `669c92bf7a3728e0de9ad80c373bc29fb5ca3d58`，通过官方 GitHub API 的 commit 和 tree 响应固定，保存于本轮 literature/root_zeta23。README 声明已给出 1、ζ(2)、ζ(3) 的 Q-线性无关性及核检查；本轮只核实际 theorem statement、选定数学文件和构造，不重跑 Lean/Comparator，也不把作者声明登记为本项目的新证明。

实际 FULL 读 Family、Interfaces、Analytic/Logistic、Analytic/Contour/Moments、Criterion、Assembly、PrimeObstruction、PrimeEdge/LocalShape、PrimeEdge/Gram、Analytic/Energy/Pointwise、Analytic/Energy/Assembly，以及 README、NOTICE。没有读全部依赖、整个仓库或 FstarInput 的全部数值证书。下文重新纸证扩展；基础 logistic moments 也给出自含验证，不依赖把 imported theorem 当作本轮内核验证。

## 2. 基础矩与全泛函身份

设
\[
 t(y)=\tfrac12+iy,\qquad \rho(y)=\frac\pi{2\cosh^2(\pi y)},\qquad
 B(G)=\int_{\mathbb R}G(t(y))\rho(y)dy.
\]

其 Fourier 变换为
\[
 \int_{\mathbb R}\rho(y)e^{-ixy}dy=\frac{x}{2\sinh(x/2)},\qquad x\in\mathbb R,
 \tag{L1}
\]
右侧在0取连续值1。一个直接证明是对 x>0 沿高为 i 的矩形积分 ρ(z)e^{-ixz}：上下边之差为 (1−e^x) 倍实轴积分，唯一双极点 i/2 的留数为 ix e^{x/2}/(2π)，两条竖边按 e^{-2π|Re z|} 消失。留数定理给 (1−e^x)I=−xe^{x/2}，即 L1；负 x 由偶性，0由 ∫ρ=1。固定高度矩形不存在无界竖向估计的借用。

于是
\[
 B(e^{-xt})=\frac{x}{e^x-1}\quad(x>0),\qquad
 B(t^m)=B_m^+,\qquad
 B((t+j)^{-k})=k(\zeta(k+1)-H_j^{(k+1)}).
 \tag{L2}
\]
这里 B_1^+=1/2，H_j^{(k)}=Σ_{a=1}^j a^{-k}。多项式身份由在0邻域的指数矩求导（ρ有指数尾）及 z/(1−e^{-z}) 的 Taylor 展开；极点身份由 Laplace 积分及 L1。交换积分绝对值可用 ∫₀∞ x^{k−1}e^{−(j+1/2)x}dx/(k−1)! 支付，随后展开 (e^x−1)^{-1} 的正级数。故 L2 对所有 j≥0、k≥1 成立。

取固定有限集合 S⊂{2,3,5,7,…}、有理系数 c_k（集合外取0），并写
\[
 X_c=\sum_{k\in S}c_k\zeta(k),\qquad
 \mathcal D_c=-c_2+\sum_{\substack{k\in S\\k\ge3}}
 \frac{c_k}{(k-1)!}\partial_t^{k-2},\qquad
 U_c(f)=B(\mathcal D_c(tf)).
 \tag{L3}
\]
对完整的简单极点表和多项式商部，有
\[
 U_c((t+j)^{-1})=jX_c-j\sum_{k\in S}c_kH_j^{(k)}-c_2,
 \tag{L4}
\]
\[
 U_c(t^e)=-c_2 B_{e+1}^+
 +\sum_{\substack{k\in S\\k\ge3,\ k-2\le e+1}}
 \frac{c_k(e+1)_{k-2}}{(k-1)!}B_{e-k+3}^+\in\mathbb Q.
 \tag{L5}
\]
L4 的和包含 k=2；不能漏去 −jc₂H_j^(2)。证明：G=t/(t+j)=1−j/(t+j)，对奇数 h=k−2，G^(h)=jh!/(t+j)^(h+1)。代入 L2 给 j c_k(ζ(k)−H_j^(k))。零阶项给 −c₂+jc₂(ζ(2)−H_j^(2))。L5 直接求导。

因此对任何具有有理多项式商部、仅在 −1,…,−M 有简单极点的 f，整个泛函严格满足
\[
 U_c(f)=a(f)X_c+b_c(f),\qquad a(f),b_c(f)\in\mathbb Q.
 \tag{L6}
\]
这是整个函数空间的真实数值恒等式；假设 X_c∈Q 即使整个所需 moment 表有理。没有先将其它周期删掉、再沿用删除前的矩阵。

## 3. 固定微分阶不改变 leading 实处能量

反复分部积分给
\[
 U_c(f)=\int_{\mathbb R}t(y)f(t(y))W_c(y)dy,\quad
 W_c=-c_2\rho+\sum_{\substack{k\in S\\k\ge3}}
 \frac{c_k i^{k-2}}{(k-1)!}\rho^{(k-2)}.
 \tag{L7}
\]
符号为 i^(k−2)。这些 f 及其任意固定阶导数沿 Re t=1/2 只有多项式增长，ρ 的各阶导数指数衰减，所有边界项消失。递推
\[
 \rho^{(h)}(y)=\rho(y)P_h(\tanh\pi y),\quad
 P_0=1,\quad P_{h+1}(z)=\pi((1-z^2)P_h'(z)-2zP_h(z))
\]
给固定 c 的常数 C_c>0，使 |W_c(y)|≤C_cρ(y)。它允许任意固定有限组合；不允许 c 或最大权随 n 无控制增长。

现在固定 Tang 原始有理核和完整列池
\[
 D_m(t)=\prod_{j=1}^m(t+j),\quad R_n=D_n^4/D_{5n},\quad h=3n,
 Q_{c,n}(T)=\det[U_{c,T}(t^{i+j}R_n)]_{0\le i,j<h},
 \tag{L8}
\]
其中 U_(c,T) 用 L4 中 T 替代 X_c、保留 L5 和全部有理修正；Q_(c,n)∈Q[T]、deg≤3n。在真实点它正是同一个积分 moment 行列式。

Andréief 展开及绝对可积（指数尾乘有限次多项式）给
\[
 |Q_{c,n}(X_c)|\le\frac{C_c^{3n}}{(3n)!}
 \int_{\mathbb R^{3n}}\prod_\ell|t(y_\ell)R_n(t(y_\ell))|\rho(y_\ell)
 \prod_{i<j}(y_i-y_j)^2\,dy.
 \tag{L9}
\]
Vandermonde(t)² 与 Vandermonde(y)² 只差绝对值1的固定相位。C_c^(3n) 仅付 O_c(n) 对数费用，故同一 absolute Heine envelope 的 n² leading rate 与所选有限组合无关。新源码 Pointwise 的估计正只使用固定常数乘 e^(−2π|y|)；其外场也是同一 R_n。

若进一步采用该仓库已陈述的完整 FstarInput 和其能量证书，则同样归一化
\[
 \widetilde Q_{c,n}=S_n^{3n}Q_{c,n}/F_n,
 \quad S_n=(5n)!/(n!)^4,\quad F_n=\prod_{i=0}^{3n-1}(i!)^2
\]
的绝对上界仍为 exp((−6+o(1))n²)。这里登记的是 **leading 能量的转移引理**；−6 的原证书依赖尚未本轮 FULL 核完，不能说它已成为新对象的独立完整证明。即使该实处证书全部付清，也完全不转移 primitive 整数内容和素数边缘非零性。

## 4. 全尺度目标系数至少有增长的秩

写 t^eR_n=q_e+Σ_j λ_(e,j)/(t+j)，a_e=Σ_j jλ_(e,j)。L6 的目标系数为 a_e，与 c 无关。由于 R_n=t^(−n)(1+O(t^(−1)))，无穷远展开给
\[
 a_e=0\ (0\le e\le n-3),\qquad a_{n-2}=-1\quad(n\ge2).
 \tag{L10}
\]
理由是该系数也是 −[t^(−2)]t^eR_n；多项式商部对此系数没有贡献。故目标系数 Hankel 矩阵 [a_(i+j)] 的左上 (n−1) 阶块反三角，反对角线均 −1，其 determinant 为 (−1)^((n−1)n/2)≠0。全矩阵 rank≥n−1。

这是 B 独立指出、Root 纸核的全尺度资产。n≥3 时它排除228所研究的 **秩一目标系数正 Gram** 假设，所以那个停止引理不能直接用于本源。它不保证 rank=3n，也不保证 determinant 在真实 X_c 或任一有理假设点非零。复权 W_c 使正定性也不能免费取得。

## 5. 主选 3ζ(3)+ζ(5) 的完整安全整模型

令 c₃=3、c₅=1、其余为0。则
\[
 \mathcal D_c=\tfrac32\partial_t+\tfrac1{24}\partial_t^3,
 \quad U_c((t+j)^{-1})=j(3\zeta(3)+\zeta(5))-j(3H_j^{(3)}+H_j^{(5)}).
 \tag{L11}
\]
所有 degree、行、列保持 L8；不是只取已知正矩或有限头。

λ_(e,j) 的完整 factorial 公式给
\[
 S_n\lambda_{e,j}=(-j)^e(-1)^{j-1}j\binom{5n}{j}\binom{j-1}{n}^{4}\in\mathbb Z.
 \tag{L12}
\]
S_n 本身是整数；j≤n 时 binomial 为0，恰给零残数。多项式商部 q_e∈Z[t]（整数首一除法）。本列池 e≤6n−2，deg(tq_e)≤5n−1。L5 只涉及此范围内的 Bernoulli 数，其分母由 von Staudt–Clausen 定理整除 d_(5n)，固定 24 清固定阶微分因子；H_j^(5) 全分母整除 d_(5n)^5。因此
\[
 (24S_nd_{5n}^{5})^{3n}Q_{c,n}(T)\in\mathbb Z[T].
 \tag{L13}
\]
该模型包括全部素数、全部幂以及全部 determinant 系数。另由同一公式可知，避开固定 c 的分母/微分阶 factorial 的素数 p>5n 时整个条目多项式都 p-整：残数差不含 p，调和数不含 p，Bernoulli 指数上界小于 p−1。外部素数支持没有随权直接无限扩张；内部素数的 valuation 深度仍会改变。

L13 是安全模型，不能当作所需 primitive 内容率。归一化的 F_n 及全系数 Vandermonde 内容必须一起计入，逐项清分母丢失它们，不能据这个粗模型判断净预算可用。原 K3 的 colVal 中 −2、局部三个 Gram 块和 prime-edge 常数非零约化均依赖原泛函，不能原样升级为 K5/K7。j>p 的调和项也含 p，非 j=p 的残数亦可能在两节点差中含 p；只挑一个极点会漏账。

## 6. 研究方向与有界准入关

L3–L13给出一个区别于239固定三函数源、228秩一 Gram 和222–227固定 Padé 包的实际新对象。主选 X=3ζ(3)+ζ(5)，先于ζ(7)：较少两层调和分母；已有 ζ(3)、ζ(5) 单独无理不蕴含其和无理。本轮没有核定该指定组合全球新颖性，不将检索未命中视为证明。

下一关只处理 **固定 L8/L11 的完整 primitive Gauss 费用与关系点非零**。设 primitive P_(c,n)∈Z[T] 与 Q_(c,n) 相差非零有理 scalar，定义 \(P_{c,n}=d_{c,n}\widetilde Q_{c,n}\)。需要先推实际 p-分解（包括商部、全部残数及各素数幂），检验能否形成固定阶非零约化证书；然后据该同一模型证明 log|d_(c,n)|≤(6−ε)n²+o(n²)，以及任意固定 q∈Q 在无界尺度上 P_(c,n)(q)≠0，或另给同对象的严格判据。两项仍未付。

241–244为有界窗口，第一轮优先尝试固定-base/素数边缘约化，第二轮必须缩小这两项之一的核心缺口。不能把 generic Q≠0、有限头 determinant、rank≥n−1或新安全分母表当作 actual rational-point 非零；也不能只提高外场或枚举参数。若连续两轮只增加外观资产，立即方向检查；244前未有新的可用核心证书则不续开同源局部优化。M₀,₁₀原积分的全尺度 D₃/相对边界证书保留为有条件后备，不因本源初步投影成功而失去它的独立要求。

本轮新数值定理为0。新证明是有限 ζ 组合的完整投影、同外场 leading 率稳定性、增长的目标系数秩以及主选组合的完整安全整模型；它们具体改变下一步，而不完成原研究目标。
