# 奇数 ζ 与偶数 β 的统一周期框架：已知结构、真正缺口和较弱研究目标

日期：2026-10-04。性质：原始文献核查与数学推导；没有数值参数搜索，也没有新的无理性定理。本文中“动机”指 motive；“周期”指 Betti 与 de Rham 实现之间的比较矩阵系数。原文定理、原文猜想和本文提出的研究目标分别标明。

核心判断是：全部奇数 ζ 和 Catalan 常数确实可以放进同一个有严格结构定理的框架——四次单位根上的混合 Tate 周期。统一的未解步骤不是再证明这些动机方向存在或非零，而是证明其**数值比较周期点足够一般**。已经证明的自由 Lie 代数、调节子非零、动机线性独立，都没有完成这一步。

## 1. 一个直接的统一对象

记

\[
\beta(s)=\sum_{k\geq0}\frac{(-1)^k}{(2k+1)^s}=L(s,\chi_{-4}),
\qquad G=\beta(2).
\]

由级数按奇偶项分拆，本文直接得到，对整数 \(s>1\)，

\[
\operatorname{Li}_s(i)
=-2^{-s}(1-2^{1-s})\zeta(s)+i\beta(s).
\tag{1}
\]

因此，两组难常数是同一序列 \(\operatorname{Li}_s(i)\) 的交替实、虚分量：

| 权指标 | 已有纯 Tate 分量 | 待解决的扩张分量 |
|---|---|---|
| 奇数 \(s\geq3\) | \(\beta(s)\in\mathbb Q^\times\pi^s\) | \(\Re\operatorname{Li}_s(i)\in\mathbb Q^\times\zeta(s)\) |
| 偶数 \(s\geq2\) | \(\zeta(s)\in\mathbb Q^\times\pi^s\) | \(\Im\operatorname{Li}_s(i)=\beta(s)\) |

权一还有 \(\operatorname{Li}_1(i)=-\tfrac12\log2+i\pi/4\)。公式 (1) 是数值恒等式；将它提升到动机周期时，要同时保留 Tate 周期及所选复嵌入，不能把“取实部”当成任意动机环的 \(\mathbb Q\)-代数运算。

四次单位根的正确基础类别是

\[
\mathrm{MT}(\mathbb Z[i,1/2]),
\]

配以固定嵌入 \(\mathbb Q(i)\hookrightarrow\mathbb C\)。Deligne 的特殊层级定理保证相关基本群生成此类别，并给出周期坐标的完整动机结构；这是 level 4 的优势。不能仅因 level 4 成立，就对任意单位根层级作相同断言。Brown 特别指出 level 5 已在权二出现生成性障碍。[Brown 2014，§4](https://www.ihes.fr/~brown/MotivicPeriodsandP1minus3pointsv3.pdf)

## 2. 原文已经证明什么

### 2.1 Brown：奇数 ζ 的动机方向已被分清

Brown 2012 的主要定理是动机多重 ζ 的 Hoffman \(\{2,3\}\) 基及相应混合 Tate 类别的生成性。通过周期映射，它给出实际多重 ζ 的生成/张成结果；数值独立性需要额外命题。自由动机 Lie 代数在奇数权 \(3,5,7,\ldots\) 各有一个生成方向。[Brown 2012，Theorem 1.1 与引言](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf)

这说明 \(\zeta^{\mathfrak m}(7)\) 不会在动机层被其他权的 ζ 或有理数消掉，尚不能排除比较周期的实值恰好为某个有理数。Brown 2014 的 Conjecture 3.2 正是周期映射单射；其 Conjecture 3.4 将 \(\pi,\zeta(3),\zeta(5),\ldots\) 的数值代数独立列为进一步后果。[Brown 2014，§3.2，作者 PDF 第15页](https://www.ihes.fr/~brown/MotivicPeriodsandP1minus3pointsv3.pdf)

### 2.2 Deligne–Goncharov：非零扩张与调节子

对数域 \(F\)，有

\[
\operatorname{Ext}^1_{\mathrm{MT}(F)}(\mathbb Q(0),\mathbb Q(n))
\simeq K_{2n-1}(F)\otimes\mathbb Q\quad(n\geq1),
\qquad \operatorname{Ext}^2=0.
\tag{2}
\]

在 \(S\)-整数类别中，仅权一的单位条件需要相应限制。调节子注入识别这些非零方向；其 Hodge 类值在 \(\mathbb C/(2\pi i)^n\mathbb Q\) 中。自由 Lie 结构来自式 (2) 与 \(\operatorname{Ext}^2=0\)，并不来自任何无理性定理。[Deligne–Goncharov 2005，§1.6、§2.1–2.4](https://www.numdam.org/article/ASENS_2005_4_38_1_1_0.pdf)

### 2.3 Borel：为何 \(\mathbb Q(i)\) 正好统一两种奇偶

对 \(n\geq2\)，Borel 的秩为

\[
\dim_{\mathbb Q}K_{2n-1}(F)\otimes\mathbb Q
=\begin{cases}r_1+r_2,&n\text{ 奇},\\ r_2,&n\text{ 偶}.\end{cases}
\tag{3}
\]

于是 \(F=\mathbb Q\) 只留下奇数权方向；\(F=\mathbb Q(i)\) 在每个 \(n\geq2\) 都有一个方向。复共轭在该方向的特征是 \((-1)^{n-1}\)：奇数权为平凡特征的 ζ，偶数权为 \(\chi_{-4}\) 的 β。调节子提取的正是奇数权实分量、偶数权虚分量。[Borel 1977](https://www.numdam.org/item/ASNSP_1977_4_4_4_613_0.pdf)，[Deligne–Goncharov 2005，§6.8–6.11](https://www.numdam.org/article/ASENS_2005_4_38_1_1_0.pdf)

Borel 原文有 [1980 勘误](https://www.numdam.org/item/ASNSP_1980_4_7_2_373_0.pdf)。本报告只用秩、特征和非零性，不用未经核对的判别式、\(i\) 次幂或调节子精确归一化常数。调节子与特殊值相等“相差非零有理因子”仍没有给出该特殊值的有理性排除。

### 2.4 Deligne：level 4 的坐标代数是可用的实质结构

Deligne 2010 的 Corollary 4.11、4.12 证明相应基本群的忠实性及类别生成性；Theorem 6.1 的证明给出 level 4 周期坐标代数的结构，和 Tate 坐标相分离。数值线性独立在定理中被明确放在 Conjecture 5.6 的条件之后。[Deligne 2010，期刊第122–124、130页](https://www.numdam.org/article/PMIHES_2010__112__101_0.pdf)

这比“猜测所有 ζ 都独立”具体得多：目标数字对应哪些扩张坐标，坐标之间在动机层有什么关系，已经有严格答案；数值求值是否产生额外关系，则还没有答案。

## 3. 哪个明确猜想足以一起解决所有目标

### 3.1 只解决奇数 ζ 的版本

设 \(\mathcal P^{\mathfrak m}_{\mathrm{MT}(\mathbb Z)}\) 为相应动机周期环，\(\operatorname{per}\) 为比较周期求值。Brown 的明确猜想是

\[
\operatorname{per}:\mathcal P^{\mathfrak m}_{\mathrm{MT}(\mathbb Z)}
\longrightarrow\mathbb C\quad\text{单射}.
\tag{PC-Z}
\]

它与已知动机代数结构合起来，推出 \(\pi,\zeta(3),\zeta(5),\ldots\) 代数独立。这比逐个无理性强得多。仅有 (PC-Z) 的写法没有包含 Catalan 的 \(\chi_{-4}\) 方向。

### 3.2 同时解决奇数 ζ 与偶数 β 的 level 4 版本

Deligne 的 Conjecture 5.6 对 level 4 作如下断言：实际比较路径周期点 \(\mathrm{dch}\) 是相关周期空间的 \(\mathbb Q\)-泛型点，即

\[
f\longmapsto f(\mathrm{dch}):\mathcal O(IU_\omega\circ D)
\longrightarrow\mathbb C\quad\text{单射}.
\tag{PC-4}
\]

更强的 Appendix Conjecture A.2 断言整个 mixed Tate 比较点 \(a_\sigma\) 泛型；Proposition A.3 证明它蕴含 (PC-4)。请使用**混合 Tate 版本**，不要仅写一个没有覆盖扩张对象的“纯动机 Grothendieck 周期猜想”。[Deligne 2010，Conjecture 5.6，第127页；Appendix A.2–A.3，第138页](https://www.numdam.org/article/PMIHES_2010__112__101_0.pdf)

**本文推导的条件结论：**(PC-4) 推出

\[
\pi,\ \log2,\ \zeta(3),\zeta(5),\zeta(7),\ldots,
\ \beta(2),\beta(4),\beta(6),\ldots
\tag{4}
\]

联合代数独立；这里“无限集合”指每个有限子集代数独立。因此全部这些 ζ、β 都超越，尤其都无理。

推导分三步，避免把数值独立偷放进结构定理。下面把第一步的坐标论证补全，系数域一直先取 \(\mathbb Q\)：

1. Deligne 的 (6.1.4) 是仿射坐标代数的同构：level 4 时，它分成 \(\mathcal O(D^1\Pi''_1)\otimes\mathbb Q[t]\)。前一因子由字母 \(x=e_0,y=e_{i^{-1}}\) 的 group-like 序列给出，附条件 \(c(x)=0\)。令 \(u_n=\operatorname{ad}(x)^{n-1}y\)；它满足 \(c(x^{n-1}y)(u_n)=1\)，且其他同样只含一个 \(y\) 的权坐标为零。对任何有限指标集以及任意 \(a_n\)，序列 \(\exp(\sum a_nu_n)\) 都满足 \(c(x)=0\)，其 \(c(x^{n-1}y)=a_n\)：指数的二次及更高项含至少两个 \(y\)，所以没有贡献。这证明这些坐标的任意有限组可独立取值；再添独立的 \(t\)，便得到代数独立。按 Deligne 的 (5.1)(A) 约定，\(c(x^{n-1}y)(\mathrm{dch})=-\operatorname{Li}_n(i)\)，而 \(t(\mathrm{dch})=2\pi i\)。这一步证明的是坐标函数独立，尚未证明该具体点的值独立。
2. **此时才使用猜想**：由 (PC-4)，其数值 \(2\pi i,\operatorname{Li}_1(i),\operatorname{Li}_2(i),\ldots\) 代数独立。\(\mathbb Q\) 上的代数独立在代数扩张 \(\overline{\mathbb Q}\) 上仍成立。
3. 用 (1)、\(\operatorname{Li}_1(i)\) 的公式及纯 Tate 特殊值公式，逐权作可逆三角代换：奇数权保留非零有理倍数的 ζ，偶数权保留 \(i\beta\)，其余项为代数系数的 \((2\pi i)^n\)。因此得到 (4)。

步骤1是从原文坐标代数作出的代数推论，步骤2依赖尚未证明的猜想。步骤2转到 \(\overline{\mathbb Q}\) 也无需额外猜想：若有有限个代数系数的非零多项式关系，对其系数域取所有共轭多项式的乘积，就会得到一个非零的 \(\mathbb Q\)-系数关系，矛盾。这里仅对已证明条件独立的坐标子代数作基域扩张，没有声称任意周期环添代数系数后都仍单射。不能把三步合称一个无条件的“Brown–Deligne 无理性定理”。若直接为 \(\beta^{\mathfrak m}(2n)\) 选取实周期符号，可加入表示 \(i\) 的有限 Artin 周期；或在 \(\overline{\mathbb Q}\) 上记系数。有限 Artin 扩张不增加这里的超越次数，但必须记清系数域。

## 4. 常见推理缺口：哪些说法没有解决无理性

| 已知信息/可能误用 | 实际边界 |
|---|---|
| 动机 \(\zeta^{\mathfrak m}(n)\) 非零、不同权独立 | 只约束形式周期。数值 \(\operatorname{per}\) 的核仍可能出现额外关系 |
| Borel 调节子注入、对应 \(K\)-群秩一 | 一个非零实格子的生成元可能是有理数；“非零”不能推出“无理” |
| Beilinson 特殊值/调节子公式 | 公式把 L 值识别为扩张/格子周期，没有自动给出实周期的算术性质 |
| Hodge 扩张非平凡，或实现函子全忠实 | 排除的是 \((2\pi i)^n\mathbb Q\) 内的消失；不是排除所有有理实数 |
| 不同数值 ζ 权不同，所以可以逐权比较 | 数值周期环的权分次没有作为免费工具建立；这是周期单射所要推出的结论的一部分 |
| 对一个假设的数值等式直接施加动机 Galois 导子 | 导子作用于形式周期。先要证明该数值关系的核受作用保持，才能下降到数字 |
| 将动机环商掉 \(\zeta^{\mathfrak m}(2)\)，再对商取数值 | 数值求值不通过这个商，因为 \(\operatorname{per}(\zeta^{\mathfrak m}(2))=\pi^2/6\ne0\) |
| 纯 Tate/临界 L 值的周期公式 | \(\zeta(2n)\)、\(\beta(2n+1)\) 的纯 Tate 奇偶与这里的扩张奇偶不同；不能由已知 Euler 公式推出难值 |

一个具体逻辑检验是：当 \(n\) 奇时，实数1在 \(\mathbb C/(2\pi i)^n\mathbb Q\) 中也是非零类。因此“扩张类非零”单独不排除其某个实代表为1。这个检验只说明 Hodge 非零性命题不足，不主张存在一个几何 ζ 动机具有该数值。Brown 的一般周期框架也把形式/实现结构与数值周期猜想分开处理。[Brown 2015，§3.5、§6.5–6.6](https://arxiv.org/pdf/1512.06410)

Beilinson 原始工作提出更高调节子与 L 值猜想；数域 mixed Tate 所需的重要部分已由 Borel 等结果建立，仍不完成 (PC-Z)/(PC-4)。[Beilinson 1984 原文及英文版本入口](https://www.mathnet.ru/php/archive.phtml?jrnid=intd&option_lang=eng&paperid=73&wshow=paper)

## 5. 可以替代“继续参数搜索”的三个明确目标

### 5.1 有限深度一周期的核：只瞄准无理性所需部分

对每个有限 \(S\subset\{2,3,4,\ldots\}\)，选取 level 4 的实目标动机符号 \(a_n^{\mathfrak m}\)，使

\[
\operatorname{per}(a_n^{\mathfrak m})=
\begin{cases}\zeta(n),&n\text{ 奇},\\ \beta(n),&n\text{ 偶}.
\end{cases}
\]

按上面的 Artin/系数约定工作。提出较弱命题

\[
\operatorname{per}|_{V_S}\text{ 单射},\qquad
V_S=\mathbb Q\,1\oplus\bigoplus_{n\in S}\mathbb Q\,a_n^{\mathfrak m}.
\tag{L1}
\]

(L1) 对每个 \(S\) 成立，就同时给出所有目标与1的数值线性独立，特别是全部无理。项目中的 \(3\zeta(3)+\zeta(5)\) 也在 \(S=\{3,5\}\) 的同一命题下无理：若它等于有理数，便产生 \(V_S\) 中的一条非零数值关系。它没有声称乘积、高深度或整个类别的周期单射，因此显著弱于完整 (PC-4)。**常数1必须包含**：仅证明一个正权方向的求值非零，已经知道，但没有证明无理性。

可把靶点写成“所选动机导子是否保持数值核”。在深度一选归一化导子 \(\partial_n\)，使 \(\partial_n a_m^{\mathfrak m}=\delta_{nm}\)、\(\partial_n1=0\)。若 \(K_S=\ker(\operatorname{per}|_{V_S})\) 满足 \(\partial_nK_S\subset K_S\)，对任何关系依次应用导子就得到各系数为零，因为 \(K_S\cap\mathbb Q=0\)。

这是一条严格的充分论证，而核稳定性仍未证明。它与所需深度一线性独立非常接近；价值是定位需新理论解决的环节，**不是把目标改名后视为进展**。一项可交付的近期工作是建立权 \(\leq W\) 的目标扩张、导子及 Artin 特征的精确正常形，并把任何待审证明中对数字的非法导子操作直接标出。

### 5.2 一个秩二扩张的比较点，而非整个无限类别

对每个 \(n\) 只研究非平凡的 polylog 扩张 \(E_n\)，及其生成的有限 Tannakian 类别。作适当 Tate/Artin 归一化后，其比较矩阵的关键部分可示意为

\[
\begin{pmatrix}1&\alpha_n\\0&(2\pi i)^n\end{pmatrix},
\qquad
\alpha_n\in\overline{\mathbb Q}^{\times}a_n
       +\overline{\mathbb Q}(2\pi i)^n.
\]

这只是允许的归一化示意，不把每份原文的周期矩阵都宣称为该精确基底。非零扩张给出一个 \(\mathbb G_a\) 方向，加上 Tate 的 \(\mathbb G_m\) 方向；有限 Artin 因子不改变维数。提出逐对象的比较点泛型命题

\[
\operatorname{trdeg}_{\overline{\mathbb Q}}
\overline{\mathbb Q}(2\pi i,\alpha_n)=2.
\tag{R2}
\]

若对所有 \(n\) 证明 (R2)，每个目标都超越。它不要求不同 \(n\) 的目标联合代数独立，故弱于整个 level 4 周期猜想。它是一个可跨权的理论目标：为这些特定扩张证明高权周期湮灭子/子群定理，说明非动机关系不能在比较矩阵上意外出现。

Huber–Wüstholz 给出真实的低阶模型：1-motives 的周期关系来自双线性与态射，他们的子群定理把周期湮灭子识别为几何子对象。[Huber–Wüstholz，arXiv:1805.10104v8，Theorems 9.7、9.10，PDF 第94–95页](https://arxiv.org/pdf/1805.10104v8)

**应用范围必须限制**：1-motive 的 Hodge 型为 \((0,0),(-1,0),(0,-1),(-1,-1)\)；\(\operatorname{Ext}(\mathbb Q(0),\mathbb Q(n))\) 在 \(n\geq2\) 有不适合该列表的权间距。共同 Tate 扭转不能消除这一间距。迭代积分是用1形式写成的，也不因此成为书中1-period。tensor 生成类别中的高权对象同样不能自动套用该线性周期定理。没有该范围检查，就会错误地声称 Catalan 已由现成超越定理解决。[同书 Theorem 8.16，PDF 第86页](https://arxiv.org/pdf/1805.10104v8)

### 5.3 从投影符号到真实几何周期与整数结构

较务实的桥梁是：用 coaction/扩张特征先选准所需方向，再构造真正的子商几何对象、Betti 链和 de Rham 类，使该**实际新周期**只含目标值及有理项。随后独立核对积分格子、分母和极小值估计。商环中“令 Tate 值为零”只有符号简化意义；若没有新的实际比较矩阵系数，无法接上无理性判据。

这可以给现有项目带来结构变化：目标从某个固定 Hankel 尾部的参数，转为“给定特征的真实扩张/子商周期，以及能否统一控制其整数实现”。它可能重用 ζ(5) 论文的正性或整数预算，但 coaction 本身不提供本原多项式在目标数上的小值，也不提供 Diophantine 下界。两种工具连接的命题必须单独写明和证明。

对 Catalan，最低权几何对象尤其具体。Bloch–Wigner 函数

\[
D(z)=\Im\operatorname{Li}_2(z)+\arg(1-z)\log|z|
\]

满足 \(D(i)=\beta(2)\)。Bloch 符号 \([i]\) 的边界 \(i\wedge(1-i)\) 在张量 \(\mathbb Q\) 后为零，因为 \(i\) 是挠元。这给出 \(K_3(\mathbb Q(i))\) 的具体调节子周期，仍没有推出其无理性。[Zagier，《The dilogarithm function》，Chapter I §3–4](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf)

可先以这个单周期测试更高周期湮灭子定理的正确表述：需要排除 \(D(i)-q=0\) 的数值关系，并说明这种关系若发生必须来自哪个不可能的动机子商。仅验证 \([i]\ne0\) 或写出五项关系不是足够输出。

## 6. 对项目的研究安排建议及证据分级

建议把后续工作分成三份可审阅的数学交付，而不再增加随机参数点：

1. **无条件结构交付**：构造 level 4 深度一实目标的统一正规形式，明确式 (1)、纯 Tate 项、Artin 系数、每权导子和非零调节子。有限权可精确核验；已有文献覆盖大部分无限结构。
2. **核心新命题交付**：选 (L1) 的数值核稳定性，或选 (R2) 的单扩张比较点命题；写清它较完整周期猜想少了哪些内容。若论证使用泛型性、数值权分次或导子下降，则把它显式列作待证假设。
3. **几何—整数桥梁交付**：针对 ζ(7) 或 Catalan 给出真实子商周期，而非形式商符号；再报告其积分格子和衰减预算。即使失败，也可得到究竟是几何投影、整数结构还是数值泛型性缺失的定理级障碍。

证据等级：式 (1) 及第3.2节条件推导为本文给出的精确代数论证；Brown/Deligne/DG/Borel 的结构命题是原文定理；(PC-Z)、(PC-4)、(L1)、(R2) 分别是原文猜想或本文研究目标。本文没有建立后三类所需的新数值单射性，也没有声称现有方法可在短期内统一证明所有目标。

## 7. 原始文献与本地整理约定

下列本地 PDF 由主任务统一下载和建立 manifest；文件名仅帮助识别，实际版本、发布日期及哈希以 manifest 为准。页码以上按本文明确指定的版本；尤其 Deligne 作者版53页与期刊版41页不应混用。Brown 2014 本地归档为 arXiv v1，本文正文引用的作者 v3 第15页来自相应在线作者 PDF，不应未经核对就把这个页码用于本地 v1。

| 原始文献 | 本文主要用途 | 本地约定及原件 |
|---|---|---|
| Brown 2012, *Mixed Tate motives over Z* | Hoffman 动机基与生成性 | [brown2012_mixed_tate_motives.pdf](/E:/kimi-build/zeta5/literature/brown2012_mixed_tate_motives.pdf)；[Annals 原件](https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf) |
| Brown 2014, *Motivic periods and P¹ minus three points* | 周期单射、奇数 ζ 条件超越、特殊 cyclotomic 层级 | [brown2014_motivic_periods.pdf](/E:/kimi-build/zeta5/literature/brown2014_motivic_periods.pdf)（本地 arXiv v1）；[正文页码所据作者 v3 PDF](https://www.ihes.fr/~brown/MotivicPeriodsandP1minus3pointsv3.pdf)，[arXiv:1407.5165](https://arxiv.org/abs/1407.5165) |
| Deligne 2010, *Le groupe fondamental unipotent motivique de Gm−μN pour N=2,3,4,6,8* | level 4 坐标、Conj.5.6/A.2 | [deligne2010_cyclotomic_fundamental_group.pdf](/E:/kimi-build/zeta5/literature/deligne2010_cyclotomic_fundamental_group.pdf)；[期刊原件](https://www.numdam.org/article/PMIHES_2010__112__101_0.pdf)，[53页作者版](https://www.math.ias.edu/files/deligne/121108Fondamental.pdf) |
| Deligne–Goncharov 2005, *Groupes fondamentaux motiviques de Tate mixte* | Ext、K理论、调节子及复共轭奇偶 | [deligne_goncharov2005_mixed_tate.pdf](/E:/kimi-build/zeta5/literature/deligne_goncharov2005_mixed_tate.pdf)；[期刊原件](https://www.numdam.org/article/ASENS_2005_4_38_1_1_0.pdf) |
| Brown 2015/2017, *Notes on Motivic Periods* | 形式周期与实值的边界、primitive 扩张 | [brown2017_notes_motivic_periods.pdf](/E:/kimi-build/zeta5/literature/brown2017_notes_motivic_periods.pdf)；[arXiv v3，2017-02-22](https://arxiv.org/pdf/1512.06410v3) |
| Huber–Wüstholz, *Transcendence and linear relations of 1-periods* | 子群/周期湮灭子定理及适用范围 | [huber_wustholz2018_one_periods.pdf](/E:/kimi-build/zeta5/literature/huber_wustholz2018_one_periods.pdf)；[v8，2022-04-21](https://arxiv.org/pdf/1805.10104v8)，首次 v1 为2018-05-25 |

补充原始参考是 [Borel 1977](https://www.numdam.org/item/ASNSP_1977_4_4_4_613_0.pdf) 及 [1980 勘误](https://www.numdam.org/item/ASNSP_1980_4_7_2_373_0.pdf)、[Beilinson 1984](https://www.mathnet.ru/php/archive.phtml?jrnid=intd&option_lang=eng&paperid=73&wshow=paper)、[Zagier 2006 的作者 PDF](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-30308-4_1/fulltext.pdf)。Brown 2014 的 *Irrationality proofs, moduli spaces and motives* 是另一篇文章，不能把它的文件名或论点与本表的 *Motivic periods and P¹ minus three points* 混淆。
