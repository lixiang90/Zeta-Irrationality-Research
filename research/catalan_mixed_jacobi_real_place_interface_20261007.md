# Actual reduced mixed Jacobi rows: real-place exterior estimate and the zero-junction term

2026-10-07. NEW isolated lemma/interface. The principal object is the exact 44N−1 square from the ten-section contact note, including its actual linear D_mu section and 8N pure-D rows. This proves finite-N real upper bounds, exact removal of the selected pure-D span, and a Rodrigues remainder bound. It does not prove actual moment nonvanishing or a strict arithmetic/analytic comparison. No producer, supplied code, old guard, prime scan, PSLQ or Lean was run.

## 1. Actual rows, section and scalar normalization

Fix nonzero rational mu=16 beta/alpha. Write
\[
n=44N-1,\ r=36N-1,\ m=8N,\quad
b=7N,\ q=4N,\ h=2N,\ e=6N,\ A=19N,\ H=65N,
\]
\[
L=b+n+q=55N-1,\qquad m_0=L-A-1=36N-2. \tag{R1}
\]
For 8N+1≤d≤44N−1 let
\[
J_d=P_d^{(e-1/2,-1/2)},\qquad P_d^0=t^A(1-t)^hJ_d.
\]
Use exactly the contact note's triangular prescription of D_j for A+1≤j<L from the filtered equations
\[
\sum_{v=0}^q(-1)^v\binom qv D_{b+k+v}
=\sum_{v=0}^q(-1)^v\binom qv
 (H_{b+k+v}(P)-\mu C_{b+k+v}(P)),
\]
with D_j=0 for j≤A. Its first 8N+1 equations are the Jacobi low-moment constraints. Complete by the specified zero-end section
\[
D_\mu^{\rm sec}(P)=t^{A+1}(1-t)^h
\operatorname{trunc}_{<m_0}
\left(\frac{t^{-(A+1)}D_{<L}}{(1-t)^h}\right).
\tag{R2}
\]
Thus D_d^0=D_mu^sec(P_d^0) retains the actual support, coefficients and endpoint factor. This is linear in P and affine-linear in mu as an operator. Adjoin the pure-D pairs (0,T_a), where
\[
T_a=t^{L+a}(1-t)^h,\quad 0\le a<m.
\tag{R3}
\]
Independent polynomial pairs do not imply independent actual moment rows.

Multiply each Jacobi pair by the same scalar on both P and D. The three distinct integral choices are
\[
\lambda_d^{\rm old}=d_\mu2^{58N-2}8^d,\quad
\lambda_d^4=d_\mu2^{58N-2}4^d,\quad
\lambda_d^{\rm red}=d_\mu2^{s_d}4^d,
\]
\[
s_d=\max(14N+d-(d\bmod2),36N-4).
\tag{R4}
\]
The finite-place note proves all-degree 4^d integrality and the row-specific clearing; pure-D rows stay unchanged. For the actual determinants,
\[
\Delta_\lambda=(\prod_d\lambda_d)\Delta_0,\qquad
\Delta_{\rm old}=2^{936N^2-26N}\Delta_4
=2^{1486N^2-42N-6}\Delta_{\rm red}.
\tag{R5}
\]
These exact scalars must appear identically on the real and finite sides. They are not a free analytic gain.

## 2. Actual integral and the Cauchy alternant

Let
\[
d\sigma(t)=|t|\,dt/\sqrt{1-t^2},\quad -1<t<1,\qquad
w(s)=s^b(1-s)^q,\quad 0<s<1.
\]
For every actual pair define
\[
U_{P,D}(s)=\int_{-1}^1\frac{P(t)}{1-ts}d\sigma(t)
-\frac32\int_0^1\frac{D(t)}{1-ts}dt. \tag{R6}
\]
Column k is exactly int_0^1 U_(P,D)(s)s^k w(s)ds. This is an unconditional real integral retaining D_mu. Under the target relation it equals the filtered conditional rational entry; the raw conditional array is not substituted before filtering.

All row functions lie in H_s=L²((0,1),w(s)ds), since
\[
|U_{P,D}(s)|\le a(P,D)/(1-s),\quad
a(P,D)=\int|P|d\sigma+\frac32\int_0^1|D|dt,
\tag{R7}
\]
and q≥4. This also pays absolute convergence of determinant expansions.

Set
\[
\mathcal A_i(t)=P_i(t)-\frac32{\bf1}_{t>0}
               \frac{\sqrt{1-t^2}}tD_i(t).
\]
D_i/t is polynomial. Two direct determinant expansions with integration-variable relabeling give
\[
\Delta_0=\frac1{(n!)^2}\int\!\int
\det[\mathcal A_i(t_j)]\,
\frac{V(t)V(s)^2}{\prod_{i,j}(1-t_i s_j)}
\prod_jw(s_j)\,ds\,d\sigma^n(t).
\tag{R8}
\]
Here V(x)=prod_(i<j)(x_j−x_i). The Cauchy alternant is det[1/(1−t_i s_j)]=V(t)V(s)/prod(1−t_i s_j): after clearing the denominator alternation forces the two Vandermondes, and the first nonzero Taylor part gives constant 1. The two 1/n! factors follow from the same permutation relabeling. No old monomial sheet determinant, Hardy interpolation bound or energy constant is used.

The alternant is positive on increasing lists, but det[A_i(t_j)] has no established sign. Kernel positivity does not pay full mixed nonvanishing.

## 3. Exact tail removal without inverse coefficient heights

Order the m pure-D rows first. Their functions are
\[
\tau_a(s)=-\frac32\int_0^1
              \frac{t^{L+a}(1-t)^h}{1-ts}dt.
\]
They are independent: their first m moment columns have, by double Andreief, a strictly positive integral apart from the known factor (−3/2)^m. Its numerator is V(t)²V(s)² and every denominator is positive. This proves only the pure-D assertion.

Let G_T=(〈tau_a,tau_c〉), Pi_T the orthogonal projection onto their span in H_s, and
\[
u_d=U_{P_d^0,D_d^0},\quad v_d=(I-\Pi_T)u_d,\quad
G_R=(\langle v_d,v_f\rangle).
\]
Exterior Cauchy–Schwarz gives
\[
\boxed{|\Delta_\lambda|^2\le
(\prod_d\lambda_d^2)\mathcal H_n(b,q)\det G_T\det G_R,}
\tag{R9}
\]
where H_n(b,q) is the monomial Gram determinant for weight w. In the row wedge subtract Pi_T u_d; its wedge with all tails is zero. The remaining vectors are orthogonal to the tails, so their Gram determinant factors. This proves R9 without charging the coefficients of an inverse tail moment matrix.

The computable formula is G_R=G_J−B^tG_T^−1B, with B_(a,d)=〈tau_a,u_d〉; no norm bound for G_T^−1 enters. Adding a selected homogeneous pure-D row to a Jacobi pair changes neither the residual nor the determinant. The full homogeneous endpoint tail has dimension 8N+1; only the selected 8N directions are removed here. Its omitted direction is not silently projected away.

## 4. Paid beta Gram factors

For nonnegative integers a,c,
\[
\mathcal H_j(a,c)=\det_{0\le i,k<j}B(a+i+k+1,c+1)
=\prod_{i=0}^{j-1}\frac{i!(a+i)!(c+i)!}{(a+c+j+i)!}.
\tag{R10}
\]
This follows by shifted Jacobi Rodrigues and integration by parts. The monic squared norms are
\[
\frac{i!(a+i)!(c+i)!(a+c+i)!}
 {(a+c+2i)!(a+c+2i+1)!}.
\]
Their product telescopes to R10; before making it monic the leading coefficient is binom(2i+a+c,i). Thus this is an exact factorial identity, not a recycled numerical constant.

Let K map L²((0,1),t^L(1−t)^hdt) to H_s with kernel 1/(1−ts). Its Hilbert–Schmidt square is
\[
\mathcal C_N=\iint
 \frac{t^L(1-t)^hs^b(1-s)^q}{(1-ts)^2}dt\,ds
=\sum_{j\ge0}(j+1)B(L+j+1,h+1)B(b+j+1,q+1)
\]
\[
\le B(L+1,h+1)B(b+1,q-1). \tag{R11}
\]
Monotone convergence gives the series; 1−ts≥1−s gives the upper bound. Compress K* K to the finite m-dimensional monomial span. Its eigenvalue sum is at most C_N, so AM–GM bounds the product by (C_N/m)^m. Hence
\[
\boxed{\det G_T\le(9/4)^m(\mathcal C_N/m)^m
                         \mathcal H_m(L,h).}
\tag{R12}
\]
The actual −3/2 has been paid, and L is 55N−1, not the old 59N.

## 5. Quantitative residual interface and an explicit finite fallback

Jacobi orthogonality under dnu_e=(1−t)^e dt/(pi sqrt(1−t²)) gives
\[
\rho_d=\int J_d^2d\nu_e
=2^{-4d-e}\frac{(2d+2e)!(2d)!}
 {(d+e)!(d!)^2(2d+e)(d+e-1)!}>0. \tag{R13}
\]
This is the specialized primary Jacobi norm, also obtainable by Rodrigues. All present degrees are positive. Define the actual residual trace
\[
\mathfrak T_N(\mu)=\sum_d\|v_d\|_{H_s}^2/\rho_d.
\]
Apply AM–GM to the finite Gram matrix of v_d/sqrt(rho_d). R9–R13 give
\[
\boxed{|\Delta_\lambda|\le
(\prod_d\lambda_d)
\sqrt{\mathcal H_n(b,q)\mathcal H_m(L,h)}
\left(\frac{9\mathcal C_N}{4m}\right)^{m/2}
(\prod_d\rho_d)^{1/2}
\left(\frac{\mathfrak T_N(\mu)}r\right)^{r/2}.}
\tag{R14}
\]
This is a new actual-row real estimate. T_N keeps the full D_mu section and the projection; no small asymptotic constant for it has yet been proved. If T_N=0 the determinant is zero.

A weaker fully explicit finite bound is obtained by putting
\[
A_d=\int|P_d^0|d\sigma+\frac32\int|D_d^0|dt.
\]
Projection is a contraction, so R7 and Hadamard give
\[
|\Delta_\lambda|\le(\prod_d\lambda_d A_d)
\sqrt{\mathcal H_n(b,q)\mathcal H_m(L,h)}
\left(\frac{9\mathcal C_N}{4m}\right)^{m/2}
 B(b+1,q-1)^{r/2}. \tag{R15}
\]
To pay A_d from the actual finite rows, let
\[
a_{d,v}=\binom{d+e-1/2}{v}\binom{d-1/2}{d-v}>0,\quad
D_d^0=t^{A+1}(1-t)^h\sum_{j<m_0}E_{d,j}t^j.
\]
The finite binomial formula and triangle inequality yield
\[
A_d\le2^h\sum_{v=0}^d a_{d,v}
 B(h+d-v+1/2,v+1/2)
+\frac32\sum_{j<m_0}|E_{d,j}|B(A+j+2,h+1).
\tag{R16}
\]
For the first term discard only |t|^(A+1)≤1 and evaluate the positive beta integral. The second retains the actual endpoint factor. E_d,j are exactly those of R2; no unknown coefficient height appears.

For a closed elementary fallback, ||P_d^0||_1≤2^(2d+e+h). The same filter and endpoint inverse coefficient sums give
\[
\sum_{j<m_0}|E_{d,j}|
 \le m_0(1+|\mu|)2^{2q+h+2m_0-2}\|P_d^0\|_1.
\]
Thus
\[
A_d\le\left[2+\frac32m_0(1+|\mu|)
 2^{2q+h+2m_0-2}B(A+2,h+1)\right]2^{2d+e+h}.
\tag{R17}
\]
This proves an exp(O_mu(N)) row bound and exp(O_mu(N²)) determinant bound. It is not claimed small enough for the finite-place comparison. R14 exposes the actual cancellation quantity that must improve this fallback.

## 6. The filter transfer and the zero-junction polynomial

A direct difference-of-powers identity, with
\[
\mathcal R_q(t,s)=\sum_{j=0}^{q-1}
       [t(1-s)]^{q-1-j}(t-1)^j,
\]
gives
\[
\frac{(1-s)^q}{1-ts}
=t^{-q}\mathcal R_q(t,s)
+t^{-q}\frac{(t-1)^q}{1-ts}.
\]
A>q pays the apparent zero-end poles. For K=A−q+1=15N+1 the actual filtered M row has the exact decomposition
\[
(1-s)^qU_{P_d^0,0}(s)
=\mathcal P_d(s)+(-1)^q\pi\mathcal S_{d,K}(s),
\quad \deg\mathcal P_d<q,
\]
\[
\mathcal S_{d,K}(s)=\int_{-1}^1
 J_d(t)\frac{\operatorname{sgn}(t)t^K}{1-ts}d\nu_e(t).
\tag{R18}
\]
P_d is the explicitly integrated polynomial quotient term, not a discarded error. The sign is forced by the actual |t| measure.

Set R_d(t)=(1−t)^e(1−t²)^(d−1/2) and b_(d,j)=[t^j]R_d. Rodrigues is
J_d dnu_e=(−1)^d R_d^(d)dt/(2^d d! pi).
For d>K, integration by parts separately across zero gives
\[
\boxed{\mathcal S_{d,K}(s)=\mathcal E_{d,K}(s)
+\frac{2^{1-d}}{\pi d}
 \sum_{j=0}^{d-1-K}
 \frac{(-1)^j b_{d,j}}{\binom{d-1}{j}}
             s^{d-1-j-K},}
\tag{R19}
\]
\[
\mathcal E_{d,K}(s)=\frac{s^{d-K}}{2^d\pi}
 \int_{-1}^1\frac{\operatorname{sgn}(t)R_d(t)}
                      {(1-ts)^{d+1}}dt.
\]
For details, H=t^K/(1−ts) has H^(d)=d!s^(d−K)/(1−ts)^(d+1). Its derivative of order a at zero is a!s^(a−K) for a≥K. The distribution derivative of sign(t)H has jump terms
2 sum H^(d−1−j)(0) delta_0^(j).
Pairing with R_d gives (−1)^j j!b_(d,j), and the factorial ratio is 1/(d binom(d−1,j)). Endpoint terms at ±1 vanish. This proves every coefficient in R19.

At the largest degree this junction polynomial has degree 29N−3. Jacobi orthogonality cannot delete it, and no cancellation with D_mu has been proved here. For d≤K use the full integral or R16/R17; R19 is not extrapolated to lower degrees.

## 7. Two explicit bounds for the genuine Rodrigues remainder

Put w_*(s)=s/(1+sqrt(1−s²)). Maximizing
(1−t²)/(2(1−ts)) gives w_*(s)/s. Moreover int dnu_e/(1−ts)≤2^e c_e: the integral is convex in s, and its endpoint values are 2^e c_e and 2^(e−1)c_(e−1), with the latter no larger for e≥1. Therefore
\[
|\mathcal E_{d,K}(s)|\le
 2^ec_e\,s^{-K}w_*(s)^d. \tag{R20}
\]
For d>K it extends continuously at s=0.

A sharper uniform bound follows by separating t>0 and t<0. On the first use s^(d−K)≤1 and 1−ts≥1−t; on the second use 1−ts≥1 and (1−t)^e≤2^e. Then
\[
\boxed{|\mathcal E_{d,K}(s)|\le
\frac{2^{e-1}}\pi B(e-1/2,d+1/2)
+2^{e-d-1}c_d,\quad 0\le s\le1.}
\tag{R21}
\]
The first term extends a positive beta integrand to (−1,1); the second uses
int_(-1)^0 (1−t²)^(d−1/2)dt=pi c_d/2.
No numerical special-function constant is used. In the present range d>K these terms are exponentially small in N: for the beta term its leading logarithm is
e log2+e log e+d log d−(e+d)log(e+d), and e=6N,d>15N+1 makes it strictly negative. The other term has exponent (e−d)log2. The polynomial in R19 remains fully present.

Consequently the remainder contribution to column k is at most
\[
\frac{\pi}{b+k+1}
\left[\frac{2^{e-1}}\pi B(e-1/2,d+1/2)
+2^{e-d-1}c_d\right]. \tag{R22}
\]
Normalized rows must multiply this by lambda_d. This bounds the actual M remainder, not the full M-minus-D entry.

## 8. Current paid interface and remaining comparison

R14, with R15–R17 as an explicit fallback, pays the actual pure-D wedge and measures Jacobi rows after exact tail removal. R18–R22 pay the actual zero junction and give a small analytic remainder. A sharper principal determinant estimate now requires control of the residual Gram quantity T_N(mu), including the explicit junction polynomial and the actual D_mu section. Neither their alignment nor a full mixed sign-regular determinant follows from kernel positivity.

The finite-place result for this same 44N−1 matrix gives, along nonzero conditional rational determinants, red lower exponent −7849/3872; old normalization adds (743/968)log2 with the identical scalar R5. R14 currently does not prove an upper exponent below that lower bound. No numerical independence conclusion is claimed.

The separate current C-map rank argument has now been paid by its author and root: full C rank 44N−1 and restricted residual rank 36N−2. These rank statements are not assumptions used in R14. They give generic parameter information, while nonvanishing at the actual conditional relation point remains unpaid. Polynomial-pair independence is not substituted for either assertion.

For the possible 43N variant, substitute L=54N, d=9N,...,44N−1 (35N Jacobi directions), and the selected 8N tails. The analytic identities R6–R22 apply with those precise new counts, section length and weights. Here sum d=(1855N²−35N)/2. Neither the 44N−1 finite-place area nor its row-specific clearing prescription is assigned without proof to the different 43N matrix. The principal object here remains R1.

## 9. Global comparison and the next proof target

The gap can be stated with exact elementary constants. Put
\[
X(x)=\tfrac12x^2\log x-\tfrac14x^2,\qquad X(0)=0,
\]
\[
\mathscr H(a;b,c)=X(a)+X(b+a)-X(b)+X(c+a)-X(c)
 -X(b+c+2a)+X(b+c+a),
\]
\[
\mathscr B(a,c)=a\log a+c\log c-(a+c)\log(a+c).
\tag{R23}
\]
Stirling's formula applied to R10 gives
N^(-2) log H_(aN+O(1))(bN+O(1),cN+O(1)) tending to Hscript(a;b,c).
The N² log N coefficients cancel. R11 gives
\[
\limsup N^{-1}\log\mathcal C_N
\le c_*:=\mathscr B(55,2)+\mathscr B(7,4).
\]
From the gamma form of R13, uniformly for the present d/N interval,
log rho_d=6N log2+O(log N). The exact row scalar sum in R4 satisfies
\[
\log\prod_d\lambda_d^{\rm red}=3410N^2\log2+O_\mu(N\log N).
\tag{R24}
\]
The leading coefficient agrees with the finite-place normalization; all fixed rational denominators contribute only O_mu(N).

If t_*:=limsup N^(-1) log T_N(mu) is finite, R14 therefore proves
\[
\limsup N^{-2}\log|\Delta_{\rm red}|
\le G_*+18t_*,
\quad G_*:=\tfrac12\mathscr H(44;7,4)
 +\tfrac12\mathscr H(8;55,2)+4c_*+3518\log2.
\tag{R25}
\]
This is an implication, not an assumption that t_* is small. Elementary evaluation gives G_*/1936 approximately 0.30932206. By contrast, the paid finite-place lower bound for nonzero conditional determinants is −7849/3872 approximately −2.02711777 on the n² scale. Thus this trace route would require the unproved strict estimate
\[
t_*<t_{\rm crit}:=\frac{-7849/2-G_*}{18}
 \quad\text{(approximately }-251.29708\text{)}.
\tag{R26}
\]
The exact expressions R23–R26, rather than decimal approximations, define this test. If T_N were merely subexponential, this upper bound would leave a gap of approximately 2.33643983; subexponential growth itself has not been proved. Passing to bare Jacobi rows subtracts 3410 log2 from both N² exponents and leaves R26 unchanged. Row normalization cannot change this comparison.

The established small remainder R21 supplies no estimate remotely of the form R26 for the full residual trace. Its polynomial junction part, the lower d≤K rows and D_mu are still present. This is not an impossibility theorem for the determinant: AM–GM on the residual trace can lose joint singular-value cancellation. R9 retains the exact det G_R and is the more faithful next interface. A useful next proof must bound that exterior quantity, or an exact Schur determinant against a suitable weighted Jacobi column basis, while retaining D_mu and the zero junction. Any standalone polynomial junction terms must be treated in a finite moment array; dividing them by (1−s)^q need not leave them individually in H_s.

The next target is therefore a symbolic cancellation or sign/rank structure for the actual residual pencil, followed by a leading upper exponent with the same red row normalization. Repeated finite values of mu and the rational period parameter establish neither this decay nor actual-point nonvanishing. If an analysis only repeats generic-rank evidence without an estimate on the full residual exterior determinant, it should stop and change the support parameters or the kernel. If a trace lower bound contradicts R26, that exits the trace shortcut; it does not exclude the exact determinant route. No favorable leading gap has currently been paid.

## 10. Actual source and review scope

Author FULL read the ten-section contact note and Jacobi scope; original foundations.tex, real-place.tex, nonvanishing.tex and odd-primes.tex were actually read in full without truncation. This was source reading, not verification of the entire original paper or its numerical certificates. No supplied program was run. R6–R22 were newly derived for the new rows and use no old Hardy/energy constants.

The primary [NIST Jacobi norm/leading-coefficient row](https://dlmf.nist.gov/18.3#T1), [Jacobi Rodrigues row](https://dlmf.nist.gov/18.5#T1) and [finite binomial formula](https://dlmf.nist.gov/18.5#E8) were opened and those entries plus immediate notation read. Existing archived snapshots were reused; no new PDF was downloaded. Exact additional reading scope is recorded in literature/catalan_mixed_jacobi_real_place_source_scope_20261007.md.

Author FULL read and independently paper-audited all ten sections J1–J30 of the finite-place note, including the row scalars, all-prime/power bounds, digit layer, new column table and area: PASS. This does not upgrade it to moment nonvanishing. The author actually FULL reread all ten sections R1–R26. The approximate constants in section 9 were obtained by direct evaluation of the displayed elementary logarithms, not by a supplied producer or a determinant experiment.

Independent review receipt: gamma_bound actually FULL read all ten sections R1–R26 and the separate source_scope, and independently rederived the actual D_mu section/scalars, double Andreief/Cauchy alternant, selected 8N-tail projection, beta/HS Gram factors, Jacobi norm, finite fallback, sign junction coefficients, both Rodrigues bounds and all leading expressions R23–R26: mathematical PASS without repair. Its independent values G_* approximately 598.8475059 and t_crit approximately −251.2970837 agree.

Root review receipt: the root actually FULL read R1–R22 in its preceding/current continuation, then FULL read the added R23–R26 and final section 10. This segmented full reading covers the complete mathematical note, and the root independently checked all displayed formulas: mathematical PASS. The main real-place formulas were not changed to add this receipt. Neither review pays actual-point nonvanishing or the final analytic/arithmetic comparison.
