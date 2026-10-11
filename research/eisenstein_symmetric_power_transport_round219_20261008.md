# Actual symmetric-power transport: weight eight and the low-weight comparison

2026-10-08, round219. NEW paper construction. This pays the complete Bol pullback, a rational regular-singular connection, the correct oldform numerator for the actual zeta(7) Lambert carrier, and a bounded all-prime transport for its distinguished logarithmic branch. It is an explicit differential-system step, not a rational Betti/Hodge extension or a numerical irrationality theorem. No mathematical program or numerical grid was run.

## 1. Actual coordinate and the restored primitive

Use the same conventions as the new Catalan connection: q=exp(2 pi i tau), z=2 tau, theta_j(z)=theta_j(0|z), and
\[
x=\lambda(2\tau)=\theta_2(z)^4/\theta_3(z)^4,\quad
F=\theta_3(z)^2={}_2F_1(1/2,1/2;1;x),\quad P=x(1-x).
\tag{S1}
\]
The theta nome exp(pi i z) is exactly q. In particular x=16q+O(q^2); the factor two is not discarded. The normalized period satisfies
\[
L F=0,\qquad L=P D_x^2+P'D_x-\tfrac14,\qquad
\Theta=qD_q=PF^2D_x .
\tag{S2}
\]
These coordinate identities are supplied by [DLMF 23.15.1-2,6](https://dlmf.nist.gov/23.15#E6), [20.9.1-2](https://dlmf.nist.gov/20.9#E2), and [19.5.1](https://dlmf.nist.gov/19.5#E1). Here is the normalization check. Set w=log q and G_0=F w=-pi F(1-x). The exact elliptic nome relation proves this equality on the real branch. Both F and G_0 solve L. Their Wronskian is C/P, and q=x/16+O(x^2), F=1+O(x), gives C=1. Hence w'=1/(PF^2), proving S2 including its scalar.

Let s>=2 and retain the matching parity chi(-1)=(-1)^(s+1). Use the actual round218 functions
\[
K_{s,\chi}(q)=\sum_{m\ge1}{\chi(m)\over m^s}{q^m\over1-q^m},
\quad
H=K_{s,\chi}(q)+{c_0w^s\over s!},\quad \Theta^sH=E_{s+1,\chi,1}.
\tag{S3}
\]
The restored constant is c_0=-B_(s+1)/(2(s+1)) for chi=1 and zero for chi_-4. For zeta(7), c_0=1/480. Set U=F^(s-1)H. Its branch is this specified function, not an arbitrary solution of a guessed ODE. Requiring H-c_0w^s/s! to be holomorphic at q=0 with zero constant fixes all homogeneous polynomial ambiguities.

The algebraic base is the actual punctured line x=0,1,infinity of the Hauptmodul lambda(2 tau). The complete global coordinate/cusp payment is in the new Catalan note read in section8; the present construction also works locally from S1-S2.

## 2. Exact symmetric-power operator with every factor retained

Write a=P'/P, b=-1/(4P). Composition of operators is from right to left; coefficients multiply on the left. Define monic operators
\[
B_0=1,\quad B_1=D_x,\qquad
B_{j+1}=(D_x+j a)B_j+j(s-j)b B_{j-1}
\quad(1\le j\le s-1),\qquad {\cal L}_s=B_s .
\tag{S4}
\]
Thus every coefficient is specified by a finite rational recurrence. No expansion of a seventh-order operator is necessary. The leading two terms are
\[
{\cal L}_s=D_x^s+\binom{s}{2}aD_x^{s-1}+\text{lower-order terms}.
\tag{S5}
\]

For a proof of its actual symmetric-power meaning put d=s-1. If f solves f''+a f'+b f=0, the products v_j=f^(d-j)(f')^j satisfy
\[
v_j'=(d-j)v_{j+1}-j a v_j-j b v_{j-1}.
\]
Successive elimination gives B_j(f^d)=d!/(d-j)! times v_j for j<=d, and B_s(f^d)=0. Apply this to every f=cF+d_1G_0 and compare the coefficients of the two arbitrary constants. The s independent functions F^(s-1)w^j, 0<=j<s, are exactly the kernel of the monic operator S4. This proves that it is the symmetric power of the normalized Legendre equation.

On a branch where F is nonzero, the other monic operator with this same kernel is F^(s-1)(w')^s D_w^s F^(1-s). Equality follows because the difference has order at most s-1 and annihilates s independent functions. Consequently the complete pullback is
\[
\boxed{P^s{\cal L}_s\big(F^{s-1}H\big)
={E_{s+1,\chi,1}(\tau)\over F^{s+1}}=:R(x).}
\tag{S6}
\]
In particular the numerator is evaluated at tau, while F and x use 2 tau. All powers of P and F in S6 are forced by w'=1/(PF^2).

There is an even simpler polynomial recurrence. Put delta=P D_x and T_j=P^j B_j. Then
\[
T_0=1,\quad T_1=\delta,\qquad
\boxed{T_{j+1}=\delta T_j-\frac{j(s-j)}4 P T_{j-1}},
\quad T_s=P^s{\cal L}_s,\quad T_sU=R .
\tag{S7}
\]
The P' terms cancel exactly in deriving S7. It specifies an actual polynomial-coefficient differential operator over Q. For s=7 its six recurrence constants are 3/2,5/2,3,3,5/2,3/2. Induction gives 8T_7 in Z[x]<D_x>.

## 3. An explicit regular-singular rational extension

Suppose R is a rational base function, as proved for the two examples below. For 0<=j<s set Z_j=T_jU, and adjoin a constant coordinate C. The actual branch has C=1. Its full system is
\[
\begin{aligned}
Z_j'&=Z_{j+1}/P+\frac{j(s-j)}4Z_{j-1}
&& (0\le j<s-1),\\
Z_{s-1}'&=\frac{s-1}{4}Z_{s-2}+\frac{R(x)}P C,
&\qquad C'&=0,
\end{aligned}\qquad Z_{-1}=0 .
\tag{S8}
\]
This is a specified connection of rank s+1 over Q(x). The homogeneous C=0 block has rank s and is Sym^(s-1) of the Legendre module. It is the actual image of S3 through S6-S7, rather than a free extension carrying an assigned target constant.

If R is polynomial of degree at most s, S8 is regular singular at exactly the allowed base punctures. Its matrix has only simple poles at 0 and 1. At infinity use the local rational gauge V_j=x^(-j)Z_j, keeping C unchanged. The resulting coefficients are -j/x on the diagonal, x/P on the superdiagonal and j(s-j)/(4x) on the subdiagonal. The last forcing coefficient is R/(P x^(s-1)), which is O(1/x) under the stated degree bound. This proves regular singularity at infinity without hiding a gauge or asserting that the initial matrix is already logarithmic there.

For the scalar homogeneous operator the local exponents are 0 repeated s times at 0 and 1, and (s-1)/2 repeated s times at infinity. These follow from the two Legendre exponents and the displayed independent symmetric products. The extension has an additional constant quotient; its resonant logarithmic terms are retained.

## 4. Weight eight: pay the oldform, not E_8(2 tau)

Distinguish Stein's E_k, whose q coefficient is one, from the constant-one form E_k^std. For even weight eight,
\[
E_8(\tau)=\frac1{480}+\sum_{n\ge1}\sigma_7(n)q^n
=\frac1{480}E_8^{\rm std}(\tau).
\tag{S9}
\]
The Bernoulli normalization and the one-dimensional full-level spaces M_4 and M_8 are checked in [Stein, equations (2)-(3), Corollary2.15](https://wstein.org/books/modform/modform/level_one.html#structure-theorem-for-level-1-modular-forms).

For completeness the required global theta identity is paid as follows. The half-sum (theta_2(tau)^8+theta_3(tau)^8+theta_4(tau)^8)/2 is a full-level holomorphic weight-four form: the theta S and T transformations permute its terms with the common weight-four factor, and its cusp constant is one. Since dim M_4=1, it equals E_4^std. Squaring and dim M_8=1 then give E_8^std=(E_4^std)^2. This is a global modular proof, not a finite coefficient fit. The theta transformations are [DLMF20.7.27-29,31-33](https://dlmf.nist.gov/20.7#E27).

Let v=sqrt(x), with the branch at the positive cusp. Theta duplication gives
\[
\theta_3(\tau)^2=F(1+v),\qquad
\theta_4(\tau)^2=F(1-v),\qquad
\theta_2(\tau)^2=2F x^{1/4}.
\tag{S10}
\]
The first and third identities follow by setting the spatial variables to zero in [DLMF20.7.14 and 20.7.12](https://dlmf.nist.gov/20.7#E14); the quartic identity gives the second with its cusp sign. Substitution in the half-sum proves
\[
E_4^{\rm std}(\tau)=F^4(1+14x+x^2),\qquad
\boxed{\frac{E_8(\tau)}{F^8}=\frac{(1+14x+x^2)^2}{480}.}
\tag{S11}
\]
The radicals cancel. In contrast E_4^std(2 tau)/F^4=1-x+x^2, so substituting that oldform would change the actual carrier.

Thus the actual zeta(7) branch
\[
U_7=F^6\left(K_{7,1}(q)+\frac{(\log q)^7}{480\,7!}\right)
\]
satisfies the fully specified equation
\[
\boxed{480T_7U_7=(1+14x+x^2)^2.}
\tag{S12}
\]
Its cleared left operator has integer polynomial coefficients, with leading terms
\[
480P^7D_x^7+10080P^6P'D_x^6+\text{lower-order terms}.
\]
Here S7 specifies all lower terms exactly. The numerator has degree four, hence S8 gives a rank-eight regular-singular connection on the same three-puncture base.

## 5. Low chi_-4 comparison and the forced logarithms

For s=2, chi=chi_-4, c_0=0. The new Catalan note pays the global identity E_(3,chi,1)=xF^3/16. Hence R=x/16 and S7 gives
\[
T_2U=(\delta^2-P/4)U=x/16,\qquad
\boxed{LU=\frac1{16(1-x)},\quad U=FK_{2,\chi_{-4}}.}
\tag{S13}
\]
Indeed T_2=P L. Its S8 frame (U,PU',1) is rationally equivalent to the Catalan frame (U,xU',1/(1-x)). Thus the low and high transports have the same coordinate and derivative normalization.

| Actual branch | Low even beta target | Odd zeta(7) target |
|---|---|---|
| Integration depth s | 2 | 7 |
| Gauge U | FK_(2,chi_-4) | F^6H_(7,1) |
| Restored c_0 | 0 | 1/480 |
| Rational R=E/F^(s+1) | x/16 | (1+14x+x^2)^2/480 |
| Homogeneous rank / full rank | 2 / 3 | 7 / 8 |
| Highest log power at x=0 in the actual branch | 0 | 7 |

At x=0 the high extension's residue connects its length-seven homogeneous nilpotent chain to C by the nonzero R(0)=1/480. The actual seventh log term cannot be removed. Translation tau->tau+1 preserves F and x and changes H_7 by
\[
\frac1{480\,7!}\left((w+2\pi i)^7-w^7\right).
\tag{S14}
\]
It lies in the homogeneous symmetric-power span and is the retained known Tate translation data.

The holomorphic scalar F^6K_(7,1) alone would instead leave forcing (E_8-c_0)/F^8, including -1/(480F^8). S11 does not make that subtraction rational in x. Consequently the restored rank-eight solution must not be silently replaced by a single holomorphic scalar jet. The actual branch and its full logarithmic coefficient data are part of the source interface.

## 6. All-prime transport in the explicit integral parameter

Choose u=x/16. From the theta products,
\[
u(q)=q\prod_{r\ge1}
\frac{(1+q^{2r})^8}{(1+q^{2r-1})^8}\in q\mathbf Z[[q]],
\quad u'(0)=1,\quad q(u)\in u\mathbf Z[[u]] .
\tag{S15}
\]
The product follows directly from [DLMF20.4.3-4](https://dlmf.nist.gov/20.4#E3). Integral reversion follows by solving each coefficient successively in a series with leading coefficient one. It introduces no odd-prime denominator. Moreover
\[
F(16u)=\sum_{n\ge0}\binom{2n}{n}^2u^n\in\mathbf Z[[u]],
\quad \delta=u(1-16u)D_u .
\tag{S16}
\]

Let d_N=lcm(1,...,N). Since the coefficient of q^m in K has denominator dividing m^s, composition by the integral q(u) and multiplication by F^(s-1) preserve the safe scalar bound d_N^s through degree N. This is a bound, not an exact denominator minimum.

Set ell(u)=log(q(u)/u). It has zero constant, and d_N ell modulo u^(N+1) is integral by the finite formal logarithm sum. Write w=log u+ell(u). Every coefficient of the full restored U polynomial in log u, through degree N, is therefore cleared by
\[
C_s d_N^s,\qquad C_s=\operatorname{den}(c_0)\,s!
\tag{S17}
\]
when c_0 is nonzero; for the present low branch c_0=0 one may use C_2=1. In particular C_7=480*7!. The holomorphic log coefficient is exactly
\[
f_0(u)=F(16u)^6\left(K_{7,1}(q(u))+\frac{\ell(u)^7}{480\,7!}\right);
\tag{S18}
\]
it is not obtained by simply discarding the restored polynomial before transporting the coordinate.

The same safe bound clears all the distinguished weighted frame coefficients Z_j. Indeed S7 in u has recurrence correction 4j(s-j)u(1-16u), an integer polynomial. The operator delta preserves Z[[u]][log u], since delta(log u)=1-16u. Its degree-N output depends only on the degree-N input. Thus no extra integration depth is created by this rational frame.

This pays an actual all-prime/all-power transport for the chosen Frobenius coefficients: safe depth seven versus depth two. It does not compute an index for every section of the full source module, a unique deepest row, a residue kernel, or determinant nonzero. In unscaled x the factor16 contributes its explicit powers of two; the integral u parameter is used above, not an unqualified d_N^s claim in x.

## 7. Target projection and the still missing arithmetic extension

On the real branch set B=F(1-x) and t=-log q=pi B/F. The round218 finite-part proof gives K_(7,1)(e^-t)=zeta(8)/t-zeta(7)/2+O(t). The restored polynomial is (-t)^7/(480*7!), so
\[
\boxed{\lim_{x\uparrow1}\left(\frac{U_7(x)}{F(x)^6}
-\frac{\zeta(8)F(x)}{\pi B(x)}\right)=-\frac{\zeta(7)}2.}
\tag{S19}
\]
This is the actual target-period projection with the same coordinate and branch. The known leading Tate value is zeta(8)=pi^8/9450, by Stein's even-value formula and B_8=-1/30; it has not been dropped.

With y=1-x and lambda_log=log(16/y), the complementary period scale used in the Catalan note gives F=lambda_log/pi+O(y lambda_log), B=1+O(y). Substituting t=pi B/F and the finite-part error proves
\[
U_7(1-y)=\frac{\lambda_{\log}^7}{9450}
-\frac{\zeta(7)}{2\pi^6}\lambda_{\log}^6
+O(\lambda_{\log}^5).
\tag{S20}
\]
The constant16 and the retained pi^6 normalization matter. This logarithmic coefficient is not asserted to be zeta(7) itself or an equivalent numerical irrationality target; S19 is the exact normalized projection.

S8 and S12 now exhibit a rational algebraic connection over the actual modular base, with the homogeneous Sym^6 Legendre interpretation. A rational/integral Betti realization of this particular Eisenstein extension, a compatible Hodge comparison including its Tate translation and zeta(7) parameter, and an actual finite source/evaluation lattice still require construction. A solution-coefficient bound S17 does not pay the all-source hypotheses of the round218 residue-flag theorem. Nor does regular singularity pay an ordinary-point evaluation at the singular cusp x=1. Actual residue kernels on successive source lattices, unbounded determinant nonzero and a strict arithmetic/analytic comparison remain open.

The precise progress is an actual finite differential transport and depth comparison. It gives no saving or numerical theorem and does not import the old Jacobi packet. Higher weight raises the rank and logarithmic/integration depth here; it has not by itself compensated that arithmetic cost.

## 8. Reading, execution and final author scope

The current low-weight note was actually FULL read, all seven sections, at 13940 bytes, SHA256 67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39. The round218 Lambert interface used here was actually read in complete sections1-7 of its 14236-byte current file, SHA256 08de641c84b6342a6202d1a671477f8d9e9dbaeea1413a06a840780ec630e7fc; that bounded reading is not a new FULL read of its section8 or primary sources.

New selected public primary readings were DLMF23.15.1-2,6 (nome/modulus/lambda), 20.9.1-2 (theta periods), 19.5.1 (hypergeometric expansion), 20.7.5,12,14,27-29,31-33 (quartic, duplication and transformations), 20.4.3-4 (products); and Stein's official level-one page for the Bernoulli/Eisenstein normalization, Proposition2.8, Theorem2.11 and Corollary2.15. Only these selected formulas and hypotheses, not full chapters or books, are claimed read. No HTML/PDF snapshot was newly downloaded by this author.

Run ledger: mathematical programs, symbolic engines, numerical evaluators, finite matrices, parameter grids, prime scans, PSLQ, Lean and Git operations: zero. Every recurrence, gauge, leading coefficient, integer transport and comparison above was derived on paper. Tools performed public source browsing and local file discovery/read/write/byte-hash bookkeeping only. No old note, main record or manifest was edited. The final saved-file FULL author reread and byte/SHA256 identity are recorded in the handoff; they are author verification, not an independent review of this note.
