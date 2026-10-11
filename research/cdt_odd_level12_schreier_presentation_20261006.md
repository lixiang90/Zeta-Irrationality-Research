# D12 全群接口：48陪集、九个自由矩阵、十尖点及完整M扩张表示

日期：2026-10-06。新proof note。仅对固定level12作有限Schreier/Bass–Serre群结构计算，不扫描研究参数或prime，不运行旧或peer producer。[NEW证书](cdt_odd_level12_schreier_presentation_20261006_verify.py)首次、单次执行，263项通过；[固定JSON](cdt_odd_level12_schreier_presentation_20261006_verify.json)包含全部cosets、生成树、矩阵、自由字、尖点和M作用。本稿没有分类真实Eichler cocycle kernel，也没有证明数值线性无关性。

## 1. Γ确为PSLΓ1(12)，48陪集是literal finite model

χ12在mod12的units1,11取+1、5,7取−1。故

\[
 Γ=\ker(χ_{12}:PSLΓ_0(12)\to\{\pm1\})
 =\left\{\pm\begin{pmatrix}a&b\\c&d\end{pmatrix}:
 c\equiv0, d\equiv\pm1\pmod{12}\right\}
 =PSLΓ_1(12).
 \tag{G1}
\]

这是analytic congruence group等式；不据此混淆standard moduli Q-model的cusp field。本文的实际complex/Q(q)-germ geometry仍用[配对坐标稿](cdt_odd_level12_paired_coordinate_20261006.md)的v。

左陪集Γ\PSL2(Z)由primitive lower rows(c,d) modulo12、再除同时sign精确识别。若两SL矩阵lower rows相同到sign，则其比的lower row是(0,±1)，恰在Γ；反之Γ左乘保持该state。因此没有在finite residue data中遗漏额外cosets。

primitive pairs有

\[
 12^2(1-2^{-2})(1-3^{-2})=96
\]

个。sign无fixed primitive pair：若(c,d)=−(c,d) mod12，两者只能0或6，不能primitive。故有48states。证书按lexicographic minimum取canonical±pair，index0是(0,1)。用

\[
 S=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
 R=ST=\begin{pmatrix}0&-1\\1&1\end{pmatrix},
 \quad PSL2(Z)=\langle S,R\mid S^2=R^3=1\rangle
 \tag{G2}
\]

右作用：S:(c,d)↦(d,−c)、R:(c,d)↦(d,d−c)，48states全部在root的orbit。由这一实际transitivity加上完整coset识别，Γ的index恰48。

## 2. 生成性来自Bass–Serre树，而不是由signature猜矩阵

(G2)的Bass–Serre tree以PSL/〈S〉、PSL/〈R〉为两类vertices，以PSL元素为edges。Γ quotient的vertices是S/R的state cycles：24个S二cycle、16个R三cycle，edges48。没有S/R fixed coset，故Γ没有任何conjugate elliptic stabilizer；PSL的有限torsion都conjugate进这两个finite factors，所以Γ torsionfree。

Γ对该tree自由作用，故Γ就是这个connected quotient graph的fundamental group；rank为48−40+1=9。程序从root S-vertex按orbit phase构建39edge spanningtree。非树edge的零基indices准确是

\[
 1,2,30,31,32,40,43,44,46.
 \tag{G3}
\]

在每个S/R vertex选其incoming tree-edge代表r；其它incident edges分别取rS^j或rR^j。每条edge i因此有实际同coset的两代表r_i^S、r_i^R。tree edges的两代表只差central sign；non-tree edge给

\[
 x_i=r_i^S(r_i^R)^{-1}\in Γ.
\]

这正是基于spanningtree的fundamental-cycle generator，不是任意找到的九个Γ矩阵。全部循环lift到实际modular tree，所以无额外relation；下面九个矩阵是Γ的free basis。

|generator|literal det1 matrix (a,b;c,d)|
|---|---|
|x1|(59,25;−144,−61)|
|x2|(1,1;0,1)=T|
|x3|(37,29;−60,−47)|
|x4|(11,3;−48,−13)|
|x5|(25,16;−36,−23)|
|x6|(11,9;−60,−49)|
|x7|(13,4;−36,−11)|
|x8|(13,6;−24,−11)|
|x9|(1,1;−12,−11)|

矩阵按首个非zero entry正取PSL代表，故trace可能−2；central−I不形成额外relation。每个xj都有c≡0、d≡±1 mod12。

### 2.1 全矩阵的确定性free-word接口

global coset representative取r_i=r_i^S，定义edge labelXi为对应xj（tree edge则1）。对rightS step i→j，Schreier factor是1；对rightR或R^-1 step，factor准确是Xi Xj^-1。因此任意Γ中的modular word从root回root时，按这些factors相乘再free-reduce，就得到其在x1,…,x9中的唯一字。

任意实际det1 integer matrix用Euclidean algorithm左乘S T^-q降低lower-left absolute value，终点为±T^n；由此取得其S/R word。这不是限长猜测。证书检查全部九个basis rewrites为自己的letter、每个实际矩阵重构一致，以及后面的M作用字在自由群中平方为identity。JSON中带sign的integer wordj表示xj，−j表示xj^-1。

## 3. 十个实际尖点、width、抛物矩阵及单一relation

T的48state action有十cycles，widths准确为

\[
 1,1,12,6,4,4,3,3,12,2,
 \quad\sum w_i=48.
 \tag{G4}
\]

每个cycle选minimum state的r_i，实际尖点r_i∞、parabolic Pi=r_i T^wi r_i^-1如下。minimal width是从Tcycle直接确定，不仅检查某个power属于Γ。

|i|cusp|width|Pi matrix (a,b;c,d)|Pi free word|
|---:|---|---:|---|---|
|1|∞|1|(1,1;0,1)|x2|
|2|−5/12|1|(61,25;−144,−59)|x1^-1|
|3|0|12|(1,0;−12,1)|x9 x2^-1|
|4|−1/2|6|(13,6;−24,−11)|x8|
|5|−2/3|4|(25,16;−36,−23)|x5|
|6|−1/3|4|(13,4;−36,−11)|x7|
|7|−3/4|3|(37,27;−48,−35)|x3^-1 x5^-1|
|8|−1/4|3|(13,3;−48,−11)|x4^-1|
|9|−2/5|12|(121,48;−300,−119)|x1 x8^-1 x3 x6^-1 x4 x7^-1|
|10|−1/6|2|(13,2;−72,−11)|x6 x9^-1|

全部literal scaling matrices、coset cycles在JSON中保留。没有将Γ0的six cusps直接当作Γ的ten。

index、无elliptic及十Tcycles给Euler arithmetic

\[
 2g-2+10=48/6=8,\quad g=0.
\]

这与实际eta cover的genus0/ten cusp完全一致。还有一个显式parabolic presentation；不是只说存在某个未知的sphere relation：

\[
 \boxed{Γ=\langle P_1,\ldots,P_{10}\mid
 P_9P_6P_8P_{10}P_3P_1P_7P_5P_4P_2=1\rangle.}
 \tag{G5}
\]

证明可完全在上表自由字里检验：从P9字开始，依次右乘P6、P8、P10、P3、P1、P7、P5、P4、P2，末尾分别cancel x7^-1、x4、x6^-1、x9^-1、x2^-1、x3、x5^-1、x8^-1、x1，最终空字。另一方面

\[
\begin{gathered}
 x1=P2^{-1},\ x2=P1,\ x3=P5^{-1}P7^{-1},\ x4=P8^{-1},\\
 x5=P5,\ x7=P6,\ x8=P4,\ x9=P3P1,\ x6=P10P3P1.
\end{gathered}
\]

因此除P9以外九个Pi就是另一free basis，与原basis有字面inverse substitutions；(G5)是全部relation。这条正文relation由展示的自由字逐项约减证明，不冒称263项producer另检了一个未列明项目。

## 4. 〈Γ,M〉的完整semidirect presentation

取

\[
 M=\begin{pmatrix}24&-7\\84&-24\end{pmatrix},
 M'=\begin{pmatrix}-24&-7\\84&24\end{pmatrix}.
\]

M²=−12I，故在PSL2(R)中是involution。M conjugates每个实际free basis matrix回Γ；由完整basis生成证明这就是MΓM^-1=Γ。M不在Γ：其normalized det1 matrix的top-left是4√3，故不可能是SL2(Z)矩阵。于是G*=〈Γ,M〉且G*/Γ≅C2，extension由实际M分裂。

为了给完整relations而不留一个未知automorphism，设

\[
 \mathcal U=x2x5x8x1^{-1},\qquad
 \mathcal V=\mathcal Ux7x4^{-1},\quad α(g)=MgM^{-1}.
\]

实际matrix conjugation加上§2.1的确定性rewrite给

|j|α(xj)|
|---:|---|
|1|V x2 x9^-1 V^-1|
|2|x2 x5 x3 x6^-1 V^-1|
|3|V x6 x3 x6^-1 V^-1|
|4|U x7^-1 U^-1|
|5|V x6 x3^-1 x5^-1 x6^-1 V^-1|
|6|U x3 x6^-1 V^-1|
|7|V x7^-1 U^-1|
|8|V x6 x9^-1 V^-1|
|9|U x8^-1 x3 x6^-1 V^-1|

表内U/V指刚定义的calligraphic words。JSON同时保留全部expanded signed letters。对九个j都在自由群中直接约减得到α²(xj)=xj，不仅核相同矩阵。因此完整presentation是

\[
 \boxed{G_*=\langle x1,\ldots,x9,m\mid
 m^2=1,\quad m x_jm^{-1}=α(x_j),\ j=1,\ldots,9\rangle.}
 \tag{G6}
\]

没有未知追加relation。每个word都唯一正规化为γ或γm，γ为自由Γ字；实际index2结构证明其faithful。第二actual elliptic representative为

\[
 M'=kM,\quad k=(97,-28;-336,97)\inΓ,
 \quad k=x7^{-1}x1x8^{-1}x5^{-1}x2^{-1}.
 \tag{G7}
\]

α(k)=k^-1在自由字中核实，故(km)²=1。只给G6的十个实际generators已经足够；若要最少的五parabolics加二elliptics表示，需要实际Tietze/基路径调整，本文不把随手挑的七个矩阵冒称一个minimal generating set。

## 5. 全compact quotient的五cusps、两order2与实际矩阵接口

M作用于一个r_i∞时，将其first column乘M、约成primitive integer column、Bezout补成SL矩阵；其48state的Tcycle给准确Γ cusp class。这与选择任何Bezout completion无关，因为不同completion只差rightT。实际cusp permutation为

\[
 (1\ 9)(2\ 3)(4\ 10)(5\ 7)(6\ 8).
 \tag{G8}
\]

即width pairs为(1,12)、(1,12)、(6,2)、(4,3)、(4,3)，没有fixed cusp。五quotient cusp可以由P1、P2、P4、P5、P6分别代表；这里陈述conjugacy classes，不冒称这些矩阵已独自生成G*。

实际几何还可直接核：

\[
 v^2=(h+6)/(h+2),\quad Γ\text{ compact curve}=P^1_v,
 \quad Mv=-\sqrt3/v.
\]

十cusps的v是±1、±√3、0、∞、±i、±i√3；M恰无fixed cusp。其fixed values只有v=±i 3^(1/4)，两个upper-half-plane fibers分别由M、M′的actual fixed points代表。后者由real-q反射给complex conjugate v，故二者不是Γ-conjugate；不需猜定±标签。

Γ torsionfree、index2 extension使新elliptic stabilizer至多order2；以上两个branch fibers全部存在。因此G*有准确two order2 classes、five cusps。invariant degree2 coordinatev−√3/v给compact quotientgenus0，Riemann–Hurwitz(两simple branch)也得g=0。area index相当于24、χorb=2−5−2/2=−4，和Γ的index48一致。

这只是full compact algebraic/orbifold group的signature；**真实Hσ一般不对全部Γ单值，不能把该compact quotient自动当成合法filled analytic leaf。** 真正period stabilizer仍须用actual cocycle计算，不能用(G8)或genus0将未消π³ carrier删除。

## 6. 三维signed cocycle的可执行接口与本稿范围

在coefficient columnbasis(1,τ,τ²)上，normalized weight−2 slash的literal rational matrix是

\[
 \mathcal R_g=\frac1{\det g}
 \begin{pmatrix}
 d^2&bd&b^2\\2cd&ad+bc&2ab\\c^2&ac&a^2
 \end{pmatrix},\quad g=(a,b;c,d).
 \tag{G9}
\]

这是right slash的coefficient action：R_(g1 g2)=R_g2 R_g1，顺序不能反。source signε(xj)=+1、ε(m)=−1。若c(g)=h|−2g−ε(g)h，则

\[
 c(g_1g_2)=c(g_1)|_{-2}g_2+ε(g_1)c(g_2).
 \tag{G10}
\]

只需给九个xj及m的actual三坐标c值，再按(G6)验证relations，即可给整个G*的cocycle。所有matrix inputs、word reduction和M conjugation均已可有限准确执行；主源的period值并不由群结构自己产生。实际scalarH的稳定子是c^-1(0)，它可能无限指数，不能由十个cusp或两个elliptic的signature直接确定。

本稿完成有限生成与全部relations，不存在“矩阵数量不够但假定已生成”的缺口。它没有求出所有c(xj)、没有解决full kernel或证明新的无理性。下一工作可在完整有限presentation上核真实Eichler cocycle，而无需继续盲猜Γ generators。

## 7. NEW证书状态

作者首次、单次运行同名NEW producer，263项全部通过：48state complete orbit、S/R/T cycles、spanningtree/free edges、全部actual representatives、九个basis rewrite、十cuspparabolic/minimalwidth、M全部conjugation字与自由群α²、第二elliptic relation、五cusp实际配对。没有import/执行任何旧或peerproducer，没有研究参数扫描。

有限checks不替代§2的Bass–Serre generation theorem、§3的展示自由约减及§5的actual v分歧证明；这些全尺度链在正文给出。

独立审阅记录：root实际只读全文§§1–7及同名verify.py，复核lower-row ± cosets和48-state transitivity、Bass–Serre自由顶点/树及lift basis、S-factor 1和R-factor X_i X_j^-1、Euclidean rewrite、全部parabolic表和(G5)消去/inverse substitutions、M semidirect faithfulness与cusp pairing、v的两个fixed branch及其scope，限定审阅通过。root没有运行263项producer，也没有将群signature认作actual H的解析叶。本稿及其已执行证书现冻结；后续cocycle/kernel工作另建文件。
