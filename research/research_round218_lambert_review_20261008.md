# Round218 Lambert carrier independent paper review

2026-10-08. Independent bounded paper audit. Mathematical program, prime-scan and numerical-grid executions: zero. Documentary reads/hashes only. The reviewer did not edit the carrier or any older mathematical note, main or manifest.

## Exact FULL reading receipt

Actually FULL read all eight sections and all displayed claims (1)–(17) of `eisenstein_lambert_period_carrier_round218_20261008.md`, first the initial version and then the entire revised saved version without truncation:

| Version | Bytes | SHA256 |
| --- | ---: | --- |
| Initial draft | 13955 | `85a54863fb445701980be3e2775084e4fecfa70d969b2939555fe302638dcf2c` |
| Revised current version | 14236 | `08de641c84b6342a6202d1a671477f8d9e9dbaeea1413a06a840780ec630e7fc` |

The revised current version passes this bounded paper audit. No necessary mathematical correction remains. The ordinary-derivative scope clarification is correct: d_N^s clears the degree-N polynomial and every degree-N Theta jet; differentiating the full K first and then truncating through N safely uses d_(N+j)^s. The explicit parity restriction and attribution of the functional-equation minus sign are also correct.

## Finite part, coefficients and analytic cocycle

The geometric-series rearrangement in (1) is absolutely convergent on compact q disks. Its integral numerator gives the all-prime/all-power scalar coefficient bound (2). It supplies no source index or determinant saving. The h(u) estimate proves the real radial finite part (3)–(5), including the O(t log(1/t)) bound at s=2. The leading period has matching parity exactly for odd zeta and even beta targets.

Stein's constant and character ordering agree with (6). The forced trivial-character polynomial in (7) restores the full modular form before applying Bol's derivative identity. The slash includes chi(d)^(-1); the modular transformation then makes the s-th derivative of P_gamma zero. Its degree at most s-1, cocycle composition and translation term (8)–(10) follow. This is a complex analytic extension datum, not a constructed rational Betti/de Rham/Hodge or arithmetic lattice.

## Boundary and Catalan reciprocity

At a primitive root of order coprime to f, the multiple-of-order sum is exactly (11). The nonmultiple terms have a uniform phase denominator bound and a finite dominated radial limit. The nonzero 1/t coefficient in (12) therefore proves a singular point at every such root. Their density yields a natural boundary and contradicts the finite ordinary-point singular set of a D-finite scalar equation. The conclusion is confined to raw q and its constant translates; it makes no assertion excluding a separately constructed algebraic modular-base model.

Independently substituting the conductor-4 functional equation gives

\[
\beta(w+2)=-(\pi/2)^{w+1}\Gamma(-w-1)
\cos(\pi w/2)\beta(-w-1).
\]

Together with zeta reflection and Gamma(w)Gamma(1-w)=pi/sin(pi w), this gives exactly the factor `-(pi/4)*pi^(2w)` in (15). The change z=-w-1 gives the sign, reciprocal argument pi^2/t and coefficient -t/(4pi) in (16).

The initial line c>1 permits absolute summation. The strip to -3/2 stays in Re(w+2)>0 for the bounded-character Abel representation; Euler–Maclaurin controls zeta there, and Stirling decay removes the horizontal integrals. Only w=1,0,-1 are crossed, with residues pi^3/(32t), -G/2 and pi*t/48. The dual transform on Re z=1/2 is justified by dominated alternating sums before summing the m^-2 kernel, so no divergent absolute character series is used. Equations (13), (16) and the positive exponential remainder bound (17) are consistent.

## Primary source and theorem scope

Actually read the saved Stein explicit-basis section with equation (4), Theorem 5.8 and its exception; the selected matching-parity special-value formula and complete chi_-4 Bernoulli Example 5.3. Actually read the DLMF primitive-character qualifier and exact equations 25.15.5–6 and 25.4.2. These are selected source passages, not FULL book or FULL proof-chain audits. Local snapshot identities were independently checked:

| Saved source under `literature/eisenstein_lambert_sources_20261008/` | Bytes | SHA256 |
| --- | ---: | --- |
| `stein_eisenstein.html` | 48189 | `b39a4ba7806d0d94aaf48971067a465fe1a01442c8fa0d45a86d9c43a7bfc95b` |
| `dlmf25_15.html` | 100871 | `7c47c4056d24881a2e5d0732a17c59155abd682397c3019a68147578c9788586` |
| `dlmf25_4.html` | 56067 | `cb568e9b18f14e2edbb5ed7d0af298e9aab41962ef4274890e82ec063d5391d5` |

The review adopts the cited modular theorem and functional equations only within their stated hypotheses. It imports no numerical irrationality theorem, global arithmetic source, Hodge comparison, residue kernel, determinant nonzero or strict arithmetic/analytic inequality. Those gates remain open in section 7. The completed claim is the uniform period carrier and its analytic interface, with exact Catalan reciprocity.
