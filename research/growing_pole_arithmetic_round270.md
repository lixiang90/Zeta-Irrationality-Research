# 第270轮有限处核查：固定纯目标Gram的全素数幂清整

2026-10-20。独立核[270任务](growing_pole_budget_charter_round270_20261020.md)及[269](global_source_review_round269.md)§3–5。始终固定其中唯一的 \(p_i,R_m,Q_m\)，\(n=8m,\ H=n-1\)，不调比例或空间。以下是已审书面算术结构与安全上界，**不是最优 \(\lambda_m\) 的实际下界，也没有新无理性定理**。没有参数、素数或Padé扫描。

记 \(d_r=\operatorname{lcm}(1,\ldots,r)\)。本轮得到
\[
 D_m=2\,4^{8m-1}d_{8m-1},\qquad
 B_n=2^{2n}d_{2n}^{\,2},\qquad
 S_m=B_{8m}D_m^2
     =2^{48m-2}d_{8m-1}^{\,2}d_{16m}^{\,2}.                 \tag{A1}
\]
它们满足
\[
 D_mp_i\in\mathbb Z[z],\qquad S_mR_m\in M_m(\mathbb Z),
 \qquad \lambda_m\mid S_m^m.                              \tag{A2}
\]
这里是同一条费用链：清基底两次进入Gram，再清全部有理头，最后取行列式；不另加一次直接清 \(Q_m\) 的费用。

## 1. 由本轮实际RHS得到线性来源高度

以下独立重建专门利用(G5)右端的清整，避免把一般逆矩阵的LCM与右端LCM相乘。设 \(K=4m\)，
\[
 b_k(\alpha)=[z^k](1-z)^\alpha=(-1)^k\binom{\alpha}{k}.
\]
对固定 \(i\) 令 \(r=H-i\)，并定义线性泛函
\[
 \ell_i(F)=[z^H]u_i(z)F(z).
\]
它只用 \(F\) 的首 \(K\) 个jet；令
\[
 E_i(Y)=\sum_{k=0}^{K-1}\ell_i(z^k)
                    b_k((Y-1)/2).
\]
这是次数至多 \(K-1\) 的有理多项式。整数节点 \(Y=j\)，\(0\le j<2m\)，对应
\(\alpha_j=(j-1)/2\)。把(G5)从 \(z^k\{1,a-1,L,aL\}\) 换到
\(\{w^k,w^{k-1/2},w^k\log w,w^{k-1/2}\log w\}\)，可得
\[
 E_i(j)=\frac{e_{i,j}-b_r(\alpha_j)}2,\qquad
 E_i'(j)=-\frac{b_r'(\alpha_j)}4,                         \tag{A3}
\]
其中 \(e_{i,j}\) 是整数：若该节点是 \(\alpha=k\) 或 \(k-1/2\)，
则 \(e_{i,j}=(-1)^i\binom{k}{i}\)。对整数节点
\(b_r(k)=0\)，因为 \(r\ge7m>k\)。

在这些节点，\(b_t(\alpha_j)\) 的分母整除 \(4^t\)：半整数情形是
\((1-z)^ka(z)\) 的系数，整数情形是整系数多项式。此外
\[
 b_r'(\alpha)=-\sum_{h=1}^r\frac{b_{r-h}(\alpha)}h,
\]
所以 \(b_r'(\alpha_j)\) 的分母整除 \(4^{r-1}d_r\)。
于是(A3)的value分母整除 \(2\,4^r\)，derivative分母整除
\(4^rd_r\)。

为控制合流逆，设 \(s=2m\)，令
\[
 L_j(Y)=\prod_{\substack{0\le a<s\\a\ne j}}\frac{Y-a}{j-a},
 \quad K_j(Y)=(Y-j)L_j(Y)^2,
 \quad H_j(Y)=L_j(Y)^2-2L_j'(j)K_j(Y).
\]
\(L_j(Y)=\binom Yj\binom{s-1-Y}{s-1-j}\)，故 \(L_j,K_j\)
在每个整数处取整数值。又
\(L_j'(j)=\sum_{a=1}^j1/a-\sum_{a=1}^{s-1-j}1/a\)，所以
\(d_{s-1}H_j\) 在整数处取整数值。Hermite公式给
\[
 E_i=\sum_j E_i(j)H_j+E_i'(j)K_j.
\]
因 \(r\le H\) 且 \(d_{s-1}\mid d_H\)，乘上
\(D_m=2\,4^Hd_H\) 后，两类贡献均在全部整数处取整数值。
特别在 \(Y=1+2h\) 处取整数值。对序列 \(D_mE_i(1+2h)\)
作Newton有限差分，便知 \(E_i\) 在基
\((-1)^k\binom{(Y-1)/2}{k}\) 中的所有系数均被 \(D_m\) 清整。
这些系数正是 \(\ell_i(z^k)\)，即 \(u_i\) 高系数的倒序；
故 \(D_mp_i\in\mathbb Z[z]\)。这是实际(G5)的全尺度证明，
不从小 \(\det\mathcal T\) 推费用。

## 2. 全部有理头：奇素数及2处

对任意 \(P\in\mathbb Z[T]\)，\(\deg P\le2n-2\)，作完整分解
\[
 \frac{P(T)}{(1+T)^n}=A(T)+\sum_{j=1}^n\frac{a_j}{(1+T)^j}.
\]
除数首一且平移为整系数，故 \(A\in\mathbb Z[T]\)、\(a_j\in\mathbb Z\)，
\(\deg A\le n-2\)。多项式头矩的分母整除 \(d_{2n}^2\)。
因此只需核(G2)中 \(2U_j'(1)+U_j'(1/2)/2\)。

对 \(j\ge2\) 写 \(s=j-1\)；\(U_1=0\) 无须清整。由(G2)的递推展开，
\[
 U_j(\alpha)=\sum_{q=1}^{s}\frac{2^{-q}}q
       \prod_{h=q+1}^{s}(1-\alpha/h).
\]
空乘积导数为零。在 \(\alpha=1\) 处乘积为 \(q/s\)，故
\[
 U_j'(1)=-\frac1s\sum_{q=1}^{s-1}2^{-q}
                       \sum_{h=q+1}^{s}\frac1{h-1}.       \tag{A4}
\]
其全部奇素数分母由 \(d_{2n}^2\) 清整，2处的 \(2^{-q}\)
也被 \(2^{2n}\) 覆盖。

在 \(\alpha=1/2\) 处令
\[
 A_{q,s}=\prod_{h=q+1}^{s}\frac{2h-1}{2h}.
\]
则
\[
 \frac{U_j'(1/2)}2
 =-\sum_{q=1}^{s-1}2^{-q}\frac{A_{q,s}}q
                     \sum_{h=q+1}^{s}\frac1{2h-1}.       \tag{A5}
\]
逐个奇素数幂 \(p^e\) 考察 \(A_{q,s}/q\)。其分母中 \(p^e\)
倍数来自整数 \(q,\ldots,s\)，分子中来自 \(q+1,\ldots,s\)
内的残基 \(2h-1\equiv0\pmod{p^e}\)。两者计数之差至多1：
若 \(p^e\nmid q\)，就是同长度区间中两残基计数之差；若
\(p^e\mid q\)，额外的 \(q\) 只增加1，而其后的倍数残基
不会多于中间残基 \((p^e+1)/2\)。所以
\[
 v_p(A_{q,s}/q)\ge-\lfloor\log_p(2s)\rfloor.
\]
(A5)中的奇数调和和再至多花一份 \(d_{2n}\)，包括所有高次幂。
2处不作奇素数类比：第 \(q\) 项中
\[
 -v_2(2^{-q}A_{q,s}/q)
 =s+v_2\!\left(\frac{s!}{(q-1)!}\right)<2s<2n,
\]
而奇数调和和没有2处分母。故 \(B_n=2^{2n}d_{2n}^2\)
统一清整(A4)、(A5)及全部多项式头。这证明(A1)–(A2)。

更明确地，令 \(e_p(t)=\max\{e:p^e\le t\}\)。本证书矩阵倍数
\(S_m\) 的全部赋值是
\[
 v_p(S_m)=(48m-2){\bf1}_{p=2}
             +2e_p(8m-1)+2e_p(16m).                     \tag{A6}
\]
没有遗漏小素数、高次幂或2处；\(p>16m\) 不出现在此清整中。

## 3. 同一首一多项式的本原内容与评价

设 \(J_m=S_mR_m\in M_m(\mathbb Z)\)，定义
\[
 F_m(Z)=\det(J_m+S_mZI_m)=S_m^mQ_m(Z),\qquad
 c_m=\operatorname{content}(F_m).
\]
由于 \(F_m\) 的首项系数为 \(S_m^m\)，\(c_m\mid S_m^m\)，且
\[
 \lambda_m=S_m^m/c_m,\qquad P_m=F_m/c_m.                \tag{A7}
\]
这是确切的同一对象桥；本轮未求出 \(c_m\)，不能把(A6)当成
\(v_p(\lambda_m)\) 的下界。若 \(X=u/v,\ v>0\)，则
\[
 v^mP_m(X)=\frac{\det(vJ_m+S_muI_m)}{c_m}
\]
是严格正整数。这里的非零仍来自原实际Gram，不要求每个
有理 \(q\) 都使 \(Q_m(q)\ne0\)。

## 4. 安全包络的实际限制

仅为检验本证书的机会成本，给出同一Gram的下界。由(G5)的
\(B_1\) 方程，\(p_i\) 的最高 \(m\) 个系数恰为半个单位矩阵；
因此
\[
 \deg p_i=8m-1-i,\qquad\operatorname{lc}(p_i)=1/2.
\]
实际测度 \(\nu_n\) 满足
\(\nu_n\ge2^{-n}(1-T)\,dT\)。权 \((1-T)\,dT\) 的次数 \(k\)
首一Jacobi范数为
\[
 h_k=\frac1{2(k+1)\binom{2k+1}{k}^2}.
\]
按次数从 \(7m\) 到 \(8m-1\) 作Gram–Schmidt，每一步首项仍为
\(1/2\)，故
\[
 \det M_m\ge4^{-m}2^{-8m^2}\prod_{k=7m}^{8m-1}h_k,
 \quad
 \liminf m^{-2}\log\det M_m\ge-38\log2.                 \tag{A8}
\]
后一式用 \(\binom{2k+1}{k}\le2^{2k+1}\) 即得。

标准 \(\log d_r=r+o(r)\) 给
\[
 \log(S_m^m)=(48\log2+48)m^2+o(m^2).
\]
结合(A8)，这个**未经内容约分的安全倍数**
\(\Lambda_m=S_m^m\) 满足
\[
 \liminf m^{-2}\log(\Lambda_m\det M_m)\ge48+10\log2>0.
\]
因此本安全包络本身不能支付(G9)。这不否定最小 \(\lambda_m\)：
实际内容 \(c_m\) 未知，较紧的同对象清整也未被否定。
本结论只支持按原一轮任务共同结算，不把“所有有限处均有安全上界”
升级成负净预算，更不把该包络失败写成全部本原方法的no-go。
