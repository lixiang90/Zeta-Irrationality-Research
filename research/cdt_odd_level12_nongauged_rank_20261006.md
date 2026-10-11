# D12 去掉 modular gauge 的实际 primitive 不具有限 holonomic 秩

日期：2026-10-06。独立新纯 MD 证明。严格使用已经 actual 全文独审并冻结的 [affine/PV 主稿](cdt_odd_level12_affine_galois_20261006.md) (A13)，不修改冻结文件，不执行/import任何 producer，不扫描参数或素数。本文证明两个固定实际源的 nongauged primitive 不满足任何有限阶 \(\mathbf C(v)\)-线性 ODE；不是新的数值无理性结果，也不是对所有源或新 bundle 定理的否定。

## 1. 实际函数与明确的 PV 输入

令 \(v\) 为实际 \(\Gamma=\ker\chi_{12}\) Hauptmodul，\(k=\mathbf C(v)\)、\(\partial=d/dv\)。令

\[
\mathcal B=E_2(\tau)-12E_2(12\tau),\qquad
h_Z=f_Z-103680\zeta(3),\qquad
h_L=f_{\sigma,L}+34560\sqrt3L(3,\chi_{12}),
\]
\[
H_j=\mathcal B h_j,\qquad
u_j=(H_j,\partial H_j,\partial^2H_j)^t\quad(j=Z,L).
\tag{N1}
\]

这里 \(f_{\sigma,L}\) 是共轭 source 的真实 Taylor primitive。所有数值常数均属于常数域 \(\mathbf C\)，不假设 \(\zeta(3)\) 或 \(L(3,\chi_{12})\) 是代数数。

共同齐次 Bol 方程的实际三列是

\[
y_0=\mathcal B,\qquad y_1=\mathcal B\tau,
\qquad y_2=12\mathcal B\tau^2,
\qquad Y=(\partial^iy_j)_{0\le i,j\le2}.
\tag{N2}
\]

冻结主稿已经证明 \(Y\) 可逆，实际七维强迫系统 regular singular，且其共同 PV 场 \(L\) 满足

\[
\boxed{\operatorname{Gal}(L/k)=\mathbf G_a^6\rtimes PSL_2(\mathbf C).}
\tag{N3}
\]

在这个具体 fundamental matrix 的标准右 block action 中，每个 automorphism 的实际作用是

\[
\sigma Y=Yg,\qquad
\sigma u_Z=u_Z+Y a_Z,\qquad
\sigma u_L=u_L+Y a_L,
\tag{N4}
\]

其中 \(g\) 属于 normalized Sym² image，\(a_Z,a_L\in\mathbf C^3\)，且 (N3) 保证所有这些 pairs 都出现。本文使用的是 (N4) 中以实际 particular columns \(u_Z,u_L\) 为基准的完整群，不以一个尚未实现的 formal affine representation 替代它。

本地冻结输入的 SHA256 为

`a74ca9ef73f3c4967e97c928ea37f9d1a599ea2dc68d959bdac24d5b042dad11`。

## 2. 一条明确的无限 Galois orbit

对任意 \(a\in\mathbf C\)，取

\[
\gamma_a=\begin{pmatrix}0&-1\\1&-a\end{pmatrix}\in SL_2(\mathbf C),
\qquad g_a=\operatorname{Sym}^2(\gamma_a)
\]

其中 Sym² 使用 (N2) 的正规化。根据 (N3)，存在实际 differential automorphism \(\sigma_a\)，其参数为 \((g_a,0,0)\)。因此

\[
\sigma_a H_Z=H_Z,\qquad \sigma_a H_L=H_L.
\tag{N5}
\]

\(g_a\) 的第一列为 \((a^2,-2a,1/12)^t\)，故

\[
\sigma_a\mathcal B
=a^2\mathcal B-2a\mathcal B\tau+\mathcal B\tau^2
=\mathcal B(\tau-a)^2.
\tag{N6}
\]

这里用的是 homogeneous PV group 的常数矩阵作用，不声称 \(\gamma_a\) 本身属于 discrete \(\Gamma\)，也不声称 \(\sigma_a\) 就是某个特定的实际短 word。完整 monodromy 的 Zariski 密性正是保证这个 PV 群元素存在的已证输入。

因为 \(h_j=H_j/\mathcal B\)，(N5)/(N6) 精确给

\[
\boxed{\sigma_a h_j=\frac{h_j}{(\tau-a)^2}.}
\tag{N7}
\]

\(h_j\ne0\)：其 \(\theta_q^3 h_j\) 是相应非零实际 source。具体 \(q^1\) coefficients 分别是 \(362880\) 和 \(294960+69120\sqrt3\)，均非零。另 \(\tau\in L\) 由 \(y_1/y_0\) 给出，它是非 constant 的实际 inverse uniformizer；特别它在 \(\mathbf C\) 上超越，因为任一非零 constant-coefficient polynomial 不可能在一个非 constant holomorphic function 的开像上恒为零。

取任意有限个 distinct \(a_1,\ldots,a_s\)。若

\[
\sum_{i=1}^s c_i\sigma_{a_i}h_j=0,\qquad c_i\in\mathbf C,
\]

除以非零 \(h_j\)，便有 \(\sum_i c_i/(\tau-a_i)^2=0\)。\(\tau\) 在 \(\mathbf C\) 上超越，使这成为 \(\mathbf C(X)\) 中的 rational identity；在每个 \(X=a_i\) 的 double pole 上比较系数，得到全部 \(c_i=0\)。因此

\[
\boxed{\{\sigma_n h_j:n\in\mathbf Z\}
\text{在 }\mathbf C\text{ 上线性无关}.}
\tag{N8}
\]

只需这个预定 infinite family 的全尺度公式；没有短 word、参数或素数搜索。

## 3. 有限阶线性 ODE 与 (N8) 矛盾

假设存在非零 \(P=\sum_{i=0}^r p_i(v)\partial^i\in k[\partial]\)，使 \(P(h_j)=0\)。\(r=0\) 会迫 \(h_j=0\)，已经排除，所以 \(r\ge1\)。每个 differential automorphism \(\sigma\in\operatorname{Gal}(L/k)\) 固定 \(k\)、与 \(\partial\) 交换，故

\[
P(\sigma h_j)=\sigma(P(h_j))=0.
\tag{N9}
\]

取一个实际 ordinary base point，避开 \(P\) 的 coefficient poles 与 leading-coefficient zeros，也避开 \(\mathcal B\) 的零。其 inverse \(\tau\) 可取在上半平面；所以对于所有整数 \(n\)，\(\tau-n\ne0\)，(N7) 都是该点的 holomorphic germs。阶数 \(r\) 的 scalar ODE 在 ordinary point 的解空间至多为 \(r\) 维，因解由首 \(r\) 个 initial derivatives 唯一决定。这个空间不可能包含 (N8) 的无限线性无关 germs。矛盾。

于是得到无条件的 functional 结论

\[
\boxed{h_Z,h_L\text{ 均非 D-finite over }\mathbf C(v).}
\tag{N10}
\]

等价地，\(\operatorname{Span}_{\mathbf C(v)}\{\partial^n h_j:n\ge0\}\) 具有无限维数。这里的“无限秩”指无限 derivative closure，不是说任意一个有限列出的 function tuple 本身会有无限维数。

## 4. 未平移 primitive 及实际 Taylor 坐标

若 \(f_j=h_j+c_j\)，\(c_j\in\mathbf C\) 是相应实际数值常数，那么 \(f_j\) 同样非 D-finite。确实，若 \(f_j\) 满足有限阶 \(k\)-ODE，其 automorphism orbit 落在一个有限维 \(\mathbf C\)-solution space；而 \(\sigma h_j=\sigma f_j-c_j\) 落在该空间加上 constant line 中，仍有限维，与 (N8) 矛盾。故

\[
\boxed{f_Z,f_{\sigma,L}\text{ 均非 D-finite over }\mathbf C(v).}
\tag{N11}
\]

同一结论适用于实际 \(t_\pm\) 坐标：\(t_\pm\) 是 \(v\) 的非 constant rational functions。任何有限阶 \(\mathbf C(t_\pm)\)-ODE 经 \(t=t_\pm(v)\) 与 chain rule 拉回都会给非零有限阶 \(\mathbf C(v)\)-ODE，contradicting (N10)/(N11)。

更换有限代数 base cover也不能把这些函数变成 D-finite：若它在一个 finite algebraic differential extension 上有 finite-dimensional derivative closure，restriction of scalars 仍给基域上的 finite-dimensional derivative-stable space。本文不涉及独立的非代数 base change。

## 5. 便宜 q 分母为何不能直接作为 rank4 scalar 包

literal \(q\)-系数确有

\[
f_j=\sum_{n\ge1}\frac{(F_j)_n}{n^3}q^n,
\quad\theta_q f_j=\sum_{n\ge1}\frac{(F_j)_n}{n^2}q^n,
\quad\theta_q^2f_j=\sum_{n\ge1}\frac{(F_j)_n}{n}q^n.
\tag{N12}
\]

它们的算术 denominator facts 与 (N10) 不冲突。问题是去掉 \(\mathcal B\) 后，实际 primitive 不再属于一个有限阶 \(\mathbf C(v)\)-holonomic closure；\(\theta_q\) 也不是一个以 \(\mathbf C(v)\) 系数直接写出的普通 derivative，它含非 rational 的 modular factor。不能把 (N12) 自动当作旧 scalar rank4 系统的三个廉价行，同时保留旧 rank、旧解析叶与旧 CDT 成本。

CDT 的一般 holonomy 定理并非总要求事先 holonomic：足够大的合法 map 与 arithmetic bounds 可以反过来强迫 holonomicity。本稿因此不是禁止把这些 germs 放进任何有限数组；它排除的是“它们已经具有旧 rank4 derivative closure”的替换，以及直接使用那个 prior-holonomic shortcut。若想应用无 prior-holonomicity 版本，仍需重新满足其真实 scalar meromorphic pullback 与足够大的 derivative 假设。

例如 gauge-free \(h_j\) 在 \(\Gamma\) 上的真实关系是

\[
h_j(\gamma\tau)=(c\tau+d)^{-2}
  \{h_j(\tau)+c_j(\gamma)(\tau)\},
\]

而非带 gauge 的 \(H_j\) 的 scalar period transformation。把它当成某个 line-bundle section 可保留 automorphy，却尚不等价于 CDT 的 scalar evaluation (7.3.8)。任何真正的 bundle 版本都应重新证明 source/graded ranks、整格、Hermitian degree 和评价高度；本稿不排除这种另证定理。

## 6. 审阅与非结论

本稿是纯 MD 全尺度证明。作者只读实际冻结 affine_galois 全文及其 primary PV 接口，不运行任何 producer，不把 functional independence/非 holonomicity 变成特殊值独立，不宣称 \(\zeta(3)\) 或 \(L(3,\chi_{12})\) 的新数值结论。

固定 Bol-gauged targets 的 rank4 结论保持有效；当前结论准确区分它们与 nongauged primitive。thin scalar subgroup、独立的新源、非代数扩张及重新建立的 bundle holonomy 定理仍不在本稿的排除范围内。

根任务已实际全文只读独审 §§1–6，重核标准 PV action 的第一列、零 translation 固定实际 \(H_j\)、\(h_j/(\tau-a)^2\) 的无限独立 orbit、共同 ordinary holomorphic germs、未平移 \(f_j\) 的 constant-line 论证、有限代数 restriction 以及无 prior-holonomic 定理的准确范围，限定通过。根任务没有运行 producer；本稿没有 producer。本文在上述范围冻结，不修改已冻结的 (A13) 输入；后续审阅只作外部记录，不为追加审阅改变本文件。
