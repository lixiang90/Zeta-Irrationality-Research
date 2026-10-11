# 第244轮：真实周期投影的方向复盘

2026-10-09启动，2026-10-10完成。Packet/B；数学程序、素数/参数扫描、Lean执行均0。实际FULL读取240正式复盘及三份机制比较稿。本轮新纸证是低权K源在一条有理覆盖上失去关系敏感性；另独立FULL核通过Root的χ₋₇正载体。没有新数值无理性/LI定理，不把文献搜索未命中当全球新颖性证明。

## 1. 四接口必须留在同一对象

真正可继续的对象须同时有：(i) 全部条目的实际目标投影；(ii) 商部、有限头、全部prime powers及固定坏素数均在内的整模型；(iii) 实际选择的行列式在无界尺度非零；(iv) 同一归一化的实侧能量与完整算术费用严格相容。形式动机维数、ambient rank、正性、分母upper各自不能替代其余接口。

| 对象 | 实际投影 | 完整整模型 | 无限非零 | 同对象能量/决策 |
|---|---|---|---|---|
| 固定K5 logistic，X=3ζ₃+ζ₅ | 全商部/简单极点已付 | 242–243同对象全系数Gauss预算upper为1511/60 | 241固定prime-edge已付 | strict费用<6及相应完整实侧输入尚未共同支付；停同源local优化 |
| K=2G−(π/2)log2的原x源 | native非亚纯分支填点已付 | 全prefix safe d_Nd_⌊N/2⌋已付 | 三行函数独立已付，不等于近似det非零 | 下节覆盖停止；原x真实多叶图仅作条件后备 |
| 原M₀,₁₀七重积分 | 原十一周期通道已付 | 尚无目标六通道的全n完整整模型 | 全n目标投影det非零未付 | 原快速模式不能免费继承；不升主线 |
| χ₋₇非对称R_n及对称A_n | 两者全商部/±简单极点均只有1,L₂χ₋₇ | 外国大素数窗口已付，固定7及全预算仍缺 | 对称A_n每个n,h已付；非对称不可继承 | 只保留完整预算校准；对称源的外场、能量必须另算 |
| 导子匹配CM混合积分器，X=735L₂χ₋₇−86π² | 文献CM身份及native真log消除 | 下节给全prefix safe与明确七行rational closure | 实际cyclic rank/∞非零尚未付 | 优先有界全source/全leaf准入；没有strict holonomy预算 |

K5的1511/60是费用upper，不是实际费用lower；“停”是本轮投资决定而非数学no-go。χ₋₇同样不能因head从五阶降二阶而预领净收益。

## 2. 低权K：有理双覆盖的明确停止引理

复用240的确切归一化
\[
F(x)=(1-4x)^{-1/2},\quad \ell(x)=\log(1-2x),\quad
H_g(x)=F(x)\left[g+\int_0^x
\frac{2\ell(t)}{(1-2t)\sqrt{1-4t}}\,dt\right].
\tag{P1}
\]
端点积分为−K，所以g=K时原生x=1/4的平方根分支确实消失。它是关系敏感的非亚纯分支消除，不能称普通pole fill。

**引理。** 在固定有理覆盖
\[
x=r(u)=\frac{u}{(1+u)^2},\qquad r(0)=0,\quad r'(0)=1,
\tag{P2}
\]
上，三行源(1,ℓ∘r,H_g∘r)的共同亚纯图准入对g关系盲。采用其下述safe三行类型的basic CDT严格不等式，不能用此覆盖证明K无理。

证明：原生平方根为(1−u)/(1+u)，故
\[
F(r(u))=\frac{1+u}{1-u},\qquad
\ell(r(u))=\log\frac{1+u^2}{(1+u)^2},
\]
\[
H_g(r(u))=\frac{1+u}{1-u}\left[g+
2\int_0^u\frac{\log((1+s^2)/(1+s)^2)}{1+s^2}\,ds\right].
\tag{P3}
\]
P3由直接换元或两边微分及u=0初值证明；u=1的积分值仍为−K。对任意g,g'∈Q，
\[
H_g\circ r-H_{g'}\circ r
=(g-g')\frac{1+u}{1-u}\in Q(u).
\tag{P4}
\]
对任意常数g,g'，右侧仍为复系数有理函数。因CDT允许meromorphic pullback，u=1处由pole变为removable并不改变共同亚纯图准入；所有transported叶上的差仍是同一有理函数。对有理g，Q(u)-span亦完全相同。

全算术没有遗漏cover成本：r∈uZ[[u]]，所以旧源前N项清分母也清除复合源前N项。固定b_gg∈Z时
\[
b_gd_Nd_{\lfloor N/2\rfloor}[u^n](H_g\circ r)\in Z
\quad(0\le n\le N),\qquad
d_N[u^n](\ell\circ r)\in Z.
\tag{P5}
\]
F∘r整数。更精确地，P4使任何两个固定有理g的scalar prefix LCD只相差至多一个固定分母因子：两方向同样成立；这里只比较同一函数行，不宣称最优联合格。

三行在Q(u)上独立：取u=i的局部支路，P3的被积函数首项为
(1/i)log(u−i)/(u−i)，F∘r在i处等于i。因此H_g∘r的首项是(1/2)log²(u−i)，ℓ∘r只有一级log。任意非零有理系数具有有限阶零/极点，不能用一级log或亚纯项消去二级log；继而一级log亦不能由亚纯项消去。

P5给与240相同的safe类型：ℓ行σ=1，H行两列宽1及1/2，故三行τ=7/6。若一张合法共同图有λ=log|φ'(0)|、BC分子J并满足
\[
3(\lambda-7/6)>J,
\tag{P6}
\]
由于图准入和类型均对g相同，它会无条件否定g=0这套确实存在的Q系数rank3源。直接CDT rank bound禁止这种情况。证毕。

停止范围是P2固定覆盖及这套basic三行入口；不排除原x源的新物理叶、其它真正目标投影或新的整格/metric。特别不能说“所有K方法失败”。原x继续的第一门槛仍是同一图上全部x=1/4 preimages的实际补点，加3(log c−7/6)>J；仅c>exp(7/4)不够。当前bivalent/ quadrivalent缩放图的导数4、4√2连此必要条件也未过。更高价图不能只读导数，更不能用P2免费修叶。

## 3. 一手文献复核：已知真实投影不是新数值出口

本轮定向检索并核官方作者页面及版本记录：Eskandari–Murty–Nemoto仍为[2510.20648v3](https://arxiv.org/abs/2510.20648v3)，2026-08-29；两篇周期族/逼近稿仍为2609.26308/354v1，2026-09-22。它们已在本项目20261004/07归档，未重复下载，不称本轮新机制。

其[Theorem8.3.1及完整§8.3](https://arxiv.org/html/2510.20648v3#S8.SS3)确实给旋转不变整数多项式F的纯a_F+b_FG投影和2^(N+2)d_Nd_(N/2)全scalar清分母。正积分可支付非零，但这个统一清分母下的特定非负族早已由本项目完整下界排除；实际primitive content、高极点、带符号积分及新det仍未由该下界排除。此二维投影不能因改导子或插入log就自动成为K/χ₋₇投影。

两族[Theorem1.1](https://arxiv.org/html/2609.26308v1#S1)的Gamma因子是真实有理归一化；motivic与hypergeometric名称不同不等于新的净率。近期0.62逼近声明也不是无理性门槛。本轮没有FULL核这三篇全部证明或重做其旧content账。

CDT当前原件物理175–180给Hadamard关系产生Q系数、真正overconvergent的新G函数；这是具体可移植原则。但其中近参数log乘积和其§2.11的χ₋₃组合本身已是原定理，不能作为我们的新数值目标。物理190–199明确：Hermite–Padé近似的生成函数不自动是G函数；§15.2的有效module finiteness是Question15.2.2，不能当已证廉价投影定理。这些判断没有添加Betti/Hodge作为直接CDT必要条件。

原M₀,₁₀对象若要恢复，首lemma须对全部n落实240指定的剩余六通道，并证明全部五个禁通道消失。D₃右因子条件只控制其中三项，另两个Tate通道仍须消除；240已核的fixed diagonal Euler/Stokes失败也只限该字段/原积分，不能推出所有relative projector失败。本轮没有新的完整六通道证书，因此保持条件储备。

## 4. χ₋₇提供了实际数值连接，但先查导子全账

本轮实际FULL独核Root最终
[正载体稿](global_chi7_positive_carrier_round244_20261009.md)，7698B、
SHA256 639071cdf1d9469046246623e2308069b55271650cd74a17d3f837720b6d34c3。
其移线得到同一实偶μχ；三项sin核的第一正项严格支配唯一负项，故μχ(y)>0(y≠0)，质量1/49。
全商部有理，且
\[
V_\chi((t+j)^{-1})=j(L-H^{(2)}_{7j,\chi}),\quad
V_\chi((t-j)^{-1})=-j(L-H^{(2)}_{7j,\chi}).
\tag{P7}
\]
这是单一实际L目标，而不是周期空间的形式投影。

取A_n=R_n(t)R_n(−t)，真实矩表变为相位共轭后的正Gram，所以对所有n,h都有实际非零。目标Hankel块rank≥2n−1，故不是228的rank-one common-period移位Gram；但也不能据此领预算。A_n把外场变成|R_n|²；非对称R_n的能量及费用不能移给它。

更关键的是非对称源出现新外国窗口：35n/2<p<35n时，完整p²首层是k=5n−⌈p/7⌉+1个单位节点原子，rank恰k；全部det系数费用upper≤2k，其PNT积分175/4。它不是actual费用lower：完整余块可以有positive content。它却具体否定“最高head降二阶就值得连续投入”的依据。固定7与所有其余素数、商部Bernoulli及归一化仍须同账。

## 5. 后续一手输入：导子匹配CM源的完整系数桥

本轮随后实际FULL读取Sun–Zhou现行v2的保存选段（完整Introduction、Theorem1.1(a,b)、Table1），并FULL读Root
[CM log-trigger稿](global_cm_log_trigger_round244_20261009.md)。
[原文v2](https://arxiv.org/html/2602.12091v2)的(1.12)及Thm1.1/Table1给
\[
F_0(z)=\sum_{n\ge0}a_nz^n,\quad
G_0(z)=\sum_{n\ge0}a_n
\left(H_{2n}^{(2)}-\frac{25}{92}H_n^{(2)}\right)z^n,\quad
a_n=\binom{2n}n^3,
\]
\[
z_0=1/4096,\qquad G_0(z_0)/F_0(z_0)=-X/1104.
\tag{P9}
\]
这按作者已证明的评价定理输入使用：引言先记录prior conjecture，随后明言Thm1.1及Table1推出(1.9)–(1.12)。本人未FULL核全部§2 modular proof，亦不从这个身份推出X无理或全球novelty。

取g=X/1104∈Q反证，S_g=G_0+gF_0，
\[
\mathcal H_g(z)=\int_0^z\frac{S_g(t)}{1-4096t}\,dt .
\tag{P10}
\]
z₀在原F₀、G₀的半径1/64内；P9令S_g(z₀)=0，确实消掉积分器的非亚纯log。这比普通点的商函数去pole强，且不同于P4：\(\mathcal H_g-\mathcal H_{g'}\)含积分F₀/(1−4096z)的真log，不能在普通点由F₀、G₀的有理系数组合吸收。但全部transported叶仍未付。

这里有两条自含全系数资产，而不只是建议。首先，若b_gg∈Z，逐项积分的全部prefix由
\[
92b_g\,d_Nd_{2N}^{\,2}
[z^m]\mathcal H_g\in Z\quad(0\le m\le N)
\tag{P11}
\]
清除；92b_gd_(2N)²清S_g，F₀整数。证明是[z^m]H=(1/m)Σ_(n<m)4096^(m−1−n)[z^n]S，内层d_(2n)²、外层m分别由d_(2N)²、d_N支付，全部prime powers均成立。原坐标4096的幂是整数，不是分母；缩放z=u/4096才需连同实侧重新付4096^N。P11也蕴含较粗的d_(2N)³安全界，不是primitive最优费用。

其次，令θ=z∂z、L=θ³−8z(2θ+1)³。n≥1的完整调和差为
\[
\left(H_{2n}^{(2)}-\frac{25}{92}H_n^{(2)}\right)
-\left(H_{2n-2}^{(2)}-\frac{25}{92}H_{n-1}^{(2)}\right)
=\frac1{(2n-1)^2}-\frac1{46n^2}.
\]
由n³a_n=8(2n−1)³a_(n−1)，包括n=0的初值逐项得到
\[
LF_0=0,\qquad LS_g=
\left[8z(2\theta+1)-\theta/46\right]F_0,\qquad
\theta\mathcal H_g=\frac{zS_g}{1-4096z}.
\tag{P12}
\]
因此实际完整七行
(F₀,θF₀,θ²F₀,S_g,θS_g,θ²S_g,\(\mathcal H_g\))有明确rational closure：
\[
\theta^3F_0=
\frac{96z\theta^2F_0+48z\theta F_0+8zF_0}{1-64z},
\]
\[
\theta^3S_g=
\frac{96z\theta^2S_g+48z\theta S_g+8zS_g
+8zF_0+(16z-1/46)\theta F_0}{1-64z}.
\tag{P13}
\]
结合P12其余shift行，就是原生Taylor芽的完整一阶有理系统；θ迭代不改变P11的prefix清分母，三类safe scalar率为0、4、5。它支付holonomicity和rank≤7，绝不是最小rank7或七行函数独立的证书；将三类率直接报作CDT最优τ仍不合法。首次不可跳过的门槛已具体缩为actual cyclic rank与同一native relation的所有图叶，而非等待一个未给定的抽象连接。

## 6. 下一轮唯一决定成败门槛

建议停K5同源局部优化；χ₋₇标量Rn保留完整预算校准，不给逐prime后续轮。若恢复此标量对象，保持固定非对称h=3n及同一Q̂χ,n，令
\[
\gamma_{n,p}=\min_e v_p([T^e]Q̂_{\chi,n}),\qquad
\log d_n=-\sum_p\gamma_{n,p}\log p .
\tag{P8}
\]
这是完整primitive比例；positive Gauss content也必须保留，不能只累积entry denominators。首lemma须给覆盖新5n..35n外国区、固定7和其余全部prime powers的统一宏观机制，证明同对象费用与实际已认证能量之和严格负。若另采用原absolute-Heine−6输入，则明确它的认证范围并要求费用leading upper<6；本文没有FULL重认证原Fstar数值证书。

非对称实际∞非零仍须另付；对称R8不解决它。safe LCD、175/4之类粗upper或有限头仍不足以给标量移植继续依据，也不是L₂χ₋₇有理或全方法no-go。

基于本轮后续P9–P13，优先给CM混合积分器一次有界245–246完整cyclic/全leaf准入，不预设成功。**下一轮唯一首lemma：**在P12–P13这个确定源上给最小cyclic商及实际Q(z)函数秩，保留native填点；逐目标z₀-preimage证明transported分子确实为0，或给出一个不为0的具体叶而停该图。没有这个证书不搜索map参数、不优化prime。其后才把合法完整类型与同对象BC/holonomy能量比较。K保留原x物理叶门槛，M₀,₁₀保留全n六通道门槛，都不自动获得新窗口。

精确实读范围和输入身份见
[packet scope](../literature/global_review_sources_round244_20261009/packet_reading_scope.md)。
仅新增本稿、scope与独审收据；旧文件未改。保存后作者实际FULL复读不冒充独立审阅。
