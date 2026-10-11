# 双极点全素数整化与真实格费用：独立实际审阅

日期：2026-10-06。审阅者：toric_chow_completion。本文为 NEW combined independent review；同行数学稿和历史来源均仅读取，未执行、import 或重跑任何旧/同行数学 producer，亦无本次数学 producer。

## 1. 最终对象与真实阅读

实际全文读并手核 [arithmetic 最终稿](cdt_odd_mixed_double_pole_arithmetic_cost_20261006.md) A1–A14，包括新增 A30a。最终 SHA256：

`452b9202ab3460f95e1ac5500092146cbe2ba0f9ed1e0a22bf5acb0a291fe985`。

亦实际全文读 [arithmetic 最终来源收据](../literature/manifest_cdt_odd_mixed_double_pole_arithmetic_cost_20261006.json)，SHA256：

`6a78cda6cf7517cdf47a83548a7974a305dc561b46b99176d0cf8a325dfaaa88`。

初始1cb5版本已全文读；最终452b只增加 A30a，将 actual change-of-basis 与 general factorial fee明确写出。最终版本再次全文阅读，不仅依据作者告知差异。

实际全文读并手核 [lattice 最终稿](cdt_odd_mixed_double_pole_primitive_lattice_review_20261006.md) P1–P9，最终 SHA256：

`93c9e1705cc63160ce7c212501df79b23b10b249d42acd26a715a538315b8ac8`。

初始 actual-fullread snapshot为 `985004e92c4483640db71494712da13373ad3a1bfe0cf38adefbb3595e631c75`。该版本误称 P16 未经gcd约除的整数约束行为primitive；arithmetic同行指出后，作者在冻结前明确raw rows、actualgcd与wholeconstraintlatticesaturation。修订不改变rationalkernel或paircancel。最终93c9版本已再次实际全文读，不把误名版本直接当finalpin。

实际全文读冻结 mixed H1–H9，SHA256 `e6e174a7306d4a9458ff9873d76e5bc40866b258d5d6f760bbf68a28c99ae463`。本轮实际读 Lai 原件 PDF1–7、17–25，共16页，包含完整 Section6；原件 SHA256 `838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58`。没有声称本审阅者阅读全文25页，或完成 Lai 全部 prime-sum/external theorem 的独立验证。以下全素数结论直接逐步手核同行的新自足推导，未将作者的“已全文读”替代自己的阅读。

## 2. Actual target polynomial 与 normalization

General B>κ≥3 布局的 degree 是 `−2h−2`，h=(B−κ)n；对degP<2h，partial fractions完全没有 polynomial part，simple coefficients sum=0。W_j的 binomial product与 C_j的 harmonic组合由 double pole 的 logarithmic derivative直接得到。ζ导数和只有在 actual candidate relation成立时才识别为此 X-polynomial；作者区分 formal Λ_X 与 analytic identity正确。

Monomial basis到binomial basis的 triangular diagonal是1/i!，因此 J=det in binomial basis与原 factorial normalization严格相同。a=−r,b=1 的single-target polynomial最高X系数是 positive evaluation Gram determinant；N+1个distinct nodes多于h，故 degree精确h。但 polynomial非零仍不足以给所有rational values上的无穷nonzero，必须另外使用 auxiliary primes。

Lattice P3的 scalar与full-space basis变化分析通过：positive c_n使primitive multiplier变为d_n/c_n，product |primitive evaluation|不变；congruence basis变化乘det(A)^2，同一空间/同一form的变化只是这种normalization。Non-unimodular basis的finite index与archimedean factor均必须付。不同subspace改变实际对象，不能据此沿用旧margin。

## 3. 全素数与全X系数的安全模型

Arithmetic A7的 derivative formula由binomial addition在辅助参数0处求导得到。整数 t上binomial values integral，故D_i f_i'(t) integral。这给所有 finite primes、包括p≤s的η_p。Harmonic sums、fixed factorial coefficients及 derivative lcm的三种费用均保留；η_p≥−s floor(log_p M)成立，Gauss valuation处理全部X系数而非只处理一个candidate integer。

p>N时仍可能H_{2n+j}出现一个p分母，但2n,j<p且2n+j<2p；此时binomial carry给W至少κ层p因子，消去这一harmonic分母。因此p>N真正integral。仅以p超出pole range省略较长harmonic是不够的，作者已经补齐。

p>sqrt(M)时Legendre仅第一层，W在同一residue上的valuation常数wρ∈{0,2,κ,κ+2}。Translated monomials使tail matrix entry的valuation至少i+j+w−s；其中first-derivative evaluation的额外p分母已经记入。Head rank≤2，tail rank≤2q，head entry至少i+j+w−1。Column展开、rank限制与行列指标总和得到准确F_s,ρ(m)。Singleton improvement只在q=0、两个harmonic下标都小于p时成立；最终δ的条件正好如此。

F_s−F₄=−(s−4)min(m,2q)通过逐项化简，故higher weight只惩罚实际tail占用。ρ=0时U₀=0、V₀=(s−1)!X，是integral rank1 head，所以capacity2q+1与Fstar的s层改善成立；不能把X=0的进一步rank下降用于未知X。

Whole determinant的row/column Laplace展开由各residue同阶minor的乘积组成；优化Σmρ=h与其capacity约束给all-coefficient valuation下界。Normalization的E_p=2Σfloor(i/p)确实需要扣掉，因h<M<p²。各Fstar离散凸：一般相邻差递增，δ在m=1处仅使两个相邻差相等，未破坏凸性。因此“取最小h个marginal increments并按前缀选取”是合法精确有限模型，不需数值solver来当证明。

Q_n=∏p p^ell_p的signed ratio使J(X)/Q_n∈Z[X]。Positive finite valuations也属于common content，不应丢掉。此为可保证的content下界，仍不是global primitive gcd的精确等式。Specialization X=u/v需付v^h，固定a,b分母同理；这些是O(n)但有限模型不能省。Coarse主率sB(B−κ)是clearing-cost upper bound，非actual denominator的lower bound。

## 4. 满rank residue与辅助素数：精确费用没有丢失

Arithmetic A24的confluent Vandermonde每对nodes差的四次幂进入detY，Gram determinant平方后为八次幂。Local2×2blockdet=−W²U²，所以满rank identity准确消去V，保留U和node differences。Unit条件下其valuation与F_s(2q+2)一致；ρ=0的U₀=0使该满rankdet零，与rank1head相容。它不是whole-matrix determinant的某个无条件主项。

Auxiliary n=2m、p=(B+κ)m+1时，bad nodes数恰d=(B−κ)m、h=2d；d<p、N<2p、4m+d<p由κ>2得到。Lucas/carry确保每个bad W是unit，C_j的principal coefficient是2/p；fixed weightleading U=−u p^{−(s−1)}、V=−(s+1)u p^{−s}，不含X leading term。Hermite pairs的Taylor误差与j<p贡献均在scaled form中为p-integral误差。Unit2×2blocks的det=−u²W²给nonzero constant polynomial reduction。

A30a与lattice P20的指数手核通过。Unscaled Hermite cardinal basis在monomial Z_p lattice上unimodular，因为d<p且node differences为units。Scaled pairs的T有valuation3d；从unit scaled determinant返到monomial form付6d，再扣factorial fee：

\[
v_p^{\rm Gauss}J=-h(s-1)-2(h-p)_+.
\]

一般B>3κ允许h≥p，且h<2p，所以factorial费正是2(h−p)_+；s5的B5/6/8、κ4均h<p。Scaled reduction是nonzero constant，因此每个p-integral specialization也达同一valuation并nonzero；固定有理specialization避开分母后成立。Dirichlet给无穷auxiliary primes，非零性来自这个算术机制，未使用 signed analytic weight正性。

在原布局p>s+1的更强条件下，EE leading coefficient unit。Schur elimination的off-diagonal multiplier在pZ_p，congruence unimodular；剩余FF leading coefficient是uD/(s+1)，符号为正。Actual Smith exponents恰q个−s及q个−(s−2)，minor ideals随后确定。Primitive multiplier的p-valuation与Gauss coefficient最低值准确对应，因此primitive polynomial modp仍是nonzero constant。单个auxiliary prime的费用只为O(n log n)，不能据此推出whole-prime n² cost下界。

## 5. Head correction、pairing subspace与解析比较

Arithmetic A31–A33与lattice P13–P14的contour/kernel signs和triple-zero crossing通过；s5 head是−bΣR'''(m)P(m)Q(m)，evaluation到2n个nodes满射、weights均非零，故actual rank精确2n。它不能作为fixed kernel常数丢掉。

Obvious subspaceP=S_{2n}A维数n。Paired subspace中m′=2n+1−m、factorial numerator相同而sign相反；约束P(m)/d_m=P(m′)/d_m′使每对head bilinearexactlycancel。n个disjoint evaluation constraints独立，故dimension2n；它包含n维evaluation kernel并给rank2n head的一半isotropic部分，确为最大isotropic选择。LeadingX Gram仍positive，target polynomialdegree2n，但不提供新restrictednonzero或arith/energy费用。

第一对约束的真实ratio d_{2n}/d₁=binom(8n,2n−1)，Stirling给(16log2−6log3)n+o(n)的row projective height。未饱和的整系数row不是已经primitive的integral-lattice basis。需要实际primitive gcd、saturation、basis norms或index时须另算；最终稿已经采用raw integer-row wording并明确这些费用。这个约束的rational kernel合法，并没有因此免费得到matchingn²总费用。

恢复zeroorderκ≥s−1确实消去全部crossing，与本文作者的[解析证明](cdt_odd_mixed_double_pole_analytic_decay_20261006.md) D24–D31使用的same rational function、sameh、samefactorialnormalization相容。该解析稿已通过root及arithmetic同行的全读独审；本记录不把自己稿算自己的独立审阅。

## 6. 审阅结论与严格范围

Arithmetic final452b的A1–A14/A30a与lattice final93c9的P1–P9全部声明范围独审通过。没有将Lai weight4的30.83/31.614直接转移到新family，也没有将coarse或LP优化cost upper bound当作actual不可改善下界。

已经有真实单目标polynomial、finite all-place common-content模型、generalrestorednonzero、精确auxiliarySmith/minor/factorial费用和head-free rational subspaces；新的ζ、L或Catalan数值结论仍须同一normalizeddeterminant的strict arithmetic/analyticmargin。No strictmargin从本combinedreview自动产生。

本审阅新PDF下载0、数学producer0、old/peer producer execution/import/rerun0。仅PowerShell read/hash和sourcePDF只读抽取；保存后实际全文回读并freeze，最终reviewSHA由root另登记，避免自引用hash。
