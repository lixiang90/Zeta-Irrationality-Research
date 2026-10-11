# A parity projection retaining Catalan and pi-squared: positive kernels and complete entry model

2026-10-07. NEW actual moment carrier, changing both supports and the column filter. It is not a change of basis inside the preceding principal contact model. This note proves the actual mixed period selector, eliminates the H/D_H channel identically, moves the interior sign junction to an endpoint, and gives integer pairs and a complete safe entry model. It also proves an all-N C rank and a genuine Hilbert--Schmidt estimate for the full M channel in the q=0 variant. The D_C contribution and the final joint determinant comparison remain unproved. No numerical irrationality theorem, supplied program, prime scan or finite coefficient experiment is used.

## 1. Two fully specified variants of one parity carrier

For N>=1 put
\[
A=19N,\quad h=2N,\quad K=8N,\quad M=44N,\quad
n=M-1,\quad L=55N-1,\quad m=L-A-1=36N-2.
\tag{P1}
\]
Choose either q=4N or q=0, and set
\[
b=11N-q,\qquad e=h+q,\qquad A-b-q=K.
\]
All h,q,e are even. Let
\[
d\nu_0(x)=\frac{dx}{\pi\sqrt{x(1-x)}},\qquad
d\nu_e=(1-x)^e d\nu_0,\qquad
Q_d(x)=P_d^{(e-1/2,-1/2)}(2x-1).
\]
Use the p=36N-1 directions K+1<=d<=M-1, spanning the polynomials of degree <M orthogonal to 1,x,...,x^K for nu_e. Define
\[
P_Q(t)=t^{2A}(1-t^2)^hQ(t^2),\qquad
V_k(s)=s^{2(b+k)}(1-s^2)^q,\quad 0\le k<n.
\tag{P2}
\]
Every D is even, starts at t^(2A+2), and has factor (1-t^2)^h. Its endpoint polynomial will be prescribed below. The full tail pool has delta=8N+1 pairs
\[
(0,T_a),\quad T_a(t)=t^{2(L+a)}(1-t^2)^h,
\quad0\le a<\delta.
\]
Thus the full pool has 44N rows and n=44N-1 columns. The designated square selects the first 8N tails and all p Jacobi rows. These two row selections must stay distinct.

## 2. The actual period projection, including its signs

Use the original actual M and Z integrals and their proven coefficient decomposition, read in foundations.tex and retained in the previous Schur note:
\[
F(P,D;j)=M^0(P;j)-\tfrac32 Z^0(D;j)
 +4G C_j(P)+\tfrac{\pi^2}{4}(H_j(P)-D_j).
\tag{P3}
\]
Here c_r=4^(-r) binom(2r,r), C_j=sum_i P_i c_((i-j)/2), H_j=sum_i P_i c_((j-i-1)/2), with invalid indices zero. Since P is even, H_(2j)=0 exactly. The new filter uses only even column indices:
\[
\widehat C_k=\sum_{v=0}^q(-1)^v\binom qv C_{2(b+k+v)},
\quad
\widehat D_k=\sum_{v=0}^q(-1)^v\binom qv D_{2(b+k+v)}.
\]
Impose -Dhat=mu Chat, not Dhat=mu Chat. Then the actual filtered matrix is
\[
\mathsf F=\widehat M^0-\tfrac32\widehat Z^0
 +(4G+\mu\pi^2/4)\widehat C.
\tag{P4}
\]
Under alpha G+beta pi^2=u, alpha!=0, set mu=16 beta/alpha and gamma=4u/alpha. The whole matrix is rational, with period term gamma Chat. This retains the same unknown mixed numerical goal. It does not assume G and pi^2 rational separately. Crucially, D_H is zero in this carrier; no high-order approximation to D_H has been silently discarded.

## 3. Complete contact and the actual endpoint section

Put R_Q(x)=(1-x)^e Q(x), and use the branch sqrt(z(z-1))~z at infinity. Define
\[
B_Q(z)=\int_0^1\frac{R_Q(z)-R_Q(x)}{z-x}d\nu_0(x),
\quad W_Q(z)=\int_0^1\frac{R_Q(x)}{z-x}d\nu_0(x).
\]
The elementary arcsine Cauchy transform is 1/sqrt(z(z-1)), giving
\[
\frac{R_Q(z)}{\sqrt{z(z-1)}}=B_Q(z)+W_Q(z),
\qquad W_Q(z)=O(z^{-K-2}).
\tag{P5}
\]
In x=t^2 the even infinity series tP/sqrt(t^2-1) is P(x)/sqrt(1-1/x). After the new filter, its relevant coefficients are those of x^(A+1)(B_Q+W_Q). Moving the finite polynomial filter across the polynomial-part operation adds only degree <q; all output indices b+q+k are above that range. The first K+1 outputs vanish by orthogonality. The remaining outputs are exactly
\[
\widehat C_{K+1+r}(Q)=[x^r]B_Q(x),\quad0\le r<m.
\tag{P6}
\]
Write D_C(t)=x^(A+1)(1-x)^h E_Q(x), where
\[
E_Q=\operatorname{trunc}_{<m}\frac{B_Q(x)}{(1-x)^e}.
\quad\boxed{D_\mu=-\mu D_C.}
\tag{P7}
\]
Then (1-x)^q D_C=x^(A+1)B_Q modulo x^L, proving every contact equation through output n-1. The same low coefficients can be prescribed by a unit triangular system, followed by endpoint completion. P7 is its exact closed form. Any two allowed completions differ by x^L(1-x)^h times a polynomial of degree <delta. Thus the full tail span accounts for the entire section freedom, rather than selecting D independently to improve an estimate.

## 4. All-N infinity coefficient rank for this new filter

For arbitrary Q=x^i of degree <M the full output-by-input matrix is
\[
\mathsf A_{\ell,i}=a_{i+K-\ell},\quad
a_s=\sum_{v=0}^e(-1)^v\binom ev c_{s+v}.
\]
Its Laurent generating series is z^(-e) Phi(z), with Phi=(1-z)^(e-1/2); e is even. A row dependence Lambda of degree <=M-2 would force all coefficients of Phi Lambda at K+e,...,K+e+M-1 to vanish. Put s0=M+K+e and Pi=trunc_<K+e(Phi Lambda). Then
\[
E=\Phi\Lambda-\Pi=O(z^{s_0}),\qquad
\deg\Pi\le K+e-1.
\]
Since (1-z)Phi'=(1/2-e)Phi, the polynomial
\[
\Omega=(1-z)(\Pi'\Lambda-\Pi\Lambda')-(1/2-e)\Pi\Lambda
\]
has degree at most s0-3 and order at least s0-1. Hence Omega=0. Pi cannot be zero because Phi(0)=1 and deg Lambda<s0. The resulting rational logarithmic derivative has residue e-1/2 at z=1, impossible for Pi/Lambda. Consequently rank A=M-1 for all N.

For ell<=K the outputs are the positive moments int x^(K-ell) Q dnu_e. Restricting to their common kernel gives exact residual rank m, by the one-dimensional kernel of A. The pure-D moment block for any required leading tail columns is strictly totally positive up to its fixed sign: double Andreief and the Cauchy determinant apply to increasing even monomials on (0,1). The entire allowed D moment map is likewise invertible. Therefore a maximal minor using all delta tails and m chosen Jacobi directions is a nonzero polynomial of exact degree m in gamma, for each fixed mu. It can still have exceptional fixed rational gamma. No all-N actual-point nonzero theorem is inferred.

## 5. An integral Chebyshev connection with no degree-dependent extra scale

Let J_d(z)=P_d^(e-1/2,-1/2)(z). Strengthen the earlier 4^d integrality statement to
\[
\boxed{4^dJ_d(z)\in\mathbb Z[2z].}
\tag{P8}
\]
For d>=1 its finite generating formula gives
\[
4^dJ_d=[w^d]
\{(1+2zw)^2-4w^2\}^{d-1/2}(1+2(z+1)w)^e.
\]
In degrees k<=d, expand the first factor as
\[
\sum_{j\le k/2}(-4)^j\binom{d-1/2}{j}
w^{2j}(1+2zw)^{2d-1-2j}.
\]
Here 4^j binom(d-1/2,j) is integral (expand (1+4u)^(d-1)(1+4u)^(1/2)), and 2d-1-2j>=0. The remaining factor belongs to Z[2z,w]. This proves P8, not a coefficient sample.

With z=2x-1, (1-x)^e=2^(-2e)(2-2z)^e. Thus 2^(2e)4^d R_Q(x) belongs to Z[2z]. Powers of 2z have integer expansions in T_j(z), as follows directly from (w+w^(-1))^i. If R_Q=sum r_j T_j(2x-1), every 2^(2e)4^d r_j is integral. Polynomial division of the arcsine transform gives
\[
B_Q(x)=2\sum_{j\ge1}r_j U_{j-1}(2x-1).
\tag{P9}
\]
Since U_j has integer coefficients, 2^(2e)4^d B_Q is integral. The inverse of (1-x)^e has integer Taylor coefficients. Therefore the pair scalar
\[
\lambda_d^{\rm pair}=d_\mu 2^{2e}4^d
\tag{P10}
\]
clears P, D_mu and all filtered C. This is an integral polynomial-pair model; it alone has not yet cleared every rational M0 entry at 2.

## 6. All primes and powers for the actual moments

Use the safe moment scalar
\[
\boxed{\lambda_d^{\rm mom}=2^{2K}\lambda_d^{\rm pair}.}
\tag{P11}
\]
P8 after z=2x-1 also says that the coefficient of x^u in 4^d Q(x) has valuation at least 2u. In P=x^A(1-x)^h Q, a term arising from this coefficient and x^v of the endpoint factor has t-degree i=2(A+u+v), v<=h. Every column has even exponent j>=2b. The only possible linear dyadic loss in M0's minus-start array is i-j<=2u+2(A+h-b)=2u+2(K+e). P11 clears it term by term. The plus-start difference j-i-1 is odd and has no such dyadic loss. The remaining diagonal M0 sums have only their integer harmonic-index denominator, and Z0 has two such layers. The proof is the actual binary-kernel argument J13--J15 of the earlier finite-place note, with the new index bounds; its odd-prime column table and leading exponent are not transferred.

For odd p, the same rational M0/Z0 formulas give entry depth at most 2 floor(log_p H), including all higher powers. All row and column indices here are <H=130N. Pair integrality and filtered C integrality have already been proved. Hence, with ell_H=lcm(1,...,H),
\[
\boxed{2d_\gamma\ell_H^2\mathsf F^{\rm mom}\in
\operatorname{Mat}(\mathbb Z).}
\tag{P12}
\]
Every prime and power is included. For a nonzero conditional n-row minor this elementary entry certificate gives the safe lower exponent -2H/n tending to -65/11 on the n^2 scale. This is a conservative starting bound, not an optimized joint-column cost or a necessary minimum. Changing from P10 to P11 adds the identical scalar at the real place; its dyadic gain is not counted on just one side.

For q=0, sum_d log(lambda_mom)=2592 log2 N^2+O_mu(N log N); for q=4N it is 2880 log2 N^2+O_mu(N log N). These exact leading normalization costs use sum d=936N^2-26N and p=36N-1. They must be retained in any analytic estimate.

## 7. Actual positive kernels with the complete D channel

For x=t^2 and y=s^2, symmetry of even P gives the exact actual M entry
\[
\boxed{M(P_Q,V_k)=\frac12\int_0^1\!\int_0^1
\frac{x^A(1-x)^{h-1/2}Q(x)
y^{b+k-1/2}(1-y)^q}{1-xy}\,dx\,dy.}
\tag{P13}
\]
There is no sign(t) junction at an interior point. For D(t)=mathcal D(t^2), its actual contribution is
\[
-\frac38\int_0^1\!\int_0^1
\frac{\mathcal D(x)x^{-1/2}y^{b+k-1/2}(1-y)^q}
 {1-\sqrt{xy}}\,dx\,dy
\]
\[
=-\frac38\iint
\mathcal D(x)y^{b+k-1/2}(1-y)^q
\frac{x^{-1/2}+y^{1/2}}{1-xy}\,dx\,dy.
\tag{P14}
\]
Thus the full D term has two positive Cauchy kernel channels, with the actual signed polynomial mathcal D=−mu x^(A+1)(1-x)^h E_Q. Positivity of the kernels does not assert positivity of these mixed rows or their determinant. Neither channel is omitted.

## 8. Full M-channel Rodrigues identity with paid endpoints

The shifted Rodrigues identity is
\[
\nu_e(x)Q_d(x)=\frac{(-1)^d}{\pi d!}
\partial_x^d[x^{d-1/2}(1-x)^{d+e-1/2}]\,dx.
\]
Putting g_y=x^(A+1/2)(1-x)^(-q)/(1-xy), d integrations by parts in the inner integral of P13 give
\[
\int_0^1\frac{x^A(1-x)^{h-1/2}Q_d(x)}{1-xy}dx
=\frac1{d!}\int_0^1x^{d-1/2}(1-x)^{d+e-1/2}
\partial_x^d g_y(x)dx.
\tag{P15}
\]
At x=0 each intermediate endpoint product is O(x^(A+1)); at x=1, for fixed y<1, it is O((1-x)^(h+1/2)). The final absolute integrand is integrable at both endpoints. After expanding the derivative by the finite Leibniz rule, one may pay the y interchange using
(1-y)^q/(1-xy)^(c+1)<=1/(1-xy) for c<=q, or directly integrate the positive absolute terms; equivalently the pre-integration inner polynomial integral is finite with the fixed h endpoint order. For the derivative terms with c>q, use (1-y)^q/(1-xy)^(c+1)<= (1-x)^(-(c-q+1)) and the paired power (1-x)^(h+c-1/2) below. Thus the two-end estimate is uniform after integration.

More explicitly, the term with a+b1+c=d has x exponent d-1/2+A+1/2-a=A+d-a and endpoint power d+e-1/2-q-b1=h+a+c-1/2, and denominator (1-xy)^(c+1). Since A+d-a>=0 and h+a+c-1/2-(c+1)=h+a-3/2>-1, its absolute double integral is finite even under the cruder bound (1-xy)>=1-x. This proves all interchanges without any parity corner term. Derivatives of x^(A+1/2) can have alternating signs above order A+1; no unproved derivative positivity is used.

## 9. A genuine whole-channel Hilbert--Schmidt estimate for q=0

Here e=h, b=11N. Let H_y=L^2(y^(b-1/2)dy) and let T act from L^2(nu_h) by
\[
(TQ)(y)=\int_0^1\frac{x^A(1-x)^{h-1/2}Q(x)}{1-xy}dx
=\pi\int\frac{x^{A+1/2}Q(x)}{1-xy}d\nu_h(x).
\]
Because b>=1/2 and int_0^1(1-xy)^(-2)dy=1/(1-x),
\[
\boxed{\|T\|_{\rm HS}^2\le
\pi B(2A+3/2,h-1/2).}
\tag{P16}
\]
This bounds the full M transform, not merely an analytic remainder. The orthonormal Jacobi subset gives
\[
\sum_{d=K+1}^{M-1}\frac{\|TQ_d\|_{H_y}^2}{\rho_d}
\le\|T\|_{\rm HS}^2,
\quad
\rho_d=\frac{\Gamma(d+e+1/2)\Gamma(d+1/2)}
 {\pi(2d+e)\Gamma(d+e)\Gamma(d+1)}.
\tag{P17}
\]
Uniformly in the present d/N interval, log rho_d=O(log N); its product has no N^2 exponential term. P16 has exponent N Bscript(38,2)+O(log N), where Bscript(a,c)=a log a+c log c-(a+c)log(a+c). Row exterior AM--GM consequently gives an actual M-channel N^2 contribution (p/2N) Bscript(38,2)=18 Bscript(38,2), before the exact row scalars and column Gram. This is a quantitative operator gain, not a full mixed determinant estimate.

The D_C term in P14 must still be controlled after tail removal. Bounding M alone cannot be compared with P12 as if D vanished. The q=4N variant does not receive P16: its domain kernel has (1-x)^(-q), and this particular Hilbert--Schmidt integral need not converge. The two variants must not borrow each other's bounds.

## 10. A bounded second-kind map and explicit endpoint data

Orthogonality makes r_0=0 in P9. Chebyshev orthogonality gives
\[
\frac8\pi\int_0^1 B_Q(x)^2\sqrt{x(1-x)}dx
=8\|R_Q\|_{L^2(\nu_0)}^2
\le8\|Q\|_{L^2(\nu_e)}^2.
\tag{P18}
\]
Thus B_Q itself is a controlled map. Its Taylor truncation after division by (1-x)^e is not automatically controlled in the D norm. In q=0, the endpoint jets needed for an alternative completion are explicit for 0<=j<h:
\[
\boxed{B_{Q_d}^{(j)}(1)=
(-1)^{j+1}\frac{(d+j)!}{\pi d!}
B(d+1/2,h-j-1/2).}
\tag{P19}
\]
Indeed R_Q/sqrt(z(z-1)) has zero endpoint jets through h-1, so differentiate P5 and use Rodrigues in the convergent integral of Q_d/(1-x)^(j+1). All resulting beta parameters are positive. P19 is an actual finite datum, not a claim that every high endpoint jet is small.

Adding any real tail combination to a selected Jacobi row leaves a determinant containing those tails unchanged. For all-tail minors this permits choosing the best real completion while retaining the original integral section for the arithmetic estimate. It does not license ignoring an omitted tail in the designated square. The useful next proof is a quantitative norm for this whole contact lift modulo the included tails, using P18/P19 or a joint Cauchy exterior calculation.

## 11. Direction and limits

This is a concrete support/kernel change with the same numerical target. It pays the actual period projection, full finite-prime entry starting model, all-N C rank, removal of D_H, and the full q=0 M-channel decay; it still lacks target-point nonzero and a strict comparison for the full mixed determinant. Its doubled original t,s index range makes the conservative odd-prime cost significant. The preceding principal odd-prime table, observed nonzero points, and real-place constants are not assigned to it.

No claim is made that a generic coefficient rank settles numerical linear independence, that positive kernels make a signed determinant nonzero, or that the bound for only M controls M−(3/2)Z. The next decision must depend on the actual D_C lift and joint denominator/exterior balance, not simply on the cleaner kernel. All formulas here were newly derived from the original actual coefficient identities and standard finite Jacobi identities; no supplied source code or historical producer was executed.

Review receipt: root authored and actually FULL read all eleven sections P1–P19. Theta_analytic_geometry and gamma_bound each independently actually FULL read the 15018-byte version SHA256 3af78a732b003156cbd10a8f5581e2d77186598fbb67890374ef0dad8385f01c, and independently rederived the actual contact signs and coefficient indices, all-N rank argument, integer Chebyshev/dyadic model, full M/D kernel constants, endpoint interchanges, whole-M Hilbert–Schmidt bound, B norm and endpoint jets. Both returned mathematical PASS without correction. Their conclusions keep full D_C control and actual relation-point nonzero open. This is paper review, not Lean or an independent coefficient-generation experiment. Root's final FULL reread and archive identity are recorded in the round-215 manifest.
