# 显式支付数域扩张后的 dyadic scale \(8\sqrt2\)

日期：2026-10-06。NEW short supplement。旧/同行数学稿与 producer 全部只读，无数学 producer 执行或 import。不修改本轮 C16 主稿；这里给另一份含全部数域费用的模型。

## K1. 对象与严格整系数目标

使用 all-odd arithmetic 主稿 A1–A15 的同一 actual 九行 paired packet \(f(q)\)，含常数1共rank10。其 four Z 和 five mixed coefficients分别满足 odd LCM七次、六次，统一额外
\[
 P_3(n)=3^{4\lfloor\log_3(n+6)\rfloor}.
\]
对参数 q所在数域 K，取 fixed \(d_0>0\) 使 \(d_0q\in\mathcal O_K\)。dyadic 纸面界不是只知道 \(16^n\)：实际全尺度卷积/derivative bound在每个2上方place、归一 \(v_2(2)=1\) 后为
\[
 v_2(d_0c_n)\ge-b(n+6)-4
   \ge-\tfrac72n-25.
 \tag{K1}
\]

令
\[
 L=K(\sqrt2),\qquad a=8\sqrt2,\qquad
 \rho=\log|a|=\tfrac72\log2.
 \tag{K2}
\]
这里 \(a\) 是实际 algebraic integer，\(a^2=128\)。本稿并非把任意正实数 \(2^{7/2}\) 宣称为有理坐标变换。必须在 L 的每个 finite/archimedean place上付清它的费用。

## K2. 全部有限 places 的 integer coefficients

对 L 中任意 finite place v，按 \(v_p(p)=1\) 归一：

- v位于2上方时，\(v_2(a)=7/2\)，不论 extension是否ramified或 K已含 \(\sqrt2\)。K1使 \(2^{25}a^n\) 清掉完整 dyadic coefficient denominator。\(d_0\)另清参数，不给 q免费integrality。
- v位于 odd p上方时，\(v_p(a)=0\)。g/F模型的所有odd费用仍按同一个 \(D_{n+6}^{\,7}\) 或 \(D_{n+6}^{\,6}\) 及 \(P_3(n)\)支付；源 square root/g2 normalization的系数已经纳入该模型，q的初始费用由 d0支付。

因此对所有n≥0，pure与mixed分别有实际 all-place integrality：
\[
 2^{25}d_0\,a^n P_3(n)D_{n+6}^{\,7}c_n(Z_j(q))
       \in\mathcal O_L,
 \tag{K3}
\]
\[
 2^{25}d_0\,a^n P_3(n)D_{n+6}^{\,6}c_n(M_i)
       \in\mathcal O_L.
 \tag{K4}
\]
这些 statements是所有 valuations非负，不只是绝对值平均界。对应全部前缀可用 \(a^N\)，因为 \(a^{N-n}\in\mathcal O_L\)，同时 \(P_3(n)\mid P_3(N)\)、\(D_{n+6}\mid D_{N+6}\)。没有用16的2-only factor去清3的额外幂。

严格 literal LCMspecies沿用主稿 A14a/b：每个 \(0<\varepsilon\le1\) 有 fixed rational integer \(d_\varepsilon\)，用六列 cutoff1 的 b=1+ε、一列 cutoff6 的 b=1+ε、四列 cutoff1 的 b=ε清 P3及shift。由K3/K4，十行
\[
 \widehat f_i(s)=2^{25}d_0d_\varepsilon f_i(a s)
 \in L[[s]]
 \tag{K5}
\]
逐coefficient满足原定理的整数LCM条件；固定常数列的该scalar也是整数。其
\[
 \tau_\varepsilon=(1+\varepsilon)329/50+
                  4\varepsilon(1-1/100)\to329/50.
 \tag{K6}
\]
这是付费转换，不把poly3费用删除。常数 \(d_\varepsilon\)虽随ε增长，对每个fixedε不贡献D²主项。

## K3. 全部 embeddings 的真实 source 参数和映射

每个 embedding \(\sigma:L\hookrightarrow\mathbf C\) 给出
\[
 q_\sigma=\sigma(q),\qquad a_\sigma=\sigma(a)=\pm8\sqrt2.
 \tag{K7}
\]
g1、g2、Fi的Taylor coefficients是有理数，所以 \(\sigma(f(q))\) 正是 canonical analytic packet \(f(q_\sigma)\)。某些 \(q_\sigma\) 不等于实际选定 regulator period q；它们仍是算术假设要求的完整 conjugate solution packet，不能省去其解析检验。

对每个σ必须选择实际使 \(f_i(q_\sigma)(\phi_\sigma(z))\) meromorphic 的map \(\phi_\sigma\)，满足主稿所列closed-disc/radial-limit regularity，并且 \(\phi_\sigma(0)=0\)。设
\[
 \psi_\sigma=\phi_\sigma/a_\sigma.
 \tag{K8}
\]
则 K5的conjugate pullback精确为
\[
 \widehat f_i^\sigma(\psi_\sigma(z))
   =2^{25}d_0d_\varepsilon
      f_i(q_\sigma)(\phi_\sigma(z)).
 \tag{K9}
\]
因此其meromorphy由真实qσpacket的假设给出。a的两个sign也付清，不能只使用positive embedding。

每个σ均有 \(|a_\sigma|=2^{7/2}\)。故
\[
 \log|\psi_\sigma'(0)|=
        \log|\phi_\sigma'(0)|-\rho,\qquad
 I(\psi_\sigma)=I(\phi_\sigma)-\rho.
 \tag{K10}
\]
费用在conformal size与Bost–Charles integral两边同时出现。不是仅减少分母、漏掉numerator。

K5的每个finiteplace上 coefficients由LCM型控制为subexponential growth，故unit-open disk收敛。各finite maps可取identity；没有额外正finite conformal size要免费加入。

## K4. extension不增加可用rank或容量

冻结实际rank证在 \(\mathbf C(t)\) 上已给nine-coordinate rank9、加1 rank10，并对每个fixedq成立。L(t)包含于 \(\mathbf C(t)\)，故同一functions在L(t)上仍独立；baseextension不能制造额外coordinate functions。坐标变换 \(t=a s\) 为 L-rational invertible scale，保持rank10与holonomicity。

作为 \(\mathbf Z\)-lattice，evaluation module的rank是 \([L:\mathbf Q]\,10(D+1)\)；CDT number-field slopes按field degree归一后有效rank仍是 \(10(D+1)\)。不能将degree2的extension当作多出一份holonomy容量。

若原来已对K的每个embedding τ有可用map，L上每个extensionσ可继承 \(\phi_\sigma=\phi_\tau\)，因为 qσ=qτ。normalized weights满足
\[
 \sum_{\sigma|_\!K=\tau}w_\sigma=w_\tau.
 \tag{K11}
\]
所以weighted arch sums没有复制收益。若map依σ另选，仍必须以这些normalized weights算全部σ，而非相加后不除field degree。

## K5. 精确新预算与common-domain障碍

置
\[
 A_\rho=\sum_\sigma w_\sigma I(\phi_\sigma)-\rho,\qquad
 L_\rho=\sum_\sigma w_\sigma
           \log|\phi_\sigma'(0)|-\rho.
 \tag{K12}
\]
在所列全部 arithmetic/analytic hypotheses成立、\(L_\rho>329/50\)时，先取ε使 \(L_\rho>\tau_\varepsilon\)，应用完整 L-all-place slopes，再令ε趋0，得到
\[
 \boxed{10(L_\rho-329/50)\le A_\rho.}
 \tag{K13}
\]
相对于有理C16安全版，主指数预算由 \(\log16\) 降至 \((7/2)\log2\)，精确差为 \((1/2)\log2\)。该费用来自已经证明的dyadic主界；本稿不声称它对所有possible integer models最优。

可精确陈述一个较小范围的最优性：若任意 algebraic scale b被要求在每个2-place上 \(v_2(b)\ge7/2\)，且在所有odd places上 \(v_p(b)\ge0\)，则product formula给
\[
 \sum_\sigma w_\sigma\log|\sigma(b)|
   =\sum_p\sum_{v|p}w_v v_p(b)\log p
   \ge\tfrac72\log2.
 \tag{K14}
\]
因每个rationalprime上 normalizedlocalweights总和1，a正好达到这个平均界。该 statement只针对按既有 uniform dyadic上界作all-place-clearing scale的条件类；它不证明实际periodcoefficients必须有该下界，也不排除另一个整数模型降低实际费用。

真实reference \(f(0)\) 定义于 \(\mathbf Q\)，经同一个a-scale定义于 \(\mathbf Q(\sqrt2)\)，再baseextend到actual参数的同一个 \(L=K(\sqrt2)\)，仍满足K3–K6且rank10。若某map family是q共同的，将它以完全相同L-embeddings及normalizedweights用于reference，便已强制K13。因此本改进仍不能凭common-domain数据反证actual q代数。canonicalorigin no-go与全部conjugate meromorphic条件保留。要得到数值定理，仍需value-sensitive域或新的完整packet。

## K6. 输入、阅读与范围

主输入为本轮 allodd稿 research/cdt_odd_R0_all_odd_generic_radius_arithmetic_interface_20261006.md（最终冻结439a21b2bdf35eeffcbf46e016b35e6ad3b11b635baa8e4148d6533741f6dc5a）、冻结 root dyadic稿 fea01700aa99716201ad0e36b161557f98f8e783755d7bfe144f434d1d59d3f8、冻结 exterior b02f39ae453143b72572bef7e91e53697bed90388108e79b267e27168dae96ef。

数域norm/embedding/slopes归一化依据本轮已实际读 CDT2025 PDF3–8 §2.3与CDT2024 PDF97–108/122–124。没有新PDF下载，没有producer，也不冒称又全文读这两份长primary。

新结论为K3/K4 complete \(8\sqrt2\) integer model与K13 all-place预算；不证明 \(\alpha_0=\pi^2(R_0-M_0)/16\) 超越或 \(R_0-M_0\) 无理，不把这两个目标等同。没有新ζ/L/Catalan数值定理或Lean。
