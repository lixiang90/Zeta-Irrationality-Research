# 偶数 Dirichlet beta 值的单周期投影与完整整数行模型

本构造针对 β(4)、β(6) 等单独的偶数 Dirichlet beta 值。它给出只含一个目标周期的真实积分矩阵，并支付行投影在每个素数处的分母；不要求较低的 β 值有理。该结果解决的是目标识别与初步整模型问题。无限尺度的行列式非零性、足够强的实数处衰减和严格的算术差额仍须另证。

日期：2026-10-07。目标 β(s)=L(s,χ₋₄)。以下证明适用于所有整数 s≥2；研究目标采用 s=2m、m≥2。这是本项目新保存的构造，尚不声称文献上的首创。

## 1 精确命中目标的 Cauchy 内核

固定 r=s−1≥1。对 u,v≥0，定义

\[
 C_r(u,v)=\int_0^1\!\int_0^1
 \frac{x^{4u}y^{4v}}{1+x^2y^2}
 \frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy.
 \tag{B1}
\]

几何级数项的积分绝对值之和收敛：其通项为 O(k⁻ʳ⁻¹)，r≥1。因此可用 Fubini，得到

\[
 C_r(u,v)=\sum_{k\ge0}
 \frac{(-1)^k}{(2k+4u+1)(2k+4v+1)^r}.
 \tag{B2}
\]

令有限的有理尾和

\[
 T_{u,a}=\sum_{j=0}^{2u-1}\frac{(-1)^j}{(2j+1)^a},
 \qquad T_{0,a}=0.
 \tag{B3}
\]

平移 2u 个项的符号为正，故

\[
 \sum_{k\ge0}\frac{(-1)^k}{(2k+4u+1)^a}
 =\beta(a)-T_{u,a}.
 \tag{B4}
\]

对角的目标身份精确为

\[
 \boxed{C_r(u,u)=\beta(r+1)-T_{u,r+1}.}
 \tag{B5}
\]

它没有逆中心二项式系数，也不以猜测的新周期代替 β(r+1)。

当 u≠v，设 d=4(u−v)。对任意非零 d，有

\[
 \frac1{(z+d)z^r}
 =\sum_{a=1}^{r}\frac{(-1)^{r-a}}{d^{r-a+1}z^a}
  +\frac{(-1)^r}{d^r(z+d)}.
 \tag{B6}
\]

两项 β(1) 精确相消。这是使用 x⁴ᵘ、y⁴ᵛ 而非任意偶次指数的原因。于是

\[
 C_r(u,v)=A_r(u,v)+
 \sum_{a=2}^{r}\frac{(-1)^{r-a}}{[4(u-v)]^{r-a+1}}\beta(a),
 \quad u\ne v,
 \tag{B7}
\]

其中

\[
 A_r(u,v)=
 -\sum_{a=2}^{r}\frac{(-1)^{r-a}T_{v,a}}{[4(u-v)]^{r-a+1}}
 +\frac{(-1)^{r-1}(T_{u,1}-T_{v,1})}{[4(u-v)]^r},
 \tag{B8}
\]

并定义 A_r(u,u)=−T_{u,r+1}。空和的约定包含 r=1。

例如 s=4、r=3：

\[
 C_3(u,v)=\frac{\beta(3)-T_{v,3}}d
 -\frac{\beta(2)-T_{v,2}}{d^2}
 +\frac{T_{u,1}-T_{v,1}}{d^3},\quad u\ne v;
 \qquad C_3(v,v)=\beta(4)-T_{v,4}.
 \tag{B9}
\]

β(2) 和 β(3) 必须真正消去；知道 β(2) 无理或 β(3) 是 π³的有理倍数并不能替代这一步。

## 2 消去全部低阶周期的显式有理行

取 n≥1、H=rn。原始行索引 u=0,…,H−1，保留的列索引 v=0,…,n−1。记

\[
 J=\{0,\ldots,n-1\},\quad I=\{n,\ldots,H-1\},
 \quad D(z)=\prod_{u=0}^{H-1}(z-u),
 \quad Q_I(z)=\prod_{u\in I}(z-u).
 \tag{B10}
\]

对 k∈J，置 B_k(z)=∏ᵥ∈ⱼ,ᵥ≠ₖ(z−v)。以 [·]ₖ,<ᵣ表示在 z=k 的 Taylor 多项式，保留次数 0,…,r−1。定义

\[
 N_k(z)=B_k(z)^r
 \left[\frac{Q_I(z)}{B_k(z)^{r-1}}\right]_{k,<r},
 \qquad p_{k,u}=\frac{N_k(u)}{D'(u)}.
 \tag{B11}
\]

所有系数有理。deg N_k≤r(n−1)+r−1=H−1，因此

\[
 F_k(z):=\frac{N_k(z)}{D(z)}
 =\sum_{u=0}^{H-1}\frac{p_{k,u}}{z-u}.
 \tag{B12}
\]

在 z=k，B11 与 D(z)/(z−k)=B_k(z)Q_I(z) 的差有零阶至少 r，故

\[
 F_k(z)=\frac1{z-k}+O((z-k)^{r-1}).
 \tag{B13}
\]

在 v∈J、v≠k，N_k 可被 (z−v)ʳ整除，故 F_k(z)=O((z−v)ʳ⁻¹)。合起来，

\[
 p_{k,v}=\delta_{k,v},\qquad
 \boxed{\sum_{u\ne v}\frac{p_{k,u}}{(u-v)^\ell}=0
 \quad(v\in J,\ 1\le\ell\le r-1).}
 \tag{B14}
\]

后式来自在 v 的完整 regular part，不是仅检查留数。B7 的每一种低阶 β(a) 的系数恰对应 ℓ=r−a+1；因此所有低阶周期严格消失。

定义真实的投影矩阵

\[
 E_{k,v}=\sum_{u=0}^{H-1}p_{k,u}C_r(u,v),
 \qquad q_{k,v}=\sum_{u=0}^{H-1}p_{k,u}A_r(u,v).
 \tag{B15}
\]

得到无条件的身份

\[
 \boxed{E=q+\beta(s)I_n,\qquad q\in M_n(\mathbb Q).}
 \tag{B16}
\]

所以每个目标 β(s) 都有一个单周期投影，而不依赖其它 β 值之间任何未证关系。其原积分行是 R_k(x)=Σᵤpₖ,ᵤx⁴ᵘ。

这些行线性独立，因为它们在 u∈J 的系数子矩阵是 I_n。它们同积分列的配对矩阵是否非奇异，是不同的问题。

## 3 全素数的行分母支付

记 d_M=lcm(1,…,M)。对 r≥2，以下给出统一整数模型：

\[
 \boxed{d_H^{3r-2}p_{k,u}\in\mathbb Z
 \quad(0\le k<n,\ 0\le u<H).}
 \tag{B17}
\]

r=1 时直接有 pₖ,ᵤ=δₖ,ᵤ，无需分母。以下证明 B17 不排除任何素数，也不依赖大素数实验。

首先，略去无关的符号，

\[
 a_k:=\frac{Q_I(k)}{B_k(k)^{r-1}}
 =\pm\frac{(H-1-k)!}{(k!)^{r-1}((n-1-k)!)^r}\in\mathbb Z.
 \tag{B18}
\]

分母中 factorial 的参数之和为 H−r−k；补上 (r−1)! 后正好为 H−1−k。因此其绝对值是 (r−1)! 乘一个整数 multinomial coefficient。

写

\[
 \frac{Q_I(k+z)}{B_k(k+z)^{r-1}}
 =a_k\sum_{a\ge0}h_{k,a}z^a.
 \tag{B19}
\]

右边正规化的级数是有限个 (1+z/(k−u)) 和 (1+z/(k−v))⁻ʳ⁺¹的乘积。所有差都是绝对值≤H 的非零整数，负整数指数的 binomial coefficients 也是整数。次数为 a 的每一项的分母都是总次数 a 的这些差的乘积，所以

\[
 \boxed{d_H^a h_{k,a}\in\mathbb Z.}
 \tag{B20}
\]

对 u∈I，B11 可写为

\[
 p_{k,u}=\frac{B_k(u)^r a_k}{D'(u)}
          \sum_{a=0}^{r-1}h_{k,a}(u-k)^a.
 \tag{B21}
\]

其中基数的绝对值为

\[
 \left|\frac{B_k(u)^r a_k}{D'(u)}\right|
 =\frac1{(u-k)^r}
 \frac{(u!)^{r-1}(H-1-k)!}
 {((u-n)!)^r(k!)^{r-1}((n-1-k)!)^r(H-1-u)!}.
 \tag{B22}
\]

对任意素数 p，令 L=⌊logₚH⌋。B22 中 factorial 比的分子有 r 个 factorial，分母有 3r 个，参数总和之差恰为 r。Legendre 公式在每一层 pᵉ≤H 的 floor 差因此严格大于 −r，作为整数至少 −(r−1)；pᵉ>H 时贡献零。故 factorial 比的 vₚ≥−(r−1)L。另一个 (u−k)ʳ损失至多 rL，所以

\[
 v_p\left(B_k(u)^r a_k/D'(u)\right)\ge-(2r-1)L.
 \tag{B23}
\]

B20 给 B21 最后一个因子 vₚ≥−(r−1)L。于是总损失至多 (3r−2)L，恰由 B17 付清。u∈J 的系数为 0 或 1，自然满足同一整性。该证明也给出所有 p>H 的 p-adic 整性。

## 4 整数积分行与有理部分的完整分母

设 mₙ=d_H³ʳ⁻²，令 p̂ₖ,ᵤ=mₙpₖ,ᵤ、R̂ₖ(x)=Σᵤp̂ₖ,ᵤx⁴ᵘ∈Z[x]。相应矩阵

\[
 \widehat E_{k,v}=\int_0^1\!\int_0^1
 \frac{\widehat R_k(x)y^{4v}}{1+x^2y^2}
 \frac{(-\log y)^{r-1}}{(r-1)!}\,dx\,dy
 =\widehat q_{k,v}+m_n\delta_{k,v}\beta(s).
 \tag{B24}
\]

Tᵤ,ₐ中出现的奇数≤4H；B8 中的 |4(u−v)|≤4H。每一项的分母总幂次≤r+1=s，因此

\[
 \boxed{d_{4H}^{s}A_r(u,v)\in\mathbb Z,
 \qquad d_{4H}^{s}\widehat q_{k,v}\in\mathbb Z.}
 \tag{B25}
\]

这里先证明整数行，再相乘，不能把未付费的有理投影当作 unimodular 变换。B17、B25 是当前实际模型的全素数上界；没有借用旧 Catalan 矩阵的两层预算或 48×48 Frobenius 种子。

若假设 β(s)=a/b∈Q，b≥1，则

\[
 b^n d_{4H}^{sn}\det\widehat E\in\mathbb Z.
 \tag{B26}
\]

仅在已另证 det Ê≠0 时，B26 才给 product-formula 下界。记 Δₙ=det E=mₙ⁻ⁿdet Ê；由 log d_M=M+o(M) 得粗界

\[
 \log|\Delta_n|\ge
 -sn\log d_{4H}-(3r-2)n\log d_H-n\log b
 =-(7r^2+2r)n^2+o(n^2).
 \tag{B27}
\]

s=4 时 r=3，常数为 69。它是当前逐项清分母得到的上限费用，远未达到已有 Catalan 论文的精度；不是证明该模型不可能改进的固有下界。全行列式素数秩估计、原列池消元和投影的精确 determinant identity，可能大幅减少这个逐项费用。

## 5 系数高度没有额外的 n² log n 障碍

固定 r。B19 每个因子的分母绝对值≥1，正规化系数的绝对值可由 (1−z)⁻ᴱ的系数控制，其中 E≤2(r−1)n。因此固定 a≤r−1，有 |hₖ,ₐ|=Oᵣ((H+1)ᵃ)。B21 最后因子的绝对值为 Oᵣ((H+1)²ʳ⁻²)。

对 0≤j≤H，统一使用

\[
 \log(j!)=j\log H+j\log(j/H)-j+O(\log(H+1)),
 \tag{B28}
\]

并约定 0 log0=0。由于 B22 的 factorial 参数总和之差是固定 r，所有 H log H 项相消；各 j log(j/H) 的绝对值≤H/e。故

\[
 \max_{k,u}|p_{k,u}|\le\exp(O_r(n)),\qquad
 \max_{k,u}|\widehat p_{k,u}|\le\exp(O_r(n)).
 \tag{B29}
\]

第二式利用 log d_H=O(H)。因此真实行的增长在 n²尺度上可以付款，而非必须损失 n²log n。然而 B29 仅是高度上界；它没有证明目标行列式足够小。

## 6 非零性与严格差额的证据边界

B16 给一个 monic polynomial det(q+TIₙ)∈Q[T]。这证明它不是恒等于零的形式多项式，却不能证明代入真实 β(s) 后非零；更不能在假设 β(s) 有理时免费断言非零。

原始 H×n 积分矩阵的所有 n×n 行子式有共同非零符号：两次 Andreief 后，单项式广义 Vandermonde 在排序节点上为正，Cauchy determinant 1/(1+xᵢ²yⱼ²) 的符号为 (−1)ⁿ⁽ⁿ⁻¹⁾ᐟ²。对数权重在内部为正且可积。这给原矩阵严格的符号正则性。但投影 p 的不同全子式尚未证明具有相容符号，不能从 Cauchy–Binet 自动得到投影矩阵非零。

该单周期模型仍须完成三个实际接口：

1. 对无限 n 序列证明投影 determinant 的非零性；优先寻找 p-index residue 的固定 Frobenius 种子，或证明投影小子式的符号。
2. 对这个具体 row family 建立统一的 n²解析界。它不等于 Catalan 的 Chebyshev 双分支行，不能直接援引其 Hardy 压缩能量常数。
3. 对同一 determinant 改进全素数费用，并证明解析衰减严格超过它。B27 的 69 是 β(4) 首个可审查预算，不是达标证书。

这三个接口完成前，没有新的 β(4) 无理性或 β 值数值线性无关性结论。它们也不能由新仓库的 motivic/Lie 自由性直接补上。

## 7 与已存文献和其它新构造的关系

Lai–Zhou 2021 已证明 β(2)、β(4)、…、β(10) 中至少一个无理，见[论文](https://arxiv.org/abs/2103.00904)。这类集合性结果不能与现有 β(2) 无理性合并推出 β(4) 无理，因为集合结论可能由 β(2) 单独满足。

新仓库的 [Catalan 论文](https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)使用精确周期消去、全原列池整模型、固定 Frobenius 种子和统一 Hardy/energy 界。本构造吸收前两项的要求，单独证明 B16、B17、B25；没有继承其数值常数或 Lean 结论。

同轮的 s-log 内核研究见 [周期分析](catalan_higher_even_beta_period_projection_20261007.md)。原内核只在权重零的 Catalan 情形有 4β(2) 的特例身份；高权重产生更多周期。另一个精确命中 β(2m) 的 outer-log 测度研究见 [解析迁移](catalan_higher_even_beta_analytic_transfer_20261007.md)。它保持原 Hardy 压缩结构，但完整周期消去和有限处费用还未得到。本构造的优势是有限个已命名 β 周期可以完全投影；代价是新的有理行需要另做解析与非零证明。两者构成可以互相核对的具体研究路线。

## 8 证明与核验记录

本稿各等式由纸面证明得到，没有数学 producer、数值拟合、prime 扩表、旧 guard 或 Lean 执行。未改写旧620条冻结记录，也没有把中断前的研究轮追记为已完成。原仓库本轮同步状态为 main 提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a，工作区干净；修复检验和数学验证是不同记录。

本稿 B1–B29 已收到 [独立全文纸审](cdt_beta_single_period_confluent_integral_model_independent_review_20261007.md)，数学结论通过；作者已全文回读。公式 B17 的整格是显式全部素数证明，纸面审查与元数据哈希检查均不称为形式化验证。
