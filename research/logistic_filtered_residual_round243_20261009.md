# 第243轮：真实CRT余空间上的Schur首层

2026-10-09，C独立纸推。固定240–242的完整K5泛函、原 \(h=3n\) 列池及 \(S_n/F_n\) 归一化。本文支付实际负pivot剥离后的首层，而不以ambient低秩代替真实限制。数学程序0；无素数样本、参数扫描或新primary下载。

## 1. 同一完整矩阵与Gauss环

令
\[
 D_a(t)=\prod_{j=1}^a(t+j),\quad R=D_n^4/D_{5n},\quad h=3n,
 \quad S=(5n)!/(n!)^4,\quad F=\prod_{i=0}^{h-1}(i!)^2.
 \tag{C1}
\]
若 \(tf=P+\sum c_j/(t+j)\)，取 \(B^+(t^a)=B_a^+\)、\(B_1^+=1/2\)，完整泛函为
\[
 U_T(f)=\tfrac32B^+(P')+\tfrac1{24}B^+(P''')
 +\sum_jc_j(3H_j^{(3)}+H_j^{(5)})-T\sum_jc_j.
\]
置 \(M(T)=[U_T(t^{i+k}R)]_{i,k<h}\)、\(Q=\det M\)、
\(\widetilde Q=S^hQ/F\)。对任意整数 \(e\ge0\)，目标系数
\(a_e=-[t^{-2}]t^eR\in\mathbf Z\)。首一除法使商部整；不能删除商部、低头、三阶项或目标 \(T\)。

全文用固定素数 \(p>29\)、\(2n<p<3n\)。记 \(s=\lfloor5n/p\rfloor\)、
\(\tau=5n-sp\)。242强头稿已付全部系数分解
\[
 SM=W(T)+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,\quad
 v_j=((-j)^i)_{i<h},
\]
\[
 \omega_j=Sj\operatorname{Res}_{-j}R
 =(-1)^{j-1}j^2\binom{5n}{j}\binom{j-1}{n}^{4},\quad
 \gamma_j=-p^{-5}\omega_j
 (H_{\lfloor j/p\rfloor}^{(5)}+3p^2H_{\lfloor j/p\rfloor}^{(3)}).
 \tag{C2}
\]
这里 \(W\) 包含全部非 \(p\) 调和头、商部和目标系数；\(W\in pM_h(\mathbf Z_p[T])\)。\(s=2\) 时头与目标系数更在 \(p^2\)，只有商部的一阶Bernoulli危险系数能留在 \(W/p\bmod p\)。

令 \(g_p\) 为多项式全部系数的最小估值，将它扩张为
\(\mathbf Q_p(T)\) 的Gauss离散估值。其整数环记 \(\mathcal O_G\)，剩余域
\(\mathbf F_p(T)\)。下文Schur消元可在此环进行：每个pivot的抽尺度首项是非零常数，所以余下分母是Gauss单位。它不要求某固定 \(T=g\) 的pivot非零。最终结论是完整多项式系数的 \(g_p\) 下界，不能以泛型 \(T\) 代替每个有理假设点非零。

## 2. s=2：真实单位CRT基与负pivot

本节 \(2n<p<5n/2\)，故 \(0<\tau<n\)、\(v_pS=2\)。所有高头实际节点为
\(-p,-2p\)，以及 \(-p-a\)（\(1\le a<p\)），另有 \(-2p-a\)（\(1\le a\le\tau\)）。取
\[
 \Psi(t)=(t+p)(t+2p)\prod_{a=1}^{p-1}(t+p+a),\quad
 r=h-p-1=3n-p-1.
 \tag{C3}
\]
真实余空间是 \(f=\Psi u\)、\(\deg u<r\)。它严格消去每类首个节点及两个零类节点，不是自由选择的minor。

为证明全基变换是单位，令 \(B_0=\prod_{a=1}^{p-1}(t+p+a)\)。对每个非零类a取degree≤p的Lagrange多项式 \(\ell_a\)：在 \(-p-a\) 取1，其他非零首节点及 \(-p,-2p\) 取0。其分母都是单位。零类取
\[
 \ell_1=-\frac{(t+p)B_0(t)}{B_0(-2p)},\quad
 \ell_0=B_0(t)(A+B(t+p)),
\]
\[
 A=B_0(-p)^{-1},\quad
 B=\frac{B_0(-p)^{-1}-B_0(-2p)^{-1}}p\in\mathbf Z_p.
\]
其零类取值分别为 \((0,p)\)、\((1,1)\)。模p后，\(\ell_a\) 给所有非零节点的值基，\(\ell_0\) 给0值，\(\ell_1\) 给0导数且其导数为−1。因此它们是 \(p+1\) 维Hermite CRT单位基。再附加首一 \(\Psi t^i\)、\(0\le i<r\)，得到degree<h的完整单位基；行列两侧变换不改变Gauss估值。

阶乘的p进数字（全部小于p²）从C2直接给
\(v_p\omega_{mp+a}=2[a=0]+[a>\tau]+4[1\le a\le n]\)。
高头系数的准确局部尺度为

| 类 | 节点 | \(v_p\gamma\) | 剥离的pivot估值 |
|---|---:|---:|---:|
| 0 | \(p,2p\) | −3,−3 | −3,−1 |
| \(1\le a\le\tau\) | \(p+a,2p+a\) | −1,−1 | −1 |
| \(\tau<a\le n\) | \(p+a\) | 0 | 0 |
| \(n<a<p\) | \(p+a\) | −4 | −4 |

两个同类比值可直接从C2支付。对 \(a\le\tau\)，除 \(p^4\) 后
\(\omega_{2p+a}/\omega_{p+a}\equiv-8\)：二项式首因子比为 \(1/2\)，
\(p^{-1}\binom{2p+a-1}n / p^{-1}\binom{p+a-1}n\equiv2\)，奇数p带来符号−1。零类除 \(p^2\) 后比为−2。因此
\[
 \gamma_{2p+a}/\gamma_{p+a}\equiv-33/4\quad(1\le a\le\tau),
 \qquad \gamma_{2p}/\gamma_p\equiv-33/16.
 \tag{C4}
\]
非零双节点值pivot的单位因子为 \(1-33/4=-29/4\)；零类首pivot为
\(1-33/16=-17/16\)。零类第二pivot由
\(\det\begin{pmatrix}\gamma_p+\gamma_{2p}&p\gamma_{2p}\\p\gamma_{2p}&p^2\gamma_{2p}\end{pmatrix}
=p^2\gamma_p\gamma_{2p}\)
给估值−1。\(p>29\) 排除2、3、11、17、29等有限例外。它们不影响宏观面积，但本文不对例外借单位结论。

这些pivot属于同一完整矩阵，不能只剥一个秩一近似。确切的首层消元理由如下。余空间在每个首节点为0，在未消去第二节点有 \(p\) 因子。非双节点pivot到余空间的交叉项至少 \(p\)，其逆估值为0、1、3或4，故它们对余空间Schur修正至少 \(p^2\)。双节点值pivot之间的非对角项至少整，其主对角为 \(p^{-1}\) 单位；其逆对角为 \(p\) 单位、逆非对角至少 \(p^2\)。该类到余空间的交叉项可以估值0，正是需要保留的首层修正。\(W\) 的交叉项至少 \(p\)，与这些负pivot混合只能给 \(p^2\) 或更高修正。零类先用估值1的shear消去其交叉项，不改变上述界。

所以完整选定 \(p+1\) 个pivot的Gauss估值和恰为
\[
 D_{\rm piv}=-4-\tau-4(p-1-n)=-n-2p.
 \tag{C5}
\]
其余实际Schur矩阵 \(Z(T)\in pM_r(\mathcal O_G)\)。所有高头和商部仍在这一个Schur对象中。

## 3. 精确首层：无穷远块加真实第二节点

记 \(A_p(t)=t^p-t\)。模p有
\(D_{5n}=A_p^2D_\tau\)、\(\Psi=tA_p\)。危险Bernoulli公式在实际degree≤5n−1范围内是
\[
 pB^+(P')\equiv[t^{2p-1}]P,\quad B^+(P''')\in\mathbf Z_p.
\]
一阶的 \(d=p\) 分母被d抵消，只有 \(d=2p-1\) 留下；三阶前几个危险次数都被falling factorial抵消。故这不删三阶，而是证明其不在首层。令
\[
 C(t)=D_n(t)^4/D_\tau(t)\in\mathbf F_p[t],\quad
 \alpha=\overline{\tfrac32S/p^2}=3\tau!/(n!)^4\ne0,
\]
\[
 H^\infty_{ij}=[t^{2p-4}]C(t)t^{i+j},\quad 0\le i,j<r.
 \tag{C6}
\]
Wilson给 \(\overline{S/p^2}=2\tau!/(n!)^4\)。由于
\(t\overline R\overline\Psi^2=t^3C\)，C6恰为 \(W/p\) 在实际余空间的商部首层；不是任取ambient高阶子块。

置 \(u_a=\overline{\omega_{p+a}/p^4}\ne0\)、\(v(x)=(1,x,\ldots,x^{r-1})^t\)。在未消去第二节点
\[
 \Psi(-2p-a)/p\equiv-a.
\]
这是 \(-\overline\Psi'(-a)\)，因为 \(\overline\Psi=tA_p\) 且
\(\overline\Psi'(-a)=a\)。保留pair的首层Schur系数为
\(\gamma_1\gamma_2/(\gamma_1+\gamma_2)\)，C4因此给
\[
 \eta_a=-\frac{33}{29}u_a a^2\in\mathbf F_p^\times.
\]
完整首层恒等式是
\[
 \boxed{\overline{Z/p}
 =\alpha H^\infty+\sum_{a=1}^{\tau}\eta_a v(-a)v(-a)^t.}
 \tag{C7}
\]
等式在 \(\mathbf F_p(T)\) 中成立，右侧实际在 \(\mathbf F_p\)。目标、全部非p头与三阶商部的首层为0；它们仍在更高层，而不是从矩阵删去。

## 4. 准确的首层kernel与有限费用改进

本节令
\[
 \delta=r-2\tau-1=3p-7n-2\ge0,\quad
 k=r-\tau-1=p-2n-2=\tau+\delta.
\]

由于 \(C\) 首一、degree \(2p-n\)，\(H^\infty_{ij}=0\) 当
\(i+j<n-4\)，边界等于1。前k行列为0，余下 \(\tau+1\) 阶反三角单位块。因此
\(\operatorname{rank}H^\infty=\tau+1\)，其radical是次数<k的多项式空间。

在该radical上，
\(q\mapsto(q(-1),\ldots,q(-\tau))\)
是满秩τ的映射，前τ单项式的Vandermonde是单位。用这τ个radical方向消去高块的所有评价值，不会改变 \(H^\infty\)。C7遂分成一个非退化τ维评价块、一个非退化 \(\tau+1\) 维无穷远块以及它们共同的radical。准确得到
\[
 \boxed{\operatorname{rank}_{\mathbf F_p}\overline{Z/p}=2\tau+1,
 \qquad\ker\overline{Z/p}=D_\tau\mathbf F_p[t]_{<\delta}.}
 \tag{C8}
\]
这里核是模p首层的核，不是完整Schur矩阵的核。其升格、多项式 \(T\) 的下一层内容均未付。

先从Z每列抽p，C8使剩下矩阵至少有δ个p因子，故
\(g_p(\det Z)\ge r+\delta\)。当δ<0时只用 \(Z\in pM_r\)，不借C8。这给同一完整矩阵
\[
 g_p(\det(SM))\ge2n-3p-1+(3p-7n-2)_+.
 \tag{C9}
\]
对 \(Q\ne0\)，令 \(d_n>0\) 为把 \(\widetilde Q\) 化成primitive整数多项式的有理标量。由 \(v_pF=2(3n-p)\)，
\[
 \boxed{v_p(d_n)\le4n+p+1-(3p-7n-2)_+,\quad2n<p<5n/2.}
 \tag{C10}
\]
在 \(p>(7n+2)/3\) 时右端 \(11n-2p+3\)。面积改进
\(\int_{7/3}^{5/2}(3x-7)\,dx=1/24\)。这与A的全部minor证明相符；真实CRT和C7另解释为何同一个首层只给δ个缺方向，不能从首层再领取更大节省。它不排除更高层内容，不是actual费用下界或全部方法no-go。

## 5. s=1：真实限制保留完整常数与目标载体

现在 \(5n/2<p<3n\)、\(s=1\)、\(n<\tau=5n-p<p\)。所有高头节点是
\(-p-a\)、\(0\le a\le\tau\)，模p互异。实际消去多项式与余维为
\[
 \Psi_1=\prod_{a=0}^{\tau}(t+p+a),\quad
 r_1=p-2n-1,\quad \overline\Psi_1=tD_\tau.
 \tag{C11}
\]
普通Lagrange评价基加 \(\Psi_1t^i\) 是整数单位基。被消去的节点pivot估值为−3（0类）、−1（1…n）、−5（n+1…τ）；所有余空间到pivot交叉项仅来自W，至少p，而逆pivot至少p。因此其Schur修正至少 \(p^3\)。真实Schur首层是
\[
 \overline{Z_1/p}
 =\overline{S/p}
 [\overline{U_T(t^{i+j}K_1)}]_{i,j<r_1},\qquad
 K_1=R\Psi_1^2=D_n^4\Psi_1/D_{p-1}.
 \tag{C12}
\]
此完整泛函在p整：剩余极点都在j<p，节点差为单位；商部degree≤5n−1<2p−1，未抵消的一阶Bernoulli危险系数不出现，三阶亦整。C12保留低头、整数商部、三阶和T，不可以因危险层为0就称整个首层为0。

令 \(E=(t^p-t)/(tD_\tau)\)、\(e_1=2p-5n-1\ge0\)。目标系数的无穷远载体为
\[
 -t\overline K_1=-\frac{t^2D_n^4}{E},\quad \deg E=e_1.
 \tag{C13}
\]
右式可以有多项式商，但它不贡献负次Laurent系数。分子与E互素；E的根在 \(-a\)、\(\tau<a<p\)，不碰0或D_n。若 \(e_1>0\)，商环
\(\mathbf F_p[t]/(E)\) 上的首项配对
\(\theta(fgN)=[t^{e_1-1}](fgN\bmod E)\)
非退化，因为N是单位；对任意非零f取 \(g=t^{e_1-1-\deg f}\) 即可证明基配对非退化。它恰是此载体的前 \(e_1\) 阶Hankel矩阵。再用E的递推及 \(r_1-e_1=3n-p>0\)，得到
\[
 \boxed{\operatorname{rank}_{\mathbf F_p}[T]\overline{Z_1/p}
 =e_1=2p-5n-1.}\tag{C14}
\]
e1=0时载体是多项式，所有目标矩为0。C14只支付目标系数的秩；它既不支付完整仿射矩阵的秩，也不使常数项自动pdiv。没有据此给s=1新的全部系数费用节省。

Root243目标载体稿T1–T7已实际FULL独立纸审；其未过滤 \([T]\overline{W/p}\) 秩 \(h-1\) 与过滤后C14均通过。前者可以含重复极点，自足商环配对不要求可分性。本文不把未过滤高秩或过滤后低秩直接代替完整Schur。

## 6. 本轮边界与下一决定

已付的是同一完整矩阵的单位基、Gauss环合法消元、s=2精确首层秩/kernel和安全面积改进1/24，以及s=1真实完整限制与目标系数秩。未付的是s=1常数/fullSchur内容、任何下一层额外费用、严格全预算<6、实处−6的独立完整认证及新数值结论。241的无界假设点非零是既有资产，不由本稿重新证明，不扩成所有n。

本轮到首层即停止；244正式全局复盘。实际读取身份、独审范围和数学运行0见
[阅读记录](../literature/logistic_residual_filter_sources_round243_20261009/dual_reading_scope.md)。没有修改242基线或旧归档。
