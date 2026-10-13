# 第267轮正式复盘：固定目标的选择器费用

2026-10-13。上一轮266交付完整安全模型、源纠错和停止决定，属于progress。本轮完成[宏观窗口](source_gate_charter_round267_20261013.md)，比较具体Mellin、周期Dirichlet与非显式Siegel机制。**没有新的数值定理，没有候选通过完整数值净预算。** 下一步仅给不同原生packet的一轮目标像核查；不是重开旧参数优化。

## 1. 全路线资源决定

| 路线 | 现行最短未付接口 | 本轮决定 |
| --- | --- | --- |
| ζ5形式化基线 | 不属于新数值目标 | 保留机制与形式化 |
| ζ7旧Gram/整数格 | 同对象本原负指数及实际无限非零 | 不扩大已闭参数 |
| K5固定3:1 | 真实完整内容与实能量净余量 | 不借宽span定理恢复 |
| logmoment/旧显式Padé | 异常本原内容或真实低成本投影 | 227固定包仍停止 |
| 已知周期推论 | 尚未隔离新指定值 | 不替代goal |
| 奇权/CM/χ−7 | 背景恢复、全叶、同对象费用 | 原范围保留 |
| χ−8 RV/native | 实际无限非零与严格预算 | 不重开252秩一Gram或旧截区 |
| mixed scalar AP | 原标量cap/地图已关闭 | 不恢复 |
| mixed actual联合格 | intrinsic负graded信用尚缺 | 263–264窗口仍关闭 |
| M₀,₈固定a完整pair | 本原净信用未付 | 266窗口仍关闭 |
| 新来源 | 完整指定值、非零和费用必须同时匹配 | 选择非显式Siegel packet的目标商，仅来源核查 |

依据[成果地图](../docs/RESEARCH_DIRECTIONS.md)、[265比较](source_selection_round265.md)及[266结算](m08_target_vector_round266.md)。没有重跑历史producer。此次定向检索拦住一个伪新候选：正密度 \((-\log x)(1+x^2)/(1+x^4)\) 的χ−8纯矩正Gram早已在[252](public_repository_global_review_round252_20261010.md)证明完整约分后的实际界 \([256(D+1)^2\,64^D]^{-1}\)，D=O(m)时不能给负m²预算。它不是此次发现的新来源。

## 2. Brown多参数Mellin：严格判据不能代替目标投影

[Brown v1](https://arxiv.org/abs/2604.20741v1)实际输入为自由函数格、同一矩阵 \(Q_n=(\int f_if_j\omega)\)、实际非零det，以及有理可逆左右矩阵使**全部周期系数**整数。费用为 \(\delta_n=|\det D_n^\ell\det D_n^r|\)。严格可用出口是
$$
2\log\operatorname{Sup}_{M,e}(f\sigma)+\log\delta_{M,e}<0,
\qquad e_n/N_n\longrightarrow\infty .
$$
若剩余周期均属于固定 \(\mathbb Q[X]\)，设其最大次数d和共同固定系数分母B，则在任意 \(X=u/v\) 假设下，整数周期线性形式的非零值至少为 \(1/(B|v|^d)\)。Minkowski的上界为 \((t_n^2\delta_n)^{1/N_n}\)，严格负e指数使它趋0。若走det多项式，则须保留 \(B^{N_n}|v|^{dN_n}\)；同一条件也吸收这项。

因此不能使用印出的Lemma7.8任意矩阵弱形式：取 \(\xi=(1,1/2)\)、\(Q_N=\frac12 I_N\)、\(d_N=1\)，symbolic det为 \(\xi_2^N\)，实际 \(d_N\det Q_N=2^{-N}\to0\)，但数值span维数为1。这里只审其任意矩阵陈述；不把该反例套给原正Mellin例，也不否定严格Criterion1.4。在固定总变差 \(\mu=\int_\sigma|\omega|<\infty\) 且所用t_n有限时，Gram/Heine给 \(|\det Q_n|\le(\mu^{N_n}/N_n!)t_n^2\)。必须保留该因子，不能另把Criterion1.3仅凭根估计判错。

已付的具体例仍是 \((1,\zeta(2))\) 或log2。Cor7.3的ambient维数至少2，在 \(\zeta(2)\) 已知无理时不提供新出口。M₀,₈原正积分的graded系数坐标为
$$
(1,\zeta(2),T),\quad T=\zeta(5)+2\zeta(2)\zeta(3),
\qquad X=\zeta(5)+3\zeta(3).
$$
在**形式系数坐标**中这两个span的交只有常数：比较ζ3和ζ2ζ3坐标便得。这里不声称实际数值span交，也不借未知跨权独立性。可逆有理左右换基不能消去非零nuisance系数矩阵。

八参数也不等于自由矩形的r=8。函数位于dim5源上有代数关系，不能用n⁸假rank领取式(1.8)。Brown实际M₀,₅五参数例用商环pole filtration，\(N_n=1+\frac52n(n+1)\)、\(e_n=\frac56n(n+1)(2n+1)\)。新目标尚缺自己的可乘配对、独立格尺度、actual非零及同尺度全处费用；§8的p-adic解释是方向，不是这四项证书。当前不准入。

## 3. 2019周期Dirichlet：完整消元界和divisor自由度

[Fischler 1904.02402v1](https://arxiv.org/abs/1904.02402v1)保留的实际整数形式是
$$
\Lambda_{n,k}=2(-1)^p\sum_{\substack{2\le j\le a\\j\equiv p(2)}}s_{k,j}L(f,j)
 +\sum_{\lambda=0}^{N-1}s_{k,a+1+\lambda}f(\lambda).
$$
错误奇偶和权1按原身份消掉，有限头不能漏。对χ−8取N=8,p=0，条件 \(1\le r<a/(3N)\) 强迫a>24，输出包括1及所有偶权L至a。对ζ取N=1,p=1，输出为1及全部奇权。源的满行秩P经实际M投影后，对于这两种压缩包仍给系数rank m+1，m为保留权数；这不证明指定数值独立。

作者的全系数清整为 \((Nd_{n/N})^{a+1}N^{(a+1)n/N}\)，全部有限头和prime powers都在内。记 \(A=(a+1)/N\)，已公布界为
$$
\alpha_D=(4e)^A(2N)^{2r+2}r^{-A+4(r+1)},\quad
\beta_D=(2e)^A((r+1)N)^{2r+2}.
$$
普通整数余子式消掉m−1个nuisance只给误差 \((\alpha_D\beta_D^{m-1})^{n+o(n)}\)。全合法域此upper的指数为正：主项
$$
A[\log(4e)-\log r+(m-1)\log(2e)]>0
$$
且余项非负。因为 \(m-1\ge(a-4)/2\)、\(\log r<\log(a/3)\le(a-3)/3\)，括号的保守下界在a=4为正，此后斜率 \(\log(2e)/2-1/3>0\)。**这是所公布完整upper不足，不是最优本原费用lower。**

原§3.2按N=DT实施的divisor滤波只令权j乘 \(D^{-j}\sum_{d\mid D}w_dd^j\)。对固定ζ7或χ−8 L2，需要杀掉其他m−1权；合法截止分别a≥7、a>24，给
$$
\tau(D)\le D\le\lfloor(a-1)/(3T)\rfloor\le m-1.
$$
在正且互异的d上，广义Vandermonde满列秩，故只能所有w为0。此范围限于原N=DT构造，不涵盖改变period、packet或算术的所有滤波。即使只留下ζ3、ζ5，满秩包也不会自动变成固定3:1。

Rivoal–Zudilin2003的不同半整数构造确有正积分和完整费用，但q=16的作者负margin只对应 \(\beta(2),\ldots,\beta(14)\) 中至少一个；q=4分母仍过大，不移给χ−8。由定义 \(\Phi_s(-1)=2^s\beta(s)\)，原PDF4–5的相反标量应纠正；固定q的2幂不改n指数，完整系数仍必须按定义恢复。本文不独立认证其显示的数值margin。

## 4. Lai与非显式Siegel：新工具的真实量词

[Lai v3](https://arxiv.org/abs/2407.14236v3)正文Theorems1.3–1.4用1.009；1.119356及有限ζ75的维数结论明标Claims1.5–1.6。不能仅从摘要领取后两项定理标签。不同长度分母砖与大素数Φ是线性级算术机制，小素数/高次幂由LCM成本覆盖；原生输出仍是全部奇值，不直接支付固定目标投影或K5/M₀,₈费用。

[Fischler 2109.10136v3](https://arxiv.org/abs/2109.10136v3)改用非显式小系数族，最终真实向量为
$$
(1,\log2,\zeta(3),\zeta(5),\ldots,\zeta(a+h)_{\rm odd}).
$$
其额外维数一项用于扣log2，不能在固定目标反证中直接删除。修订版只证明共同kernel的x₀=0，不保证总满秩。

“令所有原生外推行同时纯目标，再免费沿用α、β”可全尺度关闭。设最高非零P为 \(P_b(z)=\sum_{j=0}^nc_{b,j}z^j\)，\(N=rn,K=k-1>(r+1)n\)。对单项式指数q=N+j及t≥2，hybrid polylog满足 \(DL_t=-L_{t-1}/z\)，故 \(D^K(z^qL_t)\) 在z=−1的最高活权t−1系数为 \(q!(K-q-1)!\)：它是 \((q-u)_{\underline K}\) 的一次项，乘上z的符号后为正。p层最高活权b+p−1的系数因此除各行非零标量后为
$$
\sum_{j=0}^nc_{b,j}(N+j)!(K-N-j-1)!.
$$
再除 \(N!(K-N-n-1)!\)，得到三角多项式基
$$
\sum_{j=0}^nc_{b,j}(N+1)_j(K-N-n)_{n-j}.
$$
次数依次为n,…,0。超过n个K处消失便强迫P_b=0。原r=3.9,κ=10.58给2.78n−1个K；h≥m+2时p=h或h−1使最高活权为大于固定m的奇数，产生矛盾。对X用m=5。此结论不排除**整数行选择器**，也不把权坐标消元当数值独立。

## 5. 唯一下一对象：固定非显式packet的目标商

固定一次参数，不作优化或扫描：
$$
a=1000,\ h=360,\ r=39/10,\ \kappa=529/50,\ \omega=12,\ \Omega=300,
\quad s=a+h=1360,\quad n\in50\mathbb Z_{>0}.
 \tag{S1}
$$
只对充分大的n调用原Theorem4、Lemmas5–6和Proposition3；50不是已认证起始阈值。条件 \(a>\Omega\ge\omega\)、\(0\le h\le a\)、\(r\ge2\)、\(r+1\le\kappa\)、\(2r<\kappa<\omega\) 及
\((h+1)(\kappa-2r)+\omega=1015.58>a\) 都成立。

原源的完整界为
$$
\chi=\exp\frac{\omega\log2+3\omega^2+\omega^2\log(a+1)+\Omega^2\log r/2}{a-\omega},
$$
$$
\alpha_S=\chi r^{-\Omega}(2e^4(2a+1))^\kappa,\qquad
\beta_S=\chi(8e^3(2a+1))^\kappa2^{\kappa+r+1}.
 \tag{S2}
$$
用 \(\log2<1,\ 1<\log3.9<3/2,\ \log1001,\log2001<8\)，纸面得到
$$
\log\chi<69096/988<70,\quad
\log\alpha_S<-4623/50=-92.46,\quad
\log\beta_S<1168/5=233.6.
 \tag{S3}
$$
例如 \(8/3<e<3\) 给全部这些保守对数界。这是已支付的原生**全packet**解析/整数高度来源输入；没有支付目标selector费用。

合格选择指同一无界I⊂50ℤ上的非零系数族，满足Theorem4(i)–(iii)，且(ii)–(iii)的渐近余项统一为o(n)。逐n更换选择而没有统一证书不算合格族。Theorem4只保证存在非零小系数 \(c^{(n)}\)，不指定唯一族。对有该证书的选定族，可抽最高b相同的无限子列，但行空间仍不因此稳定。把原全部 \(0\le p\le h,\ 2rn+2\le k\le\kappa n\) 的形式转为上述真实向量，统一乘固定常数 \(C=2^{1359}\) 清除 \(2\operatorname{Li}_j(-1)=2(2^{1-j}-1)\zeta(j)\) 的分母，得到整数矩阵B_n。缺权以零列补齐；C对固定a不改n指数，log2栏保留。

令e₀为常数方向，e_X在ζ3栏取3、ζ5栏取1，其余0；令H_n取log2栏、ζ3栏减3倍ζ5栏和全部奇权j≥7。定义实际对象
$$
\Lambda_n=\ker_{\mathbb Z}H_n^t,\quad
K_n=\ker_{\mathbb Z}B_n^t,\quad
\Gamma_n=\Lambda_n/K_n.
 \tag{S4}
$$
其像 \((U,A)\) 满足 \(c^tB_n=Ue_0+Ae_X\)，给完整整数形式U+AX。弱kernel只保证e₀可见；目标首关恰为
$$
e_X\in\operatorname{row}_{\mathbb Q}B_n
\iff \forall x\in\ker_{\mathbb Q}B_n,\quad3x_{\zeta3}+x_{\zeta5}=0.
 \tag{S5}
$$
必须证明对所有合格选择成立，或给出保持同一小系数/余项证书的存在选择；不能用generic猜测或有限头。

还须在同一无界子列支付Γ_n中**两独立输出**的真实来源代表费用。若代表c₁,c₂满足 \(\|c_i\|_1\le\exp(\gamma n+o(n))\)、\(\gamma<-\log\alpha_S\)，则其误差均趋0。在每个固定X=u/v假设下，两独立 \((U_i,A_i)\) 不能同时落在U+(u/v)A=0直线上，至少一条非零值≥1/|v|，构成反证。这个接口覆盖全部有理反证类，无须先知道X无理来选择非零形式。

大量短Λ向量可能全在K_n，不能只报维数或covolume。若领取 \(g_i=\gcd(U_i,A_i)\) 的本原信用，须同时用实际 \(c_i/g_i\) 的来源范数与误差；目标像饱和不保证免费整数提升。现有通用余子式费用为O(a loga)，源衰减为O(√(a loga))，尚未有足够收益。本次没有证明(S5)、两个短非零像或其本原信用，**不准入数值实施**。

历史范围也已核：222提出的是2019显式周期Padé稳定空间；227停止的是另一ζ7四解/exterior包；244仅保留非显式工具与可见性缺口。它们没有核此固定完整p,k packet的Γ_n。不能称目标选择性方法首次出现；这只是此前未核的具体对象，见[268一轮任务](siegel_target_quotient_charter_round268_20261013.md)。

## 6. 正式决定与审阅范围

关闭267宏观窗口，last_global_review=267；连续未改善数值准入计数保留7。默认下一复盘271、最迟275；两轮停滞提前。268仅做(S4)–(S5)及真实费用的一轮来源核查，若只有rank2、矩阵定义或旧cofactor upper即结束，不另开参数/高精度窗口。所有旧数学窗口保持关闭，总goal active。

主代理完整读成果地图、252纯Gram稿，读222/227/244的具体停止/源段；旧批输出截断不领全文标签。实际选读Brown PDF1–5、20–23、25–27；2019 Fischler PDF1–11、19–20；Siegel v3 PDF1–7、10–11、20–24、28–29、39–40；Lai v3 PDF1–4；Rivoal–Zudilin PDF4–5。三位新上下文代理分别核Brown全文34页、2019指定packet及RZ、Lai与Siegel实际定理/构造。主代理独立重建严格rational分母口、divisor/费用不等式、最高weight三角多项式及(S1)–(S5)。三人完整复读保存后的两稿：Brown任务代理独核§3–5，2019任务代理独核§4–5，Lai/Siegel任务代理独核§2–3；各自先前贡献不计独审。独审无阻断错误，已按意见明确同一无界合格族的统一余项量词、各行非零归一化、单项式符号与hybrid递推范围。

原件版本与散列由program证据链记录。已核一手版本范围不等于全球新颖性；作者辅助常数/宽span结果不升级为本项目定理。无CAS、数学producer、参数/prime/Padé扫描或Lean执行；冻结文献与形式化资产保留。
