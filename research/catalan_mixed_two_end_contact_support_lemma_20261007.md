# Mixed Catalan two-end contact: exact support obstruction and smaller kernels

Date: 2026-10-07. This note is a new symbolic analysis of the current original `foundations.tex`. It does not alter the original source, the project main files, a manifest, or another research manuscript. No historical script, numerical guard, determinant experiment, or repository proof producer was run.

## 1. Actual source scope and notation

The source actually read in full, with line numbers, is

`E:\codex-build\math\preprints\Catalans-constant-is-irrational-September-24-2026\build\sections\foundations.tex`, lines 1–434.

Source receipt: 17,469 bytes; SHA-256 `21633dce32e242555dde97f82f1124f3524641bb69a2f16b7485177b667cb738`.

For the explicit alternative basis in section 9, the primary NIST DLMF pages were also actually opened: [Table 18.3.1, Jacobi row](https://dlmf.nist.gov/18.3#T1), [the Jacobi Rodrigues row of Table 18.5.1](https://dlmf.nist.gov/18.5#T1), and [Equation 18.5.8](https://dlmf.nist.gov/18.5#E8). The actual reading was these entries and their immediate definitions, not a full read of Chapter 18. The separate receipt is `literature/catalan_mixed_contact_jacobi_source_scope_20261007.md`.

The relevant original locations are:

| Original lines | Content used here |
|---|---|
| 9–16 | The integer linear parameter family |
| 17–30 | The branch of `f`, the variable `w`, the involution, and row definitions |
| 32–52 | Integral Chebyshev expressions, exact permitted supports, and zero-end contact |
| 54–62 | The bilinear moments `M` and `Z` |
| 73–91 | Raw column interval and the integer binomial filter |
| 95–105 | The numbers `c_l` and the convention on inadmissible indices |
| 135–166 | The two period starts and `pi^2 = 6 zeta(2)` |
| 168–204 | Rational arrays and the exact two-period moment decomposition |
| 243–262 | Original cancellation `H_j-D_j=0` |
| 334–346 | The separate Chebyshev coefficient valuation input, which is **not** proved for the new rows |

To avoid confusing the target coefficients with the source parameters, write the proposed rational relation as

\[
\alpha G+\beta\pi^2=u,\qquad
\alpha,\beta,u\in\mathbb Q,\quad \alpha\ne0,
\qquad \mu=16\beta/\alpha.
\]

Write `b_0` for the source column offset and `C_0` for its row exponent. The source family is

\[
n=48N,\quad b_0=7N,\quad q=g=4N,\quad h=2N,
\quad L=59N,\quad C_0=63N,\quad H=65N,\quad A=19N,
\quad N\ge1.
\]

Throughout, `H_j(P)` is a coefficient functional; the undecorated `H` is the degree cutoff `65N`.

## 2. The coefficient at infinity and the coefficient at zero

For a polynomial `P(t)=sum_i p_i t^i`, put

\[
C_j(P)=\sum_i p_i c_{(i-j)/2},\qquad
H_j(P)=\sum_i p_i c_{(j-i-1)/2},\qquad
D_j=[t^j]D(t),
\]

where `c_z=0` unless `z` is a nonnegative integer, as in original line 105. Let

\[
\mathcal C(P)(t)
=\left[\frac{P(t)}{\sqrt{1-t^{-2}}}\right]_{\ge0,\,\infty}
=\sum_{j\ge0} C_j(P)t^j.
\]

Here the square root at infinity has constant term 1, and the brackets mean the nonnegative Laurent powers. This is a finite polynomial of degree at most `deg P`. Thus `C_j` is the infinity coefficient. In contrast, with the original Taylor branch `f(0)=1`,

\[
H_j(P)=[t^j]\frac{tP(t)}{f(t)},\qquad
f(t)=\sqrt{1-t^2}.
\]

Thus `H_j` is the zero-end Taylor coefficient. These two kernels are not interchangeable.

The exact source decomposition, lines 197–204, yields for every raw index

\[
\begin{aligned}
F_j(P,D)
&:=M(P,j)-\frac32 Z(D,j)\\
&=F_j^0(P,D)+4G C_j(P)
  +\frac{\pi^2}{4}\bigl(H_j(P)-D_j\bigr),
\end{aligned}
\]

where `F_j^0` is rational for rational `P,D`. Under the proposed relation this is

\[
F_j(P,D)=F_j^0(P,D)+\frac{4u}{\alpha}C_j(P)
 +\frac{\pi^2}{4}\bigl(H_j(P)-D_j-\mu C_j(P)\bigr).
\]

Consequently the proposed mixed condition is exactly

\[
\boxed{H_j(P)-D_j=16(\beta/\alpha)C_j(P).}
\]

It is sufficient to make that entry rational under the target relation. It is also necessary for rationality of that entry under the relation, using only the irrationality of `pi^2` and rationality of the displayed coefficients. This does **not** assert any already known independence of `1,G,pi^2`.

For all `0<=j<L`, the condition is the formal two-end contact

\[
\frac{tP(t)}{f(t)}-D(t)-\mu\mathcal C(P)(t)=O(t^L).
\]

For the actual raw interval it is only the projection to `b_0<=j<L` of this equation. The original condition is the specialization `mu=0`, not the mixed condition with a free adjustment at every coefficient.

## 3. The finite operator on the permitted support

First retain both the exact source support and its common endpoint factor. Define

\[
\begin{aligned}
V_h=\{(P,D):\;&P\in t^A(1-t)^h\mathbb Q[t],\quad
D\in t^{A+1}(1-t)^h\mathbb Q[t],\\
&\deg P,\deg D<H\}.
\end{aligned}
\]

Let

\[
M=H-A-h=44N.
\]

Then `P=t^A(1-t)^h Q`, with `deg Q<M`, while the corresponding polynomial multiplying `t^(A+1)(1-t)^h` in `D` has degree `<M-1`. Hence

\[
\dim_{\mathbb Q}V_h=M+(M-1)=88N-1.
\]

For the actual raw block define the explicit rational linear operator

\[
\mathcal L_\mu:V_h\longrightarrow\mathbb Q^{L-b_0},\qquad
(P,D)\longmapsto
\bigl(H_j(P)-D_j-\mu C_j(P)\bigr)_{b_0\le j<L}.
\]

In the monomial coefficient basis its entries are precisely the finite `c` kernels above and the negative coordinate selector on `D`. No infinite linear system is involved.

For every `j<=A`, permitted support gives

\[
H_j(P)=0,\qquad D_j=0.
\]

Therefore, if `mu != 0`, the first `A-b_0+1=12N+1` raw conditions force

\[
\boxed{C_j(P)=0\quad(b_0\le j\le A).}
\]

Those coefficients cannot be assigned by changing `D` while retaining the source support.

### Independence of the forbidden low-degree constraints

Let

\[
d\nu_e(x)=\frac{(1-x)^e}{\pi\sqrt{1-x^2}}\,dx,
\qquad -1<x<1,\quad e\in\mathbb Z_{\ge0}.
\]

The arcsine moments are

\[
\int_{-1}^1x^m\,d\nu_0(x)=c_{m/2},
\]

with the same convention on half-integer indices. For `j<=A`, all exponents below are nonnegative, and

\[
C_j\bigl(t^A(1-t)^h Q\bigr)
=\int_{-1}^1 x^{A-j}Q(x)\,d\nu_h(x).
\]

The low constraints are therefore the first `k=A-b_0+1=12N+1` ordinary moments of `Q` against the positive measure `nu_h`. Their Gram matrix is

\[
\Gamma_k^{(h)}=
\left(\int_{-1}^1x^{r+s}\,d\nu_h(x)\right)_{0\le r,s<k}.
\]

For a nonzero real polynomial `U` of degree `<k`,

\[
\int_{-1}^1 U(x)^2\,d\nu_h(x)>0.
\]

Thus the Gram matrix is positive definite and nonsingular. Its entries are rational, since each is the finite sum

\[
m^{(e)}_\ell:=\int x^\ell\,d\nu_e
=\sum_{v=0}^e(-1)^v\binom ev c_{(\ell+v)/2}.
\]

Because `M>=k`, the low-constraint operator has exact rank `12N+1` over `Q`; no parity assumption reduces that rank.

### Solving the remaining coordinates and the endpoint jets

Once `P` satisfies those low constraints, the remaining raw equations uniquely prescribe

\[
D_j=H_j(P)-\mu C_j(P),\qquad A+1\le j<L.
\]

Let `D_<L` be the polynomial consisting of these prescribed coefficients. The coordinates `L<=j<H` provide `H-L=6N` free variables before endpoint contact. A direct rational completion is

\[
\begin{aligned}
Y(t)&=-\operatorname{Tay}_{1,<h}\bigl(t^{-L}D_{<L}(t)\bigr),\\
D^{\rm sec}(t)&=D_{<L}(t)+t^L Y(t).
\end{aligned}
\]

Here `Tay_(1,<h)` is the Taylor polynomial at 1 of order `<h`. This gives a linear section: `D^sec` has the prescribed coefficients below `L`, is divisible by `(1-t)^h`, retains its lower support `A+1`, and has degree at most `L+h-1<H`. For `h=0`, take `Y=0`.

All homogeneous completions are exactly

\[
D^{\rm hom}(t)=t^L(1-t)^h E(t),\qquad
\deg E<H-L-h=4N.
\]

Therefore the endpoint jets have exact independent rank `h`, and there are `4N` remaining pure-`D` directions. Combining the two parts,

\[
\boxed{\dim\ker\mathcal L_\mu=(44N-(12N+1))+4N=36N-1
\quad(\mu\ne0).}
\]

Equivalently `rank L_mu = 52N = L-b_0`. In contrast, when `mu=0` all low equations are automatic. Its kernel has dimension

\[
\boxed{\dim\ker\mathcal L_0=44N+4N=48N,}
\]

and its rank is only `40N-1`.

## 4. A concrete smaller block with integer polynomial rows

The dimension count is constructive. For `k=12N+1` and every `d=k,...,M-1`, define

\[
Q_d(x)=x^d-\sum_{s=0}^{k-1}\eta_{s,d}x^s,
\qquad
(\eta_{s,d})_s=
\bigl(\Gamma_k^{(h)}\bigr)^{-1}
\bigl(m^{(h)}_{r+d}\bigr)_{0\le r<k}.
\]

Then `Q_d` has rational coefficients and all required low moments vanish. Distinct leading degrees show that these `32N-1` polynomials form a basis of the permitted `P` kernel. Set

\[
P_d=t^A(1-t)^hQ_d
\]

and use the section in the preceding paragraph to obtain `D_d`. Adjoin the `4N` pairs

\[
(0,\ t^{L+e}(1-t)^h),\qquad 0\le e<4N.
\]

These `36N-1` pairs form a rational basis of the raw mixed kernel. They have exactly the permitted degree bounds and lower supports, and retain both endpoint factors. Multiplying each pair by a nonzero integer clearing its finite coefficient denominators gives a basis over `Q` consisting of integral polynomial pairs. More intrinsically, the kernel intersected with the original integer coefficient lattice is a free abelian group of rank `36N-1`.

This supplies a concrete positive-dimensional family for the moment-alignment problem. The abstract Gram construction alone does not bound its inverse matrices; section 9 gives a more explicit Jacobi basis with exponential coefficient heights and dyadic integralization. Neither construction establishes that its moment determinant is nonzero, that the original two-adic/odd-prime estimates survive, or that the reduced row count has a favorable analytic-to-arithmetic balance. In particular, the original Chebyshev valuation lemma at source lines 334–346 does not automatically apply to these rows.

## 5. Filtered-only rationality: exact relaxation, still below 48N

The original filtered column indexed by `ell`, `0<=ell<n`, is the combination of raw columns with indices `b_0+ell+v`, `0<=v<=q`, and weights `(-1)^v binom(q,v)`. Define

\[
\widehat{\mathcal L}_\mu(P,D)_\ell
=\sum_{v=0}^q(-1)^v\binom qv
 \bigl(H_{b_0+\ell+v}(P)-D_{b_0+\ell+v}
       -\mu C_{b_0+\ell+v}(P)\bigr).
\]

This is `T^t L_mu` in the source filter notation. Requiring only this filtered vector to vanish is the precise weaker condition for rationality of all filtered entries under the target relation.

Let

\[
K=A-b_0-q=8N.
\]

For `0<=ell<=K`, every raw index entering that output is at most `A`. Hence neither `H_j` nor `D_j` contributes. Directly summing the low infinity coefficients gives

\[
\begin{aligned}
\sum_{v=0}^q(-1)^v\binom qv C_{b_0+\ell+v}(P)
&=\int x^{A-b_0-\ell-q}(x-1)^q Q(x)\,d\nu_h(x)\\
&=(-1)^q\int x^{K-\ell}Q(x)\,d\nu_{h+q}(x).
\end{aligned}
\]

Since `mu != 0`, the first `K+1=8N+1` filtered conditions have exact rank `8N+1`, by the same positive Gram proof, now with weight `nu_(h+q)`.

For `K+1<=ell<n`, put `j_ell=b_0+ell+q`. These indices run consecutively from `A+1` to `L-1`. The coefficient of `D_(j_ell)` in that output is `-(-1)^q`, and all other `D` indices are strictly smaller. Thus the remaining `40N-1` outputs solve for `D_(A+1),...,D_(L-1)` by an invertible triangular matrix. Explicitly, with `delta_j=H_j(P)-mu C_j(P)`, the recursion is

\[
D_{j_\ell}=(-1)^q\left[
 \sum_{v=0}^q(-1)^v\binom qv\delta_{b_0+\ell+v}
 -\sum_{v=0}^{q-1}(-1)^v\binom qv D_{b_0+\ell+v}
\right],
\]

where already prescribed low coefficients `D_j`, `j<=A`, are zero. Complete the endpoint jets by the same `t^L Y` section; the same `4N` pure-`D` directions remain.

Therefore

\[
\boxed{\dim\ker\widehat{\mathcal L}_\mu
=(44N-(8N+1))+4N=40N-1\quad(\mu\ne0),}
\]

and `rank Lhat_mu = 48N`. This is an exact relaxation by `q=4N` dimensions over the raw mixed kernel, rather than a speculative rank gain.

A symbolic integral basis is obtained by replacing `k` with `8N+1` and `nu_h` with `nu_(h+q)` in the Gram construction, then using the triangular `D` recursion and the endpoint section. Its `36N-1` nonzero-`P` directions plus `4N` pure-`D` directions give `40N-1` independent pairs after clearing denominators.

For `mu=0`, the first `8N+1` filtered equations are automatic. Moreover `H_j-D_j` is already zero for `j<=A`, so the invertible triangular matrix shows that filtered contact and raw contact are equivalent. Their common kernel has dimension `48N`.

## 6. The original rows are an entire basis of the old contact space

The original rows have the two factors and supports defining `V_h`, by source lines 40–48, and satisfy the old contact, by lines 49–52. They are linearly independent as polynomial pairs: from the original definitions,

\[
R_r=P_r-\frac{f}{t}D_r
=(1-t)^h t^{C_0-1}w^{r-g}.
\]

If a rational linear combination of the pairs is zero, the same combination of these `R_r` is zero. Dividing their common nonzero factor leaves a finite linear combination of distinct Laurent monomials in `w`. All coefficients vanish. Thus the `48N` original pairs are independent and, by the old-space dimension in section 3, form a basis of that entire old contact space.

This identifies a genuine dimension change, rather than merely a defective choice of the original basis. Under nonzero `beta`, keeping the old degree supports and endpoint factors gives at most `36N-1` independent pairs for raw mixed contact and at most `40N-1` for filtered-only mixed contact. Any proposed `48N` rows in either space are rationally dependent as polynomial pairs. Bilinearity of `M,Z` makes that dependence a dependence of their moment rows for every column choice; a `48N` square determinant is therefore zero.

This excludes direct reuse of the original 48N-row architecture with those supports and factors. It does not exclude reducing the row number, changing the degree cutoffs or endpoint orders, changing the proportional parameter family, or a different moment construction.

## 7. Why the advertised trivial D adjustment fails

For an old row, `H_j(P)-D_j=0` in the contact range. Formally one could propose

\[
D^{\rm new}_j=D^{\rm old}_j-\mu C_j(P).
\]

In the interval `b_0<=j<=A`, however, this assigns prohibited coefficients of `D`. It is permitted there only if the independent moment constraints `C_j(P)=0` already hold. Clearing denominators cannot remove a nonzero prohibited coefficient. A high-degree tail can repair the endpoint jets, but cannot repair these low support violations.

There is a direct witness among the original rows. Take `r=g`, which is an allowed row index. Original lines 40–43 give

\[
P_g=(1-t)^{2N}t^{63N-1},\qquad D_g=0.
\]

The forbidden raw index `j=A=19N` has

\[
\begin{aligned}
C_A(P_g)
&=\sum_{v=0}^{2N}(-1)^v\binom{2N}{v}
 c_{(44N-1+v)/2}\\
&=-\sum_{\ell=0}^{N-1}\binom{2N}{2\ell+1}c_{22N+\ell}<0.
\end{aligned}
\]

All surviving terms are strictly positive before the minus sign. Thus for every `N>=1` and every nonzero `mu`, the proposed adjustment requires

\[
D_A^{\rm new}=-\mu C_A(P_g)\ne0,
\]

contradicting the exact source support `supp D subset {A+1,...,H-1}`. This is an exact symbolic obstruction, not a finite numerical check.

Also, if one merely recombines original pairs while retaining their original `D`, old contact remains `H-D=0`. Mixed raw contact would then require all corresponding raw `C_j` to vanish, killing the very `G` coefficient being aligned. The viable smaller construction changes the pair design, not just the original row basis.

## 8. Dimension ledger and limits of the result

The same proofs work if the common factor `(1-t)^h` is dropped, setting `h=0` only in the definition of the row space. The filter order remains the original `q=4N`. Requiring full contact `0<=j<L` replaces the forbidden low block by `A+1=19N+1` independent moments. The exact ledger is:

| Row condition | `mu=0`, no endpoint factor | `mu!=0`, no endpoint factor | `mu=0`, original endpoint factor | `mu!=0`, original endpoint factor |
|---|---:|---:|---:|---:|
| Raw block `b_0<=j<L` | `52N` | `40N-1` | `48N` | `36N-1` |
| Filtered columns only | `52N` | `44N-1` | `48N` | `40N-1` |
| Full contact `0<=j<L` | `52N` | `33N-1` | `48N` | `29N-1` |

Every listed nonzero-`mu` space has a rational basis consisting, after clearing denominators, of integer polynomial pairs. The amplitude of nonzero `mu` changes the section for `D`, but not the rank or dimension. The rank jumps precisely at `mu=0` because the low constraints on `P` disappear there.

The concrete new input so far is a smaller, fully specified mixed two-end contact kernel, together with an exact obstruction to retaining the original 48N-row architecture. Sections 9–10 add an explicit integral sublattice with exponential coefficient heights and a consistent reduced square size. Exact determinant valuations, determinant nonvanishing, and the final irrationality argument are additional tasks; positive-dimensional contact alone does not pay them.

## 9. Explicit Jacobi rows: dyadic integralization and exponential heights

The Gram inverse can be avoided. For an integer `e>=0`, define

\[
\mathsf J_d^{(e)}(x)=P_d^{(e-1/2,-1/2)}(x)
=2^{-d}\sum_{v=0}^d
 \binom{d+e-1/2}{v}\binom{d-1/2}{d-v}
 (x-1)^{d-v}(x+1)^v.
\]

This is the specialization of the primary [DLMF finite binomial formula 18.5.8](https://dlmf.nist.gov/18.5#E8). The [Jacobi orthogonality entry](https://dlmf.nist.gov/18.3#T1) has weight `(1-x)^(e-1/2)(1+x)^(-1/2)`; multiplying that weight times `dx` by `1/pi` gives precisely `nu_e`. Equivalently its Rodrigues numerator is `(1-x)^(d+e-1/2)(1+x)^(d-1/2)`; integration by parts `d` times gives orthogonality to every polynomial of degree `<d`. The relevant derivatives vanish at both endpoints. Thus no period independence conjecture is needed for this basis.

For filtered contact take `e=h+q=6N` and

\[
d=8N+1,\ldots,44N-1.
\]

These `36N-1` Jacobi polynomials are a basis of the permitted `Q` kernel: each is orthogonal to degrees `0,...,8N`, and their distinct nonzero leading coefficients give independence. For raw contact the corresponding choice is `e=h=2N` and `d=12N+1,...,44N-1`.

### Dyadic coefficients and an elementary height bound

For every integer `s>=0` and `j>=0`, expansion of `(1+z)^s(1+z)^(-1/2)` gives

\[
\binom{s-1/2}{j}
=\sum_{r=0}^{\min(s,j)}\binom sr(-1)^{j-r}c_{j-r}.
\]

Hence `4^j binom(s-1/2,j)` is an integer. Applying this to the two binomials in the finite formula proves

\[
\boxed{8^d\mathsf J_d^{(e)}\in\mathbb Z[x].}
\]

All the binomial factors in that formula are positive for `0<=v<=d` and `d>=1`. Since `||(x-1)^(d-v)(x+1)^v||_1<=2^d`, Vandermonde's identity gives

\[
\begin{aligned}
\|8^d\mathsf J_d^{(e)}\|_1
&\le8^d\binom{2d+e-1}{d}\\
&\le8^d\binom{2d+e}{d}
\le2^{5d+e}.
\end{aligned}
\]

Consequently

\[
\widetilde P_d(t)=t^A(1-t)^h8^d\mathsf J_d^{(e)}(t)
\in\mathbb Z[t],\qquad
\|\widetilde P_d\|_1\le2^{5d+e+h}.
\]

All bounds in this and the following two paragraphs are derived here from the finite formulas; they are not claims made by the original Catalan source.

### One common dyadic clearing factor for the original block

For `A<=i<H` and `b_0<=j<L`, the largest admissible integer index in the `C` kernel is

\[
\left\lfloor\frac{H-1-b_0}{2}\right\rfloor=29N-1.
\]

The largest index in the `H` kernel is `20N-1`. Since `c_l` has denominator dividing `4^l`, the common integer

\[
2^{58N-2}
\]

clears both coefficient kernels on that raw block. Let `d_mu` be a positive integer with `d_mu mu` integral. Choose

\[
P_d^\#=d_\mu\,2^{58N-2}\widetilde P_d.
\]

Then every `delta_j=H_j(P_d^#)-mu C_j(P_d^#)` with `b_0<=j<L` is an integer. This uses only a fixed denominator from `mu` and a power of 2 depending linearly on `N`; it does not assert clearing of the infinite `H_j` tail outside that block.

### The filtered D recursion introduces no further denominators

Put `m=L-A-1=40N-1`, `ell(u)=K+1+u`, and

\[
\Delta_u=\sum_{v=0}^q(-1)^v\binom qv
 \delta_{b_0+\ell(u)+v},\qquad
d_u=D_{A+1+u},\quad 0\le u<m.
\]

The triangular equations in section 5 become

\[
(1-z)^q\sum_{u=0}^{m-1}d_u z^u
\equiv(-1)^q\sum_{u=0}^{m-1}\Delta_u z^u\pmod{z^m}.
\]

The inverse coefficients are the integers `binom(q+r-1,r)`. Thus all prescribed `D_j`, `A+1<=j<L`, are integers. Writing `||.||_1` for the sum of absolute polynomial coefficients, the elementary bounds `0<c_l<=1` and

\[
\sum_{r=0}^{m-1}\binom{q+r-1}{r}
=\binom{q+m-1}{m-1}\le2^{q+m-1}
\]

give

\[
\max_{u<m}|d_u|
\le (1+|\mu|)2^{2q+m-1}\|P_d^\#\|_1.
\]

For an integral endpoint completion, the section at zero is particularly convenient:

\[
D^{\#}(t)=t^{A+1}(1-t)^h
\operatorname{trunc}_{<m}\left(
\frac{t^{-(A+1)}D_{<L}(t)}{(1-t)^h}\right).
\]

The inverse coefficients `binom(h+r-1,r)` are integers. This section has the required coefficients below `L`, the common endpoint factor, lower support `A+1`, and degree at most `L+h-1<H`. Its coefficient bound is

\[
\|D^{\#}\|_1\le2^{2h+m-1}\|D_{<L}\|_1
\le m(1+|\mu|)2^{2q+2h+2m-2}\|P_d^\#\|_1.
\]

Every exponent here is `O(N)`, with `mu` fixed. Pure-`D` rows `t^(L+r)(1-t)^h` have norm at most `2^h`. Therefore the full filtered kernel has an explicitly defined full-rank integral sublattice with coefficient heights `exp(O_mu(N))`. The raw kernel has the same property, using its Jacobi range and the direct, unfiltered prescription for `D_j`.

This is stronger than merely clearing arbitrary Gram determinants. It does not assert a primitive basis of the entire integer lattice, an index bound, the original coefficient valuation profile, favorable determinant valuations, a small enough analytic upper bound, or determinant nonvanishing.

## 10. A consistent reduced square size and a 44N-dimensional row pool

A reduced square determinant must reduce its column count as well as its row count. Retain `b_0=7N,q=4N,H=65N,A=19N,h=2N`, but choose a new filtered column count `n'`. Its raw endpoint is

\[
L'=b_0+n'+q.
\]

For

\[
8N+1<n'\le52N,
\]

the first `8N+1` filtered equations are the same positive moment constraints as before. The remaining

\[
m'=L'-A-1=n'-(8N+1)
\]

equations solve the low `D` coefficients by the same triangular operator. The assumption `n'<=52N` is precisely `L'+h<=H`, ensuring sufficient tail room for the endpoint factor. The homogeneous endpoint tail has dimension

\[
H-L'-h=52N-n'.
\]

Thus on the same ambient space `V_h`, for every nonzero `mu`, the filtered operator with `n'` outputs has exact rank `n'`, and

\[
\boxed{\dim\ker\widehat{\mathcal L}_{\mu,n'}
=(36N-1)+(52N-n')=88N-1-n'.}
\]

A necessary and, at the polynomial-pair level, sufficient condition to select `n'` independent aligned pairs is

\[
n'\le88N-1-n',\quad\text{equivalently}\quad n'\le44N-1.
\]

In particular choose

\[
\boxed{n'=44N-1,\qquad L'=55N-1.}
\]

The row pool then has dimension exactly `44N`: it consists of the `36N-1` Jacobi nonzero-`P` directions and `8N+1` pure-`D` directions. An explicit independent set of `44N-1` integral pairs is obtained by taking all the Jacobi directions with their new triangular/endpoint `D` sections, and only the first `8N` pure-`D` rows

\[
(0,t^{L'+r}(1-t)^h),\qquad 0\le r<8N.
\]

Use the same `d_mu 2^(58N-2)` clearing factor on the Jacobi rows. Since `L'<L`, the dyadic-kernel bound above still holds; the recursion and endpoint estimates hold with `m'` in place of `m`. All of these pairs have the original exact lower supports and degree cutoff, retain `(1-t)^h`, satisfy the new filtered mixed contact, and have coefficient heights `exp(O_mu(N))`.

This is an actual self-consistent integer row construction for a reduced square size, rather than placing 40N rows under 48N different filtered constraints. It leaves the principal remaining issue explicit: independence of polynomial pairs does not establish nonvanishing of their actual moment determinant. The determinant's analytic size and prime valuations must also be proved anew. No claim about `G`, or about a nontrivial rational relation with `pi^2`, follows from this construction alone.
