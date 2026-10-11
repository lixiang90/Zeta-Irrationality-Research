# 第225轮：关系外积的完整幂指数、非有理性与实际域上rank

2026-10-08，B。固定222–225同一 R_n、全部 A3/A5/A7/C、Δ/Ξ/J；数学程序 **0**。本稿新增自含的幂指数识别/Galois传递与完整渐近基，证明实际 I、J有无限非零项，J的生成函数非有理，并在假设ζ(7)=g∈Q时支付原 `(1,D,H_g)` 的 **Q(z)-rank3**。没有证明ζ7无理或完整CDT strict gate，不把difference order20当微分rank。

## 1. 实际输入与结论

本轮实际FULL读：[C actual modes](pade_actual_fourier_modes_round225_20261008.md)，11160B/SHA `37d2a980146055a4b3509d7861f77d674bec6fca40cb55e5ec138aeaccc81788`全部G1–G21；[A actual symbol](pade_actual_leading_symbol_round225_20261008.md)，最终13928B/SHA `ee1d70e843e53090cefc84dd750452e2ee6c954ae79bf674d0ea9f25ffede798`全部S1–S19（S5加号修正版和最终S13/S14术语澄清版均再次FULL）；[Root branch](pade_actual_branch_graph_bridge_round225_20261008.md)，当时6523B/SHA `5001f4693f14768d3a9ebc39f71934aaeb64aaac733225b7201911864c60be6a`全部五节。作者/数学程序输入与本人的独立新证明分别登记，不宣称重新执行他们的证书。

记 `a_r=A3,2r，b_r=A5,2r，c_r=A7,2r，q_r=C2r，i_r=I2r`，

`Δ_r=det(a,b,c)_(r,r+1,r+2)，Ξ_r=det(a,b,q)，J_r=det(a,b,i)=ζ7Δ_r+Ξ_r`。

记 `D(z)=ΣΔ_r z^r，X(z)=ΣΞ_r z^r，H_g=gD+X，𝓙(z)=ΣJ_r z^r`。D/X/H保持原有理系数源，不用含π²的B坐标改派算术费用。

令 α∈(8,9) 为 `v³−9v²+3v−3` 唯一实根，β、βbar为其另两根，置

`L1=α⁹，L2=(3+2√3)⁹，L3=3⁹，κ=(3/α)^(9/2)，s=(2√3−3)⁹`。

实际six characteristic values按下述命名为

`μ1=−L1，μ2=−L2，μ3=−L3，ν+=−β⁹，ν−=−βbar⁹，ν0=s`。

它们distinct、非零，`L1>L2>L3>1>κ>s>0`，`|ν±|=κ`。A已支付实际归一化有理递推

`Σ_(j=0)^6 a_j(r) f_(r+j)=0，a6=1，a_j(r)=χ_j+O(1/r)`，

`χ(t)=(t+19683)(t²+19704870t−19683)(t³+283965993t²+3308931t+19683)`，      (P1)

在充分大r对a,b,c,q,i成立。固定C坐标B1/B3/B5是a,b,c的常数C线性组合，故也满足(P1)。有理a_j在∞正则自动具有完整Laurent展开，不要求新程序算其next coefficient。

**结论：** 存在 `q_*∈{κ,s}`，取 `T_*=L1L2q_*`，有

`limsup |J_r|^(1/r)=T_*，J_r/T_*^r=O(r^(−33/2))→0，𝓙∉C(z)`；             (P2)

`R(D)=R(X)=1/(L1L2L3)，R(𝓙)=1/T_*`。目标关系下H_g=𝓙，因此实际相对半径收益恰为

`log[R(H_g)/R(D)]=log(L3/q_*)∈{(9/2)log(3α)，9log(3+2√3)}`。           (P3)

本稿不判定κ还是s实际出现；不是假设某个small Stokes constant非零。证明会支付small coefficients至少一个非零、完整basis以及同模pair的量词。

## 2. I/J不可能最终为零：原三行与经典ζ3输入

**P4.** I最终为零会迫使ζ3、ζ5、ζ7全Q。确实，224已付同一Δ在无界素数尺度非零。任选足够大的非零Δ_r，其三行actual period身份为

`(a,b,c)_(r,r+1,r+2)·(ζ3,ζ5,ζ7)^T=−(q_r,q_(r+1),q_(r+2))^T`。

左矩阵为invertible rational矩阵，右列为完整finite tails产生的rational列。三ζ均应有理，与经典Apéry ζ3无理矛盾。因此I有无限非零项；这个结论**无须ζ7=g**。

这里只采用已确证的经典ζ3结果。实际完整读缓存[Apéry1979原件](https://www.numdam.org/item/AST_1979__61__11_0/)四个PDF页（印刷11–13及封面），并图核印刷13页；其通用criterion与ζ3的 `λ=17+12√2，μ=e³` 确认原结论。没有借异族递推推本packet的新ζ7结论，也不以标题或搜索摘要替代原文。

**P5.** C已付 `W_r=det(a,b)_(r,r+1)=d_W r^-11(L1L2)^r(1+O(1/r))，d_W>0`。若J最终0，W最终非零，取两行唯一解出常数u,v使 `i_r=u a_r+v b_r`。三行det0把这个等式传播到下一行；相邻两行的唯一性保持同一u,v，故对所有充分大r成立。

精确B坐标中，B1/B3对a,b的2×2系数det含非零因子 `α1β3−α3β1=1/30`。任何非零(u,v)组合若B1系数未消去，其rate为L1；消去B1后若B3系数未消去，其rate为L2；两个系数同时为零只可能u=v=0。与已付 `i_r=O(poly(r)θ^(2r))，θ=2^42/3^27<1` 矛盾。于是i最终0，违反P4。因此J也有无限非零项。尚不能仅据此断言𝓙非有理；下面支付这一更强命题。

## 3. 由actual leading power识别next层：不用猜小模态

**P6：harmonic telescoping lemma。** 设实际有理归一化递推满足

`a_j(r)=A_j+B_j/r+O(r^-2)，χ(t)=ΣA_jt^j`，

并有一个实际解 `f_r=c μ^r r^γ(1+ε_r)，c≠0，ε_r=O(1/r)`，μ为χ的simple非零根。代入得

`Σd_j ε_(r+j)+C0/r+O(r^-2)=0，d_j=A_j μ^j，Σd_j=0`，

`C0=Σμ^j(B_j+γjA_j)`。

这里**不假设ε_(r+1)−ε_r=O(r^-2)**。将r=R,…,T求和：Σd_jε_(r+j)中共同内部区间因Σd_j=0消去，只留每个j的有限首尾，大小O(1/R)+O(1/T)。而 `C0Σ1/r` 若C0≠0随T发散，O(r^-2)总和有界。因此C0=0，严格得到

`γ=−B(μ)/(μχ′(μ))，B(t)=ΣB_jt^j`。                              (P6)

该证明只用actual O(1/r) amplitude，无未付的差分误差估计或高阶stationary connection。

**P7：Galois传递。** P1的a_j在Q(r)中，故B_j∈Q。C实际三B渐近分别给μ1、μ2、μ3的γ=−11/2。它们代表χ的cubic、quadratic、linear三因子：v-cubic的有理根候选±1、±3皆不为零，故不可约；μ1的共轭值模不同，μ1不在Q，度恰3。μ2的√3共轭为ν0且不同，度恰2。μ3为rational。故(P6)在每个不可约因子上经Q-embedding保持，支付**所有six roots的γ皆为−11/2**。没有把三个大actual解直接当成六个actual解；下一节构造complete basis。

## 4. 六根完整渐近基：明确past/future边界

**P8.** 实际six-state `v_r=(f_r,…,f_(r+5))^T` 有companion

`C_r=C∞+C1/r+O(r^-2)`。

simple χ roots使C∞有Vandermonde eigenbasisP，`P^-1 C∞P=Dμ=diag(μ_i)`；令T=P^-1C1P。nearidentity gauge `I+S/r` 给next层 `T+DμS−SDμ`；取 `S_ij=−T_ij/(μ_i−μ_j)`（i≠j）清除off-diagonal项。

diag T_ii/μ_i正是(P6)的γ：右向量e(μ)=(1,μ,…,μ⁵)，左向量ℓ可归一化最后分量为1。由 `C∞e(t)=t e(t)−χ(t)e6` 微分，再左乘ℓ，得 `ℓe(μ)=χ′(μ)`；C1e=−B(μ)e6，故projected next coefficient为−B(μ)/χ′(μ)。P7使diag next层统一为γDμ。再除去公共r^γ，实际系统变为

`w_(r+1)=(Dμ+E_r)w_r，E_r=O(r^-2)`。                           (P7)

**P9：mixed Green构造。** 对每个固定μ_j，寻求 `w_r=μ_j^r(e_j+z_r)`，则

`z_(r+1)=D_j z_r+F_r(e_j+z_r)，D_j=diag(d_i)，d_i=μ_i/μ_j，F_r=μ_j^-1E_r`。

对任意forcingf_r，定义其逐分量Green operator，r≥R：

`(Gf)_i(r)=Σ_(k=R)^(r−1) d_i^(r−1−k) f_i(k)，|d_i|<1`；
`(Gf)_i(r)=−Σ_(k=r)^∞ d_i^(r−1−k) f_i(k)，|d_i|≥1`。             (P8)

前者指定stable分量在R的初值为0；后者指定future tail，包括d_j=1和等模但相位不同的complex partner。没有把全部分量免费沿同一方向求和。future和绝对收敛，因为f=O(k^-2)且逆幂模≤1。

用norm `||z||=sup_(r≥R) r||z_r||`，Green将 `sup k²||f_k||` 有界地映到此norm，常数仅依赖固定d_i、对R足够大统一。future单位模用Σk^-2=O(1/r)；strict future和past用几何和。past可按k<r/2与k≥r/2拆分，分别是指数尾和O(r^-2)，故同样为O(1/r)。反馈F_kz_k满足 `sup k²||F_kz_k||≤C||z||/R`。取R大，

`z=G[F(e_j+z)]`

是严格收缩，给actual z=O(1/r)。每个μ_j均得到一个解；其六列为 `(I+O(1/r))diag(μ_j^r)`，最终invertible。因此它们构成**整个six-state solution space**的basis，不只是formal系列或stable upper。

退回两次gauge，得到scalar solutions

`φ_j(r)=μ_j^r r^-11/2(1+O(1/r))`，j=1,…,6，                    (P9)

每个actual source解在充分大r唯一为常数C线性组合。R以前的有限异常不影响tail basis或生成函数的有理性；没有宣称算出最后异常整数，也没有删实际源初值。

## 5. 实际J的small exterior modes与非有理性

**P10.** 用P9表示actual i。实际指数衰减剔除μ1、μ2、μ3的系数：若有非零，最大模那个的单一主项将有root growth>1，矛盾。P4保证remaining stable coefficients `h_+,h_-,h_0` 非全0。这支付的是至少一个非零，不判断哪个connection。

C实际B1、B3、B5的leading coeff为c1,c3,c5>0、leading roots为μ1、μ2、μ3。故其在P9 basis的large部分为上三角：B1含c1φ1及可能较小项，B3含c3φ2及较小项，B5含c5φ3及较小项。由exact B→a,b矩阵，a,b在(φ1,φ2)的系数det为

`E12=κ3κ5π⁶ c1c3/30≠0`。                                     (P10)

可能来自B1的φ2项只给同一第一系数方向，不改变det。所有其他A-pairs的模严格小于L1L2。

对每个stableν，其exact leading exterior scalar的系数为

`K_ν=E12 h_ν (μ2−μ1)(ν−μ1)(ν−μ2)`，                        (P11)

这是三行r,r+1,r+2的actual Vandermonde，故h_ν≠0时K_ν≠0。若h_+或h_-非零，则

`J_r=r^-33/2{K_+(μ1μ2ν+)^r+K_-(μ1μ2ν-)^r+O((L1L2κ)^r/r)+O((L1L2κ−η)^r)}`，某固定η>0；

若两者皆零，则 `h0≠0`，且

`J_r=K0(μ1μ2ν0)^r r^-33/2(1+O(1/r))`。                         (P12)

这些是有限六模态的exact exterior展开，每个triple的固定product有实际basis的(1+O(1/r))幅度。因此subdominant products有固定模gap，均纳入上述指数较小项，而dominant amplitude的余项为O(T_*^r/r)。这里无需对误差取差分。等模pair不能靠某一项dominance解决：令其unit phases为ω±，ω+≠ω−（χ distinct且该pair非real），Cesàro平均

`(1/N)Σ_(r=1)^N |K+ω+^r+K-ω-^r|²→|K+|²+|K-|²>0`。

相交叉几何和/N趋0。因此该pair在无界r上幅度有正下界，error→0不改变limsup root；无需排除逐项phase cancellation。得到P2的exact rate和normalized decay。

**P11：rational GF排除。** 任意非多项式rational生成函数的tail由有限个 `P_l(r) λ_l^r` 组成，P_l为非零ordinary polynomial，λ_l distinct、非零。若root growth为T_*，最大模poles的项除T_*^r后是有限个unit phases乘polynomial(r)。取最大degree d≥0，再除r^d，其平方Cesàro平均有正极限（distinct phases的交叉均值为0），因此不可能趋0。P2反而给 `J_r/T_*^r→0`，矛盾。𝓙非rational；这强于非polynomial，且无须假设ζ7有理。

## 6. 目标Q(z)-rank、exact解析收益及费用诊断

**P12.** Root已付D在 `z0=−1/(L1L2L3)` 的原径向branch非meromorphic，关系假设下H_g在那里全纯。任何 `P D+Q H_g+T=0`，P,Q,T∈Q(z)，必有P=0；否则D可由右边除非零rational P得到meromorphic延拓，矛盾。由P11，H_g=𝓙∉C(z)，故剩下QH_g+T=0亦只可能Q=T=0。因此在ζ7=g∈Q条件下

`dim_Q(z) span{1,D,X}=dim_Q(z) span{1,D,H_g}=3`。                (P13)

这是原有理源的actual域上rank；**不是H_g的最小cyclic differential rank等于3**，也不是外幂difference20等于微分20。P9在C上的gauge仅用于证明渐近，未改原Taylor源的整格。

**P13.** C actual generic radius与P12给P3。complex stable系数是否为零仍未知，但相对预算现在有精确两个可能值、已付统一上界

`(9/2)log(3α)≤log[R(H_g)/R(D)]≤9log(3+2√3)`。                   (P14)

最大可能值小于18：`3+2√3<7<e²`，后一个不等式由e²的0至5次正Taylor和>7即可；故 `9log(3+2√3)<18<166/9`。该上界属于**固定原对象的relative-radius gain**，不是任意共同图的容量上界。

**P14.** 223完整all-prime系数界继续是

`64³ d_(2r+4)^6 Δ_r∈Z，64³ c_g d_(2r+4)^13(gΔ_r+Ξ_r)∈Z`。

固定c_g、dyadic64及全部prime powers均保留；Θ derivatives只乘整数r^j。原指定三行nested array由六个width2列付D/X、另七个width2列付X，row sums为(0,12,26)，其τ=166/9（有限+4 shift可用2+ε并处理有限prefix，最后ε↓0）。这不是把d_(12r)当作六个d_(2r)的免费替换，也不证明该表最优。

若某模板的analytic budget恰为P14的relative logratio，则此safe表需至少改进

`τ下降 >166/9−9log(3+2√3)>4/9`；

一般flat row(a,b)须 `3a+5b<81log(3+2√3)`。这是该明确表的必要诊断，**不把row denominators当optimal full-source lower**。真实共同格/精细能量或其他源仍可能不同。

**P15：直接CDT条件不可省。** 实际选读CDT2025原PDF的完整Th2.1/式2.1–2.2：要求holonomic、Q(z)-独立、有合法全系数array、同一φ pullback全行meromorphic、`log|φ′(0)|>τ(b)`，且要使

`m>Energy(φ)/(log|φ′(0)|−τ(b))`

才给矛盾。本文P13支付该原三行的独立性，其余费用/共同图/energy仍须实际构造。相对半径不是φ′，raw variable algebraic缩放必须支付其他embeddings与算术费用。Root已另排除包含D的raw univalent图入口；此处不重复其证明或把它扩大为全部CDT路线no-go。

## 7. 实际scope与剩余接口

本稿新P4–P14均为纸面有限代数/收缩/渐近证明，数学程序0，无CAS、root solver、matrix执行、recurrence guessing、prime/parameter/energy扫描、PSLQ、Lean或旧producer复跑。常数a_j1未展开；其Q性质由actual rational recurrence保证，值由P6/P7识别。没有沿着更多safe contours停止，也未采用先前讨论但未写入本稿的7n/6 contour候选。

Primary实际范围：Apéry原PDF四页全文文本及印刷13页图核；CDT20页原件只实际读PDF2–5（其中完整§2.1/Th2.1跨3–4页，旁段不是全文20页）；DLMF5.11的E1/E3/E7与完整固定sector、正a/固定b及remainder相关条件。没有用DLMF2.9二阶条目承担本六阶complete-basis定理，Green证据在本文自含。详情及所有实际输入身份单存[reading scope](../literature/pade_relation_rank_sources_round225_20261008/packet_reading_scope.md)。

已新增的是actual H非rational、原源Q(z)-rank3和exact两值relative gain，不是新的ζ7无理性定理。剩余主接口是原同一完整源或目标cyclic源的真正共同meromorphic图、全部place integral模型及实际CDT energy inequality；最小微分rank、small具体connection、最优joint cost与全局数值结论未支付。保存后作者实际FULL复读，final bytes/SHA另报，独审另立收据。旧稿/main/manifest不改。
