# 第274轮：同一 Abel 对象的新二处全系数内容信用

2026-10-20，子代理 `abel_primitive_274`。开始先核 goal 工具为 null、工作树干净，运行状态工具并读 AGENTS、STATE、长期 goal、274任务、271完整对象与投影证书、272来源/预算/Gram稿及273差商和独审稿。仅写本文件，不改账或旧稿；没有 m、prime、参数或 CAS 扫描。

数值目标、全部实际有理反证范围和唯一对象固定为
\(Y=4\beta(5)-3\beta(4)=u/v\)、\(u\in\mathbf Z\)、\(v>0\)、\((u,v)=1\)，以及271的 \(n=2m-1\)、\(p_i\)、\(M_m\)、首一 \(Q_m\) 与最小 \(\lambda_m\)。所需最终出口仍是同一实际 \(\lambda_mQ_m(Y)\) 的严格负二次率；本稿只检验新规范的本原内容。取得下面的严格信用后结束此分工，不以正的安全 upper 或“仍可能有内容”延长274一轮窗口。

**结论。** 在273新规范
\[
\widehat S_m=2^{48m-19}d_{4m-3}^{\,6}d_{12m-4}^{\,5},\qquad
\widehat F_m=\widehat S_m^m|\det B_m|Q_m,\qquad
\widehat g_m=\operatorname{content}(\widehat F_m)
\]
下，可以严格给出新的、覆盖全部系数的二处信用
\[
\boxed{\liminf_{m\to\infty}m^{-2}\log\widehat g_m\ge30\log2.}
\tag{C1}
\]
这是在新 \(\widehat S_m\) 内避免过付所得的实际内容，不是273旧阶乘信用的再次扣除，也不是最小 \(\lambda_m\) 的 lower。它把既有完整安全 upper 降为
\[
\boxed{\limsup m^{-2}\log|\lambda_mQ_m(Y)|
\le86+18\log2+12\log6>0.}
\tag{C2}
\]
本稿未付严格负率、裸 \(Q_m(Y)\) 的必要 lower 或最优本原内容；C1–C2单独不准入数值实施。

## 1. Euler 泛函在单项式上的二处分母仅为对数级

记 \(\mathcal E(H)=\operatorname{Abel}\sum_{l\ge0}(-1)^lH(l)\)。已付恒等式为
\(\mathcal E(\binom tr)=(-1)^r/2^{r+1}\)。整数 Stirling 数展开给
\[
t^r=\sum_{k=0}^r {r\brace k}k!\binom tk.
\]
若 \(s_2(k)\) 是二进数字和，则
\[
v_2\!\left(\frac{k!}{2^{k+1}}\right)
=-s_2(k)-1\ge-1-\lfloor\log_2(r+1)\rfloor
\quad(0\le k\le r).
\tag{C3}
\]
这里 \(v_2(k!)=k-s_2(k)\) 来自逐次计数偶数倍；若k有s个1，则 \(k\ge2^s-1\)，故 \(s_2(k)\le\lfloor\log_2(k+1)\rfloor\)。有限和不降低此统一赋值下界。因此对任意 \(H\in\mathbf Q[t]\)、\(\deg H\le R\)，若全部单项式系数属于 \(2^{-a}\mathbf Z_2\)，则
\[
v_2(\mathcal E(H))\ge-a-1-\lfloor\log_2(R+1)\rfloor.
\tag{C4}
\]
C4不声称通常整数值多项式本身只有这些分母；下一节支付原对象的全部单项式系数。

## 2. 原唯一来源的全部二进单项式系数

令 \(L_0=d_{4m-3}\)、\(e=v_2(L_0)=\lfloor\log_2(4m-3)\rfloor\)。暂把平方节点升序记为 \(w_r=(r+1/2)^2\)、\(0\le r<m\)，只是排列原节点。沿272 H1–H4，写
\[
D(w)=\prod_{r<m}(w-w_r),\quad
\ell_i(w)=\frac{\prod_{j\ne i}(w-w_j)}{D'(w_i)},\quad
d_i=\sum_{j\ne i}(w_i-w_j)^{-1},\quad
e_i=\sum_{j\ne i}(w_i-w_j)^{-2},
\]
\[
p_i(w)=\ell_i(w)^3\{1+u_i(w-w_i)+v_i(w-w_i)^2\},
\quad u_i=\alpha_i-3d_i,
\quad v_i=\gamma_i/2-3d_i\alpha_i+(9d_i^2+3e_i)/2.
\tag{C5}
\]
没有换 Hermite 来源。节点差为 \((i-j)(i+j+1)\)，两个非零因子的绝对值不超过 \(4m-3\)，因而
\[
v_2(d_i)\ge-2e,\qquad v_2(e_i)\ge-4e.
\tag{C6}
\]
271实际公式给 \(L_0g_i\in\mathbf Z\)、\(2L_0^2h_i\in\mathbf Z\)。又 \(x_i\) 是奇整数的一半，故 \(4x_i^2\) 为二进单位。由原
\[
\alpha_i=(3-g_i)/(4x_i),\qquad
\gamma_i=-\alpha_i^2-
(h_i+4x_ig_i\alpha_i+2\alpha_i)/(4x_i^2)
\]
逐项得到
\[
v_2(\alpha_i)\ge-e-1,\quad
v_2(\gamma_i)\ge-2e-2,\quad
v_2(u_i)\ge-2e-1,\quad
v_2(v_i)\ge-4e-3.
\tag{C7}
\]

记 \(a_i=v_2(D'(w_i))\)。精确公式
\[
|D'(w_i)|=\frac{(m-1-i)!(m+i)!}{2i+1}
\]
给 \(a_i\le2m-1\)。在原t变量中，\(P_i(t)=p_i((t+m)^2)\)，每个 \((t+m)^2-w_j\) 都属于 \(2^{-2}\mathbf Z_2[t]\)。因此 \(\ell_i((t+m)^2)^3\) 的全部系数赋值至少为 \(-6(m-1)-3a_i\)。C7给C5方括号全部系数赋值至少为 \(-4e-7\)。合并甚至有 \(-12m-4e+2\) 的下界，以下取方便的稍弱界：
\[
\boxed{P_i(t)\in2^{-12m-4e}\mathbf Z_2[t]\quad(0\le i<m).}
\tag{C8}
\]
这是一份全系数局部证书，不是有限评价值的猜测。\(m=1\) 时空和与空积按通常约定，全部界仍适用。

## 3. 用完整有理函数的 Taylor 级数支付整个商部

原核在同一个t变量满足精确身份
\[
R_m(t)=2^{3(n+1)}
\frac{(t+1)_n^3}{\prod_{k=0}^{n}(2t+2k+1)^3}
\in2^{6m}\mathbf Z_2[[t]].
\tag{C9}
\]
分母常数项为奇整数，所以其形式 Taylor 逆在 \(\mathbf Z_2[[t]]\)；这一步不做数值取样。由C8，完整
\(F_{ij}=R_mP_iP_j\) 的每个 Taylor 系数均属于
\(2^{-18m-8e}\mathbf Z_2\)。

271已付完整乘积主部：右半系数为
\((A_{3,k},A_{2,k},A_{1,k})=(a_{3,k},3a_{3,k},0)\delta_{ik}\delta_{jk}\)，左半由反射给同样的赋值界。原 \(2^{6n}a_{3,k}\in\mathbf Z\) 给 \(v_2(a_{3,k})\ge-12m+6\)。每个半整数极点项的 Taylor 展开
\[
\frac{A_{s,k}}{(t+k+1/2)^s}
=\frac{2^sA_{s,k}}{(2t+2k+1)^s}
\]
全系数赋值不小于 \(-12m+6+s\)。令 \(F_{ij}=H_{ij}+F_{ij}^{\rm proper}\) 为原唯一分解；在0处作形式展开后相减，严格得到完整多项式商部
\[
\boxed{H_{ij}(t)\in2^{-18m-8e}\mathbf Z_2[t].}
\tag{C10}
\]
这不把商部视作完整函数的任意有限截断：使用的是实际proper主部的全Taylor证书，再对已知精确分解逐系数相减。交叉项proper为零时也覆盖。

\(\deg H_{ij}\le D=12m-7\)，两次微分不降低系数的二进赋值。C4用于 \(H_{ij}''\) 给
\[
v_2(\mathcal E(H_{ij}''))\ge-K_m,
\quad K_m=18m+8e+1+\lfloor\log_2(12m-8)\rfloor.
\tag{C11}
\]
所有proper有限调和头的分母均为奇整数，二阶导数与半整数改写只添整数因子和非负的二次幂，故其赋值至少为 \(-12m+6\)。目标栏 \(B_m=\pm192\operatorname{diag}((-1)^ka_{3,k})\) 也满足此宽松下界。符号归一不改赋值。因此原完整矩阵满足
\[
\boxed{2^{K_m}A_m,\ 2^{K_m}B_m\in M_m(\mathbf Z_2).}
\tag{C12}
\]

## 4. 新规范中的实际内容及剩余预算

置 \(e_E=\lfloor\log_2(12m-4)\rfloor\)，于是
\[
s_m:=v_2(\widehat S_m)=48m-19+6e+5e_E,
\quad \Delta_m=\max(0,s_m-K_m),
\quad S_m^*=\widehat S_m/2^{\Delta_m}.
\tag{C13}
\]
奇素数部分沿用273已付的完整证书；2处用C12或原 \(\widehat S_m\) 中较小的安全指数。所以
\(S_m^*A_m,S_m^*B_m\in M_m(\mathbf Z)\)。同一整多项式
\[
F_m^*=(S_m^*)^m|\det B_m|Q_m
=2^{-m\Delta_m}\widehat F_m\in\mathbf Z[Z]
\]
直接证明
\[
\boxed{2^{m\Delta_m}\mid\widehat g_m.}
\tag{C14}
\]
这是全系数内容，不是一个minor或首项的整除性；也没有把 \(s_m\) 当作最小 \(\lambda_m\) 的实际赋值。由于所有e项均为 \(O(\log m)\)，有 \(\Delta_m=30m+O(\log m)\)，即C1。273旧阶乘内容并未进入此推导。

与272同一实际Gram上界及273精确本原桥合并，用
\(m\log\widehat S_m=(84+48\log2+o(1))m^2\)，得到C2。正的C2不判定实际率的符号。若根的独立实际 \(Q_m(Y)\) 必要条件已经结束此负二次接口，C14仅作为被限定的算术资产保存，不构成继续优化本实现的理由；若未结束，最优 \(\lambda_m\)、其余奇素数幂内容和实际实率仍须同对象支付。本分工未建立局部Smith恰值或最优 \(\lambda_m\) 下界，未证明新数值结论。

## 5. 实际结算稿和后继任务的审读范围

本分工随后完整读过根的 `research/abel_primitive_budget_round274.md` 与 `research/source_gate_charter_round275_20261020.md`。逐项核对：274.2确是C14在新规范中的全系数二处信用；274.3从既有完整upper减去 \(30\log2\) 得到，未再次扣273旧阶乘内容；登记预算可行性改善只指完整净包络变紧，不等于数值准入；即使本轮有此改善，预定一轮重开到期仍应关闭。275明确由窗口到期主动触发宏观机会成本比较，距273仅一完成轮，未误记成连续两轮停滞，也未自动重开Abel。上述范围内未发现算术或资源决定错漏。本次没有另行复核实处稿R2–R16、精确诊断producer或其它新资产；读取根对这些资产的引用不计作本分工的独立证明。仅在本文件记录审读范围，不改账、其它稿件或另开数学窗口。
