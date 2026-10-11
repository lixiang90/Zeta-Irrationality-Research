# 本轮真实像秩、36顶点费用与固定三种子归约：root综合核验

2026-10-06，NEW。既有471项数学输入、历史失败源、成功数学PY/JSON与同行producer全部只读。本审阅只记录实际静态阅读和纸面推导，没有执行/import任何旧或同行数学源。本轮root自有single-bordered NEW程序仅FIRST1一次PASS142；本审阅不是第二个数学producer。

## R1. 实际阅读范围与最终数学指纹

- quarter主稿 `cdt_odd_paired_actual_unit_sector_rank_20261006.md`，e4830013ad948599c4e1bb76113aeed3a8b6df23b32a9d575052cd97d7f6fac8：实际完整读U1–U10及U1–U21两次，均无截断。PY e64add398faeae06855192fcc46a352702f156b191f3668db9dc83e3a6c82b1c完整静态读；JSON a0f74c85d2da7343eb1422091bf8670799eff675ad4f7f158976d70ce62bb6d5整个syntax parse，全部metadata及首末两个完整case字段实际读，未声称root逐字段人工读全部143记录。
- toric主稿 `cdt_odd_paired_weighted_jet_global_optimization_20261006.md`：实际全文读候选b25dd84151e645a3efe1c1fa0816df919fcffd460537e8d2f0015530c7a8408d的O1–O11/O1–O20；未冻稿仅纠正O18费用左端和标签，root实际完整补读O10整段，最终SHA1b7923801d7ff734d278163350d661516abf78fde0687976c4db1d6ef4c6f34f。成功PY1e8c6a6000a70a8484e69536da6e09946bf65000545a16d58a053de241ac54d3完整静态读。JSON5bb704e25707379253bb7733d86c44a354c917bc4c12b96fcd34dfda70bf2863完整parse，metadata和首末记录先读；首次合并全113行输出有截断，随后单独按明确字段次序完整补读113行每个字段，无截断。不冒称人工重算266036检查。
- arithmetic主稿 `cdt_odd_paired_fixed_middle_gosper_reduction_20261006.md`：初c539全文Z1–Z23已读，新增single-gate接口后最终f988d6629b01188f175fabcfa0e87fc58d51d1bf482fda8196d1fd67f2bad4c7再次实际全文完整读11节。PY4b6dce00c79c0d26d89a418af05966d8f8a7ada32b00ce636c9de20b6576b012完整静态读，JSON05907586c7113e74a9e47960de7561f0eb2964a5d56973cb51fd4e333e348b28全部字段和三cases完整读。
- root自有 `cdt_odd_paired_single_bordered_nonzero_gate_20261006.md`，a60d8116c88581028669d9a91aaaf1b848761fcfc4a37b089ca6e5b490b590f8，最终全文自读；PY84e3c06bb135ec57235880fa1490afe4a9c17e07fef62541219ce99e329e1cb3完整静态自读，JSON0273fdab538337a3a617aaed658db0e9a2e6559c91de65fc20448942a493b3ba全字段完整读。本文件对root数学属于作者自核；独立核验来自quarter另存的正式review，不能把作者自核写成独审。
- quarter正式single-bordered独审 `cdt_odd_paired_single_bordered_nonzero_gate_independent_review_20261006.md`，cdd45a63d666383c0953af77a91578996a01ddb761096a131f6383600df6a7a7，root已实际完整读V1–V6。其最终a60d全文、aux原稿、静态PY和JSON范围准确；该review没有冒称新primary阅读。

root本轮已实际全文重读冻结actual auxiliary原稿A1–A13、modified target T1–T27和weighted W1–W10，仅读。本轮另外完整只读冻结全prime预算JSON7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b所有metadata和50affine rows；与toric源码47literal逐段静态对照，恰合并46/85、5/6、7/4三个同raw affine分点，没有删除raw变化。

## R2. quarter：真实配对约束及准确延拓

头部Newton evaluation对整数头部是split surjection；primitive rows在互不交pair上且各两系数互素，所以C满射，A_Z/pA_Z恰ker(C modp)，不仅是必要raw约束。ψ基degree triangular diagonal为p-unit，保留完整底Q层及只有R参数的顶层。

unit-tail负pole residueρ对应positive head residue−ρ。由实际d_m factorial算高carry h+1恰ρ≤r6，unit sector全部高carry；reflection是σρ=V−1−ρ。unit/nonunit primitive row强迫高carry的unit侧head值为零，方向与qP(m)−pP(m')准确一致。内部unit/unit pair给一条独立约束，因此f=au−a(2u−V)_+/2=a min(u,V/2)。固定residue时V odd迫a even，无fixed整数site，f仍整数。

Q≥a时底Q层对a个unithead节点满射，故unitsector像最多Qu+min(R,u)−f。Q≥a+1时，先选真实allowed globaltop，再用outside各自由底Q层将至多a+1个head值消零；不随意改top。所有primitive rows满足后由split surjection升回原S坐标characteristic-zero解。故这个范围像秩准确；Q=a剩余窗口只用上界。

unit-tail有足够互异ψ节点消掉整个degree≤Q local polynomial，scaled derivative同时零，故实际weak核可调用whole-X DND，两侧各付p，v≥−10n+2k。没有任意subset jetrows免费减f。独立窗口4/7<x<3/5面积13/1176+1/120=19/980通过纸面核；全窗口合并必须共同max。

## R3. toric：共享信用flow与精确36顶点

fρ的普通边际是w重复Q次、w+2重复2q−Q次、w+6重复两次，Q≥1时q≥2Q−1确保顺序。特殊第Q+1槽折扣2，其前面价格w，获信用后也是w；Q0的第一槽按q≥1或q0分别价w+2或w+6。前缀交换若删已获信用的特殊槽，只会减少信用使用；若换普通后槽，前槽价格不增。故有总R信用容量的整数flow与原Ω精确等价，未把信用免费复制。

非边界flow edges若含无向环可作双向扰动，extreme点不允许；自由edges成forest，整数balances沿leaf消去迫所有flow为整数。有限compact槽位多面体加两个向上半轴后仍polyhedron；在最小费用处存在费用系数正的active inequality，其credit-capacity系数非负，给attained dual和complementary slackness。该证明完整给出strong dual，不依赖泛称greedy或未验证matroid。

η<0时coupon更贵可舍弃并改η0；λ<0不胜λ0η2的0；λ>11全部槽被选，斜率d−总槽数<0，可退至11。rectangle内仅λ=整数槽价和λ+η=整数特殊价的折线，所有vertices为整数λ与η0/1/2，36格点足够达到Ω。即使不调用equality，每个candidate已有独立合法lower bound；费用定理不依赖实际Gram达到该Ω。

continuous type以e+1替换nc产生统一O(1)，Q≤12、q≤24、槽数≤50使保守1100误差足够；floor端点使用实际integer公式，smallprime保持旧o(n²)界。源码静态保留全部branch/min/positivepart根，再加所有affine pairwise交点，闭端点逐项支配、cover及exact area检查给可审核证书；中点只选已证明affine的branch。

## R4. 有效整化费用及重叠控制

准确重现baseline A471=224674976889262531/5354135180994600。仅Ω的paid信用1433895329207009209/2765986534444032900，合并actualpair后信用4594551260881450309261834591/2837232739731183068973297600。新共同费用为

\[
A^{safe}=68678357676574195925297901887/1702339643838709841383978560
=40.343510723692\ldots.
\]

其定义是合法signed rational整化scale Q_n：D_A/Q_n∈Z[X]，log|Q_n^{-1}|≤A^safe n²+o(n²)，保留负valuation分母与正valuation共同内容。它一般不是raw最小整数分母的上界，不能把跨prime正content信用叫作raw denominator减少；O18未冻标签已据此修正，成功源/JSON数学不改。

纸面可独核的新Ω窗口2/3<x<17/24有v≥48n−78p，相对baseline提高34−48x、面积1/24；2<x<16/7另得提高16−7x、面积2/7。quarter19/980已经包含共同max，不能再加；Ω-only和combined也不能相加。本轮改善属于同一个S和D_A，实处没有用localGL更换基。

费用仍是安全上界，非actual content等式、cost lower或no-go。它尚未与已证同对象解析率>12.00357285412558形成strict margin；该下界未压过上界不等于真实方法必失败。

## R5. arithmetic：三个无目标norm分母算子的归约

actualSy(k) factorial/Wilson比值给h=(a+1)_k/(-a)_k，fixed parameters (13/18,5/18)，k=a+1确是首分母极点。三个算子在g(1−y)=g(y)的对称空间上输出even，最高coefficients是n+10r+2、n+50r+10、n−30r。第一条临界范围严格在1..p−1；D5的首非负resonance n4r−7在cutoff4r−8之外（r≥2）；D−3 resonance n12r−1在cutoff12r−6之外。三角且维数匹配，故C无seed、G两seed、H一seed的唯一分解成立，不除未知Hankel norms。

j1/5在全cutoff的upper flux须直接最后节点计算，不能将0乘undefined h_(a+1)当0；所得fullflux与middleflux准确给C两个负boundary、G full负/middle正boundary。负三次的full flux是真0，middle仍为负，Z15–17符号全部吻合。r1的G onlyconstant单独处理，无虚构第二seed。

Good constant-term递推在positive三参数时用Lagrange identity，zero边界对缺参数变量取CT余Vandermonde，唯一multinomial给Dixon alternating cube；展开符号(−1)^3a再shift l=a+k恰(−1)^k。15r<p且阶乘无p分母，full cubic为unit合法。然而B0保留真实incomplete middle，不能从fullunit推出B0unit。

原M5全部entries准确归约到三个指定实际值A0=G1、A1=G(y²)、B0=H1及显式两端点矩阵。detM5=P_{r,p}(A0,A1,B0)，总degree≤4r、A/B combined≤r、C≤3r；没证明generic非零，更没证明真实值非零。direct middle mask degree≥4r+1只排除此node空间bounded-degree捷径，不否定其他几何表达。

## R6. root新single-bordered结果的角色

quarter正式cdd独审通过actual halfjet、whole-X归一化、两个known-unit Schur以及congruence因子。它们严格证明p^(17m)D_A modp=known unit·detM5与corank equality，G0不必unit。若M5unit而G0 corank g，scaled actualGram Smith为0^(5m/2−g)、1^(2g)、2^(3m/2−g)，不继续称0/2分布。

另一个条件性higher-layer接口是N(X)−N(c)∈p³(X−c)Mat；若N(c)可逆且最大Smith指数≤2，归一化det whole-X reduction恒unit。depth3的diag(p³,1)例精确失败，阈值不能扩大。实际higher-layer条件未证，没有把一般toy或19finite perturbations当actualλ2数据。root actualr1/2/4比例identity只验证机制，不扩辅助素数表。

## R7. 新primary与实际scope

root actual新读Caruso PDF49–53五页，Elsheikh–Giesbrecht PDF1–5五页，Gosper PDF1–3三页，Adolphson–Sperber PDF1及14–17五页，总18distinct页。归档分别76、24、3、22页，总125页，不称全文125页读过。后两篇路径/URL由arithmetic候选来源收据完整读取；该candidate阅读不冒称随后final receipt已读。

Gosper印刷算法的shifted gcd及characteristic-zero degree分析不能免费转modp，当前算子有自己的临界nonresonance证明。AS Theorem6.6针对明确exponential-sum family、A、e与minimal digit profiles；root实际PDF17确认非零Hasse polynomial并不等于固定specialization非零，PDF1 Legendre λ−1在p3mod4的相消例亦可自证。当前三个种子尚未识别成同一fixed cohomological family。

Caruso determinant precision的最大Smith指数条件和Elsheikh–Giesbrecht eigenvalue/Smith反例没有被误套成实际higher-depthunit；其generic density的p相对dimension条件也不覆盖当前p线性增长family。所用Schur、Smith阈值与flow定理均自证，文献只拓宽方法并核适用边界。

## R8. 审核结论与未完成目标

通过：actualpaired unit-sector rank及精确延拓；whole-X核信用；共享coupon flow、36vertex Ω与合法共同max；signed same-S整化scale费用改善；fixedλ2全临界Gosper/三seed与显式boundary；rootsingleM5leading gate经正式独审通过。

本轮四个作者NEW各FIRST1PASS，失败0、rerun0、旧/同行数学execute/import0；root不运行同行程序，不再扩auxprime表。全尺度定理依赖上述纸面步骤，保存证书只核实现和精确分段，不证明无限nonzero。

仍缺：无穷actual detM5=P(A0,A1,B0)非零或真正higher-layer替代；fixed rational candidate的无限D_A非零；足够同对象strict margin；能够用于新ζ/L/Catalan目标的完整周期/整模型接口。没有新的特殊值无理性或线性无关性定理，没有Lean认证，研究goal继续active。

本稿最终完整回读后冻结。随后独立crossreviews和final来源收据的实际读取由新的root finalreceipt及主报告登记，不倒写此稿冒称已经读到未来元数据，也不pin可变main/auditor造成循环。
