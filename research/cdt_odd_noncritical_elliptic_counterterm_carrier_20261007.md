# 非 CM 椭圆 ratio 的反项积分核：全素数 half-width 整模型与实际五行载体

2026-10-07，作者 /root/masked_racah_finalize。唯一 NEW 纸面主稿。Authority 为 research/cdt_odd_delivery_real_gates_kummer_cauchy_extensions_20261007.json，SHA7a7b7fe3621168e0399c5abf769d12cccec76b25eaabde0ce5f5c5b603155b5a，216163 bytes；620 frozen（615数学、5guards），主报告 §§201–205。本轮数学 producer 创建/execute/import/rerun、prime/guard/Lean 与数学运行均0；全部旧数学文件及收据只读。

本稿保留上一轮非 CM conductor15 的实际 ratio，改变真正承担关系触发 logarithm 的积分核。新反项只放在原 Gauss 奇点，不新增 puncture；它给全部 n、全部 primes/powers 的 `D_floor(n/2) D_(2n−3)` 整模型，最小 coefficient-prefix 分母增长率恰5/2，严格低于旧 Cauchy primitive 的3。这个整模型还真实符合 CDT 的两个标准列，使已支付的五行安全预算改为21/10。native目标完整跳跃保留、actualrank5保留，但原奇点的 logarithm 变强，transportedµ跳跃亦仍存在；没有新的数值无理性或strict holonomy margin。

## 1. 同一真实目标、整数坐标与原连接

**N1（实际输入与目标）。** 本轮 actual FULL 重新读取冻结上一主稿 research/cdt_odd_noncritical_elliptic_cauchy_carrier_20261007.md（SHA2ee738d49bfe91a9456a28caf85f6aa466008079786d3f8b4397417b45614ac9，16238 bytes，八节 E1–E25）及其正式独审（SHA3a8ddcc3c71e9ffcf16c51dad310953268be839cac1edc6ce65286f71aafc67b，9926 bytes，V1–V8），并 actual FULL 回读当前总报告 §§201–205。既有 Koutschan–Zudilin v1 PDF1–6 与 CDT v2 PDF66–69均本轮 fresh FULL text 读取，不继承上一轮13页读域。

保留同一整数坐标 z=16t：

\[
 F(t)=\sum_{n\ge0}b_nt^n,
 \quad Y(t)=\sum_{n\ge0}\frac{b_n}{2n+1}t^n,
 \quad b_n=\binom{2n}{n}^{\!2},\quad G=\theta F,
 \quad\theta=t\partial_t.
 \tag{N1}
\]

\[
 L_2F=0,\quad L_2=\theta^2-16t(\theta+1/2)^2,
 \qquad(2\theta+1)Y=F.
 \tag{N2}
\]

置 A=256、B=16、µ=A⁻¹、σ=B⁻¹、d=A/B=16。本稿 d 只是反项 residue，不是函数秩。实际数值目标仍为

\[
 r=\frac{Y(\mu)}{F(\mu)}
   =\frac{30L(E,2)}{\pi L(E,\chi_{-4},1)},
 \qquad 0<r<1,
 \tag{N3}
\]

E 为 KZ 原件 conductor15/Cremona15a8。KZ PDF5 的两条 evaluation 已证，PDF3–4 的 denominator arrays 明确 experimental，本文不用它们。π及 critical twisted period没有降到Q，也没有将ratio替换为单独L(E,2)。上一轮已核nonCM标记，本轮只依冻结确切对象，不冒称重读LMFDB网页。

**N2（实际 rank-three 连接）。** 相对状态(Y,F,G)，

\[
 \theta\begin{pmatrix}Y\\F\\G\end{pmatrix}
 =\mathcal M(t)\begin{pmatrix}Y\\F\\G\end{pmatrix},\quad
 \mathcal M=\begin{pmatrix}-1/2&1/2&0\\0&0&1\\0&b&a\end{pmatrix},
 \quad a=\frac{16t}{1-16t},\quad b=\frac{4t}{1-16t}.
 \tag{N4}
\]

F/G/Y的原有限 singularities只有0、σ，µ是ordinary point；原∞仍须支付。完整函数1,F,G,Y在C(t)上rank4，由冻结E12–E15及下文N10的具体monodromy证明保留，不把形式ODE阶数当函数rank。

## 2. 新反项核、唯一 Q-Taylor primitive 与全部初值

**N3（真正新 primitive）。** 对任意固定 u∈Q，取M>0使Mu∈Z，H_u=Y−uF。定义

\[
 K(t)=\frac1{t-\mu}-\frac{d}{t-\sigma}
     =-\frac{15t}{(t-\mu)(t-\sigma)},
 \qquad Z_u(t)=\int_0^tK(s)H_u(s)\,ds.
 \tag{N5}
\]

µ、σ的位置、反项权重d均在原整数t坐标中支付，没有新的coordinate或normalized lattice。σ已是原连接的真奇点；N5只增加其pole order，不增加finite puncture。K(0)=0，所以起点无log，Z_u(0)=Z_u'(0)=0。

完整Taylor为

\[
 K(t)=-\sum_{\ell\ge0}
    \{A^{\ell+1}-dB^{\ell+1}\}\,t^\ell,
 \qquad A-dB=0.
 \tag{N6}
\]

所有kernel coefficients是整数。令z_n=[tⁿ]Z_u，则z₀=z₁=0，n≥2时

\[
 z_n=-\frac1n\sum_{j=0}^{n-2}
 b_j\left(\frac1{2j+1}-u\right)
 \{A^{n-j}-dB^{n-j}\}.
 \tag{N7}
\]

这是唯一primitive，全部初值已经指定；没有从数值目标自由选取particular。特别

\[
 z_2=-\frac{A(A-B)}2(1-u)=-30720(1-u).
 \tag{N8}
\]

**N4（genuine关系门）。** µ小圆盘上的原H_u analytic。K的residue为1，反项在µanalytic，故完整native身份为

\[
 \boxed{(T_\mu-I)Z_u=2\pi iH_u(\mu).}
 \tag{N9}
\]

右侧是整个constant germ，非leadinglog近似。假设r=u∈Q恰使该native完整log与全部jets消失，Z_u实际analytic穿过µ。廉价导数K H_u在µ的simplepole原已meromorphic，本文使用的是付费Z_u本身；没有在旧polefill上重新申请CDT关系收益。

## 3. 完整 transported gates、原奇点更强的 logarithm

**N5（任意basedloop的完整primitive comparison）。** 取t_*∈(0,µ)作为ordinary基点，兼容0的初始germs；ℓ为避开0、µ、σ的任意basedloop。令H_u^ℓ为其实际continuation，Π_ℓ为沿ℓ以逐段continuation的H积分所得数：

\[
 \Pi_\ell=\int_\ell K(s)H_u^{\rm continued}(s)\,ds.
\]

在基点附近的共同ordinary圆盘，完整身份是

\[
 \boxed{\Delta_\ell Z_u(t)=\Pi_\ell+
       \int_{t_*}^{t}K(s)\{H_u^\ell(s)-H_u(s)\}\,ds.}
 \tag{N10}
\]

两边在t_*相同且导数相同，故为完整germ identity。这同时付variable homogeneous jump及实际comparison常数；Π_ℓ没有免费认作Q。特别对ordinaryµ的任意transportedaccess g，H_u在µ局部无自身monodromy，故共轭小loop给完整constantjump

\[
 \Delta_{g\mu g^{-1}}Z_u=2\pi iH_u^g(\mu)
 \tag{N11}
\]

（g从基点去该µ-lift，正向小圆后逆路径返回）。原native0-loop固定初始H/Z，不保证其它transported0-germs fixed；σ、∞及任意words均按N10实际continuation，不用一个native门替代全部loop。

**N6（σ的全local expansion）。** H_u沿native正轴抵达σ；Z_u沿同一路径在µ选上侧小detour，假设r=u时µ已填可直穿。detour选择只改变下列analytic γ中的常数，不改变log coefficients。置s=t−σ。原F和Y只有一次log：F=a_F(s)log s+b_F(s)，a_F(0)≠0；由N2积分，Y=a_Y(s)log s+b_Y(s)，a_Y(0)=0。因而

\[
 H_u=q(s)\log s+h(s),\quad
 q,h\text{ analytic},\quad q_0=-u a_F(0),
 \quad u=0\Rightarrow h_0=Y(\sigma)>0.
 \tag{N12}
\]

Y(σ)的正且有限也由N1的正级数给出，terms=O(n⁻²)。K=−d/s+k(s)，k analytic。直接primitive给

\[
 Z_u=-\frac{dq_0}{2}\log^2s+\beta(s)\log s+\gamma(s),
 \quad\beta,\gamma\text{ analytic},\quad
 \beta(0)=-dh_0,
 \quad\beta'(s)=Kq+\frac{dq_0}{s}.
 \tag{N13}
\]

最后一个右侧analytic，因为pole完全相消。正向σ-loop的**全**跳跃为

\[
 \boxed{\Delta_\sigma Z_u=
    -2\pi i d q_0\log s+2\pi^2d q_0+2\pi i\beta(s).}
 \tag{N14}
\]

若u≠0，log² coefficient非零；若u=0，β(0)=−16Y(σ)≠0，仍有非零log。故此nativeσ对所有u都未填。对真实假设u=r∈(0,1)，确为log²。反项取得算术收益，同时加重了原σ的branch；未取得native rounddisc解析半径收益。

## 4. 实际函数秩五与明确有理方程

**N7（原monodromy的真实秩）。** 原Gauss在0、σ的非零unipotent固定线不同，F的orbitdifferences张成二维solution space。因此1,F,θF independent。∞重复half指数给收敛展开

\[
 F=t^{-1/2}\{A_\infty(t^{-1})\log t+B_\infty(t^{-1})\},
 \quad A_\infty(0)\ne0,
\]

\[
 Y=t^{-1/2}\left\{\frac{A_\infty(0)}4\log^2t
     +\frac{B_\infty(0)}2\log t+c
     +\sum_{j\ge1}t^{-j}(a_j\log t+b_j)\right\}.
 \tag{N15}
\]

非零leadinglog由KZ的Euler integral在负实轴给出；N2的一次resonance给Y的log²，而j≥1 eigenvalues非零只给一次log。rationalcoefficients乘1,F,G无法抵消该log²，故原rank4确立。

**N8（transportedµ仍有badlift）。** 固定上述∞access与S=T∞²。N15逐项给完整身份

\[
 (S-I)^2H_u=-8\pi^2A_\infty(0)t^{-1/2}\ne0.
 \tag{N16}
\]

它是完整function identity，不只是asymptotic。搬回ordinaryµ后，H_u、SH_u、S²H_u的µ值不能同时为0。即使native关系r=u成立，后二者至少一条的N11完整jump仍非零。反项没有删除这一旧comparison障碍；不能据此称每条µlift bad或每个允许map都omit baseµ。

**N9（actualrank5）。** 若Z_u∈span_C(t)(1,Y,F,G)，每条continuation在ordinaryµ都只可能meromorphic。N16/N11的一条完整log反驳此事，所以1,Y,F,G,Z_u independent。H_u的0/1/2θrows相对(Y,F,G)仍为

\[
 R_u=\begin{pmatrix}1&-u&0\\-1/2&1/2&-u\\1/4&-1/4-ub&1/2-ua\end{pmatrix},
 \quad\det R_u=\frac{(1-u)^2-16t}{4(1-16t)}\ne0.
 \tag{N17}
\]

θZ_u=tK H_u，三阶正jets到H/θH/θ²H的triangular rational transformation对角均tK≠0，因此

\[
 \boxed{\operatorname{rank}_{\mathbf Q(t)}
  \{1,Z_u,\theta Z_u,\theta^2Z_u,\theta^3Z_u\}=5.}
 \tag{N18}
\]

以上functionfield变换只证明秩，未免费当整basis。

**N10（rationaloperator与初值）。** 令v₀,v₁,v₂为R_u三行，v₃=θv₂+v₂𝓜，(γ₀,γ₁,γ₂)=v₃R_u⁻¹，则

\[
 \mathscr L_u=\theta^3-\gamma_2\theta^2-\gamma_1\theta-\gamma_0,
 \quad\mathscr L_uH_u=0,\quad
 \left(\mathscr L_u\circ K^{-1}\partial_t\right)Z_u=0.
 \tag{N19}
\]

N7、z₀=z₁=0及N8指定全部Taylor初值。K⁻¹在0或cyclic determinant零点的operator poles只是此scalar表示的apparent点，不能给实际函数新增puncture。本文构造一个真实rationalconnection primitive，未宣称已标记higher-Chowcycle或积分Betti/deRhamnormalization。

## 5. 全n、全primes/powers的 half-width 整模型

**N11（粗逐系数模型）。** N7首先给全部n≥2、全部primes与inputM的

\[
 M nD_{2n-3}z_n\in\mathbf Z,
 \qquad M D_{2n-3}[t^n]\theta^jZ_u\in\mathbf Z\quad(j\ge1).
 \tag{N20}
\]

D_k=lcm(1,…,k)，k≤1取1。内分母只含奇数2j+1，j≤n−2。此处尚未领取反项节省，所有primepowers已在模型中。

**N12（全部prefix的真实强化）。** 对所有N≥0及0≤n≤N，

\[
 \boxed{M D_{\lfloor N/2\rfloor}D_{2N-3}z_n\in\mathbf Z.}
 \tag{N21}
\]

下面逐prime证明，未扩素数表。

N≤1系数零；N=2仅需M z₂整，由N8给出。现N≥3。固定oddprimep，置e=v_p(D_N)、e'=v_p(D_floor(N/2))、f=v_p(D_(2N−3))。f≥e。若e'=e，旧N20直接支付e+f。若e'=e−1，则q=pᵉ∈(N/2,N]；这个半开区间最多有一个p-power，故差确为一层，**不是把q全部删除**。

若n≠q，n≤N使v_p(n)≤e−1，全部内denominator的valuation≤f，故M z_n的valuation≥−(e−1+f)。若n=q，内denominator≤2q−3；唯一valuation为e的奇数是2j+1=q，j=(q−1)/2。其余terms的内valuation≤e−1。对于唯一最高term，指数n−j=(q+1)/2，且

\[
 A^{(q+1)/2}-dB^{(q+1)/2}\equiv A-dB=0\pmod p.
 \tag{N22}
\]

因为A=2⁸、B=2⁴均为nonzero squares mod oddp，而q−1=pᵉ−1是p−1倍数。只需要一层p整除，不声称pᵉ整除。于是该term也至少−(2e−1)，其余terms和MuF部分同样不差；由f≥e，仍由e−1+f支付。

最后p=2：N7所有内denominators均odd，M z_n的2-valuation至少−v₂(n)≥−e。N≥3使f≥1，且e'≥e−1，所以e'+f≥e。N2已单独支付。故所有primes包括2、inputprimes与任意powers同时通过，证明N21。

**N13（可直接交给标准CDT的逐系数类型）。** 在N21取N=n，得到

\[
 \boxed{M D_{\lfloor n/2\rfloor}D_{2n-3}[t^n]Z_u\in\mathbf Z
   \quad(n\ge0).}
 \tag{N23}
\]

它是实际half-width LCM列，不是由一个leadingPNT数值猜出的denominator type。正jets仍用N20，fixediterationθ只乘整数indices，不新增分母。固定M只支付u；A/B与所有kernelTaylorcoeff已完整支付，没有移用experimentalarrays或normalizedintegralmodel。

## 6. Matching lower：最小prefix分母leading恰5/2

**N14（最高p层在n=p消失）。** 对p>5、p∤M，j=(p−1)/2给b_j≡1 modp。N22的e1说明p²z_p≡0 modp，仅提供消去一层，不声称z_p本身整。真正的matchinglower在两个别的indices取得。

**N15（两条全部good-prime unit身份）。** 对每个p>5、p∤M，

\[
 \boxed{p^2z_{2p}\equiv-\frac{A(A-B)}2\pmod p,
 \qquad p z_{(p+3)/2}\equiv-\frac{2A(A-B)}3\pmod p.}
 \tag{N24}
\]

在n=2p，内denominators≤4p−3<p²，含p的只有p、3p，对应j₁=(p−1)/2和j₃=(3p−1)/2。Lucas分别给b_j₁≡1、b_j₃≡4。它们的brackets分别为

\[
 A^{(3p+1)/2}-dB^{(3p+1)/2}
   \equiv A^2-dB^2=A(A-B),
\]

\[
 A^{(p+1)/2}-dB^{(p+1)/2}\equiv A-dB=0.
\]

故不能漏掉第二term，但它确在该p层消失；outer2p给N24第一式。其余terms及uF部分乘p²后全消失，左侧p-adically integral由N7先付。

在n=(p+3)/2，唯一innerp term为j₁=n−2，bracket=A²−dB²=A(A-B)；outer n是p-unit且n≡3/2，给第二式。其余terms乘p后全消失。A(A-B)=256·240的素因子只有2、3、5，所以这两条对全部goodprimes都是unit，valuation恰−2、−1。

**N16（精确leading）。** 令E_N为Z_u的0..N系数的最小positive common denominator。N24使除固定有限inputprimes外，p≤2N−3都至少支付一次p，p≤N/2又至少支付第二次。因此

\[
 \log E_N\ge\vartheta(2N-3)+\vartheta(N/2)-O(\log N)
   =\frac52N+o(N).
\]

这里仅用goodprimes时漏掉固定有限集合；O(logN)亦安全覆盖小N。N21给matchingupper

\[
 \log E_N\le\log M+\log D_{\lfloor N/2\rfloor}
      +\log D_{2N-3}=\frac52N+o(N).
\]

所以

\[
 \boxed{\log E_N=\frac52N+o(N).}
 \tag{N25}
\]

这不是prime样本、individualcoefficientlower或smallsolutionheight倒用；是本coordinate、本fixedu、真实coefficientprefix的上下界匹配。没有声称N21的每个primepowerupper逐项达到等号。

## 7. 真正改善的标准列预算与仍须支付的解析叶

**N17（whole-array真实输入）。** 按实际rank5排序

\[
 (1,\theta Z_u,\theta^2 Z_u,\theta^3 Z_u,Z_u),
 \quad b_2=(0,2,2,2,2)^t,
 \quad b_{1/2}=(0,0,0,0,1/2)^t,
 \quad e=0.
 \tag{N26}
\]

N20/N23逐系数支付两个列及fixedshift−3。本人fresh FULL CDT PDF66–69核Theorem6.0.2与Remark6.0.12：columns允许nonnegative real widths，fixedinteger shifts可按原limit机制支付。于是

\[
 \tau^\flat=2(1-1/25)+\frac12(1-16/25)
     =\frac{21}{10},\qquad \tau^\sharp=0.
 \tag{N27}
\]

这是已证的安全whole-array预算；比上一选定安全upper57/25小9/50。没有将旧upper认作已证最小值，也没有宣称21/10是所有基/列模型的最优费用。N27的依据是完整N21，不是仅从leading5/2免费推出。

**N18（真实leaf边界）。** 所有实际函数holonomic；因此Cor6.0.14允许导数门槛e^(21/10)，但meromorphicpullbacks、J(φ)与strict quotient仍须在同一t坐标逐项证明。N9只填指定nativeµ，N16/N11仍给transportedµ坏lift，N14又证明nativeσ始终未填。真实r=u时Z_u在native |t|<σ 内analytic，却在σ有log²；rounddiscφ(z)=Rz仍只能R≤σ=1/16。没有获得这一disc上的strictmargin，也没有计算其它uniformizing/multimap或CDT§7–8界。

N5不新增puncture，是比加入−µ等extraordinarypoles更有利的解析选择；本稿只保存这个反项构造，不另建其他kernel稿。算术预算确有正面改善，解析branch强度却提高；不能将两个事实混成新的数值无理性结论。

## 8. 原件检索、larger-k范围与本轮闭合纪律

**N19（为何保留此实际endpoint）。** 本轮fresh KZ PDF4–5及primary网页搜索明确区分0<k<4的真实λ/ρ family与k>4的另一个Mahler表达。后者原f(z)含log(z/16)，在0不能直接提供Q-Taylor；其新的double-integral recurrence也被原作者明确留为不产生可认领无理性的方法。该family可作以后另一个真实extension目标，但其weakApéryratio、泛称Mahler-L conjectures与未付originlog不能替换本稿N3/N9。

本轮primary搜索也定位到Brunault arXiv2305.02992的已证三变量Mahler/L(E,3)关系、Rogers–Zudilin1012.3036以及作者publicationpages。本文未下载或使用这些原件的技术证明、未拿其metadata当当前ratio的新irrationality定理；不把未搜索到新irrationality视为通用未知性证明。无需为这个已经自足的反项lemma扩大文献支线。

**N20（本轮真实读域与输入指纹）。** 本轮实际FULL：旧2ee738主稿八节、旧3a8dd正式独审V1–V8、当前总报告 §§201–205。当前authority JSON实际syntaxparse并核物理SHA/216163bytes、620 frozen与138 archivedPDFrecords；不冒称逐式重审620旧论文。

- Koutschan–Zudilin，[Apéry limits for elliptic L-values, arXiv2111.08796v1](https://arxiv.org/abs/2111.08796v1)，既有literature/cdt_gamma_noncritical_elliptic_sources_20261007/koutschan_zudilin2021_apery_elliptic_l_values_arxiv2111_08796v1.pdf，SHA8f55e4b6b8bd772ee83b5d4638af06e8af17b75e8907c49fa307434d9a515ad7，126817bytes、6归档页；本轮fresh实际FULLtext PDF1–6，含全部printedrecurrences和references，没有运行其software。
- 固定CDTv2，literature/cdt2024_l2_chi_minus3.pdf，SHA84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771，4517169bytes、218归档页；本轮fresh实际FULLtext PDF66–69四页，核whole-array、realwidth、fixedshifts及holonomic/meromorphic接口。

个人本轮main primary读域为10distinct PDF页，不继承上一轮13或同行页数。primaryweb查询是locator/status范围，不计本地PDFFULL页。新增下载0、render0、数学producer创建/execute/import/rerun0、数学运行0、prime扩表0、guard0、Lean0。文献/JSON/hash操作只是documentary。

**N21（本轮实质进展与未证缺口）。** 新结果是同一非CM ratio的counterterm真carrier、全n/allpowers half-width整模型N21、matching最小prefixleading5/2、真实标准whole-array21/10、actualrank5与完整native/transportedgates。此处同时保留Q-Taylor和关系触发的全jump，未退回便宜meromorphicpolefill。仍未证明r、任何新ζ/L数的无理性或数值LI，未构造指定motiviccycle/Betti格，未找到实际叶上的strict holonomy margin。

候选须actual FULL作者自读、指定独立reviewer actual FULL正式独审、收审后最后FULL作者回读才一次生成单向FINALreceipt。本稿尚未创建该receipt；旧620 records、旧主稿和review均不修改，不pin未来audit、mutable背景总稿或同行receipt。
