# Level 12：真实源的全前缀分母率与 Hecke 配对

日期：2026-10-06。新建证明记录。只使用已经实际阅读的 [源与周期](cdt_odd_level12_source_period_20261006.md) 和 [配对坐标及秩](cdt_odd_level12_paired_coordinate_20261006.md)。不运行旧证书，不作素数或参数扫描。本稿证明一个全尺度算术限制和一个源层的全系数 Hecke 同余；不证明新的数值无理性，也不把源层的可逆性替代为尚未构造的 native Cartier 矩阵。

## 1. 固定的源、坐标和反证假设

令 \(r=\sqrt3\)、\(K=\mathbb Q(r)\)、\(\mathcal O_K=\mathbb Z[r]\)、\(\chi=\chi_{12}\)。固定
\[
\begin{split}
F={}&1217E_4-14082E_4(2\tau)+6255E_4(3\tau)-11120E_4(4\tau)\\
&+126738E_4(6\tau)-175248E_4(12\tau)+2880E_\chi-69120rF_\chi,\\
B={}&E_2-12E_2(12\tau),\qquad f=\sum_{n\ge1}F_nq^n/n^3,\qquad
H=B(f-\Theta),\quad \Theta=34560rL(3,\chi).
\end{split}
\tag{D1}
\]
这里 \(E_\chi=23+\sum\chi(d)d^3q^{dn}\)，\(F_\chi=\sum\chi(n)m^3q^{mn}\)，普通 \(E_4\) 常数项为 1。全部正次数源系数与 \(B\) 系数在 \(\mathcal O_K\)，\(B_0=-11,B_1=-24\)。

仅在无理性反证假设 \(L(3,\chi)\in\mathbb Q\) 下，取固定正整数 \(D_0\) 清掉 \(\Theta\) 的分母。已证的 \(t_-,t_+\) 与相应 \(q(t)\) 均以一次项 1 开始，双向系数在 \(\mathcal O_K\)。所以 \(D_0D_n^3\) 清掉两个真实嵌入的全部前 \(n\) 项，\(D_n=\operatorname{lcm}(1,\ldots,n)\)。

## 2. 几乎所有素数上的完整三层分母

对任何 \(p\nmid12\)，只有 \(E_4(\tau)\) 在普通 oldscales 中贡献第 \(p\) 项。因此，写 \(\epsilon=\chi(p)=\pm1\)，准确有
\[
F_p=(294960-69120r\epsilon)
 +p^3(292080+2880\epsilon-69120r).
\tag{D2}
\]
两个可能主项的范数相同：
\[
\operatorname{Norm}_{K/\mathbb Q}(294960-69120r\epsilon)
=72668678400=2^8\,3^2\,5^2\cdot419\cdot3011\ne0.
\tag{D3}
\]
故除 \(D_0\) 的素因子及 \(2,3,5,11,419,3011\) 外，\(F_p\) 在所有 \(p\) 上方的素理想中都是单位。

当 \(1\le j<p\) 时，\(f_j\) 在这些素理想上整；\(\Theta\) 也是整的。因此
\[
[q^p]H=-11F_p/p^3+\text{\(p\)-整项}
\tag{D4}
\]
在每个 \(p\) 上方都有准确的赋值 \(-3\)。令 \(q(t)=t+c_2t^2+\cdots\) 是任一真实整数反演。第 \(t^p\) 项只增加来自 \(H_j,j<p\) 的整项，故同样有
\[
v_{\mathfrak p}([t^p]H)=-3.
\tag{D5}
\]
这对两嵌入分别成立；固定坏素数集没有依赖 \(p\) 增长。

若 \(M_n\) 是清掉 \(H(t)\) 前 \(n\) 项的最小正整数，则
\[
\prod_{\substack{p\le n\\p\notin S}}p^3\mid M_n,\qquad
M_n\le D_0D_n^3,
\]
其中 \(S\) 是上述固定有限集。由素数定理，
\[
\boxed{\log M_n=3n+o(n).}
\tag{D6}
\]
这里的结论针对这个真实函数的公共前缀分母。没有把某个有限 \(q\) 展开或固定好素数当作全尺度证明。

## 3. 对固定 Euler 导数行也存在满三层分母

第 \(q^{p+1}\) 项只有 \(f_p B_1\) 含 \(p^{-3}\) 主部：
\[
p^3[q^{p+1}]H\equiv-24(294960-69120r\epsilon)\pmod p.
\tag{D7}
\]
换到 \(t\) 后，来自 \(H_pq(t)^p\) 的额外系数为 \(p c_2H_p\)，在 (D7) 的模 \(p\) 主部中为零；低于 \(p\) 的项仍整。因此 (D7) 在 \(t\) 中同样成立。

对任一固定 \(j\ge0\)，令 \(\vartheta_t=t\partial_t\)。第 \(p+1\) 项乘以 \((p+1)^j\)，它模 \(p\) 为 1，故 \(\vartheta_t^jH\) 也保留这三层。特别是实际秩 4 的基
\[
1,\quad H,\quad\vartheta_tH,\quad\vartheta_t^2H
\tag{D8}
\]
的后三行，不能借固定 Euler 导数免费降成两层分母。普通导数有索引偏移，不能不加说明地沿用同一第 \(p+1\) 项论证；(D8) 明确采用 Euler 导数。

更具体地，若为其中一行指定 CDT 型的固定分母
\[
n^e\prod_{\nu=1}^k D_{\lfloor b_\nu n\rfloor},
\]
在 \(n=p+1\) 时 \(n^e\) 是 \(p\)-单位。固定 \(b_\nu<1\) 的列最终不含 \(p\)；固定 \(b_\nu\ge1\) 的每列最终最多含一层 \(p\)。所以至少三列必须满足 \(b_\nu\ge1\)。这只排除逐行固定分母类型的改善，**不排除随 \(p\) 变化的混合整数格、Smith 层或多函数消去**。

## 4. 全 \(q\) 系数的源层 Hecke 同余

把源分为
\[
F=U+X+Y,\qquad X=2880E_\chi,\quad Y=-69120rF_\chi,
\]
其中 \(U\) 是 (D1) 的六项 ordinary oldscale 组合。定义
\[
U_p\sum a_nq^n=\sum a_{pn}q^n,\qquad V_pG(q)=G(q^p).
\]
由除数和在 \(p\) 处的 Euler 因子，对全部系数（含常数项）有
\[
\begin{split}
U_pU&=(1+p^3)U-p^3V_pU,\\
U_pX&=(1+\epsilon p^3)X-\epsilon p^3V_pX,\\
U_pY&=(\epsilon+p^3)Y-\epsilon p^3V_pY.
\end{split}
\tag{D9}
\]
这可直接把 \(n=p^am\), \(p\nmid m\) 代入有限几何和验证；\(p\nmid12\) 时 \(U_p\) 与每个固定 oldscale 交换。常数项也准确相容。

设
\[
R_\epsilon=U+X+\epsilon Y,\quad
S_\epsilon=U+\epsilon X+Y,\quad
T_\epsilon=U+\epsilon X+\epsilon Y.
\]
于是
\[
U_pF=R_\epsilon+p^3S_\epsilon-p^3V_pT_\epsilon,
\qquad
\boxed{U_pF\equiv
\begin{cases}F,&\chi(p)=1,\\ \sigma F,&\chi(p)=-1\end{cases}\pmod {p^3}.}
\tag{D10}
\]
这不是只验证若干首项的同余。两个真实源由系数共轭配对，因而 \(U_p\sigma F\) 也对应地保持或互换。

在约化源空间中，需排除两源约化相关的有限坏素数。其前两项矩阵已经给出非零行列式
\[
\det\begin{pmatrix}F_1&(\sigma F)_1\\F_2&(\sigma F)_2\end{pmatrix}
=429616742400r,\qquad
F_2=-748080-552960r.
\tag{D11}
\]
所以该行列式范数以外的素数上，两个约化源独立，(D10) 的源层矩阵确为恒等或互换，可逆。

## 5. 下一步受到的准确限制

源层 (D10) 表明：这个固定纯 \(L\) 源没有“在某一无穷素数类上 \(U_pF\) 消失”的机会。它没有构造 native 微分行的 Cartier 矩阵，也没有证明所有多项式核或跨背景消去不存在。后者需要把源、真实连接和整数评价格实际连接起来。

(D6) 与 (D8) 给出的完整三层成本，必须与合法的同一组函数及解析地图一起进入 CDT。单行分母率、源层 Hecke 可逆性、完整格的行列式收益是三个不同问题。本稿没有将其中任意一个替代为另外两个。

固定源范数与前两项算术由 [新 source-family 证书](cdt_odd_level12_source_family_20261006_verify.py) 的有限精确计算补核；全尺度结论由上述证明承担。该证书也服务于另稿的两周期族，不调用任何旧 producer。
