# 非 CM 椭圆 L 值的实际低秩 Cauchy 载体：完整 native 跳跃、sharp 前缀分母与搬运分支障碍

2026-10-07，作者 `/root/masked_racah_finalize`。本稿仅纸证；数学 producer 新建/执行/import/rerun、prime/guard/Lean 均为0。上一 authority 为 [paired–anti–modular–slopes audit](cdt_odd_delivery_paired_anti_modular_slopes_20261007.json)，SHA `47e298629fba798cc2d11a1e711219e61746c617f25f308919d9e1c6f6a7ecab`，612 frozen（607数学、5guards），全部只读。本轮实际全文回读总报告 §§196–200；不将 metadata 指纹核验称为重审全部612项数学。

本稿恢复一个非 CM conductor15 的真实非临界 L-value/period 商，并构造一个有 Q-Taylor、完整关系触发 logarithmic jump 和全 finite-place 整模型的具体 Cauchy primitive。新增严格结论包括差商最小前缀分母的 leading cost2、primitive 的 leading cost3、实际 rank4/rank5，以及无穷远二次 logarithm 对所有 transported ordinary-point lifts 同时填洞的阻碍。尚无新的数值无理性或线性无关性定理；该阻碍仅针对明确构造，未排除所有相对周期或所有 CDT maps。

## 1. 原件实际目标：非临界椭圆 L 值与 critical period 的商

Koutschan–Zudilin，arXiv:2111.08796v1，PDF2–5，置
\[
 F_0(z)={}_2F_1(1/2,1/2;1;z),\qquad
 Y_0(z)={}_3F_2(1/2,1/2,1/2;1,3/2;z),
 \quad \rho_1(z)=\pi F_0(z),\quad\lambda(z)=2\pi Y_0(z).
 \tag{E1}
\]
原件 PDF5 对 conductor15、Cremona15a8 的 E 给**已证** evaluation
\[
 \lambda(1/16)=30L(E,2)/\pi,
 \qquad \rho_1(1/16)=\tfrac12 L(E,\chi_{-4},1).
 \tag{E2}
\]
所以必须保留的实际目标为
\[
 r:=\frac{Y_0(1/16)}{F_0(1/16)}
   =\frac{30L(E,2)}{\pi L(E,\chi_{-4},1)}.
 \tag{E3}
\]
这既不是单独 L(E,2)，也没有把 π 或 critical twisted period 免费降到 Q。原件所写 λ/ρ1 等于2r，其“quotient L(E,2)/(π L(E,χ,1)) 为 Apéry limit”的表述须保留这个有理倍数和所选初值。

[LMFDB 的 15.a7 页面](https://www.lmfdb.org/EllipticCurve/Q/15/a/7)明确对应 Cremona15a8，模型 `y²+xy+y=x³+x²`、j=−1/15、geometric endomorphism ring Z、CM no。这些字段本轮实际读取，未执行页面 Sage/Pari snippets。该点确与上一轮 level7 的 CM period-square 标量不同。weight2 的 s=2 是非临界点；s=1 是 critical point。非 CM 本身不是无理性判据。

原件 PDF3、4 的两组 coefficient denominator formulas明确称 **experimentally**；PDF5最后也明确没有取得可认领的无理性结论。其 recurrence/ratio 极限不能代替 all-prime integrality，更不能自动代替 full-germ fill。本轮 primary 搜索截至2026-10-07没有找到 E3 的已证无理性；这是一项检索状态，不以“未搜到”证明通用未知性。本文没有借 Schneider 的 elliptic period transcendence 推出 regulator/period 商 r 的无理性，也不将 Mahler-measure identity 当作 transcendence theorem。

## 2. 同一实际整数坐标与三维 period module

取整数化坐标 `z=16t`，并固定
\[
 F(t)=F_0(16t)=\sum_{n\ge0}b_nt^n,
 \quad Y(t)=Y_0(16t)=\sum_{n\ge0}\frac{b_n}{2n+1}t^n,
 \quad b_n=\binom{2n}{n}^{\!2}\in\mathbf Z.
 \tag{E4}
\]
这不是免费改基：后续所有 singular positions 和 CDT maps 都在这个 t 坐标中支付；conifold在 σ=1/16，E3 的 evaluation point在 μ=1/256。置 θ=t∂t、G=θF，则
\[
 L_2F=0,\quad L_2=\theta^2-16t(\theta+1/2)^2,
 \qquad (2\theta+1)Y=F,
 \tag{E5}
\]
\[
 \theta\begin{pmatrix}Y\\F\\G\end{pmatrix}
 =\mathcal M(t)\begin{pmatrix}Y\\F\\G\end{pmatrix},\quad
 \mathcal M=\begin{pmatrix}-1/2&1/2&0\\0&0&1\\0&b&a\end{pmatrix},
 \quad a=\frac{16t}{1-16t},\quad b=\frac{4t}{1-16t}.
 \tag{E6}
\]
全部 identities 由 E4 逐系数或 E5 直接手推；未运行 recurrence producer。

实际 integral 从原件的 Euler representation给
\[
 F(t)=\frac1\pi\int_0^1
 \frac{dx}{\sqrt{x(1-x)(1-16tx)}},\qquad
 Y(t)=\frac12\int_0^1v^{-1/2}F(tv)\,dv.
 \tag{E7}
\]
等价地，取起点兼容平方根，`Y(w²)=w^{-1}∫_0^w F(v²)dv`。这是真实 endpoint relative integral；平方根用 algebraic covers 支付，π是原件标准 period normalization。E7不自动证明该对象来自一个指定 higher-Chow cycle 的 normal function，也不提供完整 integral Betti/de Rham 标记。

记 `O_N` 为 D_(2N+1) 的 odd part。E4立即给 `O_N[t^j]Y∈Z`，j≤N。反向对每个 odd prime power p^e≤2N+1，取 j=(p^e−1)/2。Lucas theorem 逐 p-digit给
\[
 p\nmid\binom{p^e-1}{(p^e-1)/2},
 \qquad v_p\left(\frac{b_j}{2j+1}\right)=-e.
 \tag{E8}
\]
因此 Y 的0..N全部系数的**最小 common denominator恰为 O_N**；log O_N=2N+o(N)。该下界不是 small-solution height 上界的倒用，亦不依赖原件 experimental denominator arrays。

## 3. 关系触发的完整 ordinary-point logarithm

取任意固定 `u∈Q`，M>0为其 denominator。定义实际 scalar germs
\[
 H_u=Y-uF,\qquad
 D_u(t)=\frac{H_u(t)}{t-\mu},\qquad
 C_u(t)=\int_0^t D_u(s)\,ds,\quad \mu=1/256.
 \tag{E9}
\]
起点 t=0 无 log，C_u(0)=0。这里 D_u 是函数名，勿与 lcm D_n 混淆。μ是原 E6 的 ordinary point。固定0沿正实轴到μ的 native access，F(μ)>0、Y(μ)>0。由 E4的正系数、n≥1时(2n+1)^−1<1，
\[
 0<r=Y(\mu)/F(\mu)<1.
 \tag{E10}
\]
在 μ 小圆盘中，H_u 全纯，实际 primitive 的局部展开为
\[
 C_u=H_u(\mu)\log(t-\mu)+\text{single-valued analytic germ},
 \quad (T_\mu-I)C_u=2\pi i\,[Y(\mu)-uF(\mu)].
 \tag{E11}
\]
E11 是**全部 germ 的跳跃**，没有留下 variable coefficient乘log的高阶残项。若假设目标 r=u∈Q，native H_u(μ)=0，D_u 的整个 simple pole被移去，C_u 的完整 native logarithm也移去。各 θ-jets随之全 analytic。这个机制不同于只乘 `A log R` 令某一个 leading coefficient消失。

但廉价 D_u 的 μ极点在所有u下本来就是 meromorphic；CDT Theorem6.0.2允许 meromorphic pullbacks。故仅移去 D_u 的 pole**不会**给予该 theorem 一项新的 relation-dependent admissible map。真正提供关系触发分支变化的是 C_u 的 logarithm；其额外 n分母不能省略。

## 4. 实际 rank 与无穷远对 transported residues 的约束

先证明 `1,F,G,Y`在 C(t)上 independent。Gauss方程在0与σ的两个 repeated-exponent points各有非零 logarithmic local monodromy；其 analytic solutions分别是F_0(z)和F_0(1−z)，两条 fixed lines不同。对F的 orbit differences，它们张成整个二维 homogeneous solution space。若 `R F+S G+T=0`，对两独立 homogeneous orbit differences作差并用Wronskian，得R=S=T=0。这是 actual monodromy 论证，不只是方程order2。

在∞、从负实轴抵达的 branch，由 E7 的 positive Euler integral给
\[
 F(t)=t^{-1/2}\big(A(t^{-1})\log t+B(t^{-1})\big),
 \qquad A(0)\ne0.
 \tag{E12}
\]
非零性亦可从区间 `1/R<x<1/2` 的 Euler integral得到 leading `R^−1/2 log R`；两端剩余只为O(R^−1/2)。这个 statement只要非零 leading logarithm，不借任何数值拟合。E5对Y在∞有一次 resonance：令Y=t^−1/2 V，则 `2θV=A(t^−1)logt+B(t^−1)`，故
\[
 Y(t)=t^{-1/2}\left(\frac{A(0)}4\log^2t+\frac{B(0)}2\log t
 +c+\sum_{j\ge1}t^{-j}(a_j\log t+b_j)\right).
 \tag{E13}
\]
对j≥1，θ的eigenvalue−j非零，所以没有额外log² terms。Rational coefficients不能用F、G或1的至多一次log抵消Y的二次log，遂 `1,F,G,Y`确为rank4。

H_u的三阶 cyclicity 也可全部显式支付。其0/1/2 theta rows相对(Y,F,G)为
\[
 \mathcal R_u=\begin{pmatrix}
 1&-u&0\\-1/2&1/2&-u\\1/4&-1/4-ub&1/2-ua
 \end{pmatrix},\qquad
 \det\mathcal R_u=\frac{(1-u)^2-16t}{4(1-16t)}\ne0.
 \tag{E14}
\]
因此 `1,D_u,θD_u,θ²D_u`的 actual rank是4；所有 rational gauges仅在functionfield证明秩，未移入整格。

记T∞为实际∞-loop，连接路径沿上述 branch固定。两次loop令 t^−1/2 的sign恢复、logt改变±4πi。E12–13因而作为**完整 solution identity**给
\[
 (T_\infty^2-I)^2H_u=-8\pi^2 A(0)t^{-1/2}\ne0,
 \tag{E15}
\]
对所有u都成立；F的一次log不贡献二次差分。将E15搬运回 ordinary μ，右侧非零。所以 H_u 的三个 branches `H_u,T∞²H_u,T∞⁴H_u`在μ的values不可能同时为0。特别是 native relation fill成立时，后二者至少一个μ-lift仍有非零完整 residue/log jump。**不能**从E11把所有μ-preimages或所有transported μ-lifts都标为filled。

这也证明 primitive的 actual rank：若C_u是 `1,F,G,Y`的C(t)-linear combination，每条continued branch在μ只可能meromorphic，因为F/G/Y在原μ均ordinary。然而E15给一条C_u branch在μ有非零log，矛盾。所以 `1,F,G,Y,C_u` independent。又 `θC_u=t/(t−μ)H_u`，E14和三角jet transformation给
\[
 \dim_{\mathbf Q(t)}\operatorname{span}
 \{1,C_u,\theta C_u,\theta^2C_u,\theta^3C_u\}=5
 \quad(u\in\mathbf Q).
 \tag{E16}
\]
这里证明含1的实际rank5，不把形式order4说成rank4。

实际operator可不借长展开地明确写出：令v_0、v_1、v_2依次为E14的三行，v_3=θv_2+v_2𝓜（E6的matrix），置 `(γ0,γ1,γ2)=v_3 R_u^−1`，则
\[
 \mathscr L_u=\theta^3-\gamma_2\theta^2-\gamma_1\theta-\gamma_0,
 \quad \mathscr L_uH_u=0,
 \quad\big(\mathscr L_u\circ(t-\mu)\partial_t\big)C_u=0.
 \tag{E17}
\]
所有γ_i∈Q(t)，E4/E9指定全部初值。这是具体 rational connection及primitive extension；不谎称其满足原Gauss L2 的独立 rational inhomogeneous forcing。其Green/Cauchy source是H_u而非rational scalar。指定 higher-Chow normal function的同L2 rational forcing若仍需要，尚是另一个未实现的条件。

## 5. 全 primes 模型与 primitive 的 sharp leading cost3

逐系数 geometric expansion完全给
\[
 [t^n]D_u=-\sum_{j=0}^{n}256^{n-j+1}b_j
       \left(\frac1{2j+1}-u\right),
 \tag{E18}
\]
\[
 c_n:=[t^n]C_u=-\frac1n\sum_{j=0}^{n-1}256^{n-j}b_j
       \left(\frac1{2j+1}-u\right),\quad n\ge1.
 \tag{E19}
\]
因此全部 primes、全部primepowers，包括2和固定input denominator，均由
\[
 M D_{2n+1}[t^n]\theta^jD_u\in\mathbf Z\ (j\ge0),
 \quad M n D_{2n-1}c_n\in\mathbf Z,
 \quad M D_ND_{2N-1}c_n\in\mathbf Z\ (1\le n\le N)
 \tag{E20}
\]
支付；正theta-jets满足 `M D_(2n−1)[t^n]θ^jC_u∈Z`，j≥1。D_u的0..N最小prefix denominator在每个odd p∤M上与Y相同：`Y−uF=(t−μ)D_u`，geometric convolution的diagonal−256及其inverse在Z_p都是unit。E8遂给
\[
 \log\operatorname{den}_{0..N}(D_u)=2N+o(N).
 \tag{E21}
\]
固定有限p|2M只改变O(logN)项；upper由E20给出。这不是仅一个上界。

Primitive也有可核的全prime首层恒等式。对每个odd p∤M，在E19的n=p和n=(p+1)/2两种情形，唯一具有denominator p的summand均是j=(p−1)/2。Lucas给b_j≡1，Euler给256^((p−1)/2)≡1，故
\[
 p^2c_p\equiv-256\pmod p,
 \qquad p\,c_{(p+1)/2}\equiv-512\pmod p.
 \tag{E22}
\]
左侧的p-adic integrality由E19本身先支付；其它summands分别乘p或p²后都消失。于是v_p(c_p)=−2、v_p(c_(p+1)/2)=−1。前缀0..N必须至少支付p≤N的p²，以及N<p≤2N−1的p，除固定有限input primes。PNT给lower `θ(N)+θ(2N−1)=3N+o(N)`；E20给同leading upper `logD_N+logD_(2N−1)=3N+o(N)`，故
\[
 \log\operatorname{den}_{0..N}(C_u)=3N+o(N).
 \tag{E23}
\]
E23是本整数坐标、本fixed u、本coefficient prefix的真实lower/upper matching。没有将它当作任意新格、finite minors、individual coefficient或任意normalized derivative模型的费用，也没有声称E20的每个primepower upper都达到等号。

## 6. 真实 CDT 列账本与已经检查的叶范围

按固定CDT PDF66–69 Theorem6.0.2/Remark6.0.12，`D_(2n+1)`对应**一个b=2列及fixedshift1**，不替换成Dn²。三个正theta-jets消去E19的n分母，C_u自身保留e=1。对E16排序为 `(1,θC,θ²C,θ³C,C)`，实际安全输入为
\[
 m=5,\qquad b=(0,2,2,2,2)^t,
 \qquad e=(0,0,0,0,1),\qquad \tau^\flat=48/25.
 \tag{E24}
\]
取ξ=5/2时，Definition6.0.1第二积分为3/2、第三积分为1/2、第一积分为0，所以I_ξ^5(ξ)=2。由Definition6.0.1–2
\[
 \tau^\sharp(e)\le\frac2{25}(5/2+2)=9/25,
 \quad \tau(b;e)\le57/25.
 \tag{E25}
\]
这里仅用显式candidate给安全upper；未宣称另证该min的global最优点。含1的D_u三jets族m4、e0给τflat=15/8，却如§3所述没有meromorphic-criterion中的关系触发新叶。

Native r=u假设确使C_u在μ填掉完整log，允许在指定access上穿过μ。然而σ=1/16仍不filled：F在σ含非零log；Y仅在次一阶含slog，s=t−σ。若u≠0，H_u有nonzero order0 log，C_u有nonzero slog；若u=0，Y的nonzero slog给C_u的nonzero s²log。E10的目标u更在(0,1)。所以在该t坐标、该native branch的rounddisc `φ(z)=Rz`，只能R≤1/16，根本不满足CDT holonomic relaxation的positive conformal threshold。这个判断保留整数化scale16的analytic费用。

没有计算任意uniformizing maps、多maps或其它CDT§7–8配方的最优holonomy；E15只是至少一个transported μ-lift仍bad，不能改写为所有admissible maps必须omit base μ。未知的新strict margin需在**实际filled leaf**上独立证明，不能从rank小、rationalTaylor或native residue0直接领取。

## 7. 得到什么、尚缺什么

本轮已将非CM、非critical target E3 接到一套真实低秩函数：明确 initial values、actual rational connection、relation-dependent**全**native jump、所有prime的paid整模型和精确leading prefix costs都已证明。不再依赖2021论文中标为实验的coefficient arrays，也没有把ratio极限自动升为fullgerm比较。E22还是可复核的全odd-prime congruence，而非新增prime table。

尚未证明r无理或1、L(E,2)、某period/log的线性无关。现构造的便宜差商只有meromorphic polefill；真正Cauchy carrier付费3，并具有实际rank5与E15的transported residual。要获得新CDT结论，至少仍需：一个paid lower-cost genuine carrier或更有利目标/coordinate；完整native及其它access的允许leaf识别；在该leaf达到strict holonomy margin；若采用motivic normal-function形式，还需实际cycle、rational forcing/extension以及integral Betti–de Rham normalization。可以改Cauchy kernel或更换真实relative chain研究这些条件，但本文未证明新kernel存在，也未给所有方法的no-go。

## 8. 本轮实际原件、归档与执行边界

- [Koutschan–Zudilin, Apéry limits for elliptic L-values, 2111.08796v1](https://arxiv.org/abs/2111.08796v1)：本轮唯一新下载 [PDF](../literature/cdt_gamma_noncritical_elliptic_sources_20261007/koutschan_zudilin2021_apery_elliptic_l_values_arxiv2111_08796v1.pdf)，6物理页、126817bytes、SHA `8f55e4b6b8bd772ee83b5d4638af06e8af17b75e8907c49fa307434d9a515ad7`。**实际全文PDF1–6**，包括printedrecurrences与references；没有执行其 creative telescoping、software或作者数据。正常verifiedTLS HTTP200；保存前whole136 prior PDF records的identifiers及SHA comparison没有match，亦以rg核existing source identifiers。
- [固定CDT原件](../literature/cdt2024_l2_chi_minus3.pdf)：本轮重新实际全文PDF66–69四页；E24–25使用原版(b;e)、fixedshift relaxation及meromorphic假设，不继承旧218页全文域。
- [LMFDB15.a7/Cremona15a8](https://www.lmfdb.org/EllipticCurve/Q/15/a/7)：本轮实际读取label、minimal model、j、CM与endomorphism字段及其对应web文本；不采用BSD显示作新证明、不执行snippets。旧Cremona快捷URL一度返回browsercheck，LMFDB规范URL随后正常可读。
- primary检索另核Koutschan/Zudilin与Brunault作者publication pages及arXiv版本metadata；Mahler-measure/regulatoridentity和irrationality status区分。非primaryhits仅作定位线索，不作技术依据。定位到2026 transfinite-diameter publisher文章但未下载、未用其数学；2109.12972不是本目标的ellipticirrationality定理，未新增归档或将其网页截断文本算FULL页。

本稿 personal fresh local PDF读域为10不同页（6+4），归档1PDF6页。本文新数学全部纸推，数学producer、prime、guard、Lean、render均0；receipt/独审若补读其它必要输入，会另记本人真实读域。旧612冻结文件、旧论文与收据字节不改。
