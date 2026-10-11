# Second-kind and multipoint Pade sources: archive and exact reading scope

2026-10-07. Primary-source search was prompted by the actual high-Jacobi second-kind Taylor-jet problem. Download receipt: [JSON](cdt_mixed_second_kind_sources_20261007/download_receipt.json). No external paper is treated as a proof of the current mixed determinant's nonvanishing.

## Archived primary papers

1. Derevyagin and Zhedanov, [An operator approach to multipoint Pade approximations](https://arxiv.org/abs/0802.3432), explicit v2 [local PDF](cdt_mixed_second_kind_sources_20261007/Derevyagin_Zhedanov_0802_3432v2.pdf), 18 physical pages, 200577 bytes, SHA-256 `703b5c38b6e2482cf4a30c3dc9eb9c5dc76983e3511b2cb3fc21a8c85e150db0`.

   Root actually read physical pages 1--5 and visually inspected physical page 5. Section 2's abstract biorthogonal scheme explicitly imposes nondegeneracy assumptions; in particular page 5 assumes its moment determinants do not vanish. Its reciprocal determinant formulas therefore do not supply the missing nonvanishing proof for our object. Its recurrence and generalized matrix-pencil viewpoint suggested the observability reduction, but that reduction is proved directly for our matrices.

2. Baratchart and Yattselev, [Convergent interpolation to Cauchy integrals over analytic arcs with Jacobi-type weights](https://arxiv.org/abs/0911.3850), explicit v1 [local PDF](cdt_mixed_second_kind_sources_20261007/Baratchart_Yattselev_0911_3850v1.pdf), 42 physical pages, 727197 bytes, SHA-256 `479e79d58bfe0ad6bad7bb8ddef2077e0a28eac760e2dbf5076bb231339aa335`.

   Root actually read physical pages 1--8 and visually inspected physical page 3. Definitions 1--2 require interpolation nodes off the supporting arc, and Theorem 3 assumes a specific admissible interpolation sequence, fixed Jacobi exponents, and a normal family of logarithmic perturbations. Our zero-end jets lie at 0 on the original interval, and our exponent `6N-1/2` varies with N. Alternatively absorbing `(1-z)^(6N)` into the perturbation produces a non-normal logarithmic family. Thus the printed theorem cannot be applied directly. An adapted contour and varying-potential analysis would require a new proof. The paper is relevant to analytic estimates, rather than an already paid generic or arithmetic nonvanishing theorem.

The downloaded PDFs are complete, while the reading scopes above are partial. No supplied external program was executed, and neither paper received a full proof validation in this round. The printed date line in the first downloaded PDF differs from its arXiv version date; the explicit version URL and file hash identify the actual archived object.

## Verbatim current OpenAI source excerpts

The same directory contains byte-identical copies of the current Catalan manuscript's two complete source sections, read in full by the root:

- [odd-primes.tex](cdt_mixed_second_kind_sources_20261007/openai_catalan_current_odd-primes.tex), 672 lines, 26263 bytes, SHA-256 `42228a070b0d0e070f78d78146d0881869578cca9112327d72a7c6c7e8fbea10`;
- [nonvanishing.tex](cdt_mixed_second_kind_sources_20261007/openai_catalan_current_nonvanishing.tex), 413 lines, 17218 bytes, SHA-256 `4f8ddcf4a8c8eec1c1225d38a48e63a26a996ca399fea5cce88d3d0d4ef3f93f`.

The odd-prime digit identities were checked at the rational moment-kernel level and reproved/applied to the new integer pairs in the [finite-place note](../research/catalan_mixed_jacobi_moment_finite_places_20261007.md). The original nonvanishing theorem uses separate Chebyshev row identities and three fixed original matrices. Its proof is not transferred to the new Jacobi rows. The exact scale-prime content obstruction is proved in the [new root note](../research/cdt_mixed_jacobi_prime_content_20261007.md).
