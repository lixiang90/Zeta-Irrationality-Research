# 第251轮：正处全叶奇偶性、圆锥提升与能量缺口

2026-10-10，Root，纸证与独立逐式核定。固定248–250的真实源、原坐标、完整三行和安全费用，不更换目标。本轮证明正号源在两个Q+根的全部运输到达叶均不可普通补点，因而任意合法正处图具有全盘圆锥提升；也证明上一轮导数无界的线性log图族全部达不到严格能量门槛。尚无新数值无理性或线性无关性定理。

## 1. 同一实际对象及通用整数周期

记s=√2、χ=χ−7、Y=L(2,χ)、K=Q(s)，实际目标为g+=Y/2+sπ²/28∉K。源为B+=A+(I+−g+)，I+=R+(2s/7)D，坐标t=(η1η14/(η2η7))⁴。250已付全部有限order2返回

\[
r(a,b,d)=\begin{pmatrix}14b&-a\\14d&-14b\end{pmatrix},\quad
ad-14b^2=1,\quad d>0\text{ 奇},\quad(d,7)=(b,d)=1.
\]

250的严格radial Abel公式及完整odd gauge给：对应正处叶可普通补点当且仅当q(b,d)=0、θ(b,d)=1/8；χ(d)=−1对应Q+两根，χ(d)=+1对应Q−两根。这个量词覆盖全部返回，不限四个指定矩阵。负处在假设g+∈K下全部有限叶不可填的证明保持冻结。

A251将250的循环系数强化为整数闭式。令[k]m为0至m−1代表，

\[
T(z)=\frac{z+2z^2+z^3+2z^4+z^5}{1+z+\cdots+z^6}
\equiv\sum_{k=0}^{d-1}c_kz^k\pmod{z^d-1},
\]
\[
c_k=\chi(d)f([kd^{-1}]_7),\qquad
f=(1,1,0,-1,0,-1,0).
\tag{R1}
\]

Root独立核定：root filter把c_k写成χ(m)r^m在m≡k mod d的Abel和；7d周期numerator在r=1为零，一次L'Hopital给−χ(d)Σℓχ(ℓ+v)ℓ/7。有限换元及Σjχ(j)j=−7给f(v)=1−Σj<vχ(j)，故(R1)对每个d成立，包括k=0。它不是由有限d样本推出的猜测。对称c_k=c_{d−k}、augmentation Σc_k=1于是给

\[
L(b,d)=\sum_{k=1}^{(d-1)/2}c_k\min([bk]_d,d-[bk]_d)\in\mathbb Z,
\qquad\theta(b,d)=1/8-L(b,d)/d.
\tag{R2}
\]

完整M=2L。R虚部也成为另一个整数条件：置F(x)=Σj=1..6χ(j)B₂({j/7+x})，则

\[
U_d(k)=\frac{7d}{2}F(k/d)
=-7k-\sum_{j=1}^6\chi(j)(7k-d(7-j))_+\in\mathbb Z,
\]
\[
Q(b,d)=\sum_{k=1}^{(d-1)/2}(-1)^{k+1}U_d([bk]_d),\qquad
q(b,d)=-2Q(b,d)/(49d).
\tag{R3}
\]

F(1−x)=−F(x)，奇d使原Bernoulli虚部双和配对后系数恰如(R3)。故全部正处填叶的精确条件是L=Q=0。这里L为带符号的折叠和；不能假定它非负。

## 2. 关键全参数奇偶证明

核心方法由C251提出，A251展开，Root独立核定以下完整链。取H={1,…,(d−1)/2}、x(k)=k mod2。对unit u mod d定义half permutation与sign bit

\[
P_u(k)=\min([uk]_d,d-[uk]_d),\qquad
uk\equiv(-1)^{e_u(k)}P_u(k)\pmod d.
\]

P_uP_v=P_uv，e_uv=e_v+e_u∘P_v mod2。因d奇，可用同一b mod d的奇数代表；a=(1+14b²)/d也是奇数。记P=P_b、Q₂=P_2、e=e_b，后缀表示composition。

首先a≡d⁻¹ mod7且f(r)≡r+1[r=0] mod2。由

\[
\frac{2b^2k}{d}=\frac{ak}{7}-\frac{k}{7d},\quad0<k<d,
\]

当[ak]7=0时floor下降1，否则不下降。a奇，故c_k≡x(k)+floor(2b²k/d)。再写bk=dN+(−1)^e(k)P(k)。floor(2bP(k)/d)的parity为e(P(k))，负号时floor多出一个奇数，得到

\[
c\equiv x+e+eP\pmod2.
\tag{R4}
\]

doubling满足e₂=xQ₂。对b与2用两种乘法次序的sign cocycle，给

\[
v:=x+xP=e+eQ_2^{-1}\pmod2.
\]

将(R4)代入L并用P重排求和，

\[
L\equiv\langle x,xP\rangle+\langle e,v\rangle\pmod2.
\]

同weight binary vectors a与aR的xor v满足⟨a,v⟩=|v|/2。分别用(a,R)=(x,P)、(e,Q₂⁻¹)，得到⟨x,v⟩=⟨e,v⟩，遂

\[
L\equiv|x|\equiv(d^2-1)/8\pmod2.
\tag{R5}
\]

norm条件给Jacobi(−14/d)=1；quadratic reciprocity与2的补充律给χ(d)=(2/d)=(−1)^((d²−1)/8)。因此

\[
\boxed{(-1)^{L(b,d)}=\chi(d).}
\tag{R6}
\]

d=1时H为空，L=0，结论仍成立。χ(d)=−1时L为奇数，因此θ≠1/8，无需再证明Q≠0。250的whole-return身份、exact odd gauge和actual覆盖量词于是支付：**两个Q+根的每个运输到达叶均有非零首sqrt通道**。这一步对实际g+本身成立，不依赖假设g+代数。

## 3. 真正正处圆锥提升及仍可填的无限族

任何合法全纯φ:D→C、φ(0)=0，使native完整正源单值亚纯，则Q+(φ)的每个零点均为偶阶。由单连通性和native值1，存在全盘全纯y，y(0)=1、y²=Q+(φ)。这与250负处的完整椭圆提升不同；正处目前只付圆锥。

置α=(7−4s)/2、β=√(1−α²)、x=arsinh(α/β)，βcosh x=1。圆锥Q+(t)=(t−α)²+β²的全部此类提升可精确写为

\[
w=(\phi-\alpha+y)/\beta\in\mathcal O(D)^\times,
\quad w(0)=e^{-x},\quad F=-\log(w/e^{-x}),
\]
\[
\boxed{F(0)=0,\quad\phi=\alpha-\beta\sinh(x+F),\quad
\phi'(0)=-F'(0).}
\tag{R7}
\]

w不为零来自(φ−α+y)(y−φ+α)=β²，log由单连通性支付。它是所有实际合法正图的必要结构，不能反推任意F已使whole-B合法。

Q−确实仍有无限填叶。actual q函数周期T:τ→τ+1和完整Fricke身份给G=〈T,W〉⊂Stab(B+)。在z=√14τ上，translation长√14>2与inversion的边界ping-pong给G≅Z*C₂。对任意整数k，N=WT^k有

\[
NWN^{-1}=\begin{pmatrix}-14k&-1\\14(14k^2+1)&14k\end{pmatrix},
\quad(a,b,d)=(1,-k,14k^2+1).
\tag{R8}
\]

N和W都稳定whole-B，故这些返回全部填；(R2)–(R3)反过来给L=Q=0。非零k给无限多个d>1。它们在同一native W/Q−分支类，不填Q+，不证明全部Q−叶都填，也不证明Stab(B+)=G。

## 4. 线性log族全部失败及一般图的准确缺口

250当前完整K模型rank3、两列(0,1,1)、安全τ=16/9保持。250负处J−≥2λ−、λ−<log(40/3)<8/3，使arch-only basic严格秩矛盾必要

\[
\lambda_+>4,\qquad \delta_+:=3\lambda_+-J_+>32/3-\lambda_->8.
\tag{R9}
\]

这仅是当前安全模型入口，不排除更优整型或真实有限处收益。

对(R7)的线性log族F(z)=Mz，M>0，φ_M′(0)=−M，导数无界。B251的同对象纸证由sinh差值公式及torus Haar换元给

\[
J_M\ge\log M-2\log2+(2\log2/\pi^2)M,
\]
\[
\boxed{\delta_M\le2\log(2\pi^2/\log2)-2<6<8.}
\tag{R10}
\]

Root独立核定：φ_M(z)−φ_M(w)=−2β sinh(M(z−w)/2)cosh(x+M(z+w)/2)；z=e^{i(u+v)},w=e^{i(u−v)}保持product Haar。sinh圆均值由零点±iπk的Jensen等于log R+2Σlog⁺(R/(πk))，只取k≤R/(2π)，cosh均值≥log cosh x，结合E|sin v|=2/π、Elog|sin v|=−log2即得。对M精确求sup及π²<10、log2>1/2、40<e⁴给严格6界，没有搜索。该族只满足必要圆锥提升，未认证whole-B合法；(R10)已足以排除族内任何可能的实际合法图。

对于一般F，归一化difference精确分解成三个全纯二变量因子，各在(0,0)为1：

\[
\frac{\phi(z)-\phi(w)}{\phi'(0)(z-w)}=
\frac{F(z)-F(w)}{F'(0)(z-w)}
\frac{\sinh U}{U}
\frac{\cosh(x+V)}{\cosh x},
\quad U=\frac{F(z)-F(w)}2,\ V=\frac{F(z)+F(w)}2.
\tag{R11}
\]

各因子两次Jensen的径向均值非负，故Jφ=λφ+Oφ，Oφ=OF+SF+CF≥0。S记录F(z)−F(w)=2πik（k≠0）的fiber，C记录F(z)+F(w)=−2x+iπ(2k+1)的fiber。要关闭全部当前入口，仍须在每个实际合法图、λφ>4时证明

\[
\boxed{O_F+S_F+C_F\ge2\log|F'(0)|-8.}
\tag{R12}
\]

或者构造一个whole-B实际合法图跨(R9)并付完整两处预算。线性族的rotation换元对任意F不成立，(R10)不能直接换成(R12)。三个量单独非负也没有付导数相关的强下界。

## 5. 不能免费加入的正背景

负处whole y²=E(t)在native坐标有整数Taylor系数，250因此取得τ0 rank2背景。正处sqrtQ+不相同。置a=7−4s，其唯一2-adic place为unit，规范v₂(2)=1。B251与Root逐式核定

\[
y_n=[t^n]\sqrt{1-at+t^2},\quad y_0=1,
\qquad\boxed{v_2(y_n)=-2n+s_2(n)\ (n\ge1).}
\tag{R13}
\]

展开sum k=ceil(n/2)..n，k=n项为binom(1/2,n)(−a)^n，估值−2n+s₂(n)。其它k=n−r项相对深度至少2r+s₂(k)−s₂(n)≥2r−s₂(r)≥1，故唯一最深项不抵消。prefix0..N的最小规范清分母深度恰2N−s₂(N)，严格递增，具有线性费用。固定scalar不能使它成为整数背景；不据此免费领取J+≥2λ+，也不将单行估值直接当全部模型最优τ。

## 6. 本轮结果与资源决定

本轮取得全Q+运输叶不填、actual正圆锥lift、无限真实填叶族、一个导数无界族的全参数能量失败及正背景的全n分母障碍。真正缩小了正处缺口，属于结构进展；没有付完整稳定子、任意合法正图的(R12)或(R9)的成功图。没有新数值定理。

250只授权251一个有界补完关。本轮尚未完成其全部能量核心，因此不自动续开本源map/word/prime/参数优化；252正式全局复盘按计划结束本安全Fricke源默认投入并比较其它明确数值出口。该决定不声称数学方法已全面不可能。本轮非正式复盘，248后第三完成轮，下一252，计数不重置。

数学程序/CAS/interval/Lean/prime/map/word/参数扫描0，新primary原文GET/下载0、外仓库Git修改0。C有一次二query检索，仅metadata/snippets，未采用其数学命题。实际FULL读域、作者自读及独立审查分别登记于本轮scope/唯一review；不将同伴消息或保存自读冒充上游全文认证。
