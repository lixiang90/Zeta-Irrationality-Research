# Reduced mixed Jacobi moments: all finite places and joint column savings

2026-10-07. New isolated paper derivation. No historical producer, prime scan, numerical determinant experiment, main edit, or manifest edit was run. The input construction is the complete ten-section `catalan_mixed_two_end_contact_support_lemma_20261007.md`; the original `foundations.tex` lines 1--263 and complete `odd-primes.tex` were actually read. The moment formulas and their digit calculation are used below. The original Chebyshev coefficient valuation lemma and original two-adic determinant certificate are not used.

## 1. The actual conditional matrix

Fix rational target coefficients

\[
aG+b\pi^2=u,\qquad a\ne0,\quad b\ne0,
\qquad \mu=16b/a,\quad \gamma=4u/a.
\tag{J1}
\]

Take the precise reduced construction

\[
n=44N-1,\quad B=7N,\quad q=4N,\quad h=2N,
\quad A=19N,\quad H=65N,\quad L=B+n+q=55N-1.
\tag{J2}
\]

Here `B` is the column offset, not Catalan's constant. Let `d_mu` and `d_gamma` be fixed positive integers such that `d_mu mu` and `d_gamma gamma` are integers. The `36N-1` nonzero-`P` rows are indexed by

\[
d=8N+1,\ldots,44N-1,
\qquad
P_d^{\rm old}=d_\mu 2^{58N-2}8^d
 t^A(1-t)^h P_d^{(6N-1/2,-1/2)}(t).
\tag{J3}
\]

Their `D` rows are the integral triangular and endpoint sections in the input note, with the new endpoint `L`. Adjoin the `8N` pure-`D` rows `(0,t^{L+r}(1-t)^h)`, `0<=r<8N`. All rows have integer coefficients, `P` support in `[A,H-1]`, `D` support in `[A+1,H-1]`, and the filtered mixed contact.

For each raw index `B<=j<L`, define a rational column, regardless of the truth of the target relation, by

\[
\widetilde E_j(P,D)
 =\sum_iP_iM^0(i,j)-\frac32\sum_iD_iZ^0(i,j)
       +\gamma C_j(P),
\quad C_j(P)=\sum_iP_i c_{(i-j)/2}.
\tag{J4}
\]

Write `T` for the integer binomial filter with `T_(j,k)=(-1)^(j-B-k) binom(q,j-B-k)`, `0<=k<n`. The actual filtered moment matrix is, under J1,

\[
E=\widetilde E T.
\tag{J5}
\]

Indeed the coefficient of `pi^2/4` in that matrix is exactly the filtered vector `H(P)-D-mu C(P)`, which vanishes. Raw J4 need not equal the raw original moment under J1; only the filtered equality J5 is asserted. Every determinant assertion below is valid for the rational determinant of J5, including when it is zero.

## 2. A stronger integral Jacobi normalization

For every integer `e>=0`, let `J_d=P_d^(e-1/2,-1/2)`. Its finite binomial formula gives the formal coefficient identity

\[
J_d(x)=[z^d]
 (1+(x+1)z/2)^{d+e-1/2}
 (1+(x-1)z/2)^{d-1/2}.
\]

Replacing `z` by `4z`, and putting `U=xz+(x^2-1)z^2`, gives

\[
4^dJ_d(x)=[z^d](1+4U)^{d-1/2}
                        (1+2(x+1)z)^e.
\tag{J6}
\]

Both integer powers in this expression have integral coefficients, and

\[
(1+4U)^{-1/2}
 =\sum_{k\ge0}(-1)^k\binom{2k}{k}U^k
 \in\mathbb Z[x][[z]].
\]

Thus

\[
\boxed{4^dJ_d\in\mathbb Z[x].}
\tag{J7}
\]

This is a paper proof for every degree and every nonnegative integral `e`; it is not extrapolated from finite examples. The same positive finite-sum bound as in the input note yields

\[
\|4^dJ_d\|_1
 \le4^d\binom{2d+e-1}{d}\le2^{4d+e}
 \qquad(d\ge1).
\tag{J8}
\]

From this point onward the row parameter is `e=6N`, as in J3.

## 3. The row-specific dyadic section and its exact scalar

For the row of degree `d`, `deg P<=21N+d`. On the raw block J2, the largest dyadic exponent needed in the `C` kernel is

\[
2\left\lfloor\frac{21N+d-B}{2}\right\rfloor
 =14N+d-(d\bmod2).
\]

The largest exponent in the `H` kernel is

\[
2\left\lfloor\frac{L-1-A-1}{2}\right\rfloor
 =36N-4.
\]

Since `c_l=4^(-l) binom(2l,l)`, put

\[
s_d=\max\{14N+d-(d\bmod2),\ 36N-4\},
\quad
P_d^{\rm red}=d_\mu2^{s_d}4^d
             t^A(1-t)^hJ_d(t).
\tag{J9}
\]

Every `H_j(P_red)-mu C_j(P_red)` on `B<=j<L` is an integer. The inverse filter has coefficients `binom(q+r-1,r)`; the endpoint inverse has coefficients `binom(h+r-1,r)`. Applying these same two linear sections therefore gives an integer `D_d^red`. It has the same support, endpoint factor and filtered mixed contact.

Linearity of both sections gives the exact row identities

\[
(P_d^{\rm old},D_d^{\rm old})
 =2^{g_d}(P_d^{\rm red},D_d^{\rm red}),
\quad g_d=d+58N-2-s_d\ge0.
\tag{J10}
\]

Pure-`D` rows are unchanged. Consequently

\[
\det E^{\rm old}=2^{G_N}\det E^{\rm red},
\quad
G_N=\sum_{d=8N+1}^{44N-1}g_d
    =1486N^2-42N-6.
\tag{J11}
\]

For the exact sum, `s_d=36N-4` for `8N+1<=d<=22N-3`, giving `(14N-3)(37N+1)`; the remaining `22N+2` degrees give `(22N+2)(44N-2)+(11N+1)`. Their sum is J11. In particular this positive dyadic content is an actual scalar of the moment rows and determinant. It is not an inference from the sizes of polynomial coefficients. Both old and red rows have `exp(O_mu(N))` coefficient heights.

## 4. Odd-prime caps, including every prime power

Put `Lambda_H=lcm(1,...,H)` and `alpha_p=v_p(Lambda_H)`. For odd `p`, the factorial-floor formula gives, for even positive `z<=H`,

\[
v_p\left(z\binom z{z/2}\right)\le\alpha_p;
\]

and for odd positive `z<=H`,

\[
v_p\left(z\binom{z-1}{(z-1)/2}\right)\le\alpha_p.
\tag{J12}
\]

Here is the all-power proof. Write `s=v_p(z)`. At every level `p^r` with `r<=s`, the carry for the even case is zero because `z/2=0 mod p^r`. In the odd case the low digits of `(z-1)/2` equal `(p^r-1)/2`, again giving no carry. At every remaining level there is at most one carry. There are at most `alpha_p-s` remaining levels. Adding the external valuation `s` proves J12. Levels beyond `H` contribute zero. Thus this calculation does not discard small primes or higher powers.

The original explicit arrays are

\[
H_z^*=\begin{cases}c_{z/2}&z\text{ even},\\
1/(z c_{(z-1)/2})&z\text{ odd},\end{cases}
\quad m_{z-1}=2H_z^*\ (z\text{ odd}),
\]

\[
k^-_u=\begin{cases}
H_u^*\sum_{1\le z\le u,\ z\text{ even}}2/(z^2(H_z^*)^2)&u\text{ even},\\
H_u^*\sum_{1\le z\le u,\ z\text{ odd}}2/z&u\text{ odd},
\end{cases}
\quad
k^+_{u+1}=H_u^*\sum_{1\le z\le u,\ z\equiv u\ (2)}
                         2/(z^2H_z^*).
\tag{J13}
\]

Their zero-start and empty-sum conventions are those of the original source. J12 shows `v_p(H_z^*)>=-alpha_p` for odd `z`, while even `H_z^*` is integral. For even `z`, `v_p(zH_z^*)<=alpha_p`.

Each summand in even `k^-` consequently has depth at most `2alpha_p`. In odd `k^-`, the two factors have depth at most `alpha_p` each. In even-`u` `k^+`, `2v_p(z)+v_p(H_z^*)<=2alpha_p`; in odd-`u` `k^+`, use `1/(z^2H_z^*)=c_((z-1)/2)/z`, with depth at most `alpha_p`, and the prefactor has depth at most `alpha_p`. Thus both starting arrays have depth at most `2alpha_p`.

The diagonal reduction of `M^0(i,j)` subtracts only terms `m_v/k`, with `v+1,k<=H`; each has depth at most `2alpha_p`. Finally `Z^0(i,i)=-sum_(k<=i)1/k^2`, and off the diagonal `Z^0(i,j)=(B_i^(1)-B_j^(1))/(i-j)`; both have the same bound. For all indices used here,

\[
v_p(M^0(i,j)),v_p(Z^0(i,j))\ge-2\alpha_p.
\tag{J14}
\]

All `C_j` kernels are integral at odd primes. Integer polynomial rows and integer filters therefore preserve J14, with only the fixed possible loss `v_p(d_gamma)` from `gamma`.

## 5. The prime 2 and a complete entry cap

Write `s_2(l)` for the binary digit sum and `eta(l)=2l-s_2(l)`. Then

\[
v_2(c_l)=-\eta(l),\qquad
v_2(H_{2l+1}^*)=\eta(l)\ge0.
\tag{J15}
\]

The function `eta` is nondecreasing, since its increment is `2-(s_2(l+1)-s_2(l))>=1`. For `l>=1`, it also satisfies

\[
\eta(l)\ge1+v_2(l),\qquad
\eta(l)\ge1+2v_2(l).
\]

For the second bound write `l=2^t m` with odd `m`, and use `eta(l)>= (2^(t+1)-1)m>=1+2t`; this also proves the first. Therefore the inner sums in even `k^-` and even-`u` `k^+` in J13 are integral at 2: their summand valuations are respectively `1+2eta(l)-2v_2(2l)>=1` and `1+eta(l)-2v_2(2l)>=0`. Their prefactors have valuation at least `-u`. Odd `k^-` is integral. For odd-`u` `k^+`, each ratio `H_u^*/H_z^*` with odd `z<=u` is integral by monotonicity of `eta`, so that array is integral as well.

The only possible linear dyadic loss in a starting array is consequently at most `i-j` when that nonnegative difference is even, or at most `j-i-1` when that nonnegative difference is even. For a degree-`d` row these are bounded respectively by the two quantities whose maximum is `s_d` in J9. The factor `2^s_d` clears them. Moreover every nonzero `m_v` is integral at 2 by J15; the diagonal terms `m_v/k` are cleared by `Lambda_H`. The `Z^0` harmonic formulas are cleared by `Lambda_H^2`.

Since `C_j(P_red)` is an integer on the block, all terms of J4 are now cleared at 2 by `2d_gamma Lambda_H^2`; the extra factor 2 covers `3/2`. Combining with J14 proves the exact global statement

\[
\boxed{2d_\gamma\Lambda_H^2 E^{\rm red}\in
             \operatorname{Mat}_n(\mathbb Z).}
\tag{J16}
\]

The same cap holds for the old matrix. Its determinant has the stronger bound

\[
v_2(\det E^{\rm old})\ge
G_N-n\{2v_2(\Lambda_H)+1+v_2(d_\gamma)\}.
\tag{J17}
\]

J16 is a complete cap for all finite primes and all powers, not only the primes in the following large-prime argument. It also covers the pure-`D` rows, whose `P` is zero. In particular no new unaccounted prime comes from Jacobi denominators, `mu`, either integer section, or the dyadic kernels. The fixed factor from `mu` is already included in the actual rows.

## 6. The actual large-prime digit layer

Let `2sqrt(H)<p<=H` be odd with `p` not dividing `d_gamma`. Then `H<p^2/4`, and put

\[
Q(t)=(1-t^2)^{(p-1)/2}=\sum_{r=0}^{p-1}Q_rt^r
                         \in\mathbb F_p[t].
\]

The elementary digit calculation in the original rational moment arrays gives, for `0<=i,j<H`,

\[
\ell=j\bmod p,\quad r=(j-i-1)\bmod p,
\quad i'=(i+1+r-\ell)/p-1,\quad j'=\lfloor j/p\rfloor,
\]

\[
p^2M^0(i,j)\equiv Q_r M^0(i',j')\pmod p,
\quad
p^2Z^0(i,j)\equiv
\begin{cases}Z^0(\lfloor i/p\rfloor,j')&i=j\pmod p,\\0&\text{otherwise}.
\end{cases}
\tag{J18}
\]

The boundary convention is `M^0(-1,j')=k^+_(j'+1)`. These are locally integral congruences. For clarity, the calculation uses only J13 and the moment reduction, not row coefficients: if `z=Pp+r`, even `H_z^*` reduces to `H_P^*c_(r/2)` when `r` is even and has valuation one when `r` is odd; odd `H_z^*` has integral reciprocal and `pH_z^*` reduces to `(-1)^((p-1)/2)c_(r/2)H_P^*` when `r` is even and to zero otherwise. In even `k^-`, the nonzero terms group into complete blocks `z=mp-lambda`, with even `m` and `lambda=0,2,...,p-1`. Their sum uses

\[
\sum_{r=0}^{(p-1)/2}c_r^2
 \equiv\binom{p-1}{(p-1)/2}\equiv(-1)^{(p-1)/2}\pmod p.
\]

For odd `k^-` and both parities of `k^+`, only multiples of `p` survive after the stated scaling. Substituting these starting reductions and `pm_(z-1)=Q_(p-1-r)m_(P-1)` into diagonal reduction proves J18. The `Z^0` part follows directly by retaining multiples of `p` in the harmonic sums. The reduced indices are below `p/4` (the boundary index is below `p`), so their rational arrays are locally integral. This is the finite digit proof re-used at the moment-kernel level, where its hypotheses still hold.

Gathering rows, for each residue `ell`, put

\[
P'_u=[t^{(u+1)p+\ell}]\,tP(t)Q(t),\qquad
D'_u=[t^{up+\ell}]\,D(t).
\]

Then

\[
X_{kp+\ell}:=p^2\widetilde E_{kp+\ell}\bmod p
 =\sum_{u\ge-1}P'_uM^0(u,k)
   -\frac32\sum_{u\ge0}D'_uZ^0(u,k).
\tag{J19}
\]

The added `gamma C` term is integral at this odd prime and disappears. Thus J19 is valid for the present mixed rational matrix without raw contact and without assuming a nonzero leading packet for any Jacobi row.

If `ell>=H-2p`, degree bounds kill all extracted indices `u>1`. The small moment arrays give

\[
X_\ell=V_\ell,\qquad X_{p+\ell}=U_\ell-V_\ell,
\quad V_\ell=2P'_1-\tfrac32D'_1,
\quad U_\ell=2P'_{-1}-\tfrac32D'_0.
\tag{J20}
\]

Support gives `U_ell=0` for `ell<=A`. All leading vectors may vanish or be dependent; the deductions below only improve in that event.

## 7. Integral joint column elimination

For `2sqrt(H)<p<=H/2`, replace each high raw column by the sum of the pair indexed by

\[
\max(B,H-2p)\le\ell<\min(p,L-p,A).
\]

There are exactly

\[
d_0=(\min(p,L-p,A)-\max(B,H-2p))_+
\tag{J21}
\]

disjoint pairs. By J20 their sums have depth at most one; all other columns have depth at most two. The raw pool has `n+q` columns, so every choice of `n` columns contains at least `(d_0-q)_+` improved columns. Therefore

\[
v_p(\det E)\ge-2n+(d_0-q)_+.
\tag{J22}
\]

For `H/2<p<=H`, put `K=L-p`, `J=H-p`, and

\[
R=K_++(K-A)_++(J-\max(B,K))_+,
\]
\[
S=(\min(A,K)-B)_+
          +(\min(B,J)-\max(0,K))_+.
\tag{J23}
\]

Here is the full elimination, including empty ranges. Noncentral columns are the high columns with `0<=ell<K` and low columns with `B<=ell<J`. Pairing `B<=ell<min(A,K)` retains the low column and changes the high one to a depth-one sum. If `B_0=(min(A,K)-B)_+`, the number of retained depth-two columns is

\[
R_0=K_++(J-B)_+-B_0=R.
\]

The equality follows by the four cases `K<=0`, `0<K<=B`, `B<K<=A`, `K>A`, using `K<J`. Retained low columns represent `V_ell` for `B<=ell<J`; unpaired high columns represent `-V_ell` for `0<=ell<min(B,K)`, since `B<A`. The unrepresented set is exactly

\[
\mathcal U=\{\ell:\max(0,K)\le\ell<\min(B,J)\},
\quad e_0=|\mathcal U|.
\]

Central columns have `B<=j<min(p,L)` and `j>=J`. Direct diagonal reduction gives

\[
p\widetilde E_j\in\mathbb Z_p^n,
\qquad p\widetilde E_j\equiv
       -\sum_{0\le\ell<J}\frac{V_\ell}{j-\ell}\pmod p.
\tag{J24}
\]

Indeed `|i-j|<p` makes the starting arrays integral; the scaled moment summands can survive only for `p<=i-ell<2p`, producing `2P'_1`. The harmonic term can survive only at `i=p+ell`, producing `-3D'_1/2`. All denominators `j-ell` are units. Again `gamma C` is integral and disappears at this scale.

For each represented `V_ell`, choose a retained column `Y_ell` with `p^2Y_ell=±V_ell mod p`. Add an integral multiple of `pY_ell` to each central column to cancel that vector in J24. These changes are integral shears with integral inverses. The remaining central depth-one residues lie in the span of the `e_0` exceptional vectors. Choose a basis modulo `p` with its kernel last and lift it to `GL_c(Z_p)` on the central columns. At most `e_0` of them can then retain depth one; all the others become integral. Together with the `B_0` pair sums there are at most `S=B_0+e_0` depth-one columns, `R` depth-two columns, and integral remaining columns.

If a full minor uses `r` depth-two and `s` depth-one columns, its loss `2r+s` is bounded by each of `2n`, `n+R`, and `2R+S`. Hence

\[
v_p(\det E)\ge-\min(2n,n+R,2R+S).
\tag{J25}
\]

All operations occur in the entire raw pool. Cauchy--Binet with the integral inverse changes, followed by the prescribed integer filter `T`, transfers J22/J25 to J5. No column is discarded and no determinant nonvanishing is presumed.

## 8. An exact finite-N denominator model

For every prime let `alpha_p=v_p(Lambda_H)`. Define the nonnegative integer loss bound

\[
V_p=\begin{cases}
n(2\alpha_p+v_p(2d_\gamma)),
 &p=2\text{ or }p\le2\sqrt H\text{ or }p\mid d_\gamma,\\
2n-(d_0-q)_+,&2\sqrt H<p\le H/2,\ p\nmid d_\gamma,\\
\min(2n,n+R,2R+S),&H/2<p\le H,\ p\nmid d_\gamma,\\
0,&p>H,\ p\nmid2d_\gamma.
\end{cases}
\tag{J26}
\]

This covers every prime without asymptotic exceptions. The product `D_N=prod_p p^V_p` is finite, explicitly defined from J2/J21/J23, and

\[
D_N\det E^{\rm red}\in\mathbb Z,
\qquad
2^{-G_N}D_N\det E^{\rm old}\in\mathbb Z.
\tag{J27}
\]

For a zero determinant these remain true. For a nonzero determinant they give concrete lower bounds for its absolute value. The global, simpler alternative from J16 is `(2d_gamma Lambda_H^2)^n det E_red in Z`. Fixed `mu` and `gamma` affect this model through the stated integral row definitions and fixed `d_gamma`; there is no unmentioned coefficient-dependent prime exceptional set.

## 9. The asymptotic joint-column cost and floor errors

Put `x=p/N`. Each count in J21/J23 is a positive part, minimum or maximum of affine expressions in the integer parameters. These operations are 1-Lipschitz in their inputs. Replacing `n=44N-1` by `44N` and `L=55N-1` by `55N` therefore changes each count and loss by an absolute constant, uniformly over `p,N`. This explicitly accounts for the offset and floors; it is not an exact finite-N table being presented as homogeneous.

For `x<=65/2`, `d_0/N` has limiting value zero through `23`, `2x-46` from `23` to `29`, and `12` from `29` to `65/2`. For `x>65/2`, the limiting pairs `(R/N,S/N)` are

| Interval | R/N | S/N |
|---|---:|---:|
| `[65/2,36]` | `101-2x` | `12` |
| `[36,48]` | `65-x` | `48-x` |
| `[48,55]` | `113-2x` | `x-48` |
| `[55,58]` | `58-x` | `7` |
| `[58,65]` | `0` | `65-x` |

In particular `p>=L` does not eliminate every noncentral column in the new family: for `55N` to `58N` the low columns remain. Combining the minima gives the continuous limiting loss

| Interval | d(x) | Integral |
|---|---:|---:|
| `[0,25]` | `88` | `2200` |
| `[25,29]` | `138-2x` | `336` |
| `[29,65/2]` | `80` | `280` |
| `[65/2,69/2]` | `145-2x` | `156` |
| `[69/2,36]` | `214-4x` | `219/2` |
| `[36,55]` | `178-3x` | `1577/2` |
| `[55,58]` | `123-2x` | `30` |
| `[58,65]` | `65-x` | `49/2` |

The function is zero beyond `65`, and

\[
\int_0^{65}d(x)\,dx=7849/2.
\tag{J28}
\]

Small primes, including all their powers, contribute only `o(N^2)`: J16 gives a weighted loss at most `2n` times the sum of `alpha_p log p` over `p<=2sqrt H`, which is `O(n sqrt H log H)`. The fixed denominator contributes at most `n log(2d_gamma)=O(N)`. The prime 2 contributes `O(N log N)` for the red matrix. The uniformly bounded count error above contributes `O(theta(H))=O(N)` using the prime number theorem; even the elementary bound `O(N log N)` would suffice.

The standard weighted consequence of `theta(y)~y` gives

\[
N^{-1}\sum_{p\le H}d(p/N)\log p
  \longrightarrow\int_0^{65}d(x)\,dx.
\]

It follows by bounding the continuous `d` between upper and lower step functions on a fixed partition and then refining the partition. Along any sequence for which the rational determinant is nonzero,

\[
\boxed{\liminf\frac{\log|\det E^{\rm red}|}{n^2}
   \ge-\frac{7849}{3872}.}
\tag{J29}
\]

For the exact old normalization J3, J11 gives instead

\[
\boxed{\liminf\frac{\log|\det E^{\rm old}|}{n^2}
   \ge-\frac{7849}{3872}
           +\frac{743}{968}\log2.}
\tag{J30}
\]

The uniform entry cap alone would give odd cost `65/22`; J29 is the smaller safe cost obtained from the actual joint column lattice. Neither value is asserted optimal.

## 10. Exact scope

The results are complete safe entry caps, exact finite-N determinant denominator bounds, an explicit beneficial dyadic row scalar, and a joint column improvement for the actual mixed moment matrix. The proofs use the actual support, integer sections and rational moment kernels. They allow Jacobi leading packets to vanish; no universal nonzero `p^2` template is claimed. Further odd-prime row contents or Jacobi structure may improve the safe bound.

No argument here proves that the moment determinant is nonzero, that the chosen integer rows generate the full primitive contact lattice, that the real-place determinant upper bound is sufficiently small, or that the target relation is impossible. Those remain separate mathematical questions. The positive dyadic term in J30 belongs to the old normalization and must be accompanied by its identical scalar in any real-place comparison; J29 is the consistent statement for the reduced normalization.
