# A rational Taylor deformation of the canonical W7 period: an endpoint obstruction

2026-10-07. NEW isolated paper analysis. The numerical target is the canonical wheel period 24024 zeta(7), retaining its unknown numerical irrationality. This is one concrete matrix deformation, not the already excluded classical polylogarithm suspension. It has an explicit rational Taylor germ and a complete all-prime coefficient model. It fails the proposed single-relation mechanism for filling x=1 before an actual closed differential rank can be supplied. No irrationality, linear independence, or theorem about all possible wheel deformations is claimed. No producer, prime scan, PSLQ, Maple code, or numerical determinant experiment was run.

## 1. Primary input, selected source reading, and the index distinction

The primary input is [Brown--Schnetz, wheel classes, v3](https://arxiv.org/html/2402.06757v3), Theorem 1, the matrix and examples in Section 1.1, and Lemma 57/Corollary 58 in Section 8.1. These passages were actually read through the browser. For the positive orientation of its simplex,

\[
 I_{W_n}(\omega^{2n-1})=n\binom{2n}{n}\zeta(n),\qquad
 \omega_X^j=\operatorname{tr}((X^{-1}dX)^j).
 \tag{V1}
\]

For W7 the exponent is 13 and the period is 24024 zeta(7). Its positive density is

\[
 26\left(\Psi^{-2}+60S\Psi^{-3}+360S^2\Psi^{-4}\right)|\Omega|,
 \qquad S=\prod_{i=1}^7 s_i.
 \tag{V2}
\]

Here t_i are the seven rim variables, s_i the seven spokes, and Psi=det Lambda is the wheel graph polynomial. The sign of the differential form is absorbed only by the fixed orientation of the integration simplex. All three coefficients in V2 are positive. This is a canonical integral, not the usual Feynman residue. As a checked comparison, W5 has canonical exponent 9 and period 1260 zeta(5), whereas its usual Feynman residue has weight 7. No claim about an unknown target is obtained by relabeling that known comparison.

The general positive-density statement in Corollary 58 has terms S^(k-1)/Psi^(k+1), 1<=k<=(n-1)/2, with positive coefficients for odd n. The geometric estimates below work for those terms; only W7 is used as the numerical target in this note.

[Brown, Non-linear geometry of multiple zeta values, v1](https://arxiv.org/html/2604.22735v1), Sections 5.1--5.3, was read for the rational matrix-form definition, projective invariance and the difference between a finite canonical period and a meromorphic parameter germ. No motivic injectivity or numerical freeness is imported. The displayed W3 trace exponent in Section 4.5 and denominator indices in Section 5.4 are not used; the precise wheel formulas are taken from the versioned Brown--Schnetz primary paper.

The archived OpenAI Deligne--Drinfeld source was actually read at `sections/07-holonomy.tex:100--159,510--552`. It proves regularized transport after removing singular frames, and uses positivity of convergent zeta coefficients without asserting arithmetic independence. These facts do not turn an unregularized full germ into a meromorphic one. They motivate checking the exact parameter germ below; they do not furnish its differential rank.

New full HTML snapshots of the two selected public primary papers, with URL/byte/SHA receipts, are in `literature/cdt_wheel_rational_deformation_sources_20261007/`. Downloading those complete files is not counted as complete reading of either paper. The earlier carrier notes `cdt_new_repository_carriers_20261007.md` and `cdt_theta_all_weights_carrier_boundary_20261007.md` were read to avoid reusing their excluded polylogarithm towers. The specific wheel deformation below and its corner obstruction are new to this analysis.

## 2. One actual matrix deformation

Fix the cycle basis of the primary wheel matrix. On the simplex

\[
 \sigma=\{t_i,s_i\ge0:\ \sum_{i=1}^7(t_i+s_i)=1\}
\]

put

\[
 \Lambda_{ii}=t_i+s_{i-1}+s_i,\qquad
 \Lambda_{i,i+1}=\Lambda_{i+1,i}=-s_i,
 \tag{V3}
\]

with cyclic indices, so s_0=s_7. Every other off-diagonal entry is zero. This is a positive-definite matrix in the interior; explicitly its quadratic form is

\[
 v^T\Lambda v=\sum_i t_i v_i^2+
 \sum_i s_i(v_i-v_{i+1})^2.
\]

For the complex parameter x near zero define

\[
 X_x=(1-x)I_7+x\Lambda,\qquad
 K(x)=\int_\sigma\operatorname{tr}
 \left((X_x^{-1}\,x\,d_{t,s}\Lambda)^{13}\right).
 \tag{V4}
\]

The simplex is oriented as in V1--V2; the differential is only in the edge variables, not the total differential including dx. The shift I_7 depends on the fixed cycle basis. It is a specified deformation, not a claim of cycle-basis invariance for all regularizations.

Since sigma is compact and X_0=I_7, a uniform Neumann expansion exists in a complex disk around zero. V4 is a genuine holomorphic germ there and starts at degree at least 13. Its Taylor coefficients are rational, as the next section proves without taking an integral whose constant Taylor coefficient is already the unknown period.

## 3. Complete finite-prime model at the Taylor origin

Expand

\[
 X_x^{-1}=\sum_{a\ge0}(-x)^a(\Lambda-I_7)^a.
\]

In coefficient degree M>=13 the thirteen inverse factors have total Neumann degree M-13. The thirteen factors d Lambda have constant integer coefficients. Thus the coefficient of the integrand, in any affine simplex coordinate chart, is an integer polynomial in the edge variables of degree at most M-13, times the standard oriented thirteen-dimensional volume form. There are only finitely many such terms at each degree. Uniform convergence justifies integrating the power series.

For a monomial with fourteen nonnegative exponents a_i and D=sum a_i<=M-13, the standard simplex integral is

\[
 \int_\sigma\prod_i y_i^{a_i}|\Omega|
 =\frac{\prod_i a_i!}{(D+13)!}.
 \tag{V5}
\]

For a prime power Q=p^j, its denominator valuation at that layer is

\[
 \left\lfloor\frac{D+13}{Q}\right\rfloor
 -\sum_{i=1}^{14}\left\lfloor\frac{a_i}{Q}\right\rfloor
 =\left\lfloor\frac{13+\sum_i(a_i\bmod Q)}{Q}\right\rfloor
 \le13.
\]

There are no nonzero factorial layers with Q>M. Consequently, writing ell_M=lcm(1,...,M), ell_0=1,

\[
 \boxed{\ell_M^{13}[x^M]K(x)\in\mathbb Z\quad(M\ge1).}
 \tag{V6}
\]

For M<13 the coefficient is zero. This includes p=2, all small primes, and every prime power. Integer polynomial cancellations can only improve the safe cap. It is a fixed-width LCM model with thirteen width-one columns and no degree-dependent scaling. Its sharp denominator cost and the caps of a complete closed differential basis have not been computed.

For a fixed rational u and an integer d_u>0 with d_u u integral, the attempted single-relation suspension

\[
 F_u'(x)=\frac{K(x)-24024u}{1-x},\qquad F_u(0)=0
 \tag{V7}
\]

has rational Taylor coefficients and the complete cap

\[
 d_u M\ell_{M-1}^{13}[x^M]F_u\in\mathbb Z.
 \tag{V8}
\]

These are actual coefficient identities. They do not assert that this suspension has a usable full holonomic carrier or that a relation zeta(7)=u fills its endpoint.

## 4. The exact moving domain and the endpoint value

For 0<x<1 set

\[
 T(x)=7-6x,\quad \lambda=x/T(x),\quad
 c=(1-x)/T(x),\qquad \lambda+7c=1.
\]

The edge map is

\[
 t_i'=\lambda t_i+c,\qquad s_i'=\lambda s_i.
 \tag{V9}
\]

It maps sigma bijectively onto the truncated simplex

\[
 \sigma_c=\{\sum_i(t_i'+s_i')=1:\ t_i'\ge c,\ s_i'\ge0\}.
\]

Linearity of Lambda gives X_x=T(x)Lambda(t',s'). For fixed x, d_edge T=0, so X_x^-1 d_edge X_x=Lambda(t',s')^-1 d_edge Lambda(t',s'). Thus V4 is exactly the integral of the original wheel form over sigma_c. No determinant Jacobian is omitted: it is the pullback of the thirteen-form itself under V9, whose affine Jacobian is lambda^13. The orientation is preserved since lambda>0.

By V2, K(x)>0, and these domains increase to sigma as x increases to 1. Monotone convergence, or the integrability proved again in Section 6, gives

\[
 K(1^-)=I_{W_7}(\omega^{13})=24024\zeta(7).
 \tag{V10}
\]

This is an endpoint value and not a statement about a holomorphic endpoint germ. The deficit is exactly the integral of the positive density over sigma minus sigma_c.

## 5. A positive triangle-corner lower bound

Use rim t_1 and its adjacent spokes s_1,s_7 as the three small variables. Eliminate t_2 using the simplex equation. The remaining ten nonsmall edge coordinates range in a fixed positive box about 1/11, chosen sufficiently small. For all sufficiently small t_1,s_1,s_7, the eliminated t_2 remains uniformly positive. All the nonsmall rim coordinates are then at least a fixed a>0. This box has a fixed positive ten-dimensional volume, and |Omega| is the ordinary volume in the resulting affine chart.

Partition Lambda into its first row/column and the other six:

\[
 \Lambda=\begin{pmatrix}r&v^T\\v&B\end{pmatrix},\qquad
 r=t_1+s_1+s_7,
\]

where the two nonzero entries of v are -s_1 and -s_7. In this box B>=a I_6 and det B is bounded above by a constant C_B independent of the small variables. The Schur formula and positivity give

\[
 0<\Psi=\det B\,(r-v^TB^{-1}v)\le C_Br.
 \tag{V11}
\]

The leading positive term 26/Psi^2 in V2 is therefore at least C/r^2 for a fixed C>0. There is no cancellation by the other two terms, which are nonnegative.

Within the excluded region take 0<t_1<c/2, z=s_1+s_7 in [2c,delta], and s_1 in [z/3,2z/3], with fixed delta>0 sufficiently small. The change (s_1,s_7) to (s_1,z) has Jacobian 1. Its s_1 interval has length z/3, and r<=5z/4. Integrating V11 over this region and the nonsmall box proves

\[
 \boxed{K(1^-)-K(x)\ge C_0 c\log(\delta/(2c))}
 \tag{V12}
\]

for all sufficiently small c>0, with C_0>0. The region is excluded because t_1<c, while its other rims remain positive. Since c/(1-x)->1, the endpoint difference is not O(1-x). This proves a nonmeromorphic unramified germ with a finite endpoint limit. It is not an evaluation of the exact leading logarithmic coefficient.

V12 alone would not exclude finite ramification: a square-root cusp also satisfies such a lower bound. That missing issue is paid in the next two sections.

## 6. Fractional rim moments and an upper bound of every order below one

For the three terms of V2 it suffices to prove, for every rim edge r and 0<alpha<1,

\[
 \int_\sigma t_r^{-\alpha}
 \frac{S^{k-1}}{\Psi^{k+1}}|\Omega|<\infty,
 \qquad k=1,2,3.
 \tag{V13}
\]

Here t_r is the coordinate normalized by sum edges=1. The following power count also proves this for the canonical terms of any odd wheel n>=5, with k<=(n-1)/2. For a nonempty proper edge subset Gamma, let r_Gamma and s_Gamma be its numbers of rim and spoke edges, and let h_Gamma be its cycle rank. Its scaling exponent before the fractional factor is

\[
 A_\Gamma=r_\Gamma+k s_\Gamma-(k+1)h_\Gamma.
 \tag{V14}
\]

If Gamma lacks at least one rim edge, its rim subgraph is a forest of paths. If h_Gamma=0, A_Gamma=r_Gamma+k s_Gamma>=1. Otherwise, each cycle is formed by spokes joined through that rim forest, so h_Gamma<=r_Gamma and h_Gamma<=s_Gamma-1. These inequalities can be seen by grouping the path components meeting the selected spokes: their contributions are the number of spokes in that component minus one. Thus A_Gamma>=k>=1. If Gamma contains every rim and at least one spoke, the graph containing its center is connected and h_Gamma=s_Gamma; properness gives A_Gamma=n-s_Gamma>=1. If it contains the full rim and no spoke, h_Gamma=1 and A_Gamma=n-k-1>=1. Hence every proper subset has A_Gamma>=1.

For completeness this power count implies convergence by an elementary ordered-sector argument. Partition projective space into sectors ordering the 2n edge coordinates and set the largest coordinate to 1. With nested variables u_j in [0,1], write the j-th smallest edge as u_j...u_(2n-1). The volume Jacobian is the product of u_j^(j-1). The graph polynomial is a sum of positive complementary-spanning-tree monomials. A greedy spanning tree, adding edges from smallest to largest, contains a maximal forest in every nested prefix Gamma_j; its complementary monomial therefore has exponent h_Gamma_j in u_j. This one positive monomial lower-bounds Psi simultaneously in every nested variable. The numerator and Jacobian bound the sector integrand by a constant times

\[
 \prod_j u_j^{A_{\Gamma_j}-1
   -\alpha\mathbf 1_{\{r\in\Gamma_j\}}}.
\]

All exponents exceed -1 by V14 and alpha<1. Normalizing the rim variable from this largest-edge chart to sum edges=1 multiplies the fractional factor by at most (2n)^alpha. There are finitely many sectors. This proves V13, and at alpha=0 proves ordinary integrability as well. The spanning-tree description follows directly from the graph polynomial: Cauchy--Binet for Lambda=C diag(edges) C^T gives complementary spanning trees with unit nonzero minors. No numerical convergence extrapolation is used.

Since sigma minus sigma_c is contained in the union of the seven sets t_r<c, the elementary inequality 1_(t_r<c)<=c^alpha t_r^-alpha gives, for each 0<alpha<1,

\[
 \boxed{0<K(1^-)-K(x)\le C_\alpha c^\alpha.}
 \tag{V15}
\]

The constants may depend on alpha. This is all that is needed for finite ramification, and is not a sharper claimed asymptotic expansion.

## 7. Finite ramification and the failed single relation

Suppose a local holomorphic map satisfies phi(z_0)=1 and

\[
 1-\phi(z)=a(z-z_0)^ell(1+O(z-z_0)),\qquad a\ne0,
\]

with finite ell>=1. Consider the continuation which transports the germ K along 0<x<1. If this pullback were meromorphic at z_0, its finite limit V10 would remove any pole, making it holomorphic. A nonconstant holomorphic germ has a first nonzero endpoint difference of some integer degree j. Along a local inverse of the positive real path 1-x=h, this implies

\[
 |K(1^-)-K(x)|\asymp h^{j/ell}.
\]

V15 holds for every alpha<1, and c/h->1. Therefore j/ell>=1. Since j is integral this means j>=ell, and the same analytic expansion would force the difference to be O(h). V12 contradicts that conclusion. The constant-germ case contradicts the strictly positive deficit directly. Thus no finite ramification makes this transported endpoint germ meromorphic.

Now impose only the proposed contradiction relation zeta(7)=u in Q. It identifies K(1^-)=24024u and cancels only the constant endpoint value in V7. If F_u were meromorphic, then

\[
 K(x)=24024u+(1-x)F_u'(x)
\]

would be meromorphic, contradicting V12. The same reasoning survives every finite ramification. Indeed differentiating the pullback gives K(phi)=24024u+(1-phi)(F_u composed phi)'/phi', a meromorphic expression if that pullback were meromorphic. Dividing by phi' introduces at most a finite pole. Thus the single numerical relation does not control the complete target branch.

Adding or subtracting any rational function analytic at the endpoint, with coefficient depending on u, cannot remove this obstruction. A different deformation or an explicitly paid subtraction of its whole singular family is required; its constant period value alone does not do that work.

## 8. What this window did and did not supply

V4 is an actual Q-Taylor deformation of the specified W7 matrix integral. V6--V8 give complete fixed-type coefficient models including all prime powers. V9 proves its exact moving domain; V11--V15 establish the positive corner deficit and sufficient upper estimates to exclude finite ramification. These facts reject this concrete use of the single relation zeta(7)=u to fill x=1 before a rank-cost comparison. They do not exclude a CDT domain which continues to omit x=1, nor a different rank argument for this same deformation. The actual closed rank and its tau have not been calculated, so neither of those alternatives is classified here.

An actual finite closed differential space, its exact function rank, and the integer models for every row in such a space have not been constructed here. A general assertion that parameter integrals are holonomic is not a substitute for those inputs. Because this proposed x=1 filling mechanism has failed its necessary complete-germ condition, no computation of its putative Picard--Fuchs rank or tau is undertaken to present that mechanism as a successful candidate. In particular the actual independent span of 1 and K has dimension at least two, since K is not rational by its endpoint obstruction, but this is not the dimension of a derivative-closed carrier.

The bounded window therefore provides an explicit feasibility obstruction rather than a new numerical theorem. It suggests that a viable wheel deformation must isolate a vanishing-cycle or boundary correction with a paid full branch, not merely preserve the canonical period at x=1. Neither Brown's graph-homology nonvanishing nor the OpenAI rational Lie descent pays that missing correction. The outcome does not rule out another wheel realization, another relation-sensitive carrier, or another method for zeta(7).

Actual execution scope: selected primary browsing and two HTML downloads; archived source passages as listed in Section 1; new source/archive writing and paper derivation only. No mathematical code, old producer, prime scan, or finite coefficient experiment was run.

**2026-10-07 independent review receipt.** Root actually FULL read all eight sections V1--V15 and independently checked the Neumann/simplex all-prime model, exact truncated-domain pullback, positive triangle lower bound, proper-subset power counts and greedy sectors, and the upper bound for every alpha<1 combined with a finite local inverse path. Mathematical PASS. Root requested the x=1-mechanism scope qualification in this section; the author incorporated it. Root also independently read the Brown--Schnetz primary HTML passages containing Theorem 1, the matrix/W5--W7 formulas, and Lemma 57/Corollary 58, confirming the indices and positive coefficients. This is not a full primary-paper proof audit. The author subsequently performed the final FULL reread of this revised note and its source scope.
