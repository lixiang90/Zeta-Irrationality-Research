# R₀ 的最高对数旗标与 CDT holonomy：线性单值化 no-go、D² 主项与明确费用

日期：2026-10-06。NEW 全尺度纸面证明。本轮实际核验主记录 §§79–84，主稿SHA256为 2e148742cc6e80381d5b46f434f3085954209887a934bcea19c3881ed285ccab；delivery记345份冻结输入、93份proof/review、74份PDF4399页、1124个链接。所有旧/同行数学MD、PY、JSON、manifest冻结只读，没有执行/import/rerun数学producer。

本稿研究已经存在的真实 exterior packet，不把最高log³消失误称为filled point。新增正面数据是一份十行species的精确CDT加权费用329/50；新增障碍是：其canonicaloriginbranch不能由任何有限代数cover上的非零有理微分投影变成亚纯函数。固定logweight的改善不贡献D²主项；共用解析域上的q=0真实arithmeticpacket严格阻止以这些共用数据反证actualq代数。均为全尺度证明，不是有限数值搜索。

## H1. 原件、对象与定理要求

本轮实际读CDT2025一手原件PDF3–8（Theorem2.1、Theorem2.6和§2.3 slopes/local estimate）、14–17（L值与2-adic实例），并视觉核PDF4。原件20页，SHA256为 5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1，封面是arXiv2510.04156v1。该文只有§§1–5；其中所引“§§6–8”指2024的[34]。

因此另实际读CDT2024 v2 PDF1–2目录、62–67（§5与Theorem6.0.2）、89–91、97–108（§7主定理、slopes、Lemma7.4.1）、122–124（§8主定理和species formula）；视觉核PDF105、123。原件218页，SHA256为 84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771。不把这些关键页阅读宣称为全文218页阅读，或§6–8全部证明的阅读。

CDT2025 Theorem2.1和CDT2024 Theorems6.0.2、7.0.1、8.0.1共同要求：所使用的全部formal functions经所选map拉回后，成为盘上的单值meromorphic函数。分母species、integrations和Bost–Charles metric的优化都保留此条件。CDT2024 Lemma7.4.1的核心步骤是先用一个固定holomorphic multiplier h消去有限极点，再对holomorphic scalar应用Poisson–Jensen。h能消pole，不能消一个非零unipotent jump。

采用冻结[exterior终稿](cdt_odd_R0_endpoint_sensitive_exterior_packet_20261006.md)的对象
\[
 P=\theta^4-x(\theta+\tfrac12)^4,\quad t=1-x,\quad
 \Phi(q)=Y_{h+qg_0}\wedge Y_{g_1}\wedge Y_{g_2}
       =\Phi_h+q\Phi_0 .
 \tag{H1}
\]
实际目标 \(q=\alpha_0=\pi^2(R_0-M_0)/16\)。取原稿E7a的四个Z行与五个mixed行，记九行向量F(q)。该有理connection的实际solution representation \(\mathcal W\) 有
\[
 0\to V\simeq\bigwedge^3V\to\mathcal W
   \to \chi\otimes\bigwedge^2_0V\to0,\quad \dim V=4,\ \dim\bigwedge^2_0V=5,
 \qquad G^\circ=\mathbf G_a^4\rtimes\mathrm{Sp}_4.
 \tag{H2}
\]
各q的actual九行独立，加1实际秩十；原稿已全尺度证明。本稿保留原Betti/整数comparison缺口，不把有理contraction记成免费integer gauge。

## H2. 每个非零primitive quotient都生成全部W：一个实际module lemma

令Kern为 \(\mathcal W\) 的任意 \(G^\circ\)-stable complex linear subspace。若其primitive五维quotient像非零，Sp₄ irreducibility迫该像为全部5。对Kern中一个有非零quotient p的vector w，translation a给
\[
 (u_a-I)w=a\wedge p\in V\cap\mathrm{Kern}.
 \tag{H3}
\]
非零p不可能使全部 \(a\wedge p=0\)：在四空间逐basis wedge即排除。因此交集含非零bottom vector；Sp₄ irreducibility迫全部bottom4位于Kern。Kern同时满射5，故
\[
 \boxed{\mathrm{Kern}\to\chi\wedge^2_0V\text{ 像非零}
           \Longrightarrow \mathrm{Kern}=\mathcal W.}
 \tag{H4}
\]
这是实际Ga₄作用的结论，不只是composition-factor计数。所有finite-index monodromy subgroups仍有同一connected closure，故有限代数cover上也成立。

## H3. Canonical origin 的primitive quotient对每个q、每个有限loop都非fixed

原点 \(x=0\) 的homogeneous monodromy为 \(T_V=\exp N_0\)，N₀为singleJ₄；source character为−1。混合quotient与q无关，实际来自Lagrangian plane
\[
 P_c=\langle g_1,g_2\rangle,\qquad v=g_1+\tfrac34g_2\in P_c.
\]
冻结真实node/Yukawa给
\[
 C(y_0,v)=1/\pi^2\ne0,\quad
 \ker N_0=\mathbf Cy_0,\quad
 \ker N_0^3=y_0^\perp.
 \tag{H5}
\]
singleJordanblock的唯一N₀-stable二平面为 \(P_0=\ker N_0^2\)，它位于 \(y_0^\perp\)。H5因此严格给 \(P_c\ne P_0\)。

若k奇数，\(T_0^k\) 在 \(\chi\wedge^2_0V\) 的全部eigenvalues为−1，非零quotient不可能fixed。若k偶数且非零，则 \(\exp(kN_0)\) fix \(g_1\wedge g_2\) 迫P_c invariant：decomposable wedge的projective line确定其二平面；unipotent logarithm再使P_c N₀-stable，矛盾。因此
\[
 \boxed{\text{对每个 }q\in\mathbf C,\ k\ge1,\quad
    (T_0^k-I)\Phi(q)\text{ 的primitive quotient非零。}}
 \tag{H6}
\]
即使actualq满足 \(N_0^3p_+\Phi(q)=0\)，H6也不改变。那一关系只限制bottom的最高log槽；primitive5的实际origin jump仍在。

## H4. 强no-go：有限代数cover和任何线性微分投影都不能单值化

**定理。** 取任意有限代数cover，任意在该cover上代数的row R；若R对actual九维空间非零，则 \(R\,F(\alpha_0)\) 的canonicaloriginbranch在任何更深有限cover上都不是meromorphic。同一结论对每个固定 \(q\in\mathbf C\) 的F(q)成立。若把独立常数1加入packet，则其meromorphic线性微分输出只能来自algebraic coefficient乘1，不能保留目标方向。

证明：在进一步有限cover上使R单值，并取localramification index e。R与derivatives可统一写成一个algebraic row，因为F的connection有理；微分不会离开九行module。设output亚纯，则其localmonodromy固定：
\[
 R\,(T_0^{2e}-I)F(\alpha_0)=0.
 \tag{H7}
\]
固定fundamentalmatrix，在solution-to-scalar map
\[
 \operatorname{ev}_R:\mathcal W\to\{\text{analytic functions}\},\
       w\mapsto R(x)\mathscr F(x)w
\]
中，kernel是finite-cover differentialGalois group稳定的subspace：R被该group固定，零函数的所有continued conjugates仍为零。特别该kernel为H2的connectedgroup稳定。H7使它含有H6中primitivequotient非零的vector，H4迫kernel为全部 \(\mathcal W\)。故output恒零，且fundamentalmatrix可逆迫R对实际九行空间为零，矛盾。

若output为 \(a(x)+R F\)，algebraic a在所选有限cover上meromorphic，其jump为0，故同一论证仍迫R为零。由独立常数1得到的a没有从九行中提取任何目标period方向。若人为把q直接放入a的coefficient，那是把目标当作外加系数输入；其常数函数不能提供区分actualq的branch或holonomy信息。证毕。

结论同时覆盖finite algebraic gauge、任意固定阶有理微分operator、和加入常数后的微分闭包。它没有排除所有更高tensor、非线性Hadamard、或使用额外periods的另一个packet；这些必须另建全部arithmetichypotheses、actualrank和integer费用。

一个相关integration限制也严格成立：若新g满足algebraic微分operator \(L(g)=a+RF\)，且g在上述canonicaloriginbranch亚纯，则右边亚纯，H4定理迫RF=0。故直接将同一个目标敏感module作有限次有理integration，不能靠“积分降低对数阶”使这个origin填平。CDT §5的integration收益是rank/denominator的另一项变化，它不自动清除monodromy。

## H5. 全尺度解析后果：真实半径仍为1，Cauchy contour仍有cut term

F(q)的九行在canonical \(t=0\) 上全纯，connection除 \(t=0,1,\infty\) 外无奇点。canonicalconifold的全纯性使每行在 \(|t|<1\) 单值全纯。每个保留coordinate row都对actualW非零；H4说明其 \(t=1\) branch并非meromorphic，尤其并非holomorphic。因此九个scalar各自准确满足
\[
 \boxed{\operatorname{rad}_tF_i(q)=1,\qquad
       \limsup_{n\to\infty}|[t^n]F_i(q)|^{1/n}=1
       \quad(1\le i\le9,\ \text{每个固定 }q\in\mathbf C).}
 \tag{H8}
\]
这由ordinary analytic continuation与Cauchy–Hadamard直接证明，不是系数numerics。highestlog旗标能改polylog prefactor，不能改善此指数半径。

若人为在盘内沿originpreimage切开，再对一个multivalued scalar作Cauchy，外圈积分之外还存在沿cut的jump积分。除去最高log³只降低jump的logdegree；H6/H4证明jump不为0。一个固定holomorphic multiplier h只能将jump乘h，不能使它在开cut上恒零。故CDT Lemma7.4.1使用的holomorphic scalar/Poisson–Jensen步骤不能原样搬来。删去cutterm将是假设真正的单值化，不能由logweight控制替代。

## H6. 固定logweight与parabolic flag：为什么不给免费D²率

给出两个准确的估计，范围只覆盖“固定periodpacket的loggrowth降低”。

第一，rank \(r_D=m(D+1)\) 的auxiliary Hermitian lattices若两metric满足
\[
 e^{-a_D}\|s\|_D\le\|s\|'_D\le e^{a_D}\|s\|_D
 \quad\text{对全部s},\qquad a_D=O(\log D),
 \tag{H9}
\]
则其degree差绝对值≤\(r_Da_D\)。证明以Gram eigenvalues比较，determinant的half-log最多变 \(r_Da_D\)；subspace/quotient induced norms仍满足同一comparison。每层evaluationheight亦最多改O(a_D)，总共r_D个filtrationjumps，故
\[
 \boxed{\Delta\widehat{\deg}E_D,\ 
       \Delta\sum_n h(\psi_D^{(n)})=O(D\log D)=o(D^2).}
 \tag{H10}
\]
CDT2024 PDF99–103的slopes矛盾比较D²主项，H10不能贡献一个新的正exponentialrate。

在cutoff \(\epsilon_D\ge \exp(-D^A)\)、A固定的常见logarithmic exhaustion上，fixed logweight
\((1+|\log|u||)^k\)、k固定，只改变lognorm至多O(klogD)。highestlog³降低到至多log²因此属于H9的范围。若选择随D增长的极端weights或让cutoff双指数缩小，H9不再适用；这时必须独立重证metric的degree、localheight与cutjump estimates，不能把它登记为已有CDT的免费改进。

第二，nearunipotent endpoint的fixedweight \(g_k(u)=k\log(-\log|u|)\) 无atomic parabolic degree：
\[
 r\frac{d}{dr}g_k(r)=-\frac{k}{-\log r}\longrightarrow0.
 \tag{H11}
\]
因此其curvature在该point没有logarithmicatom；相比之下，真正powerweight \(\beta\log|u|\) 的上述极限为β。highestlogdegree变k不改变localexponents或这项atomicweight。source的半整数character和homogeneousunipotentexponents也不随q改变。

所以“下降一格logflag”不能直接记作可填平一个puncture或免费增加parabolicdegree。若用Deligneframe上的localflag修改bundle，必须比较globalhorizontalmodule、Betti/deRham lattice与auxiliarydegree。§H4定理已经排除了在当前module内用一个globalalgebraiclinearprojection作这种单值化。Deligneextension的localbundleframe可把log记入connection；它不将原scalar自动变为单值函数。若进一步用Nilsson/logarithmiccomparison消除scalar的log，该comparison不是algebraicgauge，且其在conifold的全部arithmetictaylorcoefficients并未由单一α₀假设得到。

## H7. 当前十行的精确CDTspecies费用329/50

令D_n为[1,…,n]，C仍为冻结整模型中包含全部坏素数的正整数；本稿不将其替换成16或其它未经all-place证明的数字。假设α₀∈Q时，固定整数d₀整化α₀。E7a的四Z行有
\(16d_0D_{N+b_0+3}^7C^{N+12}\)，五mixed行有D六，常数1无该费用。

把十行依次排列为：1、五mixed、四Z。LCMspecies用六列共同nonconstant因子（cutoffu=1）及一列只属于末四行（cutoffu=6），每列非零值b_j=1。因此
\[
 (\sigma_1,\ldots,\sigma_{10})=(0,6,6,6,6,6,7,7,7,7),
\]
\[
 \boxed{\tau(b)=6(1-1/100)+(1-36/100)
          =\frac{329}{50}=6.58.}
 \tag{H12}
\]
等价weighted sum为 \((6(3+5+7+9+11)+7(13+15+17+19))/100\)。CDT2024 Remark8.0.6证明对这种nested columns，finer \(\tau^{\flat\flat}\) 同样等于此值。这里没有新增 \(n^e\) integrationtype；故e=0，不能另取负的τ♯。

固定LCM indexshift b₀+3可按CDT2024 Remark6.0.12以每列1+ε盖住、再ε→0；不产生主项费用。为完整支付 \(C^n\)，令
\[
 \widehat f_i(s)=16d_0C^{12}f_i(Cs),\qquad
 \psi(z)=\phi(z)/C,
 \tag{H13}
\]
其中f_i为十行。固定scalar不影响rank/holomorphy；此时widehat函数满足H12的整数LCMtype。C是有理坐标scale，不是Tateperioddivision。定义
\[
 I(\phi)=\iint_{\mathbb T^2}\log|\phi(z)-\phi(w)|\,d\mu(z)d\mu(w).
\]
本节取φ在闭单位盘的某邻域全纯，确保boundaryintegral按原定理定义且有限；一般open-disc map可按原件Lemma7.4.1先作径向缩盘，满足相应finite-integral limit条件后再取极限。若全部actualpullbacks \(f_i(\phi(z))\) meromorphic于盘，且
\(\log|\phi'(0)|-\log C>329/50\)，CDT2025 Theorem2.1严格给
\[
 \boxed{10\le
 \frac{I(\phi)-\log C}
      {\log|\phi'(0)|-\log C-329/50}.}
 \tag{H14}
\]
已保留C在numerator与denominator的完整scale代价。H14是一份条件明确的定量不等式；不是已经找到违反它的map。

## H8. Number field 的all-place版本与q=0真实reference no-go

α₀∈K时不能仅使用一条Q-formula宣称其超越。给出本packet所需的field版本：令每个embeddingσ的packet参数为σ(α₀)，选择按§H7相同boundaryregularity条件、且实际在该packet上meromorphic的maps \(\phi_\sigma\)，以standardnormalizedarchimedeanweights \(w_\sigma\) 求和（总和1；complexpair合并亦可）。Cscale后，每个有限place的LCM coefficients只有O(logn) valuation，故在单位open盘收敛，可取identityfiniteplacemaps。固定d₀clearα的成本不贡献D²。

设
\[
 A=\sum_\sigma w_\sigma I(\phi_\sigma)-\log C,\quad
 L=\sum_\sigma w_\sigma\log|\phi_\sigma'(0)|-\log C .
 \tag{H15}
\]
在所有embeddings都具备所列meromorphy、有限places采用上述模型、L>329/50时，同一slopes证明给
\[
 \boxed{10(L-329/50)\le A.}
 \tag{H16}
\]
为避免只引用一个未核的field口号，简述完整D²推导。采用CDT2025 §2.3的OK evaluationmodule，rank为m(D+1)，m=10；allplaces使用其standardheight normalization。将H12的columns记u_j、b_j，选择denominatorcutoff \(y_j=u_jb_j\)。原件Lemma2.9与CDT2024(7.3.7),(7.3.14),(7.3.15)的same local estimates按places加权为
\[
 \widehat{\deg}E_D=
   \{mA/2+\sum_j u_j^2b_j\}D^2+o(D^2),
\]
\[
 \sum_n h_\infty(\psi_D^{(n)})
 \le\{-m^2L/2+mA\}D^2+o(D^2),\qquad
 \sum_n h_{\rm fin}(\psi_D^{(n)})
 \le\{m^2\sigma_m+\sum_j u_j^2b_j\}D^2/2+o(D^2).
 \tag{H17}
\]
PNT与各v|p的normalizedweights总和1使integerLCM的cost仍为原species；functionalbadapproximation的K版本正是CDT2025§2.3所用输入。Bostslopes、取D²系数，即 \(m^2(L-\sigma_m+\sum_j u_j^2b_j/m^2)\le mA\)，给H16。全部finitebadprime费由Cscale支付，不假设未知oddprimegoodness。

现在有一个严格consistency obstruction。**q=0** 的同一个F(0)无条件为Q-coefficientGpacket，实际加1rank10，同一个C/D七模型可用。对任何同时适用于actualq与q=0的map（或K-place family），H14/H16已经对q=0成立。因此仅凭common-domain/同一species数据，不可能得到一个排斥actualq的CDT矛盾：
\[
 I(\phi)-\log C\ \ge\
 10\{\log|\phi'(0)|-\log C-329/50\}.
 \tag{H18}
\]
H18在条件denominator为正时无条件来自真实q=0reference，不是toy反例。

尤其，若map避免origin，并仅通过原稿E20.3的conifoldfilledbranches取解析域，这些localconditions对全部q相同；同一map同时适用于q=0。原稿E22的∞ obstruction也对全部q相同。H4说明当前canonicalorigin最高logflag不能把一个originpreimage加入这种域。优化C、species或φ仍可改进明确bounds，但不能在共用hypotheses下违反H18；若数值优化声称如此，必有未支付费用或meromorphy错误。

## H9. 可使后续路线合法的具体突破条件

本文不排除某个**不同 transported origin word** γ 的新值敏感leaf。其准确criterion来自冻结E30：先取偶数cover杀χ，必须
\[
 P_\gamma=P_0,\qquad C(y_0,H_{\gamma,q})=0.
 \tag{H19}
\]
若第二式为 \(a_\gamma+q b_\gamma=0\)，要新增只属于actualq的fillablepoint，必须实际给word、证明 \(b_\gamma\ne0\)、并由真实marking证明 \(-a_\gamma/b_\gamma=\alpha_0\)。之后仍需allplaceembeddings上的合法maps、Betticomparison和finiteplace预算。当前未构造这个word，不能登记capacity收益。

另一合法方向是建立一个超出当前九行linearclosure的新packet或新的vector-valued/parabolic arithmeticholonomy定理。必须同时提供：真正单值化或带jumpterm的替代localheight证明；integer/numberfield model与所有embeddings；actual新增rank；新增periodcomparison费用。H4排除的是现有module中的algebraiclinear操作，H10/H11排除的是把fixedlogweight变化直接当作主率；没有将其扩大成所有高tensor或未来理论的no-go。

已经成立的highestlog关系仍有真实意义：它唯一识别α₀的markedoriginflag，可作为这种更强理论的boundarydatum。但在当前scalarCDT定理中，它不是meromorphiccondition，也不是一次periodnormalization免去全部sourcejets。

## H10. 当前结论、来源与执行范围

本轮新证明是H4有限cover微分投影no-go、H8真实半径1、H10/H11 fixedlog/parabolic主项限制、H12–H18精确species和common-domain quantitative obstruction。单初值仍只面向 \(\alpha_0=\pi^2(R_0-M_0)/16\) 的代数性；它不等价于 \(R_0-M_0\) 有理或代数。没有新的ζ/L/Catalan数值无理性定理或Leanclaim。

实际source页、PDFhash与只读receipt保存于 [NEW来源清单](../literature/manifest_cdt_odd_R0_endpoint_flag_holonomy_interface_20261006.json)。PDF只读抽取/PNG渲染用于数学公式视觉核验；第一次stdout编码错误及大输出截断后实际分段补读，不把截断内容算作阅读全文。没有下载、TLS例外、旧/同行数学producer或NEW数学producer。renderedpages属于阅读scratch，不是新的文献PDF。
