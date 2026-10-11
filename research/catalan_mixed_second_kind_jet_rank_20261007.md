# All-N second-kind jet rank and a generic mixed moment minor

Date: 2026-10-07. New symbolic lemma, separate from the contact construction and the actual-moment Schur note. No determinant producer, historical script, or numerical guard was run for this proof.

## 1. Fixed scope and theorem

Use the final ten-section contact note and the exact moment/filter definitions in original `foundations.tex` lines 54–211, actually read for this continuation. All identities below are derived from their finite `c` kernels. The all-`N` positive tail block used at the end is the theorem in

`E:\kimi-build\zeta5\research\catalan_mixed_actual_moment_schur_lemma_20261007.md`.

Fix

\[
M=44N,\quad K=8N,\quad e=h+q=6N,\quad
b=7N,\quad q=4N,\quad h=2N,\quad A=19N,
\quad n=M-1=44N-1.
\]

For every polynomial `Q` of degree `<M`, put `P_Q=t^A(1-t)^hQ` and let `C_hat(Q)` be the `n` filtered infinity coefficients at columns `0,...,n-1`. The concrete new theorem is

\[
\boxed{\operatorname{rank}\bigl(Q\longmapsto\widehat C(Q)\bigr)=M-1.}
\]

After imposing the first `K+1=8N+1` low-contact conditions, the permitted `Q` space has dimension `p=36N-1`. Its remaining `m=p-1=36N-2` filtered infinity coefficients have exact rank `m`. Equivalently, the second-kind Taylor-jet matrix in section 7 of the Schur note has full column rank for every `N>=1`.

This will prove a nonzero polynomial maximal minor of the actual rational mixed moment pencil for every `N`. It will not assert nonvanishing at every rational parameter point.

## 2. A finite Toeplitz matrix for the full infinity coefficient map

Recall

\[
c_l=4^{-l}\binom{2l}{l},\qquad c_z=0\text{ for inadmissible indices}.
\]

Since `q` is even, the filter at column `ell` reads the coefficient at index `b+q+ell` after multiplying `P_Q` by `(1-t)^q` inside the infinity expansion. The discrepancy caused by negative Laurent powers has degree at most `q-1`, below all the relevant indices `b+q+ell`. Consequently on the monomial `Q=t^i`,

\[
\widehat C_\ell(t^i)
=\sum_{v=0}^e(-1)^v\binom ev
 c_{(i+v+K-\ell)/2},\qquad
0\le i<M,\quad0\le\ell<M-1.
\]

Define the two-sided sequence, with only finitely many negative indices,

\[
a_s=\sum_{v=0}^e(-1)^v\binom ev c_{(s+v)/2}.
\]

The finite output-by-input matrix is exactly

\[
\mathsf A_{\ell,i}=a_{i+K-\ell}.
\]

Its Laurent generating series is

\[
\begin{aligned}
\sum_{s\in\mathbb Z}a_s z^s
&=(1-z^{-1})^e\sum_{l\ge0}c_lz^{2l}\\
&=z^{-e}\Phi(z),
\qquad
\Phi(z)=\frac{(1-z)^e}{\sqrt{1-z^2}}.
\end{aligned}
\]

The last equality uses even `e=6N`, and the square root has Taylor constant term 1.

## 3. A row dependence would give an impossible rational approximation

Suppose the `M-1` output functionals were dependent. There would be a nonzero polynomial

\[
\Lambda(z)=\sum_{\ell=0}^{M-2}\lambda_\ell z^\ell,
\qquad \deg\Lambda\le M-2,
\]

such that for every input exponent `0<=i<M`,

\[
\sum_\ell\lambda_\ell a_{i+K-\ell}=0.
\]

By the generating series this means that the coefficients of `Phi Lambda` at all indices

\[
K+e,\ K+e+1,\ldots,K+e+M-1
\]

are zero. Put

\[
s=K+e+M=58N,
\qquad
\Pi(z)=\operatorname{trunc}_{<K+e}(\Phi(z)\Lambda(z)).
\]

Then

\[
\deg\Pi\le K+e-1=14N-1,\qquad
E(z)=\Phi(z)\Lambda(z)-\Pi(z)=O(z^s).
\]

The crucial point is that this gives two more zero coefficients than the degree count for a rational approximation can tolerate for this first-order algebraic function.

## 4. The first-order ODE closes the degree argument

Direct differentiation gives

\[
D(z)\Phi'(z)=\sigma(z)\Phi(z),\qquad
D(z)=1-z^2,\quad\sigma(z)=(1-e)z-e.
\]

Form the polynomial

\[
\Omega(z)=D(z)(\Pi'\Lambda-\Pi\Lambda')
 -\sigma(z)\Pi\Lambda.
\]

Its degree is at most

\[
(M-2)+(K+e-1)+1=s-2=58N-2.
\]

Substituting `Pi=Phi Lambda-E` and using the ODE yields the exact identity

\[
\Omega=-D(E'\Lambda-E\Lambda')+\sigma E\Lambda.
\]

Since `E=O(z^s)`, the right side has order at least `s-1=58N-1` at zero. Thus a polynomial of degree at most `s-2` has order at least `s-1`; it must vanish identically.

If `Pi=0`, the equality `Phi Lambda=O(z^s)` is impossible for nonzero `Lambda`, because `Phi(0)=1` and `ord_0 Lambda<=deg Lambda<=M-2<s`. Hence both `Pi` and `Lambda` are nonzero. The identity `Omega=0` says that the nonzero rational function `Pi/Lambda` satisfies the same ODE as `Phi`:

\[
\frac{(\Pi/\Lambda)'}{\Pi/\Lambda}
=\frac{\sigma(z)}{1-z^2}.
\]

At `z=-1`, the right side has residue `-1/2`. The logarithmic derivative of a nonzero rational function has an integer residue at every point. This is a contradiction. Equivalently, the same ODE would force `Pi/Lambda` to be a nonzero constant times `Phi`, but

\[
\Phi(z)^2=\frac{(1-z)^{2e-1}}{1+z}
\]

has an odd-order pole at `-1`, so `Phi` cannot be rational.

Therefore no output-row dependence exists, and

\[
\boxed{\operatorname{rank}\mathsf A=M-1.}
\]

The proof is over `Q` or `C` and holds for every positive integer `N`; it uses no finite experiment.

## 5. Restriction to the Jacobi contact space and the exact jet rank

The first `K+1` rows of `A` are independent, as a subset of its independent rows. Their common kernel is the permitted positive-moment contact space

\[
\mathcal Q=\left\{\deg Q<M:
\int x^rQ(x)\,d\nu_e(x)=0\ (0\le r\le K)\right\},
\qquad\dim\mathcal Q=M-K-1=36N-1=p.
\]

The kernel of the entire full coefficient map has dimension exactly 1, and lies in `Q`. Restricting the remaining `n-(K+1)=m` coefficients to `Q` therefore gives

\[
\boxed{\operatorname{rank}C_1=p-1=m=36N-2.}
\]

The Jacobi rows of degrees `8N+1,...,44N-1` form a basis of `Q`. With the second-kind polynomial

\[
B_Q(z)=\int\frac{(1-z)^eQ(z)-(1-x)^eQ(x)}{z-x}\,d\nu_0(x),
\]

the Schur note proved `C_1(Q)_r=[z^r]B_Q`, `0<=r<m`. Thus the precise high-Jacobi second-kind Taylor-jet matrix has full column rank. No associated-polynomial sign-regularity theorem or unproved positivity assertion is needed for these jets.

## 6. A genuine all-N polynomial minor of the mixed moment pencil

Use the Schur notation

\[
S(\mu,r)=S_0+\mu S_1+rC_1,
\qquad
\mathsf F(\mu,r)=\begin{pmatrix}R+\mu U+rC\\T\end{pmatrix}.
\]

The pure-`D` first-column block `T_0` is invertible for every `N`, by strict total positivity of `Z`. Since `rank C_1=m`, choose `m` of the `p` Jacobi directions, indexed by `I`, such that `det(C_1)_I!=0`. For **every fixed** `mu`,

\[
\det S_I(\mu,r)
=\det(C_1)_I\,r^m+\text{lower powers of }r.
\]

Therefore the actual rational mixed moment minor using all `d=8N+1` tail rows and these `m=36N-2` Jacobi rows is a nonzero polynomial in `r` of exact degree `m`, with leading coefficient

\[
\det T_0\,\det(C_1)_I\ne0.
\]

This proves an all-`N` generic nonvanishing theorem. For each fixed `mu`, that chosen minor has at most `m` exceptional complex values of `r`; outside them the full pool has output rank `n` and its moment kernel has dimension 1.

The selected rows here use **all** `8N+1` pure-`D` tails and only `36N-2` Jacobi directions. The earlier designated square used `8N` tails and all `36N-1` Jacobi directions. Its determinant is a different minor and is not proved nonzero by this leading-coefficient argument.

## 7. The actual slope in mu also has maximal rank

There is an exact additional rational factorization. The section `D_C` depends only on the residual filtered `C_1` vector: its first `d` outputs are zero, the unit triangular equations solve the rest, and the fixed endpoint completion is linear. Hence for a rational matrix `L_C` of size `m by n`,

\[
U=C_1L_C,\qquad
\boxed{S_1=C_1\mathsf K,\quad
\mathsf K=(L_C)_{J_1}-(L_C)_{J_0}T_0^{-1}T_1.}
\]

This is a proved factorization, not a consequence of numerical ranks. In particular

\[
S(\mu,r)=S_0+C_1(\mu\mathsf K+rI_m).
\]

The section `D_C` has filtered coefficient map equal to `C`. The exact rank just proved implies

\[
\dim D_C(\mathcal Q)=m,
\qquad
D_C(\mathcal Q)\cap\mathcal D_{\rm tail}=\{0\}.
\]

Indeed, the unit triangular prescription gives zero `D_C` exactly when the entire filtered `C` vector is zero; the selected endpoint section adds no homogeneous tail. Consequently

\[
D_C(\mathcal Q)\oplus\mathcal D_{\rm tail}
=\mathcal D,
\qquad \dim\mathcal D=m+d=n.
\]

The complete permitted `D -> Z` moment map is an isomorphism by the all-`N` positivity theorem. Applying it to this decomposition and eliminating the same tail block proves

\[
\boxed{\operatorname{rank}(S_1+\pi^2 C_1/4)=m.}
\]

Equivalently, `mathsf K+(pi^2/4)I_m` is invertible.

The factor `pi^2/4` follows from `(3/2) zeta(2)=pi^2/4` in the `Z` coefficient decomposition. Thus the unconditional actual moment pencil

\[
S_{\rm actual}(\mu)=S_0+4G C_1
 +\mu(S_1+\pi^2 C_1/4)
\]

has a nonzero polynomial minor of degree `m` in `mu`, for every `N`. It can have only finitely many exceptional real `mu` for that minor. This does not rule out a particular nonzero rational `mu` being exceptional.

## 8. A more concrete criterion for all target values at a fixed mu

Let `q_*` be a nonzero rational row-coordinate vector spanning the one-dimensional left kernel of `C_1`. It may be written explicitly using its alternating maximal minors. The corresponding `Q_*` has all filtered infinity coefficients zero. Therefore

\[
D_C(Q_*)=0,\qquad q_*U=0,\qquad q_*S_1=0.
\]

Choose `m` rational Jacobi combinations with an invertible `C_1` minor, and use them together with `q_*` as a row basis. A rational column change makes the lower `C_1` block the identity. In these fixed bases the Schur matrix is exactly

\[
\boxed{\begin{pmatrix}v\\A+\mu B+rI_m\end{pmatrix},}
\]

with rational `v,A,B` independent of `mu,r`. In particular the top row `v` is independent of both parameters, rather than a new period term.

For fixed `mu`, put `J_mu=A+mu B`. The Schur matrix has full column rank for **every complex** `r` if and only if `v` is a cyclic observing row for `J_mu`, namely

\[
\boxed{\Delta_N(\mu)=
\det\begin{pmatrix}v\\vJ_\mu\\\vdots\\vJ_\mu^{m-1}\end{pmatrix}\ne0.}
\]

Here is an elementary proof. If a right eigenvector `w` of `J_mu` is annihilated by `v`, every row of that observing matrix annihilates `w`, and `r` equal to the negative eigenvalue makes the Schur matrix lose rank. Conversely, if the observing matrix is singular, its common kernel is nonzero and invariant under `J_mu`, by the Cayley–Hamilton identity. Over `C` it contains an eigenvector, producing such a rank-loss target value.

Thus the question of excluding all target values at a fixed `mu` can be reduced to a **single** rational polynomial in `mu`, of degree at most `m(m-1)/2`. No assertion that this observing determinant is nonzero for all nonzero rational `mu`, or that it is nonzero at a given `mu`, is made here. It is a concrete additional condition, not a numerical test already performed.

## 9. Scope of the positive result

The all-`N` second-kind jet rank is proved. The generic polynomial nonzero minor in the target coefficient `r=4u/alpha` is consequently proved for every fixed `mu`. The analogous generic actual-moment statement in `mu` is also proved, and the observing-determinant criterion gives a finite exact algebraic target for further work.

The arbitrary prescribed rational point `mu!=0,r=4u/alpha` can still be exceptional. The two-end contact construction, the new jet-rank theorem, and generic nonvanishing do not prove that it avoids those exceptions. Actual determinant nonvanishing at every such point, or a separate arithmetic/analytic argument handling an exceptional point, remains necessary for the intended irrationality application.
