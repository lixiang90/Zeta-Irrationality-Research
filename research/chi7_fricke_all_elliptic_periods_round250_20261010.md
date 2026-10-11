# 第250轮：全部有限 Fricke 返回周期与共轭源的强制二重覆盖

2026-10-10，A。实际 FULL 复读冻结 A248/A249，以下把四个有限证书推广为全部 elliptic returns 的纸面定理。数学程序0，不扫描 group words、矩阵、素数或地图。结论在假设 g=g+∈Q(√2) 下排除减号共轭源的任何有限椭圆补支，并支付 y²=E(t) 的实际拉回；没有支付新的数值定理或全 CDT 预算。

## 1. 全部椭圆返回，而不要求四矩阵生成群

沿用 χ=χ−7、s=√2、K=Q(s)、Wτ=−1/(14τ)、Γ*=Γ₀(14)∪Γ₀(14)W，实际 Hauptmodul t 与
\[
E(t)=1-14t+19t^2-14t^3+t^4=Q_+(t)Q_-(t),
\quad A_\varepsilon=A_1+\varepsilon sA_2,
\quad I_\varepsilon=R+\varepsilon(2s/7)D,
\quad B_{\varepsilon,g}=A_\varepsilon(I_\varepsilon-g),
\quad \varepsilon\in\{+1,-1\}.
\]
A248 已付 Γ₀(14) 无 elliptic points、t 在 X₀(14) 上 degree2、W 商上 degree1、四个 Q± 根为全部 ramification。Γ* 的任何椭圆元素必在 W coset。写 γ=(a b;14c₀ d)，则 γW 的 determinant14、trace14(b−c₀)。椭圆要求 |trace|<2√14，故必 b=c₀、trace0。因此全部有限 stabilizers 都可写为
\[
\boxed{r=\begin{pmatrix}14b&-a\\14d&-14b\end{pmatrix},\qquad
ad-14b^2=1.}                                      \tag{A1}
\]
反过来 (A1) 给 r²=−14I，是实际 order2 返回。将 γ 乘−I 不改变 Möbius 作用或字符因子，可取 d>0；方程同时给 d 奇、(d,7)=1、(b,d)=1，a 也为奇数。没有另附经验搜索条件。固定点和完整 multiplier 为
\[
\tau_r=b/d+i/(\sqrt{14}d),\qquad
j_r(\tau)=-i\sqrt{14}\chi(d)(d\tau-b),
\quad A_\varepsilon(r\tau)=\varepsilon j_r(\tau)A_\varepsilon(\tau).
                                                        \tag{A2}
\]
在固定点 j_r=χ(d)。χ(d)=−1 对应 Q+，χ(d)=+1 对应 Q−；各相应 weight1 零点都是 simple。

这里的全叶量词可直接由实际覆盖支付。base 删除 t=0、∞ 和四根，H 也删除四根的全部 preimages 后，t 的限制是 Γ* 的 regular covering；这是已付 degree2 的 t-map、W 商 degree1 及 H 中完整 ramification 的结果，不把它误称 ordinary universal cover。任一由 native germ 沿有限路径取得的叶可写 Bε,g(Nτ)，N∈Γ*。若 τ₀ 的局部 stabilizer 是 r₀，该叶返回对应 N r₀ N⁻¹，在 Γ* 中仍是 (A1)；其固定点为 Nτ₀。故下文的全参数公式覆盖四个相同 base branchpoints 的所有 transported 到达叶，而不依赖 A249 四矩阵是否单独生成 Γ*。它不处理 cusp0/∞ 的补点，也不把一个实际源换成任意 quotient/filter。

## 2. 每个返回的完整 affine 周期

Θ²Iε=hε 的实际模驱动给 hε(rτ)=(εj_r)³hε(τ)。两次链式微分（Bol）因此给
\[
P_{r,\varepsilon}=(\varepsilon j_r)I_\varepsilon(r\tau)-I_\varepsilon(\tau),
\qquad P_{r,\varepsilon}''=0.
\]
(εj_r(rτ))(εj_r(τ))=1；involution 约束的 affine solution space 恰一维，basis εj_r−1。因此存在唯一实际常数 g_{r,ε}，对整个 H 有
\[
\boxed{I_\varepsilon(r\tau)-g_{r,\varepsilon}
=(\varepsilon j_r(\tau))^{-1}(I_\varepsilon(\tau)-g_{r,\varepsilon}).} \tag{A3}
\]
取 τ=b/d+i/(14d²ε₀)，rτ=b/d+iε₀，ε₀↓0；native Iε(τ)→0，|j_r|→∞。所以
\[
g_{r,\varepsilon}=\lim_{\epsilon_0\downarrow0}
 I_\varepsilon(e^{2\pi ib/d-2\pi\epsilon_0}).       \tag{A4}
\]
这给两个 affine coefficients 的完整常数，而不是仅命名一个未算 CM value。

极限严格存在。奇数 d 的 finite phase set 不含−1，故 R 的每个 logistic term 由常数倍 m⁻² 支配。另一方面
\[
T(z)=\sum_{m\ge1}\chi(m)z^m
=\frac{N(z)}{S_7(z)},\quad
N=z+2z^2+z^3+2z^4+z^5,\quad S_7=1+z+\cdots+z^6,
\]
且 C(q)=Σ_{k≥1}T(q^k)/k²、D(q)=C(q)−¼C(q²)。因为 (d,7)=1，所有 phase rays 避开 T 的非平凡七次单位根 poles，z=1 已 removable。因此 T 在这些闭 rays 上统一有界，1/k² 支配支付 C、D 的 Abel 极限。没有使用条件发散的 Σχ(m) 普通求和。

## 3. 通用有限 Fourier 公式及决定性的奇偶障碍

在 Q[z]/(z^d−1) 中，S7 乘法的 determinant 恰为7：在 z=1 特征值7，其余 d 次根通过 z↦z⁷ 的 permutation 使
\[
\prod_{\zeta^d=1,\ \zeta\ne1}\frac{1-\zeta^7}{1-\zeta}=1.
\]
所以唯一 c(z)=Σ_{a=0}^{d−1}c_a z^a，S7 c=N，满足
\[
\boxed{c_a\in\tfrac17\mathbf Z,\quad \sum_a c_a=1,\quad c_a=c_{d-a}.} \tag{A5}
\]
前两项由 integer multiplication matrix 的 adjugate 与 z=1 的值给出；后一项由 T(z⁻¹)=T(z) 和唯一性给出。包括 d=1，无须另作有限例外。

置 B₂(x)=x²−x+1/6、{x} 为 fractional part。复用官方 DLMF24.8.1 完整 n=1 公式 Σ_{k≥1}cos(2πkx)/k²=π²B₂(x)，其绝对收敛包括 endpoints。令
\[
D_{b,d}=\sum_a c_a\left[B_2(\{ba/d\})-\tfrac14B_2(\{2ba/d\})\right]\in\mathbf Q.
                                                        \tag{A6}
\]
由 (A5) 的对称性，C、D 在这些 cusps 为实，D(ζ_d^b)=π²D_{b,d}。原 R real part 恰 Y/2，Y=L(2,χ)。有限 Gauss 身份 Gχ=i√7 与同一 cosine formula 给
\[
q_{b,d}=-\frac17\sum_{j=1}^{d-1}\frac{(-1)^{j+1}}2
\sum_{a=1}^6\chi(a)B_2(\{a/7+bj/d\})\in\mathbf Q,
\quad R(\zeta_d^b)=Y/2+i\sqrt7\pi^2q_{b,d}.       \tag{A7}
\]
这里用了奇数 d 的精确 group-algebra identity
z/(1+z)=1/2+Σ_{j=1}^{d−1}(−1)^{j+1}z^j/2；没有 finite d 扫描。Gχ 的值及正号已在 A249 自含有限证明，本轮复用。于是全部返回周期是
\[
\boxed{g_{r,\varepsilon}=Y/2+\pi^2\left(i\sqrt7\,q_{b,d}
+\varepsilon\frac{2s}{7}D_{b,d}\right).}           \tag{A8}
\]

真正新关不是笼统地说这些 coefficients algebraic。对 0≤x<1，逐段直接展开有
\[
B_2(x)-\tfrac14B_2(\{2x\})=\tfrac18-\tfrac12\min(x,1-x).
\]
令 k_a 为 ba mod d 的0…d−1代表、M=Σ_a c_a min(k_a,d−k_a)。由 (A5)，M∈(1/7)Z，并且
\[
\boxed{D_{b,d}=\tfrac18-\frac{M}{2d},\qquad D_{b,d}\ne-\tfrac18.} \tag{A9}
\]
否则 M=d/2，而7M 是整数、7d/2 对奇数 d 不是整数。符号和 factor1/4 是关键；这个证明不要求 M 非负，不从 signed c_a 免费取得 positivity。

## 4. exact odd layer 与全部共轭叶不填

在 ζ=(τ−τ_r)/(τ−barτ_r) 中 rζ=−ζ，j_r=χ(d)(1+ζ)/(1−ζ)。令
\[
\widetilde A_\varepsilon=A_\varepsilon/(1-\zeta),\quad
\sigma=\varepsilon\chi(d),\qquad
\widetilde A_\varepsilon(-\zeta)=\sigma\widetilde A_\varepsilon(\zeta).
\]
完整权1 gauge 不得省去。由 (A3) 得
\[
B_{\varepsilon,g}(r\tau)-B_{\varepsilon,g}(\tau)
=(g_{r,\varepsilon}-g)(\varepsilon j_r-1)A_\varepsilon,
\]
以及 exact odd part
\[
\boxed{(B_{\varepsilon,g})_{\rm odd}=
\begin{cases}
-(g_{r,\varepsilon}-g)\zeta\widetilde A_\varepsilon,&\sigma=+1,\\
 (g_{r,\varepsilon}-g)\widetilde A_\varepsilon,&\sigma=-1.
\end{cases}}                                      \tag{A10}
\]
第一种 Ãε(0)≠0，第二种 Ãε 有 simple zero；t−t(τ_r)∼非零 ζ²。因此对应整个返回叶补点 iff g=g_{r,ε}，否则 first odd coefficient 非零，是真正 sqrt branch。把 τ 换成 Nτ 仅将 disk coordinate 乘一个非零相位，故上一节覆盖论证把 (A10) 推到全部 transported leaves。

现在只在假设
\[
g=g_+=Y/2+s\pi^2/28\in K
\]
下讨论 coefficient-conjugate actual source
\[
\bar B=A_-(I_- -\bar g),
\]
而不是对未知实周期 Y 作 field automorphism。任意有限返回若填点，(A8) 迫
\[
g-\bar g=\pi^2\left[\frac{s}{28}+\frac{2s}{7}D_{b,d}
-i\sqrt7\,q_{b,d}\right].                         \tag{A11}
\]
右边括号为非零代数数：其实部因 (A9) 不为0。左边代数，故将使 π² 代数，矛盾。该证明也覆盖 g=bar g，不需要事先证明这个差非零。

\[
\boxed{g_+\in K\Longrightarrow
\text{减号实际共轭源在四个有限分支点的每个到达叶均不填。}} \tag{A12}
\]
正号源的完整 criterion 同时已支付：g=g+ 时填点恰 q_{b,d}=0 且 D_{b,d}=1/8（即 M=0）。d=1 的 W 和整数平移返回确实填；本文没有断言这个正号 criterion 在所有其它到达叶均不成立，亦没有由它领取正处地图 cap。

## 5. 任意合法减号地图的实际 elliptic lift

设 φ:D→C 全纯、φ(0)=0、φ′(0)≠0，并且 native 共轭 germ \bar B∘φ 在 D 单值 meromorphic。若 φ(w₀) 是 E 的任一根，令 k=ord_{w₀}(φ−φ(w₀))。实际 continuation 到此点属于第1节某个叶；(A12) 与 (A10) 给非零 first sqrt coefficient。有限 ramification 只能在 k 偶数时将它变为 meromorphic。因此 E(φ) 的每个零点阶数为偶数。

从原点选 native 平方根并在删去零点的盘内延拓。任一 compact loop 围绕有限多个零点，E(φ) 的 winding 因每个零阶为偶数而为偶数，故平方根没有 sign monodromy；再以偶数局部阶数跨零点延拓。单连通 D 因而给唯一 native holomorphic yφ，满足
\[
\boxed{y_\phi(0)=1,\qquad y_\phi^2=E(\phi),\qquad
 w\longmapsto(\phi(w),y_\phi(w))}
                                                        \tag{A13}
\]
是到固定 affine elliptic curve y²=E(t) 的实际全纯 lift。这里并未要求 φ univalent 或原点只有一个前像；所有 foreign finite arrivals 都由 (A12) 支付。因为 φ 全纯，该 lift 避开 compact curve 的两个 infinity points。cusp0 的其它枝可能另有 obstruction，但不需为 (A13) 预领它们。

这恰是可接入 peer Abel/period/多place预算的几何输入；本稿没有执行或独审那些预算。没有从安全 LCD 得最优 joint 费用，也没有关闭任意新源、非线性投影或全部 CDT 方法。

## 6. 实际读取与停止边界

本轮 actual FULL 复读 A248 六节Q1–Q18，12413 B/SHA256 a95eda931df3fcf8042376b5a49d66bb60f8622f2772e3548178a176a853912b；A249 六节R1–R12，11197 B/SHA256 31c4ed25574a9670e37eb9f92e33487ba92ff9821cadf49083f746586cd1f917。另 actual FULL 读 A249 的来源scope与 DLMF Fourier规范化selection；只复用24.8.1完整 n1 statement，不宣称本轮重新 browse 全网页、阅读 Apostol原证明或重新审计247/archive。无新primary下载。

数学/CAS/program0，矩阵/word/map/prime/parameter扫描0，旧producer复跑0，Lean/git mutation0。程序工具只读写文档/hash；一次默认exec因ACL helper创建失败后，按授权escalated完成读取，不计数学执行。本文、本人NEW250 scope 保存后 actual FULL 作者自读并登记 bytes/SHA；作者自读不冒充独立review。旧248/249、main/policy/manifest和同伴文件写入0。
