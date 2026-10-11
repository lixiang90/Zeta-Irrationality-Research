# 第251轮：正号填叶的整数符号与一个真实无限稳定子

2026-10-10，A。实际 FULL 读冻结250全周期稿、250报告与当前policy；本轮只有纸证，数学程序0。支付固定period7的整数Fourier公式、两个整数填叶条件、全部Q+到达叶不填及实际二重提升，以及稳定子内的无限返回族。第4节核心binary-permutation方法由同伴C提供，本文独立展开核定。没有证明完整稳定子等于所给子群，不领取全图能量或新的数值定理。

## 1. 精确问题与已经固定的全参数范围

沿用χ=χ−7、s=√2、Γ*=Γ₀(14)+W14、T₀τ=τ+1，以及A250全部order2返回
\[
r(a,b,d)=\begin{pmatrix}14b&-a\\14d&-14b\end{pmatrix},
\quad ad-14b^2=1,\quad d>0\text{ 奇},\quad(d,7)=1.
\]
实际B=B_{g+}=A_+(I_+−g+)，g+=Y/2+sπ²/28，Y=L(2,χ)。A250已证明任一transported finite叶填点恰为
\[
q_{b,d}=0,\qquad D_{b,d}=1/8,                     \tag{P1}
\]
其中R(ζ_d^b)=Y/2+i√7π²q_{b,d}、D(ζ_d^b)=π²D_{b,d}。Q+对应χ(d)=−1；Q−对应χ(d)=+1。本文研究(P1)，不复做减号全部叶不填或其预算。

## 2. 任意d的固定七项整数Fourier公式

记Tχ(z)=N(z)/S7(z)，N=z+2z²+z³+2z⁴+z⁵、S7=1+z+⋯+z⁶。A250的唯一有限Fourier多项式c(z)=Σ_{k=0}^{d−1}c_kz^k满足S7c=N modulo z^d−1。这里可强化c_k∈(1/7)Z为一个完全显式的整数公式。

root filter与已付Abel有界性给
\[
c_k=\lim_{r\uparrow1}\sum_{m\ge1,\ m\equiv k\ (d)}\chi(m)r^m.
\]
将该series按7d周期写为有限numerator/(1−r^{7d})；numerator在r=1为0。因此一次L'Hopital是精确有限运算，给
\[
c_k=-\frac1{7d}\sum_{\ell=0}^{6}(k+\ell d)\chi(k+\ell d)
=-\frac{\chi(d)}7\sum_{\ell=0}^{6}\ell\chi(\ell+v_k),
\quad v_k\equiv kd^{-1}\pmod7.                   \tag{P2}
\]
k=0时χ(0)=χ(7d)=0，同一有限numerator仍有效。χ的一个完整周期和为0，故显示式的k项确实消去，不漏边界。

令v_k取0…6。Σ_{j=0}⁶jχ(j)=−7，以及ℓ↦j=ℓ+v_k mod7的精确换元给
\[
\boxed{c_k=\chi(d)f(v_k),\quad
 f(v)=1-\sum_{0\le j<v}\chi(j),\quad
 (f(0),\ldots,f(6))=(1,1,0,-1,0,-1,0).}           \tag{P3}
\]
这是一个通用公式的七个固定character值，不是按d搜索实验。特别c_k∈Z、c₀=χ(d)；也可由root平均直接得到c₀=limΣχ(dm)r^{dm}=χ(d)Tχ(r^d)→χ(d)。f(1−v mod7)=f(v)，故c_{d−k}=c_k；Σc_k=Tχ(1)=1。因此
\[
\sum_{k=1}^{(d-1)/2}c_k=(1-\chi(d))/2.            \tag{P4}
\]
这项是带符号的和；χ(d)=−1并不免费使所有非零c_k为正。

## 3. 正号填叶化为两个整数折叠符号

令[k]_d为0…d−1的代表。A250的Bernoulli三角差分与(P3)给
\[
L(b,d)=\sum_{k=1}^{(d-1)/2}c_k
 \min([bk]_d,d-[bk]_d)\in\mathbf Z,
\qquad\boxed{D_{b,d}=1/8-L(b,d)/d.}               \tag{P5}
\]
这里完整M=2L；整性与倍数2都已经付清。但L是signed folded sum，不能从(P4)推出L非零。

另一符号也可不保留大型Bernoulli双和。置
\[
F(x)=\sum_{a=1}^6\chi(a)B_2(\{a/7+x\}),\quad0\le x\le1.
\]
Σχ(a)a=−7、Σχ(a)a²=−49支付F(0)=0及初始斜率−2；每跨过x=1−a/7，斜率跳−2χ(a)。故完整函数为
\[
F(x)=-2x-2\sum_{a=1}^6\chi(a)(x-1+a/7)_+,
\qquad F(1-x)=-F(x).                             \tag{P6}
\]
对整数0≤k<d，定义
\[
U_d(k)=\frac{7d}{2}F(k/d)
=-7k-\sum_{a=1}^6\chi(a)(7k-d(7-a))_+\in\mathbf Z.
\]
将A250 q双和按j、d−j配对，奇d使两个signed terms相等，得到
\[
\boxed{q_{b,d}=-\frac{2}{49d}Q(b,d),\quad
Q(b,d)=\sum_{j=1}^{(d-1)/2}(-1)^{j+1}U_d([bj]_d)\in\mathbf Z.} \tag{P7}
\]
因此全部正号补支的exact criterion为
\[
\boxed{L(b,d)=Q(b,d)=0,\qquad ad-14b^2=1.}        \tag{P8}
\]
这给通用整数符号，消去了每个d要解循环保型矩阵的步骤。第4节将由真正的half-set permutation支付(-1)^L=χ(d)，不是从有限例子外推。mod2虽有Tχ≡zS7′/S7，但d奇时z∂z不保持理想(z^d−1)，不能在该有限商中免费微分推出此parity。

## 4. 全Q+不填的binary-permutation证明

这一方法由同伴C提出；以下给本文独立逐式核定的完整indices。取H={1,…,(d−1)/2}，x(k)=k mod2。因b mod d决定(P5)且d奇，可在同一个cusp选择b为奇数；b↦b+d仍保持a=(1+14b²)/d为奇数整数。对任一(u,d)=1定义
\[
P_u(k)=\min([uk]_d,d-[uk]_d),\quad
uk\equiv(-1)^{e_u(k)}P_u(k)\pmod d,\quad e_u(k)\in\{0,1\}.
\]
P_u是H的permutation。置P=P_b、Q=P₂、e=e_b，后缀表示函数composition：xP(k)=x(Pk)。signed代表乘法给
e_{uv}=e_v+e_uP_v mod2，且P_uP_v=P_{uv}=P_vP_u。

先从norm精确读c的parity。令r=[ak]_7，[ak]_7=[kd⁻¹]_7；
\[
\frac{2b^2k}{d}=\frac{ak}{7}-\frac{k}{7d}.
\]
0<k<d，最后项在0与1/7之间。若r=0，floor是ak/7−1；否则是floor(ak/7)。a奇，(P3)遂给c_k≡x(k)+floor(2b²k/d) mod2。再写bk=dN+(-1)^{e(k)}Pk；2bN为偶数，floor(−v)=−floor(v)−1（这里v=2bPk/d非整数）给
\[
\boxed{c\equiv x+e+eP\pmod2.}                  \tag{P9a}
\]
因为floor(2bPk/d) mod2恰e_b(Pk)，这个等式包括b负值，不漏负号边界。

对doubling，2k<d，直接有e₂=xQ。应用两种次序的signed乘法cocycle，
\[
e+eQ=xQ+xPQ=(x+xP)Q.
\]
所以v=x+xP=e+eQ⁻¹ mod2。将L=Σc_kP(k)代入(P9a)并以permutation重排，得
\[
L\equiv\langle x,xP\rangle+\langle e,x+xP\rangle
=\langle x,xP\rangle+\langle e,v\rangle\pmod2.
\]
任意两个same-weight binary vectors a、aR，其xor v的weight为偶数，且整数count满足⟨a,v⟩=|v|/2。分别对(x,xP)和(e,eQ⁻¹)用此恒等式，给⟨x,v⟩=⟨e,v⟩=|v|/2。因此
\[
\boxed{L\equiv|x|\equiv(d^2-1)/8\pmod2.}          \tag{P9b}
\]
最后一步可直接由|x|=floor((d+1)/4)按d mod8核定。

norm同时给χ(d)=(2/d)。确实任一odd primeℓ|d都满足−14b²≡1 modℓ、b是unit，故Jacobi(−14/d)=1。标准quadratic reciprocity将(−7/d)认作χ−7(d)，于是χ(d)(2/d)=1；补充律(2/d)=(-1)^((d²−1)/8)结合(P9b)得到
\[
\boxed{(-1)^L=\chi(d).}                          \tag{P9c}
\]
d=1时H为空、L=0、χ(1)=1，全部等式仍成立。χ(d)=−1时L奇，故(P8)不可能，不需同时解Q=0。A250完整odd gauge及全transported量词因此支付：g=g+时，两个Q+根的每个到达叶均保留非零首sqrt。

若合法holomorphic φ:D→C使native B∘φ单值meromorphic，它在Q+两根的每个前像都须偶阶。因此从native值1出发，平方根的winding均偶数，存在真正全盘holomorphic lift
\[
\boxed{w_+(0)=1,\qquad w_+^2=Q_+(\phi).}          \tag{P9d}
\]
不要求univalent或unique origin。但这只是genus-zero二重cover，不是whole-B的合法图分类；Q−所有填叶仍未分类，也未支付3λ+−J+预算。尤其native sqrt(Q+)第一系数为−7/2+2s，不是O_K整数，不能给免费τ0整数背景。

## 5. 实际完整稳定子包含Hecke自由积

定义真正的函数稳定子
\[
\mathcal S=\{N\in\Gamma^*:B(N\tau)=B(\tau)\text{ 对全部H成立}\}.
\]
R、D、A±是实际q函数，所以B(T₀τ)=B(τ)。完整Fricke身份在g=g+给B(Wτ)=B(τ)。这不要求g+代数；从而
\[
\boxed{G=\langle T_0,W\rangle\subset\mathcal S.}  \tag{P10}
\]
它是whole-function稳定子，不只是一个CM固定点值。

在z=√14τ中，T₀为z↦z+λ，λ=√14>2，W为z↦−1/z。取实边界的X_W=(−1,1)、X_T=(R∪{∞})\[−1,1]。所有非平凡T₀^n将X_W送入X_T，W将X_T送入X_W。交替cyclically reduced word将相应集合送到一个proper interval，故不是identity；conjugation不改变这一结论。这是直接ping-pong证明
\[
G\simeq\mathbf Z*C_2.
\]
自由积中cyclically reduced长度≥2的word各次幂长度严格增长；所以finite-order元素均共轭于factor，Z无torsion。因此G中的每个椭圆元素都是G内部的W共轭。这些实际填叶均在同一base分支点，即native小Q−根，不能让Q+填点。

以上没有证明S=G，也没有把S视为Γ*的normal subgroup。一般Γ*共轭会改变实际周期，不能凭一个W填点将其全部Γ*共轭免费加入S。

## 6. 一个全参数、无限d的精确填叶族

取任何k∈Z，N=WT₀^k∈G。直接2×2符号乘法给
\[
NWN^{-1}=\begin{pmatrix}-14k&-1\\14(14k^2+1)&14k\end{pmatrix},
\quad(a,b,d)=(1,-k,14k^2+1).                     \tag{P11}
\]
ad−14b²=1，χ(d)=1。固定点是
\[
N(i/\sqrt{14})=-k/(14k^2+1)+i/[\sqrt{14}(14k^2+1)].
\]
因为N、W都属于实际whole-function稳定子，这个返回对每一个整数k均填。A250 whole-return formula反过来给一项无限族恒等式
\[
\boxed{L(-k,14k^2+1)=Q(-k,14k^2+1)=0.}           \tag{P12}
\]
它完全由函数identity与一条符号矩阵式证明，无有限头/参数扫描外推。非零k给无穷多个d>1，故“只有d=1填叶”是错误的；但这个族全部属于同一W类，不能反驳“只有W类填”的更强命题。它亦不证明全部W类到达叶都填。

## 7. 本轮停止点与实际来源

本轮最强结果是(P3)、(P8)的全部参数整数结构，(P9a)–(P9d)全Q+bad/实际二重lift，以及(P10)–(P12)的真正无限稳定子/填叶证书。仍未支付的决定性关是Q−另一个branch class能否填、是否S=G，以及该实际全源对合法正图的3λ+−J+ upper或跨strict预算。仅genus-zero partial lift、G的freeproduct与无限填叶不提供任意合法正图的cap。全部Q+排除缩小了核心缺口，但不能将它包装成完整正处准入已经关闭或已过门槛。

依250policy，251不自动开启素数、map、word或分母搜索，也不因新封装推迟252正式复盘。本稿不是252方向报告；它如实给出有界关的paid与unpaid部分，无新的数值无理性/线性无关性结论。

本轮actual FULL读：A25010515 B/SHA256 94a9350f6da2408bdcae27ca7502292fe916b09156b81c3d3e9f646efdd88483；250报告5713 B/da0af6ac9f07b8db781ac8b0468854c78ff1a32dd7c8e1286bff583f4be6281a；当前policy17830 B/13cfc88007ce410415440713fd21bda2befceb3bbb0b00a67085138aa7c0ffcf。DLMF24.8.1、Gauss值、完整模性/Fricke/covering只复用冻结250明确输入及此前实际读域，本轮不宣称重新FULL上游原著或新增primary。所有新式均纸推，数学/CAS/scan/旧producer/Lean/git运行0。本人NEW251稿及scope保存后actual FULL作者复读再登记身份；不冒称独审，不写250及旧稿/main/policy/manifest/同伴文件。
