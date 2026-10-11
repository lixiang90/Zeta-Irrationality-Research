# 本轮整格、真实扩张、分母与holonomy接口：root独立审阅

日期：2026-10-06。旧数学稿、脚本、JSON及manifest全部只读。
root本轮只运行两个自己新建的数学producer，各恰1次；没有执行或import旧/peer数学producer。
同行quarter另运行自己的NEW verifier1次；root只读其代码和证书。
本稿不把root自己证明的自查称作独立审阅。

## I1. 实际阅读对象及版本

root本轮实际全文读以下同行最终数学稿：

- [实际消失循环轨道整格](cdt_odd_R0_actual_vanishing_orbit_lattice_20261006.md)，
  SHA `baf29ee041a0ea48c4b64c517cf0712f24c52c4c98893e4c74a98698c7e05586`。
- [真实regulator Betti扩张与原点旗标](cdt_odd_R0_regulator_Betti_extension_flag_20261006.md)，
  SHA `4abdcbc370b69413b07e837724867897760f493b7ee65e6d0b47a705f96292f4`。
- [最高对数旗标与CDT接口](cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.md)，
  SHA `af728ecbebe3ac4827f7388706d4c5892896437e625e1bf4a0671b949bff28b5`。

真实扩张稿初读快照为 `6e58db381dca549e7a60e4b69f293fb11b943eff0f2290bce1c7a6f3a005dd6d`。
root发现B11把参数方向错写成y0外积；quarter独审也独立发现。作者在冻结前修回g0外积家族，记录该错误与修订；root实际补读最终B11和全稿。
holonomy稿初读快照 `0ba7aa00cd7d9117eadbcb134b0a374d4e6dec52b14afcd5b35bf8a81a92e338` 后，
作者补明常数系数范围及映射边界正则性；root对最终版实际补读这些段和全稿。
一批工具总输出发生截断，已另分段补读Betti尾部及holonomy开头；未把截断本身算作全文阅读。

另实际全文回读冻结Yukawa/scalar稿，特别Y8–Y10/Y27。
root的[新二进制分母证明](cdt_odd_R0_conifold_effective_denominator_20261006.md)
SHA `fea01700aa99716201ad0e36b161557f98f8e783755d7bfe144f434d1d59d3f8`
已作作者最终全文回读，独立审阅由quarter另稿承担。

## I2. 真实周期整投影的几何升级通过

共同resolution的两map是smooth proper同维degree one；degree64 quotient不在这个图中。
普通pullback与Poincare-duality定义的pushforward在free integral H3上都存在。
已证的qi=id_Q因此提升成qi=id_Zfree，而不是另猜整矩阵。
伴随性使i保持中间cup，并使Π=iq成为整数正交幂等投影。

因此实际rank-four sector中的格是饱和且unimodular；这不要求整个X的H3只有四维。
投影在finitecover上构造后，由唯一正交投影的deck不变性及逐纤维整性下降。
旧稿未认领此整性保持其历史范围；本轮给出了新的完整证明。

实际signed transport U=-M0的轨道由compact integral cycles生成。
任意整数k的交叉数

\[
\delta\cdot U^k\delta=\frac83(k^3+2k)
\]

来自真实Frobenius logshift与cup常数，不是四个样本拟合。
Gram的Pfaffian为−256，det为2^16；给出的整基变换确得8J与−32J。
故intersection Smith是8,8,32,32，饱和unimodular格内的实际轨道index恰256。
该Smith不是包含映射的Smith，作者明确保留区别。

N3=(U−1)^3=vℓ，其中v=(-1,3,-3,1)、ℓ=(1,1,1,1)；整最高log行与真实doubleloop的额外8均正确。
ΓV=v/2依赖整个period germ的单射，不依赖单点period值。
剩余real cycle α=(-3,4,-1,0)确实是actual integral组合。

unimodularity及N3z=(z·ΓV)ΓV/4使ΓV必偶；其实际divisibility只限定于2,4,8。
δdiv只可能1,2；α的模2轨道各自全交叉为0，稳定isotropic平面至多二维，使α必偶。
α·Uα=−64再限制其divisibility为2,4,8。没有选未经证的primitive case。

## I3. Selected regulator的整数扩张和CRT通过

由真实标量身份W=−aQ(Rc,ω)/16、origin W=√xB和完整conifold log投影，
采用physical Betti回路的cocycle确为c0=0、c1=PDδ。
推断使用完整局部period germ及cyclic非退化性，不能替换为单点数值比较。
两自由生成元与整数monodromy使所有word的cocycle都整数。

scalar rank-five系统需要整体χ twist，origin是diag(U,−1)，conifold矩阵的源列为δ。
所构造的整格属于actual free Betti扩张；它不是整higher-Chow completion，也不是整数Taylor比较的证明。
Γ/8修正的安全cochain费用≤4、所有word的cocycle费用≤2；不声称这些是最小值。

rank-five通用CRT分母16，最高log算子通用分母2；rank-nine通用对应分母256及32。
每个分母由单首最小多项式约化后的最高次系数得到，不能免费用一个整多项式替换。
然而在actual centered origin splitting上，两谱投影与最高log算子都是整格算子，费用1。
这些局部谱投影不与conifold作用交换，因而不是全局horizontal algebraic gauge。

B11修订后的实际家族是

\[
\Phi(q)=Y_{h+qg_0}\wedge Y_{g_1}\wedge Y_{g_2}=\Phi_h+q\Phi_0,
\qquad \Phi(\alpha_0)=Y_\Psi\wedge Y_{g_1}\wedge Y_{g_2}.
\]

以y0外积平移不会改变N3旗标：收缩的像在y0正交空间内，所以初稿公式必须纠正。
最终g0家族及“旗标零当且仅当q=α0”与冻结E10–E11一致。
g1,g2在所用解析规范下的Betti/de Rham矩阵仍未取得代数或整数坐标，不因整单值作用而完成。

## I4. 线性单值化障碍及精确CDT费用通过

实际九维representation有primitive五维不可约商和四维不可约bottom，Ga4平移将非零商向量送入非零bottom。
所以任何稳定子空间只要商像非零就包含全部九维空间。
canonicalorigin的g1,g2平面包含v但C(y0,v)不为0，故不是唯一N稳定二平面kerN2。
所有非零偶数loop都在primitive商中留下非零jump；奇数loop另有χ负号。

有限代数cover不改变connected Galois closure。
一个代数row的scalar若亚纯，其evaluation kernel含上述非零商jump；稳定性迫kernel为全九维，row只能为零。
因此有限cover、固定有理微分算子与常数层不能保留目标方向并使此canonicalorigin变亚纯。
该结论没有排除别的transportedword、非线性新packet或新的vector-valued holonomy定理。

九个规范scalar在|t|<1全纯而t=1非亚纯，故各自真实Taylor半径恰1。
固定logweight在列明norm comparison条件下仅改变O(D logD)，不能改变D2主项；其parabolic原点atom也为0。
这些范围限制保留，未泛化为对任意奇异metric的绝对障碍。

十行species依次为(0,6,6,6,6,6,7,7,7,7)，共同六列cutoff1、额外一列cutoff6，
给精确τ=6(1−1/100)+(1−36/100)=329/50。
Cn缩放同时改变解析numerator与denominator；数学稿保留全部费用及映射边界正则性。
数域版本需要全部embeddings上的实际亚纯maps及全部有限place账本，不能从一条Q公式宣布超越性。

q=0无条件是真正Q算术packet且实际含1rank10。
对actualq与q=0共同适用的解析域，CDT必要不等式已经由q=0强制成立。
所以只改善共用费用或共同cover不能得到排斥actualq的矛盾；新值敏感branch或新representation才可能改变该结论的前提。

## I5. root分母自查、独审责任和未填的接口

作者新证明把actualP转成t=4z、diag(1,2,4,1,1)的系统，所有regular coefficients在Z2，
留数R2=0且2|R。直接(nI−R)−1=I/n+R/n2使每步费用max(k,2k−1)。
整初值递推给全部n的

\[
2^{2n+2v_2(n!)-\lfloor n/2\rfloor}c_n\in\mathbb Z_2.
\]

非齐次源由(1−t)−7/2纳入第五坐标，故h同界。乘积、积分及固定导数的费用也在正文给出。
符号身份13项通过、有限prefix180项吻合，只是自有NEW证书；全尺度依据归纳证明。
quarter另作独立审阅，root此段不是独审自己。

Fischler–Rivoal Theorem3四个前提实际核读：奇素数的无极点、nilpotent留数及Gauss≤1可直接验证；
genericradius1仍要独立输入。p3的额外指数是2，不能漏掉，且其增长只是多项式。
新归档Katz35页，actualPDF9–12与23、visual10/23明确其F晶体开单位盘收敛和proper smooth/deRham局部自由前提。
本轮没有把“几何来自Q”替换为“所有奇素数radius1”。

截至上述root分母稿及其来源收据冻结时，仍未完成：解析g0,g1,g2到真实Betti整格的算术比较、所有奇素数genericradius核验、
以及只属于actualα0的有效解析叶或适用最高log边界资料的新holonomy定理。
本轮是结构和分母证明的实质进展，并给出当前线性路线的严格障碍；没有新的经典奇ζ/L/Catalan数值无理性、线性无关性或Lean定理。

## I6. 同轮后续的全部奇素数整几何与有理晶体接口

root实际全文读toric的新整几何稿，最终SHA
`bde766ee2c7825c9b7a3de7bb77ee4a2b42983a51ab2fc8f6bd28c9cb16e323d`。
同一个fixed coherent regular原格fan在Z[1/2]上成立；normal coordinates和units的overlap glue保持monomial ideal。
surviving cone characterℓ在饱和quotient格primitive，理由是实际pole exponent−1，不是char0秩计算。
所有orbit projection与normal-corner Jacobian由integer torus basis及unit得到；interior只有critical value256。
二次discriminant在λ−4Φ上有实际simple divisor，给odd geometricirreducibility；boundarydimension≤2排掉独立三维components。
S2–S8的projective smooth geometrically connected all-odd family及split relative SNC通过纸面审阅。
这没有证明integral de Rham locally free。

root实际全文读新all-odd算术稿，初读后作者加强relative comparison和literal εspecies，root又实际完整补读最终A3/A8与来源范围；
最终SHA `439a21b2bdf35eeffcbf46e016b35e6ad3b11b635baa8e4148d6533741f6dc5a`。
Morrow实际PDF1,2,5,6,7,10,11与metadata/hash已读，非宣称全部12页；Bhatt–de Jong十页本轮实际全文读。
首读BdJ在PDF1因gbk字符输出中断，改UTF8实际补读PDF1,6–10，再补2–5；不计失败输出为全文读取。
Morrow Prop2.1/3.2/6.1/Cor6.2确给proper smooth rational convergent F-isocrystal，不要求integral cohomologyfree、torsionfree或p>i。
BdJ印刷theorem基底为Zp，NEW A3自证relativeA版本：PD variable导数/积分不除n、Čech–Alexander effectiveepimorphism与surjective transitions、相对forms双复形两谱序列、formalfunctions。
第一base PD diagonal的crystal comparison与relative de Rham代表相容，其firstdifference同于transitivity definition的GM连接。
因此不是由相同rank偷换actualGM，也没有由先取integralH3再任意basechange冒称无Tor。

actual compact cohomologicalP、cyclicrank4和dual在Qp上成立；odd sqrt-coverétale。
在residue超越的Gaussgenericdisk上所有fixed rationalgauge的nonzero denominators及det无零，故G4继承开unitdisk水平收敛。
G5 determinant公式给G4inverse同收敛；source Kummer factorpodd integral且analytic，variationconstants integral除n+1仅logvaluation。
所以actual G4/G5所有奇素数genericradius1已完成；root旧D14保持条件性历史范围，由此NEW稿补其输入。

FR μ4的odd exponent为p3:5、p≥5:3；μ5为p3:5、p5:8、p≥7:4。
和root全n dyadic界相接，确得A2的g全odd LCM3+p3extra2，以及A3的h LCM4+p3extra1/p5extra4。
paired packet不直接用h，Fi积分另付一层，fourZ LCM7、fiveMixed LCM6；p3两g的额外费用完整留为P3(N)=3^{4 floorlog3(N+6)}。
固定B25、d0、16^N及D_(N+6)的A12/A13包含全部place、全prefix。
不能把literal pureLCMspecies直接套此strict型；A8明确核degree/gradedheight扰动O(DlogD)，并另给固定ε的真实整除
P3(n)|3^{4 ceillog3(14/ε)}D_floor(εn)^4与fixedshift清除。
逐ε增加四列cutoff1/bε后τε=(1+ε)329/50+3.96ε，极限回329/50；固定dε不改变D²项。
该直接转换通过，不把“polybound”误作整数整除。

root未执行此稿或同行任何数学producer；本段是独立纸面/原件阅读。
两位同行另独核整几何及Morrow/BdJ/FR→actualP全部条件。
剩余真正缺口为实际Taylor/Betti算术比较和目标敏感解析输入；allodd genericradius及有效C不再列为未解。
q=0真实rank10 reference仍满足相同C16模型，共同解析域优化不能排斥actualq。
本轮没有特殊值无理性、线性无关性或Lean数值定理；项目内部证明与审阅不等于外部发表认证。

## I7. 新数域缩放补充：全places费用与rank不复制

root实际全文读[NEW数域补充](cdt_odd_R0_dyadic_number_field_scale_supplement_20261006.md)的7af55候选，
quarter独审后作者只澄清q0 reference先定义于Q(√2)再extend至同一个实际L；root实际补读最终K14后的该修订。
最终SHA `5a800387513a2f6593087991d5371dbfca47eb8c6c1b74971fe13e3965f4c2b3`。
L=K(√2)、a=8√2具有a²=128；按v_p(p)=1归一，每个2-place的v2(a)=7/2，odd places全0。
root已证的b(n+6)+4≤3.5n+25因此确使2^25d0a^n清完整dyadic费用；P3和D_(n+6)odd费用不变。
a integral、P3/D非减整除，故a^N清整个prefix，没有把averagevaluation误当逐place整性。
每个σ的qσ是算术共轭参数，aσ=±8√2；ψσ=φσ/aσ使变换后germ pullback恰回f(qσ)(φσ)，正负embeddings均实际记账。
双边analytic scale都减ρ=(7/2)log2。finite coefficients只呈每个p的polynomial growth，unitdisk可用。
extension不制造更多functions，实际rank仍10；Z-rank乘fielddegree由normalizedslopes除回。
每个K-embedding上方的L normalizedweights合计回原weight，没有degree2复制容量。
固定ε整除及τεlim照主稿，故K13确给完整all-place改进，主指数费用较log16少(1/2)log2。
K14 productformula下界只对“所有2-place必须v2(b)≥7/2、odd v(b)≥0”的条件scale类；
没有实际periodcoefficients的matching下界，所以不称实际模型最优。
q0模型在同一个实际L与同一全部σmaps上仍强制相同不等式，故shared-domain no-go没有解除。
本补充纸面审阅通过；不执行producer、不增加PDF、不把数域扩张当数值定理。
