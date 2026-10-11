# 混合 ζ、角色迹与全 weight 非零机制：独立全文审阅

日期：2026-10-06。审阅人：quarter_actual_rank。本文 NEW，仅保存本轮独审。实际完整读取 [root 最终研究稿](cdt_odd_mixed_zeta_character_hankel_reduction_20261006.md) H1–H9，SHA256 **e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463**。初稿 253aa72d 已全文读，加入 H9 后又完整读最终稿，最后单独输出重读，输出没有截断。

全部旧/同行数学 MD、PY、JSON、manifest 只读；没有执行、import、重跑其中任何 producer。本轮本人没有新数学 producer，也没有外部 Lean execution/compilation。本审阅是全尺度纸面核验。

## J1. 来源与实际阅读的准确范围

本人实际读取 Lai 一手 PDF **1–7、20–23**，11 个不同页，未读完整 25 页：

literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf，
SHA **838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58**。

PDF 1–7给布局、double-pole partial fractions、Hermite/auxiliary-prime机制和 weight4算术背景；20–23给解析 upper bound、Proposition6.6及参考文献。此前一次组合输出的 20–23 部分截断，已另一次单独完整输出和实际读取；截断未算完成。该来源精确目标是 1、ζ(3)、ζ(4)。简介 31.6 概述和 Proposition6.6保守 −31显示界不能混称同一个已核格式；正文最终明确区分。

本人还实际完整读取 Tang immutable commit 669c92bf7a3728e0de9ad80c373bc29fb5ca3d58 下六份 source（只读，未编译）：

| literature/tang2026_zeta2_zeta3_sources_20261006/ 下文件 | SHA256 |
|---|---|
| Zeta32/Family.lean | 59d46a8462ac426bd393864d849bf4cd0f906399c4c583c9736b10835e289dbd |
| Zeta32/Interfaces.lean | 6279a135507e741685a7ba5ea688ad5d5b88044160d088d76c5c23bff3493673 |
| Zeta32/Analytic/Contour/Kernel.lean | b9c44e434de925996a975c5b2521e235128c4ebd98610a69e5b938c7e6f11489 |
| Zeta32/Analytic/Energy/Defs.lean | 4a1ceb8a3d7780b3cf9335e60d5275ffbbc56ba3164f890ec23714e3197f951d |
| Zeta32/Assembly.lean | 47b634df5e4b2cf04232658cdc3c1de013cf4b1216d97e816ccb9fc8aeb66276 |
| Zeta32/Criterion.lean | 5afe2e69a7ac6168921dfd0997232e69d9e8ffdd1edbdbb9251a62e2448e020a |

Energy/Defs初次 tail输出截断后又完整读，未将部分输出当全文。Assembly 是 three nodes 蕴涵结论的总装，其 assumptions 不代替全部 arithmetic/energy/nonvanishing依赖证明。本人未读完整 Tang repo，未实际读 Liu repo，本轮未执行任何外部 Lean。Root 的 22-file archive与 14-full/1-partial/7-archived-only scope 是 root收据范围，不冒认本人全读。

最终来源收据的只读 pin：

- literature/manifest_cdt_odd_lai2026_mixed_zeta_20261006.json，SHA **0b1cfbd3713c18ebb234b74079e4a95cceaa2fc83a874d74b4bbf2f3fa2d1634**：本人实际完整读该小收据，proof pin吻合。
- literature/manifest_cdt_odd_2026_polylog_primary_sources_20261006.json，SHA **68d48519b01704d10e8aa025fd969e7e646bdf21f3b3d405082885cfc7ac6333**：本人读取最终 metadata及22个 source items的 path/commit/SHA/read scope，不声称全部原始 JSON字节全文阅读。

PDF/source acquisition 的 normal TLS、immutable commit与上传日期由 root来源收据登记；本人本轮未下载这些字节，未独立联网核验全部版本时间。Actual原页/source阅读与 archive metadata明确分开，不能据此称本项目完整核验了外部论文或 Lean内核。

## J2. H2 contour、Fubini 与矩身份

令 \(t=1/2+iy,\rho=\pi/(2\cosh^2\pi y)\)。对列明的 fixed rational f，ρ及每阶导数 exponential decay，f及其 fixed derivatives至多 polynomial growth，因此积分与所有 IBP绝对合法。\(y\)-导数给 \(i^a f^{(a)}\)，故
\[
J_a(f)=i^a(-1)^ai^a\int f^{(a)}(t)\rho\,dy
=\int f^{(a)}(t)\rho\,dy.
\]
没有少一个负号或 i。

高度 −i 的 clockwise rectangle只围住 −i/2 double pole，
\(\rho(z)\sim-1/(2\pi(z+i/2)^2)\)。Exponential的导数给 residue \(iu e^{-u/2}/(2\pi)\)，clockwise −2πi 故得到 \(u e^{-u/2}\)。Bottom bank是 \(e^{-u}\) 倍 top，vertical tails消失，因而
\[
I(u)=u/(2\sinh(u/2)),\qquad
E[e^{-ut}]=u/(e^u-1).
\]
u=0 by normalization；near-zero bilateral generating function由 decay解析成立。

Laplace表示的 absolute Fubini以 \(\Re(t+j)=j+1/2>0\) 保证；取ρ积分后
\[
E[(t+j)^{-k}]=\frac1{(k-1)!}\int_0^\infty
u^ke^{-ju}(e^u-1)^{-1}du
=k(\zeta(k+1)-H_j^{(k+1)}).
\]
Bernoulli generating function给 \(E[t^m]=B_m(1)\)，J_a的 falling factorial identity正确，B₁(1)=1/2已固定 convention。这些是 root新纸面证明，不需假设外部 Lean验证。

## J3. Simple-pole target polynomial、解析 envelope 与条件判据

对 a≥1，\(t/(t+j)=1-j/(t+j)\) 给
\[
J_a(t/(t+j))=(-1)^{a+1}(a+1)!j
(\zeta(a+2)-H_j^{(a+2)}).
\]
Odd s≥5 时 s−2 odd、s−3 even，所以两项 precisely形成
\[
(s-1)!j\,[\zeta(s)-r\zeta(s-1)-H_j^{(s)}
{}+rH_j^{(s-1)}].
\]
s=5、7核的 i与负号正确。s=3含 J₀，额外 2r常数不能删；它与 Tang source的 r-family实际矩身份吻合。

H4 必须在 \(R_{n,k}\) partial fraction之后乘 t。因此 moments是
\(\mathcal J(tP_{n,k})+\sum a_{n,k,j}\mathcal J(t/(t+j))\)，实际 integral有 \(t^{k+1}R_n\)，并非 \(t^kR_n\)。Hankel entries affine X，det degree≤h；positive rational primitive normalization存在，但未给 content/cost。正文保留该限制。

ρ⁽ᵃ⁾/ρ是 fixed tanh polynomial，故 \(|K_{s,r}|\le C_{s,r}\rho\)。有限 determinant展开、absolute exponential tails和 polynomial growth可直接证明 Andreief；\(t_i-t_j=i(y_i-y_j)\) 的 Vandermonde phase只影响 sign，absolute bound恰 H5.2。Tang actual Interfaces 的 Heine integrand含 **tR_n**；\(w_1=2\rho+i\rho'\)，\(|w_1|\ge2\rho\)，因此本 positive envelope逐点受该 absolute bound控制，比例 \((C/2)^h\)只贡献 O(n)。这只转移解析 upper bound形状；不转移 −6严证、primitive算术283/50、非零性或 growing s uniformity。

H6 的 \(c_n>0,\widetilde d_n>0\) 已明示。若 \(\deg P_n=O(n)\)、\(\log\widetilde d_n\le An^2+o(n^2)\)、\(|\widetilde Q_n(\xi)|\le e^{-Bn^2+o(n^2)}\)，B>A，且每个 rational v有无穷非零 P_n(v)，则假设 \(\xi=a/b\) 后 \(|b^{\deg P_n}P_n(a/b)|\) 是非零整数却趋0。Condition3不能被 primitive或 signed Heine积分代替。旧 simple-pole布局的新 weight Condition3仍未证，正文没有误用 H9替代它。

## J4. Hurwitz/角色 trace 与实际未完成的 energy接口

以 \(t_\beta=\beta-1/2+iy\)，same logistic transform给 \(E e^{-ut_\beta}=ue^{-u\beta}/(1-e^{-u})\)。j≥1使 real part仍正，故
\[
E[(t_\beta+j)^{-k}]=k\zeta(k+1,j+\beta),\quad
E[t_\beta^m]=B_m(\beta).
\]
Finite removed Hurwitz tails均 rational。对 rational nontrivial χ，
\(\sum_a\chi(a)\zeta(v,a/q)=q^vL(v,\chi)\)；lower derivative的 extra rq恰补 q-power，H7.2 target系数 \((s-1)!j q^s\) 正确。s=3的 J₀ rational intercept另列即可。

多个 β的 contours实际横向平移，跨 contours 的 \(\Delta(t)\) 不能统一换成 \(i^{h(h-1)/2}\Delta(y)\)。因此 H5单直线能量不能直接套角色 sum。正文明确保留 multi-contour energy、all-prime content/nonvanishing；parity-known π-power结果也未冒记新结果。Catalan型目标在这里只是正确 target identity。

## J5. H9 double-pole form 的 exact target识别

逐项独算 H9，不仅以 Lai weight4 case作类比。对 \(\deg P<6n\)，\(\deg(\mathscr R_nP)\le-3\)，partial fractions没有 polynomial part，sum of simple coefficients \(\sum A_{1,j}=0\)。在 −j取 residue可得
\[
A_{2,j}=W_jP(-j),\quad
A_{1,j}=W_j(P'(-j)+C_jP(-j)),
\]
\[
W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad
C_j=5H_j-3H_{2n+j}-2H_{6n-j}.
\]
C_j是 actual logarithmic derivative；numerator2n负因子数为偶数，W_j正号正确。

第 d导数的 simple coefficient为 \((-1)^d d!\)，double为 \((-1)^d(d+1)!\)。H9.2的 two signs分别取消；\(\sum A_1=0\)杀低 ζ weights，而 double terms形成 \((s-1)![a\zeta(s-1)+b\zeta(s)]\)。候选 relation给 c后得到 exact rational form
\[
U_j=-(s-1)a(s-3)!H_j^{(s-2)}
-b(s-2)!H_j^{(s-1)},
\]
\[
V_j=C_jU_j+(s-1)![c-aH_j^{(s-1)}-bH_j^{(s)}].
\]
此 rational form可对任意整数 a,b,c定义；只有其 actual analytic identity使用候选关系。Normalized determinant的 factorial除数不改变非零性。正文没有混淆 unconditional rational nonzero lemma与 conditional numeric relation。

## J6. H9 all-scale auxiliary-prime blocks 与全部误差

取 n=2m，p=9m+1 prime且 p>max(s,|b|)。Hermite nodes 0..3m−1的 differences绝对值<p，故 \(F_k,c_k\in\mathbf Z_p\)。P_k,Q_k在这些 nodes的 values/derivatives按正文给 exact basis；deg<6m恰 match h=6m空间。

j<p：H_j⁽ᵛ⁾∈Z_p，C_j最多 p⁻¹，U_j∈Z_p、V_j∈p⁻¹Z_p。各 basis polynomial与导数在 pZ_p[t]，product derivative≥p²，故 local form≥p；乘 pˢ⁻⁴仍≥p。W_j整数足够，此处无需假设 unit。

剩余 j=p+l，0≤l<3m：各 relevant upper limits<2p，H_j、H_{4m+j}恰有一个 p-term，H_{12m-j}没有，故
\[
H_j^{(v)}=p^{-v}+O(\mathbf Z_p),\quad
C_j=2p^{-1}+O(\mathbf Z_p).
\]
Lucas给 W_j unit：digits reduction分别是
\(\binom{3m-1}{l}\)、\(\binom{4m+l}{l}\)，其 factorials均<p。
令 \(u=(s-2)!b\) 为 p-unit，独算得
\[
U_j=-up^{-(s-1)}+O(p^{-(s-2)}),\quad
V_j=-(s+1)up^{-s}+O(p^{-(s-1)}).
\]
第二式的 s+1来自 C_jU_j的 −2u与 double-pole的 −(s−1)u，不能误写 s−1。

在 −l−p Taylor展开，对 diagonal l=k，
P=p²+O(p⁴)、P′=O(p³)、Q=−p²+O(p³)、Q′=p+O(p²)；
off-node有 P=O(p⁴)、P′=O(p³)、Q=O(p³)、Q′=O(p²)。
Consequently diagonal product values PP/PQ/QQ是 p⁴/−p⁴/p⁴，
derivatives是 O(p⁵)/p³/−2p³。整个 form乘 **pˢ⁻⁴**，而非只缩某些 rows，mod p留下
\[
uW_{p+l}
\begin{pmatrix}-(s+1)&s\\s&-(s-1)\end{pmatrix}.
\]
三个 leading entries独算吻合：PP=−(s+1)u；PQ=(s+1)u−u=su；QQ=−(s+1)u+2u=−(s−1)u。

所有 errors至少一 p：V error乘 leading product p⁴再乘 pˢ⁻⁴为 p；U error乘 p³为 p；Taylor derivative/value errors分别至少多 p；off-diagonal blocks的 product≥p⁵、product derivative≥p⁴也至少多 p。各 j<p的前述 p-bound同样保持。故 scaled matrix整体在 Z_p且 reduction确是 block diagonal，不能只看几个 leading blocks忽略 off-block贡献。

Blockdet为 \(u^2W^2[(s+1)(s-1)-s^2]=-u^2W^2\) unit。即便 p=s+1使一 entry零，det仍 unit，不需额外排除此情形。Scaled form、basis change和 factorial normalization都是 nonzero rational factors，因此 actual rational determinant≠0。Dirichlet对 residue1mod9给无穷适合 primes，得到每个 fixed s≥4的无限非零 n。

s=4 precise还原 Lai \(2bW[[-5,4],[4,-3]]\)；一般 s的 proof已逐项完成，不是有限 s=5/7数值猜测。本独审认可它为本文完整内部推广lemma。其发表新颖性未专项调查，不能宣称已经是文献中首次命题。

## J7. 独审结论与剩余工作

最终稿 H1–H9在列明范围内通过独审：exact rational moments、odd ζ/character target identity、target polynomial、positive-envelope transfer、条件整数判据与 H9 fixed-weight auxiliary-prime nonzero subsequence均有完整纸面支持。

H9确实填补 **double-pole布局** 的非零子序列缺口；没有填 simple-pole多项式的 nonvanishing。两种布局/normalizations须分开。尚缺 new weight的严格全素数 denominator/content费用及 matching analytic decay；Lai weight4的30.83和 Tang weight3的283/50不自动转移。角色 family另缺 multi-contour energy。ζ(5)−rζ(4)等目标是否已有完整公开结果仍需下一轮专项 novelty审查。

因此本轮有正面方法进展，尚没有新的特殊值无理性、线性无关性、超越性或 Lean定理。Root将本独审及 H9归入主报告/audit；本人未修改 main/delivery或旧冻结文件。

冻结前最终回读仅修本文 J3 换行公式漏写的一个加号，恢复正文已证明的 harmonic-tail identity；root e6主稿未变。本文实际全文回读、SHA记录后冻结只读。
