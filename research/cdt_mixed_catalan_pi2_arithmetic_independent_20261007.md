# Mixed Catalan–pi squared carrier: independent arithmetic proof

2026-10-07. Isolated mathematical note. No main/manifest edits and no old producer runs. The original five-function carrier has a genuine four-function projection; this note works with that projection. All denominator claims cover every finite prime and every prime power. Necessary response claims exclude only finitely many primes determined by fixed rational coefficients. The arbitrary-basis conclusion is restricted to CDT fixed N powers and finite LCM types; it does not cover more general joint arithmetic lattices.

Let

\[
A(x)=\arctan x=\sum_{n\ge1}\chi_4(n)x^n/n,
\quad B(x)=\sum_{n\ge1}\chi_4(n)x^n/n^2,
\quad S=A^2,
\]
\[
\Psi=aB+16bS,\qquad F'=(\Psi-u)/(1-x),\quad F(0)=0,
\tag{M1}
\]

where a,b,u are rational, a is nonzero, and b is nonzero for the mixed-basis cost theorem below. The case b=0 must be treated separately. The conditional endpoint relation is \(aG+b\pi^2=u\). The closed rational system is

\[
A'=1/(1+x^2),\qquad
\Psi'=A\bigl(a/x+32b/(1+x^2)\bigr),\qquad
F'=(\Psi-u)/(1-x).
\tag{M2}
\]

## 1. Actual rank and endpoint normalization

The actual functions \(1,A,\Psi\) have C(x) rank three. A positive loop around i, with a fixed bridge on which log(i)=i*pi/2, has

\[
\Delta A=\pi,\qquad
\Delta B=\pi(\log x-\log i),\qquad
\Delta S=2\pi A+\pi^2.
\tag{M3}
\]

Subtracting a putative rational relation gives, if the coefficient of Psi is nonzero, an expression of log(x) in C(x)+C(x)A. Continuing around zero contradicts it, since A is regular there whereas log(x) gains 2*pi*i. The coefficients of Psi, A and 1 therefore vanish in turn.

For u different from the canonical value Psi(1), a loop around 1 already translates only F by a nonzero constant. If u=Psi(1), first transport around i and then around zero q times. The transported endpoint discrepancy is

\[
\Delta\Psi(1)=a\pi(2\pi iq-i\pi/2)+24b\pi^2\ne0
\quad(q\in\mathbb Z).
\tag{M4}
\]

Its imaginary part is nonzero because a is a nonzero real rational. At this transported branch a loop around 1 leaves the front three functions unchanged and gives F a nonzero constant jump. Conjugating back leaves precisely this constant translation. Thus

\[
\dim_{\mathbb C(x)}\langle1,A,\Psi,F\rangle=4.
\tag{M5}
\]

The statement is independent of whether the endpoint relation is true.

## 2. All finite-prime safety caps

Write L_N=lcm(1,...,N), L_0=1, and choose a fixed positive integer d clearing a,16b,u. Direct convolution gives, for N=2k,

\[
S_N=(-1)^{k-1}\frac1k
 \sum_{\substack{1\le j<N\\j\text{ odd}}}\frac1j,
\quad S_N=0\ (N\text{ odd}).
\tag{M6}
\]

Consequently

\[
NA_N\in\mathbb Z,\quad N^2B_N\in\mathbb Z,
\quad NL_{N-1}S_N\in\mathbb Z,
\quad L_{N-1}L_{\lfloor N/2\rfloor}S_N\in\mathbb Z.
\tag{M7}
\]

For the last assertion, in every term 1/(j(N-j)), the smaller of the two p-valuations is at most v_p(L_floor(N/2)), and the larger is at most v_p(L_(N-1)). This also handles j=N-j.

Useful projected caps are

\[
dNL_N\Psi_N\in\mathbb Z,\qquad dL_N^2\Psi_N\in\mathbb Z,
\]
\[
dNL_{N-1}^2F_N\in\mathbb Z,
\qquad dL_N^2L_{\lfloor N/2\rfloor}F_N\in\mathbb Z.
\tag{M8}
\]

Indeed F_N=(sum_(n<N)Psi_n-u)/N. For the last cap fix any prime p and write alpha=v_p(L_N), beta=v_p(L_floor(N/2)). In the B contribution n^2*N, if v_p(n)>beta, then v_p(n)=alpha and v_p(N)<=beta; otherwise v_p(n)<=beta. Both cases give 2v_p(n)+v_p(N)<=2alpha+beta. In an S contribution j*(n-j)*N with n<N, if either inner valuation exceeds beta, its value is alpha, and both the other inner valuation and the outer valuation are at most beta. Otherwise both inner valuations are at most beta. Hence the total is at most alpha+2beta<=2alpha+beta. These are exact valuation arguments, including p=2 and arbitrary powers.

The all-e-zero array

\[
e=(0,0,0,0),\qquad \sigma=(0,1,2,5/2)
\tag{M9}
\]

is legal and safe: one width-one column starts at A, a second starts at Psi, and one width-half column starts at F. Fixed normalizations do not change its cost.

## 3. Exact p and 2p packets

Consider any fixed row regular at zero,

\[
W=r_0+r_AA+r_\Psi\Psi+r_FF,
\qquad r_\bullet\in\mathbb Q(x).
\tag{M10}
\]

Finite Laurent poles at zero are allowed. After excluding finitely many primes, every Laurent coefficient of each fixed multiplier is p-integral. This follows by writing it as x^h times a polynomial quotient with unit denominator constant term and applying the formal inverse recursion. Thus full infinite rational tails are allowed throughout.

For every sufficiently large odd prime p, put epsilon=chi_4(p), a p-unit. All source coefficients with index below p are p-integral. In particular F_p has valuation at least -1: its numerator is a p-integral prefix and its only possible p denominator is the external p. Moreover

\[
p^2\Psi_p=a\epsilon,\quad
p^2\Psi_{p+k}\equiv0,\quad
p^2F_p\equiv0,\quad
p^2F_{p+k}\equiv a\epsilon/k\pmod p
\tag{M11}
\]

for each fixed positive k. Therefore, for each fixed nonzero integer offset t,

\[
p^2W_{p+t}\equiv a\epsilon[x^t](r_\Psi+r_FL)\pmod p,
\qquad L=-\log(1-x).
\tag{M12}
\]

There is no unknown F_p scalar in M12, because p^2*F_p is zero modulo p. If r_F is nonzero, r_Psi+r_F*L cannot be a constant Laurent series, since L is not rational. Hence some fixed t different from zero makes the right side nonzero for every sufficiently large prime. This forces two LCM columns of width at least one, regardless of the fixed external power N^e:

\[
r_F\ne0\ \Longrightarrow\ \sigma(W)\ge2.
\tag{M13}
\]

If r_F=0 but r_Psi is nonconstant, M12 gives the same conclusion. Thus sigma<2 forces r_F=0 and r_Psi to be constant.

In that remaining case write r_Psi=c. If c is nonzero, then for positive offsets k

\[
pW_{p+k}\equiv\epsilon[x^k](r_A+32bcA)\pmod p.
\tag{M14}
\]

Since b*c is nonzero, this response has a nonzero coefficient at some fixed positive offset: otherwise A would differ from a rational function by a finite Laurent polynomial. It follows that

\[
W\notin\langle1,A\rangle_{\mathbb Q(x)}
\ \Longrightarrow\ \sigma(W)\ge1\qquad(b\ne0).
\tag{M15}
\]

Finally S_(2p) has the unique doubly p-divisible convolution term A_p^2, giving p^2*S_(2p)=1 modulo p. The unique depth-three contribution to F_(2p) comes from a*B_p/(2p):

\[
p^3F_{2p}\equiv a\epsilon/2\pmod p.
\tag{M16}
\]

All other source coefficients in a fixed window about 2p have depth at most two. Thus p^3*W_(2p+t)=a*epsilon*[x^t]r_F/2 modulo p. If r_F is nonconstant, choose a nonzero offset; if it is constant and e=0, use t=0. Either way three width-half columns are necessary when e=0. Combined with M13's two width-one columns this gives sigma>=5/2.

## 4. Component bounds and arbitrary-basis matching

The resulting component-wise bounds are

| Nonzero coordinate | e=0 | e>=1 |
|---|---:|---:|
| r_A | sigma>=1 | sigma>=0 |
| r_Psi | sigma>=2 | sigma>=1 |
| r_F | sigma>=5/2 | sigma>=2 |

For r_Psi at e=0, either M12 already forces sigma>=2, or r_F=0 and r_Psi=c is a nonzero constant. In the latter case W_p has unique depth two, so its two p layers must be supplied by two width-one columns. For r_A at e=0, all cases with another nonzero coordinate already have sigma>=1; otherwise the fresh A_p packet gives one width-one column, at a nonzero shift if the multiplier is nonconstant and at p itself if it is constant.

Let any four rows be a full Q(x) basis. Their coordinate matrix in (1,A,Psi,F) is invertible, so its determinant has a nonzero permutation term. Match each row to the corresponding nonzero coordinate in that term. The preceding bounds apply separately to every matched row. Truncate its e to 0 for a row matched to 1, and to min(e,1) for every other row. This preserves all lower bounds and cannot increase tau-sharp, because both sum(e) and max(e) decrease and I(xi)>=0. Sorting the matched sigma lower bounds gives a componentwise lower bound for the actual nondecreasing row sums. This is the required justification for passing from individual packets to all rational bases; no natural-basis minimum is being transferred without proof.

Only the eight matched e configurations remain. For m=4 the exact I is

\[
I(\xi)=\begin{cases}
83/12-4\xi+\xi^2/2&0\le\xi\le1,\\
95/12-6\xi+3\xi^2/2&1\le\xi\le4/3,\\
21/4-2\xi&4/3\le\xi\le3/2,\\
15/2-5\xi+\xi^2&3/2\le\xi\le2,\\
7/2-\xi&2\le\xi\le3,\\
(4-\xi)^2/2&3\le\xi\le4.
\end{cases}
\tag{M17}
\]

For max(e)=1 and sum(e)=1,2,3, the exact sharp costs are respectively 7/16,21/32,77/96; they follow directly by minimizing the displayed rational quadratics. Therefore:

| (e_A,e_Psi,e_F) | flat | sharp | total |
|---|---:|---:|---:|
| (0,0,0) | 61/32 | 0 | 61/32 |
| (1,1,1) | 19/16 | 77/96 | 191/96 |
| (0,1,0) | 51/32 | 7/16 | 65/32 |
| (0,1,1) | 11/8 | 21/32 | 65/32 |
| (1,1,0) | 45/32 | 21/32 | 33/16 |
| (0,0,1) | 27/16 | 7/16 | 17/8 |
| (1,0,0) | 55/32 | 7/16 | 69/32 |
| (1,0,1) | 3/2 | 21/32 | 69/32 |

The necessary minimum is exactly 61/32, and M9 attains it with a legal all-finite-prime array. Thus the projected mixed carrier, for b nonzero, has

\[
\boxed{\tau_{\rm fixed\ type}^{\min}=61/32
\quad\text{over all full }\mathbb Q(x)\text{ bases}.}
\tag{M18}
\]

This is an exact theorem for the specified type model. More general joint arithmetic lattices require a different interface; this note makes no impossibility claim for them.

## 5. Genuine odd/even descent does not retain the same rank reduction

For y=x^2 let T(y)=F(x)+F(-x), C=A/x, D=B/x, E=A^2. Then

\[
C_y'=(1/(1+y)-C)/(2y),\quad D_y'=(C-D)/(2y),
\quad E_y'=C/(1+y),
\]
\[
T_y'=(aD+16bE-u)/(1-y).
\tag{M19}
\]

The endpoint y=1 fills under the same relation. But aD+16bE has a derivative containing -aD/(2y), so for b nonzero the single projected combination no longer closes with only C. The explicit rational closure needs (1,C,D,E,T), a five-function rank upper bound. This note does not assert its exact rank or optimal cost. The odd/even trace therefore supplies no demonstrated cheaper four-function system. Differentiating F removes its primitive quotient direction and cannot by itself be counted as retaining the same conditional holonomy trigger.

Read inputs: the complete theta arithmetic note T1–T27 and odd holonomy budget note (7)–(8), plus the parent-supplied mixed carrier. The eight cost values were independently recomputed with exact rational JavaScript, not a prime scan and not an old producer. M6–M18 are paper proofs; no numerical irrationality or linear-independence conclusion is claimed.
