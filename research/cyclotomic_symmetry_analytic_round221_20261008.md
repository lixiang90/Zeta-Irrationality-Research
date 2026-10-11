# 第221轮：Catalan 实际悬挂的奇偶对称、平方商与反射

2026-10-08。作者：round218_lambert_carrier。本稿从冻结220的实际函数出发，支付有限的恒等式、函数秩、branch 与共同图。结果是：奇支撑确有新的算术节省；平方商在已下降的奇图家族中没有额外 holonomy 收益；Möbius 反射的原始补点源不能仅由 \(G\in\mathbb Q\) 变成 Q-Taylor source。没有新的数值无理性定理，也没有否定所有独立平方坐标图。

## 1. 实际输入与完整奇偶恒等式

沿0到1的实段固定初始 branches：

\[
A(x)=\arctan x,\quad B(x)=\operatorname{Ti}_2(x),\quad
A'=\frac1{1+x^2},\quad B'=\frac Ax,\quad B(1)=G.
\tag{Y1}
\]

\(A,B\) 都是奇函数，初始 branches 在 \(\pm1\) 全纯，\(B(-1)=-G\)。对固定 \(g\in\mathbb Q\) 定义冻结的真实悬挂

\[
S_g(x)=\int_0^x\frac{B(v)-g}{1-v}\,dv,
\quad E_g(x)=\frac{S_g(x)+S_g(-x)}2,
\quad O_g(x)=\frac{S_g(x)-S_g(-x)}2.
\tag{Y2}
\]

这是实际 Q-Taylor functions；\(E_g\) 偶、\(O_g\) 奇。链式法则特别给出

\[
\frac{d}{dx}S_g(-x)=\frac{B(x)+g}{1+x},\qquad
E_g'=\frac{B-gx}{1-x^2},\quad
O_g'=\frac{xB-g}{1-x^2},\quad E_g(0)=O_g(0)=0.
\tag{Y3}
\]

若 \(G=g\)，Y3 两个分子在 \(x=1,-1\) 都为零；除以简单零因子后是全纯函数。因此两个实际初始 branches 同时补 \(\pm1\)，不是仅取消某项渐近。若 \(g\ne G\)，二点的局部对数系数仍非零。这个关系机制保留了实际 Catalan 目标。

但局部补点仍不意味着每条绕 \(\pm i\) 后到达 \(\pm1\) 的 leaf 都补点。以下共同图会实际核验这件事，不以名义 puncture 数代替 branch 检查。

## 2. 各投影秩四，完整双悬挂秩五

以下函数秩均在 \(K=\mathbb C(x)\) 上证明；对 Q-germs 也推出 Q(x)-独立。绕 \(i\) 的逆时针 monodromy 给 \(\Delta_iA=\pi\)、\(\Delta_iB=\pi\log x+C\)。对 \(r_0+r_1A+r_2B=0\) 应用它，若 \(r_2\ne0\) 则 \(\log x\) 为有理函数，矛盾；随后 \(r_1=r_0=0\)。所以背景 \(1,A,B\) 独立。

若 \(E_g=r_0+r_1A+r_2B\)，微分后按独立背景比较 B 系数，迫使 \(r_2'=1/(1-x^2)\)。这个有理函数在 \(\pm1\) 有非零简单极点残数，不是有理函数的导数。对 \(O_g\) 同理得到 \(r_2'=x/(1-x^2)\)。于是

\[
\operatorname{rank}_K(1,A,B,E_g)
=\operatorname{rank}_K(1,A,B,O_g)=4.
\tag{Y4}
\]

完整对称闭包则是五行 \(1,A,B,E_g,O_g\)，不是四行中的免费 trace。这里给它的完整独立证明。选择绕 i 的路径，使从 i 到正实轴的 \(\log x\) 为主值；局部 \(\Delta_iB\) 在 i 趋于0，因为 B 的分支项是 \((x-i)\log(x-i)\)。由 \((\Delta_iB)'=\pi/x\) 得

\[
\Delta_iB=\pi\log(x/i),\qquad
(\Delta_iB)(1)=-\frac{i\pi^2}{2},\quad
(\Delta_iB)(-1)=\frac{i\pi^2}{2},
\tag{Y5}
\]

最后一个值沿上半平面到达 \(-1\)，所以 \(\log(-1)=i\pi\)。对 Y3 先应用 \(\Delta_i\)，再在对应 leaf 上分别绕 \(1,-1\)，由残数精确得到

\[
\Delta_1\Delta_i(E_g,O_g)
=-\frac{\pi^3}{2}(1,1),\qquad
\Delta_{-1}\Delta_i(E_g,O_g)
=-\frac{\pi^3}{2}(1,-1).
\tag{Y6}
\]

背景三行的这两个双 monodromies 都为0。对任意五行有理关系应用 Y6，分别得到 \(r_E+r_O=0\)、\(r_E-r_O=0\)，于是两系数为0，背景独立再结束证明：

\[
\operatorname{rank}_K(1,A,B,E_g,O_g)=5.
\tag{Y7}
\]

原始 \(1,A,B,S_g\) 因而不在 \(x\mapsto-x\) 下封闭。裸偶投影可以只留下 \(1,E_g\) 两个独立函数，但其微分闭包依次需要 B、A，完整 connection 仍是 Y4 的四行。直接 CDT 可以另选少数行；那是一个必须重新核算费用的实际子源，不能把完整四行源的 rank 或费用直接搬给它。

## 3. 平方坐标的实际 Q-germs 与有理 connection

令 \(t=x^2\)，定义

\[
a(t)=\frac{A(x)}x=\sum_{n\ge0}\frac{(-1)^nt^n}{2n+1},\quad
b(t)=\frac{B(x)}x=\sum_{n\ge0}\frac{(-1)^nt^n}{(2n+1)^2},
\quad e(t)=E_g(x),\quad o(t)=\frac{O_g(x)}x.
\tag{Y8}
\]

这些定义与局部平方根的选择无关，都是实际 Q[[t]]；\(a_0=b_0=1,e_0=0,o_0=-g\)。完整有理微分关系为

\[
2ta'+a=\frac1{1+t},\quad
2tb'+b=a,\quad
e'=\frac{b-g}{2(1-t)},\quad
2to'+o=\frac{tb-g}{1-t}.
\tag{Y9}
\]

因此 \((1,a,b,e)\) 和 \((1,a,b,o)\) 各给一条秩四有理 connection，奇异点包含 \(0,-1,1,\infty\)。函数秩恰为四：任何 C(t)-关系拉回到 \(t=x^2\)，乘去 x 的有理规范因子后会成为 Y4 的 C(x)-关系。\(G=g\) 时，初始 \(b(1)=G\)，Y9 的两个悬挂在 t=1 都全纯。平方商没有降低这个实际完整函数秩。

二个 cyclotomic punctures 现在合并为 \(t=-1\)，却不能据此把 \(\mathbb C\setminus\{-1\}\) 的名义 parabolic geometry 当作共同图。例如绕 i 后，\(\Delta_iB=\pi\log(x/i)\)。再到一个 foreign x=0 leaf，B 可含 \(\pi\log x+C\)，从而 b 在对应 foreign t=0 leaf 可含

\[
\frac{(\pi/2)\log t+C}{\sqrt t}.
\tag{Y10}
\]

这是不可亚纯的实际分支。a 也可能含 \(\pi/\sqrt t\)。初始 t=0 的可去性并不支付这些 foreign leaves。故单 puncture 的 universal cover 并非自动 admissible；本稿没有证明所有独立 t 图的导数上限。

## 4. 一个已付的全盘平方图及一般下降比较

冻结220的实际图是 \(\phi(w)=\tan(cw)\)，\(c=3\pi/8\)。它是奇函数，并在闭单位圆盘邻域使初始 \(1,A,B,S_g\) 全纯，条件是 \(G=g\)。取

\[
\psi(z)=\tan^2(c\sqrt z).
\tag{Y11}
\]

右侧是偶函数的下降，不选择全盘平方根；它在 z=0 展开为普通幂级数，\(\psi(0)=0,\psi'(0)=c^2\ne0\)。最近极点在 \(z=16/9\)，因此闭单位圆盘附近全纯。\(\tan\) 不取 \(\pm i\)，故 \(\psi\ne-1\)。盘内0只有原点；\(\psi=1\) 在盘内只有 \(z=4/9\)，从两个实 w 前像 \(\pm2/3\) 合并而来，下一批的模至少为4。

拉回函数分别由

\[
\frac{A(\phi(w))}{\phi(w)},\quad
\frac{B(\phi(w))}{\phi(w)},\quad E_g(\phi(w)),\quad
\frac{O_g(\phi(w))}{\phi(w)},\qquad z=w^2,
\tag{Y12}
\]

这四个偶的全纯 w 函数下降。分母在 w=0 的零可去；其他0前像在盘内不存在。\(z=4/9\) 沿实路径到达初始 \(b(1)=G\) leaf，Y3 的 \(\pm1\) 补点都已支付。因此 Y11 是平方坐标四行的真实共同图，在闭盘邻域全纯。

更一般地，令 \(\phi\) 为任意已核的、奇的原 x 共同图，定义 \(\psi(w^2)=\phi(w)^2\)。实际 meromorphic 拉回函数的奇偶规范同样下降，且

\[
\psi'(0)=\phi'(0)^2.
\tag{Y13}
\]

对 CDT Theorem 7.0.1 的差值能量
\(J(\phi)=\iint_{\mathbb T^2}\log|\phi(v)-\phi(w)|\,d\mu(v)d\mu(w)\)，Haar measure 在平方映射下不变。因 \(\phi(-w)=-\phi(w)\)，有

\[
\begin{aligned}
J(\psi)
&=\iint\log|\phi(v)^2-\phi(w)^2|\,d\mu(v)d\mu(w)\\
&=J(\phi)+\iint\log|\phi(v)+\phi(w)|\,d\mu(v)d\mu(w)
=2J(\phi).
\end{aligned}
\tag{Y14}
\]

对闭盘邻域全纯非恒定图，这些对数奇点可积；一般只在该 theorem 的能量存在条件下使用等式。这里没有把原所有图称为奇图，也没有把所有 t 图称为下降图。

## 5. 奇支撑的实际节省及当前解析 gate

写 \(h_n=\sum_{j=0}^{n-1}(-1)^j/(2j+1)^2\)。Y3 给精确系数

\[
e_n=\frac{h_n-g}{2n}\quad(n\ge1),\qquad
o_n=\frac{h_n-g}{2n+1}\quad(n\ge0).
\tag{Y15}
\]

取固定正整数 \(c_g\) 使 \(c_gg\in\mathbb Z\)。冻结220的安全包直接给 e 的 \(c_gd_{2n}^2d_n\) 及 o 的 \(c_gd_{2n+1}^2d_n\) 清分母；平方四行的 e=0 类型为 \(\sigma=(0,2,4,5)\)，费用 \(61/16\)，是原半宽表费用的两倍。固定 index 的 +1 可由 CDT Remark 6.0.12 支付，小正 \(\varepsilon\) 后取极限；不能把 \(2n+1\) 免费写成 literal n。

奇源还有更好的真实包。记 \(d_M^{\rm odd}\) 为不超过 M 的正奇整数的 lcm。令 \(M=2n+1\)，则

\[
c_g(d_M^{\rm odd})^2d_{\lfloor M/3\rfloor}^{\rm odd}\,o_n\in\mathbb Z.
\tag{Y16}
\]

本作者独立逐 prime-power 核验如下。对奇素数 p，令 \(h=\max\{j:p^j\le M\}\)。若 \(M\ge3p^h\)，三层都包含 depth h，清除 \(Mk^2\)。若 \(M<3p^h\)，第三层至少含 depth h−1，因为 p≥3。若外层 \(v_p(M)=h\)，奇 M 在该窗内只能等于 \(p^h\)：另一个候选 \(2p^h\) 是偶数；因此每个内层奇 \(k<M\) 的 depth≤h−1，所需≤3h−2。若外层 depth≤h−1，内层≤h，所需≤3h−1。该包两大层加第三层提供至少3h−1。\(g/M\) 亦被固定 \(c_g\) 后包住。所有分母都是奇数，所以 p=2 处没有成本，固定 \(c_g\) 的2部分也由它自身清除。h=0 的素数不出现。这证明所有素数幂，没有仅核大素数。

Y16 给实际四行 \((1,a,b,c_go)\) 的安全 CDT 类型

\[
\sigma=(0,2,4,14/3),\quad e=0,\qquad
\tau=\frac{3\cdot2+5\cdot4+7\cdot(14/3)}{16}
=\frac{11}{3}.
\tag{Y17}
\]

奇 lcm 可安全放大为普通 lcm；Y17 不把奇 lcm 的更细主项偷放进 ordinary CDT 的宽度。同一 lemma 也直接适用于原 x 奇源 \((1,A,B,c_gO_g)\)：偶系数为0，奇系数正是 Y15。因此它已有 \(\sigma=(0,1,2,7/3),e=0,\tau=11/6\)。平方商 Y17 只是将这个新表的所有宽度和 \(\tau\) 加倍。由 Y13–Y14，同源的普通 holonomy quotient 恰满足

\[
\frac{J(\psi)}{\log|\psi'(0)|-11/3}
=\frac{J(\phi)}{\log|\phi'(0)|-11/6},
\tag{Y18}
\]

在分母为正时才作为 theorem 的 bound 使用；负分母只是未入场，不能反推秩矛盾。**净算术节省来自奇支撑，不来自平方商本身。**

冻结220已支付所有原 x 共同图必须避开 \(\pm i\)，以及 \(|\phi'(0)|\le\rho=\pi F(1/2)^2<e^{3/2}\)。因此对当前已下降的奇图家族

\[
\log|\psi'(0)|\le2\log\rho<3<11/3.
\tag{Y19}
\]

即使 a priori holonomic 的较弱条件也没有正费用差，尚不需要估计严格秩商。舍弃背景行也没有令这张已付包过门槛：\((1,o),(1,a,o),(1,b,o),(1,a,b,o)\) 的费用依次为 \(7/2,88/27,106/27,11/3\)，均大于3；每个子源的函数秩由 Y4 保证。这个判断只针对这些安全表和已下降家族，未核所有更细联合费用、multi-map theorem 或独立 t 图的最佳导数。

## 6. Möbius 反射：精确身份与 Q-germ 障碍

令 \(r(x)=(1-x)/(1+x)\)。它是对合，交换 \(0,1\)，交换 \(-1,\infty\)，交换 \(i,-i\)。在实段0<x<1 所确定的 branches 上，定义实际 Q-germs

\[
L(x)=\operatorname{artanh}x=\frac12\log\frac{1+x}{1-x},\quad
C(x)=\int_0^x\frac{A(v)}{1-v^2}\,dv,
\quad L'=\frac1{1-x^2},\ C'=\frac{A}{1-x^2}.
\tag{Y20}
\]

由导数与 x=0 的值精确得到

\[
A(r(x))=\frac\pi4-A(x),\qquad
B(r(x))=G+2C(x)-\frac\pi2L(x).
\tag{Y21}
\]

因为 \(r'/r=-2/(1-x^2)\)，第二式的导数为 \((2A-\pi/2)/(1-x^2)\)，边值为 G，证明不靠有限系数匹配。\(G=g\in\mathbb Q\) 并不使反射后的 B 为 Q[[x]]：其一次系数是 \(-\pi/2\)。A 的常数也为 \(\pi/4\)，即使先减去它，B 的这个非有理系数仍在。

若作显式 Tate compensation，\(B(r)-g+(\pi/2)L=2C\) 是 Q-germ；但 C 本身对任何 g 都存在，且在 x=1 有

\[
C(x)=-\frac\pi8\log(1-x)+\text{全纯函数}.
\tag{Y22}
\]

原始 \(B(r)\) 在 x=1 全纯，是因为 Y21 的完整对数相消；只保留 Q-germ 2C 会重新引入它。不能同时凭这一个补偿声称原 branch geometry 和 Q-Taylor source 都免费保留。

再令 \(R(x)=S_g(r(x))\)。当 \(G=g\) 时 x=0 的原悬挂奇点已补，\(R(0)=S_g(1)\) 有限，且

\[
R'=-\frac{B(r)-g}{x(1+x)}
=-\frac{2C}{x(1+x)}+\frac\pi2\frac{L}{x(1+x)}.
\tag{Y23}
\]

所以 \(R'(0)=\pi/2\)。本稿未证明 \(S_g(1)\) 有理；即使减去该常数，\(R-R(0)\) 也因这个一次系数不能仅由 G 的有理性变成 Q[[x]]。用新数值关系处理 \(\pi\) 或这个附加 period，不属于原目标假设。

为完整显示补偿所加的函数，定义

\[
H(x)=\int_0^x\frac{L(v)}{v(1+v)}\,dv,\qquad
D(x)=\int_0^x\frac{C(v)}{v(1+v)}\,dv.
\tag{Y24}
\]

两者是 Q[[x]]，原点核可去。Y23 的实际全身份是

\[
R(x)-R(0)-\frac\pi2H(x)=-2D(x).
\tag{Y25}
\]

因此 compensated Q packet \((1,A,C,D)\) 有有理秩四 connection，但它无条件存在，已失去原 \(g=G\) 的悬挂对数测试。C 在1有 Y22 的 log，D 在1有非零 \((1-x)\log(1-x)\) 分支，均不可亚纯。完整比较 packet \((1,A,L,C,D,H)\) 的有理 connection 由 Y1、Y20、Y24 给出，函数秩恰为六：\(1,A,L\) 用分别绕 i、1 的 monodromy 独立；C 的加入迫使有理系数导数为 \(1/(1-x^2)\)；D 的加入迫使 C 系数导数为 \(1/[x(1+x)]\)，都不可能。若 H 在前五行的有理张成中，微分按五行比较：D 系数先为常数 d，C 系数导数为 \(-d/[x(1+x)]\)，故 d=0；C 系数为常数 c，A 系数导数为 \(-c/(1-x^2)\)，故 c=0；最后 L 系数导数必须为 \(1/[x(1+x)]\)，仍不可能。这里“六”是确切函数秩，不把新增 companions 当免费形式标签。

## 7. 反射共同图与有限投入判断

Y21、Y25 首先是从实段 continuation 得到的恒等式；它们随后沿任何两侧共同 continuation 的路径成立。本稿不把任意避开 \(\pm i\) 的图自动当作反射四行的共同图。

例如直接用旧 \(\phi(z)=\tan(3\pi z/8)\) 作为反射 x 图，会在 z=−2/3 取 x=−1；此时 r 有极点，\(B(r),S_g(r)\) 经无穷远出现对数 branches，不能通过原 tan 图的核验。因此旧图并非反射源的免费全盘图。把旧盘自动重心移到其1前像也不能解决这个盘内 pole。

一个有限、实际但无大容量主张的共同图可以明确支付：\(\theta(z)=z/2\)。它把闭单位圆盘邻域送入 \(|x|<1\) 的较小盘，避开 \(\pm1,\pm i\)；r 将之送入 \(\Re r>0\) 的有限域。A、B 在右半平面的初始 branches 全纯；\(G=g\) 后 \((B-g)/(1-x)\) 在右半平面全纯，包括实际 x=1。该域单连通，故 S_g 也有从初始1 leaf 确定的全纯 primitive。因而原反射四行在 \(\theta\) 下实际全盘全纯。所有 Y20、Y24 的 Q-companions 也在同一图下全纯。然而原四行仍有 Y21、Y23 的非 Q coefficients；compensated packet 的补点几何已变。这个小图仅支付 branch 实现，不提供新的正 holonomy gate。

本轮最强已证收益是 Y16 的奇支撑分母改善、完整 rank5 双悬挂及真实 rank4 平方 source；它们都保留了 G 目标的补点。平方坐标还能把两个 target 点合成一个，且有显式 Y11 实际共同图，但当前已下降家族受 Y19 阻挡。继续投入若要有解析收益，应首先给出一个**独立 t 图的完整 foreign-leaf 控制与实在较大导数**，或进一步降低同源的完整算术费用；不能以单 puncture 名义容量为替代。反射原始 source 的 Q-germ 障碍已经具体可见；单靠增加 Tate companions 没有保住原关系机制，暂不作为当前主线的容量调参入口。

## 8. 读取、primary 与实际运行范围

本轮实际 FULL 读取冻结输入 [cross_target_strategy_global_round220_20261008.md](cross_target_strategy_global_round220_20261008.md) 的全部八节：18626 bytes，SHA256 `93a9adf0a563529d9a577713c1a038bf0c34330e80e06793f7ba105433f23a42`。还读取 root 当前 NEW 微分投影稿的六节，只用于对照操作范围，不把它称为冻结独审。Y1–Y25 的新推导都是有限纸面证明。

Primary 接口只采用 [CDT fixed v2](https://arxiv.org/pdf/2408.15403v2) 已付 Definition 6.0.1、Theorem 7.0.1 及冻结220中的费用/\(\rho\) 证明；本轮额外读取已本地提取的 printed page67 完整 Remark 6.0.12 与 page68 开头续段，以核固定 index shifts 和 \(\varepsilon\) 极限。两个现成提取文件还包含 appendix page203–205，实际读到但未把其中 contour 数值用于本稿。没有新浏览下载或声称读过218页全篇，没有增加非 primary 文献。

运行 ledger：数学程序0，CAS0，数值积分0，素数/参数扫描0，PSLQ0，Lean0，Git0。工具仅做全文 documentary 读取、文件定位、metadata/SHA256 和本 NEW Markdown 写入。Y16 在收到算术 agent 候选后由本作者独立纸核；本稿不代替其最终独审。作者将对最终保存文件实际 FULL 复读，最终 bytes/hash 在外部登记；该作者复读不是独立审查。未编辑旧数学稿、main 或 manifest。
