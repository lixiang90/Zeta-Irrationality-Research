# 第257轮唯一独审：同对象actual净检验与固定prototype结算

2026-10-10。审阅者为完成本轮B spectral稿的接替执行身份；本次独审对象是最终Root/A/C/report及四scope，**不以作者自审B冒充独立数学审核**。B数学稿已由Root在独立身份实际全文读并逐式核对，边界见下。收到Root最终冻结通知后，本身份重新逐份实际FULL读取八个指定文档，各工具输出无截断，再实际核bytes/hash。只新增本轮这一份唯一独审；不改任何冻结稿、main、policy或manifest，不运行归档。

**结论PASS：** 最终Root/A/C的完整数学链与report的有限范围结算一致，未发现需修正文稿的数学或净账错误。PASS是对这些证明、量词和投入边界的审查通过；没有新数值ζ/L无理性或线性无关性定理，没有actual无界非零、负二次净证书或Lean认证。当前默认monomial prototype停止投入，原数值目标保持active。

## 1. 当前实际FULL读取及最终身份

下表的Root/A/C/report与四scopes均在本次审读重新用独立 `Get-Content -Raw` 调用全文读取。随后实际bytes/hash与最终冻结通知及Root scope一致；hash未代替正文数学审读。

| 本次FULL读取文档 | Bytes | SHA256 |
|---|---:|---|
| `research/chi8_native_net_settlement_round257_20261010.md` | 7380 | `F1DF999F649203059585C429BC14E99837DE1158C0CB952CCA80B0C2818CDC5A` |
| `research/chi8_native_actual_energy_round257_20261010.md` | 9441 | `E3046B5A27631809923C05C4C9D72DF832E918B1293BC023930F303AB181DACE` |
| `research/chi8_native_primitive_feasibility_round257_20261010.md` | 12010 | `14650A9261A6940CED84E2A7AC847617E6CF18D18F463A1DC01C9F50C2A9317E` |
| `research/research_native_chi8_progress_round257_20261010.md` | 6272 | `03F510D7CEE51B40807AFD1F3950FFBECC4719AE25E9196248C95DEA827CD27E` |
| `literature/native_chi8_sources_round257_20261010/root_reading_scope.md` | 5359 | `6E119E199A0C1EE58C412F9CF4DEF6E258953E9FA5971BD40367962905A8CEF8` |
| `literature/native_chi8_sources_round257_20261010/contour_reading_scope.md` | 3370 | `1D87451045A759D79E7A2CDA99168A33BA1E4FF7EDCC1AB8DCF0B136AB758E96` |
| `literature/native_chi8_sources_round257_20261010/integer_reading_scope.md` | 2810 | `71D142B03B4E81F2A339C2BDB017FF943DA970D82B1BC9E25701525CD97F45FC` |
| `literature/native_chi8_sources_round257_20261010/spectral_reading_scope.md` | 4558 | `3C4F94A4EBDA677A71F150BA2F713132D0AF65E69254FF7D2D624F9E4B4A8252` |

B最终数学稿 `research/chi8_native_spectral_feasibility_round257_20261010.md` 的当前身份另经实际hash核对：12889 bytes / `B6375DC5F2D4BD33F08F4E5FC6083425C44EA49CC2F34F3CBD2F5F182861ED75`。该项仅为文件身份收据，不记为本次独审者对自己稿件的独立审核。先前作者全文复读与本次八份最终审读是不同事件。

## 2. A实际解析链：PASS

独核实际theta核的 `π/4..3π/4` 差：θ与π−θ的cos项抵消，线性θ项合成−2π。固定小双芽域中，`sinθ≥a`让全部i,j同时绝对展开；`x=a/sinθ`把jump精确变为 `4π∫_a^1 x^{i−j}/√(2x²−1)dx`。这与完整256实际Y继续匹配，未自由更换start。旧偶次折叠的系数16正确；ordinary Z保留整个D截断，而非删除rational heads。

O/J/Z三标签测度和行、列函数均与完整T_n=2^(−n)F_n匹配。O质量≤16；J质量 `2√2πlog(1+√2)`；Z质量 `3π²/2`，角点核可积。固定M确为总质量安全upper。每个n的函数有界、测度有限，所以有限Leibniz展开和绝对Fubini支付完整Andreief。J-only的逆序Vandermonde符号 `(-1)^(n(n−1)/2)`准确，未被误当完整det非零。

列monic Chebyshev的sup因子是 `2^(1−s)`，乘积给 `n^(n/2)2^(n−1−n(n−1)/2)`。Z行完整高度 `2^(n−r)`经Leibniz给 `n!2^(n(n+1)/2)`；与Andreief的n!精确抵消，两个二次项也恰抵消，得到

\[
|2^{-n^2}\Delta_n(Y)|\le M^n n^{n/2}2^{2n-1}.
\tag{V1}
\]

还原Δ的2^(n²)没有遗漏。A最终稿只用它实际FULL读过的256旧整数证书做初步费用比较，并明示新scalar替换接口；它没有假称未读257 C已由自己证明。Root本轮实际读C后执行新费用合并，读域边界一致。

## 3. C全prefix及whole-polynomial内容链：PASS

独核完整forcing生成式：(C/A)'中的两个8z边界项正确抵消，得 `8 arcsin(az)/(az(1−z))`。积分与A卷积给原minus rational head的双重binomial有限和；每项的两个divisors均≤d，dyadic指数满足l+h≤floor((d−1)/2)，所以P10覆盖原完整头，而非缩放后的别的对象。

plus-even递推乘l b_l后正确望远镜。其每个prime-power层是 `δ_h−δ_l−[p^e|l]−[p^e|2h+1]`；若p^e|l，则δ_l=0，故每层至少−2。plus-odd的层是 `δ_l−δ_h−2[p^e|h]`；p^e|h时δ_h=0，也至少−2。所有较大prime powers层为0；额外odd dyadic factor已由2^l付清。论证包括2，没有以样本或未付numerator信用替代全尺度证明。

finite μ heads的factorial层至多1，再加一个divisor层，完整diagonal sums由d_(H+1)²覆盖；Y/ζ(2)系数的全部dyadic指数也覆盖。ordinary Z完整heads清整，H=0由starts单独覆盖。用π²单独记未乘9的ordinary Z时需固定3的边界准确；N和contact后9Z已覆盖，不影响本轮F整数模型。

冻结P/D每行已知integer content h_r=2^(r+1)只扣一次，H=2n−1覆盖全部degrees和raw columns，任意integer filters仍在完整输入池内。因此

\[
\widetilde q_H=2^{3\lfloor H/2\rfloor+1}d_{H+1}^2,
\qquad
\frac{\widetilde q_{2n-1}^n}{\kappa_n}\Delta_{n,E}\in\mathbb Z[T]
\tag{V2}
\]

完整成立。旧新q的exact ratio `2^(n+1)d_(2n)`给旧模型全部coefficients的真正共同因子 `[2^(n+1)d_(2n)]^n`；未宣称其为最大primitive content。κ没有因另一native尺度被二次扣除。P26旧height是其明示冻结256输入的保留接口，本次新净结算使用actual(V1)，不依靠P26领取新增能量。

leading费用加上 `(n²+4n)log2` 后为

\[
\log\ell_n\le2n\psi(2n)+
\left(\frac72n^2+\frac32n\right)\log2.
\tag{V3}
\]

它是安全upper，非最大content、费用lower或实际strict。标准PNT仅为已明示的比较标尺，exact清整、whole-content和O(H)证书不依赖PNT或数学程序。

## 4. Root同对象净账及B独立审核边界：PASS

独核Root R1–R8的实际对象、量词与scalar。新qtilde^n/κ乘(V1)必须先还原2^(n²)，所得exact合并式为

\[
\log|\Pi_n(Y)|\le
2n\psi(2n)+\left(\frac72n^2-\frac12n-1\right)\log2
+n\log M+\frac n2\log n.
\tag{V4}
\]

最终Root R7的加号完整，非零与log0边界正确。等价谱积upper是 `M^n n^(n/2)2^(−2n−1)`，与(V3)正好回到(V4)，没有漏16^n或2^(n²)。沿标准PNT标尺，合并安全upper的leading为 `4+(7/2)log2>0`；这份upper不能给有理假设下的矛盾，却也不能当实际lower或一般no-go。若Y=u/v有理，非零条件仍是使用v^(−n) lower的必要前提。

Root R9的unit upper Toeplitz及inverse sqrt(1−2z)系数正确；central binomial除2l−1等于两倍Catalan整数，故inverse只有dyadic分母。这个有理row变换不改变primitiveΠ_n，也不提供额外免费内容。

B核心数学不由本次作者自审认证。Root最终scope及冻结通知记录了真正独立核对：B5同node底minor；B6全n合流mixed反例；cross-label内部邻域无全node Vandermonde；B9有理rank-one修改；B12完整bordered-adjugate无需可逆；B13/B15 Schur complement和B14的 **+9E_A** 符号；polynomial延拓到singular A及n=1边界；B22净账。Root实际FULL读的B身份就是第1节给定12889/hash，并已PASS。本独审确认Root/report对这些资产的引用和限制与该独立收据一致，不把这个确认转称本身份独立审核B证明。

因此formal目标满秩、pure J非零、pure sector容量、普通principal-minor链与generic free-start结果都没有被外借成actual∞nonzero。完整mixed terms的取消及actual谱积strict仍未证明，Root/report没有越过这些边界。

## 5. report、停止范围和下一258准入：PASS

report完整报告了两项真实新进展：actual全部数组/全n upper，以及原完整integer model的宏观内容改善。它也准确报告尚缺actual无界非零及负二次净界。当前默认monomial prototype按256的一次257准入窗口停止；保留carrier、整数和谱资产，不自动延至prime/Frobenius/参数/maps/sheetwords或换向量。停止一个实现的投入不是全部χ₋₈方法不可能，原数值ζ/L目标仍active。

下一258明确是**有界跨架构来源准入**：假设数值关系须在完整最小函数族中消掉整个非meromorphic local monodromy，并产生可量化共同解析域增益，同时支付真实period投影、函数独立性与全prefix费用。只消掉一个本已允许的meromorphic极点、增加jets/germs，或由函数代数独立直接推数值线性无关，均不准入。不同cyclotomic多源机制只是待核来源，未声明已成功；若准入失败，否决相应来源选择。本次不提前构造新Padé或参数实例，也不把抽象引理重新定义成总目标成功。

正式clock一致：**last256；257完成后计数1；下一正式260；最迟264；连续2轮核心停滞提前回顾。** 无新数值定理或Lean认证。旧spectral身份中断及新身份接替的事实、没有继承失败者FULL标签的边界，在report与四scope相符。

## 6. 独审与归档边界

本身份本次只实际读最终四正文与四scope，核这八份及B的文件身份，保存本唯一独审并最终全文复读/hash。四scope的作者历史阅读、旧pins与primary审计没有继承成本身份执行记录。Root记录的256 manifest 100/100 pin核验属于Root；本独审没有据此冒称已重新独立核全旧档。

本次数学程序、finite-n/CAS/interval/prime/参数/map/word扫描、Lean、web/primary GET/PDF/HTML下载、外Git写及旧producer运行均0。没有全球novelty或全部primary全文认证声明。文档hash、存在性读取与证明的符号审读不列作数学程序。

冻结稿、main、policy、manifest未改；本身份未运行archive。本唯一独审PASS后由Root执行本轮单次documentary归档，再以另行通知授权本身份一次只读postarchive核验。该核验尚未执行，不能预记结果；旧bytes和main/policy前缀的归档保留仍待实际工具收据。唯一独审最终保存后全文复读，外部工具提供本文件bytes/hash，避免自引用。
