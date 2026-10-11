# 第232轮：截区源的真实周期与全尺度投影独立证明

2026-10-08，Root。新对象由B提出后，Root独立推导起始周期、递推及全部高支撑有限头，并得到下述全尺度rank证明；B亦独立核归一化。C纸核rank关键链。以下不借程序。

令外区Ω={t:1/2≤|t|≤1}，

\[
M(i,j)=\int_\Omega\int_0^1
\frac{|t|t^is^j}{\sqrt{1-t^2}(1-ts)}\,ds\,dt,
\quad m_{2l}=\int_\Omega\frac{|t|t^{2l}}{\sqrt{1-t^2}}dt,
\quad K_l=M(2l,0).
\]

所有偶数矩均收敛：合并正负t后核为1/(1−t²s²)，角点奇性仍可积。令V=Cl₂(π/3)=(3√3/4)L(2,χ₋₃)。这是实际数值身份；不把V无理当作已由L的Q-无理推出，也不宣称全球新颖性已核尽。

## 1. 起始周期和完整递推

积分s再置t=sinθ给

\[
K_0=\int_{\pi/6}^{\pi/2}\log\frac{1+\sin\theta}{1-\sin\theta}\,d\theta
=4\int_{\pi/3}^{\pi/2}\log\tan u\,du
=2\{\mathrm{Cl}_2(2\pi/3)+\mathrm{Cl}_2(\pi/3)\}
=\frac{10}{3}V.
\]

Cl₂(2π/3)=(2/3)Cl₂(π/3)可由绝对收敛Fourier级数与二倍角身份直接取得。端点log奇性可积，以上积分无未记边界项。

写m_{2l}=√3 r_l，代换u=√(1−t²)和分部积分给

\[
r_0=1,\quad (2l+1)r_l=2l r_{l-1}+4^{-l};
\qquad
2lK_l=(2l-1)K_{l-1}+\sqrt3r_{l-1}+\sqrt3\,4^{-l}\log3.
\]

后式的边界是下限t=1/2带来的正项√3·4^{-l}log3。置c_l=4^{-l}binom(2l,l)，α₀=ρ₀=0，

\[
2l\alpha_l=(2l-1)\alpha_{l-1}+4^{-l},\qquad
2l\rho_l=(2l-1)\rho_{l-1}+r_{l-1}.
\]

则r_l,α_l,ρ_l皆Q，且每个l有完整身份

\[
K_l=\frac{10}{3}c_lV+\sqrt3\alpha_l\log3+\sqrt3\rho_l.
\tag{T1}
\]

对i≥j≥0且i,j偶，有限几何恒等式给

\[
M(i,j)=K_{(i-j)/2}
-\sum_{v=0}^{j/2-1}\frac{m_{i-j+2v}}{2v+1}.
\tag{T2}
\]

所以不存在只计算对角线、漏掉另一周期或把高权CMZV直接认成V的问题。

## 2. 新增log通道可以在全尺度消去而保留目标满秩

令ν(dx)=dx/(π√x√(1−x))，γ=π/(6√3)，

\[
\beta_l=\frac1{2\sqrt3}\int_0^{1/4}\frac{x^l\,dx}{\sqrt x\sqrt{1-x}}.
\]

直接积分β₀=γ。对x^{l−1/2}√(1−x)分部积分给

\[
2l\beta_l=(2l-1)\beta_{l-1}-4^{-l}.
\]

与α递推比较，得到β_l=γc_l−α_l。
若I_l=∫₀^{1/4}x^l dν，则β_l=3γI_l，故

\[
\alpha_l=\gamma(c_l-3I_l).
\tag{T3}
\]

对任意m≥1，d=m−1，定义2m×2m有理栈

\[
E=\begin{bmatrix}C\\D\end{bmatrix},\quad
C_{sr}=c_{r+s},\ D_{sr}=\alpha_{r+s},\quad
0\le s<m,\ 0\le r<2m.
\]

**E在Q上可逆。** 实数行变换把两块化为ν在[0,1/4]及[1/4,1]上的各m个矩。若E的右核给非零p(x)=Σ_{r<2m}u_rx^r，则p在每一开区间都与全部次数<m多项式正交。若某区间p的符号改变少于m次，以这些改变点构造次数<m的乘积多项式，使其与p乘积同号且非零，正积分与正交矛盾。两区间因此各至少m个不同实零点，超过deg p≤2m−1。端点1/4不能作为开区间符号改变点，未重复计数。

栈元素全为Q，实可逆即Q可逆。证明中γ是实row shear，仅用于证明rank；**没有把含π的shear当成有理整格投影。**

取U=E^{-1}[I_m;0]∈Mat_{2m,m}(Q)，即

\[
CU=I_m,\qquad DU=0.
\tag{T4}
\]

这给整个列池的共同log通道核，且在核中目标输出rank为m。

## 3. 投影作用于实际完整矩阵，以及仍欠的接口

用i=2(d+r)、j=2(d−s)，令R_{rs}=ρ_{r+s}−Σ_{v<d−s}r_{r+s+v}/(2v+1)。由(T1)–(T2)，实际2m×m矩阵为

\[
\mathcal M=\frac{10}{3}V C^\mathsf T
+\sqrt3\log3 D^\mathsf T+\sqrt3 R.
\]

因此

\[
U^\mathsf T\mathcal M=\frac{10}{3}V I_m+\sqrt3\,U^\mathsf TR.
\tag{T5}
\]

这是同一真实积分矩阵的完整投影；目标系数是满秩m，而非普通rank1移位Gram。任意固定m可用有理矩阵分母整化U；全部增长素数费用、primitive content及严格收益尚未估计。

假设V=g∈Q，则(T5)属于K=Q(√3)。另一嵌入的矩阵是(10/3)gI_m−√3UᵀR；不能再次把其真实V替换成−g。形式目标行列式的最高系数(10/3)^m非零，但这**不保证**在实际V处两个嵌入无界尺度非零；实积分正性也不能直接穿过Uᵀ。

新候选已支付原目标的数值身份、所有有限头及全尺度周期投影。下一有界任务必须先核同一投影值的非零机制及完整整模型/实误差是否改变228停止门槛，不能把满秩和形式det非零当成算术成功。没有新无理性/线性无关性定理。

## 4. 关系处的真实支撑变化，尚未转成严格收益

还可保持原系数格使用cofactor-free对象

\[
W_m(X)=\det\begin{bmatrix}D\\(10/3)XC+\sqrt3 R^\mathsf T\end{bmatrix}.
\]

其最高系数为(10/3)^m det[D;C]≠0。数值上对底块加√3log3倍上块，得到

\[
W_m(g)=\det\begin{bmatrix}D\\\mathcal M^\mathsf T+(10/3)(g-V)C\end{bmatrix}.
\tag{T6}
\]

其中D行是x^s在ν下带signed weight：高区[1/4,1]为γ，低区[0,1/4]为−2γ。原实际M的每行可写为

\[
M_{rs}=\int_{1/4}^1 x^r\left\{\frac\pi2x^{d+1/2}
\int_0^1\frac{y^{d-s-1/2}}{1-xy}\,dy\right\}d\nu(x).
\]

因此在真正关系g=V处，(T6)的整个底块仅由高区矩给出；g≠V时多出的C项把低区[0,1/4]带回来。这里的支持集合变化是同一对象的真实现象，比普通pole消失更具体。**尚未证明**它提供严格二次能量、有效CDT共同芽、非零性或低于其误差的完整清分母费用。含log3的数值行加法只用于实身份，未当成有理整格变换。
