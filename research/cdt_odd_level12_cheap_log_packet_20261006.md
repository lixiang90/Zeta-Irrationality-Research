# D12 三尖点log背景：实际秩13/23与合法低成本数组

日期：2026-10-06。新证明稿，不修改或执行任何冻结producer。本文利用当前source已经必须省去的三个nonzero finite cusp值，构造实际独立的多log背景。它改变此前一个log加平方根背景的账本，并在两个预先固定的degree族上给出CDT任意矩阵的严格安全成本。**没有算出所需真实地图的conformal radius/J，没有证明L(3,χ12)无理。**

输入是 [真实配对坐标和rank4](cdt_odd_level12_paired_coordinate_20261006.md)、[实际fullleaf §§5–7](cdt_odd_level12_full_leaf_20261006.md)、[pure-L完整算术](cdt_odd_level12_source_denominators_20261006.md)。原文使用 [CDT固定218页版](../literature/cdt2024_l2_chi_minus3.pdf) Theorem8.0.1 / (8.0.2) / Remark8.0.6，pp122–124；数域闭合系统分支见 [已审任意矩阵引理](cdt_odd_level20_arithmetic_20261006.md) §6。本文不把两个embedding的rank相加。

## 1. 三个真实log芽及全阶K算术

令r=√3、K=Q(r)、a=2+r（另一embedding为σa=2−r），以及

\[
z_+=(a+i)/2,\quad z_-=(a-i)/2,
\quad a^2+1=4a,\quad z_++z_-=a,\quad z_+z_-=a.
\tag{L1}
\]

a是O_K unit，因为 aσa=1；z±是K(i)上的代数units。选择原点值0的实际芽

\[
L_a=-\log(1-t/a),
\quad L_s=-\log\{(1-t/z_+)(1-t/z_-)\},
\quad L_d=\{-\log(1-t/z_+)+\log(1-t/z_-)\}/i.
\tag{L2}
\]

这里不是将K扩大后多计embedding。三个函数的全部formal coefficients就在K。准确导数为

\[
L_a'=\frac1{a-t},\qquad
L_s'=\frac{a-2t}{t^2-at+a},\qquad
L_d'=-\frac1{t^2-at+a}.
\tag{L3}
\]

令α±=z±^-1，则α++α−=1、α+α−=a^-1。设

\[
U_n=\alpha_+^n+\alpha_-^n,
\quad V_n=(\alpha_+^n-\alpha_-^n)/i.
\]

两者均满足 X_n=X_{n−1}−a^-1 X_{n−2}，initial values为(U0,U1)=(2,1)、(V0,V1)=(0,−a^-1)。所以所有n有 U_n,V_n∈O_K，并且

\[
[t^n]L_a=a^{-n}/n,\quad
[t^n]L_s=U_n/n,\quad[t^n]L_d=V_n/n.
\tag{L4}
\]

σ只共轭a和这些K系数，给对应的三个实际log芽。这个全n结论是代数递推，不从前缀样本推出。

## 2. 实际monomial背景和目标的交

三个derivative forms在a、z+、z−的residue vectors，按(La,Ls,Ld)列顺序，为

\[
(-1,0,0),\quad(0,-1,i),\quad(0,-1,-i).
\tag{L5}
\]

三个向量线性独立。绕这些punctures的actual continuation产生三个独立constant translations；它们生成的Z³在Ga³中Zariski dense。若有C(t)-系数非零polynomial关系P(t,La,Ls,Ld)=0，在任意generic固定t上continuation给P在整个translation lattice上的零值。Zariski density强迫P(t,X)=0为多项式恒等式，进而所有rational coefficients为0。因此三个log在C(t)上代数独立，也在K(t)上代数独立。

固定k=2或3，取所有total degree≤k的raw monomials

\[
\mathcal B_k=\langle L_a^{u}L_s^{v}L_d^{w}:u+v+w\le k\rangle_{K(t)}.
\tag{L6}
\]

实际rank是 binom(k+3,3)，且(L3)表明微分降低degree，所以这是完整闭合系统，全部composition factors是一维trivial。它不是整个高阶ODE的formal solution count。

实际pure-L目标的rank3商是dense Sym²(SL2)的不可约module；真实L3 forcing将constant1加入rank4闭包（见budget稿§6的实际monodromy说明）。背景只含一维因子，故交恰为constant1。用实际全纯target基(1,gH,gθH,gθ²H)，合并得到

\[
\boxed{m_2=10+3=13,\qquad m_3=20+3=23.}
\tag{L7}
\]

没有向背景重复追加三个homogeneous solutions，也没有将两个number-field embeddings相加。

## 3. 同一actual两地图合法；全部素数的packing分母

actual fullleaf maps已经省略a、z+、z−。在其simply connected source盘上，(L2)三个nonzero analytic factors有唯一normalized logarithm，故所有monomials全纯。目标的g=(1−4at+4t²)²也已清native导数poles。没有新增避点，没有额外积分factor n，没有新增地图或未证纤维。若要求closed disk neighborhood，先取同一盘地图的subradius，再取原定理的合法极限。

每个degree d monomial的第n项是有限个 n1+…+nd=n、nj≥1的卷积，其单项分母为∏nj，numerator在O_K。对任意prime power p^e，若k个nj被p^e整除，则n≥kp^e。因此

\[
v_p(\textstyle\prod_j n_j)
\le\sum_{e\ge1}\min(d,\lfloor n/p^e\rfloor)
=v_p\left(\prod_{h=1}^dD_{\lfloor n/h\rfloor}\right).
\]

所以全n、所有primes（包括2）有严格安全型

\[
\boxed{\prod_{h=1}^{d}D_{\lfloor n/h\rfloor}.}
\tag{L8}
\]

这是raw monomial，无需除d!；若采用normalized monomials只增加固定factor，主成本相同。目标3行仍是固定C D_n³。所有e_i=0，两embedding用完全相同的b matrix；origin coefficient以外无需任何number-field exponential成本。

## 4. 任意矩阵：不把comonotone下界当成本

k2的具体b行是：1行(0,0,0)、3行(1,0,0)、6行(1,1/2,0)、3个target行(1,1,1)。k3再有10行(1,1/2,1/3)，target仍3行(1,1,1)。这些列有多个positive levels，**不满足Theorem6.0.2的固定positive-tail条件**。即使各列非降序，也不能直接把weighted row sums当τflatflat。

comonotone assignment给下界

\[
\tau_{2}^{\flat\flat}\ge\frac{15+(3/2)84+3\cdot69}{169}
=\frac{348}{169},
\quad
\tau_{3}^{\flat\flat}\ge
\frac{15+(3/2)84+(11/6)300+3\cdot129}{529}
=\frac{1078}{529}.
\tag{L9}
\]

这只是选择一套species/grade coupling得到的下界。本文用独立column maxima给安全upper；不必先证明这些maxima能由同一个coupling同时达到。

在一列有fraction Q的positive species、其中H取b=1而Q−H取b=β<1，其余为0。normalized grade u在[0,1]均匀。threshold x下successful assignments至多分别为Q、(1−x)_+、H+(1−x/β)_+：前者是positive species总量，第二者是所有eligible grades总量，第三者将low species所需u≥x/β与high species总量合并。因此安全pointwise bound为

\[
S_{Q,H,\beta}(x)=\min\{Q,(1-x)_+,H+(1-x/\beta)_+\}.
\tag{L10}
\]

这个二种threshold的Hall matching本身也达到(L10)，但本文global upper只用≤。uniform grade/species discrepancies趋零时仅加o(1)；边界集合measure0。由原文(8.0.2)的max-of-sum≤sum-of-max，严格得到

\[
\tau^{\flat\flat}(b)\le\sum_h2\int_0^1 S_h(x)dx.
\tag{L11}
\]

单unit列是 S=min(Q,1−x)。此upper来自原数组自身，不是给每条row加大分母的另一个数组；也不在这里宣称joint transport等于各column upper之和。

## 5. 两个固定数组的精确column积分

|数组/列|positive levels|S的分界点（含0、1）|2∫S|
|---|---|---|---:|
|k2，m13，col1|0×1，1×12|0,1/13,1|168/169|
|k2，col2|0×4，1/2×6，1×3|0,7/26,1/2,10/13,1|129/169|
|k2，col3|0×10，1×3|0,10/13,1|69/169|
|k3，m23，col1|0×1，1×22|0,1/23,1|528/529|
|k3，col2|0×4，1/2×16，1×3|0,7/46,1/2,20/23,1|369/529|
|k3，col3|0×10，1/3×10，1×3|0,13/69,1/3,20/23,1|249/529|

例如m13 col2依次为常数9/13、16/13−2x、常数3/13、1−x；m23 col2相同替换为19/23、26/23−2x、3/23、1−x。m23 col3是13/23、26/23−3x、3/23、1−x。逐段积分就是上表，全x成立，不从浮点样本拟合。

合并(L9)与(L11)：

\[
\boxed{\frac{348}{169}\le\tau_2^{\flat\flat}\le U_2:=\frac{366}{169},
\qquad\frac{1078}{529}\le\tau_3^{\flat\flat}\le U_3:=\frac{1146}{529}.}
\tag{L12}
\]

e=0，所以没有τsharp。这两个upper就是当前可合法输入CDT的完整安全成本；未要求joint exact minimization。

## 6. 真正打开的条件式，以及尚未完成的解析量

闭合任意矩阵的数域版本给，在\barρ>U_k时

\[
\boxed{m_k(\bar\rho-U_k)\le\bar J.}
\tag{L13}
\]

这是安全、稍弱的holonomy upper；若未来实际同一两地图满足反向strict inequality \bar J<m_k(\barρ−U_k)，便与实际rank冲突，结束L3∈Q反证。

平均Jensen仍有\bar J≥\barρ。使用这两个安全cost通过必要筛选，分别要求

\[
\bar\rho>\frac{13}{12}U_2=\frac{61}{26},
\qquad \bar\rho>\frac{23}{22}U_3=\frac{573}{253}.
\tag{L14}
\]

它们分别约2.34615、2.26482，并且严格小于实际fullleaf的上限

\[
C_*=\log16-\tfrac14\log(2+\sqrt3)\quad(\text{约 }2.44335).
\tag{L15}
\]

更确切，61/26<12/5、573/253<12/5<C*；最后一个比较可用√3<7/4和e^(48/5)(15/4)<16⁴的有理Taylor upper certificate证明。

这改变了旧fixed背景账本“连必要容量尺度也不够”的情况。但C*是**上限**，不是已算actual\barρ的下界，更不是实际可取得的值；\bar J也不是自动等于\barρ。本文没有从(L14)<(L15)宣布无理性。下一实际任务是对已经合法的两fullleaf地图（及subradii）严格计算ρ和J，检验(L13)能否给rank矛盾。

Theorem8.0.1的已holonomic/闭合分支在这里关键：literal number-field自动holonomicity条件要求\barρ>max-column-cost=3，当前cap<3。我们已经证明实际closed systems，故应使用列明e=0任意矩阵数域引理；不能忽略这一分支，也不能把两embedding收益或dimension翻倍。

本文没有扣任何D12 Hasse/Smith信用，没有积分rows，没有更换地图和原点normalization，没有扫描degree k；只处理预先固定k2、k3。新的[独立Fraction脚本](cdt_odd_level12_cheap_log_packet_20261006_verify.py)和[JSON](cdt_odd_level12_cheap_log_packet_20261006_verify.json)由作者首次、单次执行，56项固定精确检查全部通过。它只核六column积分、两个rank/count表、上下界与严格容量常数比较；全阶算术、actual monodromy和合法fullleaf由正文证明及列明输入承担。

最终限定只读独审：root实际完整阅读本MD及新PY，通过全阶recurrence、prime-power packing、实际monomial rank与target交、safe column upper和capacity/J缺口；未运行本文producer。本文三件记录该范围后冻结，后续联合matching的精确成本另记。当前(L12)只标safe upper，不把未执行的联合LP或未知radius/J追认为本文结果。
