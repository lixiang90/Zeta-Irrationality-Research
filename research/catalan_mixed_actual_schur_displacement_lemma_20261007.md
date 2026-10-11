# Actual mixed moments: bounded displacement and positive Schur reconstruction

2026-10-07, round 215. New isolated symbolic note. No producer, finite parameter grid, prime scan or historical code was run. This derives a joint operator from the actual inhomogeneous M0/Z0 recurrences; it does not replace actual-point nonvanishing with the Phi ODE or generic C rank.

## 1. Fixed objects and the two different tail selections

The current nine-section Schur and jet notes were actually FULL reread for this continuation. The original `foundations.tex` lines 95–211, including the rational recurrences and period decomposition, were actually reread. The complete weighted-column and real-place notes were also actually FULL reread in this continuation; C8 and R9 are the interfaces being retained. The original source path is

`E:\codex-build\math\preprints\Catalans-constant-is-irrational-September-24-2026\build\sections\foundations.tex`.

Put

\[
A=19N,\ h=2N,\ q=4N,\ e=h+q=6N,\ b=7N,
\quad n=44N-1,\ L=55N-1,
\]
\[
\ell_0=8N+1,\ \ell_1=44N-1,\ p=36N-1,
\quad m_0=L-A-1=36N-2.
\]

Use the unscaled Jacobi basis `Q_j=P_j^(e-1/2,-1/2)`, `ell_0<=j<=ell_1`, for the allowed Q space, and `P_Q=t^A(1-t)^h Q`. Multiplying a whole polynomial pair by any of the established nonzero integral row scalars changes no rank conclusion; the operator identities below are stated before those row scalars.

Let

\[
T_a=t^{L+a}(1-t)^h,
\qquad V_k=s^{b+k}(1-s)^q.
\]

There are two selections. Write `delta` for the number of selected tails:

- `delta=8N`: the principal square has p Jacobi rows and delta tails, hence n rows. Its Schur matrix has p columns.
- `delta=8N+1`: the full pool has n+1 rows. Its Schur matrix has `m=n-delta=p-1=36N-2` columns.

In the formulas below `m=n-delta`; the contact section length remains m0 in **both** selections. Nonvanishing of a full-pool minor is not nonvanishing of the principal square.

## 2. The closed section and its multiplication defect

Define

\[
B_Q(z)=\int_{-1}^1
 \frac{(1-z)^eQ(z)-(1-x)^eQ(x)}{z-x}\,d\nu_0(x),
\quad d\nu_0=\frac{dx}{\pi\sqrt{1-x^2}}.
\]

The second-kind identity and the coefficient filter give the exact prescribed section

\[
E_Q(t)=\operatorname{trunc}_{<m_0}
\left(\frac{Q(t)}{\sqrt{1-t^2}}
       -\mu\frac{B_Q(t)}{(1-t)^e}\right),
\qquad
D_Q=t^{A+1}(1-t)^h E_Q.
\tag{D1}
\]

Here the square root has constant term 1. For the H part, its raw coefficients below L start at A+1, so the unit filter simply returns those coefficients. Dividing by the endpoint factor leaves `Q/sqrt(1-t^2)`. For the C part the filtered high coefficients are `[t^r]B_Q`; inverse filtering followed by endpoint completion leaves `B_Q/(1-t)^e` before the same truncation. This proves D1 for the specified section; its coefficients are not adjustable.

Directly from the divided difference,

\[
B_{tQ}(z)=zB_Q(z)+\int Q\,d\nu_e,
\qquad d\nu_e=(1-x)^e d\nu_0.
\]

Every allowed Q has integral zero. With `theta(Q)=[t^(m0-1)]E_Q`, truncation therefore gives

\[
\boxed{D_{tQ}=tD_Q-\theta(Q)T_0.}
\tag{D2}
\]

D1 defines a linear closed operator also on the two boundary polynomials Q_(ell0-1) and Q_(ell1+1); those boundary pairs need not satisfy all low contact conditions. They occur only on the right side of the operator identity and are not added to the allowed row space.

## 3. Actual rational Stein identity and every boundary

For any polynomial pair define the formal rational moment functional

\[
\mathcal F_\gamma(P,D;V)
=M^0(P,V)-\tfrac32Z^0(D,V)+\gamma C(P,V),
\]
\[
C(P,V)=\sum_{i,j}P_i V_j c_{(i-j)/2}.
\]

For the allowed mixed pairs, under the proposed relation this is exactly the actual filtered moment with `gamma=4u/a` and `mu=16b/a`. Unconditionally, the actual specialization is `gamma=4G+mu*pi^2/4`. Source lines 108–109 and 168–184 give the first recurrence below; lines 192–202 give the second:

\[
M^0(i,j)-M^0(i+1,j+1)=\frac{m_i}{j+1},
\quad
Z^0(i,j)-Z^0(i+1,j+1)
=\frac1{(i+1)(j+1)}.
\]

The second identity includes the diagonal; it follows either from the harmonic formula or the actual geometric moment recurrence, whose zeta coefficient is unchanged by this simultaneous shift. C is also unchanged. Thus

\[
\boxed{\mathcal F_\gamma(P,D;V)
-\mathcal F_\gamma(tP,tD;sV)=\eta(P,D)\beta(V),}
\tag{D3}
\]
\[
\eta(P,D)=\sum_iP_i m_i-\tfrac32\sum_i\frac{D_i}{i+1},
\qquad\beta(V)=\int_0^1V(s)ds.
\]

All quantities in D3 are rational at fixed rational parameters. This is the actual inhomogeneous moment datum; no algebraic C-kernel ODE is used.

Multiplication by t has the Jacobi three-term recurrence. Let J be its compression to degrees ell0 through ell1. The only external Jacobi directions are Q_(ell0-1) in the first row and Q_(ell1+1) in the last row. In the Jacobi orthonormal basis J is real symmetric and has spectrum strictly inside (-1,1): multiplication by t is a self-adjoint contraction, and equality at an endpoint is impossible for a nonzero polynomial in the positive measure nu_e. In the rational unscaled basis J is diagonally similar to that symmetric matrix.

Order the Jacobi pairs first and selected tails last. Multiplication of their pairs has the internal row matrix

\[
\mathcal R=\begin{pmatrix}J&\theta e_0^t\\0&H_\delta\end{pmatrix},
\tag{D4}
\]

where H_delta has ones in position (a,a+1) and zeros elsewhere. The sign of theta is positive here because `tD_Q=D_(tQ)+theta T0`. There are exactly three external pair directions: the two Jacobi boundary pairs and `(0,T_delta)` from the highest selected tail. For the principal square T_delta is the omitted permitted tail; for the full pool it has degree H=65N and is an external boundary pair outside the strict degree support. Both are paid explicitly.

Let F be the `(p+delta)-by-n` matrix of the selected allowed pairs and let S_n have ones in position (k+1,k). If G_ext is the three-by-n array of the formal rational moments of the three external pairs, and U_ext is their `(p+delta)-by-3` multiplication-coefficient array, put `G=U_ext G_ext`. Thus G has the same size as F and rank at most 3. Since `sV_k=V_(k+1)` only for k<n-1 inside the selected columns,

\[
F-\mathcal R F S_n
=\eta\bar\beta^t+G S_n+F_{\rm last}e_{n-1}^t,
\qquad\operatorname{rank}\le5.
\tag{D5}
\]

Here barbeta has the actual beta masses in positions 0 through n-2 and zero in the last position. The last column in D5 is a separate boundary, not a silently shifted contact equation. In particular V_n has raw degree L and can meet the diagonal zeta term of T0. D5 uses Z0 throughout and makes no substitution of Z for that extra column.

## 4. Tail Schur compression retains bounded displacement

Write

\[
F=\begin{pmatrix}\mathsf A&\mathsf B\\T_0&T_1\end{pmatrix},
\quad W=T_0^{-1}T_1,
\quad S=\mathsf B-\mathsf A W.
\]

The tail T0 is delta-by-delta and invertible by the paid strict positivity. Its rows include the actual factor -3/2. The column and row changes

\[
U=\begin{pmatrix}I&-W\\0&I\end{pmatrix},
\quad
L_r=\begin{pmatrix}I&-\mathsf A T_0^{-1}\\0&I\end{pmatrix}
\]

give `L_r F U=[0 S;T0 0]`. Under them the Jacobi block of `L_r R L_r^(-1)` is still J, and its lower-left block is zero. Put

\[
w^t=e_{\delta-1}^tW,
\qquad B_\delta=S_m-e_0w^t.
\tag{D6}
\]

This is the lower-right block of `U^(-1) S_n U`, with first row -w and subdiagonal ones. If K is its upper-right block and C_r is the upper-right block of `L_r R L_r^(-1)`, D5 yields

\[
\boxed{S-JS B_\delta=E,
\quad E=(L_r(F-RFS_n)U)_{\rm Jac,res}+C_rT_0K.}
\tag{D7}
\]

The first term has rank at most 5. The apparently large tail-mixing term has rank at most 3, as follows. The residual tests are

\[
R_j(s)=V_{\delta+j}(s)-\sum_{a<\delta}W_{a,j}V_a(s),
\quad0\le j<m.
\]

They annihilate every selected tail. `T0 K` evaluates the tails on
`sR_j-[j=m-1]V_n`, because the finite column shift removes exactly that last monomial. For a>=1 the actual Z recurrence gives

\[
Z(T_a,sR_j)=-\left(\int T_{a-1}\right)\left(\int R_j\right).
\]

For these a, Z(T_a,V_n)=Z0(T_a,V_n), since the tail starts above L. The row a=0 is retained as its own rational functional on the truncated test. Consequently

\[
T_0K=e_0z^t+\ell\beta_R^t-u e_{m-1}^t,
\]

where `ell_0=u_0=0`, `ell_a=(3/2)int T_(a-1)` and `u_a=-(3/2)Z0(T_a,V_n)` for a>=1. The vector z is the actual first row of T0K. Every displayed coefficient is rational. Therefore

\[
\boxed{\operatorname{rank}(S-JS B_\delta)\le8}
\tag{D8}
\]

for both tail selections, every N and all fixed rational mu,gamma. This is a joint displacement assertion about the actual rational moment data. It is neither a row-norm bound nor a nonvanishing theorem.

## 5. An exact positive model for the companion coefficients

For every j the Cramer ratio `w_j=W_(delta-1,j)` replaces the last column of T0 by the column with monomial exponent delta+j. In the positive double-Cauchy integral for that ratio, the s Vandermonde is multiplied by the complete homogeneous symmetric polynomial `h_(j+1)(s_1,...,s_delta)`. The factor (-3/2)^delta cancels in the ratio. Thus there is one probability measure on the two ordered simplices, independent of j, for which

\[
\boxed{w_j=\mathbb E h_{j+1}(s_1,\ldots,s_\delta)>0.}
\tag{D9}
\]

The determinant identity used here is the finite alternant identity
`det[s_a^(0,...,delta-2,delta+j)]/V(s)=h_(j+1)(s)`. It follows, for example, by expanding the generating function `prod_a(1-xs_a)^(-1)` and comparing the last-column alternant; it involves no unproved mixed positivity. The probability density is the positive integrand for det T0 divided by that integral. Convergence was already paid in the strict-positive-tail lemma.

Define

\[
H_\delta(x)=1+\sum_{j=0}^{m-1}w_j x^{j+1}.
\tag{D10}
\]

This is the expectation of the Taylor polynomial of degree m at zero of
`g_s(x)=prod_a(1-xs_a)^(-1)`. Each derivative of g_s is positive on (-1,1). For x<0 and **even m**, Taylor's remainder of order m+1 is negative, so its degree-m Taylor polynomial is greater than g_s(x), which is at least 2^(-delta). For x>=0 that polynomial is at least 1. Hence in the **full-pool selection**, where m=36N-2 is even,

\[
\boxed{H_\delta(x)\ge2^{-\delta}>0\quad(-1<x<1).}
\tag{D11}
\]

It follows that H_delta(J) is positive definite in the Jacobi orthonormal basis and invertible in the rational basis. Its inverse operator norm in that orthonormal basis is at most 2^delta. This positivity is derived from the actual tail moments, not from the Phi ODE.

For the principal square m=36N-1 is odd. The Taylor remainder has the opposite sign, and D11 is not claimed. Positivity of individual w_j does not suffice to settle that case.

## 6. A concrete source-driven reconstruction and the remaining target test

Let s_j,e_j be the columns of S,E. D7 with the companion D6 gives

\[
s_j-Js_{j+1}+w_jJs_0=e_j\quad(j<m-1),
\qquad s_{m-1}+w_{m-1}Js_0=e_{m-1}.
\]

Backward substitution pays the exact finite recursion

\[
H_\delta(J)s_0=\sum_{r=0}^{m-1}J^r e_r,
\tag{D12}
\]
\[
s_j=\sum_{r=j}^{m-1}J^{r-j}e_r
-\left(\sum_{r=j}^{m-1}w_rJ^{r-j+1}\right)s_0.
\tag{D13}
\]

For the full pool D11 therefore proves uniqueness of reconstruction from the actual rank-at-most-eight seed E, for every parameter pair. No homogeneous Stein resonance can cause a failure in that selection. This is an all-N positive operator theorem, not actual-point rank.

For a precise weaker target-point criterion put

\[
R_E=\sum_{r=0}^{m-1}J^r e_r,
\quad G_j(J)=\sum_{r=j}^{m-1}w_rJ^{r-j+1},
\]
\[
k_j=H_\delta(J)\sum_{r=j}^{m-1}J^{r-j}e_r-G_j(J)R_E,
\quad\mathcal K=(k_0,\ldots,k_{m-1}).
\tag{D14}
\]

All inputs in E are the displayed actual rational arrays, sections and boundary moment rows, evaluated at the **fixed** mu,gamma. D12–D13 give `K=H_delta(J)S`; in the full-pool selection,

\[
\boxed{\operatorname{rank}F=n
\iff\operatorname{rank}\mathcal K=p-1.}
\tag{D15}
\]

This is a concrete inhomogeneous Krylov-type residual condition, with the inverse operator already paid positively. It does not ask for nonvanishing at every complex gamma. Proving D15's right side along an unbounded sequence at the proposed rational relation point would suffice for full-pool nonvanishing there. No such proof is claimed here. Boundary seeds and their joint cancellations must still be controlled; a small displacement rank alone cannot imply their independence.

For the principal square the same recursion and rank-eight identity hold, but invertibility of H_delta(J) would have to be proved separately before using this reconstruction. Even successful full-pool reconstruction and rank do not prove its designated omitted-tail square nonzero.

There is a further finite polynomial compression of this actual residual test. At a fixed rational parameter pair choose any rational rank factorization

\[
E=\sum_{\alpha=1}^{r_*}u_\alpha v_\alpha^t,
\quad r_*\le8,\qquad
q_\alpha(x)=\sum_{j=0}^{m-1}(v_\alpha)_j x^j.
\]

Write H for H_delta. Define the m-by-m rational coefficient matrix B_alpha by

\[
\sum_{i,j=0}^{m-1}(B_\alpha)_{i,j}x^iy^j
=\frac{xq_\alpha(x)H(y)-yq_\alpha(y)H(x)}{x-y}.
\tag{D16}
\]

The numerator vanishes at x=y. Since both x q_alpha and H have degree at most m, the quotient has degree at most m-1 in each variable. More explicitly, the coefficient of y^j is

\[
H(x)\sum_{r=j}^{m-1}(v_\alpha)_r x^{r-j}
-\left(\sum_{r=j}^{m-1}w_r x^{r-j+1}\right)q_\alpha(x).
\]

Although each separate product could have degree up to 2m-1, these displayed products cancel all powers above m-1. Comparing this coefficient with D14 proves the exact identity

\[
\boxed{\mathcal K=\sum_{\alpha=1}^{r_*}
[u_\alpha,Ju_\alpha,\ldots,J^{m-1}u_\alpha]B_\alpha.}
\tag{D17}
\]

Thus the fixed relation-point question is a rank test for a sum of at most eight explicit Krylov–Bezout operators built from the actual boundary seeds. The J here is the parameter-independent Jacobi compression, not the canonical parameter-dependent observing matrix J_mu of the preceding jet note. D17 proves neither independence of these operators nor a bound on the heights of an arbitrary chosen rank factorization. It holds algebraically for both tail selections; using its rank as the full-pool criterion relies on D11.

## 7. Relation to the joint real-place problem and exact scope

D5 and D8 retain both actual D_mu and every Jacobi, tail and last-column boundary. Their bounded displacement is a possible joint singular-value input; proving a favorable leading exponent still requires spectral/separation and seed estimates for the exact object. No such exponent, row-norm improvement or trace estimate is supplied here. In particular the principal square cannot inherit the even-m positivity of the larger row pool.

The new proved content is the closed section multiplication defect, actual rational Stein data, constant-rank compressed displacement for both selections, a positive Cauchy-ensemble representation of the companion coefficients, unconditional positive reconstruction for the full-pool Schur operator, and the explicit degree-bounded Krylov–Bezout residual representation. The arbitrary rational relation-point rank and the complete arithmetic/analytic strict comparison remain open. The C1 left kernel still has D_C=0 and a mu-independent v; these facts do not remove the new actual-seed requirement in D15.

Both theta_analytic_geometry and gamma_bound actually FULL read the seven-section D1–D15 version (13820 bytes; SHA256 ed5c0d4249d21abc8db10b70c583fb24cac44a6a569e3ec48b9d3aac7940fe64) and independently checked every formula and scope, with PASS and no mathematical correction. Gamma_bound then actually read the complete updated section 6 and independently paper-checked D16–D17 with PASS; that added review is a bounded section reading, not a second FULL reading of the new file. It identified one missing display backslash before qquad, which was repaired. Root then actually FULL read all seven D1–D17 sections at 15959 bytes, SHA256 6c8b1328896553a7e15c16c46d5b833304cfbe41e391210b16597eefc515bde8, and independently paper-checked every formula and scope with PASS and no correction. The author actually FULL read all seven sections after D16–D17 and again after this final receipt update. No main, old note or manifest was edited.
