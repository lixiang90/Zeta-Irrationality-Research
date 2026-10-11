# Catalan–π² 混合载体：四维真实投影、完整分支条件及尺度超过 π 的共同多叶映射

2026-10-07。隔离 NEW 稿。实际读取当前主进展 §212、全阶稿 W1–W19 与 universal-cover 稿 U1–U26。本文只新增本稿，不改 main、manifest、旧几何稿或原仓库。以下是实际函数及共同映射的纸证，没有新的数值 LI 或无理性结论。

取 a,b,u∈Q、a≠0。下文严格分开 b≠0 的混合目标与 b=0 的纯 Catalan 目标。真实条件关系为 aG+bπ²=u。

## 1. 五维大空间成立，但固定目标只需四维投影

从0正规化

\[
 A(x)=\arctan x,\quad
 B(x)=T_2(x)=\sum_{n\ge1}\frac{\chi_4(n)}{n^2}x^n,\quad
 S(x)=A(x)^2,\quad \Psi=aB+16bS,
\]
\[
 F'(x)=\frac{\Psi(x)-u}{1-x},\qquad F(0)=0.
 \tag{M1}
\]

它们满足实际 rational system

\[
 A'=\frac1{1+x^2},\quad B'=\frac A x,\quad
 S'=\frac{2A}{1+x^2},\quad
 \Psi'=A\left(\frac a x+\frac{32b}{1+x^2}\right).
 \tag{M2}
\]

所以固定 a,b 后，无需同时保留 B 与 S：闭合空间是
\[
 V=\langle1,A,\Psi,F\rangle_{\mathbb Q(x)}.
 \tag{M3}
\]
这是从五维大空间取出的真实较小 differential space，不是可逆 rational 变基。
原枝在1有 A(1)=π/4、B(1)=G、16S(1)=π²，故仅
\[
 aG+b\pi^2=u
 \quad\Longrightarrow\quad F\text{ 在1的原枝完整全纯}.
 \tag{M4}
\]
u∈Q 单独给所有原始函数的 Q-Taylor coefficients；它与 M4 是不同条件。

记 l=log x，选择到 i/−i 的不绕0的标准上/下 bridge，l(i)=iπ/2、l(−i)=−iπ/2。正向 loops 的完整增量为
\[
 \Delta_i A=\pi,\quad \Delta_i B=\pi(l-i\pi/2),\quad
 \Delta_i S=2\pi A+\pi^2;
\]
\[
 \Delta_{-i}A=-\pi,\quad \Delta_{-i}B=-\pi(l+i\pi/2).
 \tag{M5}
\]
积分常数由 B 的 jump 在相应 puncture 消失确定。l 与 A 在 C(x) 上连同1独立：若 r_0+r_1A+r_2l=0，绕i首先迫 r_1=0，再绕0迫 r_2=0，最后 r_0=0。

若存在 1,A,B,S 的 rational relation，应用 i-loop 得到 rational+πr_B l+2πr_S A=0，故 r_B=r_S=0，再消去 r_A,r_0；前四项 rank4。对 1,A,Ψ 的 relation，同样得到 rational+r_Ψ(aπl+32bπA)=0；a≠0 已迫 r_Ψ=0，再消去其余系数，所以前者 rank3。

若 u≠aG+bπ²，绕1仅平移 F，证明 F 独立。若 u=aG+bπ²，先运输 i，再绕1，此 transported Ψ(1) 与原值的差恰为
\[
 -\frac{ia\pi^2}{2}+24b\pi^2\ne0.
 \tag{M6}
\]
这里 a,b 是实有理数，非零 imaginary part 排除取消。A,B,S 均在 transported 1 的局部普通；故绕1只平移 F。逆向撤回 i 的路径后，前各项恢复，F 的非零 constant translation 保留。对 rational relation 作用此 conjugate loop，迫 F coefficient 为0。因此对任意 complex u，
\[
 \boxed{\dim_{\mathbb C(x)}\langle1,A,B,S,F\rangle=5,\qquad
        \dim_{\mathbb C(x)}\langle1,A,\Psi,F\rangle=4.}
 \tag{M7}
\]
同样的 Q(x) 秩结论用于 rational u 的原始 Taylor 芽。四维空间是下文实际 CDT 接口。

## 2. 全部 transported 1 的精确条件

在 C\{0,i,−i} 上，由三个基本 generators 可将任意 transported branch 写成
\[
 A_{\rm tr}=A+\pi k,\qquad
 B_{\rm tr}=B+\pi k l+i\pi^2 c,
 \quad k\in\mathbb Z,\quad c\in\tfrac12\mathbb Z,\quad
 c\equiv k/2\pmod{\mathbb Z}.
 \tag{M8}
\]
证明只需 M5 与0-loop：后者不改变 canonical A,B，而把已出现的 l 平移2πi；composition 因此仅向 c 添加2kn 这类整数，parity relation 保持。±i generators 的 c 均为 −1/2，inverse 的 c 为1/2。任何 based path 的 homotopy class 由这些 generators 生成。到1时 l 的 transported value 为2πin；将2kn吸收到 c 后，仍有
\[
 A_{\rm tr}(1)=\pi/4+\pi k,\qquad
 B_{\rm tr}(1)=G+i\pi^2c,\qquad c\equiv k/2\pmod{\mathbb Z}.
 \tag{M9}
\]
于是 Ψ 的 endpoint 差为
\[
 \Psi_{\rm tr}(1)-(aG+b\pi^2)
    =\pi^2\{ia c+8b k(2k+1)\}.
 \tag{M10}
\]

共同 meromorphic pullback 在 φ=1 的 local point 完整可去，当且仅当 Ψ_tr(1)=u：若 φ−1 有 order q，F 的 differential residue 是 −q(Ψ_tr(1)−u)，非零时无法成为 meromorphic 函数的导数；等于0时整个 analytic numerator 被1−φ整除。不是只取消一个 leading coefficient。

在关系 M4 下，因 a≠0、a,b 为实数：
\[
 \boxed{b\ne0:\ k=c=0;\qquad b=0:\ c=0,\ k\in2\mathbb Z.}
 \tag{M11}
\]
后一个偶数约束由 parity 来，不可把纯 G 目标的所有非原 A branches 一并删掉；前一个则完整要求原 A/B 的 endpoint values。

## 3. 0 的真实条件与 arctan lift

任意 CDT holomorphic φ，φ(0)=0，若 V 的 full basis 共同 meromorphic，则 rational inverse gauge 恢复 A、Ψ、F 的 meromorphic pullbacks。A 的 differential φ'/(1+φ²) 在 φ=±i 有非零 residue（finite ramification 仍乘非零整数），因此 φ omit ±i。它在 disk 内处处 holomorphic；A pullback 的 derivative 也处处 holomorphic，所以 A pullback 实际 holomorphic。写
\[
 g=A\circ\varphi,\quad g(0)=0,\qquad \varphi=\tan g.
 \tag{M12}
\]
S pullback=g²，故 a≠0 允许由 Ψ−16bg² 恢复 B 的 meromorphic pullback，即四维投影与五维大空间有同一个必要分支条件。

φ 有限迫 g 避开 π/2+πZ。若 g(z_0)=nπ≠0，φ 在 z_0 零阶 q，则
\[
 d(B\circ\varphi)=g\,\frac{d\varphi}{\varphi}
                  =\frac{2g}{\sin2g}\,dg
 \tag{M13}
\]
有 residue qnπ≠0，违反 meromorphic derivative 的零 residue。因此
\[
 g(\mathbb D)\subset
 \Omega_g:=\mathbb C\setminus((\pi/2)\mathbb Z\setminus\{0\}).
 \tag{M14}
\]
g=0 处 M13 的系数趋于1，确实可去；B 的 transported value 在0可以是非零常数，仍然全纯。F 的 denominator1−φ在0普通，因此不额外要求 B(0)=0。混合 b≠0 时 M11 又要求每个 φ=1 原像具有 g=π/4、B=G；其它 π/4+kπ 值必须省略。省略点对的 universal cover 自身不支付这些条件，不能自动算共同 map。

## 4. 一个全显式的共同映射及有限 J

令
\[
 W=\mathbb C\setminus((-\infty,-\pi/2]\cup[\pi/2,\infty)),\qquad
 h_W(z)=\frac{\pi z}{1+z^2},
\]
\[
 \varphi_\rho(z)=\tan h_W(\rho z),\quad 0<\rho<1,\qquad
 L_\rho=\log(\rho\pi).
 \tag{M15}
\]
h_W conformally 将 disk 映到 W；inverse 为
\[
 v(s)=\frac{2s}{\pi+\sqrt{\pi^2-4s^2}},
 \quad \sqrt{\pi^2-4s^2}\big|_{s=0}=\pi.
 \tag{M16}
\]
W 内 M13 无 pole，且 W simply connected，因此从0取 primitive 给实际 B pullback。只有 g=0 给 φ=0；只有 g=π/4 给 φ=1，二者皆唯一。到 π/4 的 real bridge 正好给 B=G，M4 使 F 完整全纯。所以 V 的全部实际 pullbacks 在 |z|<1/ρ 全纯。1 的 disk preimage 是 (2−√3)/ρ；取 ρ>2−√3 则该原像在 unit disk 内。ρ>2/π 时 derivative ρπ 也超过旧 slit size2。

对每个有限 ρ，
\[
 \boxed{L_\rho\le J(\varphi_\rho)\le\pi-\log2.}
 \tag{M17}
\]
为完整支付 finite ρ，记 P_\pm(z)=(±i+z)/(±i−z)、f=e^{-(\pi/2)P_+}、h=e^{-(\pi/2)P_-}。f,h bounded analytic，0值均为 e^{-π/2}，a.e. boundary values unimodular，
\[
 h_W=\frac{i\pi}{4}(P_+-P_-),\qquad
 \varphi_1=-i\frac{f-h}{f+h}.
 \]
f+h 在 disk 零自由，因为其零点要求 h_W=π/2+πZ。故其 radiusρ 的 log mean准确为 log2−π/2。设 E(z,w)=f(z)h(w)−f(w)h(z)，得
\[
 J(\varphi_\rho)=\pi-\log2+N_\rho,\qquad
 N_\rho=\iint_{\mathbb T^2}\log|E(\rho z,\rho w)|\,d\mu(z)d\mu(w).
 \]
E(0,ρw)≠0，因为 φ_ρ 的唯一零点是0；circle compactness 与一次 Jensen 给 Nρ 一个 uniform finite lower bound。两变量 radial subharmonic means使Nρ非降，而 |E|≤2。reverse Fatou 将其 limsup 约束到 boundary circle energy。任意 probability ν 在 unit circle 的 logarithmic energy≤0：N个独立样本的 Vandermonde determinant由Hadamard界≤N^{N/2}，取log与expectation得energy≤logN/(N−1)，再令N→∞；负无穷情形本已满足。因此 Nρ≤0，给 M17 的 upper bound。两次 Jensen 给 lower bound。这里没有只算ρ→1极限再未经证明套到finiteρ。

更精确的 finite formula 是
\[
 J(\varphi_\rho)=L_\rho+
 \int_{\mathbb T}
 \sum_{\substack{n\ne0,\ s_n=h_W(\rho w)+n\pi\in W\\
                  |v(s_n)|<\rho}}
 \log\frac{\rho}{|v(s_n)|}\,d\mu(w).
 \tag{M18}
\]
所有 zeros simple；n=0 对应 boundary root z=w，不贡献。sum有限，因为 |n|π≤2 max_{|z|≤1}|h_W(ρz)|。border roots贡献0。公式由先对 z 作 Jensen，再用 φ_ρ/w 的 zero-free mean Lρ 得出。

另一个明确可用的 tight-J 范围是 0<ρ≤1/√3：harmonic maximum principle 和 boundary计算给 |Re h_W(ρz)|<π/2，tan 在这个 strip injective，所以 φρ univalent、M18没有 interior extra roots，恰有 J=Lρ。boundary max在ρ≥√2−1时是 π(1+ρ²)/(4(1−ρ²))，在更小ρ时是πρ/(1+ρ²)；ρ=1/√3时前者等于π/2。

## 5. 一个严格更大的真实共同 Riemann surface

上述 map 不必是共同 analytic leaf 的最大尺度。取
\[
 t=3\pi/4,\qquad 0<\epsilon<\pi/4,\qquad
 D=D(t,\epsilon),\quad U=D\cap\{\operatorname{Im}w>0\}.
 \tag{M19}
\]
将 W 与 D 的两个副本只在 U 上按相同 complex coordinate识别，得到
\[
 {\cal R}=(W\sqcup D)/\{w_W=w_D:\ w\in U\}.
 \tag{M20}
\]
下半盘没有识别，所以它与 W 已有的下半盘重叠值成为不同 sheets。

Hausdorff 条件需检查，不能仅因 gluing open sets 就略掉：U 在 W 与 D 中都 open。其 frontier在 W 中是 upper semicircle（不在 D），在 D 中是 real diameter（不在 W）。所以不存在同一 U-sequence 在两个未识别点有两个 limits。若两个非识别点有相同 projected coordinate，它们只能都位于 lower half disk，取下半盘内小 neighborhoods即可分离；坐标不同则取disjoint projected小 neighborhoods。其余 U 点已识别。这证明 quotient Hausdorff。两个 open chart images各有countable basis，其union给全R的countable basis；局部坐标因而给 Riemann surface。两个 chart images是 simply connected、交为 simply connected U，van Kampen 遂给 R simply connected。

projection G_R:R→C 是 locally univalent holomorphic function。它避开所有 nonzero kπ/2；R 上 G_R=0 唯一，G_R=π/4也唯一，其它π/4+kπ都省略。原因是 W 原有这些条件，而新盘与最近的 lattice points π/2、π 距离均为π/4，且与任何 1-level 的距离至少π/2。

因此 holomorphic differential
\[
 \omega_B=\frac{2G_R}{\sin2G_R}\,dG_R
 \]
在整个 R 上普通，0点可去。simple connectivity 给从0正规化的全局 primitive B_R，保留 W 的原枝，故 B_R(π/4)=G。令 A_R=G_R、S_R=G_R²、Ψ_R=aB_R+16bG_R²。在 M4 下
\[
 \omega_F=(\Psi_R-u)\frac{d(\tan G_R)}{1-\tan G_R}
 \tag{M21}
\]
亦处处 holomorphic：唯一的 potential 1 点是原π/4，numerator完整消去它。全局 primitive F_R 正是实际 F 的 continued branch。这个 construction支付了完整 target branch，而非省略点对的形式 cover。

## 6. 尺度严格增加的证明

R 的 uniformization type必须是 disk。它不是sphere，因为 G_R 非恒定且处处有限。若为plane，则非恒定 entire函数 tanG_R: C→C\{±i} 可以 lift到该双穿孔平面的 disk universal cover，给 bounded entire函数；Liouville迫其constant，矛盾。因此 standard simply connected uniformization给 h_R:D→R，h_R(0)=0，选择rotation使
\[
 r_R=(G_R\circ h_R)'(0)>0.
 \]
这步只使用 universal-cover稿 U15–U16 的已核 hyperbolicity 与标准 uniformization/Liouville，不将全平面双穿孔cover本身当实际carrier。

W→R 的包含为strict：新盘的 real diameter点不在W，并有额外 lower-half sheets。定义
\[
 f=h_R^{-1}\circ\iota\circ h_W:\mathbb D\to\mathbb D,\quad f(0)=0.
 \]
它不surjective，故 strict Schwarz lemma给 |f'(0)|<1。chain rule在0的真实 G_R coordinate给
\[
 |f'(0)|=\pi/r_R,\qquad
 \boxed{\pi<r_R\le C=\Gamma(1/4)^4/(4\pi^2).}
 \tag{M22}
\]
upper bound来自 tan(G_R∘h_R) 的 actual omission pair，而不是在plane leaf上错误套injective bound。G_R∘h_R是noninjective lift；这正是超过π的来源。

令 v_1=h_R^{-1}(π/4)。对
\[
 \max\{\pi/r_R,|v_1|\}<\rho<1,\qquad
 \widetilde\varphi_\rho(z)=\tan G_R(h_R(\rho z)),
 \tag{M23}
\]
所有 V pullbacks在 |z|<1/ρ 全纯，0、1原像唯一且canonical，derivativeρr_R>π。公式以具体glued surface及normalized uniformizer定义真实 map；本文没有求它的 closed-form uniformizer 或一个数值 r_R。

## 7. 更大 map 的 finite J 也完整定义

M23 的 derivative从不为0：h_R conformal、G_R locally univalent、tan derivative finite且非零。0也是它的唯一零点。对每个 finiteρ，
\[
 \widetilde L_\rho=\log(\rho r_R),\qquad
 J(\widetilde\varphi_\rho)=\widetilde L_\rho+
 \int_{\mathbb T}
 \sum_{\substack{|\zeta|<1\\
 \widetilde\varphi_\rho(\zeta)=\widetilde\varphi_\rho(w)}}
          \log(1/|\zeta|)\,d\mu(w).
 \tag{M24}
\]
circle root ζ=w在boundary，不在sum内；所有roots simple。sum及其integral确实有限：φ在closed disk的更大邻域locally univalent，compactness给有限个injectivity neighborhoods，故每个fiber的roots数量有同一有限上界N。boundary |φ(w)|有positive minimum，因为0唯一且不在circle；选δ>0使 |φ(ζ)|在|ζ|≤δ比该minimum更小，于是所有summed roots满足|ζ|>δ。因此
\[
 0\le J-\widetilde L_\rho\le N\log(1/\delta)<\infty.
 \tag{M25}
\]
这给 exact finite Jensen formula及finite bound，不从ρ→1的边界能量反推。本文尚未给 M23 的优于 M25 的 quantitative closed bound；它是一个严格更大且分支已支付的可用接口。

## 8. 真实完整费用与目前 rank 门槛

给一份全finiteprime有效输入，防止把四维投影算免费。令 ℓ_N=lcm(1,…,N)、ℓ_0=1，固定整数 d清a、16b、u的分母。A_N=χ₄(N)/N，S的convolution为Σ_{h+k=N}χ₄(h)χ₄(k)/(hk)。因此
\[
 \ell_N A_N,\quad d\ell_N^2\Psi_N,\quad
 d\ell_N^2\ell_{\lfloor N/2\rfloor}F_N\in\mathbb Z
 \tag{M26}
\]
对所有N、全部primes/powers成立。最后一项需核mixed terms：B部分的n²N（n<N）在任意p的valuation≤2A+B，A=v_pℓ_N、B=v_pℓ_floor(N/2)。若v_p(n)>B，则它等于A且v_p(N)≤B；否则2v_p(n)+v_p(N)≤2B+A≤2A+B。S部分分母hkN，h+k=n<N：每个valuation都≤A。若v_p(N)>B，则h,k都≤B；否则h,k至多一项>B，因为两个p^A倍数的和>N。两情形均给总valuation≤2A+B。u/N也已由d和ℓ_N支付。这个case split含p=2和任意高powers，没有有限样本推断。

所以一个完整e=0阶梯是
\[
 \sigma=(0,1,2,5/2),\quad e=0,\qquad
 \tau_{\rm safe}=\frac{3+5\cdot2+7\cdot(5/2)}{16}=\frac{61}{32}.
 \tag{M27}
\]
可用两个width-one columns分别从A、Ψ开始，另一个half-width从F开始，τsharp(0)=0。它不仅是完整可行上界；对a≠0、b≠0，[独立算术稿](cdt_mixed_catalan_pi2_arithmetic_independent_20261007.md) M10–M18 给出任意full Q(x) basis的matching下界，证明它恰为fixed-type最小值。下面先保留较弱的两层response，再给完整费用接口。

另一个独立的任何full Q(x) basis必要界已由两位作者逐式纸核。对rowY=r₀+r_AA+r_ΨΨ+r_FF，任意fixed t≠0，
\[
 p^2Y_{p+t}\equiv a\chi_4(p)[x^t](r_\Psi+r_FL)\pmod p,
 \qquad L=-\log(1-x).
 \tag{M28}
\]
pF_p=Σ_{n<p}Ψ_n−u p-integral，所以此deep layer没有unknownscalar。r_F≠0迫nonzero finiteoffset，给两个width≥1 columns，σ≥2。r_F=0、r_Ψ非constant也如此。余下r_F=0、r_Ψ=c≠0 constant，混合b≠0的fresh A response是
\[
 pY_{p+k}\equiv\chi_4(p)[x^k](r_A+32bcA)\pmod p,\quad k>0.
 \tag{M29}
\]
A非rational，故右侧有fixedpositiveoffset非零，迫一个width≥1 column。所有rational multipliers的完整Laurent tails除固定finite primes外p-integral，和前轮proof同样由formal inverse递推；每个witness是对每个充分大oddprime，fixed N^e不支付p。fullrank4 basis至少两行在⟨1,A⟩外，至少一行含F；阶梯row sums非降给
\[
 b\ne0:\qquad
 \sigma\ge(0,0,1,2),\quad \tau\ge19/16.
 \tag{M30}
\]
纯G的b=0不满足M29，不能外推这条混合必要界。

完整necessary费用包含N^e与τsharp。对任意row的每个nonzero coordinate，独立算术稿证明：

| matched coordinate | e=0 | e≥1 |
|---|---:|---:|
| A | σ≥1 | σ≥0 |
| Ψ | σ≥2 | σ≥1 |
| F | σ≥5/2 | σ≥2 |

F的额外half-width由p³F₂p≡aχ₄(p)/2 mod p及其r_F finiteoffset给出；在e=0的constant r_F情形直接用N=2p。两个width-one layers与第三个width-half layer共同迫σ≥5/2。Ψ的constant multiplier在e=0时用Ψ_p的unique depth2；A同理用其fresh p packet。这些声明都包含完整rational Laurent tails，排除的仅为fixedfiniteprime集合。

fullbasis的coordinate determinant有nonzero permutation term，把四行分别match到1,A,Ψ,F的nonzero coordinate。matched1行的e截到0，其余截到min(e,1)；Σe、maxe均不增，τsharp的integrand非负，因此τsharp不增。排序后的matchedσ lower boundscomponentwise不超过实际排序row sums。故所有bases归约为八个binary (e_A,e_Ψ,e_F) configurations，绝非只从natural basis外推。其完整flat+sharp成本为
\[
\begin{array}{c|rrrrrrrr}
(e_A,e_\Psi,e_F)&000&111&010&011&110&001&100&101\\
\tau&61/32&191/96&65/32&65/32&33/16&17/8&69/32&69/32.
\end{array}
\]
τsharp在Σe=1,2,3、maxe=1时分别为7/16、21/32、77/96；这些来自独立算术稿M17完整分段I的精确二次最小化。因此与M27的all-prime attained cap合并，
\[
 \boxed{a\ne0,\ b\ne0:\qquad
 \tau_{\rm fixed\ type}^{\min}=61/32
 \quad\text{over every full }\mathbb Q(x)\text{ basis}.}
 \tag{M31}
\]
本稿作者与root均FULL读独立稿M1–M19并逐式纸审此matching及八种费用；没有将finite自然模型上界当任意gauge下界。纯G的b=0不在M31定理内。

CDT rank4严格矛盾要求τ<L−J/4≤3L/4；而所有实际共同maps由U稿有L≤logC<3/2。较弱M30已经给19/16>9/8>3L/4；M31更给61/32>3/2>L，连positive denominator L−τ也不可能。这封住这个混合四维fullcarrier的fixed-type比较；它不是所有joint arithmetic lattice或其它periodprojection的排除。M23的更大共同map仍是真实可用输入；要使它产生新目标定理，还需要不受这些fixed-type响应约束的新周期投影、联合整格定理或其它有效输入。

## 9. 后续接口、文献范围与审阅

本轮primary检索未找到1,G,π²的无条件Q-linear independence定理；这是有范围的检索结论。child实际FULL读repo [September24 Catalan稿](https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)的introduction、foundations、conclusion三个源文件，主定理只断言G无理，未宣称读完44页全部proof。普通Taylor contact消掉ζ2的步骤只处理G∈Q。真实mixed接触要求每列 H_j−D_j=16(b/a)C_j，使period part 4C_jG+(π²/4)(H_j−D_j)在关系下为(4C_j/a)u。它涉及0点与∞点两种不同截断，尚未支付原整数支持、primitive lattice及实处界，不能照搬为成功证明。

child另实际核[EMN v3](https://arxiv.org/html/2510.20648v3)的指定sections和period matrices：其exact2维Catalan motive的pure period为−2π²i；Q上rational变基只能向G添加imaginary rational π²倍数，不能提供real bπ²。加入Q(−2)可给3维联合period包，motivic分解仍不自动给数值period injectivity。准确primary核读/归档和相关新claim范围见[独立source_scope](../literature/catalan_pi2_mixed_novelty_source_scope_20261007.md)；本稿作者FULL读取该scope记录，未把child对原论文的节选阅读称为自己或团队全文验证。

对x↦−x trace另有真实闭合检查：y=x²后需C=A/x、D=B/x、E=A²，导数分别含Euler weights−1/2、−1/2、0；aD+16bE的导数保留−aD/(2y)。故混合b≠0不能靠单组合得到免费rank3或4下降，需{1,C,D,E,traceF}。杀去F的derivative则同时杀去条件primitive方向，亦不能当新单关系触发器。

审阅receipt：本稿作者独立纸核M5–M14的fullbranch、rank与0/1条件；M19–M25的glue topology、uniformization、strictradius及finiteJ；M26–M31的allfiniteprimecap、freshresponse、matching及rank comparison。root实际FULL读本稿此前九节M1–M30及独立算术稿五节M1–M19，逐式复核均PASS；M31是按root审阅指示将已FULL审算术稿的精确全basis结论接入，不声称root此前读过新增M31文字。universal_normalization实际FULL读本稿此前九节M1–M30并逐式独审PASS，范围包括finiteρ内函数界、glue与finitefiber J；其未审独立算术稿M18最小费用，故这条receipt不扩到M31。

既有两个child复用当前任务，没有新spawn；一个负责actual arithmetic及root新联合Taylor lattice有限producer的审阅，另一个负责primary novelty/motivic及本稿独立FULL审阅。新producer的toy a=b=1,u=0与D≤6样本未假定数值endpoint relation，也未升级为渐近节省；其image最小理想依赖整数HNF源码与完整纸证，child仅独立重算一个D2例的minors。作者没有运行旧producer、guard、PSLQ或Lean，没有改main/manifest/旧稿/原仓库。
