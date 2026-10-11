# 第254轮：固定χ−8投影的primitive算术内容证书

2026-10-10。独立子任务。实际 FULL 读253 Root证明、253进展报告、manifest253及RV现存物理4–6页完整选段。固定 n≥2、r=0,…,3，仍取原第五列系数0；参数、投影方向与完整Gauss泛函均不改变。本文无有限n扫描、CAS、Lean、素数搜索或新来源下载。

**支付了直接作用于完整A、c的共同因子，以及一个精确的primitive pair公式；没有支付约分后实际误差的统一净衰减或无界非零，没有新的数值无理性定理。** 全n满秩仍引用已审253证明，本文不把它当实际线性式非零。

## 1. 同一对象与projective缩放

设 Φ=z⁴+1，Λ=d_(13n+4)d_(12n+4)，D=(6n)!(7n)!，s=(−1)^(n+1)，

\[
 M(z)=z^{3n}(z-1)^{3n},\qquad
 C_r(z)=\sum_{t=0}^{10n+r}(-1)^t\binom{10n+r}{t}W_n(t)z^t,
\]
\[
 W_n(t)=\frac{\prod_{j=2n+1}^{10n}(t+j)\prod_{j=3n+1}^{8n}(t+j)}{D}\in\mathbb Z
 \quad(t\in\mathbb Z_{\ge0}),\qquad R_r=sMC_r\in\mathbb Z[z].
 \tag{1}
\]

记 \(\widehat M\) 为首四列 \(R_r\bmod\Phi\) 的0,…,3系数矩阵，\(\delta=\det\widehat M\ne0\)，\(v=\operatorname{adj}(\widehat M)e_0\)。与253完全相同，

\[
 U=\sum_{r=0}^3v_rR_r\equiv\delta\pmod\Phi,\qquad
 Q=\Lambda U,\quad c=\Lambda\delta,
\]
\[
 A-cY=-\Lambda\int_0^1(-\log t)U(t)\frac{1+t^2}{1+t^4}\,dt,
 \quad Y=L(2,\chi_{-8}),\quad A,c\in\mathbb Z.
 \tag{2}
\]

这里完整P是∞多项式部；(2)保留原RV的全部对数修正。对任意列的非零有理共同缩放ρ_r，同时缩放相应完整P/Q，有

\[
 \widehat M'=\widehat M\operatorname{diag}(\rho_r),\quad
 v'=(\prod_r\rho_r)\operatorname{diag}(\rho_r^{-1})v,
\]
\[
 \sum_rv'_rR'_r=(\prod_r\rho_r)U.
 \tag{3}
\]

这由逆矩阵或adjugate恒等式直接得到。完整头与周期系数同乘 \(\prod_r\rho_r\)，所以将有理二元组清整再primitive约分，结果只可能整体变号。特别是Λ、D或逐列共同内容可以用于同一方向的有理计算；它们不是最终primitive费用。删去这些标度后，完整有理头的实际分母仍须支付。

## 2. 公共cyclotomic乘法的exact二进向量内容

令 \(\mathcal O=\mathbb Z[\zeta]\)，\(\zeta^4=-1\)，固定基 \(1,\zeta,\zeta^2,\zeta^3\)。对α∈O，乘法矩阵 \(L_\alpha\) 的行列式等于四个共轭之积；其范数为±1时，整数adjugate给出整数逆元。这些均是有限秩整数线性代数，不要求局部环/UFD定理。

置 λ=1−ζ。直接展开得

\[
 \lambda^4=2u,\qquad u=-2\zeta+3\zeta^2-2\zeta^3\in\mathcal O.
\]

\(N(\lambda)=\Phi(1)=2\)，\(N(2)=16\)，故 \(N(u)=1\)，u是整数单位。又 \(N(M(\zeta))=2^{3n}\)。向量 \(\operatorname{adj}(L_M)e_0\) 对应

\[
 \alpha_n=\frac{N(M(\zeta))}{M(\zeta)}
 =\frac{2^{3n}}{\zeta^{3n}(\zeta-1)^{3n}}
 =\lambda^{9n}\varepsilon_n,\qquad \varepsilon_n\in\mathcal O^\times.
 \tag{4}
\]

写 9n=4q+r，0≤r<4。由λ⁴=2u，\(\alpha_n=2^q\lambda^r\eta_n\)，η_n为单位。\(N(\lambda^r\eta_n)=2^r\)。如果剩余四个整数系数都被2整除，其范数会被2⁴整除，与r<4矛盾；如果都被某个奇素数p整除，范数会被p⁴整除，同样矛盾。因此**恰有**

\[
 \gcd\bigl(\text{四个}\ \alpha_n\ \text{系数}\bigr)
 =\kappa_n:=2^{\lfloor9n/4\rfloor}.
 \tag{5}
\]

这只对公共乘法的adjugate向量是exact。其后还要乘 \(\operatorname{adj}(N_C)\)，不能把(5)称为最终v或A/c的exact gcd。

## 3. 一个额外全n共同内容下界，不运行素数搜索

对每个素数p定义有限和

\[
 e_p(n)=\sum_{a\ge1}\left(
 \left\lfloor\frac{8n}{p^a}\right\rfloor+
 \left\lfloor\frac{5n}{p^a}\right\rfloor-
 \left\lfloor\frac{6n}{p^a}\right\rfloor-
 \left\lfloor\frac{7n}{p^a}\right\rfloor\right),\quad
 B_n=\prod_p p^{\max(0,e_p(n))}.
 \tag{6}
\]

当p>10n或p^a>10n时相应项全零；(6)是一个封闭的纸面定义，没有枚举实际素数或有限n。任意连续L个整数里，p^a的倍数至少有⌊L/p^a⌋个。对(1)两段长度8n与5n分别计数，并用 \(v_p(k!)=\sum_{a\ge1}\lfloor k/p^a\rfloor\)，得到

\[
 v_p(W_n(t))\ge e_p(n)\qquad(t\ge0).
\]

W_n(t)已由253的整数二项式和证明是整数，故其赋值也至少0。于是

\[
 B_n\mid W_n(t)\quad\text{对所有整数 }t\ge0,\qquad
 C_r/B_n\in\mathbb Z[z].
 \tag{7}
\]

还有一个不用prime-product即可定义同一B_n的有限形式。令

\[
 K_n=\frac{(8n)!(5n)!}{(6n)!(7n)!}=\frac{B_n}{Z_n},
 \quad B_n,Z_n\in\mathbb Z_{>0},\quad\gcd(B_n,Z_n)=1.
\]

其各素数赋值就是(6)中的e_p，所以既约分子恰为同一B_n。也可直接证明(7)：

\[
 W_n(t)=K_n\binom{t+10n}{8n}\binom{t+8n}{5n}.
\]

右侧二项式乘积与W_n(t)均为整数；既约性迫使Z_n整除二项式乘积，因此B_n整除W_n(t)。并且

\[
 B_n\ge K_n=\prod_{i=1}^n\frac{7n+i}{5n+i}
 \ge(4/3)^n.
 \tag{7a}
\]

最后一步逐因子使用i≤n。它给一个严格全n的指数级内容下界，无需Stirling、PNT或枚举任何素数。

Root提供且本稿纸面核对的补充还有

\[
 B_n\mid d_{8n}.
 \tag{7b}
\]

因为8x+5x=6x+7x，两对取floor后的和各只可能是⌊13x⌋或⌊13x⌋−1，故(6)每个p^a项属于{−1,0,1}。p^a>8n时该项为0；因此max(0,e_p)≤⌊log_p(8n)⌋，恰不超过d_(8n)的p赋值。这是已付内容的安全upper，仍不是最终g_n的upper或实际误差下界。

例如每个7n<p≤8n的素数在(6)中赋值1，其高次项均0，故 \(\prod_{7n<p\le8n}p\mid B_n\)。本稿不借PNT给渐近费，也不声称B_n是W全部值的exact内容。

令N_0为 \(C_r/B_n\bmod\Phi\) 的四列矩阵，整数矩阵分解为

\[
 \widehat M=s B_nL_MN_0,
 \quad\delta=B_n^4 2^{3n}\det N_0,
 \quad v=s^3B_n^3\operatorname{adj}(N_0)\operatorname{adj}(L_M)e_0.
 \tag{8}
\]

因此

\[
 \beta_n:=\kappa_n B_n^3\mid v_r\quad(r=0,\ldots,3),\qquad
 \beta_n\mid A,\ c.
 \tag{9}
\]

最后一个断言直接来自完整整数列P_r与整数v_r：它不是把Q的content推给P。虽然U还显然含额外一份B_n，(9)没有免费领取B_n⁴进入A/c；完整头可能带来该额外内容的分母。

由(7a)，已支付的完整A/c共同因子至少含

\[
 \beta_n\ge2^{\lfloor9n/4\rfloor}(4/3)^{3n}.
 \tag{9a}
\]

这是直接作用于原整数实现的指数级约分，不仅是某个大多项式的无关content。

## 4. 完整头的真实分母与精确primitive公式

首四列的原RV Theorem2.1指标为H=13n+r、K=12n+r、α=16n、β=3n−r，r≤3且n≥2。为了得到当前共同 \(z^{16n}(z-1)^{3n}\)，只是多乘整数多项式 \((z-1)^r\)。所以每个 \(R_r\) 对应的完整有理头用

\[
 \Lambda_n^*:=d_{13n+3}d_{12n+3}\mid\Lambda_n
 \tag{10}
\]

已可清整。第五列系数为0是这里可用Λ*的原因；没有改动原包或adjugate方向。

记 \(w=v/\beta_n\in\mathbb Z^4\)，\(U'=U/\beta_n=\sum_rw_rR_r\)，\(\delta'=\delta/\beta_n\ne0\)。由(8)，δ′也是整数。令

\[
 S'(t)=\frac{U'(t)-\delta'}{1+t^4}\in\mathbb Z[t],\qquad
 H'=-\sum_k[S']_k\bigl((k+1)^{-2}+(k+3)^{-2}\bigr)
 =\frac{p_n}{q_n},
 \tag{11}
\]

q_n>0、gcd(|p_n|,q_n)=1；H′=0时取p_n=0、q_n=1。完整Gauss头等式给 A=β_nΛ_n H′。由于w是整数向量且Λ*清整每个完整头，

\[
 q_n\mid\Lambda_n^*.
 \tag{12}
\]

这不是逐项清整(11)：对某些k，Λ*并不必被(k+1)²整除。清整来自完整RV模型与有理数求和的实际消去；不把各分数头的LCD当最终费用。

设 \(d_n=\gcd(|p_n|,|\delta'|)\)。因为p_n与q_n互素，

\[
 \boxed{\ g_n=\gcd(|A|,|c|)
 =\beta_n\frac{\Lambda_n}{q_n}\,d_n,\qquad
 (a_n,b_n)=\left(\frac{p_n}{d_n},\frac{q_n\delta'}{d_n}\right).\ }
 \tag{13}
\]

证明只需代入 \(A=\beta_n(\Lambda_n/q_n)p_n\)、\(c=\beta_n(\Lambda_n/q_n)q_n\delta'\)，并用 \(\gcd(p_n,q_n\delta')=\gcd(p_n,\delta')\)。即使p_n=0，取d_n=|δ′|，同样成立。因此还有确定的整数整除证书

\[
 \beta_n\frac{\Lambda_n}{\Lambda_n^*}\mid g_n.
 \tag{14}
\]

(13)是同一原实现的精确primitive公式，但并非所有n上q_n与d_n的闭式解。它清楚指出剩余算术任务：完整有理头的既约分母，以及其分子与周期行列式的共同因子。

## 5. 对真实误差预算的影响与未付项

在完全相同(2)下，primitive实际误差是

\[
 \ell_n=a_n-b_nY
 =-\frac{q_n}{d_n}\int_0^1(-\log t)U'(t)
                   \frac{1+t^2}{1+t^4}\,dt.
 \tag{15}
\]

Λ_n与已付β_n从最终标度中消失，换成实际 \(q_n/d_n\)。使用253的安全 \(E_n=2^{51n+8}\) 还可立即给出

\[
 |a_n|\le\frac{48\Lambda_n^*E_n^4}{\beta_n},\qquad
 |b_n|\le\frac{24\Lambda_n^*E_n^4}{\beta_n}.
 \tag{16}
\]

这里用 \(\|U'\|_1\le24E_n^4/\beta_n\)、完整头 \(\|P_{U'}\|_1<2\|U'\|_1\)，以及q_n≤Λ*、d_n≥1；不是primitive最优增长率。相比把原整数A/c及其粗Λ费用直接当最终费用，(13)–(16)改变了可核预算；仍不足以证明 \(\ell_n\to0\)。不能把(16)未过某阈值说成真实下界或整个RV方法不可能。

正核不使U′常号；δ′≠0也不证明实际ℓ_n≠0。未付的是：同一(15)的uniform解析小界与真实非零，q_n/d_n的有效净费或完整充分估计，以及二者结合的strict余量。本稿不据局部内容证书自动开启参数、第五列、其它投影方向或素数搜索窗口。

