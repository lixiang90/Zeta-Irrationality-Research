# 五个 baseline1 背景的完整 slow packet 与 mixed 余核补正

日期：2026-10-06。本文只新增，不改任何冻结稿、不执行旧producer或素数扫描。结论是五个原背景species在整个n<p²窗口中的实际p³ packet、其首五个slow系数的unit minor，以及加入unit source coefficients后一个明确扩大候选补正像的slow余核条件。没有证明这些列与Ξ像无交、余核条件成功、净Smith收益或新数值无理性。

## 1. 原表中的五个species

沿用 [实际P10](cdt_odd_low_cost_polylog_20261006.md) 的函数定义。设

\[
 L=-\log(1-t),\quad Q=\operatorname{Li}_2(t),
 \quad a=(1-t)^{-1/2},
\]
\[
 T_3=L^3/6,\quad R=LQ,\quad
 M=\operatorname{Li}_{1,2}(t)
   =\sum_{n\ge1}\frac{H_{n-1}^{(2)}}n t^n,
 \quad B_3=\operatorname{Li}_3(t),
\]
\[
 K_2=a(t)\int_0^t a(u)L(u)\,du/u,
 \qquad I_K=\int_0^t K_2(u)\,du/u.
\tag{B1}
\]

在 [rank19固定unit表](cdt_odd_level20_cartier_rank19_budget_20261006.md) 中，它们均取e=1、σ=2，故ν=3、共同p⁴评价baseline1。全部ν3的八行恰是这五个background和三个旧H species。K₂本身ν2，不属于这五行；新增六个target积分ν4，也不能混淆。

取好未分歧place、p≥7。这里background coefficients在Q中，没有未知周期；其全系数安全nD_n²与K₂的D_n²已有证明。因此p³B、p²K₂在n<p²的整个窗口均integral。记

\[
 F_{<p}(s)=\sum_{0\le m<p}[t^m]F(t)s^m\pmod p.
\]

这些低于p的系数均p-integral。下面所有packet等式都在k[t]/t^{p²}中；不是只核第p或p+1个系数。

## 2. 四个MPL背景：最高层只保留p倍指标

直接逐系数有

\[
 pL(t)\equiv L_{<p}(t^p),\qquad
 p^2Q(t)\equiv Q_{<p}(t^p),\qquad
 p^3B_3(t)\equiv B_{3,<p}(t^p).
\tag{B2}
\]

例如n=pm、1≤m<p时，p³/n³=1/m³；p∤n的系数被p³消掉。乘积给

\[
 p^3T_3(t)\equiv T_{3,<p}(t^p),\qquad
 p^3R(t)\equiv R_{<p}(t^p).
\tag{B3}
\]

右边的product只取slow degree<p；在此范围各卷积指标也<p，所以它就是原函数的相同低degree截断。p≥7保证6是unit。

对于M，n不是p倍时p³/n与harmonic sum最高p⁻²相乘仍divp；n=pm时只有harmonic indexk=pj、j<m能存活，故

\[
 [t^{pm}]p^3M\equiv\frac1m\sum_{j=1}^{m-1}\frac1{j^2}
       =[s^m]M_{<p},
\quad p^3M(t)\equiv M_{<p}(t^p).
\tag{B4}
\]

因此四个MPL packet都是pure slow函数。它们的slow首阶分别为3、2、2、1；这不自动证明任意有限slow前缀的列rank。

## 3. 平方根一次积分也给pure slow第三层

置

\[
 h_p(t)=(1-t)^{(p-1)/2},\qquad
 G(t)=\int_0^t a(u)L(u)\,du/u,
 \quad K_2=aG.
\]

在modp formal环中，平方根规范a(0)=1给

\[
 a(t)=h_p(t)a(t^p),\quad\deg h_p<p,
 \quad h_p(0)=1.
\tag{B5}
\]

定义relative coefficient extraction C_tF(s)=Σ_m[t^{pm}]F(t)s^m。不取coefficients的p-root。B5给C_ta=a。由G_n=[t^n](aL)/n与B2，n=pm的系数满足

\[
 [t^{pm}]p^2G
   =\frac1m[t^{pm}](paL)
   \equiv\frac1m[s^m](a(s)L_{<p}(s)).
\tag{B6}
\]

n不是p倍时p²G_n仍divp。于是完整最高packet为

\[
 p^2G(t)\equiv G_{<p}(t^p),\qquad
 p^2K_2(t)\equiv a(t)G_{<p}(t^p)
             =h_p(t)K_{2,<p}(t^p).
\tag{B7}
\]

B6用整个coefficient积分身份和C_t乘积规则，不能只凭一个fixed-offset Lucas系数声称B7。K₂的最高packet含h_p，通常有non-p support；这一点与下面I_K的结论不同。

现在I_{K,n}=K_{2,n}/n。n不是p倍时p³I_{K,n}仍divp；n=pm时

\[
 [t^{pm}]p^3I_K=\frac1m[t^{pm}]p^2K_2
       \equiv\frac{K_{2,m}}m.
\]

因为B7中的h_p degree<p，抽取p倍次数时只剩h_p的constant1。所以

\[
 \boxed{p^3I_K(t)\equiv I_{K,<p}(t^p)
                 \pmod{p,t^{p^2}}.}
\tag{B8}
\]

它的slow首阶为1。B8与已有p³I_{K,p}≡1、p²I_{K,p+1}≡1/2相容，但这里的证明覆盖全部n<p²。

## 4. 精确扩大constant-c₁补正像

采用 [mixed q-Bockstein](cdt_odd_level20_cartier_mixed_bockstein_20261006.md) 的规范。给c₀∈ker M̄_p，三jet CRT行X_c使用原source新I坐标gĉ、旧H坐标−V_r，其中g=Δ²、deg g=8。其source degreeδ≤(3p+7)/2，且

\[
 X_c/p\bmod p=g(t(q))\psi_c(q^p),
\]

ψ_c包含真实Hecke lift项与horizontal extraction项，不删除ΘA载体。t(q)是integer coordinate，故t(q)^p=t(q^p) modp；B2–B8在q坐标成为

\[
 p^3B(t(q))\equiv\bar B(t(q^p))
       \pmod{p,q^{p^2}}\quad
 (B=T_3,R,M,B_3,I_K).
\tag{B9}
\]

允许constantc₁改变ĉ→ĉ+pc₁，并对这五个background的原source坐标加入g·β_B、β_B∈k及任意integral lift。共同p⁴评价除p后的完整余项便是

\[
 g(t(q))\left\{
  \psi_c(q^p)
  +\left(\sum_i(\bar M_pc_1)_i\bar\Xi_i\right)(q^p)
  +\sum_B\beta_B\bar B(t(q^p))\right\}.
\tag{B10}
\]

因此这个明确constant-c₁加五background family中，S2成功的充要条件是

\[
 \boxed{\psi_c\in\operatorname{image}(\bar M_p\bar\Xi)
       +\operatorname{span}_k
        \{\bar T_3,\bar R,\bar M,\bar B_3,\bar I_K\},}
\tag{B11}
\]

只取当前slow q前缀，五函数都按t=t(q)表示。符号正负可由选择c₁、β反向吸收。g(0)=1，乘它不掩盖余项。

这里background coefficients是**unit residue**，不是前置p倍。在共同p⁴ source中，各列本来baseline1；乘p后再加只会影响第三层或更深，不能改变B10。β的coefficientdegree仅为deg g=8，所以若B11完整成功，base row的degree仍≤δ；之后按同一D与完整prefix乘h的规则不变。

## 5. 单独五列确有unit minor，但未证明与Ξ无交

按T₃、R、M、B₃、I_K的列顺序，slow t系数n=1,…,5为

\[
 \begin{pmatrix}
 0&0&0&1&1\\
 0&1&1/2&1/8&1/2\\
 1/6&3/4&5/12&1/27&17/54\\
 1/4&41/72&49/144&1/64&2/9\\
 7/24&65/144&41/144&1/125&21/125
 \end{pmatrix},
 \qquad\det=-\frac1{3110400}
              =-\frac1{2^9\,3^5\,5^2}.
\tag{B12}
\]

前三列由L³/6卷积、LQ卷积与harmonic²/n给出；第四列是1/n³。K₂的一阶方程给

\[
 t(1-t)K_2'=tK_2/2+L,
 \quad K_{2,n}=\frac{2n-1}{2n}K_{2,n-1}+\frac1{n^2},
 \quad I_{K,n}=K_{2,n}/n,
\]

所以最后一列也直接来自定义。B12在p≥7的每个place都是unit。若slow前缀含positive degree1,…,5（即fast N≥5p+1），这五列的实际modp rank恰为5。integer坐标t(q)=q+O(q²)使首五行只左乘unit triangular矩阵，因此q慢坐标的minor与rank结论相同。

这只证明这五列自身的rank；没有证明它们与im(MΞ)无交，没有把B11右边维数无条件增加5，也没有重复增加actual函数rank。

## 6. 范围：新补正接口而非新信用

B11给出了真实可使用的补正列，B12证明长度足够时它们自身独立；尚未证明它们在原MΞ像之外给严格新增维数，更未证明任何nonzero c₀满足B11。不把五species再计五个函数rank：它们本来已在实际rank19 source内，成本也已完整付过。

若B11成功，primitive性仍由nonzero新I投影g c₀保证；新增第二层rank还须证明不同成功方向的I投影独立并接同一source的净Smith与tensor过滤。第一层已经属于native kerM shifts和旧/background baseline1，不能重复计。更高层也没有自动得到。

本family使用旧三H、六新I和五background，已离开 [same-nine-species cap4 ceiling](cdt_odd_level20_cartier_native_s1_budget_20261006.md) 的支持条件。那个冻结界不能据此排除B11；反之，离开其条件也不代表现在能够跨log16。unit background residue与p倍lift必须始终分开。

本文全尺度依据是B2–B8的逐coefficient积分、平方根Frobenius规范及原完整packet。作者仅执行一次本次新建的 [Fraction脚本](cdt_odd_level20_cartier_background_slow_packet_20261006_verify.py)，[JSON证书](cdt_odd_level20_cartier_background_slow_packet_20261006_verify.json) 记录8项固定检查：首五行、K₂系数、B12 determinant及其denominator因子。没有执行旧producer、没有素数实验或假设nonordinary密度；实际B11的余核求解、与Ξ像的交、primitive saturation及高度收益仍开放。

root已实际完整只读新版§§1–6并独审通过：全indices packet、p/n积分与C_ta=a、integer t(q) Frobenius、commonp⁴ unit-background及constant-c₁充要接口、base degree保持δ，以及B12矩阵、递推、determinant和rank5 cutoff。conjugate_projection也实际逐次只读原packet/接口正文和新增§5–6，通过同一范围，并独立手算全部首五coefficients与determinant。两位均未执行本稿producer；审阅不声称与Ξ像无交、slow条件成功或净Smith收益。

本文及8-check配套脚本/JSON现已冻结；后续余核求解或高度研究另建报告，不更改本组三文件。
