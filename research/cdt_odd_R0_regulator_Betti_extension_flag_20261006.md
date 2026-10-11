# R0 实际 regulator 的 Betti 扩张、整数投影与原点旗标

日期：2026-10-06。NEW 推导。已有数学稿、PY、JSON、manifest 全部只读，未执行或 import 任何旧稿或同行 producer。本稿的整数结论只涉及指定四维周期分量及其实际扩张；不将它替换为整系数 higher-Chow completion 或整 Taylor germ。

## B1. 输入与本轮结果

实际全文重读主报告 §§79–84 及 delivery 的当前冻结状态：345 个输入、93 个 proof/review、74 份 PDF 共 4399 页、1124 条本地链接。主报告快照 SHA256 为
\[
\texttt{2e148742cc6e80381d5b46f434f3085954209887a934bcea19c3881ed285ccab};
\]
delivery 快照为
\[
\texttt{a1c8eb95c0052a0186ed0b2377bd41ec43c31f8ea3807825fb3daca576e5cb26}.
\]
本轮还实际全文重读 Yukawa 稿，重点 Y8–Y10 的两个 degree-one 映射、Y27 的真实 vanishing cycle；实际读 KLM 原件 PDF12–14。其余冻结结果按注明的输入使用，未重新运行任何 producer。

在基底 \(B=\mathbf P^1\setminus\{0,1,\infty\}\) 上，令 \(a=2\pi i\)，\(x=\lambda/256\)，\(\chi\) 为 \(\sqrt x\) 的符号局部系统。既有全角点定理已构造中心化 compact current \(r_c\)，并证明
\[
Q(r_c,\omega)=-16a^3W,\qquad
r_{\rm corr}=r_c+\frac{a^4}{8}\operatorname{PD}\Gamma,\qquad
Q(r_{\rm corr},\omega)=-16a^3\Psi .
\tag{B1.1}
\]
这指定了一条实际 lift，不表示所有 lift 的标量都相等。

本轮所得：

1. 四维周期空间有实际饱和、unimodular 的整数 Betti 格 \(\Lambda\)，旧有 rational graph projector 实际是整数投影。
2. 中心化 lift 在该分量上的两条生成回路 cocycle 为 \(0,\Delta\)，其中 \(\Delta=\operatorname{PD}\delta\in\Lambda\)。因此实际 rank-five 扩张有整数 monodromy，不只是某个抽象有理扩张。
3. \(\Gamma\) 的四维投影 \(G\) 属于 \(2\Lambda\)。故 \(\Gamma/8\) 修正的 cochain 成本至多 \(4\)，生成回路 cocycle 成本至多 \(2\)。
4. 原点谱投影和最高 log 旗标在实际中心化格上是整数算子。其通用 CRT 多项式表达仍分别有明确的 \(16,2\) 或 \(256,32\) 分母。
5. 上述 Betti 结论不提供 \(g_1,g_2\) 的 Betti/de Rham 比较矩阵，不消除 CDT 所需的完整算术 Taylor 前缀与有效容量条件。

## B2. degree-one graph 给出的整投影

冻结 Y8–Y10 构造光滑 proper 共同 resolution
\[
X\xleftarrow{\,a_0\,}Z\xrightarrow{\,b_0\,}W
\]
（在有限代数覆盖和一个非空光滑基底上），两映射都是 birational degree one；\(H^3(W,\mathbf Q)\) 恰为四维周期系统。此处 \(a_0,b_0\) 是映射，不能与 \(a=2\pi i\) 混淆。冻结的全尺度论证得到
\[
i=a_{0*}b_0^*,\quad q=b_{0*}a_0^*,\quad qi=1_{\mathbf Q}.
\tag{B2.1}
\]
函数域的 degree-64 商映射不是此共同 resolution 的 degree-one 映射；不带入额外的 64 因子。

令 \(H_T=H^3(T,\mathbf Z)/\mathrm{tors}\)。同维 proper 光滑流形之间的 pushforward 由整数 Poincaré duality 定义，pullback 也是整数映射，且都保留 torsion。因此 \(i,q\) 是 free 整格间的映射。\(qi-1\) 在张量 \(\mathbf Q\) 后为零，故在 free 整格上为零：
\[
qi=1_{\mathbf Z}.
\tag{B2.2}
\]
所以
\[
\Pi=iq,\qquad \Lambda=i(H_W)
\tag{B2.3}
\]
是整数幂等投影和饱和 rank-four 子格。更具体，
\[
\Lambda=H_X\cap V_{\mathbf Q},\qquad
H_X=\Lambda\oplus\ker q.
\tag{B2.4}
\]
不要求整个 \(H^3(X)\) 为四维。

cup pairing 的 pull/push 伴随性给 \(q=i^\dagger\)，于是
\[
Q_X(iu,iv)=Q_W(u,qiv)=Q_W(u,v).
\tag{B2.5}
\]
\(H_W\) 的 free 中间上同调具有 unimodular 交错 pairing，故 \(\Lambda\) 也如此；\(\Pi\) 是 self-adjoint。该投影的 rational 版本是既有 cyclic 四维空间的唯一正交投影，已从有限覆盖下降。沿原始基底的整数 monodromy 平行传输 (B2.3)，可在全部光滑基底上下降为同一整数算子。覆盖或 spread 临时删去的普通光滑点由局部常值整数格唯一补回。

因此
\[
\Delta=\operatorname{PD}\delta\in\Lambda,\qquad
G=\Pi(\operatorname{PD}\Gamma)\in\Lambda.
\tag{B2.6}
\]
第一项还使用冻结 Y27 对真实 Picard–Lefschetz image 的判定。此处没有声称 \(\Delta,G\) primitive。

## B3. current、Tate 与实际 cocycle 的归一化

将 current 的四维分量除以 Tate 因子：
\[
R_c=\Pi r_c/a^4,\qquad
f_z(x)=-\frac a{16}Q(z,\omega(x))
\quad(z\text{ 为平坦 Betti 向量}).
\tag{B3.1}
\]
则 \(W=f_{R_c}\)。冻结 compact derivative 给
\[
\nabla_{\theta_x}r_c=16\sqrt x\,\omega.
\tag{B3.2}
\]
\(\sqrt x\,\omega\) 是原始基底上的单值代数形式；两因子各带同一 \(\chi\)。继续 analytically chosen lift 所产生的差是平坦 \(\mathbf Q(4)\) Betti 类。经 (B3.1) 归一化，其 cocycle \(c_\gamma\) 位于 \(V_{\mathbf Q}\)。

选路径乘法和 transport 约定，使
\[
M_{\gamma\eta}=M_\gamma M_\eta,\quad
c_{\gamma\eta}=c_\gamma+M_\gamma c_\eta.
\tag{B3.3}
\]
这里 \(M\) 是 physical Betti monodromy。相应标量延拓写为
\[
W^\gamma=\chi_\gamma W+\chi_\gamma f_{c_\gamma},
\qquad
f_z^\gamma=\chi_\gamma f_{M_\gamma z}.
\tag{B3.4}
\]
(B3.3) 是 affine Betti 扩张的 cocycle 公式，不能用 single-point 标量值反推向量。下节使用整条局部 period germ；若 \(Q(z,\omega)\) 作为 germ 为零，连续求四个 Gauss–Manin 导数，再用 cyclic 性，才可推出 \(z=0\)。

## B4. 两条生成回路的真实平移

令 \(\gamma_0,\gamma_1\) 分别为正向 origin、conifold 回路；固定冻结稿的 Picard–Lefschetz 方向。

原点有实际收敛表示
\[
W=\sqrt x\,B(x),\qquad B(0)=1,\quad B\in\mathbf Q[[x]],
\]
故 \(W^{\gamma_0}=-W\)。\(\chi_0=-1\)，physical \(M_0=-U\)，其中 \(U=J_4(1)\)。由 (B3.4) 和 germ 的 injectivity，
\[
c_0=0.
\tag{B4.1}
\]

Conifold 的完整 log 投影是
\[
W=\Psi+\frac{\pi^4}{16}y_0,\qquad
Q(G,\omega)=\frac{a^3}{2}y_0,\qquad
g=Q(\Delta,\omega).
\tag{B4.2}
\]
真实交点和 PL 公式为
\[
\Delta\cdot G=8,\quad G\cdot\Delta=-8,\quad
M_1G=G-8\Delta.
\tag{B4.3}
\]
因此
\[
y_0^{\gamma_1}-y_0=-16g/a^3,\quad
W^{\gamma_1}-W=-\pi^4g/a^3=-ag/16=f_\Delta.
\tag{B4.4}
\]
这里用了 \(a^4=16\pi^4\)，没有删除一个未知 homogeneous germ。故
\[
c_1=\Delta\in\Lambda.
\tag{B4.5}
\]
由 \(\pi_1(B)\) 为两生成元自由群、整数 \(M\) 及 (B3.3)，所有回路都有
\[
c_\gamma\in\Lambda.
\tag{B4.6}
\]
这是真实 current 选定的 cocycle 的全 word-length 结论。

## B5. actual rank-five 的整数格

在 Betti 扩张
\[
E_{B,\mathbf Z}=\Lambda\oplus\mathbf Z e_c
\]
上定义
\[
\rho_B(\gamma)=
\begin{pmatrix}M_\gamma&c_\gamma\\0&1\end{pmatrix}.
\tag{B5.1}
\]
(B4.6) 使它成为整数局部系统，张量 \(\mathbf Q\) 后就是 selected 四维分量上的 actual regulator extension。与 scalar Picard–Fuchs rank-five 系统比较时需将整个扩张 twist by \(\chi\)：
\[
E_{5,\mathbf Z}=\chi\otimes E_{B,\mathbf Z},\quad
T_0=\begin{pmatrix}U&0\\0&-1\end{pmatrix},\quad
T_1=\begin{pmatrix}M_1&\Delta\\0&1\end{pmatrix}.
\tag{B5.2}
\]
因此 origin \(J_4(1)\oplus(-1)\)，conifold \(T_1-1\) rank one；冻结真实 Stieltjes 渐近给 infinity \(J_5(-1)\)。整数格存在没有将解函数中的 \(a,\pi\) 宣称为代数数。

这只证明 actual free Betti 扩张的整格。它没有证明 rational higher-Chow \(\Xi\) 本身的整 completion、全 \(H^3(X)\) 的某个指定 marking 为整数，或所选解析 Taylor 初值属于 \(\overline{\mathbf Q}\)。

## B6. 一个实际整数矩阵模型

可在真实 orbit 子格
\[
\Lambda_\delta=\langle\Delta,U\Delta,U^2\Delta,U^3\Delta\rangle_{\mathbf Z}
\]
上展示矩阵。冻结 real Frobenius concomitant 的一般平移 \(na\) 给
\[
\Delta\cdot U^n\Delta=\frac83(n^3+2n)\quad(n\in\mathbf Z).
\tag{B6.1}
\]
其 Gram 矩阵为
\[
J_\delta=
\begin{pmatrix}
0&8&32&88\\-8&0&8&32\\-32&-8&0&8\\-88&-32&-8&0
\end{pmatrix},
\qquad \operatorname{Pf}(J_\delta)=-256 .
\tag{B6.2}
\]
这四向量独立；在 unimodular \(\Lambda\) 内，\([\Lambda:\Lambda_\delta]=256\)。本节使用一般 \(n\) 的公式，绝非有限个数值样本推出。

在上述列基底中，
\[
U=
\begin{pmatrix}
0&0&0&-1\\1&0&0&4\\0&1&0&-6\\0&0&1&4
\end{pmatrix},
\quad
M_1=
\begin{pmatrix}
1&-8&-32&-88\\0&1&0&0\\0&0&1&0\\0&0&0&1
\end{pmatrix}.
\tag{B6.3}
\]
这是 \((U-1)^4=0\) 和 (B4.3) 的实际 PL action；physical \(M_0=-U\)。所以在 \(\Lambda_\delta\oplus\mathbf Z e_c\) 上
\[
T_0=\operatorname{diag}(U,-1),\quad
T_1=
\begin{pmatrix}
1&-8&-32&-88&1\\
0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\\0&0&0&0&1
\end{pmatrix}.
\tag{B6.4}
\]
这一子格也稳定；更大的 actual saturated 格 \(\Lambda\) 由 B2 得到。没有假设 orbit 子格已 unimodular。

## B7. \(G\) 的偶性与 \(\Gamma/8\) 的成本

令 \(N=\log U\)。因 \(N^4=0\)，
\[
N^3=(U-1)^3
\tag{B7.1}
\]
是整数算子。冻结真实 Frobenius 标度给 \(N^3\Delta=2G\)，且 \(\operatorname{im}N^3=\mathbf QG\)。\(U\) symplectic，使 \(N^3\) skew-adjoint；其 kernel 为 \(G^\perp\)。用 \(\Delta\cdot G=8\) 决定系数，得到全部向量上的恒等式
\[
N^3z=\frac{z\cdot G}{4}\,G.
\tag{B7.2}
\]
写 \(G=d\gamma\)，其中 \(\gamma\) 为 \(\Lambda\) 中 primitive 向量。unimodularity 使某个整数 \(z\) 满足 \(z\cdot\gamma=1\)；(B7.2) 及 \(N^3z\in\Lambda\) 强迫 \(d^2/4\in\mathbf Z\)。所以 \(d\) 为偶数。又 \(d\mid8\)，故
\[
d\in\{2,4,8\},\qquad G\in2\Lambda.
\tag{B7.3}
\]
不声称精确 divisibility 或 \(\gamma=G/2\) primitive。

修正 lift 的归一化平移是 \(u=G/8\)。改变 splitting 后
\[
c_\gamma^{\rm corr}=c_\gamma+(M_\gamma-1)u.
\tag{B7.4}
\]
因为 \(M_0G=-G\)、\(M_1G=G-8\Delta\)，
\[
c_0^{\rm corr}=-G/4,\qquad c_1^{\rm corr}=0.
\tag{B7.5}
\]
因此 cochain \(u\) 的安全整数成本为 \(4\)，两生成回路 cocycle 的安全成本为 \(2\)。所有回路延拓继承同一成本。也可直接取稳定整数子格
\[
\Lambda+\mathbf Z(4e_{\rm corr}),\qquad
4e_{\rm corr}=4e_c+G/2
\tag{B7.6}
\]
置于 centered \(E_B\) 内，quotient 的 index 为 \(4\)。这不是最小 index 的证明。原点最高 log 旗标也不会读出该 mark translation，因为 \(NG=0\)。

还有两个安全 divisibility 补强。若 \(\Delta=d_\delta\delta_0\)，\(U\) 为整数 automorphism，故 \(d_\delta^2\mid\Delta\cdot U\Delta=8\)，于是 \(d_\delta\in\{1,2\}\)。若 \(d_\delta=2\)，由 \(\Delta\cdot G=8\) 进一步得 \(d\in\{2,4\}\)。剩余 real cycle 投影为
\[
\alpha=(-3+4U-U^2)\Delta=2(U-1)\Delta-(U-1)^2\Delta.
\tag{B7.7}
\]
在 \(\Lambda/2\Lambda\) 中，\(\Delta\) 的全部 \(U\)-orbit span 为 isotropic，因 (B6.1) 全部交点被 \(8\) 整除；四维 symplectic 空间中的 isotropic span 维数至多 \(2\)。它是 \(U\)-stable，而 \(U\) 在特征 \(2\) 仍 unipotent，故 \((U-1)^2\Delta=0\pmod2\)。于是 \(\alpha\in2\Lambda\)。由 (B6.1) 直接得到 \(\alpha\cdot U\alpha=-64\)，同一平方整除论证给 \(\operatorname{div}(\alpha)\in\{2,4,8\}\)。这些只是上界与可能值，不宣布 actual primitive generator。

## B8. rank-five origin 的 CRT 多项式

记 \(A=T_0-1\)。最小多项式为
\[
m_5(z)=(z-1)^4(z+1).
\]
投到 \(+1\) generalized eigenspace 的唯一 degree-less-than-five 有理 CRT 多项式为
\[
p_{5,+}=1-\frac{(T_0-1)^4}{16}.
\tag{B8.1}
\]
没有整数系数多项式能表示这组 universal CRT 条件：任何 \(P\in\mathbf Z[z]\) 都有 \(P(1)\equiv P(-1)\pmod2\)，而所需值为 \(1,0\)。且单首最小多项式约化后 (B8.1) 的最高次系数为 \(-1/16\)，故通用多项式成本 \(16\) 精确。

正块上 \(N_0=\log T_0\)，负块由 projector 去掉。由 \(A^4(A+2)=0\)，\(A^7=-8A^4\)，
\[
N_0^3p_{5,+}
=A^3p_{5,+}
=A^3+\tfrac12A^4
=\tfrac12(T_0-1)^3(T_0+1).
\tag{B8.2}
\]
其通用多项式成本精确为 \(2\)。

但是在 actual centered 格 (B5.2) 上
\[
p_{5,+}(z,n)=(z,0),\qquad
N_0^3p_{5,+}(z,n)=((U-1)^3z,0)
\tag{B8.3}
\]
都是整数算子。整数算子不等于整数系数多项式，这是 actual splitting 带来的额外信息。\(p_{5,+}\) 不与 conifold action 交换，故不是整个基底上的平坦 projector，也不能当作全局代数 gauge。若以 \(e_{\rm corr}\) 为源，则 \(p_{5,+}e_{\rm corr}=G/8\) 的成本至多 \(4\)，而 \(N_0^3p_{5,+}e_{\rm corr}=0\)。

## B9. rank-nine exterior 的 actual 整格

对 B5 的扩张取 \(\wedge^3\)。商 \(E_5/\Lambda=\chi\) 给 canonical map
\[
\wedge^3E_{5,\mathbf Z}\longrightarrow
\chi\otimes\wedge^2\Lambda\longrightarrow\chi ,
\tag{B9.1}
\]
末箭头为交错 pairing。因 \(\Lambda\) unimodular，该箭头整系数 surjective。其 kernel \(W_{9,\mathbf Z}\) 是饱和 rank-nine 整格。中心化 origin splitting 下
\[
W_{9,\mathbf Z}
=\wedge^3\Lambda\oplus
e_c\wedge\wedge^2_0\Lambda.
\tag{B9.2}
\]
这与冻结 endpoint packet 的 primitive rank-nine 系统相同。

origin 的两个块分别为 \(J_4(+1)\)、\(J_5(-1)\)。后者可直接核：在一个 \(N e_j=e_{j-1}\) 的 rational Jordan 基底中，
\[
N^4(e_3\wedge e_2)=2e_1\wedge e_0\ne0,\qquad N^5=0
\]
于 primitive 五维分量；故确为一个 \(J_5\)。最小多项式为
\[
m_9(z)=(z-1)^4(z+1)^5.
\tag{B9.3}
\]

## B10. rank-nine 的完整 CRT 与最高 log 旗标

令 \(u=z+1\)。\((z-1)^{-4}=(u-2)^{-4}\) 在 \(u=0\) 的前五项为
\[
\frac{16+32u+40u^2+40u^3+35u^4}{256}.
\]
因此
\[
p_{9,+}=1-\frac{(T_9-1)^4}{256}
\left[16+32(T_9+1)+40(T_9+1)^2+
40(T_9+1)^3+35(T_9+1)^4\right].
\tag{B10.1}
\]
其通用 CRT 成本精确为 \(256\)：约化后的 degree-eight 最高系数为 \(-35/256\)。同样，
\[
F_9:=N_0^3p_{9,+}
=\frac{(T_9-1)^3(T_9+1)^5}{32}.
\tag{B10.2}
\]
右式在负块为零；在正块 \(T_9+1=2+(T_9-1)\)，乘 \( (T_9-1)^3\) 后只有常数项 \(32\) 留下。其 degree-eight 最高系数为 \(1/32\)，故通用多项式成本 \(32\) 精确。

在 actual 格 (B9.2) 上，(B10.1) 就是投到 \(\wedge^3\Lambda\) 的整数 projection，(B10.2) 在该块是整数 \((T_9-1)^3\)，在其余块为零。因此它们的 actual operator 成本为 \(1\)。symplectic contraction
\[
\wedge^3\Lambda\longrightarrow\Lambda
\tag{B10.3}
\]
也是整数 isomorphism：在任意 unimodular symplectic 基底上，其矩阵为 signed permutation。由此最高 log 旗标有真实 Betti 整数含义，无需将 Frobenius 对数系数或 \(\pi\) 归一化冒认为整数格。

## B11. 真实端点识别与仍缺的比较

冻结 endpoint proof 已给所选 analytic packet
\[
\Phi(q)=Y_{h+qg_0}\wedge Y_{g_1}\wedge Y_{g_2}
=\Phi_h+q\Phi_0,
\qquad \Phi_0=Y_{g_0}\wedge Y_{g_1}\wedge Y_{g_2}
\]
其中 \(h\) 为零初值 particular，\(g_0,g_1,g_2\) 是前三个 conifold Taylor 初值分别为单位向量的指定 holomorphic homogeneous solutions；\(g_0\) 不是 vanishing solution，真实 vanishing 解为 \(v=g_1+\tfrac34g_2\)。actual 标记有
\[
\Psi=h+\alpha_0g_0+\alpha_1g_1+\alpha_2g_2,
\quad
\Phi(q)=Y_\Psi\wedge Y_{g_1}\wedge Y_{g_2}
+(q-\alpha_0)\Phi_0.
\]
其精确端点识别为
\[
N_0^3p_+\Phi(q)=0\quad\Longleftrightarrow\quad q=\alpha_0.
\tag{B11.1}
\]
B10 使这里的 \(p_+\)、最高 log 算子成为 actual Betti 整数算子。不过 analytic \(g_0,g_1,g_2\) 的 rational Taylor normalization 并未自动给出相同归一化下的平坦 Betti \(\mathbf Q\) 或整数坐标；尤其 \(g_1,g_2\) 当前只已在 \(\Lambda\otimes\mathbf C\) 中识别。故以下推论仍不成立：

- 不可把 \(\Phi\) 的九条 analytic 行直接标记为 \(\overline{\mathbf Q}\)-Betti 整格。
- 不可用 B10 删除 D7 的完整前缀算术假设或 local filling 代价。
- 不可仅凭 integer monodromy 宣称 \(C=1\)、free Taylor integrality 或 CDT 的足够端点容量。

实际进展是：最高 log 条件的几何/Betti 一半已得到具体格和精确 CRT，而非 transcendent gauge；剩余是所选 Taylor 列到该格的算术比较及有效估计。

修订登记：未冻结快照 SHA \(\texttt{6e58db381dca549e7a60e4b69f293fb11b943eff0f2290bce1c7a6f3a005dd6d}\) 的 B11 曾误写以 \(y_0\) wedge 作为 q 平移。根独审指出该项的 contraction 被 \(N_0^3\) 杀掉，不能识别 \(\alpha_0\)。本版改回冻结 E10–E11 的 \(g_0\) 家族；B2–B10 的整格、cocycle、CRT 结论未变。未对任何 frozen 稿作修改。

## B12. rational \(\Xi\)、torsion 与安全有限成本

由 rational higher-Chow class 的定义，存在某个有限整数 \(N>0\)，使 \(N\Xi\) 来自整系数 higher-Chow class。该存在性没有给出 \(N\) 的值。KLM PDF13 §5.6 明确说明：integral topological class 可以是 torsion；要使用普通整 AJ target，还须杀掉该 topological torsion。光滑 proper family 的 free/torsion Betti 群为局部常值，故其 torsion exponent 有固定有限上界。乘这个 exponent 后可在相应整 homologically-trivial target 中工作；它仍未提供一个计算出的统一 completion 成本。

即使不选 integral completion，只要 actual rational cocycle 在固定有限 rank 的 free \(H^3(X,\mathbf Z)\) 上定义，两条生成回路具有某个共同分母 \(D\)。由 (B3.3) 和整数 monodromy，所有 word 的 cocycle 都在 \(D^{-1}H^3(X,\mathbf Z)\) 中；\(D\) 不随 word-length 增长。这是全 \(H^3\) 的最安全有限存在界。B4–B7 在指定四维分量将它强化为具体 centered 成本 \(1\)、corrected cocycle 成本至多 \(2\)、corrected source mark 至多 \(4\)。

\(\{-1\}\) 的二阶 torsion 只解释 unit centering 的 rational Chow equality，以及相应 open rational Tate 改变量。它不证明所有 boundary completion 障碍只有二阶：rational target 的零群不控制其整系数 torsion exponent。作为逻辑说明，整数映射 \(n\mathbf Z\hookrightarrow\mathbf Z\) 的 rational cokernel 总为零，其 integral cokernel 可为任意 \(\mathbf Z/n\)。没有声称本例实际出现任意奇 torsion；只是不得从 rational vanishing 推出 completion 分母 \(2\)。

## B13. integer monodromy 与 arithmetic germ 的严格区别

一个 constant normal function \(z\in\mathbf C/\mathbf Z\) 有零、因此整数 cocycle，初值 \(z\) 却可任意。故 integer Betti extension 本身不约束 analytic initial value 的代数性。更贴近本例，冻结 real Betti proof 已给合法 integral period 平移改变 origin 的某个 \(\pi^2/4\) 对数系数而保留 conifold vanishing normalization。这里中心化全 current 与 \(\Gamma/8\) 已实际选定该自由度；仍需真实 Taylor/Betti 比较才能满足 CDT。

因此本稿既不把固定标量 \(\Psi\) 的 exact equality 撤回为未知 homogeneous difference，也不将新整格结果提升成目标常数的无理性或线性无关性定理。

## B14. 来源与实际阅读范围

冻结本地数学输入：

- `cdt_odd_R0_positive_cut_boundary_flux_20261006.md`：SHA256 `3fabdbfa3f4c0fd17e50db268b86cfe8c7d752f71a462bcdf0ebaeb1faa3d150`。
- `cdt_odd_R0_Yukawa_scalar_interface_20261006.md`：SHA256 `172a0830a547fd3d018953ca996ca6c5d2d67ace172a9943acee6c1cc9044b15`；本轮实际全文读。
- `cdt_odd_R0_real_Betti_normalization_20261006.md`：SHA256 `dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f`；上一轮实际全文独审，使用一般平移、PL 标度及合法 period 平移。
- `cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md`：SHA256 `b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef`；上一轮实际全文独审，使用 actual rank、Jordan 类型与端点识别。
- `cdt_odd_R0_kummer_period_interface_20261006.md`：SHA256 `803b3eced9825fe5f40005728430188e36c4a8cd123d41223972cceb23c2e172`；实际全文读过，用 origin canonical \(W=\sqrt x B\)。
- `cdt_odd_R0_regulator_derivative_20261006.md`：SHA256 `5a3ba4ed679a5565375efdb0b9c39e4a69338e72bcce5938b5a34356d816e091`。

Primary：

- Kerr–Lewis–Müller-Stach, *The Abel–Jacobi map for higher Chow groups*, published primary，`literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf`，SHA256 `8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9`。本轮实际读 PDF12–14，特别 §5.6 整/有理 AJ、torsion topological class、\(p=n=4\) current 与 membrane 系数；既有轮实际读其它 current 页，见冻结 receipt。
- Bönisch–Klemm–Scheidegger–Zagier 原件，`literature/bonisch_klemm_scheidegger_zagier_alternate_author_url_20261006.pdf`，SHA256 `f124aab462ae953eff9a2c9df28cff63e1b63adad792a572a1c608226fdfac83`；已实际读 PDF6–7、12、19 等，提供 mirror compact 四维周期空间。两条 degree-one maps 的实际构造与 projector 全证明以冻结 Y8–Y10 为输入。
- Movasati 原件 SHA256 `69830ec409ccd1172f1ec348dad2f6bed59fe4f18342c1a4fab37b0659c85182`，已实际读 PDF93–95 的 Picard–Lefschetz 中间维 sign；不以三维 fibre 的名称误设公式中 total dimension \(n\)。

B2、B4–B10 是本轮纸面全尺度推导；无数值 producer、有限采样或 symbolic verifier 执行。同行新的 orbit 稿尚待独立全文审阅，未将它冒列为已读 input。

