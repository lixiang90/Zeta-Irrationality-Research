# Parity q=0 actual-point rank: an exact dual interface and the unpaid zero count

Date: 2026-10-07. Round 216. This is a new paper calculation. No producer,
matrix experiment, prime scan, grid, or PSLQ was run. The main manuscript and
existing manifests are unchanged.

## 1. Object and quantifier

The authoritative input actually read in full is
`research/catalan_mixed_parity_positive_kernel_20261007.md`, eleven sections
P1--P19, 15818 bytes, SHA256
`a39081cb49a101c80a6b7f69306d67fd873caebc6dbad3198c2a21dad85449d8`.
Only its q=0 carrier is used here. Put

\[
A=19N,\quad h=2N,\quad K=8N,\quad M=44N,\quad n=M-1,
\quad b=11N,\quad L=55N-1,\quad m=L-A-1=36N-2,
\quad\delta=8N+1.                                      \tag{A1}
\]

The full pool has M rows and n columns. Its Jacobi rows have indices
d=K+1,...,M-1 and its tails are
x^{L+a}(1-x)^h, 0<=a<delta. We seek rank n for fixed rational parameters
mu,gamma along an unbounded set of N. This note **does not establish that
rank assertion**. It proves exact necessary conditions for a rank failure,
an all-N tail rank assertion, and an all-N obstruction to deleting the
endpoint compensator. It also supplies a valid finite negative-cut Markov
representation, with an explicit boundary to its use.

Write

\[
d\nu_h(x)=\frac{x^{-1/2}(1-x)^{h-1/2}}\pi\,dx,
\qquad Q_d(x)=P_d^{(h-1/2,-1/2)}(2x-1),
\]
\[
\mathcal Q_N=\{Q:\deg Q<M,\ \int x^jQ(x)d\nu_h(x)=0\ (0\le j\le K)\}.
                                                               \tag{A2}
\]

Its basis is Q_{K+1},...,Q_{M-1}. Let B_Q be the polynomial second kind in
P4/P18 of the input. For the following dual calculation choose the completion

\[
F_Q(x)=B_Q(x)-x^m\operatorname{Taylor}_{1,<h}[B_Q(x)/x^m],
\qquad D_C(Q)=x^{A+1}F_Q.                              \tag{A3}
\]

The completion has the prescribed low contact, is divisible by (1-x)^h,
and has the allowed support. Replacing m in (A3) by any R with m<=R<=n
changes D_C by a member of the **full** delta-dimensional tail space.
Consequently the full-pool rank and its column annihilators are unchanged.
This statement does not apply to a pool omitting the last tail.

## 2. Both actual D channels, and the rational pencil

For a real column polynomial Lambda(y)=sum_{k=0}^{n-1}lambda_k y^k define

\[
U(x)=\int_0^1\frac{y^{b-1/2}\Lambda(y)}{1-xy}\,dy,
\qquad V(x)=\int_0^1\frac{y^b\Lambda(y)}{1-xy}\,dy,
\qquad Z(x)=x^{-1/2}U(x)+V(x).                         \tag{A4}
\]

No D channel has been omitted. Their exact combination is particularly
useful:

\[
Z(x)=x^{-1/2}\int_0^1
 \frac{y^{b-1/2}\Lambda(y)}{1-\sqrt{xy}}\,dy.           \tag{A5}
\]

Indeed (x^{-1/2}+sqrt(y))/(1-xy)=x^{-1/2}/(1-sqrt(xy)).
The actual integral row on (P_Q,D_mu), D_mu=-mu D_C(Q), equals

\[
\frac12\int_0^1x^A(1-x)^{h-1/2}Q(x)U(x)\,dx
 +\frac{3\mu}{8}\int_0^1x^{A+1}F_Q(x)Z(x)\,dx.        \tag{A6}
\]

A tail row equals -3/8 times
int_0^1 x^{L+a}(1-x)^h Z(x) dx. Formula (A6) retains the signs and the
normalizing constants of P13/P14.

There is a parameter qualification. The actual integral matrix corresponds
to gamma_*(mu)=4G+mu*pi^2/4, where G is Catalan's constant. The formal rational
pencil has entries F_0+gamma C. For arbitrary rational mu,gamma its Jacobi
rows equal (A6)+(gamma-gamma_*(mu))c_Lambda(Q), where c_Lambda is the exact
linear functional obtained from that pencil's C entries. Under the proposed
single relation gamma=gamma_*(mu), the extra term is zero. Thus an arbitrary
formal rational gamma must not silently be identified with the actual
integral parameter.

## 3. The full tails have rank delta for every N

Define the endpoint moments by

\[
r_j(\Lambda)=\int_0^1 x^L(1-x)^jZ(x)\,dx.
                                                               \tag{A7}
\]

The tail equations are equivalent to

\[
r_h=r_{h+1}=\cdots=r_{h+\delta-1}=0,                    \tag{A8}
\]

because the powers x^a and (1-x)^a are related by an integer invertible
triangular change of basis. All double integrals here are finite. Near
(x,y)=(1,1), the only possible kernel bound needed is a constant times
1/((1-x)+(1-y)), which is integrable on the square.

The double Cauchy kernel is strictly totally positive. For increasing
0<x_1<...<x_r<1 and 0<y_1<...<y_r<1,

\[
\det\left[\frac1{1-\sqrt{x_i y_j}}\right]
 =\frac{\prod_{i<j}(\sqrt{x_j}-\sqrt{x_i})
                   (\sqrt{y_j}-\sqrt{y_i})}
        {\prod_{i,j}(1-\sqrt{x_i y_j})}>0.              \tag{A9}
\]

Twice applying the determinant integration identity, first in x and then
in y, gives strictly positive square minors for row powers x^a and column
powers y^k, with positive weights x^{L-1/2}(1-x)^h and y^{b-1/2}.
The determinants of these monomial evaluation matrices are Vandermonde
determinants. Their product and (A9) have constant positive sign on the
ordered integration domains. Integrability follows termwise from the
finite single kernel integral. Taking a,k=0,...,delta-1 proves

\[
\operatorname{rank}(\hbox{full tail matrix})=\delta
\quad\hbox{for every }N\ge1.                           \tag{A10}
\]

This is an actual kernel statement independent of mu and gamma. It is
smaller than the required rank n assertion.

## 4. Endpoint moments survive the tail equations

Apply the same proof to j,k=0,...,h+delta-1 in the matrix
[r_j(y^k)]. The row evaluation determinant of (1-x)^j has the constant
sign (-1)^{r(r-1)/2} times the x Vandermonde. Hence

\[
\det[r_j(y^k)]_{0\le j,k<h+\delta}\ne0.                 \tag{A11}
\]

Here h+delta=10N+1<=n, so all these columns exist. The map from the n
column coefficients to the h+delta moments is onto. Restricting to the
kernel of the delta high moments in (A8), the h low moments
(r_0,...,r_{h-1}) remain onto R^h. In particular they are not identically
zero there. This rules out an exact cancellation of the whole endpoint
compensator merely from the filtered contact and full-tail equations.

For R=n rather than m, its compensation moments are

\[
\int x^{A+1+R}(1-x)^j Z(x)dx
 =\sum_{k=0}^{8N+1}(-1)^k\binom{8N+1}{k}r_{j+k}.
                                                               \tag{A12}
\]

Terms with h<=j+k<=h+delta-1 vanish by (A8); the surviving low moments
are the same h-dimensional endpoint data. This is consistent with the
full-tail equivalence of the two completions, and is not permission to
discard that data.

## 5. Exact second-kind adjoint

For 0<=ell<h put

\[
\beta_\ell(Q)=\int_0^1\frac{Q(t)}{(1-t)^{\ell+1}}d\nu_h(t),
\qquad
a_j(Q)=\sum_{\ell=0}^j\binom{m+j-\ell-1}{j-\ell}\beta_\ell(Q).
                                                               \tag{A13}
\]

The endpoint relation R_Q/sqrt(z(z-1))=B_Q+W_Q, R_Q=(1-z)^hQ,
gives B_Q^(ell)(1)/ell!=(-1)^{ell+1}beta_ell(Q). Consequently

\[
F_Q(x)=B_Q(x)+x^m\sum_{j=0}^{h-1}a_j(Q)(1-x)^j.        \tag{A14}
\]

For Q=Q_d all beta_ell and a_j are positive; their finite Beta formula is
P19 in the input. Formula (A13) is the linear extension to arbitrary Q.

Let f(x)=x^{A+1}Z(x) and
H_f(t)=PV int_0^1 f(x)/(x-t) dx. The arcsine Cauchy transform has zero
real boundary value in (0,1), so its polynomial divided-difference adjoint
is

\[
\int_0^1 f(x)B_Q(x)dx=-\int_0^1 Q(t)H_f(t)d\nu_h(t).
                                                               \tag{A15}
\]

For completeness, insert
B_Q(x)=int(R_Q(x)-R_Q(t))/(x-t)dnu_0(t), split at a symmetric exclusion
of x=t, and use PV int dnu_0(t)/(x-t)=0. The unsplit divided difference
is a polynomial. Passing to the limit is valid here: f is smooth on
compact interior intervals, is O(x^{A+1/2}) at 0, and is O(1+|log(1-x)|)
at 1. Its Hilbert transform is bounded at 0 and has at most logarithmic
square growth at 1. The factor (1-t)^{h-1/2} pays that endpoint, and the
remaining rational poles in (A13) have order at most h, also integrable
against nu_h.

Define

\[
E_\Lambda(t)=\sum_{\ell=0}^{h-1}
 \frac{\sum_{j=\ell}^{h-1}\binom{m+j-\ell-1}{j-\ell}r_j}
 {(1-t)^{\ell+1}},
\]
\[
W_{\mu,\Lambda}(t)=\frac\pi2t^{A+1/2}U(t)
 +\frac{3\mu}{8}\{-H_f(t)+E_\Lambda(t)\}.              \tag{A16}
\]

Then (A6) is exactly int Q W_{mu,Lambda} dnu_h. This retains the whole
endpoint rational function and both D channels.

For the formal pencil, choose the unique polynomial xi_Lambda of degree
<M with zero low Jacobi coefficients and
int Q_d xi_Lambda dnu_h=c_Lambda(Q_d), d=K+1,...,M-1. Replace W by

\[
W_{\mu,\gamma,\Lambda}=W_{\mu,\Lambda}
 +(\gamma-\gamma_*(\mu))\xi_\Lambda.                   \tag{A17}
\]

This is an exact finite-dimensional representation, not an additional
positive-kernel claim.

## 6. Two necessary zero counts, without adding them

Every column annihilator of the full pool satisfies (A8) and

\[
\int Q(t)W_{\mu,\gamma,\Lambda}(t)d\nu_h(t)=0
\quad(Q\in\mathcal Q_N).                              \tag{A18}
\]

There is therefore a polynomial P of degree <=K such that

\[
\int t^j(W_{\mu,\gamma,\Lambda}(t)-P(t))d\nu_h(t)=0
\quad(0\le j<M).                                     \tag{A19}
\]

One may obtain P by matching the low K+1 Jacobi coefficients; orthogonality
then matches every polynomial of degree <M. Only finite weighted moments
are used, not a possibly divergent unweighted L2 projection.

If Lambda is nonzero, Z is not identically zero. In fact, after z=sqrt(x),

\[
zZ(z^2)=2\int_0^1\frac{s^{2b}\Lambda(s^2)}{1-zs}ds.
\]

All Taylor moments cannot vanish for a nonzero polynomial. Moreover Z has
at most deg(Lambda) sign changes on (0,1). To see this without a general
variation-diminishing theorem, suppose it has more zeros than the number
of sign changes of Lambda(s^2). The functions 1/(1-z_i s) for those distinct
zeros span every numerator polynomial of degree below their number over
the positive denominator product_i(1-z_i s). Choose the numerator to have
exactly the sign-change zeros of Lambda(s^2); its product with the signed
density has constant nonzero sign. This contradicts all the chosen zero
equations. Thus (A8) requires

\[
\delta\le\#\operatorname{signchanges}Z
\le\#\operatorname{signchanges}\Lambda\le n-1.         \tag{A20}
\]

Also W-P is never identically zero when Lambda is nonzero, for any real
mu,gamma. Here is an endpoint proof. Near x=1, polynomial division in s
gives

\[
f(x)=a(x)\log(1-x)+b_0(x),\qquad
a(x)=-2x^{A-b}\Lambda(1/x),                           \tag{A21}
\]

with a,b_0 analytic near 1 and a not identically zero. For an analytic
coefficient a, the local principal-value integral of a(x)log(1-x)/(x-t)
has log^2(1-t) coefficient a(t)/2. This follows by writing a(x)=a(t)+
(x-t)c(x,t); the latter contributes an analytic function, while
PV int log(1-x)/(x-t) dx has leading term log^2(1-t)/2. A truncated local
interval gives the same coefficient. The other terms have only single
logarithms or rational endpoint poles. For mu!=0 the log-square coefficient
in (A16) is -3mu*a/16 and cannot disappear. For mu=0, the first term in
(A16) has single-log coefficient -pi*x^{A-b}Lambda(1/x)/2, which is
nonzero. Adding the polynomial in (A17) or subtracting P cannot cancel
these logarithmic signatures.

The standard sign polynomial argument applied to (A19) consequently gives

\[
\#\operatorname{signchanges}(W_{\mu,\gamma,\Lambda}-P)\ge M=44N.
                                                               \tag{A22}
\]

Equations (A20) and (A22) concern different functions. They cannot simply
be added to produce a contradiction. A coupled upper zero count that
retains the endpoint rational function is the missing rank lemma.

## 7. A finite negative-cut Markov representation really exists

For r>=1 define

\[
H_r(x)=\int_0^\infty
 \frac{t^{-1/2}}{(1+t)^r(x+t)}dt\quad(x>0).
\]

Let c_j=binom(2j,j)/4^j. Direct beta integration and partial fractions give
H_1=pi/[sqrt(x)(1+sqrt(x))] and
H_{r-1}=(1-x)H_r+pi*c_{r-1}. Hence the exact identity

\[
\sqrt x=P_r(x)+\frac{x(1-x)^r}{\pi}H_r(x),\qquad
P_r=x+\sum_{j=1}^{r-1}c_jx(1-x)^j.                    \tag{A23}
\]

For r=4, the positive measure t^{-1/2}(1+t)^{-4}dt, placed at -t, has
finite moments of orders 0,1,2,3. Thus the initially infinite measure in
sqrt(x)=(x/pi)int t^{-1/2}/(x+t)dt is repairable by exact polynomial
regularization; infinite mass alone is not a no-go.

There is a genuine two-measure Nikishin ambient system: take root measure
x*dnu_h on [0,1] and the above negative-cut measure on (-infinity,0].
Their supports touch only at 0 and neither has an atom there. H_4 is
O(x^{-1/2}) at 0, so the product with x*dnu_h is finite; the root has all
moments finite. In contrast, dnu_h*H_4 has density of order x^{-1} at 0
and is not integrable. A root change or an explicitly paid factor is
necessary, rather than silently using dnu_h itself.

## 8. Primary theorem scope and the actual gap

Primary source: U. Fidalgo Prieto and G. Lopez Lagomasino,
[Nikishin systems are perfect. Case of unbounded and touching supports,
arXiv:1009.1922v1](https://arxiv.org/pdf/1009.1922v1).
Selected reading covered Definitions 1.2--1.4, Theorems 1.1--1.3, and the
main proof at pp. 23--24; it was not a full-paper audit. The results require
finite constant-sign generating measures, the stated finite moments,
integrable nested products, and a common compatible root in mixed type.
They give AT zero bounds and perfectness for the resulting polynomial
linear forms. The archive and precise read scope are in
`literature/catalan_parity_actual_nonzero_sources_20261007/source_scope.md`.

The valid ambient system in section 7 does not itself prove (A22)
impossible. The actual B_Q uses Q*dnu_h, not an unconstrained polynomial
coefficient times x*dnu_h; moving to that root introduces Q/x at 0.
The endpoint function E_Lambda in (A16) has h distinct principal parts,
whose moment data survive all tail equations by (A11). Finally the mu
constraint links the first- and second-kind parts; the polynomial
coefficients are not the freely varying components of the cited mixed
type problem. Each exact map and its degree bounds would need to be
proved. Constant-sign kernels considered separately do not supply them,
and an arbitrary signed mu combination cannot be declared a positive
Nikishin generating measure.

## 9. Paid results and stopping boundary

For every N>=1 we have proved: full tail rank delta; surjectivity of the h
remaining endpoint moments after tail elimination; the exact dual
relations (A16)--(A19); the two necessary sign-change counts (A20)/(A22);
and the finite negative-cut representation (A23). These assertions use
the actual q=0 object and do not transfer any old Chebyshev valuation or
generic-C rank argument.

What remains is a coupled AT/zero-count theorem for (A16), with (A8),
the mu link, and the endpoint rational function retained, strong enough
to rule out a nonzero Lambda for the fixed rational pair mu,gamma under
the target relation. Neither all-N full moment rank nor rank along an
unbounded sequence has been established here. No nonzero determinant,
irrationality statement, analytic gap, or joint arithmetic saving is
claimed. This is an exact nonzero interface and a boundary to the direct
Nikishin invocation, not a rejection of all possible Nikishin reductions.

Review receipt: root actually FULL read the nine-section, 15081-byte
version, SHA256
`241fa766c5bfeac7b0050d72d69d03dff79c8265e1c41f218142144d2e692b7b`,
and independently paper-checked A1--A23 with PASS and no mathematical
correction. Its stated independent checks included both-channel identity,
Cauchy signs, surviving endpoint surjectivity, full-tail binomial range,
principal-value adjoint and endpoint integrability, formal-gamma
qualification, logarithmic square coefficient, the separate necessary
zero counts, and the finite negative-cut ambient system. Root's extra
primary reading at this receipt was bounded: archived text introduction
and Definitions 1.1--1.4 (first 205 text lines), plus searches of theorem
hypotheses. This is not recorded as a whole primary-paper audit. After
adding this receipt and two wording clarifications, the author actually
FULL reread the final nine sections. No mathematical program was run.
