# Actual mixed moments: a positive tail block and an exact Schur criterion

Date: 2026-10-07. New symbolic note. The preceding contact construction is used as a polynomial-pair construction; its independence is not assumed to imply independence of actual moment rows.

## 1. Actual reading and fixed spaces

For this continuation the author actually reread the complete final ten-section note

`E:\kimi-build\zeta5\research\catalan_mixed_two_end_contact_support_lemma_20261007.md`

in full, and the original current `foundations.tex` lines 54–211, including the bilinear integrals, filter, rational recurrences, and exact period decomposition. These are the only mathematical sources used in this note. No historical script, numerical guard, or determinant producer was run. All positivity and elimination arguments below are derived directly.

The fixed reduced parameters are

\[
b=7N,\quad q=4N,\quad h=2N,\quad A=19N,\quad H=65N,
\quad n=44N-1,\quad L=b+n+q=55N-1.
\]

Put

\[
k_0=8N+1,\quad p=36N-1,\quad d=8N+1,\quad m=n-d=36N-2=p-1.
\]

The permitted nonzero-`P` space consists of

\[
P_Q(t)=t^A(1-t)^hQ(t),\qquad \deg Q<44N,
\quad \int x^jQ(x)\,d\nu_{h+q}(x)=0\ (0\le j<k_0),
\]

where `d nu_e=(1-x)^e dx/(pi sqrt(1-x^2))`. Its dimension is `p`. A fixed basis independent of the mixed parameter is

\[
Q_a(t)=8^{\ell_a}P_{\ell_a}^{(6N-1/2,-1/2)}(t),
\qquad \ell_a=8N+1+a,\quad 0\le a<p.
\]

The pure-`D` tail is

\[
\mathcal D_{\rm tail}=t^L(1-t)^h\mathbb Q[t]_{<d},\qquad
T_e(t)=t^{L+e}(1-t)^h,\quad 0\le e<d.
\]

For a fixed nonzero rational `mu=16 beta/alpha`, the entire contact pool has dimension `p+d=44N=n+1`. It therefore **cannot be injective** into `n` filtered columns. The desired property is full output rank `n`, equivalently a one-dimensional actual kernel and at least one nonzero `n`-row minor.

## 2. Explicit sections and a rational affine matrix

For the fixed basis above, let

\[
\widehat H_k(P)=\sum_{v=0}^q(-1)^v\binom qvH_{b+k+v}(P),\qquad
\widehat C_k(P)=\sum_{v=0}^q(-1)^v\binom qvC_{b+k+v}(P).
\]

Both vectors have zero first `d=k_0` coordinates. The triangular prescription and zero-end endpoint section in the preceding note give fixed rational linear maps

\[
D_H(P),\qquad D_C(P),
\]

with the permitted `D` support and factor, such that

\[
\widehat{D_H(P)}=\widehat H(P),\qquad
\widehat{D_C(P)}=\widehat C(P).
\]

Here the hat on a polynomial denotes the same finite coefficient filter. Explicitly, solve successively for coefficients `A+1<=j<L` using the unit triangular filter, then apply

\[
t^{A+1}(1-t)^h\operatorname{trunc}_{<L-A-1}
\left(t^{-(A+1)}D_{<L}(t)/(1-t)^h\right).
\]

The mixed section is exactly

\[
D_\mu(P)=D_H(P)-\mu D_C(P).
\]

Every contact pair is uniquely a pair from this section plus a tail pair `(0,E)`, `E in D_tail`.

Write the filtered column polynomial as

\[
V_k(s)=s^{b+k}(1-s)^q,\qquad 0\le k<n.
\]

Define rational matrices with `p` rows and `n` columns by

\[
\begin{aligned}
R_{a,k}&=M^0(P_{Q_a},V_k)-\tfrac32 Z^0(D_H(P_{Q_a}),V_k),\\
U_{a,k}&=\tfrac32 Z^0(D_C(P_{Q_a}),V_k),\\
C_{a,k}&=\widehat C_k(P_{Q_a}).
\end{aligned}
\]

The bilinear `M^0,Z^0` here are precisely the original finite rational arrays of source lines 168–204, applied coefficientwise. Define the tail matrix

\[
T_{e,k}=-\tfrac32 Z^0(T_e,V_k).
\]

All expanded tail indices satisfy `i>=L` and `j<L`. Hence there is no diagonal zeta term, and

\[
Z^0(T_e,V_k)=Z(T_e,V_k).
\]

The actual filtered moment matrix, in the whole `n+1`-row pool, is

\[
\mathsf F_\mu=
\begin{pmatrix}
R+\mu U+(4G+\mu\pi^2/4)C\\
T
\end{pmatrix}.
\]

The factor `1/4` is required: `mu=16 beta/alpha`. Under the hypothetical relation `alpha G+beta pi^2=u`, put `r=4u/alpha`. The exact rational specialization is then

\[
\boxed{\mathsf F(\mu,r)=
\begin{pmatrix}R+\mu U+rC\\T\end{pmatrix},
\qquad r=4u/\alpha.}
\]

This is the requested concrete representation `F_0 + mu Q_1 + (4u/alpha) C`. The basis was fixed independently of `mu`; later clearing of denominators for a fixed rational `mu` only rescales rows and does not change rank.

## 3. Strict positivity for the Z moment matrix

For positive integer exponents or exponent 0, and positive weights on `(0,1)`, consider

\[
Z_{i,j}^{w_1,w_2}
=\int_0^1\!\int_0^1
 \frac{t^i s^j w_1(t)w_2(s)}{1-ts}\,ds\,dt.
\]

Every finite minor with strictly increasing selected exponents is positive, when the integrals converge. The proof is elementary:

1. For `0<t_1<...<t_r<1` and `0<s_1<...<s_r<1`, the Cauchy determinant is

\[
\det\left(\frac1{1-t_i s_j}\right)_{i,j=1}^r
=\frac{\prod_{i<j}(t_j-t_i)(s_j-s_i)}
 {\prod_{i,j}(1-t_i s_j)}>0.
\]

2. The generalized Vandermonde determinant of increasing nonnegative exponents at increasing positive arguments is positive. One elementary proof is that a nontrivial combination of `r` such monomials has at most `r-1` positive zeros, by division by the least power and induction with Rolle's theorem. The determinant is therefore nonzero; its sign near coincident ordered arguments is the sign of its Wronskian, which is the positive product of exponent differences.

3. Apply the continuous Cauchy–Binet identity twice. On the two ordered simplices the determinant of the moment minor is the integral of the two generalized Vandermonde factors, the positive Cauchy determinant, and positive weights. It is strictly positive on an open set. Absolute convergence follows from the original source integrability argument, or first truncate to compact interior intervals and pass to the limit.

Thus the `Z` matrix is strictly totally positive. This assertion concerns `Z`; the factor `-3/2` in the actual tail moment rows changes determinant signs but not their nonvanishing.

For the tail take weights

\[
w_1(t)=t^L(1-t)^h,\qquad w_2(s)=s^b(1-s)^q.
\]

It follows in particular that its first `d` filtered columns form an invertible tail block. Also, on the **entire** permitted `D` space

\[
\mathcal D=t^{A+1}(1-t)^h\mathbb Q[t]_{<n},\qquad
\dim\mathcal D=n,
\]

the matrix

\[
\bigl(Z(t^{A+1+e}(1-t)^h,V_k)\bigr)_{0\le e,k<n}
\]

has positive determinant. Consequently the whole `D -> Z` moment map is an isomorphism over `R`, and its restriction to the tail is injective. No actual moment-kernel vector can be a nonzero pure-`D` pair.

## 4. Exact Schur complement and the genuine kernel

Partition the columns into

\[
J_0=\{0,\ldots,d-1\},\qquad J_1=\{d,\ldots,n-1\}.
\]

Write

\[
T=(T_0\ T_1),\qquad
R+\mu U+rC=(A(\mu,r)\ B(\mu,r)).
\]

Section 3 proves `det T_0 != 0`. The rational matrix

\[
W=T_0^{-1}T_1
\]

is independent of `mu,r`. Column elimination gives the exact Schur matrix

\[
\boxed{S(\mu,r)=B(\mu,r)-A(\mu,r)W,\qquad
S\text{ has size }p\times m.}
\]

Since the first `d` coefficients of `C` are zero,

\[
\boxed{S(\mu,r)=S_0+\mu S_1+rC_1,}
\]

where

\[
S_0=R_{J_1}-R_{J_0}W,\qquad
S_1=U_{J_1}-U_{J_0}W,\qquad C_1=C_{J_1}.
\]

All three coefficient matrices are rational and independent of the target relation. The period coefficient `C_1` is unchanged by tail elimination.

The exact rank identity is

\[
\boxed{\operatorname{rank}\mathsf F(\mu,r)
=d+\operatorname{rank}S(\mu,r).}
\]

More explicitly, write a pool vector as nonzero-`P` coefficients `x in R^p` and tail coefficients `y in R^d`, using row-vector coordinates. It is in the actual moment kernel precisely when

\[
\boxed{xS(\mu,r)=0,\qquad
y=-xA(\mu,r)T_0^{-1}.}
\]

This is the genuine kernel as a graph, not a count of independent polynomial pairs. Its dimension is `p-rank S`. In particular it is one-dimensional exactly when `rank S=m=p-1`.

If `I` is any subset of `m` nonzero-`P` basis rows, the square minor using all `d` tail rows followed by `I`, and all columns, equals

\[
\det T_0\,\det S_I(\mu,r).
\]

Therefore at least one `n`-row minor is nonzero if and only if one of the `m`-row minors of `S` is nonzero. This pays the tail elimination in full, but does not automatically prove the remaining minors are nonzero.

## 5. Why the earlier fixed square is a separate condition

The earlier ten-section construction selected all `p` Jacobi directions and only `d-1=8N` tail directions. The full pool has one additional tail row.

If the full pool has rank `n`, its maximal minors give, up to a common nonzero factor and the usual alternating signs, the coordinates of its one-dimensional left kernel. Thus deleting a particular tail row gives a nonzero fixed square precisely when the corresponding coordinate of `y=-xAT_0^{-1}` is nonzero.

Full pool rank alone guarantees a square minor using **all** tail rows and omitting an appropriate nonzero-`P` row; it does not guarantee that the earlier specific square, which omitted one tail row, is nonzero. This distinction must be retained in any later determinant estimate.

## 6. A second exact description using the complete D isomorphism

Let `P` range over the full permitted `P` space of dimension `44N`, before low infinity-contact constraints. In fixed coefficient bases, let `M_P` be its actual filtered `M` matrix and let `Z_D` be the square filtered `Z` matrix on the full permitted `D` space of section 3. For an actual moment-zero pair,

\[
xM_P-\tfrac32 yZ_D=0,
\qquad
\boxed{y=\tfrac23 xM_PZ_D^{-1}.}
\]

Intersect this graph with the filtered mixed contact equations. The first `d` contact equations impose the positive low moment constraints on `P`, and the remaining equations are precisely the Schur kernel condition of section 4 in different coordinates.

The invertibility of `Z_D` proves uniqueness of the `D` partner of a moment-zero `P`. It does not prove that the intersection with mixed contact has only one dimension. This is another way to locate the remaining proof obligation without confusing polynomial-pair independence with moment independence.

## 7. The residual C map is exactly a second-kind Taylor-jet matrix

Put `e=h+q=6N`, `R_Q(z)=(1-z)^e Q(z)`, and take the branch `sqrt(z^2-1)~z` at infinity. Define

\[
W_Q(z)=\int_{-1}^1\frac{R_Q(x)}{z-x}\,d\nu_0(x),\qquad
B_Q(z)=\int_{-1}^1\frac{R_Q(z)-R_Q(x)}{z-x}\,d\nu_0(x).
\]

The second expression is a polynomial with rational coefficients. The arcsine Cauchy transform is `sum_(l>=0) c_l z^(-2l-1)=1/sqrt(z^2-1)`, by the same binomial generating series already used for the kernels. Direct polynomial division therefore gives

\[
\boxed{\frac{R_Q(z)}{\sqrt{z^2-1}}=B_Q(z)+W_Q(z).}
\]

Equivalently, `B_Q` is the polynomial part at infinity of the left side. All permitted `Q` have zero `nu_e` moments through degree `8N`, so

\[
W_Q(z)=O(z^{-8N-2}).
\]

In filtering the infinity coefficients of `P_Q`, one may move `(1-z)^q` inside the polynomial-part operation at all indices `j'>=b+q`: the discrepancy from negative Laurent powers has degree at most `q-1`, which is below that range. Since `q` is even, the filtered coefficient at column `k` is therefore read at

\[
j'=b+q+k=11N+k
\]

from `z^(A+1)(B_Q+W_Q)`. The highest power in `z^(A+1)W_Q` is at most `11N-1`, so it never reaches a filtered index. Consequently

\[
\boxed{\widehat C_k(P_Q)=[z^{k-8N-1}]B_Q(z),}
\]

with negative coefficient indices interpreted as zero. This proves again that the first `d=8N+1` entries vanish. The residual matrix is exactly

\[
(C_1)_{a,r}=[z^r]B_{Q_a}(z),\qquad
0\le a<36N-1,\quad0\le r<36N-2.
\]

For explicit finite computation, if `R_Q(z)=sum_i rho_i z^i`, then

\[
[z^r]B_Q(z)=\sum_{i\ge r+1}\rho_i c_{(i-r-1)/2}.
\]

Thus the remaining `C` rank is a concrete rational Taylor-jet problem for `36N-1` high Jacobi second-kind polynomials. The preceding positive Gram proof concerns ordinary moments of `Q`, not these Taylor jets, and does not prove their rank `36N-2`.

## 8. Exact nonvanishing criterion and what a generic statement would require

Define the rational determinantal locus

\[
\mathcal E_N=\{(\mu,r):\det S_I(\mu,r)=0
\text{ for every }m\text{-row subset }I\}.
\]

The rank theorem above proves, without exceptions in `N`,

\[
\boxed{\mathsf F(\mu,r)\text{ has a nonzero }n\text{-row minor}
\iff (\mu,r)\notin\mathcal E_N.}
\]

Every displayed minor is a polynomial of degree at most `m` in each affine parameter. If one separately proves `rank C_1=m`, then for every fixed `mu` a chosen nonzero `C_1` minor is the leading coefficient of the corresponding Schur determinant in `r`. For that fixed `mu` there would then be at most `m` exceptional `r` for that chosen minor. An analogous statement holds in `mu` if `rank S_1=m` is proved.

The separate subsequent note `research/catalan_mixed_second_kind_jet_rank_20261007.md` now proves `rank C_1=m` for all `N` by a finite Toeplitz/first-order ODE argument. Hence the generic statement in `r` is now paid for every fixed `mu`. No all-`N` rank assertion for `S_1` alone is made. A generic statement with finitely many exceptional parameters still does not exclude a given rational target value `r=4u/alpha` from the exceptional set. Irrationality of `pi^2` does not exclude such rational exceptional values under the hypothetical mixed relation.

The actual, unconditional real moment pencil is obtained by substituting

\[
r=4G+\mu\pi^2/4,
\qquad
S_{\rm actual}(\mu)=S_0+4G C_1
 +\mu(S_1+\pi^2 C_1/4).
\]

Treating `mu` and `r` as formally independent is a tool for exact algebraic study, not a proof that the actual line or a hypothesized rational point avoids the determinantal locus.

## 9. Proven result and precise remaining gap

The following are genuine all-`N` results from the current moments: strict total positivity of the `Z` matrix, injectivity of every pure-`D` tail, invertibility of the entire permitted `D` moment map, an exact rational tail Schur complement, the actual kernel graph, a maximal-minor identity, the affine representation `R+mu U+rC`, and the second-kind Taylor-jet representation of its residual period coefficient. The separate subsequent jet-rank note proves that residual coefficient has rank `m` for all `N`, and therefore gives a nonzero polynomial maximal minor in `r` for every fixed `mu`. Its sections 7–8 also pay the maximal actual slope in `mu` and give a concrete observing-determinant criterion for excluding every target value at a fixed `mu`.

The unresolved step is full column rank of `S(mu,4u/alpha)` for the arbitrary fixed nonzero rational `mu` and rational target value in the question, or a separate argument showing that at least one required minor is nonzero at that point. The positive tail and the contact-space dimension do not imply it. No all-`N` nonvanishing theorem for the full mixed matrix, or for the earlier particular square, is asserted here.

This note supplies an exact, finite symbolic operator and its rank criterion to the next step. A newly authorized finite check at one `N` can certify only the corresponding finite parameter statement; it cannot establish the missing all-`N` rank theorem or remove all rational exceptional values.
