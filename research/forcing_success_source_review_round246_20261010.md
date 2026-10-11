# 第246轮：成功周期源的实际 forcing 与背景恢复

日期：2026-10-10。独立纸面比较；数学程序、Lean执行、素数/参数扫描均为0。只新增本稿及本轮 packet reading scope，不改245、旧稿、主日志、manifest或外部仓库。本稿没有新的数值无理性/线性无关定理。

## 1. 两个可检验的非恢复判据

令 \(K=\mathbb C(x)\)，\(\partial=d/dx\)，对实际解析芽 \(H\) 定义
\[
\mathcal D^{\rm aff}(H)=K+K[\partial]H.
\tag{F1}
\]
这里比较的是实际函数空间，不能仅比较某个已知方程的右端。

**局部判据。** 如果沿同一基点路径，\(H\) 在一点 \(\beta\) 亚纯，而 \(A\) 在该点不亚纯，则
\[
A\notin\mathcal D^{\rm aff}(H).
\tag{F2}
\]
证明：亚纯函数的全部导数和有理系数线性组合仍亚纯。等价的单值必要条件是：若 \(A=RH+r\)，\(R\in K[\partial]\)、\(r\in K\)，则任何基点闭路 \(T\) 满足
\[
(T-1)A=R(T-1)H.
\]
所以一个 \(H\) 局部无跳跃、\(A\) 有跳跃的闭路足以否定恢复；反向包含关系本身不是充分条件。非恒定全纯图 \(\phi\) 上，\(\partial_x=(\phi')^{-1}\partial_u\)，临界点只引入亚纯极点；因此实际恢复公式也会把 \(H\circ\phi\) 的亚纯性传给 \(A\circ\phi\)。不领取非恢复本身给出的任何容量收益。

**不可约有理 forcing 判据。** 设 \(L\in K[\partial]\) 不可约，阶 \(r>1\)，\(LA=0\)、\(A\ne0\)，且 \(LH=q\in K^\times\)。若 \(A\in\mathcal D^{\rm aff}(H)\)，则必存在 \(R_0\in K\) 满足
\[
LR_0=q.
\tag{F3}
\]
证明：\(M=K[\partial]H\) 已含 \(1=q^{-1}LH\)，且方程给出 \(\dim_K M\le r+1\)。\(V=K[\partial]A\) 是秩 \(r\) 的不可约微分空间；因为 \(r>1\)，\(V\cap K=0\)。恢复假设给出 \(V\subseteq M\)，于是 \(M=V\oplus K\)。写 \(H=v+R_0\)，则 \(Lv=q-LR_0\in V\cap K=0\)，得到(F3)。因此实际无有理特解是非恢复的充分条件；不把有理特解存在说成恢复指定 \(A\) 的充分条件。本判据要求实际不可约性，不能从一个方程的名称或形式继承。

有理 forcing 单独不够。例如 \(\theta=x\partial\)，
\[
A=-\log(1-x),\quad B=\operatorname{Li}_2(x),\quad
\theta B=A,\quad \theta^2B=r(x):=\frac{x}{1-x}.
\]
对任意固定常数 \(g\)，令 \(H_g=B+gA\)。则
\[
q_g:=\theta^2H_g=r+g\theta r
 =\frac{x(1-x+g)}{(1-x)^2}\ne0,\qquad
A=\theta H_g-g\,r\,q_g^{-1}\theta^2H_g.
\tag{F4}
\]
即使二阶右端有理，全部 \(H_g\) 都恢复这个对数背景。这是实际恢复反例，没有借用数值猜测。

## 2. CDT \(\chi_{-3}\)：两个数值响应、一个局部 jump 行

本轮实际读当前218页作者PDF物理159–169。以下采用其中§11.1完整陈述/证明与积分身份；并非本轮重新证明全部模块恒等式、14函数独立性或CDT能量定理。设 \(\eta=L(2,\chi_{-3})\)，\(x(q)=q-4q^2+\cdots\)，作者源为
\[
H_A(x)=A(q(x)),\qquad H_B(x)=H_A(x)B(q(x)),\qquad
H_C(x)=H_A(x)C(q(x)).
\]
这里 \(A\) 是权1 Eisenstein形式；两个 Eichler 响应的完整级数为
\[
B(q)=\sum_{n\ge1}\frac{\chi_{-3}(n)q^n}{n^2(1+q^n)},\qquad
C(q)=\frac14\sum_{n\ge1}\chi_{-3}(n)
             \bigl(4\operatorname{Li}_2(q^n)-\operatorname{Li}_2(q^{2n})\bigr).
\tag{F5}
\]
作者给出的 Abel 极限是真正数值桥：
\[
B(q)\longrightarrow \frac{\eta}{2},\qquad
C(q)\longrightarrow\frac{\zeta(2)}4=\frac{\pi^2}{24}
\quad(q\to1^-).
\tag{F6}
\]
第二个极限要用字符部分和的 Abel/Cesàro处理，不能把不收敛的 \(\sum\chi_{-3}(n)\) 当普通求和。它是 \(\pi^2\) 通道，绝不是第二个尚未知 \(L\) 值。

令
\[
L=x(1-x)(1-9x)\partial^2+
  (1-20x+27x^2)\partial+3(-1+3x).
\]
完整系数初值 \(H_A=1+3x+\cdots,\ H_B=x+\cdots,\ H_C=x+\cdots\) 给出
\[
LH_A=0,\qquad LH_B=1,\qquad LH_C=\frac1{1-x}.
\tag{F7}
\]
例如 \(H_B\) 的递推在 \(n\ge1\) 齐次，但 \(n=0\) 的 \(b_1=1\) 正是右端1，不能丢掉；\(H_C\) 每层右端均为1。

两个真正填平的组合是
\[
P_\chi=\eta H_A-2H_B,\qquad P_2=\zeta(2)H_A-4H_C.
\tag{F8}
\]
它们在 \(\beta=1/9\) 全纯。对第一式，作者(11.1.16)给出
\[
P_\chi(x)=\iint_{[0,1]^2}
\frac{1+st+s^2t^2}
{(1+st+s^2t^2)^2-9st(1-s^3)(1-t^3)x}\,ds\,dt.
\tag{F9}
\]
可独立纸核完整峰值：设 \(u=\sqrt{st}\)，则
\[
(1-s^3)(1-t^3)\le(1-u^3)^2,\qquad
1+u^2+u^4-3u(1-u^3)=(2u-1)^2(u^2+u+1)\ge0.
\]
所以分母写成 \((1+st+s^2t^2)^2(1-\rho x)\)，\(0\le\rho\le1\)。在 \(\mathbb C\setminus[1,\infty)\) 的紧集上统一有界并可逐次积分，直接支付该域上的全纯性。

第二式不是无来源的类比。作者(11.1.14)先在
\[
G_A(v)=\frac1{1+v}H_A\!\left(\frac v{1+v}\right),\quad
G_C(v)=\frac1{1+v}H_C\!\left(\frac v{1+v}\right)
\]
给出
\[
\zeta(2)G_A(v)-4G_C(v)
=\iint\frac{ds\,dt}{1-st+v(1-s^2)(1-t^2)}.
\]
代 \(v=x/(1-x)\) 得到实际 \(P_2\)，其在 \(\beta\) 的全纯性及完整单位盘续接也由已读Lemma11.1.4支付。

\(H_A\) 的半径为 \(1/9\)，ODE除0、\(1/9\)、1、\(\infty\)无奇点，因此它在 \(\beta\) 不全纯。记 \(t=x-\beta\)，最高两项系数是
\[
x(1-x)(1-9x)=-\frac89t+O(t^2),\qquad
1-20x+27x^2=-\frac89+O(t).
\]
若有极点 \(a t^{-k}\)、\(k>0\)，\(LH_A\) 的最低项为
\(-\frac89 k^2a\,t^{-k-1}\ne0\)。所以它也不可能亚纯；局部重指数0产生非零对数 jump。由(F2)，
\[
H_A\notin\mathcal D^{\rm aff}(P_\chi),\quad
H_A\notin\mathcal D^{\rm aff}(P_2).
\tag{F10}
\]
这是真的不恢复，未以“某方程右端不含 \(H_A\)”代替证明。

在同一个 \(\beta\) 小闭路，两个响应给出的是**一个** jump 行：
\[
(\Delta H_A,\Delta H_B,\Delta H_C)
=\Delta H_A\left(1,\frac\eta2,\frac{\pi^2}{24}\right).
\tag{F11}
\]
因此假设有非零有理关系
\[
a+b\eta/2+c\pi^2/24=0
\]
时，实际 \(H=aH_A+bH_B+cH_C\in\mathbb Q[[x]]\) 填平 \(\beta\)，
\[
LH=b+\frac c{1-x}\ne0,\qquad d_n^2[x^n]H\in\mathbb Z
\]
在固定清 \(a,b,c\) 分母后成立。非零关系必有 \((b,c)\ne(0,0)\)，故 \(H\ne0\)，而且 \(H_A\notin\mathcal D^{\rm aff}(H)\)。第二响应确实接到数值 \(\pi^2\)，但(F11)不是两个独立局部跳跃，不能单凭一行消失就证明三数Q-LI。

作者实际Q-LI还用对称化
\(G(y)=H(x)+H(x/(x-1))\)，分母 \(d_{2n}^2\)，以及由 \(G,G',G'',G'''\) 和三个积分生成的7函数，连同另7个纯函数的独立性和同对象算术能量。这里已读§12.1的完整Lemma12.1.1陈述及证明开端，不声称本轮核完其后全部证明或§13预算。作者成功是这个完整接口；旧结果 \(1,\pi^2,\eta\) Q-LI不能免费成为新level7数值出口。

## 3. Catalan：标量恢复仍在，成功投影发生在整个列池

本轮FULL读已存仓库 foundations.tex，包含完整边界递推、周期分解、整数行/列contact及2-adic估计正文。这里只独立采用并重算前者，不领取其余章的无限非零或净能量。

设 \(c_l=4^{-l}\binom{2l}{l}\)，\(K^-_d=M(d,0)\)，
\[
m_i=\int_{-1}^1t^i\frac{|t|}{\sqrt{1-t^2}}dt,\qquad
dK^-_d=(d-1)K^-_{d-2}+m_{d-2}+m_{d-1}\quad(d\ge2),
\]
\(K^-_1=2,\ K^-_0=4G\)。用完整理性初值 \(k^-_0=0,\ k^-_1=2\)，定义
\[
K_g(x)=\sum_{d\ge0}k^-_d x^d+
               \frac{4g}{\sqrt{1-x^2}},\qquad
\mathcal M(x)=\sum_{i\ge0}m_i x^i
 =\frac{2\arcsin x}{x\sqrt{1-x^2}}.
\]
把 \(d=1\) 初值与 \(m_0=2\) 都保留后，递推求和精确给出
\[
\mathcal C_0K_g=x(1+x)\mathcal M,\quad
\mathcal C_0=(1-x^2)\theta-x^2,
\qquad
\mathcal C_1\mathcal M=2,\quad
\mathcal C_1=(1-x^2)\theta+1-2x^2.
\tag{F12}
\]
因此这个标量源有有理 forcing
\(\mathcal C_1[x(1+x)]^{-1}\mathcal C_0K_g=2\)，却恢复整个反三角函数背景 \(\mathcal M\)，对所有 \(g\) 都如此。实际 \(g=G\) 恢复原始 \(K^-_d\) 数值矩；不把此标量恢复说成已公布Catalan矩阵方法的反证。

成功方法的明确对象是增长列池。其完整分解为
\[
M(i,j)=M^0(i,j)+4G\,c_{(i-j)/2}
                 +\tfrac32\zeta(2)c_{(j-i-1)/2},\qquad
Z(i,j)=Z^0(i,j)+[i=j]\zeta(2).
\tag{F13}
\]
非负整数以外的 \(c\) 为0，\(M^0,Z^0\) 包括全部有限调和头。整数行 \(P_r,D_r\) 满足
\[
\frac{tP_r}{\sqrt{1-t^2}}-D_r=O(t^L).
\]
对**全部** \(b\le j<L\)，
\[
F_j(r)=M(P_r,j)-\tfrac32 Z(D_r,j)
       \in\mathbb Q+\mathbb QG
\tag{F14}
\]
因为 \(\zeta(2)\) 系数恰为
\(\frac32[t^j](tP_r/\sqrt{1-t^2}-D_r)=0\)。整数有限差分列filter用到的列全在该contact范围内。因此 \(G\in\mathbb Q\) 真正理性化同一个完整矩阵；这与只删掉标量微分闭包中的背景行不同。投影支付后仍须同一矩阵的全部素数费用、无限非零和能量；本轮不移植已有常数或数值定理到别的导子/权。

## 4. 未付数值出口：\(c_4\) 的恢复桥与 odd-zeta 边界

本轮FULL读236边界稿和235实际源稿；它们没有支付
\[
c_4=\beta(4)-\frac{\pi^2G}{8}
\]
的数值无理性或 \(1,c_4\) Q-LI。此处只说现有记录/已读结果没有给出该结论，不声称全球首次或完成全局新颖性检索。

已付的实际 \(q\)-源 \(D,B,P,S\) 满足，记
\(\alpha=(q-2)/(q(q-4))\)，
\[
D'=\alpha D-1,\quad
B'=-\frac{2D}{q(q-4)},\quad
P'=\alpha P-3B,\quad
S'=\frac S{2q}-\frac P{q(q-4)},\qquad S(4)=-192c_4.
\]
这立即给出完整恢复：
\[
P=q(q-4)\!\left(\frac S{2q}-S'\right),\quad
B=\frac{\alpha P-P'}3,\quad
D=-\frac{q(q-4)}2B',\quad 1=\alpha D-D'.
\tag{F15}
\]
所以改名 \(S+192g\)、只保留标量目标行，不能删除它的实际背景闭包。236已经另付固定 rational filter 在 \(q=4\) 的对数障碍；本文不把这个局部阻碍扩成所有混合周期源no-go。可研究的新桥必须先给整个新混合系数stack：保留 \(c_4\) 目标rank、消去其它周期，并付完整有限头，而不是仅宣称“更高权Eichler积分”。

仓库 odd-zeta 记录也不能补这个缺口。本轮只完整选读 Deligne–Drinfeld 源§7末段“A nonzero depth-one value”的命题和证明：其实际公式
\[
[x^{n-1}y]\Phi=-(2\pi i)^{-n}\zeta(n),\qquad
[x^{n-1}y]\delta_n(\alpha)=2(2\pi i)^{-n}\zeta(n)\ne0
\quad(n\ge3\text{ odd})
\]
使用的是 \(\zeta(n)>0\)，作者明确不主张这些数的算术独立性。形式生成元非零不提供某个新 \(\zeta/L\) 关系的完整整系数芽、filled域或费用。没有运行Lean或重审整篇DD证明。

## 5. 本轮准入决定

保留两个有实效的首关：(i) 新直接holonomy源的实际关系组合，要以(F2)或(F3)支付**不恢复**所限制的背景，再支付完整整模型/图；(ii) 采用混合矩阵时，先支付(F13)–(F14)式的整个周期系数投影及目标rank，允许标量背景仍恢复。两种接口不能互相免费替换。

停止把 \(LB\in\mathbb Q(x)\)、形式odd-zeta生成元、标量改名或某一个原生端点等式当新数值入口。CDT的 \(\pi^2\) 响应说明构造第二个有理 forcing 可以有真正数值意义，但还须另证该响应的实际endpoint与新目标，而不是从旧三数Q-LI继承。并行level7候选的数值身份、不可约性及状态由其独立稿负责，本文不把消息当已读primary。当前可继续的第一门槛是一个完整、可复核的实际period stack或无有理特解/填平非恢复证书；本稿没有新数值结论。

实际读域、版本和不读取的范围见本轮 packet_reading_scope.md。
