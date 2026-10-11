# Level 7 的真实填充叶：整数三次覆盖、显式 paid map 与全尺度 CDT 分子

日期：2026-10-07。作者：`/root/scaled_root_finalize`。本轮 immutable authority 为 `research/cdt_odd_delivery_real_gates_kummer_cauchy_extensions_20261007.json`，SHA `7a7b7fe3621168e0399c5abf769d12cccec76b25eaabde0ce5f5c5b603155b5a`，216163 bytes，620 frozen（615 mathematical、5 guards）。旧文件与同行数学 producer、result、guard 只读；本稿数学 producer 创建／执行／导入／重跑、prime 扩表、Lean 均为0。

本稿构造新连接常数 \(C_3\) 在有理假设下的一张真实允许圆盘，并证明其共形大小严格超过现有 \(16/9\) 费用。它也给出该同一映射的完整 §6 分子和整个半径区间上的精确 Bost–Charles characteristic。完整比较仍没有 strict margin；进一步证明本映射的 §7.1 凸性修正、合法 §7.6.4 非负 stationary weights 与当前 §8 分母加强都不能消去这个缺口。这些限制只针对下面这张具体图及指定整模型，不能推出所有 filled leaves 或所有算术模型的障碍。

## 1. 固定原载体、实际秩和算术费用

使用本轮实际 FULL 回读的冻结主稿 `cdt_odd_level7_polynomial_extension_classes_20261007.md` E1–E29，及其正式独审 V1–V7。原坐标为
\[
 \theta=t\partial_t,\qquad
 L=(1-t)^2(1-28t)\theta^2-14t(1-t)^2\theta-(2t+4t^2),
 \quad \sigma=1/28.                                      \tag{P1}
\]
\[
 LB_3=t^3,\quad B_3(0)=0,\qquad LA=0,\quad A(0)=1.          \tag{P2}
\]
这里 \(B_3\) 是原有有理 Taylor germ；\(C_3\) 是冻结 E22 的完整 Mellin 连接数，而非另选的局部投影：
\[
 C_3=4\pi^2\int_0^\infty
       y\,f(iy)\frac{t(iy)^2}{1-t(iy)}\,dy>0,\qquad
 B_3-C_3A\text{ 在原生 }\sigma\text{ 的完整 germ analytic}. \tag{P3}
\]
后一个结论使用同一从原点沿实轴到 \(\sigma\) 的分支和 Fricke 固定点；它不是所有 transported branches 的无条件填充。

以下仅在数值假设
\[
 C_3=u\in\mathbb Q,\qquad G=B_3-uA                         \tag{P4}
\]
下应用 CDT。冻结 E8/E13/E2 已证：forcing \(t^3\) 没有 rational particular，\(\{1,G,\theta G\}\) actual \(\mathbb Q(t)\)-rank 为3；存在 fixed integer \(M\) 使所有 \(n\)
\[
 MD_n^2[t^n]G,\quad MD_n^2[t^n]\theta G\in\mathbb Z,
 \qquad D_n=\operatorname{lcm}(1,\ldots,n).                \tag{P5}
\]
这给两个相同 denominator columns，各自 sorted widths 为 \((0,1,1)\)、\(e=0\)。CDT fixed v2 PDF66–69 的同一 safe 费用是
\[
 m=3,\quad \tau=2(1-1/3^2)=16/9.                          \tag{P6}
\]
所有 entries holonomic。费用是已证 safe 模型的上界，不是对全部可能整模型的费用下界。本稿将 CDT 直接用于原 \(t\)-coordinate 的三项，不把 covering degree 当新函数秩，也不将新坐标的尺度免费移给原坐标。

## 2. 全部局部门和三次覆盖

P1 的齐次 exponents 是 \(0:(0,0)\)、\(\sigma:(0,1/2)\)、\(1:(1/3,2/3)\)、\(\infty:(0,1/2)\)。这些实际 normalization 可在 Yang fixed v1 PDF15–16 核对；其 PDF5–6 给 underlying homogeneous basis \(A,\tau A\) 和积分公式。

原生 \(0\) 与 P3 的原生 \(\sigma\) 已完整 analytic。为填 \(1\)，不能只看一个 exponent。令 \(w=t-1\)。P1 的 ordinary equation 有 regular-singular indicial polynomial，其根为 \(1/3,2/3\)。所有非负 integer \(n\) 的 indicial coefficient 非零；analytic forcing \(t^3\) 因而有 convergent analytic particular。任意搬运至 \(1\) 的完整解为
\[
 G=g_{\rm an}(w)+a\,w^{1/3}g_1(w)+b\,w^{2/3}g_2(w),
 \qquad g_{\rm an},g_1,g_2\in\mathbb C\{w\}.              \tag{P7}
\]
两根之差不是整数，故无 homogeneous logarithm；analytic particular 的 recurrence 也没有 integer resonance。特别所有 branches 的 affine monodromy 满足 \(M_1^3=I\)。这是完整 germ 的结论，不需要 \(a,b\) 为零。

取 integer polynomial cover
\[
 T(x)=1-(1-x)^3=3x-3x^2+x^3,\quad s=(27/28)^{1/3},
 \quad a=1+s/2,\quad b=2+s=2a.                           \tag{P8}
\]
固定 \(s\) 的正实根、\(\zeta=e^{2\pi i/3}\)。各 finite preimages 为
\[
 T^{-1}(0)=\{0,1-\zeta,1-\zeta^2\},\quad
 T^{-1}(\sigma)=\{1-s,1-s\zeta,1-s\zeta^2\},\quad
 T^{-1}(1)=\{1\}\text{（multiplicity3）}.                 \tag{P9}
\]
非原生 \(0\) 的两个点实部为 \(3/2>a\)；非原生 \(\sigma\) 的两个点实部恰为 \(a\)。因此
\[
 \mathcal U=\{x\in\mathbb C:\operatorname{Re}x<a\}         \tag{P10}
\]
内只含原生 \(0\)、原生 \(1-s\) 和 triple point \(1\)。沿实段从 \(0\) 到 \(1-s\) 的 image 正是 P3 的 native access；在 \(x=1\)，\(T(x)-1=(x-1)^3\)，P7 的所有分数幂都成为 ordinary integer powers。P10 内没有其他 singular preimage，且 \(\mathcal U\) simply connected。逐点作这些 full local fills 后，monodromy theorem 给出
\[
 \widetilde G(x)=G(T(x))\in\mathcal O(\mathcal U).          \tag{P11}
\]
这没有声明 P9 的其余四个 points 可填，也没有声明任意绕 \(1\) 后抵达原 \(0,\sigma\) 的 transported germs 可填。

原 \(\theta G\) 的 pullback 也已经支付：
\[
 (\theta G)(T(x))=\frac{T(x)}{T'(x)}\,\widetilde G'(x).     \tag{P12}
\]
它在 \(x=1\) 可以有 pole；P12 为 meromorphic，正符合 CDT 假设。不能把“\(G\) 已填”误写成所有原 \(t\)-jets analytic。原 \(\infty\) logarithm 也没有被消去：冻结 E16/E17 给 \(B_3=(1/14)v_0\log(1/t)+\cdots\)、\(M_\infty^2B_3-B_3\ne0\)。本图将其留在域外，未以 finite cover 免费杀掉。

## 3. 显式圆盘映射及准确共形大小

以 Möbius map 将圆盘映到 P10：
\[
 x(z)=-\frac{bz}{1-z},\qquad
 \varphi(z)=T(x(z))
   =1-\left(\frac{1+(1+s)z}{1-z}\right)^3
   =-\frac{3b\,zH_s(z)}{(1-z)^3},                         \tag{P13}
\]
\[
 H_s(z)=1+sz+\frac{1+s+s^2}{3}z^2,\qquad
 \rho=\log|\varphi'(0)|=\log(3b)=\log(6+3s).              \tag{P14}
\]
P11/P12 保证 \(\{1,G,\theta G\}\circ\varphi\) 在整圆盘 meromorphic。P13 本身 holomorphic 于圆盘，唯一 pole 是 boundary \(z=1\)，所以没有把原 \(\infty\) 当 interior fill。

准确的纸面大小界是
\[
 16/9<2<\rho<\log9<8/3.                                  \tag{P15}
\]
因为 \(2/3<s<1\)，\(8<6+3s<9\)；\(e<11/4\) 给 \(e^2<8\)，而 exponential 的前三阶正项已给 \(e^{8/3}>9\)。无数值采样或优化程序用于 P15。因而当前确实获得了超过 \(16/9\) 的真实 filled-leaf map，较只在原生 Taylor 圆盘内取圆形域有实质几何增益。

原算术坐标始终为 P1 的 \(t\)，所以原点 linear scale \(T'(0)=3\) 已体现在 \(\varphi'(0)\)；全边界上的 cubic growth 也必须同时保留。若改用 \(x\)-coordinate，integer T 确实保持 Taylor cap，但不能只移其较大 derivative、仍使用另一个映射的分子。

## 4. §6 的完整分子和严格缺口

\(H_s\) 的 discriminant 是 \(-(s+2)^2/3<0\)，两根模长为 \(\sqrt{3/(1+s+s^2)}>1\)。故 P13 在圆盘内只有原点一个 simple zero。normalized Haar measure 记为 \(\mu\)。Jensen 公式给
\[
 \int_{\mathbb T}\log|\varphi|\,d\mu=\rho.                \tag{P16}
\]
令
\[
 h_s(z)=\log|H_s(z)|-3\log|1-z|,\quad
 \mathcal D_s=\iint_{\mathbb T^2}|h_s(z)-h_s(w)|\,d\mu^2.  \tag{P17}
\]
\(h_s\in L^1\)、mean 为0。其在 \(z=1\) 的 logarithmic divergence 说明它不是 a.e. constant，故 \(0<\mathcal D_s<\infty\)。CDT §6 的整个 one-map numerator 精确为
\[
 \mathcal N_6
 =\iint\max\{\log|\varphi(z)|,\log|\varphi(w)|\}\,d\mu^2
 =\rho+\frac12\mathcal D_s.                              \tag{P18}
\]
这是 whole numerator；并没有只计 \(\rho-\tau\)。固定界 P6 下，strict contradiction 需要
\[
 3(\rho-16/9)>\mathcal N_6
 \iff \rho>8/3+\mathcal D_s/4.                            \tag{P19}
\]
P15 严格否定这个条件；更准确地，
\[
 \mathcal N_6-3(\rho-16/9)
 =16/3-2\rho+\mathcal D_s/2
 >16/3-2\log9>0.                                         \tag{P20}
\]
这只说明本图和 P5/P6 的费用尚不足，并不是 \(C_3\) 无理性不可能证明。边界 pole 的所有 logarithms 为 integrable；也可先用 \(\varphi(rz)\)、\(r<1\)，再取 \(r\uparrow1\)，保留 P18–P20 的相同极限。

## 5. 真实三重纤维的全尺度 characteristic

CDT Definition7.1.2 的 characteristic 记为
\[
 \widehat T(r)=\iint_{\mathbb T^2}
       \log|\varphi(z)-\varphi(rw)|\,d\mu_zd\mu_w,\qquad
 \widehat A(r)=r\,\frac{d}{dr}\widehat T(r).               \tag{P21}
\]
以下给全 \(0<r\le1\) 的 exact interface，不以有限 knots 的样本替代。令
\[
 M(z)=\frac{1+(1+s)z}{1-z},\quad
 u_\epsilon(z)=\frac{\zeta^\epsilon M(z)-1}
                    {\zeta^\epsilon M(z)+1+s},\quad
 \epsilon=\pm1.                                         \tag{P22}
\]
除 measure-zero exceptional values，\(\varphi(u)=\varphi(z)\) 的三个 roots 是 \(z,u_+,u_-\)。\(z\) 在 boundary；Poisson–Jensen（CDT7.1.5）给
\[
 \widehat T(r)=\rho+\sum_{\epsilon=\pm1}
           \int_{\mathbb T}\log^+\frac r{|u_\epsilon(z)|}\,d\mu_z
 =\rho+\int_0^r\widehat A(v)\frac{dv}{v},                 \tag{P23}
\]
\[
 \widehat A(r)=\sum_{\epsilon=\pm1}
          \mu\{|u_\epsilon|<r\}.                         \tag{P24}
\]
P23 对 \(r=1\) 取 left limit；所有边界等号 roots 的 sets 都为 measure0。因此 numerator 与 multiplicity 是实际同一个 \(\varphi\) 的纤维，而非独立选一份“covering cost”。

在 \(|z|=1\)，写
\[
 M(z)=-s/2+i y,\qquad
 d\mu=\frac{b/2}{\pi(y^2+b^2/4)}\,dy.                    \tag{P25}
\]
它来自 \((1+z)/(1-z)=i\cot(\arg z/2)\)。展开 P22 的两平方模，\(|u_+|<r\) 精确等价于
\[
 Q_r(y):=(1-r^2)y^2+\sqrt3[1+r^2(1+s)]y
       +1-s/2+s^2/4-r^2(1+5s/2+7s^2/4)<0.              \tag{P26}
\]
\(u_-\) 对应 \(Q_r(-y)\)，Cauchy density 对称。因此全尺度公式为
\[
 \boxed{\widehat A(r)=
       2\int_{\{y:Q_r(y)<0\}}
          \frac{b/2}{\pi(y^2+b^2/4)}\,dy.}               \tag{P27}
\]
对 \(r<1\)，若 discriminant 非正则该 integral 为0，否则积分区间为这个 explicit quadratic 的两实根之间；对 \(r=1\) 取 linear inequality 或 left limit。根端点和 \(\arctan\) 给出完全封闭的纸面表达，未执行任何数值 producer。

特别 P26 在 \(r=1\) 化为 \(b(\sqrt3 y-3s/2)<0\)。故
\[
 \widehat A(1)=1+\frac2\pi\arctan\frac{\sqrt3s}{2+s}
       <\frac43,\qquad 0\le\widehat A(r)\le\widehat A(1). \tag{P28}
\]
最后一个严格界由 \(s<1\) 和 \(\arctan(1/\sqrt3)=\pi/6\)。这个付清全尺度 multiplicity 的界比仅以 degree3 作粗计数更强。令
\[
 E_s=\widehat T(1)-\rho=\int_0^1\widehat A(r)\frac{dr}{r}>0. \tag{P29}
\]
其有限性也可从 P22 或下面的 rational factorization 核查；正性由 P28 的非零 left-limit counting 得到。

## 6. §§7–8 的合法加强仍须支付

对任意 finite partition \(0<r_0<\cdots<r_l=1\)，令
\(\alpha_k=(\widehat T(r_k)-\widehat T(r_{k-1}))/\log(r_k/r_{k-1})\)。
P28 给 \(0\le\alpha_k<4/3<3\)，所以 CDT7.1.6 的 slope hypothesis 已实际满足。其 numerator 为
\[
 \mathcal N_{7,\mathrm{part}}=\widehat T(1)
       -\frac13\sum_k\alpha_k^2\log(r_k/r_{k-1})
 \ge \rho+\frac59E_s.                                   \tag{P30}
\]
证明：\(\alpha_k^2\le(4/3)\alpha_k\)，且
\(\widehat T(r_0)\ge\rho\)。代入得
\(\widehat T(1)-(4/9)(\widehat T(1)-\widehat T(r_0))
 \ge\rho+(5/9)E_s\)。
连续版本 CDT7.1.10 也满足
\[
 \mathcal N_{7,\mathrm{cont}}
 =\rho+\int_0^1\widehat A(r)(1-\widehat A(r)/3)\frac{dr}{r}
 \ge\rho+\frac59E_s.                                    \tag{P31}
\]
因此任意上述 subradius convexity refinement 都仍大于 \(\rho\)，P15 继续排除本映射与 P6 下的 strict rank3 margin。

为完整记录 §7.6 的 mixed intersections，令 \(0<r,q\le1\)、
\[
 F_\zeta(v,w)=(1-\zeta)+(1+s+\zeta)v
        -(1+\zeta(1+s))w+(1+s)(\zeta-1)vw.
\]
用 \(m_2\) 表示 normalized two-circle logarithmic Mahler integral，则
\[
 I(r,q):=\iint\log|\varphi(rz)-\varphi(qw)|\,d\mu^2
 =\log b+\log\max(r,q)
       +m_2(F_\zeta(rz,qw))+m_2(F_{\bar\zeta}(rz,qw)).     \tag{P32}
\]
证明：\(\varphi(v)-\varphi(w)=-(M(v)-M(w))
(M(v)-\zeta M(w))(M(v)-\zeta^2M(w))\)；第一 factor 的 numerator 为 \(b(v-w)\)，另两个正是 \(F\)；所有 \((1-v),(1-w)\) denominator 的 circle log means 为0。P32 也是 §7.6.5 的同对象 exact kernel，未假设其 stationary linear system 必有唯一非负解。

若任意 partition 的 §7.6.5 确实有合法 unique nonnegative solution \(s_h^*\)，CDT7.6.4 的 numerator 恰为
\[
 \mathcal N_{7,*}=\sum_h s_h^* I(r_h,1)
                =\sum_h s_h^*\widehat T(r_h)\ge\rho.      \tag{P33}
\]
故这一实际合法加强仍不能 strict。本结论没有声称 §7.6.5 的 existence/nonnegativity 是一般定理，也没有对任意未满足 theorem hypothesis 的 signed metric 作结论。

CDT8.0.1/Remark8.0.6 对 P5 的两条 standing columns 给
\[
 \tau^{\flat\flat}(b)+\tau^\sharp(0)
 =2(1-1/9)=16/9.                                       \tag{P34}
\]
所以 §8 在同一安全 denominator array 上没有另加 denominator saving；其 §8.0.4/.5 的 archimedean expressions 仍受 P30/P33 限制。本文没有排除更锋利的实际 denominator arrays、binomial-metric Theorem7.1.13 的其他选择、不同 maps／多 maps，或其他真实载体。

## 7. 与下一条低费用 rational forcing 的接口

本图可以作为多项式 source 的正面校准，不能直接赠给含 ordinary pole 的新 source。例如 root 当前研究的
\(R_a=t(1-t)/(1+a t)\)、integer \(a\ge1\)，其 \(t=-1/a\) 是新增 ordinary pole。原算子 leading coefficient 在那里非零；nonzero residue 迫 particular 的 \((t+1/a)\log(t+1/a)\) term，所有 branches 的同一 nonzero homogeneous jump 不能被有限 ramification 消去。

P13 的半平面内包含其真实 negative preimage
\[
 x_a=1-(1+1/a)^{1/3}<0,\qquad T(x_a)=-1/a,\quad T'(x_a)\ne0. \tag{P35}
\]
因此本 explicit map 对该 family 不是允许 map；需要另付 domain cut 或完整 jump cancellation。这只记录可核的兼容性边界，没有借远离原点的 \(t=-1/a\) 把 leaf 免费替成 \(\mathbb C\setminus\{-1/a\}\)，也没有在本文启动第二个 carrier 的独立研究。

当前实际新进展是：在原 \(C_3\) rational 假设下，构造一张超过 \(16/9\) 的完整允许 map；给出其 §6 精确 paid numerator、P27 的全尺度 relative covering characteristic、P28 的尖锐 explicit endpoint count，以及该图多种 CDT 加强仍无 strict 的纸面界。数值 \(C_3\) 或任何新 ζ/L 值的无理性尚未证明。下一步仍需要改变真实 leaf／map、降低同对象 arithmetic cost，或构造另一个实际 carrier，而非仅移走分子。

## 8. 当前实际读取、原件和冻结边界

本轮实际读 authority：完整 JSON parse，全部 `current_progress` 字段 printed read，并核 physical SHA/bytes；不冒认逐个全文读620冻结数学记录。当前 mutable progress 实际 FULL 读 §§201–205，用于状态定位，不作为未来 receipt pin。

本轮直接 frozen 数学输入：

- `research/cdt_odd_level7_polynomial_extension_classes_20261007.md`，actual FULL E1–E29/all8 sections；SHA `fc585a055e3b577a862f58202e24eda099394ae1b62e5f33393fb2b868690e7c`，17203 bytes。
- 同名 `_independent_review_20261007.md`，actual FULL V1–V7；SHA `a1aebf1f810e933147d5ce964e5177402146f2954dfd35aa8e4caf51b624db77`，7467 bytes。
- `research/cdt_odd_gamma_higher_slope_reference_gate_20261007.md`，actual FULL H1–H15/all7 sections，用于 CDT theorem/page 定位；SHA `debc1363d3ee14d751df60dcb62d8a457db4fc2717ea8d171aba5c2b4f754ebd`，10888 bytes。该稿旧 scalar-reference obstruction 没有移给 level7 当前 leaf。

当前本人 fresh primary exact 页域（均全文 text extraction 可见，render0）：

- [Yang fixed v1](https://arxiv.org/abs/0709.1968v1)，`literature/yang2007_apery_limits_v1_20261006.pdf`：PDF5–6、15–16，4 distinct pages；SHA `691258e04fb3f9f9fa6a4cc144c8be99d587d0af47f96cbf138ac797a1025109`，264199 bytes，24 archive pages。
- [CDT fixed v2](https://arxiv.org/abs/2408.15403v2)，`literature/cdt2024_l2_chi_minus3.pdf`：PDF66–69、89–93、105–106、113–116、122–124，18 distinct pages；SHA `84c672bd39259ab7cf8e004241f0c132e530d66dff1128d1dc1e7eb653aaa771`，4517169 bytes，218 archive pages。

本稿作者 primary 共22 distinct pages，未继承前轮13页或其他人的 Brown–Fonseca 阅读。没有新下载或新归档 PDF；documentary hash、JSON parse、metadata、text extraction 不是数学 producer。正式 independent review 的读取域将另外记录，不能回填为主稿写成前的作者阅读。旧 guard、result 和 source 字节未编辑。
