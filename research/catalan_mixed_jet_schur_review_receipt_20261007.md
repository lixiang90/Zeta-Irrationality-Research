# Final reading receipt: mixed jet rank and actual Schur operator

Date: 2026-10-07. Author: `universal_normalization`. These are independent research notes, separate from the main manuscript, manifest, original source, and historical producers.

## 1. Final files and author reading

The author actually read all nine sections of each final saved file as complete, untruncated `Get-Content -Raw` output on this continuation and checked the displayed formulas.

| file in `E:\kimi-build\zeta5\research` | bytes | SHA256 |
|---|---:|---|
| `catalan_mixed_second_kind_jet_rank_20261007.md` | 11511 | `ddf71a65bbfdd89a007bbe6e00e80ae1a3080cb41419b771b47a67d07185ab2b` |
| `catalan_mixed_actual_moment_schur_lemma_20261007.md` | 14832 | `fc4a8fa61b1c82a1793638891bd32acd836b753923db221ef6fd377323c9a396` |

The second is the final version with sections 8–9 explicitly cross-linking the new all-N jet-rank result. Its former statement that the C rank was still unpaid no longer describes the final combined status. Its distinction between ordinary Gram positivity and second-kind jet rank remains correct.

## 2. Precise mathematical and reading scope

The complete final ten-section contact construction was actually read earlier in this continuation, and the needed original `foundations.tex` lines 54–211 were actually reread again. The original path is

`E:\codex-build\math\preprints\Catalans-constant-is-irrational-September-24-2026\build\sections\foundations.tex`.

The source defines the actual M and Z integrals at lines 54–62, convergence at 63–71, the filtered columns at 73–91, c and rational recurrences at 95–118 and 168–195, and the exact period decomposition at 197–211. No historical code was executed or invoked as a proof of the new symbolic assertions. The later finite N=1 review is recorded separately and is not a premise of an all-N theorem.

The paid results are strict total positivity of Z, invertibility of the full permitted D map, the exact rational tail Schur operator and kernel graph, all-N full rank of the second-kind C jets, and an all-N polynomial maximal minor of exact degree `m=36N-2` in the formal target parameter for every fixed mu. The exact factorization `U=C1 L_C`, `S1=C1 K` and the decomposition `D_C(Q) direct-sum D_tail=D` also pay full rank of the actual mu slope `S1+pi^2 C1/4`. The rational normal form `[v;A+mu B+rI]` and the observing-determinant equivalence are proved.

The new Toeplitz proof is independent of finite ranks: a dependence produces an error of order 58N, while the first-order ODE produces a polynomial of degree at most 58N-2 and order at least 58N-1. The resulting rational logarithmic derivative would have residue -1/2 at -1, which is impossible. No conjectured sign regularity or finite numerical extrapolation enters it.

## 3. Independent paper review

`gamma_bound` reported actual FULL reading of all nine sections of the new jet/cyclic note and actual FULL rereading of the updated nine-section Schur note, with an untruncated second tool output. The mathematical review passed without a repair. The independent checks covered:

- Toeplitz indices 14N through 58N-1, ODE degree/order, and residue -1/2.
- Restricted C rank 36N-2 and the exact degree and leading coefficient of the all-tail maximal minor.
- `U=C1 L_C`, `S1=C1 K`, the D-space decomposition, and the actual slope factor pi^2/4.
- The unique C-kernel direction, independence of v from mu and r, and the Cayley–Hamilton observing-determinant equivalence.
- The determinant degree bound `m(m-1)/2` and the distinction from the earlier designated square.

Root independently paper-checked the Toeplitz/ODE chain and restricted rank and reported PASS. This receipt does not relabel that reported paper check as a FULL reading of the current complete files; root may record its own reading scope separately.

## 4. Remaining hard gate

Generic nonvanishing can still have exceptional target values. Nothing here proves `Delta_N(mu)` is nonzero for every positive N and arbitrary fixed nonzero rational mu, or proves full rank at the arbitrary rational target `r=4u/alpha`. The earlier particular square omitting a tail row is also a separate condition.

The first-order Phi ODE uses only the infinity c kernel; it does not contain the rational M0/Z0 moment arrays. Consequently it cannot by itself establish observing cyclicity of `(v,A+mu B)`. At the level of the paid algebraic identities, a matrix `S0=C1 A0` would give v=0 and a vanishing observing determinant while preserving C rank and `S1=C1 K`. This shows precisely why a further assertion about the actual rational moment data is necessary; it is not a counterexample to those actual data.

A proof using the true inhomogeneous M0/Z0 recurrences, an appropriate positive/AT system, or direct all-N observing-determinant nonvanishing would address that hard gate. Finite checks at N=1 establish only their finite scope. Arithmetic at all primes and the real-place determinant balance remain additional obligations after moment nonvanishing.
