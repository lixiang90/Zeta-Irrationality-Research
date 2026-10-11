# 第261轮 arithmetic：读取范围、原件 pins 与准入边界

2026-10-10；仅审固定259 mixed ordinary s-Taylor、bare rank3对象的精化费用。只写本轮指定数学稿、本scope和固定primary节选；不改259/260/main/policy/manifest，不归档。本文只登记本子任务实际读取，不继承Root或其它agent的FULL。FULL文本读取不代表逐页视觉检查。

## 1. 本轮实际FULL读取的既有边界

|文稿|bytes|SHA256|
|---|---:|---|
|research/global_review_mixed_arithmetic_round260_20261010.md|12736|880c8ef349207fa110af8ee568a7d6a702e3e9f7db660bd2eca5bcd8a2d3bc08|
|research/global_review_mixed_analytic_round260_20261010.md|5716|0a5058ab7181b0a9ea0bc84f53866e0de6c492e7f6fd74bad85213930fe2906d|
|research/global_review_architecture_round260_20261010.md|13020|d16d012f3f0c6b4a7232c6791e18ff4fdd01b684e1e0cfa7f9949a07ff0bda25|
|research/source_selection_mixed_field_round259_20261010.md|17525|fad9d69a943026d1b6941e9af71b8786cc6643d31007a11ebce0f12df98e0517|

这些固定稿本轮实际全文读取；第一次并行工具输出的architecture被截断，随后单独完整重读，不将截断结果当FULL。另实际全文读260 arithmetic scope 6429 B / 800c13000057b9b471b8092d4060b5edf41b7222a55a0de3fb590aa038a08149，以定位固定原件。259 field旧scope本轮未重读，不登记其为261 FULL。260 manifest不在本子任务本轮重审范围；先前260独立postcheck PASS不是261新的全资产读取。

实际对象与归一化固定：H=A(a+bB3+cC3+dB4)，d≠0；C0清有理系数后J=C0H。普通s-Taylor整数unit/逆坐标、Q(t,h)=Q(s)、bare rank3及period rank2不可约性来自259 field的最终证书。未更换primitive或加入pure族。

## 2. CDT固定原件与实际定页文本

原件 literature/cdt2024_l2_chi_minus3.pdf，arXiv:2408.15403v2，218物理页，4517169 B / 84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771。本輪原件整体为**PARTIAL**；使用已有PDF，不GET、不改原件、不声称218页全文或视觉检查。下列节选由固定原件文本提取，并实际全文读到其末尾：

|本轮FULL节选（均在本scope同目录）|物理页与使用|bytes|SHA256|
|---|---|---:|---|
|arithmetic_cdt_v2_physical066_067.txt|66–67：6.0.2的e∈N、τflat/τsharp、literal denominator；67页固定shift remark的已显示部分|5356|daabd55a329be3a7c04162a93f73f4b36d14d60c5452bbd8b0bc8a21876388c4|
|arithmetic_cdt_v2_physical119_124.txt|119–124：前节定位背景及8.0.1、Definition8.0.2 Den_N、nested baseline公式|16648|eb572629764e165d8b22309b3f3a53571a390ce8528ffbfd571446650a53af2f|
|arithmetic_cdt_v2_physical159_163.txt|159–163：B3/C3 Eisenstein两取向、A首项、普通q/t逆坐标与ODE|12835|6c69fff673278c13dcf31e8773d9eed444655f91f2a3073160c4bdf80eb6e9d5|

定位6.0.2时还实际读到物理69页的工具文本；不引用它产生新定理，未保存为本轮primary资产。定位过程中对物理45–69作有界文档文本索引并只输出匹配页；未逐页全文读全部区间，不能标成45–69 FULL。物理68不在本次FULL范围，不借Remark6.0.12后续证明完成来获得免费shift成本：本轮row obstruction直接对原g的任意固定c_h成立，渐近τ下界使用literal array的b条目。

物理页=PDF索引+1。已读66–67证明e为非负整数，τsharp各项非负；未任意借n^e、未把g先乘polynomial后免费继承原类型。已读Definition8真实sum(j,h) threshold count，R7逐row比较再取balanced max/limits，不要求不同row的大entry在同列。

## 3. PNT_AP唯一新primary：选定定理，原件PARTIAL

Kiran Kedlaya，MIT 18.785 (2007) 作者讲义，https://kskedlaya.org/18.785/dirichlet.pdf。web实际打开6页、365行PDF文本；实际使用/核对物理1页Theorem1和物理5页Theorem5及weighted theta论证，采用固定模12的ϑ(x;12,r)~x/4。不声称本轮从零重证全部Tauberian/analytic continuation证明，也不采用uniform-modulus或effective error。整体原件**PARTIAL**；所选定理陈述读取充分，保存自己的中文公式卡片而非复制整篇：

* arithmetic_kedlaya_pnt_ap_selected.md：1182 B / 476040cdf9946135ec5e441bdac1ef8b84c8a039084086d20a33e716ad328fb7；卡片本轮实际全文读核。

本子任务有一次bounded web search（两条定位query）、一次web open；未选择其它新来源。另urllib对同一作者PDF一次GET返回HTTP406，没有PDF本地文件或下载字节。这个失败是站点HTTP响应，不是自动审批拒绝；可用web原件读取，因此不阻塞所选PNT_AP引用。无后续GET重试或扩大来源搜索。全稿自己的divisor/character分类与素数幂证明为纸证，不由网页数值表或prime程序产生。

## 4. 新数学稿与已付/未付界面

research/refined_budget_arithmetic_round261_20261010.md：13152 B / b51f5bc38e0f9667b28d79ea5ce49d6a85b310f7aaecbb78e4cd31540831bbe5；最终R1–R8本子任务全文读核。R4已明确N≥1，M0=1，覆盖常数prefix；不以“每个N”留下log_p0未定义。

已付新纸证：

* 全部普通prefix最小分母在integer unit与integer互逆composition下完全不变；p^e两Eisenstein取向与chi3/chi4 parity明确。
* fixed actual coefficient每个residueclass的首非零k为1、2或3；M_N清所有N、所有prime powers。两行J与θsJ都有固定偏移的精确p² witness，未给theta免费减一列。
* 结合固定PNT_AP，真实最小prefix分母leading按四类F_r为2、7/4、3/2、4/3。generic F_r四类都非零时仍为2；特殊关系类节省不覆盖整个四项反证空间。
* 对任何固定Q(s) Laurent换基的nonconstant ordinary row，某固定k≥1与无穷大素数给v_p g_{p+k}=−2；n^e为p-unit。每个实际literal LCM row至少两个b_h≥1。经Definition8 rowwise balanced计数，当前rank3的任意有效标准literal类型仍τ≥16/9。
* 本子任务另独核裸关系实两点forcing±9√3/16与所有到达支路的u log²u，沿260 primary规范得到同holomorphic图λ<log(11/2)<7/4。结合τ≥16/9，标准literal入口无positive denominator。

未付：素数类过滤M_N的matched high-dimensional evaluation/holonomy theorem、其balanced determinant费用、全部generic与exceptional rational关系共同strict净预算、合法joint图。真实prefix leading不是CDT τ，不是已获δ；R6一条prime-head障碍先转成实际literal row要求，再由原Definition8付τ下界，未将prime头本身冒称全leading。

停止范围仅固定bare rank3、普通s-Taylor、原§6–8标准literal费用与holomorphic-map refined入口；不声称全部算术holonomy、不同meromorphic-map theorem、其它来源或目标四项LI不可能。本轮不准入prime-filtered模型实现，不另开primitive或source窗口。

## 5. 运行与冻结边界

数学程序=0；CAS=0；finite_n/prime/参数/map扫描=0；Padé/matrix=0；Lean=0；数学数值积分/优化=0；旧producer=0；archive=0。本子任务没有运行Root archive或改已有manifest/main/policy。仅文档PDF/text读取提取、指定文件写入、rg文件定位、hash/bytes与纸面推理。

数学稿自读不是独立review；Root另实际全文核R2–R8并反馈PASS，本scope不继承其阅读。最终冻结由Root在实际读取最终版后决定。scope自hash由外部receipt记录，避免自引用。
