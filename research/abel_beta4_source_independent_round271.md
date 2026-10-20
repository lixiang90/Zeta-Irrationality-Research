# 第271轮：Abel β(4)候选的独立移线与算术审查

2026-10-20，`new_primary_271`。针对根提出的具体候选作自含纸面反证审查；不运行数学程序、参数扫描、旧producer或Lean，不改状态账。

结论：Abel定义、纯β(4)投影与中心正Gram分别可以成立，但**它们不是同一纯目标对象**。中心移线必保留半整数极点的π³/π⁵残数；n=1给明确非零反例。此外，原提案从k≥1求和，不能直接继承作者k≥0模型的奇素数p>n整性。全稿的这一有限处引理均限 \(p>\max(n,2)\)；2处另付。

## 1. 原生Abel和与完整多项式头

设n=2r−1，c=−r，
\[
R_n(t)=\frac{\prod_{j=1}^n(t+j)^3}{\prod_{k=0}^n(t+k+1/2)^3},\quad
x=t-c,\quad F(t)=R_n(t)P(x),\quad P\in\mathbf Z[x^2].
\]
有 \(R_n(2c-t)=-R_n(t)\)，故F也反射奇。对任意固定degree的P，F具有唯一分解
\[
F(t)=Q(t)+\sum_{k=0}^{n}\sum_{i=1}^3\frac{a_{i,k}}{(t+k+1/2)^i}.
\tag{A1}
\]
分母monic且系数dyadic，故 \(Q\in\mathbf Z[1/2][t]\)；对每个奇素数p>n，所有 \(a_{i,k}\in\mathbf Z_p\)。后者因为局部展开只除2及非零差 \(k'-k\)，其绝对值≤n。

令 \(\mathcal E(q)=\lim_{z\uparrow1}\sum_{l\ge0}(-z)^lq(l)\)。多项式的极限存在；由生成函数 \((1+ze^u)^{-1}\) 在z=1处对u求导得到 \(\mathcal E(t^d)\in\mathbf Z[1/2]\)。因此
\[
A_0(F):=\operatorname{Abel}\sum_{l\ge0}(-1)^lF''(l)
=\mathcal E(Q'')+\sum_{i,k}(-1)^k2^{i+2}i(i+1)a_{i,k}
\left(\beta(i+2)-\sigma_k^{(i+2)}\right),
\tag{A2}
\]
其中 \(\sigma_k^{(j)}=\sum_{v=0}^{k-1}(-1)^v(2v+1)^{-j}\)。proper部分绝对收敛，不需正则化。

唯一分解保留反射，故 \(a_{i,n-k}=(-1)^{i+1}a_{i,k}\)。n奇使(A2)中奇i的周期系数为零，留下 \(A_0(F)\in\mathbf Q+\mathbf Q\beta(4)\)。这包括全部Euler多项式头；不是只对proper部分的形式投影。根提案的起点则是
\[
A_1(F)=A_0(F)-F''(0).
\tag{A3}
\]

## 2. 双头算术能保留的准确范围

对 \(1\le\ell\le n\) 定义
\[
T(\ell,k)=\sum_i a_{i,k}i(i+1)(k-\ell+1/2)^{-i-2}.
\]
整数内部三重零给 \(F''(-\ell)=0\)，从而
\[
\sum_{k\ge\ell}T(\ell,k)+\sum_{k<\ell}T(\ell,k)=-Q''(-\ell)\in\mathbf Z_p
\quad(p>\max(n,2)).
\tag{A4}
\]
这不是原proper模型中“总和为零”的身份，但右侧p整足够：如果两侧分别有坏分母，存在不同 \(k_1,k_2\in[0,n]\) 使 \(p\mid2(k_1-k_2)\)，与奇素数p>n矛盾。所以一侧逐项p整，再由(A4)迫另一侧p整。将调和头重排为这些尾和，连同dyadic的 \(\mathcal E(Q'')\)，证明**A₀的全部有理栏及β(4)系数在奇素数p>n时p整**。

这不能无条件传给A₁。\(F''(0)\) 的分母可含 \(2k+1\) 的素数，最大到2n+1。下节n=1即有 \(v_3(F''(0))=-4\)，故奇素数p>n安全性对原k≥1版本为假。加回k=0可修复该起点差别，但不消除中心移线的周期污染。

## 3. Abel和到右竖线：可证；移到中心：有额外残数

置 \(K(t)=\pi\csc\pi t\)，对 \(\sigma=1/2\) 定义
\[
V_\sigma(F)=\frac1{2\pi i}\int_{\sigma-i\infty}^{\sigma+i\infty}F(t)K''(t)\,dt.
\]
有精确身份 \(V_\sigma(F)=-A_1(F)\)。证明不能直接把多项式右边界扔掉：先在 \(F''(t)K(t)\) 中乘 \(e^{-\epsilon t}\)，向右闭合，右边界由指数因子消失，取得阻尼交错和；竖线分部积分两次得到
\(F e^{-\epsilon t}(K''-2\epsilon K'+\epsilon^2K)\)。固定竖线上的指数衰减允许 \(\epsilon\downarrow0\) 支配极限，才得到上述等价。

从σ移到c时，负整数处由三重零消去；t=0产生 \(F''(0)\)，另越过 \(-k-1/2\)，\(0\le k\le r-1\)。在这些半整数处
\[
\operatorname{Res}(FK'',-k-1/2)
=(-1)^{k+1}\left(\pi^3a_{1,k}+\frac52\pi^5a_{3,k}\right).
\tag{A5}
\]
这里使用 \(K''=(-1)^{k+1}\pi^3\)、\(K'''=0\)、\(K''''=5(-1)^{k+1}\pi^5\)。令 \(B_j(F)=\sum_{k=0}^{r-1}(-1)^ka_{j,k}\)，向上竖线/向右闭合的符号给
\[
\boxed{\ V_c(F)=-A_0(F)+\pi^3 B_1(F)+\frac52\pi^5 B_3(F).\ }
\tag{A6}
\]
因此中心实际向量一般为 \((1,\beta(4),\pi^3,\pi^5)\)。全反射只消掉完整交错和的奇周期栏，不消掉单侧半极点残数。

## 4. n=1的精确反例，无正则化争议

n=1、c=−1、x=t+1、P=1时
\[
R=\frac{x^3}{(x^2-1/4)^3}
=\frac{1/8}{(t+1/2)^3}+\frac{3/8}{(t+1/2)^2}
+\frac{1/8}{(t+3/2)^3}-\frac{3/8}{(t+3/2)^2}.
\]
直接代入绝对收敛的(A2)与导数得
\[
A_0(R)=12+72\beta(4),\quad R''(0)=6784/81,
\quad B_1=0,\ B_3=1/8.
\]
所以
\[
\boxed{\ V_{-1}(R)=\frac5{16}\pi^5-12-72\beta(4),\qquad
A_1(R)=12+72\beta(4)-6784/81.\ }
\tag{A7}
\]
非零π⁵项及p=3的大素数有限头均已出现在最小合法尺度，不能归因于高degree的Abel规则选择。

## 5. 中心正Gram真实存在，但属于(A6)

令
\[
H_r(y)=\frac{\prod_{j=1}^{r-1}(y^2+j^2)^3}
 {\prod_{j=1}^{r}(y^2+(j-1/2)^2)^3}>0.
\]
则 \(R(c+iy)=iy^3H_r(y)\)，且
\[
K''(c+iy)=i(-1)^r\pi^3\operatorname{csch}(\pi y)
\bigl(1+2\operatorname{csch}^2(\pi y)\bigr).
\]
因此全局sign和行列sign作有理变换后，中心矩确为 \(1,y^2,y^4,\ldots\) 对正测度
\[
d\mu_r(y)=\frac{\pi^2}{2}y^3H_r(y)\operatorname{csch}(\pi y)
\bigl(1+2\operatorname{csch}^2(\pi y)\bigr)dy
\]
的Gram；**此密度的积分域是整个 \(\mathbf R\)**。权重与所用偶多项式乘积均为偶函数，若改为 \(0<y<\infty\)，密度前因子须改成 \(\pi^2\)，不能仍取 \(\pi^2/2\)。该归一化直接来自 \(dt=i\,dy\) 及 \((2\pi i)^{-1}\)，没有额外的半轴因子。

零点处可去，∞指数衰减，所有大小m均严格正定。此正性付的是(A6)，不能移给A₀/A₁；仅假设β(4)有理仍留下π³、π⁵，不能形成纯目标小整数。若另行设计 \(B_1=B_3=0\) 的行池，须重新证明实际维数、Gram非零及全部费用；本审查未否定该新约束或其它源。

## 6. 旧资产去重的实际范围

定向rg检查Abel/Boole/Plana、正则交错和、csc及β(4)入口，未找到相同Abel定义；这不是全仓库数学等价性的穷尽结论。另实际读旧 `cdt_beta4_projection_exact_arithmetic_20261007.md`、`cdt_beta4_projection_nonvanishing_20261007.md`、`cdt_beta4_real_determinant_energy_20261007.md` 的入口及原对象，和236权重4复盘入口：它们是二变量 \(C_3(u,v)\) 的Hermite投影 \(q+\beta(4)I\) 或另一holonomy载体，不能直接给本Abel对象预算。

本候选改变了literal degree障碍，却在同对象周期投影上失败；这里没有新指定数值结论、无理性预算或全Abel方法no-go。
