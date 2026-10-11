# 精确 Ramanujan 四阶 jet 与原九阶周期的 Cartier 桥接

2026-10-07，作者 /root/masked_racah_finalize。本轮唯一 NEW 纸面主稿。Authority 为总记录 §190 与 `cdt_odd_delivery_relative_lift_tensor_reference_20261007.json`，SHA `61dc2465b76159ce315f083848266b6e8415543a63903b004cf944440e75c5cd`；596 冻结记录（591 数学、5 guards）只读。本轮未创建、执行、import 或重跑任何数学 producer，未运行或扩充素数表。本稿不证明新的数值无理性；建立一个准确的有限域算术入口，并核清已检索 primary 的实际证明范围。

## 1. 精确保留 polynomial、坐标与实际 reciprocal coefficient

本轮实际全文回读冻结 [Gamma G1–G19](cdt_odd_gamma_connection_projection_20261007.md)、[dual D1–D30](cdt_odd_gamma_dual_relation_extension_20261007.md) 与 [reference H1–H20](cdt_odd_gamma_lift_holonomy_reference_gate_20261007.md)。保留

\[
h_n=\binom{2n}{n}^{5}\binom{5n}{n,n,n,n,n},\quad
\Lambda=2^{10}5^5,
\quad A=-2^{20},\quad\mu=A^{-1},\quad N=380928,
\]
\[
P(X)=5532X^4-5600X^3+2275X^2-425X+30,
\quad Q(X):=P(-X)=5532X^4+5600X^3+2275X^2+425X+30.
\tag{F1}
\]

实际 lift 系数仍为

\[
b_n=-\frac{h_n}{N}\sum_{m=1}^{n}\frac{P(m)A^m}{m^9h_m}.
\tag{F2}
\]

冻结 H18–H20 已纸证，对 prime p>31 有

\[
Np^9b_p\equiv-A S_p\pmod p,
\quad S_p:=\sum_{k=0}^{p-1}Q(k)h_k\mu^k\in\mathbb Z_p,
\]
\[
S_p\equiv0\pmod p\quad\Longleftrightarrow\quad v_p(b_p)\ge-8.
\tag{F3}
\]

以下不是把 P 的负号删掉；Q 是 Wilson 反转后准确的正向 polynomial。未缩放 hypergeometric 坐标 z=Λt 给

\[
h_k\mu^k=\frac{(1/2)_k^5(1/5)_k(2/5)_k(3/5)_k(4/5)_k}{(k!)^9}z_0^k,
\quad z_0=\Lambda\mu=-\frac{5^5}{2^{10}}.
\tag{F4}
\]

这是 Guillera1908.05123v1 Table5第三项，以及 Cohen–Guillera2101.12592v1 的 divergent table #21。同一组未截断实级数 ratio 的绝对值为3125/1024>1；这里只使用有限 sum，或另外明确给出的解析延拓，不以发散 series 作普通求和。

## 2. 原整数周期的具体常数项模型及唯一内点

**F4（准确的九变量 Laurent polynomial）。** 取独立变量 x1,…,x5、y1,…,y4，定义

\[
\Phi(x,y)=\prod_{i=1}^{5}(x_i+2+x_i^{-1})\,
 \frac{(1+y_1+y_2+y_3+y_4)^5}{y_1y_2y_3y_4},
\quad f(t,x,y)=1-t\Phi(x,y).
\tag{F5}
\]

令 CT 为九变量的零指数系数。由于

\[
\operatorname{CT}_x(x+2+x^{-1})^n
=\operatorname{CT}_x x^{-n}(1+x)^{2n}=\binom{2n}{n},
\]

而后四变量常数项是在 `(1+Σy)^(5n)` 中各 y 指数恰 n 的 multinomial coefficient，故逐 n 准确

\[
\boxed{\operatorname{CT}\Phi^n=h_n,\qquad
\operatorname{CT}\frac1{1-t\Phi}=f_0(t)=\sum_{n\ge0}h_nt^n.}
\tag{F6}
\]

第二式是 Q[[t]] 中的形式身份，不需在 μ 数值求和。它保留原整数 t 坐标和全部 normalization。

**F5（明确的 Newton polytope）。** Φ 的 Newton polytope 为

\[
\Delta=[-1,1]^5\times\{(v_1,\ldots,v_4):v_i\ge-1,\ \sum_i v_i\le1\}.
\tag{F7}
\]

后因子是 `5·standard 4-simplex−(1,1,1,1)`。内部整点的 x 坐标必须为0，y 坐标满足 v_i≥0、Σv_i≤0，也全部为0。各 facet 的 primitive integral normal 与原点距离均为1；因此 Δ 为 dimension9 的 reflexive polytope，唯一 interior lattice point 是0。

更直接、对以下证明真正够用的是，对每个 prime p，

\[
\boxed{(p-1)\Delta\cap p\mathbb Z^9=\{0\}.}
\tag{F8}
\]

若 p倍整点落入其中，x坐标由 |x_i|≤p−1得0；每个 y_i≥−(p−1) 强制其 p倍整数坐标非负，而 Σy_i≤p−1 强制其和为0。此证包含边界，不误用“内点唯一”去跳过边界。

F7 只给这个显式 toric period 的 polytope。`f=0` 在九维 torus 中的 nominal dimension 为8；本稿没有证明一个光滑、nondegenerate 或指定 integral-model 的 CY8 compactification，更没有由 reflexivity 推出 μ 处存在中间 Tate class。

## 3. 精确四阶 Cartier image，而非只给一个点数迹

固定 prime p>5，在 Fp[t] 上对 **九个 Φ 变量** 定义 relative coefficient-selection operator

\[
\mathcal C_x\Bigl(\sum_{v\in\mathbb Z^9}a_v(t)x^v\Bigr)
 :=\sum_{v\in p\mathbb Z^9}a_v(t)x^{v/p}.
\tag{F9}
\]

这里 x 合并表示全部 x、y 变量；t 保持 fixed parameter，\(\mathcal C_x\) 是 Fp[t]-linear，并未对 t 作 Frobenius。对 Laurent polynomials 有

\[
\mathcal C_x\{G(x^p;t)U(x;t)\}=G(x;t)\mathcal C_xU(x;t).
\]

对本文 rational fractions，先把 denominator 提成 p次方，再用此式定义其 extension；也可在 t-adic formal series 中逐项作用。两种定义在以下 rational identity 中一致。

**F6（polynomial numerator 的唯一 surviving exponent）。** 令

\[
H_p(t):=\sum_{k=0}^{p-1}h_kt^k\in\mathbb F_p[t].
\]

由 F8、`Newt(f^(p−1))⊂(p−1)Δ`，且 binomial(p−1,k)(−1)^k≡1，有

\[
\mathcal C_x f^{p-1}=\operatorname{CT}f^{p-1}=H_p(t).
\tag{F10}
\]

又 `f(t,x)^p=1−t^p Φ(x^p)`，因此

\[
\boxed{\mathcal C_x\frac1{1-t\Phi(x)}
=\frac{H_p(t)}{1-t^p\Phi(x)}.}
\tag{F11}
\]

这是 explicit rational/formal identity，不用 unit-root、ordinary reduction 或假定某个 Hasse invariant 非零。Fp 上 D=t∂t 与本 relative operator commute；输出 denominator 只含 t^p，故被 D 杀掉。于是对任一 polynomial R∈Fp[X]，

\[
\boxed{\mathcal C_x\left(R(D)\frac1{1-t\Phi}\right)
=\frac{R(D)H_p(t)}{1-t^p\Phi}.}
\tag{F12}
\]

**F7（真正 special μ 的 weighted Cartier gate）。** p>5 时 μ∈Fp^×；只有此时利用 μ^p=μ，把 F12 specialized 成

\[
\boxed{\mathcal C_x\left(\left.Q(D)\frac1{1-t\Phi}\right|_{t=\mu}\right)
=\frac{S_p}{1-\mu\Phi}.}
\tag{F13}
\]

分母是非零 rational function，故 `S_p=0` 准确等价于左侧 Cartier image 为0。若参数保持一般 t，输出是 `1−t^pΦ`，不可写成 `1−tΦ`；若 t 在 extension finite field 中，亦须保留 μ^p，不能借本 Fp-specialization 免费消去。

为使待证输入能直接核验，设 s=μΦ，四次 Euler derivatives 展开给

\[
\left.Q(D)\frac1{1-t\Phi}\right|_{t=\mu}
=\frac{30+13712s+74282s^2+42932s^3+1812s^4}{(1-s)^5}
=:\mathscr R_\mu(x).
\tag{F14}
\]

例如 D4(1−s)^−1=s(1+11s+11s²+s³)/(1−s)^5，其他 D0…D3 用相同 denominator 合并，给上述全部五个 coefficients。这里 characteristic zero 的 pole order 恰5，因为分子在 s=1 的值为24·5532；mod p 的 pole order 可以下降，例如 p461，F14 身份与 Cartier gate 不变。四阶 Q(D) 始终保持原对象，不以 unweighted H_p(μ) 替换它。

F13 对应九变量 logarithmic top form `Ω=∧dlog x_i∧dlog y_j` 的 relative Cartier coefficient。一个 **尚未提供** 的 finite-place certificate 是，在 Fp(x,y) 中实际写出 rational functions R1,…,R9，使

\[
\mathscr R_\mu(x)=\sum_{i=1}^{9}x_i\partial_{x_i}R_i(x).
\tag{F15}
\]

此处仍以 x_i 合并九变量。对 rational functions 也有严格的 p-basis 证明：Fp(x1,…,x9) 在 Fp(x1^p,…,x9^p) 上以 x^e（0≤e_i<p）为基。写 R_i=Σ_e x^e G_e(x^p)，则 x_i∂_iR_i=Σ_e e_i x^eG_e(x^p)；relative Cartier 只保留 e=0 的分量，该分量的 e_i 为0。因此它杀掉该 exact logarithmic top form，F13 给 S_p=0。这不依赖选择多变量 Laurent 展开的收敛区域。

反向也准确成立：若 rational function 的 Cartier image 为0，其 p-basis 的 e=0 分量为0。对每个 e≠0 项 x^eG_e(x^p)，选一个 e_i≠0，把 e_i^−1x^eG_e(x^p) 加入 R_i；其 logarithmic derivative 恰恢复该项。有限 p-basis 项给 rational R_i。因此在这里允许任意 rational R_i 的范围内，F15 与 S_p0 **等价**。本稿没有求出这些 R_i，也没有证明目标四阶 row 的 e=0 分量为0；这个具体待证分量仍正是 S_p/(1−μΦ)。若另要求 R_i 具有统一低 pole order、特定 integral lattice 或全 prime geometric lift，须另付这些限制。更广泛的 crystalline/relative-cycle route 也必须实际证明 F13 的零 image，或给出控制其四阶 jet 的完整 integral comparison；只出现一个 p4 Tate eigenvalue 不提供此项。

## 4. 全 prime Lucas 与所有完整正向 blocks 的严格传递

**F8（所有 prime p>5 的 exact digit congruence）。** 对 0≤a<p、b≥0，

\[
\boxed{h_{a+pb}\equiv h_a h_b\pmod p.}
\tag{F16}
\]

若 5a<p，最低位的 binomial(2n,n) 与 multinomial(5n;n^5) 均无 carry；Lucas 给各自最低位因子乘 b 的对应 coefficient。此时 2a<p 自动成立。若 5a≥p，multinomial 最低位有 carry：n 的五个低位皆 a，其和5a≥p，所以 `multinomial(5n;n^5)` 为0 modp；h_a亦如此，F16 两侧皆0。该证明不要求 b<p，也不按 residue p≡1mod10 限制。等价地，由冻结 carry formula 可见

\[
h_a\equiv0\pmod p\quad(a>\lfloor p/5\rfloor),
\quad h_a\not\equiv0\pmod p\quad(0\le a\le\lfloor p/5\rfloor).
\tag{F17}
\]

因此 F10 的 H_p degree 在 Fp 中恰为 floor(p/5)，常数项1。另有形式级数身份

\[
f_0(t)=H_p(t)f_0(t^p),\qquad
Q(D)f_0(t)=Q(D)H_p(t)\,f_0(t^p)
\quad\text{in }\mathbb F_p[[t]].
\tag{F18}
\]

**F9（每个完整 block，包含所有 prime-power 长度）。** 记

\[
T_L(\mu)=\sum_{b=0}^{L-1}h_b\mu^b\in\mathbb Z_p.
\]

因 Q(a+pb)≡Q(a)、μ^(a+pb)≡μ^(a+b)，对全部整数 L≥1 有

\[
\boxed{\sum_{n=0}^{Lp-1}Q(n)h_n\mu^n
\equiv S_p T_L(\mu)\pmod p.}
\tag{F19}
\]

尤其令 L=p^(e−1)，递归 F16 给

\[
\boxed{\sum_{n=0}^{p^e-1}Q(n)h_n\mu^n
\equiv S_p H_p(\mu)^{e-1}\pmod p\quad(e\ge1).}
\tag{F20}
\]

这是真正的 **所有完整正向 block、modp** 传递。若 S_p0，它们全为0；若 H_p(μ)0，它可能额外使 e≥2 消失，但这不能逆推 e1。F19–F20 不声称 modp² 或 modp^(9e)，不控制任意 partial block，更不是 F2 reciprocal sum 的全部 prime-power 分母。因此它与同行正在证明的真实 reciprocal block 界分开；F3 本身仅付出第 p 个 coefficient 的一层。

## 5. 已证 finite-field point count 准确适用，但不自动支付 weighted jet

Beukers–Cohen–Mellit1505.02900 **最终v2** Theorems1.3、1.5 给 defined-over-Q finite hypergeometric sums 的 all-field definition 与 explicit point count。本参数的 cyclotomic quotient 精确为

\[
\frac{(X+1)^5(X^4+X^3+X^2+X+1)}{(X-1)^9}
=\frac{(X^2-1)^5(X^5-1)}{(X-1)^{15}}.
\tag{F21}
\]

因此 BCM notation 可取 `p-vector=(2,2,2,2,2,5)`、`q-vector=(1^×15)`、r6、s15、M=Λ，gcd 为1。取 λ=μ，BCM PDF3 的实际 projective equations 是

\[
\sum_{i=1}^{6}X_i-\sum_{j=1}^{15}Y_j=0,
\quad\mu X_1^2\cdots X_5^2X_6^5=Y_1\cdots Y_{15},
\quad X_i,Y_j\ne0.
\tag{F22}
\]

对 prime powers q 的 characteristic 不整除10且 `Λμ≠1`，该 theorem 的 specified suitable completion 给

\[
\#\overline V_\mu(\mathbb F_q)
=\mathcal P_{6,15}(q)+q^5\,\mathfrak H_q(a,1^9\mid\Lambda\mu),
\tag{F23}
\]

其中 `mathfrak H` 是 BCM 的 normalized **Gauss-sum hypergeometric function**，并非本文的 integer-coefficient H_p；符号正，因为 r+s−1=20。其通常 split-character 定义需要10|(q−1)，但 defined-over-Q Theorem1.3的扩张不强加这个 congruence class。

本 special parameter 的额外 tame exception 由

\[
1-\Lambda\mu=4149/1024=3^2\cdot461/2^{10}
\tag{F24}
\]

给出；不能对 p461 使用 smooth-specialization/ordinary-point 的推断。F5–F20 的 coefficient-selection/Lucas 身份并不需要此 ordinary condition，仍适用于 p461；F3 只另要求 p>31 支付 N 的单位性。固定有限 exceptions 与 all-large-prime theorem 须分别说明。

F23 真正给了一个同参数、已证、全 prime-power 有限域接口，却不直接计算 `Q(D)H_p(μ)`。它保存整点数/trace，而本文目标是指定四阶 de Rham row 与指定 cycle coefficient 的 comparison。一般 matrix 的 characteristic polynomial 也不确定这类指定 matrix entry：例如 diag(1,p4) 的 eigenvalues 与 trace 固定，选取其第一或第二 projection 会得一个 unit 或一个 modp零值。这个 elementary distinction 只说明所需数据更强，不构成当前 motive 的反例。

可能的 geometric bridge 因而具体为：在 F22 对应的实际 period/subquotient 或 F5 toric representation 上，证明 special μ 的某个 integral cycle/comparison 把 **F14这一固定row** 放入 F13 的 Cartier kernel，并保持全部 good primes。建立一个抽象 Tate4 factor、一个 ℓ-adic Euler factor splitting 或一个 complex period identity，各自还须支付此 comparison；本稿未提供该 cycle 或这个零性定理。

## 6. 原始文献截至本轮检索的状态与剩余 theorem

**F10（严格的 status triage）。** 本轮显式检索精确 coefficients5532/2275、argument3125/1024、`p9`、finite-field/Frobenius/CM，并查 Guillera 作者截至2026的 publication page、arXiv latest-version metadata 与 EHMM2026。以下是读到的 positive scope，不把检索没有命中当作“无人可能证明”。

| Primary | 实际结论与本目标的关系 |
| --- | --- |
| [Cohen–Guillera2101.12592v1](https://arxiv.org/abs/2101.12592v1) | PDF10的#21与PDF16的upside-down #21准确匹配；PDF17–18的一般模式是 conjectural/“should have”接口，abstract明确generalizations withoutproof，不能据其式子称 S_p≡30p4modp9已证。 |
| [Guillera2312.16827 **v14**](https://arxiv.org/abs/2312.16827v14)（2025期刊发表对应预印本） | 全文9页的§4使用形式regularization及π-power→p-adicL替换作heuristic。§5–6的generalized congruences依赖该mate，并非本rank9的独立严格证明。早期v1明确有Conj2.1；v14改写标签没有取消heuristic假设。 |
| [Dembelé–Panchishkin–Voight–Zudilin1906.07384v3](https://arxiv.org/abs/1906.07384v3) | MainConj5.1明确五参数(rank5)，Table5.2/experimental Asai matching针对1/π²；不是本九参数的CM或Tate4定理，其Asai transfer theorem亦不能把conjecturedmatching免费变成证明。 |
| [Grove–Long–Rosen–Tu2607.25173v1](https://arxiv.org/abs/2607.25173v1) | 2026最新EHMMIII Theorems1.1–1.2实际给length4、parameter1、指定d/e family的modularity；不能把general philosophy当成当前length9、z0的已证theorem。 |
| [Au2312.14051v4 ExampleX](https://arxiv.org/abs/2312.14051v4) | 已证F2的ζ5 endpoint identity；它是复解析WZ评价，不自动证明这个forward截断的all-prime congruence。 |
| [BCM1505.02900v2](https://arxiv.org/abs/1505.02900v2) | F21–F23是准确应用的已证有限域point-count接口；完整Gauss-sum trace与本weighted Cartier gate仍需comparison。 |

就本轮实际读到的来源，**未获得无条件的全大prime S_p0，也未获得精确 S_p≡30p4modp9 theorem**。因此不能宣布本lift标准prefix cap降到8或5。若另外证明S_p0，F3即改进b_p首层，F19–F20即给全部完整正向block的modp抵消；随后必须使用实际reciprocal的complete/partialblock与higher-layer传递，不能从forwardmodp9直接领取四层分母改善。

本轮root还发现同一 omitμ leaf 上更强的 integral-Taylor root-power参考族。算术桥接的意义是获得真实coefficient信息、支持另一个base/extension；不能声称它单独救活固定rank10的当前CDT接口。该新root theorem应以其正式收审后的主稿为准，本稿不提前把未归档结论当成本稿证明。

## 7. 本轮完成的数学、文献归档及实际读域

本稿新增三项已纸证的可复用信息：原整数周期的explicit CT/reflexive-polytope模型；目标S_p与指定四阶rational form的exactrelativeCartier image及kernel条件；所有p>5、所有完整正向block和prime-power长度的modp传递。另严格应用BCM的pointcount theorem，明确它还差哪一个deRham comparison。没有将未证S_p0、Tateclass、higherreciprocal抵消或新无理性写成结果。

正常TLS新增原件都在 `literature/cdt_gamma_ramanujan_frobenius_sources_20261007/`，下载前用rg核查existing filenames/identifiers；未禁用证书校验。保留历史版本与最终版本的不同fingerprint，不把先读的v1冒称最新：

- `cohen_guillera2021_rational_ramanujan_arxiv2101_12592v1.pdf`：20归档页；本人actualFULL PDF1、8、10–11、16–18，共7页。
- `guillera2023_heuristic_zudilin_arxiv2312_16827v1.pdf`：10归档页；本人actualFULL全部10页，明确只作版本历史。
- `guillera2024_heuristic_zudilin_arxiv2312_16827v14.pdf`：9归档页；本人actualFULL全部9页，为数学状态采用的最终version。
- `dembele_panchishkin_voight_zudilin2019_asai_arxiv1906_07384v3.pdf`：18归档页；本人actualFULL PDF1–4、9–13，共9页。不继承同行或旧轮读域。
- `beukers_cohen_mellit2015_finite_hypergeometric_arxiv1505_02900v1.pdf`：24归档页；本人actualFULL PDF1–8，共8页；随后查明v2而单独保存final，本文F21–F23只按final核读。
- `beukers_cohen_mellit2016_finite_hypergeometric_arxiv1505_02900v2.pdf`：26归档页；本人actualFULL PDF1–6，共6页，特别Definition1.1、Theorems1.3/1.5。
- `grove_long_rosen_tu2026_ehmm_iii_arxiv2607_25173v1.pdf`：35归档页；本人actualFULL PDF1–4，共4页，核actualtheorem scopes；不声称全文35页已读。

已有Au v4本轮actualFULL PDF19、25–26共3页；PDF26的乱码处实际目读既有frozen `research/artifacts/cdt_odd_gamma_relative_chain_candidate_20261007/au_pdf26.png`，未改该render。另existingGreene1987原件actualFULL PDF1一页仅用于定义背景。本轮本人distinctprimary PDF **57页**，其中53新归档文件的actualread、4existing；新增归档142页不能当实际读数。网页metadata/作者publication list不计PDF页。最初误试CohenGuillera不存在v2得到正常404，未保存PDF；不是数学运行失败。Asai页数以最终physical PDF metadata18为准。

本轮actualFULL旧数学输入仅列首段三个MD，authority§190全文读，audit header/current_progress与wholeJSONsyntax读/parse；不冒称手读596旧proof或全部audit rows。正式独审、收审后最终作者FULL回读及单向FINAL来源收据随后闭合；全部旧frozen文件不修改。
