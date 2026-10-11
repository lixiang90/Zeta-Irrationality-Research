# Parity mixed moments: a complete contact lift with a paid negative exponent

2026-10-07, round 216. NEW isolated paper note. This concerns only the q=0 parity carrier and minors containing the entire permitted tail space. It controls the complete D_C transform, including both Cauchy channels, by a genuine contact completion. It proves a uniform negative row exponent and an explicit finite determinant bound. The resulting bound does not meet the current conservative finite-place threshold. No producer, grid, numerical determinant experiment, supplied program, prime scan or historical code was run; no main or manifest was edited.

## 1. The fixed object and the determinant selections

The current authoritative eleven-section parity note P1–P19 was actually FULL read, without truncation, at 15818 bytes and SHA256 a39081cb49a101c80a6b7f69306d67fd873caebc6dbad3198c2a21dad85449d8. We retain precisely its q=0 variant:
\[
A=19N,\quad h=e=2N,\quad b=11N,\quad K=8N,
\quad n=44N-1,\quad L=55N-1,\quad m=36N-2,
\quad\delta=8N+1 .                                      \tag{L1}
\]
Thus L=A+1+m and n=m+delta. Write
\[
d\nu_h={x^{-1/2}(1-x)^{h-1/2}\over\pi}\,dx,
\quad Q_d=P_d^{(h-1/2,-1/2)}(2x-1),\quad K+1\le d\le n.
\]
The Jacobi polynomial has zero nu_h moments of every degree less than d. Put R_d=(1-x)^h Q_d and let B_d be its polynomial second-kind transform from P5. Its degree is d+h-1. There are p=36N-1 Jacobi directions; an all-tail n-row minor uses any set I of m of them and every delta tail.

The actual polynomial pair is P_d(t)=t^(2A)(1-t²)^h Q_d(t²), D_mu=−mu D_C, with fixed rational mu=16 beta/alpha. The conditional numerical goal is alpha G+beta pi²=u, alpha nonzero. The canonical arithmetic lift in x=t² is
\[
F_d^0=(1-x)^h\operatorname{trunc}_{<m}{B_d(x)\over(1-x)^h},
\qquad D_C^0=x^{A+1}F_d^0 .                              \tag{L2}
\]
Its original integer moment scalar is lambda_d=d_mu 2^(2K+2h)4^d from P11. We do not change that arithmetic normalization.

## 2. A valid Hermite completion using exactly the included tails

For an integer R with m<=R<=n define
\[
F_d^{R}(x)=B_d(x)-x^R\operatorname{Taylor}_{x=1,<h}
                         [B_d(x)/x^R],
\qquad D_C^{R}=x^{A+1}F_d^{R}.                           \tag{L3}
\]
The Taylor polynomial is regular at x=1. Consequently F_d^R has a zero of order at least h there. Also F_d^R−B_d is divisible by x^R, hence by x^m. The canonical F_d^0 has the same two properties. Since x and 1−x are relatively prime,
\[
F_d^R-F_d^0=x^m(1-x)^h H_d,
\quad\deg H_d\le n-m-1=\delta-1,
\quad D_C^R-D_C^0=x^L(1-x)^hH_d .                        \tag{L4}
\]
Indeed both F polynomials have degree at most n+h−1=46N−2. Thus L4 is exactly a combination of the permitted full tails, not an enlarged contact space. Multiplying a Jacobi row by its original lambda_d and replacing D_mu^0 by D_mu^R adds −mu lambda_d times such a tail combination. Every determinant containing all delta tails is unchanged. The comparison below is therefore a bound for the same conditional rational determinant whose arithmetic was paid using L2. An omitted-tail designated square does not receive this freedom.

We choose R=n throughout the quantitative argument. Its degree n+h−1 is still allowed; this choice does not involve a scalar gain.

## 3. The complete D kernel and its exact conjugation

Let C act on ordinary L²(0,1) with kernel (1−xy)^−1. The change x=(t−1)/(t+1), with the unitary map
\[
(Uf)(t)={\sqrt2\over t+1}f((t-1)/(t+1)),\quad t\ge1,
\]
turns C into the kernel (t+u)^−1 on [1,infinity). Schur's inequality with weight t^−1/2 gives
\[
\int_1^\infty{u^{-1/2}\over t+u}\,du
\le\int_0^\infty{u^{-1/2}\over t+u}\,du
=\pi t^{-1/2},\qquad \|C\|_{2\to2}\le\pi.             \tag{L5}
\]
The last integral follows by u=t v² and the elementary arctangent integral. The Schur bound follows directly by weighted Cauchy–Schwarz and Fubini, so no unverified operator theorem is needed.

Put f_d=x^(A+1/2)F_d^n and H_y=L²((0,1),y^(b−1/2)dy). For the complete D_C channel P14,
\[
Z_{F_d}(y)=C f_d(y)+\sqrt y\,C(\sqrt x f_d)(y).
\]
Both summands are present. Multiplication by sqrt(x), sqrt(y) and passage to H_y have norm at most one. Hence
\[
\boxed{\|Z_{F_d}\|_{H_y}\le2\pi\|f_d\|_2,\qquad
\|\hbox{actual D_mu contribution}\|_{H_y}
\le{3\pi|\mu|\over4}\|f_d\|_2.}                         \tag{L6}
\]
The factor 3/8 is exactly P14; D_mu=−mu D_C gives the displayed absolute bound. This is a bound for the entire signed polynomial lift, rather than for only B_d or one channel.

## 4. The polynomial B part with its actual degree suppression

For a polynomial S let B[S] be the divided-difference transform against nu_0. Direct division gives B[xS]=xB[S]+int S dnu_0. Orthogonality therefore implies
\[
B[x^rR_d]=x^r B_d\qquad(0\le r\le d).                    \tag{L7}
\]
The Chebyshev connection proves, for every S including nonzero constant moment,
\[
\|B[S]\|_{\omega}^2
=8(\|S\|_{\nu_0}^2-|\int S\,d\nu_0|^2)
\le8\|S\|_{\nu_0}^2,
\quad d\omega={8\over\pi}\sqrt{x(1-x)}\,dx.
\]
Let r_d=min(A,d), D_d=d+h−1+r_d, and
\[
W_{r,h}=\left({2r\over2r+h}\right)^{2r}
         \left({h\over2r+h}\right)^h,\qquad
S_D=\sum_{j=1}^{D+1}j^2={(D+1)(D+2)(2D+3)\over6}.
\]
Since int x^(2r)(1−x)^(2h)Q_d² dnu_0 <=W_(r,h)rho_d, and the shifted U_j are orthonormal for omega with sup norm at most j+1, Cauchy–Schwarz on their finite expansion gives
\[
\boxed{\|x^{A+1/2}B_d\|_2
\le\sqrt{8S_{D_d}W_{r_d,h}\rho_d}.}                     \tag{L8}
\]
Here x^(A+1/2−r_d)<=1. Every nonexponential factor is explicit. For scriptB(a,c)=a log a+c log c−(a+c)log(a+c), its uniform leading row exponent is at most scriptB(16,2)/2, because r_d/N>=8 and scriptB(a,2) decreases with a.

## 5. The endpoint compensation: signs and a finite positive beta formula

P19 yields, for 0<=ell<h,
\[
\beta_{d,\ell}={|B_d^{(\ell)}(1)|\over\ell!}
={1\over\pi}\binom{d+\ell}{\ell}
             B(d+1/2,h-\ell-1/2)>0 .                    \tag{L9}
\]
With R=n define
\[
a_{d,j}=\sum_{\ell=0}^j\beta_{d,\ell}
                  \binom{R+j-\ell-1}{j-\ell}>0,
\qquad0\le j<h.
\]
The signs of B_d^(ell)(1)/ell! are (−1)^(ell+1), and those in the Taylor expansion of x^−R are (−1)^k. Thus all terms have the same sign after using 1−x:
\[
\operatorname{Taylor}_{1,<h}(B_d/x^R)
=-\sum_{j<h}a_{d,j}(1-x)^j,
\quad F_d^n=B_d+x^R\sum_{j<h}a_{d,j}(1-x)^j.              \tag{L10}
\]
For the input compensation C_d=x^(A+1/2+R)sum_j a_(d,j)(1−x)^j one has the exact norm and the finite Minkowski bound
\[
\|C_d\|_2^2=\sum_{j,k<h}a_{d,j}a_{d,k}B(126N,j+k+1),
\]
\[
\boxed{\|C_d\|_2\le\mathcal S_{d,N}:=
\sum_{j<h}\sum_{\ell\le j}\beta_{d,\ell}
 \binom{R+j-\ell-1}{j-\ell}\sqrt{B(126N,2j+1)}.}          \tag{L11}
\]
The beta parameter 126N is exact: 2(A+R)+2=126N. These are all endpoint data through h−1. They neither omit the highest half-integer endpoint parameter nor assume that individual jets are small.

## 6. A closed uniform maximization, without a parameter grid

Use 0 log0=0. Put rho=d/N, t=j/N and v=ell/N. Uniformly over the finite allowed indices, each positive summand of L11 has logarithm N G(rho,t,v)+O(log N), where
\[
G=(\rho+v)\log(\rho+v)-v\log v
 +(2-v)\log(2-v)-(\rho+2-v)\log(\rho+2-v)
\]
\[
\hspace{8mm}+(44+t-v)\log(44+t-v)-44\log44-(t-v)\log(t-v)
 +63\log63+t\log t-(63+t)\log(63+t),                     \tag{L12}
\]
on the closed region 8<=rho<=44, 0<=v<=t<=2. Here is a complete analytic maximization. Its rho derivative is log((rho+v)/(rho+2−v)), so the maximum uses rho=8 for v<=1 and rho=44 for v>=1. Its t derivative has the sign of 63v−19t. For fixed v the maximizing t is min(2,63v/19).

For v<=38/63 the derivative along t=63v/19 is
log((rho+v)(rho+2−v)/((2−v)(19+v))). On the rho=8 branch its numerator minus denominator is 42+19v>0. For 38/63<=v<=1, t=2 and that derivative is
log((8+v)(10−v)/(v(46−v))), with numerator minus denominator 80−44v>0. The lower branch therefore increases to v=1. At v=1 the rho-dependent first line of L12 is zero, so the two branches meet continuously. For 1<=v<=2 the rho=44, t=2 derivative reduces to log((44+v)/v)>0. Thus the global maximum is exactly
\[
\boxed{C_* =G(44,2,2)
=46\log46-44\log44+63\log63-65\log65<0.}                 \tag{L13}
\]
Indeed C_* is the difference of the integrals of log x+1 on [44,46] and [63,65]; strict monotonicity proves negativity and gives
\[
2\log(44/65)<C_*<2\log(46/63)<0.
\]
This pays the joint positive convolution, not just the largest unweighted endpoint derivative.

For completeness the asymptotic error can be made a finite bound. Write k=h−ell−1>=0. The half-integer identity gives the exact factorial expression
\[
\beta_{d,\ell}={(d+\ell)!(2d)!(2k)!\over
                  \ell!(d!)^2k!(d+k)!4^{d+k}}.
\]
For every integer z>=0, with f(z)=z log z−z and f(0)=0,
|log(z!)−f(z)|<=1+log(z+1), by upper and lower integral sums of log x. Apply this to the displayed expression, the binomial in L11 and the integer beta factorials. All factorial arguments are <=132N. Replacing an argument by one differing by at most two costs at most 2(1+log(132N)); the zero argument is covered by the same bound. Counting fewer than forty factorial-error and shift units gives
\[
\log(\hbox{summand in L11})\le N G+100\log(264N).
\]
Therefore the following deliberately conservative bound holds for every N and every allowed d:
\[
\boxed{\mathcal S_{d,N}\le {h(h+1)\over2}(264N)^{100}e^{NC_*}.}
                                                                  \tag{L14}
\]
There are h(h+1)/2=2N²+N summands; no term-count factor has been dropped. The polynomial factor affects no N² exponent.

## 7. The complete actual mixed row and its uniform exponent

The exact Jacobi norm is
\[
\rho_d={\Gamma(d+h+1/2)\Gamma(d+1/2)\over
 \pi(2d+h)\Gamma(d+h)\Gamma(d+1)}
={d+h\over2d+h}c_d c_{d+h},\quad c_j=4^{-j}\binom{2j}{j}.
\]
Induction on c_(j+1)/c_j gives 1/(2sqrt j)<=c_j<=1/sqrt(j+1) for j>=1. Hence
\[
\frac1{368N}\le\rho_d\le\frac1{8N}.                     \tag{L15}
\]
In H_y the entire actual Jacobi row function is
\[
\mathcal U_d(y)=\tfrac12 TQ_d(y)+\tfrac{3\mu}{8}Z_{F_d^n}(y),
\]
where T is the whole M transform of P16. L6, L8 and L11 give the exact finite normalized bound
\[
\boxed{\|\mathcal U_d\|_{H_y}/\sqrt{\rho_d}\le\mathcal K_{d,N}:=
\tfrac12\sqrt{\pi B(2A+3/2,h-1/2)}
 +\tfrac{3\pi|\mu|}{4}
 \left(\sqrt{8S_{D_d}W_{r_d,h}}+
                         {\mathcal S_{d,N}\over\sqrt{\rho_d}}\right).}
                                                                  \tag{L16}
\]
This includes both D channels and the endpoint correction. For fixed mu it proves uniformly in all allowed d
\[
\boxed{\limsup_{N\to\infty}{1\over N}
                   \log\max_d\mathcal K_{d,N}\le C_*<0.}           \tag{L17}
\]
The M exponent is scriptB(38,2)/2. The B-part exponent is at most scriptB(16,2)/2. Both are strictly less than C_*: scriptB(16,2)/2=8log(8/9)−log9<−log9, while C_*>2log(44/65)>−log9. Polynomial factors and L15 do not alter the comparison. For mu=0 the D term vanishes; L17 is still a valid loose bound, but it is not asserted to be sharp for that different pure-Catalan branch.

## 8. Exact conjugation factors for every all-tail minor

Let H_j(a,c)=det_(0<=u,v<j) B(a+u+v+1,c+1), H_0=1. For a tail D=x^(L+a)(1−x)^h the ordinary input to the complete D operator is x^(L+a−1/2)(1−x)^h. Its input Gram is exactly H_delta(2L−1,2h). Change the delta tails to the monic orthogonal polynomials for x^(2L−1)(1−x)^(2h)dx, then divide by their positive norms. The real determinant factor is sqrt(H_delta(2L−1,2h)); every resulting tail output has H_y norm at most 3pi/4 by L6 with mu absent.

Change the n column monomials to monic orthogonal polynomials for y^(b−1/2)dy and normalize them. The factor is sqrt(H_n(b−1/2,0)). On each chosen Jacobi row divide by lambda_d sqrt(rho_d). The full pair scales by the same number. Row addition L4, followed by these changes and Bessel plus Hadamard, proves for every I of size m
\[
\boxed{|\Delta_I^{\rm mom}|\le
\left(\prod_{d\in I}\lambda_d\sqrt{\rho_d}\right)
\sqrt{H_n(b-1/2,0)H_\delta(2L-1,2h)}
\left({3\pi\over4}\right)^\delta
\prod_{d\in I}\mathcal K_{d,N}.}                         \tag{L18}
\]
All moments here are actual moments. Under the proposed relation, the original canonical integer-pair moment determinant is the same conditional rational Delta_I from P12. Tail rows have no diagonal zeta contribution on these columns, since their first original t degree is 2L and the highest selected column degree is 2L−2. Thus there is no hidden period correction when using the real tail changes. The changes claim no new integer model or free denominator improvement.

This argument uses all delta tails. It gives no statement about the principal square which omits the last tail. No row-function independence or positive kernel is being used to assert that Delta_I is nonzero.

## 9. Paid N² descent and the present conservative obstruction

Put X(x)=x²log x/2−x²/4, X(0)=0, and
\[
\mathscr H(a;b,c)=X(a)+X(b+a)-X(b)+X(c+a)-X(c)
                   -X(b+c+2a)+X(b+c+a).
\]
The beta Gram product and integral-sum Stirling formula give its usual leading exponent. Omitting any one of the p Jacobi rows changes the logarithm of the original moment scalars only by O_mu(N); hence every selection I in L18 has the same leading scalar cost 2592log2. The norm product rho costs only O(N log N). Uniformly over such selections, L18 proves
\[
\boxed{\limsup N^{-2}\log|\Delta_I^{\rm mom}|\le\mathcal R_*:=
2592\log2+\tfrac12\mathscr H(44;11,0)
 +\tfrac12\mathscr H(8;110,4)+36C_*.}                    \tag{L19}
\]
The 36C_* term is a real negative N² contribution of the complete mixed rows. It is not an M-only estimate or a normalization artifact.

The existing all-prime entry certificate P12 gives, along nonzero conditional minors, liminf N^(-2)log|Delta_I|>=−11440. L19 alone does not meet that threshold. One can establish this without a numerical scan. The monic squared norm for x^b dx is (2j+b+1)^−1 binom(2j+b,j)^−2. Bounding this binomial by 2^(ceil(2j+b)) gives scriptH(44;11,0)>=−4840log2. For the tail Gram, restrict its integral to [1/2,3/4]. The weight is at least 2^(−118N+O(1)), the interval length is 1/4, and the unweighted Hilbert Gram has leading exponent at least −2delta²log2. The affine monomial change contributes another −2delta²log2. Thus scriptH(8;110,4)>=−1200log2. Consequently
\[
\mathcal R_*\ge-428\log2+36C_*
>-428\log2-36\log9>-536>-11440.                          \tag{L20}
\]
The last comparison uses log2<1 and log9<3. This is a quantified failure of this particular upper certificate to contradict the current safe lower certificate. It is not a lower bound for the actual determinant, and it does not prove impossibility of a sharper joint exterior or finite-place estimate.

The next meaningful gain must come from the exact joint lift/input Gram and its exterior image, or a new paid joint finite-place denominator bound; it cannot come from discarding a D channel or counting a row scalar on one side only. The actual fixed relation-point nonzero condition remains separate. Even a strict new comparison would need an unbounded sequence of nonzero conditional all-tail minors.

## 10. Exact reading and review scope

This continuation actually FULL read only the stated current parity P1–P19 note as its mathematical input. Its original moment identities, canonical integral section and conservative entry certificate were retained; all completion, conjugation, beta-sum, maximization and norm/determinant formulas above were independently rederived. There was no new primary webpage or PDF reading/download, no original program execution and no reuse of a preceding carrier's cost table or Gram constants. Root separately developed a sharper exact joint minimum-input-Gram interface; none of its formulas is assumed in these lift estimates. Its later separate mathematical/source audit is recorded in [the bounded independent review](research_round216_complete_lift_joint_energy_independent_review_20261007.md).

Review receipt: root and gamma_bound each actually FULL read all ten sections L1–L20 of the 16183-byte version SHA256 32afa4d8322523707326ecadff9797067665eac03b5021359795f4b2ee59d10f and independently rederived the tail-degree freedom, Carleman conjugation and complete-channel factor, shift-B identity including its mean term, endpoint beta signs and exact term count, closed uniform maximization and conservative finite factorial error, Jacobi norm bounds, all monic-Gram/scalar factors, same-object leading comparison and method-limit scope. Both returned mathematical PASS without correction. The author also actually FULL reread that mathematical version. The final receipt-bearing author FULL reread and exact byte/SHA256 pin are recorded in the completion message. No favorable final irrationality comparison or arbitrary relation-point nonvanishing is claimed.
