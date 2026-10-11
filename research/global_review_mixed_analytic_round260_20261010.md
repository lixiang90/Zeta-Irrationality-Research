# 第260轮：固定混合关系的解析收益上界

本轮为正式全局复盘的一部分。固定第259轮的实际来源、坐标和关系载体，不做图、参数、有限阶或数值搜索。结论限于 CDT v2 Theorem 7.0.1 的 **holomorphic 图、原始安全 type、未精化 (7.0.3)** 入口：该 bare rank3 入口关闭。不是全部 holonomy、精化 metric 或此四项线性无关目标的否定。

解析任务的原代理在完成局部纸证及取得 primary PDF 后连续三次发生 transport 断流，未交付最终稿。Root实际读取原文物理1–2页及 CDT 物理89–90页，独立完成并写入本稿；不将代理消息算成 Root 的原文阅读。

## A1. 同一对象与两点的全部到达叶

沿用259已付的

\[
 r=1-2s,\quad t=\frac{1-r^4}{9-r^4},\quad
 p=t(1-t)(1-9t),\quad
 \mathcal D_t=p\partial_t^2+p'\partial_t+3(-1+3t).
\]

实际关系为 \(H=A(a+bB_3+cC_3+dB_4)\)，\(d\ne0\)，且

\[
 \mathcal D_tH=b+\frac c{1-t}+dR_4,
 \qquad R_4=\frac{h}{p}=\frac{(3+r^2)^3}{32r(1+r^2)}.
\]

在 \(r_0=\pm i\)，\(t=0\)，有 \(dt/dr=r_0/2\)，\(dt/ds=-r_0\)。计算 \(R_4\) 在 \(r\) 的 residue 为 \(-1/8\)，因此它在 \(t\) 的 residue 为 \(-r_0/16\)。其它两项 forcing 在这里解析。记完整 forcing 的 residue

\[
 \rho=-\frac{d r_0}{16}\ne0.
\]

\(t=0\) 是 homogeneous 方程的 double-zero indicial regular singularity，存在解析解 \(U(0)=1\)，另一解为 \(U\log t+V\)，\(V\) 解析。直接用 \(\mathcal D_tU=0\) 得到准确的 variation identity

\[
 \bigl(pU^2(H/U)'\bigr)'=U\bigl(b+c/(1-t)+dR_4\bigr).
\]

右边为 \(\rho/t+O(1)\)，且 \(pU^2=t(1+O(t))\)。连续两次积分使每个局部解含有

\[
 H=\frac{\rho}{2}U(t)\log^2t+O(\log t)+O(t\log^2t),
 \qquad \frac\rho2=-\frac{d r_0}{32}.
\]

任意两个到达解的差是 homogeneous 解，至多含一次 log，故这个二次 log 首系数对 **所有到达叶** 一致，不能通过换路径取消。若有限 ramification 为 \(t=cz^e+\cdots\)，首系数变为 \(-d r_0e^2/32\)，仍非零。也可将假设的 meromorphic Laurent 解代入 \(t\mathcal D_t=\theta_t^2+O(t)\)：负阶项不可能匹配右边的非零常数，无负阶解又不能产生该常数。

因此任何令 \(H\circ\phi\) meromorphic 的非恒定 holomorphic 图都必须省略

\[
 s_+=\frac{1+i}{2},\qquad s_-=\frac{1-i}{2}.
\]

不必完成其它八个潜在 cusp 的分类才能取得这项必要条件。forcing 的任意 pole 并不一般自动等于实际坏芽；这里已付的是具体非零 log² 的完整局部证明。

## A2. 原文 Landau 界与归一化

Primary：Kim–Ma–Ma, *Estimates of the hyperbolic metric on the twice punctured plane*, Ann. Acad. Sci. Fenn. Math. 40 (2015), 875–887，DOI [10.5186/aasfm.2015.4058](https://doi.org/10.5186/aasfm.2015.4058)。本轮实际读取物理1–2页。原文采用曲率−1，单位盘密度 \(2/(1-|z|^2)\)，(1.2) 为

\[
 K=\frac{\Gamma(1/4)^4}{4\pi^2}.
\]

(1.3) 及其紧随的 Landau 结论，对 holomorphic \(f:\mathbb D\to\mathbb C\setminus\{0,1\}\) 给

\[
 |f'(0)|\le 2|f(0)|\bigl(|\log|f(0)||+K\bigr).
\]

CDT Theorem 7.0.1 **明文要求 holomorphic \(\phi:(\mathbb D,0)\to(\mathbb C,0)\)**；meromorphic 的是 \(f_i\circ\phi\)，没有混同两者。若另用 meromorphic \(\phi\) 的不同接口，两有限省略值不能直接给本界，需另付证书。

取 \(f=(\phi-s_+)/(s_--s_+)\)。因两省略值距离为1，\(|f'(0)|=|\phi'(0)|\)，\(f(0)=(1-i)/2\)，模为 \(1/\sqrt2\)。故

\[
 |\phi'(0)|\le\sqrt2\left(K+\frac{\log2}{2}\right).
\]

本稿不用十进制数值认证。Gamma 正积分的严格 Hölder/log-convexity，在1与3/2的中点给

\[
 \Gamma(5/4)^2<\Gamma(1)\Gamma(3/2)=\frac{\sqrt\pi}{2}.
\]

由 \(\Gamma(1/4)=4\Gamma(5/4)\) 得 \(K<16/\pi<16/3\)。再用 \(\sqrt2<3/2\)、\(\log2<1\)，得到充分的粗界

\[
 \boxed{|\phi'(0)|<35/4.}
\]

这是整个合法 holomorphic 图类别的上界，不是某个被挑选图的计算；没有 map scan、CAS 或数值程序。

## A3. 与已付安全费用的矛盾

第259轮 bare \(\{1,H,\theta_sH\}\) 已付实际 rank3、全前缀 \(d_N^2\)、两列 \((0,1,1)\)，\(e=0\)，\(\tau=16/9\)。这些资产复用，不新增 product-formula 的行列式无限非零义务。

令 \(\lambda=\log|\phi'(0)|\)，\(J=\int_{\mathbb T^2}\log|\phi(z)-\phi(w)|\)。未精化 (7.0.3) 要形成 rank3 矛盾，必须有

\[
 3(\lambda-16/9)>J.
\]

对 standing 条件下的 holomorphic 图，两次 Jensen 给 \(J\ge\lambda\)。故必要 \(\lambda>8/3\)。但 A2 给 \(\lambda<\log(35/4)<9/4<8/3\)。其中 \(e^{9/4}>35/4\) 由其 Taylor 的0–5项正和严格证明：该和为 \(377983/40960>358400/40960=35/4\)。0–4项尚差 \(5/2048\)，不使用那个不足的截断。因此没有图能通过这个固定 safe/unrefined 入口，额外分类或图优化不能改变决定。

同一未精化入口若仅改善有限处费用，必要

\[
 \tau_{\rm new}<\frac23\log(35/4).
\]

相对当前 \(16/9\)，必要节省严格大于
\(16/9-(2/3)\log(35/4)>5/18\)。这只是必要改进幅度，既不是已付的精化费用，也不是严格能量充分证书。改变原文 archimedean/convexity interface 时必须重列完整账本，不能把此必要式强加给另一个定理。

## A4. 本轮决定

停止 fixed bare rank3、\(\tau=16/9\)、\(e=0\)、holomorphic 图及 (7.0.3) 的默认实现窗口。保留真实周期投影、全坏芽、最小 forcing 场、全前缀及实际 rank 资产。没有证明四项数值线性无关，也没有证明全部 CDT 方法不可能。扩充 pure 族及其独立的同对象费用另由本轮 arithmetic 稿结算；本稿不从九germ生成上界领取其独立性或 type。
