# beta(4) 原 Hermite 投影的固定 23 幂次三层非零定理

日期：2026-10-07。本稿的新结论是完整的无限尺度非零接口：对每个固定的 T∈Q₂₃，原矩阵 E_n(T)=q_n+TI_n 在 n=23^j、4j+v₂₃(T)≥3 时非奇异。这里 q_n 是原单周期积分模型的有理部分，没有换行族，也没有假定其它 beta 值有理。特别地，在 beta(4) 有理的假设下，得到无限多个真实投影 determinant 非零。同一 determinant 的实处衰减已由审过的[实处 energy 稿](cdt_beta4_real_determinant_energy_20261007.md)建立；尚缺严格超过完整有限处费用的差额，本稿不证明 beta(4) 无理。

直接输入已实际全文读完：[原模型](cdt_beta_single_period_confluent_integral_model_20261007.md)、[精确算术稿](cdt_beta4_projection_exact_arithmetic_20261007.md)、[素数尺度稿](cdt_beta4_projection_nonvanishing_20261007.md)。先用 rg 搜索 fixed23、23 幂次、carry、Frobenius 及 B_k(k)：这些 beta(4) 稿仅登记该传递为缺口，未找到同一已存定理。以下证明自足；有限模运算仅用于展示固定 5×5、6×6 证书，没有运行旧 producer、扩展 prime 表、改写冻结记录或旧稿。

## 1 原对象与结论

固定 p=23，j≥1，n=p^j，N=p^(j−1)，J={0,…,n−1}，I={n,…,3n−1}。沿用原对象

\[
 D(z)=\prod_{u=0}^{3n-1}(z-u),\quad
 B_k(z)=\prod_{v\in J\setminus\{k\}}(z-v),\quad
 Q_I(z)=\prod_{u\in I}(z-u),
\]
\[
 N_k=B_k^3[Q_I/B_k^2]_{k,<3},\qquad P_{k,u}=N_k(u)/D'(u).
 \tag{F1}
\]

用 P 表示投影，避免与素数 p 混淆。原完整 regular-part 条件给 P_J=I 和全部一、二阶周期消去。准确的有理部分为

\[
 q_{kv}=\frac1{64}\sum_{u\ne v}
 \frac{P_{k,u}(T_{u,1}-T_{v,1})}{(u-v)^3}
 -\delta_{kv}T_{v,4},\quad
 T_{u,a}=\sum_{h=0}^{2u-1}\frac{(-1)^h}{(2h+1)^a}.
 \tag{F2}
\]

设

\[
 m_j=\lceil n/4\rceil,\qquad d_j=\lfloor N/4\rfloor,\qquad
 \varepsilon_j=(-1)^{(n-1)/2}=(-1)^j.
 \tag{F3}
\]

**已证定理 F4。** 若 T∈Q₂₃ 且 4j+v₂₃(T)≥3（T=0 时取估值 +∞），则

\[
 \boxed{\det(q_n+TI_n)\ne0,\qquad
 v_{23}\det(q_n+TI_n)=-4jn+m_j+d_j.}
 \tag{F4}
\]

更准确地，整矩阵 p^(4j)(q_n+TI_n) 的 Smith 指数为

\[
 \underbrace{0,\ldots,0}_{n-m_j},\quad
 \underbrace{1,\ldots,1}_{m_j-d_j},\quad
 \underbrace{2,\ldots,2}_{d_j}.
 \tag{F5}
\]

j=1 时 d₁=0，F4 给 −4·23+6=−86，回收原种子。对任何固定有理 T，包括既约分母含任意 23 幂次的 T，上述条件对所有充分大的 j 成立。未知实数 beta(4) 没有在此被无条件当成 Q₂₃ 元素；正确应用是在其有理性的假设下代入。

## 2 所有分母层与归一化 Taylor jets

原精确二项式身份给，对 u∈I，d=u−k，

\[
 P_{k,u}=b_{k,u}\{1+\sigma_k d+(\sigma_k^2+\tau_k)d^2/2\},
\]
\[
 b_{k,u}=(-1)^{3n-1-u}
 \binom uk^2\binom{3n-1-k}{u-k}
 \binom{u-k-1}{u-n}^3\in\mathbb Z,
 \tag{F6}
\]
\[
 \sigma_k=\sum_{u\in I}(k-u)^{-1}
 -2\sum_{v\in J\setminus\{k\}}(k-v)^{-1},
\quad
 \tau_k=-\sum_{u\in I}(k-u)^{-2}
 +2\sum_{v\in J\setminus\{k\}}(k-v)^{-2}.
 \tag{F7}
\]

B_k(k) 在 j>1 一般不是单位，不能沿用素数稿的未归一化整级数。本稿使用 x_j(k)=nσ_k、y_j(k)=n²τ_k；所有非零差的估值≤j，所以这两个量确实在 Z_p 中。F6 已精确包含 Taylor 的 0、1、2 阶，不漏 denominator 层或未正规化常数。

写 u=an+i，a=1,2，0≤i<n，s=v_p(u−k)。逐 Legendre 层 e=1,…,j，把 factorial 身份

\[
 |b_{k,u}|=
 \frac{(u!)^2(3n-1-k)!}
 {(u-n)!^3(k!)^2(n-1-k)!^3(3n-1-u)!(u-k)^3}
 \tag{F8}
\]

中的 floors 展开。每一层 factorial 分子减分母恰为 3；例如 floor((3n−1−k)/p^e)=3n/p^e−1−floor(k/p^e)，其余项同理。因为 3n<p^(j+1)，没有 e>j 的 factorial 层。因此

\[
 \boxed{v_p(b_{k,u})=3(j-s).}
 \tag{F9}
\]

这里 0≤s≤j；s=j 恰是 u=k+an。

写 k=i+pK，n=pn′。F7 中与 k 同余的节点严格给出较小尺度的 jets，其余差都是 p 单位。因此

\[
 x_j(k)=x_{j-1}(K)+nR_1,\qquad
 y_j(k)=y_{j-1}(K)+n^2R_2,
 \tag{F10}
\]

其中 R₁、R₂∈pZ_p：在每个其它模 p 剩余类，I 的项数为 2n′，J 的项数为 n′，常数余数的 2−2 或 −2+2 恰消去。于是误差分别在 p^(j+1)、p^(2j+1) 中。该证明包括低位进位与任意 k，不只适用于整倍数节点。

在 j=1，删去两个 matching 因子后，设 d=k−i（i≠k）。

\[
 R_1=\sum_{i\ne k}\{(d-p)^{-1}+(d-2p)^{-1}-2d^{-1}\}
 \equiv3p\sum_{i\ne k}d^{-2}\pmod {p^2},
\]
\[
 R_2\equiv-6p\sum_{i\ne k}d^{-3}\pmod {p^2}.
\]

模 p 的差 d 枚举全部非零元，二、三次逆幂和为零。故 R₁,R₂∈p²Z_p，并由 F10 归纳得到完整 uniform jets：

\[
 \boxed{x_j(k)=-3/2+O(p^3),\qquad
 y_j(k)=-5/4+O(p^4).}
 \tag{F11}
\]

对 s<j，F6 的二次项严格主导，F9 给

\[
 v_p(P_{k,u})=j-s.
 \tag{F12}
\]

对 u=k+an，括号的主项为 (a−1)(a−2)/2=0，F11 支付剩余项，而 b 是单位，故

\[
 \boxed{P_{k,k+an}\in p^3Z_p\quad(a=1,2).}
 \tag{F13}
\]

特别是原 P 全体 p 整。F13 比单素数稿的 p² 安全界更强；这里使用的是固定三层保护，不能将它免费乘成 3j 层。

## 3 第一关联分次与实际簇的模 p³ 传递

对 factorial 的剥离单位，可由 Wilson 逐层证明

\[
 p^{-v_p(a!)}a!\equiv(-1)^{v_p(a!)}\prod_e a_e!\pmod p,
 \tag{F14}
\]

其中 a_e 是 p 进制各位。把 F8 的 factorial 组合代入 F14：低位 i_e 的 factorial 比是 (−1)^(i_e+1)，k_e 的比为 1；Wilson 指数和为 3j。合并原符号后，整个 factorial 比的 p^(3j) 剥离单位为 (−1)^a C_a，C₁=2、C₂=8。故若 k≠v、s=v_p(v−k)、δ=(v−k)/p^s，F11 给

\[
 \boxed{P_{k,v+n}/p^{j-s}\equiv-1/\delta,\qquad
 P_{k,v+2n}/p^{j-s}\equiv4/\delta\pmod p.}
 \tag{F15}
\]

还需高于首层的真正传递。以下是自足的 p-free factorial 引理。

**引理 F16。** n=pn′，k=i+pK、u=i+pU，0≤i<p，则

\[
 b^{(n)}_{k,u}/b^{(n′)}_{K,U}\equiv1\pmod {p^3}.
 \tag{F16}
\]

比值是 p 单位。证明令 f(a)=∏_(1≤h≤a,p∤h)h，a!=p^floor(a/p)floor(a/p)! f(a)。F8 中 floors 的指数为 3，恰与 (u−k)³ 的 p³ 相消。剩下的比值是

\[
 (-1)^i\frac{f(u)^2f(3n-1-k)}
 {f(u-n)^3f(k)^2f(n-1-k)^3f(3n-1-u)}.
 \tag{F17}
\]

令 W=(p−1)!、H_i=Σ_(h=1)^i1/h、H_i^(2)=Σ_(h=1)^i1/h²。配对 h,p−h，加上 F_p^× 的平方逆幂和为零，给 H_(p−1)∈p²Z_p、H_(p−1)^(2)∈pZ_p。每个完整 p-free 块因此为 W mod p³，并有

\[
 f(pA+i)\equiv W^A i!\{1+pAH_i+
 p^2 A^2(H_i^2-H_i^{(2)})/2\}\pmod {p^3}.
 \tag{F18}
\]

对 c=p−1−i，H_c≡H_i+pH_i^(2) mod p²，H_c^(2)≡−H_i^(2) mod p。F17 中 i 残尾的线性 A 和为 X=−U+3n′−2K，c 残尾的线性和为 3−X；两类平方 A 和之差恰 −2X+3。用有限二阶 log 展开，所有 X 项消去，残尾因子的 log 为 3pH_i+(3/2)p²H_i^(2)。另一方面

\[
 (-1)^iW^3\{i!c!\}^{-3}
 =\prod_{h=1}^i(1-p/h)^3
\]

的 log 是其相反数。因此比值为 1 mod p³，证明 F16。这里使用的 log 只是次数≤2 的代数恒等式，全部分母 2 为 p 单位。

若固定一个真实簇 r mod N，写 k=r+NK、u=r+NU。重复 F16 j−1 次，b 的比值为 1 mod p³。F10 同时给 x_j(k)≡x₁(K) mod p³、y_j(k)≡y₁(K) mod p⁵。对 K≠V、u=r+N(V+ap)，b 估值为 3，而 d/n=(V−K+ap)/p 的最低估值为 −1。因此 jets 误差和 b 比值误差均使 P 的误差至少为 p⁴。对 K=V，F13 直接够用。得

\[
 \boxed{P^{(p^j)}_{r+NK,r+N(V+ap)}
 \equiv P^{(p)}_{K,V+ap}\pmod {p^3}.}
 \tag{F19}
\]

这是所有 j、r 的证明；n=529 的指定 r 检查不承担归纳证明。

## 4 全 harmonic 层、epsilon 与前三层原矩阵

实际奇分母≤12n−5<23n=p^(j+1)，所以其全部 p-power 层至多 j。令 α_v=4v/n∈[0,4)。最高层 simple-tail 差为

\[
 H_a(v)=\sum_{\substack{
 b\ \mathrm{odd}\\
 \alpha_v<b<\alpha_v+4a}}
 \frac{(-1)^{(b-1)/2}}b,\quad a=1,2.
 \tag{F20}
\]

准确地，

\[
 \boxed{n(T_{v+an,1}-T_{v,1})
 \equiv\varepsilon_j H_a(v)\pmod {p^2}.}
 \tag{F21}
\]

证明必须包含第 j−1 层：其奇分母 p^(j−1)b 枚举一个长度 4ap 的区间中的奇数，恰有 2ap 个。非 p 倍数部分可分成 a 个含 2p 个奇数的完整块，并配对 b,b+2p；分母 mod p 相同，交错符号相反，故该层归一化后的 p 系数为零。更低层归一化后已经在 p² 中。j=1 时同一配对支付全部 unit-denominator 部分。符号 (−1)^((p^j b−1)/2)=ε_j(−1)^((b−1)/2)，不能把 ε_j 固定成 ε₁。

最高层第四尾为

\[
 n^4T_{v,4}\equiv\varepsilon_j d(v)\pmod {p^4},\quad
 d(v)=\begin{cases}0,&\alpha_v<1,\\1,&1<\alpha_v<3,\\80/81,&3<\alpha_v<4.\end{cases}
 \tag{F22}
\]

因为 n 奇数，α_v 不会等于 1 或 3。所有较低奇分母的第四幂至少多四层。

设 M=ε_j^(-1)p^(4j)q_n。其 entries 在 Z_p。对 F2 的 u∈I、u不等于v+an，记 h=v_p(u−v)<j、t=v_p(u−k)。若 t<j，F12 与尾估值≥−j给该项在 M 中的估值≥4j−t−3h≥4；若 t=j，F13 给更强估值≥6。低节点 u=k 的非对角项估值≥3(j−v_p(k−v))≥3。故 mod p³ 的全部原矩阵，只剩 F22 对角及两条 u=v+an 的尾项。F21 的误差至少 p²，乘非对角 P 至少 p 后即消失；matching P 已在 p³。

对全部 s=v_p(v−k)<j，还可比较其它项与预期首项的 M 估值 j−s：若 h>s 则 t=s，若 t>s 则 h=s，若 h=t 则 h≤s。上述三种情形给其它高节点估值至少分别为 j−s+3、3(j−s)+1、4(j−s)，均至少多三层；matching k 节点和低节点也严格更高。由此不只是前三层，对低块 L={0,…,m_j−1} 的所有 k≠v 都得到

\[
 v_p(q_{kv})=-3j-v_p(v-k),\quad
 p^{3j+s}q_{kv}\equiv-\varepsilon_j/(210\delta)\pmod p;
 \tag{F23}
\]

低对角在 M 中为 p³ 整除。全块非对角 M 估值≥1；高对角模 p 为 −d(v)，单位。

三种列相位的准确 off-diagonal 首项常数为

\[
 c(v)=\sum_{a=1}^2\frac{c_aH_a(v)}{64a^3}
 =\begin{cases}-1/210,&\alpha_v<1,\\1/1260,&1<\alpha_v<3,\\-1/3465,&3<\alpha_v<4,\end{cases}
 \quad(c_1,c_2)=(-1,4).
 \tag{F24}
\]

例如三种 H₁ 为 2/3、−2/15、2/35，三种 H₂ 为 76/105、−52/315、268/3465。这明确包括 9n、11n 的新分母。

## 5 第一低层的 A₅、A₆ carry 与下一层有限证书

按 r mod N 分簇。m_j=5N+r₀，r₀=ceil(3N/4)，所以 r<r₀ 的低簇有 K=0,…,5 六点，其余 r≥r₀ 有 K=0,…,4 五点。令 A_ℓ(K,V)=1/(V−K)，K≠V，零对角。由 F19、F23，M 的低首层是 p c_L A_ℓ，c_L=−1/210≡15 mod23。A₆ 是单位，因为 Pf(A₆)=2593/2160；A₅ 秩为四，因四阶主 Pfaffian 13/12 非零。五点簇有共同核向量

\[
 w=(3,9,9,9,3)^t\in\mathbb F_{23}^5,\qquad
 A_5w=0,\quad\sum_Kw_K=10.
 \tag{F25}
\]

例如有理 Pfaffian 核向量为 (13/12,−7/12,73/72,−7/12,13/12)，其 mod23 恰为 F25。因此第一低层缺损数为 d_j=N−r₀=floor(N/4)。仅复制成功 A₆ 种子会漏掉这些核。

为计算其下一层，固定五点簇。F11、F19 使其中的 P mod p³ 可由如下完全整数的固定 seed 公式给出（K≠V）：

\[
 P^{(p)}_{K,V+ap}\equiv
 b^{(p)}_{K,V+ap}\frac{(V+ap-K-p)(V+ap-K-2p)}{2p^2}
 \pmod {p^3}.
 \tag{F26}
\]

b 在 p³ 中，右边确实是整数。K=V 的 residue 为零。以 H₁=2/3、H₂=76/105 组成低块局部矩阵

\[
 U_{KV}=\sum_{a=1}^2
 P^{(p)}_{K,V+ap}H_a/(64a^3)\pmod {p^3}.
\]

直接代 F6、F26 得 U=p c_L A₅+p²X mod p³，其中 c_L A₅ 取原有理的反对称 lift，而

\[
 X=\begin{pmatrix}
 0&11&20&14&5\\11&0&11&20&14\\20&11&0&11&20\\
 14&20&11&0&11\\5&14&20&11&0
 \end{pmatrix}\pmod {23},\qquad w^tXw=1.
 \tag{F27}
\]

这是固定有限证书，可仅用所显示的二项式整数式逐格重算，不是拟合。直接的整数 contraction 为 wᵗXw=11754≡1 mod23。使用 w 的任意 p-adic lift 不改变该 contraction：首层反对称且 w 左右均在其核中。

还要消去全部真实高列。五点簇 r≥r₀ 的 θ=r/N∈[3/4,1)，其同簇高 K=5,…,22；K≤16 的 d=1、c=1/1260≡9，K≥17 的 d=80/81≡22、c=−1/3465≡3。其它簇的高列因至少多一层，其二次 Schur 项在 p³ 中。令

\[
 a_K=\sum_{i=0}^4w_i/(K-i).
\]

按 K=5,…,22 顺序，a_K 的 residues 为
\[
 (3,1,17,3,19,13,0,15,4,19,8,0,10,4,20,6,22,20).
\]
平方后两段分别相加，得到

\[
 \sum_{K=5}^{16}a_K^2=9,\qquad
 \sum_{K=17}^{22}a_K^2=10,\qquad
 F=9\cdot9+(3/22)\cdot10=5\pmod {23}.
 \tag{F28}
\]

高块 mod p 对角为 −d；同簇 low-high 首项为 p c(K)/(K−i)，high-low 首项为 −p c_L/(K−i)。故真实高 Schur 补在该核上的贡献是 −p²c_LF。结合 F27，局部 residual 对角是

\[
 h=1-c_LF=1-15\cdot5=18=-5\pmod {23}.
 \tag{F29}
\]

这一步支付全部高列，并没有只取 K=5 的一个便利子列。

不同五点簇 r,r′ 之间，只有 v_p(r′−r)=j−2 可以在 p² 层留下项；F15、F23 给其 kernel contraction 为

\[
 \frac{c_L(\sum_iw_i)^2}{(r'-r)/p^{j-2}}
 =\frac5{(r'-r)/p^{j-2}}\pmod {23}.
 \tag{F30}
\]

更低 carry 的项在 p³ 中。第一低层其它单位 pivots 的进一步 Schur 项也在 p³ 中，因为与 kernel 相接的两边已经各在 p² 中，而该 pivot 只损失一层。

## 6 完整三层消元与无限结论

高块先提供 n−m_j 个单位 pivots。低簇的 A₆ 单位、A₅ 四阶单位提供 m_j−d_j 个一层 pivots。可在每个 A₅ 使用同一行列基 (e₀,e₁,e₂,e₃,w)，其 determinant w₄=3 为单位，故全部变基都在 GL(Z_p) 中。

剩余 d_j 个位置是 r∈[r₀,N)。按 r mod p^(j−2) 分簇，每簇含连续的五或六个最高位；F29、F30 说明其 p² 层为

\[
 \boxed{5(A_\ell-I_\ell),\quad\ell=5\text{ 或 }6.}
 \tag{F31}
\]

连续数字的起点仅平移核索引，不改变 A_ℓ。普通模23消元无需换行的 pivots 为

\[
 A_5-I:\quad22,21,7,8,19;\qquad
 A_6-I:\quad22,21,7,8,19,22.
 \tag{F32}
\]

因此 det(5(A₅−I))=10、det(5(A₆−I))=19 mod23，均为单位。这完成全部 residual，并证明 F5。j=1 没有 A₅ kernel，直接由 A₆ 种子完成同一结论。

若加入固定 T，其 M 增量为 ε_j^(-1)p^(4j)TI。在 4j+v_p(T)≥3 时该增量在 p³M_n(Z_p) 中，上述三个层次和合法 Schur 消元全不变。F5 给 determinant 估值 m_j+d_j；去掉原 uniform 缩放 p^(4jn) 便得 F4。

**证明边界。** F4 是原 q_n+TI_n 的无限非零定理，目标 rational denominator 的 23 例外已通过充分大 j 支付。它不依赖 root 另推的单尺度 Newton polygon，也不要求对 T 的第三、四分母层另行排除。同一 determinant 的实处 n² 衰减见已审[实处 energy 稿](cdt_beta4_real_determinant_energy_20261007.md)；尚未证明其严格超过 771/40 完整有限处费用的差额。本稿没有由形式 monic 性推出目标特殊化。

## 7 计算与核验的实际范围

数学主证是 F6–F32 的纸面全 j 推导。为核对 F19，运行一次新的即时 exact modular arithmetic，固定 n=529、r=0,1,17,18,22、K=0,2,4,5 的四个指定 U，所有 projection 模23³与 n=23 seed 相同；该有限检查不承担一般证明。随后用新的即时整数二项式/有理模运算计算固定 F25–F32 表，并对 F21 的五个指定 (j,r,V,a)=(1,0,4,1)、(1,0,5,2)、(2,18,5,1)、(2,18,17,2)、(3,400,5,2) 逐项累加完整 simple tail，模23²差全部为零。没有保存或执行新的 producer 文件，没有运行旧脚本，没有随机 prime 扩表。未新增 PDF 或引用未实际核读的 primary 文献。

root 已实际全文读取七节 F1–F32 并独立纸审通过，另展开核对 F17 的平方 A 和之差、F19 的完整 jets 误差、F21 的低层配对、F23 的全部 carry 分支及高簇相位。energy 代理另实际全文纸审通过，并独立重算 X、完整高 Schur contraction 与五、六阶 pivots 全部通过。作者完成收审修订后的最后全文回读；纸面审查与有限 exact checks 不称为形式化验证。
