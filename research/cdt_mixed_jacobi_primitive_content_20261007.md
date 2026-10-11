# Exact all-prime Jacobi content and its strategic ceiling

2026-10-07. New paper lemma, no numerical content scan or historical producer. The purpose is to decide whether primitive row contents can materially change the current same-object comparison. No new numerical irrationality or linear independence theorem is claimed.

## 1. Integer Newton coefficients

Let `d>=1,e>=0` be integers and `J_d=P_d^(e-1/2,-1/2)`. The [primary Jacobi hypergeometric formula, DLMF 18.5.7](https://dlmf.nist.gov/18.5#E7), together with the symmetry obtained by reindexing the finite binomial formula, gives

\[
J_d(x)=(-1)^d c_d\,{}_2F_1
\left(-d,d+e;\tfrac12;\tfrac{1+x}{2}\right),
\qquad c_d=4^{-d}\binom{2d}{d}.
\]

Expanding this terminating series yields the exact Newton-basis coefficients

\[
4^dJ_d(x)=\sum_{k=0}^d A_k(x+1)^k,
\]

\[
\boxed{A_k=(-1)^{d+k}\binom{2d}{d}
 \frac{d!}{(d-k)!}
 \frac{(d+e+k-1)!}{(d+e-1)!}
 \frac{2^k}{(2k)!}.}
\tag{P1}
\]

Indeed `(-d)_k=(-1)^k d!/(d-k)!` and `(1/2)_k=(2k)!/(4^k k!)`. The factor `(1+x)^k/2^k` leaves precisely `2^k/(2k)!` in P1. This proves the formula, rather than inferring it from any finite coefficient sample.

The previous formal-generating-series proof establishes `4^d J_d in Z[x]` for every d,e. The translation from monomials to `(x+1)^k` and its inverse both have integer triangular matrices with diagonal 1. Thus every A_k is an integer, and the gcd of these Newton coefficients is the exact content of the ordinary integer polynomial. In particular

\[
A_0=(-1)^d\binom{2d}{d},\qquad
A_d=2^d\binom{2d+e-1}{d}.
\]

The root actually read the selected DLMF equation and its immediate attribution, not all of chapter 18. A direct download of its TeX encoding failed; no missing TeX snapshot is counted as archived. The mathematical derivation and the source URL above remain explicit.

## 2. All primes and powers, exactly

Define `F_p(j)=sum_(r>=1) floor(j/p^r)` for nonnegative integers j, and

\[
g(d,e)=\gcd(A_0,\ldots,A_d)>0.
\]

P1 gives the exact valuation formula

\[
\boxed{v_p(g(d,e))=\min_{0\le k\le d}
\left\{F_p(2d)-2F_p(d)+F_p(d)-F_p(d-k)
 +F_p(d+e+k-1)-F_p(d+e-1)-F_p(2k)
 +k\,v_p(2)\right\}.}
\tag{P2}
\]

This includes p=2, every small prime, and every prime power. All summands in F_p are finite. The minimum is taken only after summing all power layers; exchanging `min_k` with `sum_r` would generally be invalid and is not done. Since `g(d,e)` divides A0, it has no prime factor above 2d.

P2 is a finite exact formula for every degree. It is not yet an evaluated asymptotic formula for the sum of contents over the N-dependent Jacobi block.

## 3. A real integral-row improvement

For the principal mixed object retain

\[
e=6N,\quad8N+1\le d\le44N-1,
\quad s_d=\max(14N+d-(d\bmod2),36N-4).
\]

Replace the red Jacobi pair of the [finite-place note](catalan_mixed_jacobi_moment_finite_places_20261007.md) by the section constructed from

\[
P_d^{\rm prim}=d_\mu2^{s_d}t^{19N}(1-t)^{2N}
\frac{4^dJ_d}{g(d,6N)}.
\tag{P3}
\]

The quotient polynomial is integral. The factor `d_mu*2^s_d` still clears the finite C/H kernels; both triangular and endpoint sections therefore give integral D. The same degree/support bounds and filtered contact hold. Linearity gives the exact pair and actual moment-row identity

\[
(P_d^{\rm red},D_d^{\rm red})
=g(d,6N)(P_d^{\rm prim},D_d^{\rm prim}).
\]

Pure-D rows are unchanged. The all-prime entry cap and joint-column denominator argument use only those retained supports, clearing factors and integer row coefficients. They apply afresh to this new primitive-Jacobi construction. Hence its safe asymptotic lower exponent is still `-7849/3872` along nonzero conditional determinants, while its actual real determinant is divided by

\[
\mathcal G_N=\prod_{d=8N+1}^{44N-1}g(d,6N).
\]

This is a possible genuine improvement of the lattice estimate: merely transporting the old lower bound under a scalar division would not establish it. The fresh safe bound for the new integer rows is the necessary input. P3 concerns primitive Jacobi polynomials; it does not assert a primitive basis of the entire paired contact lattice.

## 4. A rigorous upper ceiling for this improvement

The endpoint coefficient A0 forces

\[
g(d,e)\mid\binom{2d}{d},\qquad
\log g(d,e)\le2d\log2.
\]

Therefore, for every N,

\[
\boxed{0\le\log\mathcal G_N
\le(1872N^2-52N)\log2.}
\tag{P4}
\]

On the `n^2` scale its possible leading gain is at most `(117/121)log2`. The actual positive leading gain has not been established by this upper bound.

For comparison the [real-place interface](catalan_mixed_jacobi_real_place_interface_20261007.md), equations R23--R26, gives the trace-bound requirement

\[
G_*+18t_*<-7849/2,
\qquad t_*:=\limsup N^{-1}\log\mathfrak T_N(\mu).
\]

Even using the largest possible content allowed by P4, the requirement becomes

\[
t_*<\frac{-7849/2-G_*+1872\log2}{18},
\]

approximately `-179.21`, instead of approximately `-251.30`. Those decimals only illustrate the exact expressions. Thus the content ceiling by itself cannot make the current trace comparison succeed with subexponential residual trace. It is not a no-go theorem for the exact exterior determinant: its joint singular values may give a stronger bound than trace AM--GM.

The strategic consequence is concrete. An exact all-N content formula is worth retaining, but a large content scan alone cannot close the current gap. The next main proof must control the actual residual exterior determinant, including the zero-junction polynomial and D_mu, or change the support/kernel so that both sides have a demonstrably better comparison.

## 5. Exact residue minimum at large odd primes

For the principal block fix N>=1, e=6N, 8N+1<=d<=44N-1, and an odd prime p>2 sqrt(65N). Every factorial argument in P1 is at most 2d+e-1<94N<p^2. Thus only the first floor layer of P2 is present. Put

\[
\eta_p=(p+1)/2,\qquad
i=d\bmod p,\qquad t=(d+e-1)\bmod p,
\qquad j=k\bmod p.
\]

Writing d=ap+i, k=bp+j and d+e-1=cp+t gives

\[
\begin{aligned}
\left\lfloor\frac{2d}{p}\right\rfloor
 -2\left\lfloor\frac d p\right\rfloor
 &=\mathbf 1_{i\ge\eta_p},\\
\left\lfloor\frac d p\right\rfloor
 -\left\lfloor\frac{d-k}{p}\right\rfloor
 &=b+\mathbf 1_{j>i},\\
\left\lfloor\frac{d+e+k-1}{p}\right\rfloor
 -\left\lfloor\frac{d+e-1}{p}\right\rfloor
 &=b+\mathbf 1_{j\ge p-t},\\
\left\lfloor\frac{2k}{p}\right\rfloor
 &=2b+\mathbf 1_{j\ge\eta_p}.
\end{aligned}
\]

Consequently the valuation of the actual integer Newton coefficient is exactly

\[
v_p(A_k)=\mathbf 1_{i\ge\eta_p}
 +\mathbf 1_{j>i}+\mathbf 1_{j\ge p-t}
 -\mathbf 1_{j\ge\eta_p}.
\tag{P5}
\]

This holds for every allowed k, including k with several complete p-blocks; the b terms cancel. If i<eta_p, k=0 has valuation zero, so the content valuation is zero. If i>=eta_p and t<eta_p-1, choose k=eta_p. This is allowed since d>=i>=eta_p, and its residue j=eta_p is <=i and <p-t. P5 again gives zero. Finally suppose i>=eta_p and t>=eta_p-1. For j<eta_p, P5 is at least one. For j>=eta_p, the inequality p-t<=eta_p implies its third indicator is one, so P5 is again at least one. The coefficient k=0 has valuation one. This proves the exact closed formula

\[
\boxed{v_p(g(d,6N))=
 \mathbf 1_{d\bmod p\ge(p+1)/2}\,
 \mathbf 1_{(d+6N-1)\bmod p\ge(p-1)/2}.}
\tag{P6}
\]

No extra prime-power floor was discarded: the imposed p bound excludes it for every factorial in P1. P6 does not apply to the remaining small primes, whose complete answer remains P2. It also does not by itself evaluate the leading sum over all primes and degrees. At N=p it recovers the high-half row content in the separate prime-content lemma, since (d+6p-1) mod p equals (i-1) mod p.

## 6. A proved positive leading contribution beyond the kernel range

Consider only primes 65N<p<88N which are prime to the fixed parameter-clearing integers d_mu and d_gamma. Omitting this fixed exceptional set has no leading effect; for all sufficiently large N none lies in the interval. Such p satisfy the hypothesis of Section 5, and

\[
d<p,\qquad d+6N-1<p.
\]

The two residues in P6 are therefore d and d+6N-1. Its second inequality follows from its first. Hence

\[
v_p(g(d,6N))=\mathbf 1_{d\ge(p+1)/2}.
\]

The number of affected Jacobi rows in the selected square is exactly

\[
T_p=44N-(p+1)/2\ge0,
\qquad
\mathcal Q_N=
 \prod_{\substack{65N<p<88N\\p\nmid d_\mu d_\gamma}}p^{T_p}.
\tag{P7}
\]

Here T_p can be zero at the upper end of the interval. The lower degree endpoint 8N+1 never truncates these rows, since (p+1)/2>32N. From the exact integral pair identity in Section 3, the corresponding red row is divisible by p as a polynomial pair. All conditional rational moment kernels are p-integral for p>H=65N: the all-prime entry cap in the finite-place note has zero exponent there at good primes. This also applies afresh to the primitive pair. Thus the actual conditional red moment determinant has v_p at least T_p, not merely a smaller negative denominator cap.

Let \(\mathcal D_N\) be the complete denominator certificate for the red determinant in J27--J30 of the finite-place note. Its good prime factors lie at p<=H; its other factors are fixed parameter primes. Therefore it is coprime to \(\mathcal Q_N\), and the exact finite implication for every nonzero conditional determinant is

\[
\mathcal D_N\Delta_{\rm red}\in\mathcal Q_N\mathbb Z,
\qquad
|\Delta_{\rm red}|\ge\mathcal Q_N/\mathcal D_N.
\tag{P8}
\]

For example, P8 also follows from the fresh primitive-row certificate
\(\mathcal D_N\Delta_{\rm prim}\in\mathbb Z\)
and the exact scalar identity
\(\Delta_{\rm red}=\mathcal G_N\Delta_{\rm prim}\),
because \(\mathcal Q_N\mid\mathcal G_N\). This distinction matters: the primitive determinant retains the freshly proved safe denominator bound, whereas the original red determinant acquires a genuine positive numerator valuation. Simply subtracting \(\log\mathcal G_N\) from the old red lower bound would give no such improvement. All these statements are conditional on the proposed rational relation and on the determinant being nonzero; none proves nonvanishing.

By the prime number theorem, partial summation on the fixed interval [65,88] gives

\[
\begin{aligned}
\log\mathcal Q_N
 &=\sum_{65N<p<88N}
   \left(44N-\frac{p+1}{2}\right)\log p+o(N^2)\\
 &=N^2\int_{65}^{88}(44-x/2)\,dx+o(N^2)
 =\frac{529}{4}N^2+o(N^2).
\end{aligned}
\tag{P9}
\]

The fixed exceptional primes contribute zero for sufficiently large N, and the constant -1/2 in T_p contributes only O(N). The endpoint floor error is consequently paid explicitly. Together with \(\log\mathcal D_N\le(7849/2+o(1))N^2\), P8 proves for the original red object, along any nonzero conditional determinants,

\[
\boxed{\liminf\frac{\log|\Delta_{\rm red}|}{N^2}
 \ge-\frac{7849}{2}+\frac{529}{4}
 =-\frac{15169}{4}.}
\tag{P10}
\]

Equivalently its n^2-scale lower bound is -15169/7744, since n=44N-1. This is a proved contribution from this one prime interval. It is not the full asymptotic sum of all Jacobi contents, nor an optimal denominator estimate.

Use the same red real-place object and its unchanged upper exponent \(G_*+18t_*\). The newly sufficient strict comparison is

\[
\boxed{t_*<t_{\rm crit}^{\rm interval}:=
 \frac{-7849/2+529/4-G_*}{18}
 =\frac{-15169/4-G_*}{18},}
\tag{P11}
\]

approximately -243.94986. If instead one uses primitive rows at the real place, the exact scalar \(\mathcal G_N\) must be divided out of that actual determinant as well; its lower bound must be the freshly reapplied primitive certificate. These are equivalent comparisons when the same scalar is accounted for on both sides. P11 requires neither an unevaluated full-content asymptotic nor a one-sided normalization saving. The required residual-trace estimate and actual-point nonvanishing remain unproved.
