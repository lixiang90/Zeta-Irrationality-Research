# A uniform Eisenstein–Lambert period carrier for odd ζ and even β

2026-10-08, round218. NEW paper derivation, after demotion of the fixed Jacobi route. The construction below gives one explicit family with rational Taylor coefficients, a proved target-period identity and an actual analytic Eichler cocycle. It covers every ζ(2r+1), r≥1, and every β(2r), r≥1, including Catalan's constant G=β(2). It proves no new irrationality theorem. A rational algebraic connection/Hodge source and its arithmetic evaluation packet are still missing; the raw q germ cannot be their asserted D-finite coordinate.

## 1. The carrier and its exact finite-jet denominators

Let χ be either the primitive trivial character of conductor f=1 or χ₋₄ of conductor f=4, where χ₋₄(m)=0 for even m and χ₋₄(2j+1)=(-1)^j. For an integer s≥2 define, on |q|<1,

\[
K_{s,\chi}(q)=\sum_{m\ge1}\frac{\chi(m)}{m^s}\frac{q^m}{1-q^m}
=\sum_{n\ge1}\frac{a_{s,\chi}(n)}{n^s}q^n,
\qquad
a_{s,\chi}(n)=\sum_{m\mid n}\chi(m)(n/m)^s\in\mathbf Z.
\tag{1}
\]

Both identities follow by absolutely expanding the geometric series on each compact q disk: the coefficient of qⁿ is Σ_{m|n}χ(m)/mˢ. No special value enters the Taylor coefficients. If d_N=lcm(1,…,N), then

\[
d_N^s K_{s,\chi}(q)\bmod q^{N+1}\in\mathbf Z[q].
\tag{2}
\]

Here a finite jet means the coefficients through degree N at q=0. The same multiplier clears the truncation of every ΘʲK, j≥0, where Θ=q∂q, since its nth coefficient is nʲa(n)/nˢ. Differentiation of the degree-N truncated polynomial introduces only integer falling factorials. If one instead differentiates the full K by ∂qʲ and then retains coefficients through degree N, the safe multiplier is d_{N+j}ˢ, since those coefficients use the original degrees through N+j. This is an upper denominator bound for this one scalar coordinate. It is not a source-lattice index, a determinant nonzero statement, or a denominator-saving theorem.

## 2. A proved finite-part extraction of every target

Put q=e⁻ᵗ, t>0, and write L(s,1)=ζ(s), L(s,χ₋₄)=β(s). Define

\[
h(u)=\frac1{e^u-1}-\frac1u+\frac12.
\]

Taylor expansion at zero and boundedness for u≥1 give |h(u)|≤C min(u,1) on u>0. Consequently

\[
K_{s,\chi}(e^{-t})
=\frac{L(s+1,\chi)}t-\frac{L(s,\chi)}2+R_{s,\chi}(t),
\quad
R_{s,\chi}(t)=\sum_{m\ge1}\frac{\chi(m)}{m^s}h(mt),
\tag{3}
\]

\[
|R_{s,\chi}(t)|
\le C\left(t\sum_{m\le1/t}m^{1-s}+\sum_{m>1/t}m^{-s}\right)
=\begin{cases}O(t\log(1/t))&s=2,\\O(t)&s>2.\end{cases}
\tag{4}
\]

The estimates are as t→0⁺; their constants may depend on s. Formula (3) is an elementary absolutely justified identity, and (4) proves the actual regularized cusp value

\[
\boxed{L(s,\chi)=-2\lim_{t\to0^+}
\left(K_{s,\chi}(e^{-t})-\frac{L(s+1,\chi)}t\right).}
\tag{5}
\]

With χ(-1)=(-1)^{s+1}, the leading L(s+1,χ) has matching parity and is a known rational multiple of πˢ⁺¹. Thus s odd≥3, χ=1 gives every odd ζ target; s even≥2, χ=χ₋₄ gives every even β target. Formula (5) separates a known leading Tate period from the actual target finite part. If α=L(s,χ) is hypothetically rational, K+α/2 is a rational germ with a fixed additional denominator; this observation supplies no analytic or arithmetic contradiction.

## 3. Exact modular normalization and the parity interface

In William Stein's q normalization,

\[
E_{k,\chi,1}(q)=c_0+\sum_{n\ge1}
\left(\sum_{d\mid n}\chi(n/d)d^{k-1}\right)q^n,
\quad
c_0=\begin{cases}-B_k/(2k)&\chi=1,\\0&\chi=\chi_{-4}.\end{cases}
\]

Restrict now to χ(-1)=(-1)^{s+1}. For k=s+1≥3, the character-parity condition is precisely χ(-1)=(-1)ᵏ; Stein's Theorem 5.8 gives the holomorphic form on Γ₀(f), with nebentypus χ. Therefore the correctly normalized identity is

\[
\boxed{\Theta^sK_{s,\chi}=E_{s+1,\chi,1}-c_0.}
\tag{6}
\]

The operator is Θˢ=(q∂q)ˢ; there is no extra q factor. For trivial χ the positive-degree part alone has a removed constant and is not being called a modular form. For χ₋₄ its constant is zero. These conventions follow directly from [Stein, equation (4) and Theorem 5.8](https://wstein.org/books/modform/modform/eisenstein.html#explicit-basis-for-the-eisenstein-subspace). The matching-parity special-value formula in the same source, with Gauss sum τ(χ₋₄)=2i, gives the known leading period; for s=2 it is β(3)=π³/32.

## 4. An actual analytic source cocycle, with its field limitation

Let τ lie in the upper half plane, \(q=e^{2\pi i\tau}\), and set

\[
H_{s,\chi}(\tau)=K_{s,\chi}(e^{2\pi i\tau})
+\frac{c_0(2\pi i)^s}{s!}\tau^s.
\qquad
\partial_\tau^sH_{s,\chi}=(2\pi i)^sE_{s+1,\chi,1}.
\tag{7}
\]

The polynomial in (7) is forced by the trivial-character constant. It is zero for the even β family. For γ=(a b;c d)∈Γ₀(f), use the twisted slash

\[
(F|_{1-s,\chi}\gamma)(\tau)
=\chi(d)^{-1}(c\tau+d)^{s-1}F(\gamma\tau).
\]

The exact chain-rule identity

\[
\partial_\tau^s\big[(c\tau+d)^{s-1}F(\gamma\tau)\big]
=(c\tau+d)^{-s-1}F^{(s)}(\gamma\tau)
\tag{8}
\]

follows by induction using ad−bc=1. Applying (8) to (7), and using the modular transformation of E, proves

\[
P_\gamma(\tau):=H|_{1-s,\chi}\gamma-H\in\mathbf C[\tau]_{\le s-1},
\quad
P_{\gamma\delta}=P_\gamma|_{1-s,\chi}\delta+P_\delta.
\tag{9}
\]

This constructs the actual analytic polynomial representation and its Eichler cocycle, rather than a freely assigned scalar coordinate. For translation T:τ↦τ+1,

\[
P_T=\frac{c_0(2\pi i)^s}{s!}\big[(\tau+1)^s-\tau^s\big].
\tag{10}
\]

In particular a nonzero translation correction in the odd ζ family is retained. Along τ=it/(2π), the added polynomial is c₀(−t)ˢ/s!, which tends to zero; (5) remains the same regularized endpoint of H. Equations (7)–(10) give a complex analytic extension datum with an s-dimensional polynomial fiber. They do not construct its rational Betti lattice, an algebraic de Rham comparison, a variation of mixed Hodge structures, or an arithmetic source evaluation. Those further identifications require actual construction and cannot be inferred from the word “Eichler.”

## 5. Dense radial singularities: the raw q germ is not D-finite

Let ρ be any primitive kth root of unity with gcd(k,f)=1. On q=ρe⁻ᵗ split the defining sum into multiples and nonmultiples of k. Complete multiplicativity gives the exact multiple part

\[
\sum_{k\mid m}\frac{\chi(m)}{m^s}
\frac{q^m}{1-q^m}
=\frac{\chi(k)}{k^s}K_{s,\chi}(e^{-kt}).
\tag{11}
\]

For k∤m, the finitely many nontrivial kth-root phases give a constant δ_k>0 such that |1−rρᵐ|≥δ_k for 0≤r≤1. Hence the nonmultiple part is uniformly bounded by δ_k⁻¹Σm⁻ˢ and has a finite radial limit by dominated convergence. Equations (3) and (11) therefore prove

\[
\boxed{K_{s,\chi}(\rho e^{-t})
=\frac{\chi(k)L(s+1,\chi)}{k^{s+1}t}+O_k(1).}
\tag{12}
\]

The leading coefficient is nonzero. For these two characters, χ(k)=±1 and L(s+1,χ)>0; positivity of β on real arguments>1 also follows directly by pairing successive terms of its alternating series. Thus these are genuine singular boundary points. Formula (12) is a simple radial pole asymptotic, not an assertion of an isolated meromorphic pole in a neighborhood already containing other singularities.

Orders coprime to f supply a dense set of roots: all orders when f=1, and all odd orders when f=4. Every open unit-circle arc therefore contains a singular point, so |q|=1 is a natural boundary. A D-finite germ over Q(q) satisfies a nonzero scalar linear differential equation with polynomial coefficients, whose leading coefficient has only finitely many zeros. At any other boundary point the ordinary-point existence theorem continues its solution across a neighborhood. This contradicts the dense singularities. Thus K, and every constant translate of it, is not D-finite over Q(q). The modular source in section 3 and the analytic cocycle in section 4 do not remove this coordinate obstruction. This conclusion concerns the raw q scalar; it does not rule out an algebraic differential model after an actually constructed modular-base coordinate and source comparison.

## 6. Catalan: a paid exact reciprocity and exponential remainder

For this section write K(t)=K_{2,χ₋₄}(e⁻ᵗ) and define the positive dual kernel

\[
\widetilde K(u)=\sum_{m\ge1}\frac1{2m^2\cosh(mu)},\qquad u>0.
\]

Then for every t>0,

\[
\boxed{K(t)=\frac{\pi^3}{32t}-\frac G2+\frac{\pi t}{48}
-\frac{t}{4\pi}\widetilde K(\pi^2/t).}
\tag{13}
\]

Here is the contour payment. Mellin inversion and absolute summation on Re w=c>1 give

\[
K(t)=\frac1{2\pi i}\int_{(c)}
\Gamma(w)\zeta(w)\beta(w+2)t^{-w}\,dw.
\tag{14}
\]

Shift to Re w=−3/2. In the closed strip, β(w+2) has polynomial vertical growth: its character partial sums are bounded, and Abel summation represents β(z)=z∫₁^∞A(x)x⁻ᶻ⁻¹dx for Re z>0. A fixed Euler–Maclaurin continuation through the fourth Bernoulli remainder gives polynomial vertical growth for ζ on Re w≥−3/2. Uniform Stirling bounds give exponential decay e⁻π|Im w|/2 for Γ, so the horizontal integrals vanish and both vertical integrals converge absolutely. The only crossed poles are w=1,0,−1, with residues β(3)/t, −β(2)/2, β(1)t/12. Their values are π³/(32t), −G/2, πt/48: β(1)=π/4 by the arctangent integral, and ζ(0)=−1/2, ζ(−1)=−1/12 by the same Euler–Maclaurin continuation.

The primitive-character equation with conductor 4 and Gauss sum 2i, together with zeta reflection, gives the meromorphic identity

\[
\Gamma(w)\zeta(w)\beta(w+2)
=-\frac\pi4\pi^{2w}\Gamma(-w-1)\zeta(1-w)\beta(-w-1).
\tag{15}
\]

The exact source formulas are [DLMF 25.15.5–6](https://dlmf.nist.gov/25.15#E5) and [DLMF 25.4.2](https://dlmf.nist.gov/25.4#E2). Their substitution cancels the sine factors; Γ(w)Γ(1−w)/Γ(w+2)=Γ(−w−1) supplies the remaining gamma factor. The odd-character factor supplies the minus sign in (15).

Put z=−w−1 in the residual integral; its line becomes Re z=1/2 and its value is

\[
-\frac{t}{4\pi}\frac1{2\pi i}\int_{(1/2)}
\Gamma(z)\zeta(z+2)\beta(z)(\pi^2/t)^{-z}\,dz.
\tag{16}
\]

For Re z>0 the Mellin transform of 1/(2cosh x) is Γ(z)β(z). This conditional character identity is justified by dominated convergence of the alternating finite sums Σ_{j=0}^M(−1)ʲe⁻⁽²ʲ⁺¹⁾ˣ, whose absolute values are at most e⁻ˣ. Summing the m⁻² kernel is then absolutely justified by Σm⁻²⁻ᴿᵉᶻ<∞. Mellin inversion on Re z=1/2 identifies (16) with the last term of (13). No divergent absolute double series on that line is used.

Finally 1/(2cosh x)≤e⁻ˣ gives the explicit error

\[
0<\widetilde K(u)\le\frac{e^{-u}}{1-e^{-u}},\qquad
\left|K(t)-\frac{\pi^3}{32t}+\frac G2-\frac{\pi t}{48}\right|
\le\frac{t\,e^{-\pi^2/t}}{4\pi(1-e^{-\pi^2/t})}.
\tag{17}
\]

Thus the Catalan endpoint has an exact reciprocal analytic comparison and an exponentially small remainder. The comparison exchanges two kernels; it is not a paid arithmetic relation between rational values and G, nor an irrationality proof.

## 7. What a genuine arithmetic carrier still has to supply

The next proof object is the modular/Eichler source of (6)–(9) on an algebraic modular base, with its actual target-period evaluation. An algebraic coordinate or Hauptmodul, a weight-compatible frame and a finite-rank connection must first be exhibited so that the chosen transformed coordinates really satisfy an algebraic differential system. Equations (1)–(17) do not exhibit that coordinate change. In particular a formal “replace q by a Hauptmodul” sentence does not transport the rational jets, denominator bound or endpoint value.

The same constructed source must then carry a rational/integral model and comparison lattice, including the known Tate leading term and the actual L(s,χ) extension parameter. One must specify its rank, source-degree filtration, every row of maximal integration depth, and the normalization of finite jet evaluation. Only after those data are fixed can its residue maps and successive source lattices be audited using the [round218 residue-flag interface](arithmetic_packet_residue_flags_round218_20261007.md). Scalar clearing (2), or a first mod-prime relation alone, cannot supply all later residue layers.

Finally one must prove the actual determinant nonzero, its analytic continuation and quantitative bounds in the same algebraic coordinate, and a strict arithmetic/analytic contradiction under the particular rationality hypothesis. No fixed Jacobi rank, window, zero count, determinant nonzero or numerical gap is transferred to this new family. The new completed result is the uniform period carrier and its analytic source interface; arithmetic promotion remains an explicit construction problem.

## 8. Source scope, executions and review status

Primary web reading in this derivation was limited to William Stein's *Modular Forms, A Computational Approach*, the Eisenstein page: equation (4), Theorem 5.8 and their normalization context; the matching-parity special-value formula and χ₋₄ Bernoulli example on that page. DLMF §25.15 was read for the series/Euler-product definitions and equations 25.15.5–6; DLMF §25.4 was read for equations 25.4.1–2. These are public author/NIST sources. No full-book read is claimed, and no new HTML/PDF source download was made or assigned a local hash. The modular theorem is used in section 3; the functional equations are used in section 6. All finite-jet, endpoint, cocycle, natural-boundary and contour arguments above were derived on paper from the displayed formulas and stated estimates.

For local scope, the author read the existing level12 Eisenstein auxiliary note and the round218 residue-packet note; they are context rather than proofs of this new carrier. No mathematical program, numerical grid, parameter search or old producer was executed. Filesystem commands only inspected local text/instructions and will read and hash this NEW Markdown file. No prior note, main report or manifest is modified. The author will report the actual full saved-file read and SHA-256 after the final revision. Independent review is pending and is not registered as completed by this note.
