# 同一 excellent quotient 的 generic 平方提升不能延伸到 modp³

日期：2026-10-06。本文新建，不改此前冻结报告。主结论涉及当前 level20 的**同一个完整 excellent quotient** \(G_p\)：其 generic Hasse 双根平方可以提升到 modp²，但不能整体提升到 modp³，若平方因子仍是原 generic 因子的同次数 monic 提升。§5另给所有 \(W\) 的全形式 order≤2 行的 primitive 层数上限。两者都不是任意第三层或第四层 Smith 方向的排除，也不涉及有限 jet 的最优性。

## 1. 已证输入与命题范围

使用 [完整 Frobenius 稿](cdt_odd_level20_frobenius_20261006.md) 的全形式比值、[自然第三层稿](cdt_odd_level20_third_layer_20261006.md) §§1、4 的曲率恒等式，以及 [平方提升稿](cdt_odd_level20_square_lift_20261006.md) 的 Hasse 因子。取好素数 \(p\ge7\)，系数环为 \(O=O_{K,\mathfrak p}\)，\(K=\mathbf Q(\sqrt5)\)，或其完成。此处 \(p\) 是 uniformizer，固定规范的坏素数按原稿排除。以下完整多项式与形式级数都在 \(O\) 上；没有把 target 的 \(n<p^2\) 截断关系外推成全多项式关系。

令 \(\vartheta=t\,d/dt\)，

\[
\Delta=1-12t+28t^2-32t^3+16t^4,
\quad g_s=(1-t)\sqrt\Delta,
\quad D_s=g_s^2=(1-t)^2\Delta.
\]

沿原点规范分支设

\[
s=t(q(t)^p),\quad S=g_s\Phi,\quad b=S(s)/S(t),
\quad\Phi/\Phi(s)\equiv G_p\pmod{p^3}.
\tag{1}
\]

这里 \(G_p\in O[t]\) 是完整 norm 多项式，\(G_p(0)\equiv1\pmod p\)，且 \(\deg G_p\le3p\)。原点的 \(g_s,\Phi,S,b,G_p\) 全部是 unit；\(s=t^p\cdot\text{unit}\)，且 \(s\equiv t^p\pmod p\)。最后一式来自整数互逆芽 \(q(t),t(q)\) 的 Frobenius 关系。

记 \(P=G_p\bmod p\)。已证 Hasse 除子给

\[
P=B H^2,\qquad H\text{ monic、squarefree},\quad B\mid\Delta,
\quad 2\deg H+\deg B=3(p-1),\quad\deg B\le4.
\tag{2}
\]

待排除的提升严格指：存在 \(\beta,\eta\in O[t]\)，其中 \(\eta\) monic、\(\deg\eta=\deg H\)、\(\eta\bmod p=H\)，使

\[
G_p\equiv\beta\eta^2\pmod{p^3}.
\tag{3}
\]

无需对 \(\deg\beta\) 加界，也不要求 \(\beta\) 的提升仍整除 \(\Delta\)。改变 \(G_p\) 的 modp³ 类、允许不同次数的非 monic 因子、换用另一个函数或仅要求有限前缀的方案，不在命题内。

## 2. 曲率清分母得到一个非零全多项式余项

置

\[
h=\vartheta\log g_s=-\frac{t}{1-t}+\frac{t\Delta'}{2\Delta},
\quad q_{\rm proj}=t^2Q(t),
\quad\mathcal T=4q_{\rm proj}+2\vartheta h+h^2.
\]

已有完整模型的明确恒等式为

\[
\mathcal T=
\frac{-8t(18t^4-36t^3+28t^2-10t+1)}{(1-t)\Delta}.
\]

因此

\[
\boxed{M=D_s\mathcal T=-8t(1-t)(18t^4-36t^3+28t^2-10t+1)}
\tag{4}
\]

是次数6的多项式，其展开为

\[
M=-8t+88t^2-304t^3+512t^4-432t^5+144t^6.
\]

定义对任意 \(U\in O[t]\) 的清分母曲率多项式

\[
\boxed{\mathcal R_{D_s}(U)=
D_s\{2U\vartheta^2U-(\vartheta U)^2\}
 +2D_s h\,U\vartheta U+M U^2.}
\tag{5}
\]

\(D_sh\in\mathbf Z[1/2][t]\)，所以 (5) 确为 \(O[t]\) 中的多项式。若 \(U\) 是原点 unit，置 \(z=h+\vartheta\log U\)，直接展开给

\[
\mathcal R_{D_s}(U)=D_sU^2\{2\vartheta z+z^2+4q_{\rm proj}\}.
\tag{6}
\]

对 \(U=G_p\)，[自然第三层稿](cdt_odd_level20_third_layer_20261006.md) (3) 的全形式曲率关系是

\[
F:=2\vartheta z+z^2+4q_{\rm proj}
\equiv p^2b^2\mathcal T(s)\pmod{p^3}.
\tag{7}
\]

这只用完整 excellent quotient、Riccati 恒等式及真实 Frobenius lift，未用截断的 \(W\) 或未知目标的数值。

由 (1) 的 unit 除法，

\[
b=\frac{g_s(s)\Phi(s)}{g_s\Phi}
\equiv\frac{g_s(s)}{g_sG_p}\pmod{p^3},
\qquad D_sG_p^2b^2\equiv D_s(s)\pmod{p^3}.
\tag{8}
\]

将 (7)、(8) 代入 (6)：

\[
\mathcal R_{D_s}(G_p)
\equiv p^2D_s(s)\mathcal T(s)=p^2M(s)
\equiv\boxed{p^2M(t)^p}\pmod{p^3}.
\tag{9}
\]

末步只需 modp：\(s\equiv t^p\)，且 \(M\) 的整数系数在 characteristic \(p\) 下满足 \(M(t^p)=M(t)^p\)。两边均为多项式；在 \(O[[t]]\) 中得到的同余逐系数就是 \(O[t]\) 的同余。(9) 因而是全多项式关系，而非根处有限 jet 的猜测。

## 3. 任何平方型都迫使曲率含三次因子

对任意 \(\beta,\eta\in O[t]\)，代入 \(U=\beta\eta^2\)，直接 Leibniz 展开得到

\[
2U\vartheta^2U-(\vartheta U)^2
=\eta^3\{\eta(2\beta\vartheta^2\beta-(\vartheta\beta)^2)
 +4\beta\vartheta\beta\,\vartheta\eta
 +4\beta^2\vartheta^2\eta\}.
\]

另两个项 \(2D_sh\,U\vartheta U\)、\(MU^2\) 也含 \(\eta^3\)。所以精确地

\[
\boxed{\mathcal R_{D_s}(\beta\eta^2)\in(\eta^3)\subset O[t].}
\tag{10}
\]

这对任意 \(\beta\) 成立，不依赖 Hasse 分支因子的提升位置。

## 4. monic 理想的 p-saturation 与次数矛盾

若 (3) 成立，\(\vartheta\) 保持 \(p^3O[t]\)，(5) 的多项式运算给

\[
\mathcal R_{D_s}(G_p)\in(\eta^3)+p^3O[t].
\]

结合 (9)，得到 \(p^2M(t)^p\in(\eta^3)+p^3O[t]\)。因为 \(\eta\) monic，商环

\[
Q=O[t]/(\eta^3)
\]

作为 \(O\)-模自由，基可取 \(1,t,\ldots,t^{3\deg H-1}\)。在此自由模中 \(p^2x\in p^3Q\) 蕴含 \(x\in pQ\)；这是本处需要的 p-saturation，不能在未经验证的商环内直接除 \(p^2\)。因此

\[
M(t)^p\in(\eta^3)+pO[t],\qquad
\boxed{H^3\mid M(t)^p\quad\text{in }k[t].}
\tag{11}
\]

\(H\) squarefree，故 (11) 蕴含 \(H\mid M\)。更具体地，在代数闭包中每个 \(H\) 根都必须是 \(M\) 根；当 \(p\ge3\)，反向的重数条件也成立，但此处只需必要方向。

另一方面，由 (2)，

\[
\deg H=\frac{3(p-1)-\deg B}{2}
\ge\frac{3p-7}{2}\ge7>6=\deg M\quad(p\ge7).
\tag{12}
\]

\(M\bmod p\) 的最高系数144对 \(p\ge7\) 非零。因此 \(H\mid M\) 与 (12) 矛盾，(3) 不存在。

## 5. 通用全形式 order≤2 行不能有 primitive S3 或 S4

这个辅助结论与 (3) 的平方因子假设不同，需分别使用其限定条件。取任意 \(\mathscr A\in O[[t]]^\times\)，沿同一个真实 lift 令 \(u=\vartheta\log s=pb\)，其中 \(b\in O[[t]]^\times\)、\(b(0)=1\)。设

\[
L=c_2(t)\vartheta^2+c_1(t)\vartheta+c_0(t),\quad c_i\in O[t],
\]

并要求对每个 zero-constant \(W(z)\in O[[z]]\)，有完整形式级数 \(L[\mathscr A W(s)]\in p^\ell O[[t]]\)。这里只讨论 \(\ell\ge3\)、\(p\ge7\)。令 \(\rho=\vartheta\log\mathscr A\)、\(\zeta=\vartheta\log b\)，它们都是 integral 形式级数。直接测试 \(W=z,z^2,z^3\)：

\[
C_j:=\frac{L(\mathscr A s^j)}{\mathscr A s^j}
=P_0+jP_1+j^2P_2\quad(j=1,2,3),
\]

\[
P_0=c_0+c_1\rho+c_2(\vartheta\rho+\rho^2),
\quad P_1=u\{c_1+c_2(2\rho+\zeta)\},
\quad P_2=c_2u^2.
\tag{13}
\]

除去 \(\mathscr A s^j\) 不损失 p 整除性：\(\mathscr A\) 是 unit，而 \(s=t^p\cdot\text{unit}\)，故其幂的乘法在 \(O[[t]]/p^\ell\) 中是 injective。于是三个 \(C_j\in p^\ell O[[t]]\)。二阶差给

\[
2P_2=C_3-2C_2+C_1\in p^\ell O[[t]].
\]

因为2与 \(b\) 是 unit，得到 \(c_2\in p^{\ell-2}O[t]\)。再由 \(P_1=C_2-C_1-3P_2\in p^\ell O[[t]]\)，除 \(u=pb\) 后推出

\[
c_1+c_2(2\rho+\zeta)\in p^{\ell-1}O[[t]],
\quad c_1\in p^{\ell-2}O[t].
\]

最后 \(P_0=C_1-P_1-P_2\in p^\ell O[[t]]\)，给 \(c_0\in p^{\ell-2}O[t]\)。因此

\[
\boxed{\min_i v_p(c_i)\ge\ell-2;\quad
\ell\ge3\text{ 时不存在 primitive 的通用 order≤2 行。}}
\tag{14}
\]

特别是通用 S3、S4 行除去其强制公共 content 后最多仍提供两层。这证明只用了三个实际测试芽，没有依赖常数 \(W\)。它不排除对一个实际 Eichler packet 的特殊消除、不排除加入新的实际独立函数后出现 order3 行，也不排除有限 leading jets 中的同余。

## 6. 对继续研究的精确含义

已证 modp² generic 平方提升保持有效；新的障碍只说明，不能对同一个 \(G_p\) 把该平方因子再整体抬高一层，然后据此宣称更高 Smith 阈值。曲率的余项 \(p^2M(t)^p\) 已是实际非零输入。它不排除利用余项构造一个不同的、原格中 primitive 的 S3/S4 行，不排除 special Eichler packet、finite leading jets、多个 packet 或新的张量构造。

[最小 symbolic 核验脚本](cdt_odd_level20_squarelift_modp3_obstruction_20261006_verify.py) 与 [证书](cdt_odd_level20_squarelift_modp3_obstruction_20261006_verify.json) 只核 (4)、(6)、(10)、(13) 的有理代数恒等式、次数与系数；未计算未知周期、未扫描素数，也未重跑任何冻结 producer。全素数同余 (9)、商模的 p-saturation 与两个限定排除由上面的证明给出。
