# 非临界椭圆 Cauchy 载体的独立全文审阅

2026-10-07。Reviewer：/root/scaled_root_finalize；作者：/root/masked_racah_finalize。指定本轮唯一正式审稿对象：

- research/cdt_odd_noncritical_elliptic_cauchy_carrier_20261007.md
- SHA2ee738d49bfe91a9456a28caf85f6aa466008079786d3f8b4397417b45614ac9；16238bytes
- 本人 actual FULL 全部八节、E1–E25，physical SHA/bytes核验与逐式纸核；不是依据作者摘要给PASS。

结论：**PASS，无正文修改请求。** 核准的是本文明确构造的 native complete-log mechanism、全primes模型、sharp prefix leading2/3、actualrank4/5及保守CDT upper费用。没有核准任何新的数值无理性，也没有将nativefill扩成所有transported μ-lifts或所有maps可填。以下给具体复核证据。

## 1. V1：实际 L-value 目标、整数坐标与原件范围

本轮review新actualFULL原件Koutschan–Zudilin，Apéry limits for elliptic L-values，arXiv2111.08796v1，PDF1–6全部text；路径 literature/cdt_gamma_noncritical_elliptic_sources_20261007/koutschan_zudilin2021_apery_elliptic_l_values_arxiv2111_08796v1.pdf，SHA8f55e4b6b8bd772ee83b5d4638af06e8af17b75e8907c49fa307434d9a515ad7，126817bytes，6物理页。PDF2–3给 \(\lambda=2\pi\,{}_3F_2\)、\(\rho_1=\pi\,{}_2F_1\)，PDF5给 \(\lambda(1/16)=30L(E,2)/\pi\)、\(\rho_1(1/16)=L(E,\chi_{-4},1)/2\)。因此 \(r=Y/F=\lambda/(2\rho_1)\) 的factor准确为
\[
 r=\frac{30L(E,2)}{\pi L(E,\chi_{-4},1)} .
\]
作者没有把centralperiod或π降为Q，没有把单一L(E,2)当同一目标。PDF3–4两组denominator arrays明确experimental，审稿没有用它们证明本文E20–E23。

独立web检查canonical15.a7/7及Cremona15a8 URLs均返回browserchallenge，不能冒称本人重读了作者那份curvepage。随后primary [LMFDB ec_curvedata API](https://www.lmfdb.org/api/ec_curvedata/)的search返回明确15.a7 record，实际可见字段为Clabel15a8、conductor15、ainvs[1,1,1,0,0]、jinv[-1,15]、cm0。这核对了主稿的label/model/nonCM字段；不执行任何Sage/Pari snippets、不使用BSD字段。对无理性的检索状态仅按“作者本轮未找到”理解，本人没有进行穷尽文献检索，不将它升级为通用未知性定理。

\(z=16t\) 后 \(F=\sum\binom{2n}{n}^2t^n\)，\(Y=\sum b_nt^n/(2n+1)\)准确；evaluation point \(\mu=1/256\)、Gauss singularity \(\sigma=1/16\)同时随scale支付。E5–E7的ODE、matrix和Euler integrals由这些实际coefficients手核一致。

## 2. V2：complete native logarithm 与 meromorphic pole 的区别

在ordinaryμ，\(H_u=Y-uF\)analytic。写
\[
 \frac{H_u(t)}{t-\mu}
 =\frac{H_u(\mu)}{t-\mu}
   +\frac{H_u(t)-H_u(\mu)}{t-\mu}.
\]
第二项整个analytic，所以primitive为
\(H_u(\mu)\log(t-\mu)+\text{analytic}\)。因此E11的jump为整个constant germ \(2\pi iH_u(\mu)\)，没有variablehigherlog残项。u=r时ordinarypole和nativewholelog全部消失；正θjets全analytic。

反之D_u的simplepole在所有u下已meromorphic，CDT本来允许meromorphicpullbacks。这一polefill不能单独提供关系触发的新leaf。作者明确只让带真实integralcost的C_u承担该机制，scope正确。E10由positivecoefficients给0<r<1，亦准确。

## 3. V3：原rank4、三阶cyclicity及rank5的真实来源

Gauss在0、σ的两个非平凡unipotents有不同fixedlines。σjump把F送到非零的σ-fixed solution；再作0jump给非零f0 direction，orbit differences张成二维space。一个relation \(RF+SG+T=0\)差分对两独立solutions给nonzeroWronskian，迫R=S=T=0。没有以order2替代rank证明。

∞ repeated-half exponents给 \(F=t^{-1/2}(A(t^{-1})\log t+B(t^{-1}))\)，其 \(A(0)\ne0\) 可由负实Eulerintegral的 \(R^{-1/2}\log R\) leading直接确认。由 \((2\theta+1)Y=F\)，写Y=t^{-1/2}V，得到 \(2\theta V=A\log t+B\)。j0resonance给 \(A(0)\log^2t/4\)，j≥1的nonzero−j eigenvalues只给一次log。Rational coefficients乘F/G/1不能抵消Y的nonzero二次log；rank4成立。

本人手算E14 determinant：
\[
 \det\mathcal R_u
 =\frac14-\frac u2(1+a)
   +u^2\left(\frac14+\frac a2-b\right)
 =\frac{(1-u)^2-16t}{4(1-16t)} ,
\]
其中a=16t/(1−16t)、b=a/4。它对任何constantu都非零rationalfunction，因此H_u及0/1/2θjets恰span(Y,F,G)，乘 \((t-\mu)^{-1}\) 的triangulargauge不改functionfieldrank。没有把gauge无偿改成整basis。

C_u若在span\(_{\mathbf C(t)}\)(1,Y,F,G)内，则其每条continuedbranch在ordinaryμ仅可meromorphic。V4的actualtransportedlog反驳此事；所以加C有rank5。又θC=tH/(t−μ)，θ/θ²/θ³C到H/θH/θ²H的lowertriangulartransformation对角均nonzero，E16的实际五行rank确为5。E17给explicitrationaloperator/connection，未冒充原GaussL2的rationalinhomogeneousforcing或未构造cycle。

## 4. V4：无穷远的完整二次差分与搬运 access

令S=T∞²，保持指定∞access。\(t^{-1/2}\) sign恢复、logt增±4πi。所有j≥1terms至多一次log，其二阶finite-difference为0，唯j0doublelog贡献
\[
 (S-I)^2H_u
  =2(\pm4\pi i)^2\frac{A(0)}4t^{-1/2}
  =-8\pi^2A(0)t^{-1/2}\ne0 .
\]
这在∞是收敛展开的完整identity，不只是leadingasymptotic；沿ordinarypaths搬回μ，右边仍非零。因此H_u、SH_u、S²H_u在μ不能同时取0。nativefill时后二者至少一条仍nonzero，C相应branch有完整log。这足以证明V3的rank5。

没有由此宣称每条μlift都bad，也没有宣称每个admissiblemap必omitbaseμ。E15的三个具体transportedbranches及其至少一个residual范围准确。nativeσ处F含order0log，Y的E5integral含nonzeroslog；u≠0时H带order0log、C带slog，u0时C带s²log。故作者对native rounddisc Rz限制R≤1/16正确，但不把它推广为所有maps的no-go。

## 5. V5：全prime prefix 分母精确 leading2

对odd p^e≤2N+1，j=(p^e−1)/2的p-digits都为(p−1)/2，Lucas给
\(\binom{p^e-1}{(p^e-1)/2}\not\equiv0\pmod p\)，所以Y_j有valuation−e。全部j≤N的odd denominators又整除D_(2N+1)的oddpart，故Y的最小prefixdenominator准确为该oddpart；leading2由PNT获得。

对p∤2M，乘(t−μ)和geometricinverse的finiteprefixcoefficientmatrices均Z_p-integral，其diagonal−μ及−1/μ均unit。uF在该p整，所以Y、H、D的prefixnegativevaluationmin相同。有限p|2M至多O(logN)，E20upper同时支付。故E21是matchinglower/upper的2N+o(N)，不是作者原件experimental数组的移植。

E18/E19逐项geometric/primitivecoefficients手核正确。M D_(2n+1)支付D_jets；M n D_(2n−1)支付C_n，prefix M D_ND_(2N−1)支付所有n≤N；正θjets的n multiplier消去primitive n分母。所有primepowers含2和inputprimes都在upper模型中，不仅odd-primes first layer。

## 6. V6：sharp leading3 的两条全odd-prime lower

设odd p∤M，j*=(p−1)/2。Lucas给 \(b_{j*}\equiv1\pmod p\)（centralbinomial的符号被平方）。在n=p与n=(p+1)/2，summationrange内唯一含p分母的2j+1就是j*，且power仅为p。其余summands在相应缩放下全消失。手算给
\[
 p^2c_p\equiv-256^{(p+1)/2}b_{j*}
   \equiv-256\pmod p,
\]
\[
 pc_{(p+1)/2}
   \equiv-\frac{256b_{j*}}{(p+1)/2}
   \equiv-512\pmod p .
\]
256是2的偶次幂，故Euler的 \(256^{(p-1)/2}\equiv1\) 对每个oddp成立。两个residues均unit，valuation准确−2/−1，不靠prime样本。

在prefix≤N，p≤N可用indexp，N<p≤2N−1可用index(p+1)/2。去掉固定有限exceptions仍给Chebyshevprime-sum lower
\(\vartheta(N)+\vartheta(2N-1)=3N+o(N)\)。prefix upper是logD_N+logD_(2N−1)加fixedM，同leading3。E23因此是sharpleading，且仅针对该coordinate/fixedu的coefficientprefix；不推每个primepowerupper等号、normalizedmodel或任意finite-minorbudget。

## 7. V7：whole-array CDT 费用及未闭合的 strict margin

本人本轮 actualFULL CDT PDF66–69已在ownmain阅读，review同页复用，不doublecount。E20的D_(2n±1)对应一个b2列的fixedshift，依Remark6.0.12支付。E16排序(1,θC,θ²C,θ³C,C)给m5、b=(0,2,2,2,2)、e=(0,0,0,0,1)，flat=2(1−1/25)=48/25。

在ξ=5/2，Definition6.0.1的三积分分别0、3/2、1/2。第二项的harmonicfloor仅在t≥7/2取1；第三项仅在[5/2,7/2]给t−5/2，其integral1/2。故I=2，sharpcandidate为 \(2(5/2+2)/25=9/25\)，得到safeupper57/25。没有核准这是globalminimum；D三jetsm4的flat15/8也准确，但D没有新增meromorphicleaf。native rounddisc的σ限制使该检查对象无strictmargin，未扩大成任意maps不能成功。

审稿接受的新carrier是一份 actual低rank数值目标接口，不是已证明的目标无理性。新的allowedleaf、holonomy优化、cycle/integralBetti标记与更低费用等均保留为未证条件；未免费套Schneider、Mahlermeasureidentity或weakApérylimit。

## 8. V8：actual read domains 与冻结范围

本人本轮该正式review实际FULL 2ee738主稿八节/E1–E25，freshFULL KZ PDF1–6；所用CDTv2 PDF66–69已本轮actualFULL读，不继承以前阅读。reviewprimary页域为10distinct（KZ6+CDT4），其中仅KZ6为相对ownmain新增；ownmainGM1–3+CDT66–69共7，两域合并本轮个人13distinctPDF页。没有读取Brown–Fonseca69页，因为该carrier没有使用它，不继承root/同行的页数。

本review未下载、render、启动数学producer或数学计算；没有执行creative-telescoping软件、任何旧/同行producer、guard、prime或Lean。实际web范围是browserchallenge记录与上述primaryAPIreturnedrecord，不冒称完整LMFDBcurvepage重读。所有数学复核为纸面恒等式/valuation/秩论证，不将JSON/hash documentarychecks称作数学认证。

最终本review actualFULL自读和physicalSHA确认后交作者收审；作者最后FULL回读原main再生成其单向receipt。本文只pin实际main/已有primary/authority，未pin未来audit或同行receipt；没有修改612旧记录或原件。除实质纠错外本review保持最终字节。
