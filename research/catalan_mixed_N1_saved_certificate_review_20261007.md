# Independent review of the two saved N=1 mixed certificates

Date: 2026-10-07. Reviewer: `universal_normalization`. This is a bounded finite receipt, independent of the two producer sources. It records no all-N numerical extrapolation.

## 1. Reading and execution scope

The reviewer actually read both complete Python sources as `Get-Content -Raw` tool output without truncation:

- `cdt_mixed_actual_moment_pencil_N1_20261007.py`, 8284 bytes, SHA256 `a0935ae43ceb6f5601ed8223f20facd34badeb784eae8e38a5eed0032bd78144`.
- `cdt_mixed_N1_observability_20261007.py`, 4990 bytes, SHA256 `8e4e901c9ccb39a303c8bc3fc8fbeb205178a2ac0d51bd40c5e8b264fc62e6c7`.

The original `foundations.tex` lines 54–211 were actually reread, including the integrals (57–59), integer column filter (73–91), `m` and boundary recurrences (95–118), rational starts and arrays (168–195), and period decomposition (197–204). No historical producer, numerical guard, or period approximation was executed.

Both saved JSON files were read completely into an independent parser. Every stored row coefficient array was checked for its finite support and range. Every entry of all saved coefficient matrices, Schur transforms, inverses, canonical matrices, and observing matrices used below was consumed by the independent checks. The remaining scalar metadata and inference text were displayed and read. This is complete structured parsing and verification of the recorded matrix data; it is **not** a claim to have manually read each line of the approximately 462 kB of indented number tables. The Gaussian pivot traces were not individually regenerated; their rank and determinant conclusions were independently checked.

Neither producer was imported, executed, or rerun. The new independent validator reads only their JSON files and performs finite linear algebra using Python-FLINT 0.9.0. It does not reconstruct Jacobi polynomials, the rational moment arrays, endpoint sections, or the original entries of `E0`, `E1`, and `CF`.

## 2. Source-paper audit

The first source implements exactly the reduced `N=1` parameters

\[
A=19,\ H=65,\ h=2,\ q=4,\ b=7,\ n=43,\ L=54,\ e=6.
\]

The DLMF finite binomial Jacobi formula is used with parameters `(e-1/2,-1/2)` and degrees 9 through 43. Its coefficients are reduced modulo 101 before multiplication by `4^d` and `kappa=2^56`. This is the same rational Jacobi basis up to nonzero row factors; no primitive-lattice conclusion is attached to the factors.

The kernels `C` and `HH` use the original `c_(i-j)/2` and `c_(j-i-1)/2`. The filter uses `(-1)^v binom(q,v)`. The low section solves successively for the coefficient at `b+k+q`, whose filter coefficient is 1, for `k=9,...,42`. Completion by the truncated inverse of `(1-t)^h` preserves all coefficients below `L`, starts at `t^(A+1)`, and supplies the endpoint factor. Since `h=2`, the code's `(t-1)^h` equals `(1-t)^h`. Thus `D0=D_H` and `D1=-D_C`; its recorded `E1=-(3/2)Z0(D1,.)` has the required positive sign `+(3/2)Z0(D_C,.)`.

The `m`, minus-boundary, plus-boundary, and diagonal `M0` recurrences agree with the source lines above, including starts `minus[1]=2` and the zero period starts. The harmonic formula for `Z0` agrees with lines 190–195. Every arithmetic denominator introduced in these finite arrays, the Jacobi formula, and the kernels is a unit modulo 101: their prime factors are at most 65, apart from powers of 2. The section uses integer inverse-binomial coefficients. Consequently these modular coefficient arrays have rational lifts at the stated prime.

The last nine rows are exactly pure-D tails `t^(L+r)(1-t)^h`, `r=0,...,8`. The code forms the rational pencil

\[
E0+\mu E1+\gamma CF,
\qquad \mu=16\beta/\alpha,\quad\gamma=4u/\alpha.
\]

No relation between actual periods is assumed in this calculation.

The second source reads the first saved JSON and does exact tail Schur elimination. Its normalization is a row operation: if `Csel` is the 34-by-34 selected C block, the lower canonical rows are `Csel^{-1} S0` and `Csel^{-1} S1`. The extra row subtracts its C coordinates times those lower rows. This yields the form `[v; A+mu B+gamma I]` used in the paper observing-determinant criterion. The orientation of both inverse multiplications is correct.

## 3. Independent stored-matrix results

The validator is

`E:\kimi-build\zeta5\research\catalan_mixed_saved_N1_matrix_validator_20261007.py`,

6110 bytes, SHA256 `b216a5a9b7b8134899f3a3c0c49eff52147709de41a024bb31cb8682721b98ec`. It is read-only and writes no outputs. Its completed run passed all assertions. A first development run stopped at conversion of FLINT `nmod` scalars to Python integers; after adding that adapter, the completed run passed. This was a validator type issue, not a certificate discrepancy, and neither run executed a producer.

Over `F_101` the independently checked component ranks are

\[
\operatorname{rank}E0=43,\quad
\operatorname{rank}E1=\operatorname{rank}CF
=\operatorname{rank}C1=34.
\]

The pure-D first-nine-column block has rank 9 and determinant 50. The first nine C columns and the pure-D `E1,CF` rows are zero. All nine tested full pools have rank 43. For the first 43 rows, the saved square determinants are independently reproduced:

| mu | gamma=0 | gamma=1 | gamma=-1 |
|---:|---:|---:|---:|
| 1 | 77 | 63 | 51 |
| 2 | 58 | 58 | 4 |
| -1 | 87 | 74 | 54 |

For the second certificate, the saved tail inverse, `W`, `S0`, `S1`, `C1`, selected C inverse, canonical `A,B,v`, and extra `S1` row were all recomputed from the **saved** first coefficient matrices and compared entry by entry. The selected C rows are 0 through 33; row 34 is extra. `v` is nonzero and the extra `S1` row is zero. Both `S0` and `S1` have rank 34 at this finite modulus.

For each record, every saved `J_mu=A+mu B` entry and every saved row `v J_mu^j`, `j=0,...,33`, was compared with the independent FLINT result. The observing determinants are:

| fixed mu | rank | determinant mod 101 |
|---:|---:|---:|
| 1 | 34 | 100 |
| 2 | 34 | 71 |
| -1 | 34 | 29 |
| 0 | 34 | 32 |

The first JSON's 222008 bytes have SHA256 `2ff87f2ba4236ed4ee2663fd85b01aca94e775c729375136c2c63c42b3a4e265`. The second JSON's 239995 bytes have SHA256 `21d4574f62f96408464b9de74dd1496376bc0ef652728cf11e3cdb8338a83890`. The second's input hash matches the first exactly.

## 4. Exact inference and limits

The invertible tail and selected C blocks lift over Q, because their determinants are nonzero modulo 101. Each nonzero observing determinant likewise lifts to a nonzero rational determinant. The observing criterion in the all-N jet-rank note therefore proves, at **N=1 and each of the four fixed rational values mu=1,2,-1,0**, full column rank of the 44-by-43 formal mixed pencil for **every complex gamma**.

This is stronger than the nine sampled gamma evaluations, but its quantifier on N and mu stays finite. It does not prove every rational mu is admissible. It does not prove the previously designated square omitting one tail row remains nonzero for every gamma: full-pool rank and a particular maximal minor are distinct. It does not pay the all-N observing determinant, determinant arithmetic at every prime, a real-place balance, or a numerical irrationality conclusion.

Review conclusion: the two complete producer sources agree with the original finite definitions; their saved matrix and observing-determinant conclusions pass independent finite verification within the scope just stated. No mathematical repair to either source or saved JSON was required, and neither was modified.
