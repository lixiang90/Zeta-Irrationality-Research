# level20 Cartier 原函数的三导数表示与 q 坐标 Bockstein

日期：2026-10-06。本文新建，不改冻结输入。目标是将六积分第二层的非p倍数缺陷接到实际旧三导数 source，而不是认领新的数值无理性。本文给出全特征p的低次数 polynomial 表示，以及保留所有项的 q 坐标第二层公式。完整 mixed S2 仍有明确的慢变量余类，尚未证明它为零。

## 1. 输入与规范

沿用 [Hasse 规范](cdt_odd_level20_hasse_20261006.md)、[六积分矩阵](cdt_odd_level20_cartier_packet_matrix_20261006.md)及[第二层分类](cdt_odd_level20_cartier_packet_s2_20261006.md)。记 K=Q(r)、r²=5，k为K中p上的剩余域。p≥7，排固定 N/C 判别式及碰撞坏素数29、1049；真实 packet 还须排假设周期的分母等既有固定坏素数。没有排 Hasse 零点与 N 或 C 相交的素数，这些相交必须在下面的局部残数中合并处理。

取源符号 A=A₋、N=N₋、C=C₋，ϑ=t d/dt。Hasse 分子记为 P，避免与 degree5 的 source numerator P_c 混淆。已有输入为
\[
 \deg N=\deg C=2,\quad
 \deg P=3p-3,\quad P(0)P(1)\ne0,
 \quad\deg\operatorname{rad}P\le(3p+1)/2,
\]
\[
 \frac{A'}A=\frac{N'}N+\frac12\frac{C'}C+\frac{P'}P.
 \tag{M1}
\]
Hasse simple-zero 与 tame Fricke 商保证 P 的根重数仅为1或2。N、C自身 squarefree 且互素；其 leading coefficients 和0、1处值均为unit。

本文采用 [有理 Cartier 原函数](cdt_odd_level20_cartier_rational_primitive_20261006.md) 的结论：给定 c₀∈ker \bar M_p，Q_c=P_c/[(1-t)NC]，存在
\[
 u=J/P,\quad \deg J\le3p-3,\quad u(0)=0,\quad
 \vartheta(uA)=Q_cA.
 \tag{M2}
\]
该输入是特征p的实际 formal 身份；不声称特征零的 de Rham exactness。其有理原函数构造与全坏素数规范须以链接稿的实际证明为准。

## 2. 双极点插值给出三导数 polynomial 表示

置
\[
 \ell_1=\frac{\vartheta A}A,\qquad
 \ell_2=\frac{\vartheta^2A}A=\vartheta\ell_1+\ell_1^2,\quad
 D_{\rm red}=\operatorname{rad}(NCP),\quad d=\deg D_{\rm red}.
 \tag{M3}
\]
在代数闭包中的任一根α处，设 P 的根重数为e∈{0,1,2}，N、C的根重数分别为n,c∈{0,1}，且nc=0。由M1，A'/A的残数是
\[
 \rho=e+n+c/2.
\]
α不为0，ρ在p≥7时非零。ℓ₁的simple pole系数及ℓ₂的double pole系数分别为
\[
 [ (t-\alpha)^{-1}]\ell_1=\rho\alpha,\qquad
 [ (t-\alpha)^{-2}]\ell_2=\rho(\rho-1)\alpha^2.
 \tag{M4}
\]
u只在P的根有极点，次数最多2。当ρ=1时，只可能为P的simple根而非N/C根，或为N的根而非P/C根；因此u的double pole系数恰为0。

对ρ≠1的点，指定V₂(α)等于u的double pole系数除以M4的非零double系数；ρ=1处指定V₂(α)=0。D_red squarefree，CRT给唯一degV₂<d的多项式。数据在k上的Galois作用下相容，故V₂∈k[t]。于是u−V₂ℓ₂只有simple poles。

再指定V₁(α)为u−V₂ℓ₂的simple pole系数除以ρα。第二次CRT给degV₁<d，且u−V₁ℓ₁−V₂ℓ₂没有任何有限极点，所以它是一个多项式V₀。

无穷远的leading constant为
\[
 \ell_1(\infty)=2+1+(3p-3)=3p=0\quad\text{in }k.
 \tag{M5}
\]
因此ℓ₁=O(t⁻¹)、ℓ₂=O(t⁻¹)。M2给u=O(1)，所以degV₀≤max(0,d−2)。本处d≥2；遂得
\[
 \boxed{uA=V_0A+V_1\vartheta A+V_2\vartheta^2A,\qquad
 \deg V_r\le d-1\le(3p+7)/2.}
 \tag{M6}
\]
在0处ℓ₁、ℓ₂均为0，故V₀(0)=0。两次CRT及取差都对u线性。P与N/C相交时ρ须合并，M4仍适用；不能按互不相交的极点集合重复计数。

这个结论只表示一个特征p有理函数；它没有增加固定 characteristic-zero species 或其独立秩。

## 3. q 坐标消除 genuine-lift 记号，但保留真正余项

令 t=t(q)=q+O(q²)、S=θ_qt/t，其中θ_q=q d/dq。B_j=Q_jAS为已证 weight4 Hecke 基。对源常向量ĉ取c₀=ĉmodp∈ker \bar M_p；矩阵方向采用
\[
 T_pB_j^-=\sum_i M_{p,ij}B_i^{\rm target},\quad
 \varepsilon=\chi_5(p),\quad\text{target sign}=-\varepsilon.
\]
令 f=f_ε(q) 的 degree<p 实际整截断，\(\Xi_i(q)=\int_0^q B_i^{\rm target}(v)f(v)\,dv/v\)，只取slow degree<p，其系数均整，且Ξ_i(0)=0。它仍是完整 Af primitive，不删除周期carrier。

实际源packet给
\[
 Y_c^q=p^3\{B_c^-(f_- -\Theta)-Q_c(0)H_-(0)S\}
 \equiv B_c^- f(q^p)\pmod{p^3,q^{p^2}},
 \quad Z_c=p^4I_c,\quad
 [q^n]Z_c=\frac p n[q^n]Y_c^q\quad(n>0).
 \tag{M7}
\]
这里将t积分的constant正规化乘S后原样带到q坐标，故系数身份精确。被减项乘p³后在源modp³ packet为0；经一次积分并除p后仍在p²中，不影响下面的modp Bockstein。不能在精确q系数身份中直接漏掉S。

定义q系数抽取 \(\mathcal U_p h(q)=\sum_m[q^{pm}]h(q)\,q^m\)。这是q坐标的finite-prefix操作，未宣称为t坐标的rational函数操作。精确乘积规则给
\[
 \mathcal U_p(B_cf(q^p))=(\mathcal U_pB_c)f(q),
 \quad\mathcal U_pB_c=T_pB_c-\varepsilon p^3B_c(q^p).
 \tag{M8}
\]
因为 \(\bar M_pc_0=0\)，\(m_1=M_p\hat c/p\) 为整向量。逐系数M7–M8得
\[
 \frac{Z_{\hat c}}p\bmod p
 =\left(\sum_i\bar m_{1,i}\bar\Xi_i\right)(q^p)
   +\mathcal O_c^q(q)
 \quad\bmod q^{p^2},
 \tag{M9}
\]
其中O_c^q只含非p倍的positive次数，其n项为\([q^n](\bar B_c\bar f(q^p))/n\)。

由θ_q=Sϑ与M2，
\[
 \theta_q(uA)=B_c,\qquad
 \theta_q(uA\,\bar f(q^p))=B_c\,\bar f(q^p).
\]
非p倍系数可除n，故有完整身份
\[
 \mathcal O_c^q
 =uA\,\bar f(q^p)
  -\bigl((\mathcal U_p(uA))\bar f\bigr)(q^p).
 \tag{M10}
\]
式中\(\mathcal U_p(uA)\)包括零系数，但uA(0)=0，故其constant恰为0。组合M9–M10，定义
\[
 \boxed{\psi_c(q)=
 \sum_i\bar m_{1,i}\bar\Xi_i(q)
 -(\mathcal U_p(uA))(q)\bar f(q),\quad \psi_c(0)=0.}
 \tag{M11}
\]
则对Y=p³H₋的native规范，
\[
 \boxed{Z_{\hat c}/p-u\bar Y=\psi_c(q^p)\quad\bmod q^{p^2}.}
 \tag{M12}
\]
这里\(\bar Y=A\bar f(q^p)\)。M11第二项是必须保留的horizontal余项；并未证明它rational、有界度、属于Hecke矩阵像，或为零。M9–M12避免在中间步骤误将t(q^p)换成t^p。由于t↔q为整坐标同构、首项1，finite-prefix valuation并未改变；转回t正好产生旧稿所保留的genuine-lift缺陷。

## 4. 接到原九species的整source

旧实际species为gH、gϑH、gϑ²H，g=Δ²、deg g=8；共同p⁴评价时它们本来已有baseline1。用M6的任意整多项式lift \(\widehat V_r\) 构造
\[
 X_c=gZ_{\hat c}
     -\sum_{r=0}^2\widehat V_r\,[p^4g\vartheta^rH].
 \tag{M13}
\]
I的六坐标是gĉ，旧三坐标是−Vr。所有species均为原数组中已有项；安全source degree为
\[
 \delta_p=\max(8,d-1)\le(3p+7)/2\quad(p\ge7).
 \tag{M14}
\]
原S1因Zĉmodp=0和旧baseline1成立，且
\[
 X_c/p\bmod p=g(t(q))\,\psi_c(q^p).
 \tag{M15}
\]
所以非p倍原函数补正已完成，但M13是S2当且仅当所需完整前缀的ψ_c为0。g(0)=1，不会掩盖该余项。第一层并非新信用：它属于已知native kerM polynomial shifts及旧baseline1。

若只允许更改ĉ→ĉ+pc₁，u及Vr的modp保持不变，则
\[
 \psi_c\longmapsto\psi_c+\sum_i(\bar M_pc_1)_i\bar\Xi_i.
 \tag{M16}
\]
因此在此明确family中，可提升到S2的充要条件是
\[
 \boxed{\psi_c\in
 \operatorname{span}_k\{\sum_i(\bar M_ph)_i\bar\Xi_i:h\in k^6\}}
 \tag{M17}
\]
（只取当前slow前缀）。它不是一般polynomial mixed source的完整分类；允许额外horizontal old corrections时须将其真实像加入余核。已有旧S2/S3行的共同p⁴像divp²，所以它们除p后modp为0，不能靠重复加入这些行改变M17。

## 5. 范围与审阅

本文没有素数扫描、没有运行旧producer、没有假设非普通素数密度。M6依赖实际有理primitive输入、Hasse根重数和固定N/C好约化；M9–M17逐系数来自完整packet、真实weight4 Hecke恒等式和整坐标。尚需取得M17的非零可解方向、primitive saturation及净Smith收益，才可能进入新的数值无理性证明。当前rank19同支持四层预算仍是已知瓶颈，不能将本次降度解释为已经跨过它。

两个指定素数的冻结矩阵还给一个范围核查：[Hecke 证书](cdt_odd_level20_hecke_space_20261006.json) 中p=7的old/new blocks分别为−13T₃、−T₃，T₃²分别为−4、−76，均为模7单位；p=11的old/new blocks分别为−28I、20I，均为模11单位。Eisenstein block亦为单位，故这两个p的完整M_p核为零。这里χ₅(7)=−1，比较跨符号T₃；χ₅(11)=1，比较同符号identity，不可混用。此处只是从已有exact矩阵与已证commutant读出的两例，未重跑producer，也没有据此推断其它素数的ordinary性质或密度。

helper_tensor_budget 实际只读独审 §§2–4/M1–M17通过：全碰撞的double/simple CRT、无穷远3p=0降度、q正规化乘S、完整slow与off-p两部分、保留U_p(uA)、constant-c₁ family的充要条件、原共同p⁴ source坐标。conjugate_projection 实际只读独审同 §§2–4通过，特别核对exact正规化、p³误差除p的阶数、M16/M17的允许补正范围。二者均未运行producer，未在本次重证旧Hasse/完整Hecke输入，未将慢余核可解或净Smith信用记为已证。此稿无producer与有限数值证书；全尺度结论依赖正文证明及明确的冻结输入。
