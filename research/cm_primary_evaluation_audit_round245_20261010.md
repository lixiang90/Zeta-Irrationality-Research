# 第245轮：导子7 CM 评价证明链及一个实际失配叶

2026-10-10，C。实际 FULL 读244冻结 CM 稿6783 B / 187cbbd9bda470a07691dc2c962dd5054144e6c65a6542491498bb9342456d9c；复用 Sun–Zhou 官方 v2 已存 HTML，完整读所需 §2.1–§2.3，不读无关三阶调和数 §3。结论：C1 的作者证明链可准确接通；存件中一个中间公式需补因子。另独立纸证一条 Fricke transported 叶不保留该关系。后者限制全叶补点，未排除所有合法图，未得到新数值无理性定理。数学程序0。

## 1. 对象、参数及原文证明范围

沿用原坐标 z：
\[
 F(z)=\sum_{n\ge0}a_nz^n,\quad G(z)=\sum_{n\ge0}a_nh_nz^n,\quad
 a_n=\binom{2n}n^3,\quad h_n=H_{2n}^{(2)}-\frac{25}{92}H_n^{(2)}.
\]
记 Y=L(2,\chi_{-7})，X=735Y−86π²，z₀=1/4096。为区别数值坐标，以下用 τ 表原文上半平面变量，并置
\[
 t=\alpha_4(\tau)=\lambda(2\tau),\quad z=\frac{t(1-t)}{16},\quad
 \tau_0=\frac{i\sqrt7}{2}.
 \tag{P1}
\]
Table 1 给 z(τ₀)=z₀、t₀=(8−3√7)/16、r=1/46。这里采用作者的 CM λ 参数值；不冒称本文重新证明了 Zagier [69, §6] 的一般 CM 特值理论。

原文 Theorem 1.1(a) 的使用域是2τ/i≥1，或 Re τ=1/2且 Im τ≥1/√2。τ₀属于第一域。Prop.2.2 的完整条件是 Im τ>0、|Re τ|≤1/2、|4t(1−t)|≤1、|τ|≥1/2；Clausen 分母由 (2.24)/(2.33) 非零。该域和分支选择不能省略。

本文将经典 holomorphic Eisenstein series 记 E₄，原文 Eichler integral (1.17) 另记 \(\mathcal E_4\)，非全纯 Epstein 函数保留 E(τ,2)。原存 HTML 的 TeX alttext 会合并前两个对象的字体区别；选段 HTML 保留原 MathML，本文公式按定义区分。

## 2. 必要完整 proof 链及中间公式补丁

1. Lemma2.1/(2.5)–(2.6) 完整 proof：参数二阶导数产生两种调和头；Clausen 型恒等式、Legendre 非齐次方程和 variation of parameters 给椭圆积分表达，边界常数由 (2.20)–(2.23) 决定。
2. Prop.2.2/(2.30)–(2.31) 完整 proof：Lambert–Ramanujan 积分恒等式及反射式 (2.27) 转成两个 quotient；Theorem1.1 完整 proof 进一步以 (2.39)/(2.46) 和倍角关系得到 Q₁,Q₂ 的 Epstein/Eichler 表达。
3. Prop.2.3(b) 完整 proof：在 \(\omega=(1+i\sqrt7)/2\) 使用 (2.64)–(2.66) 以及反射式/倍角式，得到
\[
 12\mathcal E_4(\omega)-\mathcal E_4(i\sqrt7)
 =\frac{29i\sqrt7}{6}+\frac{330\zeta(3)}{\pi^3i}.
 \tag{P2}
\]
代入 S_(1/46) 的正确定义后给 S_(1/46)(τ₀)=43π²/552。

重要补丁：存件 (2.67) 最后项仅写除184。由完整定义 (1.26) 逐项代入 r=1/46，必须是
\[
 S_{1/46}(\tau)=\frac{\pi^2 y^2}{69}
 +\frac{165\zeta(3)}{92\pi y}
 -\frac{\pi^2i[12\mathcal E_4(\tau+1/2)-\mathcal E_4(2\tau)]}{184y},
 \quad y=\operatorname{Im}\tau .
 \tag{P3}
\]
这是存件 TeX annotation 与正确代数定义的差别，不是 TXT 提取漏项；同类 (2.63)/(2.68) 亦少最后分母的 y。原件未改，未读取 PDF 来断言 PDF 同误。使用 (1.26) 可直接绕过这处 display。将 P2 代入 P3，在 y=√7/2 时 ζ(3) 精确抵消，π²系数为7/276+29/552=43/552，因此作者的最终 (2.58)/C1 不变。

以上原文仍引用 upstream 的经典 Clausen/Legendre、Lambert 和 λ 特值身份；本文完整读了 Sun–Zhou 使用它们的 statements/proofs，并未 FULL 读 [12],[14],[69],[72],[75] 所有原著。§2.3还完整读到 Prop.2.4；其加权一阶评价不是当前 C1 必要输入。§3不是这条证明链，未读。

## 3. 两个 χ₋₇ Epstein 表值的自含核对

这两个表值原文引用 Glasser–Zucker [37, Table VI]。这里另给所需两值的纸证，不领取其它 Table1 CM 行。

令 \(\mathcal O=\mathbb Z[\omega]\)，Norm(a+bω)=a²+ab+2b²。任意复数先按虚部选整数 b，再按实部选整数 a，其到 a+bω 的平方距离至多1/4+7/16=11/16<1。因此此环对范数 Euclidean，所有理想主、单位仅±1。Euler factors：2分裂、7分歧，其它 prime 由二次特征 χ₋₇ 控制；故
\[
 S=\sum_{(a,b)\ne(0,0)}\frac1{(a^2+ab+2b^2)^2}
 =2\zeta(2)Y.
 \tag{P4}
\]
这也可直接由 Euclidean 唯一因子分解按 split/inert/ramified 三类相乘验证。由原文 (1.18) 的归一化，
\[
 E(\omega,2)=\frac{7S}{8\zeta(4)}
 =\frac{105Y}{4\pi^2}.
 \tag{P5}
\]
\(\sqrt7i=2\omega-1\) 对应 b 偶的子格。\(\mathcal O/2=\mathbb F_2\times\mathbb F_2\)：b偶的元素恰是 norm 奇的元素或2倍的全部格点。去掉两个2-adic split Euler factors给奇范数和 (1−2⁻²)²S=9S/16；2倍格点给 S/16。因此子格和为5S/8，故
\[
 E(i\sqrt7,2)=\frac{7}{2\zeta(4)}\frac58S
 =\frac{525Y}{8\pi^2}.
 \tag{P6}
\]
全部格和绝对收敛，无条件交换问题；这两项正好是 Table1 当前行的归一化。

由 (1.21)/(1.22) 及 S 的定义，
\[
 Q_1-Q_2/46=S_{1/46}
 -\frac{\pi^2}{23}E(\tau+1/2,2)
 +\frac{\pi^2}{138}E(2\tau,2).
\]
在 τ₀代 P3/P5/P6，得到
\[
 \boxed{\frac{G(z_0)}{F(z_0)}
 =\frac{43\pi^2}{552}-\frac{245Y}{368}
 =\frac{86\pi^2-735Y}{1104}=-X/1104.}
 \tag{P7}
\]
因1/4+1/46=25/92，Q₁−Q₂/46确为本项目 G/F，未换调和头。P7是作者 (1.12) 的核对，不是新的数值无理性结果。

## 4. 一条同一源的真实 Fricke 续接叶

Prop.2.2 的两个 RHS 是上半平面全纯函数；在 compact 子集上指数尾一致收敛。具体令
\[
 A(\tau)=\sum_{\substack{k\ge1\\ k\ \mathrm{odd}}}
 \frac{2}{k^2\cosh^2(k\pi\tau/i)},
\]
\[
 B(\tau)=\sum_{k\ge1}\frac{2}{k^2\sinh^2(4k\pi\tau/i)}
 -\sum_{k\ge1}\frac{1}{2k^2\sinh^2(2k\pi\tau/i)}
 +\sum_{\substack{k\ge1\\ k\ \mathrm{odd}}}
 \frac{2}{k^2\sinh^2(k\pi\tau/i)}.
 \tag{P8}
\]
初始域内 A=Q₁、B=Q₂，故 \(\widehat Q=A-B/46\) 匹配 G/F。原文脚注4已经明确 Fricke 变换 τ↦−1/(4τ) 不保持这些 RHS 的值；不能从 z 参数不变推出响应不变。

取
\[
 \tau_1=-1/(4\tau_0)=i/(2\sqrt7),\quad
 t_1=1-t_0,\quad z(\tau_1)=z_0.
 \tag{P9}
\]
必须说明这是一条实际续接，而不是把超出定理域的 power series 强行求值。由 Clausen (2.33)，沿 t∈(0,1) 邻域的 F 拉回是
\[
 \widetilde F(t)=(2/\pi)^2\mathbf K(\sqrt t)^2,
\]
它在这条实段非零。式 (2.24) 给 \(\tau=i\mathbf K(\sqrt{1-t})/(2\mathbf K(\sqrt t))\)，沿实段从 τ₀走到τ₁。此参数的导数非零：分子微分贡献负项、分母微分亦贡献负项，因 K,K′>0。绕过 t=1/2的小弯，其 z像由
\[
 z-1/64=-(t-1/2)^2/16
\]
绕 z=1/64一次；整个路径可避开0、1/64和∞。P8全纯且在起点邻域等于原 quotient，由解析唯一性与 F 的拉回匹配，遂给同一 F,G 的 transported 分支。没有在 z=1/64 本身穿越奇点。终点 F 非零。

## 5. 精确不等式：目标 native 关系在该叶不消 log

初始 h₀=0，0≤h_n<2；a_n≤64ⁿ。故
\[
 0\le Q_{\rm native}=G(z_0)/F(z_0)
 \le2(F(z_0)-1)/F(z_0)\le2/63.
 \tag{P10}
\]
对 y₁=Im τ₁=1/(2√7)，有 πy₁<2/3。利用
\(\cosh x\le(1-x^2/2)^{-1}\)（0≤x<√2；逐项用(2j)!≥2^j）及 sinh x≥x，
\[
 A(iy_1)\ge98/81,\qquad
 B(iy_1)\le\frac{2\zeta(4)}{\pi^2y_1^2}
 =\frac{28\pi^2}{45}<56/9.
\]
这里 B 的负项直接舍去；两种正项分别贡献 ζ(4)/(8π²y₁²) 和15ζ(4)/(8π²y₁²)。于是
\[
 \boxed{\widehat Q(\tau_1)>98/81-28/207>1.}
 \tag{P11}
\]
只用 π<22/7、√7>5/2、π²<10；没有数值样本或不明 L 值大小。

令 g*=X/1104=−Q_native。原生 S_(g*)在 z₀为0，另一叶却满足
\[
 \frac{S_{g*,\,{\rm transported}}(z_0)}
 {F_{\rm transported}(z_0)}
 =\widehat Q(\tau_1)-Q_{\rm native}>1-2/63>0.
 \tag{P12}
\]
因此同一 H_(g*) 在该 transported 叶的 z₀仍有非零 log 系数−S/4096。即使假设 g*∈Q，也不能全叶补点。有限 ramification z−z₀∼c(w−w₀)^e仅将 log 系数乘正整数 e，不能把这一个坏叶变亚纯。

## 6. 准入作用及仍缺的接口

P12直接排除“所有 CM 原像都照 native 评价取消”这一免费步骤，并不排除某个限制 monodromy、避免这条坏叶的共同图。不能借脚注或一个坏叶宣布全部图 no-go。需要实际地图证书逐个记录 preimage、返回路径及所选全部行的亚纯性。

Lemma2.1 的变参数表达和 P8 为计算实际 monodromy/连接提供输入，但本稿没有从它们领取七行函数独立或 minimal rank。244 G-function/holonomic 上界仍保留；Root 本轮全素数分母收紧另经独立 FULL 纸核、收据单存，不代替秩或全叶。

245–246仍是唯一有界 CM 准入；formal复盘248。若剩下的只有 native 补点、safe 类型或形式秩，不能自动延长。目标仍 active；数学程序、CAS、参数/prime扫描、Lean、外仓库写、新原件 GET 都0。新保存仅既存原文选段、提取记录、本文及读取 scope；最终保存后实际 FULL 作者复读。
