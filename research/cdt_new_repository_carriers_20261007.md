# 原仓库全文新读与 Θ 的有理复合 dilogarithm 算术补法

2026-10-07。NEW。只新增本稿，不改 main、manifest、旧研究稿、原仓库或旧 producer/Lean。原仓库只读 HEAD 为 `adc7f1241b42e322a6451854ab7e4b4c146bf78a`。先实际 FULL 读取 `cdt_weight4_space_germ_bridge_20261007.md` 九节 S1–S40，重点承接 S37–S40 的真实 Θ，而不是重启旧 Catalan determinant。

本轮从一份此前仅局部阅读的原稿完成全文 source 新读，提取有理字母的 differential/holonomy 方法。具体新增是一个真实 rank-three dilogarithm 复合载体，以及 Θ 原五行和 suspension 的更小、覆盖全部 prime powers 的 LCM cap。没有得到新数值无理性或 LI 定理；全稿 source 阅读亦不等于重新验证其 Deligne–Drinfeld 主定理。

## 1. 选稿、实际全文范围及没有重算的旧结果

唯一选为本轮 FULL 的原稿是

`E:/codex-build/math/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/build/paper.tex`。

实际读取 paper、preamble、sections/01–08、references、两个被 input 的 figures，共 13 个 source inputs、148564 bytes。第一次合并输出中间截断，随后独立完整重读 02-algebra 和 03-degeneration，不将被截掉的内容算作已读。此前 scope audit 只记 intro 及 holonomy 的具体 coefficient 段；本轮没有把此前局部阅读冒称全文。

候选检索使用原仓库 `rg --files` 与 `.tex/.md` 定向正文检索，涉及 Catalan、linear independence、polylog/dilog、period/holonomy、monodromy 与 endpoint/depth-two。Catalan 已在既有 reading manifest 记为 team 完整 44 页，故未选为“新 FULL”；未再运行它的 producer 或 Lean。CDT 的 `The linear independence of 1, ζ(2), and L(2,χ₋₃)` 是既有 literature 外源，不在这次原仓库同名 source 文件中；没有由文件名检索推称已经全文审计。

另实际完整读入 `A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/build/main.tex` 与 `sections/00-introduction.tex`，作为 map/J 适用性筛选。它的主接口是 normalized univalent f 的 inverse derivative means 的增长指数；intro:23 说明乘常数不改指数，:46–50 的 bound 是 `M_{-1}[f'](r) ≤ C(1-r)^{-1/4+ε}`，:56 明确 ε 没有数值评估。此接口没有提供 Θ 的实际共同 map 或其 CDT J；因此没有为凑 FULL 而读其余六节，也没有将其主定理当作本轮已独立核验输入。π exponent 稿仅 main 的 intro/input routing 被候选筛选读到，不选作本轮研究输入，未读其余 sections。

## 2. 真正可复用的原公式及精确假设

DD `04-deletion.tex:41–47` 对 rational letters/endpoints P 定义整数 deletion matrix

\[
 T_H(P_1\cdots P_k)=\sum_{j=1}^k
 \bigl(\operatorname{ord}_H(P_j-P_{j+1})-
 \operatorname{ord}_H(P_{j-1}-P_j)\bigr)
 P_1\cdots\widehat{P_j}\cdots P_k.
 \tag{N1}
\]

等字母差的 valuation 按定义取 0；不能取零函数的无限 order。`04:68–76` 将所有非恒定差写成有理线性因子的整数 dlog 组合，例如

\[
 p-w=\frac{2z_2(z_1-z_3)}{(z_2+z_3)(z_2+z_1)}.
 \tag{N2}
\]

相邻删除的 logarithmic triangle identity 给 Ω∧Ω=0。原稿取 residues 得 flat-relation matrices，再在 Z 上下降；这里必须先保留 characteristic-zero 的 hyperplane incidences，不能模 2 后把不同的 ± hyperplanes 合并。有限 word cutoff 给有限整数矩阵，合理的 rational substitution 不需要把 period 数值先当作 rational。

DD `07-holonomy.tex:16–34` 的连接是

\[
 dg=\lambda\sum_{i<j}t_{ij}d\log(z_i-z_j)\,g,
 \qquad\lambda=(2\pi i)^{-1}.
 \tag{N3}
\]

其 actual coefficient identities 来自固定有限 weight quotient 中的有限 iterated integrals。`07:120–159` 的 regularized transport 有真正 collar estimates `C_N ε^{η-1}(1+|log ε|)^N`，η>0；它证明消去 singular frame 后的极限存在，而不是证明未换 frame 的全部 transported germs 在 endpoint meromorphic。CDT 所需共同 pullback 仍须逐枝核验，不能将 regularized value 当成普通点的全 germ。

`06-category.tex:190–225` 的 rational descent 只适用于有限 rational linear equations 的 kernel/image。在 `07:517–527`，实际 convergent word coefficient 是 `−λ^n ζ(n)`；`07:540–550` 用它非零来取得某个 rational Lie solution。原文明确只用 real series positivity，不作 arithmetic independence assertion。因此这里不能从 Lie freeness、rational descent 或 λ normalization 推出 ζ 数值 LI，λ 亦不能免费带入 Q-Taylor carrier。本稿只复用 N1–N3 的有理 dlog 与全 local-branch 核验策略；下面载体全部自行推导。

## 3. q 的真实三维载体：有理复合、实际 rank、全有限处

采用 root 本轮指出的 rational function

\[
 q(x)=\frac{x(1-x)}{1+x},\quad
 R(x)=\log(1-q(x))=\log(1+x^2)-\log(1+x),\quad
 K(x)=\operatorname{Li}_2(q(x)).
 \tag{N4}
\]

这里所有 log/Li₂ 是 x=0 的实际正规芽及其延拓，不能在每个复 x 重新取 principal value。q∈x Z[[x]]，K∈Q[[x]]。直接逐项导数得到

\[
 R'=\frac{2x}{1+x^2}-\frac1{1+x},\quad
 K'=-R\frac{q'}q,\quad
 \frac{q'}q=\frac1x-\frac1{1-x}-\frac1{1+x}.
 \tag{N5}
\]

因此 `{1,R,K}` 是实际 closed rational differential space，order 至多 3 的 holonomic carrier。R(0)=R(1)=0；沿 [0,1] 有 0≤q≤(√2−1)²<1，所以 K(0)=K(1)=0 且在两处整个 canonical germ 全纯。q' 的两个零点只是 rational composition 的 critical points，不能当成 K 的新增 branch points。

**N6（实际 rank=3）。** 绕 i 一次，1−q 在 i 有 simple zero，故 ΔR=2πi。由 N5，

\[
 \Delta K=-2\pi i\log q+C
 \tag{N6}
\]

于指定 bridge 的邻域成立，C 为该 continuation 的 constant。若 aK+bR+c=0、a,b,c∈C(x)，取此 continuation 的差得到 `a(−log q+C/(2πi))+b=0`。log q 不在 C(x)：围绕 q 的 simple zero x=0 连续作圈使它平移任意整数倍 2πi，而 rational function 单值。因此 a=0，再 ΔR 迫 b=0，最后 c=0。这个 rank 证明用实际 analytic continuation，不依赖 numerical period independence，也不把 formal words 的维数当 actual rank。

写 `ℓ_N=lcm(1,…,N)`、ℓ₀=1。N5 的 R' 全 Taylor coefficients 为整数；q'/q 的全部 Laurent tail 亦为整数。因此

\[
 N[x^N]R\in Z,\qquad
 N\ell_N[x^N]K\in Z \quad(N\ge1).
 \tag{N7}
\]

具体写 r_N=[x^N]R=a_N/N，则

\[
 a_N=\begin{cases}-1&N\text{ odd},\\
 1+2(-1)^{N/2+1}&N\text{ even},\end{cases}
\]
\[
 N[x^N]K=-r_N+
 2\sum_{j<N,\ j\equiv N-1\ (2)}r_j.
 \tag{N8}
\]

N7 覆盖 p=2 和全部 prime powers，fixed normalization 为 1。精确 e 型为 σ=(0,0,1)、e=(0,1,1)；e=0 可用 σ=(0,1,2)。尚未给此精确 e 型的 τsharp 优化值，不能免费删除它。K 自身 endpoint K(1)=0 不编码 Θ 的数值关系，不能把 rank-three carrier 误当一个 Θ irrationality proof。

## 4. Θ 原载体的 nonlinear identity 与全 prime-power 半宽 cap

令 U=θ²D、V=θD，承接桥文 S37–S40 的同一实际 D。由 N5、经典 Li₂ 导数和 x=0 正规化，root 提出的 identity 直接核为

\[
 \boxed{U(x)=\frac14\operatorname{Li}_2(-x^2)
 -\frac12\operatorname{Li}_2(-x)
 -\frac12K(x).}
 \tag{N9}
\]

右侧导数是 `−R/(1−x²)`，值在 0 为 0，与 S37 的 U 完全相同。N9 的意义在于 highest-denominator cancellation 在实际 rational composition 中逐系数发生，不是仅在 x=1 消一个点值。

记 h_n=Σ_{j<n,j≡n−1 (2)} a_j/j，则

\[
 u_n=[x^n]U=-h_n/n,\quad
 v_n=[x^n]V=-h_n/n^2,\quad
 d_n=[x^n]D=-h_n/n^3.
 \tag{N10}
\]

首先 N10 给全 N 精确 e 型 `nℓ_n u_n, n²ℓ_n v_n, n³ℓ_n d_n∈Z`。由 N9 可给整个 prefix 的更小 e=0 cap：

\[
 \boxed{
 \ell_Nr_n,\quad
 \ell_N\ell_{\lfloor N/2\rfloor}u_n,\quad
 2\ell_N\ell_{\lfloor N/2\rfloor}^2v_n,\quad
 2\ell_N^2\ell_{\lfloor N/2\rfloor}^2d_n
 \ \in Z\qquad(1\le n\le N).}
 \tag{N11}
\]

**完整 prime-power 证明。** 固定 odd prime p，设 E=v_p(ℓ_N)、E'=v_p(ℓ_floor(N/2))。若 E'=E，N10 的普通 bound 已给 u/v/d 最大 denominator exponents 2E/3E/4E，N11 正好支付。若 E'=E−1，则 p^E>N/2，唯一 1≤n≤N 且 v_p(n)=E 的 n 是 p^E。

对 n≠p^E，v_p(n)≤E−1，内和 denominators 最深至 E，故 u/v/d 最大 exponents 分别至 2E−1、3E−2、4E−3，均由 N11 支付。对 n=p^E（odd），N9 第一项无 x^n coefficient；第二项贡献 +1/(2n²)；K 的 k=n 项是 `(q^n)_n/n²=1/n²`，给 −1/(2n²)，恰相消。剩余所有 k<n 的 dilog denominators k² 至多 2(E−1) 个 p 层；1/2 是 p-unit。因此 `v_p(u_n)≥−2E+2`，再除 n 或 n²得 V/D exponents 至多 3E−2、4E−2，仍准确由 N11 支付。这里允许 E 任意，不将 p 一阶 head 的 observation 外推到 p^E。

对 p=2，N10 的 outer n 与 inner j 奇偶相反。n 偶时所有内 j 奇，h_n 为 2-integral；n 奇时 outer n 是 2-unit。故 prefix u/v/d 的最大 2-denominator exponents 分别 ≤E、≤2E、≤3E。E≥1 时 E'=E−1。U 的 N11 cap 给 2E−1≥E；V/D 加 fixed 2 后给 3E−1≥2E、4E−1≥3E。N=1 时全为 0。固定 2 不能删：d₂=1/8，v₂=1/4 就说明低层支付确有必要。至此包括 small primes、all prime powers、整个 prefix，而非只 large-prime asymptotics。

N11 是无条件的原五个 Q-Taylor functions 的整性输入，不含 u，也不依赖 Θ 的数值关系。对任意固定 u∈Q，取整数 d>0 使 du∈Z，并写 F=F_{Θ,u}。S40 的 coefficient formula 配合 N11 给

\[
 \boxed{2d\,N\ell_{N-1}^2
 \ell_{\lfloor(N-1)/2\rfloor}^2[x^N]F\in Z.}
 \tag{N12}
\]

N12 的 Taylor 付款只需要 u∈Q；额外关系 Θ=u 仅用于在 x=1 消去 F 的完整 logarithmic germ，是解析填点的假设。这里外层 N 仍真实存在，d 是一次固定 scaling，不增长。吸收 N 入 ℓ_N 得原六项 generating system `{1,R,U,V,D,F}` 的有效 e=0 阶梯：

\[
 \sigma=(0,1,3/2,2,3,4),\qquad
 \tau_{\rm safe}=\frac{3+15/2+14+27+44}{36}
 =\frac{191}{72}.
 \tag{N13}
\]

五个 columns 的 widths 依次为 1,1/2,1/2,1,1，各列从某行开始全为 1，故满足 CDT staircase，而非只报 row-sum 猜测。比桥文 conservative `(0,1,2,3,4,5)` 的 125/36 小，但仍高于 log 2；没有凭此得到 CDT 矛盾。若保留 exact n powers，则有效输入为

\[
 \sigma=(0,0,1,1,1,3),\quad e=(0,1,1,2,3,1),
 \tau^\flat=3/2,\quad \tau=3/2+\tau^\sharp(e).
 \tag{N14}
\]

N13/N14 是候选六生成行的付款；没有假定六行实际独立。它们不能继承 Catalan 的 real-place constants、nonvanishing certificate 或 numerical theorem。真正贡献是从 actual rational pullback 的 top k=n 精确取消取得两个半宽 columns，并完整修补“只检查 p 一阶”的缺口。

## 5. univalent map 的 J：为何 screened manuscript 没有给免费实处收益

若 φ 在 closed unit disk 邻域全纯，φ(0)=0、φ'(0)≠0，且在稍大的 disk 单叶，则

\[
 H(z,w)=\frac{\varphi(z)-\varphi(w)}{z-w}
\]

（在 diagonal 取导数）是 nonzero holomorphic function。log|H| 对两个变量分别 harmonic，连续双 mean-value 给平均 log|H|=log|φ'(0)|；log|z−w| 的双边界平均为 0。因此

\[
 \boxed{J(\varphi)=\log|\varphi'(0)|.}\tag{N15}
\]

若仅在 unit disk 单叶，可先用 φ(rz) 并在 boundary integrability 条件下取 r↑1；不能未经检查就作 boundary limit。N15 已足以说明：inverse derivative means 的 scale-invariant growth exponent 无法改善 fixed derivative 下的 CDT J。它也不构造使 Θ 全六行共同单值的实际 φ。较大 map 仍须支付 q=1 在 ±i、q pole 在 −1，以及 transported logs 在 0/1 的 branch 兼容。N4–N15 不把 φ omit 三点误写成落在某个 canonical slit domain，更不把 Li₂(q) endpoint 0 当任意 transported branch 的 0。

## 6. 新核证、source 收据及剩余事项

本輪仅执行一段全新 inline Python `Fraction` 运算，n=1,…,64，逐 prefix 核 N7/N11 和 N12（测试 u=7/13）。输出全部 PASS，并准确核 `191/72, 3/2, d₂=1/8, u₆=23/90, d₉=−13/5832`。这只是有限 certificate；N11/N12 的全 N 保证来自上述 prime-power 纸证。没有执行旧数学 producer、旧 Lean、旧扩表或 PSLQ，没有下载/读取新 PDF，没有外网新来源，所以无需伪造 external-source receipt。

本轮所用原稿关键输入 SHA256：

| input（相对 DD/build） | bytes | SHA256 |
|---|---:|---|
| paper.tex | 766 | cf42f7115c7c873968c6850c265ce5bde6c112670eea7d729e874c6f9e8ee082 |
| preamble.tex | 1449 | c6327153beae693e38f4526ca67bae65342c5bd654eaafea3b4f7f732b2fdc44 |
| sections/01-introduction.tex | 9745 | 9d632ee8436f3fd986d2f784d1acc2c3024262aacb13a560e921b31963a7289a |
| sections/02-algebra.tex | 18447 | 969876e978b959a11a67922f8d7e9741ebe2ad5c40854d45085853ddd86153fb |
| sections/03-degeneration.tex | 19331 | 6435e307b67109999602ea3d2a584cfccee13fb44e624782b78327a16e167a62 |
| sections/04-deletion.tex | 19410 | ba83917c34f482d0cfbb067e0b1e0d31920d7e88733f90f6177fd16946f3f7af |
| sections/05-image.tex | 20625 | 6caabe2bb12e41856058ce535fb1ec43578ef11fc6dd9af26c8af86a933c1e18 |
| sections/06-category.tex | 10386 | 12eb6b4ebed2f93336a4bc8976cc3eaac8635b026bed214f64dd496871a49b48 |
| sections/07-holonomy.tex | 27594 | aec06f4767cf810e421c4a394f543b1d7ce128c4a31f02cec5c32e3ecb2a8c44 |
| sections/08-induction.tex | 9196 | f04cd73a654b53ff7872b57e5b533d095e2d75758ddd279ae7f2c1a595f5ca39 |
| references.tex | 4871 | 84c788f7f1728028a7cbaadb9c55191a73e8e377b14ebd0e28bc077147d4834f |
| figures/deletion-block.tex | 2880 | db6111cd8df5e18c73f4bc87f16f2eb5d5b96b2aa50cb1f012166e4a26ae67dc |
| figures/reassociation.tex | 3864 | f240a1dc5733260397473646b52f3ce4da83c1d4db2b3b3bcdabf0ddd73da759 |

新的可审验接口是 N6 的实际三维空间秩、N9 的同对象 nonlinear identity、N11/N12 的 complete cap。下一步应在 Θ 同一对象上核 rank、single-relation pullback 与真实 τsharp/map/J，或改 carrier 实现；不能以 DD 的完整 Lie-theorem 名称代替数值 period injectivity。未发现上述借用公式中的致命缺口，但本稿并未宣称独立认证 DD 整篇主定理、原仓库所有 odd ζ 或某个新 numerical LI 结论。

**2026-10-07 root 写后纸审收据。** root 实际 FULL 读取本稿 N1–N15，独立重证 N6 的 actual monodromy rank、N7/N8 的全部 Taylor 系数付款、N11 的 odd-prime highest power 唯一 n=p^E 及 top k=n 精确取消、p=2 的完整 parity cap、N12 的 outer N，以及费用 191/72 与 exact-e flat 3/2，数学 PASS。root 另要求本稿明示：N11 不依赖 u，N12 仅需 u∈Q，Θ=u 只承担解析填入 x=1；作者已按此澄清。该纸审针对本稿 N11 的 half-width cap 证明；它与另一稿 T10 的 boundary cap 是各自独立的证明，不能合并署名或把一份的 PASS 转移给另一份。此收据不宣称 root 已完成 DD 原稿全部 source 的第二遍全文审计，也不称 Lean 形式化验证或新的 numerical theorem。
