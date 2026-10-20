# 第270轮结算：实际Euler逆、完整清整与到期停止

2026-10-20。完成[一轮预算任务](growing_pole_budget_charter_round270_20261020.md)。**没有新无理性定理，最优本原预算仍未闭合。** 固定构造的实际来源系数已得到exp(O(m))级控制，全部有限处和有理头已有统一清整；这个尚未内容约分的安全清整族实际增长，不能承担数值反证。一轮窗口到期，结束该实现的默认投入。

## 1. 对象与本轮真正支付的接口

始终固定[269](global_source_review_round269.md)(G4)–(G5)唯一的p_i，n=8m、N=8m−1，实际X=ζ(2)+2G：
$$
M_m=(\mathcal I_{8m}(p_i(1+T)p_j(1+T)))=R_m+XI_m>0,
\quad Q_m(Z)=\det(R_m+ZI_m).
$$
R_m包括全部有理头，Q_m首一、次数m。λ_m为其全部系数的最小共同分母。对每个假设X=u/v、v>0，v^mλ_mQ_m(X)是正整数；目标仍是同一对象的
$$
\limsup_{m\to\infty}m^{-2}(\log\lambda_m+\log\det M_m)<0. \tag{270.1}
$$
没有改变比例、纯化空间、坐标或反证量词。

| 本轮接口 | 全尺度结果 | 证明 |
| --- | --- | --- |
| 实际逆与来源高度 | Hermite整数节点/逐项Newton公式；共同D_m及系数exp(O(m)) | [Euler证书](growing_pole_euler_inverse_round270.md)E1–E10 |
| 全部有理头及有限处 | B_n清全部头；S_mR_m整；每个p^e包括2处明确 | [算术证书](growing_pole_arithmetic_round270.md)A1–A6 |
| 同对象本原桥 | λ_m=S_m^m/c_m，c_m为完整整数多项式内容 | 同上A7 |
| 实际实处 | 最高m个系数锚；随尺度权的正Gram上下界 | [实处证书](growing_pole_gram_bounds_round270.md)B–G |
| 严格净预算 | 所选安全清整实际失败；最优内容收益未付 | 下文 |

## 2. 避免逆det费用：同一来源的显式证书

令d_h=lcm(1,…,h)。写u_i=z^{4m}v_i，并把
H_i(α)=[z^{4m−1}]v_i(z)(1−z)^α改为F_i(Y)=H_i((Y−1)/2)。
其value和derivative在连续整数节点0,…,2m−1完全由(G5)决定。Lagrange基在整数处整值；Hermite的value基只用一份d_(2m−1)，derivative基整值。实际value数据仅有dyadic分母，导数卷积另用一份d_N，所以这两份LCM无需相乘。

Newton差分恢复的是原p_i，给
$$
D_m=2\,4^{8m-1}d_{8m-1},\qquad D_mp_i\in\mathbb Z[z],
$$
$$
v_p(D_m)=(16m-1)\mathbf1_{p=2}+\lfloor\log_p(8m-1)\rfloor. \tag{270.2}
$$
这里及下文的floor取最大满足p^e≤所给正整数的e。相同分母也清T坐标，整平移不加费用。全部实际z系数满足
$$
\limsup m^{-1}\log\max(1,\max_{i,k}|[z^k]p_i|)
\le\mu:=9\log2+16\mathfrak h(1/4),
$$
其中\(\mathfrak h(t)=-t\log t-(1-t)\log(1-t)\)。这是对实际逆的证书，不从小det推二次行高度；也没有认定D_m最小。

## 3. 完整清整及恰当本原化

对任意整系数P、degP≤2n−2，全部有理头被
$$
B_n=2^{2n}d_{2n}^{\,2}
$$
清整。证明保留多项式头以及U_j′(1)、U_j′(1/2)：奇p^e逐残基计数，2处单独估值，不用有限样本。
因此同一费用链为
$$
S_m=B_{8m}D_m^2
=2^{48m-2}d_{8m-1}^{\,2}d_{16m}^{\,2},
\quad J_m=S_mR_m\in\operatorname{Mat}_m(\mathbb Z). \tag{270.3}
$$
先清基底两次进入Gram，再清有理头；不额外领取直接清Q的费用。

令
$$
F_m(Z)=\det(J_m+S_mZI_m)=\Lambda_mQ_m(Z),\quad
\Lambda_m=S_m^m,\quad c_m=\operatorname{content}(F_m).
$$
首项系数为Λ_m，故c_m|Λ_m且
$$
\boxed{\lambda_m=\Lambda_m/c_m},\qquad
P_m=F_m/c_m\in\mathbb Z[Z]\ \text{本原}. \tag{270.4}
$$
假设X=u/v时，v^mP_m(X)=det(vJ_m+S_muI_m)/c_m是正整数。
全素数幂安全S_m和实际最小λ_m在(270.4)中明确分开。

## 4. 所选安全清整族实际增长，不能靠裸实处改善补救

(G5)强制deg p_i=8m−1−i、首项系数1/2。令ρ=3+2√2、c=ρ/4。
单位圆变元T=(2+ξ+ξ^−1)/4与Parseval给随尺度权的单首范数下界；逐阶Gram–Schmidt因此给同一实际矩阵
$$
\det M_m\ge(5\pi/128)^m
c^{-8m^2}16^{-(15m^2-m)/2}. \tag{270.5}
$$
无需假设实际率极限存在。与(270.3)相乘，得到有限、全部m≥1的明确下界
$$
\boxed{\Lambda_m\det M_m\ge
(5\pi/128)^m d_{8m-1}^{\,2m}d_{16m}^{\,2m}
e^{\kappa_0m^2}>1},
\quad \kappa_0=34\log2-8\log\rho>10\log2. \tag{270.6}
$$
末个严格不等式只用ρ<8、5π/128>1/16及m≥1，不依赖素数渐近。这证明**未经内容约分的这一指定实际族**不能趋零；不只是安全上包络为正。

若再使用标准logd_h=h+o(h)，则
$$
\liminf m^{-2}\log(\Lambda_m\det M_m)
\ge\kappa:=48+34\log2-8\log\rho>0. \tag{270.7}
$$
实际来源高度配合实处Hadamard还给完整安全上界
$$
\limsup m^{-2}\log(\Lambda_m\det M_m)
\le48+73\log2+32\mathfrak h(1/4).
$$
两侧是同一Λ_m、同一p_i和同一实际Gram；没有拼接其他源的费用或衰减。

(270.4)说明(270.1)若成立，就必须有
$$
\liminf m^{-2}\log c_m>\kappa. \tag{270.8}
$$
证明：取(270.1)的固定严格余量δ>0，用
logc_m=log(Λ_mdetM_m)−log(λ_mdetM_m)及(270.7)，得到liminf≥κ+δ（缩小δ也可）。这只是实际内容的**必要门槛**，不是充分条件。本轮未证明这项收益，也未证明最优λ_m预算不可能；换成更紧的完整清整时，内容和安全倍数必须一起更换。

实处单首极小范数已有匹配二次率，不能仅重复最高项锚就推出更强实际det增长。实际纯空间的额外Euler约束能否给足够内容或更强实处估计，仍是缺口。

## 5. 到期决定与审阅范围

本轮付清实际逆、exp(O(m))来源、全部有理头、全素数幂安全链及实际安全族失败证书，但未改善完整数值准入，停滞计数保留10。**关闭本次n=8m、唯一(G5)空间的默认实施窗口**。不调比例、扩大参数、扫描gcd或改名续期。重开须有改变完整本原预算的新机制与全尺度证据；单独再证正性、rank或安全清整不足不够。

下一轮[271正式宏观比较](source_gate_charter_round271_20261020.md)只恢复定期资源决策，比较所有路线的最短未付接口，不自动重开这个数学source。总goal保持active，最终成功仍须新指定数值定理、完整证明链、独审及实际范围的新颖性核查。

根代理全文核三份子证书，独立重建(270.2)–(270.8)及全部有理反证。Euler代理交叉核算术与实处；实处代理交叉核Euler与算术；算术代理交叉核Euler与实处。三位均全文复核保存的主结算和271任务，分别确认全量词、2处、常数及本原桥；作者贡献不计自身独审。本文是书面结构及范围明确的停止结算，未Lean形式化，未执行数学扫描、CAS或producer，原文献和形式化资产不变。
