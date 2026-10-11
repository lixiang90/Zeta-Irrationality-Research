# 第254轮唯一独审：完整primitive与解析预算结算

2026-10-10，B。**PASS：未发现需修改的数学或报告范围。** 本次通过工具实际FULL读以下Root/primitive/C最终数学稿、正式报告及四份scope，输出完整未截断，并逐式独立纸核。本人的8522稿仅绑定作者身份，其独立审核者为Root；不把作者自读冒称独审。数学程序、有限头手算/证书、CAS、扫描、GET、外Git写和旧producer执行0，只新增本收据。

## 1. 冻结目标身份

|文件|bytes|SHA256|本收据范围|
|---|---:|---|---|
|research/rv_chi8_mellin_uniform_gate_round254_20261010.md|7789|8a1787ba5e7e19ac877327d63fca62e565489d0949570b34c0e85628ebc219d1|FULL独审(1)–(9)|
|research/rv_chi8_primitive_budget_round254_20261010.md|9256|a21fc59352a6343befa23023adc695f5fdeecc978c5528aa57785007f3f61060|FULL独审(1)–(16)，含(7a/b)、(9a)|
|research/rv_chi8_signed_error_round254_20261010.md|8062|d823df352a0c657262b7e14d409992cbff9f46cddbe80d238312fd33f7695a29|FULL独审(1)–(12)|
|research/rv_chi8_analytic_admission_round254_20261010.md|8522|1a9676cfb61d22d694f2f8b946861145f17ceb5117d7ec242c99e2ad5b05fadd|B作者稿，Root已独审；这里只绑定|
|research/research_rv_chi8_budget_progress_round254_20261010.md|5575|98d10951e7c51f353455989b516aa23ab8bab38eb7af8023fea4deea25c94961|FULL独审全部5节|

四份scope均实际FULL读并核身份：同目录 literature/rv_chi8_sources_round254_20261010/ 下，root_reading_scope.md 3467 B /69785f36c1750955e6cdac81c8663de4bc149b68f8a031cb99ed3f7ac8905121；primitive_reading_scope.md 2906 B /87210fc94ffbcebcb9540d0469846a2ab1107568486fe215e34ac49f56b6bd58；error_reading_scope.md 1798 B /dfa335133ea964929b4093d655db762072edd44fae9b3b01148c3f6f36220602；packet_reading_scope.md 2751 B /1b5579450c9b9112245f3f9afd0bfeda5e98f73dad0ea15f5bd75b89edc83f69。

## 2. 完整算术内容与primitive公式

逐式核 λ⁴=2u、N(λ)=2、N(u)=1，故u的整数乘法矩阵可逆。N(M)=2^(3n)且adj(L_M)e₀对应λ^(9n)乘整数单位。剥去2^floor(9n/4)后，剩余范数是2^r、0≤r<4，排除所有四系数再共同被2或奇素数整除。因此这份公共乘法向量的content是exact，但作者没有把它冒称最终v或A/c的exact gcd。

W(t)=K_n binom(t+10n,8n)binom(t+8n,5n)与W整数性相容。K_n既约分子B_n确整除每个W；逐因子(7n+i)/(5n+i)≥4/3支付B≥(4/3)^n。两对floor和的差在{−1,0,1}、p^a>8n项为0，支付B|d_(8n)，没有执行素数枚举。

矩阵分解给β=2^floor(9n/4)B³整除v，故直接整除完整整数P组合的Gauss头A及c；没有从Q的额外B推给有理头。首四列r≤3的原RV参数清整用Λ*=d_(13n+3)d_(12n+3)，完整头分母q|Λ*。实际gcd公式使用gcd(p,qδ′)=gcd(p,δ′)，p=0、q=1边界也成立。Λ及共同β消去后仍保留q/d与同一U′，未领取最优净费用。

## 3. Rodrigues、Mellin与signed核

两个Euler块逐单项式核为 t^(−2n)D^(8n)[t^(7n)D^(5n)(t^(8n)f)]；原符号与(t−1)³ⁿ合成Q=−C t^n(1−t)³ⁿD^(8n)h正确。负j测试 t^(n+j)(1−t)³ⁿ仍是多项式。0端h至少10n重零、1端至少5n，分别支付8n次分部积分的全部边界；测试degree<8n给−n≤j<4n的5n矩消失。

对log测试，D^(8n)(t^K log t)公式的符号、指数与阶乘正确；乘t^(7n)后degree≤j+3n<5n，再转移5n导数，边界由原t^(8n)(1−t)^(10n)支付。C稿完整高阶误差转移在0的最坏t^(3n)log仍可积，未删除log修正或假设导数核为正。奇偶精确尾分别为t^(2n)w₈和t^(2n)(1−t²)/(1+t⁴)，整体(−1)^(floor(n/2)+1)符号正确。

Mellin公分母长度13n+4、endpoint零给分子degree≤10n+3。负j普通零与0≤j<2n双零均避开分母极点；首一整数因子除法给非零H∈Z[s]、degree≤3n+3。绝对交换由∫ρ|U′|/(1−t)<∞支付。5n内部变号、H非零或正尾核均没有被误用于actual error非零。

## 4. 统一解析界及upper增长账

四个复极点的 w+w⁻¹=2u、|w|>1选择唯一，s=(w−w⁻¹)/2非零。把两几何级数相加得到Chebyshev展开，degree2n−1截断的尾常数C有限且与n无关；log正交删除截断项。ρ=min|w|>1，且|u|≤3给ρ<7。实际充分界含V=(q/d)∫ρ(t)|U′|，未以另一对象的能量替代。

LCM递推也自含成立。m=ceil(N/2)，d_N/d_m每个素数最多新增一级；该最大p幂在中央binomial的Legendre式贡献1，其余贡献非负。固定坐标toggle把所有floor(N/2)-大小子集单射到非同大小子集，故中央binomial≤2^(N−1)。由d₁=1加强归纳可得d_N≤2^(2N−2)≤4^N，不需PNT。

于是β≤2^(201n/4)；E_n⁴=2^(204n+32)后差指数为615/4。Λ*≥1及ρ<7确给认证量 ℬ_n≥24C·2³²(2^(615/4)/49)^n→∞。**这是当前认证upper自身的lower，不是实际|ℓ_n|的lower。** Root数学与报告都明确保留真实q/d、实范数与signed cancellation可能更优的范围；不能据此宣称optimal no-go。

## 5. 报告决策、来源与执行范围

正式报告准确把结论限定为同一 fixed adj(R)e₀、v₄=0 实现：已付指数级共同约分、精确primitive表达和统一解析gain，尚未付无界实际非零与严格净衰减。依253有界检验条件结算其默认投入，不自动开放第五列、换向量、prime、参数或map续窗。255跨架构比较只是下一项任务，未冒称已有新目标或比较已完成。last formal252、completed2、next256、本轮no reset、goal active、numeric theorem false一致。

本人本轮实际FULL读253权威数学9888、报告5913、manifest14372及RV既存物理PDF4–6完整提取文本8499 B /81df172f798f8c13b288371fcb536688dcb996971ffbc9ed21b9f61561f0bdd7，含原(2.1)–(2.9)与完整Theorem2.1。采用已发表整数定理，未冒称49页全文、所有前置算术引理本轮重审或视觉原件认证。新数学为保存稿自含纸证；作者scope声明只核其陈述边界，不继承为本人读域。未采用Root metadata查询为新数学命题或全球新颖性证据。

最终保存后实际FULL复读本收据并报bytes/SHA。本审查不执行archive，不改任何冻结目标、253文件、main、policy或manifest；后续归档仅作一次只读pin/prefix核验，不产生第二收据。
