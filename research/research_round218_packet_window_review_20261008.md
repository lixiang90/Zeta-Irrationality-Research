# Round218 packet/window independent paper review

2026-10-08. Independent review receipt. Mathematical program and prime-scan executions: zero. Documentary file reads and SHA256 hashing only. Existing research notes, main and manifest were not edited by this reviewer.

## Exact reading receipt

Actually FULL read all six sections of each NEW note without truncation, including every displayed claim R1–R8 and W1–W14. After the author's local correction, also actually FULL reread all six sections of the revised packet:

| Note | Bytes | SHA256 |
| --- | ---: | --- |
| Packet, initial round218 version | 10533 | `2778726ebfec896f091f89dda30503ef141bc18bd7d0e1cfbd29f8bfe9b0d96a` |
| `arithmetic_packet_residue_flags_round218_20261007.md`, revised current version | 10923 | `c8b136eee92e109c669f3a7c25f59cfed94fb2a36b83552f1746f5ac7b293a64` |
| `catalan_b0_joint_window_certificate_round218_20261007.md` | 12149 | `d04548cfb3d5ffceb179f28021492e927eadb9ffcc85b1ec72e1e3a7d49b69a1` |

Read complete sections 1–4 and 6 of `catalan_b0_arithmetic_gate_round217_20261007.md` (17670 bytes, SHA256 `4cb75887e8d013b1ab4e947b805d4a29722a1c53273cf0d5dddc7090e65e71a6`) and complete sections 2–4/F4–F10 of `catalan_parity_joint_finite_places_20261007.md` (15271 bytes, SHA256 `f4400e1e72b99e57f7a830c4e390e0c8ade78505a434196233a5cba6e2fab0a0`). These are bounded input-section reads, not new FULL audits of those older notes. Also read the complete `literature/cdt_hasse_joint_gate_sources_20261007/reading_scope.md` receipt.

## Packet verdict and necessary qualifier

R1–R4 are the exact Smith/residue-flag index formula for the same finite-jet source lattice: the lifted kernel of delta_k is L_(k+1), and the index exponent is the sum of successive residue ranks. R5's saving of kappa from one mod-prime kernel is sharp in the stated diagonal example. It supplies no repeated higher-layer saving.

The rank-nullity calculation R6 and clearing argument R7 are valid under the explicit genuine-source, integral splitting, bounded reduction-degree, fixed denominator and unique-deepest-row hypotheses. Those hypotheses are not established for any current Catalan or new zeta/L carrier. The weighted PNT calculation R8 requires their stated uniformity, fixed parameters and a fixed exceptional-prime set; the one-layer guaranteed fraction remains strictly below 1/s. This is a ceiling for that guarantee, not a necessary denominator cost or an impossibility result.

The initial version needed one exact scope qualifier: R7 requires `a>=1`. Since C2 is an unrestricted fixed integer, a prime in `(N-sharp, xi D]` can have `a=0`, and the unqualified bound `sa*n_D-kappa` can be negative. The revised current version explicitly restricts R7 to `a>=1`, uses index zero/the integral baseline at `a=0`, and bounds the fixed cutoff difference by O(D log D). Independently FULL reread and checked this correction: it preserves R8's D-squared term and removes the endpoint issue. No further necessary correction was found; the revised packet's conditional paper statements pass this bounded review.

## Same-object window verdict

W4 is valid without a nonzero residue packet. F4–F7 apply to the divided integral pairs and all complete n columns. W5 counts `(J+1)/2` noncentral low columns and `(J-1)/2` common odd residue vectors, giving W6's rank loss J. W7–W8 include 2, every prime power, outside primes and the fixed gamma denominator; the mu denominator is already paid by the pair scale.

W11–W12 retain every high column. The shear sign cancels its represented V-vector in the central p-scaled residue. The remaining central rank is at most min(c,e); the local determinant loss is `2R+ell+min(c,e)`. Exact endpoint counts and vanishing residue vectors cause no problem. The PNT gains are 2622 for the main window and 89+192 for the two adjoining windows. Thus the certificate exponents 8818 and 8537, and conditional pair lower exponents -8080.5 and -7799.5, are consistent. W3's Omega division is applied once to this same E_div; overlap in the adjoining window introduces no double count. W14 is the exact Schur-complement next layer and does not establish any further defect.

## Source and theorem boundary

This review checks the independent paper calculations and their cited frozen local interfaces. It does not independently read or validate the full Long manuscript, its global source/BGG/descent/Cartier/continuation chain, CDT's entire arithmetic analytic module, or any numerical irrationality theorem. The recorded original-source reads remain the bounded author/root scopes in the source receipt. No global source or numerical theorem is imported.

Actual relation-point nonzero along an unbounded sequence and a favorable strict real/finite inequality remain unproved. These notes do not promote the fixed carrier. The packet qualifier is now paid; the remaining numerical and source gates remain open.
