# New nonlinear-period sources: reading scope and usable interface

2026-10-07. Two new primary-source PDFs and their HTML counterparts are archived in this directory. SHA256 and byte receipts are in download_receipt.json. Downloading is not full reading or proof verification.

## Sources actually read

1. [Francis Brown, Non-linear geometry of multiple zeta values, v1](https://arxiv.org/html/2604.22735v1), 2026-04-24: root actually read PDF physical p.1 and pp.31–34 (5 pages), plus selected public HTML introduction and epilogue. PDF pp.32 and 34 were visually inspected. The 35-page paper was not fully read.
2. [Brown–Schnetz, The wheel classes…, v3](https://arxiv.org/html/2402.06757v3), 2025-01-13: root actually read PDF physical pp.1–3 and 11–12 (5 pages), and public HTML Theorem 1 and section 2.4. PDF p.1 was visually inspected. The 39-page paper was not fully read. An initial v2 HTML opening was superseded by v3 for every claim recorded here. Supplied Maple programs were not executed.

## Useful primary input and its limit

Brown–Schnetz Theorem 1 gives, for every odd n≥3,

\[
I_{W_n}(\omega^{2n-1})=n\binom{2n}{n}\zeta(n),
\qquad\omega_X^k=\operatorname{tr}((X^{-1}dX)^k).
\]

The canonical wheel integrals provide real, finite single-period representations. They differ from the usual Feynman residue, whose weight is 2n−3. Nonvanishing detects graph homology; it does not establish numerical irrationality. Brown's lecture notes suggest a common determinantal geometry and connect it to arithmetic-group cohomology. They present the proposed general framework as future work, rather than an irrationality theorem.

For the current CDT program, this gives a potential genuinely different carrier. The missing work is an explicit rational-coefficient deformation, projection that keeps precisely the desired numerical period, and a complete integer model with a usable real-place estimate. Replacing an integral representation alone does not supply these. In particular, Taylor coefficients of a parameter-dependent integral can themselves be periods; rationality of those coefficients must be proved, not assumed.

## Formula-level cautions found during the actual read

These are root's direct checks, not a claim that the papers' main results fail. The lecture PDF p.32 Example 52 displays Q=x₁²+2x₁x₂+x₂². As written this is (x₁+x₂)², so its nonzero integer minimizers include every (k,−k); it cannot have the displayed finite six-vector set. Do not use that example as an exact Gram-matrix input without resolving the coefficient.

The lecture PDF p.32 Theorem 50 gives a volume proportional to ζ(3)ζ(5)…ζ(g), while its p.34 quotient example uses g=7 but a numerator ζ(3)ζ(5). The Brown–Schnetz PDF p.12 also has inconsistent zeta upper indices and the same quotient example. Therefore no regulator quotient from these displays is imported as an exact numerical identity here. The checked wheel Theorem 1 is the retained input; a future use of regulator normalization must return to its original definitions and prove the relevant indexing.

No numerical independence of odd zeta values, no proof of all odd-value irrationality, and no period-injectivity assumption is furnished by this reading. This scope note is separate from the new mixed Catalan arithmetic and geometry proofs.

Independent bounded review: theta_analytic_geometry FULL read this note; actually read Brown PDF pp.32/34 and Brown–Schnetz pp.1/12 with visual inspection of all four, and additionally Brown–Schnetz pp.2–3 as text. The retained wheel normalization, stated reading limits and the displayed-formula cautions passed. No supplied program or whole-paper proof review was performed.

## Jacobi normalization for the constructive contact space

Root also checked the official [NIST DLMF Table 18.3.1](https://dlmf.nist.gov/18.3#T1), [Rodrigues formula and its Jacobi row](https://dlmf.nist.gov/18.5#ii), and [finite binomial formula 18.5.8](https://dlmf.nist.gov/18.5#E8) through the browser tool. These confirm the weight (1−x)^α(1+x)^β, α,β>−1, and the normalization used in the new two-end contact construction. Only those entries were read; entire DLMF chapters were not read. Direct archival retrieval initially returned HTTP 403; any successful later downloads appear individually in download_receipt.json, otherwise the browser-read references and this scope are the record.
