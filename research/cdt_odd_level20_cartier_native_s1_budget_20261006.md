# level20 native S1 的条件账本与严格收益门槛

日期：2026-10-06。本文只新增。输入是 [六积分 packet](cdt_odd_level20_cartier_packet_matrix_20261006.md)、[原生前缀秩](cdt_odd_level20_cartier_native_rank_20261006.md)、[冻结 rank19 固定表](cdt_odd_level20_cartier_rank19_budget_20261006.md) 和 [integrated tensor 接口](cdt_odd_level20_integrated_tensor_bridge_20261006.md)。结论是一个条件性增益公式，以及比该公式更乐观、仍严格失败的全 cutoff 账本。未证明新的全局净 Smith 桥，没有假设非普通素数密度，没有新数值无理性定理。

## 1. 对象、prefix 和已知 native 方向

仍取 rank19 固定 unit 表：m=19、τflatflat=963/361、E=14、e*=1、a₀=2、s=4。六个新增积分 I_j 的 ν_j=4，pure p⁴-evaluation 的统一 baseline floor为0；其余13 rows 的 ν≤3。三个旧 H rows 有 baseline1，旧 k₁、k₂ 只将它们提升到threshold2、3。

实际 prefix 为 n<N_D，N_D=19(D+1)+O(1)，涵盖原 primitive leading flag。只使用 p²>N_D、p<N_D 的好place；原点周期分母、规范与 packet 首项109只排固定坏素数。小p的排除不改变下列 D² 主项。

记 k𝔭=dimₖker(M̄_p)。固定 Hecke 分解给

\[
k_{\mathfrak p}=2\mathbf1_{\alpha_O(p)=0}
                 +\mathbf1_{\alpha_N(p)=0}\le3.
\tag{B1}
\]

Eisenstein三维block为unit，故不能从「每符号三维源空间」误推出整个六矩阵的核为3；B1只是最多3，并且是否出现仍依赖实际mod𝔭标量。

选择kerM的residue basis、任取integral lifts；各行只支持六个新积分。packet给其p⁴评价像在𝔭中、source至少一个unit coefficient。因此乘以tᵃ、0≤a≤D后，提供 k𝔭(D+1) 个 residue-independent primitive S1 方向。完整 prefix 的消除保证shift也消除；不能只核某个较短prefix后，未经长度调整就乘任意shift。

原生秩稿已证明慢变量前六个系数构成unit三角矩阵。因此在N≥6p+1时，constant kernel恰为kerM；p>D且N−1−D≥6p时，整个degree≤D原生核亦恰为这些monomial shifts。在目前ξ约1.28或本稿最乐观ξ约1.6的窗口内，此长度条件具有固定正余量，没有免费的短前缀增核。p≤D的不同monomial residue重叠，仍不在该精确多项式等式的范围内。

## 2. 同一 cutoff 下的形式接口

设a≤min(2,ξ)，并始终先固定ξ与a，再取D、tensor degree及各严格内窗极限。新的native S1支持六个ν=4 blocks；旧H的k₁、k₂只支持三个旧blocks。因此在统一p⁴矩阵中可安全相加的local floor账本为

\[
\begin{array}{c|c}
\text{threshold}&\text{保证的方向数}\\\hline
1&13(D+1)+k_{\mathfrak p}(D+1)\\
2&5(D+1)+k_1\\
3&2(D+1)+k_2\\
4&D+1.
\end{array}
\tag{B2}
\]

old S1与old S2允许嵌套；新的S1与旧方向在source坐标支持上分离。新方向仅增加第一层，不能再把同一k𝔭同时计入threshold2、3。

定义field-normalized候选累计信用

\[
\Gamma_I(a)=\liminf_{D\to\infty}\frac1{D^2[K:\mathbf Q]}
 \sum_{\substack{\sqrt{N_D}<p\le aD\\\mathfrak p\mid p}}
 k_{\mathfrak p}(D+1)\log\operatorname{Norm}\mathfrak p.
\tag{B3}
\]

这里不可再乘两个embedding。即使不给任何密度假设，PNT与B1已给Γ_I(a)≤3a。B3若用于更窄strict window，最后从内侧逼近a；边缘只按有界counts处理。

如果B2经**同一实际source、selected leading minor与same-ξ baseline**认领为净determinantal增益，则已冻DVR tensor论证的cap仍为4、codimension损失仍为4dc，finite归一信用是Γ_I/19、最终cost信用才是2Γ_I/361。因此其限定形式公式为

\[
\boxed{\kappa_{\rm native}(\xi;a)
 =\frac{963}{361}+\frac2{361}
  \{P_{19}(\xi)-\gamma(\min(\xi,1))-\Gamma_I(a)\},}
\qquad P_{19}(\xi)=14\xi+I_{19}(\xi).
\tag{B4}
\]

B4不是本稿已经完成的新全局CDT定理。认领前须核：native evaluation与原积分species的整格坐标一致；完整prefix包含flag；局部primitive submodules与near-balanced坐标子格的饱和交正确；native方向不是原row/source因子重复；同ξ的sharp小prime baseline覆盖此窗口。a≤a₀=2保证flat匹配，a≤ξ保证使用原小prime序号粗界；a不必再被旧H的有效x≤1截断，因为新方向degree0。不过旧γ仍按原公式计，不能据此将它扩大到ξ。

## 3. 原最佳 cutoff：即使三维在每个素数都出现也不够

冻结账本的P19最小区间是[19/15,9/7]，Pmin=(37/2)H₁₄，旧γ=5/6。取具体ξ=a=9/7，甚至给每个好place k𝔭=3、全部合法净信用，则Γ_I≤27/7。这个乐观成本为

\[
\kappa_{9/7}^{\rm opt}
 =\frac{389780201}{130089960}-\frac{54}{7\cdot361}
 =\frac{387000281}{130089960},
\]
\[
\boxed{\rho>\frac{19}{18}\kappa_{9/7}^{\rm opt}
  =\frac{387000281}{123243120}
  >\frac{14}{5}>\log16.}
\tag{B5}
\]

该必要尺度约3.14014。未知nonordinary密度只会减少B3的信用，不会改善B5。

## 4. 大prime短prefix核与更强的全ξ过度信用

纯长度的constant核从p约N/6≈19D/6才出现，不能用于ξ约1.28的主窗口。不能把kerM与(6−r)_+相加；实际constant核为ker(V_rM)，两种来源可能重叠。

对p>D，原生秩稿按不同monomial residue a 分块，r_a=floor((N−1−a)/p)。若M可逆，整个raw polynomial kernel的精确数为

\[
K_{p,N,D}^{\rm ord}
 =\sum_{h=1}^6\min\{D+1,(D+1-N+hp)_+\}.
\tag{B6}
\]

这从p/D>3启动，比constant kernel的19/6早，原因只是高shift缩短prefix。对退化M，Sylvester rank inequality给每个a的安全上界

\[
6-\operatorname{rank}(V_{r_a}\overline M_p)
 \le k_{\mathfrak p}+(6-r_a)_+.
\tag{B7}
\]

所以可把「三维Hecke核全给」与「可逆矩阵的全部长度核全给」相加，作为一个**过度信用上界**；真正两类核的重叠反而不应如此相加。令

\[
k_{19}(x)=\sum_{h=1}^6\operatorname{clamp}(hx-18,0,1),
\qquad G(\xi)=\int_0^\xi k_{19}(x)\,dx.
\tag{B8}
\]

G=0在ξ≤3；G(19)=2747/40。它是raw kernel面积，不是已证净height。大prime窗口不满足此前a₀=2的flat饱和匹配，sharp尾部也可能已经记入这些前缀限制；尤其不能把raw S1直接再扣一次原baseline。以下故意将这些未核净收益、所有place普通与非普通的重叠全部乐观认领，并甚至取消a≤2限制，给

\[
\boxed{\Gamma_{\rm over}(\xi)=3\xi+G(\xi).}
\tag{B9}
\]

只对已知kerM生成的小prime族以及p>D的原生S1族作这个上界；它不排p≤D未知的cross-residue polynomial kernels，也不涵盖S2以上的新层。

即使这种过度信用，重新选择ξ也不能成功。证明如下。原完整积分成本在ξ≥1有

\[
I_{19}'(\xi)=-\sum_{k=1}^{18}
          \operatorname{clamp}(19-k\xi,0,1),
\tag{B10}
\]

从固定rank19账本逐项的C¹ convex函数直接求导。对ξ≥3，k≥7的项全零，并逐个使用

\[
\operatorname{clamp}(h\xi-18,0,1)
 +\operatorname{clamp}(19-h\xi,0,1)=1
\]

得到精确恒等式

\[
\boxed{I_{19}'=G'-6,\quad
 (P_{19}-G)'=8,\quad (P_{19}-3\xi-G)'=5
 \qquad(\xi\ge3).}
\tag{B11}
\]

所以越过3后，sharp成本比全部raw长度面积加三维信用还增长得快，不可能在大窗口找到更小形式成本。

ξ≤3时G=0。min(11ξ+I₁₉)的精确区间为

\[
\boxed{19/12\le\xi\le18/11,
\qquad\min(11\xi+I_{19})=(37/2)H_{11},
\quad H_{11}=83711/27720.}
\tag{B12}
\]

证明与原表相同：ξ≤1的导数为ξ−8<0；ξ≥1各combined term convex；在B12区间恰有k≤11处于线性段、k≥12为0，所以导数为0。B12在1<ξ<2内，旧γ正好饱和5/6，且G仍为0。ξ≥3由B11递增，ξ≤1可用γ≤5/6的乐观下界。因此**全[0,19]的过度信用最小值**为

\[
\boxed{\kappa_{\rm over,min}
 =\frac{963+37H_{11}-5/3}{361}
 =\frac{29745467}{10006920},}
\]
\[
\boxed{\rho>\frac{19}{18}\kappa_{\rm over,min}
 =\frac{29745467}{9480240}
 =\frac{14}{5}+\frac{640159}{1896048}
 >\log16.}
\tag{B13}
\]

必要尺度约3.13763。B13是一张比可认领B4更乐观的形式账本失败，不是先证明大prime桥又宣布失败。任意实际密度较小、两核重叠、raw收益被baseline吸收，只会使该规定输入更差。

## 5. 需要多大的密度、层数或有效窗口

以当前解析上限ρ≤log16，在原P19最小区间，新增净信用必须严格超过

\[
\boxed{\Gamma_{\rm req}
 =(37/2)H_{14}-5/6+963/2-171\log16.}
\tag{B14}
\]

新纯有理Taylor证书给2.772<log16<2.773。故

\[
\frac{1200675731}{18018000}
 <\Gamma_{\rm req}
 <\frac{1203756809}{18018000},
\tag{B15}
\]

即约66.64至66.81。对其它ξ，P≥Pmin与γ≤5/6保证所需信用至少有B15同一下界。

若仅为说明而假设两个block的field-normalized log-weighted nonordinary密度δO、δN存在，则kerM×shifts在窗口a的形式信用为a(2δO+δN)，各δ∈[0,1]。本稿不证明这些密度存在或非零。固定a=9/7，B15要求

\[
2\delta_O+\delta_N
 >\frac{1200675731}{23166000}>51,
\tag{B16}
\]

而左边≤3。密度方面没有可弥补的余量。

更一般，需要一个真实额外Smith层质量h(x)，使∫h(x)dx超过所需Γ，而不是只多几个depth1核。固定窗口9/7，即使所有p都出现同样层数：仅三个方向每个提供L层，必要L≥18；即使所有六个方向每个提供L层，也必要L≥9。这里每层都是额外净determinantal valuation，不能由一个modp关系重计。超过原p⁴分母的层属于新的正Smith整除性，须另证明，不能套现有cap4免费获得。

在全部当前matching窗口a≤2中，甚至乐观给六个方向各四层，累计最多24a≤48，仍小于B15的下界。若保持原成本最低值不变，仅三个S1方向需要有效a>1200675731/54054000>22，已超过整个N/D≈19的prefix范围；六个方向各四层也至少需a>1200675731/432432000>2.77，超过a₀=2。真正扩大ξ还会增加P19，故这些只是乐观必要条件，不是成功方案。B11–B13更精确地说明原长度核不能通过重选ξ补上这个差距。

这些门槛限定于固定rank19数组、原解析上限及规定的额外信用。改变完整分母类型、原source、其它p≤D actual polynomial kernels、更高净Smith层、degree过滤或共同几何仍是不同问题，本稿没有排除。

## 6. 同一支持内四层全部给满仍不足

还有一个比前述native S1族更宽、但范围必须明确的上界。固定本表的九个目标source species：三个旧H的ν=3、baseline1，六个新I的ν=4、baseline0。假设新增threshold只支持这九个species，只计统一p⁴矩阵的四层cap以内，并且信用只来自同一flat matching窗口p≤a₀D=2D。这里不要求关系保持旧、新支持分离，也不限制其阶数或degree；但不计混入其它background坐标的关系、outside-window信用及高于四层的正Smith阶。

每个prime的九species子空间秩为9(D+1)，cap4最多贡献36(D+1)个累计floors；其中三个旧H在threshold1已有3(D+1)个baseline floors。因此最大**额外**累计floor和是

\[
 3(4-1)(D+1)+6(4-0)(D+1)=33(D+1).
\tag{B17}
\]

这是有限维上界：四个threshold的高阶子空间在该支持内均不超过9(D+1)，扣掉已存在的三个threshold1 blocks。即使所有好prime都给满，field-normalized PNT积分也只给Γ_total≤2·33=66。这里Γ_total已经包含旧γ=5/6；不能再将它追加到66外面。为使账本更乐观，可以对任意ξ独立给予整段p≤2D的66，不再检查a≤ξ。

由于P₁₉(ξ)≥(37/2)H₁₄，任何采用这项上界的形式成本都满足

\[
\kappa\ge\frac{963+37H_{14}-132}{361}
 =\frac{342813281}{130089960},
\]
\[
\boxed{\rho>\frac{831+37H_{14}}{342}
 =\frac{342813281}{123243120}
 =\frac{2773}{1000}+\frac{26502731}{3081078000}
 >\frac{2773}{1000}>\log16.}
\tag{B18}
\]

该必要尺度约2.78160，低于14/5，所以这里必须用已经精确证明的log16<2.773，不能用14/5代替。B18排除的只是**本数组、同一九species支持、p≤2D matching窗口、四层cap以内**的全部额外信用组合，仍是一张过度信用的形式账本。它不排cross-background混合、更高Smith阶、outside-window输入、改变安全分母或source与几何；也没有把所有实际信用认领为新的global高度定理。

## 7. 核验与未完成声明

新Fraction certificate只核一张固定表和已确定的形式函数：same-cutoff counts、H11/H14、B5/B13/B15–B18、G的六个斜坡面积、B11的互补clamp代数、严格log16有理区间与层数必要门槛。不运行旧producer，不扫描素数，不猜nonordinary密度。

作者已执行本次新建并随§6更新的 [Fraction脚本](cdt_odd_level20_cartier_native_s1_budget_20261006_verify.py)，[JSON证书](cdt_odd_level20_cartier_native_s1_budget_20261006_verify.json) 记录59项精确检查通过。它不把上述尚未认领的global增益桥或密度、higher-layer输入当成核验项。

root已实际只读§6/B17–B18并限定独审通过：33(D+1)的cap上界、包含旧γ的总信用66、κ与ρ精确分数及ρ>2.773>log16均匹配。该审阅只认可本数组、九species支持、matching≤2D、cap4以内的过度信用账本；没有认领新global桥或排cross-background、outside-window及更高Smith阶。root未执行producer。此记录不把该限定审阅扩写为本文其它未完成接口的证明。

原生packet、unit慢前缀及p>D residue分解由root新native rank稿证明；本稿只核其预算后果。待认领的仍是实际global净高度桥和任何新的高层输入。本文已闭合的结果是：即使对规定的native S1方向采用超过已证接口的乐观信用，也不能使这张固定rank19表跨过当前解析上限。

以上正文与59-check配套证书现已冻结；后续研究使用新的报告，不改本组三文件或以重跑producer代替新增数学证据。
