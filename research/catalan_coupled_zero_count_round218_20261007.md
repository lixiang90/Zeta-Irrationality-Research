# Round 218: independent endpoint jets and the unavailable Hilbert self-test

2026-10-07. NEW paper note for the actual q=0 carrier. The new result is
joint surjectivity of the original endpoint moments and the pole-cleared
endpoint jets after every tail equation. A separate lemma excludes a
direct polynomial Hilbert self-test. Neither result proves or refutes the
required at-most-n zero theorem. No mathematical program was executed.

## 1. Actual object, hypotheses, and source reading

The actual dual interface A1--A23 was actually FULL read again during
round 218. Its frozen 16005-byte identity is SHA256
`6646d25d91e54347bb73ea29486bec0cf1b4cf7d061baaae3e216180ab84d900`.
The round-217 master-weight mathematical version M1--M15 had been
independently FULL paper-reviewed; the author's coupled Z1--Z19 note had
been FULL read and independently reviewed by root. Their formulae are
used below. This does not claim another FULL reading of their subsequent
receipt-only versions or of any primary paper.

State the algebra for integers A>=b>=0, h>=1, n>=1, with

\[
L=b+n,\quad K=A-b,\quad m=L-A-1=n-K-1\ge h,
\quad\delta=K+1,\quad H=h+\delta,
\quad q_*=h+H=2h+\delta\le n.                         \tag{O1}
\]

The current support is

\[
A=19N,\ b=11N,\ h=2N,\ n=44N-1,
\quad m=36N-2,\ \delta=8N+1,
\quad H=10N+1,\ q_*=12N+1.                           \tag{O2}
\]

All O1 hypotheses hold for every N>=1. For a real polynomial Lambda of
degree <n use the actual complete channels

\[
U(x)=\int_0^1\frac{y^{b-1/2}\Lambda(y)}{1-xy}dy,
\quad V(x)=\int_0^1\frac{y^b\Lambda(y)}{1-xy}dy,
\]
\[
Z=x^{-1/2}U+V
=x^{-1/2}\int_0^1
 \frac{y^{b-1/2}\Lambda(y)}{1-\sqrt{xy}}dy,
\quad f=x^{A+1}Z,\quad a=(1-x)^h,\quad g=af.        \tag{O3}
\]

Fix real mu and the actual integral parameter
gamma_*(mu)=4G+mu*pi^2/4. There is no unrelated formal gamma in this
note. The actual dual, with every endpoint principal part, is

\[
W=\frac\pi2 x^{A+1/2}U
       +\frac{3\mu}{8}(-H_f+E_\Lambda),\qquad
H_f(t)=\operatorname{PV}\int_0^1\frac{f(x)}{x-t}dx.   \tag{O4}
\]

## 2. The joint endpoint map is onto, not only its separate parts

Define

\[
s_\ell=\int_0^1x^{A+1}(1-x)^\ell Z(x)dx\quad(0\le\ell<h),
\qquad
r_j=\int_0^1x^L(1-x)^jZ(x)dx\quad(0\le j<H).
                                                               \tag{O5}
\]

The linear map from degree-<n column polynomials to
(s_0,...,s_{h-1},r_0,...,r_{H-1}) is onto R^(q_*).
Indeed its square restriction to columns 1,y,...,y^(q_*-1) has a
nonzero determinant. This statement holds before selecting mu.

Here is a proof of that particular minor. The common x weight after O3
is x^(A+1/2)dx, the y weight is y^(b-1/2)dy, and the positive kernel is
C(x,y)=1/(1-sqrt(xy)). The x test polynomials are

\[
(1-x)^\ell\ (0\le\ell<h),\qquad
x^m(1-x)^j\ (0\le j<H).
\]

An invertible triangular change separately in the two groups replaces
them by the distinct monomials with ordered exponents

\[
0,1,...,h-1,\quad m,m+1,...,m+H-1.                   \tag{O6}
\]

Their generalized Vandermonde is strictly positive at increasing
positive points. For completeness, distinct nonnegative exponent
monomials form a Chebyshev system: divide a nonzero combination by its
smallest power, differentiate, and apply Rolle inductively to show at
most q_*-1 distinct positive zeros. Its evaluation determinant cannot
vanish. Its sign is positive by the coalescing-point Wronskian, whose
nonconstant factor is the positive product of exponent differences;
the ordered-point domain is connected.

The y monomials have the ordinary positive Vandermonde. Also, at ordered
x_i,y_j in (0,1),

\[
\det[C(x_i,y_j)]
=\frac{\prod_{i<j}(\sqrt{x_j}-\sqrt{x_i})
                  (\sqrt{y_j}-\sqrt{y_i})}
       {\prod_{i,j}(1-\sqrt{x_i y_j})}>0.             \tag{O7}
\]

Applying the determinant integration identity twice expresses the
changed minor as the integral of these three positive determinants and
the positive weights, divided by (q_*!)^2. It is strictly positive;
undoing the two triangular changes leaves a nonzero minor.
All interchanges are justified: the corner kernel is bounded by a
constant times 1/((1-x)+(1-y)), which is integrable on the square.
The zero-end weights have exponents A+1/2>=1/2 and b-1/2>=-1/2.
Each finite determinant expansion is dominated termwise by a product
of finite single-entry integrals. No asymptotic or finite sample is used.

## 3. Fixing the original compensator leaves every cleared jet free

The full tails are r_h=...=r_(H-1)=0. Surjectivity in section 2 implies
that on this exact tail kernel the map

\[
\Lambda\longmapsto (s_0,...,s_{h-1},r_0,...,r_{h-1})
\quad\hbox{is onto }\mathbb R^{2h}.                 \tag{O8}
\]

This is stronger than separate surjectivity of the h original endpoint
moments. It keeps their joint relation with the commutator moments.
Set the invertible upper-triangular matrix

\[
T_{\ell j}=\binom{m+j-\ell-1}{j-\ell}\quad(j\ge\ell),
\qquad T_{\ell j}=0\quad(j<\ell),
\quad e=s-Tr_{\rm low}.                              \tag{O9}
\]

Its diagonal is one. The actual E_Lambda coefficients are precisely
Tr_low, and the pole-cleared low jets are e. Consequently
(e,r_low), and equivalently (e,the h coefficients of E_Lambda), are
jointly onto R^(2h) on the full tail kernel.

For clarity, with any polynomial P of degree <=K, the exact commutator
of the round-217 note gives

\[
\Psi=a(W-P)=\frac\pi2 t^{A+1/2}a(t)U(t)
             -\frac{3\mu}{8}H_g(t)-\Pi(t),
\]
\[
\Pi=aP+\frac{3\mu}{8}\{J_h-aE_\Lambda\},\qquad
J_h=\sum_{\ell<h}s_\ell(1-t)^{h-1-\ell},\quad
\deg\Pi\le K+h,
\]
\[
\Pi\bmod(1-t)^h
=\frac{3\mu}{8}\sum_{\ell<h}e_\ell(1-t)^{h-1-\ell}.
                                                               \tag{O10}
\]

For fixed nonzero mu, fixing the entire compensator E does not fix or
restrict these h jets: any e is attainable while all tails remain zero.
The map has kernel dimension n-2h-delta=32N-2 in the current support.
For mu=0 the e functionals still have this rank, but their contribution
to Pi is zero; no nonzero endpoint coefficient is claimed in that case.

Thus tail/contact elimination cannot reduce this actual endpoint data
to one scalar by asserting a hidden dependence between s and r. A
successful zero theorem can still use their linked dependence on the
same Lambda and on the other terms. Joint surjectivity does not make
all coefficients in the actual dual freely independent.

## 4. The Hilbert self-pairing exists but its test is unavailable

For the real g in O3, g vanishes at both endpoints and is Holder
continuous with some positive exponent. Near zero it is O(x^(A+1/2));
near one it is O((1-x)^h(1+abs(log(1-x)))). Thus the elementary
finite-interval Hilbert antisymmetry identity applies:

\[
\int_0^1g(t)H_g(t)dt=0.                              \tag{O11}
\]

One may prove O11 directly by symmetrically excluding abs(x-t)<=eps in
the double integral: the antisymmetric kernel has zero integral against
g(x)g(t). Subtracting g(t) from g(x) bounds the nonsingular part by an
integrable Holder difference quotient. The remaining elementary logarithm
is integrable, since g vanishes at both endpoints. The excluded integrals
therefore converge to O11.

However a full-pool annihilator supplies only
int t^j Psi(t)dnu_0(t)=0 for 0<=j<=n, where
dnu_0=dt/[pi sqrt(t(1-t))]. In order to obtain int g Psi dt from these
equations by a polynomial test, the required test would be

\[
\mathcal T_\Lambda(t)=\frac{g(t)}{d\nu_0/dt}
=\pi t^{1/2}(1-t)^{h+1/2}f(t).                      \tag{O12}
\]

For every nonzero Lambda this is not even a rational function, so it
is not an allowable polynomial of degree <=n. Indeed the exact endpoint
division of A21 gives
f(t)=a_log(t)log(1-t)+b_0(t), with a_log,b_0 analytic near one and
a_log(t)=-2t^(A-b)Lambda(1/t) not identically zero. Multiplying by the
factor in O12 preserves a nonzero logarithmic term with half-integer
endpoint exponent. It cannot be a rational Laurent germ. Multiplying
O12 by any nonzero rational scalar gauge likewise cannot remove its
logarithmic term.

Therefore the known polynomial orthogonality does not justify setting
int g Psi to zero, even though the Hilbert piece would cancel in that
particular pairing. The tails give only polynomial moments of g in
degrees m,...,n-1 and do not supply this nonrational test. This excludes
the direct self-test step, not other contour identities, a coupled
operator pairing or a properly proved positive matrix argument.

## 5. Effect on the decisive gate

The actual space of W_mu,Lambda-P with all tails has dimension n, and a
full-pool column annihilator requires n+1 sign changes. These previously
proved facts are not counted as new round-218 results. The new facts are
the joint endpoint rank O8--O10 and the exact unavailability of the
otherwise valid self-test O11--O12.

No at-most-n zero theorem, counterexample to that theorem, full-rank
sequence or numerical independence statement has emerged here. The
constant four-master-weight one-defect result cannot be substituted for
this missing high-degree coupled theorem. The present lemmas exclude
specific shortcuts; they do not show that every variation-diminishing,
mixed multi-level or differential-chain mechanism fails. They therefore
do not pass the round-218 decisive gate or justify promoting the fixed
support. A numerical theorem remains the research goal.

## 6. Execution and review scope

This note is self-contained paper work from the stated frozen interfaces.
No new primary-paper download or FULL source claim, and no mathematical
program, interval evaluator, finite matrix, parameter grid, prime scan,
PSLQ or Lean was executed. No old mathematical note, main or manifest was
edited. Independent review is pending. The author will actually FULL
read this new file before reporting its byte/SHA identity.
