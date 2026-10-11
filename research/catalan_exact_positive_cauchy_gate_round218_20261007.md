# A quantitative gate for the exact positive Cauchy exterior

2026-10-07, round 218. NEW isolated paper note. The exact unrestricted whole-M Cauchy exterior integral is positive, but that fact gives a quantitative lower barrier for the value of the upper certificate built from it. This barrier remains far above the paid arithmetic threshold, even after the new common dyadic cancellation. The proof retains the entire mixed exterior and all included tails. It does not assert a lower bound for an actual determinant or for the source-restricted, tail-projected M exterior. No producer, parameter grid, prime scan, log evaluator or historical program was run. Old notes, main and manifests are unchanged.

## 1. The fixed carrier and the certificate under examination

Use the current q=0, b=11N parity carrier. The proposed relation is \(\alpha G+\beta\pi^2=u\), with rational \(\alpha,\beta,u\), \(\alpha\beta\ne0\), and fixed \(\mu=16\beta/\alpha\ne0\), \(\gamma=4u/\alpha\). The real estimates do not assume that relation. The parameters are
\[
A=19N,\quad h=2N,\quad b=11N,\quad K=8N,\quad
n=44N-1,\quad L=55N-1,\quad m=36N-2,\quad
p=m+1,\quad\delta=8N+1.                              \tag{C1}
\]
Write
\[
d\nu_h=\pi^{-1}x^{-1/2}(1-x)^{h-1/2}dx,
\quad H_y=L^2(y^{b-1/2}dy),
\quad Q_d=P_d^{(h-1/2,-1/2)}(2x-1),\quad K<d\le n.
\]
Let \(J_N\) be the isometric inclusion of the p normalized Jacobi directions \(Q_d/\sqrt{\rho_d}\), and \(\Pi_N\) projection off the **entire** actual tail-transform span. The whole M operator is
\[
(\mathcal MQ)(y)=\frac\pi2\int_0^1
\frac{x^{A+1/2}Q(x)}{1-xy}\,d\nu_h(x),\qquad
M_N=\Pi_N\mathcal MJ_N.                              \tag{C2}
\]
Let \(D_N\) be the whole completed D residual operator per unit \(\mu\), with both Cauchy channels. Its minimum input Gram \(\widehat G_D\) has rank m and positive eigenvalues \(\lambda_1\ge\cdots\ge\lambda_m\). The paid complete operator inequality is
\[
D_N^*D_N\le c_0^2\widehat G_D,\quad c_0=3\pi/4.
\]
All contact completions are actual combinations of the included delta tails. No omitted-tail principal square is considered.

The exact positive whole-M exterior integral from the frozen round217 interface is
\[
\begin{aligned}
I_{r,N}=\frac{(\pi/2)^{2r}}{(r!)^2}
\int_{(0,1)^{2r}}&\prod_i x_i^{2A+1}\,d\nu_h(x_i)
                      \prod_j y_j^{b-1/2}dy_j\\
&\times\frac{V(x)^2V(y)^2}{\prod_{i,j}(1-x_iy_j)^2},
\end{aligned}\qquad I_{0,N}=1.                       \tag{C3}
\]
It equals \(\|\bigwedge^r\mathcal M\|_{\rm HS}^2\), hence bounds the exterior operator norm of \(M_N\). Its integrability and the factor \((r!)^{-2}\) were paid in round217; the new argument below evaluates a leading **lower barrier for this upper-certificate integral**, rather than repeating the Taylor approximation numbers.

## 2. An all-r finite beta-Gram lower bound for the exact integral

For \(a,c>-1\), define the positive beta Gram
\[
H_r(a,c)=\det_{0\le u,v<r}B(a+u+v+1,c+1),\quad H_0=1.
\]
Expanding both Vandermonde determinants and integrating termwise proves
\[
\int_{(0,1)^r}V(z)^2\prod_i z_i^a(1-z_i)^c dz_i
=r!H_r(a,c).                                        \tag{C4}
\]
This is just the determinant integral identity: the two permutation sums have r! identical determinant contributions. All terms are integrable for the stated parameters.

On the full integration support, each \((1-x_iy_j)^{-2}\ge1\). Retaining that inequality in C3 and using C4 twice gives the exact finite bound
\[
\boxed{I_{r,N}\ge(\pi/4)^r
H_r(2A+1/2,h-1/2)H_r(b-1/2,0).}                     \tag{C5}
\]
The power is \((\pi/2)^{2r}\pi^{-r}=(\pi/4)^r\): the r source measures each contribute \(\pi^{-1}\), and the two r! factors cancel the denominator. The entire Cauchy denominator remains in the exact integral; positivity gives a lower estimate for its value. No cut or signed component is removed from the actual mixed operator.

The beta Gram product, obtained by multiplying monic shifted-Jacobi norms, is
\[
H_r(a,c)=\prod_{j=0}^{r-1}
\frac{j!\,\Gamma(a+j+1)\Gamma(c+j+1)}
     {\Gamma(a+c+r+j+1)}.                             \tag{C6}
\]
Equivalently the monic norm is
\(\Gamma(j+1)\Gamma(a+j+1)\Gamma(c+j+1)\Gamma(a+c+j+1)
/[(2j+a+c+1)\Gamma(2j+a+c+1)^2]\); its product cancels to C6. Thus with
\[
X(t)=\tfrac12t^2\log t-\tfrac14t^2,\quad X(0)=0,
\]
\[
\mathscr H(r;a,c)=X(r)+X(a+r)-X(a)+X(c+r)-X(c)
                  -X(a+c+2r)+X(a+c+r),
\]
uniform integral bounds for \(\log(j!)\), or uniform Stirling bounds, give
\[
\lim N^{-2}\log H_{rN+O(1)}(aN+O(1),cN+O(1))
=\mathscr H(r;a,c).
\]
In particular C5 proves the new exact-positive leading barrier
\[
\boxed{\liminf N^{-2}\log\sqrt{I_{m,N}}
\ge\tfrac12\mathscr H(36;38,2)
   +\tfrac12\mathscr H(36;11,0).}                    \tag{C7}
\]
This lower barrier is an explicit finite-logarithm expression. No equality with the exact integral's limit, solved vector equilibrium or independent numerical value is claimed.

## 3. A closed finite interval bound and an explicit rational threshold

The preceding expression can be bounded without a numerical evaluator. For \(a,c\ge0\) and \(0<l<u\le1\), C4 restricted to \([l,u]^r\) gives
\[
\boxed{H_r(a,c)\ge l^{ar}(1-u)^{cr}(u-l)^{r^2}H_r(0,0).}
                                                               \tag{C8}
\]
When c=0 and u=1, the endpoint factor is defined to be one. The affine Jacobian contributes \((u-l)^r\), and the squared Vandermonde contributes \((u-l)^{r(r-1)}\), paying the exponent r² exactly.

Here
\[
H_r(0,0)=\prod_{j=0}^{r-1}
\{(2j+1)\binom{2j}{j}^2\}^{-1}
\ge2^{-2r(r-1)}(2r)^{-r},\quad r\ge1,                \tag{C9}
\]
because \(\binom{2j}{j}\le2^{2j}\) and \(2j+1\le2r\). The matching binomial lower \(\binom{2j}{j}\ge2^{2j}/(2j+1)\), obtained by summing the 2j+1 binomial coefficients, gives the other bound with only O(r log r) logarithmic error. Thus its leading exponent is \(-2r^2\log2\) on the proportional-size scale.

Choose x in \([1/2,3/4]\) and y in \([1/2,1]\). For the actual parameters in C5, C8 gives
\[
H_r(38N+1/2,2N-1/2)
\ge2^{-(42N-1/2)r-2r^2}H_r(0,0),
\]
\[
H_r(11N-1/2,0)
\ge2^{-(11N-1/2)r-r^2}H_r(0,0).
\]
Consequently the following bound is finite and holds for every N,r:
\[
\boxed{\sqrt{I_{r,N}}\ge
(\pi/4)^{r/2}
2^{-(53N-1)r/2-3r^2/2}\,H_r(0,0).}                 \tag{C10}
\]
With r=m=36N−2, C9–C10 prove
\[
\boxed{\liminf N^{-2}\log\sqrt{I_{m,N}}
\ge-5490\log2.}                                     \tag{C11}
\]
The two individual Gram leading bounds are \(-6696\log2\) and \(-4284\log2\); their half-sum is C11. The factor \((2m)^{-m}\) costs only \(O(N\log N)\). These choices are fixed rational intervals, not a parameter optimization or scan.

## 4. The complete mixed certificate and all actual tail factors

The source dimension is p=m+1. Every unit m-vector is decomposable; multilinearity of \((M_N+\mu D_N)v_1\wedge\cdots\wedge(M_N+\mu D_N)v_m\) and the exterior product norm inequality therefore give the lawful exact-positive certificate
\[
\boxed{\|\bigwedge^m(M_N+\mu D_N)\|\le
\mathcal E_N^{\rm exact}:=
\sum_{r=0}^m\binom mr\sqrt{I_{r,N}}
 (c_0|\mu|)^{m-r}\sqrt{\prod_{i=1}^{m-r}\lambda_i}.} \tag{C12}
\]
Empty products are one. Every middle value \(0<r<m\) remains. There is no assumption that M and D have a common singular basis. The positive sum is an upper bound; cancellation in the actual mixed exterior can make its volume much smaller.

For an all-tail minor choosing m source directions I, put
\[
\mathcal P_{I,N}^{s}=
\left(\prod_{d\in I}\lambda_d^s\sqrt{\rho_d}\right)
\sqrt{H_n(b-1/2,0)H_\delta(2L-1,2h)}\,c_0^\delta,
\]
where s specifies the consistent row model. Exactly the original column normalization and complete input-tail Gram factors are used. Bessel contraction and the actual orthogonal projection \(\Pi_N\) prove
\[
|\Delta_I^s|\le\mathcal C_{I,N}^{s}:=
                   \mathcal P_{I,N}^s\mathcal E_N^{\rm exact}.
                                                               \tag{C13}
\]
The r=m term in C12 is \(\sqrt{I_{m,N}}\). Thus C10 is a lower bound on the value of this full upper certificate, **even if every D-containing term could be made negligible**. This keeps the complete mixed operator, original determinant normalization, every tail and the actual tail projection in the comparison. It does not substitute a D-only component for the mixed determinant.

## 5. New dyadic model and the conditional arithmetic lower on the same object

The frozen new dyadic gate proves: if an even integral P has integral raw \(C_j(P)\) at 2, then its actual \(M^0(P,j)\) lies in \(2\mathbb Z_2\) for every even j. Together with integrality of the whole prescribed pair and C outputs, it permits
\[
\lambda_d^{\rm pair}=d_\mu2^{2h}4^d=d_\mu2^{4N}4^d,
\quad \lambda_d^{\rm mom}=2^{16N}\lambda_d^{\rm pair}.
                                                               \tag{C14}
\]
The aggregate dyadic lemma is applied with its C-integrality hypothesis, not to an arbitrary monomial. The odd-prime proofs in F4–F15 depend only on locally integral even pairs with the same support. The removed powers of 2 are units at every odd prime; their proofs and finite column counts remain valid for the pair model. At 2 the new aggregate lemma and the harmonic Z formula give the complete fallback \(2d_\gamma\operatorname{lcm}(1,\ldots,130N)^2\), whose 2-part costs only \(O(N\log N)\) in a determinant.

The proved odd content \(\Omega_d\) can still divide the entire pair and C outputs; its odd denominator is a unit at 2, so the aggregate lemma still applies. Therefore the same F15 all-prime determinant certificate in the pair model has area \(30779/4\), and the retained odd row content has leading \(864N^2\). This independently yields, conditional on a nonzero rational minor along an unbounded sequence,
\[
\boxed{\liminf N^{-2}\log|\Delta_I^{\rm pair}|
\ge-27323/4.}                                      \tag{C15}
\]
This is a reapplication of the complete cap to a newly paid integral model, not a mechanical transfer of the old lower. Omitting one Jacobi direction changes the content only by O(N). Under the same conditional relation, the exact determinant conversion is
\[
\Delta_I^{\rm mom}=2^{16Nm}\Delta_I^{\rm pair},
\quad16Nm=576N^2-32N.
\]
Hence the old moment model now has the stronger lower \(-27323/4+576\log2\), while the pair model has C15. This is a new actual dyadic arithmetic gain. The real upper factors must convert by the identical scalar. The pair scalar's leading cost is \(2016\log2\), and the historical moment scalar's cost is \(2592\log2\).

## 6. A decisive leading barrier for this exact-positive construction

Uniformly in the omitted Jacobi direction, \(\prod\rho_d\) contributes only \(O(N\log N)\). Therefore C7 gives the exact-logarithm lower barrier
\[
\begin{aligned}
\liminf N^{-2}\log\mathcal C_{I,N}^{\rm pair}\ge
&2016\log2+\tfrac12\mathscr H(44;11,0)
 +\tfrac12\mathscr H(8;110,4)\\
&+\tfrac12\mathscr H(36;38,2)
 +\tfrac12\mathscr H(36;11,0).                        \tag{C16}
\end{aligned}
\]
No D spectrum refinement can change the r=m term which proves this barrier.

For a completely rational comparison, the exact monic norm for \(y^{11N-1/2}dy\), bounded by its integral-parameter binomial ceiling, gives
\(\mathscr H(44;11,0)\ge-4840\log2\).
Restricting the tail beta Gram to \([1/2,3/4]\) gives weight at least \(2^{-118N+O(1)}\), an affine factor \(2^{-2\delta^2}\), and C9's Hilbert factor \(2^{-2\delta^2+O(N\log N)}\); hence
\(\mathscr H(8;110,4)\ge-1200\log2\).
The pair prefactor is thus at least \(-1004\log2\) on the leading scale. Combining with C11 proves
\[
\boxed{\liminf N^{-2}\log\mathcal C_{I,N}^{\rm pair}
\ge-6494\log2>-\frac{22729}{5}>-\frac{27323}{4}.}     \tag{C17}
\]
Here \(\log2<7/10\) follows directly from the first five positive exponential terms:
\(1+7/10+(7/10)^2/2+(7/10)^3/6+(7/10)^4/24
=482921/240000>2\).
The certificate's leading barrier exceeds the paid arithmetic lower by more than \(45699/20\), that is 2284.95, on the N² scale. In the old moment model the barrier is \(-5918\log2>-20713/5\), while its updated lower is \(-27323/4+576\log2\); the identical gap follows. A further division by the already proved odd row content subtracts 864 from both sides and changes neither comparison.

This also closes the immediate hybrid construction which replaces the r-th Taylor exterior bound by \(\min(A_{r,N},\sqrt{I_{r,N}})\): its all-M term is the minimum of the two all-M certificates. The separately frozen Taylor certificate has old-model floor greater than −680; conversion to the pair model subtracts \(576\log2\). That floor remains strictly above \(-22729/5\). Since both choices have this lower barrier, their minimum does too. This uses the existing round217 result as a logical input and introduces no new singular-bound derivation.

C17 is a bound for the value of a specified upper certificate. It is not an actual determinant lower bound, not a necessary arithmetic minimum and not a carrier no-go theorem. It applies while the unrestricted positive whole-M exterior and displayed input-tail/operator prefactor are used. A new actual tail-output exterior estimate, actual source restriction, cross-channel cancellation or joint arithmetic lattice can change the comparison.

## 7. The vector-energy meaning and the unclosed actual mixed Gram

The obstruction has a simple exact energy explanation. For noncolliding configurations in C3, let \(a_N=r/N\), and let \(\sigma_x,\sigma_y\) be their empirical probability measures. Define \(I_r(\sigma_x)=r^{-2}\sum_{i\ne j}\log|x_i-x_j|\), and similarly for y. Apart from constants independent of the particles, the log integrand divided by N² is exactly
\[
\begin{aligned}
&a_N(38+1/(2N))\int\log x\,d\sigma_x
 +a_N(2-1/(2N))\int\log(1-x)\,d\sigma_x\\
&+a_N(11-1/(2N))\int\log y\,d\sigma_y
 +a_N^2\{I_r(\sigma_x)+I_r(\sigma_y)\}\\
&-2a_N^2\iint\log(1-xy)\,d\sigma_xd\sigma_y.          \tag{C18}
\end{aligned}
\]
The last interaction is nonnegative throughout the square and continuous on the selected compact x interval. It can increase the unrestricted positive partition function, but cannot suppress the two uncoupled weighted-Gram contributions used in C5. Thus solving the full vector equilibrium cannot rescue this particular certificate: the simple uncoupled-energy lower barrier already proves C17. No assertion that a variational supremum equals the integral limit, or that an equilibrium measure was computed, is needed for this conclusion.

The actual source restriction is materially different. Its reproducing kernel
\[
P_J(x,t)=\sum_{d=K+1}^{n}q_d(x)q_d(t)
\]
appears inside the restricted whole-M output Gram kernel as
\[
\frac{\pi^2}4\iint
\frac{x^{A+1/2}t^{A+1/2}P_J(x,t)}{(1-xy)(1-tz)}
                         d\nu_h(x)d\nu_h(t).
\]
It has oscillatory cross terms; it is not C3 with a smaller positive support. The actual tail projection is another Schur complement. For whole mixed row functions U_d and pure-tail functions V_a, if the tail Gram T is invertible, the exact residual source Gram is
\[
G_{\rm actual}=A-BT^{-1}B^t,\quad
A_{dd'}=\langle U_d,U_{d'}\rangle,\quad
B_{da}=\langle U_d,V_a\rangle,\quad
T_{aa'}=\langle V_a,V_{a'}\rangle.                    \tag{C19}
\]
If tails are dependent, the same projection uses the Moore-Penrose inverse, and every all-tail moment minor is zero. The full U includes both M and \(\mu D\), so A and B retain all mixed cross terms. Neither the input Gram \(\widehat G_D\) nor the unrestricted integral C3 equals C19. C17 therefore proves no lower barrier for \(e_m(G_{\rm actual})\) or for the actual projected whole-M exterior.

The next decisive question is a bound for this actual source-restricted, projected mixed Gram, or a new complete tail-output exterior/joint-column estimate. Further effort solving only the positive unrestricted C3 equilibrium, or refining D within C12, has an explicit exit criterion C17. Actual rational relation-point nonzero along unbounded N remains a separate gate.

## 8. Accurate reading, execution and review scope

In this round the author actually FULL read, without truncation, the frozen round217 whole-M note X1–X16 (17621 bytes, SHA256 8744b960b96d2e1a50b1977ea6b67b643d09b351a5d0322a492275ffb10ea31b), the final dyadic gate G1–G21 including its eighth-section receipts (17670 bytes, SHA256 4cb75887e8d013b1ab4e947b805d4a29722a1c53273cf0d5dddc7090e65e71a6), the current finite-place F1–F17 note (15271 bytes, SHA256 f4400e1e72b99e57f7a830c4e390e0c8ade78505a434196233a5cba6e2fab0a0), and exact second-kind/joint-energy E1–E18 note (16036 bytes, SHA256 c18bd6973c4a198e1c0c4eea598d0bd3c3369e29f51680c9ed5a6b9ef7a86040). These are current file readings, not new FULL readings of their underlying original papers, source files or programs.

All new estimates above were derived on paper. No webpage/PDF was newly read or downloaded and no mathematical program was executed. One bounded subtask was sent to universal_normalization to check the exact-positive exterior interface; its separate root arithmetic task had priority. No helper FULL draft review is claimed. Root review and the author final FULL reread/byte pin remain pending.
