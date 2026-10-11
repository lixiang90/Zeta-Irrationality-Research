# 第225轮：完整模态与函数域独立性的 Root 独立纸审

2026-10-08。结论 PASS，范围为同一固定源的渐近、非有理性和条件函数域独立性；不是数值无理性或 CDT strict gate。数学程序0。

实际 FULL 读取 [B最终主稿](pade_relation_power_rank_gate_round225_20261008.md) 七节/P1–P15，14444 bytes / SHA256 `7752b5bfeb3b2090d913b999600695c5a12ffc1c731dd36649d4d89104b5b255`；实际 FULL 来源账5116 / `a6eb373027024c39bcf5fa20809cbefdb1acbe1c95ade509889b7453f5c0b28c`。最终包括 A13928 输入及 finite exterior 指数余项澄清。此前完整读过中间稿，PASS只指这个最终身份。

独立核验 P6：实际误差 ε_r=O(1/r)代入只产生O(1/r²)余项。主系数和为零使 harmonic sum 的内部 ε 严格消去，有限首尾不能抵消非零 C0 log T；无需 ε 的差分估计。下一层 B(t)∈Q[t]。三个实际 Fourier 大根分别代表线性、二次和三次不可约因子，μ1位于degree3域且其 conjugates模不同，μ2位于Q(√3)且共轭不同，因此 Galois 传递确付六根统一 γ=−11/2。

独立核验 P8：companion 右向量 e(t)满足 C∞e=t e−χ(t)e6，微分后左乘 μ 的左特征向量得 ℓe=χ′(μ)ℓe6。C1e=−B(μ)e6，故 diagonal correction/μ与 P6一致。nearidentity gauge 清 off-diagonal 后除 r^γ，系统确为 D+O(1/r²)，不能只据“可和扰动”免费宣称完整基。

P9的两方向Green完整支付这一步。|μi/μj|<1用过去和、≥1用未来和；等模复对和自身unit ratio都在未来组，forcing O(k^−2)绝对可和。past几何和及future尾把forcing送到O(1/r)。反馈多一因子1/r，使 sup r|z_r| 的operator norm为O(1/R)，因此收缩。六列 I+O(1/r)最终可逆，解空间basis实际存在，不是formal展开。

I无限非零另由已付无限Δ及经典ζ3结果证明；既有指数衰减再剔除三个大根。B1/B3对a,b的det1/30保证其最大pair系数非零，small系数至少一个非零和不同根的Vandermonde保证J主项非零。其他有限products有模gap；可能的大模态亚三角修正不改变最大pair的det。等模complex主项不能逐项支配，Cesàro平方均值正确支付limsup。J/T^r→0与确切root rate合并才排除有理GF，未误用“非多项式”。

原径向分支已证明D非亚纯，目标H在该点全纯；有理因子P即使有有限零仍可在邻域除，故D不在span_Q(z){1,H}。再用H非有理得到Q(z)-rank3。没有宣称最小微分rank3或外幂difference20为CDT rank20。两值relative gain与safe166/9的比较范围正确；不是对任意图的上限。

Root实际已完整读C11160、A最终13928、原branch6523及对应来源账，并纸审其必要接口。B的Apéry四页全文与CDT20页中的2–5页读取归B账登记；Root本轮FULL读其scope，不冒称本人重新FULL这些PDF。Root实际CDT固定选段、DLMF所用完整条件另载总scope；新Green证明未借未读任意阶定理。无程序、CAS、扫描、积分、PSLQ、Lean或旧producer重跑。保存后实际全文自读；另由A给B最终稿独审收据。
