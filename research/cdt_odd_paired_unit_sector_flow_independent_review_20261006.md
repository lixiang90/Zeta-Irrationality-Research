# 原单位sector精确像秩与36顶点flow共同预算：独立全文数学审查

2026-10-06，/root/conifold_arithmetic_hypothesis。NEW正式combined独审。baseline471既存数学输入、旧/同行数学producer与成功JSON全部只读。本审不执行/import/rerun任何数学程序，不新增数学producer。本人本轮另一个自有Gosper producer已FIRST1成功1次，不能把本审的0次执行误计为整个作者本轮0次。

## V1. 实际全文读取对象与版本

独立实际完整读取quarter主稿 [actual unit sector](cdt_odd_paired_actual_unit_sector_rank_20261006.md)，SHA e4830013ad948599c4e1bb76113aeed3a8b6df23b32a9d575052cd97d7f6fac8：全部U1–U10 sections及U1–U21 equations，正文、执行史及未证范围，没有截断。完整静态读取同stem PY e64add398faeae06855192fcc46a352702f156b191f3668db9dc83e3a6c82b1c。

其保存JSON a0f74c85d2da7343eb1422091bf8670799eff675ad4f7f158976d70ce62bb6d5实际syntax parse，全部metadata及143records的所有字段，分前72/后71两批compact读取，无截断。91 exact-domain与52 cap-only范围准确；不声称人工重新计算124959 assertions。实际完整读取候选source receipt dfa3d7d6951ecec723d2b9875b664ca0bee5f5bb6068d7b4b96009544e9409aa；作者后来增加root独审记录，不冒称未来final receipt已读。

实际完整读取toric [weighted global optimization](cdt_odd_paired_weighted_jet_global_optimization_20261006.md)初稿b25dd84151e645a3efe1c1fa0816df919fcffd460537e8d2f0015530c7a8408d：O1–O11 sections及O1–O20 equations。随后实际补读最终1b7923801d7ff734d278163350d661516abf78fde0687976c4db1d6ef4c6f34f的O18 signed-scale修订；唯此label改变，没有新数学结果或证书变动。完整静态读PY 1e8c6a6000a70a8484e69536da6e09946bf65000545a16d58a053de241ac54d3。保存JSON 5bb704e25707379253bb7733d86c44a354c917bc4c12b96fcd34dfda70bf2863全部syntax parse，全部metadata及113 certificate rows每一个字段，分38/38/37三批compact读取，没有截断；不声称人工重做全部266036 checks。

另外实际静态完整读取冻结raw JSON [all-prime table](cdt_odd_paired_all_prime_budget_verify_20261006.json)，SHA 7cb512f237d3d29370e164ff3fe69bd319d8685582ef7c6d46d7adf9f738e14b：全部metadata及50segments各字段。它的producer没有执行/import。toric candidate receipt完整读取，内含smith-credit旧pin多一字符的65位metadata笔误，已通知作者在未冻receipt修正；不是数学错误。本审不钉住未来receipt状态，最终source由root分别记录。

## V2. 实际饱和格、integer-valued GL与ragged top

U2的整数split论证成立：头部2n evaluation矩阵在前2n个Newton列lowertriangular对角1，后n列为零，所以完整evaluation是split surjection。除掉真实gcd后，每pair primitive row两个系数互素，且pairs支撑不交。于是constraint map满射，kernel确为原饱和rank2n格。模p的constraint解可以在原S坐标提升为characteristic-zero精确paired vector；这比raw约束仅模p成立严格。

U9的ψ=(t^p−t)/p坐标是原integer-valued格的真实Zp GL。i=i0+p i1<3n<p²，i0!,i1!是units；每列integer-valued，Newton有限差分系数整，highest-ratio估值v_p(i!)−i1=0，因此degree-triangular矩阵对角全unit。平移t→t−1保持原Newton格。这个证明没有换成普通polynomial coefficient格。

底Q层允许任意residue functions，最高层仅一个degree<R的low-digit polynomial，故在u个residues上的合法ambient维数是Qu+min(R,u)，不是(Q+1)u。后续延拓先固定一份真实global top原像，只改底Q自由coefficients，因此没有破坏最高层相关性。

## V3. 真unit sector的carry、reflection与constraint方向

p²>8n保证所有factorials只出现第一p层。W的估值2·1_(ρ>r6)+3·1_(ρ≥V)和d_m的h/h+1 carry直接相容；ρ0在高carry及unit sector内，不能删去。负tail residueρ对应positive head residue−ρ，而不是m−1。inner packet0≤ρ<V每cluster恰a个head sites，outer每cluster a+1；actual反射在inner为ρ↦V−1−ρ。

unit/nonunit primitive约束确实迫高carry的unit侧head value为0：其对侧d/g为unit，本侧d/g被p整除。不能反向强迫nonunit侧为0。unit/unit pair给一条两侧value的非零row。二者支撑独立，约束数准确f=au−a(2u−V)_+/2。

固定residue时V奇数迫a偶数，因为2n=ap+r2且p奇数；cluster的a个实际整数sites成a/2 pairs，c=2n+1奇数没有fixed integer site。因而f是整数，反射loop没有重复计费。

## V4. 精确像秩域、whole-X DND与独立paid window

每unit residue tail有h个互异ψ值，h≥2Q≥Q+1，vanishing values迫整个local polynomial为0，故scaled derivative同样为0。rank不是凭一个value节点推出的jetrank。

Q≥a时，在每个unit cluster的a个head sites上底Q层插值满射，所以f条约束在合法B_U空间独立，得所有p≤2n的像秩上界。Q≥a+1时，外部head sites至多a+1≤Q，先固定global top，再用每nonunit residue底Q层使全部outside head values为0。unit/unit及unit/nonunit rows已满足，outside/outside双方为0；split constraint保证这是原格的精确提升，故像秩等于Qu+min(R,u)−f。Q=a区间只保留上界，有限JSON中的等式不能升级全尺度范围。

由unit-tail核基的原S提升和已证integer jet block，各weak vector的unit jets被p整除；nonunit blocks至少p²、head至少p⁴，所以完整whole-X矩阵确有DND，D=diag(1,p)。行列式内容下界−10n+2k逐X系数成立；D_A为零多项式时估值∞也满足，没有非零推断。local GL不改变原S解析范数。

U18的uniform floorerror在x∈[1/4,1]由a≤8,Q≤12给|k−nκ|≤21，包含ρ0、r6=0及p整除n的端点。手算4/7<x<3/5新增piece为12x−6与36−60x，面积13/1176+1/120=19/980；它相对于完整471基线，且旧root窗口和旧x>1窗口不交。PNT方向是较大的valuation lower bound降低整化scale的实费用，不是实际费用下界。

## V5. Ω整数flow与准确dual

O3的每residue边际为w、w+2、w+6；唯一special槽Q+1获−2。在Q≥1时它的折扣后价格不低于前缀、不高于后续；Q0也成立，包括q0第一槽w+6。flow的slot→sink容量1禁止ordinary与coupon重复选择同一槽，coupon总capacity R保留真实ragged top。

对任何整数flow，若后槽被选而前槽遗漏，交换不增费用；若换出获credit的special槽，较早槽不比其折扣后价格贵，可删除coupon以保持capacity。迭代得前缀，再最大化可用credit，费用正是O3。optimal real extreme flow的非边界edges若有无向环，可±ε保持balance；两方向optimal迫成本平，违反extreme。余forest由leaf整数balance消元给整数flow，因而整数与real LP minimum相等。

O4的polyhedral separation证明给attained strong dual，credit-capacity向上射线迫γ≥0。η=2−γ<0时忽略credit、移至η0只改善；λ<0不胜0，λ>11全槽选中且totalcapacity>2n，移回11不减。故optimum在[0,11]×[0,2]。special边际是w+2−η或Q0/q0的w+6−η，其他边际为整数竖线；所有arrangement vertices落λ整数、η0/1/2。因此36个candidate确求原整数Ω的准确值。

这只是该minor model的准确最优，不是实际paired Gram valuation等式；每candidate本身已有独立合法lower bound，安全费用也不需要未知Gramunit。

## V6. 完整进位count、证书覆盖及共同max

actual residue counts用e+1与T，连续模型仅把e+1换nc，ρ0保留。两种ordering、emptytypes、e0与T=p在integer公式中都合法。fixedcompact上每type差至多1，|α|≤550的保守界付1100；actualfloor跳点仍用原integer公式，异常fixed端点只付O(n)主率以外费用。

静态source以Fraction构造全部2/j、3/j、6/j floorcuts；在每cell加入carry/min/positivepart切点和baseline/36candidate/pair界全部pairwise交点。最终闭cell上chosen affine两端支配全部allowed函数，因此整个cell支配，不靠随机sample或finiteprime表。完整覆盖端点相接且面积用exact rational；merge仅当所有标签、floors、系数相同，保留两种面积之和。保存的113行全部实际读取，其中quarter手算两行面积13/1176及1/120准确出现。

old50rawrows中，只有三组同raw affine的邻段合并：8/15–46/85–6/11的(85,−56)，4/5–5/6–6/7的(36,−40)，8/5–7/4–2的(8,−24)。其余47literal逐行与实际冻结表吻合，不重复执行旧producer。baseline费用在独立NEWsource中assert回到完整471值，旧carry信用只在已证兑现区间保留。

手核新Ω窗口2/3–17/24的34−48x面积1/24；2–16/7的16−7x面积2/7。共同budget是max(g471,gΩ,gpair)，不能把Ω-only与combinedgain相加，也不能重复扣quarter19/980。O20准确总gain约1.619377640946，scale safe rate约40.343510723692；这些是已证界与闭区间certificate的主率，不是实际最优费用。

## V7. Signed scale修订、审查结论与未证范围

初稿O18把signed正content预算写成raw denominator的label，root与本人独立指出：别的prime正content不会直接抵扣最小整数分母。作者未冻时仅改为log|Q_n^−1|，Q_n=Π p^ℓp，D_A/Q_n∈Z[X]，准确表达原S整化并除共同内容后的有理normalization scale；已实际补读最终1b792修订，范围正确。它既付负估值分母，又保留正估值内容信用，无免费跨prime分母混同。固定有理source统一分母O(n)、smallp旧o(n²)及p>6n整性仍保留，实处不换局部GL基。

**独立全文数学审查通过**，没有剩余数学修正。两份主稿保留真实degree<3n、饱和S、whole-X与所有finite-place fallback。本文primary新读/新归档0：flow、插值及valuation论证自证，不冒用作者或本人另一个Gosper稿的PDF读域。

本审执行/import/re-run数学producer为0，仅文件读取、静态JSON parse、SHA核对与NEW审稿写入。所有有限mechanism records和exact affine证书只按上述实际读域记录，不把143cases当无限非零，不把266036 checks当人工全部重算。仍缺无穷M5unit或真正higher-layer替代、足够arithmetic–analytic strict margin；不证明ζ(7)、Catalan或其他ζ/L新无理性/线性无关性定理。
