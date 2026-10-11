# b=0 actual parity moments: a same-object prime-window certificate

2026-10-07, round218. NEW bounded paper proof. This pays the proposed G21 denominator corollary for the complete actual matrix, including all outside primes and powers, and the already proved exact row division. It also pays a small adjoining two-layer improvement. No complete prime-area sweep, producer, validator, numerical evaluator, prime grid or historical program was run. The actual relation-point determinant nonzero remains unproved.

## 1. Fixed object and exact source scope

Use the q=0,b=0 model G1–G10 of the frozen [round217 gate](catalan_b0_arithmetic_gate_round217_20261007.md): 17670 bytes, SHA256 4cb75887e8d013b1ab4e947b805d4a29722a1c53273cf0d5dddc7090e65e71a6. The author actually FULL read its final eight sections in round217; this round actually reread complete section6/G21 and checked that identity. This round also actually read complete sections2–4/F4–F10 of the frozen [parity finite-place note](catalan_parity_joint_finite_places_20261007.md), 15271 bytes, SHA256 f4400e1e72b99e57f7a830c4e390e0c8ade78505a434196233a5cba6e2fab0a0. That is a bounded current-round reading, not a new FULL reading of all old notes. Original foundations.tex lines95–263 were read in round217; their rational recurrence definitions are retained through these frozen interfaces, not called a new original-source FULL audit here.

In brief,
\[
A=19N,\ h=2N,\ n=L=44N-1,\ H=130N,\quad
m=25N-2,\ \delta=19N+1,\quad d=19N+1,\ldots,44N-1.
\tag{W1}
\]
All row exponents are even and below H. All n actual columns are
\[
j=0,2,\ldots,2n-2=88N-4.
\]
Fix rational mu!=0 and rational gamma. The Jacobi pairs have the proved scalar \(\lambda_d^{\mathrm{pair}}=d_\mu2^{2h}4^d\), and the pure-D tails are integral. Write E_pair for any specified n-row square restriction of the n+1 full pool, with the complete n-column list retained. Its rational entries are the actual relation-point expression
\[
M^0(P,j)-\tfrac32 Z^0(D,j)+\gamma C_j(P).
\tag{W2}
\]
Neither the coefficient matrix C alone nor a separately rational D-only matrix replaces W2.

For each selected Jacobi row use the exact odd divisor
\[
\Omega_d=\prod_{\substack{p\ {\mathrm{odd\ prime}}\\d+h-1<p\le2d}}p,
\qquad \Omega_I=\prod_{d\in I}\Omega_d.
\]
The integer pairs and C outputs remain integral after this division, and
\[
\det E_{\mathrm{pair}}=\Omega_I\det E_{\mathrm{div}},
\qquad \log\Omega_I=\tfrac{1475}{2}N^2+o(N^2).
\tag{W3}
\]
This covers both the designated square and all-tail maximal minors: omitting one degree changes only O(N). The row identity is exact, and no new primitive-lattice claim is attached to it.

## 2. The same-object local rank-to-denominator lemma

If an n-square matrix E over Q_p satisfies \(pE\in\operatorname{Mat}_n(\mathbb Z_p)\) and
\[
\operatorname{rank}_{\mathbb F_p}(pE\bmod p)\le r,
\]
then
\[
\boxed{v_p(\det E)\ge-r.}
\tag{W4}
\]
Indeed a basis of the residue-field column kernel lifts to an element V of GL_n(Z_p). At most r columns of pEV have nonzero residues; hence at least n−r columns of EV are integral, and its remaining columns have depth at most one. Multiplying those r columns by p gives an integral matrix. As det V is a unit, W4 follows. A smaller actual residue rank only strengthens the conclusion. This is a local integral column operation on the whole matrix, not column deletion or a nonzero residue-packet assumption. Zero determinants also satisfy the valuation statement.

Now take an odd prime \(92N<p\le H\), with p not dividing d_gamma. Then \(p>H/2\), \(a_p=v_p(\operatorname{lcm}(1,\ldots,H))=1\), and every actual column j is below p. F6's vanishing depth-two residue for low even columns, together with the complete depth bound F4, proves \(pE_{\mathrm{div}}\) is integral.

Put J=H−p, an odd integer with J<38N<n. There are (J+1)/2 noncentral low columns j<J. For every remaining column, F7 gives
\[
pE_j\equiv-\sum_{\substack{0\le\ell<J\\\ell\ {\mathrm{odd}}}}
\frac{V_\ell}{j-\ell}\pmod p.
\tag{W5}
\]
All denominators are units. The (J−1)/2 vectors V_ell are common row vectors for the entire full pool. Hence the complete n-column residue matrix has rank at most J. Restriction to any n rows preserves that bound. W4 therefore proves
\[
\boxed{v_p(\det E_{\mathrm{div}})\ge-(130N-p)
\qquad(92N<p\le130N,\ p\nmid d_\gamma).}
\tag{W6}
\]
All n columns and the same row restriction occur throughout this argument.

## 3. A complete all-prime certificate and the requested leading gain

Let \(\ell_H=\operatorname{lcm}(1,\ldots,H)\), and let d_gamma be a positive fixed denominator of gamma. G7–G9 pay the pair model at 2; F4 pays every odd prime and power. Thus the global entry fallback is \(2d_\gamma\ell_H^2E_{\mathrm{div}}\) integral.

For all primes put
\[
W_p^{(0)}=
\begin{cases}
H-p,&92N<p\le H,\ p\nmid d_\gamma,\\
n\{2v_p(\ell_H)+v_p(2d_\gamma)\},&\text{otherwise}.
\end{cases}
\]
The finite integer product
\[
\mathcal D_N^{(0)}=\prod_p p^{W_p^{(0)}}
=\frac{(2d_\gamma)^n\ell_H^{2n}}
{\displaystyle\prod_{\substack{92N<p\le H\\p\nmid d_\gamma}}
p^{\,2n-H+p}}
\tag{W7}
\]
has nonnegative exponents and proves
\[
\boxed{\mathcal D_N^{(0)}\det E_{\mathrm{div}}\in\mathbb Z,\qquad
\mathcal D_N^{(0)}\det E_{\mathrm{pair}}/\Omega_I\in\mathbb Z.}
\tag{W8}
\]
This is complete at small primes, 2, higher powers and primes dividing the fixed parameter denominator. At p>H only the fixed gamma-denominator factor can remain. The fixed mu denominator has already been cleared by the integer pair model; numerator divisibility of mu does not hurt the certificate.

Since \(2n-H+p=p-42N-2\), the weighted PNT gives
\[
\begin{aligned}
\sum_{\substack{92N<p\le130N\\p\nmid d_\gamma}}
(2n-H+p)\log p
&=N^2\int_{92}^{130}(x-42)\,dx+o(N^2)\\
&=2622N^2+o(N^2).
\end{aligned}
\]
The constant −2 per prime costs only O(N). Fixed excluded primes leave this window for all sufficiently large N. The baseline \(2n\log\ell_H\) has leading 11440N², so
\[
\log\mathcal D_N^{(0)}=8818N^2+o(N^2).
\tag{W9}
\]
Every power is already present in W7; there is no omitted higher-power term. In particular, conditional on the selected actual rational determinant being nonzero along an unbounded sequence,
\[
\boxed{\log|\det E_{\mathrm{pair}}|
\ge-\tfrac{16161}{2}N^2+o(N^2)
=-8080.5N^2+o(N^2).}
\tag{W10}
\]
This pays the proposed improvement from G13's −10702.5 by exactly 2622 on the N² scale. It is a sufficient conditional arithmetic lower bound, not a necessary denominator minimum or an actual nonzero theorem.

The main window primes exceed 92N while every Omega_d prime is at most 88N−2. These two proved gains are disjoint here. More generally W8 is proved for E_div itself, so the row identity W3 must be used with that divided same-object matrix; one must not subtract Omega twice or change the analytic normalization silently.

## 4. A bounded adjoining two-layer improvement

One further short window is paid without deriving a full prime-area table. For an odd prime \(86N<p\le88N\) with \(p\nmid d_\gamma\), set
\[
J=H-p,\quad
R=\left(L-\frac{p+1}{2}\right)_+,\quad
\ell=\frac{J+1}{2},\quad c=n-R-\ell,\quad
e=\frac{J-1}{2}-R.
\tag{W11}
\]
These nonnegative integers count high even columns, noncentral low columns, central columns and unrepresented odd residues. High columns are \(j=p+\ell'\), where odd ell' runs from1 through 2L−2−p. This last bound is below2A, so U_(ell')=0. F6 gives \(p^2E_{p+\ell'}=-V_{\ell'}\bmod p\). F7 gives the central p-scaled residues in W5.

For a represented odd residue ell', the integral shear
\[
E_j\longmapsto E_j-(j-\ell')^{-1}pE_{p+\ell'}
\]
with a Z_p lift of the displayed unit cancels that V_(ell') term in pE_j modulo p. Every high column is retained. The remaining central residues lie in at most e unrepresented common vectors. A lifted central-column kernel basis therefore makes all but at most min(c,e) central columns integral. High columns have depth≤2, low noncentral columns depth≤1. The complete same-object determinant consequently satisfies
\[
\boxed{v_p(\det E_{\mathrm{div}})
\ge-\{2R+\ell+\min(c,e)\}.}
\tag{W12}
\]
This conclusion allows the actual residue vectors to vanish; it requires no full-rank packet.

Uniformly for x=p/N in (86,88), the loss in W12 is
\[
\{174-\tfrac32x\}N+O(1).
\]
Indeed R/N→44−x/2, ell/N→65−x/2, c/N→x−65 and e/N→21, so min(c,e)/N→21. Exact endpoint offsets in W11 are retained; only the displayed leading limit drops them.

For an odd prime \(88N<p\le92N\) with \(p\nmid d_\gamma\), all columns are already below p and J<42N<n. The same rank proof as section2 gives loss at most J, with leading \((130-x)N\). No second-depth column exists in this subwindow.

Define \(\mathcal D_N^{(1)}\) by replacing the outside-window fallback exponents of W7 by W12 on (86N,88N] and by J on (88N,92N], always retaining the fixed-denominator fallback at p dividing d_gamma. Together with W6 this is another complete all-prime certificate. Relative to W9 its two additional leading savings are only
\[
\int_{86}^{88}\{88-(174-3x/2)\}\,dx=89,\qquad
\int_{88}^{92}\{88-(130-x)\}\,dx=192.
\]
Thus
\[
\log\mathcal D_N^{(1)}=8537N^2+o(N^2),
\quad
\boxed{\log|\det E_{\mathrm{pair}}|
\ge-\tfrac{15599}{2}N^2+o(N^2)=-7799.5N^2+o(N^2).}
\tag{W13}
\]
The division by Omega is still paid for E_div before this proof; possible overlap of Omega primes with (86N,88N] does not double-count a gain. The divided pairs remain integral, and the residue proof was uniform in every such pair. This section examines only two adjoining short windows, not the entire range (65N,130N).

## 5. What a further residue layer would have to prove

The rank argument itself does not force any further uniform content. Let \(M=pE\) be integral, and let r be its exact residue rank. Integral row and column bases put it in block form
\[
UMV=\begin{pmatrix}A&B\\ C&D\end{pmatrix},
\qquad A\in\operatorname{GL}_r(\mathbb Z_p),\quad B,C,D\equiv0\pmod p.
\]
The exact next-layer matrix is
\[
\mathcal S_1=\frac{D-CA^{-1}B}{p}\in
\operatorname{Mat}_{n-r}(\mathbb Z_p),
\qquad
v_p(\det E)=-r+v_p(\det\mathcal S_1).
\tag{W14}
\]
If \(\operatorname{rank}(\mathcal S_1\bmod p)=t<n-r\), it supplies at least n−r−t further powers of p. However gamma C, absent from the leading residue of pE, re-enters this next layer. The actual rational M0/Z0 correction also enters it. The known C Vandermonde minors and common Jacobi row content do not determine this compressed matrix or force its rank defect.

The abstract matrix \(\operatorname{diag}(p^{-1}I_r,I_{n-r})\) saturates W4 and has S1 invertible. This shows the leading integral/rank data alone cannot prove additional loss saving. It is not a claim that the actual moment matrix realizes that example. No uniform second-layer defect, next-layer unit determinant or relation-point nonzero along unbounded N is asserted here. A useful next proof must calculate this actual compressed layer, rather than reuse generic coefficient rank.

## 6. Scope and author receipt

W7–W10 pay the requested same-object main window with complete outside-prime coverage; W11–W13 give a small further integral-column gain from two adjoining windows. Both are conditional arithmetic lower bounds for the same rational actual matrix. They do not change the fixed support or numerical target, and do not use a D-only determinant in place of the mixed one.

The real/finite gap remains large. The row normalization and a real upper bound must refer to the same E_pair or E_div model. Nothing here proves a favorable strict comparison or actual determinant nonzero, and no full prime-area sweep or unbounded parameter variation is hidden in the fixed-parameter PNT limit.

Author reading and execution scope is stated in section1. The mathematical proof used paper valuation, local integral linear algebra, finite residue counts and the weighted PNT. The author actually FULL read all six W1–W14 sections without truncation, and reread the final file after the fixed-denominator qualifiers and this receipt were updated. No numerical or coefficient program was run, and no round217 file, old note, main or manifest was edited.
