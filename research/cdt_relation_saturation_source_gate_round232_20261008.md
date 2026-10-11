# 第232轮：关系值饱和、真实q2分母下界与CDT源准入

2026-10-08，C。正式复盘的纸面结论，数学程序0。原目标仍为新的ζ/L数值算术结论；完整周期投影、正基可逆和形式rank不是目标完成。本稿给一个关于同一q2对象的实际下界，不以229安全upper之和为正冒称最优失败。

## 1. CDT真正需要的输入

实际完整读固定CDT长稿PDF16–20：Theorem2.5.1要求一个**固定**m元组 `f_i∈Q[[x]]`，在Q(x)上独立，其全Taylor系数有指定有限LCM-slope数组，且同一个holomorphic `φ:(D,0)→(C,0)` 上所有 `f_i∘φ` 都meromorphic。基本非holonomic版本要求 `log|φ′(0)|>σ_m`；已知全部holonomic时可降为 `>τ(b)`。严格秩反证还须

`m[log|φ′(0)|−τ(b)] > J(φ)`，
`J(φ)=∫∫ log|φ(z)−φ(w)| dμ_Haar(z)dμ_Haar(w)`。          (S1)

Theorem2.7.1的univalent特例把J换为log conformal radius。CDT短稿完整PDF3–4的§2.1/Theorem2.1也明确：目标关系给有理系数的实际Apéry组合，组合的真实延拓和费用共同决定秩矛盾。无需先构造Betti/Hodge实现；但一个有限矩阵的2m阶系数秩，不等于已存在这个固定源函数元组。

φ本身holomorphic，pullback只要求meromorphic。普通点的pole变可去，与真实log/分数幂branch被取消，作用不同。本稿核基本Q-field判据；没有把它代替所有fine/all-place联合格定理。

## 2. 新命题：同一q2行列式对所有复g都有同一二次小界

沿229冻结规范，`m=d+1`，`N=ΘAᵀ+GBᵀ+a`，

`𝒲_d(X)=det[B;XA+aᵀ]`，`A_{s,r}=c_{r+s}`。

每个固定 `g∈C` 都有精确行消元身份

`𝒲_d(g)=det[B;Nᵀ+(g−Θ)A]`。                              (S2)

这不使用Θ=g。B、N以及A的每一行都为同一 `[0,1]` 上的矩，A行测度为 `x^sν`，`ν=dx/[π√x√(1−x)]`。229已核B行总变差<6、N行总质量<4；A行总质量 `c_s≤1`，且 `0<Θ<4`。因此(S2)各行总变差不超过

`C_g=8+|g|`。

将全部2m列换成首一shifted Chebyshev基，三角变换det=1。第j≥1列的sup为 `2^(1−2j)`。逐列Hadamard给同一对象的明确上界

`|𝒲_d(g)|≤C_g^(2m)(2m)^m 2^(−(2m−1)²)`，                    (S3)

对**每个复g、每个d**成立；零值亦包含。它在g的紧集上一致。故

`ℋ_g(z)=Σ_{d≥1}𝒲_d(g)z^d`

对每个复g都是整函数。这里没有证明这些函数非多项式、也没有证明全部或无界多个𝒲_d(g)非零。该literal determinant generating germ的整个平面延拓是无条件的，Θ=g不为它新增解析域。

## 3. 实际关系值的最简分母：不是安全费用表

现在固定 `g∈Q`。若某个尺度 `𝒲_d(g)≠0`，写其最简分数 `u_d/q_d`，`q_d>0`。因为 `|u_d|≥1`，(S3)立即给**真实最小分母下界**

`q_d≥2^((2m−1)²)/[C_g^(2m)(2m)^m]`，
`log q_d≥4log2·d²−O_g(dlog d)`。                            (S4)

该下界仅沿非零尺度，不推断其存在、密度或没有长零段。它适用于目标关系假设下的最简evaluation分母，已经允许全部系数在g处相消；不是全多项式LCD的下界，也不是primitive kernel费用的猜测。

从而有一个严格的源准入二分：若ℋ_g是多项式，则与1的Q(z)-span只有rank1；若ℋ_g非多项式，则有无界非零系数，(S4)证明它不可能具有任何固定有限LCM-slope分母型。甚至允许固定坏素数整体因子 `C^d`、固定整数倍或固定系数多项式清因子，也只增加O(d)+O(log d)，不能承担这个二次分母下界。固定非零有理坐标缩放 `z↦az` 同样只改O(d)估值费用。

因此不能直接把229–231的𝒲序列当成CDT所需的廉价有理Taylor源：一边是rank1，另一边是未过分母准入。该结论不要求先猜ℋ_g的递推或holonomicity。把d²重新称作Taylor序号、新增非可逆projection或另造源，都须重新支付actual holonomicity/rank/整模型和共同图，不能沿用此literal芽的证书。

这是限定该直接拼接的结构障碍；不是所有q2方法、所有Padé源或Θ算术结论的no-go。更精细的target-specific实误差、新生成载体或真实联合格仍可能改变问题。尤其(S3)本身对所有g相同，不能把它包装成已付Apéry式相对解析收益。

## 4. relation-specific饱和可以改什么，尚未改什么

对固定有理g，精确清evaluation分母是

`q_d(g)=∏_p p^max(0,−v_p𝒲_d(g))`。

完整polynomial的强迫系数费用不能自动搬给它。例如 `p^(−k)(X−g)+1` 有p^k系数分母，但在g处值为1。228 χ₋₈满秩Gram的cap明确限于完整scalar多项式及同尺寸可逆换基，不排除另付relation-specific整化；当前q2更不能被那个cap直接否定。

230同一对象的饱和引理恰保留了关系值：将B行格饱和，指标为p^e；在其商空间中令 `D_g=p(gA+aᵀ)Q|_{后m列}`，`r=rank(D_g mod p)`。对真实单位枢轴作Schur消元，第一剩余层S₁(g)给

`v_p𝒲_d(g)=e−r+v_p det S₁(g)`。                            (S5)

raw最高层不满秩时，S₁含gA及regular tail，不能删去它来假装relation费用已降低。若full residual stack满秩、e=0、r=m，则估值恰−m，对每个p整g同时成立；它支付条件非零，却也是真实分母负担。

边界 `p=4d+1` 的无界满秩仍须同一prime子族上同时支付初始Hankel块和half-shift Gaudin核。单个无界prime子族可支付无限非零；若要声称二次费用的累计改进，还要控制增长窗口内的总估值，不能把一项m logp当作c d²收益。231的Γ可逆只给 `𝒲_d(Θ)=(-2)^m detΓ_d P_m(1/4)`，仍缺这个耦合点值。

即使以后证𝒲_d(Θ)无界非零，也仅新增一个接口。229的安全费率 `6log4+14` 与目标实处upper `−4log2` 之和为正，仅表示该证书未过gate；(S4)则独立给非零有理evaluation的真分母下界。二者都不代替完整最优费用或更强实际误差证明。

## 5. 真实ζ/L对象必须保留哪些源信息

|对象|已付信息|不能省掉的下一桥|
|---|---|---|
|q2 Θ|真实完整G投影、原𝒲、已有Li₃身份；本稿(S2)–(S4)|Θ不是已识别的单个新ζ/L值。必须给实际目标隔离，或明确研究的是混合周期算术。𝒲点值非零与廉价CDT源亦须分别证明。|
|q3 β(4)入口|229精确式 `Θ₃=4β(4)+2A−4B−log2·Θ₂−2log²2·G`|全低权Θ投影不自动消掉同权2A−4B。需确切周期身份或实际满秩投影，不能用motivic dimension判零/独立。|
|原生χ₋₈ quotient|Root232自含证明全叶log branch、完整prefix LCD、rank2|`(B−c)/(1−z)`仅取消普通pole；保留1时与{1,B}具有同一Q(z)-span和共同meromorphic图。必须另给非meromorphic branch取消、真实rank收益或已付joint费用。|
|新截区V源|当前Root独立稿已给 `V=Cl₂(π/3)=(3√3/4)L(2,χ₋₃)`、全有限头及全尺度log-kernel投影|这是真实不同对象。还需同一投影的无限非零、全部prime费用、实误差，以及Q(√3)下两个嵌入的完整关系；不能把共轭g再改成−g。|

原生quotient的一般原则并非新发现：历史mixed Catalan稿已经用过rational inverse gauge恢复完整tuple。Root232的新明确应用是CDT所允许类下的χ₋₈全叶/LCD/rank联证，而非旧GB结果的新包装。可逆rational gauge保留共同meromorphic图，却不自动保留费用：`1/(1−z/2)`的2^(−n)系数就是固定2线性费用的反例。

对新V栈，本人独立核β低区积分、 `2lβ_l=(2l−1)β_(l−1)−4^(−l)` 和 `β=γc−α`；低/高两区各m个矩正交迫使degree<2m多项式有≥2m个零点，确给原Q栈满秩。含γ=π/(6√3)的实shear只用于rank证明，不能用于免费整格变换。此项不借普通q2或χ₋₈停止cap；它亦尚未给数值定理。

## 6. 可检验的继续条件与实际审读

保留q2的完整投影、(S5)、Gaudin核和A232固定混合Padé条件为结构资产。A232的精确固定窗口及duplicate-row反例已本人完整纸核：K全正/无限秩和固定Stieltjes尾不自动给原signed窗口的无界非零，standalone Kronecker捷径暂停正确。不能再以同类正性公式或低阶样本替代这个缺口。

下一主源先给固定actual f_i、目标关系使其Q/K系数的完整证明、足够Q(x)/K(x)函数秩、所有transported branches的共同meromorphic图、全Taylor分母及严格(S1)或相应已读fine/all-place判据。若走有限行列式而非CDT，则直接给同一非零整数的完整费用与target-specific误差；不把有限矩阵rank升为源rank。这些是具体准入项，不是要求额外motivic实现。

本轮实际阅读与文件身份另存 `literature/global_review_sources_round232_20261008/dual_reading_scope.md`。新primary PDF0，复用CDT原件并新抽取完整选页TXT2；定向web仅核出处，没有采用摘要定理。数学程序0、probe/scan/CAS/旧producer/Git/Lean0；只写NEW文件，旧稿/main/manifest未改。保存后实际FULL作者复读，不冒充独立审查。
