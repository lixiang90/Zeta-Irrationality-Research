# 自然第三层 connection 的 primitive 陷阱

日期：2026-10-06。本稿仅审查从已证 level20 excellent Frobenius 输入自然接出的第三个 connection。结论：第三次组合的模p³消除是真实的，但在约去真实 Bol 方程并换回原 CDT 源格坐标后，完整 source row 共同含 **恰好 p²**。除掉它后只保证一层整性，不能为该方案增加新的 primitive 第三层 Smith 方向。本稿不排除其他更高阶方法，也不修改其它冻结稿。

## 1. 已证输入及规范

使用 [Frobenius 比值与两层稿](cdt_odd_level20_frobenius_20261006.md)、[其107项证书](cdt_odd_level20_frobenius_20261006_verify.json) 和 [完整模型](cdt_odd_level20_model_20261006.md)。取 p≥7，p∤20，排除假定有理周期的有限分母素数。K=Q(√5)，所有讨论在 p 上的 O_{K,𝔭} 完成。

令 ϑ=t d/dt。为避免与 Fourier q 混淆，用 **q_proj=t²Q(t)** 表示模型的 projective connection。以下字母均沿真实原点分支：

\[
g_s=(1-t)\sqrt\Delta,\quad R=N\sqrt C,
\quad k=R/g_s=\frac{N}{(1-t)\sqrt{C_o}},
\quad s=t(q(t)^p),
\]

其中 Δ=CC_o，且

\[
S=\theta_q\log t=g_s\Phi,\quad
\Phi/\Phi(s)\equiv G_p\pmod{p^3},\quad\deg G_p\le3p,
\quad\vartheta s=psb,\quad b=S(s)/S(t).
\]

令 Y=p³H，W 是冻结稿的真实 p-integral source 截断，则

\[
Y\equiv R G_p W(s)\pmod{p^3,t^{p^2}}.
\]

一般文献输入仍是 Beukers 固定 v3 pp3、15、17、20–21；这里使用此前已重新证明的完整 G_p，而非直接把其 Theorem1.13 用于零阶3的 Φ。

## 2. 第三次链式消除确实成立

设

\[
a=\vartheta\log k,\quad h=\vartheta\log g_s,
\quad \ell=\vartheta\log\Phi,
\quad z=\vartheta\log(g_sG_p),\quad z_S=\vartheta\log S=h+\ell.
\]

取

\[
\nabla_0=\vartheta-a-z,\qquad
\nabla_1=\vartheta-a,\qquad
\nabla_2=\vartheta-a+z.
\]

前稿给

\[
\nabla_1\nabla_0Y\equiv p^2k b g_s(s)
  [W_2(s)+h(s)W_1(s)]\pmod{p^3,t^{p^2}}.
\]

由 ratio 的 logarithmic derivative

\[
z\equiv z_S-pb\ell(s)\pmod{p^3},\qquad
\vartheta\log b=pbz_S(s)-z_S.
\]

因此第二层 prefactor 应用 ∇₂ 时，其 logarithmic derivative 与 +z 项合起来被 p 整除，内部 W_j(s) 的 ϑ derivative 也带因子 p。得到

\[
\boxed{\nabla_2\nabla_1\nabla_0Y\equiv0
       \pmod{p^3,t^{p^2}}.} \tag{1}
\]

Euler derivative 保持 t^{p²} 理想，所有 connection coefficients 在原点 p-integral。式(1)没有截断或坐标错误；陷阱出现在 primitive reduction。

## 3. 约去真实 Bol 方程

模型中 √S 满足 ϑ²√S+q_proj√S=0；令

\[
\mathcal B=k[\vartheta^3+4q_{proj}\vartheta
                          +2\vartheta q_{proj}]k^{-1}.
\]

这是原模型三阶算子乘t³后的 Euler 形式。对实际 H 有

\[
\mathcal BH=t^3U(t),
\]

而 t³U 是原点 p-integral 的固定 rational function。所以 𝓑Y=p³t³U≡0modp³。

直接展开得到

\[
(\vartheta+z)\vartheta(\vartheta-z)
 =\vartheta^3-V\vartheta-\tfrac12\vartheta V,
\quad V=2\vartheta z+z^2.
\]

置 F=V+4q_proj，则

\[
\boxed{\nabla_2\nabla_1\nabla_0-\mathcal B
 =k[-F\vartheta-\tfrac12\vartheta F]k^{-1}
 =-F\vartheta+(aF-\tfrac12\vartheta F).} \tag{2}
\]

因此在真实 rank4 系统中，该第三次组合约掉最高阶后只剩一阶 target row。

## 4. 公共 p² 因子及其确切阶

Riccati identity为

\[
2\vartheta z_S+z_S^2+4q_{proj}=0.
\]

将 z=z_S−pbℓ(s) 和 ϑlogb=pbz_S(s)−z_S 代入 F，得到

\[
F\equiv-p^2b^2
 [\ell(s)^2+2h(s)\ell(s)+2(\vartheta\ell)(s)]\pmod{p^3}.
\]

同一 Riccati identity 把方括号改为 −4q_proj(s)−2(ϑh)(s)−h(s)²。故

\[
\boxed{F\equiv p^2b^2\mathcal T(s)\pmod{p^3},
\quad\mathcal T=4q_{proj}+2\vartheta h+h^2.} \tag{3}
\]

用模型的明确 Q₈、Δ 精确化简：

\[
\boxed{\mathcal T(t)=
\frac{-8t(18t^4-36t^3+28t^2-10t+1)}{(1-t)\Delta(t)}
=-8t+O(t^2).} \tag{4}
\]

s=t^p+…，b(0)=1，所以 F/p² modp 的 t^p coefficient 是 −8。对每个 p≥7 均非零。因此(2)两个 coefficients 共同被 p² 整除，而 derivative coefficient −F 不被 p³ 整除；这个公共因子恰是 p²。

全级数 rational congruence 可在其他点测试：其分母在原点为 unit，清分母后的 polynomial 到原点形式级数的映射 modulo p^j 为单射。这里没有从有限 jet 推断全局 polynomial。

## 5. G_p³ 足以清分母

置 J=(1−t)Δ、D_z=JG_p。h 的分母为 J，z 的分母为 D_z，F 的分母为 D_z²，ϑF 的分母为 D_z³；a 的分母整除 NJ。因此

\[
\boxed{D=N[(1-t)\Delta G_p]^3} \tag{5}
\]

即可清(2)全部 coefficients，也可清固定 forcing t³U。D(0)=G_p(0)³是 p-adic unit，degree≤9p+17。令

\[
P_1=-DF,\qquad P_0=D(aF-\tfrac12\vartheta F).
\]

P₀、P₁属于 O_{K,𝔭}[t]，次数不超过9p+17；所有 coefficients 属于 p²，且 P₁/p² 的 t^p coefficient为8modp。因此不能将 (P₀,P₁) 直接当作模p非零的第三层方向。

## 6. raw coefficients、原 CDT 源格与 Smith

在 raw basis (1,H,ϑH,ϑ²H) 上，将(1)约去 Bol 方程后，物理 polynomial coefficients 为

\[
(D t^3U,\ P_0,\ P_1,\ 0).
\]

其 constant polynomial c₀=D t³U 未必含p²；例如其 t coefficient为(5√5−4)/20modp，p≠109时在每个好place为unit。因此 raw 四元 coefficients 并不共同含p²。raw constant polynomial在p³-scaled evaluation下自然输出p³，这只能描述raw coefficient格。

真正使用的是 [原 Smith bridge](cdt_odd_level20_hasse_smith_bridge_20261006.md) 的固定源格

\[
E_{4,D}=\ell_D^{-3}O_K[t]_{\le D}\oplus O_K[t]_{\le D}^{\oplus3},
\quad\ell_D=\operatorname{lcm}(1,\ldots,D).
\]

在合法窗口 √N<p≤D，v_p(ℓ_D)=1。同一个物理 constant polynomial c₀在此源格基中的坐标是 ℓ_D³c₀。故完整第三行的 **source coordinates** 实际为

\[
(\ell_D^3c_0,\ P_0,\ P_1,\ 0).
\]

第一坐标在p³中，target坐标共同恰在p²中。因此完整source vector共同恰含p²，其modp reduction是零。除p²之后 constant坐标仍在p中，target坐标有unit。设Ψ=p³eval；原第三关系Ψ(v)∈p³只给Ψ(v/p²)∈p。这是原E内的p-primitive一层方向，不能将raw constant S₃描述当成原E的免费primitive第三层或新的rank方向。rank7原source的constant block在此窗口也有valuation−3，解释相同；固定pole gauge只改变固定polynomial因子，不改变上述p-content。

写 target坐标 \(\widetilde P_i=P_i/p^2\)，相应必要 reduction为

\[
\widetilde P_0Y+\widetilde P_1\vartheta Y\equiv0\pmod p.
\]

这只是一层输入。模p下 ϑlog(F/p²)=−2z_S，因为其 numerator 是 t^p 的函数。因此

\[
\widetilde P_0+\widetilde P_1\vartheta\log A=0\pmod p,
\quad\vartheta\log A=a+z_S.
\]

它属于已有 Hasse 的一阶 rational annihilator 模。进一步 polynomial gcd/saturation 可以改变度数，但本自然第三层方案本身没有提供新的 primitive 第三层 Smith image。这里也没有证明其p-primitive row 不可能偶然获得第二层；只说当前模p³链条除去公共p²后保证的收益是一层。

## 7. 精确核验与范围

[独立脚本](cdt_odd_level20_third_layer_20261006_verify.py) 读取冻结107check证书中的完整 G_p modp³ 数据；不修改该输入。对固定 p=7、11、13，逐项检查清分母后全部 polynomial coefficients，而不只是前若干 coefficients：

- F numerator 的所有 coefficients 在 p²，且并非全部在 p³；F/p² 的首个 degree是p、coefficient是−8；
- 两个 embedding 的 P₀、P₁共同 p²且恰有p²，degree bound成立；
- 除p²后以完整 polynomial cross-multiplication验证其确属已有一阶 annihilator 模。

共54项精确检查。该脚本不重新计算 source packet或独立重新证明 excellent ratio；这些依据冻结稿及其独立审阅。第三次链条的依据是 §§2–4 的全素数推导。

辅助审阅记录：low_period_closure 已独立重推此前 Frobenius 稿 §5 的全形式级数、primitive 一阶障碍，包括真实 s'、p+2 pole、local factored lifts 和 generic double-root count；该限定障碍不用于本稿第三层结论。此前 Frobenius 及其它冻结文件保持原样。
