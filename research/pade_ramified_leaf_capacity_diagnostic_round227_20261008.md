# 第227轮：分歧图上限的全叶量词与实际准入诊断

2026-10-08。固定222–226的原R_n、D、X及H_g=gD+X；不换源、不删有限尾。本稿独立纸付一个会改变图界论证的精确障碍：**原生径向非零半整数分支、局部reflection及整体不可约性，仍不足以迫使合法图在该值的所有前像偶数分歧。** 两值完全偶分歧本身也没有有限导数上限。三值orbifold界及唯一原点的64|a|界只在明示条件下成立；当前packet未支付这些条件。

本轮没有构造原packet的正净收益图或完整新整模型，没有证明全部ramified图失败。按227准入规则，本接口没有给继续主攻的认证对象，应把固定包降为结构工具，供228复盘比较；数值ζ/L目标仍active。数学程序0。

## 1. 同一实际packet及历史排重

**N1.** 冻结226已经付清：实际二十个非零有限operator谱点simple，整个相关向量在每点为analytic+t^(31/2)analytic；允许fractional系数为0。原D在ρ_M=−1/M的原生径向branch非零，原J在225已识别的T_s或Tκ尺度有实际径向branch。H_g在ζ7=g∈Q时才等于J的生成芽；{1,D,H_g}的函数域秩3不变。

原共同图ρ_M(2t−t²)、|t|<3/2只支付一张der3/M<1的图。0其他返回叶、∞及全局monodromy仍未付。不能把本轮conditional orbifold另当成这张图已经满足的必要上限。

**N2.** 历史level20 leaf稿完整§§4–7已记录：匹配CDT时要核全部foreign前像、native0、canonical叶及finite involutions；其三elliptic值提升为genus1曲线，不自动给capacity；native0唯一+omit cusp的Carathéodory界也已有。这里只将方法应用所需量词重新核清，未把这些旧framework包装成新载体。本文不继承旧level20的非零log来否定当前无logpacket。

## 2. 局部reflection究竟要求哪个前像分歧

**N3.** 在一个已付simple finite点a，226 augmented系统的residue满足R²=ηR，η是非整数半整数。令Π=R/η，则Π²=Π、rankΠ=1。收敛gauge后的局部monodromy为

`M_a=I−2Π`。

因此固定空间kerΠ很大；局部全解阶2不是每个解都有分支。对沿具体路径γ从原芽延拓来的实际tuple，是否有fractional项取决于其connection coefficient落在Π方向与否。Π≠0只保证某些解分支，不保证每个reachable叶均分支；形式不可约也不改这个区别。

**N4.** 设φ(ζ0)=a、局部次数e≥1。在该前像实际到达的叶上，若D或X有非零局部项

`(z−a)^(31/2+k)b(z)，k∈Z，b(a)≠0`，

则拉回指数为e(31/2+k)。e奇数时是非整数半整数，故不能meromorphic；e偶数才消掉这一分支。固定阶原变量导数只改整数k，不改此奇偶性。若这一叶D、X的fractional部分都为0，e=1亦可能合法。只保留H_g时，还需检查gB_D+B_X有无抵消。

因此“每个φ-preimage都even”需要**每个该图可达叶上至少一个保留源的fractional系数非零**。原径向证明只处理一条指定path，不能支付该全称命题。下节给包含holonomic、函数域秩及不可约monodromy的精确反例；它用于否定这一逻辑推导，不替代当前packet的connection计算。

## 3. 不可约cubic芽仍允许simple前像与任意大图

**N5.** 令w(z)为

`w³−3w=z，w(0)=0`

的原生解析芽。由implicit function theorem它在0存在，且Taylor系数有理。该cubic在Q(z)不可约：若有rational root，有限pole会在左边产生pole而右边有限，所以root必为polynomial；非恒定polynomial的三次组合degree不可能为1。故{1,w,w²}在Q(z)上独立，秩3。

直接微分原cubic，w满足完整二阶方程

`(4−z²)w″−zw′+w/9=0`。                         (N5.1)

验证可用w′=1/[3(w²−1)]、w″=−2w/[9(w²−1)³]及4−z²=−(w²−1)²(w²−4)。w²同样holonomic：Q(z,w)是三维且在d/dz下封闭，有限维线性依赖即给有理系数微分方程。

**N6.** 在z=−2，原生径向w趋于1；写w=1+δ得z=−2+3δ²+δ³，所以其square-root项非零。另一叶w=−2却正则，因为3w²−3=9。在z=2同理：原生w趋于−1、有非零square-root，而w=2叶正则。局部indices0、1/2，两处monodromy均为reflection。

三根函数之和为0；任取两根独立，例如在0，w_0=0、w_+=√3且w_0′=−1/3。两branch transpositions共享原生root，生成S3；其在三根和为0的二维空间是标准不可约表示。具体地，每个transposition的固定/反固定线与另一个transposition的对应线都没有共同非零向量。因此即使在这个真正不可约的两维monodromy空间，第三叶仍可落在某一个reflection的固定线。

**N7.** 对任意实K>0，取整个polynomial图

`Φ_K(ζ)=K³ζ³−3Kζ`。

在0附近w(Φ_K(ζ))=Kζ；右侧是整个函数，因而给该拉回的完整单值延拓。tuple {1,w,w²}全体拉回为1、Kζ、K²ζ²，均在unit disc的邻域全纯，且

`Φ_K(0)=0，|Φ_K′(0)|=3K→∞`。

但

`Φ_K+2=(Kζ−1)²(Kζ+2)，Φ_K−2=(Kζ+1)²(Kζ−2)`。

当K>2时，−2在ζ=−2/K有**simple**前像，那里正是在w=−2的正则叶；+2在2/K亦然。native0的其它前像±√3/K到达另外两条正则0叶。这同时证明：native两处真实分支、局部order2、global不可约及rank3本身，既不强迫全部even fibers，也不强迫原点唯一，更不产生universal derivative cap。

该例不是实际Padé packet，不能证明原D/X有这样的大图；只是这些已付输入不能推出所希望的所有图上限。也没有声称完整算术holonomy允许免费使用此例。

## 4. 同一反例的真实energy与固定3-adic费用

**N8.** 为免把任意大derivative误读成净收益，直接算这个同一Φ_K的CDT双积分energy。取K≥1，归一Haar测度μ，定义

`E(Φ)=∫∫ log|Φ(z)−Φ(w)| dμ(z)dμ(w)，|z|=|w|=1`。

由差分factorization及∫∫log|z−w|=0，换变量u=z/w（torus的Haar保持变换），再在w²上用Jensen，严格得到

`E(Φ_K)=3logK+∫ log max(|1+u+u²|,3/K²)dμ(u)`。       (N8.1)

polynomial1+u+u²的两根在unit circle，constant term为1，故其log Mahler measure为0。max项的积分≥0，且当K→∞趋于0；log|1+u+u²|的两个对数奇点可积，dominated convergence支付极限。因此

`E(Φ_K)≥3logK，3log|Φ_K′(0)|−E(Φ_K)≤3log3`。       (N8.2)

rank3的解析margin不会随K无界增大。对于假定类型费用τ，3(ℓ−τ)−E至多3log3−3τ；这只是此指定polynomial family的精确账，不是所有maps的上限或当前packet的τ下界。

**N9.** 原芽还有一个明确的不合法算术入口。写w=zψ(w)、ψ(t)=−1/[3(1−t²/3)]。Lagrange系数公式可由Cauchy residue换元z=t/ψ(t)及一次formal integration by parts自证：[z^m]w=(1/m)[t^(m−1)]ψ(t)^m。因此

`[z^(2n+1)]w=−binom(3n,n)/[(2n+1)3^(3n+1)]，n≥0；`

`[z^(2n)]w=0，n≥0`。                              (N9.1)

其中n=0给−z/3，符号不是交错。由Legendre floor公式，v3 binom(3n,n)是各个floor carry的0/1之和，至多O(log(n+2))；v3(2n+1)亦O(log(n+2))。故

`v3([z^(2n+1)]w)=−3n−1+O(log(n+2))`，

并有实际3-adic convergence radius **3^(−3/2)**。任意有限固定LCM数组在固定p=3仅提供O(log n)深度，乘固定整数亦只改O(1)，不能整化这个原芽的线性负深度。既有arbitrary derivative反例没有跨过完整整模型；它不是CDT theorem的反例或新数值无理性入口。本文没有据此断言允许S-integer/maps的全部数域方法失败。

## 5. 真正可用的conditional bounds与停止判断

**N10. 两值也不足。** 即使额外要求两个非零不同值a,b的全部preimages均even，holomorphic到C仍无universal derivative cap。令c=(a+b)/2、d=(b−a)/2，选cosh h0=−c/d。a,b非零使sinh h0≠0。整个图

`φ_K(ζ)=c+d cosh(h0+Kζ)`

满足φ_K(0)=0、|φ_K′(0)|=|d sinh h0|K；而φ_K−a=2d cosh²((h0+Kζ)/2)、φ_K−b=2d sinh²((h0+Kζ)/2)，全部fibers均even。∞不取。primary的(2,2,∞) parabolic classification与此显式证明一致；无需把该family认成当前packet共同图。

**N11. 三值仅conditional。** 若已支付三个不同非零值a1,a2,a3的全部preimages even，则φ:D→C是到signature(2,2,2,∞) orbifold O的holomorphic map。其Euler characteristic=2−3/2−1=−1/2，故hyperbolic；按curvature−1归一，完整orbifold Schwarz lemma给

`|φ′(0)|≤2/λ_O(0)`。                             (N11.1)

λ_O(0)>0，但其数值/conformal comparison仍须另付；存在finite constant不自动证明小于1或小于exp τ。更基本地，当前实际packet未证这三个值的全叶非零fractional系数，所以不能应用此界。三value genus1提升也已见历史level20，未作为新付carrier。

**N12. 唯一native0的64|a|界。** 若额外支付φ^−1(0)={0}及一个非零值a的全部preimages even（允许a omitted），unit disc上存在s=√(1−φ/a)，取s(0)=1。even divisor及simply connectedness支付global square root。由原点唯一，s不能取−1。于是g=(1−s)/2是holomorphic、g^−1(0)={0}并omit1。冻结CDT§2.8引用的完整Carathéodory界给|g′(0)|≤16，而g′(0)=φ′(0)/(4a)，故

`|φ′(0)|≤64|a|`。                                (N12.1)

取a=ρ_M则64/M<1。这是严格、无需数值的**指定类cap**；当前packet没有证所有合法图满足原点唯一或所有a-preimages even，不能推广为全部ramified maps。226的小图具有这些条件，不能从一张图的性质反推所有图。

**N13.** 全面图界的可审入口是同一tuple在每条实际connection path上至少一个fractional coefficient非零，或另一个确切的return-to0/log/leaf排除定理；这比已付local involution或generic irreducibility更强。没有这样的新证明，也没有一个原packet positive map+energy+完整费用对象，本稿不再把conditional三值uniformization作为继续主攻的理由。

227本接口未获实际正准入；建议按冻结停止规则将本源降为结构工具，在228全局复盘转向能给新完整算术/解析结构的源。未证明所有同包maps不可能，未抹掉223–226已付资产；正式cadence仍222→228（允许226–230），没有新数值ζ/L定理。

## 6. Primary范围、运行及保存

**N14.** 只采用两个primary来源的明确选段：McMullen作者 *Complex Dynamics and Renormalization*，[author PDF](https://people.math.harvard.edu/~ctm/papers/home/text/papers/real/book.pdf) 的完整PDF182–188（印刷177–183），全部§A.1/§A.2含orbifold map的divisibility条件、全部uniformization分类和完整TheoremA.3；仅使用这些条件和curvature归一，不称FULL219页。另完整读冻结CDT PDF23–27，包含§2.8的Carathéodory条件和完整§2.9/Proposition2.9.3。后者是sufficient univalent-leaf设计，不是所有合法CDT地图都必须原点唯一的定理。没有读Carathéodory1954书原页，因此界16的primary证据是CDT原文准确引用，而不是冒称独审原书证明。

**N15.** NEW227保存新PDF1、selectedTXT3，HTML/TEX0；旧CDT原件复用不重下载。bounded web searches的Beardon–Minda、Eremenko及其它结果仅定位，未采用其摘要/未完整读定理，也未下载。actual读取范围和exact identity详见[作者scope](../literature/pade_ramified_capacity_sources_round227_20261008/dual_reading_scope.md)。

全部counterexample、energy、Lagrange、估值和conditional cap均纸推；数学程序0，旧producer/import/rerun0，无参数/素数/能量扫描、数值积分、CAS、PSLQ、Lean、Git mutation。下载/文字提取/hash/Markdown是文档操作。本文保存后须 actual FULL 作者复读并登记bytes/SHA；作者自读不替代独审。
