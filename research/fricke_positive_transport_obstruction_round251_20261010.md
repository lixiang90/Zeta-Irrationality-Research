# 第251轮：正处全部 Q+ 运输叶的不补支奇偶证书

2026-10-10，C。固定第248–250轮的同一 Fricke 商坐标、完整 rank3 源与数域假设
\[
s=\sqrt2,\quad K=\mathbf Q(s),\quad Y=L(2,\chi_{-7}),\quad
g=g_+=Y/2+s\pi^2/28\in K.
\]
本文证明：**正处两个 Q+ 根的每一个实际运输到达叶均不能补支**。证明是全奇分母的有限 Fourier / half-permutation 奇偶恒等式，不执行分母、群字、地图或素数扫描。由此合法正图确实提升 Q+ 的 genus0 二重覆盖；这个部分覆盖本身仍允许任意大的 derivative，故没有在本文领取全图能量、免费整数背景或新数值无理性。

## 1. 固定实际源、全叶输入与待排除的实条件

令
\[
Q_\pm(t)=1-(7\mp4s)t+t^2,\quad E=Q_+Q_-,
\]
\[
A_\pm=A(\tau)\pm sA(2\tau),\quad
I_\pm=R\pm(2s/7)D,\quad B_{+,g}=A_+(I_+-g).
\]
完整 frame 是冻结的 \((1,7b_0B,7b_0E\delta B)\)，其中 \(b_0g\in\mathcal O_K\)、\(\delta=t\partial_t\)。下文整数 \(b\) 是稳定子参数，和固定清分母 \(b_0\) 无关。

本轮 actual FULL 读取 A250 的 A1–A13 与 C250 的 T1–T10。它们已支付以下完整输入：
\[
\Gamma^*=\Gamma_0(14)\sqcup\Gamma_0(14)W,\qquad W\tau=-1/(14\tau).
\]
全部有限 order2 stabilizers 都可取
\[
\gamma=\begin{pmatrix}a&b\\14b&d\end{pmatrix},\quad
ad-14b^2=1,\quad d>0,\quad
r=\gamma W,\quad \tau_r=b/d+i/(\sqrt{14}d).                \tag{P1}
\]
于是 \(d,a\) 奇，\((d,7)=(b,d)=1\)。regular covering 的每个 transported 到达叶，其局部返回经共轭仍属于(P1)；不需要尚未认证的有限生成清单。

正处 multiplier 与完整返回常数为
\[
j_r=-i\sqrt{14}\chi(d)(d\tau-b),\quad j_r(\tau_r)=\chi(d),
\]
\[
I_+(r\tau)-g_{r,+}=j_r^{-1}(I_+(\tau)-g_{r,+}),\quad
g_{r,+}=Y/2+\pi^2\{i\sqrt7\,q_{b,d}+(2s/7)\theta_{b,d}\}.  \tag{P2}
\]
\(\chi=\chi_{-7}\)，\(q_{b,d},\theta_{b,d}\in\mathbf Q\)。\(\chi(d)=-1\) 恰为 Q+ 两根的返回，\(\chi(d)=+1\) 为 Q−。这里 \(A_+\) 在 Q+ 有 simple zero；权1 gauge 的精确 odd 公式使整个叶补支 iff \(g_{r,+}=g\)，而不是只取消一个普通点值。其必要充分条件是
\[
q_{b,d}=0,\qquad \theta_{b,d}=1/8.                        \tag{P3}
\]
本文只需在 \(\chi(d)=-1\) 时排除第二式，不声称计算了所有虚周期。

可选 \(b\) 为奇数代表：把 \(b\) 换成 \(b+\ell d\)，相应
\(a\mapsto a+28\ell b+14\ell^2d\)，仍满足(P1)。这是 \(T^\ell rT^{-\ell}\)，固定点实部加整数，\(R,D,I_\pm\) 的 q-相位与填点条件不变。因为 d 奇，存在奇 b 代表；以下证明实际上只使用 b mod d。

## 2. 从实际 Fourier 系数到整数与 floor

令
\[
T(z)=\sum_{m\ge1}\chi(m)z^m
=\frac{z+2z^2+z^3+2z^4+z^5}{S_7(z)},\quad S_7=1+\cdots+z^6.
\]
在 \(\mathbf Q[z]/(z^d-1)\) 中唯一写 \(T=\sum_{k=0}^{d-1}c_kz^k\)。冻结250的严格 Abel 极限、对称性与完整 Bernoulli Fourier 公式给
\[
c_k=c_{d-k},\quad \sum c_k=1,\quad
\theta_{b,d}=\frac18-\frac{M_{b,d}}{2d},\quad
M_{b,d}=\sum_{k=0}^{d-1}c_k\min(bk\bmod d,d-(bk\bmod d)).  \tag{P4}
\]
本轮进一步支付精确整数公式
\[
\boxed{c_k=\chi(d)f([kd^{-1}]_7),\qquad
f=(1,1,0,-1,0,-1,0).}                                  \tag{P5}
\]
\([\,]_7\) 为0…6代表。特别 \(c_k\in\mathbf Z\)，\(c_0=\chi(d)\)。

自含证明(P5)：在 d 个 roots 作有限 Fourier filter，并令径向变量 \(\rho\uparrow1\)。对 \(1\le k<d\)，投影系数是
\[
\lim_{\rho\uparrow1}\sum_{\ell\ge0}\chi(k+\ell d)\rho^{k+\ell d}
=-\frac17\sum_{\ell=0}^6\ell\,\chi(k+\ell d).
\]
右式由七周期 numerator 的零 augmentation 与一次 derivative 直接得到；所用只是有限 polynomial / geometric denominator 极限。置 \(r_k=[kd^{-1}]_7\)，有
\(\chi(k+\ell d)=\chi(d)\chi(\ell+r_k)\)。而
\[
\sum_{\ell=0}^6\ell\chi(\ell+r)
=-7+7\sum_{j=0}^{r-1}\chi(j).
\]
在 r=0 时左边为−7，递推 r→r+1 的差恰 \(7\chi(r)\)，所以全部 r 已证明。\(1-\sum_{j<r}\chi(j)\) 就是 f。对 k=0，正倍数子级数为 \(\chi(d)T(\rho^d)\to\chi(d)\)，补齐(P5)。此处没有在 quotient ring 中对 \(z^d-1\) 作不合法微分。

置 \(h=(d-1)/2\)。对每个 unit u mod d 定义唯一 signed half-permutation：
\[
uk\equiv(-1)^{e_u(k)}P_u(k)\pmod d,\quad
1\le P_u(k)\le h,\quad e_u(k)\in\{0,1\},\quad1\le k\le h.
\]
记 \(P=P_b,e=e_b,x(k)=k\bmod2\)。由(P4)
\[
M_{b,d}=2L,\qquad L=\sum_{k=1}^h c_kP(k)\in\mathbf Z,
\quad \theta_{b,d}=1/8-L/d.                             \tag{P6}
\]

(P1) 给 \(a\equiv d^{-1}\pmod7\)、a 奇。对 \(1\le k\le h\)，置
\(r=[ak]_7\)、\(n=\lfloor ak/7\rfloor\)，则
\[
2b^2k=dn+(dr-k)/7.
\]
若 \(r>0\)，余项在 \((0,d)\)；若 r=0，余项在 \((-d,0)\)。因而
\[
\lfloor2b^2k/d\rfloor=n-\mathbf1_{r=0}.
\]
由(P5)，\(f(r)\equiv r+\mathbf1_{r=0}\pmod2\)，又 a 奇给
\(r\equiv k+n\pmod2\)，遂
\[
c_k\equiv x(k)+\lfloor2b^2k/d\rfloor
=x(k)+e_{b^2}(k)
=x(k)+e(k)+e(Pk)\pmod2.                                \tag{P7}
\]
中间等号：\(\lfloor2b^2k/d\rfloor\bmod2\) 恰普通残数 \(b^2k\bmod d\) 是否落入上半区的 sign；没有将 signed residues 当 ordinary residues。

## 3. commuting half-permutation 的完整奇偶恒等式

对任意两个 units u,v，直接从 signed representatives 得
\[
P_{uv}=P_uP_v,\qquad
e_{uv}=e_v+e_u\circ P_v\quad\text{in }\mathbf F_2.
\]
置 \(Q=P_2\)。因为 \(2k<d\)，unreflected 2k 为偶、reflected \(d-2k\) 为奇，故
\(e_2=x\circ Q\)。P、Q 交换，由 2b=b2 的 sign cocycle 得
\[
e\circ Q+e=e_2\circ P+e_2.
\]
置 \(v=x\circ P+x\)，于是
\[
\boxed{v=e+e\circ Q^{-1}.}                              \tag{P8}
\]

以下内积在 \(\mathbf F_2\)，\(|z|\) 是 binary vector 的普通整数 weight。
若两个 binary vectors z,z′ 有同 weight，并且 \(w=z+z'\)，则改变的1→0与0→1各有 \(|w|/2\) 个，所以
\[
\langle z,w\rangle\equiv |w|/2\pmod2.
\]
P、Q 都为 permutations。因此分别对
\((z,z')=(x,x\circ P)\)、\((e,e\circ Q^{-1})\) 应用，给
\[
\langle x,v\rangle=\langle e,v\rangle\pmod2.             \tag{P9}
\]
不能省略 equal-weight 条件；这里它由真实 permutations 支付。

从(P6)(P7)，变指标 P 后得到
\[
L\equiv\langle x,x\circ P\rangle+\langle e,v\rangle
\equiv |x|+\langle x,v\rangle+\langle e,v\rangle
\equiv |x|\pmod2.
\]
最终精确结论为
\[
\boxed{L\equiv \frac{h(h+1)}2
=\frac{d^2-1}{8}\pmod2.}                               \tag{P10}
\]
这是全部(P1)参数的证明；没有六类小 d 表或有限样本升格。

## 4. χ(d) 对应实际 Q+，从 parity 到每个完整返回叶

对每个奇素数 \(\ell\mid d\)，(P1) 使
\(14b^2\equiv-1\pmod\ell\)，所以
\[
(-14/\ell)=1,\qquad \chi(\ell)=(2/\ell).
\]
乘各 prime powers 得
\[
\chi(d)=(2/d)=(-1)^{(d^2-1)/8}.                         \tag{P11}
\]
最后一步是 Jacobi symbol 的2补充律；也可逐个 d mod8核其符号。没有使用错误的“所有正返回均属于一个指定 subgroup”量词。

若返回对应 Q+，则 \(\chi(d)=-1\)。由(P10)(P11)，L 为奇数，
\[
M_{b,d}=2L\equiv2\pmod4,\qquad
\theta_{b,d}=1/8-L/d\ne1/8.
\]
于是(P3)的整个补支条件不成立，无论 \(q_{b,d}\) 是不是0。结合(P1)覆盖所有 transported 返回的分类，支付
\[
\boxed{\text{正处 Q+ 两根，每个实际运输到达叶均保留非零完整 odd germ。}} \tag{P12}
\]

为明确普通点值与完整通道的区别：在
\(\zeta=(\tau-\tau_r)/(\tau-\bar\tau_r)\) 中 \(r\zeta=-\zeta\)，
\(j_r=\chi(d)(1+\zeta)/(1-\zeta)\)，
\(\widetilde A_+=A_+/(1-\zeta)\)。当 \(\chi(d)=-1\)，冻结250的精确身份是
\[
(B_{+,g})_{\rm odd}=(g_{r,+}-g)\widetilde A_+.
\]
\(\widetilde A_+\) 有 simple zero，(P12)使 coefficient 非零，因此首 odd 项是非零 \(\zeta\)，而 \(t-t_r\sim\mathrm{unit}\,\zeta^2\)。任意 transportation 只改变局部坐标的非零相位，不会取消该 sqrt 项。非零实周期差已足够，不要求整个 affine cocycle 虚部另有符号。

有符号 M 的正性反而不成立。例如纸面固定参数
\((d,b,a)=(19,2,3)\) 满足 \(ad-14b^2=1\)，(P5)直接给 L=−1，
所以 \(\theta=1/8+1/19\)。这只是一个精确校准例，说明新证书依赖奇偶而非正性；没有运行参数扫描。

## 5. 实际 genus0 lift；为何还不能领取全预算

设正处完整源共同拉回的合法 \(\phi:(\mathbb D,0)\to(\mathbf C,0)\) 全纯、非恒定。每个 \(\phi(z_0)\) 为 Q+ 根的到达叶都由(P12)不填。若 \(\operatorname{ord}_{z_0}(\phi-e)\) 为奇数，非零 sqrt 首项仍非 meromorphic。因此全部 \(Q_+(\phi)\) 零点阶数均偶数；单连通盘给唯一
\[
w_\phi^2=Q_+(\phi),\qquad w_\phi(0)=1,
\]
且 \(w_\phi\) holomorphic。这是实际合法图的必要条件，而不只是存在某个坏叶。

此曲线是 genus0，仍没有第三个 persistent branchpoint。置
\[
\alpha=(7-4s)/2\in(0,1),\quad\beta=\sqrt{1-\alpha^2}>0,\quad
Q_+(t)=(t-\alpha)^2+\beta^2.
\]
其 affine conic 在
\[
v=(t-\alpha+w)/\beta\in\mathbf C^\times,\quad
t=\alpha+\frac\beta2(v-v^{-1}),\quad
w=\frac\beta2(v+v^{-1})
\]
中显式为 \(\mathbf C^\times\)。对盘取 \(v=e^H\)，native
\(H_0=\log((1-\alpha)/\beta)\) 给
\[
\phi=\alpha+\beta\sinh H,\quad w=\beta\cosh H,\quad
\phi(0)=0,\quad w(0)=1,\quad \phi'(0)=H'(0).
\]
仅该部分覆盖条件允许 \(H=H_0+Mz\) 任意 M，给 entire \(\phi,w\) 与任意大的 derivative。它们**未认证为实际完整 B 源的合法图**；其它根、cusps 和 affine periods仍可能限制。故不能用这组必要条件反例否定实际全图 cap，也不能由(P12)直接宣布严格 CDT 预算可达。

尤其 native \(\sqrt{Q_+}\) 的首个系数 \(-7/2+2s\notin\mathcal O_K\)。本文没有支付其完整整类型，不按零费 rank2数组领取 \(J_+\ge2\lambda_+\)；其 coefficient-conjugate也不能免费搬到同一正图。真实原 frame rank3、安全两列均(0,1,1)、\(\tau=16/9\) 没有改变。

本轮 actual FULL 读取 B250 全文B1–B16，其负处 all-map提升、\(c_-<40/3\)、整数背景 \(J_-\ge2\lambda_-\) 已纸核。当前安全基本入口的必要条件仍为
\[
\lambda_+>4,\qquad \delta_+=3\lambda_+-J_+>8.
\]
(P12)支付正图新的全叶结构，尚未认证或排除这个剩余正处能量关。Q−的 native W 叶确实填；本文没有证明所有填叶 stabilizer恰为 \(\langle T,W\rangle\)，没有全群字分类、全 multi cap、primitive费用优化或其它整模型 no-go。数值目标仍 active；第252轮正式全局复盘不重置。

## 6. 实际读域、独立性与执行账

本轮 actual FULL 读三个冻结数学输入：
A250，10515 B/SHA256 94a9350f6da2408bdcae27ca7502292fe916b09156b81c3d3e9f646efdd88483；
C250，10946 B/SHA256 4ad6e536e8531c5d39caa03e7a35de13e37776dec96cc74d31c89800fd1ca3b7；
B250，10497 B/SHA256 f8ca50e7f185b00b2e40e215364c700dc34b60a8167f9859a8826f06ff61623f。
(P1)–(P4)与完整 odd gauge复用这些已证明输入；(P5)–(P12)是本文新增的自含全参数证书。

一次 bounded web search（两query）只读返回metadata/snippets，没有打开或下载其原文、采用 theorem或声称文献覆盖。随后纸证闭合，未扩检索；不是以检索未命中声明全球新颖。精确实际范围在本人的 NEW dual_reading_scope.md。

数学/CAS/producer/finiteprime/map/word/parameter/Lean运行0；新source GET/download0；外repo/Git mutation0。工具只进行文件读取、NEW Markdown写入和 hash。旧250、peer、Root、main、policy、manifest写0。两个独占输出写前已核不存在；作者保存后 actual FULL 复读并报告身份，作者读不冒充独立审核。

