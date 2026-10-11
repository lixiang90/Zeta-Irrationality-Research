# 第242轮：完整非整调和头的分级内容证书

2026-10-09，Root。固定240–241的同一完整矩阵。本稿证明外层素数余项的全部系数都具有额外整内容；不改变泛函、列池、目标变量、归一化或primitive定义。数学程序、参数扫描及Lean运行均0。独立审阅另登记，本稿不以消息中的同意代替最终全文审阅。

## 1. 固定对象与待加强的完整余项

令
\[
 D_m(t)=\prod_{j=1}^m(t+j),\quad R_n(t)=D_n(t)^4/D_{5n}(t),\quad
 h=3n,\quad S_n=(5n)!/(n!)^4,\quad F_n=\prod_{i=0}^{h-1}(i!)^2.
\]
以Bernoulli有理泛函 \(B^+(t^d)=B_d^+\)、\(B_1^+=1/2\) 定义
\[
 U_T(f)=\tfrac32 B^+(P')+\tfrac1{24}B^+(P''')
 +\sum_jc_j(3H_j^{(3)}+H_j^{(5)})-T\sum_jc_j,
 \quad tf=P+\sum_j\frac{c_j}{t+j}.
\]
完整对象为 \(M_n(T)=[U_T(t^{i+k}R_n)]_{i,k<h}\)、
\(Q_n=\det M_n\)、\(\widetilde Q_n=S_n^hQ_n/F_n\)。
目标仍为 \(T=3\zeta(3)+\zeta(5)\)。

写 \(t^eR_n=q_e+\sum_j\lambda_j(-j)^e/(t+j)\)，其中
\(\lambda_j=\operatorname{Res}_{t=-j}R_n\)。首一整数除法给 \(q_e\in\mathbf Z[t]\)。定义
\[
 L_e=\tfrac32B^+((tq_e)')+\tfrac1{24}B^+((tq_e)'''),\quad
 \omega_j=S_nj\lambda_j
 =(-1)^{j-1}j^2\binom{5n}{j}\binom{j-1}{n}^4\in\mathbf Z.
 \tag{H1}
\]
\(j\le n\) 时 \(\omega_j=0\)。乘以 \(t\) 时出现的额外常数被两个导数消掉；没有删除其余商部。实际列池 \(0\le e\le6n-2\) 满足 \(\deg(tq_e)\le5n-1\)。

固定素数 \(p\ge11\)、\(n<p\le5n\)，设
\[
 s=\lfloor5n/p\rfloor\in\{1,2,3,4\},\quad
 \tau=5n-sp,\quad R_s=\max(1,s-1).
\]
\(5n<p^2\) 且 \(v_p(S_n)=s\)。剥离全部 \(p\) 的倍数，定义
\[
 \eta_{r,j}=\sum_{\substack{1\le u\le j\\p\nmid u}}u^{-r},\qquad
 H_j^{(r)}=p^{-r}H_{\lfloor j/p\rfloor}^{(r)}+\eta_{r,j},\quad r=3,5.
\]
于是完整余项是
\[
 (W_p(T))_{ik}=S_nL_{i+k}
 +\sum_{j=1}^{5n}\omega_j(-j)^{i+k}(T-3\eta_{3,j}-\eta_{5,j}).
 \tag{H2}
\]
本稿的结论为
\[
 \boxed{W_p(T)\in p^{R_s}M_h(\mathbf Z_p[T]).} \tag{H3}
\]
它是完整多项式矩阵的系数结论，并非只在 \(T=0\) 或某个有理值的整性。

## 2. 所有整数多项式的真实残数矩

在无穷远处，\(R_n=t^{-n}\) 乘以 \(\mathbf Z[[t^{-1}]]\) 中的级数：整数首一分母的形式反演保留整数系数。因此对每个整数 \(e\ge0\)，
\[
 a_e=\sum_jj\lambda_j(-j)^e=-[t^{-2}]\,t^eR_n\in\mathbf Z,
 \qquad \sum_j\omega_j(-j)^e=S_na_e. \tag{H4}
\]
故对于每个 \(P\in\mathbf Z[t]\)，\(\sum_j\omega_jP(j)\in S_n\mathbf Z\)。
这里的全 \(e\) 恒等式只用代数Laurent展开与有限残数；不增加实际矩阵列池，也不使用未证明的泛函连续性。

对于模 \(p\) 的任一类 \(b\in\{0,\ldots,p-1\}\)，取整数多项式
\[
 E_b(t)=1-(t-b)^{\varphi(p^s)}.
\]
指数 \(\varphi(p^s)\ge s\)。若 \(j\equiv b\pmod p\)，则 \(E_b(j)\equiv1\pmod{p^s}\)；否则Euler定理给 \(E_b(j)\equiv0\pmod{p^s}\)。H4用于 \(E_bP\) 后得到
\[
 \sum_{j\equiv b\ (p)}\omega_jP(j)\in p^s\mathbf Z_p.
 \tag{H5}
\]
写该类的整数节点 \(j=pm+b\)，取 \(P(t)=(t-b)^\ell\)，即得
\[
 v_p\!\left(\sum_{j\equiv b\ (p)}\omega_jm^\ell\right)\ge s-\ell
 \qquad(\ell\ge0). \tag{H6}
\]
对于 \(\ell>s\) 此下界虽弱，仍有效；后面只需 \(\ell<s\)。零类与 \(m=0\) 的节点均在H5–H6内，没有被省略。

## 3. 非整头的分级多项式结构

设 \(j=pm+b\)，\(0\le b<p\)。非 \(p\) 部分严格等于
\[
 \eta_{r,pm+b}
 =\sum_{a=0}^{m-1}\sum_{u=1}^{p-1}(pa+u)^{-r}
   +\sum_{u=1}^{b}(pm+u)^{-r}. \tag{H7}
\]
对单位 \(u\) 作有限二项式展开，模 \(p^s\) 得
\[
 \eta_{r,pm+b}\equiv
 \sum_{k=0}^{s-1}p^k\binom{-r}{k}
 \left[S_{r+k}\sum_{a=0}^{m-1}a^k+H_b^{(r+k)}m^k\right],
 \quad S_v=\sum_{u=1}^{p-1}u^{-v}. \tag{H8}
\]
余项逐节点在 \(p^s\mathbf Z_p\)；求和范围有限，不涉及分析收敛。
\(r+k\le8<p-1\) 保证 \(S_{r+k}\in p\mathbf Z_p\)。
\(k\le3\) 时 \(\sum_{a=0}^{m-1}a^k\) 是次数 \(k+1\) 的有理多项式，分母只含2、3，因此在 \(p\ge11\) 时为 \(p\)-单位。

H8中完整循环项的前因子至少含 \(p^{k+1}\)，其每个次数 \(\ell\le k+1\) 的系数估值至少 \(\ell\)；部分循环项的次数是 \(k\)，系数至少含 \(p^k\)。故存在 \(A_{r,b}(m)\in\mathbf Z_p[m]\) 使
\[
 \eta_{r,pm+b}\equiv A_{r,b}(m)\pmod{p^s},\qquad
 v_p([m^\ell]A_{r,b})\ge\ell. \tag{H9}
\]
次数 \(\ell\ge s\) 的项可丢入模 \(p^s\) 的余项。
\((-pm-b)^e\) 的次数 \(\ell\) 系数也含 \(p^\ell\)，所以乘以它仍保留H9的分级条件。对该乘积逐项使用H6，得到
\[
 \sum_{j\equiv b\ (p)}\omega_j(-j)^e\eta_{r,j}\in p^s\mathbf Z_p.
\]
误差乘以整数 \(\omega_j\) 仍在 \(p^s\mathbf Z_p\)。再遍历全部类可得
\[
 \boxed{\sum_j\omega_j(-j)^e\eta_{r,j}\in p^s\mathbf Z_p,
 \quad r=3,5, e\ge0.} \tag{H10}
\]
这是完整调和头间的内容抵消，而非逐个残数具有相同高估值。

## 4. 商部与目标系数

H4已经给H2的全部 \(T\) 系数至少 \(p^s\)，H10给全部非 \(p\) 调和头至少 \(p^s\)。商部不能因此删除。
von Staudt–Clausen给每个Bernoulli数的估值至少 \(-1\)，H1的商部是整数多项式，固定24是单位，因而
\[
 v_p(S_nL_e)\ge s-1. \tag{H11}
\]
这支付 \(s\ge2\) 时H3。

若 \(s=1\)，则 \(\deg(tq_e)\le5n-1\le2p-2\)。对单项式 \(t^d\)，一阶贡献是 \(dB_{d-1}^+\)。第一个可能的Bernoulli分母在 \(d=p\)，被 \(d\) 抵消；第一个未被抵消的可能次数为 \(2p-1\)，超出范围。三阶贡献是 \(d(d-1)(d-2)B_{d-3}^+\)：Bernoulli指数 \(q(p-1)\) 的 \(q=1,2,3\) 对应次数 \(p+2,2p+1,3p\)，均被falling factorial中的 \(p\) 因子抵消；第一个可能未抵消的次数为 \(4p-1\)。\(B_0,B_1^+\) 无 \(p\) 分母。因此 \(L_e\) 在 \(s=1\) 本身 \(p\)-整，\(S_nL_e\) 至少含 \(p\)。结合H10即证明H3所有情形。

固定素数2、3、5、7不在本稿范围，其全素数幂费用由A的小素数引理处理，累计 \(o(n^2)\)。不以有限素数例外掩盖一个大小随 \(n\) 增长的窗口。

## 5. 全部系数的秩一展开及费用接口

设 \(v_j=((-j)^i)_{i<h}\)。同一完整矩阵严格分解为
\[
 S_nM_n=W_p(T)+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,\qquad
 \gamma_j=-p^{-5}\omega_j(H_{\lfloor j/p\rfloor}^{(5)}+3p^2H_{\lfloor j/p\rfloor}^{(3)}).
 \tag{H12}
\]
\(\lfloor j/p\rfloor\le4\)，所以 \(v_p(\gamma_j)\ge\nu_b-5\)，其中
\[
 \nu_b=2[b=0]+[b>\tau]+4[1\le b\le n],\qquad
 C_b=s\ (b\le\tau),\quad C_b=s-1\ (b>\tau).
 \tag{H13}
\]
\(C_b\) 是该类 \(j\ge p\) 的真实节点数；H13来自参数小于 \(p^2\) 的二项式carry，未继承原一阶源的内容值。

在完整行列式双minor展开中，使用总计 \(k=\sum_bk_b\) 个秩一节点的项，余下的 \((h-k)\)-阶 \(W_p\) minor至少含 \(p^{R_s(h-k)}\)。同类 \(k_b\) 个不同节点的两个交替minor，各被类内Vandermonde整除，共至少 \(k_b(k_b-1)\) 层 \(p\)。因此全部系数的Gauss估值满足
\[
 g_p(\det(S_nM_n))\ge R_sh+
 \min_{\substack{0\le k_b\le C_b\\\sum_bk_b\le h}}
 \sum_b\{k_b(\nu_b-5-R_s)+k_b(k_b-1)\}.
 \tag{H14}
\]
删去总秩限制仍给有效、可能更弱的下界，其各类最小值为递增slot的负项之和。于是，在 \(Q_n\ne0\)、\(P_n=d_n\widetilde Q_n\) primitive且 \(d_n>0\) 时，
\[
 \boxed{v_p(d_n)\le v_p(F_n)-R_sh
  -\sum_b\sum_{\ell=0}^{C_b-1}\min(\nu_b-5-R_s+2\ell,0).} \tag{H15}
\]
这里已支付 \(S_n\)，必须保留 \(F_n\)，也必须保留负费用；不能把它变成取正部的LCD预算。

供B/C独审的宏观profile为 \(v_p(d_n)\le n\Phi(p/n)+O(1)\)：

| 区间 \(x=p/n\) | \(\Phi(x)\) | 段积分 |
|---|---|---|
| \(1<x<5/4\) | \(2+x\) | \(25/32\) |
| \(5/4<x<4/3\) | \(20-11x\) | \(139/288\) |
| \(4/3<x<3/2\) | \(8-2x\) | \(31/36\) |
| \(3/2<x<5/3\) | \(2+2x\) | \(31/36\) |
| \(5/3<x<2\) | \(20-7x\) | \(43/18\) |
| \(2<x<5/2\) | \(4+x\) | \(25/8\) |
| \(5/2<x<3\) | \(29-8x\) | \(7/2\) |
| \(3<x<4\) | \(23-6x\) | \(2\) |
| \(4<x<5\) | \(7-2x\) | \(-2\) |

九段积分合计12，\(3<x<5\) 的净积分为0。断点及零类直接由H13–H15给 \(O(1)\) 修正，PNT将该修正累计为 \(o(n^2)\)。这些是费用上界，不是最优费用或实际费用下界。

Root消息中曾建议在 \(3/2<x<5/3\) 用总秩限制进一步得到5、\(13-5x\)。B指出负slot总数实际是 \(2(p-n)+2\tau+(n-\tau)=4n-p<h\)，所以该建议已撤回，没有纳入任何定理或预算。此处保留真实的 \(2+2x\)。

## 6. 进展与下一关

H3与H10把完整调和头的分级整数矩连接到整模型内容，实质缩小全prime费用缺口。配合A的小素数与内窗口引理，可以形成有限的whole-prime upper。它仍未给严格 \(<6\) 的预算，原实处 \(-6\) 的完整证书也未独立认证；没有新的数值无理性或线性无关性定理。

下一项应检验H11中损失的一层是否是完整商部的真实障碍，以及带剩余 \(W_p\) 的完整过滤行列式能否有全窗口额外内容。必须给同一多项式的系数证明，不能再次增加素数样本、删除商部、或把所选上界过大当成实际无望。窗口仍限241–244，全局复盘计数仍从240开始。
