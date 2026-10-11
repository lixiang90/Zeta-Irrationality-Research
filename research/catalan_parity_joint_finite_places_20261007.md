# Parity q=0 mixed moments: joint columns and explicit row content

2026-10-07, round 216. NEW symbolic note, conditional on actual determinant nonzero. No producer, validator, coefficient experiment, prime grid or historical code was run. This changes neither the mixed numerical target nor the authoritative parity carrier. The old consecutive-column odd-prime table is not transferred.

## 1. Actual inputs and exact row models

The author actually FULL read the eleven-section authoritative parity note, 15818 bytes, SHA256 `a39081cb49a101c80a6b7f69306d67fd873caebc6dbad3198c2a21dad85449d8`, and the complete earlier finite-place note, including J12–J16. Original foundations.tex lines 95–263 and the complete original odd-primes.tex were actually read. Only their rational moment formulae and elementary digit proof are used; all column counts below are new counts for even columns.

Use the q=0 parameters

\[
A=19N,\ h=e=2N,\ K=8N,\ b=11N,\quad
n=44N-1,\ L=55N-1,\ H=130N,
\]

with x=t^2, degrees 8N+1 <= d <= 44N-1, and unscaled pairs

\[
Q_d(x)=P_d^{(h-1/2,-1/2)}(2x-1),\quad
P_d=t^{2A}(1-t^2)^hQ_d(t^2),
\]
\[
D_d=-\mu x^{A+1}(1-x)^h
 \operatorname{trunc}_{<36N-2}\frac{B_{Q_d}(x)}{(1-x)^h}.
\tag{F1}
\]

The moment-normalized integer pair is F1 multiplied by

\[
\lambda_d=d_\mu 2^{2K+2h}4^d.
\tag{F2}
\]

Select all 36N-1 Jacobi pairs and the first 8N integral tails `t^(2(L+a))(1-t^2)^h`. Write E^mom for this n-square rational matrix, with columns j=2(b+k), 0 <= k < n, and entries

\[
M^0(P,j)-\tfrac32Z^0(D,j)+\gamma C_j(P),
\quad \mu=16\beta/\alpha,\ \gamma=4u/\alpha.
\tag{F3}
\]

Under alpha G+beta pi^2=u, F3 is the actual matrix: even P kills H_j at every even j, and the exact contact is -D_j=mu C_j. All row exponents i are even and less than H; P starts at 2A, D at 2A+2. Every column is even, from 2b through 2L-2. There is no binomial column filter in this variant.

## 2. A complete all-prime, all-power starting cap

Put ell_H=lcm(1,...,H), a_p=v_p(ell_H). The original rational arrays give, at every odd prime,

\[
v_p(M^0(i,j)),\ v_p(Z^0(i,j))\ge-2a_p.
\tag{F4}
\]

For completeness, the all-power argument bounds `v_p(z binom(z,z/2))` for even z and `v_p(z binom(z-1,(z-1)/2))` for odd z by a_p. If s=v_p(z), the first s carry levels vanish and at most a_p-s remaining levels contribute. In the explicit starting arrays of source lines 213–240 each summand therefore has depth at most 2a_p. Diagonal reduction adds only m_v/k at that depth. The harmonic formula for Z0 has the same two-layer bound. This argument includes all higher powers and every small odd prime.

At 2, the coefficient of x^u in 4^d Q_d has valuation at least 2u. A contribution to P from that coefficient and endpoint degree v <= h has i=2(A+u+v). Since j >= 2b,

\[
i-j\le2u+2(K+h).
\]

The only possible linear dyadic loss of its minus start is at most i-j, so F2 clears it termwise. The plus-start difference j-i-1 is odd and its start is integral at 2. This follows from `v_2(c_r)=-2r+s_2(r)` and the monotonicity of `2r-s_2(r)` in the explicit starting sums. The m_v/k terms are cleared by ell_H; Z0 by ell_H^2. F1's prescribed section and C outputs are integral after F2, by the authoritative Chebyshev connection and integer inverse endpoint series. Thus

\[
\boxed{2d_\gamma\ell_H^2E^{\rm mom}\in\operatorname{Mat}_n(\mathbb Z).}
\tag{F5}
\]

This remains the complete fallback for all primes and powers. Its safe limiting lower exponent is -65/11 on the n-squared scale. No claim of optimality is attached to that fallback.

## 3. The new even-column digit layers for p > H/2

Fix an odd prime p > H/2 not dividing d_gamma. Then i,j < 2p and a_p=1. Put

\[
\Pi_p(t)=(1-t^2)^{(p-1)/2},\qquad
\epsilon=(-1)^{(p-1)/2}.
\]

Its even coefficient at 2r is c_r modulo p, its odd coefficients vanish, and reversing its coefficients multiplies by epsilon. These identities follow from the finite binomial expansion, not a row packet assumption.

Here is the needed specialization of the explicit boundary arrays. For odd z=p+r<2p (r even), the recurrence H*_(z+2)/H*_z=(z+1)/(z+2), starting with `pH*_p=epsilon mod p`, gives

\[
pH^*_{p+r}\equiv\epsilon c_{r/2},\qquad
pm_{p+r-1}\equiv2(\Pi_p)_{p-1-r}.
\]

For odd z<p, pH*_z vanishes modulo p. For even u<2p, `p^2 k^-_u=0 mod p`: if u<p its starting factors are integral, while if u>p the single carry in c_(u/2) cancels one of the possible two denominator powers. For the even plus start k^+_(u+1), with u odd, the only p^-2 term when u=p+r is z=p in its explicit sum; it gives `p^2 k^+_(u+1)=2(Pi_p)_r mod p`. For u<p that layer is zero. Diagonal reduction now contributes at depth two only at harmonic index k=p. These facts rederive the needed moment residues directly from the rational arrays.

For each residue ell define row vectors

\[
P'_v=[t^{(v+1)p+\ell}]\,tP(t)\Pi_p(t),\quad
D'_v=[t^{vp+\ell}]D(t),
\]
\[
V_\ell=2P'_1-\tfrac32D'_1,\qquad
U_\ell=2P'_{-1}-\tfrac32D'_0.
\]

For the columns actually present, the just-derived moment reductions and harmonic formula give

\[
p^2F_j\equiv0\quad(j<p,\ j\ {\mathrm even}),\qquad
p^2F_{p+\ell}\equiv U_\ell-V_\ell
\quad(\ell\ {\mathrm odd},\ p+\ell\text{ present}).
\tag{F6}
\]

Since tP Pi_p is odd and D is even, V_ell is zero for every even ell. Also U_ell=0 for ell <= 2A. Hence **every low even column j<p has depth at most one**. Only high even columns j=p+ell, with odd ell, can retain depth two. This parity assertion differs from consecutive raw-column pairing; the absent odd column is never introduced.

For a central even column `H-p <= j < p`, its two starting differences have absolute value less than p. Reindexing its diagonal sum and using the displayed m reduction gives

\[
pF_j\equiv-\sum_{\substack{0\le\ell<H-p\\\ell\ {\mathrm odd}}}
\frac{V_\ell}{j-\ell}\pmod p.
\tag{F7}
\]

Each denominator is a unit. For Z0 the only poles are i=p+ell, giving `pZ0(i,j)=1/(ell-j) mod p`; this pays its sign in F7. Gamma C is integral and disappears at both displayed layers. F6/F7 are valid for arbitrary locally integral even pairs with the specified support, whether or not leading vectors vanish.

## 4. Finite counts and integral column elimination

For p > H/2 define the integer counts

\[
R_p=\left(L-\frac{p+1}{2}\right)_+,\qquad
\ell_p=\left(\frac{H-p+1}{2}-b\right)_+,
\quad c_p=n-R_p-\ell_p.
\tag{F8}
\]

They count respectively high even columns, noncentral low even columns, and central even columns. All low columns have depth at most one. Consequently the determinant loss is at most n+R_p, without any leading-rank hypothesis.

For p > 75N, every high column has ell <= 2L-2-p < 2A. Its residue is therefore -V_ell. These high columns represent all odd residues from 1 through 2L-2-p. In F7 the unrepresented odd residues number

\[
e_p=\left(\frac{H-p-1}{2}\right)_+-R_p\ge0.
\tag{F9}
\]

For each represented vector, adding an integral multiple of p times its high column cancels its contribution to pF_j. These are integral shears with integral inverses, retaining every high and low noncentral column. The remaining scaled central residues lie in the span of at most e_p vectors. An invertible change of central columns over Z_p, obtained by lifting a residue-field basis with its kernel last, leaves at most min(c_p,e_p) central columns with depth one; all other central columns are integral. Thus

\[
D_p^{\rm col}=\begin{cases}
n+R_p,&H/2<p\le75N,\\
\min\{n+R_p,\ 2R_p+\ell_p+\min(c_p,e_p)\},&75N<p\le H
\end{cases}
\tag{F10}
\]

is a complete finite-N determinant loss bound at these primes. No column is discarded. An n-square matrix changes determinant only by a local unit under these operations. The same loss bound holds for every n-row minor of the full row pool.

## 5. A new explicit integral row division

For Q_d, the coefficient A_(d,k) of x^k in 4^d Q_d(x) is exactly

\[
A_{d,k}=(-1)^{d+k}\binom{2d}{d}
\frac{d!}{(d-k)!}
\frac{(d+h+k-1)!}{(d+h-1)!}
\frac{4^k}{(2k)!},\quad0\le k\le d.
\tag{F11}
\]

It follows by expanding the finite shifted Jacobi polynomial at x=0; the rising factor (1/2)_k=(2k)!/(4^k k!) gives the displayed normalization. Indeed, the binary factorial formula gives

\[
v_2(A_{d,k})=2k+s_2(d-k)+s_2(d+h-1)+s_2(k)
-s_2(d+h+k-1)\ge2k,
\]

by binary digit subadditivity. This also directly proves the coefficient valuation used in section 2.

Suppose d+h-1 < p <= 2d is odd. Then d<p, d+h-1<p and d+h+k-1<2p. The factorial formula gives

\[
v_p(A_{d,k})=1+[d+h+k-1\ge p]-[2k\ge p].
\tag{F12}
\]

If 2k<p it is at least one. Otherwise d>=k and h>=2 force d+h+k-1>=p, so it is also one. The constant coefficient has valuation exactly one. Therefore the whole polynomial has p-content, and this conclusion holds for every N in the stated interval, rather than a special N=p family.

Define the explicit odd squarefree integer

\[
\Omega_d=\prod_{\substack{p\ {\mathrm odd}\ {\mathrm prime}\\d+h-1<p\le2d}}p,
\qquad \Omega_N=\prod_{d=8N+1}^{44N-1}\Omega_d.
\tag{F13}
\]

Every coefficient of 4^d Q_d is divisible by Omega_d. Multiplication by the endpoint factor preserves this. The second-kind polynomial B_Q uses only dyadic coefficient denominators; the integral Chebyshev model and integer inverse endpoint series in F1 preserve each of these odd prime factors as well. Thus the **entire prescribed integer pair and its integral C outputs** can be divided by Omega_d. This is a proved integral row model, not a claim to produce the whole primitive contact lattice.

Let E^div be E^mom with those Jacobi rows divided by Omega_d; tails stay unchanged. Then

\[
\boxed{\det E^{\rm mom}=\Omega_N\det E^{\rm div}.}
\tag{F14}
\]

At 2 these odd divisions change no valuation. At any odd prime, the divided pairs and C outputs remain integral, so F4 and the new column proof apply to E^div without a coefficient-dependent exceptional set.

## 6. An exact denominator certificate and its leading cost

For all primes define

\[
W_p=\begin{cases}
n\{2a_p+v_p(2d_\gamma)\},&p=2\text{ or }p\le H/2\text{ or }p\mid d_\gamma,\\
D_p^{\rm col},&H/2<p\le H,\ p\nmid d_\gamma,\\
0,&p>H,\ p\nmid2d_\gamma.
\end{cases}
\]

Put D_N=prod_p p^(W_p). This finite product includes all prime powers and fixed denominator primes, and proves

\[
D_N\det E^{\rm div}\in\mathbb Z,
\qquad D_N\det E^{\rm mom}/\Omega_N\in\mathbb Z.
\tag{F15}
\]

Writing x=p/N, the new limiting column loss is

| x interval | limiting loss d(x) | integral |
|---|---:|---:|
| [0,65] | 88 | 5720 |
| [65,75] | 99-x/2 | 640 |
| [75,108] | 174-3x/2 | 4851/4 |
| [108,110] | 120-x | 22 |
| [110,130] | (130-x)/2 | 100 |

It is zero beyond 130, is continuous at 75, 108 and 110, and has a permitted downward jump at 65. Its total area is 30779/4. These counts come from F8–F10: for 65<x<108, R/N=(110-x)/2, ell/N=(108-x)/2, c/N=x-65; after x=75 the exceptional dimension is 10. For 108<x<110 only the high count remains, and after 110 every column is central. Integer offsets in L and n change each count by O(1), uniformly in p,N.

The prime number theorem in its usual weighted form theta(y)~y, applied to this bounded Riemann-integrable function by upper and lower step sums, gives

\[
\log D_N=(30779/4)N^2+o(N^2).
\]

The extra prime-power levels are supported on p<=sqrt(H) and cost O(N sqrt(N) log N); the prime 2 costs O(N log N). Fixed denominator primes and uniform count offsets also contribute o(N^2). Thus every power is covered in F15 without contributing an omitted leading term.

The exact prime product in F13 has logarithm

\[
\log\Omega_N=\sum_d\{\theta(2d)-\theta(d+h-1)\}
=864N^2+o(N^2).
\]

Uniformity follows because all endpoints lie in fixed positive multiples of N, so the PNT error per degree is uniformly o(N). In particular this gain is attached to actual integral rows, not an assumed denominator minimum.

## 7. Conditional lower bounds and consistent normalization costs

Along any unbounded sequence on which the specified rational determinant is nonzero, F15 gives

\[
\boxed{\liminf\frac{\log|\det E^{\rm div}|}{n^2}
\ge-\frac{30779}{7744},}
\qquad
\boxed{\liminf\frac{\log|\det E^{\rm mom}|}{n^2}
\ge-\frac{27323}{7744}.}
\tag{F16}
\]

Both are safer lower bounds, not necessary minima. In the moment model specified in the authoritative parity note, the second improves the uniform starting lower bound -65/11. For any full-pool maximal minor omitting one Jacobi row, the missing Omega_d costs only O(N); the same leading bounds hold uniformly over the choice of the omitted row.

The exact leading scalar costs must be retained at the real place:

\[
\sum_d\log\lambda_d=2592\log2\,N^2+O_\mu(N),
\qquad
\sum_d\log(\lambda_d/\Omega_d)
=(2592\log2-864)N^2+o(N^2).
\tag{F17}
\]

The first uses `sum d=936N^2-26N` and `2K+2h=20N`. Dividing the rows by Omega removes the same 864N^2 from the analytic determinant upper bound and from the arithmetic lower bound. It cannot close a gap by normalization alone. In particular one must not compare the lower bound for E^mom with the real upper bound for E^div.

## 8. Scope

This note pays a new parity-specific joint column certificate, all primes and powers including 2, an explicit integral odd row division, and the resulting conditional N-squared lower bounds. It permits arbitrary leading vectors to vanish and uses no historical odd-column loss table, fixed-packet nonzero claim or numerical extrapolation.

The arbitrary rational relation-point determinant nonzero remains open. This note supplies no real-place norm for the complete D_C lift or joint exterior. A strict arithmetic/real comparison remains a separate obligation. These arithmetic bounds alone prove no numerical linear independence and exclude no alternative support or lattice.

Review receipt: the author actually FULL read all eight sections after writing F1–F17. Root actually FULL read and independently paper-checked that 13707-byte version, SHA256 7203be9527f6701fc8889ac9eb43f1173432d078a29d1c3461b70627859e3273, with PASS and no mathematical correction. Root also reported a bounded direct source reading of the moment/start/reduction/H* formulae in original foundations.tex lines 95–263 and original odd-primes.tex lines 245–381; that source reading is not recorded as FULL. It checked the even residue and support signs, finite counts and new area, row-content interval, PNT gain, all-power fallback and consistent F16 normalization. The author actually FULL reread the final file after this receipt update. No old note, main or manifest was edited.

Final independent receipt: gamma_bound actually FULL read all eight F1–F17 sections at 14447 bytes, SHA256 376675c63dea272c8e90a37c7bdf5bc7a1e8c4102acc0d1a83983874a4f44707, and independently paper-checked every formula and scope with PASS and no correction. Its additional source reading was bounded to original foundations.tex lines 95–263 and odd-primes.tex lines 245–381, not FULL old-source reading. It independently checked the even moment layers and signs, all-power/dyadic fallback, finite integral column changes, new area, shifted Newton content and PNT gain, complete certificate and both normalizations. No code, producer or scan was run for that review. Only this receipt was appended after mathematical freezing; the author actually FULL reread the resulting final eight-section file without truncation.
