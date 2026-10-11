# 第255轮：完整 holonomy 预算、多源幂与一个新的 χ−8 全数组出口

2026-10-10。本文只作一次跨架构比较。旧 fixed RV adjugate 实现、Fricke 与 K5 的默认窗口不重新开放。实际读域见本轮 packet_reading_scope.md；数学程序、有限头、CAS、prime/map/参数扫描均0。没有新的数值无理性或线性无关性定理。

本稿付两项自含工具：真正多源幂的完整旗标相位，以及参数 Cauchy 矩在特定继续叶组合下的 **Q 全数组周期投影**。后者给明确的数值目标 Y=L(2,χ−8)，不同于已停止的固定 RV 向量和旧 integrated Gram；完整净预算仍未付。

## 1. 成功机制比较必须保留全部接口

实际 FULL 读 [CDT ICM 官方稿](https://math.uchicago.edu/~fcale/papers/ICM.pdf) 物理3–4、9–13。Theorem 2.1 对同一组 m 个 Q[[x]] holonomic 函数要求 Q(x)-线性独立、完整 LCM 数组和共同 meromorphic pullback；合法图满足原文边界条件。写 λ=log|φ′(0)|、J=双圆周 log|φ(z)−φ(w)| 的均值，则严格入口为 λ>τ，结论为

\[
m(\lambda-\tau)\le J,
\qquad \tau=\frac1{m^2}\sum_{i=1}^m(2i-1)\sigma_i.
\tag{H1}
\]

不能只算 λ−τ 而不计 J。数域版本需要加权全部嵌入和有限处；下文幂命题先在 Q 上，不能直接贴到未经同一数值关系整化的 K 源上。

另外 FULL 读保存的 CDT 冻结稿物理159–166选段。其 χ−3 成功对象由实际关系
\(a+bL(2,\chi_{-3})/2+c\zeta(2)/4=0\) 给
\[
H=aH_A+bH_B+cH_C,\quad
\mathcal LH=b+\frac{c}{1-x},\quad
\mathcal L=x(1-x)(1-9x)\partial^2+(1-20x+27x^2)\partial+3(-1+3x).
\tag{H2}
\]
完整 d_N² 系数和 x=1/9 的真实过收敛来自同一关系。原始同时 Padé 收敛指数约0.523，单值小界不够；最终还利用 analytic continuation 和十四个真实独立函数，而不是把二阶背景直接报成十四行。选段未覆盖最终 §13 全预算证明，本稿不声称重审其全部证明。

保存的 Catalan foundations 则给完整列池
\[
F_j(P,D)=M(P,j)-\tfrac32Z(D,j)\in\mathbb Q+\mathbb QG,
\quad tP/\sqrt{1-t^2}-D=O(t^L),\quad j<L.
\tag{H3}
\]
整数 filter 的全部原列均在 contact 范围。实际 nonvanishing 源将 N=p 的 48p 阶关系值归约到三个固定 rational 块，排除固定有限坏素数后估值恰 −96p。real-place 源控制两个实际 sheet 的评价 determinant，uniform 插值因子仅 exp(O(n log n))，同时保留相应 Vandermonde 能量。有限处最终命题与 conclusion 以 **同一 Δ_p** 给下界 >−2.29084、实上界 <−2.2909。本文实际读这些保存文件的指定完整段，但未重跑固定101证书或数值能量证书；这些常数只用于解释已归档的机制，不移植到新对象。

与之相对，254 的固定 RV 实现已有完整整数 A/c、精确 primitive 因子和统一 Chebyshev gain ρ^(−2n)，却没有关系值在无界 n 上非零，也没有同一 q/d·实范数的 strict。所选认证 upper 自身增长不是 actual error lower。一个单向量的正交或形式秩不能替代 Catalan 全增长矩阵的四个接口。

## 2. 多源幂：改变相位要付代数独立，不是微分行数

设 k≥1，实际关系假设下得到
\(H_a\in x\mathbb Q[[x]]\)（1≤a≤k），均 holonomic。固定 b≠0、β_ν≥0，使对所有 N 和 n≤N
\[
bD_N[x^n]H_a\in\mathbb Z,
\quad D_N=\prod_\nu d_{\lfloor\beta_\nu N\rfloor},
\quad S=\sum_\nu\beta_\nu.
\tag{H4}
\]
若实际 H_a 在 Q(x) 上代数独立，则 total degree≤L 的所有单项式给
\[
m_L=\binom{L+k}{k}
\tag{H5}
\]
个 Q(x)-线性独立函数。各固定 L 的 holonomicity 可由 k 个有限维有理微分系统的 tensor product 直接支付；L 先固定再应用(H1)，不让 L 随 Taylor 索引 N 在同一次定理内变化。

任一 degree j 单项式的每个卷积项有 j 个正整数索引。降序后第 i 个索引≤n/i，故其完整前缀由
\[
b^j\prod_{\nu}\prod_{i=1}^j d_{\lfloor\beta_\nu N/i\rfloor}
\tag{H6}
\]
清整；n<j 的系数为0。固定 b^j 吸收到对应行，不贡献固定 L 的 leading 类型。按 total degree 排行，宽度 β_ν/i 的列在所有 degree<i 行为0，在余行为该宽度。首 i 层之前的行数是
\(u_i=\binom{i+k-1}{k}\)。因此该 **实际合法但未必最优** 数组有精确费用
\[
\tau_L=S\sum_{i=1}^L\frac1i-
\frac{S}{m_L^2}\sum_{i=1}^L\frac{u_i^2}{i}.
\tag{H7}
\]
这包括2及所有 prime powers，不把只清单项系数的 literal 猜测当全前缀。

固定 k，\(u_i/m_L\) 的 Riemann 和给
\[
\frac1{m_L^2}\sum_{i=1}^L\frac{u_i^2}{i}\longrightarrow
\int_0^1x^{2k-1}dx=\frac1{2k}.
\]
证明可先限 i/L≥ε，那里多项式比一致趋近 x^k；余项由 \(u_i/m_L\le C_k(i/L)^k\) 支配，至多 O_k(ε^(2k))。故 τ_L=S log L+O_k(S)。无需渐近常数也有 τ_L≤S H_L≤S log L+S。

若另已付同一共同合法图族 c_R≥R、J_R≤CR^ρ+C_0，且完整闭盘/径向条件成立，取 τ_L≤S log L+B、R=e^(B+d)L^S，则(H1)要求
\[
m_Ld\le C e^{\rho(B+d)}L^{S\rho}+C_0.
\tag{H8}
\]
因此 Sρ<k 给足够大的固定 L 矛盾；Sρ=k 时充分条件是
\(Ck!\rho e^{\rho B+1}<1\)，取 d=1/ρ 后留严格余量。S=0 单独取一个固定合法 R>1，再增 L。Sρ>k 只表示这些证书无自动矛盾，不证明最优费用/能量失败。

完整单项式族包含每个 H_a，所以共同合法图集合与原 k 源相同；加幂没有扩大地图，也没有减去(H6)的分母。没有实际代数独立时，不能用(H5)；固定循环模块的行数并不等于 k。

## 3. 一个实际 rank 反例与 level-raising 的不同首关

ICM §3.3 的实际函数
\[
A=(1-4z^2)^{-1/2},\quad B=-2A\arcsin(2z),\quad H=B-gA
\]
满足
\[
H'=\frac{4z}{1-4z^2}H-\frac4{1-4z^2}.
\tag{H9}
\]
这是逐式微分所得，适用于任意常数 g。故所有 H 的 jets 都在 Q(z)+Q(z)H 中，所有这些 jets 的混合多项式都在 Q(z)[H]；degree≤L 的真实 rank 至多 L+1，不能因二阶齐次化或两个 jets 就领取 L² rank。若还加入代数 A，所在字段至多在 Q(z)(H) 上二次，仍只有 O(L) 增长。已付 ICM 例子成功，是完整 S=1 与实际二面体填点图带来的有效 ρ<1，未免费改变 transcendence degree。

有限代数 cover 也不会把这些 jets 变成多个代数独立生成元。与此不同，modular level-raising 可能加入旧函数场之外的新函数；但它必须先有实际有限指数 modular 函数、bounded denominators、目标关系对应的全部周期投影和合法 level transport。本稿未完整重审 UDC 相关命题，不将 Root 的另一分工或 metadata 当作自己的准入证明。任意 Eichler/polylog 的 τ→pτ 不是此工具的假设实例；没有具体完整源时不以 χ−7 旧 dyadic 源给它自动续窗。

## 4. 新 χ−8 候选：完整矩与真实继续叶

记 f(t)=√(1−t²)、c_l=4^(−l)binom(2l,l)，约定非非负整数下标的 c 为0。令
\[
m_i=\int_{-1}^1\frac{|t|t^i}{f(t)}dt,
\quad m_{2l}=\frac2{(2l+1)c_l},\quad m_{2l+1}=0,
\quad m_{-1}=0.
\]
对 |a|<1 的原生芽定义
\[
M_a(i,j)=\int_{-1}^1\int_0^1
\frac{|t|t^is^j}{f(t)(1-ats)}dsdt
=\sum_{u\ge0}\frac{a^um_{i+u}}{j+u+1},
\quad T_d=\sum_{u\ge0}a^um_{d+u}.
\tag{H10}
\]
固定 a=1/√2，沿 a=1 的一个简单单圈取继续叶 M^(1)，原生叶为 M^(0)。具体圈不绕 −1 或0；令 α=arcsin a，则继续为 α→π−α。以下身份从原生区的绝对积分/级数证明，再沿同一圈继续，包含所有有限头。

置 K_d^−=M_a(d,0)、K_d^+=M_a(0,d)。逐项用 \((i+1)m_i=im_{i-2}\) 得
\[
M_a(i-1,j-1)-aM_a(i,j)=m_{i-1}/j\quad(i,j\ge1),
\]
\[
T_d=a^{-d}\left(T_0-\sum_{v=0}^{d-1}a^vm_v\right),
\]
\[
dK_d^−=(d-1)K_{d-2}^−+(a^2-1)T_d+m_{d-2}+am_{d-1}\quad(d\ge1),
\]
\[
(d-1)a^2K_d^+=(d-2)K_{d-2}^++(a^2-1)T_0+2/(d-1)\quad(d\ge2).
\tag{H11}
\]
在 d=1 中省去乘0的 K_(−1)^−。三种初值是
\[
T_0=\frac{2\alpha}{a\cos\alpha},\qquad
K_1^+=\frac{\alpha^2}{a^2},\qquad
aM_a(0,0)=2\int_0^\alpha\frac{v}{\sin v}dv.
\tag{H12}
\]
首式直接令 t=sin θ 积分；第二式由 arcsin² 的 Taylor 系数或对其微分得到。第三式对 aM00 求导后使用第一式，在0取极限。α/sin α 在0可去，在0<α<π无其它极点，因此所取继续叶确实取上限3π/4，未引入未知运输常数。

令 Y=L(2,χ−8)，ℓ=log(1+√2)。分部积分并 Abel 积分
\(\log\tan(v/2)=-2\sum_{k\ {\rm odd}}\cos(kv)/k\) 得
\[
M^{(0)}(0,0)=4Y-\frac\pi{\sqrt2}\ell,\quad
T_0^{(0)}=\pi,\quad (K_1^+)^{(0)}=\pi^2/8.
\]
这里 sin(kπ/4)=χ−8(k)/√2（k奇）。继续叶差为
\[
M^{(1)}(0,0)-M^{(0)}(0,0)
=\frac2a\int_{\pi/4}^{3\pi/4}\frac{v}{\sin v}dv
=2\sqrt2\pi\ell.
\]
所以 3倍原生加1倍继续叶的三个完整初值恰是
\[
\bar M(0,0)=16Y,\quad \bar T_0=0,\quad \bar K_1^+=3\pi^2/2,
\qquad \bar M=3M^{(0)}+M^{(1)}.
\tag{H13}
\]
Abel 级数在每个紧子区可逐项积分；log tan(v/2) 的0端点仅有可积 log v，最终 sine/n² 和绝对收敛。此 identity 不由单个未知周期的数值近似获得。

## 5. Q 全数组、完整 contact 与全阶目标系数秩

定义 **按原矩行归一化** N_ij=a^i \bar M(i,j)。由(H11)的 diagonal reduction，所有 finite heads 的 a 指数在 m_v≠0 时均为偶数。minus 边界乘 a^d 后递推的所有 rational heads 在 Q；plus 边界直接用 a²=1/2 和 \bar T_0=0 递推。由(H13)初值传播，得到对所有 i,j≥0 的精确式
\[
N_{ij}=R_{ij}
+16Y\,a^{i-j}c_{(i-j)/2}
+\frac32\pi^2 a^{i-j+1}c_{(j-i-1)/2},
\qquad R_{ij}\in\mathbb Q.
\tag{H14}
\]
两个非零周期系数中 a 的指数同样均为偶数。这是一个 Q 数组，**不要求假设 Y 的未证明 K-Galois 共轭身份**。实际积分的 a^i 行尺度当然须在实处计价；Q 有理性不是免费实高度。

为核对有限头，可写 i≥j 时
\[
N_{ij}=a^{i-j}\bar K^-_{i-j}
-4\sum_{k=1}^j a^{i+k-j-1}\frac{m_{i-j+k-1}}k;
\]
i<j 时
\[
N_{ij}=\bar K^+_{j-i}
-4\sum_{k=j-i+1}^j a^{i+k-j-1}\frac{m_{k-(j-i)-1}}k.
\]
没有丢弃有限头或只取 period 部分。

令 Z(i,j)=∫_[0,1]² t^is^j/(1-ts)dsdt，则
\(Z(i,j)=Z^0(i,j)+[i=j]\pi^2/6\)，完整 Z^0 由 harmonic partial fractions 得到。对 P,D∈Q[x]，定义
\[
\mathcal F_j(P,D)=N(P,j)-9Z(D,j).
\]
其 π² 系数为
\[
\frac32[x^j]\left(\frac{xP(x)}{\sqrt{1-2x^2}}-D(x)\right).
\tag{H15}
\]
故 contact 为 O(x^L) 时，**全部** j<L 的 raw columns 同时属于 Q+QY。假设 Y∈Q 才把完整矩阵整化为有理对象；这里只付有理性，还未付完整 LCD。

存在一个无需搜索的全阶 integer contact prototype。对 n≥1、0≤r<n 取
\[
P_r=2^n x^{2r},\qquad
D_r=2^n\sum_{l=0}^{n-r-1}2^{-l}\binom{2l}{l}x^{2r+2l+1}\in\mathbb Z[x].
\tag{H16}
\]
contact 余项阶至少2n+1，故所有 j<2n 均可用。degree≤2n−1；行系数高度≤n·2^(2n)，是已付的 exp(O(n)) projection height，不是整个 determinant 的费用已付。

选 n 个列 j=2s（0≤s<n）。这些 entries 的 Y 系数是
\[
16\cdot2^n\cdot2^{-(r-s)}c_{r-s}\quad(r\ge s),
\quad0\quad(r<s).
\]
下三角 diagonal 全为16·2^n，所以 target coefficient determinant 恰 \((16\cdot2^n)^n\ne0\)。这是真实全尺度 **目标系数** 的满秩，不是 actual 值 \(\det\mathcal F(Y)\ne0\)。正测度在继续叶组合后也不能免费继承。此 prototype 只用于证明整个 contact module 不把 Y 通道杀死，不作为已选择的最终优化参数。

## 6. 投入决定与唯一下一关

主候选保持具体 Y=L(2,χ−8)，但使用(H10)–(H16)的完整 parameter/sheet mixed source。它不是 old RV fixedadj，也不是旧 plain integrated Gram：完整 Y coefficient rank n，不是固定 rank-one period；实际两个叶、按行尺度和其它有限 heads 改变了整模型/能量。它也不是内变量加 log 后错误声称仍纯 β(s) 的方案。

这里已经付 uniform all-entry period decomposition、整个 raw pool contact 和一个 integer target-rank prototype。最早仍未付的是：对**这些同一继续叶数组的完整 generating 芽/contour**写可核表示，并给 degree≤H、全部 i,j≤H 的 rational heads 与 period 系数一个含全部 prime powers 的 uniform 清整因子 q_H，log q_H=O(H)。投影行高度、固定2的尺度与所有 finite heads必须计入；不能把 formal recurrence 长度变成免费 d_H²。若完整继续芽引入不能由(H13)三初值控制的新通道、或者 contact 与该完整整模型不相容，就停止这项载体准入。即便这首关成功，也只允许再判断同对象无限非零和 real energy，不领取旧 Catalan 三个 fixed48 块或旧严格常数。

备选数值目标仍 X=3ζ(3)+ζ(5)。240 whole logistic 泛函真有全商部/全简单极点投影，241有关系点无限非零；但243的宏观费用 upper 1511/60 和原 −6 能量的认证缺口未闭。本文未给新全内容或新能量，故不给它同源局部 prime 续窗。已知单独无理性不能推出指定和无理；本稿不声称全局新颖性已核定。

多源(H7)–(H8)是条件工具，不是当前任一 Y/X 候选的 k>1 准入证明。CDT fixed-source powers 与 growing mixed determinant 是两种不同获益机制；它们都必须支付真实数值投影、完整整模型、关系点无界非零和同对象全部能量。正式下一复盘仍256，本文不重置计数，也不宣称原总目标完成。
