# 经典ζ(7)完整目标：实际秩10与无forcing模块特解

日期：2026-10-06。NEW证明；冻结输入只读，不执行/import任何冻结或同行producer。本稿证明完整实际C₂及F₂的最小微分秩恰为10，不给新的ζ(7)无理性结论。有限符号证书只核预定换元与最高log系数；实际秩依赖正文的全Laurent-log与不可约模块论证。

## 1. 真实输入与要证明的命题

使用[forcing spin](cdt_odd_classical_zeta7_forcing_spin_20261006.md)及[实际spin/单值群](cdt_odd_classical_spin_pullback_20261006.md)。令θ=x d/dx，

\[
\begin{aligned}
K&=(\theta+\tfrac12)^4-x\theta^4,& KH&=16x,\\
P_3(X)&=48X^3+80X^2+40X+5,\\
Q_4(X)&=8X^4+16X^3+20X^2+12X+3,\\
L_5&=\theta^5-\frac{x}{8}(2\theta+1)Q_4(\theta)
       +x^2(\theta+1)^5,\\
G&=960x-\frac32x\theta^2P_3(\theta)H,&L_5F&=G.
\end{aligned}\tag{R1}
\]

这里H是冻结的实际analytic germ，C₂=ΣCₙ,₂(x/256)ⁿ，且真正目标是

\[
F_2=C_2+91440\zeta(7)A(x/256).\tag{R2}
\]

L₅A=0；所有C₂+cA（固定c∈C）均满足(R1)。全程保留(R2)，不对ζ(7)赋Galois作用，也不把某个formal characteristic solution替代真实germ。

已证输入：齐次K是绝对不可约rank4；W_H是实际非split扩张

\[
0\longrightarrow\mathbf C(x)x\longrightarrow W_H
\longrightarrow K_{\rm hom}\longrightarrow0,
\qquad \dim W_H=5;\tag{R3}
\]

L₅的齐次carrier是绝对不可约rank5，来自Sp₄的primitive外平方。本稿证明

\[
\boxed{W_G=W_H,\quad\operatorname{rank}C_2
=\operatorname{rank}F_2=10.}\tag{R4}
\]

秩指C(x)上的实际函数导数闭包；C₂在Q(x)上的秩也为10。ζ(7)为有理数的假设下，F₂同样可用Q(x)完整模型，但该假设不改变实际秩。

## 2. 无穷远的四阶真实forcing：最高log⁴不可取消

置t=1/x、δ=t d/dt，l=log t，选任意可实际延拓到无穷远sector的分支。KH=16x准确化成

\[
\boxed{[\delta^4-t(\delta-\tfrac12)^4]H=-16.}\tag{R5}
\]

其解在该sector有收敛Laurent-log展开

\[
H(t)=\sum_{n\ge0}t^n h_n(l),\quad\deg h_n\le4,
\qquad h_0(l)=-\tfrac23l^4+p_3(l),\quad\deg p_3\le3.
\tag{R6}
\]

这里p₃的系数是真实未知连接常数，不能删除；但最高log系数由方程唯一固定。完整证明如下。n=0给∂_l⁴h₀=−16。n≥1给

\[
(n+\partial_l)^4h_n
=(n-\tfrac32+\partial_l)^4h_{n-1}.\tag{R7}
\]

在degree≤4的固定五维polynomial space，n+∂_l可逆。转移矩阵为I+O(1/n)，故在任意固定norm下其乘积至多多项式增长；(R6)收敛于充分小的|t|，实际上系数界给|t|<1。四个独立的p₃自由系数给齐次方程全部四维解空间，因此任意真实分支都属于这个展开族。这个维数论证也排除另有未列出的负次Laurent解；不靠只拟合一个解或有限系数。

由θ=−δ，forcing本身为

\[
G=t^{-1}\{960-\tfrac32\delta^2P_3(-\delta)H\}.
\tag{R8}
\]

因为δ²P₃(−δ)=−48δ⁵+80δ⁴−40δ³+5δ²，代入(R6)严格得到

\[
G=t^{-1}\{60l^2+\text{degree}\le1\text{ in }l\}
       +\sum_{n\ge0}t^n g_n(l),\quad\deg g_n\le4.
\tag{R9}
\]

最高60不依赖p₃，也不依赖延拓路径。G不是有理函数。

## 3. 五阶目标的精确reciprocity与最高log⁷

写F=t f。Q₄(−X−1)=Q₄(X)，非交换换元的全部t-factors准确给

\[
\boxed{-t\,L_{5,x}(t f)=L_{5,t}f,}\qquad
L_{5,t}=\delta^5-\frac{t}{8}(2\delta+1)Q_4(\delta)
                 +t^2(\delta+1)^5.
\tag{R10}
\]

不是仅将θ换成−δ而漏掉F=t f的shift。于是

\[
L_{5,t}f=-960+\tfrac32\delta^2P_3(-\delta)H=:S(t,l).
\tag{R11}
\]

S₀的最高项严格为−60l²。其余连接常数只改变degree≤1项。寻求

\[
f(t)=\sum_{n\ge0}t^n f_n(l),\qquad\deg f_n\le7.
\tag{R12}
\]

n=0给∂_l⁵f₀=S₀，因此

\[
\boxed{f_0(l)=-\frac1{42}l^7+p_6(l),\quad\deg p_6\le6.}
\tag{R13}
\]

未知p₆中degree≤4的五个自由系数是齐次L₅连接常数；其degree5、6部分还由S₀决定，不能任意选择。n≥1时完整递推为

\[
\begin{aligned}
(n+\partial_l)^5f_n={}&S_n
+\frac18(2n-1+2\partial_l)Q_4(n-1+\partial_l)f_{n-1}\\
&-(n-1+\partial_l)^5f_{n-2},\qquad f_{-1}=0.
\end{aligned}\tag{R14}
\]

逆算子作用于固定degree≤7 space。两个转移矩阵对n≥1统一有界；Sₙ至多多项式增长，来自(R7)并施加固定五阶polynomial δ。因而fₙ至多指数增长，(R12)在某个真实punctured neighborhood收敛。齐次情形由degree≤4的f₀给五个独立解，穷尽整个齐次解空间。故任何实际F分支满足(R12–13)，不只是构造出的formal特解。

在x坐标，最高项等价于

\[
F(x)=\frac{1}{42x}(\log x)^7
  +\frac1x\{\text{degree}\le6\text{ in }\log x\}
  +\sum_{n\ge2}x^{-n}\{\text{degree}\le7\}.
\tag{R15}
\]

此处含log的表达在固定sector解释。任意homogeneous L₅解在∞只有t times degree≤4的log；所以(R2)中的实际91440ζ(7)A不会取消最高log⁷。这一结论对所有固定c的C₂+cA成立，不假定Apéry限值或某个连接常数数值。

## 4. 全forcing模块生成性与实际秩10

G∈W_H，故W_G⊂W_H。由(R9)，G∉C(x)x，因此W_G在(R3)的K商中的像非零；不可约性使该像为全部rank4。若W_G与trivial line交为0，则投影W_G→K为同构，给(R3)的微分split；已证non-split排除它。因此

\[
\boxed{W_G=W_H,\qquad\dim W_G=5.}\tag{R16}
\]

可给独立的Ore式非零检查：D=θ²P₃(θ)按K右除的商与余式在x=0均正则，因为K的θ⁴系数1−x在0为unit。若D=UK，则在x=0多项式D(X)应被(X+1/2)⁴整除；但D(−1/2)=−1/4。这个检查同样不能替代实际forcing非split输入。

另一方面，W_H中的任意元素是H、θH、θ²H、θ³H及x的有理函数组合。由(R6)，所有Laurent-log系数的log-degree≤4；有理乘子仅改变Laurent指数，不增加log-degree。故(R13–15)严格排除

\[
\boxed{F\notin W_H.}\tag{R17}
\]

令W_F为实际F的导数闭包。G=L₅F保证W_G⊂W_F。商W_F/W_G由bar F循环生成并被L₅消去；(R17)使商非零。L₅的绝对不可约rank5输入因此强制商秩5，得到(R4)。安全upper10来自冻结forcing spin；这里才真正把它升级为最小秩10。

## 5. 精确特解与Hom障碍的范围

不存在有限阶有理微分算子M∈C(x)[θ]及r∈C(x)使

\[
\widetilde F=M H+r x,\qquad L_5\widetilde F=G.
\tag{R18}
\]

因为这类特解属于W_H、log-degree≤4，而所有实际解由第3节都必须有不可取消的log⁷。证明涵盖所有有理系数M，不是给degree cutoff的ansatz失败；也不需要选取M的未知初值。这个结论仍只排forcing模块内部的特解；其他新的geometric extension、非有理比较或改变真实源不在此范围内。

齐次模块的Hom也准确为零：K的rank4 carrier与L₅的rank5 carrier都不可约，非零微分module map必须是同构，而秩不同。因此两个方向Hom均为0。进一步W_H的composition factors为1与K，均不含L₅，故Hom(W_H,L₅)=Hom(L₅,W_H)=0。不能因两个实际模块恰同rank5就把W_H与不可约L₅认成同一模块。

完整目标是实际扩张

\[
0\longrightarrow W_H\longrightarrow W_F
\longrightarrow (L_5)_{\rm hom}\longrightarrow0.
\tag{R19}
\]

扩张(R19)也实际非split。若有与θ交换且在W_H上为identity的投影π:W_F→W_H，则πF∈W_H且L₅πF=π(L₅F)=πG=G，正好给(R18)排除的特解。这是完整投影证明，不从Hom零或秩相加自动推出non-split。

本文未计算完整扩张的Picard–Vessiot群、具体extension class全部参数或整周期格，也不把实际秩10直接换成CDT算术holonomy的成功预算。

## 6. NEW固定证书与审阅状态

[NEW producer](cdt_odd_classical_zeta7_full_rank_20261006_verify.py)只从明示(R1)定义构造symbolic换元、预定最高log系数、固定degree polynomial-space逆算子，以及冻结MD/单值群JSON哈希；不执行/import任何旧producer，不扫描n、degree或primes。证书中的n是单一符号用于全n可逆性，并不是采样循环。具体数学输入的不可约性、convergent全Laurent-log展开与实际quotient证明在正文给出。

NEW固定证书首次单次21项通过，结果由[JSON](cdt_odd_classical_zeta7_full_rank_20261006_verify.json)如实记录。首次证书已核完整(R5)而未逐行核(R7)的n-shift；作者在实际审稿前发现正文(R7)从t-times算子取系数时漏了前一指数的−1，已修正为n−3/2。该正文修正不改变任何证书输入/结果、最高log系数、可逆性、收敛性或实际秩证明，未重跑证书。当前待root实际全文/PY/JSON独审；没有新的数值无理性或Lean结论。
