# Fixed fan R0 模型的全奇素数 smooth proper / relative SNC 几何

日期：2026-10-06。NEW 全尺度纸面证明。旧数学 MD/PY/JSON/manifest 与同行 producer 全部冻结只读，未执行或 import。本文将已固定 characteristic-zero fan 的具体 monomial construction 放到 \(\mathbf Z[1/2]\) 上，并逐 stratum 核 smoothness；不从 characteristic-zero 光滑性推断好约化。

## S1. 对象、正结论和未删的条件

令
\[
R=\mathbf Z[1/2],\quad
U_R=\mathbf P^1_R\setminus\{0,\infty,-1\},\quad
S=\operatorname{Spec}R[\lambda,\lambda^{-1},(\lambda-256)^{-1}],
\]
\[
\phi=\prod_{j=0}^3(1+v_j)^2/v_j,\qquad P_R=(\mathbf P^1_R)^4 .
\]
使用冻结 `cdt_odd_R0_toric_completion_20261006.md` §3 已固定的同一个 finite coherent regular subdivision：原 lattice 不变，先沿 \(\ell=0\) 切 cone，再作相容 projective regular refinement。以下不重新运行 fan producer，不换 ramified lattice，也不调用在某个有限数据集上找到的 fan。

**几何定理。** 这个 fan construction 定义于 \(R\)，产生 projective smooth \(R\)-scheme \(\widetilde P_R\) 以及 morphism \(f:\widetilde P_R\to\mathbf P^1_R\)。令
\[
\mathcal X=f^{-1}(S),\qquad
\mathcal E=\mathcal X\setminus (U_R^4\times_{\mathbf G_{m,R}}S).
\]
则 \(\mathcal X\to S\) projective smooth、relative dimension3、geometrically connected；\(\mathcal E\) 是 split relative SNC。这涵盖每个奇素数（包括3）、每个满足 \(\lambda\ne0,256\) 的几何点及所有 boundary corners，不只 generic fibre 或有限个 primes。

**尚未证明的接口。** 本定理不证明相应全部 \(R^i f_*\Omega^\bullet_{\mathcal X/S}\) 在所有奇素数上 locally free/base-change，不提供 \(p=3\) 的 crystalline torsion 检验，也不直接证明四维 PF 在全部奇素数的 generic radius1。因此 root 的有效分母稿 D14 保持其明确第四条件；不在本稿宣布 \(C=16\)。

## S2. 全 grid 在整数基底上的 split charts

十二个 divisors \(v_j=0,\infty,-1\) 在每个 \(\mathbf P^1_R\) 上两两不交；其 product grid 是相对 \(R\) 的 split SNC。每个 fixed grid stratum
\[
T_A=U_R^{4-s}
\]
固定了 \(s\le4\) 个不同因素，每个 fixed coordinate 有全局 normal parameter
\[
z_i=v_i,\quad z_i=v_i^{-1},\quad z_i=v_i+1
\]
分别用于 \(0,\infty,-1\)。完整 Zariski 邻域是 \(\mathbf A^s_R\times U_R^{4-s}\) 的 open subset：前两类删 \(z_i=-1\)，后一类删 \(z_i=1\)。normal lines 由同一 parameter trivialize over \(T_A\)，没有 arithmetic torus twisting。

精确整数公式为
\[
\phi=c(z,v_{\rm free})\prod z_i^{e_i},\qquad
e_i=-1\ (0,\infty),\quad e_i=2\ (-1),
\tag{S2.1}
\]
其中 c 为上述邻域的单位；在 stratum 上
\[
c_A=(-1)^p\prod_{\rm free}(1+v_j)^2/v_j\in\mathcal O(T_A)^\times,
\quad p=\#\{\text{fixed }-1\}.
\tag{S2.2}
\]
这些 identity 在 \(R\) 上逐项成立，不只有 complex analytic validity。

## S3. Fixed regular fan construction 本身是整数的

在每个 original \(s\)-cone \(N_A=\mathbf Z^s\)、\(\sigma_A=\mathbf R_{\ge0}^s\) 上，map 的 character 为
\[
\ell_A(n)=\sum e_i n_i.
\]
normalized graph 所用 monomial ideal为 \((z^{e_+},z^{e_-})\)。在 (S2.1) 中乘 invertible generators 不改变这个 ideal。其 coherent fan 由 \(\max(0,\ell_A)\) 给出，和原稿一致。

现在直接用已选 fan 的 toric scheme charts
\[
\operatorname{Spec}R[\tau^\vee\cap M_A]
\]
作 monomial modifications，和 \(T_A\) 取 product 并限制 S2 的 open。相容 face/localization 给 glue；原 grid normal coordinates 与 monomial ideal 在 overlap 相差 units，故就是同一个 global toroidal modification。这里用的是 explicit fan/monoid scheme construction，未假定“任意 characteristic-zero resolution 会 spread 到全奇素数”。

regular cone 的 primitive rays 是原 lattice 某个整数基底的一部分。所以其 toric charts 为 \(\mathbf A^r_R\times\mathbf G_{m,R}^{s-r}\)，均 smooth over R；normal boundary 坐标形成相对 SNC。整个 finite coherent fan 的 projective monomial modification 定义于 R，glue 保留 projectivity。每 cone 仍在原 \(\ell\) 的一个 closed half-space，\(\phi\) 或 \(\phi^{-1}\) 成为 regular monomial times unit，于是 map f 在全部 chart 上无 indeterminacy。

\(\widetilde P_R\) projective over R，graph f 在 \(\widetilde P_R\times_R\mathbf P^1_R\) 中为 closed immersion，故 f projective。局部扇形平滑性的证明与 prime 无关；coherence/projectivity 是固定 integral fan 的组合性质。

## S4. 所有 surviving cones 与完整 orbit products

非零 refined cone \(\tau\) 的 original minimum support 为 s 个 fixed factors，dim\(\tau=r>0\)。它在 \(f^{-1}(\mathbf G_m)\) 中 surviving 当且仅当 \(\ell_A|_\tau=0\)。若一条 ray 的 order 正/负，则对应 divisor 映入0/∞，相应 orbit 不可能 surviving。

相对内部中有一个原 support 的全部 s 个坐标都正的 vector。若全部 \(e_i\) 同号，不能满足 \(\ell_A=0\)。所以 surviving support 同时含一个 \(-1\) coefficient 和一个 \(+2\) coefficient；对应至少一个 \(0/\infty\) fixed point和一个 \(-1\) fixed point。且
\[
2\le s\le4,\qquad 1\le r\le s-1\le3.
\tag{S4.1}
\]
regularity 使 \(N_\tau\) saturated，quotient \(N_A/N_\tau\) free。整个 orbit product 为
\[
D_{A,\tau}^{\circ}=U_R^{4-s}\times\mathbf G_{m,R}^{s-r}.
\tag{S4.2}
\]
它全局成立：minimum support 条件使每个 original normal monomial z_i 在该 orbit 上为0，因此 S2 删去的 \(z_i=\pm1\) 没删任何 orbit 点；该完整 orbit 已被单个 global product chart 覆盖。无需 étale split 后再忽略扭转。

在此 orbit 上
\[
f=c_A\chi_{\ell_A}.
\tag{S4.3}
\]
由于 original 某个 coordinate vector 的 \(\ell_A\) value 为 \(-1\)，它在 quotient 上给 \(-1\)，故 quotient character仍 primitive。选 \(GL_{s-r}(\mathbf Z)\) 基变换，再将一条 torus coordinate乘 \(c_A\)，得到整数 scheme identity
\[
D_{A,\tau}^{\circ}
\simeq U_R^{4-s}\times\mathbf G_{m,R}^{s-r-1}
\times\mathbf G_{m,R,\lambda},
\tag{S4.4}
\]
且 f 为最后一因子 projection。整数 determinant ±1 不会在 p3 或其它 odd prime 引入 inseparability。式 (S4.4) 是全部 cones 的证明，未只核最简单 \((1,2)\) ray。

## S5. Boundary 全角点的相对 Jacobian

S4 已给每个 boundary orbit 的 f 为 smooth projection。更明确，在 orbit 上取 primitive torus coordinate q，使 \(\lambda=c_Aq\)，则
\[
\partial f/\partial q=c_A
\]
为单位，over每个几何 residue field 仍为单位。邻近 chart 上 c 可依 normal monomials，但限制 orbit 的 derivative 仍是 c_A；故该 Jacobian minor 在该 point 邻域为单位。

Ambient \(\widetilde P_R\) 已 smooth over R，target \(\mathbf G_{m,R}\) 也 smooth。沿 orbit tangent 的 surjective relative differential 给 f smooth at该point；或直接用上述 Jacobian minor 与 normal coordinates 组成 relative étale chart。对 r 个交叉 boundary components，其 normal parameters \(u_1,\ldots,u_r\) 和 q 的 Jacobian block仍 invertible。因此 f 相对光滑，且 \(\{u_1\cdots u_r=0\}\) 为 relative SNC。此 argument 包括 r2/r3 corners，finite fan 覆盖所有 boundary points；没有额外不可见的 vertical arithmetic component，因为全部 charts over R 明确为 smooth toric products。

这也表明每个 boundary stratum 的 fibre dimension为 \(3-r\le2\)。boundary 无 relative-codimension4 surviving stratum。

## S6. Interior 在每个奇 residue characteristic 的临界点

在 \(U_R^4\) 上，\(\phi\) 为 unit，精确 identity
\[
\partial_{v_j}\log\phi=\frac{v_j-1}{v_j(1+v_j)}
\tag{S6.1}
\]
在 R 上成立。对任意 geometric point，分母为单位；所有 derivatives 同时为0，恰当且仅当所有 \(v_j=1\)。其 value为 \(\lambda=4^4=256\)。在 odd characteristic 中 \(1\ne-1\)，故这些是 interior 点，已由 S 的 localization 删除。

于是所有几何 points above S 有一个 invertible Jacobian minor，f 在 interior smooth。结合 S5，\(\mathcal X\to S\) smooth everywhere，relative dimension3。256 在每个 odd residue field是非零，base 的两个删点确为0与256；并非把两点意外合并后使用 characteristic-zero PF。

## S7. Geometric connectedness 的直接代数证明

为未来 Katz interface 核其另一明示条件。取任意 S 的 geometric point，residue field k algebraically closed、char k为0或odd，\(\lambda\in k^\times\)。在 \((v_0,v_1,v_2)\in U_k^3\) 上置
\[
\Phi=\prod_{j=0}^2(1+v_j)^2/v_j,\qquad A=\lambda/\Phi.
\]
interior fibre 恰为 monic quadratic cover
\[
v_3^2+(2-A)v_3+1=0,
\quad\operatorname{disc}=A(A-4)=\lambda(\lambda-4\Phi)/\Phi^2 .
\tag{S7.1}
\]
v3 与 v3+1 在 quotient ring中都为单位：constant term1，且代入−1的值为 A单位。故这就是整个 \(U_k^4\) 的 interior fibre。

\(\lambda-4\Phi\) 有 multiplicity-one divisor。实际可取 \(v_1,v_2\) 使其 product值 C 满足 \(\lambda/(4C)\ne4\)；k无限，每个 \((1+v)^2/v\) 在 U_k上取遍 k的非零值，故这样的 C 存在。取 v0满足 \((1+v_0)^2/v_0=\lambda/(4C)\)。它不是1，且 S6 的 derivative在该点非零；于是该 divisor有一个 smooth point，对应某 prime divisor的 order1。S7.1 的 discriminant在其上奇 order，不能是 k(U³) 中的平方。char k≠2，quadratic不可约。因此 interior fibre是几何 integral 三维 variety。

proper smooth fibre的每个 irreducible component都是三维。S5 的全部 boundary strata dimension至多2，finite union不能包含某个三维 component。所以每个 component都遇到 interior；interior irreducible迫只有一个 component。smoothness给 reduced；故 proper fibre geometrically integral，尤其 connected。这里没有用 complex connectedness 自动推出 mod p connectedness。

## S8. 真正得到的 all-odd 幾何输入

S2–S7给：
\[
\mathcal X/S\text{ projective smooth with geometrically connected fibres},\qquad
\mathcal E/S\text{ split relative SNC}
\tag{S8.1}
\]
for all odd primes，包含p3。λ=256x是R上的单位坐标scale；\(\sqrt x\) 的 cover在 \(x\ne0\) 的该基底上 finite étale，因为2 invertible。此 cover 不改变 proper smoothness。

不过本稿只构造 fibrewise/relative model与boundary几何，不把 rational \(\Xi\) 的原 Q-family completion自动延拓为整 arithmetic higher-Chow class，不默认 degree-one mirror maps 的整好约化，也不把 B2 的 complex Betti unimodularity当 p-adic de Rham local freeness。

## S9. Katz primary 的实际条件与 precise remainder

本轮实际读 newly archived Katz primary
`literature/katz1972_travaux_de_dwork_author_20261006.pdf`，PDF23–24，§7：
proper smooth、geometrically connected，以及 **de Rham cohomology locally free**，共同给 Gauss–Manin 为 F-crystal 的 underlying equation。作者括注 locally free 是为了避 derived categories，并不等于此初等版本没有该条件。后一段的 \(p>i\) 属于额外 projective/Hodge locally-free 的 Mazur divisibility；它不是“p3时不存在 geometric F-crystal”的断言。

因此 S8 确实完成 §7 的 geometric smooth/proper/connected hypotheses，尚缺具体 \(\mathcal X/S\) 的 required de Rham local-freeness/base-change、或者一个已实际核准且允许此 rational derived 情形的 general convergent Gauss–Manin theorem。若后者完成，还须识别 actual four-dimensional cyclic subquotient、algebraic \(\sqrt x\) twist与 root 四维 regular-singular G 的 p-adic realization，才能将 convergence传给该系统。

本稿未宣称缺口只能是p3；当前对 **所有** odd primes 的 local-freeness均未给全尺度证明。p3没有被从 theorem范围偷偷删掉，也没有靠 Hodge degeneration 的大素数界覆盖。root D13–D14 的第四条件仍保留。研究可继续检查 rational crystalline/convergent direct image 或用实际 model的 Hodge/de Rham计算，而非把“smooth proper”三个词替代上述接口。

## S10. 来源、冻结状态与执行

本轮实际全文重新读 frozen toric completion稿，SHA256
\[
\texttt{abbb47907e85e2ae15c12bfaa6655f8f25497e804e299e15bd9277e7a6a667b0}.
\]
重读 §§2–4 的 global parameters、fixed lattice fan、whole orbit products，以及其余全文，未运行 producer。S2–S8是本轮 NEW integral argument；不改旧稿只证 Q 的历史范围。

Katz primary SHA256
\(\texttt{b885d13a652d87763c5864eb22238f0695613a3dab774507e2ba570a487eca1a}\)，35PDF页；本轮实际全文页读23–24。原件URL为
[author archive](https://web.math.princeton.edu/~nmk/old/travdwork.pdf)。
该原件由 root 本轮 verified TLS归档，本人没有重复下载、没有 insecure flag。阅读只用 fitz抽取原件页和元数据；不存在数学代码执行。

尚未提供 C16、目标无理性/线性无关性或 Lean；本稿给 all-scale 整几何正结论和其与 generic radius之间的确切剩余条件。

