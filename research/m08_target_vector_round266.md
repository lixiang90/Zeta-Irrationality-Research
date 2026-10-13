# 第266轮：完整M₀,₈向量的安全模型与源核查停止

2026-10-13。[任务窗口](m08_target_vector_charter_round266_20261013.md)限一轮。本轮给出直接Barnes全素数幂安全模型、下降归一化纠错及群信用的精确范围，**没有新的无理性定理，也没有通过数值实施准入**。上一轮265完成正式来源比较，属于progress；本轮不是重跑263–264或K5。

固定 $X=3\zeta(3)+\zeta(5)$、$a=(8,16,10,15,12,16,18,13)n$，沿用[265](source_selection_round265.md)的canonical
$$
 E_n=Q_nX-R_n,\qquad R_n=P_n+3\widehat P_n,\qquad
 I_n=2Q_n\zeta(5)+4Q_n\zeta(2)\zeta(3)-2P_n-4\widehat P_n\zeta(2).
 \tag{1}
$$
以下直接模型以一手稿(4)的**同一graded系数识别**为来源输入；不靠未知的实数跨权线性无关性辨认系数。本轮没有从头重证非对称族所有额外权的抵消或完整cohomology。原件是[Brown–Zudilin v3](https://arxiv.org/pdf/2210.03391v3)，本地[冻结PDF](../literature/brown_zudilin_cellular.pdf)保持不变。

## 1. 先修归一化，不能直接移交印出的下降式

原PDF14的(22)写 $I''=\sum_k C_kJ_{3,k}$，同页又写 $J_{3,k}=2A_k\zeta(3)-B_k$。其中
$$
 C_k=(-1)^{p_4+p_5+p_6+k}
 \binom{k}{p_6}\binom{q_4}{k-p_4}\binom{q_5}{k-p_5}.
$$
把该页 $A_k$ 双和代入后，外符号为 $(-1)^{\sum p_i}$，第三binomial的下标为 $p_3+q_3-p_0-p_6$，上标为 $j+k+q_3-p_0-p_6$；与原(17)逐项一致。因此 $\sum C_kA_k=Q_n$，印出的下降和的ζ3系数是 $2Q_n$。

$n=0$ 更直接：原(23)积分先积 $y_3$，再用非负级数得到
$$
 J_3(0)=\int_{[0,1]^2}\frac{-\log(y_1y_2)}{1-y_1y_2}\,dy_1dy_2
 =2\sum_{r\ge1}r^{-3}=2\zeta(3),
$$
而canonical $I''_0=\zeta(3)$。原页已视觉核对，缺因子不是OCR错误。

一致的下降候选必须是 $2I''=\sum C_kJ_{3,k}$、$\widehat P_{\rm des}=\frac12\sum C_kB_k$。**系数匹配本身不证明其常数项与canonical $\widehat P$ 相等**；伴随cycle的归一化桥仍需另付。本文清整不借这条未独证的桥。

原PDF11的Mellin表达还少印一个符号：
$$
 \int_0^1u^{t+k-1}(\log u)^{\alpha-1}du
 =(-1)^{\alpha-1}\Gamma(\alpha)/(t+k)^\alpha.
$$
故两变量基本积分的log表达须乘 $(-1)^{\alpha+\beta-2}$。下文保留此符号；它不改变费用，但改变完整有理向量。两项纠错不覆盖原PDF或265的历史证据。

## 2. 实际double-Barnes核及部分分式费用

在原(16)令 $s=t_1-14n-1$、$t=t_2-12n-1$，两条新线均取实部1/3。对应 $c_1=14n+2/3,c_2=12n+2/3$，符合原约束；交叉Gamma的实部分别为 $3n+2/3,9n+1/3$。反射公式给
$$
 I_n=\frac1{(2\pi i)^2}\int\!\int\mathscr R_n(t_1,t_2)
 \frac{\pi}{\sin\pi t_1}\frac{\pi}{\sin\pi t_2}
 \frac{\pi}{\sin\pi(t_1+t_2)}\,dt_1dt_2,
$$
$$
 \mathscr R_n=(-1)^n\frac{(8n)!(16n)!}{(12n)!}
 \frac{\prod_{r=1}^{14n}(t_1-r)\prod_{r=1}^{12n}(t_2-r)
       \prod_{r=-9n}^{3n-1}(t_1+t_2+r)}
 {\prod_{k=n}^{15n}(t_1+k)\prod_{k=2n}^{14n}(t_1+k)
  \prod_{\ell=6n}^{14n}(t_2+\ell)\prod_{\ell=n}^{17n}(t_2+\ell)}.
 \tag{2}
$$
区间含端点。每一变量单独趋无穷时至少是 $O(t_j^{-2})$，所以没有polynomial part：
$$
 \mathscr R_n=\sum_{k=n}^{15n}\sum_{\ell=n}^{17n}
 \sum_{\alpha,\beta=1}^2
 \frac{c_{k\ell}^{\alpha\beta}}{(t_1+k)^\alpha(t_2+\ell)^\beta}.
 \tag{3}
$$
令 $d_N=\operatorname{lcm}(1,\ldots,N)$、$d_0=1$。有全素数幂结论
$$
 d_{15n}^{\,2-\alpha}d_{16n}^{\,2-\beta}
 c_{k\ell}^{\alpha\beta}\in\mathbb Z.
 \tag{4}
$$
证明：将(2)写为 $(-1)^nA(t_1)B(t_2)C(t_1+t_2)$，$C(z)=\binom{z+3n-1}{12n}$。$A,B$ 是原整数值polynomial $(s+1)_{p_0}/p_0!$ 或 $(t+1)_{p_6}/p_6!$ 乘两项 $q!/(s+p+1)_{q+1}$。后者的简单留数为整数binomial；双极点的二阶系数因此整数。其一阶项增加polynomial导数和另一factor的regular part，分别由 $d_{15n}$、$d_{16n}$ 清除：原pole之间距离最多15n、16n，regular part是整数留数除这些距离的和。单极点处同样适用，不能漏掉小素数。

整数值binomial的有限差分展开还给 $d_{12n}^j[x^j]C(z+x)\in\mathbb Z$，$j=0,1,2$、整数z；一次系数分母为j，二次系数为 $H_{j-1}/j$。展开两个Laurent因子和C至 $xy$ 项即得(4)。不存在未计的factorial分母。对每个p，(4)等价于
$$
 v_p(c^{\alpha\beta})\ge
 -(2-\alpha)\lfloor\log_p(15n)\rfloor
 -(2-\beta)\lfloor\log_p(16n)\rfloor.
$$

## 3. 基本积分的有限尾与完整两坐标安全清整

记原PDF11基本积分为 $I_{k\ell}^{\alpha\beta}$、$w=\alpha+\beta+1$、$N=k+\ell$。以下证明它的weight0有理部分r和单独weight2的ζ2系数z满足
$$
 d_N^wr_{k\ell}^{\alpha\beta}\in\mathbb Z,\qquad
 d_N^{w-2}z_{k\ell}^{\alpha\beta}\in\mathbb Z.
 \tag{5}
$$
在 $u<v$ 令 $u=xv$，使用原f(u,v)并先合并两个harmonic发散项。该半域的解析生成式为
$$
 T(k+\epsilon,\ell+\eta)=
 \sum_{m=k+1}^\infty\frac{H_{m+\ell}^{(1)}(z)-H_N^{(1)}(z)}{(m+\epsilon)^2}
 -\sum_{m=k+1}^\infty\frac{\zeta(2,1+z)-H_{m+\ell}^{(2)}(z)}{m+\epsilon},
 \quad z=\epsilon+\eta,
 \tag{6}
$$
其中 $H_j^{(s)}(z)=\sum_{h=1}^j(h+z)^{-s}$，这里 $\zeta(2,1+z)$ 为Hurwitz ζ。生成式来自 $\sum_{b\ge0}((N+1+z+b)^{-1}-(m+\ell+1+z+b)^{-1})$ 的有限差。对ε、η各求至一阶导数，再加交换k、ℓ的半域，并乘上上述Mellin符号，就得到全部四种基本积分；收敛允许这些导数，不能单独拆开两个发散harmonic和。

为使有限尾范围可核，记 $U_{r,s}=\sum_{m>k}H_{m+\ell}^{(s)}/m^r$、$V_{r,s}=\sum_{m>k}(\zeta(s)-H_{m+\ell}^{(s)})/m^r$。用到的U均有 $r\ge2$，V均有 $s\ge2$。它们分解为
$$
 U_{r,s}=\zeta(r,s)+\zeta(r+s)-\sum_{m=1}^kH_m^{(s)}/m^r
             +\sum_{h=1}^\ell S_{r,s}(k,h),
$$
$$
 V_{r,s}=\zeta(s,r)-\sum_{m=1}^k(\zeta(s)-H_m^{(s)})/m^r
             -\sum_{h=1}^\ell S_{r,s}(k,h),
$$
$$
 S_{r,s}(k,h)=\sum_{m>k}\frac1{m^r(m+h)^s}.
$$
对 $w'=r+s$，直接部分分式为
$$
 \frac1{m^r(m+h)^s}=
 \sum_{i=1}^r\frac{(-1)^{r-i}\binom{w'-i-1}{s-1}}{h^{w'-i}m^i}
 +\sum_{j=1}^s\frac{(-1)^r\binom{w'-j-1}{r-1}}{h^{w'-j}(m+h)^j}.
 \tag{7}
$$
一阶项合成 $H_{k+h}-H_k$；其余项是 $\zeta(j)-H_{k+h}^{(j)}$ 或 $\zeta(i)-H_k^{(i)}$。所有有限尾index最多 $k+h\le N$，有理分母总次数最多w，ζ2系数最多w−2。这证明(5)的**每个prime power**，没有只核大素数。纯MZV项权至少3，其同权化简不流入weight0或单独weight2；不需要在这两个分量再领取未知数值独立性或忽略一个通用常数。

在(1)的来源输入下，完整明确模型是
$$
 P_n=-\tfrac12\sum cr,\qquad
 \widehat P_n=-\tfrac14\sum cz,\qquad
 R_n=-\tfrac12\sum cr-\tfrac34\sum cz.
 \tag{8}
$$
因为 $N\le32n$、$(4-\alpha-\beta)+w=5$，由(4)–(5)得
$$
 2d_{32n}^5P_n\in\mathbb Z,\qquad
 4d_{32n}^3\widehat P_n\in\mathbb Z,\qquad
 S_n(Q_n,R_n)\in\mathbb Z^2,\quad S_n=4d_{32n}^5.
 \tag{9}
$$
Q用原(17)的非零整数双和，整体符号 $(-1)^n$ 不能只在这一栏改掉。PNT给 $\log S_n/n\to160$。这是直接Barnes的安全模型，不使用原experimental式(28)，也不使用下降常数桥。

## 4. 下降积分自身的独立全幂证书

固定 $18n\le k\le26n$、$w_k=29n-k$，显式 $J_{3,k}$ 的一重Barnes核为
$$
 J_{3,k}=\frac{(-1)^{w_k}}{2\pi i}\int_{\Re t=1/2}
 \frac{(1-t)_{15n}(t-w_k)_{12n}}
 {(14n+1-t)_{15n+1}(16n+1-t)_{12n+1}}
 \left(\frac\pi{\sin\pi t}\right)^2dt.
$$
同样的整数值polynomial/整数留数证明给Laurent系数 $c_{\ell,2}\in\mathbb Z$、$d_{15n}c_{\ell,1}\in\mathbb Z$，且 $\sum c_{\ell,1}=0$。左闭合三角核得到
$$
 A_k=(-1)^{w_k}\sum c_{\ell,2},\quad
 B_k=(-1)^{w_k}\sum(2c_{\ell,2}H_{\ell-1}^{(3)}-c_{\ell,1}H_{\ell-1}^{(2)}).
$$
这里 $\ell\le29n+1$，故 $d_{29n}^3B_k\in\mathbb Z$。若另付修正后的伴随桥，则 $2d_{29n}^3\widehat P_n\in\mathbb Z$；目前仅对显式下降积分无条件领证，不把这个条件界与(9)混同。

## 5. 群能移交什么，全部素数幂为何不产生新线性信用

原(27)令 $F_n(a)=\prod_{i\in\mathcal F}(nh_i(a))!$，$\mathcal F=\{1,2,3,4,5,6,7,9,10,11,14,16,18,20,23,27,28\}$。原文在canonical分量层面给 $W_g=c_gW$、$W=(Q,R)$、$c_g=F_n(ga)/F_n(a)>0$。这不是把数值ζ3、ζ5的独立性当已知。

生成元的下降核兼容可另核：$p_{01},p_{12}$ 是左 ${}_3F_2$ 参数置换；对 $h'$，令 $r=q_3-p_6,k'=k+r$，原PDF17 Bailey内身份取 $t=-k-1$ 给
$$
 J'_{k+r}/J_k=\frac{(p_2+q_2-p_1)!}{p_2!}\frac{k!}{(k+r)!},\quad
 C'_{k+r}/C_k=\frac{p_6!}{q_3!}\frac{(k+r)!}{k!}.
$$
乘积正是I的 $h'$ 标量，符号差 $4r$；固定参数 $r=-2n$、$k+r\ge16n$。$i_1$ 对Q的双和交换两指标；I不变后仅剩两有理系数乘1、ζ2，已知ζ2无理性使其各自不变。此核查支持原分量标量作用，**不补证§1未付的cycle常数桥或整个group的motivic猜想**。

若每个g都有经证明的完整安全清整 $D_gW_g\in\mathbb Z^2$，则
$$
 t_p=\min_g\{v_pD_g+v_pF_n(ga)-v_pF_n(a)\},
 \quad T=\prod_p p^{t_p},\quad TW\in\mathbb Z^2.
 \tag{10}
$$
这是全p的条件移交引理。**只有统一D确实清整全部orbit的完整pair**时才可简化成 $D/\Psi_n$，$\Psi_n=\prod_pp^{\nu_{p,n}}$、$\nu_{p,n}=\max_g(v_pF_n(a)-v_pF_n(ga))$。本轮(9)只证明固定代表，不能直接用它领取全部orbit信用。

固定族的对称坐标为 $(s_0;s_1,\ldots,s_7)=(20.5;3.5,4.5,5.5,6.5,7.5,8.5,9.5)$。F对应全部21条边减路径 $\pi_0=(2,7,1,6,4,5,3)$ 六边，加两个端点diagonal；全部g都有 $\sum_{\mathcal F}h=2s_0+4\sum s_i=223$。设
$$
 L_\pi(x)=\sum_{i=1}^6\lfloor(s_{\pi_i}+s_{\pi_{i+1}})x\rfloor
 -\lfloor(s_0-s_{\pi_1})x\rfloor-\lfloor(s_0-s_{\pi_7})x\rfloor.
$$
精确Legendre模型为 $\nu_{p,n}=\max_\pi\sum_{j\ge1}(L_\pi(n/p^j)-L_{\pi_0}(n/p^j))$；max必须在整个幂次和外。各L的线性项相同为50x，floor误差在 $(-6,2)$，每幂整数差至多7。于是
$$
 0\le\nu_{p,n}\le7\lfloor\log_p(18n)\rfloor,\qquad
 0\le\log(\Psi_n/\Phi_n)\le7\sqrt{18n}\log(18n)=o(n).
 \tag{11}
$$
这里 $\Phi_n$ 是原文已保留 $p>\sqrt{18n}$ 的同一群信用。补齐其遗漏的小素数及高次幂没有新的线性收益；不重算原报告的34.394…，不作5040 orbit扫描。这不排除目标R真实取消或不同积分表示的新算术。

## 6. 真正本原预算与停止决定

对任意共同安全S，实际倍率为
$$
 \delta_n=S/\gcd(SQ_n,SR_n),\qquad
 v_p\delta_n=-\min(v_pQ_n,v_pR_n).
 \tag{12}
$$
它与任务中的最小分母定义一致，允许负局部指数。若 $X=u/v\in\mathbb Q$、实际 $E_n\ne0$，则 $\delta_nE_n\in v^{-1}\mathbb Z\setminus\{0\}$，故 $\delta_n|E_n|\ge1/v$。充分反证需要在**同一无界子列**上非零且乘积趋0。若实际率为−b，$\liminf\log\delta_n/n<b$ 足够抽子列；一般指数等号仍可能有次指数收益，不能把严格不等式写成所有证明的必要条件。

(9)只付 $\limsup\log\delta_n/n\le160$。采用作者31.55…作为条件定位时，这个安全upper不够；它不证明实际δ增长。原49.61…单栏定位同样不是δ下界。本轮没有证明完整pair的额外共同内容可改变18.05n缺口；(11)只拒绝从补小素数获得这种线性信用。

**关闭266这一轮来源核查，不准入数值实施。** 重开须给同一canonical pair的新全尺度或同一无界子列内容，连同实际E的严格衰减/非零，足以改变完整净预算；更多有限头、补高次幂、固定群重排或给任务改名不够。未否定全部M₀,₈方法或X无理性。

连续未改善数值可行性记为6，不因安全模型和纠错重置。下一轮267安排提前[宏观准入复盘](source_gate_charter_round267_20261013.md)，比较真实新机制的最终出口与机会成本；若仍未改善，265之后即达两轮早评门槛。这是宏观决策，不重新开放已关闭的数学实现。总goal保持active。

## 7. 实际核查边界

主代理实际读原PDF物理8–20、26–32页，视觉核14页，核primary HTML对应实验措辞；未把全文定位结果当FULL32页。三个新上下文子代理分别重建Barnes系数/有限尾、群生成元/全幂floor模型及下降/primitive量词；主代理独立重建(2)的Gamma移位、(4)的Laurent和整数值导数、(6)–(7)的半域生成及有限尾、下降留数、路径floor界和(12)。三位审阅者保存后全文复读本稿与267任务说明；descent独核Barnes/PF/有限尾，barnes独核下降与群floor，symmetry独核下降/primitive范围，主代理核全部推导。各段作者自审只算转录，不计独审。按意见修正LaTeX转录、h′索引及267未来计数措辞，没有剩余阻断项；未认证作者数值区间。

来源输入和未付范围：原(4)canonical graded识别未从头重证；作者实际衰减/非零连接及数值区间未认证；下降常数桥未独证；没有完整orbit共同安全模型或actual primitive净信用。未运行CAS、数学producer、参数/orbit、素数或Padé扫描；冻结文献与形式化资产均保留。
