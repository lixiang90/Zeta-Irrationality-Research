# 第252轮：成功源机制、完整预算与两个数值候选

2026-10-10。正式全局复盘；第248–251轮 Fricke 默认窗口结束。本稿只比较实际源与第一准入证书，不延长该源的 map、prime 或固定滤波优化。数学程序、参数/素数/map/word 扫描、Lean 与旧 producer 均0；没有新数值无理性或线性无关性定理。实际读取身份和完整选段另见本轮 packet_reading_scope.md。

## 1. 已证明的边界与成功机制

本轮全文读取248正式报告、251冻结报告、246成功源对照、232截区源及243 K5进展。251已证明正处两点所有到达叶不填、实际部分 conic lift、无限填叶子群和线性指数族的能量界；尚未证明全部实际合法非线性图的正处能量。这里停止投资，并不把一个未付的全图界改写成最优 no-go。

实际重读 CDT 的完整选段显示，成功不来自“低 genus + native 补点”：

* 对 \(\eta=L(2,\chi_{-3})\)，原生模参数的单位整系数逆变换支付完整前缀。实际三源满足
  \[
  L H_A=0,\qquad L H_B=1,\qquad L H_C=(1-x)^{-1},
  \]
  且完整 \(d_N^2\) 清分母。假设 \(a+b\eta/2+c\zeta(2)/4=0\)，得到的有理系数源实际越过 \(x=1/9\)。完整二重积分支付了这次过收敛；不是在普通点去掉一个人工极点。最后证明还用14行、纯函数及精细类型，不能只保留三行的分母表而继承最终结论。
* CDT 的近参数两对数乘积定理已经证明。两个 Apéry 响应的 Hadamard 积把真实关系写进同一有理非齐次源，\(d_N^2\) 清整个源；接近的参数使未取消奇点的整体几何接近有利的三穿孔背景。它是可迁移的机制，但 \(m/n\) 接近1的现有结论、以及已经由 Lindemann–Weierstrass/Baker 覆盖的单对数，不能充作新数值出口。
* 仓库 Catalan 的增长混合矩阵机制，依赖整个列池的周期系数消去、整接触模块、无限非零及统一能量；它不要求把固定有限源的所有背景恢复到一个共同图。本文未重新全文审阅该仓库证明，采用A本轮的独立机制核验作为比较输入。

CDT 末章的整数 holonomic module 局部自由性是 Question 15.2.2，不能采用为已证定理。把 \(h=1/x\) 的 bivalent 构造写下来，并不支付该整数模块假设或尚未解决的 \(\operatorname{Li}_2(1/n)\) 个别值。

## 2. 可迁移的全前缀整性命题

设 \(h(q)=\sum_{n\ge1}a_nq^n\)，固定整数 \(C\ne0\) 与整数 \(s\ge0\)，并已证明
\[
 C a_n/n^s\in\mathbf Z\quad\text{对全部 }n\ge1.
\]
若 \(k\ge s\)，则 \(I_k=\delta_q^{-k}h\) 的完整前缀由
\[
 C d_N^{\,k-s}
\]
清分母，包含2及所有素数幂。证明就是 \(a_n/n^k=(a_n/n^s)n^{-(k-s)}\)，每个 \(n\le N\) 的分母都整除该 LCM 幂。

若 \(x(q)=q+q^2\mathbf Z[[q]]\)，其原生逆函数 \(q(x)\in x\mathbf Z[[x]]\)，且 \(A(x)\in\mathbf Z[[x]]\)，则同一个因子清 \(A(x)I_k(q(x))\) 的全部前缀：次数不超过N只用 \(I_k\) 的前N项，合成与乘法系数为整数。Euler jets保持此界；先对完整函数普通微分再截断至N，须按更高输入截断处理。

Pasol–Zudilin 的完整定理给出实际例子：
\[
 F_{4a}=\Delta/E_4^2,\quad F_{4b}=E_4\Delta/E_6^2
\]
均满足一次积分整性；\(F_6=E_6\Delta/E_4^3\) 满足二次积分整性。因此三次、五次积分分别可由 \(d_N^2,d_N^3\) 清前缀，确实改变宏观费用。本文采用其已建立的 Theorems 1–2，不冒称独立重证全文 Shimura–Borcherds 论证。

但这不是任意角色的性质。标准权3 Eisenstein 系数
\[
 a_n=\sum_{d\mid n}\chi_{-8}(d)d^2
\]
在每个奇素数p满足 \(a_p=1+\chi_{-8}(p)p^2\equiv1\pmod p\)，故 \(n\mid a_n\) 根本不成立。换导子不能免费获得 magnetic 降层。已读 CDT 的 Cooper 示例响应为已知 \(\pi^2\) 倍数，也不能当新目标。新的 magnetic 载体还须证明 holonomic 坐标、目标周期投影、实际秩和同对象能量。

## 3. 整数增长与能量的一个精确相图

独立纸核如下全前缀命题。若 \(H(0)=0\)，\(w\in\mathbf Z_{\ge0}\)，且固定b满足 literal
\[
 b n^w h_n\in\mathbf Z\quad(n\ge1),
\]
则固定j的 \(H^j\) 全部前缀由
\[
 b^j\prod_{i=1}^{j}d_{\lfloor N/i\rfloor}^{\,w}
\]
清分母。对一个正整数分拆 \(n_1+\cdots+n_j=n\)，把 \(n_i\) 降序排列就有 \(n_i\le\lfloor n/i\rfloor\)；逐项乘积即得所有素数幂的整性，不能用有限头代替此证明。

对 \(1,H,\ldots,H^{m-1}\)，宽度 \(1/i\) 的列重复w次，给
\[
 \tau_m=w\left(H_{m-1}-\frac{m-1}{2m}\right)
 \le w\log m+w/2.
\]
w>0时上述不等式严格；w=0时费用为0。这里先固定m再取 Taylor 渐近；\(b^j\) 为固定清分母。各幂的实际秩m仍要求H在 \(\mathbf Q(x)\) 上超越，不能由原微分方程的有限秩领取。

若另外确实支付同一共同图族
\[
 c_R\ge R,\quad J_R\le C R^\rho+C_0,\quad
 \operatorname{rank}_{\mathbf Q(x)}\{1,H,\ldots,H^{m-1}\}=m,
\]
并有 \(\tau_m\le w\log m+B\)，取 \(R=e^{B+d}m^w\)，基本 CDT 严格条件可由
\[
 md>C e^{\rho(B+d)}m^{w\rho}+C_0
\]
认证。\(w\rho<1\) 自动给大m严格余量；临界 \(w\rho=1\) 的充分条件是
\[
 C\rho e^{\rho B+1}<1.
\]
\(w\rho>1\) 只说明此上界证书没有自动跨关，不是所有方法失败。

更一般地，若固定b乘完整
\(D_N=\prod_a d_{\lfloor\beta_aN\rfloor}\) 清每个前缀，排序证明直接给
\(\prod_{a,i\le j}d_{\lfloor\beta_aN/i\rfloor}\) 清 \(H^j\)，费用公式以
\(S=\sum_a\beta_a\) 代w。**普通完整 \(d_N^w\) 本身足够该幂旗标，不要求 literal \(n^w\)**；它不推出后一个更强的单系数类型，坐标合成后也不能偷保后者。

因此可改变相位的是完整前缀S、实际能量指数或常数，而不是只改某个系数的记法。共同图还须满足所采用CDT的闭盘/边界条件或另付合法径向近似；单个根式的部分lift不够。S=0时取一个导数大于1的固定合法图，再增大固定m即可，无须R随m增长。当前 Fricke 或 K5 源没有在此领取新的全幂、全图证书。

## 4. 优先候选：导子8的 Rhin–Viola 完整五列包

目标为 \(L_8=L(2,\chi_{-8})\notin\mathbf Q\)。它不由单对数定理、\(\pi^2\) 代数倍数、CDT 的 \(\chi_{-3}\) 定理或仓库单个 Catalan 结论推出；本文不据检索未命中宣称全球首次或完成全局目标状态证明。

实际 FULL 读 Rhin–Viola 2005 pp392–394 的定义及 Theorem 2.1。对非负参数，该定理使用修正的完整泛函
\[
 I_z=I_z^{(0)}-(\log z)I_z^{(1)}
\]
并给整系数多项式身份
\[
 d_Hd_K z^\alpha(z-1)^\beta I_z
 =P(z)-Q(z)\operatorname{Li}_2(1/z).
\]
因此 Li1/log 通道已经由实际混合积分消去；不能只取未经修正的正方形积分继承此式。

固定 \(n\ge2,\ r=0,\ldots,4\)，取
\[
 (h,j,k,l,m)=(10n+r,8n,8n,5n,10n).
\]
直接代入定理的全部 max/min 定义给
\[
 H=13n+r,\quad K=12n+r,\quad
 \alpha=16n,\quad\beta=3n-r,\quad\delta=16n.
\]
统一因子
\[
 D_n=d_{13n+4}d_{12n+4},\qquad
 D_n z^{16n}(z-1)^{3n}
\]
因而把五个完整泛函写成
\[
 P_{nr}(z)-Q_{nr}(z)\operatorname{Li}_2(1/z),
 \qquad P_{nr},Q_{nr}\in\mathbf Z[z],\quad\deg\le16n+4.
\]
这是所有系数、所有素数幂的实际整数结论。对非实八次单位根采用从原定理域延拓的同一 dilogarithm 原生支；不把复杂混合积分当正测度。

令 \(\zeta=e^{\pi i/4}\)，\(\tau_\chi=i\sqrt8\)。若存在整数向量 \(v_{nr}\) 使
\[
 Q_n=\sum_{r=0}^4v_{nr}Q_{nr}
 \equiv c_n\ne0\pmod{z^4+1},
\]
则对 \(P_n=\sum v_{nr}P_{nr}\) 取有符号 Gauss 迹
\[
 -\tau_\chi^{-1}\sum_{a\in\{1,3,5,7\}}\chi_{-8}(a)
 \{P_n(\zeta^a)-c_n\operatorname{Li}_2(\zeta^{-a})\}
 =A_n-c_nL_8,\qquad A_n\in\mathbf Z.
\]
因为 \(\sum_a\chi(a)\zeta^{ak}=\tau_\chi\chi(k)\) 及
\(\sum_a\chi(a)\operatorname{Li}_2(\zeta^{-a})=-\tau_\chi L_8\)；
\(A_n=-\sum_k[P_n]_k\chi(k)\)。无额外固定导子清分母。

**第一且唯一建议的253证书**是上述固定五列的全n常数非零 intersection。把 \(Q_{nr}\bmod(z^4+1)\) 的后三个系数组成3×5整数矩阵；其整数核非零是维数事实，但核中常数 \(c_n\ne0\) 不是维数事实。必须证明实际 image 含非零常数，或给无界n子族的严格证书及明确向量高度。有限头、泛型秩、其他五列包均不能替代它。

依赖顺序为：完整 RV 身份（已付）→实际非零常数投影（未付）→投影整数高度/primitive 费用→同一有符号完整泛函的真实能量与无限非零。若第一关失败，停止该固定包；若成功，仅获得下一项准入，不获得数值定理或长期优化窗口。它比 Fricke 全图能量缺口更有限可验，但后三个接口尚未更近，不能预领主方法胜利。

## 5. 截区导子8：一个已付投影资产及停止理由

为避免把χ8名称当新机制，另纸证与232截区架构同型的完整Q模型。设 \(a=1/\sqrt2\)，
\[
 {\cal M}_8(i,j)=
 \int_{[-1,-a]\cup[a,1]}\int_0^1
 \frac{|t|t^is^j}{\sqrt{1-t^2}(1-ts)}\,ds\,dt .
\]
令 \(\ell_8=\sqrt2\log(1+\sqrt2)\)，
\[
 r_l=\sum_{b=0}^l\frac{(-1)^b\binom lb2^{-b}}{2b+1},
 \qquad k_l={\cal M}_8(2l,0)/\sqrt2.
\]
这些积分绝对收敛，因为端点上界是
\((1-t)^{-1/2}(1+|\log(1-t)|)\)。
\({\cal M}_8(0,0)=2[\operatorname{Cl}_2(\pi/4)+\operatorname{Cl}_2(3\pi/4)]\)，
而 \(\sin(n\pi/4)+\sin(3n\pi/4)=\sqrt2\chi_{-8}(n)\)；
故 Fourier 和给 \(k_0=2L_8\)。积分分部给全部l
\[
 2lk_l=(2l-1)k_{l-1}+r_{l-1}+2^{-l}\ell_8,
 \qquad k_l=2c_lL_8+\alpha_l\ell_8+\rho_l ,
\]
其中 \(c_l=4^{-l}\binom{2l}l\)，\(\alpha_0=\rho_0=0\)，
\[
 2l\alpha_l=(2l-1)\alpha_{l-1}+2^{-l},\quad
 2l\rho_l=(2l-1)\rho_{l-1}+r_{l-1}.
\]
完整池 \(m=d+1,\ r=0,\ldots,2m-1,\ s=0,\ldots,d\) 满足
\[
 N_{rs}={\cal M}_8(2(d+r),2(d-s))/\sqrt2
 =2L_8c_{r+s}+\ell_8\alpha_{r+s}+R_{rs},
\]
\[
 R_{rs}=\rho_{r+s}
 -\sum_{v=0}^{d-s-1}\frac{r_{r+s+v}}{2v+1}.
\]
故没有遗漏 finite heads，也没有额外 π² 通道。

写 \(\nu(dx)=dx/(\pi\sqrt{x(1-x)})\)，
\(I_l=\int_0^{1/2}x^l\nu(dx)\)，则
\[
 \alpha_l=\frac\pi4(c_l-2I_l).
\]
两m块 \([c_{r+s};\alpha_{r+s}]\) 等价于同 arcsine 测度在 \([0,1/2]\)、\([1/2,1]\) 的m+m矩。任何次数至多 \(2m-1\) 的左核多项式须在每区至少m次变号，矛盾；因此完整堆栈有理满秩。具体令 \(E=[A;B]\)、\(A_{sr}=c_{r+s}\)、\(B_{sr}=\alpha_{r+s}\)，取 \(k=4^L d_{2L+1}\) 清E，则
\[
 U=k\,\operatorname{adj}(kE)[I_m;0]\in\mathbf Z^{2m\times m},
 \quad BU=0,\quad AU=\det(kE)I_m.
\]
它杀全部 \(\ell_8\) 并保留m个独立 \(L_8\) 列。投影高度仍须作为实际费用，不是免费整数化。

令 \(L=3d+1\)。全部头的安全因子是
\[
 Q_d=4^L d_{2L+1}^2.
\]
可自含核验：对
\(\mu_k=\int_{[-1,-a]\cup[a,1]}t^k/\sqrt{1-t^2}\,dt\)，
\(\mu_{2l}/\sqrt2=r_l\)，而
\[
 \frac1{\sqrt2}\int_{\pi/4}^{\pi/2}\cos(2j\theta)
 \log\frac{1+\sin\theta}{1-\sin\theta}\,d\theta
 =-\frac{\sin(j\pi/2)}{2j}\ell_8-\frac{v_j}{j},
\]
\[
 v_j=\sum_{b=0}^{j-1}
 \frac{(-1)^{j-1-b}\binom{j+b}{j-1-b}2^b}{2b+1}.
\]
展开 \(\sin^{2l}\theta\) 后，每项内外两个分母都不超过 \(2L+1\)，即得上述全素数幂界；完整头也同样被清。它是安全上界，不是 primitive 最优费用。

但此资产不打开自动续窗。对 cofactor-free
\[
 W_d(X)=\det[\alpha_{r+s};\,2Xc_{r+s}+R_{rs}]
\]
的实行列式身份，先加 \(\ell_8\) 上块，底块为实际高区矩加 \(2(X-L_8)c\)。上块密度在低、高区分别是 \(-\gamma,+\gamma\)，\(\gamma=\pi/4\)。再加 \(2(X-L_8)/\gamma\) 倍上块，低区对**每个实X**都取消；高区成为原矩加 \(4(X-L_8)\nu\)。含π的此操作仅证明实 determinant identity，不是整数 gauge。

所以新Q规范化确实消除了数域共轭标记问题，却没有免费的关系敏感支撑收益，也未证明 \(W_d(L_8)\) 无限非零或净预算。它不同于228 integrated Gram，但属于232/233已研究的截区架构，应作为投影资产停放，不能用改导子重新启动六轮素数/能量优化。

## 6. 第二候选与决定

具体后备数值目标为 \(X_5=3\zeta(3)+\zeta(5)\notin\mathbf Q\)。单个 Apéry 定理、形式 depth-one 自由性或两数分别无理均不排除有理相消。243权威进展记录：完整 logistic 目标投影、全部素数幂整模型、固定有理关系点的无界非零已付；同一 primitive 费用仅有
\[
 \log d_n\le(1511/60+o(1))n^2.
\]
同对象原 \(-6\) 实处完整认证和严格费用小于6均未付。若先认证能量6，则需要新的完整宏观内容证书跨越所选上界的 \(1151/60\) 缺口；这只是该上界证书所需折扣，不是实际费用 lower 或 source no-go。局部 \(1/24\) 收益不能自动延长资源。

两候选的决定如下。优先一次固定 RV χ8 常数投影准入，因为完整整系数和周期选择已有原始定理，第一关是明确有限维全n命题；通过后仍须重新判断高度、非零和能量。K5保留为已有三接口的后备，但只有新的全局 primitive 内容机制与同对象能量证书才重开。Fricke、χ8截区同架构和未经证明的整数模块猜想都不获默认窗口。Magnetic 全系数降层与第3节相图是值得保留的宏观工具；没有目标匹配及实际共同图时，它们只是准入工具。
