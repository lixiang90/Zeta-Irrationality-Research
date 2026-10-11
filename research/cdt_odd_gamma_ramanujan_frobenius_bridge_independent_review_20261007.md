# Ramanujan–Cartier 桥接稿的最终完整独立审阅

2026-10-07，审阅者 /root/scaled_root_finalize。本轮唯一 NEW outgoing review。实际 FULL 读取最终主稿 research/cdt_odd_gamma_ramanujan_frobenius_bridge_20261007.md 的全部七节/F1–F24，物理 SHA a73af0926ab50c256462ceaffe9fc68459861b74bf8f4f6b5a1afa8a8ab462af，18032 bytes。此前候选64619、69742不作为最终pin。Authority为主记录§190及audit61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd；596旧记录只读，不执行/import/rerun数学producer、guards或prime表，不新建数学producer。

审阅结论：最终稿纸证通过，没有剩余修改请求。它严格建立原整数周期、指定四阶row、relative Cartier和所有正向完整block之间的身份，并没有证明该row的零性、更高reciprocal分母改善或新数值无理性。以下是实际逐式审阅范围，不继承作者的57页原件阅读或其网页检索证据。

## V1. 同一原归一化与真实第p系数

本轮实际 FULL 回读冻结Gamma G1–G19/七节、dual D1–D17/公式D1–D30/七节、reference H1–H20/七节。h_n、Λ、A、μ、N、P的全部符号与这些输入一致。Q=P(-X)是Wilson反转后的正向polynomial；正向argument为Λ/A=-3125/1024，不能删除反转负号或以发散实级数的普通求和替换有限sum。

H18的范围1≤k≤floor(p/5)及m=p项保留。p>31支付N和A单位；p²>5p使第p系数只需第p层carry。对m=p-k，h_p p⁹/((p-k)⁹h_(p-k))≡h_k；m=p贡献-30A，并与k0一起给Np⁹b_p≡-A S_p。除去高k的正p valuation后，F3正是same b_p的第一层，v_p(b_p)≥-8与S_p0等价。它不是all-n的Dn⁸定理；没有将同行新的whole-block预算提前作为输入。

F4可由五个central binomial和一个五项multinomial的multiplication formula直接核对。Λ=2¹⁰5⁵，参数共九个，coefficient denominator为(k!)⁹，绝不是rank5 Asai对象。

## V2. CT、完整Newton边界与Cartier surviving exponent

F5的五个x因子各有CT binom(2n,n)；四个y因子在(1+Σy)^(5n)中选每个指数n，得到(5n)!/(n!)⁵。变量独立，因此CT Φⁿ=h_n；形式t-adic身份F6成立而不要求t=μ处实级数收敛。

后因子Newton polytope为5·standard4-simplex−(1,1,1,1)，与五个[-1,1]作Cartesian product。其primitive normals距离原点均为1，dimension9、interior整点唯一0均准确。关键F8直接支付边界：p倍x坐标在[-p+1,p-1]中只能0；p倍y坐标各≥-p+1，只能非负，其和≤p-1则都0。未用“内点唯一”跳过boundary。

因为0∈Δ，Newt((1-tΦ)^(p-1))⊂(p-1)Δ；F8确使variable-only Cartier只留constant exponent。binom(p-1,k)(-1)^k=1 in Fp，故numerator准确H_p(t)，包括k0。没有借CY compactification或Tate class替代这一显式证明。

## V3. Fixed-t relative Cartier和准确specialization

所定义C_x只选择九个Laurent变量的p倍exponent，t保持固定，Fp[t]-linear；并非对t作Frobenius的绝对Cartier。拉出G(x^p;t)的规则成立。把denominator提升p次，得到1-t^pΦ(x^p)，因而输出分母准确1-t^pΦ(x)，F11无遗漏。

D=t∂t与variable-only选择commute，且D(t^p)=0 in Fp；因此四阶row的F12在有理函数和t-adic两种解释中一致。只有在μ∈Fp且μ^p=μ时才得到F13的1-μΦ分母。在一般参数或extension field上不可免费删去t^p或μ^p。Fp中这个非零rational denominator使S_p0与C_x R_mu=0严格等价，不依赖H_p(μ)非零或ordinary/unit-root假设。

## V4. 显式四阶row、pole例外及p-basis双向证书

以共同分母(1-s)⁵合并D0…D4：D0给30(1-s)^4，D1给425s(1-s)^3，D2给2275s(1+s)(1-s)^2，D3给5600s(1+4s+s²)(1-s)，D4给5532s(1+11s+11s²+s³)。五项合并的coefficients确为30、13712、74282、42932、1812。s1的numerator为24·5532；characteristic zero的pole5准确，5532=12·461使mod461 pole可下降。最终稿已明确此范围，F14本身及Cartier gate仍有效。

Fp(x1,…,x9) over Fp(x1^p,…,x9^p)的有限p-basis为x^e，0≤e_i<p。Euler derivative杀e0并将非零e_i作为单位乘其分量，所以F15⇒C_x R_mu=0。反向若C_x R_mu=0，则e0 coefficient为0；每个e≠0可选e_i≠0，向R_i分配e_i^-1 x^e G_e(x^p)，得到有限rational primitives。故在允许任意rational R_i的明确范围内，F15确与S_p0必要且充分。最终稿已补齐反向；额外低pole、integral lattice、all-prime lift等限制不由这个裸p-basis证明支付。

这只是等价certificate，尚未证明特定R_mu的e0分量为0，亦未构造该特殊row的primitives。其Cartier image仍为未知S_p/(1-μΦ)；不能把形式等价命题当完成目标。

## V5. Lucas与全部正向完整block的严格量词

对n=a+pb、0≤a<p，若5a<p，五项multinomial及central binomial最低位均无carry，Lucas给h_n≡h_a h_b；b可任意大。若5a≥p，五个最低位a相加已carry，multinomial两侧均0。p>5保证a<p中不会产生p²层，h_a valuation=5floor(2a/p)+floor(5a/p)，恰在a≤floor(p/5)为0，其他为正。这核准F16–F17及H_p的准确degree。

重排全部n=a+pb的Lp个terms，Q(a+pb)=Q(a)和μ^(a+pb)=μ^(a+b) modp，直接给F19的S_p T_L，任意L≥1有效。对长度p^e，递归Lucas给T_(p^(e-1))=H_p(μ)^(e-1)，F20成立，包括e1。H_p(μ)0使后续blocks消失不意味着首block S_p0。完整正向block的modp量词既不覆盖任意partialblock，也不等于reciprocal F2的all-prime-power分母，最终稿的scope限制必要且准确。

## V6. BCM最终v2的原件核读和全部适用假设

本人实际 FULL text读BCM1505.02900v2 PDF1–4四页：Definition1.1在PDF2，Theorem1.3/Assumption1.4与projective equations在PDF3，Theorem1.5在PDF4。初始split-character定义需(q-1)α_i、(q-1)β_j整数；defined-over-Q的Theorem1.3及其definition extension确覆盖char不整除common denominator的其它prime powers，不能把10|(q-1)保留为全版本限制。

F21 cyclotomic ratio准确，p-vector=(2^×5,5)、q-vector=(1^×15)的总和同为15，r6/s15/gcd1/M=2¹⁰5⁵。F22是原件projective模型，所有坐标非零，λ=μ；Theorem1.5要Mλ≠1、λ≠0及适当nonsingular completion，均显式保留。min(r-1,s-1)=5和(-1)^(r+s-1)=+1给F23的+q⁵ normalized Gauss-sum hypergeometric term。

1-Λμ=4149/1024=3²·461/2¹⁰准确。p461不得领取smooth-specialization/ordinary-point说法，但不影响纯coefficient的F5–F20；p3也不是point-count good parameter。F23的mathfrakH_q与整数H_p是不同定义。一个trace或Tate eigenvalue不足以确定指定四阶row与cycle的comparison，最终稿没有偷渡这个等同。

## V7. 文献状态的实际原件域

以下仅核实际已读版本的positive scope，不独立声称穷尽2026全部文献或重做作者网页metadata搜索：

- Cohen–Guillera2101.12592v1：实际PDF1、10、16–18共5页。abstract明示generalizations withoutproof；#21的Q、argument、upside-down P/N与原对象匹配；PDF17用“should have”给supercongruence模式，不能当rank9 modp⁹已证。
- Guillera2312.16827v1：实际PDF1–4共4页；PDF4明确Conjecture2.1，其Cor2.2依赖它。论文中嵌入Maple代码只作为原件文字读，没有执行。
- Guillera2312.16827v14：实际全文PDF1–9共9页；§4的formal regularization、π→p-adic L替换是heuristic，§5–6依此推出extended congruences，没有提供此rank9的独立严格证明。
- Dembelé–Panchishkin–Voight–Zudilin1906.07384v3：实际PDF1–4、9–13共9页；MainConj5.1的β=(1^×5)与Table5.2是rank5 experimental matching。PDF10–11的Asai transfer theorem虽是独立严格输入，却不把猜测matching变成已证rank9 CM/Tate4结论。
- Grove–Long–Rosen–Tu2607.25173v1：实际PDF1–4共4页；Theorems1.1–1.2的κ(d,e)length4、parameter1和指定d/e量词明确，不能代替当前length9、z0=-3125/1024的theorem。
- BCM最终v2：实际PDF1–4共4页，域见V6。历史BCMv1未在本审阅中读取，未混作final。Au endpoint身份按当前FULL读冻结dual/reference输入核，不冒称本审阅重新读Au原件；Greene同样未计新增页。

本审阅实际distinct primary PDF35页，全部从已有库读取，下载0/render0。第一次并行输出的总budget截断了Guillera后4页和Asai前5页，随后分别实际完整重新读这些页才计FULL，重复页不重复计数。本人own split稿另actualGM PDF1–3共3页、CDT v2 PDF66–69共4页，本轮个人合计42 distinct；这7页为own主稿域，不混作本审阅的35页。不继承作者57页或此前轮次页数，不把归档142页当阅读数。

## V8. 最终结论和证据范围

最终稿的F1–F24全部逐式纸核通过，F14 finite-characteristic pole范围与F15 p-basis反向均已在当前字节落实，没有剩余纠错请求。新证据提供exact CT/Cartier及完整正向modp blocks；它尚未给S_p0、modp⁹、partialreciprocal高层传递、Dn⁸/Dn⁵ cap或新ζ/L/Catalan无理性。作者所有网页查找和下载owner按其正文归属，本审阅不替代那些独立来源证据。

此review待实际FULL最终审阅者自读和物理SHA核后冻结；当前数学producer新建/execute/import/rerun、数学失败、prime扩表、Lean均0。旧596文件不修改，未来/root/peer receipt不作为本review的输入。
