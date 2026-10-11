# 第223轮：固定三周期 Padé 包的 P-recursive 与 G-function 结构

2026-10-08。对象保持222冻结的 R_n 三周期包，不修改旧稿。本文证明 A₃、A₅、A₇、C 的实际偶子序列，以及连续三行外积 Δ、Ξ 的 P-recursive 存在性；其普通生成函数均为 G-functions。证明使用可追溯的 general closure certificate，没有猜测递推或运行 telescoping。它不付最小阶数、无限非零、主奇点或CDT严格解析差额。

## 1. 固定对象与所用 primary closure

输入是 [222原稿](relation_source_architecture_global_round222_20261008.md)，11908B/SHA256 `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`，其P1–P15保持历史状态；Δ₀>0的新有限补充及独审另存，不在本稿重跑。令

R_n(t)= [∏_{j=1}^n(t−j)(t+n+j)]³ / [∏_{k=0}^n(t+k)]⁶.

为证明n方向结构，将此同一有理式暂定义于所有n≥0；数值三周期身份仍只使用偶n。部分分式 c_{j,k,n} 及 C_n 由旧稿P2、P5的有限公式延伸到所有n，不把奇n的周期分解改写成旧P4。

本稿使用两个原始定理层接口：[Zeilberger1990作者PDF](https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1991_p321.pdf) 的 Proposition2.1、3.1′–3.4′及§3.2.1，分别给有理生成函数的系数数组、离散加法/乘法/有限求和、P-recursive与D-finite对应；[Wilf–Zeilberger1992作者PDF](https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1992_p575.pdf) PDF10–12的 proper-hypergeometric 定义允许交换参数不定元，且proper项holonomic，PDF16–19给实际telescoping/closure接口及边界要求。这里只用固定维数的有限求和，不采用“任何有理shift ratio都holonomic”的错误命题；原文反例1/(n²+k²)正说明二者不同。

所有参数结论都在特征零域Q(v)上作离散holonomic运算。v是系数参数，不是要求连续D-finite的变量；没有假定Gamma函数对v holonomic。

## 2. 正则部分成为一个 proper-hypergeometric 参数项

定义实际有限乘积

F_{n,k}(v)=v⁶R_n(−k+v)
= (−1)^n [(k+1−v)_n(n+1−k+v)_n]³
            /[(1−v)_k(1+v)_{n−k}]⁶,     0≤k≤n.                  (H1)

这里(a)_m为上升阶乘，空积1。由原式在极点处约去v⁶可直接验证；第一个分子积换符号给(−1)^(3n)，分母六次幂的符号为正。每个支持内项在|v|<1全纯，且

[v^(6−j)]F_{n,k}(v)=c_{j,k,n},  1≤j≤6.                         (H2)

将Gamma表达用于generic v及任意整数n,k的proper项extension，有

F_{n,k}(v)= (−1)^n Γ(1−v)⁶Γ(1+v)⁶
 · Γ(n+k+1−v)³Γ(2n−k+1+v)³
 /[Γ(k+1−v)⁹Γ(n−k+1+v)⁹].                                     (H3)

支持内(H3)与(H1)完全相同，外侧仅供乘cutoff前的closure使用。也可把(H3)写成

(−1)^n (1−v)_{n+k}³(1+v)_{2n−k}³
          /[(1−v)_k⁹(1+v)_{n−k}⁹]，

其中负整数长度的上升阶乘按倒数定义，故每个整数index的值实际在Q(v)中。忽略只依赖v的非零normalizing factor后，这是整数仿射阶乘参数及整数幂的proper项；恢复该因子不改变任何n、k shift operator。由WZ允许交换参数不定元的定义，(−1)^kF是Q(v)上的proper-hypergeometric离散项，因而holonomic。该式只用作generic参数递推证书；不能对每个v分别存在递推，就未经证明宣称有一条Q(v)递推。

## 3. 两个有理 cutoff 支付所有有限边界及 C 行

定义整数数组

χ₂(n,k)=1 当0≤k≤n，其他处0；
χ₃(n,k,u)=1 当1≤u≤k≤n，其他处0。

它们在N²、N³上的生成函数准确为

Σχ₂(n,k)xⁿyᵏ = 1/[(1−x)(1−xy)],
Σχ₃(n,k,u)xⁿyᵏzᵘ = xyz/[(1−x)(1−xy)(1−xyz)].                  (H4)

两个分母常数项均1。由Zeilberger Proposition2.1及离散对应，它们是holonomic数组。与proper项相乘、再对有限支持变量求和，由3.2′、3.4′得到

S_n(v)=Σ_{k=0}^n(−1)^k F_{n,k}(v),
V_n(v)=Σ_{1≤u≤k≤n}(−1)^(k+u)F_{n,k}(v)/(u−v)²                  (H5)

均为Q(v)上的P-recursive参数序列。第二个summand也是proper：额外kernel等于Γ(u−v)²/Γ(u+1−v)²，u仿射阶乘参数合法。

这是实际boundary certificate：乘cutoff后，每个固定n只有有限多个非零项，外侧项定义为Q(v)中的零。先乘cutoff，再在v=0取支持内的正则Taylor系数；不在foreign整数范围对Gamma极点直接取Taylor，不免费调用generic参数自然终止，也不把无限sum的边界丢掉。

S_n的第0、2、4个系数分别给旧稿最高三行：

A_{s,n}=(s−1)(1−2^(1−s))[v^(7−s)]S_n(v),  s=3,5,7.              (H6)

更关键的是完整有理tail：

C_n=[v⁵]V_n(v).                                                 (H7)

证明：1/(u−v)²=Σ_{a≥0}(a+1)vᵃ/u^(a+2)。与(H2)相乘取v⁵，得到Σ_{j=1}^6 j c_{j,k,n}/u^(j+1)，再乘(−1)^(k+u)求和，恰为旧P5。这里包含奇j及偶ζ消失后仍保留的全部有限修正，没有从A₇一行推断C。

## 4. 固定 Taylor 系数的三角递推证明

下面的lemma不需要在连续参数v方向的holonomicity。

**Lemma.** 若f_n(v)是Q(v)上的P-recursive序列，且每个n≥0的值在v=0正则，则对每个固定h≥0，[v^h]f_n(v)是Q上的P-recursive序列。

证明：将一个非零annihilator清分母、改成forward shifts，写成

L(v)=Σ_{j=0}^d p_j(n,v)E_n^j，p_j∈Q[n,v]，L(v)f=0。

除去所有p_j共有的最大v幂后，展开L(v)=Σ_{a≥0}vᵃL_a，L₀≠0。令f^[h]_n=[v^h]f_n(v)。形式系数比较给

L₀ f^[h] = −Σ_{a=1}^h L_a f^[h−a].                             (H8)

h=0有非零齐次递推。若较低h已经P-recursive，右端由有限shift、polynomial乘法及加法closure也是P-recursive；取它的非零annihilator M_h（右端为零可取1），则

M_h L₀ f^[h]=0。

Q(n)[E_n]的shift Ore环无零因子，因此M_hL₀非零。归纳证毕。有限初始n处的异常或leading polynomial整数零点，可保留为有限初值；不会破坏P-recursiveness或生成函数D-finiteness。

对S、V只用h≤5，(H8)给一个固定六层三角difference packet。这是general closure proof，不是已计算出L、M_h的系数，不给具体n-order上界，更不是最小rank证书。由(H6)–(H7)，所有n的三个A序列及C序列实际P-recursive。

## 5. 偶子序列、连续外积及实际 G-functions

取偶子序列不免费假定递推只跳偶数。δ(r,n)=1当r≥0且n=2r，其余0；生成函数Σδ(r,n)yʳzⁿ=1/(1−yz²)是有理函数，因而holonomic数组。将上一节的序列扩为与r无关的数组，乘δ后对n有限求和，即得f_{2r}是P-recursive。固定前移r↦r+h也保此性质。

记a_r=A₃,₂ᵣ、b_r=A₅,₂ᵣ、c_r=A₇,₂ᵣ、q_r=C₂ᵣ。原Δ_r、Ξ_r是三行对应列的determinants。展开成六个带符号的termwise products；加法、乘法closure支付全部项。因此Δ、Ξ及对每个固定g∈Q的

h_{g,r}=gΔ_r+Ξ_r                                                 (H9)

实际P-recursive，其普通生成函数D-finite overQ(z)。固定θ=z∂z导数也D-finite。这里的“每个固定g”本来就给有理序列；只有它与实际数值J_r的周期表示 H_g=ΣJ_rzʳ，需要ζ(7)=g假设。

G-function性质现在已付：CDT固定v2 PDF189 Definition15.1.1列出的条件是D-finite、代数系数共轭增长至多指数、全部前缀共同分母至多指数。旧P9/P13提供全素数幂指数前缀上界，旧P15给poly(n)2^(15n)增长；扩至奇n时，最高c₆只多出(−1)^n，整性、正则jet清整与绝对值界都不变，故同界也支付所有n的有限公式。Δ、Ξ由固定移位及三个因子获得poly(r)2^(90r)增长及旧24/48分母上界。Q系数只有一个共轭。故上述全部普通生成函数都是actual G-functions，H_g的任意固定θ导数也是。这里不需另假定geometric realization，也不因没有Betti/Hodge数据拒绝direct CDT。[CDT定义原文](https://arxiv.org/abs/2408.15403v2)。

本证书已经利用旧安全上界足够完成G定义。Root另行优化全powers分母的稿由另人独审；新费用不能倒写成222原证据，也不作为本closure证明的前提。没有由G-function这一性质推出最优整格、最小微分秩、特定数值独立或实际overconvergence。

## 6. 相近 Zudilin 族核对与仍未付的主gate

完整选读作者版§7 PDF23–24及相邻PDF25。式62在k=7时用单次balanced分子、denominator八次、2t+n、n!⁶且非交错；文中另一个tilde F_n用当前R_n乘2t+n后取二阶导数，并作非交错和。两族都不同于当前交错的一阶导数I_n。所述四阶recurrence的characteristic polynomials不能移给本包；PDF25的general WZ论述也不代替当前具体operator。[Zudilin作者版](https://www.math.ru.nl/~zudilin/PS/z234.pdf)。

本轮新增结论是实际P-recursive存在性和actual G定义条件闭合。下一主gate仍是可检验的n-recurrence/差分模块、无界尺度的Δ非零、generic背景不可去主奇点与数值关系选择性。Δ₀>0仅证明序列非恒零，不排除最终零；P-recursiveness也不自动补这一缺口，例如只在r=0非零的有限支持序列就是P-recursive。若后续Δ的exact recurrence最早系数a₀(r)在r≥r₀从不零，且另有一个r≥r₀的已证非零项，反向递推才可排除零尾；本稿没有提供此异常集合或finite bridge。本稿也没有提供实际connection rank、dominant谱、完整共同解析图或CDT严格费用差。

仅证明holonomic存在性已达到本次限定命题，后续不应凭此继续盲调参数或借相邻族charpoly作asymptotic输入。

## 7. 文献身份、实际读取与运行账

新primary均从作者official页面归档至 [pade_structure_sources_round223_20261008](../literature/pade_structure_sources_round223_20261008)，lambert_前缀：

| PDF | bytes | SHA256 | 本人actual FULL选页 |
|---|---:|---|---|
| Zeilberger1990，48页 | 3514835 | `3d6f88a09982574a7c74565d286fb2cd88aa1a3c0d5f76655f4be999cd516966` | 1、14–20（印刷321、334–340） |
| Wilf–Zeilberger1992，59页 | 2889794 | `8dc85466d9bdffad1f44f33826df31b61076654b1dbf681c3c40ee33002e57b1` | 1、10–12、16–19（印刷575、584–586、590–593） |
| Zudilin作者版，33页 | 317847 | `81eeeca38692773d3760cef033d007c63da4da8747276f707aa09ef0d3de9207` | 1、23–25 |

Zudilin首页Date2002-03-21，LaTeX-revision2003-03-04，pdfinfo实核33页，不能当Numdam35页出版扫描同一字节。Root/C复用此作者PDF，各自选读另记。Numdam网页仅locator，未另下载。Zeilberger文件名含1991但首页出版是JCAM32(1990)321–368，身份按首页记录。

另本轮完整重读CDT固定v2 PDF189并存选页TXT；源4517169B/SHA256 `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`。复用本人已FULL读的222原稿及有限证书身份，不冒称独审自己的旧稿。全PDF locator只用于定位，不登记整篇FULL阅读；actual选页TXT另存，详细scope见同目录lambert_reading_scope.md。

本轮本任务数学程序、CAS、矩阵执行、prime/参数扫描、猜测递推、telescoping运行、数值积分、PSLQ、Lean、Git均0。只下载/定位/提取/读取primary及写Markdown/hash；未重跑222任何producer。H1–H9与closure应用为纸面证明，尚未形式化。最终保存后作者actual FULL复读，身份另报；作者自读不冒充独审。
