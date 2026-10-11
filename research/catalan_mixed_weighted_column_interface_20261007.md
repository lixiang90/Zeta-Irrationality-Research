# Actual mixed Jacobi moments: a weighted column interface

2026-10-07. NEW isolated paper lemma for every N≥1. The principal object is the same 44N−1 square and actual D_mu section as the contact and real-place notes. This proves an exact monic Jacobi column change, its endpoint justification, a full beta-series expression for the D_mu contribution, and explicit finite Hadamard upper bounds. It proves neither a favorable leading gap nor actual-point nonvanishing. No producer, supplied program, prime scan or numerical determinant experiment was run.

## 1. Fixed actual rows and normalization

Keep
\[
n=44N-1,\quad b=7N,\quad q=4N,\quad
A=19N,\quad h=2N,\quad e=6N,\quad L=55N-1,
\]
\[
r=36N-1,\quad m=8N,\quad m_0=L-A-1=36N-2.
\tag{C1}
\]
Fix nonzero rational mu=16 beta/alpha. For 8N+1≤d≤44N−1 set
\[
Q_d(t)=P_d^{(e-1/2,-1/2)}(t)
      =\sum_{j=0}^d q_{d,j}t^j,\qquad
P_d^0=t^A(1-t)^hQ_d(t).
\]
Prescribe D_j=0 for j≤A. The actual filtered equations
\[
\sum_{v=0}^q(-1)^v\binom qvD_{b+k+v}
=\sum_{v=0}^q(-1)^v\binom qv
 (H_{b+k+v}(P)-\mu C_{b+k+v}(P))
\]
solve the coefficients at A+1≤j<L by the unit triangular recursion of the ten-section contact note. Use exactly its zero-end section:
\[
D_d^0=t^{A+1}(1-t)^h
 \operatorname{trunc}_{<m_0}
 \left(t^{-(A+1)}D_{<L}/(1-t)^h\right)
=t^{A+1}(1-t)^h\sum_{j<m_0}E_{d,j}(\mu)t^j .
\tag{C2}
\]
Every E_(d,j)(mu) is the prescribed rational affine expression
E_(d,j)^H−mu E_(d,j)^C; it is not freely chosen to improve a bound. Adjoin the m pairs (0,T_a) with T_a=t^(L+a)(1−t)^h, 0≤a<m. There is one additional permitted homogeneous tail in the full pool which this square does not select.

The bare determinant uses these pairs. Multiplication of both P and D in Jacobi row d by a positive scalar lambda_d multiplies the determinant by prod_d lambda_d. The row-specific integral choice is
\[
\lambda_d^{\rm red}=d_\mu2^{s_d}4^d,\qquad
s_d=\max(14N+d-(d\bmod2),36N-4).
\tag{C3}
\]
The other current choices are lambda_d^4=d_mu 2^(58N−2)4^d and lambda_d^old=d_mu 2^(58N−2)8^d. Their exact determinant scalars are those of R4–R5 in the real-place note. No normalization is removed from only one side of an arithmetic/analytic comparison.

## 2. The actual filtered moments

Put
\[
d\sigma(t)=|t|\,dt/\sqrt{1-t^2},\qquad
w(s)=s^b(1-s)^q,
\]
\[
U_i(s)=\int_{-1}^1\frac{P_i(t)}{1-ts}d\sigma(t)
-\frac32\int_0^1\frac{D_i(t)}{1-ts}dt .
\tag{C4}
\]
The actual bare matrix is
\[
M_{i,k}=\int_0^1 U_i(s)s^kw(s)\,ds,\qquad 0\le k<n.
\]
Its determinant is Delta_0; the normalized determinant is Delta_lambda=(prod_d lambda_d)Delta_0. Under alpha G+beta pi²=u these actual filtered entries equal the conditional rational moment entries. The unfiltered raw rational array is not substituted for C4.

Define the actual nonnegative masses
\[
a_{i,k}=\int_{-1}^1|P_i(t)||t|^k\,d\sigma(t)
+\frac32\int_0^1|D_i(t)|t^k\,dt .
\tag{C5}
\]
All are finite. Differentiation under the integral on compact s intervals gives, for every integer ell≥0,
\[
U_i^{(\ell)}(s)=\ell!\left[
 \int_{-1}^1\frac{P_i(t)t^\ell}{(1-ts)^{\ell+1}}d\sigma(t)
-\frac32\int_0^1\frac{D_i(t)t^\ell}{(1-ts)^{\ell+1}}dt\right],
\]
\[
|U_i^{(\ell)}(s)|\le\ell!a_{i,0}(1-s)^{-\ell-1}.
\tag{C6}
\]
It is also bounded near s=0. These estimates justify the endpoint calculations below; no mixed positivity is assumed.

## 3. A determinant-preserving monic Jacobi column change

Let
\[
L_k=\binom{2k+b+q}{k},\qquad
\pi_k(s)=L_k^{-1}P_k^{(q,b)}(2s-1).
\]
This is the monic polynomial of degree k orthogonal for w(s)ds. Its shifted Rodrigues identity is
\[
w(s)\pi_k(s)=
\frac{(-1)^k}{k!L_k}
\frac{d^k}{ds^k}\left[s^{b+k}(1-s)^{q+k}\right].
\tag{C7}
\]
One can establish C7 directly: after dividing by w its right side is a degree-k polynomial, k integrations by parts give orthogonality to all degrees below k, and its leading coefficient is 1. Before making it monic that leading coefficient is L_k. This also identifies it with the stated shifted Jacobi polynomial.

Since pi_k=s^k plus lower powers, replacing columns s^k by pi_k uses a unit triangular matrix. Thus
\[
\det M=\det\widetilde M,\qquad
\widetilde M_{i,k}=\int_0^1U_i(s)\pi_k(s)w(s)\,ds .
\]
There is no extra product of L_k in the column transformation; L_k appears inside the exact entry formula after Rodrigues.

## 4. Endpoint payment and the exact actual entry

Write g_k(s)=s^(b+k)(1−s)^(q+k). At an intermediate integration by parts, the endpoint terms have the form U_i^(ell) g_k^(k−1−ell), 0≤ell<k. Near s=1 the second factor is O((1−s)^(q+1+ell)); C6 makes their product O((1−s)^q), which tends to zero. Near s=0 it is O(s^(b+1+ell)) and U_i^(ell) is bounded. All endpoint terms therefore vanish. The final integral is absolutely convergent, since its absolute value is bounded by k! a_(i,k) times
int s^(b+k)(1−s)^(q−1)ds. Here q=4N>0. The k=0 formula needs no integration by parts.

The two signs from Rodrigues and integration by parts cancel, and C6 cancels the k!:
\[
\boxed{\begin{aligned}
\widetilde M_{i,k}
={1\over L_k}\int_0^1 s^{b+k}(1-s)^{q+k}
 \left[
 \int_{-1}^1{P_i(t)t^k\over(1-ts)^{k+1}}d\sigma(t)
 -{3\over2}\int_0^1{D_i(t)t^k\over(1-ts)^{k+1}}dt
 \right]ds .
\end{aligned}}
\tag{C8}
\]
This is the actual reduced-row identity for all N and every selected row, with its full D_mu contribution. Negative t produces t^k with its actual sign. Kernel positivity cannot be used to declare the mixed determinant nonzero.

## 5. Full D_mu beta terms

For a Jacobi row, expand its actual D polynomial in the endpoint basis C2. Its contribution in C8 is exactly
\[
-{3\over2L_k}\sum_{j<m_0}E_{d,j}(\mu)\,
 \sum_{\nu\ge0}\binom{k+\nu}{\nu}
 B(A+j+k+\nu+2,h+1)
 B(b+k+\nu+1,q+k+1).
\tag{C9}
\]
Indeed (1−ts)^(-k−1)=sum_(nu≥0)binom(k+nu,nu)(ts)^nu on (0,1)². For each j all terms are nonnegative before multiplying by its finite scalar E_(d,j)(mu). The whole series is absolutely convergent: 1−ts≥1−s bounds the associated double integral by
B(A+j+k+2,h+1) B(b+k+1,q). Thus Fubini or monotone convergence pays each interchange. No portion of D_H or mu D_C is omitted.

For a pure-D tail the exact entry is
\[
-{3\over2L_k}\sum_{\nu\ge0}\binom{k+\nu}{\nu}
 B(L+a+k+\nu+1,h+1)
 B(b+k+\nu+1,q+k+1).
\tag{C10}
\]
These entries have a known sign, but that proves no full mixed sign assertion.

For completeness, the P contribution also has the absolutely convergent series
\[
{1\over L_k}\sum_{\nu\ge0}\binom{k+\nu}{\nu}
 B(b+k+\nu+1,q+k+1)\,I_{k+\nu}(P),
\]
\[
I_\ell(P)=\int_{-1}^1P(t)t^\ell\,d\sigma(t)
 =\sum_{\substack{j\\j+\ell\ {\rm even}}}
 p_j B((j+\ell)/2+1,1/2),\quad P=\sum_jp_jt^j.
\tag{C11}
\]
Absolute convergence follows by replacing t by |t| in the geometric series and using 1−|t|s≥1−s. Thus C9–C11 are complete exact entries in beta functions and the actual finite coefficients, not a replacement polynomial-row model.

## 6. Explicit finite beta masses retaining both endpoint factors

Put
\[
c_k={B(b+k+1,q)\over L_k}>0 .
\]
C8 and 1−ts≥1−s give
\[
|\widetilde M_{i,k}|\le c_k a_{i,k}.
\tag{C12}
\]
For a pure-D tail its exact mass is a_(a,k)=(3/2)B(L+a+k+1,h+1).

For a Jacobi row define
\[
\overline P_{d,k}=
\sum_{j=0}^d|q_{d,j}|
 \sum_{\substack{0\le v\le h\\v\ {\rm even}}}
 \binom hv B((A+j+k+v)/2+1,1/2),
\]
\[
\overline D_{d,k}(\mu)=
{3\over2}\sum_{j<m_0}|E_{d,j}(\mu)|B(A+j+k+2,h+1).
\tag{C13}
\]
Then a_(d,k)≤barP_(d,k)+barD_(d,k)(mu). To check the P term, use the triangle inequality on Q_d without expanding its endpoint factor. Pair positive and negative t:
\[
(1-t)^h+(1+t)^h=
2\sum_{\substack{0\le v\le h\\v\ {\rm even}}}\binom hv t^v,
\]
and evaluate int_0^1 t^(A+j+k+v+1)/sqrt(1−t²)dt as one half of the displayed beta function. This proves C13 and retains t^A and (1−t)^h. The D bound uses its actual endpoint factor and coefficients in C2. In particular it retains the complete dependence on mu.

All q_(d,j) are explicit rational coefficients of the finite Jacobi binomial formula, and all E_(d,j)(mu) are the specified finite triangular/endpoint section. Thus C13 is a fully specified finite bound; no unspecified inverse height or independently adjustable D remains.

## 7. The finite Hadamard interface

Factor c_k out of column k of the transformed matrix, and the chosen lambda_d out of each Jacobi row. Its bare entries are bounded by a_(i,k). Row Hadamard therefore proves
\[
\boxed{
|\Delta_\lambda|\le
\left(\prod_d\lambda_d\right)
\left(\prod_{k=0}^{n-1}c_k\right)
\prod_i\left(\sum_{k=0}^{n-1}a_{i,k}^2\right)^{1/2}.}
\tag{C14}
\]
An entirely explicit beta upper bound is
\[
\boxed{\begin{aligned}
|\Delta_\lambda|\le&
 \left(\prod_d\lambda_d\right)
 \left(\prod_{k=0}^{n-1}{B(b+k+1,q)\over L_k}\right)\\
&\times\prod_{d=8N+1}^{44N-1}
 \left[\sum_{k=0}^{n-1}
 (\overline P_{d,k}+\overline D_{d,k}(\mu))^2\right]^{1/2}\\
&\times\prod_{a=0}^{m-1}
 \left[\sum_{k=0}^{n-1}
 \left({3\over2}B(L+a+k+1,h+1)\right)^2\right]^{1/2}.
\end{aligned}}
\tag{C15}
\]
The bound permits the determinant to be zero. It does not presume that linearly independent polynomial pairs have independent moment rows. It applies to the exact selected square C1, including all its actual D_mu rows. For another all-tail/Jacobi subset, C8–C15 must retain precisely that chosen row list and its scalar product.

## 8. Relation to the residual wedge and review scope

C8 supplies a concrete weighted-column operator, and C9/C13 pay the full D_mu beta terms. C15 is an explicit finite all-N upper bound. No leading coefficient of C15 has been proved favorable; no numerical scan has been used to suggest one. Triangle inequalities and row Hadamard can lose precisely the joint cancellations needed for the intended comparison.

This is not a replacement for the exact residual exterior determinant in R9 of the real-place note. The selected pure-D projection there removes tail components without inverse coefficient-height loss; C15 instead charges all selected rows separately. The weighted operator C8 can be combined with an exact tail Schur or exterior calculation, but that additional estimate must be proved. Neither generic C rank nor finite nonzero samples supplies it.

The author actually FULL read the contact ten-section note, the real-place R1–R26 note, the finite-place J1–J30 note, and the current Schur/jet notes as recorded in literature/catalan_mixed_jacobi_real_place_source_scope_20261007.md. The primary [NIST Jacobi norm and leading coefficient](https://dlmf.nist.gov/18.3#T1) and [Rodrigues row](https://dlmf.nist.gov/18.5#T1) had already been opened and their relevant entries read; no new public PDF or HTML was downloaded. C7–C15 are derived here from the actual moments. This is a bounded new-interface proof, not an audit of the entire original Catalan paper.

The author actually FULL reread the eight-section C1–C15 note. Independent review receipts: universal_normalization and gamma_bound each actually FULL read all eight sections, with untruncated output, and independently paper-checked C1–C15. Both found mathematical PASS without repair. Their scope includes the exact shifted leading coefficient and monic column determinant, both signs and k!, all integration endpoints, the complete actual D_mu beta terms and series interchanges, the P parity formula, positive/negative t pairing, the finite Hadamard bound, the selected eight-N tails and scalar convention, and the limits of the result. Neither ran a producer or a scan.

Root review receipt: the root actually FULL read all eight sections C1–C15 and independently checked monic leading/Rodrigues, every integration-by-parts endpoint, every index in the beta double series, P parity and endpoint absolute masses, C14–C15, the selected square and all row scalars: mathematical PASS without repair. Adding these exact receipts changes no mathematical formula. No receipt proves the remaining leading gap or actual-point nonvanishing.

