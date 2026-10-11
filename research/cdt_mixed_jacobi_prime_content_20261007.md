# Exact Jacobi content at the scale prime, and a finite actual moment pencil

Date: 2026-10-07. This note contains a new all-prime paper lemma and one bounded, new finite certificate. It establishes no new irrationality or linear independence statement. All references to a rational period relation below are conditional; no numerical relation is assumed or approximated.

## 1. The precise objects

For the mixed-space dimension statements take `alpha!=0,beta!=0`, hence `mu!=0`. Use the reduced construction in section 10 of [the contact note](catalan_mixed_two_end_contact_support_lemma_20261007.md):

\[
A=19N,\quad h=2N,\quad b=7N,\quad q=4N,\quad H=65N,
\quad n=44N-1,\quad L=55N-1,\quad e=h+q=6N.
\]

The nonzero-P directions are

\[
\mathsf J_d^{(e)}(t)=P_d^{(e-1/2,-1/2)}(t),\qquad
8N+1\le d\le44N-1.
\]

Put `kappa=d_mu*2^(58N-2)`, with a fixed positive integer `d_mu` clearing the denominator of `mu`. Both the older normalization `kappa*8^d*J_d` and the smaller `kappa*4^d*J_d` are considered. The pair has

\[
P=\kappa t^A(1-t)^h\rho_d\mathsf J_d^{(e)},
\qquad \rho_d\in\{4^d,8^d\}.
\]

Construct D by the linear triangular low-coefficient section for the filtered equations `H-D=mu*C`, followed by the linear completion

\[
D=t^{A+1}(1-t)^h
\operatorname{trunc}_{<L-A-1}
\left(\frac{t^{-(A+1)}D_{<L}}{(1-t)^h}\right).
\]

Adjoin either all `8N+1` pure-D tails `t^(L+r)(1-t)^h`, or the first `8N` for the designated square. Define `gamma=4u/alpha`, `mu=16beta/alpha`. Under `alpha G+beta pi^2=u`, the filtered rational moment matrix is exactly

\[
E(\mu,\gamma)=E_0+\mu E_1+\gamma C_{\rm filt}.
\]

Here the section is linear in `mu`, `E0=M0(P)-3Z0(D0)/2`, and `E1=-3Z0(D1)/2`. The formal rational pencil is meaningful without any period relation.

## 2. A smaller dyadic normalization

The finite Jacobi formula used in the contact note implies

\[
\mathsf J_d^{(e)}(x)
=[z^d]\left(1+\frac{x+1}{2}z\right)^{d+e-1/2}
\left(1+\frac{x-1}{2}z\right)^{d-1/2}.
\]

Substituting `z -> 4z`, and setting `U=xz+(x^2-1)z^2`, gives

\[
4^d\mathsf J_d^{(e)}(x)
=[z^d](1+4U)^d(1+4U)^{-1/2}
(1+2(x+1)z)^e.
\]

Since

\[
(1+4U)^{-1/2}
=\sum_{k\ge0}(-1)^k\binom{2k}{k}U^k,
\]

the right side belongs to `Z[x]` for all integers `d,e>=0`. This proves `4^d J_d in Z[x]`. With the same kappa, C and H are cleared on the same finite contact interval. Both linear D sections remain integral. Thus each old pair is `2^d` times an integral pair with the smaller normalization, and its actual moment row has the same factor.

For the stated square, the sum of the Jacobi degrees is

\[
\sum_{d=8N+1}^{44N-1}d=936N^2-26N.
\]

Dividing those rows by `2^d` changes the determinant by the exact scalar `2^-(936N^2-26N)`. This is an actual integer-row rescaling, not a claim that coefficient height is the denominator of a moment. It does not prove a primitive full lattice.

## 3. Exact content at N=p

**Lemma.** Let p be an odd prime with `p>88`, set `N=p,e=6p`, and take `d=rp+i`, `0<=i<p`, in the Jacobi degree range. The minimum p-adic valuation among coefficients of either `4^d J_d` or `8^d J_d` is

\[
\epsilon_i=\begin{cases}
0,&0\le i\le(p-1)/2,\\
1,&(p+1)/2\le i<p.
\end{cases}
\]

If `p` does not divide the fixed integer `d_mu`, then the minimum valuation among all coefficients of the corresponding integral pair `(P,D)` is also exactly `epsilon_i`.

**Proof of the lower bound.** In the finite Jacobi formula the upper binomial parameters are `d+6p-1/2` and `d-1/2`. When `i> (p-1)/2`, their residues in `Z_p/pZ_p` are both

\[
s=i-(p+1)/2.
\]

For `a in Z_p`, a necessary condition for `binom(a,v)` to be nonzero modulo p is that the least digit `v0` satisfies `v0<=a0`. This is the lowest-digit Lucas rule. It applies to these half-integer parameters because their binomial coefficients are p-integral. For completeness it can be obtained by approximating a by nonnegative integers modulo sufficiently high powers of p and then applying ordinary Lucas; the finite binomial polynomial is continuous after accounting for the denominator `v!`.

If the two binomial factors in a term of the Jacobi formula were both nonzero modulo p, the least digits of v and d-v would both be at most s. Those two digits add to either i or i+p. But

\[
2s=2i-p-1<i,
\]

which is impossible. Thus every term, and every polynomial coefficient, is divisible by p. Powers of 2 are units here.

**Proof of exactness.** Evaluation at x=-1 retains only one term:

\[
\mathsf J_d^{(e)}(-1)
=(-1)^d\binom{d-1/2}{d}
=(-1)^d\frac{\binom{2d}{d}}{4^d}.
\]

Here `2d<88p<p^2`. Legendre's formula therefore gives

\[
v_p\binom{2d}{d}
=\left\lfloor\frac{2d}{p}\right\rfloor
-2\left\lfloor\frac d p\right\rfloor
=\left\lfloor\frac{2i}{p}\right\rfloor
=\epsilon_i.
\]

The endpoint evaluation bounds coefficient content from above by epsilon_i. Combined with the lower bound, and with nonnegativity of valuations, it proves the first assertion.

Multiplication by `t^A(1-t)^h` preserves the minimum valuation: after removing the known power of p, its reduction and the reduction of the remaining Jacobi polynomial are nonzero polynomials over a field. Kappa is a p-unit. The finite C and H coefficients are dyadic and hence p-integral; `mu` is p-integral. The triangular recursion and endpoint section use integer coefficients. Consequently D inherits every p-factor of P. Since P already has exact content, the pair has that same exact content. This proves the lemma.

## 4. The consequence for a Frobenius determinant proof

There are exactly

\[
t_p=18(p-1)
\]

upper-half Jacobi directions in `d=8p+1,...,44p-1`: the interval is 36 complete residue blocks with only the lower-half index `d=8p` removed. Each of these pair rows can be divided by p while remaining an integral polynomial pair.

For the actual rational moment pencil, exclude also the fixed denominator primes of gamma. The safe moment cap `2*d_gamma*lcm(1,...,65p)^2` clears entries. As `p>88`, the lcm has p-valuation 1. Thus `p^2 E_entry` is p-integral. On every upper-half row it is zero modulo p, because the entire polynomial pair has the factor p.

The unrescaled `p^2 E` matrix is therefore singular modulo p. A proof of its nonsingularity obtained by simply importing the original Catalan Chebyshev blocks cannot be correct for this new row normalization. This does not imply that the rational determinant is zero.

Writing the determinant after these row divisions as `Delta_red`, exact row multilinearity gives

\[
\Delta=p^{18(p-1)}\Delta_{\rm red},
\qquad
v_p(\Delta)\ge18(p-1)-2(44p-1)=-70p-16,
\]

with the usual interpretation `v_p(0)=+infinity`. Equality would need a new nonsingularity certificate for the divided rows. It is not established here. For the smaller 4^d normalization the same statement holds; its dyadic factors are p-units.

This single scale-prime contribution is `O(N log N)` along `N=p`, and is `o(N^2)`. It neither supplies a leading all-prime improvement nor a bound for a full primitive lattice index.

## 5. A candidate with complete residue blocks

An optional self-consistent variant has `n=43N,L=54N`. For `mu!=0` its aligned pair space has dimension `45N-1`. One can select

\[
d=9N,\ldots,44N-1\quad(35N\text{ Jacobi directions}),
\]

and the first `8N` of the available `9N` pure-D tails. They give exactly `43N` independent polynomial pairs. At `N=p` both row groups have complete p-blocks. The exact scale-prime content count becomes `35(p-1)/2`. This could simplify a new Frobenius bridge, but no such bridge or actual determinant nonvanishing follows just from the block counts. All leading estimates in the other current notes retain the principal `44N-1` object unless explicitly stated otherwise.

## 6. New finite certificate: N=1 actual pencil

The new producer [source](cdt_mixed_actual_moment_pencil_N1_20261007.py) was run once and writes the complete [modular matrix and pivot data](cdt_mixed_actual_moment_pencil_N1_20261007.json). It uses one fixed modulus 101, one scale N=1, the smaller `kappa*4^d` normalization, `kappa=2^56`, and the exact same triangular/zero-end D sections. The 44-row pool has Jacobi degrees 9 through 43 and nine pure-D tails; there are 43 filtered columns. The designated square discards the last tail.

All scalar denominators in the source rational arrays and the Jacobi construction are units modulo 101. The moment indices are `0<=i<=64`, `0<=j<=53`; rational recipes only divide by integers of absolute value at most 65, or powers of 2. Thus the computed residues are reductions of actual rational matrices, without numerical integration.

The component ranks over `F_101` are

\[
\operatorname{rank}E_0=43,\quad
\operatorname{rank}E_1=34,\quad
\operatorname{rank}C_{\rm filt}=34.
\]

The 35 by 34 residual C matrix has rank 34. The pure-D first-nine-column square has determinant 50. Its Gaussian pivots are `89,91,32,19,86,96,33,16,51`, with one row swap.

For the nine finite parameter substitutions, the designated 43-square determinants are:

| mu | gamma=0 | gamma=1 | gamma=-1 |
|---|---:|---:|---:|
| 1 | 77 | 63 | 51 |
| 2 | 58 | 58 | 4 |
| -1 | 87 | 74 | 54 |

The full 44 by 43 pool has rank 43 at every displayed substitution. In particular its designated determinant is a nonzero polynomial over Q in `(mu,gamma)`. This is a finite generic-rank statement. It does not prove nonvanishing at every rational parameter pair, at the parameters of a hypothetical period relation, at all scales, or along the scale-prime sequence. The finite residual C rank likewise does not prove its all-N counterpart.

## 7. Primary source scope and outstanding payment

For the original comparison, the root actually read all 413 lines of

`E:\codex-build\math\preprints\Catalans-constant-is-irrational-September-24-2026\build\sections\nonvanishing.tex`.

Its original Chebyshev proof passes through a palindromic basis and successor-row identities, then proves nonsingularity from three fixed 48-square rational matrices. The fixed modulus 101 there certifies only those finite original matrices. The present producer constructs different actual Jacobi pairs and a different matrix; it neither reruns that certificate nor transfers its valuation theorem.

The new tasks remain: derive a bridge for correctly divided Jacobi rows, or an all-N actual Schur-complement nonvanishing proof; pay the same-object prime and real-place estimates; and obtain a strict final comparison. The endpoint content lemma prevents a false shortcut and supplies a precise normalization for that next bridge.
