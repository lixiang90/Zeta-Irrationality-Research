# D12 全 Γ 真实 cocycle 的有理 Tate 归约：含12分母的有限尖点

日期：2026-10-06。独立新 proof note。仅使用已证明的固定 pure L3χ12 source，不修改或执行冻结文件，不扫描参数。补全此前互素分母有限核未覆盖的 k divisible12 情形，证明所有 Γ cocycles 在 h=fσ+Θ 的真实正规化后均属于 iπ³Q[τ]≤2。它不解整个 signed cocycle kernel，不声称得到新的无理性结果。

## 1. 固定实际 source 与有限尖点的范围

采用[已证 source](cdt_odd_level12_source_period_20261006.md)及[已冻结 signed cocycle](cdt_odd_level12_signed_cocycle_20261006.md)：

\[
 F_\sigma=\sum_{j\mid12}u_j E_4(j\tau)
       +dE_\chi+\kappa dF_\chi,\quad
 d=2880,\quad\kappa=12\sqrt{12}=24\sqrt3,
 \tag{G1}
\]

其中 j=1,2,3,4,6,12 的 u_j 为1217,−14082,6255,−11120,126738,−175248。Eχ constant23。准确的 source constraints 是

\[
 \sum u_j=-23d=-66240,\qquad
 \sum u_j/j^3=0,\qquad
 \kappa L(4,\chi)=\frac{115}{3}\zeta(4).
 \tag{G2}
\]

令 fσ=θq⁻³Fσ、fσ(i∞)=0，Θ=κdL(3,χ)/2=34560√3L(3,χ)，h=fσ+Θ。 Γ=kerχ12；采用 normalized right slash f|−2γ=det(γ)⁻¹(cτ+dγ)²f(γτ)。对 γ∈Γ，Bol 给

\[
 c_h(\gamma)=h|_{-2}\gamma-h\in\mathbf C[\tau]_{\le2}.
 \tag{G3}
\]

本文的有限尖点是 \(a/k\in\Gamma\infty\)、k>0。它们准确满足 k divisible12、gcd(a,k)=1、χ(a)=+1。必要性来自 γ=(a,b;k,dγ)∈Γ；反向由选择 determinant1 completion，χ(dγ)=χ(a)=+1 得到。分子可按 modulo k 取值，不改变 q endpoint。

特别 **∞ 本身不用于下文的 Tate 尖点值定理**：h(i∞)=Θ。我们证明的是所有有限 Γ∞ 尖点的值属于 iπ³Q；不把 ∞ 和有限尖点混同。

## 2. 含极点的 χE 循环核：全 k 的显式有理模型

写 k=12r，r≥1，并在 \(\mathcal R_k=\mathbf Q[x]/(x^k-1)\) 中定义

\[
 H(x)=x-x^5-x^7+x^{11},\quad
 J(x)=x-5x^5-7x^7+11x^{11},\quad y=x^{12},
\]
\[
 I=\frac1r\sum_{l=0}^{r-1}y^l,\qquad
 K=\frac1r\sum_{l=0}^{r-1}\left(\frac{r-1}{2}-l\right)y^l.
 \tag{G4}
\]

有限 geometric identities 给

\[
 I^2=I,\quad yI=I,\quad IK=0,\quad(1-y)K=1-I.
 \tag{G5}
\]

所以 I 在 k 阶 roots 上准确为 y=1 的 projector；K 是1−y在其补空间上的唯一零平均 inverse。r=1 时 I=1、K=0，同一公式有效。定义两个 degree<k 的 rational residue/finite-part polynomials

\[
 R_k=IH/12,\qquad
 C_k=HK+I(H/2-J/12).
 \tag{G6}
\]

令 ζ=e^(2πi/k)，任意整数 a 与 gcd(a,k)=1。真实 χ kernel 为

\[
 e_\chi(z)=\frac{H(z)}{1-z^{12}}.
\]

对每个 n 的 phase z0=ζ^(an)，当 v↓0 时

\[
 e_\chi(z_0e^{-v})=R_k(z_0)/v+C_k(z_0)+O(v).
 \tag{G7}
\]

若 z0¹²≠1，I=0、K=(1−z0¹²)⁻¹；若 z0¹²=1，直接 Taylor 展开 numerator 与 denominator 得 residue H(z0)/12、finite part H(z0)/2−J(z0)/12。H(z0)=0 的可去 phase 也由同一公式覆盖。没有在 pole 上将原有理函数作普通除法。

也可用 CRT 表示：D=x¹²−1、Q=(x^k−1)/D，在 D roots 上 Q=r，因此两者互素；Ck 是唯一 degree<k rational polynomial，满足 Ck≡H/2−J/12 mod D、(1−x¹²)Ck≡H mod Q。投影公式(G6)明示这个全尺度模型。

取 star:x↦x⁻¹。χ even 给 H*=y⁻¹H、J*=y⁻¹(12H−J)，而 I*=I、K*=−yK。由(G5)得到

\[
 R_k^*=R_k,\qquad C_k^*=-C_k.
 \tag{G8}
\]

因此 Ck(ζ^n) 为纯 imaginary，且若 Ck=Σc_m x^m，其 rational coefficients 满足 c_(k−m)=−c_m（c0以及偶数k的中点coeff为0）。这同时说明 finite Fourier coefficients 为Q；不需要从浮点认出有理数，也不依赖某个未知 period 的 Galois action。

## 3. 极点减法与真实径向极限

χE 的 q primitive 是 Σn≥1 eχ(q^n)/n³。沿 q=ζ^a e^−ε，根据(G7)，需要先保留准确 pole

\[
 \sum_{n\ge1}\frac{R_k(\zeta^{an})}{\epsilon n^4}.
 \tag{G9}
\]

只有 n=rℓ 可能出现 residue。原始 even Gauss identity H(e^(2πim/12))=√12χ(m) 给

\[
 \sum_{n\ge1}R_k(\zeta^{an})/n^4
  =\frac{\sqrt{12}\chi(a)L(4,\chi)}{12r^4}
  =\frac{5520\chi(a)\zeta(4)}{k^4}.
 \tag{G10}
\]

这里的 last equality 正是(G2)，Gauss normalization 没有遗漏根式。χF primitive Σχ(n)n⁻³q^n/(1−q^n) 的 pole phase 要求 k|n；因12|k，此时χ(n)=0，所以它完全无 pole。

普通 E4 oldform primitive 为240j⁻³T(q^j)，T(q)=Σn≥1n⁻³q^n/(1−q^n)。因j|12|k，其 pole coefficient为

\[
 \frac{240\zeta(4)}{\epsilon k^4}\sum_{j\mid12}u_j
     =-\frac{5520d\zeta(4)}{\epsilon k^4}.
 \tag{G11}
\]

所以 full Fσ primitive 的唯一 radial pole 为

\[
 \frac{5520d(\chi(a)-1)\zeta(4)}{\epsilon k^4}.
 \tag{G12}
\]

在所有 finite Γ∞ cusps χ(a)=+1，pole **准确为0**。χ(a)=−1 不属于本文的实际有限极限定理；不能把一个 regularized finite part 自动改称 actual boundary value。

还需 justify 求和和极限。对固定 k，每个有限 phase 上

\[
 e_\chi(z_0e^{-v})-R_k(z_0)/v
\]

在所有 v>0 uniformly bounded：v→0 来自已写出的 Laurent 展开，v≥v0 的有理分母远离零，v→∞ 两项均趋0。普通 Lambert phase 减 pole 后也 uniformly bounded；无 pole 的 χ-weighted phases 已是有限 bounded family。因此除 pole 后的所有项均由固定常数 times n⁻³ 支配。dominated convergence 与(G12)证明 full source 的极限确为下面的 finite parts；不是任意选择的 regularization。

## 4. 全部 finite part：实部恰为 −Θ，剩余为有理 Tate

记 B3(x)=x³−3x²/2+x/2。对任何 rational odd cyclic polynomial P=Σp_m x^m，由 Euler–Bernoulli sine identity

\[
 \sum_{n\ge1}P(\zeta^{an})/n^3
 =i\pi^3\frac23\sum_{m=0}^{k-1}p_m B_3(\{am/k\}).
 \tag{G13}
\]

所以 χE finite part由 Ck 给出纯 iπ³ rational；没有 L3 实部。

普通 Lambert 的 phase finite-part polynomial为

\[
 -\frac12+O_l(x),\qquad
 O_l=\sum_{m=1}^{l-1}(1/2-m/l)x^m,
 \tag{G14}
\]

其 pole phase x=1 的 finite value也是−1/2，O_l(1)=0。l=1 时 O1=0。故 T 在任何 root phase 的 real finite part均为−ζ3/2；当前 source 的 real trivial contribution 为−120ζ3Σu_j/j³=0。

scaled χF 要把 relative Gauss 因子保留：令

\[
 A_k(x)=\sum_{b=1}^{12}\chi(b)x^{rb}.
\]

它满足 A_k(ζ^n)=√12χ(n)、A_k*=A_k。χF finite part的 real contribution 为−κL3χ/2。其 imaginary contribution是 rational odd polynomial

\[
 F_{k,a}(x)=12A_k(x)O_k(x^a)\pmod{x^k-1}.
 \tag{G15}
\]

这是因为 κ/√12=12；Γ0/Γ 的源系数根式在这一 Gauss Fourier 转换中准确消去。F_(k,a)*=−F_(k,a)，由(G13)其贡献为iπ³ rational。不能在 inert embedding 或 unknown L-value 上暗用 σ；此处是实际复数 Gauss identity。

明确写出 whole-source finite coefficient：

\[
 \mathcal T_l(a)=\frac23\sum_{m=1}^{l-1}(1/2-m/l)B_3(\{am/l\}),
\]
\[
 \mathcal E_k(a)=\frac23\sum_m[x^m]C_k B_3(\{am/k\}),\quad
 \mathcal F_k(a)=\frac23\sum_m[x^m]F_{k,a} B_3(m/k),
\]
\[
 \alpha_{k,a}=240\sum_{j\mid12}\frac{u_j}{j^3}\mathcal T_{k/j}(a)
                 +d\mathcal E_k(a)+d\mathcal F_k(a)\in\mathbf Q.
 \tag{G16}
\]

普通 oldscale denominator 正是 k/j，不能继续套 coprime(k,12)=1 的旧 factor。于是所有有限 Γ∞ 尖点满足实际定理

\[
 \boxed{\lim_{\epsilon\downarrow0} f_\sigma(e^{2\pi ia/k-\epsilon})
       =-\Theta+i\pi^3\alpha_{k,a},\qquad
       h(a/k)=i\pi^3\alpha_{k,a}.}
 \tag{G17}
\]

这些恒等式不假设 L3χ rational，也不假设 Θ 与 π³ 的任何独立性。

## 5. 真实路径兼容与三点 interpolation：全部 Γ 的结论

在 finite Γ∞ cusp a/k，source Fσ 的 transformed constant为0。先只使用(G3)的 **complex-coefficient** polynomial存在性（不假定 rationality）：若 γ0∞=a/k，则

\[
 f_\sigma(\gamma_0 z)
  =(c_0z+d_0)^{-2}\{f_\sigma(z)+P_{\gamma_0}(z)\},
 \quad\deg P_{\gamma_0}\le2.
 \tag{G18}
\]

fσ(z)在∞ exponentially趋0，故右边给 finite Stolz/nontangential cusp limit，独立于路径。因 vertical radial path 也是此种路径，其值就是已经严格计算的(G17)。这一点允许在 cocycle polynomial上真正取 boundary limit，不从抽象 finite part直接代用。

任意 γ∈Γ，取四个预定 finite cusps

\[
 x_j=\eta^j\infty=1/(12j),\qquad j=1,2,3,4.
 \tag{G19}
\]

至多一个 xj 被 γ 送到∞；删除它，取剩下的任意三个。它们及其 γ-images 都是 finite Γ∞ points，由(G17)/(G18)

\[
 c_h(\gamma)(x_j)
   =(cx_j+d_\gamma)^2h(\gamma x_j)-h(x_j)\in i\pi^3\mathbf Q.
 \tag{G20}
\]

三个 xj 是不同 rational numbers，Vandermonde inverse是 rational。结合(G3) degree≤2，得到无条件 whole-group结论

\[
 \boxed{c_h(\gamma)/(i\pi^3)\in\mathbf Q[\tau]_{\le2}
         \quad\text{对全部 }\gamma\in\Gamma.}
 \tag{G21}
\]

∞ 自身从未进入这个 interpolation；h(∞)=Θ与(G21)相容。若某γ把一个 xj送到∞，也不能将该一项直接代入(G20)。四点只是确保永远有三个合法有限点，不是 parameters搜索。

再令 \(\mathcal G=\langle\Gamma,M\rangle\)、εΓ=+1、εΓM=−1。已证 c_h(M)=0及 signed cocycle式给 c_h(γM)=c_h(γ)|−2M。因此同一 rational Tate结论对全部 \(\mathcal G\) 成立。未平移的 fσ 满足准确 signed coboundary账本

\[
 f_\sigma|_{-2}\gamma-\epsilon_\gamma f_\sigma
  =i\pi^3P_\gamma-
    \Theta\left\{(c\tau+d_\gamma)^2/\det\gamma-
                       \epsilon_\gamma\right\},
 \quad P_\gamma\in\mathbf Q[\tau]_{\le2}.
 \tag{G22}
\]

所以有限 Schreier generators 不需要额外未知 L-values；Θ 只在 f-normalization中以这一明确 coboundary出现。计算实际 kernel 仍需生成元 matrices 与完整 finite Bernoulli值；没有因为所有 cocycles rational Tate就自动使它们为0。

## 6. NEW 固定证书及尚未解决的问题

同名 NEW verify从 rational cyclic arithmetic 独立实现(G4)–(G16)，只核(G19)预先固定的四个 finite cusp k=12,24,36,48、a=1；不import任何旧 producer、不枚举参数/prime。核 projection identities、residue/FP CRT与star、Gauss-square normalization、source pole/realpartconstraints、有限Bernoulli全值及其与已证 ηj cocycle 的 leading coefficient对应。四个 finite values应分别为14400、29280、132160/3、58800（除iπ³）；这只是 normalization cross-check，全k与全Γ定理由正文承担。

作者首次、单次执行这个 NEW producer，61项全部通过，准确得到以上四个 finite values。有限检查与全 k/全 Γ 的正文证明分别记录，不将四点计算冒充全部尖点定理。

root 已实际全文只读正文 §§1–6 及 verify.py，独立核(G4)–(G8)投影/star、(G10)–(G12)全 pole 5520d(χ(a)−1)、(G15) scaled Gauss、(G16)oldscale k/j、(G18)Stolz路径兼容与四点删γ-pole interpolation，限定通过全 Γ/ΓM rational Tate结论。root没有执行producer；61固定检查仅由作者首次单次执行。本文据这个实际独审冻结，后续peer审阅另记精确范围，不为追加审阅改冻结文件。

本稿证明 rationality interface，未给全 Γ 的生成元表、完整 word kernel分类、额外zero generators、对应合法叶拓扑或新的容量收益。所有冻结输入保持原样。
