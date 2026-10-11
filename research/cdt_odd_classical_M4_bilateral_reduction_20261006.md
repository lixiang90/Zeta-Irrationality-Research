# 双边超几何端点：M₃ 的精确校准与 M₄ 的 forcing 边界归约

日期：2026-10-06。NEW 全尺度证明；冻结输入仅只读，不执行或 import 旧/同行 producer。本文给实际端点恒等式，不给新数值无理性或免费算术信用，也不降低已证的 rank5/rank10。

## 1. 固定归一化与结果

沿用冻结 [connection_moments](cdt_odd_connection_moments_20261006.md) 的

\[
 \Phi(t)=\left[\frac{\Gamma(t)}{\Gamma(t+1/2)}\right]^4,
 \quad T(e)=\sum_{n\ge0}\Phi(n+1/2+e),
 \quad M_j=(-1)^jT^{(j)}(0).
 \tag{B1}
\]

再定义真实收敛函数

\[
 R(e)=\sum_{n\ge0}\left[\frac{\Gamma(n+1+e)}{\Gamma(n+3/2+e)}\right]^4,
 \qquad R_0=R(0)>0.
 \tag{B2}
\]

本文完整证明

\[
 \boxed{M_3=8\pi^2M_1,\qquad
 M_4=20\pi^2M_2-24\pi^4M_0-24\pi^4R_0.}
 \tag{B3}
\]

下面还通过固定半周期值证明

\[
 \boxed{M_2=4\pi^2M_0,\qquad
 M_4=56\pi^4M_0-24\pi^4R_0.}
 \tag{B3a}
\]

结合 root 另稿的精确 Bailey 证明 [M₁=64L(f₈,3)](cdt_odd_bailey_M1_period_20261006.md) 及已核的 M₀=16L(f₈,2)，f₈=η(2τ)⁴η(4τ)⁴，可得 M₂=64π²L(f₈,2)、M₃=512π²L(f₈,3)。这不是用数值拟合推出，也不把 M₄ 的最后一项省略。

冻结 forcing 记号为

\[
 H(x)=\sum_{n\ge1}h_nx^n,
 \quad h_n=\pi^2\frac{\Gamma(n)^4}{\Gamma(n+3/2)^4},
 \quad K=(\theta+1/2)^4-x\theta^4,
 \quad KH=16x,\quad\theta=x\frac d{dx}.
 \tag{B4}
\]

因此另一种完全校准的表述是

\[
 \boxed{R_0=\frac{[(\theta+1/2)^4H](1)}{\pi^2}
 =\frac{[\theta^4H](1)+16}{\pi^2}.}
 \tag{B5}
\]

式中所有 H 的边界值都是从 0 沿 (0,1) 的 canonical 分支；不改变连接路径或积分格。

## 2. 原始来源与适用条件

实际读取的新固定原件为 W. Zudilin, *A Hypergeometric Version of the Modularity of Rigid Calabi–Yau Manifolds*, arXiv:1805.00544v2，16页。PDF5–7 的 (7)、Lemma3 和 Remark5：归一化 bilateral \({}_mH_m\) 乘 \(\prod\sin\pi(a_j+e)\) 后是有限 Fourier polynomial，模式 \(e^{\pi ike}\)，|k|≤m、k≡m mod2；在 z=1 且双边级数收敛时，两端模式 k=±m 不出现。

这里取 m=4，四个 a_j=1/2、四个 b_j=1。原文 (7) 的常数归一化是 Γ(1)⁴/Γ(1/2)⁴=π⁻²；本稿未除 π² 的双边和恰为该原文函数的 π² 倍。重复 half 参数不造成新奇点；可由局部一致收敛对参数连续延拓，亦可直接用下文独立证明。sum b−sum a=2，所以 z=1 的正、负两端都 O(n⁻²)，绝对收敛。

本文 §4 重新证明所需的模式限制与两个最高模式的消失，而不是只引用 Remark5 的描述。原文 PDF3–4 的一般模性数值观察及其它 conjectural L-value 关系不作为证明输入。实际原件阅读范围为 PDF1–8、13–14；PDF7 已渲染核对 Lemma3/Remark5 的公式和 bank/endpoint 限定。固定文献元数据与哈希见新独立 manifest，不改旧文献清单。

## 3. 真正双边级数与反射

在 e 不属于 1/2+Z 时定义

\[
 \mathcal B(e)=\sum_{n\in\mathbb Z}
 \left[\frac{\Gamma(n+1/2+e)}{\Gamma(n+1+e)}\right]^4.
 \tag{B6}
\]

对 n=−m−1 的每一项，Gamma 反射公式逐项给

\[
 \frac{\Gamma(e-m-1/2)}{\Gamma(e-m)}
 =-\tan(\pi e)\frac{\Gamma(m+1-e)}{\Gamma(m+3/2-e)}.
\]

四次幂使负号消失。因此在 e=0 的充分小圆盘内（亦在其它不含极点的共同域）

\[
 \boxed{\mathcal B(e)=T(e)+\tan^4(\pi e)R(-e).}
 \tag{B7}
\]

正负两尾在 compact e 集上一致 O(n⁻²)，可逐次求导。因而 e=0 的连续值就是 T(0)，没有把带极点的 formal 分解代入未定义的级数。特别在四次导数之前，负尾不能贡献；在第四次导数，它贡献 24π⁴R₀，必须保留。

令

\[
 \mathcal C(e)=\cos^4(\pi e)\mathcal B(e)
 =\cos^4(\pi e)T(e)+\sin^4(\pi e)R(-e).
 \tag{B8}
\]

Gamma 反射还给每一 summand 的 entire 写法

\[
 \cos^4(\pi e)
 \left[\frac{\Gamma(n+1/2+e)}{\Gamma(n+1+e)}\right]^4
 =\frac{\pi^4}
 {\Gamma(1/2-e-n)^4\Gamma(1+e+n)^4}.
 \tag{B9}
\]

Gamma reciprocal entire；compact 集上取足够大的正、负 n，再用相应的反射及右半平面 Stirling，仍有 O(n⁻²) 的尾界。有限项的 half-integer 极点已由 (B9) 消除。因此 C 是 entire。绝对收敛允许 B(e+1)=B(e) 的指标换元，cos⁴ 周期1，故 C 也是 period1 entire。

## 4. 全尺度 Fourier 界与最高模式消失

取 e=u+iy，0≤u≤1，|y|≥1。右扇形一致 Stirling 给

\[
 \left|\frac{\Gamma(z)}{\Gamma(z+1/2)}\right|^4
 \le C|z|^{-2},\qquad \Re z\ge0,\ |z|\ge1.
 \tag{B10}
\]

可先对大 |z| 用 uniform Stirling，再在剩余 compact 集上放大 C。正尾的 z=n+1/2+u+iy，负尾在 (B7) 中的 z=m+1-u-iy，均符合此界。后者在 u=1,m=0 时 Re z=0，但 |y|≥1，仍在闭右扇形，未遇 Gamma 极点。tan(π(u+iy)) 在这个域有统一界。由

\[
 \sum_{n\ge0}\frac1{(n+v)^2+y^2}=O(|y|^{-1})
 \quad(v\in[0,3/2])
\]

的积分比较，得到对 u 一致的

\[
 \mathcal B(u+iy)=O(|y|^{-1}),
 \quad \mathcal C(u+iy)=O(e^{4\pi|y|}/|y|).
 \tag{B11}
\]

period1 entire 的 C 降为 punctured plane 上的单值 holomorphic F(q)，q=e^{2πie}。其 Laurent series \(F(q)=\sum_{k\in\mathbb Z}c_kq^k\) 在整个 0<|q|<∞ 收敛。式 (B11) 给，r→∞ 和 r→0 时分别

\[
 \max_{|q|=r}|F(q)|=O(r^2/\log r),\qquad
 O(r^{-2}/|\log r|).
\]

Cauchy 系数界于是使 c_k=0 对所有 k≥2 和 k≤−2：k=±2 也因分母 log 而消失。这完整证明

\[
 \boxed{\mathcal C(e)=c_{-1}e^{-2\pi ie}+c_0+c_1e^{2\pi ie}.}
 \tag{B12}
\]

与原 Lemma3/Remark5 的 m=4 专门情形一致。这里不会把 |x|<1 的某条 bank 极限当作所有 continuation 的共同端点；只用实际绝对收敛 z=1 的 ε 函数。

因此全 e 恒等式

\[
 \mathcal C'''+4\pi^2\mathcal C'=0,
 \quad\mathcal C^{(4)}+4\pi^2\mathcal C''=0
 \tag{B13}
\]

成立。

还有一个固定而完全可定义的取值：式 (B8) 的右边在 e=1/2 的邻域全纯，因为 T(e) 在 Re e>−1/2、R(−e) 在 Re e<1 全纯。因此即使 B 本身在那里有极点，其已消极点函数 C 的实际值仍由连续性精确给

\[
 C(1/2)=R(-1/2)
 =\sum_{n\ge0}\left[\frac{\Gamma(n+1/2)}{\Gamma(n+1)}\right]^4
 =T(0)=C(0)=M_0.
\]

代入 (B12) 得 c₁+c₋₁=0；再由 (B8) 的一阶导数 C′(0)=−M₁，完整归一化为

\[
 \boxed{\cos^4(\pi e)T(e)+\sin^4(\pi e)R(-e)
 =M_0-\frac{M_1}{2\pi}\sin(2\pi e).}
 \tag{B13a}
\]

该式在 −1/2<Re e<1 成立，并通过 C 的 entire 继续给整个 e 平面。不是把 B 的极点直接赋有限值，而是取 (B9) 所确定的 C。特别 C″(0)=C⁽⁴⁾(0)=0。

## 5. 导数与两个精确校准

固定展开

\[
 \cos^4(\pi e)=1-2\pi^2e^2+\frac53\pi^4e^4+O(e^6),
 \quad\sin^4(\pi e)=\pi^4e^4+O(e^6)
\]

以及 (B8) 给

\[
 \begin{aligned}
 C'(0)&=-M_1,\\
 C''(0)&=M_2-4\pi^2M_0,\\
 C'''(0)&=-M_3+12\pi^2M_1,\\
 C^{(4)}(0)&=M_4-24\pi^2M_2+40\pi^4M_0+24\pi^4R_0.
 \end{aligned}\tag{B14}
\]

代入 (B13) 精确得到 (B3)；使用 C″(0)=0 再给 M₂=4π²M₀，代入 M₄ 的一般关系便得 (B3a)。未对任何未知周期作用 Galois conjugation，也不把所有 M_j 都归到 L(f₈,3)；高于四阶时 R(-e) 的新导数亦进入。

## 6. H 的边界项与作用域

Gamma recurrence 对每一 n≥1 精确给

\[
 (n+1/2)^4h_n
 =\pi^2\frac{\Gamma(n)^4}{\Gamma(n+1/2)^4}.
 \tag{B15}
\]

h_n=O(n⁻⁶)，所以 θʲH 在 x=1 的级数对 0≤j≤4 绝对收敛；它们从 (0,1) 的边界值可与级数求和交换。对 (B15) 求和即得 (B5) 第一式。对冻结的 KH=16x 取这个合法边界，得第二式。故还可写

\[
 M_4=20\pi^2M_2-24\pi^4M_0
      -24\pi^2[\theta^4H](1)-384\pi^2.
 \tag{B16}
\]

这是明确的 forcing-period 接口：需要校准的是 H 的实际四阶 boundary moment，而不是任意选一个 rational particular。另稿已证 H 实际 rank5 非分裂、M₄ 的 Z₄ 实际 rank5 非分裂；单个端点的关系 (B16) 不构成全函数的 gauge splitting，亦不把完整 F₂ 的 actual rank10 降成5。文献中的周期矩阵数值或 rational PSLQ，不替代此真实双边证明；本稿不新增整数模型、p-adic 层、合法解析叶或 arithmetic-holonomy 矛盾。

## 7. 新证书与准确审阅

同名 NEW `_verify.py/json` 仅作预定 symbolic 核对：四阶 Taylor 归一化、(B14) 导数、(B13) 三模式 identity、M₃/M₄ 常数、H coefficient recurrence 与 θ-shift。它不作素数/word/参数搜索，不执行或 import 冻结/同行 producer。全尺度证明由正文给出，有限检查不代替 Gamma 一致界和 Fourier 系数极限。

作者仅首次执行一次，19项固定检查全部通过；没有执行失败或再次运行。

首次执行后新增固定半周期值的纯正文证明 (B13a) 及推论 (B3a)，没有改变或再次执行 producer；该新增范围以实际数学审阅核对，不把先前19项检查说成覆盖其解析证明。

root 已实际阅读全文、PY/JSON（只读未执行），完整独核 §§3–6 的反射、entire compact tail、period1、闭右扇形一致 Stirling、纵向 O(1/|y|)、Laurent-Cauchy 连边缘模式的消失、M₃/M₄ 导数常数，以及 R₀ 与 canonical H 边界含16的归一化。首次全文审后又实际读取新增 (B13a)、(B3a) 与本节，独核 T/R 的共同域允许 e=1/2 取已消极点的 C、固定半周期值与 sin 校准。root 同时实际重读 Zudilin 固定v2的 PDF5–7（包括 Lemma3/Remark5），并实际读取独立 manifest；没有运行证书，不把有限检查当 Gamma 解析证明。

helper_tensor_budget 已实际只读原正文 §§1–7、PY/19项 JSON，并重读 Zudilin PDF5–7，独核反射负尾、entire/period、闭扇形与积分尾界、Laurent 模式、M₃/M₄ 原式、H 边界和 KH 归一化。又实际只读新增 §4/(B13a) 和 §1/(B3a)，独核 T/R 的共同全纯域、合法消极点的半周期值、完整 sin 校准、M₂ 与 M₄ 的简化式，限定通过。未执行 producer，未把新增解析证明记入旧19check范围，未认领 Smith 信用、rank 下降或新数值定理。

本稿至此冻结；后续新增研究另稿保存，冻结 producer/JSON 不再执行或修改。
