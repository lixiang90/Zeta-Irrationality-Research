# Gamma 商的正实 Euler 相对链：完整跳跃、Taylor 整模型与正则化障碍

2026-10-07，NEW，作者 `/root/masked_racah_finalize`。本轮 authority 为主报告 §§181–185 和 `cdt_odd_delivery_balanced_gamma_direction_20261007.json`（SHA `b3a9c11266257168b103c14a13541b503dc53df1d7ad56c327c8ea83a5c43d50`）；588 个既有冻结记录只读。本文是一个新 Euler/resolvent 候选的完整纸面检验，不声称新数值无理性。数学 producer 新建、执行、导入、重跑及辅助素数扩表均为 0。

实际 FULL 读冻结 Gamma 主稿 G1–G19/七节与其根端正式独审 R1–R7；主报告只实际读 §§181–185 和 §180 末段，不冒认整份主报告全文。新原件读域、下载与版本精度见 §8。本文从积分直接证明全部数学式，不从 normal-function 示例免费转移连接常数、初值或整数基。

## 1. 当前目标及一个新的正实模型

冻结系统的九个参数及整数坐标为

\[
 a=(\tfrac12,\tfrac12,\tfrac12,\tfrac12,\tfrac12,
       \tfrac15,\tfrac25,\tfrac35,\tfrac45),\qquad
 \Lambda=2^{10}5^5=3200000,\quad c=\Lambda^{-1},
 \quad \kappa(s)=\frac{\Gamma(1+s)^{15}}
 {\Gamma(1+2s)^5\Gamma(1+5s)}.                     \tag{E1}
\]

冻结 Gamma 稿已证明原齐次 Frobenius 解的 complete conifold jump 是 \(\kappa_j\psi\)，而其 Taylor analytic parts 的 jump 含完整的 \(\log t\) 多项式。本候选另从参数 Euler 积分尝试产生相对链扩张。

令 \(\Omega=[0,1]^5\times\Delta_4\)，其中 \(y_5=1-y_1-\cdots-y_4\)，\(\Delta_4\) 是五个非负 \(y_k\) 和为 1 的单纯形；使用普通坐标体积 \(d\mu=dx_1\cdots dx_5dy_1\cdots dy_4\)。定义

\[
 Q=\prod_{i=1}^5x_i(1-x_i)\prod_{k=1}^5y_k,
 \qquad p(s)=(1+2s)^5\prod_{k=1}^4(5s+k).          \tag{E2}
\]

这里 \(p\) 是本文的次数九多项式，不是旧稿端点有理式中的同名符号。\(Q\) 是有理系数多项式，内部严格正，边界为零；AM–GM 与 \(x(1-x)\le1/4\) 给唯一内部最大值

\[
 \max_\Omega Q=4^{-5}5^{-5}=c,
 \quad x_i=\tfrac12,\quad y_k=\tfrac15.           \tag{E3}
\]

对 \(\Re s>-1\)，分别使用五个 beta 积分及一个 Dirichlet 积分，有

\[
 \int_\Omega Q^s\,d\mu
 =\frac{\Gamma(1+s)^{10}}{\Gamma(2+2s)^5}
   \frac{\Gamma(1+s)^5}{\Gamma(5+5s)}
 =\frac{\kappa(s)}{p(s)}.                        \tag{E4}
\]

所有积分绝对收敛；在紧子带上也可逐次对 \(s\) 微分。\(p(0)=24\)，\(\operatorname{vol}\Omega=1/24\)，所以 \(\kappa(0)=1\) 被真实正实链校准，没有任意 period 比例。

## 2. Resolvent 相对周期、真实递推及初值

用新变量 \(T\)，不把它冒认作原变量 \(t\)。对 \(|T|<\Lambda\) 定义

\[
 I(s,T)=\int_\Omega\frac{Q^s}{1-TQ}\,d\mu,
 \quad E(s,T)=p(s+D)I(s,T),\quad D=T\frac d{dT}.
                                                               \tag{E5}
\]

几何级数在紧子圆一致收敛，(E4) 给

\[
 E(s,T)=\sum_{n\ge0}\kappa(n+s)T^n,
 \quad B(s,T)=\frac{E(s,T)}{\kappa(s)}
             =\sum_{n\ge0}b_n(s)T^n,
 \quad b_n(s)=\frac{\kappa(n+s)}{\kappa(s)}.       \tag{E6}
\]

固定 \(n\) 后 gamma 的整数位移显示 \(b_n(s)\in\mathbb Q(s)\)，在 \(s=0\) 正则。multiplication 或逐项位移给

\[
 b_n(s)=\Lambda^{-n}
       \frac{(1+s)_n^9}{\prod_{i=1}^9(a_i+s)_n},
 \qquad b_n(0)=h_n^{-1},\quad
 h_n=\frac{((2n)!)^5(5n)!}{(n!)^{15}}.            \tag{E7}
\]

因此这个 Euler resolvent 的系数是原 factorial-ratio 系数的**倒数**；它不是原齐次 Taylor 周期。记 \(B_j=[s^j]B\)、\(E_j=[s^j]E\)，使用系数而非导数约定。初值为

\[
 B(s,0)=1,\quad B_0(0)=1,\quad B_j(0)=0\ (j>0),
 \qquad E_j(0)=\kappa_j.                         \tag{E8}
\]

对 \(n\ge1\)，准确 recurrence 及非齐次算子是

\[
 b_n(s)\prod_i(n+s+a_i-1)
   =c(n+s)^9b_{n-1}(s),
\]
\[
 M_s=\prod_i(D+s+a_i-1)-cT(D+s+1)^9,
 \qquad M_sB(s,T)=\prod_i(s+a_i-1).              \tag{E9}
\]

这是次数九的非齐次 Picard–Fuchs 型候选，源项与 \(n=0\) 初值一并保留；源项不等于零。系数提取给有限 triangular \(\mathbb Q(T)\) 微分系统，故每个有限族 \(B_0,\ldots,B_d\) 都 holonomic。齐次 \(M_0\) 在起点的 exponents 是 \(1-a_i\)，不是原系统的九重 0。有限临界点是 \(T=\Lambda\)，不是原系统的 \(t=c\)。若选 \(T=\Lambda^2v\) 使它落在 \(v=c\)，须重新支付该坐标的系数、分母数组和 conformal derivative；本文不免费进行这一变换。

## 3. 有理 differential forms 的相对链与校准界限

每个 \(I_j=[s^j]I\) 是

\[
 I_j(T)=\int_\Omega\frac{(\log Q)^j}{j!(1-TQ)}\,d\mu.
                                                               \tag{E10}
\]

由于 \(0<Q\le c<1\)，可以实际增加 \(j\) 个 Kummer 积分变量：

\[
 \frac{(\log Q)^j}{j!}
   =(-1)^j\int_{Q<u_1<\cdots<u_j<1}
                   \frac{du_1\cdots du_j}{u_1\cdots u_j}.
                                                               \tag{E11}
\]

积分域由有理多项式不等式给出，边界包含 \(u_1=Q\)、\(u_j=1\) 与相邻 \(u\) 相等的面；被积 differential form 是有理式。\(Q=0\) 附近的对数幂仍可积，故这是收敛的、给定实际边界的 rational-form relative period 表示，不是只有形式 \(\log Q\) 的写法。\(E_j\) 是 \(I_\ell\) 经有限个 \(D\) 和有理整数系数的组合，微分只增加 \((1-TQ)\) 的有理极点阶数，故同样有实际相对周期表示。

这一构造没有自动给 \(B_j\) 的 rational Betti-chain 校准。事实上

\[
 B_j=\sum_{\ell=0}^j\lambda_{j-\ell}E_\ell,
 \qquad \lambda(s)=\kappa(s)^{-1}
                  =\sum_{j\ge0}\lambda_js^j,    \tag{E12}
\]

其中 \(\lambda_j\) 是比较常数，一般不是有理数。\(B_j\) 的 Taylor 系数全在 \(\mathbb Q\) 由 (E7) 确实证明；但不能据此把 (E12) 当作有理系数相对链的变基。反过来，实际链 \(E_j\) 在起点已有未知 \(\kappa_j\)，也不满足未经变换的 \(\mathbb Q[[T]]\) 条件。本文准确保留这两种校准的区别。

## 4. 完整分支跳跃由 residue 给出

将普通体积沿 \(Q\) push forward，在 \(0<q<c\) 写作 \(w(q)dq\)。靠近唯一内部最大值，此 density 存在且有解析延拓的半整数展开。局部的符号由 continuation 路径固定；下面把 \(\Delta\) 定义为从临界点 \(\Lambda\) 的两侧得到的有向解析分支之差，并把符号纳入 \(\psi_I\)。

\[
 I(s,T)=\int_0^c\frac{q^sw(q)}{1-Tq}\,dq,
 \qquad \Delta I(s,T)=T^{-s}\psi_I(T),
 \quad \psi_I(T)=\pm2\pi i\,T^{-1}w(T^{-1}).     \tag{E13}
\]

这是**完整局部 germ**等式。证明是越过 pole \(q=T^{-1}\) 时使用 residue/Plemelj，pole 上 \(q^s=T^{-s}\)；远离临界小邻域的积分单值，对差没有贡献。先在实轴 \(T>\Lambda\) 的小区间上得到差，再以解析延拓得到完整邻域 germ，不仅比较 leading coefficient。此局部 \(\log T\) 取同一正实分支，绕 \(\Lambda\) 的小 loop 不使它跳跃。

微分与 continuation 可交换，而

\[
 p(s+D)(T^{-s}h)=T^{-s}p(D)h.
\]

所以 (E5) 的全部分支跳跃为

\[
 \Delta E(s,T)=T^{-s}\Psi(T),\qquad
 \Psi(T)=p(D)\psi_I(T).                          \tag{E14}
\]

必须检验 \(\Psi\ne0\)。在 (E3) 的临界点，\(\log Q\) 的 Hessian 的 \(x\)-block 是 \(-8I_5\)，\(y\)-block 是 \(-25(I_4+\mathbf1\mathbf1^t)\)，交叉 block 为零，故是真正的非退化九维最大值。解析 Morse 坐标和球面面积给

\[
 w(q)=C(c-q)^{7/2}(1+O(c-q)),\qquad C>0.         \tag{E15}
\]

普通解析 density 展开中的首项不会抵消。\(p\) 次数九且首项系数为 \(2^5 5^4\)；\(D^9\) 对 \((T-\Lambda)^{7/2}\) 的首项系数含 \(\Lambda^9(7/2)(5/2)\cdots(-9/2)\)，各因子都非零。因此

\[
 \Psi(T)=C'(T-\Lambda)^{-11/2}(1+O(T-\Lambda)),
 \qquad C'\ne0.                                \tag{E16}
\]

这也独立验证 reciprocal-factorial 候选确有 genuine branch，不能把 jump 除去后当作恒零比较。

## 5. Q Taylor 和完整常数行不能在该候选中同时取得

从 (E12)–(E14) 得准确完整公式

\[
 \Delta B_j(T)=\Psi(T)H_j(\log T),\qquad
 H_j(L)=\sum_{k=0}^j\lambda_{j-k}\frac{(-L)^k}{k!}.
                                                               \tag{E17}
\]

\(\lambda_0=1\)，所以 \(H_j\) 的最高项总是 \((-L)^j/j!\)。任意 \(u\in\mathbb C\) 对 \(j\ge1\) 都不能使 \(\Delta(B_j-uB_0)\) 恒为零；即使 \(\lambda_j=u\) 或 \(\kappa_j=u\)，剩余正次数项仍非零。

如果保持完整参数 factor，令

\[
 F(s,T)=T^sB(s,T),\quad F_j=[s^j]F,
 \quad \Delta F_j=\lambda_j\Psi,
 \quad \Delta(F_j-uF_0)=(\lambda_j-u)\Psi.        \tag{E18}
\]

这是真实完整填洞等式，但常数行是**倒数 Gamma 商**，不等于原 \(\kappa_j\)。例如冻结 \(\kappa_2=-15\zeta(2)\)、\(\kappa_3=50\zeta(3)\)、\(\kappa_5=654\zeta(5)-750\zeta(2)\zeta(3)\) 给

\[
 \lambda_5=-654\zeta(5)-750\zeta(2)\zeta(3).     \tag{E19}
\]

更重要的是 \(F_j\) 在起点的最高对数项为 \((\log T)^j/j!\)，来自 \(B_0(0)=1\)；减去 \(uF_0\) 无法消去。算子亦须正确支付：\(M_0F(s,T)=T^s\prod_i(s+a_i-1)\)，不是把 \(F_j\) 宣称为原 homogeneous Frobenius 解。

如一定要原 \(\kappa\) 行，\(\widetilde F(s,T)=\kappa(s)T^sE(s,T)\) 满足 \(\Delta\widetilde F=\kappa(s)\Psi\)。但其起点仍有最高对数，而且 Taylor analytic part 是 \(\kappa(s)E(s,T)\)，起点为 \(\kappa(s)^2\)；有理校准更没有闭合。这个乘法不是获得原目标的免费 rational differential-form 变换。

通常 tangential basepoint 只固定 \(\log T\) 的支路和正则化初值，**不会把整个 \(F_j\) 变成普通 Taylor germ**。若另采用更强的 coefficientwise constant-in-\(\log T\) 投影，由

\[
 F_j=\sum_{k=0}^j\frac{(\log T)^k}{k!}B_{j-k}   \tag{E20}
\]

可见投影结果正是 \(B_j\)，其完整 jump 又回到 (E17)。这一投影与完整 conifold variation 不交换。固定其他非零 tangent 仅平移 \(\log T\)，有限 cover \(T=v^h\) 使最高项乘 \(h^j\)；两者都不消去最高项。

还有一个对本 package 的精确函数秩结论。若 \(r_*+\sum_{j=0}^dr_j(T)B_j=0\)，\(r_*,r_j\in\mathbb C(T)\)，取完整 variation 并除去非零 \(\Psi\)，得到 \(\sum_jr_jH_j(\log T)=0\)。\(\log T\) 对 \(\mathbb C(T)\) 超越：绕 0 后它在普通点取得无穷多个 \(\log T+2\pi iN\)，非零有限次数多项式不可能全消失。三角最高项逐次给所有 \(r_j=0\)、\(r_*=0\)。同一论证表明，在 \(\mathbb C(T)\)-span\(\{1,B_0,\ldots,B_d\}\) 内，完整 jump 为零的 rows 只有 rational-function rows。因此不能靠此 package 的 rational change of basis 同时得到新 Q Taylor row 和 relation-dependent 填洞。该论证**不涉及**其他相对扩张、对偶周期实现、不同代数 cycle 或其它 normal function。

## 6. 全 finite-place 的真实安全 cap 与 CDT 费用

\(h_n\) 是五个 central binomial 与一个五项 multinomial 的整数乘积。对任意素数 \(p\)，Legendre 公式给

\[
 v_p(h_n)=\sum_{\ell\ge1}
 \left(5\left\lfloor\frac{2n}{p^\ell}\right\rfloor
 +\left\lfloor\frac{5n}{p^\ell}\right\rfloor
 -15\left\lfloor\frac n{p^\ell}\right\rfloor\right).
                                                               \tag{E21}
\]

每一层令 \(f=\{n/p^\ell\}\)，括号恰为 \(5\lfloor2f\rfloor+\lfloor5f\rfloor\in[0,9]\)，且 \(p^\ell>5n\) 时为零。因此 \(h_n\mid D_{5n}^9\)，其中 \(D_N=\operatorname{lcm}(1,\ldots,N)\)。没有只核大素数或漏掉 2、5。

再将 (E7) 除以 \(b_n(0)\)：分子由 \((1+s/l)^9\) 构成，分母由 \(1+2s/(2l+1)\) 与 \(1+5s/(5l+k)\) 的整数负幂构成，\(0\le l<n\)、\(1\le k\le4\)，分子 \(1\le l\le n\)。每个 \(s\)-degree-\(j\) 项恰消耗 \(j\) 个 reciprocal，所有分母整数不超过 \(5n\)，负二项式展开系数为整数。于是对所有 \(n\ge1,j\ge0\)，

\[
 D_{5n}^{9+j}[s^j]b_n(s)\in\mathbb Z.            \tag{E22}
\]

这是 safe upper cap，不是证明 minimal denominator 或实际 content。\(n=0\) 的初值已由 (E8) 单独处理；使用 \([s^j]\) 无额外 \(j!\) 费用。

对已证函数秩 \(m=d+2\) 的族 \(1,B_0,\ldots,B_d\)，选九个 width-5 columns 同时作用于全部 \(B_j\)，再选 \(d\) 个 width-5 嵌套 columns，第 \(h\) 个仅作用于 \(j\ge h\)。各 column 满足 CDT (6.0.3) 的阶梯要求，row sums 是 \(0,45,50,\ldots,45+5d\)，积分指数 \(e=0\)。CDT (6.0.4) 给真实但粗的代价

\[
 \tau_d=\frac{5\sum_{j=0}^d(9+j)(2j+3)}{(d+2)^2}
 =\frac{5(d+1)(4d^2+65d+162)}{6(d+2)^2}.         \tag{E23}
\]

例如 \(d=5,7\) 时分别为 \(2935/49\)、\(5420/81\)。这与旧 factorial 系数 analytic parts 的便宜数组完全不同，不能移用旧 \(\tau\)。holonomic 性允许 CDT Corollary6.0.14 使用 \(\log|\varphi'(0)|>\tau_d\) 的形式，但仍须所有实际 pullback 在单位 disk 上 meromorphic，并取得严格 holonomy quotient；本文没有构造这种地图或证明 strict margin。尤其 (E17) 的完整 branch 阻止在 \(\lambda_j=u\) 假设下自动穿过 \(T=\Lambda\)。

## 7. 文献启发的准确落点与尚待解决的接口

Golyshev–Zagier 的 PDF11–14 把不同 gamma lifts、Mellin 积分与同一个 motive 的不同纤维化连接起来；PDF12–13 明确保留积分解释和 rational Betti spaces 的要求。Bloch–Vlasenko PDF22–23 的 Theorem30/Corollary31 证明 Frobenius constants 的周期性质，并用额外 Kummer 变量把 \(\log^j\) 积分实现为周期；PDF23–24 的 Apéry 示例另有 \(LB=6t\)、\(B-\zeta(3)A\) 的真实填洞。该文明确没有把某个 Gamma Taylor coefficient 与另一个整数处的 Gamma 值免费等同。

Laporte–Walcher PDF4–5 的实际 normal function 是 bounding three-chain 积分；其非齐次项来自指定代数 cycle，且额外的 open discriminant 边界条件选择了实际链。PDF7–9 的全 monodromy 常数主要经数值 continuation 获得，特殊值识别在那里仍是数值发现，末尾要求直接几何证明。本文只用它作为**必须另付 cycle、源项、边界条件与积分 basis**的具体提醒，不将该示例转成我们模型的无条件定理。

当前确实完成了一个新相对链候选的检验：

1. (E4) 以指定正实链给 \(\kappa(s)\) 的 exact Euler 实现；(E10)–(E11) 给 log moments 的 actual rational differential forms。
2. (E9)、(E8)、(E21)–(E23) 支付了新的非齐次源、起点初值、全部素数与 CDT 安全数组。
3. (E13)–(E18) 支付了**完整** branch，发现 relation-dependent scalar row 与 log-free Q Taylor 起点无法在这个 Euler/resolvent package 中同时取得；这不是只对 leading branch 的检验。

若继续尝试其它几何扩张，需要一个真正不同的有理相对 cycle：其规范化 analytic germ 在 0 属 \(\mathbb Q[[T]]\)，且其全 variation 恰为原 \((\kappa_j-u)\psi\)（或已准确声明的另一个目标），还须给出相应源项、积分基、全部有限处 cap 和可用 conformal map。本候选的失败没有证明这种扩张不存在。

## 8. 原件、实际读域与冻结边界

本轮新增、正常 TLS 下载并去重检查后保存两份原件：

- Golyshev–Zagier，*Interpolated Apéry numbers, quasiperiods of modular forms, and motivic gamma functions*，[作者 PDF](https://people.mpim-bonn.mpg.de/zagier/files/tex/DubrovinVolume/GZ_AperyInterpolation.pdf)，本地 `literature/cdt_gamma_relative_chain_sources_20261007/golyshev_zagier_interpolated_apery_motivic_gamma_author.pdf`，21页，398788 bytes，SHA `529a92d1ba0744e00c3d26ea97400ae3da25b0615dea5dacbaa0b3f25697d669`。实际 FULL 文本读 PDF1–3、11–14，共7 distinct页；原稿封面仍有 MSC/copyright 占位，未替作者稿编造出版日期或版本。
- Laporte–Walcher，*Monodromy of an Inhomogeneous Picard–Fuchs Equation*，[固定 arXiv v2 PDF](https://arxiv.org/pdf/1206.1787v2)，本地 `literature/cdt_gamma_relative_chain_sources_20261007/laporte_walcher2012_inhomogeneous_picard_fuchs_arxiv1206_1787v2.pdf`，10页，309651 bytes，SHA `98d13843bf09e0ae20e9df9c589dfdbb5973243578eb069749e4106754e06d0f`。本轮实际 FULL 文本读 PDF1–10，另实际 rendered/read PDF4；render 不重复计 distinct页。

既有原件只读、不重新下载：Bloch–Vlasenko arXiv1908.07501v2 PDF22–27 实际 FULL 文本6页；CDT `cdt2024_l2_chi_minus3.pdf` PDF66–69 实际 FULL 文本4页。本作者本轮共27 distinct primary PDF页，新增归档31页，两数不混淆。网页搜索/截取不额外冒认原件整页。PDF4审阅 PNG 仅为本轮原件视读 artifact。

本文未读取或运行旧/同行数学源码、结果表、guards；未扩大素数表，也未把 period identification 或 coefficient height upper 当作新无理性定理。正式审查及收审后最终作者全文回读完成前，本文仍是 NEW 候选；FINAL 来源收据须另外单向记录最终物理 SHA 和实际读域，不 pin 自己、mutable 主报告、未来 audit 或对方 receipt。
