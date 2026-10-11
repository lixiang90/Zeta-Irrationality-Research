# 第259轮唯一总审：完整混合坏芽、实际降场与条件性秩入口

2026-10-10。审阅者 `source259_log_products`，独立于mixed、field和Root gate/report作者。本人是log稿作者，**不将其作者自核计为独审**；log数学的独审证据是Root对最终L1–L6的实际FULL复核，记在冻结root scope。

结论：**本轮有限数学链与来源选择结算PASS；实现准入、严格全图holonomy和新数值定理均未通过。** 总目标active。通过的是固定混合来源的完整关系收益、最低forcing场、单关系实际rank3及全N原始type入口，不是1、ζ(2)、L(2,χ−3)、G的数值线性无关性。

## R1. 实际最终读件与冻结身份

审阅者实际FULL读下表中mixed最终8730版、field最终F1–F11、gate G1–G5、report四节及全部四scope；此前mixed7968版另有完整独审，最终版重新整件读取，不借旧读件替代最终身份。log稿由本人撰写、Root独审，表中身份另实际重核。本review以当前冻结稿为准。

|文件|bytes|SHA256|核验角色|
|---|---:|---|---|
|research/source_selection_mixed12_round259_20261010.md|8730|a806789488ee4987df679c199eacdd2c9257254ac2cc5964b887e4a6af8c46a7|本review独审M1–M15与新增M5接口|
|research/source_selection_mixed_field_round259_20261010.md|17525|fad9d69a943026d1b6941e9af71b8786cc6643d31007a11ebce0f12df98e0517|本review独审F1–F11|
|research/source_selection_log_products_round259_20261010.md|9137|c12d4e25b661f42b76165a2de4af2b2e442a32dd63fff61485b1f279d1bcb206|Root独审；本人不自审数学|
|research/source_selection_gate_round259_20261010.md|6595|7f6e75fe89123c9a4ca1a9a5f9bc8c5f0bc23097144a778401f80e63aa562503|本review独审G1–G5|
|research/research_source_selection_progress_round259_20261010.md|4937|e80c468c14dc13c0f1955d08b5cbf45586281c0e48ac1c011c9e25c6b7a80b07|本review独审结算与clock|
|literature/source_selection_round259_20261010/root_reading_scope.md|6562|cd9921d660ddb467dccd4fc60b4ce0105228ca6452ed465491590ac47a9240ce|FULL读，区分Root独核与作者自读|
|literature/source_selection_round259_20261010/mixed_reading_scope.md|6066|9fbd6a3625190b48c7fc7744bc24f2e011e1f2c64f2500e779482bf569c0660b|FULL读，核对应最终数学身份|
|literature/source_selection_round259_20261010/field_reading_scope.md|6647|3ffda140355086a345f10f3cb69b2858245b63ebb5c93c1ba863168fc9ea4771|FULL读，核输入与未付条件边界|
|literature/source_selection_round259_20261010/log_reading_scope.md|5879|688a801f0c9a6f71d7f0f951b5445141a384d07770d4a1425fdfadc025ebe364|FULL文档核，作者scope不是独审数学|

散列只证明读件身份，以下纸面核算才是数学审核。未把任何scope中的作者primary FULL标签继承为审阅者FULL。

## R2. mixed完整坏芽与精确四叶障碍：PASS

逐项重推M1–M15。δ²B₄的divisor-sum方向是E_{3,χ−4,1}，不是反向角色；固定dyadic scale给level8，和CDT level6的自然共同层级为24。Mellin kernel Γ(s)ζ(s)β(s+2)在1、0、−1的三残数是π³/(32u)、−G/2、πu/48。ζ与primitive β的函数方程连同duplication/reflection确实给M5的−(π/4)π^(2s)系数；z=−s−1后的cosh kernel给完整dual D项。余项是恒等式而非丢掉指数小项的渐近。

K(u)−2K(2u)消去1/u，保留−πu/16与两个dual series。u=−2πiτ、q₀=exp(−πi/(12τ))分别把其指数变成q₀³和q₀⁶，故M8所有常数与符号正确。二维Poisson对A₂ Gram determinant3给Θ(−1/(3τ))=−i√3τΘ(τ)，进而A₃=iT/(2√3τ)=−(2√3/π)T log q₀，T(0)=3/2。

因此H₄−(G/2)A₃的完整M11右端确实是收敛Taylor芽；A₃的log坏芽非零。与CDT两个已付完整差组合得到[M13]=R[A₃]，对全部固定复系数成立，R=0当且仅当此canonical cusp的整个非亚纯类消失。字面常函数1不具备该单位周期作用。

旧x₆底的width比24/6给x₆−1/9阶4。M11的q₀³系数√3/2非零，而CDT两个residual仅有q₀⁴倍幂。故含d≠0的完整关系仍有exact inertia4：少于四次旧底循环不能恢复。审核没有把cover上全纯改写为旧底亚纯，也没有断言其它所有到达叶都已消支。

A₃系数整性可由A₂非零格点六元旋转轨道支付。B₃、B₄和C₃逐项分母均由n≤N的n²控制；C₃的1/(4m²)写成1/(2m)²，index条件保证2m≤N。因此完整d_N²安全清整包含全部素数幂。旧x₆整数逆换元保该前缀，但不自动完成新的curve推前数组。

## R3. field群、实际最低场与显式forcing：PASS

F2 eta规范与Sturm纸证一致。A的两个Newman和为0，weight1、χ−3及cusp orders(0,1,0,0)正确；constant/q项1、3和bound1足够。f₄的两个和24、24，weight3、χ−4，四cusp orders(1,0,1,1)正确；固定0、1、−4、8与bound3足够。h=f₄/A³的eta式weight0、characterχ12、q-leading1。三个固定系数的已发表Sturm准则是纸面全函数证明，未被当成有限头实验。

F3自然场证书是合法模型：j(24τ)在Γ₀(6)中的generic stabilizer恰Γ₀(24)，故四阶base extension；χ12在矩阵(5,1;24,5)上为−1，h给真正二阶character extension，总degree8。完整cusp表均使character为+1，unramified doublecover的genus仍1。八条integer背景确实独立，但这不证明它们是本forcing不可避免的收费模型。

F4的链式法则给h=−√3 δ_w²C₄/(24T³)，leading(2√3/9)q₀³。D的偶index系数是半index的1/4，所以−2D(r)+D(r²)/2全部偶次项消失；δ_w²删除constant，而T只含q₀⁴幂。这支付完整h(−q₀)=−h(q₀)。γ12把w送w−1/2，故其对h的作用为−1。结合Γ₀(24) coset与实际character，得到的群是

\[
 \Gamma_\psi=\ker\{\chi_{12}(d)(-1)^{c/12}\}\subset\Gamma_0(12).
\]

ψ的乘法性与ψ(−I)=1都直接由矩阵乘法核清。半平移P的共轭矩阵整数，χ12(d−6k)=χ12(d)(−1)^k，因此Γψ=P⁻¹Γ12P。**P是共轭换坐标，不是h的不变deck；不能以κ quotient或h(−q)=h(q)替代此证明。** h(q)leading q已排除后一个不变式。

F5复用的是旧已付Γ12 genus0参数及其完整character曲线，不复用旧weight4 L3数值、rank或预算。其方程u+u²=x12−2x12u−2x12u²逐阶的未知系数系数1，给所有阶整数；s=−u(−q)及其formal inverse同样整数。这不是只看leading几项。ψ cusp characters(−,+,−,+,+,+)给两个branch cusps和genus0，与明确共轭一致。

F6、F7的divisor证明和常数规范正确。置r=1−2s，直接消元验证

\[
 t=\frac{1-r^4}{9-r^4},\qquad
 h=\frac{2(1-r^2)r^3}{(3-r^2)^3},\qquad
 \frac hp=\frac{(3+r^2)^3}{32r(1+r^2)}.
\]

t的两degree4 branch fibers是r=0与∞；全部zeros/poles无公因子。h完整zeros/poles数各6：s=0、1各1，1/2阶3、∞阶1，两实pole各3。它与eta/Ligozat八cusp orders(3,−6,1,0,0,0,1,1)下降一致。q-leading1定唯一常数，不是有限拟合。

局部h的3/4指数迫Q(t,h)/Q(t)的ramification至少4；该field包含于degree4的Q(s)/Q(t)，遂恰为Q(s)。这给实际最低forcing场，并不将原自然E曲线改称genus0。F3的degree8与F6的degree4是不同完整对象，均保留其范围。

## R4. ordinary holonomicity与单关系实际rank3：PASS

CDT D_t同次解A、τA的Wronskian及∞归一化给δ_qt=pA²；直接链式核D_t(AB_j)=δ_q²B_j/(pA³)。三forcing是1、1/(1−t)、h/p，全在Q(s)。t(s)完整拉回确实给Q(s)上的order2 scalar operator；没有把q-modularity直接当q-D-finiteness。Root G3的monic conjugate写法与这条显式拉回一致。

χ−3 twist的二维homogeneous monodromy在Γψ上不可约：T与下幺幂(1,0;24,1)均在kerχ−3∩Γψ，两个单参数Zariski子群生成SL₂。有限cover保此不可约性。未经假设的九germs只是有限生成上界，**未付这九germs的实际独立rank或其扩充type**。

对单一假设关系H，CDT已知三项独立迫d≠0；h∉Q(t)使forcing非零。若H∈C(s)，则f=H/A是meromorphic weight−1、χ−3的form。内部pole经二阶导数增加两阶；cusp负Fourier项经Bol身份乘非零指数平方，均不能与holomorphic forcing相容。所有cusps的holomorphic性可在共同有限cover上核，再下降；character处需用实际width或kerχ−3，不能漏半整数指数。

实际f₄的Γψ character是χ₃，不是直接χ₄=χ₃：它等于χ₄(d)(−1)^(c/12)，h不变和A³变换给完整等式。稿中(5,2;12,5)反例正确，raw χ₄与χ₃在那里不等。全纯负权form由y^(−1/2)|f|的最大值/严格subharmonic论证只能为0，与forcing非零矛盾。因此H非有理。

V中有1（由非零rational forcing），V/K·1的非零cyclic quotient被不可约order2算子消去，故quotient rank2，加上1得实际rank3。{1,H,θ_sH}确实独立。此rank已付，不能仍把它列为未付首关；也不需要额外附加product-formula才需要的某个Δ_n无界非零条件。holonomy入口的非零证据就是实际forcing和rank；乘积公式另按自身对象支付其非零义务。

## R5. 全prefix、type与必要导数门槛：PASS但仅条件性入口

整数q(s)合成只使用degree≤N的输入，固定C₀清关系系数后d_N²清H全部prefix。θ_s只乘Taylor index，故同一个multiplier清θ_sH。常数行1不新增费用。两列(0,1,1)的m3原始safe type及e0全部来源于本对象，不借旧χ7或CDT14。

审阅者实际FULL读保存的固定CDT v2 physical89–90和122–124选段：

|选段|bytes|SHA256|
|---|---:|---|
|field_cdt_holonomic_physical089_090.txt|5908|8083235335c31b62694b5483d0cc54bcbd4d1936bdebd07018752d0b19a307c2|
|field_cdt_types_physical122_124.txt|9277|b37afdb257f65a8978a2f8b7e6c083ed7b785a3afa6bb2c6ed0ab6c80a3b4557|

Remark8.0.6对嵌套column的τ确为每列1−1/9，两列共16/9；e0附加费用0。Theorem7.0.1允许对已知holonomic族将size条件减为λ>τ，但仍要求同一φ上全部芽为亚纯并满足standing/boundary条件。未精化(7.0.3)的矛盾要求3(λ−16/9)>J。对合法holomorphic φ两次Jensen给J≥λ，故此固定safe入口的必要条件λ>8/3。

**16/9不是已证最优实际算术费用；λ>8/3不是所有holonomy方法的必要条件。** 更精细metric、convexity修正、新type或aux族会改变账本；F10已明确此限定。未构造任何共同图，未付返回支路、全部cusps/fibers、θ_sH poles、极点clear与边界半径条件，也没有certify strict。单一canonical cusp填点和genus0不足以领取原CDT图或能量。

## R6. Root gate、report、log独审证据与复盘结算：PASS

G1–G3和report准确区分自然level24、最低forcing场Q(s)、九germ生成upper与单关系实际rank3。G4/G5只允许进入下一正式全局比较，不准入本轮Padé/map/参数优化；不会由局部引理或降场重开无界搜索。对bare holonomy下一缺口为合法全局graph与strict budget；其actual非零已经由R4支付。与product-formula资产比较时仍须核各自实际det非零，不混用。

log稿数学不由本作者自审。冻结root scope明确记录Root实际FULL读最终9137版并独核L1–L6：完整坏芽、prefix、纠错、depth-two拆和及有限tensor条件；原文17rank/16.2图只作为已发表接口，未向新族借用。本review核该独审记录、最终身份和两log拒绝决定的限定：原近参数Theorem C已覆盖，拆和不孤立新个别值，没有将Baker单log或有限检索0结果算成新数值目标；没有全部Hadamard方法no-go。

独立解析258 manifest元数据：实际40150 bytes / 9d4cc7d8abc31bbbfefb2f04b1696789765bcd135567531f1368bdfa86ea2aca，file list长度160，上一轮classification progress、新数值false。正式clock为last256、258后count2、next260、latest264。259不是正式复盘，完成后count3、不reset；默认4轮、最多8轮、连续核心停滞2轮提前。Root gate/report的下一步符合这个时钟和停止规则。

本审未重新逐个核258全部160 file pins或旧main/policy前缀；该连续性由Root本轮开始核验与后续单次归档/postcheck另付。report中保留159非policy旧输入和旧bytes prefix是归档义务，**本review不把尚未执行的新归档宣称PASS**。没有以数学审核替代文件保全。

## R7. 本review实际范围与执行

本次审阅新增FULL为最终mixed、field、gate、report、四scope及R5两份primary选段。258 manifest只解析指定元数据/clock/file数量，不声称旧corpus全文数学认证。F5采用已付旧Γ12参数作为输入，本审核本轮共轭、代入、整数递推和divisor链；不重新认证旧weight4全文或旧数值预算。旧源218 reciprocity复用不计本轮新定理；review独立核其用于M4–M11的函数方程、残数、参数与完整analytic链。

本作者先前log任务的实际primary页段及网络动作见log scope；新的总审阶段没有web动作，也没有将其他作者primary FULL继承为本人。团队scope准确区分下载、选段、失败403、局部原文及整本PDF：一个Allen原件下载不是整篇认证。没有fresh cloud equality、全仓库或Lean认证、全球新颖性声明。

本review阶段数学程序、CAS、数值/interval、参数/prime/map/word扫描、Padé、Lean、旧producer、外Git写、归档均0；Python只文档读/hash与JSON元数据解析。仅写此唯一新review，未修改冻结数学、scopes、main、policy或manifest。全队数学程序0的报告与四scope相符；不得把文献下载或准备archive算成数学运行。

最终判定：有限来源数学进展PASS，条件性bare入口PASS；全图strict、实现准入、新数值结果未取得。保持原数值目标和active goal，不mark complete/blocked、不reset clock。第260轮的首决策是实际全域允许收益与已付算术入口是否相容；严格相容证书没有交付时，不能仅凭本轮降场延长局部优化。
