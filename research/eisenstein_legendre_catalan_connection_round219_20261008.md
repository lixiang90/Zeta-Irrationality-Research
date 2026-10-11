# Catalan's Lambert carrier in an explicit rational Legendre connection

2026-10-08, round219. NEW paper construction. For the actual round218 Catalan carrier, this note constructs a genuine Hauptmodul coordinate, proves the required global modular identity, and gives a rank-three regular-singular connection over Q(x) with an explicit rational frame. Its canonical branch has an exact projection to G=β(2) at x=1. This completes an algebraic differential-system interface; it does not establish a rational Betti realization of the extension, a Hodge/source packet, or arithmetic holonomy, and proves no new irrationality theorem.

## 1. Coordinate conventions, the Legendre period and the derivative identity

Throughout q=e^{2πiτ}, z=2τ, Im τ>0. Thus the theta nome e^{πiz} is exactly q; the factor two is retained. Write θ_j(z)=θ_j(0|z), and set

\[
x=\lambda(z)=\frac{\theta_2(z)^4}{\theta_3(z)^4},\qquad
F=\theta_3(z)^2,\qquad P=x(1-x),\qquad \Theta=q\partial_q.
\tag{1}
\]

On the branch issuing from q=0, x=16q+O(q²). The classical elliptic-period identities identify

\[
F(x)={}_2F_1(\tfrac12,\tfrac12;1;x)
=\sum_{n\ge0}\frac{\binom{2n}{n}^2}{16^n}x^n,
\quad
\mathcal L F=0,
\quad
\mathcal L=P\partial_x^2+(1-2x)\partial_x-\frac14.
\tag{2}
\]

The sources are [DLMF 23.15.1–2, 6](https://dlmf.nist.gov/23.15#E6), [20.9.1–2](https://dlmf.nist.gov/20.9#E2) and [19.5.1](https://dlmf.nist.gov/19.5#E1). The equation in (2) also follows directly by comparing the displayed series coefficients, so no differential equation is inferred from a finite sample.

For 0<x<1 put B(x)=F(1−x). The exact nome relation is

\[
q=\exp[-\pi B/F].
\tag{3}
\]

Both F and B solve (2). Their Wronskian satisfies (P(FB'−F'B))'=0. Near x=0, F=1+O(x) and B=π⁻¹log(16/x)+O(x log x), by the convergent complementary-elliptic expansion [DLMF 19.12.1, 3](https://dlmf.nist.gov/19.12#E1). Its differentiated series gives PB'→−1/π. Therefore

\[
FB'-F'B=-\frac1{\pi P},\qquad
\frac{d\log q}{dx}=\frac1{PF^2},\qquad
\boxed{\Theta x=PF^2.}
\tag{4}
\]

These identities first hold on the real branch and then holomorphically on its continuation. Theta product formulas show F has no zeros in the upper half plane; hence (4) has no interior coordinate-critical point. The products used here are [DLMF 20.5.2–4](https://dlmf.nist.gov/20.5#E2).

## 2. Global modular proof and the actual Hauptmodul

Conjugation z=2τ takes Γ₀(4) to Γ(2): γ=(a b;c d) acts on z by (a 2b;c/2 d). Modulo the central −I, generators may be taken as z↦z+2 and z↦z/(2z+1). They correspond to T=(1 1;0 1) and V=(1 0;4 1) in the τ coordinate. Their generation is the ordinary even-entry Euclidean reduction for Γ(2). The theta S and T formulas [DLMF 20.7.27–29, 31–33](https://dlmf.nist.gov/20.7#E27) give

\[
F(\tau+1)=F(\tau),\qquad
F(V\tau)=(4\tau+1)F(\tau),
\]

and the corresponding weight-two rule for θ₂(2τ)⁴. The −I rule is χ₋₄(−1)(−1)=1 for F, and χ₋₄(−1)(−1)³=1 for the weight-three product. Consequently

\[
F\in M_1(\Gamma_0(4),\chi_{-4}),\qquad
A(\tau):=\frac{\theta_2(2\tau)^4\theta_3(2\tau)^2}{16}
\in M_3(\Gamma_0(4),\chi_{-4}).
\tag{5}
\]

Here cusp holomorphy is paid, not just the transformation rule. The three cusp classes are ∞, 0, 1/2, corresponding in z to ∞, 0, 1. After inversion at z=0, the product in A becomes, up to a nonzero scaling constant, θ₄⁴θ₃². After translation and inversion at z=1 it becomes θ₄⁴θ₂². Their convergent theta series have no negative cusp powers. The same transformations prove cusp holomorphy of F; a half-integral leading exponent at the irregular cusp is compatible with its character. Thus (5) holds at every cusp.

By [Stein's equation (4) and Theorem 5.8](https://wstein.org/books/modform/modform/eisenstein.html#explicit-basis-for-the-eisenstein-subspace),

\[
E:=E_{3,\chi_{-4},1}
=\sum_{n\ge1}\left(\sum_{d\mid n}\chi_{-4}(n/d)d^2\right)q^n
\in M_3(\Gamma_0(4),\chi_{-4}).
\tag{6}
\]

Both A and E have constant zero and q coefficient one, so R=A−E=O(q²). To prove global equality, suppose R≠0. Then R² is a holomorphic weight-six form of trivial character on Γ₀(4). This subgroup has index six: primitive pairs modulo 4, modulo multiplication by ±1, give six cosets. Its coset norm

\[
\mathcal N=\prod_{\gamma\in\Gamma_0(4)\backslash\mathrm{SL}_2(\mathbf Z)}
(R^2|_6\gamma)
\]

is a nonzero holomorphic full-level form of weight 36. All factors are holomorphic at ∞; the identity factor has order at least four. Hence ord∞N≥4. The full-level valence formula bounds this order by 36/12=3, a contradiction; the exact source is [Stein, Theorem 2.11](https://wstein.org/books/modform/modform/level_one.html#structure-theorem-for-level-1-modular-forms). Thus

\[
\boxed{E_{3,\chi_{-4},1}=\frac{xF^3}{16}.}
\tag{7}
\]

The coefficient comparison only initiates a proved global vanishing argument; it is not finite-coefficient recognition.

The same transformations show x is Γ₀(4)-invariant, and the theta products exclude interior zeros or poles of its defining theta constants. The identity θ₃⁴=θ₂⁴+θ₄⁴ gives x(Sz)=1−x(z), while x(z+1)=x(z)/(x(z)−1). These follow from [DLMF 20.7.5 and the cited S/T formulas](https://dlmf.nist.gov/20.7#E5). The actual cusp scalings give:

* At τ=∞, x=16q+O(q²), a simple zero.
* At τ=−1/τ', z=−2/τ', x=1−λ(τ'/2); thus 1−x has a simple zero in the width-four parameter e^{2πiτ'/4}.
* At τ=τ'/(2τ'+1), z=1−1/(2τ'+1), x=1−1/λ(2τ'+1); thus x has a simple pole in the width-one parameter e^{2πiτ'}.

There are no other cusp classes. A meromorphic function on the compactified quotient with exactly one pole of order one has degree one to P¹. Therefore x is an actual Hauptmodul, and the three punctures are exactly x=0,1,∞. The algebraic base used below is the explicit rational punctured line X=Spec Q[x,x⁻¹,(1−x)⁻¹]. This fixes the coordinate rather than merely calling q a Hauptmodul.

## 3. The actual Lambert branch and its forced gauge equation

Use the actual round218 function

\[
K(q)=\sum_{m\ge1}\frac{\chi_{-4}(m)}{m^2}\frac{q^m}{1-q^m},
\qquad J=\Theta K,\qquad U(x)=F(x)K(q(x)).
\tag{8}
\]

On the branch x=0, q(x)=x/16+O(x²), F(0)=1, and K(q)=q+O(q²). Round218 proves Θ²K=E with exactly the normalization (6). Thus (4) and (7) give

\[
\boxed{J'=\frac{F}{16(1-x)}.}
\tag{9}
\]

Since K'=J/(PF²), multiplication by the nonzero period F converts the two Θ integrations into a rational Legendre equation:

\[
\mathcal L(FK)=\frac1F(PF^2K')'
=\frac{J'}F=\frac1{16(1-x)}.
\tag{10}
\]

The equality follows by expanding the derivatives and using LF=0. It is an identity of the actual functions, not a separately selected solution of the same formal operator.

For completeness it also fixes the branch uniquely. If U=Σu_nxⁿ, equation (10) gives

\[
(n+1)^2u_{n+1}-(n+\tfrac12)^2u_n=\frac1{16},\qquad n\ge0.
\tag{11}
\]

The actual boundary normalization is u₀=0; hence u₁=1/16 and the holomorphic branch is unique. All u_n are rational. The logarithmic homogeneous solution at x=0 is excluded by holomorphy, while the remaining homogeneous F direction is fixed by u₀=0. Equality of the analytic germs then persists along continuation on the chosen universal covering branch. No additional free constant is available to replace the actual G endpoint.

## 4. An explicit rank-three rational Fuchsian connection

Set W=xU' and T=(1−x)⁻¹. The normalized actual branch satisfies

\[
\frac d{dx}\begin{pmatrix}U\\W\\T\end{pmatrix}
=A(x)\begin{pmatrix}U\\W\\T\end{pmatrix},\qquad
A(x)=\begin{pmatrix}
0&1/x&0\\
1/[4(1-x)]&1/(1-x)&1/[16(1-x)]\\
0&0&1/(1-x)
\end{pmatrix}.
\tag{12}
\]

Indeed U'=W/x, while (10) gives W'=(U/4+W+T/16)/(1−x), and T'=T/(1−x). Therefore ∇=d−A(x)dx is a specified algebraic connection on the free rank-three bundle over X. Its matrix has rational coefficients and simple poles at 0 and 1, with A(x)=O(1/x) at ∞; the connection is Fuchsian at all three punctures. In the convention A=R₀/x+R₁/(x−1), its residues are

\[
R_0=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},\quad
R_1=\begin{pmatrix}0&0&0\\-1/4&-1&-1/16\\0&0&-1\end{pmatrix},\quad
R_\infty=-R_0-R_1.
\tag{13}
\]

The actual normalized solution has U(0)=W(0)=0 and T(0)=1, interpreted by the holomorphic germ rather than ordinary-point existence at the singular x=0. More generally C=(1−x)T is constant. The kernel C=0 is the rank-two homogeneous Legendre module; the quotient is a trivial rank-one differential module. Thus (12) is an explicit extension over Q(x), and its actual branch has C=1. Equivalently U satisfies the homogeneous order-three operator

\[
\left(\partial_x-\frac1{1-x}\right)\circ\mathcal L\;U=0.
\tag{14}
\]

The frame is rational in the algebraic base, and (8)–(10) prove its relation to the actual modular carrier. The scalar period F used to define U is an analytic solution of the Legendre module, not a rational base function.

## 5. The exact x=1 period projection and its logarithmic normalization

For the real branch 0<x<1 set B=F(1−x). From (3), q=e⁻ᵗ with the exact relation

\[
t=\frac{\pi B}{F}.
\tag{15}
\]

As x→1⁻, B→1, F→+∞ and t→0⁺. Use the rigorously justified round218 reciprocity

\[
K(e^{-t})=\frac{\pi^3}{32t}-\frac G2+\frac{\pi t}{48}
-\frac{t}{4\pi}\widetilde K(\pi^2/t),
\qquad
\widetilde K(v)=\sum_{m\ge1}\frac1{2m^2\cosh(mv)}.
\]

Substitution of (15), with multiplication by F, gives the exact identity of this normalized U branch:

\[
\boxed{U(x)=\frac{\pi^2F(x)^2}{32B(x)}
-\frac G2F(x)+\frac{\pi^2}{48}B(x)
-\frac{B(x)}4\widetilde K\!\left(\frac{\pi F(x)}{B(x)}\right).}
\tag{16}
\]

The dual kernel bound 0<K̃(v)≤e⁻ᵛ/(1−e⁻ᵛ) proves the actual period projection

\[
\boxed{G=-2\lim_{x\to1^-}
\frac{U(x)-\pi^2F(x)^2/[32B(x)]-\pi^2B(x)/48}{F(x)}.}
\tag{17}
\]

In particular the known leading Tate contribution and the G multiple of the homogeneous period are distinct. This is a singular-cusp comparison of actual analytic branches.

The canonical local scale can also be displayed directly. Put y=1−x and ℓ=log(16/y). The convergent complementary-period expansion gives F(x)=ℓ/π+O(yℓ), B=1+O(y). Then πF/B=ℓ+O(yℓ), so the last term of (16) is O(y). Therefore

\[
\boxed{U(1-y)=\frac{\ell^2}{32}-\frac{G}{2\pi}\ell
+\frac{\pi^2}{48}+O(y\ell^2).}
\tag{18}
\]

This pays the finite-part normalization, including its constant 16. If one uses L=−log y instead, its linear-log coefficient is log(16)/16−G/(2π); dropping the nome scale would change the extracted coefficient. A formal Frobenius coefficient without its actual branch and scale cannot be identified with G alone.

## 6. What is completed, and what the ODE does not supply

Equations (1)–(18) complete the previously missing algebraic-coordinate step for the s=2, χ₋₄ carrier: x is an actual Hauptmodul, the source identity (7) is global, the actual branch satisfies the explicit rational rank-three connection (12), and its normalized endpoint projects to G by (17). The raw q natural boundary proved in round218 is compatible with this result: q(x) is an analytic uniformizing function, not an algebraic coordinate change of Q(q).

An algebraic connection over Q(x) and rational Taylor coefficients do not, by themselves, make its rank-three analytic extension a rational Betti local system or a variation of mixed Hodge structures. The homogeneous Legendre factor has its usual elliptic-period interpretation, but a compatible rational/integral model of this particular extension and its G comparison parameter still has to be constructed. Its source filtration, evaluation lattice, deepest rows, residue flags, and all necessary determinant nonzero and quantitative analytic bounds remain separate obligations. The endpoint x=1 is singular; an ordinary-point arithmetic theorem does not automatically apply to (17).

No denominator-saving assertion, Hodge realization, arithmetic-holonomy conclusion, or irrationality contradiction is inferred from (12) or (14). Other round219 notes handle denominator transport and higher integration depths; their eventual claims require the same normalization and actual source. No old Jacobi packet or numerical comparison is inherited by this connection.

## 7. Exact source selections, execution scope and author verification

The actual selected primary web reads were DLMF 23.15.1–2, 6 for the nome/modulus/lambda conventions; 23.17.4, 7 for the lambda expansion/product; 20.5.2–4 for zero-free theta constants; 20.7.5, 27–29, 31–33 for the theta identity and S/T transformations; 20.9.1–2 for the theta/elliptic-period relation; 19.5.1 for the hypergeometric period; and 19.12.1, 3, including d(0)=2log2, for its convergent complementary expansion. Stein's official author pages were read for equation (4)/Theorem 5.8 on the Eisenstein page and Theorem 2.11 on the level-one page. The whole book and all other DLMF sections are not claimed read. These sources are used exactly at the displayed identities above; the generator, cusp, coset-norm, Wronskian, gauge, frame, branch and projection arguments are paper derivations from them.

The author used the actual round218 Lambert note and its proved Catalan reciprocity, rather than rerunning a producer or treating a numerical fit as proof. No new HTML/PDF download was made by this author; local source identity/download scope, if separately recorded by root, is distinct from this reading scope. Mathematical program executions, symbolic checks and numerical grids in this construction are zero. Tools only performed source browsing, local filename/text inspection, and saving/reading/hashing this NEW Markdown note. No old note, main report or manifest is edited. The final handoff will state the actual full author saved-file read and SHA-256; independent review is registered only by its actual separate receipt.
