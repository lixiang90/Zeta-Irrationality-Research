# Actual Eisenstein periods and the global arithmetic-holonomy interface

2026-10-08, round220. NEW paper audit and exact structural derivation. The direct CDT route can bypass a Betti/Hodge realization. Its unpaid interface is an actual arithmetic germ packet with the required common meromorphic pullback and a strict bound in the same normalization. A hypothetical rational cusp target does not supply those properties by itself. For the present Catalan Legendre column the highest logarithmic monodromy is a concrete obstruction, independent of the arithmetic nature of G. No irrationality claim or new numerical theorem is made.

## 1. Actual reading scope and identities

The following frozen round219 mathematical notes were actually read FULL, including every displayed formula, in this round220 audit. The arithmetic note is my own earlier derivation; its rereading here is a consistency check, not a second independent mathematical review.

| File under research/ | Bytes | SHA256 |
|---|---:|---|
| eisenstein_legendre_catalan_connection_round219_20261008.md | 13940 | 67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39 |
| eisenstein_legendre_integral_flags_round219_20261008.md | 15599 | bc41296fb85c5548adae93d25cde5f9e4983f5d223ada8e6a39cd1b87b765730 |
| eisenstein_symmetric_power_transport_round219_20261008.md | 15514 | 32910f3ad35dcf3307786b75764ae024a4eaca2d32eec013e482be99e177aaee |

The actual CDT local sources and documentary reads are:

* literature/cdt2024_l2_chi_minus3.pdf: 4517169 bytes, SHA256 84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771. This is the 218-page arXiv:2408.15403v2, 16 September 2024. Complete selected pages read: pp1–5 for identity/outline; pp16–18, Theorem2.5.1 and its surrounding hypotheses; pp66–69, Definition6.0.1 and Theorem6.0.2; pp122–124, Theorem8.0.1; pp162–164, Proposition11.1.8 and the actual integral overconvergence; pp171–173, the complete §13 rational-relation application; pp193–195, complete §15.2. This is not a FULL 218-page review.
* literature/cdt2025_arithmetic_holonomy.pdf: 751610 bytes, SHA256 5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1. The actual PDF identifies arXiv:2510.04156v1, 5 October 2025, 20 pages. Complete pp1–6 were read, including §2.1/Theorem2.1 and the subsequent quantitative framework. No effective irrationality estimate is imported.
* Primary web reading: Hain, arXiv:1403.6443v3, actual PDF §13.2–13.3 and §18.3–18.4, plus the elliptic cohomology framing/limit-comparison paragraphs in §9; the v2 HTML Theorems8.1–8.2 were read separately, without mixing their numbering with v3. Brosnan–Fang–Nie–Pearlstein, arXiv:0711.0964v2, introductory definition paragraphs, §2.5, Fact2.6, Lemma2.8, Corollary2.9 and Theorem2.11. Wildeshaus, arXiv:math/0006170v1, selected introductory paragraphs specifying elliptic symbols, their differentials/regulator and the residue construction. These are selected-source reads, not FULL paper audits.

Documentary extraction, filesystem reads and SHA256 hashes are separate from mathematical execution. Mathematical programs, symbolic runs, prime scans and grids are zero. Old mathematics, main and manifests are untouched.

## 2. What CDT actually requires

The [fixed original CDT source](https://arxiv.org/abs/2408.15403v2), Theorem2.5.1, starts with Q(x)-independent f_i in Q[[x]], specified coefficient denominator types, and one holomorphic map phi:(D,0)->(C,0) for which every pulled-back germ extends to a single-valued meromorphic function on D. Each column of its nonnegative denominator array is zero on an initial block and constant on the remaining rows. Put

\[
\sigma_i=\sum_j b_{ij},\qquad
\tau(b)=m^{-2}\sum_{i=1}^m(2i-1)\sigma_i,
\quad
J(\phi)=\iint_{\mathbb T^2}\log|\phi(z)-\phi(w)|\,d\mu(z)d\mu(w).
\tag{G1}
\]

Its conclusion is m<=J(phi)/(log|phi'(0)|-tau(b)). The weaker size hypothesis log|phi'(0)|>tau(b) is allowed when all f_i are already holonomic; otherwise the stated basic theorem requires log|phi'(0)|>sigma_m. A contradiction needs the quotient strictly below the actual independent m. The [short CDT paper](https://arxiv.org/abs/2510.04156v1), §2.1/Theorem2.1, repeats precisely this direct analytic route with the holonomicity hypothesis.

Neither statement lists a geometric origin, a Betti comparison, a Hodge filtration or an admissible normal function. Therefore these cannot be imposed as extra prerequisites to direct application. The wording in arithmetic219 §7 about a needed period comparison applies to a stronger period/determinant plan; it is not a logical necessity of G1. This new clarification leaves the frozen note unchanged.

The original application pays a much more specific implication. Proposition11.1.8 forms H=aH_A+bH_B+cH_C in Q[[x]] under a rational relation between the target periods. The integral identities in Remark11.1.11 make its overconvergence across the original singularity explicit. §13 then pays the transformed denominators, independence of fourteen actual germs, a common meromorphic pullback and the strict bound. “The target is a cusp period of a rational connection” is not the replacement for any of these steps.

Added integrations must also be paid literally. In Theorem6.0.2 a factor n^e has an additional tau-sharp(e); it is not free and cannot silently be transported through a coordinate change. Likewise the finite source-index bound 33/4 below is not itself a b-array, tau(b), or a completed alternative slopes theorem.

The broader §15.2 route is distinct again. It discusses local finiteness of the entire denominator-constrained holonomic module after effective localization, then an ordinary, nonsingular special-value argument. A given rank-three rational differential system does not establish that whole-module finiteness, and a regularized logarithmic cusp coefficient is not the ordinary special value required by that argument.

## 3. The same-object finite arithmetic has been paid; the direct global packet has not

Use x=lambda(2tau), F(x)={}_2F_1(1/2,1/2;1;x), B(x)=F(1-x), and

\[
\mathcal L U=\frac1{16(1-x)},\quad
\mathcal L=x(1-x)\partial_x^2+(1-2x)\partial_x-\tfrac14,\quad U(0)=0.
\tag{G2}
\]

The actual u=x/16 frame is

\[
(\mathcal U,\mathcal V,\mathcal W)
=(U(16u),\,u\partial_uU(16u),\,(1-16u)^{-1}).
\]

All its coefficient jets through N are cleared by d_N^2; its dyadic coefficients are already integral. For the complete u-polynomial source L_D=(Z[u]_{\le D})^3 and the complete coefficient output through N=3D, arithmetic219 proves

\[
\log[L_D:L_D^{\rm int}]\le\tfrac{33}{4}D^2+o(D^2).
\tag{G3}
\]

This is actual all-prime arithmetic for a rectangular map with 3D+3 source directions and 3D+1 outputs. It provides neither a square nonzero determinant nor every graded evaluation estimate used by CDT. To insert this improvement into a new slopes proof one must pay the remaining graded maps/lowest nonzero coefficient, source norm and real-place estimate in this same u basis. An x-based capacity cannot be combined with G3 without the real coordinate/basis cost. Direct use of the original denominator-type theorem may instead use its stated coefficient caps, but then G3 cannot simply be substituted for tau.

The rank of a displayed connection matrix and the rank of the scalar packet over Q(u) must also be distinguished. Root's new obstruction note supplies an actual rank-three argument for these scalar rows. The three-dimensional connection has regular singularities at 0,1/16,infinity; this establishes holonomicity, but does not remove any branch monodromy from a pullback that crosses 1/16.

In particular, this actual packet and G3 exist unconditionally. A contradiction involving only these unconditional germs would itself be unconditional. A proposed proof under G=g in Q must specify how that hypothesis changes the actual arithmetic germs or their common analytic domain.

## 4. Exact global monodromy makes the distinction concrete

The exact paid reciprocal identity in analytic219 is

\[
U=\frac{\pi^2F^2}{32B}-\frac G2F+\frac{\pi^2}{48}B
-\frac B4\widetilde K(\pi F/B),\qquad
\widetilde K(v)=\sum_{n\ge1}\frac1{2n^2\cosh(nv)}.
\tag{G4}
\]

Near x=1 put y=1-x and ell=log(16/y). For positive real y,

\[
U(1-y)=\ell^2/32-G\ell/(2\pi)+\pi^2/48+O(y\ell^2).
\tag{G5}
\]

For a small counterclockwise loop about x=1, F changes to F-2iB and B stays fixed. This continuation can be performed in a small punctured neighborhood with Re(pi F/B)>0. There the series in G4 is normally convergent and holomorphic, and v changes by -2pi i, under which every cosh(nv) is invariant. G4, initially established on a real interval, extends by the analytic identity theorem. Thus its complete continuation, not merely an asymptotic guess, gives

\[
T_1U=U-\frac{i\pi^2}{8}F+
\left(iG-\frac{\pi^2}{8}\right)B,\qquad
(T_1-1)^2U=-\frac{\pi^2}{4}B.
\tag{G6}
\]

At x=0 the actual U and F are holomorphic and fixed, while B changes to B-2iF. The two loops generate the fundamental group of P^1 minus {0,1,infinity}. Define the following complex comparison basis in their common solution space:

\[
e_1=F,\quad e_2=iB,\quad
e_3=\frac{8i}{\pi^2}
\left[U+\left(\frac G2+\frac{i\pi^2}{16}\right)F\right].
\tag{G7}
\]

In this basis the generators act integrally:

\[
T_0:e_1\mapsto e_1,\ e_2\mapsto e_2+2e_1,\ e_3\mapsto e_3;
\qquad
T_1:e_1\mapsto e_1-2e_2,\ e_2\mapsto e_2,\ e_3\mapsto e_3+e_1.
\tag{G8}
\]

The vectors are independent: e1,e2 are independent Legendre solutions; applying L to U gives the nonzero right-hand side of G2. Hence G8 exhibits an abstract integral monodromy lattice, with no assumption G in Q. The occurrence of G in the complex comparison change is not a rationality test for G and does not identify a prescribed geometric Betti/de Rham comparison. Confusing these different rational structures would make the intended relation hypothesis disappear.

Conversely, adding any homogeneous Legendre solution to U leaves G6's second difference unchanged. Under G=g in Q, U+(g/2)F has a rational Taylor germ, but still has the quadratic logarithm in G5 and the nonzero second difference in G6. This particular relation-dependent germ therefore fails to become meromorphic across x=1.

There is also a simple global obstruction to reconstructing an extension from one local invariant. For the Legendre rank-two local system H on Y=P^1 minus {0,1,infinity}, pi_1(Y) is free on T0,T1. Their invariant lines are distinct, so H^0(Y,H)=0. Group cocycles have dimension four and coboundaries dimension two, whence dim_C H^1(Y,H)=2. Restriction to either one cusp circle lands in H/(T_i-1)H, of dimension one. It therefore has a nonzero kernel. This exact dimension argument does not say the actual Eisenstein class is undetermined after all global data are known; it says one local limit or residue alone cannot determine an arbitrary global extension.

## 5. What a stronger Eisenstein/VMHS identification would additionally mean

[Hain's actual construction](https://arxiv.org/pdf/1403.6443v3), §13.3, supplies Hodge/weight filtrations, rational periods and the relative weight filtration, rather than inferring them from one local limit. §18.3–18.4 places extension classes in global Deligne cohomology. It provides a plausible global model for these Eisenstein columns; it does not identify the exact comparison of our frame automatically.

For a proposed canonical identification the minimum remaining lemma is explicit: identify our rational differential extension with the correctly normalized Eisenstein class on the level cover, determine its rational Betti lattice/Tate powers and tangent-basepoint comparison, and check the compatible filtrations at every cusp. A character must be included or killed on a stated cover. The solution-space representation and its dual de Rham bundle must not be assigned the same weights without specifying the convention. G7–G8 alone pay none of these canonical normalization choices.

[Wildeshaus's symbol construction](https://arxiv.org/pdf/math/0006170) starts with an elliptic family and divisor/section data, uses differential and residue conditions, and compares regulator images. A claimed symbol for our target should exhibit such global data and the regulator equality; a rational local endpoint is not that input. No conditional higher-degree symbol existence result from that paper is imported.

An ordinary admissible normal function has a more restrictive definition. [Brosnan–Fang–Nie–Pearlstein](https://arxiv.org/pdf/0711.0964), §2.5/Fact2.6, identifies it as a VMHS extension of Z by a weight-minus-one variation; its underlying global cohomology class and cusp restriction are distinct from its numerical limit. This definition is not a general theorem turning any rational inhomogeneous ODE into a normal function.

In the usual cohomological Eisenstein convention, a weight-(m+2) Eisenstein extension has homogeneous term Sym^m H(m+1), of weight -m-2. The low weight-three case would have m=1 and weight -3; the zeta7 weight-eight case m=6 and weight -8. Thus the weight-minus-one normal-function theorem cannot simply be relabelled as either of these cases. An appropriate higher extension description could still exist. Neither the ordinary theorem nor a global motivic realization would by itself cancel the nonzero logarithmic monodromy in G6 or prove a strict CDT inequality.

## 6. Minimal direct lemmas and current decision

For Catalan, the useful next lemma is not “there exists some rational monodromy form”: G8 already gives one abstractly. It is a relation-dependent arithmetic cancellation lemma. Under G=g in Q, exhibit actual holonomic Q[[u]] germs, with stated coefficient bounds, whose pullbacks are meromorphic on a common disc larger in the required conformal sense, and prove their Q(u)-independence. The current three rows cannot furnish a germ involving mathcal U or mathcal V which becomes meromorphic through u=1/16; Root's separate obstruction proves the stronger rational-coefficient version. Any new construction must change the packet, projection or analytic geometry and pay that change.

For zeta7, the restored column is

\[
U_7=F^6\{K_7+c_0(\log q)^7/7!\},\qquad c_0=1/480,
\]

and has a genuine degree-seven Frobenius logarithm at the origin. It is not one holomorphic Q[[u]] germ to which G1 directly applies. The bound 480*7!*d_N^7 clears the distinguished Frobenius coefficient packet, not an independently established full-source index. The holomorphic part F^6K_7 alone does not retain the same rational forcing. To use coefficient functions of the log polynomial, one must specify the actual germ list, prove its holonomicity and independent rank, pay its exact denominator types, and obtain a common meromorphic pullback; restoration of c0 or rationality of the cusp target proves none of those statements automatically.

Accordingly, the direct CDT route remains logically available without a motivic prerequisite, but no current frozen packet satisfies a relation-dependent global contradiction. The 33/4 bound is a real finite-place advance on the specified complete u-source. The quadratic Catalan monodromy and the high-weight Frobenius origin are specific gates which survive the target rationality assumptions. A strict same-packet arithmetic/analytic comparison, with every analytic continuation condition actually checked, remains unproved.

Root's separate NEW monodromy-obstruction note was subsequently actually FULL read and independently checked: 6798 bytes, SHA256 a8f36047325f2133fac8c45477086351d441db01d0843414a7041bfba17a1c41. Its complete Frobenius recurrence, G1–G5, rational-coefficient rank argument and finite-ramification factor passed without a necessary mathematical revision; the separate receipt is [research_round220_legendre_target_obstruction_review_20261008.md](research_round220_legendre_target_obstruction_review_20261008.md). This saved global-gate note will receive a FULL author reread and exact byte/SHA256 record; that reread is not independent review.
