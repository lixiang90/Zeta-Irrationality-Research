# 第226轮进展：实际分歧桥已通，净算术入口仍未通

2026-10-08。本轮改变的是225所确定的准入问题：从真实递推证明完整无log局部模型，构造原三行共用的合法二重分歧盘，并检查变量缩放的实际算术费用。**这些是结构进展；ζ(7)、其他ζ/L特殊值的数值无理性或线性无关性新定理仍未得到。** 原目标保持active。

## 1. 本轮真正补上的接口

仍为222的固定R_n、原A3/A5/A7/C及完整有限尾。J_r=Δ_r ζ7+Ξ_r，D=ΣΔ_rz^r、X=ΣΞ_rz^r、H_g=gD+X；H_g无条件有有理系数，只有反证假设ζ7=g∈Q时等于ΣJ_rz^r。未换对象或删去背景。

[C226实际生成算子](pade_ramified_generating_operator_round226_20261008.md)采用224已经有效于全部r≥0的多项式递推，明确给出原A/C的生成微分方程及完整初始多项式。粗清分母degree为N=10989，它只是这个明确operator的阶数，不是最小微分秩。

其六个非零有限leading点的真实局部指数为9/2。更关键的是，C证明了完整无log和收敛，而不是从r^-11/2径向主项猜一个Puiseux式：将初始项加入augmented jet，一阶residue为rank1且R²=ηR；η非整数，kI−adR的逆与显式majorant支付收敛gauge，重复0特征值没有留下未检查的log。general vector版本包含完整head与N−1的jet offset。

[Root226外幂稿](pade_exterior_ramification_model_round226_20261008.md)进一步纸证实际二十个三根乘积全部互异。证明用14个不相交的有理模区间及各内部非实共轭对，不展开degree20多项式、不数值求复根。原companion末行只出现一次，q=p6即可使P=q∧³C为多项式并支付所有整数异常；生成向量准确满足

`[q(θ−1)I−zP(θ)]V=q(−1)W0`。

下一层指数在外幂相加为−33/2，故全部二十个非零有限operator谱点上的每个完整V坐标为

`A(t)+t^(31/2)B(t)，A、B全纯`。

因此这些点的局部monodromy阶至多2，二重分歧后函数全纯、原有理微分表达亚纯。B可以为0，未声称全部operator点都是实际源奇点。0的其他叶、∞及全局monodromy未解决；一组阶2局部reflection不保证全局群有限。

## 2. 真正共同分歧图及其明确失败

令M=L1L2L3=(3αb)^9、ρ_M=−1/M，构造

`T(t)=ρ_M(2t−t²)，|t|<3/2；φ(w)=T(3w/2)，|w|<1`。

ρ_M只有double前像1；0的前像为0、2，第二个在域外。其他operator谱点至少远出M/(L1L2κ)=(3/u)^9>5^9，而|2t−t²|<21/4，全部避开。先在盘去掉{0,1}支付解析延拓：原生0 loop固定原Taylor芽，1 loop投影两圈且局部monodromy平方在全部解上为I；再填0/1。这给原D、X及所有固定有理g的H_g共用的实际全纯盘，而非只填一个形式leading项。

但这张图的

`|φ'(0)|=3/M<1`。

所以它连零算术费用的正conformal入口也不过。**合法图存在性已付，正净容量未付。** 这不是所有ramified图的上限。下一步必须给更大图的实际净收益，不能以消掉更多branch点替代CDT所需比较。

## 3. 有理缩放：完整格必要费用与受限中性

[A226有理缩放稿](pade_rational_scaling_admissibility_round226_20261008.md)证明f(x/N)若仍使用有限固定LCM数组，对每个固定p|N必须有原系数内容

`v_p(f_n)≥n v_p(N)−O(log n)`。

原安全清分母只给负O(log n)下界，没有排除正线性内容。可变素数上的同余不能替代固定p的内容结论。因此不能把N^n免费藏进有限LCM列，也不能据旧safe166/9宣称所有缩放失败。

对完整次数≤D的m行polynomial frame，实际jet矩阵精确协变

`E_N=diag(N^-k) E diag(N^j)`。

若I为非零full-column minor、q=m(D+1)，β_I=Σ_(k∈I)k−mD(D+1)/2≥m(m−1)(D+1)²/2，实际整数值格Λ_N的必要index费用满足

`v_p[Z^q:Λ_N]≥max(0,v_p(N)β_I−v_p detE_I)`。

这保留了原minor的正内容项，也保留有效nonzero cutoff的缺口。若最早q行minor非零或另付相应asymptotic normality，标准metric转换的shift才为(1−1/m)logN，并与解析logN、energy logN恰好中性；一般I用其实际β_I。normality在本包尚未付，这不是已认证的最佳整模型成本下界或新LCM数组。

独立于该normality，所有整数N≤24^9/4的目标原变量单叶入口均失败，保留D时可扩大到N≤144^9/4。更大N、分歧图和真正primitive模型未排除。

## 4. 自然代数尺度：全部共轭会改变判断

[B226数域稿](pade_galois_normalization_gate_round226_20261008.md)检查实际目标的两个自然growth尺度

`T_s=(3α)^9，Tκ=[b√(3α)]^9`。

δ=3(α+1)/(α−3)满足δ²=3α且在cubic field内，故Tκ只需degree6场，无需猜degree12。完整norm/embeddings给平均log尺度12log3与(21/2)log3；所有3-place深度同为12或21/2，其他finite places均unit。这个精确valuation是尺度transport的账，不是实际目标系数最佳内容下界。

每个embedding仍为同一个原有理H_g，只有坐标σc改变。Koebe界平均后，这两个自然尺度的arch-only单叶入口已经严格为负；在3处选已认证linear map c·id的全处transport，product formula又把scale credit减掉，conformal sum与energy同步回到原坐标。一般positive finite maps、另一个projected source、所有代数下降未排除。

B还给一个自含nonsplit差分反例：leading polynomial的coprime factors并不能自动支付rational projector。对本包仍需实际intertwining/Ore identity、目标state membership和全部有限初值，不能从formal谱分组认领低秩CDT源。

## 5. 大局判断、cadence及下一轮的停止条件

222以来的成果链已经清楚：223付整性和实际存在性，224付非零性与真实递推，225付完整渐近/函数域rank并排除原变量单叶入口，226付真实无log及合法共同分歧图。它们可作为结构资产，但当前原始增长很大，已付小图与自然缩放均没有净入口。距离数值定理最关键的缺口仍是**同一完整整模型下的正解析/算术margin**。

因此227的投入要限定：先检验一个确实可能跨过该缺口的较大同叶图、已付完整模型或明确总上限；不给正净收益希望的具体对象，就将此固定包降为结构工具。暂停原变量单叶优化、safe166/9细化及无准入的prime/参数扫描。不能用更多形式factor或局部classification绕过停止条件。

按用户要求每4～8个完成轮次俯瞰全局，默认6轮；正式复盘仍222→228，窗口226–230。225是提前的有限方向检查，并未重置全局复盘cadence。228将比较原目标之外的周期/ζ/L源、新论文提供的实际输入、已付上限与继续/停止条件；结构障碍或连续两轮无核心接口进展可提前触发。226有核心接口进展，但**有进展不代表值得无限延长当前路线**。

## 6. 独审、文献与运行

数学程序合计0，CAS/复根求解/degree20展开/序列或参数素数扫描/数值积分/PSLQ/Lean/旧producer重跑均0。本轮自含纸证及独立纸审，未宣称形式化验证。

新增primary PDF2、HTML2、selected TXT3：C归档Novikov–Yakovenko作者PDF并实际读完整PDF33–38的§6，DLMF仅完整相关§2.7(i)；B归档官方当前CDT ICM原件并完整读PDF3–8的定理/places/proof条件，另存Abramov官方bibliographic metadata，失败PDF请求未记成功；A提取既存CDT2025两页选段，不重复下载。Root实际完整读新ICM六页TXT与旧fixed-v2完整Remark8.2.42及相关段，DLMF二阶校准不承担高阶proof。没有重新检查云端仓库/Git/Lean，222身份只复用。

[Root独审收据](research_round226_root_math_review_20261008.md)另存。A初版目标符号错误已修成plus；B独审又要求明确normality才可认领特定metric shift；C独审要求Root共同图先处理原生0 operator点。均在226终稿内修正，不改旧冻结数学。作者与独审责任、实际FULL范围见[Root scope](../literature/pade_ramified_admission_sources_round226_20261008/root_reading_scope.md)。各同行收据及最终文件身份进入[226 manifest](../literature/manifest_cdt_pade_ramified_admission_round226_20261008.json)。归档仅核225不可变输入并保留main的542249-byte前缀，追加本报告。
