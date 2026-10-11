# 第253轮：真实RV系数、正实零点与全n cyclotomic满秩

2026-10-10。Root独立推导。固定252选择的包，不做n头、参数、素数或CAS扫描：n≥2、r=0,…,4，参数为$(10n+r,8n,8n,5n,10n)$，共同归一化为$\Lambda_nz^{16n}(z-1)^{3n}$，$\Lambda_n=d_{13n+4}d_{12n+4}$。实际原始输入是Rhin–Viola2005的(2.3)双留数及Theorem2.1；本轮FULL读现存物理4–6、17–21选段，不冒称全部49页证明。

**首四列的真实余数矩阵对每个n≥2满秩4**。因此252未付的非零常数intersection已全部支付。下文同时给一个少付公共LCM的整数投影与安全向量高度。没有支付目标值处形式的实际非零、primitive最优费用或原复杂积分的strict余量；没有新的数值无理性定理。

## 1. 从原双留数到全系数公式

记$H=10n+r$，$p=6n+1$。原文内层留数在$y=x/(x-z)$。令$u+v=6n$，Leibniz公式给

\[
 \operatorname{Res}_y\frac{y^{8n}(1-y)^{5n}}
 {[x+(z-x)y]^{6n+1}}
 =\frac{\sum_{u=n}^{6n}\binom{8n}{u}\binom{5n}{6n-u}
                  x^{8n-u}z^{u-n}}{(z-x)^{13n+1}}.
 \tag{1}
\]

内层符号为$(-1)^{8n-u+v}=(-1)^{14n-2u}=1$，上下界来自$v\le5n$与$u\le6n$。再乘原$x^{8n}(1-x)^H z^{-15n}$并取$x=z$的外层留数；外层符号是$(-1)^{13n+1}=(-1)^{n+1}$。Theorem2.1的实际周期系数因此是

\[
 Q_{n,r}(z)=\Lambda_n R_{n,r}(z),\quad
 R_{n,r}(z)=(-1)^{n+1}z^{3n}(z-1)^{3n}
 \sum_{t=0}^{H}(-1)^t\binom Ht W_n(t)z^t,
 \tag{2}
\]
\[
 W_n(t)=\sum_{u=n}^{6n}\binom{8n}{u}\binom{5n}{6n-u}
                         \binom{16n-u+t}{13n}.
 \tag{3}
\]

这里来自$[w^{13n}](z+w)^{16n-u}(1-z-w)^H$，不是把一般Padé系数贴到本对象。对于所有整数$t\ge0$，(3)是整数，故$R_{n,r}\in\mathbb Z[z]$；$\deg R_{n,r}\le16n+r$。完整$P_{n,r}$仍由原定理的$\Lambda_n$清整，不能因此把整个$P-Q\mathrm{Li}_2$的LCM删去。

## 2. 一个自含的有限和闭式证明

将(3)视为t的13n次多项式。定义

\[
 T_n(t)=\prod_{j=2n+1}^{10n}(t+j)
         \prod_{j=3n+1}^{8n}(t+j).
\]

则

\[
 W_n(t)=\frac{T_n(t)}{(6n)!(7n)!}. \tag{4}
\]

证明不需要有限计算。第一，对$2n+1\le s\le10n$，每个上指标$16n-u-s$都在$0,\ldots,13n-1$，所以$W_n(-s)=0$。

第二，对$3n+1\le s\le8n$，令$\ell=16n-u-s$。广义二项式多项式在其简单根处导数为

\[
 \left.\frac d{dt}\binom{16n-u+t}{13n}\right|_{t=-s}
 =\frac{(-1)^{13n-1-\ell}\ell!(13n-1-\ell)!}{(13n)!}.
\]

用Beta积分及Leibniz公式整理，恰有

\[
 W_n'(-s)=\frac{(-1)^{s-3n-1}}{(6n)!}
 \int_0^1 x^{8n-s}(1-x)^{s-2n-1}
       \partial_x^{6n}[x^{8n}(1-x)^{5n}]\,dx. \tag{5}
\]

Leibniz式的具体组合是

\[
 \frac{(1-x)^n}{(6n)!}\partial_x^{6n}[x^{8n}(1-x)^{5n}]
 =\sum_{u=n}^{6n}(-1)^u\binom{8n}{u}\binom{5n}{6n-u}
                       x^{8n-u}(1-x)^u.
\]

在(5)，test多项式$g=x^{8n-s}(1-x)^{s-2n-1}$的degree是6n−1。在0，原被微分多项式$f=x^{8n}(1-x)^{5n}$的8n重零消掉全部6n次分部积分边界；在1，若$f^{(6n-1-j)}(1)$未由5n重零消掉，则$j\le n-1$，而$g$在1至少n重零，故$g^{(j)}(1)=0$。所有边界项因此为零，$g^{(6n)}=0$，得到$W'_n(-s)=0$。

最后，$W_n$的leading系数是
$\binom{13n}{6n}/(13n)!=1/[(6n)!(7n)!]$，由普通Vandermonde求和得到。8n个已付根与中间5n个额外重数总共13n，恰等于degree，证明(4)。A另给了直接交错Vandermonde版本，B/C独立检查本Beta版本；不以互相转发消息代替保存稿的审阅。

## 3. 正实根保持引理与真实秩

令$\theta=z\partial_z$。由(2)–(4)，

\[
 Q_{n,r}(z)=\frac{(-1)^{n+1}\Lambda_n}{(6n)!(7n)!}
 z^{3n}(z-1)^{3n}\,T_n(\theta)(1-z)^{10n+r}. \tag{6}
\]

**引理。** 对$a>0$与非零实多项式f，$(\theta+a)f$保持degree，且按重数计的正实根总数至少与f相同。单项式系数乘$k+a>0$，所以算子在多项式空间可逆且leading非零。对根数，设正根$x_1<\cdots<x_s$，重数$m_i$。函数$z^af(z)$在0连续且值为0；导数为$z^{a-1}(\theta+a)f$。每个根保留$m_i-1$个重数，$(0,x_1)$有一个Rolle根，各内部间隙有$s-1$个，合计$\sum_i m_i$。不要求$z^af$在0可微；只需每个开区间可微。

所有$T_n$因子中的$j>0$，故引理可逐项使用。设首四列存在非零实常数关系，模$\Phi_8=z^4+1$输出为0。把输入写为

\[
 \sum_{r=0}^3v_r(1-z)^{10n+r}=(1-z)^{10n}p(z),
 \quad p=\sum_{r=0}^3v_r(1-z)^r\ne0,\quad\deg p\le3.
\]

输出$T_n(\theta)[(1-z)^{10n}p]$非零，degree≤10n+3，且至少有10n个正实根。公共$z^{3n}(z-1)^{3n}$模$\Phi_8$是单位，常数也非零，故输出必须被$\Phi_8$整除。这会另外产生四个不同非实根，总degree至少10n+4，矛盾。

因此实际4×4余数矩阵在$\mathbb R$上可逆，尤其在$\mathbb Q$上满秩4；后三行秩3。第五列不需要参与这个证明，仍留在同一固定包。此证明直接支付252的rank严格差，不是generic span或微分方程阶数猜测。

这个根数论证本身还有一般形式：若实算子$\prod(\theta+a)$全部$a>0$，输入$(1-z)^H p_{d-1}$，则对degree d且全部非实根的实多项式Ψ，其前d个移位余数满秩；公共因子须模Ψ为单位。这里只应用已固定Φ8，不借一般命题另开新包或数值目标。

## 4. 完整整数投影及一个有界高度证书

令$\widehat M_n\in\mathrm{Mat}_4(\mathbb Z)$的第r列是$R_{n,r}\bmod\Phi_8$的0,…,3系数，r=0,…,3。取

\[
 \widehat\Delta_n=\det\widehat M_n\ne0,\qquad
 (v_{n,0},\ldots,v_{n,3})^t=\operatorname{adj}(\widehat M_n)e_0,
 \qquad v_{n,4}=0.
 \tag{7}
\]

则完整$Q_n=\sum_rv_{n,r}Q_{n,r}$满足
$Q_n\equiv c_n=\Lambda_n\widehat\Delta_n\ne0\pmod{\Phi_8}$。使用$R$的adjugate避免人为把$\Lambda_n^3$塞入v；但整体$P_n$仍带一次Λ，所有清整对象显式保留。252的canonical Gauss trace给

\[
 \tau_\chi^{-1}\sum_{a=1,3,5,7}\chi(a)
 \sum_rv_{n,r}F_{n,r}(\zeta^{-a})=A_n-c_nY,
 \quad A_n,c_n\in\mathbb Z,\quad c_n\ne0,
 \tag{8}
\]

其中$\tau_\chi=i\sqrt8$，$Y=L(2,\chi_{-8})$，$A_n=-\sum_k[P_n]_k\chi(k)$。没有额外conductor清整因子。

一个全n、非最优的安全高度也可立即给出。(3)的正权重和为$\binom{13n}{6n}\le2^{13n}$，且$t\le10n+r$时二项式上指标≤25n+r，故$W_n(t)\le2^{38n+r}$。于是

\[
 \|R_{n,r}\|_1\le2^{3n+10n+r}2^{38n+r}
                       =2^{51n+2r}\le2^{51n+8}=:E_n.
\]

按指数模4折叠只会把系数带符号相加，余数每个系数绝对值≤E_n。3×3 cofactor与4×4 determinant分别给

\[
 \max_r|v_{n,r}|\le6E_n^3,\qquad
 |\widehat\Delta_n|\le24E_n^4. \tag{9}
\]

这是已支付的O(n)对数高度upper，包括完整向量，非primitive最优费用；没有从这份很粗upper推出strict或方法不可能。完整$A_n$的共同内容、$c_n$与v约分后的实际增长尚未分析。

## 5. 完整对数修正与同对象的一维实积分

还可从原定义确定完整P，而不是只保留周期列。固定n,r，令实z≥2。原$I^{(0)}$中$D=x(1-y)+yz\ge yz$，于是$y^{8n}/D^{6n+1}$被$z^{-6n-1}y^{2n-1}$控制，后者可积。包含原$z^{-15n}$得到

\[
 I^{(0)}_z=O(z^{-21n-1}).
\]

由(1)，$I^{(1)}_z$的每项含$z^{-15n}z^{u-n}(z-x)^{-13n-1}$、$u\le6n$，而x∈[0,1]、z≥2，所以

\[
 I^{(1)}_z=O(z^{-23n-1}).
\]

这些是每个固定n的∞行为，常数允许依赖n；不声称uniform energy。乘共同$z^{16n}(z-1)^{3n}$后，完整修正泛函

\[
 F_{n,r}=P_{n,r}-Q_{n,r}\operatorname{Li}_2(1/z)
 =O(z^{-2n-1})+O((\log z)z^{-4n-1})\longrightarrow0.
\]

因此P恰等于$Q\operatorname{Li}_2(1/z)$在∞的多项式部。使用

\[
 \operatorname{Li}_2(1/z)=\int_0^1\frac{-\log t}{z-t}\,dt,
 \qquad z\in\mathbb C\setminus[0,1],
\]

以及$Q(z)-Q(t)$除以$z-t$，得到精确完整式

\[
 P(z)=\int_0^1(-\log t)\frac{Q(z)-Q(t)}{z-t}\,dt,
 \qquad F(z)=-\int_0^1\frac{(-\log t)Q(t)}{z-t}\,dt.
 \tag{10}
\]

原real z>1域上的相等式确定同一canonical延拓，八次单位根都在该slit域内。故(10)包含原$I^{(0)}-(\log z)I^{(1)}$的全部修正；没有丢掉复杂contour项再给它一个免费的正核小界。

对整数投影后的Q_n同样成立。有限Gauss和及绝对收敛给

\[
 \tau_\chi^{-1}\sum_a\frac{\chi(a)}{\zeta^{-a}-t}
 =\frac{1+t^2}{1+t^4},\qquad 0\le t<1.
\]

于是完整实际线性式有一个同对象的实积分载体：

\[
 A_n-c_nY=-\int_0^1(-\log t)Q_n(t)
                       \frac{1+t^2}{1+t^4}\,dt.
 \tag{11}
\]

若$Q_n=c_n+(1+t^4)S_n$，则$S_n\in\mathbb Z[t]$且

\[
 A_n=-\int_0^1(-\log t)(1+t^2)S_n(t)\,dt
 =-\sum_k[S_n]_k\left((k+1)^{-2}+(k+3)^{-2}\right).
 \tag{12}
\]

(12)与已付整数Gauss身份相同，不能单独把各分数头的LCD当primitive费用。由∞阶还可得完整正交条件

\[
 \int_0^1(-\log t)t^jQ_{n,r}(t)\,dt=0,
 \qquad j=0,\ldots,2n-1. \tag{13}
\]

最后，(10)逐系数写为$P_j=\sum_{k>j}Q_k/(k-j)^2$，故$\|P\|_1<2\|Q\|_1$。结合(7)–(9)，全模型具有明确但很粗的安全界

\[
 \|Q_n\|_1\le24\Lambda_nE_n^4,
 \|P_n\|_1\le48\Lambda_nE_n^4,
 |A_n|\le48\Lambda_nE_n^4,
 |c_n|\le24\Lambda_nE_n^4. \tag{14}
\]

这是一次完整A/c高度upper与实积分身份，不是净衰减估计。真正的primitive pair仍须除$\gcd(A_n,c_n)$并分析同一(11)。

## 6. 与目标及资源判断的边界

(8)的$c_n\ne0$不意味着$A_n-c_nY\ne0$。假设Y有理时可能实际形式为0，因此仍需关系点无界非零。(11)的测度正，但Q_n不保证常号；不能据此宣布实际线性式非零。完整canonical载体已由(10)支付，primitive内容与(11)的统一净衰减仍未给strict余量。

本轮确实改变了首关：全n满秩、整数向量、安全全高度和包含全部对数修正的一维实载体均已支付。它只允许重新评估下一项完整预算，不自动重开长期map/prime/参数窗口。主目标仍是新的数值ζ/L定理；此处未实现。
