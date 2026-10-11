## 222. 提前全局复盘：停止模板升权，检验真正关系诱导的生成函数源

2026-10-08。上一轮是实质进展，已证明的全图上界触发本轮提前复盘。**尚无新的ζ/L数值无理性或线性无关性定理，原目标继续active。** 本轮新增两项全族结构引理、一项真实联合整格和一个具体纯ζ7生成函数包，并证明其首个目标行列式Δ₀精确非零；它们改变下一步选择，但不替代最终数值结论。

### 222.1 当前仓库与已有成果的实际作用

已只读核对用户指定 `E:/codex-build/math`：main工作区干净，HEAD为`adc7f1241b42e322a6451854ab7e4b4c146bf78a`，与本轮GitHub main API一致，无需再次checkout。Root亲自核status/HEAD并完整读保存的API响应；未做Git mutation。[公开固定提交](https://github.com/openai/math/commit/adc7f1241b42e322a6451854ab7e4b4c146bf78a)。

实际原文架构阅读没有发现已经可以直接迁移、付清费用并解决指定ζ7的结果。Deligne–Drinfeld的奇权holonomy非零不是各个奇ζ数值独立；其原文明确不要求数值算术独立。Catalan主稿提供完整局部格、反证关系点沿无界尺度非零、同一混合外积的strict比较，值得学习，但已是项目此前输入，不因重读变成新载体。本轮没有完整复核其energy/certificate或执行Lean，目录和verification说明也不能替代它们。

Fauzan ζ5正Hermite泛函、pole-class和polynomial correction与旧ζ7研究对照后，确认μ7及p⁻6分布、正Gram与联合content已存在；本轮未改善原ζ7的算术、能量或无限非零缺口。故不把“重新写出μ7正核”升级为主线。历史报告将ζ5归于Apéry是误述：Apéry证明ζ3，当前ζ5来源另有原预印本和形式化仓库；本轮未验证其全部proof/Lean。[原始ζ5 v1](https://zenodo.org/records/22826419)、[形式化发布范围](https://github.com/danromik/zeta5-irrationality)。旧有限扫描失败也不升为所有参数no-go。

精确原件与读域见[来源记录](../literature/global_review_sources_round222_20261008/source_reading_record.md)及[架构复盘](openai_source_architecture_global_round222_20261008.md)。这是有界的实际来源核对，不是全球最新ζ7/β4文献的穷尽排查。

### 222.2 两个全族引理：哪些“统一推广”没有提供新输入

对β(s)的elementary奇悬挂，实际完整源(1,f₁,…,f_s,o_s)的秩为s+2，全幂分母有一般lemma

\[
Mk^s\mid q_M^s q_{\lfloor M/3\rfloor}
\quad(M,k\text{正奇数},\ k<M).
\]

由它得到已付staircase费用

\[
\tau_s=\frac{4s^3+21s^2+27s+6}{3(s+2)^2}\ge\frac{11}{3}
\quad(s\ge2).
\]

另一方面，微分链从实际高权f_s或o_s恢复f₂、f₁，因此所有允许共同图仍有log|ψ′(0)|<7/2。费用随权增、解析限制保留，**这张已付完整表对所有s≥2均失败**。它不是最优联合格下界，不排除新源，也不声称所有高权β方法失败。完整证明与独审见[全权重稿](elementary_beta_weight_family_global_round222_20261008.md)、[独审](research_round222_beta_weight_family_review_20261008.md)。

对朴素ζ悬挂T_g=∫(Li_s−g)/(1−x)，有精确身份T_g=T₀−gLi₁。保留完整背景(1,Li₁,…,Li_s)后，源空间、共同亚纯图和秩s+2与g无关；固定有理shear只带来O(D)格指数损失。目标条件ζ(s)=g没有新增完整输入，Li₁的log分支仍禁止经过1。见[源不变性引理](zeta_residue_suspension_rigidity_global_round222_20261008.md)及[独审](research_round222_zeta_suspension_rigidity_review_20261008.md)。这解释了为什么只减去一个数值，不能复制β ordinary-point的补点桥。

### 222.3 联合整模型：真实收益与不能迁移的短矩形

在实际五行(1,a,b,2c_ge,c_go)源上，p>N/2的最高p³层恰为两个移位窗口的联合kernel。真实p-unit剪切降低重叠方向一层；CRT交加全部其余素数/高幂fallback给真正安全整子格，不是逐行分母猜测。

但完整五行若连续jet可单射，必要N≥5D+4，使该窗口重叠为0。三行子源(1,e,o)在N=3D+O(1)确有(1/16+o(1))D²指数节省；它的微分闭包仍秩五，该矩形的单射/无限非零、全层费用和实处基高度尚未付。不能把1/16直接从CDT τ减去。

当前三行array前两列费用下界32/9仍超过7/2；普通J严格商小于3甚至要求有效τ<7/3，而非仅τ<7/2。故这一有限top-layer收益保留为算术资产，不继续只优化该层。见[联合格稿](cyclotomic_joint_integral_global_round222_20261008.md)、[Root独审](research_round222_joint_integral_review_20261008.md)。

### 222.4 唯一进入下一窗口的具体候选：三周期Padé系数包

不同的变量编码近似尺度n，而非旧atan/Ti₂的解析变量。取偶n，

\[
R_n(t)=\frac{[(t-n)_n(t+n+1)_n]^3}{(t)_{n+1}^6},\qquad
I_n=\sum_{t\ge1}(-1)^tR_n'(t).
\]

已付实际精确身份I_n=A₃,nζ3+A₅,nζ5+A₇,nζ7+C_n。连续三行外积严格消ζ3、ζ5，给J_r=Δ_rζ7+Ξ_r；假设ζ7=g∈Q时，H_g(z)=Σ(gΔ_r+Ξ_r)z^r是由实际收敛和产生的Q芽。最高pole binomial整性、所有低层与有限tails给完整分母；n=2r后的安全前缀指数Δ为24、Ξ/H为48，固定2及g分母均付。

这是新增具体接口，仍**不是可用CDT完整源已成立**。其后对n=0,2,4精确展开部分分式，得到

\[
\Delta_0=\frac{11581683398946533579805}{32768}>0.
\]

这说明目标系数级数非恒零；n=0本来含纯ζ7项，故它尤其不证明大n稳定或无限多个非零项。见[有限补充引理](pade_target_head_nonzero_round222_20261008.md)、[精确证书](pade_target_head_certificate_round222_20261008.json)及[独审](research_round222_pade_target_head_review_20261008.md)。原包与其独审的“尚无Δ非零”是生成此补充前的阶段记录，由本引理更新。

粗界仍只给背景半径≥2⁻⁹⁰、关系芽≥2⁻⁶⁰；两个下界不能证明实际严格过收敛。无限非零、n-recurrence、cyclic秩、G-function和主奇点仍未付。保留(1,Δ,Ξ)背景时H_g只是shear，不能免费增加解析方向。现有安全费用也未显示净优势。见[具体关系包](relation_source_architecture_global_round222_20261008.md)、[Root独审](research_round222_relation_packet_review_20261008.md)。

Fischler的目标选择性系数空间条件提供另一个核验口：未投影Padé矩阵的rank不能免费移给实际目标投影；消v个nuisance的余子式乘子会增加β^v高度。αβ^v<1只是某不缩放整数线性形式绝对趋零的充分条件，不是CDT必要门槛；相对radius下界也不是已付新domain。本轮没有利用渐近维数结果宣称指定ζ7或β4结论。

### 222.5 下一步、退出条件与复盘节奏

下一窗口只保留一项主要证明任务：**认证上述固定三周期包是否能成为真正关系诱导的cyclic源。** 第223轮先证明其n方向的holonomic/递推结构，并处理目标系数Δ的非退化；随后必须支付无限非零、generic不可去主奇点和关系造成的严格解析增益。只有得到同源的可证明净优势，才细化整格/共同图/能量。

联合整模型和Fischler目标选择性只保留为围绕这项缺口的结构工具；不扩原Hankel种子，不重启elementary图/prime参数调整，不把一般motivic生成元自由当数值周期单射。若该候选仍只产生安全上界或形式rank，而两个完成轮次未支付一个核心接口，立即降级复盘。即使holonomic存在性成立，也不能由此跳过实际rank、目标非零与strict比较。

本轮是正式提前全局复盘，节奏从222重新计：**正常下一次228，允许226–230；严格上界/反例/两轮无核心进展即提前。** 每轮继续报告新证明、未通接口、是否有数值新结论及下一步选择依据。

### 222.6 阅读、独审与归档

本轮五份数学/架构稿与新增有限补充引理分别独审，Root完整阅读最终稿和收据；报告另审，见[报告独审](research_round222_global_report_review_20261008.md)。Root新证明、其他作者纸面推导、有限精确计算及原文架构阅读分开登记；文献选页/section阅读不升格为整篇proof审定。

literature保存固定仓库的六个Catalan section及DD introduction、CDT/FR/Mistiaen实际选页TXT、已有Fauzan/Fischler定位文本、API与DLMF原始公式。没有新PDF下载。Δ₀的有限证书涉及精确有理计算，运行数在[合并阅读范围](../literature/global_review_sources_round222_20261008/root_reading_scope.md)和[独审](research_round222_pade_target_head_review_20261008.md)单独登记；其他数学稿为纸面推导。没有CAS、参数扫描、旧矩阵证书重跑、数值积分、PSLQ或Lean；Git仅只读状态/身份核对。来源与归档见[来源记录](../literature/global_review_sources_round222_20261008/source_reading_record.md)、[本轮清单](../literature/manifest_cdt_global_source_review_round222_20261008.json)。

main保留221最终507032-byte前缀，只原样追加本报告；旧稿与221manifest保持不变。原目标仍active，未将本轮结构成果重新定义为最终完成。
