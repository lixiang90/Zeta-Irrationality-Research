# Catalan / pi-squared mixed target: primary source and reading scope

Date: 2026-10-07. Independent read-only research by `universal_normalization`; no main manuscript, manifest, or producer was changed. The MPIM PDF named below is the only new downloaded source in this audit. Existing local PDFs were reused. No Lean proof or supplied mathematical program was executed.

The task is to test novelty of excluding

\[
aG+b\pi^2=u,\qquad a,b,u\in\mathbb Q,\quad a\ne0,
\]

for the carrier \(A=\arctan x, B=T_2, S=A^2, F'=(aB+16bS-u)/(1-x)\), with the original branch filled at \(x=1\).

## 1. Precise outcome and logical scope

This primary search did not locate an unconditional theorem establishing the Q-linear independence of \(1,G,\pi^2\), or irrationality of every mixed \(aG+b\pi^2\) with \(a\ne0\). This is a bounded literature-search conclusion, not a claim to have verified all publications or all proofs. Two September 2026 preprints claim that G alone is irrational; their statements do not settle this mixed target. The Sun claim has a specific published primary critique. That critique predates, and does not refute, the independent September 24 OpenAI manuscript.

Even if G irrationality is granted, a relation with \(b\ne0\) would make \(G=u/a-(b/a)\pi^2\) transcendental, hence irrational. Therefore separate irrationality statements do not contradict the mixed relation.

Directly from the defining series,

\[
\zeta(2,1/4)=\pi^2+8G,\qquad
\zeta(2,3/4)=\pi^2-8G.
\]

Thus the complete mixed target is equivalent to Q-linear independence of \(1,\zeta(2,1/4),\zeta(2,3/4)\). The homogeneous \(u=0\) subproblem is the Chowla--Milnor \((k,q)=(2,4)\) problem; adjoining 1 is a stronger assertion. The conductor-3 CDT theorem cannot be substituted for this conductor-4 statement.

## 2. Primary sources actually read

| Source | Actual reading in this audit | Applicable conclusion and limits |
|---|---|---|
| [Rivoal--Zudilin, 2003](https://rivoal.perso.math.cnrs.fr/articles/betacatalan.pdf) | Local PDF pp.1--3; public author PDF opened. | Theorems 1--2 give family dimension growth and at least one irrational among beta(2),...,beta(14). They do not give the mixed target. No full-proof verification was claimed. |
| [Zudilin, 2019, v2](https://arxiv.org/pdf/1804.09922v2) | Public PDF introduction and Theorem 1, p.1. | At least one of beta(2),...,beta(12) is irrational; not identification of G or independence from pi-squared. |
| [Viola--Zudilin, MPIM 2014-26](https://archive.mpim-bonn.mpg.de/1914/1/preprint_2014_26.pdf) | Public PDF printed pp.1--3, Main theorem; Proposition 6.1, printed pp.34--35, including its explicit real rational parameter conditions. | Independence of 1, Li1(1/z), Li2(1/z), Li2(1/(1-z)) for integers z>=9 or z<=-8, and certain rationals. The theorem does not apply to the nonreal argument i. |
| [Lai--Li, v2, April 9, 2026](https://arxiv.org/html/2505.12687v2#S1) | Local PDF pp.1--2 read without output truncation; public abstract/history and HTML beginning of section 1. A larger initial extraction was truncated and is not counted as additional reading. | Section 1 identifies the conductor-4 beta subspace and records other Chowla--Milnor cases as open at that date. The new result is a dimension lower bound as q tends to infinity, not a theorem at q=4. |
| [Sun, v1, September 3, 2026](https://arxiv.org/abs/2609.04176v1) | Public abstract and current submission history; local PDF pp.1--2 including Theorem 1.1. | Claimed result is only G irrationality. The current arXiv history showed only v1. No independent verification of its 20-page proof was performed. |
| [Wachs, v1, September 16, 2026](https://arxiv.org/html/2609.22339v1) | Abstract, section 2 rank discussion, sections 3.3--3.4, exact dyadic identity, Corollary 3.5 and its proof, remarks 3.6--3.7. | The printed Sun derivation leaves an order-B-squared dyadic term unaccounted for. The conclusion is that Sun's displayed proof is incomplete. Finite computations alone do not refute an asymptotic little-o claim. It says nothing about the truth of G irrationality or the later OpenAI proof. Supplied scripts were not rerun. |
| [Eskandari, September 22, 2026](https://arxiv.org/html/2609.26354v1#S1) | Abstract, theorem 1.1 and sections 1.2--1.3. | Explicit approximations have exponent >=0.62. This construction does not itself prove G irrationality or the mixed target. Its polynomial combinations and motivic-to-hypergeometric identity are useful construction inputs. |
| [OpenAI, September 24, 2026](https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf) | Repo `introduction.tex`, `foundations.tex`, `conclusion.tex` FULL; reference list and overview searched; archived PDF receipt checked. | Main theorem is G irrationality. The exact moment decomposition and Taylor contact deliberately cancel zeta(2), so rationality of determinants follows from G in Q. The whole 44-page proof and its certificates were not independently verified in this audit. |
| [Eskandari--Murty--Nemoto, v3, August 29, 2026](https://arxiv.org/html/2510.20648v3) | Public version history, section 1, Proposition 5.3.1, section 6 text and its period matrices, overview 7.1 and Proposition 7.3.1 statement. Commutative diagrams absent from HTML text were not separately rendered. | A two-dimensional Catalan motive and explicit forms in 1,G; no numerical independence theorem for 1,G,pi-squared. |
| [OpenAI, Deligne--Drinfeld, September 23, 2026](https://github.com/openai/math/blob/main/preprints/The-Deligne-Drinfeld-conjecture-September-23-2026/paper.pdf) | Repo `01-introduction.tex` FULL and README; existing source receipt checked. | Claimed isomorphism of the ordinary Grothendieck--Teichmueller Lie algebra with the free odd-weight Lie algebra. Neither period injectivity nor conductor-4 numerical independence is a stated result. |

## 3. Exact constructive inputs for a mixed approach

The EMN original bases give, in Eq. (6.3),

\[
P_C=\begin{pmatrix}1&G\\0&-2\pi^2 i\end{pmatrix},\qquad
\operatorname{Gr}^W C=\mathbb Q(0)\oplus H^1(x^2+y^2=1)(-1).
\]

The introductory matrix uses a rationally rescaled lower entry \(i\pi^2\). Over Q(i) the weight-four quotient becomes Q(-2). Over Q, rational basis changes in C add imaginary rational multiples of pi-squared to the off-diagonal period, not the real term \(b\pi^2\). The direct sum \(C\oplus\mathbb Q(-2)\) is an explicit three-dimensional joint period package containing 1,G,pi-squared. This is a structural construction, not a proof of minimal dimension or numerical independence. Distinct motivic components do not establish numerical independence without a period-injectivity input.

For the repo moment decomposition, set \(c_l=4^{-l}\binom{2l}{l}\), with zero for inadmissible indices, and define

\[
C_j(P)=\sum_i p_i c_{(i-j)/2},\qquad
H_j(P)=[t^j]\frac{tP(t)}{\sqrt{1-t^2}},\qquad D_j=[t^j]D(t).
\]

Then the period part of \(M(P,j)-(3/2)Z(D,j)\) is exactly

\[
4C_j(P)G+\frac{\pi^2}{4}\bigl(H_j(P)-D_j\bigr).
\]

To specialize to a rational number under the mixed hypothesis, impose

\[
H_j(P)-D_j=16\frac ba C_j(P).
\]

The resulting period part equals \((4C_j(P)/a)u\). This is a derived finite rational linear constraint for joint lattice design. Its two coefficient extractions are at different ends: C_j is the nonnegative-power coefficient in the Laurent expansion of \(P(t)/\sqrt{1-t^{-2}}\) at infinity, whereas H_j comes from zero. Changing D in this manner requires new support, integrality, prime-valuation and real-place estimates; the existing Chebyshev proof does not transfer automatically.

## 4. Independent branch and glue check

These are mathematical derivations in this audit, not literature theorems. If all carrier pullbacks are holomorphic and \(g=A\circ\varphi\), then \(\varphi=\tan g\). Finiteness of phi omits \(\pi/2+\pi\mathbb Z\); holomorphy of B omits \(\pi\mathbb Z\setminus\{0\}\), because at a zero of phi of order k with \(g=n\pi\ne0\), the differential \(g\,d\varphi/\varphi\) has nonzero residue \(kn\pi\).

At x=1, generator continuation gives \(A=\pi/4+\pi d\), \(B=G+(i\pi^2/2)N\), with integers d,N and \(N\equiv d\pmod2\). If b is nonzero, the original mixed relation and the removable-pole condition for F force N=d=0. When b=0 only N=0 follows.

The parent-specified surface gluing W with D(3pi/4,epsilon), identifying only the upper half disk, passes the independent topology/branch check for 0<epsilon<pi/4. The cross-chart graph is relatively closed: a limit on the real diameter is absent from W, and a limit on the upper semicircle is absent from the disk. The quotient is open, Hausdorff and second countable. Both charts and their intersection are simply connected, so van Kampen gives a simply connected surface. It supports the global B differential \(2g\,dg/\sin(2g)\); the mixed hypothesis removes the sole F pole at g=pi/4.

Uniformization and lifting tan(g) to the omitted-pair disk cover exclude the plane by Liouville. Proper inclusion of W gives strictly larger normalized radius r_R>pi by Schwarz. With z_1 the disk coordinate of the canonical g=pi/4 point, choose \(\max\{|z_1|,\pi/r_R\}<\rho<1\). The restricted common map extends beyond the closed disk and has derivative rho*r_R>pi. Its CDT double-circle functional is finite and pays for interior extra fibers via the exact Jensen formula

\[
J_\rho=\log(\rho r_R)+\int_{\mathbb T}\sum_{\substack{\zeta\in\mathbb D\\\varphi_\rho(\zeta)=\varphi_\rho(w)}}\log\frac1{|\zeta|}\,d\mu(w).
\]

Boundary zeros contribute zero. This is the double-circle functional in [CDT Eq. (2.2)](https://arxiv.org/html/2510.04156v1#S2), not a single-circle ratio integral. The formula shows J>=log|phi'(0)|; a derivative improvement alone does not establish a strict holonomy inequality.

After the source work, the independent reviewer actually read the entire nine-section `research/cdt_mixed_catalan_pi2_geometry_20261007.md`, M1--M30, without truncation. The ranks, complete branch classification, explicit slit map, finite-rho inner-function bound, gluing, strict radius argument, finite-fiber Jensen bound, the displayed all-prime safe cap, and the displayed two-response basis obstruction were rederived on paper and passed. The separate arithmetic manuscript and its natural-family minimum were not reread or credited as part of this check. No change to the geometry manuscript was made.

## 5. Local source fingerprints

New public source: `viola_zudilin2014_dilogarithmic_li_mpim1426.pdf`, 42 pages, SHA256 `39b606010cb25a07595310de80208e3031d0c3b7046752f9a97f32a2eb64799a`.

Reused archived sources, each hash recomputed except the OpenAI PDF whose existing receipt was inspected:

| Local file under literature | SHA256 |
|---|---|
| `eskandari_murty_nemoto2025_catalan_motive.pdf` (v3, 39 pages) | `199ae70c14c6763b0065e1c9fbb3640e38ad60a55dd739d3d2202e512db1d858` |
| `lai_li2026_chowla_milnor_v2.pdf` (39 pages) | `3ae91a7d6eef13d6a88c8219d317d79af1dad2946b2ecd9cdd2da6cc082c822a` |
| `sun2026_catalan_claim.pdf` (v1, 20 pages) | `0aa3bc7e80be3658630fa5d82cb773cba7ec8692d9855a70e71e47f235d2819f` |
| `catalan2026_claim_critique.pdf` (v1, 8 pages) | `82940e9304cc0b36662ae3b56cf1bfa452deab2e1f1860efeb8026dd40b289ab` |
| `eskandari2026_improved_catalan_approximations.pdf` (v1, 11 pages) | `47bc30efc97bb68c58f1cbacaafdf54a4de596183964a7609ddff11c8764ece6` |
| `rivoal_zudilin2003_catalan_relatives.pdf` (17 pages) | `24da4f15fcb76df57e6bfc9150d6753ed32e20538b6589023baa33c487744edf` |
| `openai_math_2026_special_values_20261007/openai2026_catalans_constant_irrational_20260924.pdf` (44 pages; existing receipt) | `4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e` |

