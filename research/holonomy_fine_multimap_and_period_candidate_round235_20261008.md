# 第235轮：细型、多图与一个实际周期候选

2026-10-08。本文只作有界准入诊断，不新增数值无理性结论，不修改234及更早冻结稿。数学程序0。

## 1. 当前原文与本次范围

复用当前220页 CDT 作者原件 [L2chi.pdf](https://www.math.uchicago.edu/~fcale/papers/L2chi.pdf)，本地3628820 B、SHA256 `9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c`。实际完整读本次保存的选页：目录1–2；67–71；90–95；114–117；123–126；154–159。主陈述包括 Definition6.0.1、Theorem6.0.2、Corollary6.0.14、Theorems7.0.1、7.1.6、7.1.10、7.1.13、7.6.4、8.0.1，以及 Remarks6.0.18、8.0.6、10.1.8。没有全文阅读或重证§6–8的长证明。

只读 OpenAI math 仓库状态：HEAD `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`，`git status --short`无条目，remote为 `https://github.com/openai/math`。相关题目与 Catalan 源的定向定位没有成为本文采用的完整定理或替代源；唯一替代候选取自上述 CDT 原文。

## 2. 两个入口能省什么

**I1：integrated 名称不是收益。** Theorem6.0.2 的成本是
\[
 \tau(b;e)=\frac1{m^2}\sum_i(2i-1)\sigma_i
 +\frac2{m^2}\min_{0\le\xi\le m}
 \left(\xi\sum_i e_i+\max_i e_i\,I_\xi^m(\xi)\right).
\]
所以逐项的序号因子 \(n^{e_i}\) 必须计入全 jet 模型，不能当成只清某个系数的零费用。当前原文 Remark6.0.18 明确给出三行例子：fine 型的 \(10/9\) 比 flat 型的 \(8/9\) 更贵。

对本轮三行模板，若实际系数已支付 \(D_{2n}\)、\(nD_{2n}\) 两个非恒定行，则
\[
 m=3,\quad b=(0,2,2)^t,\quad e=(0,0,1),
 \quad\tau^\flat=16/9,\quad\tau^\sharp=5/9,
 \quad\tau=7/3.                                      \tag{I1}
\]
这里 \(5/9\) 是原文相同 \(m=3\)、单个 \(e=1\) 的值；Definition6.0.1 的表达式只依赖 \(\sum e_i\) 与 \(\max e_i\)，故可直接复用。它恰等于 e=0 两标准列 \((0,2,2)^t,(0,0,1)^t\) 的 \(7/3\)。式(I1)是模板条件判断，不冒称本人已独审本轮新的系数级细型证明。要取得真收益，仍需源级 cancellation、prime packing 或更小的已证格。

**I2：多图已经在§6。** Theorem6.0.2 对全部行、全部图都要求实际 meromorphic pullback。对两图、一个分点 \(\gamma\in(0,m)\)，其分子为
\[
 \int_0^1 2t\,g_{\phi,\gamma}^{*}(t)dt
 +\frac{\gamma^2}{m}
       \log\frac{|\phi_1'(0)|}{|\phi_0'(0)|}.          \tag{I2}
\]
分母为 \(\log|\phi_1'(0)|-\tau(b;e)>0\)。因此只新增一张图、只比较最大导数，或漏掉切换项，都不是完整的新准入证书。两图也不自动共享同一被填叶。

**I3：凸性是独立的实处扣项。** Theorem7.1.6 对同一合法图 \(\phi\) 的次半径 \(r_k\) 给
\[
 m\le\frac{T_b(1,\phi)-\displaystyle\frac1m
       \sum_k\frac{(T_b(r_k,\phi)-T_b(r_{k-1},\phi))^2}
                         {\log r_k-\log r_{k-1}}}
                   {\log|\phi'(0)|-\tau(b;e)},         \tag{I3}
\]
条件包括最后一个斜率 \(\alpha_l\le m\)。更强的 Theorem7.6.4 要求其权重线性系统有唯一解，而且每个权重非负；Remark7.6.7 明确说这些条件不自动成立。式(I3)实际改变实处评价高度，区别于给旧源附加两个 Tate 行。

Theorem8.0.1 允许任意已付分母数组，并可加入这些凸性扣项。但 Remark8.0.6 严格证明：对§6的 nested 标准列，\(\tau^{\flat\flat}=\tau^\flat\)。所以给同一标准列换定理名称不会再省有限处费用。作者在§8开头指出其新增强化在 A/C 的具体应用中为0；这是那两个应用的事实，不是所有新源无收益的定理。

本轮可检验的独立任务是：固定实际三维源和合法图，给有限个次半径的完整 \(T_b\) 界，核斜率条件或权重系统，再比较右端是否严格小于3。先付图与能量，不能从理论存在扣项推断当前已过门槛。

## 3. 唯一备用目标：一个 β(4) 混合连接值

当前 CDT Remark10.1.8 明列偶数族
\[
 J_k(x)=\frac1{\sqrt{1-x}}\int_0^x
              \frac{\log^{k-1}(1-t)}{t\sqrt{1-t}}dt,
 \qquad J_k\in\sum_{n\ge1}\frac{x^n}{D_n^k}\mathbf Z
 \quad(k\text{正偶数}).
\]
这个全素数型是 Remark10.1.8 的原文断言；本次采用所读主陈述，没有独立复证其一般偶数族整性。只选 \(k=4\) 的实际源 \(K_4=-J_4\)，及确定数值目标
\[
 \mathfrak c_4:=\beta(4)-\frac{\pi^2G}{8}
                =-\frac{K_4(2)}{96},\qquad G=\beta(2). \tag{I4}
\]
这里 \(K_4(2)\) 指从0绕1上侧或下侧的两条指定原生 access；下文证明两者在2取同一实数，不扩成所有叶。目标为 \(\mathfrak c_4\notin\mathbf Q\)，不把它冒称单独 \(\beta(4)\) 的无理性。本次已读 CDT 数值定理和 Catalan 无理性均不直接给这个混合值；没有做全球新颖性认证。

**I4 的完整纸面核。** 置 \(v=\sqrt{1-x}\)、\(F_s(v)=(\operatorname{Li}_s(v)-\operatorname{Li}_s(-v))/2\)，其中 \(F_1=\operatorname{atanh}v\)。在从 \(v=1\) 到 \(v=i\) 的上四分之一圆弧，取连续的 \(\log v\)，则对应从 \(x=0\) 到2的下侧 access。由逐项积分再解析延拓，
\[
 A_4(v):=\log^3v F_1(v)-3\log^2v F_2(v)
             +6\log v F_3(v)-6F_4(v),
 \qquad A_4'(v)=\frac{\log^3v}{1-v^2},
\]
\[
 K_4(x)=\frac{16}{v}\bigl(A_4(v)-A_4(1)\bigr).       \tag{I5}
\]
\(v=1\) 是可积端点：带 log 的三个项都趋零，而 \(F_4(1)=15\zeta(4)/16\)。在 \(v=i\)，\(F_1\) 的闭式及 \(s\ge2\) 的绝对收敛奇支撑级数给
\[
 F_1(i)=i\pi/4,\quad F_2(i)=iG,\quad
 F_3(i)=i\pi^3/32,\quad F_4(i)=i\beta(4).
\]
\(\beta(3)=\pi^3/32\) 也由 [DLMF24.8.2](https://dlmf.nist.gov/24.8.E2) 在 \(n=1,x=1/4\) 的 Bernoulli sine series 立即得到；\(\zeta(4)=\pi^4/90\) 可由同页24.8.1取得。故
\[
 A_4(1)=-\pi^4/16,\quad
 A_4(i)=-\pi^4/16+i(3\pi^2G/4-6\beta(4)),
\]
从(I5)得 \(K_4(2)=12\pi^2G-96\beta(4)\)。共轭圆弧 \(v=1\to-i\) 给相同实值。端点 polylog 取从单位盘内部的连续极限，\(s\ge2\) 的级数绝对收敛；\(F_1\) 在 \(i\) 正则。这付清了此特定连接值的路径和常数，没有借形式 saddle 或数值拟合。

完整有理关系源是
\[
 \mathcal H_5=\langle1,L,T_2,T_3,K_4\rangle_{\mathbf Q(x)},
 \qquad L=-\log(1-x),\quad T_j=L^j/j!.
\]
非恒定行在0都取0，连接为
\[
 L'=\frac1{1-x},\quad T_2'=\frac L{1-x},\quad
 T_3'=\frac{T_2}{1-x},\quad
 K_4'=\frac{K_4}{2(1-x)}+\frac{6T_3}{x(1-x)}.         \tag{I6}
\]
有限奇点只有0、1，∞另付。这五行实际独立：前四行的 log 多项式次数给独立性；\(K_4\) 在1有非零 \((1-x)^{-1/2}\) leading，因其积分到1的有限极限为一个严格正积分，不能属于前四个 unipotent 行的有理 span。其 \(D_n^4\) 型与现成初值已经明确；本文没有找到低于该型的 relation-specific 整格。

**I7：同一源的精确 descent 资产。** 在原点附近，\(\sigma(x)=x/(x-1)\) 使 \(v\mapsto1/v\)。直接求导及在 \(v=1\) 定常数给
\[
 A_4(1/v)+A_4(v)=2A_4(1),\quad
 K_4(\sigma(x))=-(1-x)K_4(x).
\]
所以 \(S=xK_4\) 真正 invariant。置
\[
 q=\frac{x^2}{x-1},\quad r=x-\sigma(x)=\frac{x(x-2)}{x-1},
 \quad D=rL,\quad B=L^2,\quad P=rL^3.
\]
\(1,D,B,P,S\) 均 invariant，而且属于 \(\mathbf Q[[q]]\)：取 \(y=x/(2-x)\) 后 \(\sigma y=-y\)，invariant 芽为偶 \(y\) 级数，再用 \(y^2=q/(q-4)\)。由 \(r^2=q(q-4)\)、\(L_q=-1/r\)，得到完整连接
\[
 a=\frac{q-2}{q(q-4)},\quad D_q=aD-1,\quad
 B_q=-\frac{2D}{q(q-4)},\quad P_q=aP-3B,
\]
\[
 S_q=\frac{S}{2q}-\frac{P}{q(q-4)}.                  \tag{I7}
\]
actual rank5 由它们在 \(\mathbf Q(x)\) 上相对(I6)的非零 diagonal 变换得出，因此在较小的 \(\mathbf Q(q)\) 上也独立。有限奇点为0、4；∞另付。这个完整 q 源和 \(S(4)=-192\mathfrak c_4\) 比裸普通点评值有更具体的几何；但本次没有支付它的联合整格或新费用。

若 \(\mathfrak c_4=g\in\mathbf Q\)，则 \(K_4+96g\in\mathbf Q[[x]]\) 在这两条原生 access 的2处取0。但2本来是 ordinary point，这个取0本身不改变 meromorphic 延拓；除以 \(x-2\) 的有理差商也只改变普通极点。descended 源也不能据此免费填4：从(I6)精确得到
\[
 \left.\frac{d(xK_4)}{dx}\right|_{x=2}
       =\log^3(1-x)|_{x=2}=\pm i\pi^3\ne0,
 \quad q-4=\frac{(x-2)^2}{x-1}.
\]
因此 \(S(q)+192g\) 仍有非零 square-root 项。这里只核两条指定 access，不宣称全叶。真正 branch-triggered 投影、更低整模型与严格 holonomy 能量仍未支付。因此(I4)是来自现成完整源的唯一备用对象，不升为默认下一主线，也不把附加旧背景的 logdegree 误记为这项数值问题的进展。它不同于停用q2的 \(\Theta\) 三对数目标；本次没有重启W投影。

## 4. 本轮方向判断

优先完成当前三维源的 source-specific 细型检验与一个有限次半径凸性证书。两入口在定理层面可以并用，但(I1)说明当前最直接的 integrated 替换可能完全中性；(I2)要求多图节省由完整联合式证明；(I3)才给一个可单独审查的实处改进。

若没有正分母及严格 rank 矛盾，停止这一有界准入，不默认继续加 Tate 行。备用(I4)保留现成完整源、精确 involution/(I7)和明确目标，同时记录其源到条件性 branch 的缺口；它目前也不构成已经可用的数值路线。可留给下一次正式全局比较与已存 Catalan 实际源、source-level joint 格对照；本次不启动此候选的成本优化。没有重启停用的W、Gram或参数扫描。
