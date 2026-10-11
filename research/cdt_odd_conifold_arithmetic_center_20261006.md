# 已填平 conifold 的算术展开点：一个条件明确的完整接口

状态：NEW 纸面证明；证明结构性接口，不声明新的数值无理性或线性无关性。旧冻结材料只读。本文独立于 toric higher-Chow completion 是否成立。

## C1. 实际周期与变量

沿 [真实相对周期稿](cdt_odd_R0_relative_cycle_mirror_20261006.md) 的 canonical 实支取
\[
 P=\theta^4-x(\theta+\tfrac12)^4,\quad \theta=x\partial_x,
 \qquad \Psi=W-\frac{\pi^4}{16}y_0.
\]
已证明 \(P\Psi=\sqrt{x}/16\)，且 \(\Psi\) 在 \(x=1\) 全纯。该实分支由真实整相对链 \(8C-T\Gamma\) 标记；本文不把 scalar 全纯性提升为所有 transported branches 的单值性。

令 \(t=1-x\)、\(D=\partial_t\)，并定义三个实际初始数据
\[
 \alpha_0=\Psi(1),\qquad
 \alpha_1=-\partial_x\Psi(1),\qquad
 \alpha_2=\tfrac12\partial_x^2\Psi(1).
\]
它们就是 \(\Psi(1-t)=\sum c_nt^n\) 的 \(c_0,c_1,c_2\)。这里只对已校正的全纯函数取导数；不分别对有 log 的 \(W,y_0\) 取未正则化的端点导数。

\[
 \alpha_0=\frac{\pi^2}{16}(R_0-M_0).
\]
另外两个初始数的算术性质尚未证明。单独假设 \(\alpha_0\) 有理或代数，不足以推出以下整模型。

## C2. conifold 处精确微分算子

在 \(t\) 坐标中，直接展开 Euler powers 得
\[
\begin{aligned}
 P={}&t(1-t)^4D^4+(1-t)^3(2-8t)D^3\\
 &+\frac{(1-t)^2(29t-15)}2D^2
 +(1-t)(4-5t)D-\frac{1-t}{16}.
\end{aligned}
\tag{C2.1}
\]
这里 \(\theta=-(1-t)D\)，各项次序是左侧函数系数、右侧导数。令
\[
 L=(\theta-\tfrac12)P.
\]
则 \(L\Psi=0\)。最小幂项的 indicial polynomials 分别为
\[
 I_P(\rho)=\rho(\rho-1)^2(\rho-2),\qquad
 I_L(\rho)=-\rho(\rho-1)^2(\rho-2)(\rho-3).
\tag{C2.2}
\]
因此 \(L\) 的五个 local exponents 为 \(0,1,1,2,3\)，全为整数。重复 exponent 1 的第四个 homogeneous 方向含 log；不能把 conifold 当作微分系统的普通点。

## C3. 三个初始数据足以控制全部 Taylor 系数

写 \(P f=\beta\sqrt{1-t}/16\)、\(f=\sum c_nt^n\)，约定 \(c_{-1}=0\)，设
\[
 h_n=(-1)^n\binom{1/2}{n}.
\]
对每个 \(n\ge0\)，精确系数递推为
\[
 A_nc_{n+3}-B_nc_{n+2}+C_nc_{n+1}-E_nc_n
 +(n-\tfrac12)^4c_{n-1}=\frac{\beta h_n}{16},
\tag{C3.1}
\]
其中
\[
\begin{aligned}
 A_n&=(n+3)(n+2)^2(n+1),\\
 B_n&=\frac{(n+2)(n+1)(8n^2+20n+15)}2,\\
 C_n&=\frac{(n+1)(12n^3+24n^2+23n+8)}2,\\
 E_n&=\frac{64n^4+32n^3+40n^2+8n+1}{16}.
\end{aligned}
\]
由于 \(A_n\ne0\)，给定 \(c_0,c_1,c_2,\beta\) 唯一确定形式解。regular singular convergence，或下面的 G-function local-basis theorem，保证该形式解实际收敛。特别地
\[
 c_3=\frac{\beta+c_0}{192}-\frac{c_1}{3}+\frac{5c_2}{4}.
\tag{C3.2}
\]
取 \(\beta=1\)、\(c_i=\alpha_i\) 就是实际 \(\Psi\) 的完整 germ。取 \(\beta=0\)、前三初值依次为标准单位向量得到三个有理 Taylor homogeneous germs \(g_0,g_1,g_2\)；取 \(\beta=1\)、前三初值全零得到一个有理 Taylor particular germ \(h\)。于是
\[
 \Psi(1-t)=h(t)+\alpha_0g_0(t)+\alpha_1g_1(t)+\alpha_2g_2(t).
\tag{C3.3}
\]
这不是原点上的代数系数校正族：\(g_i\) 的基点是 conifold，原点 connection constants 未知，不能将它们当成原点 arithmetic-initial homogeneous backgrounds。

## C4. 几何分母定理给出的整模型

本文实际读取 Fischler–Rivoal 的出版原件 [Denominators of the coefficients of G-functions](https://www.jstage.jst.go.jp/article/kyushujm/71/2/71_287/_article/-char/en)，尤其 PDF2–5、9（印刷288–291、295）；本地 [原始 PDF](../literature/fischler_rivoal2017_G_function_denominators_published_20261006.pdf)。Thm1–2 给：阶数 \(\mu\) 的 geometric G-operator 所消去的 G-function，其 \(n\) 次系数可用
\[
 D_{bn+b_0}^{\mu-1}C^{n+1}
\]
整化，\(b\) 可取该展开点 local exponents 分母的最小公倍数。\(D_m=\operatorname{lcm}(1,\ldots,m)\)，\(D_0=1\)。这不是假定 Bombieri 猜想的版本；geometric 情形无条件。

其 geometric 定义允许 Picard–Fuchs factors 的乘积。这里 \(P\) 是已识别的 half-four Calabi–Yau Picard–Fuchs 因子；\(\theta-1/2\) 是代数覆盖 \(u^2=x\) 的 rank-one finite-character Picard–Fuchs 因子。故它们的乘积 \(L\) 符合 geometric 条件，且代数平移 \(x=1-t\) 保留此条件。无需先证明 \(8C-T\Gamma\) 已是 higher-Chow regulator。

原文 PDF4 的 André–Chudnovsky–Katz local-basis theorem 给该 algebraic singular point 的 Nilsson–G-function basis。对于本文的四个 holomorphic germs，(C3.1) 使系数为有理数，并与 full local basis 的 holomorphic 子空间接合，因此它们本身是 G-functions。更具体地，local basis 的 Taylor/log 系数在 \(\overline{\mathbf Q}\)，以 \((c_0,c_1,c_2,\beta)\) 规范化的可逆初值矩阵也在 \(\overline{\mathbf Q}\)；无需用可能超越的 connection constants 作归一化。

四个 germs 都由原 \(L\) 消去，因此直接用 \(\mu=5\) 而不是任意去 log 部分的 \(\mu^2\) 安全上界。C2.2 的整数 exponents 给 \(b=1\)。对这四个有限的有理 germs 取共同 \(b_0\) 与 \(C\)，得到
\[
 D_{n+b_0}^{4}C^{n+1}[t^n]g_i\in\mathbf Z,
 \qquad D_{n+b_0}^{4}C^{n+1}[t^n]h\in\mathbf Z.
\tag{C4.1}
\]

**条件性实际周期结论。** 若 \(\alpha_0,\alpha_1,\alpha_2\in K\)（某 number field），存在固定正整数 \(d_0\)，使
\[
 d_0D_{n+b_0}^{4}C^{n+1}c_n\in\mathcal O_K
 \quad\hbox{对全部 }n\ge0.
\tag{C4.2}
\]
若三个初值均有理，右端即为 \(\mathbf Z\)。反方向也直接成立：Taylor 全系数为代数数必然使前三个初值为代数数。故这个 particular germ 的 Taylor algebraicity 缺口精确集中在这三个实际初始数据；这不证明它们代数。

## C5. prefix 与完整导数模型；费用不能省略

设 \(\Delta_N=d_0D_{N+b_0+3}^{4}C^{N+4}\)。对 C4 的实际周期和 \(j=0,1,2,3\)，
\[
 \Delta_N[t^n]D^j\Psi(1-t)\in\mathcal O_K\quad(0\le n\le N),
\]
因为 \([t^n]D^jf=(n+j)!c_{n+j}/n!\)，乘数是整数。增加固定 \(C\) 的倍数可同时整化 \(\sqrt{1-t}\)（由 Eisenstein 定理，或其 binomial coefficients 的 2-adic 界）。因此
\[
 1,\quad\sqrt{1-t},\quad\Psi(1-t),\quad D\Psi(1-t),\quad D^2\Psi(1-t),\quad D^3\Psi(1-t)
\tag{C5.1}
\]
有完整 arithmetic prefix model。C2.1 使这个六行系统对 \(D\) 在 \(K(t)\) 上闭合；最高导数通过 \(P\Psi=\sqrt{1-t}/16\) 解出，不能在 \(t=0\) 生硬除以 \(t\) 丢初始条件。

\[
 \log\Delta_N\le (4+\log C)N+o(N).
\tag{C5.2}
\]
\(b_0,d_0\) 固定，不改变主率；\(C^{N+4}\) 是指数项，确实改变主率。FR PDF9 正是用 \(C^{n+1}\) 支付有限坏素数费用，不能因其只有有限 support 就删去。当前尚未有效计算最小 \(C\)，也未证明这些六行的 finite-place Smith / CDT transport optimum。

本文只需模型上界，未把六行数目直接充当已经独立审查的 CDT rank。已有 \(W\) 的 non-split rank-five 结论提示其最小秩，但新中心的预算仍需独立核证；无需在本接口中作附加秩承诺。

## C6. 可推进的下一步与严格局限

1. 用 (C3.1) 构造这四个 canonical rational germs 的全尺度 good-prime block recurrences，实际计算 \(C\)、整格和 Smith，而非重新扫描未知周期。
2. 将三个初值组成的 period-jet vector 与相对 MHS 的 Betti/de Rham 格比较，寻找在假设某一具体数值关系时使全部初始数据代数的机制，或改以该三维向量的线性无关性为目标。
3. 计算实际标记分支的 holonomy leaf / covering stabilizer，再核算新中心的 archimedean capacity。canonical branch 在一个 puncture 全纯，不自动填平所有 transported punctures；没有任何免费全局 capacity 结论。

本文完成的是「真正填平的 scalar period → 在 algebraic initial jet 条件下的完整 geometric G-function 整模型」接口。它消除了需要手写 closed-form coefficients 或先有 regulator lift 的技术前提，仍没有给新的奇 ζ、Catalan 或 L-value 数值定理。

## C7. 核验边界

NEW [符号核验](cdt_odd_conifold_arithmetic_center_20261006_verify.py) 只验证 C2.1 的 operator identity、C2.2 的 indicial polynomials、C3.1 对所有符号 n 的五个 coefficients，以及 C3.2 的首项；它不证明 G-function 定理，不证明初始周期代数或数值结论，也不执行任何旧数学 producer。实际运行结果单列在 [核验记录](cdt_odd_conifold_arithmetic_center_20261006_verify.json)。FR 保存、读取范围见 [新来源清单](../literature/manifest_cdt_odd_conifold_arithmetic_20261006.json)。
