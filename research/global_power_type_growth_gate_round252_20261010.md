# 第252轮：完整幂旗标与算术—增长门槛

2026-10-10。本文提供本次全局选路的一个可证明工具：把完整前缀分母传到所有固定幂，精确计算基本 CDT 的旗标费用，再比较同一实际地图的能量增长。它不是新的数值无理性定理，也不声称相关幂方法在文献中首次出现。

一手基础是 Calegari–Dimitrov–Tang 的 ICM 文稿 Theorem 2.1 与 §3.2–3.3；实际完整读取现存官方 PDF 的物理页3–4、9–13，未读全20页。版本、摘录与读域见本轮 root scope。[官方 PDF](https://math.uchicago.edu/~fcale/papers/ICM.pdf)，[arXiv v1](https://arxiv.org/html/2510.04156v1)。

## 1. 假设必须是完整前缀，不是某一系数的样本

记 $d_N=\operatorname{lcm}(1,\ldots,N)$，$d_0=1$。设

\[
 H(x)=\sum_{n\ge1}h_nx^n\in\mathbb Q[[x]],\qquad H(0)=0,
\]

是 holonomic。固定整数 $b\ne0$ 与有限个非负宽度 $\beta_a$，并假设对每个 $N\ge0$ 和 $0\le n\le N$ 都有

\[
 bD_Nh_n\in\mathbb Z,\qquad
 D_N=\prod_{a=1}^{r}d_{\lfloor\beta_aN\rfloor}.
 \tag{1}
\]

这要求实际整个有理系数源；某个目标列、未付全n的literal $n^w$ 分母猜测、单个素数窗口或有限数值头不能代替(1)。已证明的完整literal $n^w$ 型则确实蕴含 $d_N^w$ 前缀，是本命题的特例。设 $S=\sum_a\beta_a$。以下先固定幂数 $m$，再使用 holonomy 定理；不让 $m$ 随系数索引 $N$ 在一次定理内变化。

对每个 $j\ge1$，令

\[
 D_{N,j}=\prod_{a=1}^{r}\prod_{i=1}^{j}
                d_{\lfloor\beta_aN/i\rfloor}.
\]

则 $b^jD_{N,j}[x^n]H^j\in\mathbb Z$ 对全部 $0\le n\le N$ 成立。证明：当 $n\ge j$ 时，把每个组合 $n=n_1+\cdots+n_j$ 的正整数项降序排列；第 $i$ 项不超过 $\lfloor n/i\rfloor$。由(1)，各 $bh_{n_i}$ 的分母分别被 $D_{n_i}$ 整除，而

\[
 \lfloor\beta_an_i\rfloor\le\lfloor\beta_an/i\rfloor
                         \le\lfloor\beta_aN/i\rfloor.
\]

因此每个卷积项及其和都被所写乘积清分母；$n<j$ 时系数为零。$j=0$ 对应常数1，空乘积为1。固定标量 $b^j$ 可以直接吸收到第 $j$ 行函数中，不影响固定 $m$ 的 leading 型费用。

完整前缀还允许纯算术的整数形式代换：若 $u(x)\in x\mathbb Z[[x]]$，则 $D_{N,j}$ 同时清掉 $b^jH(u(x))^j$ 的全部 $N$ 前缀，因为 $[x^n]u(x)^k$ 是整数且 $k\le n\le N$。一般形式代换并不自动保留 holonomicity、真实函数秩或合法解析图；此处只证明整性。

## 2. 精确的基本 CDT 旗标费用

使用 $m$ 个行函数 $1,bH,\ldots,b^{m-1}H^{m-1}$。对每个 $(a,i)$、$1\le i\le m-1$，放入一列宽度 $\beta_a/i$：前 $i$ 行为零，余下各行为该宽度。这就是 Theorem 2.1 允许的0后接固定宽度列；该列第一非零行是 $H^i$。于是

\[
 \tau_m
 =S\left(\mathcal H_{m-1}-\frac{m-1}{2m}\right),
 \qquad \mathcal H_k=\sum_{i=1}^{k}\frac1i.
 \tag{2}
\]

确实，最后行宽度和是 $S\mathcal H_{m-1}$，旗标扣除项是
$m^{-2}\sum_{i=1}^{m-1}i^2(S/i)=S(m-1)/(2m)$。

对 $m\ge2$，逐项积分给
$1/i-\log(1+1/i)\le1/[i(i+1)]$，因此

\[
 \mathcal H_{m-1}\le\log m+1-1/m,
 \qquad \tau_m\le S\log m+S/2-S/(2m).
 \tag{3}
\]

若 $S>0$，特别有 $\tau_m<S\log m+S/2$。$S=0$ 时 $\tau_m=0$。常见完整 $d_N^w$ 模型只是 $S=w$ 的特例；多个非整数宽度也适用。

真秩 $m$ 另需 $H$ 在 $\mathbb Q(x)$ 上超越：若这些幂有有理函数线性关系，就得到 $H$ 的代数方程。仅仅 $H\ne0$ 或非常数不够，例如 $H=x$。所有固定幂的 holonomicity 由乘积封闭性得到；源的超越性仍须在实际对象上证明，不能由目标值未知性倒推。

## 3. 同一实际地图的三种增长区间

假设已另外证明 $H$ 超越，且对充分大的 $R$ 存在同一实际合法图 $\phi_R$，满足 $\phi_R(0)=0$，所有这些幂的 pullback 均单值 meromorphic，并且

\[
 \lambda_R=\log|\phi_R'(0)|\ge\log R,
 \quad J_R=\iint_{\mathbb T^2}\log|\phi_R(z)-\phi_R(w)|\,d\mu(z)d\mu(w)
          \le CR^{\rho}+C_0,
 \tag{4}
\]

其中 $C>0$、$C_0\ge0$、$\rho>0$ 与 $m,R$ 无关。必须满足所用 CDT 版本的边界/闭盘条件，或另付合法径向近似；这里不从形式的开盘图免费推到边界能量。地图需让实际整个 $H$ 的全部奇点/运输叶合法，单个平方根的圆锥提升不够。

由(3)可取 $\tau_m\le S\log m+B$，例如 $B=S/2$。当 $S>0$，固定 $d>0$ 后设 $R=e^{B+d}m^S$；对充分大的固定 $m$ 有 $R\ge R_0$。于是 $\lambda_R-\tau_m\ge d$，基本 CDT 要求

\[
 md\le C e^{\rho(B+d)}m^{S\rho}+C_0.
 \tag{5}
\]

因此这个已支付的证书具有明确门槛：

* $S\rho<1$：固定 $d$，足够大的固定 $m$ 与(5)矛盾。
* $S\rho=1$：充分条件为 $C\rho e^{\rho B+1}<1$。取使 $d e^{-\rho d}$ 最大的 $d=1/\rho$，严格差额在足够大的固定 $m$ 吸收 $C_0$。
* $S\rho>1$：这些 upper 证书没有自动的大幂矛盾。它不证明实际方法失败；更好的整型、能量、常数、有限处收益或有限秩证书仍可能改变结果。

$S=0$ 时取任意固定且足够大的合法 $R$，令 $\lambda_R>0$，再令固定 $m$ 增大即可；无需上面的随 $m$ 选择式。

此工具得到数值无理性还需要：假设目标数有理时确实产生满足(1)–(4)的同一个有理系数 $H$；完整数值周期投影、固定标量、超越性/真秩与真实路径都必须独立支付。形式 motivic 非零不是数值投影单射性。数域的加权多实处版本须另写完整权重与整模型，不能把(5)直接贴到 $\mathbb Q(\sqrt2)$ 上。

## 4. 为什么这能指导选路，不能替代核心证书

ICM §3.3 对已知 $\pi$ / logarithm 示例先付完整 $d_N$ 模型和两有限支点的真实二面体源，再付一处导数 $R^2$、其余处 $R$ 的全部 pullback。能量 $O(R)$ 相对于加权导数给有效指数 $d/(d+1)$；有理域 $d=1$ 时是 $\rho=1/2$，$S=1$ 属于亚临界区。这解释了幂数增加为何真正有效，而不是仅增加形式秩。

在同样已支付的地图增长下，普通 weight2 型 $S=2$ 已到临界区，更高 $S$ 进入超临界区；该比较没有断言实际 $\zeta(7)$ 源有二面体地图。ICM Lemma 3.2 的 order $1/2$ 图须整个实际源仅有指定的两有限支点及无穷点、且某一原生叶已真补支。当前 Fricke 源还涉及其它有限点、cusps、共轭与运输叶，251只付部分圆锥必要条件，不能凭它借用此图或重开默认窗口。

Pasol–Zudilin 的 magnetic divisibility 可在特定实际 modular 核上降低完整分母层数，是可能改变 $S\rho$ 的宏观机制。它未自动给本项目目标的纯数值周期、全部合法图或秩。多端点 Padé 及完整 cyclotomic trace 可以改变目标投影，但也未自动改进能量。这些须在同一对象重新对齐。

本轮因此把“能否改变完整门槛”置于局部引理数量之前。当前 Fricke、K5 与两个不同χ−7矩阵不再默认续窗；新方向必须先给一个明确、全n、同对象的首证书，再决定是否值得付总预算。没有新数值无理性或线性无关性结论。
