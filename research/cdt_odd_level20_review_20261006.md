# level 20 奇权模型的独立审阅：全局极点、真实秩与两个角色 twist

日期：2026-10-06。审阅对象是 level 20 的纯 \(L(3,\chi_5)\) 两嵌入构造及根分支的 [最终模型](cdt_odd_level20_model_20261006.md)、[精确脚本](cdt_odd_level20_model_20261006_verify.py)。本分支另利用 [探索脚本](cdt_odd_level20_probe_20261006.py) 的基本系列运算 helper 作独立计算。本文不证明新数值无理性；周期 source 的证明见 [共轭投影报告](cdt_odd_conjugate_projection_20261005.md)，level 10 的恢复见 [低周期报告](cdt_odd_low_period_coupling_20261005.md)。

本分支独立重推得到：正确的全局极点界使有限系数确定有理公式；每个真实误差具有最小齐次阶 \(4\)；两个 rank \(4\) 系统的交恰为常数，合并实际秩为 \(7\)。这些结论依赖下面明确写出的原始函数、全局 eta 除子和局部 monodromy，不从有限拟合或目标无理性推出。

## 1. eta 商和 quotient 的全局证明

定义
\[
h=\frac{\eta(4\tau)^2\eta(5\tau)^2}
        {\eta(\tau)^2\eta(20\tau)^2},\qquad
u=\frac{\eta(2\tau)^4\eta(10\tau)^4}
        {\eta(\tau)^3\eta(4\tau)\eta(5\tau)\eta(20\tau)^3},
\qquad B=\eta(2\tau)^2\eta(10\tau)^2.
\]
对 \(h,u\)，权为 \(0\)，两个 eta congruence sums 都是 \(-24\)，
\(\prod d^{r_d}=1\) 是平方；故它们是 \(\Gamma_0(20)\) 上 trivial character 的模函数。对 \(B\)，权 \(2\)，两个 congruence sums 是 \(24\)，
\(\prod d^{r_d}=400\) 是平方。

全部 cusp order 为：

| \(c\)，cusp \(1/c\) | 1 | 2 | 4 | 5 | 10 | 20 |
|---|---:|---:|---:|---:|---:|---:|
| \(h\) | −1 | 0 | 1 | 1 | 0 | −1 |
| \(u\) | −1 | 1 | 0 | 0 | 1 | −1 |
| \(B\) | 1 | 1 | 1 | 1 | 1 | 1 |

其中 \(c=1\) 与 cusp \(0\) 等价，\(c=20\) 与 \(\infty\) 等价。eta 在上半平面没有零点。故 \(h,u\) 都有两处简单极点，总度恰为 \(2\)。

\(\Gamma_0(20)\) 的指数为 \(36\)，有 \(6\) 个 cusp，且没有 elliptic point；
因此 \(X_0(20)\) 的 genus 为 \(1\)。若 \(D=(0)+(\infty)\)，
Riemann–Roch 给 \(\ell(D)=2\)。于是 \(1,h,u\) 的关系已经由全局极点确定；
由 \(h=q^{-1}+2+\cdots,u=q^{-1}+3+\cdots\)，必有
\[
u=h+1.
\]
这不是以有限 \(q\)-jet 猜测无穷恒等式。

用实际 eta 变换计算 \(W_{20}\) 的常数因子：\(h,u\) 的因子均为 \(+1\)，
\[
h(W_{20}\tau)=h(\tau),\quad u(W_{20}\tau)=u(\tau),\quad
B(W_{20}\tau)=-20\tau^2B(\tau).
\]
\(W_{20}\) 非平凡，而 \(h\) 的度为 \(2\)，所以它恰是此 degree \(2\) map 的 deck involution；Fricke quotient 为 genus \(0\)，\(h\) 在 quotient 上度 \(1\)。取
\[
t=(h+1)^{-1}.
\]
三个 cusp pair 的像为：\((0,\infty)\mapsto0\)；
\((1/4,1/5)\mapsto1\)；\((1/2,1/10)\mapsto\infty\)。
每个 cusp 在此 map 下都未分歧。

## 2. 四次 branch polynomial 与二阶底层方程

\(B\,d\tau\) 在 \(X_0(20)\) 上处处非零：在六个 cusp，\(B\) 的简单零点抵消 \(d\tau\) 的简单极点，在内部 eta 无零点。因而
\[
D_h=\theta_q h/B
\]
只在 \(h\) 的两处简单极点有二阶极点，且 \(W_{20}\) 下变号。故
\[
D_h^2=P_4(h)
\]
必为首一四次多项式；其五个系数可由五个精确展开系数全局确定。最终模型的 branch polynomial 为
\[
\Delta(t)=t^4P_4(1/t-1)
=1-12t+28t^2-32t^3+16t^4=C_+(t)C_-(t),
\]
\[
C_\pm(t)=1-(6\pm2\sqrt5)t+(6\pm2\sqrt5)t^2 .
\]
这四个根互异，且均不同于 \(0,1,\infty\)。在已给 pole bound 下，五个精确系数核查足够确定全局恒等式。本分支独立计算也得到
\(P_4(h)=h^4-8h^3-2h^2-8h+1\)，并核验额外 jets。

令 \(S=\theta_q\log t\)，在 \(q=0\) 取 \(S(0)=1\)，\(Y=\sqrt S\)，则
\[
S^2=B^2\Delta/t^2,\qquad
W(Y,\tau Y)=\frac1{2\pi it}.
\]
因此 \(Y,\tau Y\) 的二阶方程可取
\[
Y''+\frac1tY'+Q(t)Y=0,\qquad
Q=-\tfrac12(S'/S)'-\tfrac14(S'/S)^2-\frac1{2t}(S'/S).
\]
沿实际 quotient 的 continuation，\(Y,\tau Y\) 由固定线性矩阵变换：
这来自 \(\tau\) 的 Möbius uniformization 及 \(S\) 的 weight 2 变换。
故方程系数在 quotient 上单值；下面的局部极点控制使它们成为球面上的 meromorphic、因而有理的函数。

其全局极点界可从实际 uniformization 而非 series 拟合证明：

- 在四个 branch \(a\) 处，\(t-a\sim(\tau-\tau_a)^2\)，\(Y\) 的局部指数为 \(1/4,3/4\)；故 \(Q\) 的二阶主部为 \(3/[16(t-a)^2]\)。
- 在 cusp \(t=1\)，指数为 \(1/2,1/2\)；故二阶主部为 \(1/[4(t-1)^2]\)。
- 在 cusp \(t=0\)，指数为 \(0,0\)，\(1/t\) 已承担所需一阶系数；故 \(Q\) 最多有简单极点。
- 在 \(t=\infty\)，两个解的适当线性组合是 \(1,\log t\) 的型，故 \(Q=O(t^{-3})\)。

没有额外的 \(S\) 零点：\(dt/(B\,d\tau)\) 的零点正是 degree \(2\) map 的四个 simple ramification point。因此
\[
Q(t)=\frac{N_8(t)}{t(t-1)^2\Delta(t)^2},\qquad \deg N_8\le8 .
\]
九个精确系数即可全局识别 \(N_8\)；本分支从独立 \(S\) 的 Fraction 微分运算得到
\[
N_8=\frac14(256t^8-1344t^7+3200t^6-4176t^5+3104t^4
-1316t^3+320t^2-49t+6).
\]
额外系数 \(t^9,\ldots,t^{29}\) 的 remainder 均精确为零；这些额外 jet 是诊断，恒等式的全尺度依据仍是上述全局极点界。

## 3. 角色、gauge 和 forcing 的实际下降

这里的 \(A_\pm,V_\pm,f_\pm,\Theta\) 都指 [level 20 共轭投影报告](cdt_odd_conjugate_projection_20261005.md) 的原始函数。\(A_\pm/B\) 本身仍有 Nebentypus \(\chi_5\)，不能将它直接当成 \(X_0(20)\) 上的单值模函数。其平方才有 trivial character，并且只在六个 cusp 有二阶极点，故
\[
(A_\pm/B)^2=\frac{M_{6,\pm}(h)}{h^2(h+1)^2},\qquad\deg M_{6,\pm}\le6.
\]

最终模型的实际 gauge 为
\[
R_-=\frac{A_-}{S}
=-\frac{1-(6+\sqrt5)t+(1+\sqrt5)t^2}
        {5(1-t)\sqrt{C_+(t)}},\qquad
R_+=\operatorname{conj}_K R_- .
\]
其 logarithmic derivative \(R_\pm'/R_\pm\) 属于 \(K(t)\)；
因此 gauge 后的 \(\operatorname{Sym}^2\) 二阶系统产生在 \(K(t)\) 中的 monic 三阶算子 \(\mathcal L_{A_\pm}\)，齐次解为
\(A_\pm,A_\pm\tau,A_\pm\tau^2\)。

对真实误差 \(H_-=A_-(f_--\Theta)\)、\(H_+=A_+(f_++\Theta)\)，Bol 恒等式给
\[
\mathcal L_{A_\pm}H_\pm
=U_\pm(t)=\frac{A_\pm V_\pm}{(\theta_qt)^3}.
\]
右侧确实是 \(K(t)\) 有理函数，而非待付费的 character extension：
\(A_\pm V_\pm\) 的 weight 是 \(6\)、character 是 \(\chi^2=1\)，
两者的 Fricke signs 相乘为 \(+\)；\(\theta_qt\) 在 Fricke 下的因子是
\(+20\tau^2\)，其立方正好抵消分子的 weight \(6\) 因子。

右侧的完整极点界为
\[
U_\pm=\frac{N_{6,\pm}(t)}{t^2(t-1)^3\Delta(t)},\qquad
\deg N_{6,\pm}\le6.
\]
理由：\(t=0\) 的 \(V\) vanishing order 至少 \(1\)，而 \(\theta t\) order \(1\)，故 pole 至多 \(2\)；\(t=1\) 两 source 常数非零、\(\theta t\) order \(1\)，故 pole 至多 \(3\)；\(t=\infty\) 的 \(\theta t\) 是 simple pole，故 \(U=O(t^{-3})\)。在四个 branch，局部 \(t-a\sim z^2\)，\(\theta t\sim z\)。分子 \(AV\) 在 weight \(6\) 的 deck action 下为 odd，至少有一阶零点；所以 quotient 中至多 simple pole。没有把 elliptic branch 的角色成本未经证明地消掉。

本分支直接以原始 \(A_-,V_-\) 的 coefficients 与 \(\theta t\) 的 Fraction 序列运算得到
\[
\begin{aligned}
N_{6,-}&=U_0+\sqrt5U_1,\\
U_0&=-\tfrac{68}5t^6+\tfrac{148}5t^5-\tfrac{247}5t^4+10t^3
 +\tfrac{51}5t^2-4t+\tfrac15,\\
U_1&=22t^5-44t^4+44t^3-27t^2+\tfrac{21}4t-\tfrac14.
\end{aligned}
\]
\(N_{6,+}\) 是其系数共轭。额外 remainder \(t^7,\ldots,t^{28}\) 均精确为零。
\(U_\pm\sim-17/(20t^3)\) 还与下一节的实际 cubic monodromy 系数一致。

## 4. 每个误差的最小齐次阶恰为四

非零有理 forcing 保证
\[
1\in K(t)\operatorname{Span}\{H_\pm,H_\pm',H_\pm'',H_\pm'''\},
\]
以及
\[
(\partial_t-U_\pm'/U_\pm)\mathcal L_{A_\pm}H_\pm=0.
\]
因此实际 cyclic rank 至多 \(4\)。**forcing 非零本身不保证下界为 \(4\)**，下界须由实际 monodromy 证明。

在 cusp \(\gamma_c=(1,0;c,1)\) 的高虚轴变量 \(\sigma\)，Bol 恒等式给
\[
(c\sigma+1)^2 f_\pm(\gamma_c\sigma)
=\frac{(2\pi i)^3}{6}v_{\pm,c}\sigma^3+\text{次数至多二的项及指数小项}.
\]
因此 \(H_\pm\) 的最高 cubic 系数是
\(a_{\pm,c}v_{\pm,c}(2\pi i)^3/6\)。subtracting \(\Theta A_\pm\) 至多改变二次项，不能消去该项。

在 \(t=\infty\)，cusp \(c=2,10\) 的 width 分别为 \(5,1\)，由完整常数表：
\[
[\log^3t]H_\pm=-a_{\pm,c}v_{\pm,c}w_c^3/6=-17/120 .
\]
两个 cusp 的结果一致。在 \(t=1\)，\(c=4,5\) 的 width 为 \(5,4\)，同样得到
\[
[\log^3(t-1)]H_\pm=-17/6 .
\]
这些数都非零。绕未消 cusp 的四个 monodromy translates 的最高 log 多项式由 Vandermonde 矩阵给出常数线性独立，故任意有理系数齐次 ODE 的阶至少 \(4\)。结合上述上界，最小阶恰为 \(4\)。

这里用的是常数线性独立的四个实际 ODE 解来证明最小阶，不将它误写成四个 monodromy translates 在 \(K(t)\) 上线性无关。原误差的 \(K(t)\)-cyclic rank 随最小阶为 \(4\)。

## 5. 两个 rank 四系统的交恰为常数，合并秩七

设
\[
\mathcal M_\pm=K(t)\operatorname{Span}\{H_\pm,\partial H_\pm,\ldots\}
\]
为实际函数微分模块。它们都包含常数模块 \(K(t)\cdot1\)。
\(\mathcal N_\pm=\mathcal M_\pm/(K(t)\cdot1)\) 的秩为 \(3\)，并由对应 \(\mathcal L_{A_\pm}\) 描述。

\(\Gamma_0(20)\) 有非交换的上下 parabolic 元素，其 Zariski 闭包的连通部分为 \(\mathrm{SL}_2\)。\(\operatorname{Sym}^2\) 的标准三维表示不可约；有限 character twist 不改变连通部分不可约性。所以 \(\mathcal N_\pm\) 都是 irreducible rank \(3\) 模块。

还须证明它们不相同。两个 gauge 的 ratio 满足
\[
(R_-/R_+)^2=
\left(\frac{1-(6+\sqrt5)t+(1+\sqrt5)t^2}
           {1-(6-\sqrt5)t+(1-\sqrt5)t^2}\right)^2
\frac{C_-(t)}{C_+(t)} .
\]
\(C_+\) 与 \(C_-\) 各有两个互异根、彼此无公共根，所以 ratio 有非平凡 quadratic monodromy。两 rank \(3\) determinant 模块的 ratio 是 \((R_-/R_+)^3\)；因为 \(3\) 为奇数，此 quadratic twist 在 determinant 上仍非平凡。因此 \(\mathcal N_-\not\simeq\mathcal N_+\)。这不依赖只比较两原始函数的某几个系数。

该 determinant 计算也可以直接由真实解的 Wronskian 检验：
\[
W(A,A\tau,A\tau^2)=2A^3(\tau')^3
=\frac{2R^3}{(2\pi i)^3t^3}.
\]
ratio 的 logarithmic derivative 在 \(C_\pm\) 根有残数 \(\pm3/2\)；
有理 gauge 的 logarithmic derivative 的残数必为整数，所以无法建立有理 determinant 同构。

若 \(\mathcal M_-\cap\mathcal M_+\) 包含非恒定模块，其在两个 simple quotient 中的像均非零，因而均为整个 rank \(3\) quotient。常数 kernel 秩 \(1\) 迫使交等于两个 rank \(4\) 模块，从而两个 quotient 同构，矛盾。因此
\[
\boxed{\mathcal M_-\cap\mathcal M_+=K(t)\cdot1,\qquad
\operatorname{rank}(\mathcal M_-+\mathcal M_+)=7.}
\]
这是一条真实函数秩结论，不是七个端点数值独立的结论。

两模块还可以显式 descent 到有理系数芽：在 \(L(3,\chi)\in\mathbb Q\) 的假设下，
\[
J_0=(H_-+H_+)/2,\qquad J_1=(H_--H_+)/(2\sqrt5)
\]
都属于 \(\mathbb Q[[t]]\)，在已验证的 Fricke 叶正则。
它们与常数行的 derivative closure 的秩仍为 \(7\)，因为拉回 \(K\) 后的变换可逆；
\(J_1(0)=\Theta/(5\sqrt5)=-L(3,\chi)/16\)，目标没有在 trace 中全消。
这避免把 \(K\)-维数未经 descent 原样称为 \(\mathbb Q\)-维数。

## 6. 数值目标的剩余证明义务

上述 pole bounds、角色相消、rank \(4\) 与交仅常数已由实际全局函数推导。它们并未给出 \(L(3,\chi_5)\) 无理：仍须在同一 \(t\) 坐标中核查两个 embedding 的 admissible analytic cover、七维（及任何背景增广）全部算术类型、完整 prefix content 和严格 holonomy 不等式。有限 polynomial/jet certificate 也不能替代这四项输入。

\(R_\pm\) 的 numerator 零点及 \(U_\pm\) 的零点会在 gauge 或 homogenization 算子中引入 apparent poles；它们不自动成为实际函数的奇点，也不自动要求从共同解析覆盖删去。须以真实 \(H_\pm\) 及背景函数的延拓判断。

本分支的独立 Fraction 运算已完成并通过，未保存为独立运行证书；相关实现以审阅时读取的 \(N=48\) probe 系列运算 helper 为底层，\(Q,U_\pm\) 的微分、原始 source 构造和 polynomial remainder 由本分支另写。最终模型的 \(Q,U_\pm\) 与此计算一致；最终模型用 \((1-t)^3\) 分母，本稿用 \((t-1)^3\)，分子整体负号已核查。已读取最终脚本，确认它确实额外检查三阶 homogeneous multiplier 与实际 inhomogeneous Laurent identity 的系数 \(-5,\ldots,35\)，以及全部固定安全整数前缀；本分支没有重新执行该脚本，执行状态由根分支的输出承担。

最终模型 §6–7 的非分裂与单行 cyclic rank 论证亦已独立审阅：cusp 的实际 size \(4\) Jordan block 排除 rank \(3\)+constant 的分裂；任一 trace 单行在两个 nonisomorphic simple quotient 都有非零投影，故生成全部 rank \(6\) quotient；若未生成常数，便得到整个 joint extension 的 complement，继而使两个 rank \(4\) 子模分裂，矛盾。

限定的交叉审阅：conjugate_projection 分支独立挑战本稿 §4–5，重推 log³ cusp monodromy、rank \(4\) 上下界、quadratic determinant twist、intersection 仅常数及显式 \(\mathbb Q\) descent，均通过。其审阅不覆盖本稿全部 \(Q,U\) 计算和最终根脚本。若统一采用 horizontal solution representation 或其对偶，determinant ratio 会互为倒数；非平凡 quadratic twist 和全部 rank 结论不变。
