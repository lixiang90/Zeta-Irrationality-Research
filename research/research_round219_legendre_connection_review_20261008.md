# Round219 independent review: actual Catalan Legendre connection

2026-10-08. Independent paper review by the dual-audit agent. Verdict: PASS for the stated algebraic differential-system and actual endpoint projection claims. No correction to the reviewed mathematical note is required. This is not an arithmetic source, Betti/Hodge, saving, or irrationality certificate.

## 1. Exact version and full reading scope

The reviewed file is `research/eisenstein_legendre_catalan_connection_round219_20261008.md`: **13940 bytes**, SHA256 **67586f910a830e0fa458529c0d0b0eedab06a8550e512ffbb0a4a228b87cda39**. I actually FULL read all seven sections, equations (1)-(18), every proof paragraph and the source/execution limitations. After completing my separate high-weight construction and an author saved-file read, I performed the requested independent final FULL reread at this same identity. No section of this main note was omitted. Its author is another agent; my author verification of the high-weight note is not being substituted for independent review here.

The retained round218 interface is `research/eisenstein_lambert_period_carrier_round218_20261008.md`: 14236 bytes, SHA256 08de641c84b6342a6202d1a671477f8d9e9dbaeea1413a06a840780ec630e7fc. It was previously actually read in complete sections 1-7; for this endpoint audit I additionally reread its entire section 6, including equations (13)-(17), contour shift, transformed residual integral and positive dual-kernel bound. This is not a new FULL read of its section 8 or of all primary sources.

## 2. Global modular identity and Hauptmodul

The conjugation matrix sends Gamma_0(4) to Gamma(2), with the generators and central -I retained. Applying the theta S/T rules to z/(2z+1) gives F(V tau)=(4 tau+1)F(tau), with the compatible weight-two rule for theta_2^4. The -I factors are compatible with the odd character for weights one and three. The theta products transformed at all three cusps have nonnegative powers; the half-integral exponent at the irregular cusp is allowed by the character. Thus A=theta_2(2 tau)^4 theta_3(2 tau)^2/16 is a genuine holomorphic weight-three form with the claimed character, rather than only a transformation identity in the upper half plane.

Stein's actual E_(3,chi_-4,1) convention has coefficients sum_(d|n) chi_-4(n/d)d^2, conductor product four, zero constant and matching parity. It agrees with the differentiated Lambert series. If R=A-E were nonzero, R^2 would be holomorphic weight six with trivial character and cusp order at least four at infinity. The index-six coset norm is a nonzero full-level holomorphic form of weight 36. Every other factor contributes nonnegative order at infinity, so its order is at least four; valence permits at most three. This proves E=xF^3/16 globally. Comparing the first coefficients here is part of a paid vanishing argument.

The displayed scalings pay a simple zero of x at tau=infinity, a simple zero of 1-x at tau=0, and the unique simple pole of x at tau=1/2, in widths 1,4,1 respectively. In particular at the last cusp lambda(2 tau'+1) has leading -16 exp(2 pi i tau'), so 1-1/lambda has a simple pole. Interior theta constants do not vanish. These facts prove degree one of the compactified quotient map to P^1, hence an actual Hauptmodul with exactly the stated punctures. The rational base Spec Q[x,x^-1,(1-x)^-1] is explicit.

## 3. Derivative, actual branch and rational equation

The nome is exp(pi i z)=exp(2 pi i tau), so no factor two is lost. The complementary-period expansion gives P(FB'-F'B)=-1/pi. Differentiating log q=-pi B/F consequently gives (log q)'=1/(PF^2), and Theta x=PF^2 with precisely the stated scalar.

For the actual functions K,J=Theta K and U=FK, the global identity implies J'=F/[16(1-x)]. Expanding the product using LF=0 gives L(FK)=J'/F, hence L U=1/[16(1-x)]. This is the actual image of the Lambert branch. The full coefficient recurrence (n+1)^2 u_(n+1)-(n+1/2)^2 u_n=1/16 is correct. Holomorphy and u_0=0 fix the logarithmic and F ambiguities, respectively; u_1=1/16 agrees with q=x/16+O(x^2). An arbitrary homogeneous addition cannot replace its endpoint parameter.

## 4. Frame, residues and regular singularity

For W=xU' and T=(1-x)^-1, direct paper elimination gives W'=(U/4+W+T/16)/(1-x) and T'=T/(1-x). Every entry of (12), both finite residues in (13), and R_infinity=-R_0-R_1 have the correct sign and scalar. The matrix is O(1/x) at infinity, so this particular rational frame itself is Fuchsian at all three punctures. The branch is normalized by its holomorphic germ at the singular x=0.

The quotient coordinate C=(1-x)T is constant. Its kernel is the homogeneous rank-two Legendre module, and its actual value is one. The third-order operator (D_x-1/(1-x)) composed with L annihilates U because the actual forcing has that logarithmic derivative. The analytic period F in the gauge is correctly distinguished from a rational base function.

## 5. Exact endpoint and log(16/y) scale

Substituting t=pi B/F into the paid round218 reciprocity and multiplying by F yields all four terms of (16): pi^2 F^2/(32B), -GF/2, pi^2 B/48 and -B Ktilde(pi F/B)/4. The positive bound on Ktilde proves the normalized limit (17), with its known leading Tate term retained.

For y=1-x, DLMF's convergent expansion with d(0)=2 log 2 gives F=log(16/y)/pi+O(y log(16/y)) and B=1+O(y). Thus the dual argument is log(16/y)+O(y log(16/y)), the dual term is O(y), and (18) follows with error O(y log(16/y)^2). Replacing this scale by -log y changes the linear coefficient to log(16)/16-G/(2 pi), as stated. The paper does not identify an unnormalized Frobenius coefficient with G.

## 6. Claim boundary and independent source selections

The note pays an actual rational rank-three connection and a singular-cusp projection. It explicitly leaves a compatible rational/integral Betti model, Hodge comparison, finite source/evaluation lattice, deepest rows/residue flags, determinant nonzero and quantitative saving open. A rational Taylor germ alone pays none of these. Its explanation of the raw-q natural boundary is compatible with the analytic modular uniformization used here. No old Jacobi packet or numerical gate is transferred.

I checked selected primary formulas, not whole chapters: the retained DLMF 23.15.1-2,6, 20.9.1-2, 19.5.1 and 20.7.5,27-29,31-33 coordinate/period/transformation selections, and Stein's level-one Theorem 2.11. Additional actual public web reads for this independent review were [Stein equation (4), its constant case distinction and Theorem 5.8](https://wstein.org/books/modform/modform/eisenstein.html#explicit-basis-for-the-eisenstein-subspace), [DLMF 19.12.1,3 and d(0)=2 log 2](https://dlmf.nist.gov/19.12#E1), and [DLMF 20.5.2-4 at spatial argument zero](https://dlmf.nist.gov/20.5#E2). The web tool could not read the application/x-tex formula links; the successful HTML outputs displayed the complete selected formulas, which were then actually read. No formula read is claimed from the failed TeX calls. No source snapshot was downloaded by this reviewer.

A separate follow-up actually reread [DLMF 20.4.3-4](https://dlmf.nist.gov/20.4#E3). These are the specialized theta_2(0,q) and theta_3(0,q) product formulas and are correct sources for the high-weight note's S15. The equally correct general-spatial formulas 20.5.2-3 do not make that original citation an error. A temporary citation-only change in my NEW high-weight note was reversed; its original reviewed 15514-byte version and SHA256 32910f3ad35dcf3307786b75764ae024a4eaca2d32eec013e482be99e177aaee were restored, with no mathematical change. This paragraph records the extra actual 20.5 reading without labeling the correct original 20.4 citation a defect.

## 7. Execution and archive scope

Mathematical programs, symbolic engines, numerical evaluators/grids, coefficient fitting, finite matrices, prime scans, PSLQ, Lean and Git operations: zero for this review. All verification above is independent paper calculation. Tools performed only public primary browsing and local discovery/read/write/byte-hash bookkeeping. I wrote only this NEW receipt for this review and made no change to the main mathematical note, old records or manifests. The final saved receipt FULL author reread and its identity are recorded in the handoff. Any subsequently created report/manifest/reading-scope links require root's final archive check; this receipt does not claim that future check completed.
