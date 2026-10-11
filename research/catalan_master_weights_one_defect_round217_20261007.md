# Actual parity dual: finite master weights and an exact one-extra-zero lemma

2026-10-07, round217. NEW paper derivation. The actual dual is reduced to four explicit master functions with linked polynomial coefficients and its complete endpoint correction. The four-dimensional constant-coefficient master space has at most four distinct zeros on (0,1), and some element has four: it misses the ordinary Chebyshev bound by exactly one. This does not prove the corresponding bound for the high-degree constrained actual space. That stronger bound remains the numerical rank gate.

## 1. Actual object and coefficient reversal

The authoritative [actual dual note](catalan_parity_actual_nonzero_interface_20261007.md) was actually FULL read in its final16005-byte version. Use q=0, integer b>=0, K=A−b>=0, n=M−1, L=b+n, m=L−A−1=n−K−1>=1, delta=K+1. Assume h>=1 and delta+h<=n when using its endpoint-surjectivity assertion. The paid current choice is A=19N,b=11N,h=2N,n=44N−1. The b=0 choice is an exploratory changed support with K=A; its integer and real-place costs are not inherited.

For a column polynomial Lambda(y)=sum_(k=0)^(n−1)lambda_k y^k set
\[
S(x)=x^{n-1}\Lambda(1/x),\quad
U(x)=\int_0^1\frac{y^{b-1/2}\Lambda(y)}{1-xy}dy,
\quad V(x)=\int_0^1\frac{y^b\Lambda(y)}{1-xy}dy,
\quad Z=x^{-1/2}U+V.
\tag{M1}
\]
The actual Jacobi dual is
\[
W_{\mu,\Lambda}=\frac\pi2 x^{A+1/2}U
 +\frac{3\mu}{8}(-H_f+E_\Lambda),\quad
f=x^{A+1}Z,\quad H_f(t)=\operatorname{PV}\int_0^1\frac{f(x)}{x-t}dx.
\tag{M2}
\]
Here E_Lambda has all h principal parts from A16, not a disposable error. This is the integral parameter gamma_*(mu)=4G+mu*pi²/4. An unrelated formal gamma adds (gamma−gamma_*)xi_Lambda; it must not be silently inserted with the degree bounds below.

## 2. Exact linked truncations, including every cancellation at zero

For 0<x<1 put
\[
\mathcal A(x)=\frac{\operatorname{atanh}\sqrt x}{\sqrt x}
=\sum_{j\ge0}\frac{x^j}{2j+1},\quad
\mathcal B(x)=-\log(1-x)=\sum_{j\ge1}\frac{x^j}{j},
\]
\[
T=\operatorname{trunc}_{<L-1}(S\mathcal A),\qquad
R=\operatorname{trunc}_{<L}(S\mathcal B).
\tag{M3}
\]
Then deg T<=L−2 and deg R<=L−1, with a zero polynomial interpreted by its usual harmless degree convention. Direct geometric division of the monomial integrals gives
\[
x^LZ=-2S\log(1-\sqrt x)-2\sqrt x\,T-R,
\quad
x^m\frac\pi2 x^{A+1/2}U
=\pi S\operatorname{atanh}\sqrt x-\pi\sqrt x\,T.
\tag{M4}
\]
For clarity, if S=sum_i s_i x^i, the coefficients are
\[
[x^u]T=\sum_{i\le u}\frac{s_i}{2(u-i)+1}\quad(0\le u<L-1),
\quad
[x^v]R=\sum_{i<v}\frac{s_i}{v-i}\quad(0\le v<L).
\tag{M5}
\]
For the monomial Lambda=y^k write r=b+k. Its U integral is
2x^(−r−1/2)atanh(sqrt x)−2sum_(j=1)^r x^(−j)/(2r−2j+1);
its V integral is −x^(−r−1)log(1−x)−sum_(j=1)^r x^(−j)/(r−j+1). Combining 2atanh(sqrt x)−log(1−x)=−2log(1−sqrt x) and reversing the coefficients proves M4–M5. The empty sums cover r=0.

Equivalently x^LZ=2sqrt x(SA−T)+(SB−R). This retains the cancellation of negative powers and low Taylor coefficients at zero. S,T,R are not three independent polynomial coefficients; they are determined by one Lambda.

## 3. One explicit principal-value master function

Define
\[
I(t)=\operatorname{PV}\int_0^1
 \frac{\log(1-\sqrt x)}{x-t}dx\quad(0<t<1).
\]
The real identity is
\[
\boxed{I(t)=\operatorname{atanh}^2\sqrt t
 +\tfrac14\log^2(1-t)-\tfrac12\log t\log(1-t)
 -\tfrac12\operatorname{Li}_2(t)-\frac{\pi^2}{3}.}
\tag{M6}
\]
To prove it, put x=u² and z=sqrt t. The kernel 2u/(u²−z²) splits as 1/(u−z)+1/(u+z). With F(a)=PV int log(1−u)/(u−a)du, the substitution v=1−u and the defining dilogarithm integral give F(a)=−Re Li_2(1/(1−a)) for 0<a<1 and F(−a)=−Li_2(1/(1+a)). Thus
I(z²)=Li_2(1−z)−Li_2(1/(1+z))+(1/2)log²(1−z)−pi²/3.
The Euler reflection and Landen/inversion identities reduce this to M6; Li_2(z)+Li_2(−z)=Li_2(z²)/2 follows directly from the defining series.

The definition, principal branch and connection identities were checked in [DLMF25.12.1–6](https://dlmf.nist.gov/25.12). The master integral and its use here are self-contained derivations, not a theorem quoted from DLMF. I(0+)=-pi²/3 follows also from int_0^1 log(1−u)/u du=−pi²/6.

The two elementary principal-value weights are
\[
H_1(t)=\log\frac{1-t}{t},\qquad
H_{\sqrt x}(t)=2-2\sqrt t\operatorname{atanh}\sqrt t.
\tag{M7}
\]
These follow by direct integration; no positive measure with support disjoint from (0,1) is asserted merely from a principal-value formula.

## 4. The complete actual finite master reduction

For any polynomial J and integrable weight w define the polynomial
C_(J,w)(t)=int (J(x)−J(t))w(x)/(x−t)dx. Its degree is at most deg J−1. Also set
\[
C_f(t)=\sum_{j=0}^{m-1}t^j\int_0^1x^{m-1-j}f(x)dx.
\tag{M8}
\]
All these integrals exist: f=O(x^(A+1/2)) at zero and has at most a logarithmic endpoint at one. Polynomial commutation gives
t^m H_f=H_(x^mf)−C_f. Using M4 then gives, for any polynomial P of degree<=K,
\[
\boxed{t^m(W_{\mu,\Lambda}-P)
=S\Phi_\mu+T\Psi_\mu+R\Theta_\mu+\Pi
 +\frac{3\mu}{8}t^m E_\Lambda,}
\tag{M9}
\]
where
\[
\Phi_\mu=\pi\operatorname{atanh}\sqrt t+\frac{3\mu}{4}I(t),
\quad
\Psi_\mu=-\pi\sqrt t+\frac{3\mu}{4}H_{\sqrt x}(t),
\quad
\Theta_\mu=\frac{3\mu}{8}H_1(t),
\]
\[
\Pi=\frac{3\mu}{8}
 (C_f+2C_{S,\log(1-\sqrt x)}+2C_{T,\sqrt x}+C_{R,1})-t^mP.
\tag{M10}
\]
In particular deg Pi<=max(L−2,n−1), since m+K=n−1. Multiplying M9 by (1−t)^h clears every principal part of E; its added polynomial has degree at most m+h−1. This multiplication, and t^m, preserve interior sign changes. It does not make Pi, T, R or the endpoint jets independent; their coefficients and the tail constraints remain linked.

For b=0 the ordinary Pi bound is n−1; for the paid b=11N it is L−2. These are actual integral degree bounds. For arbitrary formal gamma, an extra (gamma−gamma_*)t^m xi enters, potentially of degree m+M−1; the actual bounds must not be claimed for that unrelated pencil.

## 5. A rank-four Fuchsian auxiliary module

On the quadratic variable z set
A(z)=atanh z, Theta(z)=log[(1−z²)/z²], and J0(z)=I(z²). Then
\[
A'=\frac1{1-z^2},\quad
\Theta'=-\frac2{z(1-z^2)},\quad
J_0'=\frac{2A-z\Theta}{1-z^2}.
\tag{M11}
\]
Therefore (1,A,Theta,J0) has a rational triangular differential system with regular singularities only at 0,1,−1,infinity. It is an auxiliary differential module of exact rank4 over C(z): near z=1 J0 has nonzero log² coefficient1/2, while A,Theta have at most a single log; after its coefficient vanishes, the log at z=0 forces the Theta coefficient to vanish, then the log of A at1 forces its coefficient to vanish. Rational coefficient poles do not cancel these different logarithmic signatures.

It is also cyclic. Put J=(1−z²)J0'=2A−zTheta. Then
\[
J'=\frac4{1-z^2}-\Theta,\qquad
J''=\frac{2(1+3z^2)}{z(1-z^2)^2}\ne0.
\tag{M12}
\]
Derivatives of J0 thus generate1,Theta,A as well. This is not an arithmetic-holonomy bound for a newly constructed rational Taylor germ, and not a numerical independence theorem. The logarithmic branches and period constants in the actual coefficients must still be paid before any CDT use.

## 6. Exact one-extra-zero theorem for constant master coefficients

Let V=span_R(1,A,Theta,J0) on0<z<1. Every nonzero element of V has at most4 distinct zeros there, and an element with4 distinct zeros exists. In particular V is not a four-function Chebyshev/AT system, which would permit at most3.

Proof of the upper bound: A'>0. Put q=Theta'/A'=−2/z, so q'=2/z²>0. For the highest weight,
\[
\left(\frac{(J_0'/A')'}{q'}\right)'
=z\left\{\frac{5-z^2}{(1-z^2)^2}-\Theta(z)\right\}.
\tag{M13}
\]
The expression in braces, F(z), is strictly increasing, because
\[
F'=\frac{2z(9-z^2)}{(1-z^2)^3}
 +\frac2{z(1-z^2)}>0.
\tag{M14}
\]
It tends to minus infinity at0 and plus infinity at1, so it has exactly one simple zero. Apply Rolle three times to a constant linear combination: differentiate and divide by A', differentiate and divide by q', then differentiate. The result is its J0 coefficient times M13. If that coefficient is nonzero, r distinct zeros would force at least r−3 zeros of M13, giving r<=4. If it is zero, the first three weights give at most2 zeros by the same positive divisions. The lower-dimensional cases are immediate.

For existence, the Wronskian is
\[
\operatorname{Wr}(1,A,\Theta,J_0)
=(A')^3(q')^2zF(z).
\tag{M15}
\]
At z=1/100 its rational term is<6 and Theta=log9999>6 (e<3 gives e^6<729); at z=1/2 its rational term is76/9 and Theta=log3<2. It therefore has opposite signs. Four distinct points in a sufficiently small increasing cluster near either point give evaluation determinants with those signs, by the Taylor/Vandermonde limit. A continuous path between these ordered quadruples stays in the ordered domain; some determinant on that path is zero. A nonzero constant combination consequently has four distinct zeros. The upper bound makes four exact. This proof uses no sampled zero grid or numerical Wronskian calculation.

## 7. Why the full extra row may matter

In the actual full pool the tail kernel has dimension n−delta=m. Allowing P of degree<=K adds delta=K+1 dimensions. The map (Lambda,P) -> W_mu,Lambda−P is injective: a nonzero Lambda has the noncancellable log/log² signature in A21; if Lambda=0 a nonzero P remains. Hence the constrained dual space has exactly n dimensions for every real mu.

Rank failure would provide a nonzero element with at least M=n+1 sign changes by A19/A22. A bound of **at most n**, rather than the stronger at most n−1, would already exclude that failure. Thus an analogue of the one-extra-zero result could suffice for this rectangular full pool. M13–M15 prove it only for the four constant master coefficients, not for arbitrary-degree linked S/T/R/Pi, the full endpoint jets or the tail kernel. Multiplying polynomials into a one-defect master space can create additional zeros; no uniform high-degree extrapolation is asserted.

This leaves a concrete next proof target: establish at most n interior sign changes in the exact constrained space M9 with every tail and endpoint relation. If proved, it pays actual full-pool nonzero for all real mu (and therefore any rationality relation specialization). A separate strict real/arithmetic comparison would still be required.

## 8. Primary source scope and stopping boundary

Selected [López Lagomasino–Medina Peralta–Szmigielski1805.02195v1](https://arxiv.org/pdf/1805.02195v1) Definitions1.1–1.3 and Theorems1.4–1.5 motivate retaining linked multi-level interpolation instead of declaring all coefficients free. The paper's direct/reversed and multi-level systems require actual Nikishin measure products and their interpolation identities. Those have not been identified with M9; no perfectness theorem is imported. Its source-derived description here is limited to this assumption check. The full PDF and DLMF page are saved with selected reading scope, not claimed as full proof audits.

This note was derived on paper. No mathematical producer, interval evaluator, finite matrix, prime scan, PSLQ or Lean was executed. The constant-master theorem is a new paid structural result in this research record; no claim that it is novel in all prior literature or that a numerical theorem has been proved. Original records and manifests are preserved.

Review receipt: gamma_bound actually FULL read all eight sections M1–M15 of the 11403-byte mathematical version, SHA256 4d34e59d5b86e93f07d8509bd81c60f83fce4f73741cc8b06f8c3a68aef559e2, and independently paper-checked every formula and scope with PASS, no mathematical correction. It checked linked truncations/zero-end cancellations, principal-value signs and constants, complete endpoint retention and degrees, actual/formal gamma boundary, exact auxiliary differential rank/cyclicity/regular singularity at infinity, Rolle upper bound and clustered determinant four-zero existence, actual constrained dimension and only-conditional high-degree gate. Its review did not claim a FULL reading of the new1805 primary source. Root authored and actually FULL read the mathematical version; the final update makes the already-used m>=1 hypothesis explicit and adds this receipt. Root's final author FULL reread and byte/SHA identity are recorded in the round archive. Primary downloads and exact selected scope are in [the new literature receipt](../literature/catalan_coupled_master_sources_20261007/reading_scope.md).
