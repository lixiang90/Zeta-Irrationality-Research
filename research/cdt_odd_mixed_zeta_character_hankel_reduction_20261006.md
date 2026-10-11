# 改变目标表示：混合奇ζ值与角色迹的Hankel归约

日期：2026-10-06。本轮NEW纸面推导，不执行任何数学producer或外部Lean代码。

当前R₀九行packet的全部origin路径受到真实模8障碍。继续寻找同一packet的filled-origin路径不能突破这个障碍。本稿改变目标表示：直接把待研究常数写进有理矩泛函的整多项式，而不是先要求旧周期packet在原点亚纯。

本稿已证的是精确矩身份、目标值身份、整化的存在、解析上界的转移及一个条件归约；H9另证明double-pole布局在全部固定weight s≥4的无穷非零子序列。**尚未证明新布局的整化费用与匹配衰减，因此没有新的特殊值无理性或线性无关性定理。** simple-pole布局的素数非消失亦未证。它也不是“统一解决全部奇ζ”的证明。

## H1. 新一手来源与证据范围

正常TLS归档作者公开源码，固定到读取时的immutable commit：

- [Qian Tang，1、ζ(2)、ζ(3)线性无关性项目](https://github.com/dtq1997/zeta2-zeta3-linear-independence)，commit `669c92bf7a3728e0de9ad80c373bc29fb5ca3d58`。
- [Si-Qi Liu，有理点Li₂项目](https://github.com/siqiliu-tsinghua/Li2Rational)，commit `b2a61c46c157860b57faa163341fda725c629139`。

共22份README/Lean源文件、116874 bytes保存于literature的两个独立source目录；[来源收据](../literature/manifest_cdt_odd_2026_polylog_primary_sources_20261006.json)逐项登记URL、commit、SHA与actual reading scope。没有把源码文件算成PDF文献，没有执行或编译其代码。

Tang的Family/Interfaces/Assembly/Criterion/PrimeObstruction明确给出以下结构：布局(4,5,3)，有理Hankel行列式、primitive整化、解析node −6、算术node 283/50，以及无穷素数上的primitive多项式模p为非零常数。Assembly是“三个nodes蕴涵结论”的总装；其声明不代替未逐一核查的全部依赖证明。repo最终线性无关性和Lean验证是作者报告，**本项目没有独立完成其完整内核重验**。

Liu的RationalCheck是原始级数陈述；RationalCriterion对参数范围保留严格算术/解析margin。归档与部分源码阅读不等于本项目证明这些外部结果或其新颖性。

下述H2–H8是本项目直接推导，涉及输入和缺口分别列明。

## H2. 一个实际解析矩泛函

令
\[
 t(y)=\tfrac12+iy,\qquad \rho(y)=\frac{\pi}{2\cosh^2(\pi y)},\qquad
 J_a(f)=\int_{\mathbf R} f(t(y))i^a\rho^{(a)}(y)\,dy.
 \tag{H2.1}
\]
这里a为固定非负整数，f为在该直线上无极点且在无穷至多多项式增长的有理函数。全部积分绝对收敛，所有分部积分boundary项为零，故
\[
 J_a(f)=\int_{\mathbf R} f^{(a)}(t(y))\rho(y)\,dy. \tag{H2.2}
\]
符号来自 \(i^a(-1)^ai^a=1\)，不是把y导数和t导数混用。

为独立核对矩身份，记 \(I(u)=\int\rho(y)e^{-iuy}dy\)。u>0时沿高度−i的矩形积分 \(\rho(z)e^{-iuz}\)：ρ的周期为i，唯一double pole为−i/2，其principal part为 \(-1/(2\pi(z+i/2)^2)\)。顺时针residue给
\[
 (1-e^{-u})I(u)=u e^{-u/2},\quad
 I(u)=\frac{u}{2\sinh(u/2)}.
\]
两vertical边因sech²而消失；u=0由 \(\int\rho=1\) 的极限得到。因此
\[
 \int \rho(y)e^{-ut(y)}dy=\frac{u}{e^u-1}\quad(u\ge0). \tag{H2.3}
\]

对j≥1、k≥1，Re(t+j)>0。Laplace表示与Fubini（绝对值积分有限）给
\[
 \int\frac{\rho(y)}{(t(y)+j)^k}dy
  =\frac1{(k-1)!}\int_0^\infty
       \frac{u^k e^{-ju}}{e^u-1}du
  =k\bigl(\zeta(k+1)-H_j^{(k+1)}\bigr),
 \quad H_j^{(v)}=\sum_{m=1}^j m^{-v}. \tag{H2.4}
\]
此外 \(\int\rho e^{ut}=u e^u/(e^u-1)\) 在0附近成立，故
\[
 J_0(t^m)=B_m(1)\in\mathbf Q,\qquad
 J_a(t^m)=\frac{m!}{(m-a)!}B_{m-a}(1)
 \ (m\ge a), \tag{H2.5}
\]
而m<a时为0。此处Bernoulli convention以生成函数固定，B₁(1)=1/2。

## H3. 直接隔离ζ(s)−rζ(s−1)

固定奇数s≥5和r∈Q。定义
\[
 K_{s,r}=i^{s-2}\rho^{(s-2)}+(s-1)r i^{s-3}\rho^{(s-3)},\qquad
 \mathcal J_{s,r}=J_{s-2}+(s-1)rJ_{s-3},\qquad
 \xi_{s,r}=\zeta(s)-r\zeta(s-1).
 \tag{H3.1}
\]
由H2.2–H2.4，a≥1时
\[
 J_a\left(\frac{t}{t+j}\right)
 =(-1)^{a+1}(a+1)!j
        \bigl(\zeta(a+2)-H_j^{(a+2)}\bigr).
\]
所以准确地
\[
 \boxed{\mathcal J_{s,r}\left(\frac{t}{t+j}\right)
 =(s-1)!j\left(\xi_{s,r}-H_j^{(s)}+rH_j^{(s-1)}\right).}
 \tag{H3.2}
\]
全部其余polynomial moments是有理数。s=5的核是 \(-i\rho'''-4r\rho''\)，s=7是 \(i\rho^{(5)}+6r\rho^{(4)}\)。这改变目标值身份；不是宣称这些核已经有足够的算术性质。

s=3需单独保留J₀的常数项。核 \(i\rho'+2r\rho\) 给
\[
 2j(\zeta(3)-r\zeta(2))-2jH_j^{(3)}+2rjH_j^{(2)}+2r,
\]
与归档Tang Family/Interfaces完全一致，作为本归约的低阶校准。

## H4. 可明确写出的目标多项式

可先取Tang的有理布局
\[
 D_m(t)=\prod_{j=1}^m(t+j),\quad
 R_n(t)=\frac{D_n(t)^4}{D_{5n}(t)},\quad h_n=3n,
 \quad R_{n,k}(t)=t^kR_n(t).
\]
每个R_{n,k}均具有Q上的精确partial fraction
\[
 R_{n,k}(t)=P_{n,k}(t)+\sum_{j=1}^{5n}\frac{a_{n,k,j}}{t+j},
 \quad P_{n,k}\in\mathbf Q[t],\ a_{n,k,j}\in\mathbf Q.
\]
从H3.2定义有理仿射多项式
\[
 \mu_{n,k}(X)=\mathcal J_{s,r}(tP_{n,k})
 +(s-1)!\sum_j j a_{n,k,j}
       \left(X-H_j^{(s)}+rH_j^{(s-1)}\right),
\]
则**真实目标身份**为
\[
 \mu_{n,k}(\xi_{s,r})=\int t(y)^{k+1}R_n(t(y))K_{s,r}(y)dy.
 \tag{H4.1}
\]
因此
\[
 Q_{n,s,r}(X)=\det[\mu_{n,i+j}(X)]_{0\le i,j<h_n}\in\mathbf Q[X],
 \quad\deg Q_{n,s,r}\le h_n. \tag{H4.2}
\]
对非零Q取其唯一正有理倍数d_nQ使之成为选择正比例方向的primitive整系数多项式P_n；Q=0时置P_n=0。整化存在来自Q[X]的有限系数和gcd，**它并未给出log d_n的上界**。不得把原Tang weight3的content费用283/50原封不动移到新weight。

Rn和h可改成其他固定布局；每次改变都须重证下面的两种算术输入。

## H5. 解析衰减的可转移部分

ρ的每阶导数除以ρ是tanh(πy)的一个多项式。归纳使用
\(\rho'/\rho=-2\pi\tanh(\pi y)\)、\((\tanh\pi y)'=\pi(1-\tanh^2\pi y)\)，故固定s,r时存在有限C_{s,r}>0使
\[
 |K_{s,r}(y)|\le C_{s,r}\rho(y)\quad(y\in\mathbf R). \tag{H5.1}
\]
Andreief/Heine在本例可直接由有限det展开和Fubini证明；多项式增长加exponential tails使所有展开项绝对可积。由于t_i−t_j=i(y_i−y_j)，得到
\[
 |Q_{n,s,r}(\xi_{s,r})|
 \le\frac{C_{s,r}^{h_n}}{h_n!}
 \int_{\mathbf R^{h_n}}
    \prod_i |t_iR_n(t_i)|\rho(y_i)
    \prod_{i<j}(y_i-y_j)^2\,d\mathbf y.
 \tag{H5.2}
\]
如果右侧positive-envelope积分连同所选normalization已有严格D²级energy上界，那么换成任何固定s,r只增加h_n log C=O(n)，不改变该**上界**的n²主指数。

更具体，Tang r=1的kernel为 \(w_1=2\rho+i\rho'\)，\(|w_1|\ge2\rho\)。所以其已定义Heine bound的absolute integrand逐点控制本稿positive envelope，差因子至多 \((C_{s,r}/2)^{h_n}\)。这是实际不等式；将外部完整energy proof或其−6常数当作输入时需另外核完整证明，不能仅依据Assembly node定义宣告本项目已经验证−6。

**这里仅转移解析上界。没有转移非零性、content估计、任意s同时一致的常数，也没有结论“高weight与weight3一样容易”。**

## H6. 明确的条件无理性归约

设选择正有理normalization \(\widetilde Q_n=c_nQ_n\)、c_n>0，及 \(P_n=\widetilde d_n\widetilde Q_n\in\mathbf Z[X]\)、\(\widetilde d_n\in\mathbf Q_{>0}\)。若对固定s,r证明：

1. \(\deg P_n\le Cn\)，且 \(\log\widetilde d_n\le A n^2+o(n^2)\)（非零Q时）；
2. \(|\widetilde Q_n(\xi_{s,r})|\le\exp(-B n^2+o(n^2))\)，B>A；
3. 对每个v∈Q有无穷n使P_n(v)≠0；

则ξ_{s,r}无理。证明：若ξ=a/b∈Q，\(b^{\deg P_n}P_n(a/b)\) 是整数；沿条件3的无穷n非零，故绝对值≥1；但条件1–2给其绝对值≤exp(−(B−A)n²+O(n)+o(n²))→0，矛盾。

一个足够的条件3是无穷素数p上 \(P_{p-1}\bmod p\) 是非零常数，且p避开v的分母。原Tang证明 precisely 做了这个额外的局部算术工作；仅“primitive”不能保证它，Heine积分含complex signed kernel亦不能保证其正性。

本稿尚未证明新weight的A或条件3。r=0、s=5只是已有ζ(5)结果的新表示，不计本项目新结论。优先的非重复目标为ζ(5)−rζ(4)的统一无理性（r∈Q）；若全r且包括r=0可达，再结合ζ(4)无理性得到1、ζ(4)、ζ(5)的Q线性无关性。此目标是否已有公开证明仍需专项文献核查。

## H7. 有理角色的精确目标迹

令χ为mod q的Q值非平凡Dirichlet角色，β_a=a/q，1≤a≤q。改用
\[
 t_\beta(y)=\beta-\tfrac12+iy,\qquad
 J_{b,\beta}(f)=\int f(t_\beta(y))i^b\rho^{(b)}(y)dy.
\]
对j≥1仍有Re(t_β+j)>0。H2的同一Laplace论证严格给
\[
 \int\frac{\rho}{(t_\beta+j)^k}dy=k\zeta(k+1,j+\beta),
 \qquad J_{0,\beta}(t_\beta^m)=B_m(\beta)\in\mathbf Q.
 \tag{H7.1}
\]
ζ(s,j+β)=ζ(s,β)−Σ_{l=0}^{j−1}(l+β)^−s，后者的有限和是有理数。采用
\[
 \mathcal T_{s,r,\chi}(f)=\sum_{a=1}^q\chi(a)
  \bigl(J_{s-2,\beta_a}(f)+(s-1)rq J_{s-3,\beta_a}(f)\bigr)
\]
得到simple-pole的准确系数
\[
 \boxed{\mathcal T_{s,r,\chi}(t/(t+j))
  =(s-1)!j q^s\bigl(L(s,\chi)-rL(s-1,\chi)\bigr)
       +\text{明确有理有限和}.} \tag{H7.2}
\]
用到的exact角色身份为 \(\sum_a\chi(a)\zeta(v,a/q)=q^vL(v,\chi)\)。多项式部分仍有理。于是同H4可造degree≤h的Q目标多项式。

H7.2对奇s≥5如写；s=3按H3的J₀常数项补入有理intercept后同样成立。可以选择even quadratic χ的L(3,χ)为非critical目标，也可以把s=3、odd χ的L(2,χ)放进类似构造以涉及Catalan型目标。这里没有证明这些值无理。

**角色版本不能直接套H5的单直线Δ(y)²积分。** determinant展开面对多个水平实部不同的t_β轮廓；同一measure的Vandermonde是Δ(t)，跨轮廓时不等于i次幂Δ(y)。因此角色迹除全素数content/非消失以外，还须证明多轮廓的energy上界。固定q或有限χ求和并未自动解决这个步骤。

## H8. 下一轮的可检验任务

对simple-pole布局固定s=5，从residue-class pulled moments计算其actual p-adic leading blocks，要求证明全部尺度的content上界并展示无限p上parameter多项式的非零leading reduction。H9追加后优先研究已经有无穷非零子序列的double-pole布局的全部尺度分母费用。若算术主费用已超过positive-envelope衰减，则改变布局；不得用有限n数值衰减推全n。

角色路线先完成H7多轮廓Andreief与energy问题，再选择χ和parity。parity-matching L值化为π的幂的已知结论不计新结果；保留odd s/even χ等真正未解决目标。与CDT的连接在于相同的真实目标投影、全部place费用、D²解析收益以及独立的非消失条件；本稿没有把这个行列式判据冒称为现成arithmeticholonomy定理。

本轮root没有数学producer执行，外部代码执行/Lean编译0；已有及同行producer执行/import/rerun0。旧冻结文件保持不变。独立审阅另存，不把作者回读算作独审。

## H9. 新Lai一手预印本与全固定weight的非零归约

本稿初稿后专项检索发现[Li Lai预印本](https://arxiv.org/abs/2610.06838)，2026-10-05 17:58:29 UTC上传的v1，准确目标是1、ζ(3)、ζ(4)，不是1、ζ(4)、ζ(5)。[实际原件](../literature/lai2026_linear_independence_1_zeta3_zeta4_arxiv2610_06838v1_20261006.pdf)25页，SHA `838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58`；[独立来源收据](../literature/manifest_cdt_odd_lai2026_mixed_zeta_20261006.json)登记版本和实际读取。root本轮实读PDF1–7、20–23，未称全文独验。

PDF2–6使用double-pole同时逼近、auxiliary primes与Hermite basis。PDF20–22保留一个显式real upper bound；其简介的31.6概述和Proposition6.6显示的保守−31界不能混称为同一个已核严格式。本项目不把其1、ζ(3)、ζ(4)结果列为自己的新结论。下述是对其非零机制的直接全weight推导，算术费用另缺。

固定整数s≥4及整数a,b,c，b≠0。设候选关系
\[
 a\zeta(s-1)+b\zeta(s)=c. \tag{H9.1}
\]
定义与Lai相同的double-pole layout（这里记为\(\mathscr R\)，区别H4的simple-pole R）
\[
 \mathscr R_n(t)=\frac{(6n)!^2}{(2n)!^3}
     \frac{(t-2n)_{2n}^3}{(t)_{6n+1}^2},\quad h_n=3n,
\]
\[
 \mathscr L_{n,s}(P)=(-1)^{s-3}(s-1)a
       \sum_{m\ge1}(\mathscr R_nP)^{(s-3)}(m)
      +(-1)^{s-2}b
       \sum_{m\ge1}(\mathscr R_nP)^{(s-2)}(m).
 \tag{H9.2}
\]
对degP<6n，deg(\(\mathscr R_nP\))≤−3，级数绝对收敛；finite partial fractions与求导/求和可以交换。设
\[
 W_j=\binom{6n}{j}^2\binom{2n+j}{j}^3,\quad
 C_j=5H_j-3H_{2n+j}-2H_{6n-j}.
\]
实际partial fraction系数为A₂,j=W_jP(−j)、A₁,j=W_j(P'(−j)+C_jP(−j))，且ΣA₁,j=0。这最后一个等式来自无穷处deg≤−3。对任意d≥1，
\[
 \sum_{m\ge1}(\mathscr R_nP)^{(d)}(m)
 =(-1)^d\sum_j\left[d! A_{1,j}(\zeta(d+1)-H_j^{(d+1)})
 +(d+1)!A_{2,j}(\zeta(d+2)-H_j^{(d+2)})\right].
\]
ΣA₁,j消去两种较低ζ值，H9.1消去其余目标，故
\[
 \mathscr L_{n,s}(P)=\sum_{j=0}^{6n}W_j
    \bigl(U_jP'(-j)+V_jP(-j)\bigr)\in\mathbf Q,
 \tag{H9.3}
\]
\[
 U_j=-(s-1)a(s-3)!H_j^{(s-2)}-b(s-2)!H_j^{(s-1)},
\quad V_j=C_jU_j+(s-1)!\bigl(c-aH_j^{(s-1)}-bH_j^{(s)}\bigr).
\]
定义有理bilinear form \(\mathscr B_{n,s}(P,Q)=\mathscr L_{n,s}(PQ)\)，degP,Q<3n，及normalized determinant
\[
 \mathscr J_{n,s}=\frac{\det[\mathscr B_{n,s}(t^i,t^j)]_{0\le i,j<3n}}
                         {\prod_{i=0}^{3n-1}i!^2}\in\mathbf Q.
\]

**定理H9。** 对每个固定s≥4及a,b,c∈Z、b≠0，若按H9.3定义有理form（不要求数值关系H9.1真的成立），则对每个素数p=9m+1，p>max(s,|b|)，有 \(\mathscr J_{2m,s}\ne0\)。因此有无穷非零n。H9.1仅用于把这个有理form识别为实际解析级数。

证明：在deg<6m的空间取Hermite basis。令
\[
 F_k(t)=\prod_{0\le l<3m,l\ne k}\frac{t+l}{l-k},\quad c_k=F_k'(-k),
 \quad P_k=p^2(1-2c_k(t+k))F_k(t)^2,
 \quad Q_k=p(t+k)F_k(t)^2.
\]
所有F_k,c_k在Z_p，因为0<|l−k|<p。它们满足
P_k(−l)=p²δ_kl、P_k'(−l)=0、Q_k(−l)=0、Q_k'(−l)=pδ_kl，故构成Q上的basis。

先令n=2m。j<p时，各H_j^{(v)}在Z_p，而C_j∈p^−1Z_p，所以U_j∈Z_p、V_j∈p^−1Z_p。每个basis polynomial及其导数至少在pZ_p[t]，故每个local bilinear contribution在pZ_p。乘上p^{s−4}后仍在pZ_p。

其余j=p+l，0≤l<3m。注意12m<2p、4m+j<2p、12m−j<p，故
\[
 H_j^{(v)}=p^{-v}+O(Z_p),\quad C_j=2p^{-1}+O(Z_p),\quad W_j\in Z_p^\times.
\]
W_j的unit可直接用Lucas：\(\binom{12m}{p+l}\equiv\binom{3m-1}{l}\)、\(\binom{4m+p+l}{p+l}\equiv\binom{4m+l}{l}\pmod p\)，两者下方factorials都小于p。

记u=(s−2)!b，是p-unit，则
\[
 U_j=-u p^{-(s-1)}+O(p^{-(s-2)}Z_p),\qquad
 V_j=-(s+1)u p^{-s}+O(p^{-(s-1)}Z_p).
 \tag{H9.4}
\]
Taylor在−l给
\[
 P_k(-j)=p^2\delta_{kl}+O(p^4),\quad P_k'(-j)=O(p^3),
\]
\[
 Q_k(-j)=-p^2\delta_{kl}+O(p^3),\quad Q_k'(-j)=p\delta_{kl}+O(p^2).
\]
代入H9.3的product derivative，**缩放整个form为p^{s−4}\(\mathscr B\)**，所有误差在pZ_p，得到modp的block diagonal matrix，其第l个block为
\[
 \boxed{uW_{p+l}\begin{pmatrix}-(s+1)&s\\s&-(s-1)\end{pmatrix}.}
 \tag{H9.5}
\]
每个block的det是 \(-u^2W_{p+l}^2\)，因为(s+1)(s−1)−s²=−1，故都是unit。缩放form、basis变化和factorial normalization都是非零有理倍数，不改变“det≠0”。Dirichlet对p≡1 mod9给无穷这样的素数，证明完毕。

s=4时block为2bW[[-5,4],[4,−3]]，正好恢复Lai的[[-10b,8b],[8b,−6b]]W。s=5及s=7也满足同一个unit determinant机制。因此，**对这个double-pole新目标family，非零子序列缺口已补；尚缺的是严格全素数分母费用与匹配解析界**。不把H4 simple-pole多项式的非消失自动视作H9的结论，两种布局和normalizations不同。

下一轮先选s=5、a=−rD、b=D（D清r和候选ξ的分母）并计算double-pole local minors全尺度费用。Lai weight4的30.83不得直接沿用：H_j^{(s)}、fixed derivative order、全p residue grouping均已改变。s=7或χ版本另付费用。H9是可复核的内部推广lemma，是否作为单独数学命题已有先例尚未调查，不宣称它是已发表新定理。
