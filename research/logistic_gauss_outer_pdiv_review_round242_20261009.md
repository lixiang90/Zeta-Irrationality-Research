# 第242轮补充：outer完整整余项实际上被p整除

2026-10-09，A独立纸证。实际FULL读C outer稿六部分O1–O12：
9354 B，SHA256
994ea8727792abc787e8b4b27db5171dc171f23a29bbd7793584eb8c4a9f416c。
以下支付同一对象中W_p(T)∈pM_h(Z_p[T])，不是数值点代入或费用lower。
本人数学程序、参数扫描、Lean及新增primary均0。

## 1. 同一完整余项

固定n<p≤5n、p≥7、h=3n、s=floor(5n/p)∈{1,2,3,4}。
写R_n=D_n⁴/D_(5n)，λ_j=Res_(t=−j)R_n，
q_e是t^eR_n的完整多项式商部，0≤e≤6n−2。
令
\[
 L_e=\tfrac32B^+((tq_e)')+\tfrac1{24}B^+((tq_e)'''),\quad
 \omega_j=S_nj\lambda_j\in Z,\quad
 \eta_{j,r}=\sum_{\substack{1\le a\le j\\p\nmid a}}a^{-r},
 \quad r=3,5.
\]
C稿完整分解中的余项entry是
\[
 (W_p(T))_{ik}
 =S_nL_{i+k}
  +\sum_{j=1}^{5n}\omega_j(-j)^{i+k}
       (T-3\eta_{j,3}-\eta_{j,5}). \tag{P1}
\]
未删除商部、任何调和head或跨p残数。结论是P1全部polynomial系数
均有valuation≥1。

## 2. 商部的首个危险degree

q_e∈Z[t]，deg(tq_e)≤5n−1。von Staudt–Clausen给Bernoulli
valuation≥−1。若s≥2，则S_n含p^s而固定24为单位，
所以S_nL_e至少p^(s−1)，特别pdiv。

若s=1，则5n<2p，deg(tq_e)≤2p−2。
对单项式t^d，一階泛函是d B^+_(d−1)；
可能的Bernoulli分母在d−1=q(p−1)。q=1时d=p抵消分母，
首个未被此系数抵消的可能degree是2p−1，超出范围。
三阶泛函是d(d−1)(d−2)B^+_(d−3)：
q=1、2、3的对应degree p+2、2p+1、3p均含p于falling factorial；
首个未抵消的可能degree4p−1也超出范围。
B_0与B_1不含p，低于微分阶的单项式为0。
故s=1时L_e本身p整，乘S_n仍pdiv。这付清商部，不以“三阶杀低次”
删除可能出现的高次多项式。

## 3. 完整残数类和全部目标系数

R_n的无穷远形式展开为t^(−n)乘以Z[[t⁻¹]]元素：
分子与首一分母均整数，分母反演保整数。因此对每个e≥0，
\[
 a_e=\sum_jj\lambda_j(-j)^e
     =-[t^{-2}]\,t^eR_n\in Z,\qquad
 \sum_j\omega_j(-j)^e=S_na_e\equiv0\pmod p. \tag{P2}
\]
这只使用形式Laurent系数与有限部分分式，没有未付泛函连续性。

令Ω_b=Σ_(j≡b modp)ω_j。将P2取e=0,…,p−1，得到
Σ_b Ω_b(−b)^e=0。Fp中p个不同节点的Vandermonde determinant是单位，
故每个Ω_b≡0。e=0包括零节点的常数单项式，未删零类。
P2因而同时证明P1的T系数至少p^s，特别pdiv。

对r=3、5，p−1不整除r。Fp*中Σ_a a^(−r)=0，
所以每个完整nondiv harmonic cycle模p为0。
于是η_(mp+b),r≡η_(b,r)只依赖b=j modp。
将P1的有理head部分按class分组，模p即
\[
 -\sum_b\Omega_b(-b)^{i+k}
       (3\eta_{b,3}+\eta_{b,5})=0. \tag{P3}
\]
P3使用全部j，包括j>p和多个p的倍数之前的完整头。
结合商部和T系数，
\[
 \boxed{W_p(T)\in pM_h(Z_p[T])}. \tag{P4}
\]

## 4. 可用范围

P4可替代原outer界仅使用的Gauss整余项，供C在同一矩阵的全部
cofactor/minor展开中计入更高层。这里只证明第一层pdiv；
未认证整个W_p具有p^(max(1,s−1))的更强head valuation，
也未从P4推出最优费用或预算<6。不能以完整leading更新块的秩
代替剩余Schur determinant的内容。

本轮A原GreedyBound与小prime稿8719 B /
0b2bdf55e221aa353b90aaabaf96b4545d0daa69465e2941166c36cad4191cdf
及其scope仍冻结；本文件单独登记后来新增的C全文读域和新paper引理。
没有改C/Root稿、241、main或manifest。保存后实际FULL复读，
身份另报；本人的纸面新证明与对C旧outer输入的独立核读分别记录。
