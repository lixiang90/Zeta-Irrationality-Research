# 第247轮：χ−7 的 dyadic 两周期源与完整 Fricke 比较

2026-10-10，A。数学程序 0；以下恒等式均为纸证。记 χ=χ−7、Y=L(2,χ)、L₃=L(3,χ)、q=e^{2πiτ}、Θ=q∂q。本文支付两个真实 primitive、全部系数及一个完整 Fricke cocycle；没有证明新的数值无理性、线性无关性或 CDT 严格预算。

## 1. 原始两方向与去常数问题

取 Stein Equation (4)/Theorem 5.8 的规范
\[
 E_0=E_{3,\chi,1}=\sum_{n\ge1}e_nq^n,
 \quad e_n=\sum_{d\mid n}\chi(n/d)d^2,
\]
\[
 E_1=E_{3,1,\chi}=-\frac87+\sum_{n\ge1}a_nq^n,
 \quad a_n=\sum_{d\mid n}\chi(d)d^2.                 \tag{D1}
\]
字符为奇字符，故 χ(−1)=−1=(−1)³ 满足所用全纯模性定理。常数 −8/7 可直接由 generalized Bernoulli 数核：χ 在 1,…,6 为 (+,+,−,+,−,−)，其三个带权和为 −7、−49、−295，故 B₃,χ=48/7。

定义 |q|<1 的绝对收敛级数
\[
 K(q)=\sum_{n\ge1}\frac{e_n}{n^2}q^n
     =\sum_{m\ge1}\frac{\chi(m)}{m^2}\frac{q^m}{1-q^m},
\quad C(q)=\sum_{m\ge1}\chi(m)\operatorname{Li}_2(q^m)
         =\sum_{n\ge1}\frac{a_n}{n^2}q^n.             \tag{D2}
\]
于是 Θ²K=E₀，而 Θ²C=E₁+8/7。原 C 的模驱动去掉常数后确实改变模性；本文不用 E₁+8/7 作为模形式。E₁ 的二重 primitive 是 C−(4/7)(log q)²，它在 native q=0 有非全纯项。

唯一可在 C(q)−cC(q²) 中抵消这个常数的 c 为 1/4，因为 Θ² 对第二项产生 4c。取
\[
 R=K(q)-2K(q^2)
   =\sum_{m\ge1}\frac{\chi(m)q^m}{m^2(1+q^m)},
 \quad D=C(q)-\frac14C(q^2).                          \tag{D3}
\]
其真实驱动为
\[
 h_R=\Theta^2R=E_0(q)-8E_0(q^2),\qquad
 h_D=\Theta^2D=E_1(q)-E_1(q^2).                        \tag{D4}
\]
两者均在 M₃(Γ₀(14),χ) 全纯、native 常数 0。此处只调用明确的 oldform 模性 statement，不重证 Miyake 的一般定理。

## 2. 严格 Abel 极限与完整 prefix

令
\[
 T(x)=\sum_{m\ge1}\chi(m)x^m
 ={x+x^2-x^3+x^4-x^5-x^6\over1-x^7}.                  \tag{D5}
\]
T 在 x=1 的 removable value 为 1，因为 Σχ(m)m=−7；直接代入也有 T(−1)=1。它在 [−1,1] 连续有界。绝对重排得 C(q)=Σ_{k≥1}T(q^k)/k²。因此 dominated convergence 支付
\[
 C(e^{-a})\longrightarrow\zeta(2),\quad
 C(-e^{-a})\longrightarrow\zeta(2),\quad
 D(\pm e^{-a})\longrightarrow\frac{\pi^2}{8}.         \tag{D6}
\]
没有把普通发散和 Σχ(m) 命名为 1；这是实际 Abel 极限，恰与解析延拓 L(0,χ)=1 一致。

第246轮已付 K(e^{-a})=L₃/a−Y/2+o(1)。或者直接用 D3 的 bounded logistic kernel，可得
\[
 R(e^{-a})\longrightarrow Y/2.                       \tag{D7}
\]
所有 n≥1 的确切系数为
\[
 [q^n]R={e_n-8[2\mid n]e_{n/2}\over n^2},\qquad
 [q^n]D={a_n-[2\mid n]a_{n/2}\over n^2}.              \tag{D8}
\]
故 d_N² 清除 R,D 的完整前 N 项，以及任意固定 Θ^j 行；无需额外固定 4。对普通 ∂q^j，只先微分 degree-N truncation 才共用 d_N²；先微分完整级数再保留 degree N 需 d_{N+j}²。固定 rational 关系的分母须另保留。这是合法安全模型，未声称 primitive LCD 或联合源格最优。

## 3. 支付全函数 Fricke 比较的模形式身份

复用第246轮实际已证 u=(η(7τ)/η(τ))⁴ 为 X₀(7) degree-one 坐标，f=η(τ)³η(7τ)³ 在 H 无零、两个 cusps order 1，以及 E₀/f=1+8u。对 E₁/f，同一 divisor 论证给 Laurent 空间 span{u⁻¹,1,u}。这里先付 degree bound 再用三个系数，不是从有限头猜身份。

由 u=q+4q²+14q³+…、f=q−3q²+0q³+…，
\[
 E_1/f=-8/(7q)-17/7-16q/7+\cdots,
 \quad u^{-1}=q^{-1}-4+2q+\cdots,
\]
唯一得
\[
 E_1=-f\left(7+{8\over7u}\right).                   \tag{D9}
\]
η 的主平方根 S 变换给 u(W₇τ)=1/(49u)、f(W₇τ)=i7√7 τ³f(τ)。D9 与 E₀ 身份于是支付
\[
 E_0(W_7\tau)=-i\sqrt7\,\tau^3E_1(\tau),\qquad
 E_1(W_7\tau)=-i49\sqrt7\,\tau^3E_0(\tau).
\]
令 w=W₁₄τ=−1/(14τ)，D4 的实际 oldform 组合满足
\[
 h_R(w)=8i\sqrt7\,\tau^3h_D(\tau),\qquad
 h_D(w)=49i\sqrt7\,\tau^3h_R(\tau).                  \tag{D10}
\]
字符、常数与 q² 的所有 chain factors 均保留。

## 4. 完整耦合 period cocycle及实际混合出口

对任何 Θ²I=h，直接两次微分有
\[
 \Theta_\tau^2[\tau I(w)]={h(w)\over196\tau^3}.
\]
故 D10 表明 τR(w)−c_R D(τ) 与 τD(w)−c_D R(τ) 均为 affine，
\[
 c_R=2i\sqrt7/49,\qquad c_D=i\sqrt7/4.
\]
沿 τ=iy→i∞，D6/D7 与 R,D→0 唯一确定 affine 的斜率为 Y/2、π²/8。再用 W₁₄²=id 及 c_Rc_D=−1/14 确定两个常数，得到对整个 H 的真实恒等式
\[
 \boxed{\tau R(w)={2i\sqrt7\over49}D(\tau)
            +{Y\over2}\tau-{i\sqrt7\pi^2\over196},}
\]
\[
 \boxed{\tau D(w)={i\sqrt7\over4}R(\tau)
            +{\pi^2\over8}\tau-{i\sqrt7Y\over8}.}     \tag{D11}
\]
不需要 Mellin contour 的未付误差；仿射性来自完整驱动身份，常数来自严格极限与 involution。

特别地令 I±=R±(2√2/7)D、g±=Y/2±√2π²/28，则
\[
 I_\pm(W_{14}\tau)-g_\pm
 ={\pm i\over\sqrt{14}\tau}[I_\pm(\tau)-g_\pm].     \tag{D12}
\]
在 τ*=i/√14，只有减号式强制
\[
 R(\tau_*)-{2\sqrt2\over7}D(\tau_*)
       ={Y\over2}-{\sqrt2\pi^2\over28}.              \tag{D13}
\]
加号式的 g+ 是实际 cocycle 的响应，不是断言 I+(τ*)=g+。若再取 A+=A(τ)+√2A(2τ)，Yang 的 A 变换给 A+(W₁₄τ)=−i√14τ A+，所以 A+(I+−g+) Fricke-invariant。这仅支付该固定点的解析 even 性；本文没有支付其完整代数坐标、零点规范、实际独立秩或全叶准入。

## 5. 其它 cusp 的精确有限部分，不能只看 q=1

Γ₀(14) 的四个 cusp 可取 ∞、0、1/2、1/7。所有下式使用明确 radial 坐标 q=ξe^{-a}，a↓0；有限部分随坐标规范而变，本文不将表格直接冒认完整 monodromy 矩阵。

由奇偶分拆 D3，
\[
 R(-e^{-a})=-{7L_3\over8a}+{Y\over2}+o(1).          \tag{D14}
\]
减去奇数 m 的 −1/(am) 后，各 kernel uniformly bounded，故常数的 dominated convergence 合法。D 在同一路径无 pole，D6 已给有限值 π²/8。

令 ζ=e^{2πi/7}、𝔤=Σ_{r=1}⁶χ(r)ζ^r。对每个 k mod 7，有限个 rational kernel 的 Laurent 展开为
\[
 T(\zeta^ke^{-v})={\mathfrak g\chi(k)\over7v}
       +\beta_k+O(v),\quad
 \beta_k=\sum_{r=1}^6\chi(r)(1/2-r/7)\zeta^{kr},     \tag{D15}
\]
其中 k=0 的 pole 0、β₀=1。减去 pole 后的余项对全部 v>0 有统一界，故 Σk⁻² 支配，支付 C 的有限部分。β_k 的 Fourier 权重对 r↔7−r 对称，利用
Σk≥1 cos(2πkx)/k²=π²B₂(x)，得
\[
 C(\zeta^he^{-a})={\mathfrak g\chi(h)L_3\over7a}
   +\pi^2\sum_{r=1}^6\chi(r)(1/2-r/7)B_2(\{hr/7\})+o(1).
\]
在 h=1,2，两个有限系数分别为 55/2058 与 −137/2058；B₂(1/7),B₂(2/7),B₂(3/7)=(13,−11,−23)/294。χ(2)=1，故
\[
 D(\zeta e^{-a})={\mathfrak gL_3\over8a}
                         +{119\pi^2\over2744}+o(1). \tag{D16}
\]
𝔤 非零，例如其虚部为 2(sin(2π/7)+sin(4π/7)−sin(6π/7))>0；pole 真实非零。

R 在 ζ 处的 logistic 分母不为 0，绝对支配允许逐项极限。其实部为 Y/2，非实项为
\[
 {i\pi^2\over196}\sum_{r=1}^6
    \chi(r)\tan(\pi r/7)\csc^2(\pi r/7)
 ={i\pi^2\over49}[\csc(2\pi/7)+\csc(4\pi/7)-\csc(6\pi/7)]=0.
\]
这里对本处 g(0)=0 的 residue-periodic 偶 7 周期序列，求和用
Σm≥1 g(m)/m²=π²Σr=1⁶g(r)csc²(πr/7)/98；不能把 residue 值误当 Fourier 系数直接乘 B₂。最后的三角恒等式乘 sin(π/7)sin(2π/7)sin(4π/7) 后用 product-to-sum 即证。因此 R(ζe^{-a})→Y/2。

两源在 cusp 0 均无 a⁻¹；R 在 1/2 有 pole、D 没有，D 在 1/7 有 pole、R 没有。故任何固定组合 αR+βD 同时删除这两个 pole，必须 α=β=0。这里 pole 是已识别的 Tate 方向；该限定障碍不排除另加 Tate primitive、完整整数 period projector、其它解析图或相对周期。D11 已付 Fricke 全函数比较，却不能从两个 endpoint 值宣称全部 cusp 属于同一个可免费消去的 jump 行。

## 6. 文献边界与单一未付接口

本轮实际核 CDT 官方 arXiv 2408.15403v2 的当前身份、所存作者本物理 PDF1–5、33–35 完整选段：Theorem A 针对 χ−3，§2.11 的收益来自同一 homogeneous function 的完整 monodromy coefficient，以及关系真正诱导 overconvergence。它没有在这些所读段落支付本文 level14 的全叶、源秩或预算。Gun–Kandhil–Philippon arXiv2212.00366 的本轮读域仅 abstract；它明示讨论 same-parity 范畴，不能当成 k=2、odd χ−7 的结论。有限检索不证明全球新颖性；本文不宣称 Y、g± 或三周期线性无关性已知或首次解决。

最强新资产是 D8 完整整模型与 D11/D12 实际两响应 Fricke cocycle。下一首证书应是：在同一个实际 level14 代数源中支付目标关系诱导的完整 jump cancellation，并核实际独立秩与解析图；原 level7 的非模常数项/非Dfinite分析不能未经比较直接搬到相关 dyadic 差分。单独 endpoints、安全 LCD 或模驱动身份都不支付这项，更不支付同对象 strict 算术 holonomy 预算。

程序账本：数学程序、扫描、Lean、git mutation 均 0。只新增本文及本人来源记录，246 及更早冻结稿未改。
