# Principal mixed moments: joint Cauchy structure and the corner block

2026-10-07. NEW isolated paper interface, round 215. The principal object is the actual n=44N−1 red square with all 36N−1 Jacobi rows and the selected first 8N pure-D tails. This proves an exact closed section, a constant-rank actual Stein displacement, an orthogonal two-level Cauchy representation, an exact N²-scale polynomial block, and precise limits on deleting that block. It establishes no favorable full leading estimate or actual conditional moment nonvanishing. No producer, prime scan or finite determinant experiment was run.

## 1. Actual section and the two endpoints

Keep
\[
n=44N-1,\ r=36N-1,\ m=8N,\quad
A=19N,\ h=2N,\ b=7N,\ q=4N,\ e=h+q=6N,
\]
\[
L=55N-1,\ m_0=L-A-1=36N-2,\quad
d_-=8N+1,\ d_+=44N-1.
\tag{I1}
\]
Let Q_d=P_d^(e−1/2,−1/2), P_Q=t^A(1−t)^hQ, f(t)=sqrt(1−t²) with f(0)=1, and dnu_e=(1−t)^e dt/(pi sqrt(1−t²)). Every selected Q has zero nu_e moments of orders 0,...,8N.

Define its polynomial second-kind transform
\[
B_Q(z)=\int_{-1}^1
 { (1-z)^eQ(z)-(1-x)^eQ(x)\over z-x}\,d\nu_0(x),
\qquad
W_Q(z)=\int_{-1}^1{Q(x)\over z-x}\,d\nu_e(x).
\]
The arcsine generating series gives
\[
{(1-z)^eQ(z)\over\sqrt{z^2-1}}=B_Q(z)+W_Q(z),
\qquad W_Q(z)=O(z^{-8N-2}) .
\]
The infinity branch is sqrt(z²−1)~z. The actual triangular/zero-end section is exactly
\[
\boxed{\begin{aligned}
F_Q(t)&={Q(t)\over f(t)}-\mu\,{B_Q(t)\over(1-t)^e},\\
E_Q(t)&=\operatorname{trunc}_{<m_0}F_Q(t),\\
D_\mu(Q)(t)&=t^{A+1}(1-t)^h E_Q(t).
\end{aligned}}
\tag{I2}
\]
This retains both D_H and mu D_C.

Here is the coefficient justification. Write Cpoly(P)=PolyPart_infty[tP/sqrt(t²−1)]. Moving (1−t)^q inside this polynomial part creates only a polynomial discrepancy of degree at most q−1. The polynomial part of t^(A+1)W_Q has degree at most A−8N−1=b+q−1=11N−1. Thus
\[
(1-t)^q Cpoly(P_Q)-t^{A+1}B_Q(t)
\quad\hbox{has degree at most }11N-1.
\]
The filtered outputs are the coefficients at b+q,...,L−1; all relevant high coefficients at A+1,...,L−1 are therefore those of t^(A+1)B_Q. The zero initial D coefficients and the unit triangular recursion imply
(1−t)^q D_C≡t^(A+1)B_Q mod t^L. Dividing its endpoint factor (1−t)^h gives E_C=trunc B_Q/(1−t)^e. For D_H the zero initial coefficients directly give D_H,j=H_j(P) below L, hence E_H=trunc Q/f. These are precisely I2, with m_0=L−A−1. No free tail adjustment or coefficient-height estimate enters.

Use the actual row function and bilinear form
\[
U_{P,D}(s)=\int_{-1}^1{P(t)\over1-ts}d\sigma(t)
 -{3\over2}\int_0^1{D(t)\over1-ts}dt,\quad
d\sigma=|t|dt/\sqrt{1-t^2},
\]
\[
\mathcal F(P,D;V)=\int_0^1U_{P,D}(s)V(s)\,ds.
\tag{I3}
\]
The original filtered columns use V=s^(b+k)(1−s)^q. Under the hypothetical rational relation these actual filtered entries are the conditional rational ones. The red scalar lambda_d=d_mu 2^(s_d)4^d, s_d=max(14N+d−(d mod2),36N−4), multiplies both P and its actual D.

## 2. The exact section commutator

Direct polynomial division gives
\[
B_{tQ}(z)=zB_Q(z)+\int Q\,d\nu_e.
\]
The last integral vanishes for every selected Q. Thus F_(tQ)=tF_Q. If theta(Q)=[t^(m_0−1)]F_Q, truncation gives
\[
\boxed{D_\mu(tQ)=tD_\mu(Q)-\theta(Q)T_0,\qquad
T_0=t^L(1-t)^h.}
\tag{I4}
\]
I2 defines the same linear formal section also for the two adjacent Jacobi polynomials used as exterior boundary rows. It need not put those boundary rows in the contact space; no arithmetic claim is made for them.

For any polynomial pair put
\[
\eta(P,D)=\int P\,d\sigma-\frac32\int_0^1D(t)\,dt.
\]
The elementary identity st/(1−st)=1/(1−st)−1 proves
\[
\boxed{\mathcal F(P,D;V)-\mathcal F(tP,tD;sV)
=\eta(P,D)\int_0^1 V(s)\,ds.}
\tag{I5}
\]
I4–I5 retain the full mu-dependent section. They are identities of actual integrals, not relations inferred from finite samples.

## 3. Real orthogonal bases with every determinant factor paid

Let rho_d=int Q_d²dnu_e, exactly R13 of the real-place note, and chi_d=Q_d/sqrt(rho_d), d_-≤d≤d_+. Use the actual Jacobi row pairs
\[
g_d=(P_{\chi_d},D_\mu(\chi_d)).
\]
Let psi_a, 0≤a<m, be the positive-leading orthonormal polynomials for t^L(1−t)^h dt on (0,1). The tail pairs are
\[
\tau_a=(0,t^L(1-t)^h\psi_a(t)).
\]
Let phi_k, 0≤k<n, be the positive-leading orthonormal polynomials for w(s)ds=s^b(1−s)^qds on (0,1). Define the real actual matrix
\[
\mathcal M_{i,k}=\mathcal F(r_i;w\phi_k),
\]
where the row list r_i consists of all g_d and these m tails, in that order.

For H_j(a,c)=det B(a+u+v+1,c+1), the exact determinant identity is
\[
\boxed{\Delta_{\rm red}=
 \left(\prod_{d=d_-}^{d_+}\lambda_d\sqrt{\rho_d}\right)
 \sqrt{\mathcal H_m(L,h)\mathcal H_n(b,q)}
 \det\mathcal M.}
\tag{I6}
\]
To verify it, first change monomials to the corresponding monic orthogonal polynomials by unit triangular row/column changes. Then divide by the square roots of their positive squared norms. The product of the squared norms is precisely the stated beta Gram determinant. On the Jacobi rows divide by lambda_d sqrt(rho_d). The D section is linear, so the same scaling applies to the full pair. All these real changes are paid explicitly in I6; they do not claim a fresh integer-row denominator bound.

## 4. A constant-rank actual Stein displacement

Orthogonality proves the three-term recurrence for each of chi, psi and phi: multiplication by its variable has no components more than one degree away. For the high Jacobi block, let J be the symmetric tridiagonal compression of multiplication by t to chi_(d_-),...,chi_(d_+). Let T be the symmetric tridiagonal compression to psi_0,...,psi_(m−1), and C the corresponding n-square column compression to phi_0,...,phi_(n−1).

Since T_0 equals sqrt(B(L+1,h+1)) times the first normalized tail, I4 shows that row multiplication is
\[
t r_i=\sum_j\mathcal R_{ij}r_j+\sum_{\ell=1}^3B_{i\ell}r_\ell^{\rm ext},
\]
\[
\boxed{\mathcal R=
 \begin{pmatrix}J&\kappa e_0^t\\0&T\end{pmatrix},
\qquad
\kappa_d=\theta(\chi_d)\sqrt{B(L+1,h+1)}.}
\tag{I7}
\]
There are only three exterior rows: the lower adjacent Jacobi polynomial chi_(d_-−1), the higher one chi_(d_++1), and the next tail psi_m. The matrix B has nonzero entries only in the first/last Jacobi rows and the last selected tail row. All section, recurrence and boundary functions here are explicit finite expressions.

On columns,
\[
s\phi_k=\sum_{j<n}C_{jk}\phi_j+\xi_n\phi_n\delta_{k,n-1},
\qquad \xi_n>0.
\]
Let M_ext be the three exterior rows evaluated in the current n columns; let v_n and v_ext be their respective phi_n moment vectors. Let eta_i be eta(r_i). Inserting the row and column recurrences into I5 gives the exact identity
\[
\boxed{\begin{aligned}
\mathcal M-\mathcal R\mathcal M C=\mathcal E,\qquad
\mathcal E={}&
 \sqrt{B(b+1,q+1)}\,\eta e_0^t+B M_{\rm ext}C\\
 &+\xi_n(\mathcal Rv_n+Bv_{\rm ext})e_{n-1}^t .
\end{aligned}}
\tag{I8}
\]
The first term has only the first column, because phi_k is orthogonal to the constant for k≥1. The second term has only the three boundary rows. The third term has only the last column. Therefore
\[
\operatorname{rank}\mathcal E\le5 .
\tag{I9}
\]
This is a joint operator identity with the actual D_mu, including its last-coefficient commutator. It is stronger than another row-norm estimate. It does not imply that det M is nonzero.

## 5. A two-level Cauchy representation without spectral-separation assumptions

For a nonzero polynomial u in the relevant finite space, all integrals of (1±t)|u|² against nu_e are positive. Thus every eigenvalue x_i of J lies strictly in (−1,1). The positive measures on (0,1) similarly give
\[
z_a\in(0,1)\quad\hbox{for }T,\qquad
y_j\in(0,1)\quad\hbox{for }C.
\tag{I10}
\]
These facts hold for every N, by the Rayleigh quotient. They do not assert a uniform N-independent distance between a spectral endpoint and 1.

Orthogonally diagonalize each block. Let the transformed upper coupling be h v^t, and transform M and E by the same orthogonal row-block and column matrices. These changes have determinant of absolute value 1. In this basis I8 is solved columnwise:
\[
\boxed{\begin{aligned}
M^{T}_{a,j}&={E^{T}_{a,j}\over1-z_a y_j},\\
M^{J}_{i,j}&=
 {E^{J}_{i,j}
 +y_j h_i\displaystyle\sum_a{v_aE^{T}_{a,j}\over1-z_a y_j}
 \over1-x_i y_j}.
\end{aligned}}
\tag{I11}
\]
All denominators are positive. No assumption that the x and z spectra are disjoint is required, even if they share an eigenvalue. The coupling is rank one, but its full mu dependence is retained in h and in the actual forcing entries E.

Equivalently,
\[
\mathcal M=\sum_{\nu\ge0}\mathcal R^\nu\mathcal E C^\nu .
\tag{I12}
\]
For fixed N this converges: R is block triangular with spectra J and T strictly inside the unit disk, while C has spectrum in (0,1). Possible Jordan factors have only polynomial growth. I8 consequently has a unique solution for its given actual forcing. That forcing still contains the specified exterior-row and next-column moments from I8; uniqueness does not estimate these generators or make them independent data.

I11 gives a genuine pair of coupled Cauchy kernels, rather than a presumed positive mixed row determinant. The forcing rank is at most five, and its boundary generators are exactly I8. Kernel denominators have a known sign; h and E have no established common sign. A leading determinant estimate must control these actual generators and their coupled exterior determinant. Replacing them by independent free polynomial rows, or by row maxima, loses the structure just paid.

## 6. The zero-junction core has a paid N²-scale polynomial block

This section uses a different but determinant-preserving column representation. Transfer the filter into the row, F_Q(s)=(1−s)^q U_(P_Q,0)(s), and use monic orthogonal columns vartheta_k for s^b ds. This is the same actual M moment array before adding D, with the filter retained; its column transform is unit triangular.

Put K=A−q+1=15N+1. For d>K, R18–R19 give
\[
F_{Q_d}(s)=Z_d(s)+\pi\mathcal E_{d,K}(s),\qquad
Z_d=\mathcal P_d+\pi\,\hbox{junction}_d,\quad \deg\mathcal P_d<q.
\]
The junction has degree d−1−K and leading coefficient 2^(1−d)/(pi d). Hence for
\[
A+2=19N+2\le d\le44N-1,\qquad
\delta_d=d-1-K,
\]
the full polynomial Z_d has degree delta_d and leading coefficient
\[
\ell_d=2^{1-d}/d>0 .
\tag{I13}
\]
There are exactly 25N−2 such rows, with delta_d=q,...,29N−3. Thus the polynomial part, even after including the quotient term, has rank at least 25N−2. The junction alone on all d>K has exact rank 29N−2, from its distinct leading degrees. These are linear-rank statements for actual derived polynomials, not independence claims for the final moment rows.

For the high rows I13 and columns k=q,...,29N−3, orthogonality makes the polynomial-component block triangular:
\[
\int_0^1 Z_d(s)\vartheta_k(s)s^bds=0
\quad(k>\delta_d),
\]
and its diagonal is ell_d times the monic squared norm at k=delta_d. Consequently its exact red-normalized determinant is
\[
\boxed{\Omega_N=
 \left(\prod_{d=19N+2}^{44N-1}
       \lambda_d\,{2^{1-d}\over d}\right)
 {\mathcal H_{29N-2}(b,0)\over\mathcal H_{4N}(b,0)}>0.}
\tag{I14}
\]
This pays an explicit block Vandermonde/orthogonality factor on the N² scale.

For X(x)=x²log x/2−x²/4, X(0)=0, define
\[
\mathscr H(a;b,c)=X(a)+X(b+a)-X(b)+X(c+a)-X(c)
-X(b+c+2a)+X(b+c+a).
\]
Stirling and the exact red scalar give
\[
\boxed{\lim N^{-2}\log\Omega_N=
 {3859\over2}\log2+\mathscr H(29;7,0)-\mathscr H(4;7,0).}
\tag{I15}
\]
The sum of d over this block has leading coefficient 1575/2; the sum of s_d has leading coefficient 1142. The factors 1/d cost only O(N log N). The exact expression is approximately −12.49967567. This is the polynomial component alone. The full block includes the genuine Rodrigues remainder and the full filtered D_mu transform; no lower or upper bound for their combined block follows by dropping them from I14. This block calculation and I6 use distinct column weights and must not have their Gram factors mixed.

## 7. What exact D projection can and cannot remove

The analytic Stieltjes map (P,D)↦U_(P,D) is injective on all polynomial pairs. Here is a direct proof. It extends from the germ at s=0 to the slit plane with cuts [1,infinity) and (−infinity,−1]. For real s>1 put x=1/s. A local subtraction of the continuous density at t=x and integration of 1/(1−st) gives the upper-minus-lower boundary jump
\[
2\pi i\left[{P(x)\over s^2\sqrt{1-x^2}}
 -{3D(x)\over2s}\right].
\tag{I16}
\]
This local jump calculation can also be obtained by integrating the constant-density term explicitly; the remainder is continuous across that interior point.

If U is zero, the jump vanishes on (0,1). Thus xP(x)=(3/2)sqrt(1−x²)D(x), and polynomial continuation gives
x²P(x)²=(9/4)(1−x²)D(x)². At x=1, the two nonzero sides would have respectively even and odd orders. This is impossible. Therefore P=D=0.

It follows that for every real mu the selected Jacobi row functions modulo the selected pure-D span have rank r=36N−1. Their normalized residual Gram determinant in the actual H_s is strictly positive. Indeed a linear combination lying in the tail span would give U_(P,D−tail)=0 and hence P=0; the Jacobi polynomial basis is independent. This pays a function-space exterior rank, not nonvanishing of its compression to only n prescribed moment columns.

For pure D one has the exact expression
\[
\int_0^1{D(t)\over1-ts}dt
=-{D(1/s)\over s}\log(1-s)
-\sum_iD_i\sum_{\ell=0}^{i-1}
 {s^{\ell-i}\over\ell+1}.
\tag{I17}
\]
Apparent zero-end poles cancel in this expression. A nonzero such transform cannot be a rational function: its logarithmic coefficient is nonzero, or equivalently its boundary jump is nonzero. Multiplication by (1−s)^q does not change this conclusion. Thus the entire filtered polynomial D-transform space has zero intersection with the rational functions.

In particular a nonzero junction polynomial cannot be exactly replaced by a pure-D tail function. This statement may be made in L²((0,1),s^bds) after filtering. It must not be misused as a projection assertion about a standalone junction divided by (1−s)^q in H_s: that divided function may fail to lie in H_s. The rational pieces of I17 and the nonrational Rodrigues term can still cancel in the full joint operator. I16–I17 do not rule out favorable coupled singular values in I11 or R9.

There is also a dimension cost for a proposal to kill every sign-junction term simply by requiring d≤K. The allowed low Jacobi directions d_-≤d≤K have only 7N+1 dimensions. Even with every 8N+1 permitted pure-D tail, the total is 15N+2, smaller than n=44N−1 by 29N−3. Such a proposal cannot retain the principal square. Raising the zero-end order enough to meet K≥d_+ also changes the ambient row count and needs new arithmetic. Moreover removal of a jump alone would not prove a favorable analytic bound.

## 8. Exact next comparison and reading scope

The current primitive-content interval result P10 gives the paid same-red lower exponent
\[
\liminf N^{-2}\log|\Delta_{\rm red}|\ge-15169/4
\tag{I18}
\]
along nonzero conditional determinants. The author actually FULL read its six-section P1–P11 note for this continuation and rechecked the interval implication P7–P11; this is not an assumption of a full-content asymptotic.

In I6 the paid orthogonal prefactor has leading logarithm
\[
B_*={1\over2}\mathscr H(44;7,4)
 +{1\over2}\mathscr H(8;55,2)+3518\log2 .
\]
A strict upper estimate capable of meeting I18 would therefore be
\[
\boxed{\limsup N^{-2}\log|\det\mathcal M|
<-15169/4-B_* .}
\tag{I19}
\]
Alternatively retain R9/R12 and normalize the residual Gram by sqrt(rho_d). If theta_*=limsup N^(-2)log det Ghat_R, the exact sufficient exterior target is
\[
\boxed{\theta_*<2(-15169/4-G_*),}
\tag{I20}
\]
where
\[
G_*=B_*+4\{\mathscr B(55,2)+\mathscr B(7,4)\},\quad
\mathscr B(a,c)=a\log a+c\log c-(a+c)\log(a+c).
\]
The right side of I20 is approximately −8782.19501187. I19–I20 are exact quantified targets, not additional trace/row-norm upper bounds. A scalar change of row normalization changes both sides consistently. The proved content interval is not counted twice.

The new paid interface is I8–I15: constant-rank actual forcing with two-level Cauchy denominators, and an exact polynomial block on the leading scale. What remains is a bound for its actual mu-dependent boundary generators and the full coupled exterior determinant, together with actual relation-point moment nonvanishing. Positivity of the denominators and the polynomial component does not pay those steps. Repeated generic-rank or finite-sample evidence cannot change I19. The concrete condition for a different kernel is to remove or relocate the interior sign jump while still representing both target periods and paying its new D section and denominator model; the present 44N−1 support cannot do this by discarding the high directions just counted.

Actual current FULL reading for this task: the ten-section contact note, eight-section weighted-column C1–C15 note, ten-section real-place R1–R26 note, and six-section primitive-content P1–P11 note, all with untruncated outputs. Only their stated actual kernels, section, Rodrigues formula, Gram factors and current finite-place interval bound are used. No new primary webpage, PDF or HTML was read/downloaded. The three-term, spectral and jump arguments were derived above; no unverified Nikishin or potential-theory theorem is invoked. This is not a full audit of the original Catalan paper.

Review receipt: gamma_bound actually FULL read all eight sections I1–I20 of the 17460-byte version SHA256 05760fc7380b7fd4402a68a8da790bbbfeb5dd5a0dfd0095b47f2768476a4560 and independently checked every displayed identity, normalization and scope limit, with mathematical PASS. Its only wording correction was the square-root wording in I6, now implemented. The author actually FULL reread that version and independently rechecked the actual section, recurrence, displacement signs, orthogonal determinant factors, corner degree/block and same-red comparison. Root actually FULL read all eight sections I1–I20 of the subsequent 18286-byte version SHA256 76dc5ab293ade62adb617517bd68ef2f8aad28d1105f988a182d4c971917c189 and independently checked the boundary signs in I4/I8, orthogonal Gram factors I6, spectral intervals and coupled resolvent, high-corner degree/count/scalar I13–I15, the I16 jump and function-space rank distinction, and the same-red comparison I19–I20, with mathematical PASS and no correction. The final receipt-bearing author FULL reread and byte/SHA256 pin are recorded in this continuation's completion message.

