# 一次多项式 slow source 的固定 minor 与全好素数核分类

日期：2026-10-06。本文新增，旧 producer 与报告保持冻结。本次只选一个预定 minor：ORDER12，行次数1,…,12，列 Ξ₀,…,Ξ₅,sΞ₀,…,sΞ₅。作者单次执行新的独立 literal eta/E/F 程序，32 项检查通过；未扫描素数、未尝试另一个 minor。所得行列式非零，给固定 polynomial degree K=1 的全好素数分类，仍未证明 K 随 p/D 增长的统一结论，未得到新的净 Smith 收益。

## 1. 实际函数与独立计算规范

沿用 [完整 Af packet](cdt_odd_level20_cartier_packet_matrix_20261006.md) 的两 target 符号及 [实际 cohomology](cdt_odd_level20_cartier_cohomology_20261006.md)。令 r²=5，先取原减号

\[
 A=E_2-4rF_2(4\tau),\quad
 V=E_4-5E_4(2\tau)+4E_4(4\tau)
 -\frac{5r}{4}(F_4-20F_4(2\tau)+64F_4(4\tau)),
\]
\[
 f(q)=\sum_{n\ge1}V_nq^n/n^3,\quad
 N=1-(6+r)t+(1+r)t^2,
\]
\[
 C=1-(6-2r)t+(6-2r)t^2,\quad D_-=(1-t)NC,
 \quad \Xi_j(t)=\int_0^t\frac{v^jA(v)f(v)}{D_-(v)}\frac{dv}{v}.
\tag{K1}
\]

C 是 A 的 own-zero 因子。完整 F=Af 的 carrier 未删去；Ξ 仅以原点实际芽及其 slow prefix 使用，没有将它们加入此前共同 G 解析叶。

新 [producer](cdt_odd_level20_cartier_poly_k1_20261006_verify.py) 不 import 或执行任何旧 producer。E/F 由 χ₅ 除数和直接实现；E₂,0=−1/5，E₄,0=1，全部 F 的 constant0。坐标

\[
 t=q\prod_{d,n}(1-q^{dn})^{e_d},\quad
 e_{1,2,4,5,10,20}=(3,-4,1,1,-4,3)
\]

由 Euler 对数导数递推得到，q(t) 则逐次数解 t(q(t))=t。程序检查双向递归及整数性，没有调用冻结坐标实现。最后直接使用

\[
 [t^n]\Xi_j=\frac1n[t^{n-j}]\frac{A(t)f(t)}{D_-(t)}.
\tag{K2}
\]

加号的全部实际代数 coefficients 是 K1 的共轭；程序同时重建并核共轭，不对未知周期规定一个虚构的 Galois 作用。

## 2. 唯一预选 12×12 minor

在慢坐标 s 中，以列顺序 Ξ₀,…,Ξ₅,sΞ₀,…,sΞ₅、行次数1,…,12记矩阵 J₁。其完整矩阵在新 [JSON](cdt_odd_level20_cartier_poly_k1_20261006_verify.json) 中保存。32 项固定检查给

\[
 \det J_1=a+br\ne0,
\]
\[
 a=\frac{-908963683580282309352933681705860257750121096629075060860357040532809671767793220041521}
 {520978141993282621418840335133125937610855556426235904000000000000000000000000000000000000},
\]
\[
 b=\frac{169231146019924203017082105974580800496949968025241036756957989663850187164791468283249}
 {217074225830534425591183472972135807337856481844264960000000000000000000000000000000000000}.
\tag{K3}
\]

其约分范数分子为非零正整数

\[
 \mathfrak n_1=
 7032857555943229119723855226797964278295394523145231546248076430814412114452497632600769462601857269244872628739080098785582353449983863386815194049138617738621706484543061.
\tag{K4}
\]

所有矩阵条目分母的素因子均≤12：E/F 固定规范只引入2、5，eta 双向坐标及 D⁻¹ 整数，而 f 与积分只用1≤n≤12。程序亦逐条验证分母仅含2、3、5、7、11。故任意 p>12、p∤𝔫₁，在 K 的每个 p-place，J₁ 都是 unit matrix；加号的共轭 minor 有同一个 norm 排除集。无需对 𝔫₁ 完全因式分解才给出一个明确有限坏集合。

因此对于这些 p，保留至少前12个 positive slow coefficients 时，十二个列 Ξᵢ,sΞᵢ 在剩余域 k 中线性独立。这是固定次数的新结论，不是从有限素数测试猜测所有 p。

## 3. 原多项式 source 的全好素数第一层分类

使用 [精确多项式 Cartier 接口](cdt_odd_level20_cartier_p13_polynomial_20261006.md) 的最高 packet。其共同规范为 Ψ=p⁴eval，六积分 species 的 residue 为

\[
 \bar\Psi(I_j)=g(t)\sum_i\bar M_{p,ij}\bar\Xi_i(t^p)
 \pmod{t^N},\quad g(0)=1.
\tag{K5}
\]

该身份仅在 N≤p² 的实际 prefix 范围内使用，relative k-linear Cartier 规范及完整 carrier 均保留。

假设

\[
 p>12,\quad p\nmid\mathfrak n_1,\qquad
 p\le D\le2p-1,\qquad 13p\le N\le p^2,
\tag{K6}
\]

并保留源 packet 的固定好约化及周期分母条件。对次数≤D的六个 coefficient polys 唯一分解

\[
 c_j(t)=\sum_{a=0}^{p-1}t^aC_{j,a}(s),\quad s=t^p,
 \quad K_a=\left\lfloor\frac{D-a}{p}\right\rfloor\in\{0,1\}.
\tag{K7}
\]

每个 a 的慢 prefix 行数

\[
 M_a=\left\lfloor\frac{N-1-a}{p}\right\rfloor\ge12
\tag{K8}
\]

由 N≥13p 及 a≤p−1保证。K=1 时 K3 给全部12列独立；K=0时取这同一 unit matrix 的前六列，仍独立。故每一个块 H(Kₐ,Mₐ) 都 injective。指数剩余类直接和于是给出准确等价

\[
 \bar\Psi\Bigl(\sum_jc_j(t)I_j\Bigr)=0\pmod{t^N}
 \quad\Longleftrightarrow\quad
 \bar M_p\,(c_0(t),\ldots,c_5(t))^T=0
 \quad\text{逐多项式 coefficient 成立}.
\tag{K9}
\]

因此在原六积分 polynomial residue source 中

\[
 \boxed{\ker\bar\Psi_I
 =k[t]_{\le D}\otimes_k\ker\bar M_p,
 \qquad\dim_k\ker\bar\Psi_I=(D+1)\dim_k\ker\bar M_p.}
\tag{K10}
\]

特别地，若 Mp 为 unit，degree≤D 的六积分块没有 S1 kernel。若 Mp 非 unit，全部这些方向都来自已有 constant Hecke kernel 的 monomial shifts；在本窗口没有额外的 polynomial slow syzygy 信用。

原 rank19 系统若选 full leading prefix N≥19(D+1)+C，还须同时满足 K6。K10 不取消该 leading-order 条件。例如 p=13、D≥p 时 19(D+1)>p²，所以 [固定 p=13 的 ordinary 证据](cdt_odd_level20_cartier_p13_polynomial_20261006.md) 本身不落入这一原 rank19 多项式窗口，不能冒充此窗口的实验。

## 4. 第一层及未完成边界

K10 是六积分最高 residue 的完整 S1 分类。其余13个 species 在共同 p⁴ 规范下已有第一层 floor；将它们加入完整 source 后仍须将 raw kernel、row baseline、leading minor 和净 determinant 分开记账。K10 没有产生新的净 γ，也没有由 Mp 的 p-adic valuation 自动推出 S2/S3。

这里新证明的是固定 K=1 的全部好素数、完整 chosen prefix 结论，允许 Mp 普通或非普通。它没有假设非普通密度，也没有证明 K≥2、K随p增长时 H(K,M) 的统一零估计。更高次数若有真实短 slow syzygy，仍可能给新的第一层输入，须在同一原格验证。

## 5. 执行与独立审阅范围

作者新 producer 单次执行32项检查：整数 Euler recursion、双向坐标、实际 E/F 与 primitive derivative、两 embedding 共轭、唯一固定 minor/norm、条目分母支持。未试其它 prefix/minor/prime；未运行或 import 冻结 producer。完整 12×12 matrix、K3 两分量和 norm 在 JSON 保存。

K6–K10 是以非零固定 minor 和冻结 packet 为输入的全尺度数学证明，不由32项检查单独替代。conjugate_projection已实际只读 §§2–3，限定审核通过：K6保证 Kₐ∈{0,1}、Mₐ≥12，g(0)=1的取消、剩余类直接和与 K9/K10 的完整 native kernel 分类成立；其审阅条件于新 K3 minor 和冻结 K5 packet，未执行 producer、重算巨大行列式或重复证明 packet。

root亦已实际只读全文及新 producer，限定审核通过：实际数学输入、literal eta/E/F构造、逐系数 reversion、完整 Af积分及固定 minor规范、K6–K10 的剩余类分块和准确 kernel 分类。root未运行 producer，未把单个固定 K minor 推成统一变动 K 零估计，亦未认领新的净 Smith 收益。本次追加实际审阅范围后冻结 MD/PY/JSON，不再运行 producer。
