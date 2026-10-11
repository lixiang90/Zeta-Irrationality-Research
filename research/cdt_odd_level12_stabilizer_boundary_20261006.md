# D12 原点稳定子的尖点限制、上同调信息与 strip 方法的适用边界

日期：2026-10-06。本稿使用已冻结的[完整群表示](cdt_odd_level12_schreier_presentation_20261006.md)和[真实九生成元周期](cdt_odd_level12_generator_cocycle_20261006.md)，不执行/import任何冻结producer，不作短word或参数搜索。

固定纯L的实际函数 h=fσ,L+Θ、Γ=PSLΓ1(12)、G*=Γ⋊〈M〉。令 c(g)=h|−2g−εg h=iπ³P(g)，并使用原稿的真实整数affine作用。本文证明八个尖点类的**所有共轭、所有非零幂**不能进入原点稳定子，给出其余两个类的准确局部条件；它没有求出全部双曲zero words，也没有宣布新的数值无理性。

## 1. 抛物元的尖点边界类是全尺度的固定点障碍

取实际尖点scaling A∈SL2(Z)、宽w>0、P=A T^w A^-1∈Γ。记B为Fσ,L|4A的常数项。Bol identity保证h|−2A在此尖点具有

\[
 (h|_{-2}A)(z)=\frac{(2\pi i)^3B}{6}z^3+p_A(z)+O(e^{2\pi iz/w}),
 \qquad \deg p_A\le2.
 \tag{B1}
\]

这里未将整primitive假定为周期：差值在z↦z+w下才是degree≤2的Eichler polynomial。由右slash和A T^w=P A，有

\[
 P(P)|_{-2}A
 =\frac{h|_{-2}A(z+w)-h|_{-2}A(z)}{i\pi^3}.
\]

因此其quadratic coefficient准确为

\[
 \boxed{\beta_P:=\operatorname{coeff}_{z^2}(P(P)|_{-2}A)=-4wB.}
 \tag{B2}
\]

p_A的degree≤2项之差没有quadratic coefficient。若A第一列为(a,c)，则β=c²P(P)(a/c)；c=0时取polynomial最高系数。不能把P的一个finite endpoint值不加c²便称为归一boundary class。

在普通basis(1,z,z²)上，R_(T^w)−I的image恰是degree≤1空间，rank2。于是抛物affine作用有固定点，准确当且仅当β=0。其固定点若存在是一条affine line；**β=0不意味着原点就在该line上**。

对P^n，n≠0，quotient V/(R_P−I)V上的translation乘以n。非零β仍非零，故A_(P^n)没有任何固定点。任意G*共轭只是affine共轭，保留“没有任何固定点”。所以

\[
 B\ne0\Longrightarrow c(gP^ng^{-1})\ne0
 \quad(g\in G_*,\ n\in\mathbf Z\setminus\{0\}).
 \tag{B3}
\]

这个结论不依赖chosen origin、不依赖affine action properness，也没有使用signed M的正锥假设。

## 2. 完整十尖点：八类全排，两个局部允许

下表从完整parabolic words和真实九period vectors重推，并以(B2)核对全部source constants。所有A、宽及matrices取实际完整Schreier表。这也有一个不依赖period table的固定source检查：令u_j在j=1,2,3,4,6,12上为1217,−14082,6255,−11120,126738,−175248，d=2880，κ=24√3。对scaling A的第一列(a,c)，普通E4旧形的常数为

\[
 B_{\rm triv}(c)=\sum_{j\mid12}u_j\left(\frac{\gcd(j,c)}{j}\right)^4.
\]

χE=E4(1,χ12)只在12|c的slot有常数23χ(a)，χF=E4(χ12,1)只在gcd(c,12)=1的slot有常数23χ(c)/(144κ)，其余slots为0。前一式可从primitive Gauss sum的support读出；后一式同样由character orthogonality给support，而Fχ|4S=κ^-1·12^-2 Eχ(τ/12)给常数大小。对coprime c，选n使d_A+nc divisible12，则A T^n S^-1∈Γ0(12)，Nebentypus χ(−c)=χ(c)给相应符号。因此本纯σ source的character部分准确为

\[
 B_\chi(A)=66240\left(\mathbf1_{12\mid c}\chi(a)
       +\frac{\mathbf1_{(c,12)=1}\chi(c)}{144}\right).
 \tag{B2a}
\]

全部10个actual A的普通部分依次为−66240,−66240,460,−36160/3,13785,13785,−73520/3,−73520/3,460,108480；character部分依次为66240,−66240,460,0,0,0,0,0,−460,0。相加就是下表的B，不是只对几项数例归纳。本文不把此χ-slot公式推广到其它conductor/新source。

|id|Γ cusp|w|B=const(Fσ,L\|4A)|β|affine fixed point|
|---|---|---:|---:|---:|---|
|1|∞|1|0|0|有|
|2|−5/12|1|−132480|529920|无|
|3|0|12|920|−44160|无|
|4|−1/2|6|−36160/3|289280|无|
|5|−2/3|4|13785|−220560|无|
|6|−1/3|4|13785|−220560|无|
|7|−3/4|3|−73520/3|294080|无|
|8|−1/4|3|−73520/3|294080|无|
|9|−2/5|12|0|0|有|
|10|−1/6|2|108480|−867840|无|

M在尖点上配对(1,9)、(2,3)、(4,10)、(5,7)、(6,8)。所以在G*的五个peripheral conjugacy classes中，只有(1,9)通过(B3)的必要条件；其余四类的任意conjugate power都不能稳定原点。这不是K=c^-1(0)自己的尖点计数：一个G*尖点类可在无限指数K中分裂成多个乃至无限多个K尖点。

P1=T的实际period为0，固定line是常数polynomials。P9的实际PL vector为

\[
 (-197310720,-994765440,-1253721600),
\]

本身并非zero，但在−2/5处的β为0，所以它有affine fixed line。另一conjugate M T M^-1确为zero，不能从表中P9非zero就排掉整个允许class。

更准确的剩余局部判据是：若P有fixed affine line L_P，则

\[
 A_{gPg^{-1}}(0)=0
 \quad\Longleftrightarrow\quad A_g(0)\in L_P
 \tag{B4}
\]

这里用原稿right action A_(gh)=A_h A_g，所以A_(gPg^-1)=A_g^-1 A_P A_g。只有已知整数affine orbit与这些lines的交，才能继续限制允许类；β数据不能代替这个orbit问题。

## 3. 完整有限上同调与实际gauge：24=14+10不能分类原点

Γ=F9，V=Sym²有dimension3。任意九个V-values都唯一延伸为1-cocycle，所以Z1有dimension27。完整矩阵的coboundary map

\[
 V\longrightarrow V^9,\qquad p\longmapsto ((R_{x_j}-I)p)_j
\]

rank3；本文新证书用实际matrices直接核实。十个(B2) boundary functionals作用在27个free-generator coordinates上，矩阵rank10，并杀掉所有coboundaries。因此

\[
 \dim H^1(\Gamma,V)=24,\qquad
 \dim\ker(H^1\to\bigoplus_{10\ cusps}H^1(\langle P_i\rangle,V))=14.
 \tag{B5}
\]

这个有限rank计算来自完整presentation，不需要假定十cusp relation以外还有未知relations。经典Eichler–Shimura中的14个cuspidal dimensions、10个Eisenstein boundary dimensions与之相容。源是明确的Eisenstein oldforms/χ-Eisenstein之和；但是描述它的cohomology class仍须和**已经选定的真实gauge**区分。

一个明确反例解释为何仅class/decoration不够：令q(τ)=1−12τ²。实际R_M与R_M′均满足q|−2M=q|−2M′=−q。将h换成h+80iπ³q，源F不变，cohomology class和十个β不变，且两个reflection仍zero；但

\[
 q|_{-2}T-q=-12-24\tau\ne0.
 \tag{B6}
\]

T因此不再稳定原点。这个改动破坏原点的q-regular/T-periodic实际germ，**不是另一合法CDT目标模型**；它证明任何只保留H1类和两reflection signs的分类都丢掉必要信息。原q-germ正规化必须一直保留，不能在strip参数化的translation conjugacy中消去。

已有Schreier图也给一个准确ideal-triangulation接口：Farey triangles对应R的16个orbits，unoriented edges对应S的24个orbits，ideal vertices是T的10个cusp cycles。它是Γ quotient的16-triangle、24-edge ideal triangulation；把Bass–Serre图的24个degree2 S-vertices收缩，得到其dual graph，rank仍9。全部连接由已证coset permutations给出，不是从signature猜一个triangulation。

在universal dual tree上，可把实际normalized cocycle实现为real tilewise Killing-field potential。Γ有16个Farey triangle轨道，并不transitive于全部tiles：须选16个tile representatives δ_i，给它们独立seed values s_i∈V，并把一个base代表δ_0的s_0固定为0。再使用左作用u(g)=P(g^-1)=c(g^-1)/(iπ³)、ρ(g)=R_(g^-1)，定义

\[
 \phi(g\delta_i)=\rho(g)s_i+u(g).
 \tag{B6a}
\]

Γ对tiles的作用free（Γ torsionfree，tile stabilizer在PSL2Z中有限），所以这个transport well-defined。相邻tile差给完整三维relative motion。**仅在base orbit**有φ(gδ_0)=u(g)，故u(g)=0准确判定被g移动的base tile仍有value0；其它15个orbits必须保留其seed，不能全都假定由同一个base transitive transport得到。这个全尺度转换始终保留origin。

要把它进一步叫作generalized strip，还须核每条edge的jump属于该geodesic的两维允许plane；要成为positive strip又须额外正性。这些条件不由“源是Eisenstein”或上述dimension count自动成立。即使signed strip表示存在，tree上不同路径的相消仍是全stabilizer问题。

## 4. 文献给出了表示工具，没有替代zero-word生成性

实际保存并定向读取的primary文献：

- [Danciger–Guéritaud–Kassel, Margulis spacetimes via the arc complex](https://www.ihes.fr/~/kassel/Strip.pdf)：印刷pp3–6的主要参数化要求convex-cocompact linear holonomy和admissible、uniformly lengthening/contracting deformation。Γ有十个cusps，且本affine action已有无限T stabilizer，不能直接套用。Appendix A的generalized signed relative motions和局部zero-cocycle关系可作线性表示工具，未给任意原点stabilizer的生成性定理。
- [Panda, Parametrisation of decorated Margulis spacetimes using strip deformations, v2](https://arxiv.org/pdf/2306.09985v2)：实际PDFpp2–3、15–18的对象是有boundary spikes的crowned/decorated surfaces，admissible条件要求所有closed curves和horoball connections一致uniform lengthening。本例是十个interior cusps的cofinite quotient；其topological identification及admissibility都不能省略。
- [Paşol–Popa, Modular forms and period polynomials](https://arxiv.org/pdf/1202.5802)：实际PDFpp22–23，Propositions8.1/8.2准确处理非cuspidal constant terms、extendedperiod和逐cusp Eisenstein basis。它支持boundary与period空间的分解，并不断言c(g)=0的subgroup可由某些boundary loops生成。

本例还有一个与uniform cone直接冲突的真实hyperbolic：

\[
 k=M'M^{-1}=(97,-28;-336,97),\quad
 \operatorname{tr}k=194,\quad c_L(k)=0.
 \tag{B7}
\]

自由word是x7^-1 x1 x8^-1 x5^-1 x2^-1，SL代表可能差central−I，PSL及normalized period相同。Sym²与adjoint representation的识别使c_L为infinitesimal holonomy deformation；c_L(k)=0迫k的translation-length derivative为0。加coboundary只共轭holonomy，不改变marked length derivative。因此这个**cohomology class本身**不可能uniformly lengthen或uniformly contract所有closed geodesics。即使将十尖点适当decorate，也不能把它放入这些primary论文的strict admissible cone。

此外signed linear partεM R_M=−R_M反转time cone；正锥路径的论证必须先分开Γ与signed coset。本文没有以nonproper theorem推出“没有更大的thin稳定子”。

## 5. 完整稳定子仍需的输入及已证范围

可完成的新限制是(B3)：四个G* cusp classes被所有共轭/幂排除；一个class保留准确的affine-line orbit intersection(B4)。全hyperbolic部分需要actual three-coordinate path potentials的全尺度控制，或一个保持origin的fundamental-domain/automaton证明。有限H1维数与arc-complex参数化本身均不给这样的控制。

K不是普通group homomorphism的kernel，一般不normal。事实上本例K∩Γ非trivial（含T）且不可能normal：若normal，非trivialnormal subgroup的Zariski closure在PSL2中为全部PSL2；对k∈K的cocycleconjugation式迫所有c(g)被ρ(K)固定。Sym²无nonzero invariantvector，故c(g)全zero，与η的实际nonzero period矛盾。这是结构提醒，不是新增数值结论，也不排更大的nonnormal thin K。

还有一个algebraic-closure层面的明确限制。令H_0=〈T,M,M′〉为已知zero thin subgroup，令K=c^-1(0)为完整稳定子。H_0∩Γ含T和M T M^-1，两者的fixed cusps分别为∞和2/7。两个不同fixed points的nontrivial unipotent subgroups不可能共同包含在一个Borel里，其Zariski closure生成PSL2；也可由相应Lie algebra生成直接证明。因此**H_0∩Γ与K∩Γ**的affine闭包均为原点的整个linear stabilizer{0}⋊PSL2。这个陈述限于ε=+1的Γ部分：全H_0还包含M的negative signed-linear component −R_M，不能称全H_0或全K的affine闭包只有PSL2。完整双源affine/Galois closure的强结论可排全Γ投影，却不能在这个代数闭包层面区别已知thin subgroup与未知full K。这正是离散origin/path信息仍必要的地方。

已知η unipotent且c_L(η)≠0给K无限指数；已知base/augmented Hecke radii限制固定地图族。本稿不把这些旧结论重称为新成果，不排所有CDT source、所有可用leaf或新的arithmetical improvement。

## 6. 新证书与文献manifest

同名NEW verify.py仅读取冻结period JSON数据，pin其SHA256为b8dfb80d30a4fc276d225d148c76ead7032de51523896664f5c743eb0af966ef；不执行/import其producer。固定九matrices另外逐项pin。74项最终全部通过：全部10个actual width/scaling/parabolicwords、boundary常数与affine fixed-point ranks、27-dimensional自由cocycle到10-dimensional boundary的rank、三维coboundary及14维parabolic cohomology、known zero hyperbolic与显式sameclass gauge。

执行记录准确为三次NEW执行：第一次在k的central ±SL代表检查失败；修正为PSL后，第二次数学checks通过、写JSON时遇到SymPy Integer serialization；转成int后第三次保存74项全部通过。没有旧producer执行，没有word/参数扫描。有限checks不替代(B1)–(B4)的任意幂与共轭证明、真实gauge区别或primary定理条件。

三个新primary PDF共122页，实际只作上述定向阅读。版本、SHA、页数和未扩大阅读范围记于[本轮manifest](../literature/manifest_cdt_odd_stabilizer_boundary_20261006.json)。

实际独立审阅记录：root实际只读全文§§1–6及同名verify.py，独核cusp Bol residue −4wB、全部10个source slots/常数、right conjugate origin criterion、cohomology rank的完整参数化、gauge反例与strict strip定理scope，限定通过。root指出16个tile轨道须各自seed和Γ部分闭包须分清negative signed component；正文已据此修正，没有重跑producer。conjugate_projection实际只读本稿，限定独审§§1–2及§3的显式gauge/left-cocycle部分通过：cubic→β、rank2 quotient、任意非零幂/共轭no-fixedpoint、P9 affine line/原点区别、B4顺序、χslots与κ/144大小、十常数及q的anti/T差；未运行74check，也未认领rank10矩阵或所有primary定理页的独审。本文据此冻结，后续stabilizer或algebraic-closure工作另稿。
