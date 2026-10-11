# 真实 supported 配对约束向 weighted dual 的全尺度转移

2026-10-06，NEW，toric_chow_completion。baseline487全部既存数学文件/收据/成功或失败数学producer只读；旧、同行execute/import/rerun0。本稿保留原S、B6/κ3/s5、degree<3n、rank2n、原source与whole-X。研究的是signed same-S normalization scale，不称raw最小整数分母。验证只允许一份DISTINCT NEW FIRST1 guarded affine certificate，成功/失败随后均不重跑。

## T1. 实际读过的当前权威输入

本轮实际全文读主报告§§133–137，hash ee3475aa18e73d8477d0cdece0a5e7504cfb99e3d5a52d6a66cfa1f2e7536837，无full-main claim。冻结global optimization O1–O11给原joint jet model，当前signed整化费用为

\[
A_{487}=\frac{68678357676574195925297901887}{1702339643838709841383978560}
=40.343510723692\ldots.
\tag{T1}
\]

其frozen JSON5bb704…的全部metadata及113 rows的combined affine（lo/hi/slope/intercept）本轮完整读取。NEW certificate仅更新x∈[1/4,2]，以这个已冻结closedcover作为literal旧baseline；不重新运行旧全window[1/4,6]、旧36vertex producer或任何auxiliaryprime表。

设p>5、p²>8n、p≤2n。记

\[
2n=ap+r_2,\quad3n=Qp+R,\quad6n=hp+r_6,\quad
V=p-r_2,\quad U=\{0,\ldots,u-1\},\ u=\min(r_6+1,V).
\tag{T2}
\]

unit-tail residue的actual positivehead反射是σρ=V−1−ρ。U中的每residue有a个headsites；其完整independent primitive constraint数

\[
f=a\min(u,V/2)
\tag{T3}
\]

已由冻结actual-unit-sector稿U2–U6证明：unit/nonunit强迫高carry unithead值0，unit/unit一pair一relation。Q≥a，使bottomQ层对这些a个headsites满射，固定raggedtop后约束仍独立。下文的supported coefficient-space观察由quarter本轮独立推进；其正式稿落地后实际阅读全文和准确pin将另登记，当前此处给自足证明，不提前声称已读未保存peer稿。

## T2. 指定 jetrows 上可支付的真实 supported rank

选2n个actual jetrows I，记residue中所选行数r_ρ；置B={ρ:r_ρ>Q}、C=B∩U。按原degree cutoff，B上的完整允许coefficient space维数为Q|B|+min(R,|B|)：bottomQ层各residue自由，top是一个degree<R low-digit polynomial restriction。

先把B外的小blocks的全部selectedrows当成至多Σ_(ρ∉B)r_ρ维贡献。B上的selectedrow map是其完整coefficient space的一个projection；无需assert Hermiteunisolvent或恢复constant。actualA_Z的coefficient vectors全部满足支撑在B∩U的primitive head constraints：

* ρ∈C而σρ∉U：unit/nonunit高carry方向给a个headvalue zero relations。
* ρ与σρ均在C：各实际headpair给一条relation；其总数为(a/2)|C∩σC|。

反射固定residue时V odd迫a even，因此半数公式仍整。记

\[
f_B=a|C\setminus\sigma U|+\frac a2|C\cap\sigma C|.
\tag{T4}
\]

这些relations在完整B coefficient space上独立：固定真实top，bottomQ在各unitresidue的a个headvalues上仍满射，互不交primitivepair的relations独立。于是allowed B-space减少f_B维，selected projection只能进一步降rank。因此

\[
\boxed{\operatorname{rank}_{\mathbf F_p}Y_I|_{A_Z}
\le\sum_\rho\min(r_\rho,Q)+\min(R,|B|)-f_B.}
\tag{T5}
\]

这不在任意selectedrows上免费减完整f。subtract的仅是supported在big coefficient sectors的f_B。derivative-only可能漏constant，但T5是在projection之前bound完整allowedspace；没有将缺方向又重复作为额外信用。实际saturatedS的精确char0 lifts和integer-valued ψ GL均保持冻结证明。

## T3. 原 whole-X minor 模型的新修正

原p⁵B_X的node-block仍是W_j[[p⁵V_j,p⁴U_j],[p⁴U_j,0]]；全部X系数integer，head另付4、nonunittailw=2/3/5，旧形式未改。非零A-minor的左右nodecounts相同，所以左右指定jetminors在每residue有相同r_ρ，因而同一B和f_B。

两次Cauchy–Binet与T5严格给

\[
v_pD_A\ge-10n+\Omega_p^{sup},
\]
\[
\Omega_p^{sup}=\min_{\substack{0\le r_\rho\le2q_\rho+2\\\sum r=2n}}
\left[\sum_\rho\{w_\rho r_\rho+4(r_\rho-2q_\rho)_++2(r_\rho-Q)_+\}
-2\min(R,|B|)+2f_B\right].
\tag{T6}
\]

原w,q沿用冻结integer定义。T6是actualwhole-X新lowerbound，并未宣称新的actualGramSmith等式。局部projection或GL没有改变原S实处范数。

## T4. supported head graph 的删除界

完整U有f条独立relations。若删除s=|U\B|个unitresidues，每个包含a个headsites；一个actualprimitivepair至多因其某端被删而失去一条relation。故至多损失as条，得到

\[
\boxed{f_B\ge(f-as)_+.}
\tag{T7}
\]

这也直接由T4计数得出。unit/unitpair两端都被删时这个upperloss可能重复计数，方向只会使T7更安全；不能将as解释为准确损失。

## T5. 全p的权重 gap 支付 missing constraints

沿用旧dual λ∈{3,…,11}、η∈{0,1,2}；不是假定本轮新model仍有36vertex准确dual。每residue定义

\[
\alpha_\rho=\min_{0\le r\le2q_\rho+2}
\{w_\rho r+4(r-2q_\rho)_++2(r-Q)_+-\lambda r-\eta\mathbf1_{r>Q}\}.
\tag{T8}
\]

unitρ∈U有q_ρ=h、w_ρ0。因为h≥2Q且h≥3a、a≥1，2h>Q。对λ≥3，unitpricedminimum在r=2h或2h+2，准确为

\[
\alpha_U=(2-\lambda)2h-2Q-\eta-2(\lambda-6)_+.
\tag{T9}
\]

若unitblock不big，即r≤Q，其pricedminimum为−λQ，因而相对T9的gap准确为

\[
G=(\lambda-2)(2h-Q)+\eta+2(\lambda-6)_+\ge2a.
\tag{T10}
\]

最后一项不等式完全alln：h≥2Q⇒2h−Q≥3h/2；h≥3a⇒3h/2≥9a/2≥2a，λ−2≥1、η≥0。没有从finiteprime探针推unit或jet层。

于是任何allocation的sum pricedcost≥Σα_ρ+Gs。其oldragged项满足−2min(R,|B|)+η|B|≥−(2−η)R（对|B|≤R和≥R分别检查）。联合T7，

\[
Gs+2f_B\ge2as+2(f-as)_+\ge2f.
\]

所以得到本轮主要全尺度theorem

\[
\boxed{v_p^{Gauss}D_A(X)\ge-10n+\Phi_p(\lambda,\eta)+2f,
\quad\lambda=3,\ldots,11,\ \eta=0,1,2,}
\tag{T11}
\]
\[
\Phi_p=2n\lambda-(2-\eta)R+\sum_\rho\alpha_\rho.
\]

27个candidate均逐X系数合法。这里不是将完整f直接加到旧Ω：T10的真实weight gap支付了那些看不到约束的unitblocks，再由T7合接。也不直接给旧λ0/1/2同样信用；那些candidate的unit行数未必足够，不能忽略其missingconstraint费用。

## T6. 连续转移和全place费用

x=p/n∈[1/4,2]，令a=floor2/x、Q=floor3/x、h=floor6/x，c=6−hx、t=(a+1)x−2、r=3−Qx、u=min(c,t)，F=a min(u,t/2)。旧三type continuous counts与pricedα沿冻结定义，得到新界

\[
g_{sup}(x)=\max_{\lambda=3..11,\eta=0..2}
[-10+\phi_{\lambda,\eta}(x)+2F(x)].
\tag{T12}
\]

在取整参数固定的各**开区间**，actualu与nu差≤1，actualf与nF差≤a≤8；原φ count移位误差付1100，故T11保守统一付1116误差。不可把这个邻段误差声明免费延伸到floor跳点：例如x=1/4准确a8/h24/Q12，右侧a7/h23/Q11，type counts在跳点可不连续。

取有限集合J，包含域端点、全部2/j、3/j、6/j的floor分点以及本次closed affine certificate的所有分点。若p/n∈J，就直接用T11的准确整数式或原487精确fallback，不以邻段continuous值声明该prime的统一O(1)误差。对每个n，每个固定有理x∈J至多对应一个prime p，故这类places数有与n无关的上界；本window所有相关界的量级至多O(n)，分别付logp后合计O(nlogn)=o(n²)。这保留全部endpoint primes，而不会改变T13主率。证书的closed端点比较只证明各分段affine延拓的积分，不声称它们在跳点都等于准确integer模型。smallprime、p<n/4、p>2n保持487baseline所有places的合法signedlowerbounds。

以g487为冻结113row combined affine，逐prime取max；设Δ_sup=∫_(1/4)^2(max(g487,g_sup)−g487)dx。原same-S合法Q_n满足D_A/Q_n∈Z[X]，PNT/统一O(1)误差给

\[
\boxed{\log|Q_n^{-1}|\le(A_{487}-\Delta_{sup})n^2+o(n^2).}
\tag{T13}
\]

signed正content可降低此有理归一化尺度的实费用，不能跨prime抵扣raw最小integerdenominator。whole-X、原source固定分母O(n)、原arch范数和旧allprimefallback完整保留。

## T7. 一个无需程序的真实新增窗口

2/3<x<17/24，h8、Q4、a2、u=t=3x−2，unitclosedreflection使F=t。λ3η2旧φ给gΩ=48−78x，T11新界给

\[
\boxed{v_pD_A\ge44n-72p},\qquad g_{sup}=44-72x.
\tag{T14}
\]

这个finite inequality无需O(1)：unitcount准确T=3p−2n，f=T，φ边界亦准确。487此前共同max在该window为max(48−78x,10−24x)，交点19/27。新paidgain分别为6x−4和34−48x，因此

\[
\boxed{\int_{2/3}^{19/27}(6x-4)dx+
\int_{19/27}^{17/24}(34-48x)dx=\frac1{243}+\frac1{1944}=\frac1{216}.}
\tag{T15}
\]

quarter独立以unitmirrorpair pricing得到同一window。本稿后续全cover会包含它，不得再次外加1/216。当前不把一个小window当作整体最优收益。

## T8. FIRST1 closed certificate、全尺度主率与来源

纸面T1–T15先保存后，完整静态读DISTINCT NEW `cdt_odd_paired_supported_weighted_dual_transfer_20261006_verify.py`。程序在数学计算之前以exclusive-create建立状态JSON，若失败保留失败源/状态。实际首次且唯一执行1次，exit0 PASS，success1/failed0/rerun0，全部旧/同行execute/import0；成功PY/JSON随后只读。没有finiteprime样本表或auxunitprime新探针。

程序只更新[1/4,2]：literal录入本轮已读冻结113cover的combinedbounds，其中106rows与更新域相交；保留原不变费用T1，不重算旧[2,6]模型。所有2/j、3/j、6/j的floor分点及c=t、c=t/2、t=t/2的type分点先切开；每cell的27个candidate是affine。再加入它们与旧baseline以及彼此的所有内部交点，得到213arrangementcells。在每个closedcell的左右端点检查选定winner≥全部candidate、≥旧bound；affine函数的端点检查即全cell证明。精确积分并合并相同表达式，最后saved JSON记98mergedrows。213是内部检查计数，**并未在JSON逐条保存213cell记录**；98条记录全部含lo/hi、Q/h/a、old、新winner/new、gain、exactarea，作者已完整实际读取metadata及这98条的全部字段。首次组合读输出中段被截断，随后独立完整补读700–1399行与1400行至末尾；不把截断输出算作完整阅读。

共12141endpoint/area checks，严格有理结果为

\[
\boxed{\Delta_{sup}=\frac{589881521281691}{20345444272717200}
=0.0289932976333532\ldots,}
\tag{T16}
\]
\[
\boxed{A_{new}=\frac{800671681093752110193539327219}{19860629178118281482813083200}
=40.314517426059346\ldots.}
\tag{T17}
\]

T15的1/216已在共同max中包含，不额外叠加quarter的同一窗口。小p、p<n/4、p>2n均保留原487完整界；T6在开floor cells的uniform1116误差，加上有限jump/endpoint places的准确整数fallback及O(nlogn)费用，使PNT主率T17覆盖全部n，而非从有限n拟合。成功PY/JSON的closed affine积分不因零测度端点处理改变，未重跑或修改。程序的成功不代替T2–T5的all-scale proof。

成功数学源SHA256为 `92b737b19375e973c97b67830477b10313b365f617df6dc5e0f193e74bd0aa94`，结果SHA256为 `a37ce3e552a6ded9efaa48f07ca268ec207000d4a165cc4e072ba52dc31f1694`。本轮已实际全文读取冻结actual-unit-sector稿U1–U10（含全部U1–U21），据其U2/U3/U5/U6核对primitive split、真实ψ GL、方向与ragged top；没有执行其producer。

本轮principal无需新PDF/外部source；T2 supported coefficient-space思想与quarter协同，T4–T11的删除/weightgap转移为本文新证明。正式peerpaper落地后的实际readscope会如实补记，不伪称已读未保存文件。

本稿没有证明无限target非零、actualhigherGramSmith单位、strict margin或新ζ/L/Catalan特殊值定理。新的安全费用仍须与已证同对象解析率比较；若新safe上界仍较大，不能推actual方法no-go。

## T9. 未计入本轮费用的一个确切后续接口

root在本轮成功源/JSON冻结后指出：n<p≤2n使a=1，此时λ=2、η=2亦可支付完整f。直接手核unitprefix：r≤Q的minimum是−2Q，而Q<r≤2h的minimum是−2Q−2；r>2h只增加费用，故notbig的gap准确为2=2a。T7和T5的ragged不等式仍适用，因此这个特定域可严格给

\[
v_p^{Gauss}D_A\ge-10n+\Phi_p(2,2)+2f\qquad(n<p\le2n).
\tag{T18}
\]

T18是本轮纸面的附加接口，未进入已成功程序的27candidate，不据它改写T16/T17、不重跑成功源、不声称已兑现额外全window面积。下一轮若更新新certificate，必须在同一487/本轮commonmax上再计实际新增面积。
