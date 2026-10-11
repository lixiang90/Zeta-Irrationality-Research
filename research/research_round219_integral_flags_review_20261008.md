# Independent FULL review of the round219 Legendre integral flags

2026-10-08. Reviewer: /root/round218_lambert_carrier. Result: PASS for the stated coefficient, finite-jet source-lattice and two-flag theorems. This is not a numerical irrationality result or a rational Betti/Hodge/global-holonomy audit.

## 1. Exact final object and actual reading scope

The reviewer actually FULL read all seven sections of [eisenstein_legendre_integral_flags_round219_20261008.md](eisenstein_legendre_integral_flags_round219_20261008.md), including the final u=x/16 normalization and its all-prime certificate. The final author confirmed this saved identity, which matches the reviewer's actual full-file read:

* Bytes: 15599.
* SHA-256: bc41296fb85c5548adae93d25cde5f9e4983f5d223ada8e6a39cd1b87b765730.

PASS attaches only to that identity. The review independently rederived A3–A20 on paper. The reviewer is also the author of the separate analytic companion and has actually FULL read that companion; the modular-coordinate and target-period input is therefore identified precisely, but this receipt registers its independent review only for the arithmetic note above. No source text, earlier note, main report or manifest was edited.

## 2. Exact coefficients and all-prime/all-power clearing

Dividing A2 by the nonzero homogeneous recurrence gives

\[
\frac{u_n}{c_n}-\frac{u_{n-1}}{c_{n-1}}
=\frac{1}{16n^2c_n},
\]

which telescopes to A3 with u₀=0. All subsequent coefficient estimates can therefore be checked term by term without assuming cancellations.

The odd-prime carry inequality A6 is valid at every power. For e≤a=floor(log_p n), the carry C_e(j) and divisibility indicator 1_{p^e|j} cannot both equal one, so their sum minus C_e(n) is at most one. For e>a, both j,n<p^e, and C_e(j)=1_{2j≥p^e}≤1_{2n≥p^e}=C_e(n); the divisibility indicator is zero. Summation gives exactly A6. In particular carry levels p^e>n have not been discarded, and A5/A7 cover all odd primes and powers, including primes greater than n.

At 2, the displayed digit-sum valuation in A5 is nonnegative. More importantly, after u=x/16 the cleared coefficient b_n=16^n u_n itself is 2-integral. Its jth exact summand has valuation

\[
2s_2(n)+4j-4-2v_2(j)-2s_2(j).
\]

For j=1 this is 2s₂(n)−2≥0; for j≥2, v₂(j)≤j−1 and s₂(j)≤j give the same nonnegative lower bound. Thus A7b pays prime 2 without a multiplier. At odd primes it follows from A6. Multiplication by the integer n clears the theta coordinate as well, and the rational third coordinate has globally integral normalized coefficients 16^n. Hence d_N² clears the complete normalized three-row coefficient jet. The ordinary-derivative statement is correctly restricted to differentiation of the already truncated polynomial; differentiation before truncation requires the enlarged cutoff.

## 3. Hasse unit and the actual depth-two coefficient

Lucas' identity applies to the whole p-integral F series, including the zero cases in which the low digit of n exceeds h=(p−1)/2. Its low-digit factor is precisely H_p, so A8 is a formal identity, not a finite-coefficient fit. Vandermonde gives H_p(1)=binom(p−1,h)=(-1)^h, while H_p(0)=1. The reduced Legendre equation and deg H_p=h<p exclude repeated roots away from 0 and 1: the ordinary-point Taylor recurrence forces a polynomial with value and derivative zero there to vanish identically. Thus H_p is squarefree.

The field distinction in A10 is correct. F'/F=H_p'/H_p is rational, whereas F^{p−1}=1/H_p has a simple pole at a root of H_p and cannot be a (p−1)st power in F_p(x). This does not create an unscaled mod-p U.

For n<p, the central-binomial carry is monotone in j≤n, and every j is a p-unit; A3 therefore makes u_n p-integral. The exact Wronskian identity A11 follows by differentiating x(1−x)(FU'−UF') and using A1. At degree p its right integral has, after multiplication by p, coefficient (1/16)Σ_{j=0}^{p−1}c_j. On the left the only nonintegral term is p u_p. Hence

\[
p^2u_p\equiv(-1)^h/16\pmod p
\]

is a unit and v_p(u_p)=−2. The homogeneous recurrence after this coefficient, through degree 2p−1, gives A13; its vanishing range after k=h is included. Only p² times the supported finite jet is reduced. Under x=16u, its first unit becomes μ_p=(-1)^h, since 16^p=16 modulo p. This checks every factor used in A15.

## 4. The whole source, both surjectivity alternatives and the second flag

For N/2<p≤N one has N<2p and v_p(d_N)=1. In A14 the original source is all three copies of degree-≤D polynomials, and the output is every coefficient 0,…,N. Products with source polynomials introduce no frame coefficient beyond N. All coefficients below p are integral, so the nonintegral output lies in the m-dimensional high-jet group, m=N−p+1,

\[
p^{-2}u^pJ_N/u^pJ_N\simeq(\mathbf Z_p/p^2)^m.
\]

The reduction of p²E_N is exactly A15; every c-direction is retained and has zero first residue. The rank bound A16 and its explicit polynomial syzygies concern this same complete source and cutoff.

Both alternatives in A17 really give rank m. When D≥m−1, multiplication by H̃_p with constant one is a triangular unit map on the m truncated high coefficients. In the second alternative, gcd(H̃_p,theta_u H̃_p)=1, and both polynomials have degree h. Every bounded-degree kernel pair is a multiple of (−theta_u H̃_p,H̃_p), with dimension (D−h+1)_+. At D=h−1 the kernel is zero and the source and polynomial-target dimensions are both 2h. For every D≥h−1 the image dimension is therefore exactly D+h+1, so it fills all polynomials of degree ≤D+h and hence the m truncated coefficients when m−1≤D+h.

Surjectivity modulo p promotes to surjectivity onto the entire group (Z_p/p²)^m: lift m residue basis vectors and use the unit determinant of their high-coefficient matrix over Z_p, or apply Nakayama to the finite quotient. The quotient image therefore has order p^{2m}, and its kernel is exactly the integral-evaluation source lattice. This proves the exact index in A17 without finite-jet injectivity.

The second flag is also paid on the changed lattice. With T=p²E_N, L₁={v:T(v)∈pJ_N} and L₂=L_D^{int}, the two actual residue maps have ranks summing to 2m by the exact flag/index identity. The first has rank m, so the second also has rank m. No unchanged first-layer congruence is repeated. Both kernel dimensions are n_D−m for n_D=3(D+1), and the third source row has never been removed from the source.

## 5. Complete N=3D coverage, gain and finite-jet cost

Every odd prime 3D/2<p≤3D is covered. For p≥2D the first A17 condition holds. For p<2D, D≥h−1 and 3D−p≤D+h are equivalent to elementary bounds implied by p>3D/2 for D≥2; the D=1 odd-prime case falls in the first alternative. No gap in the window remains.

The fallback multiplies only the two potentially nonintegral source rows by (d_N^{odd})² and retains the integral third row. Its index is (d_N^{odd})^{4(D+1)}. At each paid prime the actual index exponent is 2(N−p+1), so the nonnegative saving is 2p−2D+2 when N=3D. All smaller odd primes and their powers retain the proved cap; primes above N and prime 2 have integral full jets. Localization of the finite-index global rational evaluation lattice therefore gives the divisibility certificate A18 with no missing finite-place term.

The weighted PNT computation is

\[
\int_{3/2}^{3}(2x-2)\,dx=15/4.
\]

The per-prime constant contributes O(D). The baseline is 12D²+o(D²); deleting the power of 2 changes it by O(D log D), and the paid window subtracts 15D²/4+o(D²). Consequently the coefficient 33/4 in A20 is correct. It bounds this complete rectangular finite-jet integral lattice; it is not a necessary cost, an optimized small-prime theorem, a nonzero numerical determinant, or a strict analytic/arithmetic comparison.

## 6. PASS boundary and review executions

The normalized u-polynomial source, all three frame rows, complete cutoff and all finite primes have been kept compatible throughout. A real-place basis norm or capacity in the x coordinate is not transported for free by x=16u. The target's period projection is at the singular endpoint, and this finite-jet lattice result supplies no rational Betti realization of the extension, integral period comparison, Hodge filtration, globally compatible arithmetic-holonomy source, or unbounded nonzero evaluation determinant. These remain unpaid in the reviewed note, as stated there.

No mathematical program, symbolic check, numerical evaluation, prime scan or old producer was executed by this reviewer. Verification was a FULL saved-file read and independent paper rederivation; filesystem reads and SHA-256 calculation are documentary operations. No mathematical correction to the frozen target was necessary, and the reviewer made no edit to it. The final handoff records this NEW receipt's actual full saved-file read and hash separately from the target identity above.
