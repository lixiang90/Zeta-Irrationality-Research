# 经典ζ(7)：forcing的全hypergeometric特解障碍与真实减项账本

日期：2026-10-06。新的完整范围证明。只读[冻结经典导数投影](cdt_odd_classical_derivative_projection_20261006.md)及其PY/JSON，没有执行/import冻结producer；没有n、degree、prime或研究参数扫描。本文不否定nested sums、一般Dfinite特解或新的几何源。

## 1. 固定真实forcing与待解问题

用冻结稿的A_n、D_n=C_n,1、C_n=C_n,2；本稿D_n只指这条ζ(5)系数序列，不指LCM。设

\[
 \mathscr L_nY=(n+1)^5Y_{n+1}-32(2n+1)Q(n)Y_n+65536n^5Y_{n-1},
\quad Q(n)=8n^4+16n^3+20n^2+12n+3.
 \tag{F1}
\]

真实恒等式是

\[
 \mathscr L A=\mathscr L D=0,\quad
 \mathscr L C=G_n=-384n^2P(n)h_n\quad(n\ge1),
\]
\[
 P(n)=48n^3+80n^2+40n+5,
 \qquad h_n=\frac{256^n(n-1)!^4}{(1/2)_{n+1}^4}\ (n\ge1).
 \tag{F2}
\]

初值(A0,A1)=(1,96)、(D0,D1)=(0,−1024)、(C0,C1)=(0,245760)。G_n非零，h_(n+1)/h_n=256n⁴/(n+3/2)⁴。

**定理。**不存在eventually nonzero hypergeometric序列Y_n，其shift quotient在C(n)内，满足(F1–F2)的非齐次方程。特别不存在rational function of n特解，也不存在h_n乘任意rational R(n)的特解。证明是全pole-orbit与infinity-degree argument，不把solver的None当作证明。

## 2. 任意hypergeometric特解自动化为同一forcing的rational乘子

若Y_(n+1)/Y_n=v(n)∈C(n)，则

\[
 \mathscr L_nY=Y_n\left((n+1)^5v(n)-32(2n+1)Q(n)
                    +\frac{65536n^5}{v(n-1)}\right)=Y_nJ(n).
 \tag{F3}
\]

J(n)∈C(n)。右边必须等于nonzero G_n，因此J不恒为0，且

\[
 Y_n=h_nR(n),\qquad R(n)=-384n^2P(n)/J(n)\in C(n).
 \tag{F4}
\]

因此只需排除一个完整rational image，而不是扫描不同hypergeometricansätze。允许有限个初始zeros或exceptions；eventual equality在无限多个integers成立，清分母后给同一个rational identity。h0未定义不妨碍这个eventual argument，也不借此任意改掉真实initial values。

将Y=hR代入，乘(n+3/2)⁴(n−1)⁴，得

\[
 a(n)R(n+1)+b(n)R(n)+c(n)R(n-1)=f(n),
 \tag{F5}
\]
\[
\begin{aligned}
 a&=256(n+1)^5n^4(n-1)^4,\\
 b&=-32(2n+1)Q(n)(n+3/2)^4(n-1)^4,\\
 c&=256n^5(n+1/2)^4(n+3/2)^4,\\
 f&=-384n^2P(n)(n+3/2)^4(n-1)^4.
\end{aligned}\tag{F6}
\]

## 3. 有限pole不存在：完整universal denominator为1

假设R有一个finite pole，按其C/Z orbit取全部poles中最左端α和最右端β，即β−α是nonnegative integer、α−1和β+1等不再是poles。

在n=α−1，R(n+1)有pole，而R(n)、R(n−1)均regular；f是polynomial。因此a(α−1)=0，迫

\[
 \alpha\in\{0,1,2\}.
 \tag{F7}
\]

在n=β+1，只有R(n−1)有pole，所以c(β+1)=0，迫

\[
 \beta\in\{-1,-3/2,-5/2\}.
 \tag{F8}
\]

但α是nonnegative integer；同一Z-orbit的β也必须integer，此列表只剩−1，与β≥α矛盾。故没有finite poles，R是polynomial。这里“最左/最右”只在一个finite pole的integer translate orbit内排序，不需要对任意complex numbers全序。

这是本固定算子的直接universal-denominator证明。[SymPy官方rsolve_ratio说明](https://docs.sympy.org/latest/modules/solvers/solvers.html#sympy.solvers.recurr.rsolve_ratio)给一般Abramov分母算法；本稿不依赖该算法定理来替代(F7–F8)的特殊算子证明。

## 4. 两个局部四阶零与无穷远次数矛盾

在n=1，a、b、f都含(n−1)⁴，而c(1)≠0；(F5)迫R(n−1)含(n−1)⁴，即n⁴|R(n)。在n=−3/2，b、c、f都含(n+3/2)⁴，而a(−3/2)≠0；迫R(n+1)含(n+3/2)⁴，即(n+1/2)⁴|R(n)。因此nonzero R必须满足

\[
 n^4(n+1/2)^4\mid R(n),\qquad\deg R\ge8.
 \tag{F9}
\]

另一方面，a,b,c的最高三阶为

\[
\begin{aligned}
 a&=256(n^{13}+n^{12}-4n^{11})+O(n^{10}),\\
 b&=-512n^{13}-2304n^{12}-2048n^{11}+O(n^{10}),\\
 c&=256(n^{13}+8n^{12}+27n^{11})+O(n^{10}).
\end{aligned}
\]

对degree d、leading coefficient r_d的polynomial R，(F5)左边准确的首个possible leading term为

\[
 256r_d(d-3)(d-5)n^{d+11}.
 \tag{F10}
\]

n^(d+13)、n^(d+12) coefficients全d恒等消掉，(F10)由R(n±1)=r_dn^d[1±d/n+d(d−1)/(2n²)]+lower-degree terms给出。低次项的operator degree至多d+10，不影响(F10)。f的degree是13。因此d>5时(F10)非零且degree>d+11>13，不可能；所有solutions必d≤5。与(F9)冲突。R=0也不解nonzero forcing。这完成全部hypergeometric特解排除。

它不声称homogeneous operator没有hypergeometric解；(F3)中J=0正是homogeneous情形，此时不能除J。也不排有限和、iterated hypergeometric sums、rational generating functions之外的Dfinite或geometric特解。

## 5. 一般rational-initial特解仍存在，但坏素数带不会凭减forcing消失

二阶recurrence的(n+1)⁵在所有n≥1非零，所以一个特解由Y0、Y1唯一确定。A与D的initial determinant为−1024；故任意特解都有完整精确分解

\[
 Y_n=C_n+\alpha A_n+\beta D_n,\quad
 \alpha=Y_0,\quad
 \beta=(245760+96Y_0-Y_1)/1024.
 \tag{F11}
\]

若Y0,Y1 rational，α、β rational，所有Y_n也rational；这并不使Y hypergeometric。原n=0的generating differential equation会随initial values给不同z项，必须保留这个信息。

对每个足够大prime p，冻结稿已证v_p(C_(p+1)/2)=−4。A全n integral；D0、D1 integral，homogeneous recurrence在indices j<p的leading j⁵都是p units，因此D_j对j<p全p-integral。排除α、β固定分母素数后，(F11)给

\[
 \boxed{v_p(Y_{(p+1)/2})=-4.}
 \tag{F12}
\]

因此**所有固定rational initial values的特解自身**仍有同一N<p≤2N−1全prefix的p⁴带，最小全prefix分母的log-growth至少4N+o(N)。这不是只排一个ansatz。若把特解作为actual model的一列/forcing input，不能称其无需算术代价。

允许Y0/Y1 nonrational则不应用此有限分母结论；但必须把它们的真实数值period及数域embedding加入目标和整格，不能隐去。

## 6. 真正目标补偿：一个可写出的特解并未保留“纯ζ(7)”投影

固定经典真实线性形式为

\[
 F_{n,1}=D_n+744A_n\zeta(5),\qquad
 F_{n,2}=C_n+91440A_n\zeta(7).
 \tag{F13}
\]

减去(F11)的任意particular solution后，准确得到

\[
 F_{n,2}-Y_n
 =-\beta F_{n,1}
   +[91440\zeta(7)+744\beta\zeta(5)-\alpha]A_n.
 \tag{F14}
\]

例如唯一Y0=Y1=0的particular为Y=C+240D。它使(F1)齐次，但(F14)变成

\[
 F_{n,2}-Y_n=-240F_{n,1}
 +[91440\zeta(7)+178560\zeta(5)]A_n.
 \tag{F15}
\]

不能省略这个真实F_(n,1) carrier，然后把新的连接周期称作原纯ζ(7)。β=0时则只剩(91440ζ(7)−α)A_n，这是把整个非齐次C源搬到Y里的tautological homogeneous projection；没有因此证明ζ(7)假设消去A的某个真实branch singularity。

(F14–F15)是源级恒等式，没有使用Archimedean Apéry-limit conjecture，也没有声称lim D_n/A_n=−744ζ(5)或lim F_(n,r)/A_n=0。冻结源尚未证明这些limits；本文不得凭“Apéry外观”补入它们。

于是本轮的明确结果是：hypergeometric减forcing不可能；一般rational-initial减forcing会转移同一坏p带，并带有必须完整记录的实际目标/carrier补偿。下一正方向需寻找不同真正零目标周期的geometric particular solution、或对完整inhomogeneous extension核monodromy/最小秩，而不是只在recurrence删掉G。

## 7. NEW证书、执行记录与范围

[NEW fixed producer](cdt_odd_classical_zeta7_forcing_20261006_verify.py)在每次执行中只调用一个固定operator的Abramov求解，答案均为None；另核(F6)、两个局部divisibilities和all-degree(F10)，没有degree扫描。首次四个clearing checks通过后，冻结输入pin filename写成`.verify.py`导致FileNotFoundError，未产JSON。修为真实`_verify.py`/`_verify.json`并加入以上独立完整proof identities，第二次17项通过；[JSON](cdt_odd_classical_zeta7_forcing_20261006_verify.json)保留真实历史。这个I/O错误不改变operator、solver答案或数学source。

whole-pole proof、all-hypergeometric reduction、全部rational-initial带和真实period/carrier identity由正文证明；finite checks不替代它们。没有新的ζ(7)数值无理性、linear independence或Lean结论，未认领inhomogeneous actual rank或共同全纯leaf。

实际审阅：root只读本文全文及NEW producer/JSON，独核pole-orbit、all-hypergeometric reduction、local/infinity degree、全rational-initial坏p带与真实period/carrier恒等式，通过；没有执行producer。helper_tensor_budget实际只读第2–4节，独核有理差分reduction、pole-orbit两端、两个local divisibilities及256(d−3)(d−5)的all-degree障碍，通过；未将此范围扩大到第5–6节或整模型。审阅者均未重跑本稿或同行证书；本稿自己的执行记录准确为第二次17项通过，首次I/O错误如上完整保留。

本文及两个NEW证书文件现冻结；旧冻结输入保持原状。后续实际forcing微分秩5证明见独立[forcing spin稿](cdt_odd_classical_zeta7_forcing_spin_20261006.md)，不是本文的hypergeometric序列障碍自动推出。
