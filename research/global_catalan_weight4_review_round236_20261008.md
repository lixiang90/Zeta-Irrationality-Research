# 第236轮：Catalan 实际混合证明与权重4的准入界限

2026-10-08。目标仍是新的 ζ/L 数值结论。本文实际读取外仓库 Catalan 原始证明源码，比较第235轮的
\[
 c_4=\beta(4)-\pi^2G/8,\qquad S=xK_4,\qquad S(4)=-192c_4.
\]
没有证明 \(c_4\) 无理或单独 \(\beta(4)\) 无理。数学运行0；不 fetch、不认证远端 freshness，不声称 Lean 或全部有限证书已独立执行。

## 1. 实际读过的原件与证明架构

本地 E:/codex-build/math HEAD 为 fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，本次 git status --short 无条目，remote 为 https://github.com/openai/math。实际 FULL 读 preprints/Catalans-constant-is-irrational-September-24-2026 的 README、main.tex，以及 introduction、foundations、odd-primes、nonvanishing、real-place、energy、certificate、conclusion 八个完整 section 源码。其原件副本及哈希见本轮 dual_reading_scope.md。本文引用源码中的实际证明与证书陈述，没有把题目、README 或之前 locator 当作 proof。

**C1. 原对象先是一个精确的周期投影。** 原件取
\[
 n=48N,\ a=11N,\ b=7N,\ q=g=4N,\ h=2N,\quad
 L=59N,\ C=63N,\ H=65N,\ A=19N.
\]
令 \(f=\sqrt{1-t^2}\)、\(w=t/(1+f)\)，star 为 \(w\mapsto w^{-1}\)，固定 \(t\)，反转 \(f\)。整数 Chebyshev 行为
\[
 R_r=(1-t)^ht^{C-1}w^{r-g},\quad
 P_r=(R_r+R_r^*)/2,\quad D_r=t(R_r^*-R_r)/(2f).
\]
它们满足 \(tP_r/f-D_r=O(t^L)\)。两个实际矩数组是
\[
 M(i,j)=\int_{-1}^1\!\int_0^1
 \frac{|t|}{f(t)}\frac{t^is^j}{1-ts}\,ds\,dt,\quad
 Z(i,j)=\int_0^1\!\int_0^1\frac{t^is^j}{1-ts}\,ds\,dt.
\]
完整递推及起点 \(M(0,0)=4G,\ M(0,1)=3\zeta(2)/2\) 给
\[
 M(i,j)=M^0(i,j)+4G\,c_{(i-j)/2}
                 +\tfrac32\zeta(2)c_{(j-i-1)/2},\quad
 Z(i,j)=Z^0(i,j)+[i=j]\zeta(2),
\]
其中 \(M^0,Z^0\) 有理，\(c_l=4^{-l}\binom{2l}{l}\)，非法下标取0。故每个 raw entry
\[
 F_j(r)=M(P_r,j)-\tfrac32Z(D_r,j),\qquad b\le j<L
\]
的 \(\zeta(2)\) 系数恰是
\[
 \tfrac32[t^j](tP_r/f-D_r)=0.
\]
随后整数列滤波 \(s^{b+k}(1-s)^q\) 留下一个指定的 \(n\times n\) 行列式 \(\Delta_N\)，全部 entry 属于 \(\mathbf Q+\mathbf QG\)。这是全 entry、全部所需列的同对象身份；没有依赖未知周期的算术独立性。其条件收益来自真正消去辅助周期，并不是取消一个 ordinary point 的 pole。

**C2. 非消失是一条独立的算术定理。** 原件在 \(G\in\mathbf Q,\ N=p\) 时，把每个 entry 乘 \(p^2\)。Frobenius、两个 extraction shift 和整数列滤波，将 \(48p\) 阶矩阵化为
\[
 \mathbf a^T\otimes\mathcal B_0+\mathbf b^T\otimes\mathcal B_1,\quad
 \mathbf b=\mathbf a\Pi,\quad \det\mathbf a=2^{-p(p-1)/2}.
\]
\(\Pi\) 的特征值是 \(0,1,-1\)，重数分别 \(1,(p-1)/2,(p-1)/2\)。因此非消失归约到三个固定的有理 \(48\times48\) 矩阵
\(\mathcal B_0,\mathcal B_0+\mathcal B_1,\mathcal B_0-\mathcal B_1\)。
源码给模101的全部 Gaussian pivots、两个 row swap 及精确构造 recipe，从而断言三固定 determinant 非零。排除固定有限集合后得到
\[
 v_p(\Delta_p)=-96p,\qquad \Delta_p\ne0
\]
对全部充分大素数成立。正测度不承担这里的 mixed determinant 非消失；本文 FULL 读证书与 reduction，没有执行其模101算术。

**C3. 完整整模型保留两层，而不是只看 \(p^2\) residue rank。** odd-primes.tex 对 \(p>2\sqrt H\) 证明 digit reductions；对 \(p>H/2\) 再证明 central \(p\)-layer。全 raw pool 的可逆 \(\mathbf Z_p\) 列操作及其逆均积分，保留可能有 \(p^{-2}\) 的 \(R\) 列、至多 \(p^{-1}\) 的 \(S\) 列，最终
\[
 v_p(\Delta_N)\ge-\min(2n,n+R,2R+S).
\]
Cauchy–Binet 将所有 full raw minors 的界传给指定整数 filter。small primes、目标假定分母的固定素数及所有高 \(p\)-power 另计 \(o(n^2)\)；2处用 convergent smoothing 和两项固定 discrepancy，得
\[
 v_2(\Delta_N)\ge-\frac{505}{4608}n^2-O_G(n\log n).
\]
PNT 加权的实际 odd-prime loss area 为 \(8609/2\)，同一归一化
\[
 \mathcal L_N=n^{-2}\log|\Delta_N|-\tfrac12\log2
\]
沿非零尺度满足
\[
 \liminf\mathcal L_N\ge-\frac{8609}{4608}
  -\left(\frac12+\frac{505}{4608}\right)\log2>-2.29084.
\]
它不是 generic cofactor height 免费、leading residue 消失即全格积分、或只付某一单元系数的结论。

**C4. 实处也完全绑定同一个 mixed determinant。** 两次 Andréief 的精确因子为 \((n!)^{-2}\)，Cauchy determinant 留下一个 \(t\) Vandermonde、两个 \(s\) Vandermonde及正分母。近/远 sheet 系数在 \(t<0\) 为 \((1/2,1/2)\)，在 \(t>0\) 为 \((5/4,-1/4)\)，不是正 Gram。

对一个配置范围，原件构造 clustering-uniform 的 holomorphic interpolant 并用有限维 Hardy compression，让 evaluation determinant 在商中代数消去；没有 inverse-Vandermonde conditioning 损失。互补配置用完整 Hadamard sheet bound。matched damping、全部 diagonal correction 和 endpoint correction 在 supremum 之前支付。最终两张 case 的一元 barrier 各由 rational trial sequences、exhaustive root brackets 及 rational logarithms 证书控制。同一 \(\mathcal L_N\) 的上界为
\[
 \limsup\mathcal L_N\le-2.290939875
\]
（另一 case 为 \(-2.296789875\)），与 C3 的非零序列下界冲突。本文读取证书的完整定义、数据和误差证明，没有重算全部 root count、pivot 或 interval table，故不声称独立重新验证原论文每个有限算术值。

## 2. 哪些资产能搬，哪些已在旧稿中失效

第235轮实际 FULL 输入是五行有理源及其 exact descent：
\[
 \langle1,L,L^2,L^3,K_4\rangle_{\mathbf Q(x)},\quad
 L=-\log(1-x),\quad K_4=-J_4,\quad
 K_4(2)=12\pi^2G-96\beta(4).
\]
\[
 q=\frac{x^2}{x-1},\quad r=\frac{x(x-2)}{x-1},\quad
 D=rL,\ B=L^2,\ P=rL^3,\ S=xK_4,
\]
\[
 a=\frac{q-2}{q(q-4)},\quad
 D_q=aD-1,\quad B_q=-\frac{2D}{q(q-4)},\quad
 P_q=aP-3B,\quad S_q=\frac{S}{2q}-\frac{P}{q(q-4)}. \tag{C5}
\]
这是真正 rank5 的完整源，且 \(1,D,B,P,S\in\mathbf Q[[q]]\)。原点 involution、目标连接值及 rational descent 已付；完整 source-level joint lattice、mixed period matrix 和条件性 branch 投影未付。普通点 \(x=2\) 的 zero 与下降后 \(q=4\) 的 branch 不是同一事。

不能将“增加 log 权重”再次当新核心。旧 catalan_higher_even_beta_period_projection_20261007.md 本次 FULL 读，已经证明原内变量 log 权重的 \(M_4(0,0)=C_4\) 是 inverse-binomial 混合值，严格 \(0<C_4<4\beta(4)\)；全数组还含 \(T_4\)、低权重和 zeta 周期。原 Taylor contact 留下真实非零的最高辅助系数 \(T_4/8-3\zeta(4)/2\)，不做全周期投影就不能把 \(G\) 换成 \(\beta(4)\)，更不能换成当前 \(c_4\)。

旧 catalan_higher_even_beta_analytic_transfer_20261007.md 的完整§7–10本次已读：固定可积外权重能准确命中 \(4\beta(4)\)，并保留原同对象的解析上界；但新 moments 的 rational decomposition、全有限处和无穷非零仍未付。增加固定 log 密度不自动保留 \(p^2\) 层，其示例 harmonic tail 已出现 \(p^{-4}\)。这些是已有框架，本文不重新命名为236的新入口。

可以搬的工具是 Chebyshev polynomial integrality、精确 contact 的设计方法、完整 pool 的 integral elimination、Frobenius 的有理曲线身份以及条件满足时的 Hardy/Cauchy estimate。不能搬的是旧目标常数、旧 period coefficient arrays、旧三固定 seeds 或旧二次有限处费。当前 \(c_4\) 是 \(\beta(4)\) 与 \(\pi^2G\) 的混合目标，不能把 \(\pi^2G\) 当有理系数；已知 \(G\) 无理不决定 \(c_4\)。

## 3. 新的完整奇数 jet 命题：固定背景过滤不能填 \(q=4\)

**C6（范围精确的命题）。** 取第235轮从 \(x=0\) 绕1上/下侧到2的任一指定 access。令 \(A,A_0,A_1,A_2,A_3\in\mathbf C(q)\)，\(A\ne0\)。该 transported branch 上的
\[
 F(q)=A(q)S(q)+A_0(q)+A_1(q)D(q)
                  +A_2(q)B(q)+A_3(q)P(q) \tag{C6}
\]
不能在 \(q=4\) meromorphic。特别，任何保留非零 S 通道的固定 \(\mathbf Q(q)\) 线性背景过滤或 rational target shift 都不支付此点的完整 branch filling。这不是 growing mixed-kernel、非线性 determinant 投影或其他新 source 的 no-go。

**完整局部定义。** 在 \(x=2\) 取
\[
 z=\frac{2-x}{x},\quad x=\frac2{1+z},\quad
 q=\frac4{1-z^2},\quad r=-\frac{4z}{1-z^2}.
\]
在 \(z=0\) 的小圆盘，所选 L branch 为
\[
 L(z)=\ell+J(z),\quad \ell=\pm i\pi,\quad
 J(z)=\log(1+z)-\log(1-z)=2\operatorname{atanh}z.
\]
这里 \(\log(1\pm z)\) 在0取0，J 是 odd holomorphic germ。对任何此盘内 meromorphic germ \(f\)，定义
\[
 \operatorname{Odd}f(z)=\frac{f(z)-f(-z)}2.
\]
这是同一局部 analytic branch 的两点评值，不将第二项偷偷换成原点附近的 native star 分支。若一个 q germ 在4 meromorphic，其 z pullback Laurent series必为 even；反之 even meromorphic germ由 \(z^2=(q-4)/q\) 下降。所以完整奇数 jet 必须恒等为0，消常数或某一个导数不足够。

**C7（S 的全部 odd jet 与目标常数无关）。** 从(C5)，或直接从 x 连接，得
\[
 S_z=\frac{z}{1-z^2}S+\frac{2(\ell+J)^3}{1-z^2}.
\]
积分因子 \(\sqrt{1-z^2}\) 在0取1。两个局部解中目标连接常数 \(S(0)\) 只乘 even homogeneous solution。因此
\[
 \operatorname{Odd}S(z)=
 \frac2{\sqrt{1-z^2}}\int_0^z
 \frac{\ell^3+3\ell J(t)^2}{\sqrt{1-t^2}}\,dt. \tag{C7}
\]
该式来自完整 even forcing 的积分，不是有限 Taylor 拟合；端点0正则，被积函数 holomorphic。尤其
\(\operatorname{Odd}S=2\ell^3z+O(z^3)\ne0\)。
假设 \(c_4=g\in\mathbf Q\) 只将 \(S(0)=-192c_4\) 改成被抵消的 even 常数，式(C7)完全保留。

**C8（任意有理背景也不能取消全部 odd jet）。** 背景的 odd parts 精确为
\[
 \operatorname{Odd}D=r\ell,\quad
 \operatorname{Odd}B=2\ell J,\quad
 \operatorname{Odd}P=r(\ell^3+3\ell J^2),\quad
 \operatorname{Odd}1=0. \tag{C8}
\]
有理 q 系数在 z 中 even，所以若(C6)可 meromorphic，就有
\[
 A(q(z))\operatorname{Odd}S+
 A_1(q(z))r\ell+2A_2(q(z))\ell J+
 A_3(q(z))r(\ell^3+3\ell J^2)=0. \tag{C9}
\]
继续所有这些 germs 沿上半平面中的一条路径，从0附近绕过1，避开 \(\pm1\) 及有限个 rational-coefficient poles，到正实方向的 ∞ sector。可取此 sector 的 \(\log z\)，上述连续分支满足
\[
 J(z)=i\pi+2/z+O(z^{-3}),\qquad
 \sqrt{1-z^2}=-iz(1+O(z^{-2})).
\]
这些式子由两个 log 和 square-root 的指定继续直接给出；无 contour/saddle 假设。于是
\[
 \ell^3+3\ell J(z)^2=-4\pi^2\ell+O(1/z).
\]
对(C7)积分，或其微分式，得
\[
 (\operatorname{Odd}S)\sqrt{1-z^2}
       =-8i\pi^2\ell\log z+\mathrm{const}+O(1/z),
\]
\[
 \operatorname{Odd}S=
        8\pi^2\ell\,\frac{\log z}{z}+O(1/z). \tag{C10}
\]
对数项系数非零。另一方面，J、r 和所有有理 \(q(z)\) 系数在这条 ∞ 叶都有 convergent Laurent expansion；J在∞趋 iπ而没有 log z。故(C8)及其有理倍在∞均 meromorphic，没有 log z。非零 \(A(q(z))\) 只有有限阶 zero/pole，不能消除(C10)的 logarithmic monodromy。若(C9)在0附近成立，解析继续会在这个 sector 成立，与非零 log 系数矛盾。这证明 C6。下半平面的指定 access 同样适用；证明只需 \(\ell=\pm i\pi\)，不借未核的全图叶量词。

这也解释为什么仅去掉 \(S(4)\) 后除以 \(q-4\)，或额外加入几行旧 log 背景，不能完成当前自然下降源的关系敏感填点。命题没有声称全部合法 ramified 图都不存在：图可用偶 ramification承接一个对所有 g 都存在的 branch；这种动作还要独立付 degree、finite lattice及energy。

## 4. 首个未付引理与停止条件

**C9. 源码移植的第一关是实际周期矩阵，不是最终能量扫描。** 若要走 OpenAI mixed determinant 路线，下一项必须给一个明确参数族的全 entry 身份
\[
 \mathcal M_N=Q_N+c_4T_N+\sum_\nu\omega_\nu B_{\nu,N},
 \qquad Q_N,T_N,B_{\nu,N}\text{ 为有理矩阵},
\]
并以实际整数行/列或相对链投影消去全部 \(B_{\nu,N}\)，同时保留足够大的目标通道和同一指定 determinant。这里 \(\omega_\nu\) 可当自由形式符号作充分消元，不需假设它们独立；但若它们含 \(\pi^2G\)，不能免费并入 rational coefficient。必须证明目标 map 在该 nuisance kernel 上没有同时被杀，并给 projection 的完整原格、指数及实际两 sheet 解析表示。当前 rank5 连接及 endpoint identity 没有提供这个矩阵。

这一个 first lemma 若没有兑现，就没有可供 N=p Frobenius reduction 的新 rational seed，也没有可比较的全 prime loss curve。即使已得到 rational determinant，仍需沿无限尺度非零、全层局部格与同对象实处预算，才可复用 C1–C4 的比较方式。旧 Catalan 常数的 margin很小，不能把增加权重称低阶误差而沿用全部旧费。

**C10. 本轮判断。** 保留 \(c_4\) 的精确连接值、rank5 rational descent 与 C6–C10 的完整 jet 诊断，作为正式全局比较的结构资产；停止将“目标常数取零＋旧背景 rational filtering”当作默认数值主线。仅在一个有界窗口产出 C9 的同对象 period projection、足够目标 rank及完整整模型，或一条真正不同的关系敏感完整 source，才进入非消失/energy阶段。没有这项新输入，继续降级为结构工具，不能默认再做六轮费用/参数优化。这里没有全局禁止高偶数 beta 的命题，也没有把辅助 lemma 改称数值目标成功。

本次实际读域和运行账见 [dual_reading_scope.md](../literature/global_review_sources_round236_20261008/dual_reading_scope.md)。外仓库与全部235及更早冻结稿未修改。
