# R₀ 真实消失球归一化的独立复核

日期：2026-10-06。Reviewer：quarter_actual_rank。实际全文读取作者 final NEW 稿，包括最后新增的 V11 Morse-ball density 奇偶性说明：
[vanishing normalization](cdt_odd_R0_vanishing_regulator_normalization_20261006.md)，
SHA256 **7a254a5d974379a76142aee36120390d5dbd7491c4794d97997976d082cbf296**。
本文及被审稿都是纸面数学；旧/同行 mathematical producers 均只读，未执行、import 或重跑。

结论：在声明的实际 local-symbol evaluation、rational compact lift normalization、三维剩余差额范围内通过。没有证明整个 compact regulator 等于 \(\nu_{\rm corr}\)，没有证明它的三个实际 holomorphic jets 代数。

## 1. Local unit product 与真正周期评价

本 reviewer 实际重新读 KLM published primary PDF8、12、13：
[本地原件](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，
SHA256 **8e612fd409fc0f9ca392434a8c40c39b658e10ea27b69d84afdfdc03704114d9**。
PDF8 Proposition4.2 是任意 \(n\) 的 unit Deligne cup-product；PDF12 给 higher-Chow regulator ring map；PDF13 §5.6–5.7 给 \(p=n\) 的 ordinary-class/cycle evaluation 和 Tate-period ambiguity。未冒认全文阅读。

在所有 \(v_j\) 接近1且 negative cuts 为空的实际 neighbourhood，cup-product current只剩
\[
 R_{\rm loc}=\log v_0\,d\log v_1\,d\log v_2\,d\log v_3,\qquad
 dR_{\rm loc}=\Omega.
\]
这里是 unit-product 的 holomorphic 延拓；\(v_j=1\) 时 \(\log1=0\) 不要求 raw graph 在compact边界admissible。
在smooth local fibre上，\(\Omega\) 是四形式而 fibre只有complex dimension3，restriction为0；cut-chain亦为0。因此 triple确实给 ordinary degree-three class \([R_{\rm loc}]\)。由指定 \(\Xi\) 限制为 unit symbol、AJ map自然性、compact ordinary lift 的restriction，评价 \(\delta\) 得
\[
 \int_\delta r=\int_\delta R_{\rm loc}\pmod{(2\pi i)^4\mathbf Q}.
\]
这说明 V9 并非把 KLM 的 projective ordinary-cohomology theorem无条件套到一般open variety；本例 local current triple已明确简化，compact restriction再与它比较。
\(\delta\) 属于实际 rank-four sector，故对 \(r\) 先作 \(\Pi\) 不改变这个 evaluation。

Morse radius \(r\) 下，log为 \(O(r)\)，三个pullback one-forms各有一个 \(r\)，所以 V10 的 \(O(r^4)\) 成立。Stokes作用在 ambient total neighbourhood 的四球；不是宣称该四球位于一个complex三维 fibre内。实际 \(\Omega=16\,du^4+O(|u|^2)\)，Morse Jacobian首项为1。作者 final V11 已说明变换后一次density项的球对称积分为0，余项 \(O(\tau^3)\)。故
\[
 A_\delta=8\pi^2(x-1)^2+O((x-1)^3)
\]
是正确的独立sign/scale核对。

Cartan 在 total primitive 上给 \(\theta A_\delta=16\sqrt{x}\,g\)；LEFT residue 正号沿冻结真实规范核对。于是 \(t=1-x\)、\(g=-\pi^2v(t)\) 给
\[
 A'_\delta(t)=16\pi^2v(t)/\sqrt{1-t},\qquad A_\delta(0)=0,
\]
严格恢复 V3。\(v\) 的前三Taylor data是 \(0,1,3/4\)，冻结齐次递推给 \(v_3=29/48\)；以后全部系数有理。
\(A_\delta/(2\pi i)^2=-4\int_0^tv/\sqrt{1-s}\,ds\) 的有理 germ也通过；这不赋予整个 scalar免费的rational gauge。

## 2. 整数 Tate 常数与 raw cup 的 dual sign

Concomitant恒等式给
\[
 \theta(A_\delta-256\mathcal C_0(W,g))=0.
\]
对任意analytic \(H\)，endpoint \(\mathcal C_0(H,g)=H(0)(2b-3a/2)=0\)，因 \(b=3a/4\)。
实际log period给 \(\mathcal C_0(y_0,g)=-1\)，故
\[
 \mathcal C_0(W,g)\big|_{t=0}=-\pi^4/16.
\]
常数因此为 \(16\pi^4=(2\pi i)^4\)，不是其负值，也没有factor16误差。得到
\[
 A_\delta=256\mathcal C_0(W,g)+(2\pi i)^4
         =256\mathcal C_0(\Psi,g).
\]

Reviewer 独立手核 period-column 与 \(J\) 的sign：\(h_j=Q(r,E_j)\) 的column为 \(-Jc\)，\(g_j=Q(PD\delta,E_j)\) 为 \(-Jd\)。于是
\[
 (-Jc)^TJ^{-1}(-Jd)=-Q(r,PD\delta)
                   =Q(PD\delta,r)=\int_\delta r.
\]
因此 \(\mathcal C_0(\nu,g)/\kappa_{\rm raw}=\int_\delta r\) 是正该evaluation。结合
\(\nu_{\rm corr}=-16(2\pi i)^3\Psi\)、\(\kappa_{\rm raw}=-(2\pi i)^3/16\)，其ratio正好为256，V20成立。

## 3. 合法 rational normalization只消一个方向

两个实际continuous lifts 的δ evaluation差为 \(q(2\pi i)^4\)，且由相同derivative使 \(q\in\mathbf Q\) 常值。不能把未标记的 \(q\) 定为1。
\(\Gamma\cdot\delta=-8\) 给 \(\delta\cdot\Gamma=8\)，所以
\[
 r_{\rm can}=r-\frac{q(2\pi i)^4}{8}\Pi PD\Gamma
\]
恰消该差；\(\Pi\) 已为actual rational horizontal projector，因此shift保持AJ class和derivative。这不证明integral projector或 \(\Gamma/8\) integral primitive。

差额 \(H=\nu_{\rm can}-\nu_{\rm corr}\) 满足 \(PH=0\)、\(\mathcal C_0(H,g)=0\)。
conifold的三个analytic solutions被此functional杀掉；第四个solution为 \(g\log t+\)analytic，concomitant的limit为 \((-\pi^2)^2=\pi^4\ne0\)（整体非零scale不影响结论）。
因此该条件严格等价于无log分量，得到实际scalar全纯lift，但其差仍有三个自由Taylor data。
冻结 \(P\) 的analytic递推使 \(H(0),H'(0),H''(0)/2\) 唯一决定全部germ；本稿没有认领这些数的算术性质。

## 4. V24 的合法超越 jet 反例

\((2\pi i)^4PD\delta\) 是实际 compact rational Tate flat shift。
\(\delta^2=0\) 保持消失球evaluation，\(g(1)=0\) 保持scalar endpoint。其scalar改变量为
\[
 (2\pi i)^4g=-16\pi^6v(t).
\]
对 \(\widehat\nu=-\nu/[16(2\pi i)^3]\)，变为
\[
 \Delta\widehat\nu
 =\pi^6v(t)/(2\pi i)^3=i\pi^3v(t)/8.
\]
故 V24 的正号及factor8通过。第一jet差 \(i\pi^3/8\) 超越；两个合法lifts不可能同时有代数第一jet。这是实际lift歧义的明确反例，不是新特殊值无理性定理，也不排除经过完整Betti标记后的某一lift可能有算术germ。

最终独审通过；被审final和本独审可在root回读后冻结。没有数学producer、数值搜索、PSLQ或Lean执行。
