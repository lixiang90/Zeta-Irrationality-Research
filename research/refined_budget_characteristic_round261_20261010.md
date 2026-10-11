# 第261轮：固定 bare 关系的 Bost–Charles 精化入口审查

2026-10-10。对象固定为第259轮实际关系 tuple \(\{1,H,\theta_sH\}\)，实际 \(\mathbb Q(s)\)-rank3、两列安全 flag \((0,1,1)\)、\(e=0\)。本稿没有新的数值无理性或线性无关性定理。结论是：本轮新增的实两点完整坏芽，使所有所选 fixed-safe 的 §7–8 凸性精化入口在正分母条件之前关闭。不是全部算术 holonomy 或四项数值目标的否定。

## C1. 原文精化真正改了什么

Actual FULL 读固定 CDT v2 物理89–96、113–120、121–124页，视觉核物理92、123页公式。Definition7.1.2 定义的是同一 holomorphic \(\phi:(\mathbb D,0)\to(\mathbb C,0)\) 的

\[
 \widehat T(r,\phi)=\int_{\mathbb T^2}\log|\phi(z)-\phi(rw)|\,d\mu(z)d\mu(w),
 \qquad J=\widehat T(1,\phi).
\]

这里外侧圆周固定为1，不是把两变量同时缩到r。原文 meromorphic disc-map 的注脚明确需要另加 polar counting 项，且本节不处理那个接口。\(f_i\circ\phi\) 亚纯不能将 \(\phi\) 本身改为亚纯。

设 \(1=r_l>\cdots>r_0>0\)，\(\Delta_k=\log r_k-\log r_{k-1}\)，\(a_k=(\widehat T(r_k)-\widehat T(r_{k-1}))/\Delta_k\)。§7.1.6 与 §8.0.4 的合法 numerator correction 为

\[
 C_1=\frac1m\sum_{k=1}^l a_k^2\Delta_k,
\]

并继承 \(a_l\le m\) 及原定理条件。§7.6.4 与 §8.0.5 的合法 correction 为

\[
 C_2=\sum_{h=0}^{l-1}s_h^*\bigl(\widehat T(1)-\widehat T(r_h)\bigr),
\]

其中 \(s^*\) 必须是原文线性系统(7.6.5)的唯一解且所有分量非负、和为1。一般的非负权重不能冒充这个已陈述的定理；原文Remark7.6.7自己没有证明这个特殊系统对任意图都有所需解。

这些修正都只改 numerator。Theorems7.1.6、7.1.10、7.1.13及7.6.4明文继承7.0.1的条件。已知 holonomic 时也只把条件降到

\[
 \lambda=\log|\phi'(0)|>\tau(b;e).
\]

§8.0.1–8.0.5同样明文先要求 \(\lambda>\tau^{\flat\flat}(b)+\tau^\sharp(e)\)。物理123页该 holonomic 备选条件有排版残余符号；其紧邻主条件及所有分母清楚给出上述严格正分母。本稿不以排版残余另造一个允许负分母的定理。

当前两列均属 §§6–7 的 flag，Remark8.0.6给出

\[
 \tau^{\flat\flat}(b)=\tau^\flat(b)=2(1-1/9)=16/9,
 \qquad\tau^\sharp(0)=0.
\]

因此，若不另付整个实际 tuple 的新 type，选择更多 subradii、binomial metric或 \(s^*\) 不会自行改变16/9。原文某个14维成功算例也不能改变这里的实际三维对象。

## C2. 本轮新增的实两点完整坏芽

沿用已冻结259/260对象

\[
 r=1-2s,\qquad t=\frac{1-r^4}{9-r^4},\qquad
 p=t(1-t)(1-9t),
\]

\[
 \mathcal D_t=p\partial_t^2+p'\partial_t+3(-1+3t),\qquad
 \mathcal D_tH=b+\frac c{1-t}+d\frac{(3+r^2)^3}{32r(1+r^2)}.
\]

潜在数值关系系数 \(a,b,c,d\in\mathbb Q\)，且旧三项 CDT 线性无关使 \(d\ne0\)。在 \(r_0=\pm\sqrt3\) 的两个实点，\(t\) 有简单极点。令 \(u=1/t\)，\(\theta= u\partial_u\)，直接变换微分算子得准确恒等式

\[
 u\mathcal D_t=9(\theta-1)^2
 +u(-10\theta^2+10\theta-3)+u^2\theta^2.
\tag{C1}
\]

forcing 的常数为

\[
 F_0=b\pm\frac{9\sqrt3}{16}d\ne0.
\tag{C2}
\]

非零是有理系数与 \(\sqrt3\) 无理的实际后果，不是把 pole 当作坏芽，也没有借额外 pure 函数来迫这个常数。两个 forcing germs 在u处均解析。

(C1)的 indicial root1重复两次。其 homogeneous 正则解可取 \(U(u)=u(1+O(u))\)，另一解至多有 \(U\log u\) 项。更准确地，沿任一局部叶使用恒等式

\[
 \bigl(pU^2(H/U)'\bigr)'=U\,\mathcal D_tH
\]

（这里 prime仍为t导数）。因为 \(pU^2=9t(1+O(1/t))\)、\(U\mathcal D_tH=F_0/t+O(1/t^2)\)，两次积分给出

\[
 H=\frac{F_0}{18}\,u\log^2u+O(u\log u)+O(u^2\log^2u).
\tag{C3}
\]

任意两个到达解之差为 homogeneous 解，至多有一次log；因此(C3)的二次log首系数对全部到达叶不能取消。有限局部 ramification \(u=cz^e+\cdots\) 将首系数乘以 \(ce^2\)，仍非零。故任何非恒定 holomorphic 图使 \(H\circ\phi\) 亚纯，都必须省略

\[
 s_a=\frac{1-\sqrt3}{2},\qquad s_b=\frac{1+\sqrt3}{2}.
\tag{C4}
\]

这比260已付的复两点省略条件更早阻断当前 refined 入口；无需继续做十 cusp 的图搜索来得到本停止结论。

## C3. 同一合法图的 uniform size 上界

Actual FULL 读 Kim–Ma–Ma 2015 primary 保存的物理1–2页，曲率−1的单位盘密度为 \(2/(1-|z|^2)\)。其(1.2)、(1.3)及随后的Landau结论给，对 \(f:\mathbb D\to\mathbb C\setminus\{0,1\}\)，

\[
 |f'(0)|\le2|f(0)|\bigl(|\log|f(0)||+K\bigr),\qquad
 K=\frac{\Gamma(1/4)^4}{4\pi^2}.
\]

取 \(f=(\phi-s_a)/(s_b-s_a)\)。其 base值

\[
 x=f(0)=\frac{\sqrt3-1}{2\sqrt3}\in(0,1),
\]

且 \(|\phi'(0)|=\sqrt3|f'(0)|\)，故

\[
 |\phi'(0)|\le(\sqrt3-1)(-\log x+K).
\]

严格Gamma log-convexity在1与3/2中点给 \(\Gamma(5/4)^2<\sqrt\pi/2\)，从而 \(K<16/\pi<16/3\)。又有 \(\sqrt3>5/3\)、\(\sqrt3<7/4\)，故 \(x>1/5\)、\(\sqrt3-1<3/4\)，而 \(\log5<2\) 由 \(e^2>1+2+2+4/3>5\) 得到。因此

\[
 \boxed{|\phi'(0)|<\frac34\left(\frac{16}3+2\right)=\frac{11}2.}
\tag{C5}
\]

这是整个合法图类别的上界，不是某一个被选择图的测试值。\(e^{7/4}\)的0–4项正和为 \(34193/6144>33792/6144=11/2\)，故

\[
 \boxed{\lambda<\log(11/2)<7/4<16/9.}
\tag{C6}
\]

所以对当前 fixed-safe type，所有所选 §7–8 入口的分母都有严格上界

\[
 \lambda-16/9<-1/36<0.
\tag{C7}
\]

## C4. 精化准入决定与精确边界

本轮新增的是同一个 bare tuple 的(C3)全到达叶障碍及(C7)统一分母上界，而不是重抄260必要收益式。即使 \(C_1\) 或 \(C_2\)在某个图上很大，原文也不允许在负分母时使用其 rank quotient。**当前 fixed-safe refined admissible graph class为空**。无需为该空入口付 \(C_\phi\)数值上界；本稿没有谎称 \(C_\phi=0\)，也没有把 \(J\ge\lambda\)错施给 \(J-C_\phi\)。

如果未来另有同一完整 tuple 的 actual全前缀新 type把费用降为 \(16/9-\delta\)，仅为恢复正分母，已经必要

\[
 \delta>16/9-\log(11/2)>1/36.
\]

若最终仍用 \((J-C_\phi)/(\lambda-16/9+\delta)\)产生rank3矛盾，独立的必要条件还包括

\[
 3\delta+C_\phi>16/3-2\log(11/2)>11/6.
\]

这两个条件既不是已付减费或收益，也不是充分条件，不授权重开图搜索。有限处分支若没有新全尺度 type 证书，当前 fixed-safe refined窗口应结束；保留真实周期投影、最小 forcing 场、实际rank和整模型资产，转向有新 whole-source 准入机制的对象。结论不覆盖未陈述的 meromorphic-map 接口、不覆盖全部其它 metric/多图定理，也不否定四项数值线性无关本身。

本分支数学程序、CAS、数值、map/参数/prime/Padé扫描、旧producer、Lean与archive均为0。只执行定页文档提取、两页视觉查看及文档保存/身份统计。
