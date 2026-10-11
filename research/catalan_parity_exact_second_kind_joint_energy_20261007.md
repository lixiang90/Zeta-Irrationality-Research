# Parity carrier: an exact second-kind polynomial and joint contact energy

2026-10-07, round216. NEW paper derivation for the actual q=0 carrier. This proves an explicit secondary Jacobi identity, Vandermonde minors for all residual coefficient rows, and the exact minimum input-energy Gram after all permitted tails. It also supplies a complete-D operator bound. The mixed M+D exterior and actual rational relation-point nonzero remain open. The input-energy Gram is not silently identified with the actual moment or output Gram.

## 1. Fixed actual carrier and the relevant input norm

Retain A=19N,h=2N,b=11N,K=8N,n=44N−1,L=55N−1,m=36N−2 and delta=n−m=8N+1 from [the parity note](catalan_mixed_parity_positive_kernel_20261007.md). All h are even. Put
\[
Q_d(x)=P_d^{(h-1/2,-1/2)}(2x-1),\quad
d=K+1,\ldots,n,
\]
\[
d\nu_0=\frac{dx}{\pi\sqrt{x(1-x)}},\quad d\nu_h=(1-x)^h d\nu_0,
\quad R_d=(1-x)^h Q_d.
\]
Let B_d be the exact polynomial second-kind transform in P5. Every allowed contact lift is
\[
\mathcal D_C(x)=x^{A+1}(1-x)^h E(x),\quad
\deg E<n,\quad
E\equiv B_d/(1-x)^h\pmod{x^m}.
\tag{E1}
\]
The entire section freedom is x^m(1-x)^h times a polynomial of degree <delta, corresponding exactly to the delta permitted pure-D tails. The signed actual correction is D_mu=−mu D_C. Work with the input norm
\[
\|x^{A+1/2}(1-x)^h E\|_{L^2(dx)}^2
=\int_0^1 x^{2A+1}(1-x)^{2h} E(x)^2dx.
\tag{E2}
\]
This is chosen for the complete D kernel, not as a new integer-row normalization.

## 2. The secondary Jacobi identity, including negative parameters

For d>=1 and integer h>=0, define D=d+h−1. Then
\[
\boxed{B_d(x)=(-1)^h P_D^{(1/2-h,\,1/2)}(2x-1).}
\tag{E3}
\]
For our h, the sign is +. These parameters do not give a positive Jacobi orthogonality measure; only the polynomial definition and differential equation are used.

Here is a proof which does not assume an unverified second-kind formula. The shifted Jacobi equation for Q is
\[
x(1-x)Q''+[1/2-(h+1)x]Q'+d(d+h)Q=0.
\]
The basic differential equation and polynomial hypergeometric definition were independently checked in [DLMF Table18.8.1, row1](https://dlmf.nist.gov/18.8) and [18.5.7](https://dlmf.nist.gov/18.5.E7); their shifted forms and all following identities are derived here. Set S=(1-x)^h Q/\sqrt{x(x-1)} on the infinity branch. The logarithmic derivative of its prefactor is −1/(2x)+(h−1/2)/(x−1). Substitution gives
\[
\mathcal L S=0,\quad
\mathcal L=x(1-x)\partial_x^2+[3/2-(3-h)x]\partial_x+D(d+1).
\tag{E4}
\]
The exact second-kind decomposition is S=B_d+W_d with W_d=O(x^(−d−1)) at infinity, because Q_d has all nu_h moments through d−1 zero. The operator L maps the polynomial B_d to a polynomial, while L W_d=O(x^(−d−1)). Thus L B_d=0. A nonzero polynomial solution must have degree D: the two infinity degree roots are D and −d−1. The degree-D polynomial solution is unique up to scalar by comparing its highest powers successively; all lower-degree eigenvalue differences are nonzero. Its leading coefficient equals that of the Jacobi polynomial on the right in E3, with sign (−1)^h, since
\[
[x^d]Q_d=\binom{2d+h-1}{d},\qquad
[x^D]P_D^{(1/2-h,1/2)}(2x-1)
=\binom{2d+h-1}{d+h-1}.
\]
The two binomials are equal. This proves E3 for every stated d,h, not only sampled N.

## 3. Residual coefficient minors are exact Vandermonde determinants

Put u_d=d(d+h), c_d=binom(D+1/2,D). The finite hypergeometric polynomial at x=0 gives
\[
\boxed{[x^r]B_d=
\frac{(-1)^{h+D+r}c_d}{(3/2)_r r!}
\prod_{j=0}^{r-1}\{u_d+(j+1)(h-1-j)\}.}
\tag{E5}
\]
This includes the zero coefficients for r>D. Each displayed product is monic of degree r in u_d. Thus for any m distinct increasing allowed degrees d_1<...<d_m, writing C=( [x^r]B_(d_i))_(i,r), r=0,...,m−1,
\[
\boxed{|\det C|=
\frac{\prod_{i=1}^m c_{d_i}}
 {\prod_{r=0}^{m-1}(3/2)_r r!}
\prod_{i<j}(d_j-d_i)(d_j+d_i+h)>0.}
\tag{E6}
\]
The sign in E5 is removed by row/column signs. The Newton-to-monomial coefficient change is unit triangular. These statements pay every residual C minor for this basis, a stronger concrete statement than a generic nonzero minor. They still do not pay a minor of the full actual mixed moment at fixed rational mu,gamma.

The low E coefficients in E1 are a unit triangular transform of these low B coefficients, so their square determinant has the same absolute value. For the p=m+1 permitted Jacobi directions, every selection of m directions therefore gives nonzero coefficient determinant. This is a coefficient/contact assertion, not a numerical-period independence assertion.

## 4. Exact minimum energy after every permitted tail

Let G be the n-square positive beta Hankel matrix
\[
G_{uv}=B(2A+u+v+2,2h+1),\quad0\le u,v<n.
\tag{E7}
\]
Split the first m coefficients from the final delta coefficients, and write G in ll,lh,hl,hh blocks. Fixing low E coefficients c, the unique minimum of E2 is obtained at high coefficients −G_hh^(−1) G_hl c, with minimum c^t S_G c, where
\[
S_G=G_{ll}-G_{lh}G_{hh}^{-1}G_{hl}>0.
\tag{E8}
\]
This follows by completing the positive quadratic square. Every high coefficient is a permitted tail change, so this real optimization leaves any moment determinant containing all delta tails unchanged. It does not optimize an omitted-tail principal square.

For H_r(a,c)=det[B(a+u+v+1,c+1)]_(u,v<r), one has
\[
\boxed{\det S_G=
\frac{H_n(2A+1,2h)}{H_\delta(2A+2m+1,2h)}.}
\tag{E9}
\]
The denominator is precisely the high-coefficient Gram: no Jacobian or extra endpoint factor is inserted. For m selected unscaled Q rows let G_lift be the input Gram of their optimal complete lifts. The low coefficient transformation is unit triangular, so
\[
\boxed{\det G_{\rm lift}=(\det C)^2
\frac{H_n(2A+1,2h)}{H_\delta(2A+2m+1,2h)}.}
\tag{E10}
\]
This is an exact joint determinant rather than m separate norm bounds. Dividing the source rows by sqrt(rho_d) divides E10 by their product rho_d; log rho_d=O(log N), hence that operation has no N² leading term.

## 5. Its explicit N² leading term

Set X(t)=t² log(t)/2−t²/4, X(0)=0, and
\[
\mathscr H(a;b,c)=X(a)+X(b+a)-X(b)+X(c+a)-X(c)
-X(b+c+2a)+X(b+c+a).
\tag{E11}
\]
The exact beta Gram product follows from monic Jacobi norms, or the elementary beta determinant:
\[
H_r(a,c)=\prod_{j=0}^{r-1}
\frac{j!\,\Gamma(a+j+1)\Gamma(c+j+1)}
 {\Gamma(a+c+r+j+1)}.
\]
Uniform Stirling gives N^(−2) log H_(rN+O(1))(aN+O(1),cN+O(1))→Hscript(r;a,c). The quadratic changes from integrating −t in Stirling cancel in E11.

For any m-row selection out of d=8N+1,...,44N−1, omitting one row changes log|det C| only by O(N log N), uniformly over the omitted degree. In E6 log c_d=O(log N). The Vandermonde factors have an integrable diagonal logarithm; Riemann sums, splitting a narrow diagonal strip, give
\[
V_C:=\lim N^{-2}\log|\det C|
=\frac12\{X(90)-2X(54)+X(18)\}
-\frac{36^2}{2}\log36+\frac{36^2}{4}.
\tag{E12}
\]
Indeed the d-difference triangle contributes 36² log36/2−3·36²/4, the denominator product contributes −36² log36+3·36²/2, and the sum triangle is one half of the double integral of log(s+t) over 9<=s,t<=45. Its antiderivative is X(t)−t²/2, giving E12. The powers of log N cancel exactly between the Vandermonde and factorial layers.

Therefore
\[
\boxed{J_D:=\lim N^{-2}\log\det G_{\rm lift}
=2V_C+\mathscr H(44;38,4)-\mathscr H(8;110,4).}
\tag{E13}
\]
This limit is exact for the complete optimal input lift. It is not an asymptotic equality for the full mixed moment determinant or its output Gram.

## 6. Complete D kernel and the actual output bound

On unweighted L²(0,1), let C_0 g(y)=int_0^1 g(x)/(1−xy)dx. The unitary substitution x=(t−1)/(t+1), t>=1, sends its kernel exactly to 1/(t+u) on L²(1,infinity). Schur's test with weight t^(−1/2) gives norm<=pi, because int_0^infinity u^(−1/2)/(t+u)du=pi t^(−1/2). The same bound holds on the truncated half-line. No approximate corner kernel is substituted.

The whole actual D contribution from P14 is
\[
-\tfrac38\{C_0 g+\sqrt y\,C_0(\sqrt x\,g)\},\qquad
g=x^{A+1/2}F,\quad F=(1-x)^h E.
\tag{E14}
\]
Both multipliers are contractions; the output weight y^(b−1/2)<=1 is also a contraction. Thus its norm is at most 3pi/4 times the E2 input norm. After orthogonal projection off the actual tail transforms, the full D-only residual output Gram is bounded in positive-semidefinite order by (3pi/4)² G_lift, and its determinant is at most (3pi/4)^(2m) det G_lift. For the signed D_mu insert |mu|^(2m), which costs only O_mu(N) at fixed nonzero mu. This is a joint output inequality for the whole D channel.

The actual output projection can reduce the norm still further. Conversely input equality in E10 does not prove equality of output Gram, tail moment minors, or prescribed columns. C_0 injectivity alone does not prove nonzero compression to those columns.

## 7. Full-row trace interface and scope of the next comparison

The explicit endpoint-Hermite completion independently developed in [the complete-lift note](catalan_parity_complete_lift_20261007.md) gives the uniform complete D norm exponent
\[
C_*=46\log46-44\log44+63\log63-65\log65<0.
\]
It retains both D kernel terms. Combining that bound with the earlier whole-M bound gives the same safe exponent C_* for the actual mixed row at fixed mu; an improved bound for mu=0 does not settle arbitrary relation parameters.

Orthogonalize the pure-D input polynomials with weight x^(2L−1)(1−x)^(2h), and the columns with weight y^(b−1/2). The real determinant changes have exact factors sqrt H_delta(2L−1,2h) and sqrt H_n(b−1/2,0). Their leading terms are unchanged by the fixed half offsets. All selected m Jacobi moment scalars have sum log lambda_mom=2592 log2 N²+O_mu(N log N); omitting one of the p directions changes only O(N). Source rho_d has no N² term. Consequently every conditional full-tail minor has the safe complete trace/Hadamard upper exponent
\[
U_{\rm mix}=2592\log2+\tfrac12\mathscr H(44;11,0)
+\tfrac12\mathscr H(8;110,4)+36C_*.
\tag{E15}
\]
This compares the entire M−(3/2)Z, not M alone, and includes the full row normalization. A favorable strict comparison with a proven lower bound is still required.

For the D-only component one may instead use its joint input determinant, yielding the safe exponent
\[
U_{D\text{-only}}=2592\log2+V_C
+\tfrac12\mathscr H(44;38,4)+\tfrac12\mathscr H(44;11,0).
\tag{E16}
\]
The tail Gram in E9 cancels its orthogonal tail prefactor here. **E16 is not an upper bound for M+D.** Expanding the mixed exterior also produces all intermediate combinations of M and D; controlling only the extreme D-only and M-only terms does not control them. The exact new joint result is E10/E13/E14. An additive perturbation can overwhelm small D singular values, so determinant smallness is not automatically stable under the M term.

The complete mixed rationality under the proposed relation does not make the separate D-only array rational; that array cannot simply inherit its conditional integer lower bound. The component estimates are inputs for a joint exterior problem, not independent irrationality proofs.

A new bounded [log-expression evaluator](catalan_parity_log_expression_bounds_20261007.py) was executed exactly once and saved [its interval receipt](catalan_parity_log_expression_bounds_20261007.json). It uses exact rational atanh sums with a geometric tail and outward-rounded endpoints, rather than unqualified floating values. It gives C_* in (−0.704525,−0.704524), V_C in (1208.175682,1208.175683), J_D in (−1572.280467,−1572.280466), U_mix in (−20.855272,−20.855271), and the D-only bound in (−781.632626,−781.632625). These are N² leading expressions, except C_* which is the N-scale row exponent. The interval program verifies expression values only; paper derivations and any proposed improved arithmetic lower require separate audit. In particular the original entry lower −11440 on the N² scale remains far below this U_mix.

Reading/execution scope: root actually FULL read the current parity and round215 report; selected DLMF row1 and finite Jacobi representation were checked publicly, not a full special-functions chapter. No historical producer, prime scan, finite-N matrix or supplied mathematical software was run for this derivation. Any bounded evaluation of the explicit logarithmic expressions is separately recorded, rather than called a new coefficient experiment. Numerical independence remains unproved.

## 8. Why refining D alone cannot rescue the scalar-M certificate

Normalize all p=m+1 Jacobi source directions in L²(nu_h), and let G_Dhat be their p-square minimum input-energy Gram from E8. It has exactly rank m by E6. Projection off the entire actual tail-transform span is contractive. The complete M part has operator norm at most
\[
a_N=\tfrac12\sqrt{\pi B(2A+3/2,h-1/2)}.
\]
The D-only residual singular values are at most (3pi/4)|mu| times the square roots of the eigenvalues of G_Dhat, by E14. The singular-value triangle inequality then gives, for i<=m,
\[
s_i(M+\mu D)\le(3\pi/4)|\mu|\sqrt{\lambda_i(G_{D\rm hat})}+a_N.
\]
Using (r+s)²<=2(r²+s²) and the single zero eigenvalue yields the valid full exterior certificate
\[
\boxed{\prod_{i=1}^{m}s_i(M+\mu D)
\le2^{m/2}\left\{
\frac{\det_p[(3\pi\mu/4)^2G_{D\rm hat}+a_N^2I_p]}{a_N^2}
\right\}^{1/2}.}
\tag{E17}
\]
This holds for every actual parameter specialization; the rational relation is only needed for the later arithmetic lower comparison.

The determinant expression on the right is **at least** a_N^m (including its harmless 2^(m/2) factor), regardless of the D Gram. Consequently the best possible leading bound available from this construction while keeping only the scalar M norm is bounded below by
\[
\boxed{U_{\rm scalarM\ floor}=
2592\log2+\tfrac12\mathscr H(44;11,0)
+\tfrac12\mathscr H(8;110,4)+18\mathscr B(38,2),}
\tag{E18}
\]
where Bscript(38,2)=38log38+2log2−40log40. The saved outward intervals put E18 in (−138.423368,−138.423367). Thus refining only D singular values, while using that scalar M estimate in E17, cannot bring this certificate near the existing conditional arithmetic lower −11440. Even an arithmetic lower improved to −27323/4 would leave a gap above 6692 on the N² scale; that latter improved lower is a separate paper claim pending audit when this section is written.

This is a limitation of **one upper-bound construction**, not a lower bound for the actual mixed determinant and not impossibility of the parity carrier. A proof could still use the whole M singular spectrum, cross-channel cancellation, a different joint arithmetic lattice or another carrier. It explains why continuing D-only norm optimization cannot be the next main task. The next relevant object is the full mixed exterior including intermediate M/D combinations and the actual relation-point nonzero criterion.

Review receipt: theta_analytic_geometry actually FULL read the original seven-section E1–E16 version (12446 bytes), then actually read the complete revised section7 and new section8 E17–E18 (14853-byte version, SHA256 8441775922889d5761346b7b69838835bb3c2d4ea6670094ac170f7386da1be9). Its independent paper derivation returned PASS without mathematical correction. It also FULL read the 4123-byte log-expression evaluator and its 5144-byte JSON, checking formula encodings, exact-rational remainder and outward rounding; it did not run the program or independently recompute the 70-digit intervals. The bounded independent receipt is [saved separately](research_round216_complete_lift_joint_energy_independent_review_20261007.md). Root authored and actually FULL read all eight sections, code and JSON. No finite-coefficient/rank producer or prime scan was executed. After the earlier writing-time pending label above, root independently FULL audited F1–F17 of the new finite-place note and gamma independently FULL audited it with PASS: the improved lower −27323/4 now has a separate paper audit. This later audit does not change what the scalar evaluator itself verified.
