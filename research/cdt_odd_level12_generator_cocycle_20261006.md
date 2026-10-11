# D12 完整九生成元的真实周期表与整数三维接口

日期：2026-10-06。独立新 proof/table note。本文固定[完整 Schreier presentation](cdt_odd_level12_schreier_presentation_20261006.md)的全部九个自由矩阵，直接从[全 Γ 真实有限尖点公式](cdt_odd_level12_gamma_cocycle_20261006.md)计算每个生成元的实际周期。不是搜索参数或短 word；没有执行/import旧或peer producer。未知 ζ3/L3 不参与 period table 的数值计算，也未解 full kernel。

## 1. 两个真实正规化函数及 exact finite 数据来源

令 Γ=kerχ12=PSLΓ1(12)，M=(24,−7;84,−24)。使用实际 functions

\[
 h_Z=f_Z-\Xi_Z,\quad \Xi_Z=103680\zeta(3),\qquad
 h_L=f_{\sigma,L}+\Theta,\quad
 \Theta=34560\sqrt3L(3,\chi_{12}).
 \tag{P1}
\]

两个 source 均为 Γ-modular，M-anti；hZ与hL都已有真实 h|−2M=−h。这里 hL是共轭 source 的 primitive，不是原 FL。对Γ有

\[
 c_Z(\gamma)=h_Z|_{-2}\gamma-h_Z=i\pi^3P_Z(\gamma),\qquad
 c_L(\gamma)=h_L|_{-2}\gamma-h_L=i\pi^3P_L(\gamma).
 \tag{P2}
\]

全 Γ 尖点稿已经严格证明 PL∈Q[τ]≤2。纯ζ源的 uZj 在j=1,2,3,4,6,12为1512,−27216,1944,−3456,244944,−217728；ΣuZj=0、ΣuZj/j³=−864。因此同稿普通Lambert(G14)在finite Γ∞ cusps的 pole为0、real finite part为ΞZ；减ΞZ后同一路径/interpolation证明PZ∈Q[τ]≤2。这不假设ζ3/L3为代数数，也不把∞本身的值当作finite endpoint。

NEW implementation仅读取群结构 JSON 的 matrices/words等**数据**，没有执行或导入其producer。这个输入JSON SHA256固定为

`387b30f338e5231397b905a64a58e5648bae1772af305b8baf9ed28e3b970fe4`。

为避免数据替换，脚本还逐项确认九个矩阵等于正文下面完整列表。周期核则从(G4)/(G6)/(G15)/(G16)的rational finite sums独立重新实现，不读取旧period JSON。

## 2. 全部九矩阵的实际 polynomial period

每个 xj 用预定four finite cusps x=1/12,1/24,1/36,1/48。其image取实际primitive rational fraction γx；这九个矩阵没有把任一个seed送到∞。通过

\[
 P(\gamma)(x)=(cx+d)^2\alpha(\gamma x)-\alpha(x)
 \tag{P3}
\]

取前三点的rational Vandermonde inverse，得到degree≤2 polynomial。第四点独立核对；真实polynomial degree≤2来自Bol，不是从四个数拟合后猜测全域。总计使用36个确定finite Γ∞ endpoint，其中Gauss/pole/realpart已经由全尺度尖点定理保证。

下表vector(a0,a1,a2)表示 a0+a1τ+a2τ²，均为实际 c/(iπ³) coefficients。

|xj|det1 matrix(a,b;c,d)|PZ(xj)|PL(xj)|
|---|---|---|---|
|x1|(59,25;−144,−61)|(−85017600,−401034240,−472780800)|(−55466880,−261559680,−308275200)|
|x2|(1,1;0,1)|(0,0,0)|(0,0,0)|
|x3|(37,29;−60,−47)|(40884480,104509440,66769920)|(27162080,69396480,44307840)|
|x4|(11,3;−48,−13)|(−2367360,−17210880,−31311360)|(−2266160,−16555200,−30256320)|
|x5|(25,16;−36,−23)|(−1365120,−4354560,−3525120)|(−1329040,−4311360,−3531840)|
|x6|(11,9;−60,−49)|(−41230080,−101606400,−62622720)|(−36342880,−89385600,−54983040)|
|x7|(13,4;−36,−11)|(−2609280,−17210880,−28408320)|(−1899280,−12615360,−20973120)|
|x8|(13,6;−24,−11)|(5218560,23639040,26956800)|(2819360,12723840,14459520)|
|x9|(1,1;−12,−11)|(0,0,0)|(−1587840,−3617280,−2073600)|

完整九free basis的来源是Schreier/Bass–Serre证明，不能用“恰好九个矩阵”代替生成性。NEW cert首次、单次174项全部通过，包含两source约束、36个endpoint合法性、全九第四点核验、所有M relations及下面的fixed checks。

## 3. 整个 Γ⋊C2 的 exact signed word 计算

令 εΓ=+1、εΓM=−1。采用已证 normalized right slash，coefficient matrix

\[
 R_g=\det(g)^{-1}
 \begin{pmatrix}
 d^2&bd&b^2\\2cd&ad+bc&2ab\\c^2&ac&a^2
 \end{pmatrix}.
\]

用 c(g1g2)=c(g1)|−2g2+ε(g1)c(g2)，逆元 c(g⁻¹)=−ε(g)c(g)|−2g⁻¹。full presentation是Γ自由九基再加m²=1及MxjM⁻¹=α(xj)。由于 c(M)=0，所有九条period compatibility必须为

\[
 P(\alpha(x_j))=-P(x_j)|_{-2}M.
 \tag{P4}
\]

NEW computation使用该presentation的全部九个expandedαwords，对Z/L两period逐项核(P4)，并核actualprojective matrices。central±I的normalizedslash相同，所以period/word relations是PSL relations；不把parabolicword代表的central sign误判成period改变。

另外准确核实

\[
 \eta=x2x9^{-1},\quad P_Z(\eta)=0,\quad
 P_L(\eta)=(44160,529920,2073600),
 \tag{P5}
\]

以及M′=kM，k=x7⁻¹x1x8⁻¹x5⁻¹x2⁻¹，PZ(k)=PL(k)=0。这与已经独立完成的ordinary-W cubic derivation和actualM′ period相符。

所有十个固定cusp parabolics的period由其exact freeword得到，JSON保留整张表。整个sphere relation

\[
 P_9P_6P_8P_{10}P_3P_1P_7P_5P_4P_2=1
\]

对两period均给0；其actualmatrix也为central identity。这里Pi表示parabolic matrices，不是periodpolynomial的下标；它们的words取Schreier稿固定表。

这些relations，加上freebasis的真实period值，给整个 G*=Γ⋊〈M〉的完整可执行actual cocycle。任意指定word无需再计算Bernoulli或L-value。P=0即actualscalar B0h的invariant判据，source/B0 sign仍共同保留。

## 4. 一个较有理性更强的整数 translation lattice

完整表还给出明确的全群结论：

\[
 \boxed{\frac{c_Z(g)}{80i\pi^3},\frac{c_L(g)}{80i\pi^3}
 \in\mathscr P_{12}:=\mathbf Z+\mathbf Z\tau+12\mathbf Z\tau^2
       \quad(g\in G_*).}
 \tag{P6}
\]

证明不需要再从finite examples推全群。先直接由上表核九basis values均属于80𝒫12；Γ的所有矩阵c divisible12，所以在basis(1,τ,12τ²)上Rγ为integer：

\[
 \begin{pmatrix}
 d^2&bd&12b^2\\2cd&ad+bc&24ab\\c^2/12&ac/12&a^2
 \end{pmatrix}.
\]

M在同basis上的准确matrix为

\[
 R_M=\begin{pmatrix}48&14&49\\-336&-97&-336\\49&14&48\end{pmatrix}.
 \tag{P7}
\]

因此𝒫12对Γ、M及其逆slash稳定；M的translation为0，signed cocycle乘±1也保持它。由完整生成性，(P6)对所有words成立。其binary discriminant为b1²−48b0b2，normalizedslash保持它；signed −R_M在正定cone上反向，故不能凭η family的正性排除任意mixedword取消。

这只是实际period的整数三维接口。除以已知transcendental iπ³得到integer translations，不等于target的Taylor coefficients变成integers，也不给CDT免费Smith/height信用。完整Taylor整模型和capacity仍是各自的问题。

### 4.1 同一真实函数的整数 affine holonomy

将𝒫12的coefficient视为basis(1,τ,12τ²)上的column。对Z或L分别定义

\[
 b_\gamma=\epsilon_\gamma c(\gamma)/(80i\pi^3),\qquad
 \rho_\gamma=\epsilon_\gamma R_\gamma,\qquad
 A_\gamma=\begin{pmatrix}\rho_\gamma&b_\gamma\\0&1\end{pmatrix}
       \in GL_4(\mathbf Z).
 \tag{P8}
\]

归一化是**同一个80**；若用普通(1,τ,τ²)表，则thirdcoordinate必须除960才能取得本lattice的坐标，不得将80与960混用。signed cocycle直接给

\[
 b_{\gamma\delta}=\rho_\delta b_\gamma+b_\delta,
 \quad \rho_{\gamma\delta}=\rho_\delta\rho_\gamma,
 \quad\boxed{A_{\gamma\delta}=A_\delta A_\gamma}.
 \tag{P9}
\]

这是right-action的准确乘法顺序。整数affine作用的原点(0,0,0,1)固定，准确当且仅当bγ=0，即cγ=0；由actual gauge同sign的identity，也准确当且仅当同一真实scalar B0h保持γ。这些affine matrices来自上述actualperiod，不是一个替代目标函数的formalmodule。

例如纯L正规化函数的η矩阵是

\[
 A_{\eta,L}=\begin{pmatrix}
 1&0&0&552\\24&1&0&6624\\12&1&1&2160\\0&0&0&1
 \end{pmatrix},\qquad
 A_M=\begin{pmatrix}
 -48&-14&-49&0\\336&97&336&0\\-49&-14&-48&0\\0&0&0&1
 \end{pmatrix}.
 \tag{P10}
\]

纯Z的η矩阵有相同homogeneous部分而translation为0。所有其它actualmatrices由九表和(P9)确定。这完成integer affine holonomy接口，尚未分类其原点稳定子；integer定义本身不保证稳定子是某个预期thin group，也不提供Taylor算术成本折扣。

## 5. 精确推进与仍未解的kernel

全group的unknown-period接口现在已闭合：两真实cocycles完全由九个integer vectors和M的zero translation给出。对任意固定word，检查其三个coordinates同时为0就判定对应actualH稳定性。联合关系source的cocycle可按[联合模型](cdt_odd_level12_joint_full_model_20261006.md)线性组合B PZ−C√3 PL；B、C均非zero时，其kernel准确为两个actualkernels的交。

固定九basis中，PL只在x2=T为0；PZ另在x9为0。这是完整basis的事实，**不是**kernel的生成元分类。已经知道M′的非trivial freeword为zero，说明按单个basis的zero项猜fullkernel会漏掉实际symmetry。本文没有枚举短words，也没有把integer cocycle table直接转成一个未经证明的新的filledleaf。

下一实质问题是这个明确affine/Sym² representation的stabilizer分类：是否有Gaug之外的zero words，如何证明其fundamental domain与fullanalytic/capacity。现在这可以在全presentation上进行，且需要的period常数全已固定；仍不由这张表宣布新的irrationality结论。

## 6. 实际审阅状态

作者实际只读Schreier正文全文，限定独审其§§4–6通过：M半直积、第二ellipticcoset、五cusps/twoelliptic与右slashmatrix顺序；没有执行peer263checkproducer。群freebasis的全尺度来源仍是其已通过root全文审核的Bass–Serre证明。

NEW table证书首次单次174项通过，JSON记录exactinputhash、36个finiteboundarycache及所有checks。root已实际阅读全文及新verify.py，独立核(P1)–(P10)：有限尖点取值、完整生成性接口、right slash/cocycle顺序、整数格(80,80,960)的坐标、R_M与εR的GL4(Z)右作用及原点稳定子判据，限定通过。root未执行producer，不认领fullstabilizer分类或Taylor-Smith信用。本文据此实际独审冻结，旧群/period/source文件没有变化。后续peer审阅可外部记录其精确范围，不为追加记录修改冻结文件。
