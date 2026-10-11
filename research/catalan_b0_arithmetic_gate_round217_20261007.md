# b=0 parity support: a common dyadic cancellation and an arithmetic gate

2026-10-07, round217. NEW bounded paper note. No coefficient producer, validator, numerical log evaluator, prime scan or historical program was executed. This note proves an actual joint cancellation at 2, rather than importing a monomial valuation table. It quantifies what row scalars/content can buy for b=0 and records a specific obstruction to a one-layer modular nonzero proof. Actual rational relation-point nonzero remains open.

## 1. Inputs, source scope and the exact b=0 model

The author actually FULL read the current eleven-section [parity note](catalan_mixed_parity_positive_kernel_20261007.md) (15818 bytes, SHA256 a39081cb49a101c80a6b7f69306d67fd873caebc6dbad3198c2a21dad85449d8), the eight-section [parity joint finite-place note](catalan_parity_joint_finite_places_20261007.md) and the eight-section [exact second-kind joint-energy note](catalan_parity_exact_second_kind_joint_energy_20261007.md). Original [foundations.tex](E:/codex-build/math/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex) lines 95–263 were actually read with line numbers. These bounded original lines supply m, the rational starts and diagonal reduction; this is not a FULL reading of the original repository. Frozen round216 notes are not edited.

Keep q=0, fixed nonzero rational \(\mu\), and fixed rational \(\gamma\). Define
\[
A=19N,\quad h=2N,\quad b=0,\quad K=A,\quad
n=44N-1,\quad L=n,\quad m=L-A-1=25N-2,\quad
\delta=n-m=19N+1.
\tag{G1}
\]
For \(d=K+1,\ldots,n\), put
\[
Q_d(x)=P_d^{(h-1/2,-1/2)}(2x-1),\quad
P_d(t)=t^{2A}(1-t^2)^hQ_d(t^2),
\]
\[
D_d(t)=-\mu x^{A+1}(1-x)^h
 \operatorname{trunc}_{<m}\frac{B_d(x)}{(1-x)^h},
\qquad x=t^2.
\tag{G2}
\]
Here B_d is the exact second-kind polynomial of the parity note. There are p=m+1=25N−1 Jacobi pairs, and delta pure-D tails \(x^{L+a}(1-x)^h\), \(0\le a<\delta\). The full pool has n+1 rows; the designated principal square instead selects delta−1 tails and all p Jacobi rows. The statements below about all-tail minors use all delta tails and omit one Jacobi row.

The columns are the actual even indices \(j=2k\), \(0\le k<n\). Every row index is even and below H=130N. Exact contact is \(-D_j=\mu C_j\), with the first K+1 C outputs zero. The rational actual entry under the proposed numerical relation is
\[
\mathcal E(P,D;j)=M^0(P,j)-\tfrac32 Z^0(D,j)+\gamma C_j(P).
\tag{G3}
\]
The target remains \(\alpha G+\beta\pi^2=u\), with \(\mu=16\beta/\alpha,\ \gamma=4u/\alpha\). No component is declared separately rational.

## 2. A common 2-adic cancellation in the actual M channel

Write \(c_r=4^{-r}\binom{2r}{r}\), and let \(s_2(r)\) denote the binary digit sum. Set
\[
\eta(r)=2r-s_2(r),\qquad v_2(c_r)=-\eta(r).
\]
For r≥0, the explicit minus start in original foundations.tex lines 223–233 is
\[
k^-_{2r}=c_r S_r,\qquad
S_r=\sum_{\ell=1}^r\frac1{2\ell^2c_\ell^2}.
\tag{G4}
\]
The increment \(\eta(r+1)-\eta(r)=1+v_2(r+1)\) is positive. If \(v=v_2(\ell)\), monotonicity and \(\ell\ge2^v\) give
\[
\eta(\ell)\ge2^{v+1}-1\ge2v+1.
\]
Thus
\[
v_2\!\left(\frac1{2\ell^2c_\ell^2}\right)
 =2\eta(\ell)-1-2v_2(\ell)\ge\eta(\ell)\longrightarrow\infty.
\]
The convergent 2-adic number \(S_\infty=\sum_{\ell\ge1}(2\ell^2c_\ell^2)^{-1}\) belongs to \(2\mathbb Z_2\). For \(\ell>r\), the summand after multiplying by c_r has valuation at least
\[
-\eta(r)+2\eta(\ell)-1-2v_2(\ell)
\ge\eta(\ell)-\eta(r)\ge1.
\]
Consequently
\[
c_r(S_\infty-S_r)\in2\mathbb Z_2\quad(r\ge0).
\tag{G5}
\]
This is a 2-adic auxiliary series; no real value of it, or identification with G, is used.

Let P be any even integral polynomial, and let j be even. If its actual infinity coefficient \(C_j(P)=\sum_{i\ge j}P_i c_{(i-j)/2}\) is integral at 2, then G4–G5 give
\[
\sum_{i\ge j}P_i k^-_{i-j}
=S_\infty C_j(P)
-\sum_{i\ge j}P_i c_{(i-j)/2}
       (S_\infty-S_{(i-j)/2})\in2\mathbb Z_2.
\tag{G6}
\]
For i<j the plus start has index j−i even. In the original formula write u=j−i−1 odd. Its summands have valuation
\[
1+\eta((u-1)/2)-\eta((z-1)/2)\ge1
\]
for odd z≤u; hence \(k^+_{j-i}\in2\mathbb Z_2\).

Finally, original lines 97–102 give
\[
m_{2r}=\frac2{(2r+1)c_r}\in2\mathbb Z_2,\qquad m_{\mathrm{odd}}=0.
\]
For even i,j, every nonzero term m/k in the diagonal reduction of lines 177–183 has k odd. Each such term is therefore in \(2\mathbb Z_2\). Combining all parts proves the actual aggregate lemma
\[
\boxed{P\in\mathbb Z[t^2],\ C_j(P)\in\mathbb Z_2,\ j\ {\mathrm{even}}
\quad\Longrightarrow\quad M^0(P,j)\in2\mathbb Z_2.}
\tag{G7}
\]
It holds for every even column and every size, without a termwise monomial denominator assumption.

## 3. The smaller complete all-prime moment model

The parity note P8–P10 already proves that
\[
\lambda_d^{\mathrm{pair}}=d_\mu 2^{2h}4^d
\tag{G8}
\]
clears P, the entire prescribed D_mu and every raw C output for q=0. Here d_mu is a fixed positive denominator of mu. Applying G7 to the resulting integer P proves that the additional factor \(2^{2K}\) in the earlier safe moment scale is unnecessary.

Let \(E^{\mathrm{pair}}\) be the actual matrix with G8 on its Jacobi rows and integral pure-D tails. Put \(\ell_H=\operatorname{lcm}(1,\ldots,H)\), and choose a positive denominator d_gamma of gamma. The odd-prime all-power argument of F4 applies unchanged to these integer pairs. G7 pays the M part at 2; the harmonic Z0 formula is cleared by \(\ell_H^2\), and its 3/2 coefficient by 2. Thus
\[
\boxed{2d_\gamma\ell_H^2E^{\mathrm{pair}}
\in\operatorname{Mat}(\mathbb Z).}
\tag{G9}
\]
This is a complete all-prime and all-power certificate. In particular, conditional on the chosen rational minor being nonzero, its conservative lower exponent is \(-11440N^2+o(N^2)\), equivalently \(-65/11\) on the n² scale.

The old q=0,b=11N moment model had an additional \(2^{16N}\) on each of its 36N−1 Jacobi rows. G7 pays an actual determinant divisibility of leading \(576\log2\,N^2\) there. For b=0 the old \(2^{38N}\) factor gives leading \(950\log2\,N^2\). These are new actual arithmetic facts about the joint rows. When converting models, the identical row scale must also be removed from the analytic upper bound. Frozen round216 formulae retain their historical normalization and are not silently overwritten.

## 4. Explicit b=0 row content and its limited remaining budget

The new shifted coefficient formula, already proved in F11, is
\[
[x^k]\,4^dQ_d=(-1)^{d+k}\binom{2d}{d}
\frac{d!}{(d-k)!}
\frac{(d+h+k-1)!}{(d+h-1)!}\frac{4^k}{(2k)!}.
\]
For odd primes \(d+h-1<p\le2d\), the factorial carry argument gives valuation
\[
1+[d+h+k-1\ge p]-[2k\ge p]\ge1
\]
in every coefficient, with valuation one at k=0. Define
\[
\Omega_d=\prod_{\substack{p\ {\mathrm{odd\ prime}}\\d+h-1<p\le2d}}p.
\tag{G10}
\]
The entire integer pair in G8, and its C outputs, may be divided by Omega_d: the second-kind map has only dyadic denominators, and the endpoint inverse series is integral. This proof applies at the present degrees; no old consecutive-column loss table is moved to b=0.

The sums for d=19N+1,...,44N−1 are exact:
\[
\sum d=\tfrac{1575}{2}N^2-\tfrac{63}{2}N,\qquad
\sum\log\lambda_d^{\mathrm{pair}}
=1675\log2\,N^2-67\log2\,N+O_\mu(N).
\tag{G11}
\]
The weighted prime number theorem gives
\[
\sum\log\Omega_d=\tfrac{1475}{2}N^2+o(N^2).
\tag{G12}
\]
Its endpoints range over fixed positive multiples of N, so its errors are uniform. Omitting one degree costs only O(N). Combining G9 and this actual row division gives the safe conditional lower
\[
\boxed{\log|\det E^{\mathrm{pair}}|
\ge-\tfrac{21405}{2}N^2+o(N^2)}
\tag{G13}
\]
along any nonzero sequence. This is a sufficient denominator/content certificate, not a necessary denominator minimum. No new optimized odd-prime column area is claimed.

There is also a rigorous ceiling for further whole-pair row divisions in this specified model. The lowest coefficient of P equals
\[
d_\mu2^{2h}(-1)^d\binom{2d}{d}.
\]
Therefore its odd primitive content divides the odd part of this number. The secondary Jacobi identity E3 gives, with D=d+h−1,
\[
B_d(0)=(-1)^{h+D}\frac{(D+1)\binom{2D+1}{D}}{4^D}
=(-1)^{h+D}\frac{(2D+1)\binom{2D}{D}}{4^D}.
\]
The lowest D_mu coefficient in the scaled pair has valuation
\[
v_2(d_\mu\mu)+2h+2d-2D
+v_2(D+1)+v_2\binom{2D+1}{D}
=v_2(d_\mu\mu)+1+v_2(d+h)+s_2(d+h)=O_\mu(\log N).
\tag{G14}
\]
Thus the total 2-content of these complete pairs is o(N²), while the odd-content ceiling is \(1575\log2\,N^2+o(N^2)\). Beyond the paid Omega product, further whole-pair row division can gain at most
\[
1575\log2-\tfrac{1475}{2}<365
\tag{G15}
\]
on the N² scale. The residual scalar cost in a primitive version of these rows is at least \(100\log2\,N^2+o(N^2)\). These are only row-scalar statements; they do not restrict arbitrary joint lattices, determinant-only congruences or a new basis of the full contact lattice.

For comparison, the b=11N pair scale costs \(2016\log2\), and its paid Omega product costs 864. The scalar-minus-known-content advantage of b=0 is only
\[
(2016\log2-864)-(1675\log2-1475/2)
=341\log2-253/2.
\tag{G16}
\]
It lies between 100 and 113, using \(2/3<\log2<7/10\). This compares only actual row factors. The different column and tail Grams must still be paid separately.

## 5. A legal graded mixed certificate and a quantitative method limit

This section provides a short gate for one chosen upper-bound construction, not a lower bound on the actual determinant. In the b=0 output space \(L^2(y^{-1/2}dy)\),
\[
\int_0^1\frac{y^{-1/2}}{(1-xy)^2}dy
=\frac1{1-x}+\frac{\operatorname{atanh}\sqrt x}{\sqrt x}
\le\frac2{1-x}.
\]
Truncating the geometric Cauchy kernel after k terms gives a rank-k approximation to the entire M transform. Its remainder has Hilbert–Schmidt bound
\[
s_{k+1}(M)\le a_{k+1}:=
\tfrac12\sqrt{2\pi B(2A+2k+3/2,h-1/2)}.
\tag{G17}
\]
This is valid after restricting to the Jacobi source subspace and after projecting off the full actual tail span.

The complete D transform remains bounded at b=0. If C_0 is the unweighted Cauchy operator of E14, split y at 1/2: on the low half, \(|C_0g|\le2\|g\|_2\); on the high half use its norm≤pi and \(y^{-1/2}\le\sqrt2\). Thus
\[
\|C_0g\|_{L^2(y^{-1/2}dy)}
\le2^{1/4}\sqrt{4+\pi^2}\,\|g\|_2.
\]
The other complete channel \(\sqrt y C_0(\sqrt xg)\) has norm≤pi in the same space. The actual 3/8 factor gives the explicit finite constant
\[
c_D=\tfrac38\{2^{1/4}\sqrt{4+\pi^2}+\pi\}.
\tag{G18}
\]
Both channels and all tails are retained. Projection is contractive. Therefore the D residual singular values are bounded by \(c_D|\mu|\sqrt{\lambda_i(G_D)}\), where G_D is the exact minimum input-lift Gram with rank m, derived as in E8.

In the present source dimension p=m+1, every unit m-vector is decomposable and is represented by an orthonormal m-frame. For the operators M,D on this common input, multilinearity on that frame and the exterior norm inequality give
\[
\|\wedge^m(M+D)\|
\le\sum_{r=0}^m\binom mr
 \|\wedge^rM\|\,\|\wedge^{m-r}D\|.
\tag{G19}
\]
The paid singular bounds yield the legitimate positive-sum certificate obtained by replacing the factors by \(\prod_{j<r}a_{j+1}\) and \((c_D|\mu|)^{m-r}\prod_{i\le m-r}\sqrt{\lambda_i(G_D)}\). All middle terms are present. A D-only determinant estimate cannot replace this sum.

Its all-M term alone puts a floor on this particular certificate. With X(t)=t²log(t)/2−t²/4 and Hscript as in E11, that leading floor in the pair model is
\[
U_{\mathrm{graded\ certificate\ floor}}
=1675\log2+\tfrac12\mathscr H(44;0,0)
+\tfrac12\mathscr H(19;88,4)
+\tfrac14\int_{38}^{88}\mathscr B(u,2)\,du.
\tag{G20}
\]
The exact row rho factors and finite kernel constants cost only O(N log N). The column Gram has \(\mathscr H(44;0,0)=-3872\log2\). For a rigorous cheap bound on the tail Gram, restrict its positive Andreief integral to [1/4,3/4]. The weight is at least \(4^{-(92N+O(1))}\); the affine interval Gram adds \(2^{-\delta^2}\), and the ordinary Hilbert Gram has leading \(-2\delta^2\log2\). Hence
\[
\mathscr H(19;88,4)\ge-4579\log2.
\]
On 38≤u≤88, \(\mathscr B(u,2)>-2-2\log45>-10\). It follows that G20 is strictly greater than −2675.5. The currently paid arithmetic lower G13 is −10702.5. Thus, with the displayed input-tail Gram and finite tail-operator prefactor fixed, this chosen graded positive-sum certificate still has a gap exceeding 8027 on the N² scale, even with perfect residual D singular-value refinements. The whole-pair content budget G15 cannot bridge that gap.

This floor is a lower bound for the value of the selected upper certificate, not for the actual determinant. The safe arithmetic lower is not a necessary cost either. Cross-channel cancellation, a different M exterior argument, a new actual tail-operator exterior estimate or a genuine joint-column lattice can change the comparison. Dividing by the known Omega product shifts both G13 and G20 consistently.

## 6. Actual-point modular gate and a one-layer obstruction

A sufficient new nonzero mechanism would be an unbounded prime/size sequence and paid local row/column scalings for which the actual matrix is integral and its leading residue is invertible at the fixed rational mu,gamma. One possible form is \(\mu A_D+A_M+\gamma A_C\), with A_D invertible modulo p, A_M and A_C vanishing, and mu a unit. Neither C coefficient rank nor generic gamma rank proves those residue assertions.

In fact one leading p-layer has a concrete limitation here. Take an odd prime
\[
92N<p\le130N,\qquad p\nmid d_\gamma.
\]
All actual even columns are below p. The direct even-column residue lemma F6 says every entry has depth at most one. Write J=130N−p, which is odd. The noncentral low columns \(j<J\) number (J+1)/2. Every remaining column is central, and F7 puts its p-scaled residue in the span of the odd vectors \(V_\ell\), \(0\le\ell<J\), of number (J−1)/2. Thus, for the actual b=0 pair matrix,
\[
\boxed{\operatorname{rank}_{\mathbb F_p}
 (pE^{\mathrm{pair}}\bmod p)\le J=130N-p<38N<n.}
\tag{G21}
\]
This uses only the original even support and the exact parity residue identity, rather than an odd-column packet or a finite check. Fixed exceptional parameter primes can be excluded. It shows why a unit C minor or a common Jacobi content factor cannot by itself give an invertible leading packet in this window. A multi-layer column lattice or a different prime/size mechanism is needed. It does not exclude a proof using lower layers, and does not prove the determinant zero.

## 7. Decision and remaining hard gate

The common dyadic cancellation G7–G9 is a genuine new actual-row improvement and applies to the current q=0 parity route as well as b=0. The b=0 row-factor advantage is modest once the same improvement is applied to both supports. Its enlarged tail span does not itself pay the mixed output determinant. The specified whole-pair content route and D-only refinements of G19 cannot close the currently certified gap.

Accordingly b=0 is a bounded alternative, not yet a reason to replace the main carrier. A promotion needs a new actual relation-point nonzero mechanism along unbounded N, or a complete mixed exterior/joint-column argument changing the N² balance. G21 identifies an explicit missing multi-layer step. No numerical linear independence, universal carrier impossibility or necessary prime-cost minimum is asserted.

## 8. Accurate review receipt

Author receipt: the mathematical text was derived on paper from the source scope in section1 and the cited frozen interfaces. The author actually FULL read all seven G1–G21 mathematical sections without truncation after writing, and actually FULL reread the final eight-section file including this receipt after the receipt update. No original note, main, manifest or historical ledger was modified.

Initial independent review: root actually FULL read the 15428-byte version, SHA256 c09fd19be55a2f3c9ebbd0c6bd0fb10e631f6d4f3c9a98a67266462ccefd8c37, and independently paper-checked G1–G21. It found the omitted factor D+1=d+h in B_d(0); the exact formula and G14 valuation were corrected above. This adds only O(log N) per row and leaves every stated N² leading bound unchanged. Root also requested the explicit current p=m+1 source scope for the frame proof of G19; that scope is now stated. Its review otherwise returned mathematical PASS. This receipt records the correction rather than an unqualified initial PASS.

Independent correction review: gamma_bound actually FULL read the same 15428-byte seven-section initial version, then actually read complete sections4–5 of the 16371-byte corrected version, SHA256 67146f31a50883e8b349e2cd8c19f39a3afab96ea2da2658a0f3de8746584104. Its second reading was bounded, not FULL. It independently paper-checked the corrected zero-endpoint factor and valuation, the p=m+1 exterior scope and G20's fixed-tail-prefactor limit, with PASS and no further correction. Its initial FULL reading also checked the common 2-adic sum/all-power certificate, content interval, complete operator bounds and low/central residue counts. The G14 correction is credited to root. Neither review ran code, a producer or a scan.

Root correction review: root actually bounded-read complete sections4–5 and the then-section7 receipt of that same 16371-byte version and SHA256. It independently paper-checked the corrected G14 identity/valuation, G19's p=m+1 source scope and G20's fixed-tail-prefactor method limit with PASS. This is an initial FULL reading plus a bounded correction/receipt reading, not a second FULL review. Only this receipt was appended thereafter; the mathematical text was frozen.
