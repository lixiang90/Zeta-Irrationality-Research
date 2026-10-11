# Level‑7 多项式相对扩张：正式独立全文审阅

日期：2026‑10‑07。审阅者：`/root/source_pencil_finalize`。作者：`/root`。结论：**PASS，最终候选无待修改项。**

本次实际 FULL 阅读最终 [主稿](cdt_odd_level7_polynomial_extension_classes_20261007.md) 八节／E1–E29，SHA `fc585a055e3b577a862f58202e24eda099394ae1b62e5f33393fb2b868690e7c`，17203bytes。此前1905dc版本也完整读过；作者已在唯一NEW稿澄清 rational-source arithmetic cap 的量词及 CDT 的准确公式号，随后审阅者对当前最终版本实际全文回读并核查。本文不审定未来修改版本。

## V1. 全 forcing 商与真实 rational splitting

E1/E4 的 Euler coefficient 与 ordinary coefficient分别为 `p=(1−t)²(1−28t)`、`p₂=t²p`，全篇计算没有混用。纸核 leading output `−14d(2d+1)t^(d+3)`、`L1=−2t−4t²`，从每个degree≥4逐次降阶给三维余项，而 `L1` 只去掉其中一维。`t−t²,t³` 与 `L1` 确实 independent；`L` 的 polynomial kernel 为0。因此 E6/E9 的所有degree existence/uniqueness都成立。

E8 不止是 polynomial ansatz：ordinary poles 的最高 derivative、finite singular points 的 negative integer indicial values共同排除全部 finite poles，使任意 rational splitting必为polynomial。对combination `a(t−t²)+bt³`，若degree(T)≥1，output degree≥4；若T constant，两项forcing比例不兼容。故 complex a,b也只有零combination split，rational coefficients 情形自然下降到Q。0处normalized analytic solution的 `n²` recurrence保证 E9 的第二等式。

## V2. 真对象的全 prime cap

实际 `t(q)=qV(q)`、`V∈1+qZ[[q]]` 给 `S=qt_q/t∈1+qZ[[q]]`。审阅者独立展开 `θ_q=Sθ_t` 的 chain rule：`LA=0` 消去E项，`L(Aτ)=0` 消去一阶 `θ_qE` 项，留下 `pAS⁻²θ_q²E`。所以 E11/E12 的 denominator 是Euler p，没有ordinary `t²`漏因子。

`p(t(q))`、`A(q)` 是integral units，integer R(t(q))有zero constant，故全部 `f_R∈qZ[[q]]`。两重 `q∂q` inverse给唯一分母 `n²`；与integer A相乘及integer q(t)复合在第n项只使用j≤n。由 `j²|D_n²`，所有primes/powers/n的 E13成立，固定θ-jets不加费用。Qforcing只需fixed M，绝非good-prime或机器抽样结论。E14的f₃=f t²/(1−t)与r_B normalization吻合。

最终§6已明确：actualrank3允许complex参数；`MD_n²` arithmetic cap仅对 `a,b,u∈Q`、`(a,b)≠0`。这一修订解决初稿的literal量词歧义，未改变任何rank或连接计算。

## V3. 无穷远 logarithm 与旧 field 逃逸

在z=1/t独立纸核 `z³L=(z−1)²[(z−28)ϑ²+14ϑ]−4z−2z²`。indicial为 `−28α²+14α`，所以 `Lhat(v₀ logz)` constant恰为 **+14**。`Lhat B₃=1`迫 E16 的 **+1/14**，转写logt时才变负号。减去此term后RHS无constant，所有integern≥1 indicial非零，得到收敛analytic particular；0、1/2齐次指数差非integer，无齐次log。

正向绕z=0两次增加4πi，故 `(T∞²−I)B₃=(2πi/7)v₀≠0`。旧B的RHS为z²−z，确无constant resonance，因此旧homogeneous matrix及B/B′的所有entries都被同一doubleloop固定。E17的field结论保留完整germ，不是某个leading coefficient近似。

μ=−1/28 ordinary，μ-loop固定B₃与旧field，独立地平移ℓ。若B₃是旧field上的rational function in ℓ，固定所有integertranslations迫该rationalfunction constantinℓ，再与E17矛盾。故 E18 排除的是完整 `E_B(ℓ)`，不只polynomial log ansatz。有限cover不能消去非零log亦正确。

## V4. actual joint rank5

对B₃的based∞doubleloop conjugates，homogeneous action为I，所以 conjugation中的affinecoboundaries确实消去；jump为 `(2πi/7)g v₀`。所有conjugates仍固定旧field。不可约V使这些vectors spanV，两个独立homogeneous solutions及非零Wronskian迫任意rowrelation里的B₃与θB₃系数同时为0。剩余旧B affinekernel为V、同一Wronskian迫其它三coefficients为0。

这里Kummer分类K12给旧B kernel的proof不依赖待审root新稿，故不存在证明循环。五个row的ordinary/Euler derivatives由同一rationalforcing系统闭合，actualfulljetrank恰为5。一般非零combination G的rank3来自E8非拆分及irreducible V；数值connection是否有rationalrelation不改变该函数rank。全文没有把这个statement冒充 `1,κ,C₃` 数值LI。

## V5. Fricke 与轴积分给完整 σ germ

审阅者核对eta inversion符号 `f(wτ)=i7^(3/2)τ³f(τ)`，以及invariantt derivative给 `S(wτ)=7τ²S(τ)`，由实际f=gS²/A推得 `A(wτ)=−i√7τ A(τ)`。f₃继承sameweight。imaginaryaxis的eta值正，AM–GM给 `0<t≤1/28`，`1−t`从不为0；两端cuspidaldecay加Fricke有限power支付C₃,D收敛，并给D=√7 C₃。

E23的orientation与−4π² normalization独立核查：`E_h''=−4π²h`，`E_h(iy)=4π²∫_y∞(v−y)h(iv)dv`。令Q=jE_h∘w−E_h，`2j'w'+jw''=0`，`j(w')²E_h''∘w=E_h''`，所以Q''=0。y→∞的两项分别确定linear coefficient与constant coefficient，精确为 `Q=C₃(j−1)`，不是只在fixedpoint取相等值。

该proof只需axis及其pole-freecontinuation neighbourhood，连接到τ_c；并未把meromorphich当作处处holomorphic去套Yang Lemma4，也未跨未经支付的interiormodularpoles。E24作为analyticidentity在该真实branch有效。τ_c处w的order2involution及t−σquadraticuniformizer使 E25 的 invariant analyticgerm下降成完整t-analyticgerm，故 E26全jump成立。E27从E9得aκ+bC₃−T0，符号正确。

正integrand与 `t²/(1−t)≤1/756` 给strict `0<C₃<κ/756`；t在两端趋0保证strictness。不允许由路径Mellin period直接称普通DirichletL(h,2)，最终稿明确保留这一点。没有C₃=log2或新irrationality结论。

## V6. CDT与primary范围

fresh实际FULL fixedCDT PDF66–69核对Theorem6.0.2的(6.0.4)、Remark6.0.11与Cor6.0.14。两列widths(0,1,1,1,1)给2(3+5+7+9)/25=48/25，三元组给16/9，都是安全upperbudget。主稿没有据此声称严格analyticmargin；新增∞log的真实puncture费用完整保留。

fresh实际FULL Brown–Fonseca v2 PDF1–4、41–43、49–50：Theorem8.4属于cuspcohomologyvanishingcase，Theorem8.6要求evenk=2m，odd k=1 的Rankin–Selberg比较在PDF49确为expected/conjectural。PDF50的mixedTateExt¹不自动让E5属于该category。root没有调用这些scope以外的定理证明C₃数值识别。

本轮审阅者actual primary域：Yang PDF5–10、15–16，共8页；CDT66–69，共4页；Brown–Fonseca1–4、41–43、49–50，共9页。因此本review直接primary21 distinct pages。另自己主稿的Singer13–14/19–20四页与Milne86/300/489–490四页也是本轮实际读域；与review overlap Yang四页后，**个人本轮union29页**（自己主稿阶段12页、reviewadditional17页）。没有继承root或其它agent的阅读。无render、新PDF下载、数学producer或prime/guard执行；仅documentaryPDFextraction与metadata。

## V7. 最终判定

最终fc585a候选的 E6/E8/E9、E13、E16–18、actualrank5、E22/E26/E27与E28均通过独立纸核。未完成项与正文一致：新周期C₃的特殊值识别、数值LI／irrationality、所有requiredleaf的strictCDTmargin、真正指定motiviccyclecomparison以及Lean结果仍未给出。原ξ数据未替换。review只确认本稿的实际定理及严格scope，不对这些未证部分作延伸。
