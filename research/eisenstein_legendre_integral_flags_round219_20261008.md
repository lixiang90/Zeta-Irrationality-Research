# Legendre period column: exact coefficients, integral jets and two residue flags

2026-10-08, round219. NEW bounded paper derivation. The [analytic companion](eisenstein_legendre_catalan_connection_round219_20261008.md) supplies the explicit column U=F(x)K(q(x)), with x=lambda(2 tau), F={}_2F_1(1/2,1/2;1;x), and the actual inhomogeneous equation below. This note proves arithmetic statements from that displayed equation and its rational initial condition. It does not derive the modular coordinate change, construct a rational Betti/Hodge lattice, or prove a numerical irrationality theorem. No mathematical program, prime grid or parameter sweep was run.

## 1. Exact column and rational Fuchs frame

Put theta=x d/dx and

\[
\mathcal L=x(1-x)\partial_x^2+(1-2x)\partial_x-\tfrac14,
\qquad
\mathcal LU=\frac1{16(1-x)},\quad U(0)=0.
\tag{A1}
\]

The unique power-series solution U=sum_(n>=0)u_n x^n satisfies

\[
(n+1)^2u_{n+1}-(n+\tfrac12)^2u_n=\tfrac1{16}.
\tag{A2}
\]

For the homogeneous analytic solution F=sum c_n x^n,

\[
c_n=\frac{\binom{2n}{n}^2}{16^n},\qquad c_0=1,
\quad (n+1)^2c_{n+1}=(n+\tfrac12)^2c_n.
\]

Divide A2 by the homogeneous recurrence and telescope from u_0=0. This proves the exact identity

\[
\boxed{u_n=c_n\sum_{j=1}^n
\frac{16^{j-1}}{j^2\binom{2j}{j}^2}.}
\tag{A3}
\]

Let V=theta U and W=1/(1-x). The complete rational frame Y=(U,V,W)^t satisfies

\[
\partial_xY=
\begin{pmatrix}
0&1/x&0\\
1/[4(1-x)]&1/(1-x)&1/[16(1-x)]\\
0&0&1/(1-x)
\end{pmatrix}Y.
\tag{A4}
\]

Its only poles are simple at 0,1 and infinity; this is a rank-three Fuchs system over Q(x). The homogeneous vector (F,theta F,0)^t satisfies the same system. A4 is a rational de Rham differential system in this explicit frame. This statement alone is not a rational Betti comparison or an arithmetic source theorem for the endpoint.

## 2. A complete all-prime coefficient certificate

For n>=1 write d_n=lcm(1,...,n). Then

\[
\boxed{16^n d_n^2 u_n\in\mathbf Z.}
\tag{A5}
\]

Proof at an odd prime p: put a=floor(log_p n). For j<=n, the carry formula is

\[
v_p\binom{2j}{j}=\sum_{e\ge1}C_e(j),\qquad
C_e(j)=\lfloor2j/p^e\rfloor-2\lfloor j/p^e\rfloor\in\{0,1\}.
\]

At e<=a, C_e(j)+1_(p^e divides j)<=1: divisibility forces C_e(j)=0. At e>a, p^e>n>=j, the divisibility indicator is zero and C_e(j)<=C_e(n). Summing these levelwise inequalities gives

\[
v_p\binom{2j}{j}+v_p(j)-v_p\binom{2n}{n}\le a.
\tag{A6}
\]

Each summand after multiplying A3 by 16^n d_n^2 therefore has nonnegative p-valuation. This includes every odd prime and power, including carry levels above n.

At 2, v_2 binom(2j,j)=s_2(j), the binary digit sum. Put a=floor(log_2 n). The valuation of that same cleared summand is

\[
4(j-1)+2\{a-v_2(j)+s_2(n)-s_2(j)\}\ge2(j-1)\ge0,
\]

because v_2(j)<=a, s_2(n)>=1 and s_2(j)<=j. This proves A5 at 2 as well. No cancellation between summands is needed.

For complete coefficient jets through N, the single integer

\[
M_N=16^N d_N^2
\tag{A7}
\]

clears all three coordinates U,V,W. The factor n in V_n=n u_n is integral. It also clears F and theta F; in fact 16^N suffices for those homogeneous coordinates. Theta derivatives retain the same multiplier. Ordinary differentiation of an already degree-N polynomial also retains it; differentiating a full series j times before truncation through N safely uses 16^(N+j)d_(N+j)^2. A7 is an all-prime/all-power upper bound, not an optimized determinant denominator.

There is a better explicit integral coordinate. Put u=x/16 and

\[
\mathcal U(u)=U(16u)=\sum b_nu^n,\quad b_n=16^nu_n,
\quad \mathcal V=\theta_u\mathcal U,\quad
\mathcal W=(1-16u)^{-1}.
\tag{A7a}
\]

At an odd prime A6 already proves d_n^2 b_n integral, since 16 is a unit. At 2 each A3 summand for b_n has valuation

\[
2s_2(n)+4j-4-2v_2(j)-2s_2(j)\ge0.
\]

For j=1 this is 2s_2(n)-2. For j>=2 use v_2(j)<=j-1 and s_2(j)<=j, giving the same nonnegative lower bound. Thus b_n is itself 2-integral, and

\[
\boxed{d_n^2b_n\in\mathbf Z,\quad
d_N^2[\mathcal U,\mathcal V,\mathcal W]_{\le N}
\text{ has integral coefficients}.}
\tag{A7b}
\]

The homogeneous coordinates F(16u)=sum binom(2n,n)^2 u^n and theta_u F(16u) are globally integral. The actual scaled frame satisfies

\[
\partial_u
\begin{pmatrix}\mathcal U\\\mathcal V\\\mathcal W\end{pmatrix}
=
\begin{pmatrix}
0&1/u&0\\
4/(1-16u)&16/(1-16u)&1/(1-16u)\\
0&0&16/(1-16u)
\end{pmatrix}
\begin{pmatrix}\mathcal U\\\mathcal V\\\mathcal W\end{pmatrix}.
\tag{A7c}
\]

This remains a rational rank-three Fuchs system, now with poles 0,1/16,infinity. All finite-source statements below use the actual u frame and u-polynomial source. At odd p, x=16u changes source and jet bases by local units, so the x computations transfer exactly. At 2 the scaled frame is integral without any multiplier. A real-place source basis or analytic bound in x is not carried across this change for free.

## 3. The precise Hasse identity and field distinction

Fix an odd prime p, put h=(p-1)/2, and reduce the p-integral F in F_p[[x]]. Lucas' theorem applied to binom(2n,n), with its zero carry cases included, gives

\[
\overline F(x)=H_p(x)\overline F(x^p)
=H_p(x)\overline F(x)^p,
\quad
H_p(x)=\sum_{j=0}^{h}\binom hj^2x^j.
\tag{A8}
\]

Indeed the low base-p digit j>h produces a carry and a zero coefficient; when j<=h, Lucas separates the higher digits, and 16^p=16 in F_p. Also c_j= ((1/2)_j/j!)^2 reduces to binom(h,j)^2 for j<=h. Thus H_p has degree h, H_p(0)=1, and

\[
H_p(1)=\binom{p-1}{h}=(-1)^h\ne0\quad\text{in }\mathbf F_p.
\tag{A9}
\]

Differentiating A8 in characteristic p proves

\[
\boxed{\overline F'/\overline F=H_p'/H_p\in\mathbf F_p(x).}
\tag{A10}
\]

This is a rational logarithmic derivative, not rationality of F. In fact F^(p-1)=1/H_p. The polynomial H_p solves the reduced homogeneous equation, and has simple roots: none is 0 or 1 by A9; at another repeated root the ordinary-point equation recursively forces every Taylor coefficient to vanish, since deg H_p=h<p. Hence 1/H_p has a pole of order one at a root. It cannot be the (p-1)-st power of a rational function. Thus the chosen formal F lies in an algebraic extension of F_p(x), not in F_p(x) itself.

Moreover U is not globally p-integral: section 4 proves v_p(u_p)=-2. Consequently A8–A10 do not define an unscaled mod-p U or transport a whole-source kernel from a different carrier. Integral model, source filtration and finite cutoff must be specified first.

## 4. The actual first bad coefficient is a unit at depth two

For every odd p, A3 implies u_n is p-integral when n<p. In this range j and 16 are units, and v_p binom(2j,j) is either zero or one according as j<(p+1)/2 or j>=(p+1)/2. This carry is monotone for j<=n<p, so every A3 summand is p-integral.

Use the homogeneous F to form the actual Wronskian expression

\[
B=F\,\theta U-U\,\theta F.
\]

A1 and the homogeneous equation give the exact formal identity

\[
\boxed{(1-x)B=\frac1{16}\int_0^x\frac{F(t)}{1-t}\,dt.}
\tag{A11}
\]

The integration constant is zero. The integrand has p-integral coefficients. Through degree p, the integral's only possible p-denominator is its x^p term; multiplying that coefficient by p gives (1/16) sum_(j=0)^(p-1)c_j modulo p. On the left, the only nonintegral contribution to the coefficient of x^p in B is p u_p, since all smaller u_n and all F coefficients are p-integral. Thus A9 and A11 prove

\[
\boxed{p^2u_p\equiv\lambda_p:=(-1)^h/16\ne0\pmod p,
\qquad v_p(u_p)=-2.}
\tag{A12}
\]

This is an exact uniform arithmetic statement, not a nonzero guess from a prime scan. The recurrence A2 now determines the whole leading layer through degree 2p-1: after multiplying by p^2, every n=p+k with 1<=k<p has unit denominator and follows the homogeneous recurrence modulo p. Together with the vanishing coefficients below p, this gives

\[
\boxed{[p^2U]_{<2p}\equiv\lambda_p x^pH_p(x),\qquad
[p^2V]_{<2p}\equiv\lambda_p x^p\theta H_p(x)
\pmod{(p,x^{2p})}.}
\tag{A13}
\]

The unscaled U is not reduced here. Only its cleared finite jet is reduced.

## 5. A complete finite-source kernel and exact second flag

Let N/2<p<=N be odd, so a=v_p(d_N)=1, and put m=N-p+1. Fix D>=0 and the explicit free source

\[
L_D=(\mathbf Z_p[u]_{\le D})^3,\quad n_D=3(D+1),
\quad J_N=\mathbf Z_p[u]/(u^{N+1}).
\]

Evaluate the entire source against the entire actual frame by

\[
E_N(a,b,c)=[a\mathcal U+b\mathcal V+c\mathcal W]_{\le N}
\in\mathbf Q_p\otimes J_N.
\tag{A14}
\]

All source directions and all jets 0,...,N are retained. A7b makes T=p^2E_N integral at this p. Put H-tilde_p(u)=H_p(16u) and mu_p=16 lambda_p=(-1)^h in F_p. Its actual first residue map is

\[
T(a,b,c)\bmod p
=\mu_p u^p[a\widetilde H_p+b\theta_u\widetilde H_p]
\bmod u^{N+1}.
\tag{A15}
\]

This pays the complete kernel on this source. Its rank obeys

\[
\rho_0\le\min\{2(D+1),D+h+1,m\}.
\tag{A16}
\]

Every c-direction is in the kernel. If D>=h, an additional explicit polynomial syzygy is (a,b,c)=(-theta_u H-tilde_p,H-tilde_p,0), and all its multiples of degree at most D-h. Its coefficients are lifted integrally before using A15. None of these statements assumes an isolated raw coordinate is a whole-source packet.

There is also an exact two-layer theorem under either of the following sufficient conditions:

* D>=N-p=m-1;
* D>=h-1 and N-p<=D+h.

\[
\boxed{v_p[L_D:L_D^{\rm int}]=2m,
\qquad \rho_0=\rho_1=m,}
\quad
L_D^{\rm int}=\{v:E_N(v)\in J_N\}.
\tag{A17}
\]

Proof: coefficients of mathcal U,mathcal V below p are integral, and all coefficients through N have depth at most two. Therefore the image modulo integral jets lies in

\[
(J_N+p^{-2}u^pJ_N)/J_N
\simeq p^{-2}u^pJ_N/u^pJ_N,
\]

a group of order p^(2m). Under the first condition, multiplication of mathcal U by polynomials of degree at most m-1 gives full first residue rank m because H-tilde_p(0)=1. This can also be seen integrally: remove the entire integral polynomial [mathcal U]_<p; the high coefficients of its remaining product give a triangular map with diagonal p^2b_p, a unit by A12 and 16^p a p-adic unit.

Under the second condition, gcd(H-tilde_p,theta_u H-tilde_p)=1 by the simple-root proof of section 3 and H-tilde_p(0)=1. The polynomial map (a,b) -> aH-tilde_p+b theta_u H-tilde_p, with deg a,deg b<=D, has kernel (-theta_u H-tilde_p,H-tilde_p)R of dimension (D-h+1)_+. For D>=h-1 its image dimension is exactly D+h+1, equal to the dimension of every polynomial of degree at most D+h. Thus it is onto that whole polynomial space. Since m-1<=D+h, truncation then fills every one of the m high residue jets in A15.

In either case, the image modulo integral jets surjects onto the reduction modulo p of (Z_p/p^2)^m. Lifts of m residue basis vectors give an m-square coefficient matrix invertible over Z_p; equivalently apply the elementary finite-module Nakayama argument. Hence the image is the entire group, has exactly p^(2m) elements, and its kernel is L_D^int. The exact residue-flag formula on this same T and cutoff gives rho_0+rho_1=2m; since rho_0=m, also rho_1=m.

Equivalently define L_0=L_D, L_1={v:T(v) in p J_N}, L_2=L_D^int. Each map delta_k:L_k/pL_k -> J_N/pJ_N is v -> p^(-k)T(v) modulo p, for k=0,1. A17 concerns these successively changed source lattices. It does not reapply an unchanged first-layer congruence. Compared with the uniform entry cap p^2 on n_D directions, both flags have actual kernel dimension n_D-m. For p>N, the entire frame jet is integral and the local index is zero. At 2 the scaled frame is integral at every cutoff and its local index is zero. Smaller odd primes and higher powers retain the complete cap A7b; no optimized small-prime index is asserted.

## 6. A same-source all-prime certificate at N=3D

For D>=1 choose N=3D and keep the full source and complete coefficient jet of section 5. All odd primes N/2<p<=N satisfy one of A17's two conditions. If p>=N-D, the first applies. If p<N-D=2D, then D>=h-1, and N-p<=D+h follows from p>3D/2 (the finitely small D=1 case is already in the first condition).

The global rational source is L_Z=(Z[u]_(<=D))^3 with the same E_N in A14. Let L_Z^int be the sublattice whose complete jet is integral. Put d_N^odd=d_N/2^(v_2(d_N)). The row-wise fallback, retaining mathcal W unscaled and using actual 2-integrality, has index (d_N^odd)^(4(D+1)). At each odd prime in the paid window its fallback exponent is 4(D+1), whereas A17 gives the exact exponent 2(N-p+1). Consequently the finite integer

\[
\mathcal C_D=
\frac{(d_N^{\rm odd})^{4(D+1)}}{
\displaystyle\prod_{\substack{N/2<p\le N\\p\ {\rm odd\ prime}}}
p^{4(D+1)-2(N-p+1)}}
\quad(N=3D)
\tag{A18}
\]

is a complete index certificate: [L_Z:L_Z^int] divides C_D. Its exponent is nonnegative at every prime. Its 2-exponent is zero; every outside odd prime and power retains the original all-power d_N cap. There is no missing finite-place term. This is a rectangular finite-jet lattice statement, not a numerical determinant statement.

Using log d_N=N+o(N) and the weighted PNT, the paid odd-prime gain is

\[
\sum_{3D/2<p\le3D}\{2p-2D+2\}\log p
=D^2\int_{3/2}^3(2x-2)\,dx+o(D^2)
=\tfrac{15}{4}D^2+o(D^2).
\tag{A19}
\]

The constant 2 per prime costs O(D). Since removing the power of 2 from d_N costs only O(log N), the complete scaled-frame fallback has leading 12D^2. Therefore

\[
\boxed{\log[L_Z:L_Z^{\rm int}]
\le\log\mathcal C_D
=\tfrac{33}{4}D^2+o(D^2).}
\tag{A20}
\]

Only the stated window and exact frame/source are optimized. A19 is not a sweep, not a necessary arithmetic cost, and not a strict comparison with an analytic determinant bound.

## 7. Scope of the new arithmetic result

The source in A14 is the stated u-polynomial filtration of the complete explicit rational Fuchs frame. Its finite-jet integral lattice and the two-layer index in A17 are actual same-object constructions. The coordinate change x=16u and its integral source basis have been paid at every finite prime, including 2. Any real-place norm/capacity, endpoint projection and source normalization must also use this same u frame, rather than silently borrowing an x-polynomial estimate. The index saving A20 does not pay that analytic change. The construction does not identify a rational Betti source, transport the Tate subtraction or endpoint comparison, determine a numerical square determinant, or prove nonzero along an unbounded sequence. An output with N+1 coordinates is deliberately allowed to be rectangular; no finite-jet injectivity is presumed.

The [round218 residue-flag note](arithmetic_packet_residue_flags_round218_20261007.md) supplies the elementary index identity used at the last step, not a genuine-source rank-nullity hypothesis for this new frame. No R6 kernel or one-layer area from the fixed Jacobi carrier is imported. A10 alone would be insufficient: the actual unit A12 and the supported cleared residue A13 are what pay A15–A17.

For a numerical irrationality argument, the same explicit algebraic source still needs its period comparison/integral model, an appropriate nonzero evaluation determinant, compatible finite-place estimates beyond this bounded prime range, and a strict arithmetic/analytic comparison in the same normalization. This note proves none of those remaining gates.

The author will FULL read the final saved seven-section file and record its bytes and SHA256. The derivation uses only exact recurrence algebra, carry/Lucas identities, a formal Wronskian integral, finite-lattice linear algebra and the weighted PNT. Mathematical executions, numerical evaluations and prime scans are zero; documentary filesystem reads/hashes are separate. No old note, main or manifest was edited. Independent review is pending.
