# 第242轮：固定 K5 全 prime 费用上界的宏观率

2026-10-09，B。数学程序、interval/CAS 计算、素数或参数扫描、Lean run 均为0。固定第241轮完整 \(Q_n,\widetilde Q_n=S_n^{3n}Q_n/F_n\)，没有改变列池、实处模型或 primitive 定义。本稿给完整可核的费用上界 \(1009/40<26\)，并证明所选两个上界（greedy连续松弛与完整类内容界）取优后的宏观积分不能认证所需 \(<6\)。后者不是 actual 费用下界，更不是本源的 no-go。全矩阵的额外正内容使旧外窗口面积4降到0，旧 \(56/5\) 或 \(1171/160\) 诊断均不作为本稿最终证据。

## 1. 同一完整费用与 normalization

记 \(h=3n\)、\(D_j=\prod_{\ell=1}^j(t+\ell)\)、\(R_n=D_n^4/D_{5n}\)，
\[
 S_n=(5n)!/(n!)^4,\quad F_n=\prod_{i=0}^{h-1}(i!)^2.
 \tag{R1}
\]
完整泛函为
\[
 U_T(f)=\tfrac32B^+(P')+\tfrac1{24}B^+(P''')
 +\sum_jc_j(3H_j^{(3)}+H_j^{(5)})-T\sum_jc_j,
 \quad tf=P+\sum_jc_j/(t+j).
 \tag{R2}
\]
定义 \(g_p=\min_kv_p([T^k]\widetilde Q_n)\)。当 \(Q_n\ne0\) 时，正有理比例 \(d_n\) 使 \(P_n=d_n\widetilde Q_n\) 是 primitive 整数多项式，故
\[
 v_p(d_n)=-g_p,\qquad \log d_n=\sum_p(-g_p)\log p.
 \tag{R3}
\]
全部 coefficient 的 minimum 是必须保留的对象；不能改成某个有理关系值的分母，也不能给负费用取正部再称为同一个净费用。

本轮 A 的完整 CRT 与 binomial 基引理支付下列输入，本文已实际 FULL 读其最终稿。对 \(p\ge7,5n<p^2\)，令
\[
 N_b=\#\{1\le j\le n:j\bmod p=b\},\quad
 C_b=\#\{1\le j\le5n:j\bmod p=b\},
\]
\[
 c_{5,b}=4N_b-C_b+[b=0]-4.
 \tag{R4}
\]
从 slot \(c_{5,b},c_{5,b}+2,\ldots\) 取最低 \(h\) 项，各列取数 \(k_b\)，
\[
 G_5=\sum_b\{k_bc_{5,b}+k_b(k_b-1)\},\qquad
 g_p\ge G_5+\mathcal N_p,
\]
\[
 \mathcal N_p=h(\lfloor5n/p\rfloor-4\lfloor n/p\rfloor)
       -2\sum_{i=0}^{h-1}\lfloor i/p\rfloor.
 \tag{R5}
\]
这是新 \(H^{(5)}\) 和全部商部共同给的全系数下界；不是从旧 \(K_3\) 自动继承。

小素数用完整 \(\binom ti\) 基，精确保留 \(F_n\)：
\[
 g_p\ge-3n\{5\lfloor\log_p(10n)\rfloor+v_p(24)\}.
 \tag{R6}
\]
将 \(p\le n^{2/3}\) 的费用上估，至多 \(O(n^{5/3}\log n)=o(n^2)\)；固定2、3同样包含。\(p>5n\) 的全部条目、\(S_n,F_n\) 都 \(p\)-整，故这些费用非正，可以合法舍弃作 upper。以下只处理 \(n^{2/3}<p\le5n\)，所有 factorial 参数都小于 \(p^2\)，R5没有漏掉更高幂。

## 2. greedy 整体平移与内窗口公式

原一阶 column 是 \(c_{3,b}=4N_b-C_b+[b=0]-2\)。因此
\[
 c_{5,b}=c_{3,b}-2,\qquad G_5=G_3-2h=G_3-6n.
 \tag{R7}
\]
每一步的比较和固定 tie-break 都相同，故是同一个完整 allocation；\(S_n,F_n\) 的 \(\mathcal N_p\) 不变。逐 prime 的 greedy 费用 upper 增加 \(6n\)，不是 \(2n\)。

令 \(x=p/n,\ a=\{1/x\},b=\{5/x\},\eta=\{3/x\}\)，定义
\[
 \psi(x)=6+x\eta(1-\eta)-3(4a-b)
   +\frac{x}{4}\{16a+b-8\min(a,b)-(4a-b)^2\}.
 \tag{R8}
\]
这是已读 pinned Profiles 中的明确函数，本文另纸付 normalization 的代数接口。设 \(n=Ap+r,\ 5n=Lp+s\)，则
\[
 \sum_bc_{3,b}=p(4A-L-2)+4r-s+1,
\]
\[
 \sum_bc_{3,b}^2=p(4A-L-2)^2
 +2(4A-L-2)(4r-s+1)+1+16r+s-8\min(r,s).
 \tag{R9}
\]
任意整数 allocation 的平方完成给
\[
 G_3\ge h^2/p+h(\overline c_3-1)
       +(\sum c_3)^2/(4p)-\sum c_3^2/4.
 \tag{R10}
\]
再用 \(\sum_{i<h}\lfloor i/p\rfloor=hq-pq(q+1)/2\)，\(h=qp+t\)，
将 R9代入R10和R5，纯代数化简得
\[
 -\mathcal N_p-G_3\le n\psi(x)
    +\frac{p-12n-8r+2s-1}{4p}
 \le n\psi(x)+3/4.
 \tag{R11}
\]
所以内窗口可用
\[
 -g_p\le n(\psi(x)+6)+3/4.
 \tag{R12}
\]
这实际联合了两个 factorial；没有把 \(F_n\) 丢进“小 prime”黑箱。这里只需要 R12 在 \(x\le7/3\)。

## 3. 固定 greedy 的外窗口与更好的完整类消元

首先独立纸算原固定 greedy。在 \(7/3<x<5/2\)，忽略零类的有界修正，最低 slots 是：
\[
 -6,-4\text{ 各 }p-n\text{ 项},\quad
 -3\text{ 共 }5n-2p\text{ 项}.
 \]
故 \(G_5=-5n-4p+O(1)\)，\(\mathcal N_p=2p\)，费用 upper 是 \(n(5+2x)+O(1)\)。在 \(5/2<x<3\)，三组为
\[
 -6\text{ 共 }4n-p,\quad -5\text{ 共 }2p-5n,\quad
 -4\text{ 共 }4n-p.
 \]
于是 \(G_5=-15n+O(1)\)，\(\mathcal N_p=2p-3n\)，upper 是 \(n(18-2x)+O(1)\)。\(3<x<5\) 的 greedy upper 恒为 \(12n+O(1)\)。零类的固定偏移只改 \(O(1)\) 个被选 slot，断点也只产生 \(O(1)\)，不改变 leading 积分。

本轮 C 给出 \(p>n\) 完整共同头/双 Cauchy–Binet 引理，Root进一步支付余项的强内容；以下给独立纸面证明及全部 class count，不用旧外 profile。在完整 \(S_n\) 倍 moment matrix中，剥去 \(p\) 倍数的调和头后，
\[
 S_nM_n(T)=W(T)+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,\qquad
 v_j=((-j)^i)_{0\le i<h}.
\]
每个极点 atom 的 scalar 为
\[
 -p^{-5}\omega_j\big(H_{\lfloor j/p\rfloor}^{(5)}
                    +3p^2H_{\lfloor j/p\rfloor}^{(3)}\big),
\quad
 \omega_j=\pm j^2\binom{5n}{j}\binom{j-1}{n}^{4}.
 \tag{R13}
\]
对 \(p>n,p\ge11\)，令 \(s=\lfloor5n/p\rfloor,\tau=5n-sp\)。完整整数 residue moments满足
\[
 \sum_{j=1}^{5n}\omega_j(-j)^e=S_na_e\in p^s\mathbb Z_p
 \quad(e\ge0).
\]
这里 \(a_e=-[t^{-2}]t^eR_n\) 是整数：首一整数分母在无穷处的逆 Laurent 系数均为整数。此式不是只给原 \(0\le e\le6n-2\) 列池。

在 \(\mathbb Z_p[t]\) 对互素的 \((t-b)^s\) 作CRT，得到各 residue class 的 indicator \(E_b\)。将 \(E_b(t)(t-b)^\ell\) 代入上述全部 moments，类外误差含 \(p^s\)，类内 \(E_b(j)-1\) 同样含 \(p^s\)。因此
\[
 v_p\!\left(\sum_{j=mp+b}\omega_jm^\ell\right)\ge s-\ell
 \quad(0\le\ell<s).
\]
所有 \(\omega_j\) 为整数，故 \(\ell\ge s\) 时也至少0。

令 \(\eta_{j,r}=\sum_{1\le q\le j,\ p\nmid q}q^{-r}\)，\(r=3,5\)。对 \(j=mp+b\)、\(m\le4\)，完整 unit cycles和最后 partial head给
\[
 \eta_{mp+b,r}\equiv
 \sum_{k=0}^{s-1}\binom{-r}{k}p^k
 \left(S_{r+k}F_k(m)+H_b^{(r+k)}m^k\right)\pmod {p^s},
\]
其中 \(S_q=\sum_{\ell=1}^{p-1}\ell^{-q}\)，
\(F_k(m)=\sum_{v=0}^{m-1}v^k\) 是 degree \(k+1\)、分母为 \(p\)-单位的有理多项式。因为 \(r+k\le8<p-1\)，\(S_{r+k}\in p\mathbb Z_p\)。故右边每个 degree-\(\ell\) coefficient至少含 \(p^\ell\)；再乘 \((-mp-b)^e\) 保持该性质。用上一 class moment界，完整 \(\sum_j\omega_j\eta_{j,r}(-j)^e\) 含 \(p^s\)，参数 \(T\) 的系数也含 \(p^s\)。全部调和头保留，没有删远极点。

商部的 Bernoulli 数一般最多损一层，所以 \(S_nL_e\in p^{s-1}\mathbb Z_p\)。在 \(s=1\) 时有更好的单位性：对单项式 \(t^d\)，\(V_1\) 是 \(dB_{d-1}^+\)，首次未被导数因子清掉的 Bernoulli \(p\)-分母在 \(d=2p-1\)；\(V_3\) 是 \(d(d-1)(d-2)B_{d-3}^+\)，首次在 \(d=4p-1\)。而完整商部 degree不超过 \(5n-1<2p-1\)。这证明
\[
 \boxed{W(T)\in p^{R_s}M_h(\mathbb Z_p[T]),\qquad
 R_s=\max(1,s-1).}
 \tag{R14}
\]
这条强内容兼顾全部商部和参数列，不能只由 residue rank推得。

类 \(a=0\) 的 \(\nu_a=v_p(\omega)\) 是2；其它类是
\[
 \nu_a=[a>\tau]+4[1\le a\le n].
\]
该式对同一类所有实际 atoms相同，来自完整 factorial carries。该类可选 atoms数是 \(s\)（\(a\le\tau\)）或 \(s-1\)。同类每对节点相差恰一个 \(p\)，双 Cauchy–Binet 的两份 Vandermonde 给 \(k(k-1)\)。determinant 的完整系数都满足相应下界；不能只在 \(T\) 的某个值套秩一分解。

抽出 \(p^{R_sh}\) 后，atom的负 slot是 \(\nu_a-5-R_s+2k\)。因此同一完整 determinant 满足
\[
 -g_p\le v_p(F_n)-R_sh
 -\sum_{a=0}^{p-1}\sum_{k=0}^{C_a-1}
       \min(\nu_a-5-R_s+2k,0).
 \tag{R15}
 \]
允许每类独立最小化是安全的下界；不存在的 atom 不可选。总选数最多 \(h\) 的约束没有被冒称已给额外改善。例如 \(s=3,3/2<x<5/3\) 时，全部 negative slots数恰 \(4n-p<3n\)，该 rank约束不改变下面表。
**尚须减去 \(F_n\)**：它增加费用
\[
 v_p(F_n)=2\{(3n-p)_++(3n-2p)_+\}.
 \tag{R16}
\]
R15–R16给新的完整上界 profile
\[
 \phi(x)=
 \begin{cases}
 2+x&1<x<5/4,\\
 20-11x&5/4<x<4/3,\\
 8-2x&4/3<x<3/2,\\
 2+2x&3/2<x<5/3,\\
 20-7x&5/3<x<2,\\
 4+x&2<x<5/2,\\
 29-8x&5/2<x<3,\\
 23-6x&3<x<4,\\
 7-2x&4<x<5.
 \end{cases}
 \tag{R17}
\]
手算方式是对 \(\nu=0,1,4,5\) 分别取上式 negative-slot和，乘对应类长度 \((\tau-n)_+,p-\max(n,\tau),\min(n,\tau),(n-\tau)_+\)，零类只改 \(O(1)\)。例如 \(s=4,\tau\le n\) 的四组损失是20、15、6、4，得到 \(2+x\)；\(s=3,\tau\le n\) 是15、10、4、2，得到 \(8-2x\) 或 \(2+2x\)。断点用exact整数公式或有界端点修正。此 \(\phi\) 是全系数费用 upper，不是 actual fee 或 optimal bound；完整 cancellation尚可能更强。特别 \(3<x<5\) 可有负费用，必须保留其符号。

## 4. 同对象取优、PNT 与不用数值程序的常数

对同一 \(g_p\) 取两下界的 max，即费用 upper 的 min：
\[
 F(x)=
 \begin{cases}
 \psi(x)+6&0<x\le1,\\
 \min(\psi(x)+6,\phi(x))&1<x\le7/3,\\
 \phi(x)&7/3<x\le5 .
 \end{cases}
 \tag{R18}
\]
后两段 C profile亦严格优于第3节 exact outer greedy，故没有重复累计节省。

R8有界，除0外每个 compact子区间仅有有限个 floor 断点。PNT、分部求和和先切 \(x\ge\delta\) 后令 \(\delta\downarrow0\)，给
\[
 \limsup_{\substack{n\to\infty\\Q_n\ne0}}
 \frac{\log d_n}{n^2}\le C_F:=\int_0^5F(x)\,dx.
 \tag{R19}
\]
截去 \(p\le n^{2/3}\) 用 R6，固定阶误差的 prime sum是 \(O(n)\)。没有因分母带高幂而只数 prime一次；高幂已在小 prime证明中。

本文不把原196-piece数值证书或原 \(283/50\) 定理转移为新预算。用嵌套指标随机变量 \(Y=4{\bf1}_{[0,a]}-{\bf1}_{[0,b]}\)，其
\[
 \operatorname{Var}Y=16a+b-8\min(a,b)-(4a-b)^2\in[0,4].
 \tag{R20}
\]
因为 \(a\le b\) 时值在 \([-1,3]\)，反之在 \([0,4]\)；中点平方界自含证明 variance≤4。\(b=\{5a\}\)，令 \(q=\lfloor5a\rfloor\)，则 \(4a-b=q-a\in[-1/5,16/5]\)。又 \(0\le\eta(1-\eta)\le1/4\)。因此
\[
 12/5\le\psi(x)+6\le63/5+5x/4.
 \tag{R21}
\]
R17在 \(1<x<3\) 都至少3，而 \(\int_3^5\phi=0\)。所以当前所选上界的积分有严格诊断
\[
 C_F\ge(12/5)\cdot3=36/5>6.
 \tag{R22}
\]
这只约束 **已经选择的连续松弛/class upper函数** 的积分，绝不推出 \(\log d_n/n^2\ge36/5\)。尚未用精确整数 greedy全区间积分或更强跨类内容。

同时，九段 \(\phi\) 的梯形积分依次为
\[
 25/32,\ 139/288,\ 31/36,\ 31/36,\ 43/18,\ 25/8,\ 7/2,\ 2,\ -2,
 \]
总和恰12。R21在0至1的积分至多 \(529/40\)。于是
\[
 C_F\le529/40+12=1009/40<26.
 \tag{R23}
\]
全部是有限有理代数和纸面 inequality，无程序/interval 运算。

## 5. 唯一下一瓶颈与范围

R19、R23是新的完整净费用 upper，涵盖全 prime、全部幂、固定2/3、商部、所有残数、\(S_n,F_n\)。但本稿选定的 greedy连续松弛与强class界之取优积分至少 \(36/5\)，不能认证所需费用 \(<6\)。这不排除精确整数 greedy取优积分或更强内容界；实处 \(-6\) 的完整原证书本身也尚需认证。

下一可检验瓶颈是 **同一完整 coefficient polynomial 的进一步 Gauss 内容或精确allocation整体证书**，例如目前未进入 R15 的跨类 cancellation或完整 filtered residual rank。单个 auxiliary \(p=n+1\) 费用是 \(o(n^2)\)，不能代替宏观认证。全余项 \(p^{R_s}\) 内容是真实已付改进，使外窗口积分从4降到0；不能继续拿旧诊断指挥方向。也不能从新上界积分太大推出 actual费用太大。没有新数值无理性结论、不重开参数或素数扫描，不改241主稿或旧日志。

真实读取域见 [packet_reading_scope.md](../literature/logistic_gauss_budget_round242_20261009/packet_reading_scope.md)。
