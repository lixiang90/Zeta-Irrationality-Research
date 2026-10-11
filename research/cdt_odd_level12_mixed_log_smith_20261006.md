# D12 原整格与三log：最高packet、实际S1及第三层接口

日期：2026-10-06。独立新理论稿；只读冻结 source、budget、cheap-log、transport、signed-cocycle、character-tensor及Smith桥，不执行或import任何producer，不作prime或参数扫描。研究的是同一固定原 polynomial source，而不是随p换一个global格再漏算其index或高度。

本稿给三个新接口：(i)由全系数Hecke同余得到真实 native三jet的完整prefix packet；(ii)Hasse商给两条次数≤2p+7的实际第一层关系及固定原格γ₁=1/2；(iii)三个linear logs只会在第三threshold参与mixed消除，其自身的最高packet有一个全特征p、多项式degree依赖的注入证明。没有证明target第二/第三层成功，也没有证明新的数值无理性。

当前指定真实两盘的平均容量上界<5/4，远低于这几张数组在ordinary J / plain-CDT账本下的必要尺度。最后给一个同matching窗口、cap3内的过度信用上界，说明即使这些窗口的全部混合层都成功，仍不够；它不处理其它metrics或refined numerators、窗口外信用、更高Smith指数、其它实际period groups或其它source。

## 1. 固定原系统、prefix和全素数规范

采用 [pure source denominators](cdt_odd_level12_source_denominators_20261006.md) 的 B、F、f、H及反证假设L(3,χ12)∈Q；K=Q(r)、r²3、O_K=Z[r]。令ϑ=t∂t，g=(1−4at+4t²)²、a=2+r，对另一embedding取σa、σt。实际全纯三target为

\[
Y_0=gH,\qquad Y_1=g\vartheta H,\qquad Y_2=g\vartheta^2H.
\tag{S1}
\]

三个logs是冻结 [cheap-log](cdt_odd_level12_cheap_log_packet_20261006.md) 的La、Ls、Ld。其导数为

\[
L_a'=1/(a-t),\quad
L_s'=(a-2t)/(t^2-at+a),\quad
L_d'=-1/(t^2-at+a).
\tag{S2}
\]

tuple `(1,La,Ls,Ld,Y0,Y1,Y2)` 的实际rank7：三log背景闭合且rank4，全部因子一维；target的rank3商是dense Sym²不可约，与背景交只有常数。这是冻结cheap-log实际交证明的degree1子族，不用两个embedding重复计rank。

取固定degreeD原整格

\[
U_D=O_{K,\mathfrak p}[t]_{\le D}^{\oplus m},\qquad
R=m(D+1),\quad N_D=m(D+1)+C+1,
\tag{S3}
\]

C取固定非负常数，使实际leading set V_D⊂[0,N_D)、#V_D=R（CDT Theorem3.2.8，闭合独立tuple）。若只研究rank7则m7；degree≤2/3 logmonomials的已证arrays分别m13/23。好p排除2、3、11、固定Θ分母、source主项和两source minor的固定norm以及模型固定坏素数。取 `p²>N_D`。于是所有需要的Taylor前缀至多有一层p-index，高层p-powers仍保留原CDT估计。

Ψ_D=p³eval_{<N_D}在U_D上integral。换局部整基只用于原评价矩阵Smith估计，不能更换原格再把sourceindex的损失删除。Euler derivatives与普通导数在下文各按写明的算子使用。

## 2. target的完整packet：modp³必须保留真正Frobenius lift

设 ε=χ12(p)，Fε=F（ε+1）或σF（ε−1）。冻结source的全系数关系给 `UpF≡Fε modp³`。定义p-integral的实际有限slow primitive

\[
f_{\varepsilon,<p}(z)=\sum_{1\le n<p}(F_\varepsilon)_n z^n/n^3.
\]

对全部n<p²，n非p倍数时p³f_n∈p³；n=pm时p³f_pm=(UpF)_m/m³，m<p。因此有全prefix而不是只有p+1项的同余

\[
p^3H(t)\equiv B(t)f_{\varepsilon,<p}(q(t)^p)
 \pmod{p^3,t^{p^2}}.
\tag{S4}
\]

Θ项乘p³后消失只是因为反证假设下它在固定好place整。若用实际slow Hε表示fε，必须保留 `fε=Hε/B+Θε`，不能删除完整period carrier。

写 `b(t)=ϑlog q(t)∈O_{K,𝔭}[[t]]`、z=q(t)^p，令f₁=θ_zf、f₂=θ_z²f。整数反演保证b的coefficients整。对(S4)作整数Euler导数，准确三jet packet是

\[
\begin{split}
\Psi Y_0&\equiv gBf,\\
\Psi Y_1&\equiv g(\vartheta B)f+p\,gBb f_1,\\
\Psi Y_2&\equiv g(\vartheta^2B)f+
 p\,g\{2(\vartheta B)b+B\vartheta b\}f_1+
 p^2gBb^2f_2
\end{split}
\quad\pmod{p^3,t^{p^2}}.
\tag{S5}
\]

Ψ此处表示乘p³后的函数，而非另一个源格。g置于native derivative外，故没有多算ϑg项。

模p时 `q(t)^p=σp q(t^p)`；σp(r)=εr。这使slowpacket在相应共轭t坐标上属于k[[t^p]]。**在modp²、modp³不能把精确q(t)^p直接替换成t^p的naive lift**；(S5)的p、p²项及lift误差正是下一层问题。从只知modp的packet除p，并不能证明S2或S3。

## 3. D12 Hasse商给真实、次数≤2p+7的第一层

标准level1 E_{p−1}的q-expansion≡1 modp。实际原始输入已只读核 [Katz1973 §2.0–2.1，印刷pp97–98/PDF29–30](../literature/katz1973_padic_modular_forms.pdf)，q-expansion principle见该原件§1.6。只用Hasse holomorphy和平方的偶数重数，不需要猜simple supersingular roots。

在Γ=kerχ12的好约化上定义

\[
\mathcal R_p=\frac{E_{p-1}^2}{B^{p-1}}.
\tag{S6}
\]

权为0。E|W12=12^((p−1)/2)E(12τ)，B|₂W12=−B；平方和p−1偶数给Fricke比例12^(p−1)=1 modp，且E(12τ)≡E(τ)≡1。q-expansion principle因此使R_p在W下真的不变。M=γW且γ∈Γ0(12)，level1 E与B的weight ratio在γ下不变，故同样在M下不变。它下降到各实际K-model的P1t，而不是把source-only的Fricke身份当成完整H的period消除。

Γ的PSL index48，torsionfree；weight2的B零divisor总degree8。E²的weight2(p−1)零divisordegree8(p−1)。比值(S6)的zeros或poles在Γ曲线上degree≤8(p−1)，下到t的二阶quotient以后均≤4(p−1)。令R_p=P_p/Q_p，P、Q互素。于是

\[
\deg P_p,\deg Q_p\le4(p-1).
\]

除两个quotient branchpoints外，numerator零重数为E²零阶减(p−1)B零阶，都是偶数；E与B的碰撞不破坏此偶数结论，不排除随p变动的collision primes。至多两个odd-multiplicity numerator roots，故

\[
\deg\operatorname{rad}P_p\le2p-1.
\]

Q_p的support全部在B的零support中，至多8点（若∞在其中，只减少finite次数）。对固定好约化B非zero；还允许零points合并，不会增加support。无须用未算出的B-zero坐标或假设B在cusps零。

由E≡1得到q/t germs上的 `R_p=B^(1−p)`，故

\[
\alpha_p:=\vartheta B/B=\vartheta\mathcal R_p/\mathcal R_p
            =N_p/D_p\in k(t),
\quad\deg D_p,\deg N_p\le\delta_p:=2p+7.
\tag{S7}
\]

具体可取D=rad(PQ)，N=tD(P′/P−Q′/Q)，再去common gcd；Euler logder在∞bounded，所以N degree≤D degree。

Lp=Dϑ−N annihilates B modp。模p的(S5)中slow factor被ϑ杀掉，因而以下两条**原三个target坐标**的polynomial rows消掉整个最高packet：

\[
v_0=(-N,D,0),\qquad
v_1=(-\vartheta N,\vartheta D-N,D).
\tag{S8}
\]

两者k[t]-独立，第三坐标D区分；ϑ不增加polynomial degree。degree≤D−δ_p的多项式倍数给k-linearly independent、可整lift的primitive source方向，数量至少

\[
k_1(p,D)=2(D-2p-6)_+.
\tag{S9}
\]

所有这些向量在整个prefix的Ψimage∈p；也在所选actual leading minor中如此。**这只给S1，没有给S2**。背景source坐标为0，不拿其已有floors重复记方向。

## 4. 三linear logs的完整最高packet和前两threshold的decoupling

记 δ=χ−4(p)，σp(r)=εr。对所有n<p²，直接从L_n=unit/n抽取p-multiple indices：

\[
pL_a(t)\equiv (\sigma_p L_a)_{<p}(t^p),\quad
pL_s(t)\equiv (\sigma_p L_s)_{<p}(t^p),
\]
\[
\boxed{pL_d(t)\equiv\delta\,(\sigma_pL_d)_{<p}(t^p)}
\quad\pmod{p,t^{p^2}}.
\tag{S10}
\]

截断表示仅reduce系数n<p，不能reduce含p分母的整个log。La的a^-pm=σp(a)^-m；Ls的U_pm=U_m^p。Ld则

\[
V_{pm}=\frac{\alpha_+^{pm}-\alpha_-^{pm}}i
       =\frac{i^p}{i}V_m^p
       =\delta\,\sigma_p(V_m),
\]

因为i^p=δi。这个额外χ−4(p)不可省略。相对Cartier最高矩阵是diag(1,1,δ)，对全部好p可逆；没有非普通素数密度假设。

在common p³矩阵中，constant block floor3、三linear-log blocks floor2。设T是三个target blocks，A是constant+log blocks。对ℓ1或2，Ψ(A)⊂p²使

\[
S_\ell(U_D)/\bar A\simeq S_\ell(T),\qquad \ell=1,2,
\tag{S11}
\]

这里Sℓ是可lift到Ψimage∈pℓ的modp primitive source reductions。证明：给任何target lift加A坐标，Ψ在modp²不变；反之target lift成立可直接添任意A。因此A的unit residue坐标不会改变新target S1或S2的存在性。A的baseline floors照常计入，但不能再把它们作为新的mixed收益。

所以三个linear logs最早只能在S3帮助消掉实际target S2行的p² residual。quadratic logmonomials baseline1、cubic monomials baseline0，可能分别在S2、S1参与；(S11)不推广给那些更大背景。

## 5. 全特征p的log零估计：多项式slow列自身注入

这是替代“特征零独立所以模p也独立”的一个uniform proof。设K≥0、K<p，在k（或k的splitting extension）上取degP_j≤K。令

\[
Z(s)=P_0(s)+P_a(s)\widetilde L_a(s)+
 P_s(s)\widetilde L_s(s)+P_d(s)\widetilde L_d(s),
\tag{S12}
\]

其中tilde logs为(S10)的normalized slow packet，系数只使用0≤n<p。若其前M项为0，且

\[
4K+4\le M\le p,
\tag{S13}
\]

则四个polynomials全为0。

证明：取(K+1)次**普通s导数**。所有未导log的项含P_j^(K+1)=0，剩rational函数。三个punctures `σa,(σa±i)/2`（labels容许Frobenius交换）互异，全部good p仍distinct：z+−z−=i，(a−z+)(a−z−)=a是unit。公分母可取三个linear factors的(K+1)次方，degree3(K+1)。在∞，每项是polydegree≤K乘log的(K+1)导数，故O(s^-1)，numeratordegree≤3K+2。

前M项零迫此rational在0消失阶至少M−K−1≥3K+3，故numerator0。在某punctureγ，原log terms的singular part是R_γ(s)log(s−γ)，degRγ≤K。将Rγ展开到degreeK，对 `(s−γ)^j log(s−γ)` 作K+1导数，其系数为

\[
j!(-1)^{K-j}(K-j)!\,(s-\gamma)^{j-K-1},\quad0\le j\le K,
\]

全部为units；不同j的pole orders不同。因此rational恒零迫每个Rγ polynomial恒零。三个logs的residue matrix是冻结cheap-log的unit matrix，det仅含2i；再乘diag(1,1,δ)仍invertible，迫Pa、Ps、Pd全0，随后P0由prefix0迫0。

用truncated logs作这个导数是合法的：M≤p，char0 normalized log的每个n<M coefficient都p-integral，且至少一次导数消掉n分母。完整rational derivative与truncation的误差只从degree≥M−K−1开始；没有从modp identity除p。K<p保证上面的factorials不消失。

K0时首positive次数1..3的小minor可直接写成

\[
\det([L_j]_{n})_{1\le n\le3,j=a,s,d}
 =-1/(3a^5),
\tag{S14}
\]

其σ/δ变体对p≥5也是unit；但(S12)–(S13)的uniform polynomial结论来自导数与partial fractions，而不是把这个constant minor外推到任意K。

### 5.1 它确实覆盖原degreeD/m7 matching window

给三个log polynomial coefficients分解

\[
P_j(t)=\sum_{h=0}^{p-1}t^hP_{j,h}(t^p),\quad
K_h=\lfloor(D-h)/p\rfloor\quad(K_h<0时无列),
\]

slow prefix长度为 `M_h=floor((N_D−1−h)/p)+1`。若p≤D、p²>N_D且N_D≥7(D+1)，则M_h≤p、K_h<p，并且

\[
M_h\ge4(K_h+1).
\tag{S15}
\]

当Kh≥1时D≥h+Kh p，故M_h≥7Kh+1≥4Kh+4；Kh0时p≤D和h≤p−1给M_h≥7>4。不同h的fast exponents不同，不会互相抵消。

由(S13)，三个degreeD logsource最高packets在整个prefix上注入。因此纯背景log directions不能从自身baseline2额外升到S3。所选leading rows只删O(1)个rows时可损失O(1)的rank，不产生D²信用。m13/23前缀更长，但此处只对其三个linear-log blocks认领这个结论。

## 6. 唯一有希望的cross-log补正仍在第三层：精确接口

若另有实际target source rowx（degree≤D）及固定原格lift，使Ψ_Tx∈p²，定义真实残余

\[
\mathcal E_x(t)=p^{-2}\Psi_Tx(t)\pmod p,
\tag{S16}
\]

保留(S5)的精确lift、p和p²项。对这个**固定target S2 lift x**，仅添三个log polynomial unit coordinates的S3充要条件是

\[
\mathcal E_x(t)+\sum_{j=a,s,d}P_j(t)
      \widetilde L_j(t^p)=0\pmod{t^{N_D}}.
\tag{S17}
\]

逐residue h拆开后，是

\[
\operatorname{Extract}_{h,p}(\mathcal E_x)(s)+
 \sum_jP_{j,h}(s)\widetilde L_j(s)=0
 \pmod{s^{M_h}},\qquad\deg P_{j,h}\le K_h.
\tag{S18}
\]

(S13)使对固定残余E_x的背景补正若存在则唯一（在本window），但不保证存在。另加degree≤D的p²target补正y会把残余改为 `E_x+Ψ_Ty modp`；其它允许的target lift变化也须进入实际Bockstein余核。因此(S17)不是全部S3 lifts的分类。它只判定这个固定残余是否实际落入三个log的polynomial slow span；特征零target Sym²不可约不等于特征p这个span无交，source Up identity/swap也不证明交为0。

本稿只构造了S1 rows，没有给x满足S2的lift，因而没有可代入(S16)的已完成新信用。接下来应先证明一个实际S2及其完整Bockstein residual，再用(S18)判定第三层；不能从(S8)模p行直接除p²，不重复已有S1，也不能更换source lattice后把degree/index费用省掉。

## 7. 固定原格实际S1的账本，以及全部cap3过度信用仍不够

在m7原整数source中baseline floor和为 `3(D+1)+3·2(D+1)=9(D+1)`。新(S9)只支持target，与背景baseline disjoint；SNF给累积floor和≥9(D+1)+k1。实际leading minor仍保留整除，且p²>N_D保障完整prefix。

与冻结 [balanced Smith bridge §2及§6](cdt_odd_level20_balanced_smith_bridge_20261006.md) 的**一般DVR lemma和e0 matching proof**接合：近均衡source是primitive coordinate子格，Smith tensor floors损失至多3dc；leading set在V_D^d中。这里移用这些已证线代/极限接口，不移用level20的local rows或5/6收益。

将θ_i=max(1/b_i,h)按非降排序：zero row有θ0；target及linear log共6个θ1；m13再有quadratic的6个θ2；m23再有cubic的10个θ3。按原桥(B9)，首positive row给 `(i−1)/θ=1`，quadratic的最小值7/2、cubic的最小值13/3，其余值更大。因此三张arrays均有明确 `a₀=1`，合法matching平顶窗口p≤D；不是只根据rows的ν排序猜这个窗口。先严格内窗，再作原D→∞、d→∞、tolerance→0的顺序。

PNT给

\[
\sum_{p>\sqrt{N_D}}2(D-2p-6)_+\log p
 =(1/2+o(1))D^2.
\tag{S19}
\]

数域finite places先除[K:Q]，因此两embedding不把收益翻倍。高度归一收益γ₁/m，最后rank成本下降2γ₁/m²=1/m²。新的**实际S1**账本为

|固定系统|m|原τ|仅S1后的κ|Jensen必要平均ρ|
|---|---:|---:|---:|---:|
|1、3linear logs、3target|7|114/49|113/49|113/42|
|degree≤2三log monomials、3target|13|366/169|365/169|365/156|
|degree≤3三log monomials、3target|23|1146/529|1145/529|1145/506|

m13/23原τ使用冻结的 [exact transport](cdt_odd_level12_cheap_log_transport_20261006.md)，不是其comonotone lower；本S1 source仅用target，其余monomial baseline按ν3−floor处理。

更强的限定必要上界是：在同一matching≤D窗、commonp³矩阵及cap3内，即使每个source species都尽可能多得到额外floor，单p额外floor和最多 `Σ_iν_i(D+1)`。degree1、2、3 monomial的ν分别1、2、3；targetν3，constantν0。故**包含已有S1、任何待证mixed S2/S3，全部加起来**只能过度信用为

\[
\gamma_{\rm total}\le\sum_i\nu_i=
12\ (m7),\quad24\ (m13),\quad54\ (m23).
\tag{S20}
\]

它们不是可达到的Smith收益，也不能再加γ₁。代入成本后仍有

|固定array|任意cap3/matching≤D信用后的乐观κ下界|必要平均ρ下界|
|---|---:|---:|
|m7|90/49|15/7|
|m13|318/169|53/26|
|m23|1038/529|519/253|

三者都严格大于5/4。当前原支Hecke disk与共轭augmented disk的合法平均半径已证 [<5/4](cdt_odd_level12_augmented_radius_20261006.md)；映入这些指定盘的任何合法maps也受Schwarz控制，加入现有logs不增加其半径。对本稿**ordinary J / plain-CDT**账本，平均J≥平均ρ，所以这个whole cap3/window内的混合信用即使全给也不能产生当前两盘的rank矛盾。没有在本稿援引refined numerator floor，故不把这个结论概括成所有metrics或所有指标失败。

这不是全部D12 no-go。不同metrics/refined numerator、窗口外的净Smith slack、a_i>3、更大的实际signed-cocycle kernel、不同source/geometry、e>0新类型均没有被(S20)处理。纯背景的全charp注入也不排target↔background第三层混合；只是该指定window/cap的plain-CDT账本内，即使成功其总量仍太小。

## 8. 证明记录和审核边界

纯MD；没有新producer、finite scan或certificate。本稿直接读取Katz、现有source/geometry/原格桥，不运行冻结代码。Hasse的divisor界、整个modp³ source packet、log的χ−4符号与全特征p零估计由正文全尺度证明承担。有限bad primes始终固定，不能假非普通素数的正density。

conjugate_projection已通过消息独立挑战Hasse下降、index48/二阶商valence及degree2p+O1接口，特别指出inert不能把q(t)^p naive换成t^p lift；本稿已保留精确(S4)/(S5)。其另独推全charp三log零估计与Kh/Mh窗口通过，尚不填为对本MD的实际全文审阅，也不替代固定原格/全部账本审计。

Root 已实际全文只读本MD §§1–8，回读balanced bridge§6，通过精确packet、Hasse下降/碰撞偶性/rad degree、native g外三jet、χ−4 Cartier符号、全charp零估计及窗口、γ₁=1/2和cap3总数。按该审核要求，已显式列θ排序/a₀=1；已将S17限定为fixed target lift并保留另加p²target的残余变化；容量结论仅ordinary J/plain-CDT。Root没有运行producer；本稿纯MD在此限定范围冻结，旧文件保持冻结。
