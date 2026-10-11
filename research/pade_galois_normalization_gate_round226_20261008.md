# 第226轮：实际目标的Galois尺度、全处transport与下降准入

2026-10-08，B。固定225的同一实际Δ/Ξ/J；假设ζ7=g∈Q时记H=gD+X=ΣJ_rz^r。数学程序 **0**。本文支付两个自然正实尺度的全部embeddings/norm/finite valuations，以及指定全处坐标transport的严格负入口；并以自含nonsplit例子证明leading characteristic分组不能自动给实际rational projector。没有构造本packet的低阶实际因子，没有新的ζ/L数值定理。

## 1. 封存对象与避免历史重复

实际FULL重读225 [完整basis稿](pade_relation_power_rank_gate_round225_20261008.md)，14444B/SHA `7752b5bfeb3b2090d913b999600695c5a12ffc1c731dd36649d4d89104b5b255`全部七节P1–P15，及[目标径向cap](pade_relation_radial_cap_round225_20261008.md)，5015B/SHA `8d46532cde29b6133687e926e4af02f82e1cf3a7dfbb9f9eaf26a45ff9835afa`全部四节R1–R5。225 manifest49255B/`f2f89ce01ca7e9e56aca9a98185c0ced3c2594c60fe44f26af1fb9d535f79a42`实际读完整navigation/completed_math/remaining_gates/ledger/source-policy字段；未声称FULL所有pins/links，初次raw输出截断不计FULL。

历史实际FULL读[dyadic数域模型](cdt_odd_R0_dyadic_number_field_scale_supplement_20261006.md) K1–K6，7862B/`5a800387513a2f6593087991d5371dbfca47eb8c6c1b74971fe13e3965f4c2b3`：它已明确finite/arch费用及field-degree归一，故“代数尺度可以更精确清分母”不是本轮新机制。实际FULL读[221 actual trace](cdt_actual_trace_transfer_round221_20261008.md)，13182B/`7f267e3c856313435b59a4bcb02d0fd655336c2377d995a851aa058a6642be92`：保秩要求真实stable module与合法图，粗trace无净红利。关键词命中的旧[scaled-root稿](cdt_odd_paired_scaled_root_optimum_20261007.md)，12581B/`c529ece382b5e9959d35210a8ef3675d4ef76fa08ffab60daa232a7f359552e2`亦FULL读；那是积分多项式根分布，不是当前变量缩放。未执行这些历史producer或重做archive检查。

记α∈(8,9)为P(v)=v³−9v²+3v−3的唯一实根，另根β、βbar，b=3+2√3，b'=3−2√3。沿225

`L1=α⁹，L2=b⁹，L3=3⁹，κ=(3/α)^(9/2)，s=(2√3−3)⁹`，

实际目标growth恰为以下二者之一：

`T_s=L1L2s=(3α)⁹，T_κ=L1L2κ=[b√(3α)]⁹`。                  (G1)

没有判定哪一个small connection出现。共同下界是T≥L1L3>(24)⁹。目标有一个模1/T上的非亚纯径向点；凡原目标芽与单叶图相容，导数≤4/T。下文每次缩放均保留这一原径向路径的量词。

## 2. 两个自然尺度的全部共轭与精确finite费用

**G2：平方根已在cubic中。** 令

`δ=3(α+1)/(α−3)`。

由P(α)=0直接有3(α+1)²=α(α−3)²，故δ²=3α；α>8使δ>0。并且

`δ³−3δ²−9δ−9=0，Q(δ)=Q(α)，Norm_(Q(α)/Q)(δ)=9`。        (G2)

第二个身份由δ(3α−9)=9α+9得出，field equality由α=δ²/3。因α的degree为3，该monic cubic正是δ的minimal polynomial。δ因此是algebraic integer；有理式中的α−3不引入未支付的2-adic分母。

令K3=Q(α)，K6=Q(α,√3)。quadratic不能包含于degree3 field，故[K6:Q]=6。全部六embeddings以v∈{α,β,βbar}和w∈{b,b'}编号；δ(v)=3(v+1)/(v−3)，满足δ(v)²=3v。两个自然正实尺度的完整conjugates为

`σ(T_s)=(3v)⁹，σ(T_κ)=[wδ(v)]⁹`。                         (G3)

前者在K6中每个K3 embedding重复两次；后者实际属于K6，无需免费或另收费一个猜测的degree12 extension。T_κ的实选定embedding模严格大于其余五者，因为|b|>|b'|且|δ(α)|>|δ(β)|=|δ(βbar)|；所以它生成K6。类似T_s生成K3。这是有限纸面degree证明，不是root solver。

由Norm_K3α=3、Norm_K3δ=9、Norm_Q(√3)b=−3，

`Norm_K3(T_s)=3³⁶，Norm_K6(T_s)=3⁷²，Norm_K6(T_κ)=−3⁶³`。 (G4)

按field-degree归一后的archimedean logarithmic means分别为

`h∞(T_s)=12log3，h∞(T_κ)=(21/2)log3`。                     (G5)

这里只取平均log|σc|，不是absolute Weil height的正部。扩域后embedding权重归一，均值不复制。

**G3：全部finite places。** P(v)在3为Eisenstein，故每个3-place按v3(3)=1归一有v3(v)=1/3；w²−6w−3亦Eisenstein，v3(w)=1/2。由δ²=3v有v3(δ)=2/3。因此

`v3(T_s)=12，v3(T_κ)=21/2`。                               (G6)

在所有p≠3处，v、w、δ皆为unit：它们是algebraic integers且norm只含3。故两个T也在这些places为unit，包括p=2。K6在3处totally ramified degree6（local ramification index同时被3与2整除，已达6），唯一3-prime𝔭的相应integer valuations为72和63；K3中(T_s)=𝔭3³⁶。没有省掉prime powers。

更精确地，

`T_s=3¹² ε_s，T_κ=3¹⁰√3 ε_κ，ε_s∈O_K3^×，ε_κ∈O_K6^×`。 (G7)

ε_s=(α³/3)³且α³/3=3α²−α+1。ε_κ的全部finite valuations为0，故为unit；Norm_K6ε_κ=1。unit部分在某个实embedding的大值不能当作所有embeddings共同的容量。

complex actual exterior roots也可写成ξ=−(3b/v)⁹，其中v为剩余cubic根，因为αββbar=3。它在对应conjugate degree6 field Q(v,√3)中的norm同为−3⁶³、每个3-place深度21/2；complex ξ不被放进选定实嵌入的K6。这只是真实root product的代数记账，不宣称ξ是T_κ的共轭，更不是已找到actual module因子。

## 3. 自然scale的arch-only严格cap与真正全处transport

设c为T_s或T_κ，定义实际K-valued germ

`F_c(z)=H(z/c)=ΣJ_r c^(−r) z^r`。                           (G8)

关系假设下J_r∈Q，故每个σ的conjugate **仍是同一个H**，只是坐标变成H(z/σc)。若φσ单叶且F_c^σ∘φσ在整个unit disc亚纯，225的同径向Koebe证明应用于φσ/σc，给

`log|φσ′(0)|≤log4+log|σc|−logT`。

取全部embeddings的normalized mean，

`L∞≤log4+h∞(c)−logT≤log(108/8⁹)<0`。                     (G9)

最后只用h∞(c)≤12log3、T>(24)⁹、8³>108。即使暂不计finite费用，这两个**自然scale的arch-only number-field LCM入口**仍没有正导数分母。ε_s/ε_κ的unit scale平均log为0，更不能改变该结果。这里不把单一选定embedding的|c|=T当作全部σ均有相同|c|。

**G4：指定finite transport是另一种完整模型。** 原safe bound

`64³ c_g d_(2r+4)^13 J_r∈Z`

给原H在每个finite place的open unit disc收敛，因为固定p的lcm valuation为O(log r)，fixed64/c_g也不改变root radius。对F_c，在v|3选择实际linear mapφ_v(z)=c z，则pullback正是H(z)，在所有其他finite places选φ_v=id，c为unit所以F_c也在unit disc收敛。这些linear maps在unit disc邻域解析且除有限places外为identity，满足所需family形式。S-integer LCM类型允许S'含3；不把c^(−r)免费写进O_K的literal LCM numerator。

因此此**已明确付清的transport**中

`Σ_(v finite) log|φ_v′(0)|_v=−h∞(c)`，

`L_all=L∞+Σ_(v finite)log|φ_v′(0)|_v≤log4−logT<0`。        (G10)

finite贡献确为−12log3或−(21/2)log3；它不是额外可加的positive conformal credit。CDT number-field local heights还在numerator中包含finite的sup log|φ_v|_v；linear transport对此同样为log|c|_v。若arch maps写成cσψσ，arch Bost–Charles energy加h∞(c)，finite项减同一量，conformal sum与energy同时回到原坐标预算。这个指定transport的scale-invariance是product formula的实际费用结论，不依赖safe166/9最优性。

**G5：不允许扩大范围。** 若改在3处用unit identity并要求F_c有literal O_K-LCM coefficients，则必须另证actualJ的exponential 3-adic content：必要条件是v3(J_r)≥ρr−O(log r)，ρ=12或21/2，抵消c^(−r)；原safe lcm下界只为−O(log r)，完全没有支付这个positive content。若只要求F_c在unit disc亚纯，不要求literal coefficients，则仍须实际付此更大的p-adic延拓，不能把meromorphy与content条件等同。一般all-place定理可以使用另一些positive finite conformal maps；G9/G10没有排除它们，其actual meromorphy/radii/numerator均未支付。另一个projected source的conjugates也可能不再是同一个H，亦不受本文自然scale cap自动约束。

## 4. Leading Galois分组不能承担actual splitting

六个leading roots分为cubic集合C={μ1,ν+,ν−}、quadratic集合Q={μ2,ν0}和R={μ3}。其中prodC=prodQ=μ3=−3⁹。∧³leading products可按

`C3，C2Q，C2R，C1Q2，C1QR，Q2R`

分成计数1、6、3、3、6、1的Galois-stable集合。相应乘积polynomial在Q[t]中，但本文不认证全部20 product distinct，也不把每一集合宣称为已独立认证的不可约actual factor。Root另承担实际observable/leading认证；此处没有运行其producer。

**G6：明确nonsplit反例。** 在Q(r)上取actual rational difference system

`y_(r+1)=C(r)y_r，C(r)=[[1,1/r],[0,2]]`。

其leading polynomial为(t−1)(t−2)，simple、coprime，并有formal near-identity diagonalization：在r^(-1)中逐系数解u(r)−2u(r+1)=1/r，每个新系数的系数均为1−2≠0。然而若存在投到实际invariant lineQ(r)e1的rational projector，则必为P(r)=[[1,u(r)],[0,0]]，intertwining identity

`P(r+1)C(r)=C(r)P(r)`

迫使

`u(r)−2u(r+1)=1/r`。                                      (G11)

这没有rational解。若u的某pole orbita+Z不含0，取该有限orbit的最小、最大整数标签，u(r+1)在左端向前多一个pole、u(r)在右端多一个pole，均无法抵消；故该orbit不可能。对integer orbit，设min pole k_min、max pole k_max，左端k_min−1和右端k_max都必须等于右侧唯一pole0，于是k_min=1、k_max=0，矛盾。若无finite poles，u为polynomial，也不可能等于1/r。论证在任何constant number-field extension中同样有效。

这个例子已有rank1 invariant submodule，**不声称没有Ore rightfactor**；它严格反证的是“leading coprime factors自动支付rational splitting/projector”。对本packet，右因子本身也仍须实际Ore identity证明，不能由formal root grouping移入。这里的pole-orbit证明自含，没有引用未读的Abramov算法定理或执行算法。

## 5. 真正下降的最小可审证书

令C_r为225实际normalized six-state companion，M_r=∧³C_r∈Mat20(Q(r))，h为(0,1,2)外积observable。实际state

`w_g=g(v_a∧v_b∧v_c)+(v_a∧v_b∧v_q)`

在g∈Q时为完整Q-valued列，并有h w_g=gΔ+Ξ，在目标关系g=ζ7下等于J。ζ3、ζ5 nuisance在整个state中由外积恒等式消掉，不能只证明一个scalar asymptotic就换源。

可审projector证书至少需

`P²=P，P(r+1)M_r=M_rP(r)，rank P=d`                         (G12)

及实际target membership或observable identity，保留有限exceptional r的处理。若采用w_g=P w_g，需在一个regular初值及递推中付等式（g关系不能由猜测connection取代）；若仅h(I−P)w_g=0，则必须对全部r付清，不由主阶消失推出。另一可审路线是actual Ore factor𝓛3=𝓠𝓡，且𝓡真实消灭全Hg系数，包括有限prefix。leading factor或formal infinity projector不满足G12。

即便有此证书，difference factor degree d也不是生成函数的最小Q(z)-微分rank d。必须把actual生成函数ODE、完整cyclic source/函数独立性、全部finite LCD/原点异常、目标关系保留、各embedding共同图与energy再付清。数域extension的evaluation lattice rank乘[K:Q]后，slopes也按同一degree归一，没有免费复制函数数。

本轮未找到本packet的actual P或右因子。因此新的明确进展是G2–G10：自然Galois尺度的全部共轭/整性与受限strict negative entrance；G11给leading→splitting推断的结构反例。它不是全部algebraic normalization/descent或所有finite-place优化的no-go。

## 6. Primary与执行范围

实际归档官方当前 [CDT ICM原件](https://math.uchicago.edu/~fcale/papers/ICM.pdf)，653266B/SHA `1b3fe13a89d04c3bc570b78c1130e5a03e33d4c2915ab4b065c3dc248b3eb98f`，20页；实际读完整PDF3–8，含§1.1 normalizedplaces、完整Th2.1、Th2.6的全部条件及§2.3跨页proof/local-height estimates。新原件不同于旧缓存657333B，不混同其身份。所用定性slopes接口的conformal sum为所有places的Σlog|φ′|_v，numerator含arch双积分与finite sup；positive denominator与合法S-integer LCM及共同meromorphy缺一不可。G9是arch-only限制，G10是明确family的all-place限制，没有把它升级为任意all-place theorem。

Abramov1989的Math-Net官方metadata实际读并保存，确认题名/卷页/DOI；英文作者PDF请求timeout，1974页面请求cache miss，没有保存或假称读过论文定理。G11全为本文纸证，不借metadata承担算法正确性。实际scope与来源账见[NEW226读取记录](../literature/pade_galois_normalization_sources_round226_20261008/packet_reading_scope.md)。

数学程序、CAS、root/matrix执行、递推guessing、素数/参数扫描、PSLQ、数值积分、旧producer运行均0。PDF文档提取、来源下载及metadata/hash不算数学执行。只新增本文及NEW226来源/记录，旧稿/main/manifest不改。保存后作者实际FULL复读，final bytes/SHA另报；同行独审另存。
