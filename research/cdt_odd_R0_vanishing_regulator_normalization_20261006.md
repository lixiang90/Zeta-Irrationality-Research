# R0 的真实消失球 regulator、整数 Tate 常数及三维剩余差额

日期：2026-10-06。本稿是 NEW 全尺度纸面证明；旧稿、同行稿、数学 PY/JSON 与 manifest 均只读。没有创建、执行或导入数学 producer。本稿以已核验的紧化 family、regulator derivative、实际 compact projector 和 Yukawa 为输入，新增一个真实 Betti 归一化条件，不宣称数值无理性或完整 scalar-regulator 等式。

## 1. 对象、规范与新增结论

采用冻结稿中的实际对象
\[
 \theta=x\partial_x,\quad t=1-x,\quad
 P=\theta^4-x(\theta+\tfrac12)^4,\quad
 \phi=\prod_{j=0}^3(v_j+2+v_j^{-1}),\quad \lambda=256x,
\]
\[
 v_j=(1+u_j)/(1-u_j),\qquad
 F_x=1-x\prod_{j=0}^3(1-u_j^2),\qquad
 \omega=\sqrt{x}\operatorname{Res}_{F_x=0}\frac{du_0\wedge\cdots\wedge du_3}{F_x}.
\]
始终使用左留数、raw cup 配对第一参数在前，以及
\[
 Q_4=(2\pi i)^4,\qquad
 \kappa_{\rm raw}=-(2\pi i)^3/16.
\]
指定唯一有理 family class 为 \(\Xi\in CH^4(Y,4)_{\mathbf Q}\)。实际紧化 cohomology lift 的四维投影 \(r\) 已证明满足
\[
 \nabla_\theta r=16\sqrt{x}\,\omega,\qquad
 \nu=Q_{\rm raw}(r,\omega),\qquad P\nu=-(2\pi i)^3\sqrt{x}.
 \tag{V1}
\]
这些是输入，不是本稿重新证明的结论。

令 \(\delta\) 是节点附近、实 \(x>1\) 上取 outward real orientation 的真实消失三球，并延拓到选定的 conifold punctured disk。其实际周期及另一真实闭周期满足
\[
 g=\int_\delta\omega=-\pi^2v(t),\quad
 v(t)=t+\tfrac34t^2+\tfrac{29}{48}t^3+\cdots,\qquad
 \Gamma\cdot\delta=-8,
 \tag{V2}
\]
其中 \(v\in\mathbf Q\{t\}\)，\(Pv=0\)。这里 \(\operatorname{PD}\delta\) 属于真实 compact rank-four sector；不假设整个 compact/open \(H^3\) rank four。

对局部 symbol 的 principal-log representative 定义实际周期 \(A_\delta\)。本稿证明
\[
 \boxed{A_\delta(t)=16\pi^2\int_0^t\frac{v(s)}{\sqrt{1-s}}\,ds},\qquad
 A_\delta(0)=0,
 \tag{V3}
\]
以及精确整数 Tate 比较
\[
 \boxed{A_\delta=256\mathcal C_0(W,g)+(2\pi i)^4}.
 \tag{V4}
\]
因此候选全纯 scalar
\[
 \nu_{\rm corr}=-16(2\pi i)^3\Psi,\qquad
 \Psi=W-\pi^4 y_0/16
 \tag{V5}
\]
与真实 regulator 的 canonical vanishing-cycle evaluation 完全对齐。实际 compact lift 可以通过有理 Tate-period shift 达到这个消失球归一化；归一化后
\[
 \boxed{\nu_{\rm can}-\nu_{\rm corr}\in\ker P\cap\mathcal O_{t=0},
 \quad \dim(\ker P\cap\mathcal O_{t=0})=3.}
 \tag{V6}
\]
这给出一个条件明确的真实 compact scalar 全纯 lift。它只消去原四维齐次差额的一个方向，没有确定另外三个全纯系数。

## 2. 实际局部 symbol regulator，无紧化 graph 的额外前提

节点 \(u=0,x=1\) 在 \(Y^*=U^4\) 的内部。取足够小的 total-space neighbourhood，所有 \(v_j\) 都接近1，避开 \(0,\infty,-1\) 和负实 logarithm cuts。采用 \(\log v_j\) 的 holomorphic principal branch，\(\log1=0\)。四个 unit Deligne classes 的乘积由
\[
 R_{\rm loc}=\log v_0\,d\log v_1\wedge d\log v_2\wedge d\log v_3
 \tag{V7}
\]
代表，且在 total space
\[
 dR_{\rm loc}=\Omega:=d\log v_0\wedge\cdots\wedge d\log v_3.
 \tag{V8}
\]
这是 KLM published PDF8 Proposition4.2 的 unit-cup product，配合 PDF12 的 regulator ring homomorphism 和 restriction。局部所有 cuts 为空，product 的其余 delta 项为零。\(v_j=1\) 时主 logarithm 为0，表达式本身 holomorphic 延拓；不是要求 raw cubical graph 在紧化边界同时满足全部 face 条件。

\(\Xi\) 在这个 neighbourhood 限制为指定 unit symbol。故 KLM PDF13 的 \((p,n)=(4,4)\) cycle-evaluation 规范给
\[
 \int_\delta r\equiv\int_\delta R_{\rm loc}\pmod{Q_4\mathbf Q}.
 \tag{V9}
\]
本例 cohomological prefactor \((-2\pi i)^{p-n}=1\)，没有额外 Tate 除法。局部表达式固定一个具体代表；全局紧化 lift 的评价仅由 (V9) 固定模有理 Tate 常数。

令 \(A_\delta=\int_\delta R_{\rm loc}\)。在 holomorphic Morse coordinates 中，实球半径 \(r\to0\)，\(\log v_0=O(r)\)，三个 smooth one-forms 在球上的积分尺度为 \(O(r^3)\)。故
\[
 A_\delta=O(r^4),\qquad A_\delta(0)=0.
 \tag{V10}
\]
也可直接用实际 real Morse ball \(D_\tau\)、\(\partial D_\tau=\delta\)，在 total neighbourhood 中 Stokes：
\[
 A_\delta=\int_{D_\tau}\Omega.
\]
\(\Omega=16\,du_0\wedge\cdots\wedge du_3+O(|u|^2)\)，\(\tau=(x-1)/x\)。换到实际 Morse ball 坐标后，volume density 的常数项仍为16；其一次项在中心对称的球上积分为零，二次及更高项给 \(O(\tau^3)\)。ball 的 real four-volume 为 \(\pi^2\tau^2/2\)，所以
\[
 A_\delta=8\pi^2(x-1)^2+O((x-1)^3).
 \tag{V11}
\]
这一 leading term 是符号和因子16的独立局部核对。

Cartan formula 应用于 (V8)，并沿 flat \(\delta\) transport，给
\[
 \theta A_\delta=16\sqrt{x}\,g.
 \tag{V12}
\]
代入 \(\theta=-(1-t)\partial_t\) 与 (V2)，即
\[
 \partial_t A_\delta=16\pi^2v(t)/\sqrt{1-t}.
\]
初值 (V10) 唯一确定 (V3)。这是实际局部 regulator 周期，未使用正切积分是否等于 compact regulator。

## 3. 消失周期的有理 germ 与有限尺度说明

实际 \(g\) 的首项由真实节点球给 \(-\pi^2t\)。齐次 conifold log block 的 singular-coefficient cancellation 给二阶项与一阶项之比 \(3/4\)。对 \(P\) 的三维 analytic homogeneous solution space，初始三项确定唯一 analytic solution；系数递推全部有理。因此 \(v=-g/\pi^2\in\mathbf Q\{t\}\)；三阶项 \(29/48\) 来自同一个冻结的全尺度递推，而非数值拟合。

由 (V3)，
\[
 \frac{A_\delta}{(2\pi i)^2}
 =-4\int_0^t\frac{v(s)}{\sqrt{1-s}}\,ds
 =-2t^2+O(t^3)\in\mathbf Q\{t\}.
 \tag{V13}
\]
有理 geometric period germ 与 algebraic twist 的乘积及 primitive 是 G-function；此处也可取消去式 \(P[\sqrt{1-t}\,\partial_t A_\delta]=0\)，按 (V3) 的常数 scale 理解。本文只用有理 Taylor 身份，不计算该 operator 的最小阶数或有效 prefix 整模型。

特别地，(V13) 除以的是 Tate weight two 的真实常数；这不是把目标 scalar 的 \(\pi^2\) gauge 当成 CDT 模型中的免费有理操作。其 conifold endpoint 为0，也没有因此新增一个非平凡数值无理性目标。

## 4. Concomitant 与确切整数 Tate 常数

采用已核准的
\[
\begin{aligned}
 \mathcal C_0(h,k)={}&\frac x2(h\theta k-\theta h\,k)
 +x(h\theta^2k-\theta^2h\,k)\\
 &-(1-x)(h\theta^3k-\theta^3h\,k)
 +(1-x)(\theta h\,\theta^2k-\theta^2h\,\theta k),
\end{aligned}
\]
\[
 \theta\mathcal C_0(h,k)=(Ph)k-h(Pk).
 \tag{V14}
\]
由于 \(PW=\sqrt{x}/16\)、\(Pg=0\)，(V12)–(V14) 给
\[
 \theta\{A_\delta-256\mathcal C_0(W,g)\}=0.
 \tag{V15}
\]

对任意 analytic \(H(t)\)，若 \(g=a t+b t^2+\cdots\)，则直接把 \(\theta=-(1-t)\partial_t\) 代入得到
\[
 \mathcal C_0(H,g)\big|_{t=0}=H(0)(2b-3a/2)=0,
 \tag{V16}
\]
因为 \(b=3a/4\)。\(y_0\) 的真实 log branch 首项是 \(t\log t/\pi^2\)，其全部 log 部分与 \(g\log t\) 成比例。冻结 Yukawa 证明的 full-log limit（也可在 V14 直接代入）给
\[
 \boxed{\mathcal C_0(y_0,g)=-1.}
 \tag{V17}
\]
这对两个 homogeneous solutions 是全分支上的常数；leading limit 为 \((1/\pi^2)(-\pi^2)=-1\)。

\(\Psi=W-\pi^4y_0/16\) 在 canonical conifold branch analytic。用 (V16)–(V17)，
\[
 \lim_{t\to0}\mathcal C_0(W,g)=-\pi^4/16.
\]
再用 \(A_\delta(0)=0\)，(V15) 的常数恰是
\[
 256\pi^4/16=16\pi^4=(2\pi i)^4.
\]
得到 (V4)。特别地，
\[
 \boxed{256\mathcal C_0(\Psi,g)=A_\delta.}
 \tag{V18}
\]
这一步把先前仅解析的 \(\Gamma/8\) 修正与真实局部 regulator 的一个指定周期联系起来；不要求全部 raw positive-cut current 已完成紧化比较。

## 5. 实际 compact scalar 的周期评价符号

令 \(E_j=\nabla_\theta^j\omega\)，\(0\le j\le3\)，\(J_{ij}=Q_{\rm raw}(E_i,E_j)\)。已核准的 cyclic cup matrix 满足 period-vector formula
\[
 (h,\theta h,\theta^2h,\theta^3h)J^{-1}
 (k,\theta k,\theta^2k,\theta^3k)^T
 =\mathcal C_0(h,k)/\kappa_{\rm raw}.
\]
对 (V1) 的实际 \(r\)，Hodge zeros 给 \(\theta^j\nu=Q(r,E_j)\) 对 \(j\le3\)。对 \(\operatorname{PD}\delta\)，则 \(\theta^jg=Q(\operatorname{PD}\delta,E_j)\)。若两者的列坐标为 \(c,d\)，对应 period columns 是 \(-Jc,-Jd\)，故
\[
 (-Jc)^TJ^{-1}(-Jd)=-c^TJd
 =Q(\operatorname{PD}\delta,r)=\int_\delta r.
\]
因此
\[
 \boxed{\mathcal C_0(\nu,g)/\kappa_{\rm raw}=\int_\delta r.}
 \tag{V19}
\]
不能在这里沿用两个 cycle 的 intersection 顺序而多加负号。

由 (V5)、(V18) 和 \(\kappa_{\rm raw}=-(2\pi i)^3/16\)，
\[
 \boxed{\mathcal C_0(\nu_{\rm corr},g)/\kappa_{\rm raw}=A_\delta.}
 \tag{V20}
\]
这只是一项周期评价的精确身份。本文不从某 scalar function 拟构造一个已经识别的 motivic class。

## 6. 合法 lift 归一化与三维剩余项

在一个 punctured conifold sector 选实际 holomorphic compact lift。其与 (V7) 的局部 symbol restriction 同 regulator class，故
\[
 \int_\delta r=A_\delta+qQ_4,\qquad q\in\mathbf Q.
 \tag{V21}
\]
该 \(q\) 局部为常数：两边的 derivative 相同，且 Tate discrepancy 取有理值。不得预设某个未标记 compact lift 的 \(q=1\)。

Poincaré-dual 约定是
\(\int_\gamma\alpha=Q(\operatorname{PD}\gamma,\alpha)\)。由于 skew intersection 与 (V2)，
\[
 \int_\delta\Pi\operatorname{PD}\Gamma
 =\delta\cdot\Gamma=8.
\]
所以合法有理 Tate shift
\[
 r_{\rm can}=r-\frac{qQ_4}{8}\Pi\operatorname{PD}\Gamma
 \tag{V22}
\]
给 \(\int_\delta r_{\rm can}=A_\delta\)，保留实际 AJ class 和 (V1) 的 derivative。这里投影是已证明的有理 compact projector，不冒认 integral projector 或 primitive integral lattice。消失球归一化仅固定一个评价，\(r_{\rm can}\) 仍有 annihilate-\(\delta\) 的 flat rational Tate shifts。

设 \(\nu_{\rm can}=Q(r_{\rm can},\omega)\)、\(H=\nu_{\rm can}-\nu_{\rm corr}\)。两者 forcing 相同，故 \(PH=0\)；(V19)–(V20) 给
\[
 \mathcal C_0(H,g)=0.
 \tag{V23}
\]
Local homogeneous solution space 的 conifold monodromy 为一个非零 rank-one transvection；三个解 analytic，一个有 \(g\log t\) 分量，且没有负幂。公式 (V16) 杀掉全部 analytic 解，\(\mathcal C_0(g\log t,g)\ne0\)。因此 (V23) 等价于 \(H\) 没有 log 分量，即 (V6)。

三个剩余参数可取 \(H(0),H'(0),H''(0)/2\)。本稿没有证明这些参数为0、有理或代数，也没有因此识别 \(\nu_{\rm can}(1)\) 与 \(-(2\pi i)^3\pi^2(R_0-M_0)\)。实际 normalized lift 的全纯性成立，指定数值的 marked regulator identity 尚未完成。

## 7. 对后续算术推导的严格限制

消失球归一化不赋予整个实际 scalar 一个代数 Taylor model。一个明确仍合法的平移是
\[
 r_{\rm can}\longmapsto r_{\rm can}+Q_4\operatorname{PD}\delta.
\]
其 \(\delta\) evaluation 不变，因为 \(\delta^2=0\)，且 scalar 的 endpoint 不变，因为 \(g(1)=0\)。但对 \(\widehat\nu=-\nu/[16(2\pi i)^3]\)，此平移改变
\[
 \widehat\nu\longmapsto\widehat\nu+\frac{i\pi^3}{8}v(t).
 \tag{V24}
\]
第一 Taylor coefficient 的差 \(i\pi^3/8\) 超越。因此两个这类真实合法 lifts 不可能同时有代数第一 jet。这个严格例子说明：endpoint、实际 derivative、Yukawa 和消失球归一化，仍不足以唯一指定 CDT 所需的算术 germ。补齐实际 scalar 的其余周期标记、完整整模型及所有 place 费用仍是必要工作。

## 8. 来源与实际阅读、执行范围

Root 本轮实际全文读取以下冻结 MD：compact regulator derivative、Yukawa scalar interface、Kummer period interface、positive-cut period comparison。输入对象及全部规范分别来自这些稿，不重跑其 mathematical producers。

* [紧化 derivative](cdt_odd_R0_regulator_derivative_20261006.md)：\(\nabla_\theta R=16\sqrt{x}\omega\)，actual AJ restriction、BM membrane 与 prescribed-fibre moving。
* [Yukawa 与真实 compact projector](cdt_odd_R0_Yukawa_scalar_interface_20261006.md)：full cyclic pairing、真实 \(\delta,\Gamma\)、\(\Gamma\cdot\delta=-8\)、\(\kappa\) 与 full-log concomitant limit。
* [Kummer/conifold 输入](cdt_odd_R0_kummer_period_interface_20261006.md)：\(PW=\sqrt{x}/16\)、\(\Psi\) 全纯、\(y_0\) 的完整 log branch、actual endpoint。
* [正切及闭周期修正](cdt_odd_R0_positive_cut_period_comparison_20261006.md)：\(\nu_{\rm cut}=-16(2\pi i)^3W\)，\(\Gamma/8\) 的实际 scalar/relative-chain 比较。本稿不扩大其 compact scalar scope。
* KLM, *The Abel–Jacobi map for higher Chow groups*, [本地 published 原件](../literature/kerr_lewis_muller_stach2006_abel_jacobi_published_20261006.pdf)，[DOI](https://doi.org/10.1112/S0010437X05001867)：root 本轮实际抽取并读 PDF8–10、12–13；Prop4.2、ring homomorphism、\(p=n\) topological-cycle evaluation 和 Tate lattice是本稿局部 class/evaluation 输入。首次只读抽取因 GBK 终端编码失败，没有获得正文；之后 UTF-8 只读重抽取成功。这不是数学 producer 执行。

全部新增数学为纸面推导；没有 numerical PSLQ、finite mathematical verifier 或 Lean claim。独立同行审阅另存新文件；本文当前不冒认已经完成其最终全文审阅。
