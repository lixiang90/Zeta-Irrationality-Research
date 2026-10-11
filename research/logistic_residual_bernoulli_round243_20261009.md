# 第243轮：商部Bernoulli首层与完整minor内容

2026-10-09，A。固定第240–242轮的完整K5泛函、列池和归一化，目标仍为 \(3\zeta(3)+\zeta(5)\)。本稿在 \(2n<p<3n\) 给出商部首层的精确矩阵、全部minor下界及一个受限的完整费用改进。数学程序、素数样本、参数扫描、Lean运行均0；不改任何冻结稿。

## 1. 同一完整对象

令
\[
 D_a(t)=\prod_{j=1}^a(t+j),\quad R_n=D_n^4/D_{5n},\quad
 h=3n,\quad S_n=(5n)!/(n!)^4,\quad F_n=\prod_{i=0}^{h-1}(i!)^2.
 \tag{B1}
\]
\(B^+(t^a)=B_a^+\)，\(B_1^+=1/2\)。若
\(tf=P+\sum_jc_j/(t+j)\)，完整泛函是
\[
 U_T(f)=\tfrac32B^+(P')+\tfrac1{24}B^+(P''')
 +\sum_jc_j(3H_j^{(3)}+H_j^{(5)})-T\sum_jc_j.
\]
\(M_n(T)=[U_T(t^{i+k}R_n)]_{i,k<h}\)，
\(Q_n=\det M_n\)，\(\widetilde Q_n=S_n^hQ_n/F_n\)。
对 \(0\le e\le6n-2\) 写
\[
 t^eR_n=q_e+\sum_j\frac{\lambda_j(-j)^e}{t+j},\quad
 q_e\in\mathbf Z[t],\quad
 L_e=\tfrac32B^+((tq_e)')+\tfrac1{24}B^+((tq_e)''').
 \tag{B2}
\]
首一除法支付 \(q_e\) 的整性，且 \(\deg(tq_e)\le5n-1\)。
乘以 \(t\) 带来的额外常数被两个导数消掉，不能据此删除商部。

本轮实际完整复读Root的242强头稿H1–H15。使用其已证
\[
 (W_p(T))_{ik}=S_nL_{i+k}
 +\sum_j\omega_j(-j)^{i+k}(T-3\eta_{3,j}-\eta_{5,j}),
 \quad
 \omega_j=(-1)^{j-1}j^2\binom{5n}{j}\binom{j-1}{n}^4,
 \tag{B3}
\]
其中 \(\eta\) 是删除 \(p\) 倍数后的完整调和头。固定
\(p\ge11,\ 2n<p<3n\)，故 \(5n<p^2\)。
若 \(s=\lfloor5n/p\rfloor\)，则 \(s=2\) 或1。
242的分级整数矩证明给B3中所有调和头与全部 \(T\) 系数估值至少 \(s\)，而非只在某个 \(T\) 值成立。

## 2. 唯一危险商部系数

对整数多项式 \(P\)、\(\deg P\le5n-1\)，有
\[
 \boxed{pB^+(P')\equiv[t^{2p-1}]P\pmod p,\qquad
 B^+(P''')\in\mathbf Z_p.}
 \tag{B4}
\]
证明逐单项式即可。von Staudt–Clausen给
\(pB_a\equiv-1\pmod p\) 当正整数 \(a\) 被 \(p-1\) 整除；
其余Bernoulli数在 \(p\) 整。一阶项 \(dB_{d-1}^+\) 在
\(d=p\) 的分母被 \(d\) 抵消，在 \(d=2p-1\) 给
\((2p-1)(-1)\equiv1\)。下一可能次数 \(3p-2\) 已大于
\(5n-1\)，因为 \(p>2n\)。
这里 \(3(p-1)\) 是偶数，不能用“奇Bernoulli数为零”排除它；
排除依据是实际次数范围。\(B_0,B_1^+\) 无 \(p\) 分母。

三阶项为 \(d(d-1)(d-2)B_{d-3}^+\)。
Bernoulli指数 \(a(p-1)\) 的前三种危险次数
\(p+2,2p+1,3p\) 各被falling factorial中的 \(p\) 因子抵消。
首个可能未抵消次数 \(4p-1>5n-1\)，故三阶项整。
特别地，
\[
 pL_e\equiv\tfrac32[t^{2p-2}]q_e\pmod p. \tag{B5}
\]
当 \(s=1\)，\(2p>5n\)，B4的右端恒零；这仅证明商部本身整，
没有证明完整 \(W_p/p\) 恒零。

## 3. 精确首层Hankel矩阵及nullspace

以下限 \(s=2\)，即 \(2n<p<5n/2\)。置
\[
 \tau=5n-2p,\quad m=\tau+1,\quad
 b=h-m=2p-2n-1,\quad L=n+2p-2.
\]
在无穷远展开
\[
 R_n=t^{-n}\sum_{\ell\ge0}r_\ell t^{-\ell},
 \quad r_\ell\in\mathbf Z,\quad r_0=1,\quad r_\ell=0\ (\ell<0).
 \tag{B6}
\]
整数首一分母的形式反演给整系数。实际商部为
\(q_e=\sum_{\ell=0}^{e-n}r_\ell t^{e-n-\ell}\)，空和为0。
因此定义
\[
 H_{ik}=r_{i+k-L},\quad 0\le i,k<h,\qquad
 \alpha=\tfrac32\,S_n/p^2\in\mathbf Z_p^\times,
\]
得到完整的系数恒等式
\[
 \boxed{W_p(T)=p\alpha H+p^2E(T),\quad
 E(T)\in M_h(\mathbf Z_p[T]).} \tag{B7}
\]
B5给商部首层，B3的全部头与目标系数至少 \(p^2\) 给余项；
B7既保留三阶贡献，也保留全部有限头。

\(H\) 的前 \(b\) 行与列恒零。其右下 \(m\) 阶块重编号
\(I,J=0,\ldots,m-1\) 后是
\[
 H^{\rm act}_{IJ}=r_{I+J-(m-1)},\qquad
 \det H^{\rm act}=(-1)^{m(m-1)/2}. \tag{B8}
\]
反对角线上全为 \(r_0=1\)，其上侧为零，故这是真单位块。
于是 \(H\) 在 \(\mathbf Q\) 及 \(\mathbf F_p\) 的秩都精确为 \(m\)；
\(W_p/p\bmod p\) 的左右kernel正是前 \(b\) 个坐标，
亦即次数 \(<b\) 的系数多项式空间。像为最后 \(m\) 个坐标空间。
首层与 \(T\) 无关；不把这个秩误当完整矩阵的秩。

## 4. 全部minor的安全内容

记 \(g_p\) 为全部多项式系数的最小 \(p\)-估值。B7给任意
\(k\) 阶、任意行列位置的minor：
\[
 \boxed{g_p(\operatorname{minor}_k W_p)
       \ge k+(k-m)_+.} \tag{B9}
\]
确实，先抽出每列的 \(p\)，再对
\(\alpha H+pE\) 展开。若使用超过 \(m\) 列的 \(\alpha H\)，
该项为零；剩下每项至少使用 \((k-m)_+\) 列的 \(pE\)。
这是系数证明，不是选定数值 \(T\) 的估计。
当 \(k\le m\)，B8内存在单位 \(k\) 阶反三角minor，故相应
\(W_p\) minor的估值恰为 \(k\)。
当 \(k>m\)，B9不声称最优，也不支付下一Schur层。

为了传到完整矩阵，使用242的严格秩一分解
\[
 S_nM_n=W_p+\sum_{j=p}^{5n}\gamma_jv_jv_j^t,\quad
 v_j=((-j)^i)_{i<h},\quad
 v_p(\gamma_j)\ge\nu_c-5,
\]
\[
 \nu_c=2[c=0]+[c>\tau]+4[1\le c\le n],\qquad
 C_c=2\ (c\le\tau),\quad C_c=1\ (c>\tau).
 \tag{B10}
\]
\(c\) 为 \(j\bmod p\)，\(C_c\) 是真实节点数。
双minor展开中节点只能使用一次。若第 \(c\) 类用 \(a_c\) 个节点，
其两个交替minor均被类内Vandermonde整除，合计至少含
\(p^{a_c(a_c-1)}\)；节点差小于 \(p^2\)，这一层合法。
因而任意 \(k\) 阶完整minor有
\[
 g_p(\operatorname{minor}_k(S_nM_n))\ge
 \min_{\substack{0\le a_c\le C_c\\t=\sum a_c\le k}}
 \left\{\sum_c[a_c(\nu_c-5)+a_c(a_c-1)]
 +(k-t)+(k-t-m)_+\right\}. \tag{B11}
\]
没有删除商部、有限头或目标系数，也未把ambient残数矩阵的秩
免费当成完整堆栈秩。

## 5. 对完整归一化费用的有限改进

在B11取 \(k=h\)。相对于余项每阶成本1，四类增量为

| 类 | 节点数 | 依次增量 \(\nu_c-6+2\ell\) |
|---|---:|---|
| \(c=0\) | 2 | \(-4,-2\) |
| \(1\le c\le\tau\) | 2 | \(-2,0\) |
| \(\tau<c\le n\) | 1 | \(-1\) |
| \(n<c<p\) | 1 | \(-5\) |

全部增量非正，额外项 \((h-t-m)_+\) 也随 \(t\) 非增。
总节点数 \(C_{\rm tot}=5n-p+1\le h\)，所以这个安全最小式
由使用全部节点达到。增量和为 \(-n-3p-1\)，留下
\(h-C_{\rm tot}=p-2n-1\) 阶余项minor。因此
\[
 g_p(\det(S_nM_n))\ge
 2n-3p-1+(3p-7n-2)_+. \tag{B12}
\]
特别要保留表中第二个零增量槽：它可以减少余项阶数，
所以不能只数负槽后直接宣布“\(h-p-m\)”层额外内容。

若 \(Q_n\ne0\)，以 \(P_n=d_n\widetilde Q_n\) primitive、
\(d_n>0\) 定义比例，则
\(v_p(d_n)=v_p(F_n)-g_p(\det(S_nM_n))\)。
\(2n<p<3n\) 时 \(v_p(F_n)=2(3n-p)\)，故B12给
\[
 \boxed{v_p(d_n)\le
 4n+p+1-(3p-7n-2)_+,\quad 2n<p<5n/2.} \tag{B13}
\]
当 \(p>(7n+2)/3\) 时右端为 \(11n-2p+3\)；
其余这一子窗口仍是原安全上界 \(4n+p+1\)。
在 \(5n/2<p<3n\) 的 \(s=1\) 部分，本稿只保留242原界；
B7–B13不能跨 \(s\) 使用。

宏观上B13将 \(7/3<x<5/2\) 的既有profile \(4+x\) 改为
\(11-2x\)，这一局部安全上界的面积减少
\(\int_{7/3}^{5/2}(3x-7)\,dx=1/24\)。
这只是同一完整多项式的已证费用上界改进。
没有由上界大小推出actual费用下界、最优费用或不可能定理；
没有宣布全prime预算严格小于6。

## 6. 已付范围与停止点

已付：商部唯一危险系数、首层精确秩和kernel、全部minor内容、
保留全部节点后的受限归一化费用改进。
未付：下一Schur层的额外全部系数内容、全窗口最优费用、
完整实处证书的独立认证及新数值无理性/线性无关性结果。
241的无穷非零是既有独立资产，本稿不由B13重新证明它，
也不假定所有 \(n\) 都非零。

实际读取与运行范围见
[本人记录](../literature/logistic_residual_filter_sources_round243_20261009/alternative_reading_scope.md)。
本稿仅引用Root242强头最终9113 B /
\(1daeea8510afa88179d877bbd1a68481ea225d06b4020156411120fd09d46ca5\)，
没有把尚未完整审阅的C243过滤稿当作输入。

