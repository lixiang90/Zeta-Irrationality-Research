# Catalan 真实参数种子的每阶关系与二阶完整重写

2026-10-07。已收到 root 的独立全文数学审查 PASS。用户请求优先处理原仓库同步时，将已经完成的数学推导保存于此；没有继续扩大算例或修改旧笔记。

本稿在同一实际积分内证明新的函数关系，消去一个完整 Z 种子函数，准确识别全部十五个零、一、二阶 seed 值，并将任意二阶 M/Z 矩归入一个十五项的实际周期生成系统。不是数值线性无关性定理，也没有宣称 full pool 投影已成功。

## 1. 实际对象、端点与 Hasse 约定

令 \(f(t)=\sqrt{1-t^2}\)、\(a(t)=\operatorname{artanh}t\)。沿用已经证明的实际积分

\[
M_z(i,j)=\int_{-1}^1\!\int_0^1
\frac{|t|t^is^je^{za(t)}}{f(t)(1-ts)}\,ds\,dt,
\qquad
Z_z(i,j)=\int_0^1\!\int_0^1
\frac{t^is^je^{za(t)}}{1-ts}\,ds\,dt.
\tag{R1}
\]

定义 \(T=M_z(0,0),U=M_z(0,1),V=Z_z(0,0),W=Z_z(1,0),X=Z_z(0,1)\)，并写 \(Y_k=[z^k]Y(z)=Y^{(k)}(0)/k!\)。所有 M 种子在 \(|\Re z|<1\) 内全纯；所有 Z 种子实际在 \(\Re z<2\) 内全纯。端点 \(u=a(t)\to\infty\) 后由固定多项式乘 \(e^{-(1-|\Re z|)u}\) 或 \(e^{-(2-\Re z)u}\) 支配，任意固定阶参数微分合法。对二阶 outer-log，真实矩仍是 \(M^{(2)}=M_{z,2}/3\)、\(Z^{(2)}=Z_{z,2}/3\)，不得遗漏这个 3。

已知外矩的完整起点为

\[
A_0(z)=\int_0^\infty e^{zu}\operatorname{sech}u\,du
=2\sum_{k\ge0}\beta(k+1)z^k,
\]
\[
B_0(z)=\int_0^\infty e^{zu}\operatorname{sech}^2u\,du
=1+\sum_{k\ge1}2^{1-k}\eta(k)z^k.
\tag{R2}
\]

这里 \(\eta(1)=\log2\)，\(B_{0,2}=\zeta(2)/4\)，\(B_{0,3}=3\zeta(3)/16\)。实区间上的 log 都取通常实值，参数指数用这些固定实 log 定义；没有复 log 分支选择的歧义。

## 2. 一个每阶成立的真实 Z 消元身份

置 \(L(t)=-\log(1-t)\)。直接先积掉 s 得

\[
V=\int_0^1e^{za}L/t\,dt,\quad
W=\int_0^1e^{za}L\,dt,\quad
X=\int_0^1e^{za}(L/t^2-1/t)\,dt.
\tag{R3}
\]

对 \(E(t)=(1/t-t)e^{za(t)}L(t)\) 求导：

\[
E'(t)=e^{za(t)}\left(-L/t^2-L+zL/t+(1+t)/t\right).
\]

在 \(t\to0\) 时 \(E\to1\)；在 \(t\to1\) 时 \(E\to0\)，后者对 \(\Re z<2\) 成立。R3 的合并 integrand 在0也可积，不能将其中单独的 \(1/t\) 发散项另积分。因此

\[
\boxed{X(z)+W(z)=zV(z)+B_0(z)+1}\qquad(\Re z<2).
\tag{R4}
\]

由全纯性，对每个 \(k\ge0\)，

\[
X_k+W_k=V_{k-1}+B_{0,k}+\delta_{k0},\qquad V_{-1}=0.
\tag{R5}
\]

这实际消去完整 X 函数，可逐阶代入完整 H14/H20；没有假定任何周期数值独立。

## 3. U 的全部奇阶，以及 U 偶部与 T 奇部的同一函数

配对 \(\pm t\)、令 \(t=\tanh u\)，得到

\[
U(z)=2\int_0^\infty
\frac{(u-\tanh u)\sinh(zu)+\log\cosh u\cosh(zu)}{\sinh u}\,du,
\]
\[
T(z)=2\int_0^\infty
\frac{u\cosh(zu)+\log\cosh u\sinh(zu)}{\cosh u}\,du,
\qquad
V(z)=2\int_0^\infty
\frac{e^{zu}(u+\log\cosh u)}{\sinh2u}\,du.
\tag{R6}
\]

它们在相应 common strip 绝对收敛。对每个奇数 \(k\ge1\)，分开两个收敛的 log moments，并使用几何级数，给

\[
\boxed{U_k=4(k+1)(1-2^{-k-2})\zeta(k+2)-4\beta(k+1).}
\tag{R7}
\]

具体是 \(U_1=7\zeta(3)-4G\)。Teven 仍为

\[
T_{\rm even}(z)=A_0'(z)+A_0'(-z),
\quad T_{2j}=4(2j+1)\beta(2j+2).
\tag{R8}
\]

定义一个已知单参数 trigamma 项和一个共同实际函数

\[
R(z)=2\int_0^\infty\frac{ue^{zu}}{\sinh2u}\,du
=4\sum_{m\ge0}(4m+2-z)^{-2}
=\frac14\psi'((2-z)/4),
\]
\[
S(z)=V(z)-R(z)=2\int_0^\infty
\frac{e^{zu}\log\cosh u}{\sinh2u}\,du\qquad(\Re z<2).
\tag{R9}
\]

因为 \((e^u+e^{-u})/\sinh2u=1/\sinh u\) 及 \((e^u-e^{-u})/\sinh2u=1/\cosh u\)，在 \(|\Re z|<1\) 内

\[
\boxed{U_{\rm even}(z)=\tfrac12\bigl(S(z+1)+S(z-1)+S(1-z)+S(-1-z)\bigr),}
\]
\[
\boxed{T_{\rm odd}(z)=\tfrac12\bigl(S(z+1)-S(z-1)-S(1-z)+S(-1-z)\bigr).}
\tag{R10}
\]

故每阶 U 偶 jet 和 T 奇 jet 是同一 S 在参数中心 \(\pm1\) 的导数和/差。这里两个 shifted centers 都仍在实际收敛域内。它是一条准确的函数合并身份；不能把 \(\pm1\) 的导数自动当作0中心有限 jet 的有理组合，也未证明 S 的 Taylor 系数为有理数。

R9 使用的 trigamma 级数实际核于 [NIST DLMF 5.15.1](https://dlmf.nist.gov/5.15.E1)；积分到级数本身亦由非负几何展开直接证明。

## 4. W 的全部偶阶与二阶 Z 种子闭式

对 \(|\Re z|<2\)，完整区间 beta 积分给

\[
C(z):=B_0(z)+B_0(-z)
=2B(1+z/2,1-z/2)=\frac{\pi z}{\sin(\pi z/2)},
\]
\[
D(z):=\int_{-1}^1e^{za(t)}[-\log(1-t)]\,dt
=C(z)\bigl(\psi(2)-\log2-\psi(1-z/2)\bigr).
\tag{R11}
\]

第一式用变量 \(x=(1+t)/2\)；第二式对 beta 的第二参数微分，保持第一个参数不变。Euler beta/gamma 身份实际核于 [DLMF 5.12.1](https://dlmf.nist.gov/5.12.E1)，reflection 与 recurrence 核于 [DLMF 5.5](https://dlmf.nist.gov/5.5)。参数微分由同一端点可积 log 支配合法。

在负半区间以 \(t=-s\) 代换，\(-\log(1+s)=L(s)-2a(s)\)，所以

\[
D(z)=W(z)+W(-z)-2B_0'(-z).
\tag{R12}
\]

取 R12 的偶部，再用 \(\psi(1+w)\) 的局部级数（实际核 [DLMF 5.7.4](https://dlmf.nist.gov/5.7.E4)），得到整个 \(|z|<2\) 的准确 jet identity

\[
\boxed{W(z)+W(-z)=B_0'(z)+B_0'(-z)
+C(z)\left(1-\log2+\sum_{j\ge1}\zeta(2j+1)(z/2)^{2j}\right).}
\tag{R13}
\]

因此全部 W 偶 jets 可用已知 zeta/log 周期表达。特别 \(C_0=2,C_2=\zeta(2)/2\)，从 R13 得

\[
W_0=1,\qquad W_2=\frac{13}{16}\zeta(3)+\frac14\zeta(2)(1-\log2).
\tag{R14}
\]

为识别余下的一阶值，这里给实 log/polylog 的自含推导。记 \(l=\log2\)，\(b(t)=\log(1+t)\)。直接积掉 s 后

\[
W_1=\tfrac12\int_0^1(Lb+L^2)dt
=l+\operatorname{Li}_2(1/2)=l+\tfrac12\zeta(2)-\tfrac12l^2.
\tag{R15}
\]

其中 \(\int L^2dt=2\)、\(\int Lb\,dt=2l+2\operatorname{Li}_2(1/2)-2\)，可对 \(\log(2-y)\) 分部积分或用绝对收敛级数直接取得。

另外

\[
V_1=\tfrac12\int_0^1(Lb+L^2)\,dt/t.
\]

令 \(J=\int_0^1\log^2(1+t)dt/t\)。因为 \(\log(1-t^2)=-L+b\)，平方后积分得 \(\int Lb\,dt/t=\zeta(3)/2+J/2\)；这里 \(\int L^2dt/t=2\zeta(3)\)，可用 beta 的二阶导数在 removable 参数0取极限证明。再令 \(u=1/(1+t)\)，分部积分给

\[
J=2\zeta(3)-\tfrac23l^3-2l\operatorname{Li}_2(1/2)-2\operatorname{Li}_3(1/2)=\tfrac14\zeta(3).
\tag{R16}
\]

所用两个 half-values 不以数值拟合取得：dilog 的 reflection identity 由微分及0端点证明；trilog 身份对 \(0<x\le1/2\) 微分验证为

\[
\operatorname{Li}_3(x)+\operatorname{Li}_3(-x/(1-x))+\operatorname{Li}_3(1-x)
=\zeta(3)+\zeta(2)\log(1-x)
-\tfrac12\log x\log^2(1-x)+\tfrac16\log^3(1-x).
\tag{R17}
\]

证明只用 \(\operatorname{Li}_2(-x/(1-x))=-\operatorname{Li}_2(x)-\tfrac12\log^2(1-x)\) 和 dilog reflection，这两式也由微分与0端点得到。令 \(x=1/2\)，再用 \(\operatorname{Li}_3(-1)=-3\zeta(3)/4\)，得 \(\operatorname{Li}_3(1/2)=7\zeta(3)/8-\zeta(2)l/2+l^3/6\)。所以

\[
\boxed{V_1=\frac{21}{16}\zeta(3),\quad
X_1=\frac12\zeta(2)+\frac12l^2,\quad
X_2=\frac12\zeta(3)+\frac14\zeta(2)l.}
\tag{R18}
\]

后两项直接来自每阶 R5，而非另猜 Z 值。全部显示的实积分在0、1绝对收敛；half-value 推导只在实区间作，故不会掩盖多对数复分支修正。

## 5. 未匿名化的 level-four/level-two 实际生成元

定义 \(\mathcal L_{p,1}(z,w)=\sum_{n>k\ge1}z^nw^k/(n^pk)\)，本节 \(p=2,3\)，参数全在单位圆上。因 \(\sum H_{n-1}/n^p<\infty\)，这里的值全部绝对收敛。沿用已审 boundary 稿的准确约定

\[
\mathcal A=\Re(\mathcal L_{3,1}(1,i)-\mathcal L_{3,1}(-1,i)),
\qquad \mathcal B=\mathcal L_{3,1}(1,-1)-\mathcal L_{3,1}(-1,1),
\]
\[
\mathcal C=-\Im(\mathcal L_{2,1}(i,1)+\mathcal L_{2,1}(i,-1)).
\tag{R19}
\]

R6 与 \(x=e^{-u}\) 给

\[
\boxed{U_2=\frac{45}{4}\zeta(4)-\frac72\zeta(3)l-4\mathcal A,
\qquad V_2=\frac{45}{32}\zeta(4)-\frac7{16}\zeta(3)l-\frac14\mathcal B.}
\tag{R20}
\]

这也可由已审 O7–O10 单独读出：U2 的 log(1+x²) 部分是 \(4\mathcal S_U=-4\mathcal A\)，V2 的部分是 \(4\mathcal S_V=-\mathcal B/4\)；其余经典 log moments 分别为 R20 的两项。它们不是再次计算 Ω 的近似。

剩下的 \(T_1\) 具有新的完整组成。直接端点变换得

\[
T_1=4\int_0^1\frac{(-\log x)(\log(1+x^2)-l-\log x)}{1+x^2}dx.
\]

展开 \(\log(1+y)/(1+y)=\sum_{n\ge1}(-1)^{n+1}H_n y^n\)，得到

\[
\int_0^1\frac{-\log x\log(1+x^2)}{1+x^2}dx
=\sum_{n\ge1}\frac{(-1)^{n+1}H_n}{(2n+1)^2}=\mathcal C.
\tag{R21}
\]

交换可积级数合法，因为 \(\sum H_n/(2n+1)^2<\infty\)。parity 证明准确如下：置外指标 \(N=2n+1\) 奇、内指标 \(K=2k<N\) 偶，\(H_n=2\sum_{K\ \mathrm{even}<N}1/K\)，并且 \((-1)^{n+1}=i\,i^N\)。于是 R21 等于

\[
\frac i2\left(\mathcal L_{2,1}(i,1)+\mathcal L_{2,1}(i,-1)
-\mathcal L_{2,1}(-i,1)-\mathcal L_{2,1}(-i,-1)\right),
\]

即 R19 的 \(\mathcal C\)。余下两个 log moments 为 G 和 \(2\beta(3)\)，所以

\[
\boxed{T_1=8\beta(3)-4Gl+4\mathcal C.}
\tag{R22}
\]

此处 \(\mathcal C>0\) 来自原正积分，但不意味着它与 G、β4 或其他周期独立；也未调用未读的 MPL basis/降深定理。

## 6. 二阶十五个种子的完整表、整模型与投影范围

将全部实际值一次列全：

|种子|零阶|一阶|二阶|
|---|---|---|---|
|T|\(4G\)|\(8\beta(3)-4Gl+4\mathcal C\)|\(12\beta(4)\)|
|U|\(3\zeta(2)/2\)|\(7\zeta(3)-4G\)|\(45\zeta(4)/4-7\zeta(3)l/2-4\mathcal A\)|
|V|\(\zeta(2)\)|\(21\zeta(3)/16\)|\(45\zeta(4)/32-7\zeta(3)l/16-\mathcal B/4\)|
|W|\(1\)|\(l+\zeta(2)/2-l^2/2\)|\(13\zeta(3)/16+\zeta(2)(1-l)/4\)|
|X|\(1\)|\(\zeta(2)/2+l^2/2\)|\(\zeta(3)/2+\zeta(2)l/4\)|

完整 H7 系统中，\(\mu_{-1}(z)=4Gz+O(z^3)\)、\(\mu_0(z)=2+4Gz^2+O(z^4)\)。其递推证明所有 \(\mu_{i,k}\)，\(i\ge-1,0\le k\le2\)，只需 \(1,G\)。β1 的 π 项在实际 \(\pm t\) 合并后消失；B 的二阶外矩只需 \(1,l,\zeta(2)\)。因此完整边界/diagonal 递推给出实际包含

\[
\boxed{M^{(2)}(i,j),Z^{(2)}(i,j)\in\operatorname{span}_{\mathbb Q}\mathscr R_2\quad(i,j\ge0),}
\]
\[
\mathscr R_2=\{1,G,\beta(3),\beta(4),l,\zeta(2),\zeta(3),\zeta(4),
l^2,\zeta(2)l,\zeta(3)l,Gl,\mathcal A,\mathcal B,\mathcal C\}.
\tag{R23}
\]

这十五项是一个完整可代入的生成系统，没有声称最小数值基。尤其 β3 和各乘积也必须按完整系数消除或并入目标；\(\log2\) 已超越不推出这些乘积或整组数值 LI。

表中所有有理 substitution 系数由固定 32 清分母。对已经认证的全素数输入 cap \(Q_{2,H}=12\,2^{12(H+6)}D_{H+4}^6\)，在原 H17–H20 数组中先做实际 μ 的 parity 合并，再作这张表的 substitution，\(32Q_{2,H}\) 是新系数系统的安全全素数 cap。与原 cap 相比，n 阶 determinant 的额外付款至多 \(n\log32=O(n)\)，不是新的 \(n^2\) 节省；它仍只是系数模型，不清除未有理化的周期。

在原 Chebyshev/contact raw pool，\(\mathcal A\) 只来自 U2，\(\mathcal B\) 只来自 V2，所以它们完整系数分别准确为

\[
C_{\mathcal A}=-\frac43\mathcal D_N,\qquad
C_{\mathcal B}=\frac18\mathcal D_N,
\quad (\mathcal D_N)_{r,j}=[t^j]D_r.
\tag{R24}
\]

这是本稿重写后依然保留的真实 coefficient 事实。没有额外已证数值关系时，逐项消去 A 或 B 仍强迫同一 \(\mathcal D_N\) 核；所以前稿原 raw 核维数 \(12N+1\)、endpoint 核维数 \(8N+1\) 的认证障碍并没有自动消失。未来若能证明 A/B/C 与目标或其他周期的准确身份，必须先实际 substitution，再重算完整 stack。R24 不声称所有可能的数值消元都受此核限制。

## 7. 本轮实际阅读、验证与尚缺内容

本轮实际完整读取 higher-jet 稿全部8节/H1–H30、full-pool 稿全部8节/P1–P28及P9a–d、原仓库 foundations.tex 全434行，以及 boundary evaluation 稿全部7节/O1–O26。原仓库只读，旧620/producer/guard/prime表和主进展文件均未动。

网页 primary 输入是 NIST DLMF 的5.12 beta integral、5.5 reflection/recurrence、5.7 digamma expansion、5.15 trigamma series，实际打开上述对应公式；没有引用外部新颖性或 MPL 独立性结论。本轮新PDF阅读0页；已经将上述4个官方原始HTML网页保存于 literature，并记录路径、字节数和SHA256于[文献记录](../literature/dlmf_catalan_seed_sources_20261007.md)。只实际阅读指明公式与条件，没有把整页下载等同于全文阅读。

只运行1段全新内联 mpmath 70位计算，以原真实 u/t 积分核对 R15/R18/R14/R7/R22，所有闭式吻合。X1 的积分截去 \(u<10^{-30}\)，误差约 \(-2.5\cdot10^{-61}\)，故它只是浮点一致性核查，不称严格有理证书。没有PSLQ、未知常数拟合、旧脚本、Lean或机器形式化验证。公式证明来自上文分部积分、beta导数、绝对收敛parity与实polylog身份，不依赖浮点检查。

已证结果是 R4/R5 每阶 Z 消元、R7/R10 每阶 U/T 关系、R13 全部 W 偶 jets、R18/R20/R22 二阶准确值、R23 完整十五项实际周期生成系统和 R24 的准确系数范围。仍缺的是这些真实多对数周期与目标的进一步合并身份、成功的 full-stack 投影、同一对象的费用/解析余量及非零。尚未得到新的 β4、ζ奇数值或其他常数无理性/LI 定理。

root 已实际全文读本稿全部7节/R1–R24及完整表，独立核对 R4 分部积分端点、R7/R10 的符号和倍数、R11–R14 的 beta 参数导数、R17 的 trilog 微分/半值、R21 parity、R23 完整周期生成系统、32cap和 R24 的系数适用范围；补读原 H21 cap 段，明确纸面数学 PASS，无修正请求。root 另以1段全新内联40位积分核对 J/R16 与 half-trilog，吻合；该浮点核对只是说明，不能替代纸面证明或称为严格数值证书。作者收讫后补入以上实际审查记录，并完成最后全文回读。
