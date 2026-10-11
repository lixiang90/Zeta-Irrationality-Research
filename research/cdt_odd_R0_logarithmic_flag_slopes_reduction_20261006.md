# R0 对数旗标到算术 slopes：全跳跃评价界与算术下降的严格 reduction

日期：2026-10-06。NEW 全尺度纸面研究。旧/同行数学 MD/PY/JSON/manifest全部只读，未执行、import或重跑；本轮没有数学 producer。本稿从实际 current R0 packet与原件评价不等式出发，不把一个 integer Betti operator当作 arithmetic Taylor gauge，也不宣称已经得到新的 vector-valued holonomy定理。

## G1. 当前权威状态与研究问题

本轮实际完整读主报告 §§85–93，SHA256
**1e0161b49ee96adae6cc30e9e7c89ca667b81877fd484919b86e7fd38e105f4c**；只读交付元数据确认366份旧冻结数学输入。actual九行paired packet加1的秩为10，严格前缀使用全place scale a=8√2、fixed2^25、P3(N)与LCM七/六次，主费τ=329/50。这些已证结果保持原范围。

原点整数旗标满足
\[
 N_0^3p_+\Phi(q)=0\quad\Longleftrightarrow\quad q=\alpha_0,
 \qquad\Phi(q)=\Phi_h+q\Phi_0.
 \tag{G1}
\]
这个条件检测 marked solution的最高log³，不代表完整branch单值或亚纯。

本轮另实际全文独审 NEW origin-orbit稿 a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc：真实整数行ℓ在全部signed words上模8为1，在physical words上为±1；因此所有transported Pc都不等于kerN²。任意q、任意有限cover的origin branch仍有非零primitive quotient jump。该独审另存，不将其作者回读当独审。当前packet合法CDT maps的meromorphy于是自动对q共同；q=0 reference仍阻止纯capacity优化的反证。

本稿问的是另一个接口：如果准许非零jump进入新的vector-valued评价定理，最高log资料究竟需要补什么，才可能成为degree平方级的、对目标值敏感的高度收益？

## G2. 原件的准确内容

本轮实际读取：

- CDT 2026 author原件 PDF3–8：Theorems2.1/2.6、Lemma2.9及其证明。其source是数域Taylor coefficients，目标是K-linear graded coefficient maps；所有实际组合在指定域须meromorphic。Lemma2.9的有效误差是
\[
 \bigl(n\log\rho^{-1}-(\kappa-\varepsilon)h(\beta)\bigr)^+.
 \tag{G2}
\]
误差来自完整的 B−ηA 与 B−βA差，而非一个nilpotent最高旗标。degree D与h(β)同比例时，这项总和才有D²主项。
- Bost 2006 PDF1–5、15–17：evaluation maps从K-rational formal germs构造；“parabolic Riemann surface”在这里指Liouville/null-boundary解析条件，不是给一个monodromy nilpotent flag指定parabolic weights。二者不能因为同一个词而混同。
- 新归档 Bost–Chambert-Loir arXiv math/0702593v3，实际读PDF1–4、6–8、17–22、37–40、47–49。PDF18的ϕ_D^i是K-linear map到(T_P^∨C)^i⊗L_P^D；PDF38–40的h(ϕ_D^i)=Σ_v log||ϕ_D^i||_v及(6.6)要求一个真正全处的、与i成正比例的收益。Theorem6.1要求A-analytic formal curve through P∈X(K)；Theorems7.8/7.9仍要求完整meromorphic extension与all-place条件。
- 新归档 André《Slope filtrations》，实际读PDF1–8、70–71。其12.1的arithmetic degree依赖O_K module和全部archimedean norms；differential regular-singular/Turrittin-Levelt slope是不同范畴的数据。统一形式论不会自动把后者的flag数值转为前者的Arakelov degree。

本轮新原件都正常默认证书验证TLS下载。BCL实际55页；André实际95页，首叶arXiv stamp为0812.3921v2/3Apr2009，但内部Date写November26,2024。receipt同时记录这两个观察，不将它冒认某一期刊版本。只读页定位/摘要不是全文阅读；精确actual范围见来源收据。

## G3. 新局部定理：带非零跳跃的 Cauchy评价公式

这是本稿真正自证的全尺度接口，尚不是全局arithmetic-holonomy theorem。

设D为单位盘，0不在一组有限piecewise-C¹ embedded arcs组成的cuts Γ中；arcs只有有限交点/节点，在这些点分段，使有限thin-cut加endpoint-circle的smooth exhaustion可用。cuts连接有限branch points至boundary，令
\[
 \rho=\inf_{z\in\Gamma}|z|>0.
\]
函数F在D减去cuts上single-valued holomorphic，在0附近holomorphic；每个cut内部的两侧branches各自在远离有限节点的compact subarc附近holomorphically延拓穿过人工cut，故thin-cut的两侧积分在这些subarcs上一致趋于所用traces。这是实际PF人工cuts具有的条件；也可直接假设相应thin-cut边界积分L¹收敛，但不能仅假设trace存在。外圈有integrable traces，并明确要求径向外边界积分在L¹中收敛至所用trace（例如F在闭盘各外边界arc附近延拓、边界cut端点满足下列可积增长条件即可）。cut两侧的trace差记JF；按cut边界方向选择其符号。假定各有限端点/节点b的增长为
\[
 F=O(|z-b|^{-\alpha_b}(1+|\log|z-b||)^{k_b}),
 \qquad \alpha_b<1,
 \tag{G3}
\]
并且JF在cuts上绝对可积。固定origin各分量的log或sqrt·log增长符合此条件；若改用具有更高pole的gauge，必须先另清这些pole，不能省略G3。

对于每个整数n≥0，令c_n=[z^n]F，则有带cut的精确Cauchy formula
\[
 c_n=\frac1{2\pi i}\int_{\partial D}\frac{F(z)}{z^{n+1}}dz
   +\frac1{2\pi i}\sum_{\Gamma_j}
      \int_{\Gamma_j}\frac{JF(z)}{z^{n+1}}dz .
 \tag{G4}
\]
亦可先取smooth outer circles并取trace极限。若存在interior ordinary poles，formula另有residues；本定理的版本没有默默删掉它们。

证明：先固定各endpoint/节点半径ε的小圈，再挖去剩余有限smooth cut subarcs的细管，沿其整个边界应用Cauchy。远离节点的bank解析延拓保证细管两侧boundary integrals趋于JF积分，不存在未记录的cut边界mass。endpoint circle integrals至多常数ε^{1−α_b}(1+|logε|)^{k_b}，故对每个固定n和F趋0；z^{-n−1}在b≠0处bounded。随后令ε趋0，绝对integrability使cut积分极限存在，外圈另由已列L¹径向收敛得到G4。每个D,n均先有这个精确formula，因此无需把n→∞与ε→0交换。

特别，
\[
 |c_n|\le \frac1{2\pi}\int_{\partial D}|F||dz|
 +\frac{\rho^{-n-1}}{2\pi}
       \sum_j\int_{\Gamma_j}|JF||dz|.
 \tag{G5}
\]
这明确说明：允许log branch后，outer-domain容量估计必须额外支付**完整jump积分**；最高log项为零不令第二项消失。

## G4. degree-uniform operator版本与真正的正部误差

设E_D为某一固定degree D的normed辅助空间，s↦F_s线性，所有F_s满足G3–G4。对所有||s||≤1同时要求
\[
 \frac1{2\pi}\int_{\partial D}|F_s||dz|\le M_D,\qquad
 \frac1{2\pi}\sum_j\int_{\Gamma_j}|JF_s||dz|
       \le C_\Gamma M_D\,e^{-\sigma D}.
 \tag{G6}
\]
CΓ、ρ与σ独立于D,n和s；M_D>0，σ≥0。允许用一个固定integrable weight w(z)证明第二式，例如|JF_s|≤M_De^{-σD}w、Σ∫w<∞。

则对所有D,n有实际operator norm界
\[
 \log\|{\rm ev}_{D,n}\|
 \le\log M_D+
       (n\log\rho^{-1}-\sigma D)^+ +O_\Gamma(1).
 \tag{G7}
\]
证明：对G5取source unit ball上sup，ρ^{-1}并入固定CΓ，使用
log(1+C e^u)≤u^++log(1+C)。无有限截断或渐近猜测。

其形状与CDT Lemma2.9完全相同，但本定理的第二式控制完整cut-jump operator，尚未在R0实际辅助lattice上证明。它并非只控制一个branch vector或某个log coefficient；单个q恰好取消最高log，不能代替source unit ball上的G6。

该接口可以用于新的logarithmic/vector-valued theorem：source继续是arithmetically defined coefficient space，archimedean评价改用G7，finite-place heights与rank/injectivity另完整证明。没有这些额外输入，就不能把G7当作现成CDT定理套用。

## G5. 若真有jump抑制，degree平方收益怎样产生

设a=logρ^{-1}>0，σ>0。对scalar graded Taylor maps，令V_D是非零rank-one increments的indices，其数为r(D+1)，且indices不同。相对于未抑制jump的界，G7的每项节省为
\[
 an-(an-\sigma D)^+=\min(an,\sigma D).
\]
这是完全显式的正量。至少约rD/2个indices有n≥rD/2，故
\[
 \sum_{n\in V_D}\min(an,\sigma D)
 \ge \frac r2\,\min\!\left(\frac{ar}{2},\sigma\right)D^2+O(D).
 \tag{G8}
\]
对每个degree位置multiplicity至多k的vector graded target，将ar/2换为ar/(2k)，同一计数给同阶结果。

因此真正的D²收益需要对**O(D)个评价位置**取得e^{-σD}的uniform full-jump改善。G8不是新无理性定理：source高度若因constructing these vectors多付O(D) per graded position，也会抵消这项收益，必须全place记账。CDT quantitative proof正是对这种误差与height成本共同优化。

若仅有fixed σD替换成O(logD)，则每项最多O(logD)，总节省只有O(DlogD)。如果a=0，此处没有jump距离的D² penalty可削减。不能通过符号重命名制造收益。

## G6. fixed log metric为何不产生该σ

为本项目的**固定秩linear packet**作精确局部比较。保持相同semisimple power factors，只改变固定log weights，例如两个packet-factor norms在距boundary b至少r_D的区域满足
\[
 (1+|\log r_D|)^{-A}\|\cdot\|_1
 \le\|\cdot\|_2
 \le(1+|\log r_D|)^A\|\cdot\|_1,
 \quad |\log r_D|\le D^B,
 \tag{G9}
\]
A,B固定。rank E_D=O(D)，line O(D)自身的Bost–Charles metric保持不变，改动只在固定packet factor。

G9每个singular value的log变化O(logD)，故source determinant degree变化O(DlogD)。固定packet target的graded height每rank-unit也只变O(logD)，其total rank为O(D)，所以全部graded费用变化同样O(DlogD)。这是上下双向bound，不是只列一条可能的upper bound。

所以从log³降低到log²，本身只给logarithmic weight的变化，不给G6的e^{-σD}。若构造不同tensor/polynomial packet，packet rank、nilpotent order和auxiliary dimension可能随D改变；G9结论不能自动搬过去，必须重新证明rank、metrics与全部place heights。也不能将r_D取成e^{-e^{cD}}再省略由此发生的evaluation及domain费用。

## G7. module-functorial斜率与marked solution资料的区别

actual W9作为differential module并不随参数q变化；q选择同一module的一个marked solution Φ_h+qΦ_0。因此任何只依赖该module的functorial invariant——regular/irregular slopes、local semisimple exponents、以同一Deligne lattice和同一exponent convention定义的parabolic weights——都对q相同。

在regular-singular local frame
\[
 H(z)z^S\exp(N\log z),\quad [S,N]=0,
\]
det exp(Nlogz)=1；nilpotent chain长度改变log polynomial，不能仅凭这个变化更改S的power exponent。所有regular differential modules的Turrittin-Levelt irregular slopes为零；André PDF6–7对此定义清楚。

G1是关于marked solution的nilpotent旗标，可能被未来一种针对marked section的height theorem利用；它不是新的module slope。若想从更强的 cancellation取得额外power vanishing，需证明整个相应semisimple block消失或另一个实际divisibility条件，不能从N³p+Φ=0自行推出。这一段不排除未构造的新parabolic/section theorem，但明确它所需的输入不同于已有functorial module资料。

## G8. rank-one endpoint row的算术下降：必要且充分的线性代数条件

设K嵌入C，W_K为已固定Taylor/Levelt coefficient空间，W_B,Q是实际Betti空间，C:W_K⊗C→W_B,Q⊗C是实际comparison。最高flag是一个rank-one operator，其kernel由非零Betti covectorℓ_B定义；在Taylor coordinates的covector为
\[
 a=\ell_B C.
 \tag{G10}
\]

**下降lemma。** complex hyperplane ker a是某个K-hyperplane的base change，当且仅当
\[
 [a]\in\mathbf P(W_K^\vee)(K),
 \tag{G11}
\]
即选任意a_j≠0后所有a_i/a_j属于K。

证明：若ker a由K定义，其annihilator是K-line，取非零b∈W_K^∨，則a=c b。反向显然；或直接以a_j归一得K-row。lemma只需projective comparison row，不需要整个comparison matrix都代数。因此它把缺口缩到实际需要的local period ratios，未过强地索取完整period conjecture。

若b∈W_K^∨已得到，可清一个fixed denominator并计算其全部place operator heights；于是这个fixed row至少成为合法arithmetic morphism。它的系数是period ratio这一事实必须先证明。fixed K-row本身的height仍不能自动给G6的degree-dependent抑制；完整新packet和endpoint formal Taylor bounds仍需核。

Betti ℓ_B整数并不推出G11。纯线性代数反例是C=diag(π,1)、ℓ_B=(1,1)，Taylor row=(π,1)，其kernel在Qbar上无定义。本例只是反驳逻辑蕴涵，不声称这是当前R0的comparison。允许按actual period常数换Taylor basis，会失去原来已证明的arithmetic prefix；这一费用不能省略。

## G9. 假设α0代数仍只确定一项ratio

Φ_h、Φ_0是在canonical Taylor/Levelt coefficient结构中定义的两个独立vectors。G1等价于
\[
 a(\Phi_h)+q\,a(\Phi_0)=0,\qquad a(\Phi_0)\ne0.
\]
假设q=α0∈K只给这两个vectors上的ratio
\[
 -a(\Phi_h)/a(\Phi_0)=\alpha_0.
 \tag{G12}
\]
它并不使a在完整九维空间上的projective coordinates全在K。一个complex hyperplane包含某个K-rational vector，也不等于该hyperplane由K定义。

所以要将整个highest-flag kernel作为Bost/K-linear evaluation target或arithmetically filteredsource使用，G11是精确需要补的下降条件。另一条可能路线是不要求完整flag下降，而只构造一个新的K-defined辅助空间，它的全部jump evaluations由已知的G12控制；此时必须实际证明其injectivity/rank与G6，而非只看到原参数族中一个ratio代数。

本稿未断言G11在R0中不成立，未证明这些period ratios超越。当前只是没有该proof，且整数Betti模型与α0∈K假设均不补它。来源中的arithmetic slope theorem明确要求相应K-defined对象，故这是实际条件，而非额外审批或保守假设。

## G10. 完整新theorem所需的可核接口

一个真正对目标敏感的jump-holonomy突破，至少需同时给：

1. K-defined marked-section/auxiliary germ、实际rank与全place前缀；若用endpoint-row projection，证明G11或上述更窄的K-auxiliary构造。
2. actual q的auxiliary unit ball上完整jump抑制G6，σ>0，cuts和outer operator bounds统一，全部lower logarithmic jumps亦支付。
3. G8的收益比新增finite-place、source height与scale费用更大，并对所有embeddings成立。
4. 证明q=0 reference不能同时享有同样marked-section/jump条件；否则只是重用共同packet的已有不等式。

当前G1只有最高nilpotent旗标取消，既不填origin，也没有G6；quarter的全路径模8证明进一步说明换word不会把完整primitive jump变零。将其取消残余jump的计算问题改写为“找更长word”已无效。

我们新证明的G3–G8仍有作用：它告诉下一轮应计算的是uniform full-jump operator，而不是单个period图上的一项log coefficient；真正的positive-part和D²预算都已写出，不再笼统说“也许使用更深的数学”。

## G11. 本轮进展与边界

新增已证是cut-current/Cauchy全尺度评价界G4–G7、真实D²收益的uniform条件G8、fixed packet logarithmic metric的低阶费用G9，以及rank-one endpoint flag算术下降的精确lemmaG11。实际全文独审还确认所有transported-origin word的mod8障碍和当前packet共同域结论。

尚未证明R0满足G6或G11，尚未构造新的vector-valued arithmetic-holonomy定理，也没有新特殊值无理性、超越性或线性无关性结论。当前α0目标仍为π²(R0−M0)/16，其代数性不等价于R0−M0的无理性。

本轮只新增两份正常TLS一手PDF，55+95=150归档页；actual reading范围已逐页列明，未全文读150页。没有旧/同行数学producer执行；本稿新数学producer数也为0。来源receipt另存NEW，最后全文回读与独审后冻结；root主报告/audit未改动。

冻结前修订记录：初候选0d4ec96的G3只列rectifiable cuts与外圈L¹条件。root与quarter独审分别指出smooth exhaustion和cut-bank边界收敛需明确；本版改为有限piecewise-C¹ arcs/有限节点，并要求人工cut内部bank解析延拓（或明确thin-cut L¹收敛），G4证明按先细管后endpoint circles取极限。没有把仅存在可积trace当作足够条件。实际PF人工cuts满足这项几何/解析假设；本稿未冻结旧版。

