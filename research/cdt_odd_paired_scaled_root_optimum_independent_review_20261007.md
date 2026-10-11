# 单根尺度最优与可支付解析率：独立实际全文审阅

2026-10-07，NEW，审阅人 `/root/masked_racah_finalize`。旧及同行数学程序 execute/import/rerun 0；本审没有新增数学执行、素数数据或 PDF 下载。518既存冻结记录保持只读。本文记录已经完成的静态阅读和纸面检查，不以未来收据作为当前证据。

## V1. 当前实际读取对象

本轮实际完整读取主稿 [scaled-root S1–S18](cdt_odd_paired_scaled_root_optimum_20261007.md)，物理 SHA256
`c529ece382b5e9959d35210a8ef3675d4ef76fa08ffab60daa232a7f359552e2`。
完整读取以下三件的全文及保存结果每个字段：

- [certify.py](cdt_odd_paired_scaled_root_optimum_20261007_certify.py)，SHA `95e7ff89a97a6633de4441288a32c787d6ef59aa16efc93d7d50dec5f744e242`；仅静态读取，未执行或 import。
- [certify.json](cdt_odd_paired_scaled_root_optimum_20261007_certify.json)，SHA `321d0da51964c27e6fa710d844b2d251071e2736cf6bc5b6047b8d0b1b1855ff`；state PASS_FIRST1、7 explicit assertions、18 completed outer bisections，全部 fixed_values/optimum/limitations 已读。
- [guard](cdt_odd_paired_scaled_root_optimum_20261007_certify_guard.json)，SHA `e1e97654436d92dada737c0a9dee938008df3b976e85d67cc51a422647364189`；exclusive-create STARTED_FIRST1 保存历史开始状态，成功状态取自独立结果。

另实际全文回读冻结 [coupled Gram 稿](cdt_odd_paired_coupled_gram_decay_20261007.md) C1–C23、C1–C10各节，确认新主稿使用其真实 all-n C9 和同一 envelope。本人没有读取同行本轮 Mhaskar–Saff PDF，不继承作者7页读域；相关数学在稿中自足证明，primary阅读另由作者收据记录。本人另外实际读的KS PDF28–29只服务本人掩膜Racah稿，不挪作本解析审阅的一手阅读。

## V2. all-s 的唯一双峰与最优根

独立核 S5 导数：Q''=2(y²−416)/[(4+y²)(64+y²)]，Q' 在0右端为π/2，最终为−2π。Q' 的先减后增及 Q'(1)<0 保证唯一最大点 y0∈(0,1)。左峰在 min(y0,√s) 以内严格凹，越过 y0 后导数严格负，因此左峰唯一；其 stationary map a²+2a/Q'(a) 的导数严格正。

对整个 y>√s，Q''<2/y²，而 log(y²−s) 的负曲率绝对值严格大于2/y²；故右峰全区间严格凹。这里没有错误地要求 Q 全轴严格凹。两侧 envelope 导数 L'>1/s、R'<0，而0<I'<1/s；L−R 从−∞到+∞严格增，故 unique crossing 确实给整个 s>0 家族的唯一全局最大。主稿没有把它升级为多根分布的最优。

## V3. s=4/7 的全轴保守界

逐项核强凹性常数 cL=51/20+7/2=121/20。左取1/4时 log 因子为 log(57/112)，导数减56/57。右在 √s<y≤2 上 Q''' >0，Q''≤Q''(2)=−103/68；log 曲率下界7/9，给 cR=1403/612。右取4/3时 log 因子为 log(76/63)，导数加42/19。

两切点的全区间强凹二次式上界与源的 d²/(2c) 完全匹配。保存 JSON 的 dR upper=−4398227419/10¹²<0，结合右侧导数严格减，排除 y>2 尾部增加 supremum。负半轴按偶性覆盖。固定值的两 gain lower 分别是611819519300/10¹²和642526347079/10¹²，均严格超过3/5。以 M0≥Q(1/2) 得 ε(4/7)>3/5，范围是整个轴上的 paper bound 加 elementary interval evidence，不是有限采样 supremum。

## V4. 静态证书边界及区间正确性

静态核 Fraction interval 四则运算、包含0的平方、倒数非零符号检查；atan使用偶数96项交错余项，log使用 z=(x−1)/(x+1) 的正几何尾，Machin identity 给π，sqrt90步二分给包含区间。所有变量依赖导致的 interval widening 只会放宽上下界，不使包含性失效。

decreasing-root 的每次 bisection 只在区间导数严格有符号时移动端点；不确定时停止。left/right 的 bracket denominators 在指定 s∈[1/2,7/10] 始终非零。outer bisection 的18步和初末 crossing 符号是保存的结果范围。

唯一性证明给 L 增、R 减，因此 Mstar lower=max(Llo lower,Rhi lower)、upper=min(Lhi upper,Rlo upper) 正确；a、b 对 s 增，所以 endpoint 拼接也正确。主稿 S9 的小数逐个匹配保存的有理端点。没有重新运行证书，也没有把7个explicit assertions称为 all-s/all-n 自动验证。

## V5. 同一 whole-X 的 all-n 支付

S1 的 degree≤n 剪切项严格位于同一 high span，其变换 det1，所以真实 whole-X D_A(X) 恒等。S2 是冻结 coupled C9 的同一个对象。S13 convex combination 对奇偶 n 的 θ=2floor(n/2)/n 成立；n1的q=1单独按有限常数覆盖，避免0乘−∞的记号歧义。

实际两镜像 δ 值分别2n+1/2−m与m−1/2，均≥m−1/2。因此 S15 对每个 actual head 付费，不假设镜像q相等。midpoint sum 对固定s的 Lipschitz function 给 O(1) 误差；乘 N 后只有 O(n)。综合 n log A 与两次 head-log，4Nn log n 准确抵消，新增主率是2Nn ε(s)，奇数 n 与 n²只差 O(n)。尾部的固定 polynomial prefactor 由统一指数衰减吸收，未遗留未计费 supremum。

S17 保留 −2logΓ_n 后再用 liminf γ，没有未经证明把 gcd 余项改成 O(nlog n)。旧 high/mirror/factorial/Γ 只支付一次。结合冻结 strict baseline，S18 的 limsup<−12.60357285412558 由 ε>3/5 正确得到。

## V6. 独审结论和范围

当前 c529 主稿 S1–S18 与全部保存 source/result/guard 的静态范围通过独立全文纸面核查。新增成果是单根尺度家族全局唯一最优、显式有理尺度全轴 ε>3/5，以及同一原格 all-n 可支付解析率改善。

没有证明 actual determinant 无限次非零、固定有理 source 无限成功、辅助单位或 higher Smith 的全尺度结果；safe arithmetic upper scale 约40.3145仍未和当前已证 decay 构成 strict margin。它也不是实际最小费用下界，不构成方法 no-go。没有新ζ/L/Catalan数值无理性或线性无关性、没有 Lean。同行后续若改变被审稿，必须重新记录当前读域；本审不预先审核未来修改。
