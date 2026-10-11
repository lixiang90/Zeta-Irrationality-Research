# R₀ transported origin 的真实模8障碍：全部路径不相交与共同解析域

日期：2026-10-06。NEW 全尺度纸面证明。本轮实际读取权威主报告 §§85–93，SHA256 为
1e0161b49ee96adae6cc30e9e7c89ca667b81877fd484919b86e7fd38e105f4c；
只读交付元数据及正文确认基线366份冻结数学输入、108份证明/审阅、78个PDF归档文件4476页。归档页数不是实际全文阅读页数。全部旧/同行数学MD、PY、JSON、manifest保持只读，未执行/import/rerun数学producer；本稿没有创建或执行新producer，没有有限word搜索。

本稿证明：规范conifold平面 \(P_c=\langle g_1,g_2\rangle\) 的**全部实际单值群轨道**均不等于原点平面 \(P_0=\ker N_0^2\)。关键是实际vanishing-cycle轨道上的模8整数行，而不是假设 \(P_c\) 已有有理Betti坐标。随后把这个障碍接到现有九行packet：原点的全部transported branches在每个有限cover上仍不亚纯；结合已经证明的conifold与∞分类，当前CDT maps的合法性自动对参数共同适用。没有新的特殊值无理性结论。

## 1. 同一实际周期表示与已有输入

在已指定的rank-four compact扇区 \(V\) 内，以actual oriented cycle的period表示
\[
 h_z(x)=\int_z\omega,\qquad
 \omega=\sqrt{x}\eta,\qquad
 P=\theta^4-x(\theta+\tfrac12)^4,\quad\theta=x\partial_x.
 \tag{M1}
\]
不把整个compact/open \(H^3\)认作rank four。实际period map在 \(V_{\mathbf C}\) 与 \(P\) 的solution space间是线性同构；这是冻结Yukawa/cup及[轨道整格稿](cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md)O24–O25使用的输入。

取actual vanishing cycle \(\delta\)，physical origin monodromy \(M_0\)，以及
\[
 U=-M_0,\quad N=\log U,\quad e_j=U^j\delta\ (0\le j\le3),\quad
 \Lambda_\delta=\sum_{j=0}^3\mathbf Ze_j.
 \tag{M2}
\]
冻结轨道稿O8–O17已经用真实cup与Picard–Lefschetz证明
\[
 \delta\cdot U^k\delta=\tfrac83(k^3+2k)\quad(k\in\mathbf Z),\qquad
 U=\begin{pmatrix}
 0&0&0&-1\\1&0&0&4\\0&1&0&-6\\0&0&1&4
 \end{pmatrix},
\]
\[
 M_1=\begin{pmatrix}
 1&-8&-32&-88\\0&1&0&0\\0&0&1&0\\0&0&0&1
 \end{pmatrix}.
 \tag{M3}
\]
两个矩阵及其逆都保持actual integral sublattice \(\Lambda_\delta\)；column coordinates固定为 \(e_0,e_1,e_2,e_3\)。无需使用其饱和化Smith因子或 \(\delta\) 的primitive case。

记
\[
 \ell=(1,1,1,1),\quad b=(0,1,4,11),\quad
 w=(-1,3,-3,1)^T.
\]
冻结O19–O25给
\[
 N^3=w\ell,\quad w\ne0,\quad
 \ker N^3=\ker\ell,\quad 2\Gamma_V=w,\quad
 C(y_0,h_z)=-\ell(z),\quad z\cdot\Gamma_V=8\ell(z).
 \tag{M4}
\]
以上 \(\ell\) 是在 \(\Lambda_\delta\) 上的整数行；没有称它在饱和unimodular格上也primitive。当前证明只在实际轨道格上使用它。

规范conifold germs满足
\[
 v=g_1+\tfrac34g_2,\qquad h_\delta=-\pi^2v,\qquad
 P_c=\operatorname{span}_{\mathbf C}(g_1,g_2).
 \tag{M5}
\]
因此通过period map把两侧表示识别之后，\(P_c\)确实包含actual \(\delta\) 的complex line。不是从某个数值Taylor初值猜测Betti坐标。

## 2. 全部word的整数不变量

**定理1。** 对每个physical monodromy word
\[
 \gamma\in\mathcal G_{\rm phys}=\langle M_0,M_1\rangle
 \subset\operatorname{Sp}(\Lambda_\delta,G),
\]
均有
\[
 \boxed{\ell(\gamma\delta)\equiv +1\ \text{或}\ -1\pmod8.}
 \tag{M6}
\]
对signed solution群 \(\mathcal G_{\rm sol}=\langle U,M_1\rangle\) 则有更强的
\[
 \boxed{\ell(\gamma\delta)\equiv1\pmod8.}
 \tag{M7}
\]

证明完全在真实整数矩阵内。直接按M3的每个column求和给
\[
 \ell U=\ell,\quad \ell U^{-1}=\ell,\qquad
 \ell M_1=\ell-8b,\quad \ell M_1^{-1}=\ell+8b.
 \tag{M8}
\]
\(M_1-I\)的平方为零，故最后一式亦由整数逆 \(M_1^{-1}=2I-M_1\) 得到。对任意 \(z\in\Lambda_\delta\)，因此
\[
 \ell(M_1^{\pm1}z)\equiv\ell(z)\pmod8,\qquad
 \ell(M_0^{\pm1}z)=-\ell(z).
 \tag{M9}
\]
从 \(\ell(\delta)=1\) 逐个letter应用M9即得M6；signed letters用M8即得M7。证明涵盖任意正负word长度，非有限枚举、非有限样本插值。

等价的真实intersection表述为
\[
 \boxed{(\gamma\delta)\cdot\Gamma_V
       \in8(8\mathbf Z+1)\ \cup\ 8(8\mathbf Z-1),}
 \tag{M10}
\]
尤其所有这些交叉数均非零。也可不用坐标验证：轨道格内所有与 \(\delta\) 的交叉数是8的倍数；PL添加 \((z\cdot\delta)\delta\) 使 \(z\cdot\Gamma_V\) 改变64的倍数，physical \(M_0\) 则改变其符号。

这里 \(\mathcal G_{\rm phys}\) 是**实际monodromy subgroup**，不是声称完整 \(\operatorname{Sp}(L,\mathbf Z)\) 满足M6。任意额外整辛变换或任意非flat比较矩阵，不是一个已授权的analytic-continuation word。此有限同余不变量亦不与实际Zariski closure \(\operatorname{Sp}_4\) 矛盾。

## 3. 周期、Kummer符号与全部路径不相交

period form \(\eta\) 是algebraic single-valued，而 \(\omega=\sqrt{x}\eta\)。沿physical loop的scalar continuation与其cycle transport满足
\[
 \operatorname{cont}_\gamma h_z
  =\chi(\gamma)h_{\gamma z},\qquad \chi(\gamma)\in\{\pm1\}.
 \tag{M11}
\]
故homogeneous \(P\)-solution表示的generator是 \(U\) 与 \(M_1\)，而physical cycle表示的origin generator是 \(-U\)。Kummer sign只乘整个transported plane一个非零scalar，不影响该plane或M6中的“非零”。若路径记号采取inverse action，\(\gamma^{-1}\)仍是同一群内的word，必须同时转换origin flag；论证不改变。

取固定real参考路径把origin的MUM flag运回同一basepoint：
\[
 P_0=\ker N^2\subset\ker N^3=\ker\ell.
 \tag{M12}
\]
**定理2。**
\[
 \boxed{\gamma P_c\ne P_0\qquad
     \text{对每个实际physical或signed monodromy word }\gamma.}
 \tag{M13}
\]
证明：M5与M11给 \(\gamma P_c\) 包含 \(h_{\gamma\delta}\) 的line。如果 \(\gamma P_c=P_0\)，就有 \(\gamma\delta\in\ker\ell\)，与M6/M7矛盾。更强地，
\[
 \boxed{C(y_0,\operatorname{cont}_\gamma v)
      =\chi(\gamma)\ell(\gamma\delta)/\pi^2\ne0}
 \tag{M14}
\]
（physical convention）；signed convention将 \(\chi\)吸收。没有假设 \(P_c\) 为rational Betti plane，没有要求计算 \(g_2\) 的完整connection matrix。

若改变参考路径使 \(P_0\) 变成 \(\eta P_0\)，其相交问题等价于
\(\eta^{-1}\gamma P_c=P_0\)，仍由M13排除。由 \(\mathbf P^1\setminus\{0,1,\infty\}\) 上任何有限algebraic cover得到的continuation，只取这些word的subgroup；ordinary-point ramification没有新的nontrivial local monodromy。cover中的origin logarithm乘非零整数，不改变 \(\ker N^2\)。所以所有有限cover仍不相交。

## 4. 真实origin criterion的第一项永不满足

冻结[exterior稿](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md)E30的潜在filled-origin criterion为：先用even local cover杀source的Kummer sign，再要求
\[
 P_\gamma=P_0,\qquad C(y_0,H_{\gamma,q})=0.
 \tag{M15}
\]
第二项检测actual参数，但**第一项已被M13全部排除**。不存在可先找word、再用第二项选择actual \(q=\alpha_0\) 的这一分支。

具体而言，mixed quotient为非零
\(\chi\otimes(g_1\wedge g_2)\)。奇数local winding的semisimple eigenvalue为−1，不能fixed。偶数非零winding若fixed，decomposable wedge的line迫 \(\gamma P_c\) invariant；regular \(J_4\) 的唯一invariant二plane是 \(\ker N^2=P_0\)，与M13矛盾。因此
\[
 \boxed{\text{origin的全部transported branches、
 任意 }q\in\mathbf C\text{、任意有限cover均非meromorphic。}}
 \tag{M16}
\]
这里涵盖paired九行tuple以及raw exterior vector的monodromy；允许meromorphic poles不能取消非零jump。

冻结[holonomy接口](cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.md)H2–H4进一步给：在实际九维module
\[
 0\to V\to\mathcal W\to\chi\otimes\wedge^2_0V\to0,\qquad
 G^\circ=\mathbf G_a^4\rtimes\operatorname{Sp}_4
\]
中，任何stable subspace若primitive quotient像非零，便等于全部 \(\mathcal W\)。在任意transported origin branch上，M16的jump都具有非零primitive quotient。若一个finite-cover algebraic row \(R\) 输出meromorphic scalar，则evaluation kernel含该jump，故等于全部 \(\mathcal W\)，于是该输出恒零。因此H4的linear no-go现在覆盖**全部transported origin branches**。加独立常数1仅留下其algebraic coefficient；有限次algebraic differential integration亦不能用同一module保留目标并填平origin。

这没有排除高tensor、新periods、非线性packet或具jump项的vector-valued holonomy理论。

## 5. 对当前CDT maps，参数共同域成为结论

令 \(F(q)\) 为冻结E7a的四个paired \(Z\) 行及五个mixed行，canonical \(t=1-x=0\) germs；加入1后的actual rank为10。此前已经证明：

- ordinary points的connection/gauge无新branch singularity；
- conifold全部transported branches在paired tuple中holomorphic，准确当且仅当 \(v\in\gamma P_c\)，对每个 \(q\) 相同（E20.3）；
- ∞的全部transported branches在任意finite cover均不fillable（E22）。

M16新增origin的全路径分类。由此得到如下准确解析结论。

**定理3。** 设 \(\phi\) 为闭单位盘某邻域上的nonconstant holomorphic map，\(\phi(0)=0,\ \phi'(0)\ne0\)，沿canonical germs解释 \(F(q)\circ\phi\)。如果某个 \(q_*\in\mathbf C\) 的九个pullbacks在单位盘内single-valued meromorphic，则同一 \(\phi\) 对**每个** \(q\in\mathbf C\) 都有该性质。

证明：若盘内存在 \(\phi(z)=1\)（target origin），nonconstant holomorphic map在该点有有限正local ramification。拉回local monodromy正是M16中的非零power，不能meromorphic，矛盾。因此合法 \(\phi\) 避免1。holomorphic \(\phi\) 本来没有∞ preimage；若允许meromorphic maps，任何pole亦由E22排除。

\(\phi^{-1}(0)\) 在闭盘中有限，因为 \(\phi\) 在其邻域holomorphic且nonconstant。对每个这样的point，先沿盘内避开该有限集合的路径继续canonical germ，其arrival word \(\gamma\) 由路径与homogeneous connection决定，不依赖 \(q\)。假设 \(q_*\) 的tuple meromorphic，尤其local monodromy固定；E20.3迫 \(v\in\gamma P_c\)，从而同一分支对全部 \(q\) 实际holomorphic。中心canonical branch亦全体 \(q\) holomorphic。

剩余punctured disk的fundamental group由这些小loops生成。所有 \(q\) 的continued germs在每个generator下fixed，故全体single-valued；再用上述local holomorphic extensions填回所有punctures。证明完毕。临近盘boundary的任何额外估计，仍须采用CDT所列regularity与finite-integral limit条件，不能从此局部论证自动得到。

定理3适用于选择依赖 \(q_*\) 的maps：选完以后，reference \(q=0\) 仍可使用同一个map；没有要求map的构造独立于目标。对number-field全部embeddings逐个应用亦同样成立。

同样的meromorphy结论适用于只在open unit disk内holomorphic的 \(\phi\)：在每个compact subdisk中只存在有限个conifold preimages，每个loop落在某个这样的subdisk，逐个重复上述延拓/填点证明即得全盘结论。它不保证CDT boundary integral的极限存在；这仍按所引用定理的boundary条件另核。

于是冻结H18的“共用域hypothesis”在这类current packet/maps中自动满足。以已核[数域缩放补充](cdt_odd_R0_dyadic_number_field_scale_supplement_20261006.md)的最新付费scale
\(\rho=(7/2)\log2\)、\(\tau=329/50\)，若全部embeddings/boundary/finite-place条件成立且
\[
 L_\rho=\sum_\sigma w_\sigma\log|\phi_\sigma'(0)|-\rho>\tau,
 \quad A_\rho=\sum_\sigma w_\sigma I(\phi_\sigma)-\rho,
\]
无条件 \(q=0\) 的同一rank10 arithmetic reference已经强制
\[
 \boxed{10(L_\rho-\tau)\le A_\rho.}
 \tag{M17}
\]
所以当前九行packet不能通过选择一个“只适用于actual \(q\)”的transported filled-origin/CDT map产生反证。这是对指定packet、maps和已核预算的障碍，不是所有arithmeticholonomy方法的no-go。

## 6. 本轮新增、剩余方向与审计范围

新增已证：actual cycle orbit的 \(\ell\)-值模8为±1；真实torus交叉数模64为±8；全部actual plane orbits与 \(\ker N^2\) 不相交；origin全部branches在finite covers及非零linear differential outputs下不可填；列明CDT maps的meromorphy自动对参数共同适用。

原点highest-log关系
\(N^3p_+\Phi(q)=0\iff q=\alpha_0\)
仍是真实value-sensitive boundary datum，但它不产生filled point。规范 \(g_2\) 的Betti/de Rham comparison依然是另一个有用问题；其完成也不能推翻M13。下一步须改变representation/packet，或为非零jump及endpoint flag建立真正新的local height/slopes估计，重新付actual rank和all-place费用。

没有新的奇ζ、L值、Catalan或 \(\alpha_0\) 的无理性/超越性定理，没有Lean证明。目标仍未完成。纯优化已有species/scale/capacity或继续枚举此word问题不再是该packet的突破点。

实际读取范围与冻结输入：

- 权威main §§85–93及delivery selectedmetadata；main hash见首段。
- 轨道格稿完整实际读取，SHA baf29ee041a0ea48c4b64c517cf0712f24c52c4c98893e4c74a98698c7e05586。
- real Betti稿完整实际读取，SHA dd541870010dc296993f512252e6b359bec2a1c147b382d288637078ef9c490f。
- exterior稿本轮实际E1–E12；初次组合输出截断后，E3–E7a、E8全部、E20.3–E30及全部scope分段实际补读；SHA b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef。
- endpoint holonomy稿本轮实际全文读取；组合输出后另将完整正文单独再次输出，SHA af728ecbebe3ac4827f7388706d4c5892896437e625e1bf4a0671b949bff28b5。
- 数域缩放补充的complete budget上一轮已实际全文独审，本轮复用其已冻结结果并读取权威main §92，没有冒认本轮又读补充全文。

本轮没有新增primary PDF读取/下载，没有凭文献abstract增加输入。论证M6–M17是基于列明真实冻结输入的新纸面推导；同行独审另存，不把作者自己的回读记作独立审阅。新数学producer执行数0，旧/peer producer执行/import/rerun数0。首次尝试把核心手核交给闲置child被thread limit拒绝，随后两位既存同行已收到核心proof并独立手核；该工具限制没有阻断数学工作。
