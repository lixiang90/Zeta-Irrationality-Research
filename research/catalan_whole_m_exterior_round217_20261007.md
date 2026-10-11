# Whole M exterior bounds for the actual parity mixed carrier

2026-10-07, round 217. NEW isolated paper note. This pays explicit approximation numbers for the whole M transform, a finite complete mixed-exterior bound retaining every M/D intermediate term, and a quantified limitation of that particular bound. It does not prove a favorable arithmetic comparison or actual relation-point nonvanishing. No producer, finite grid, prime scan, historical program or numerical evaluator was run. Old notes, main and manifest remain frozen.

## 1. Fixed object, source normalization and the full tail projection

Use only the authoritative q=0, b=11N parity carrier:
\[
A=19N,\quad h=2N,\quad b=11N,\quad K=8N,\quad
n=44N-1,\quad L=55N-1,\quad m=36N-2,\quad
p=m+1,\quad\delta=n-m=8N+1.                         \tag{X1}
\]
The fixed proposed relation is \(\alpha G+\beta\pi^2=u\), with rational parameters, \(\alpha\ne0\), and \(\mu=16\beta/\alpha\). It is needed to identify the original moment determinants as rational; all real operator estimates below hold for every fixed real \(\mu\).

Put
\[
d\nu_h(x)=\frac{x^{-1/2}(1-x)^{h-1/2}}\pi\,dx,
\quad H_x=L^2(\nu_h),\quad
H_y=L^2(y^{b-1/2}dy),
\]
\[
Q_d=P_d^{(h-1/2,-1/2)}(2x-1),\quad
d=K+1,\ldots,n,\quad \rho_d=\|Q_d\|_{H_x}^2.
\]
The \(p\) vectors \(q_d=Q_d/\sqrt{\rho_d}\) are orthonormal. Let \(J_N:\mathbb R^p\to H_x\) be their isometric inclusion. Let \(\mathcal T_N\subset H_y\) be the span of the **entire** actual pure-D tail transforms, corresponding to \(x^{L+a}(1-x)^h\), \(0\le a<\delta\), and let \(\Pi_N\) be orthogonal projection onto \(\mathcal T_N^\perp\).

An all-tail maximal minor uses every \(\delta\) tail and any \(m\) of the \(p\) Jacobi directions. Tail row additions do not change it. The statements below do not cover a principal square which omits a tail. No independence of row functions is used to infer independence after compression to the prescribed columns.

## 2. Explicit approximation numbers of the complete M transform

The actual M part of the row function is the operator
\[
(\mathcal M Q)(y)=\frac\pi2\int_0^1
\frac{x^{A+1/2}Q(x)}{1-xy}\,d\nu_h(x).                 \tag{X2}
\]
Its kernel is the whole Cauchy kernel, including the endpoint region. For every integer \(k\ge0\), replace \((1-xy)^{-1}\) by \(\sum_{j<k}x^jy^j\). This defines an operator of rank at most \(k\), with exact remainder kernel
\[
\frac\pi2\frac{x^{A+k+1/2}y^k}{1-xy}.
\]
Since \(b-1/2+2k\ge0\), its Hilbert-Schmidt norm satisfies
\[
\begin{aligned}
\|\mathcal M-\mathcal M^{[k]}\|_{\rm HS}^2
&=\frac{\pi^2}4\int x^{2A+2k+1}d\nu_h(x)
       \int_0^1\frac{y^{b-1/2+2k}}{(1-xy)^2}dy\\
&\le\frac\pi4 B(2A+2k+3/2,h-1/2),
\end{aligned}                                                   \tag{X3}
\]
because \(\int_0^1(1-xy)^{-2}dy=(1-x)^{-1}\). All beta parameters are positive, including at \(N=1,k=0\).

Define
\[
a_{k+1,N}=\frac12\sqrt{\pi B(38N+2k+3/2,2N-1/2)}.
\]
The min-max characterization of singular values, or its direct rank-\(k\) approximation proof, gives
\[
\boxed{s_{k+1}(\mathcal M)\le a_{k+1,N},\qquad
s_{k+1}(M_N)\le a_{k+1,N},\quad
M_N=\Pi_N\mathcal M J_N.}                              \tag{X4}
\]
Indeed restriction to the isometric source inclusion and multiplication by a projection preserve the rank bound and cannot increase the error norm. In particular the actual Jacobi source and actual complete tail projection are retained. This is an approximation-number estimate, not a new scalar row norm.

## 3. The complete D input matrix and its lawful output use

Let \(B_d\) be the polynomial second-kind transform of \((1-x)^hQ_d\). The actual canonical section is
\[
D_C=x^{A+1}(1-x)^hE_d,\qquad
E_d\equiv B_d/(1-x)^h\pmod{x^m},\quad\deg E_d<n.
\]
The remaining \(\delta\) coefficients are exactly the included tail freedom. For
\[
G_{uv}=B(2A+u+v+2,2h+1),\quad0\le u,v<n,
\]
split low indices \(0,\ldots,m-1\) from high indices \(m,\ldots,n-1\), and put
\[
S_G=G_{ll}-G_{lh}G_{hh}^{-1}G_{hl}>0.
\]
Writing
\[
C_{r,d}=\frac{[x^r]\{B_d/(1-x)^h\}}{\sqrt{\rho_d}},
\quad0\le r<m,
\qquad \widehat G_D=C^tS_GC,                            \tag{X5}
\]
the least input norm is obtained by the unique high-coefficient choice \(-G_{hh}^{-1}G_{hl}c\). This choice is linear in the source, so X5 is the exact \(p\)-square Gram of these completed, normalized input lifts. The secondary Jacobi coefficient Vandermonde proves \(\operatorname{rank}C=m\); consequently \(\widehat G_D\) has exactly \(m\) positive eigenvalues \(\lambda_1\ge\cdots\ge\lambda_m>0\) and one zero eigenvalue.

For completeness, an input is \(f=x^{A+1/2}(1-x)^hE\), and its complete actual D transform, with the sign appropriate to \(D_\mu=-\mu D_C\), is
\[
\frac38\{C_0f+\sqrt y\,C_0(\sqrt x f)\},\qquad
(C_0f)(y)=\int_0^1\frac{f(x)}{1-xy}dx.                 \tag{X6}
\]
Both channels are included. The exact unitary substitution \(x=(t-1)/(t+1)\) sends \(C_0\) to \((t+u)^{-1}\) on \([1,\infty)\). Schur's inequality with weight \(t^{-1/2}\) gives \(\|C_0\|\le\pi\). The multipliers \(\sqrt x,\sqrt y\) and output weight \(y^{b-1/2}\le1\) are contractions. Thus, with \(c_0=3\pi/4\), the completed D operator after \(\Pi_N\), denoted \(D_N\), satisfies
\[
D_N^*D_N\le c_0^2\widehat G_D,
\qquad s_i(D_N)\le c_0\sqrt{\lambda_i},\quad i\le m.   \tag{X7}
\]
This holds for every linear combination of source directions, rather than just individual rows. All completions differ from the canonical arithmetic section by tail combinations; hence \(\Pi_ND_N\) is the same actual residual transform. X5 is an **input** Gram. X7 is an inequality for its complete output image, not an equality for the mixed moment Gram.

## 4. A full mixed exterior inequality with every intermediate term

Set \(A_{0,N}=1\), \(A_{r,N}=\prod_{j=1}^r a_{j,N}\), and
\(L_{0,N}=1\), \(L_{j,N}=\prod_{i=1}^j\lambda_i\). Then the complete residual mixed operator
\(K_N=M_N+\mu D_N\) satisfies
\[
\boxed{\|\bigwedge^mK_N\|\le\mathcal E_N
=\sum_{r=0}^m\binom mr A_{r,N}
            (c_0|\mu|)^{m-r}\sqrt{L_{m-r,N}}.}         \tag{X8}
\]
Here is the complete exterior argument. For orthonormal \(v_1,\ldots,v_m\), multilinearity expands
\(K_Nv_1\wedge\cdots\wedge K_Nv_m\) into the \(2^m\) terms specifying which inputs use M and which use D. Each term using r copies of M has norm at most
\(\|\bigwedge^r M_N\|\,|\mu|^{m-r}\|\bigwedge^{m-r}D_N\|\),
because each input sub-wedge has norm one and the output wedge of two groups has norm at most their product. There are exactly \(\binom mr\) such terms. X4 and X7 bound their two exterior norms by \(A_{r,N}\) and \(c_0^{m-r}\sqrt{L_{m-r,N}}\). Finally \(p=m+1\); every element of \(\bigwedge^m\mathbb R^p\) is decomposable, by Hodge duality. The supremum on these unit wedges is therefore the full operator norm. This proves X8, including its coefficient, without assigning M and D a common singular basis.

In particular, the generally false estimate \(s_i(M+\mu D)\le a_{i,N}+c_0|\mu|\sqrt{\lambda_i}\) is not assumed. X8 keeps every middle value \(0<r<m\), which cannot be removed merely because the D-only determinant is small.

## 5. Actual determinant factors and the resulting finite certificate

Write
\[
H_j(a,c)=\det_{0\le u,v<j}B(a+u+v+1,c+1),\quad H_0=1,
\quad \lambda_d^{\rm mom}=d_\mu 2^{20N}4^d.
\]
For a selection I of m Jacobi directions, the actual original moment-normalized all-tail determinant obeys
\[
\boxed{|\Delta_I^{\rm mom}|\le
\left(\prod_{d\in I}\lambda_d^{\rm mom}\sqrt{\rho_d}\right)
\sqrt{H_n(b-1/2,0)H_\delta(2L-1,2h)}\,
c_0^\delta\,\mathcal E_N.}                            \tag{X9}
\]
To verify the factors, orthogonalize monic column polynomials for \(y^{b-1/2}dy\), with determinant factor \(\sqrt{H_n(b-1/2,0)}\). Orthogonalize and normalize the complete tail inputs for \(x^{2L-1}(1-x)^{2h}dx\); their factor is \(\sqrt{H_\delta(2L-1,2h)}\) and their output volume is at most \(c_0^\delta\). The normalized Jacobi source contributes the displayed original scalars and \(\sqrt{\rho_d}\). The identity for wedging tails with the remaining rows projects the latter off the actual tail span. If the tail functions were dependent, the determinant is zero and X9 is immediate. Otherwise it gives exactly the projection \(\Pi_N\). Bessel contraction to the prescribed n columns completes X9.

These are real changes to the same determinant; no new integer model is asserted. Tail additions preserve its conditional rationality, because the tail input support starts at original degree \(2L\), above the highest column \(2L-2\), so they have no diagonal period term there. X9 controls the full signed M+D determinant, rather than a separately irrational component.

## 6. A paid N-squared gain in the all-M term

Define
\[
\mathscr B(a,c)=a\log a+c\log c-(a+c)\log(a+c),
\quad X(z)=\tfrac12z^2\log z-\tfrac14z^2,\quad X(0)=0,
\]
\[
\mathscr H(a;b,c)=X(a)+X(b+a)-X(b)+X(c+a)-X(c)
                  -X(b+c+2a)+X(b+c+a).
\]
Uniform factorial or Stirling integral bounds give, for \(k/N\to t\in[0,36]\),
\(N^{-1}\log a_{k+1,N}\to\mathscr B(38+2t,2)/2\), with an \(O(\log N/N)\) error uniform over the actual indices. Therefore
\[
\boxed{J_M:=\lim N^{-2}\log A_{m,N}
=\frac14\int_{38}^{110}\mathscr B(v,2)dv
=\frac14\{X(110)-X(112)-X(38)+X(40)+144\log2\}.}       \tag{X10}
\]
This is the leading exponent of the **Taylor approximation certificate**, not an equality for the actual M exterior. It is strictly smaller than the old scalar-only term \(18\mathscr B(38,2)\). More quantitatively,
\[
\boxed{\frac{81}{7}<18\mathscr B(38,2)-J_M
                         <\frac{648}{19}.}             \tag{X11}
\]
Indeed \(-\partial_v\mathscr B(v,2)=\log(1+2/v)\). On \([38,110]\),
\(1/56<\log(1+2/v)<1/19\). Integrating from 38 to v and then over v gives X11, since \(\frac14\int_{38}^{110}(v-38)dv=648\). Thus the new graded bound pays a genuine fixed amount of N-squared descent, with no numerical scan and no normalization change.

## 7. A rigorous method cap for this complete positive exterior sum

All terms in X8 are nonnegative. Its r=m term is precisely \(A_{m,N}\), independently of the D spectrum, \(\mu\), or its refined input Gram. Consequently the right side of X9, viewed as this chosen upper certificate, has leading floor
\[
\boxed{\mathcal U_{\rm Taylor\ floor}=
2592\log2+\tfrac12\mathscr H(44;11,0)
 +\tfrac12\mathscr H(8;110,4)+J_M.}                    \tag{X12}
\]
The source norm product has only \(O(N\log N)\) logarithm; omitting one Jacobi direction changes the scalar sum only by \(O_\mu(N)\). The binomial and \(c_0^\delta\) factors cost only \(O_\mu(N)\). They do not alter X12.

A fully elementary size comparison suffices. For the column Gram the monic norm formula and \(\binom uv\le2^u\) give
\(\mathscr H(44;11,0)\ge-4840\log2\). For the tail Gram restrict x to \([1/2,3/4]\). Its weight is at least \(2^{-118N+O(1)}\); the monic affine scale contributes \(-2\delta^2\log2\), and the unweighted Hilbert Gram contributes at least another \(-2\delta^2\log2\). Hence
\(\mathscr H(8;110,4)\ge-1200\log2\). Thus the prefactor in X12 is at least \(-428\log2\).

For \(38\le v\le110\),
\[
\mathscr B(v,2)=-v\log(1+2/v)-2\log((v+2)/2)
                  >-2-12\log2,
\]
because \((v+2)/2\le56<64\). Substitution into X10 proves
\[
\boxed{\mathcal U_{\rm Taylor\ floor}
>-36-644\log2>-680>-27323/4.}                          \tag{X13}
\]
The last number is the separately paid current conditional lower exponent for the **same moment normalization**, from the new parity finite-place note, valid along any unbounded nonzero all-tail sequence. Even if every D-containing term in X8 could be made negligible, this particular positive exterior-sum certificate could not establish the required strict comparison. Its gap to that lower threshold is greater than \(24603/4\) on the N-squared scale.

X13 is a lower bound for a chosen upper-certificate expression. It is not a lower bound for the actual determinant and proves no no-go statement for the parity carrier, another joint inequality, the actual whole-M spectrum, a new arithmetic lattice or a different support. It does not exclude cancellation between mixed exterior terms. In particular, division by the proved odd row content changes the real prefactor and arithmetic lower by the same \(864N^2\); it cannot remove this same-object gap.

## 8. Exact Cauchy exterior and the missing joint information

There is a further exact whole-M entrance, without evaluating its leading term. For \(r\ge1\), define
\[
\begin{aligned}
\mathcal I_{r,N}=\frac{(\pi/2)^{2r}}{(r!)^2}
\int_{(0,1)^{2r}} &\prod_{i=1}^r x_i^{2A+1}\,d\nu_h(x_i)
                       \prod_{j=1}^r y_j^{b-1/2}dy_j\\
&\times\frac{\prod_{i<j}(x_j-x_i)^2
                 \prod_{i<j}(y_j-y_i)^2}
                {\prod_{i,j}(1-x_iy_j)^2}.
\end{aligned}                                                   \tag{X14}
\]
Then
\[
\boxed{\|\bigwedge^r\mathcal M\|_{\rm HS}^2
=\mathcal I_{r,N},\qquad
\|\bigwedge^rM_N\|\le\sqrt{\mathcal I_{r,N}}.}          \tag{X15}
\]
Indeed the determinant of the r-by-r Cauchy kernel is exactly
\(\det[(1-x_iy_j)^{-1}]=V(x)V(y)/\prod_{i,j}(1-x_iy_j)\).
The antisymmetric tensor-kernel formula contributes \((r!)^{-2}\); integrating its square gives X14. It can also be checked by finite orthonormal expansions and two applications of the determinant integral identity, followed by Hilbert-Schmidt convergence. The integrals are finite: expansion of the determinant and Cauchy-Schwarz bound them by a finite constant times \(\|\mathcal M\|_{\rm HS}^{2r}\), which is finite by X3. This equality is for the unrestricted whole-M operator; source restriction and tail projection only yield the stated inequality.

One may replace \(A_{r,N}\) in X8 by \(\min(A_{r,N},\sqrt{\mathcal I_{r,N}})\). That gives another lawful finite certificate retaining every intermediate term. This note pays **no** leading evaluation or favorable lower estimate for \(\mathcal I_{r,N}\); therefore X13 is not asserted for this potential strengthened certificate. The integrand carries the joint Vandermonde interaction and all Cauchy denominators. Bounding every denominator only by \(1-x_i\) would cause a nonintegrable upper integrand once \(2r\ge h+1/2\), so that shortcut pays no all-r exterior estimate.

For the actual restricted, projected mixed operator there is also the exact finite identity
\[
\boxed{\|\bigwedge^mK_N\|_{\rm HS}^2
=e_m(K_N^*K_N),\quad
K_N^*K_N=M_N^*M_N+\mu(M_N^*D_N+D_N^*M_N)
                         +\mu^2D_N^*D_N.}             \tag{X16}
\]
Here \(e_m\) is the sum of all m-by-m principal Gram minors. Each is precisely the squared residual function volume for a selected source set. The projection is the common actual \(\Pi_N\); if written as a tail Gram Schur complement, its cross blocks must also be retained. Input equality X5 cannot replace either the D output block or the mixed cross blocks in X16.

Thus a concrete next test is a uniform joint bound for X16, or a paid N-squared evaluation of X14 after the actual Jacobi-source restriction, with lawful control of all D-containing terms. The new approximation-number descent X11 alone does not justify more finite parameter scans. If the next proof still replaces the cross blocks by the positive sum X8 and uses only these Taylor \(a_{k,N}\), X13 supplies an explicit exit trigger: no refinement of the D Gram within that construction can reach the current arithmetic threshold. The arbitrary relation-point nonzero condition remains an independent obligation.

## 9. Exact reading, execution and review scope

For this continuation the author actually FULL read the current parity P1–P19 note (15818 bytes, SHA256 a39081cb49a101c80a6b7f69306d67fd873caebc6dbad3198c2a21dad85449d8), the complete-lift L1–L20 note (17007 bytes, SHA256 ead30b8662bf01acd69e2fcf97e7f5e31b902bdbe247e95f5f3f24dc05e8858c), the exact second-kind/joint-energy E1–E18 note (16036 bytes, SHA256 c18bd6973c4a198e1c0c4eea598d0bd3c3369e29f51680c9ed5a6b9ef7a86040), and the current finite-place F1–F17 note (15271 bytes, SHA256 f4400e1e72b99e57f7a830c4e390e0c8ade78505a434196233a5cba6e2fab0a0), without claiming new FULL reads of their underlying old papers or programs. A batched tool result omitted/truncated the latter two files; they were then actually separately FULL read. The approximation, exterior and cap derivations here are paper derivations. There was no new webpage/PDF reading or download and no mathematical program execution.

The bounded helper universal_normalization independently derived the legal multilinear mixed-exterior sum and its all-M method-floor formula by message; that was not a FULL review of this draft. No extra independent draft audit or program run is claimed.

Review receipt: root actually FULL read all nine sections X1–X16 of the 16756-byte mathematical version, SHA256 fff568f99be774ea79d800fc457c330008afa07c5c26d0ad1550915fee28bc3b, and independently paper-checked the rank-k exact remainder and beta parameters, actual source restriction and full-tail projection, whole-D input PSD bound, the p=m+1 decomposability and complete mixed wedge sum, every original scalar/source-norm/tail/column factor, X10–X11 leading gain, the certificate-specific cap, X14's (r!)^-2 and integrability, and the actual mixed cross Gram. Root returned mathematical PASS without correction. The author had already actually FULL reread that version. Only this receipt was changed afterwards; the final receipt-bearing author FULL reread and byte/SHA pin are recorded in the completion message. Any separate new dyadic gate is outside the mathematical and reading scope of this fixed-normalization note.
