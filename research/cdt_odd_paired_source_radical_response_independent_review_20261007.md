# 原配对格的真实源响应、质量映射与固定源门槛：独立审阅

2026-10-07，quarter_actual_rank，NEW。504 baseline records（503数学文件及1个入口guard）和全部旧/同行producer只读；本审阅不执行或import任何数学producer。实际全文核 root 最终数学稿，sections S1–S6含S3b、equations S1–S14；结论通过，条件范围保留。候选正文的待审标签由本正式审阅及其作者外部final receipt supersede，不要求改数学文本。

## R1. 实际读取和最终指纹

最终主稿 [source radical response](cdt_odd_paired_source_radical_response_20261007.md) SHA
`10897f75c7a2cb932988a751a25a85dafd79640b715090b7715fc96aeaa37a7a`。
先完整读初稿16019、实际执行史及S5反机制更新后的b102，再完整读含S12–14的e68e，最后完整读10897，均无截断。对最终文本只逆向替换新增的singular-slope说明，在内存中重算SHA恰回到
`e68e814ebcb1bf303474e3dd26214ff1809f676d4453bc4235ebacfcdb4f9656`；文件未修改。这确认最后修订只有已讨论的范围澄清。

实际完整静态读 [NEW PY](cdt_odd_paired_source_radical_response_20261007_verify.py)，且读取发生于root首次执行前；执行后SHA仍为
`dd457d93d1ce5bc4c80265381d877daf11cabf427b6f4e2100097b6a8e1f06ed`，没有重读即冒称执行或import。
实际完整读 [保存JSON](cdt_odd_paired_source_radical_response_20261007_verify.json) 的metadata、三个actual case和九toy的每个字段，SHA
`064c740175b4122156c8bc7de242f4ea789ff757606b2ed4c27a96cbf51cdb19`；实际完整读 [guard](cdt_odd_paired_source_radical_response_20261007_verify.guard.json)，SHA
`50d52715865eeb9cd6929a6b3ae4223c35d44b8294ec6513753860d9ae4656c8`。
guard记录入口及source指纹，成功记录在独立JSON，未把STARTED标签说成另一次数学执行。

本轮另实际完整读：冻结single-bordered a60d（B1–B8/B1–B11）；冻结value-Gram 57f9（V1–V8/V1–V14）；冻结Racah-border 2e04（十一节/R1–R30）；NEW cross-Racah当时快照58c1（十一节/C1–C30）。cross快照实际SHA为
`58c1f79eb8ca81b07ef6bc3b8fe433289e7a2f46eccfc75c0931cf947fcf0340`。
这里登记实际读过的文本，不提前登记其未来来源收据或未读primary。

## R2. 实际source与归一化符号

原B6/k3/s5、完整S、degree<3n和rank2n不变。辅助域n4r、p18r+1使degree<12r<p，ordinary derivatives为p整数；strong/weak局部basis依赖原paired格，不能换成自由coefficient模型。

对tail j=p+l，Hj、H2n+j都恰有一个p极点，H6n−j无p极点，所有端点<2p。因此
\[
pC_j=2\pmod p,\quad p^3H_j^{(3)}=p^4H_j^{(4)}=1\pmod p,
\]
\[
p^5U_\alpha=-8p^2\pmod {p^3},\qquad
p^5V_\alpha=-40p\pmod {p^2}.
\]
weak的实际translated value是P(−p−l)/p=(η−1)J，不是ηJ；导数为J。逐块得到source response
\[
SS=-40Z^tDZ,
\quad SW=8Z^tD(4-5\eta)J,
\quad WW=8J^tD d_4J,
\]
其中d4=1−η²−4(1−η)²。故S6的8A4和leading 6βA5准确，包括middle halfjet。head的scaled Vα至少p4，除两侧Dp和source的额外p后仍至少p；非unit head带额外W，不遗漏任何头部项。

对weak×weak，S4低表面精度足够是因为两取值先各含p：Vα的p2余项至少p4，Uα的p3余项至少p4；再除p3仍消失。weak O(p2)精确paired修正同样只贡献更高阶；strong只需modp值Z，其更高lift和derivatives不改变此响应。

## R3. 真正的affine质量Gram

令E=[Z,−(1−η)J]。逐block有
\[
\partial_s\mathcal A_s=-E^tDE,
\qquad\mathcal A_4-\mathcal A_5=E^tDE.
\]
在K=kerA5上限制时A5项为零，因此S9确为G_K=T^tE^tDET。这里D的ambient单位性没有提升成restricted Gram单位性。一个有限域的一般例子即可说明逻辑区别：D=diag(1,−1)，v↦(v,v)单射，而其restricted Gram恒零；此例不是actual原family反例。

## R4. 完整cross的实际fold与质量核重建

S12的θ由first radical block唯一确定，因为Z full-column-rank、imZ=kerL、L full-row-rank。直接代回得到G*θ=C*q及H*q=C*ᵗθ；反向Zz=(K5Jq−D⁻¹Lᵗθ)/6确在kerL，并重建全部原kernel，不除G*、H*或任何未知restricted form。

物理center c/2=13r+1，a_l−c/2=5r−l；negative nodes覆盖−r+1,…,5r。middle非零paired节点出现两次，每次(1−η)=1/2；middle原点只出现一次、系数1/2；outer节点出现一次、系数1。T/Q/S_y均even，故F*=L(1−η)J精确等于完整对称sum的一半。半权重原点保留，没有把χ删掉后冒称actual identification。

独立核cross稿C3–C11的有限Racah极限。KS Eq1.2.2在α=−a−1、β=2a+1、γ=a、δ=−a−1、a5r处给
\[
\nu_0=(-1)^a\frac{(2a+1)!}{(a+1)(a!)^2},\quad
\frac{\nu_n}{\nu_0}
=\frac{(n+a+1)_n(n!)^3(2a+2)_n}
{(a+2)_{2n}(-a)_n(a+1)_n^2}.
\]
三个n!来自两次(1)n及原n!，没有继承旧cubic族的三个(−2a)n。其leading coefficient也为明确单位；最大factorial index15r+1<p，终止范围内无零分母。g→0权重k0为1、k>0为2倍实际比值，保留原点。首r阶complete profile因此正常，F*满rowrankr。

S14的36倍展开为两项kernel交叉及两项LJ；用C*+LJ=6F*准确缩成
\[
(Ev)^tDEw=(\theta^tF_*q'+\theta'^tF_*q)/6.
\]
若Ev0，由Jq=−D⁻¹Lᵗθ和kernel第二行得6F*ᵗθ0；F*满行秩、J/Z单射逐步迫θ,q,z全零。因此E|K单射已实际闭合，不是仅条件性的符号lemma。

令τ=rank(θ:K→F^r)，上述symmetrized factorization给rankG_K≤2τ。最终稿补充的边界正确：k>2τ只排除斜率G_K自身满秩，不能排除R0+8αG_K因R0补方向而unit。一个singular slope不等于整个pencil恒奇异；S11的nondegenerate-slope条件是充分路径，不是目标非零的必要条件。

## R5. 第一真实Schur residual和非零判据

leading matrix与α无关，故固定α-independent的known-unit complementary block合法。cross和radical-diagonal都先含p；Schur correction为cross²，除p后其α依赖仍含p。唯一残留为S6在K上的source slope，准确得到
\[
\overline R_\alpha=\overline R_0+8\bar\alpha G_K.
\]
R0仍包含β-source、实际高lift和高层，未自由化。若G_K单位，det pencil的最高系数8^kdetG_K非零，degree恰k，失败α residues至多k；p−k≥16r+1。通过的anchor Smith为0^(8r−k),1^k。

Dp determinant贡献6r，p5B整体det缩放40r，所以原D_A valuation=−40r+6r+k=−34r+k。原adapted basis的det是p-unit，不改变此成本。whole-X扰动为24p5实际value-Gram；anchor最大Smith≤1已充分稳定，S11所有X∈Zp非零且归一化模p为非零常数正确。若candidate或sources有固定分母，须先避开有限例外素数。

## R6. 程序与保存certificate的真实覆盖

完整静态source检查通过：guard在math前exclusive-create、output亦exclusive-create，没有import旧/同行模块。source以modp4工作，α-response最大除p3，足以保留模p；scaled harmonic数组对唯一p pole写1，其余写p^e/k^e，指数e≥4的regular项恰在这个精度消失。所有端点<2p，因此没有漏掉第二个p倍数。

代码仅检查旧r1/2/4的literal weights/harmonics及modp2 halfjet representatives；strong cardinal和weak半jet代表没有被声称自身满足char0完整pairing。它们与精确actual lift共享的低jets为何充分，由R2/S2–6纸证负责。保存的4694checks也与static循环计数相符：
\[
5(36+136+528)+(60+228+888)+9+9=4694.
\]
这是静态计数，不是再次执行check。三个actual case、九general diagonal residual toys的保存字段全部实际读；toy根数只支持一般pencil机制，不能当作actual G_K或higher Smith证据。

S12–14在第一次source执行后才补入证明，程序未覆盖其kernel重建、fold、满秩、单射或rankG_K≤2τ；本审阅用完整全尺度纸证核这些新增内容。root实际FIRST1成功1、失败0；本审阅自身数学执行0，旧/同行execute/import/rerun0，Lean0，没有扩辅助unit表。

## R7. Primary实际阅读与工具范围

[De Terán–Dopico作者原件](https://gauss.uc3m.es/fdopico/papers/LAA2009-polsing1storder.pdf)本地SHA
`c4637952f45e75c0fe34584502861e2b525a8c4c98f40697893e0fcf42f625f9`，18归档页；本审阅实际完整文本读取并逐页查看渲染的PDF1、4、7、14、15，共5页。原文local Smith、semisimple和generic complex perturbations的前提保留；它不证明实际有限域G_K单位或fixed α无限成功。

[Koekoek–Swarttouw作者报告](https://tudelft.roelofkoekoek.nl/documents/as98.pdf)本地SHA
`cca44bd484fabaada8b8e2b52700a319890edac9488f3026d54256e85b4ca23e`，170归档页；本审阅实际完整文本+渲染查看PDF29（印刷27），Eq1.2.2及三个M分支。只登记这一页，不声称全文读170页；cross的具体normality在R4逐因子独核。

本审阅新下载0。两份PDF分别是root本轮新增原件与旧已归档原件，不能把本审阅的6实际页重复计成新增PDF或188页全文阅读。web open可读文本，五张web截图请求因cache miss失败；随后本地pdfplumber文档阅读/渲染工具成功，六张PNG实际查看。文档阅读工具不是数学producer，未执行/import任何研究PY。scratch PNG不作为证明或新数学source。

## R8. Fixed specialization与本轮结论

每prime的至多k个失败source residues不保证同一个fixed rational α在无限prime成功。最终S5的一般反机制正确：枚举Q，坏集含前floor((p−1)/9)个分母为unit的reduced rational residues，每个固定有理数最终可被包含。它只说明density/degree界不足，并非构造本题actual坏集或证明fixed-source路线不可能。

已证：实际偶源第一高层响应、质量Gram斜率、完整cross实际fold、质量map单射、核精确重建、第一Schur residual、条件性whole-X常数非零及明确valuation。本轮safeA没有降低；单个辅助prime仍只产生O(nlogn)定标。

尚缺：实际G_K或另一条R0+pencil的算术正常性、fixed source在无限prime成功、无限original target非零与strict解析–算术margin。E单射、complete cross正常、per-prime好source数、无限fixed source成功和新特殊值定理均严格分开。本审阅通过最终10897数学内容，不宣布新ζ/L/Catalan无理性、线性无关性或Lean结论。

本文完整自读后冻结只读；没有新数学程序，没有修改任何old/peer proof、source、result或receipt。最终来源收据另NEW一向登记，不要求改本文或产生反向hash循环。
