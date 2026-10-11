# higher-slope 同秩整代数参照稿的独立全文审查

2026-10-07，NEW，审阅者 /root/source_pencil_finalize。唯一被审最终主稿 research/cdt_odd_gamma_higher_slope_reference_gate_20261007.md，SHA256 debc1363d3ee14d751df60dcb62d8a457db4fc2717ea8d171aba5c2b4f754ebd，10888bytes。本人 actual FULL 读该最终七节/H1–H15全部公式和文字，独立纸核如下。604冻结记录只读；本报告不创建/执行/import/rerun数学producer、guard、prime表或Lean。结论：PASS，无进一步数学或正文修订请求。

## V1. 实际same-leaf输入、真实rank与全部有限处费用

本人本轮 FULL 读冻结 dual f8e36、整代数参照 d38ca A1–A15以及本文最终稿。实际F_u=B5−u f0在μ=-2^-20的pole5/log4完整jump非零，任意transported branch只加ordinary homogeneous analytic解，不改变非零log系数。非constant holomorphic map若取值μ，局部finite multiplicity仍留log，故不能给meromorphic pullback。原conifold是否已由数值关系填掉不改变这个μ证据。

G_k=(1−At)^(k/q)的Q(t)独立性由绕μ的distinct root characters/Fourier可逆矩阵，适用于first m roots，未把degree或formal representation rank自动当函数rank。k0=1的所有正阶系数0已在final稿明确；对k>0、约分指数denominator2^s'，每个numerator k'−2^s'j为odd，于是
\[
 v_2([t^n]G_k)=(20-s')n-v_2(n!)
 =(19-s')n+s_2(n)\ge0.
\]
odd primes的p-adic binomial integrality亦在FULL已读A3自足支付。q≤2^19无需scale；omitμ确保disk中1−Aφ无零且规范global log存在，所以全部参考pullbacks genuinelyholomorphic。

对CDT8.0.2，b0时每个positive k不可能满足k≤0；全部计数确0，故tau-flatflat0。e0给tau-sharp0，不能仅因reference是algebraic就跳过该费用定义。非负target arrays的两项费用由原定义非负。这构造的是same-rank m参考tuple，未增加target rank。

## V2. Bost–Charles与convexity bounds的准确应用

本人实际FULL读固定CDT v2 PDF89–93。Theorem7.0.1使用C=double Haar log|φ(z)−φ(w)|；它不同于第六节log max rearrangement integral。Reference费用0、rho>0给C≥m rho，目标正denominator rho−tau_T后只增商。

Theorem7.1.6需要alpha_l∈[0,m]；原特征convex increasing自动给非负，主稿保留关键alpha_l≤m。Reference和target有完全相同radii/alpha，故附加条件同时适用，给C−S/m≥m rho。连续版须另外Ahat(1)≤m，主稿明确保留，S为该原式的integral。无假设失败时的免费saving。

所有target应用仍须原定理全部standing hypotheses；若functions非holonomic，额外derivative gate仍保留。本文只在原条件合法时排除strict quotient<m，不将rho>tau单独当任意nonholonomic tuple的充分条件。

## V3. 权重linear system确实是same m、same geometry

本人实际FULL读PDF113–116。7.6.5的matrix entries为I_hk−I_h,k−1除logr difference，以及constant m；它不含source comparison constants或arithmetical arrays。唯一solution s*∈[0,1]^(l+1)和Σs*=1是明示条件，不是已证普遍特征。

7.6.6的numerator准确为Σs_h I_hl，即
\[
 C_m^*=C-\sum_{h<l}s_h(C-I_{hl}).
\]
同一m reference因此使用同一system及same s*，费用0给C_m*≥m rho。若unique/nonnegative条件失败，target theorem也不能从该权重得到所称bound。主稿未用7.6.7 heuristic替代这一条件。

## V4. 任意nonnegative mixed数组的第八节改进

本人实际FULL读PDF122–124。Theorem8.0.1的8.0.3、8.0.4、8.0.5将相应C、C−S/m、C_m*分母费用改成tau-flatflat(b)+tau-sharp(e)，并保留各原附加条件。Zero reference直接以任意matrix体系的b0证明费用0，所以对每个合法numerator都给至少m rho；非负target费用不能取得strict rank矛盾。

原8.0.7确有[0,1,2]^t费用5/3，较dominating nested[0,2,2]^t的16/9更小；这一真实改进不与zero-fee calibration冲突。审查未把所有数组的真实最小denominator exponent等同于原文upper fee，也未排除这些theorems外的negative finite-place收益或新geometry。

## V5. Binomial metrics的全部条件与same R

实际FULL读PDF93的7.1.13完整公式。定义Γ仅通过x−ν和r,λ依赖变量；χ0由logR−ν决定，χ1=(T−Γ(logR))/(rho−logR)。原限制r>1、λ>0、ν≤logR<rho、χ0≤χ1≤m、χ0<1全部仍须满足。

若target含F_u，它的原Taylor radius至多|μ|（另一个更近的base singularity只使半径更小），reference G_k在open disc |t|<|μ|收敛，所以同一个target initialR适用。Reference可代入相同7.1.13参数，费用0得到原完整binomial numerator≥m rho；无遗漏χ terms或只比较某个较弱numerator。删除F_u并真正消μ的projection不属于这一比较。

## V6. 精确scaling逐项核查与finite amplification

令a=logB，ψ=φ/B，Rψ=R/B，νψ=ν−a。在H13中，每个I_hk减a，所以I differences、alpha、Ahat、S全部不变。Weight-system只用这些differences，故solution及其唯一性/非负性不变；Σs=1又使C_m*准确减a。

Binomial Γ(log|ψ|;νψ)=Γ(log|φ|;ν)，T integral不变；λ/(r+1)+ν/2+T减a/2。χ0、χ1、rho−logR、Γ(logR)、logR−ν以及所有correction terms均不变，故完整numerator准确减a。全部original parameter inequalities也同时协变，不可只scale arithmetic而保持旧ν或R。

Scaled reference由v2(AB)≥s+1与原odd-prime证明确为integerTaylor，pullback仍是同一actual G_k∘φ。rho>a后零费bound给
\[
 \mathcal C_m\text{ 或 }\mathcal B_m
 \ge m\rho-(m-1)a.
\]
tau_T≥a、rho>tau_T便给与m(rho−tau_T)的差至少m tau_T−(m−1)a≥0。它是充分排除条件，未被声称最优必要条件。

对finite degree≤d、含1和F_u的九jet polynomial family，FULL已读冻结A10–A12支付真实rank upper m≤2^(9d)、uniformDn^(9d) cap和tau_T=9d(1−m^-2)。最终稿明确选s=ceil(log2m)，B≤m；因此logB≤logm≤9d log2<27d/4≤tau_T。该费用只是此uniform账本，审查不扩到更细array、quotients、删F_u的row或原ξ的另一整模型。

## V7. 阅读证据、状态及范围

本报告被审input为final debc全稿，完整纸核H1–H15通过。此前候选e19的v2公式k0边界已由作者在仍NEW稿澄清，本人已actualFULL回读新最终版；该documentary改动未改变参考族或定理。

个人本轮actualFULL原件为 literature/cdt2024_l2_chi_minus3.pdf 的PDF66–69、89–93、105–106、113–116、122–124，共18distinct页，SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771，固定218页本。首次将十八页与另一稿合并输出曾截断，随后实际完整分成9+9重读；截断输出不计FULL或额外页。没有读取同行页面来替代个人页域，也不继承以前CDT页数。

自己paired主稿的fresh BH3、GM3、Singer11共17页是另一明确读域；本轮个人合计35distinctPDF页。本报告primary新下载0、render0、数学producer新建/execute/import/rerun0、数学失败0、prime扩表0、Lean0。主稿的web README声明不是本轮新数学theorem，本review不称本人重建Lean或验证该外部仓库。

PASS只限列举CDT公式、实际forced-omission carrier与同秩整reference；没有新ζ7/Catalan或原ξ数值无理性/LI结论。主稿仍保留原source与endpoint，未以reference替换target。本报告不pin未来audit、作者receipt或其它同行receipt；等待实际FULL审阅者最终自读及作者收审。
