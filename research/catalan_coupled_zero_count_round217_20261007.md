# Coupled zero count, round 217: pole removal, locked jets, and a two-cut regularization gate

2026-10-07. NEW symbolic note. No mathematical program, producer, grid,
prime scan, or PSLQ was run. No old mathematical note, main manuscript,
or existing manifest was edited. This does not prove full moment rank.

## 1. Actual object and the weaker zero-count target

The input is the round-216 actual-nonzero interface A1--A23, whose final
16005-byte author reread has SHA256
`6646d25d91e54347bb73ea29486bec0cf1b4cf7d061baaae3e216180ab84d900`.
The b=0 precheck was additionally read in the complete updated section 5
of `research_global_review_round216_20261007.md`, 8957 bytes, SHA256
`60119f1598fa41ff07a23223a181735d34c23f9611e796df9ae885b2f9431450`.
That section reading was bounded, not a fresh whole-file read.

It is useful to state the q=0 bookkeeping for general integer b>=0:

\[
L=b+n,\quad K=A-b\ge0,\quad m=L-A-1=n-K-1\ge1,
\quad\delta=K+1=n-m,\quad M=n+1.                       \tag{Z1}
\]

In the current carrier A=19N,b=11N,h=2N,n=44N-1; therefore K=8N,
m=36N-2,delta=8N+1. The b=0 candidate with the same A,h,n instead has
K=19N,m=25N-2,delta=19N+1. The formulas below use an integer h>=1.
No arithmetic cost or output Gram is transferred to that candidate.

Fix real mu and use the actual integral parameter
gamma_*(mu)=4G+mu*pi^2/4. Under the proposed rational relation this is
the rational gamma of the conditional pencil. Away from this equality
the polynomial correction of A17 must still be included; it is not part
of the degree bound for Pi below.

Let dnu_h=(1-x)^h dnu_0, dnu_0=dx/[pi sqrt(x(1-x))]. For a column
polynomial Lambda of degree <n define U,V,Z as in A4/A5, and

\[
f(x)=x^{A+1}Z(x),\quad a(x)=(1-x)^h,\quad g(x)=a(x)f(x).
                                                               \tag{Z2}
\]

Both D channels are retained in
Z=x^{-1/2}U+V=x^{-1/2}int y^{b-1/2}Lambda(y)/(1-sqrt(xy))dy.
Write H_f(t)=PV int f(x)/(x-t)dx and E_Lambda for the full h-principal-part
function in A16. The actual dual function is

\[
W(t)=\frac\pi2 t^{A+1/2}U(t)
       +\frac{3\mu}{8}(-H_f(t)+E_\Lambda(t)).           \tag{Z3}
\]

The question is whether the actual constrained functions W-P, with
deg P<=K and the full tail constraints, have at most n distinct zeros.
This weaker bound would already suffice: a column annihilator requires
M=n+1 sign changes by A19--A22. It is unnecessary to prove the stronger
Chebyshev bound n-1. None of the lemmas below assumes either bound.

## 2. Clearing the principal parts retains their exact boundary data

Define the polynomial commutator

\[
J_h(t)=\int_0^1\frac{a(t)-a(x)}{x-t}f(x)dx.
\]

Since a(t)-a(x)=(x-t)sum_{ell=0}^{h-1}(1-t)^{h-1-ell}(1-x)^ell,

\[
a(t)H_f(t)=H_g(t)+J_h(t),\qquad
J_h(t)=\sum_{\ell<h}(1-t)^{h-1-\ell}s_\ell,
\quad s_\ell=\int_0^1(1-x)^\ell f(x)dx.                \tag{Z4}
\]

All integrals are finite: f=O(x^{A+1/2}) at 0 and grows at most
logarithmically at 1. The divided difference is a polynomial, so Z4
does not require an additional singular integral interchange.

For any deg P<=K put

\[
\Psi(t)=a(t)(W(t)-P(t))
=\frac\pi2t^{A+1/2}a(t)U(t)-\frac{3\mu}{8}H_g(t)-\Pi(t),
\]
\[
\Pi(t)=a(t)P(t)+\frac{3\mu}{8}\{J_h(t)-a(t)E_\Lambda(t)\},
\qquad\deg\Pi\le K+h.                                \tag{Z5}
\]

The h endpoint poles have become a polynomial; they have not disappeared.
Let r_j=int x^L(1-x)^j Z(x)dx. The exact remainder modulo (1-t)^h is

\[
\Pi(t)\bmod(1-t)^h
=\frac{3\mu}{8}\sum_{\ell=0}^{h-1}e_\ell
                                 (1-t)^{h-1-\ell},
\]
\[
e_\ell=s_\ell-
\sum_{j=\ell}^{h-1}\binom{m+j-\ell-1}{j-\ell}r_j.       \tag{Z6}
\]

Thus Pi is not a freely varying polynomial of degree K+h. Its high
part is aP and its h low endpoint jets are fixed by Lambda and mu.
For mu=0 those jets are zero. Dividing by the positive a on (0,1)
preserves every interior zero and sign change.

## 3. The full tails move the locked jets to a higher-contact kernel

The full-tail equations are r_h=...=r_{h+delta-1}=0. Put H=h+delta.
They imply the following new finite identity:

\[
\boxed{e_\ell=\int_0^1x^{A+1}(1-x)^H Z(x)
 \sum_{q=0}^{m-1}\binom{H-\ell+q-1}{q}x^q\,dx,
 \qquad0\le\ell<h.}                                   \tag{Z7}
\]

Every coefficient in this finite polynomial kernel is positive. The
values e_ell can have either sign, since Z is a signed transform.

Here is a self-contained proof. For integer r,m>=1 and v=1-x,

\[
(1-v)^{-m}-\sum_{j=0}^{r-1}\binom{m+j-1}{j}v^j
=\frac{v^r}{(1-v)^m}
 \sum_{q=0}^{m-1}\binom{r+q-1}{q}(1-v)^q.              \tag{Z8}
\]

For r=1 this is the finite geometric identity. Increasing r by one and
using Pascal's identity gives Z8 inductively: the difference of the two
finite polynomials on the right is binom(m+r-1,r)*x^m.
In Z6, s_ell=int x^L Z*x^{-m}v^ell. The tail equations allow the
subtracted sum to extend from j<h to j<H. Apply Z8 with r=H-ell and
multiply by x^L v^ell Z. Since L-m=A+1, the result is Z7.

This is stronger structural information than simply counting the
remaining h endpoint moments. It retains their precise mu linkage
after pole removal, through a higher-contact positive kernel.

## 4. A coupled Cauchy boundary problem with a genuine gap

The tail constraints are precisely

\[
\int_0^1x^j g(x)dx=0\quad(m\le j<n).                  \tag{Z9}
\]

Define, outside [0,1],

\[
C_g(z)=\int_0^1\frac{g(x)}{z-x}dx,\qquad
C_{g_m}(z)=\int_0^1\frac{x^m g(x)}{z-x}dx.
\]

Then the exact multiplication identity and tail order are

\[
C_{g_m}(z)=z^m C_g(z)-
 \sum_{j=0}^{m-1}z^{m-1-j}\int_0^1x^j g(x)dx,
\qquad C_{g_m}(z)=O(z^{-\delta-1}).                    \tag{Z10}
\]

The coefficients of C_g at orders m+1,...,n vanish, but its first m
coefficients are not asserted zero. This is a gap condition, not the
free consecutive multi-index of an ordinary perfection theorem.

For an actual column annihilator the other Cauchy transform is

\[
C_\Psi(z)=\int_0^1\frac{\Psi(x)}{z-x}d\nu_0(x),
\qquad C_\Psi(z)=O(z^{-M-1}),                           \tag{Z11}
\]

because A19 becomes int x^j Psi dnu_0=0 for 0<=j<M. This uses finite
weighted moments; Pi in Z5 has the locked boundary jets Z7.
If F(z)=(pi/2)z^{A+1/2}a(z)U(z)+(3mu/8)C_g(z)-Pi(z), its boundary
average on (0,1) is Psi and its jump is

\[
F_+(x)-F_-(x)=-\frac{3\mu\pi i}{4}g(x).               \tag{Z12}
\]

This follows from the Cauchy boundary formula; g is continuous and
locally smooth in the open interval. Thus Z5/Z7/Z10/Z11 specify the
actual coupling without deleting either channel or the endpoint data.

## 5. The actual constrained function space has dimension n

The complete D tail matrix has rank delta by A9--A10, valid also for
the b=0 positive integrable weight. Its column kernel therefore has
dimension n-delta=m. Adding P of degree <=K gives m+K+1=n parameters.
The map (Lambda,P) to Psi in Z5 is injective for every fixed real mu.
Indeed A21's nonzero log-square signature for mu!=0, or the nonzero
single-log signature for mu=0, precludes W-P=0 when Lambda!=0. If
Lambda=0 then W=0, so P=0.

Consequently this is an explicitly constrained n-dimensional real
function space, not an ambient space with an independent polynomial
Pi of degree K+h. Even a zero bound of n, allowing one defect beyond
the strongest Chebyshev bound, would establish the desired full-pool
rank. Dimension alone proves no such zero bound. This identifies the
precise next zero-count gate instead of asserting a free AT system.

## 6. An exact two-cut product before separating polynomial coefficients

Put S(t)=t^{n-1}Lambda(1/t), so deg S<=n-1, and

\[
d\sigma_+(t)=t^{-L+1/2}dt\quad(t\ge1).
\]

Changing y to 1/t in A4 gives

\[
U(z)=\int_1^\infty\frac{S(t)}{t-z}d\sigma_+(t),\qquad
V(z)=\int_1^\infty\frac{S(t)t^{-1/2}}{t-z}d\sigma_+(t).
                                                               \tag{Z13}
\]

The base measure sigma_+ has finite mass for L>3/2, as in both carriers.
The two displayed complete transforms converge for every b>=0. Even
when b=0 makes sigma_+ S have infinite mass, its Cauchy integral is
finite; it must not be called a finite generating measure.

For integer r>=1 let

\[
d\sigma_r(s)=s^{-1/2}(1+s)^{-r}ds,\qquad
H_r(z)=\int_0^\infty\frac{d\sigma_r(s)}{z+s}.
\]

The measure is finite. The exact regularizations are

\[
\sqrt z=P_r(z)+\frac{z(1-z)^r}{\pi}H_r(z),\quad
P_r=z+\sum_{j=1}^{r-1}c_jz(1-z)^j,
\]
\[
z^{-1/2}=\sum_{j=0}^{r-1}c_j(1-z)^j
                 +\frac{(1-z)^r}{\pi}H_r(z),
\qquad c_j=4^{-j}\binom{2j}{j}.                       \tag{Z14}
\]

The second identity follows from the same recurrence as A23. For 0<z<1
the product admits an exact absolutely convergent two-cut decomposition:

\[
\boxed{H_r(z)U(z)=
 \int_0^\infty\frac{U(-s)}{z+s}d\sigma_r(s)
 +\int_1^\infty\frac{S(t)H_r(t)}{t-z}d\sigma_+(t).}     \tag{Z15}
\]

Use 1/((z+s)(t-z))=(1/(t+s))(1/(z+s)+1/(t-z)) and Fubini.
For absolute convergence one may use |U(-s)|<=C(1+s)^(-1/2), directly
from its y integral, H_r(t)<=sigma_r(total)/t, and deg S<=n-1.
At the finite endpoints no denominator is zero for this z. The identity
extends analytically off the two cuts. It retains the actual linked
coefficient S within U(-s), instead of inventing a free negative-cut
coefficient.

## 7. The tail kernel does not remove the highest reciprocal coefficient

There are tail-annihilating column polynomials with Lambda(0)!=0.
Choose just the first delta+1 columns of the full tail matrix. It has
rank delta, and its delta-by-delta minor on columns 1,...,delta is
strictly positive by the same double-Cauchy/Vandermonde proof as A10.
The cofactor nullvector of this rectangular matrix thus has a nonzero
coefficient at column 0. It defines a Lambda of degree <=delta with
all tail equations and Lambda(0)!=0.

For this permitted column, deg S=q=n-1. This conclusion uses the actual
full-tail kernel for every N; it is not a generic parameter or sample
claim. The Jacobi moment equations may impose further restrictions,
but their unproved consequences cannot be assumed before the nonzero
argument.

## 8. A sharp obstruction to one common regularization order

Let U_0(z)=int d_sigma_+(t)/(t-z). Polynomial division gives the exact
identity

\[
U(-s)=S(-s)U_0(-s)+D_S(s),\quad
D_S(s)=\int_1^\infty\frac{S(t)-S(-s)}{t+s}d\sigma_+(t).
                                                               \tag{Z16}
\]

D_S is a polynomial of degree <=q-1, since the needed moments of
sigma_+ through q-1 are finite. If the leading coefficient of S is c
and q>=1, then

\[
S(-s)U_0(-s)\sim c(-1)^q\sigma_+(\mathbb R)s^{q-1},
\quad D_S(s)\sim-c(-1)^q\sigma_+(\mathbb R)s^{q-1}.     \tag{Z17}
\]

Here sU_0(-s) tends to the positive mass by dominated convergence,
whereas U(-s)=O(s^{-1/2}). The two leading powers cancel only in the
complete expression. Separating them inside the negative-cut integral
of Z15 gives tail magnitude s^{q-r-5/2}. Therefore each separate
Cauchy integral is absolutely finite exactly when

\[
r\ge q-1.                                             \tag{Z18}
\]

For the corresponding separated finite measures, rather than only the
Cauchy integrals, the stronger condition is r>=q. In particular r=4
does not permit this free high-degree splitting in the actual tail
kernel of section 7.

There is a conflicting requirement at the other cut. Apply the second
identity of Z14 to t^{-1/2} in V. The polynomial part has exact degree
r-1 and leading coefficient (-1)^{r-1}c_{r-1}. The nested part has the
opposite leading coefficient, since tH_r(t) tends to pi*c_{r-1}.
After multiplying by S, sigma_+ and the Cauchy denominator, each
separate positive-cut integrand has tail magnitude

\[
t^{q+r-L-3/2}.
\]

For q=n-1, its absolute convergence is exactly r<=b+1; finiteness of
the separated measures is r<=b. Thus one common order that makes both
free Cauchy splits legitimate would need

\[
\boxed{n-2\le r\le b+1.}                              \tag{Z19}
\]

For the actual b=11N,n=44N-1, n-2-(b+1)=33N-4>0. For b=0 the gap is
44N-4>0. Hence no such integer order exists in either carrier, for any
N>=1. The complete U,V and product Z15 remain finite: this failure is
caused by separating linked counterterms, not a divergence of the
actual carrier.

This is a no-go only for the specified **single-order, two separately
freed Cauchy decompositions**. Different regularizations, retained
linked counterterms, another common-root representation, or a weak
zero-count argument for the constrained space in section 5 are not
excluded. Increasing a negative-cut regularization order also introduces
an exact degree-r polynomial P_r and degree-(r+1) multiplier in Z14;
these degrees must be paid before invoking a free polynomial AT theorem.

## 9. Primary scope and the remaining gate

The available primary theorem is Fidalgo Prieto--Lopez Lagomasino,
*Nikishin systems are perfect. Case of unbounded and touching supports*,
[arXiv:1009.1922v1](https://arxiv.org/pdf/1009.1922v1). This round uses the
existing selected source reading recorded in
`literature/catalan_parity_actual_nonzero_sources_20261007/source_scope.md`;
no new primary-paper FULL reading or download is claimed here. Its finite
constant-sign measures, finite moments, integrable products, compatible
common root and free polynomial coefficient conditions are not replaced
by formal cancellation of divergent separated integrals.

The new paid structures are: pole removal with precisely locked h jets;
the higher-contact finite kernel Z7; the coupled boundary problem
Z10--Z12; the exact n-dimensional constrained space; and the sharp
regularization conflict Z19. They neither assert a coupled AT theorem
nor repeat the round-216 necessary sign counts as a new conclusion.

The useful next gate is now precise: prove a bound of at most n zeros
for the actual constrained space Z5/Z7/Z9, possibly with one allowed
defect, or construct a different absolutely legitimate common-root
representation whose degree budget yields that bound. A free masterweight
space need not itself be a Chebyshev system for this weaker constrained
route to work. No full rank, nonzero sequence, numerical irrationality,
or strict arithmetic/real comparison has been established in this note.

## 10. Author and independent review scope

The author will actually FULL reread this new note before pinning its
identity. Every displayed identity and threshold above is a paper
derivation. No old-source reexecution, numerical coefficient generation,
or new program is part of this work. Independent review is pending.

Final review receipt (round 217): the preceding pending sentence records
the initial pre-review state. The author subsequently actually FULL read
all ten sections Z1--Z19 in the 14504-byte version, SHA256
`cba6d02dc6d6f85ac89744987464e5985cebb2830322e3f0033054c41c319c35`,
and independently checked each displayed identity and threshold on paper.
Root then actually FULL read that same ten-section version and independently
paper-reviewed it: PASS, with no mathematical correction. Its review covered
the commutator and locked-jet signs, Z7--Z8's finite remainder, the tail-gap
orders and jump, dimension n, both exact split convergence thresholds, and
the expressly limited single-order free-split obstruction. Root did not
convert that obstruction into a claim of full moment rank or a numerical
theorem. Only this receipt was appended after its review. The author will
now FULL read the resulting complete file and report its final identity;
no mathematical program was executed.
