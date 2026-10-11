# 真实配对辅助素数结构稿：独立全文审阅

日期：2026-10-06。审阅者：`/root/toric_chow_completion`。NEW 独审，不修改被审稿；未执行、import或重跑任何同行或冻结数学producer。下述通过只针对明确列出的纸面命题与来源范围，不把有限探针推广为无限非零。

## V1. 实际审阅文件与固定输入

实际全文读取作者结构稿 `research/cdt_odd_paired_auxiliary_units_structure_20261006.md`，全部§1–11、U1–U35，SHA256：

`dcc6d4d670dbcc3960936d3ee1b21a877f73c03e2ba65c479c9d550e0624a8a5`。

另实际全文重读冻结辅助素数稿 A1–A13，SHA `4d907340bf9752b3fee94173ecaaddfd81b11cfb5760e8c9954ae4528ce6581b`，特别反射偶子空间、shared节点的η=1/2、真实middle修正与conditional Smith范围。不是仅核一个替代的full trace矩阵。

实际静态全文读作者NEW probe PY：

`research/cdt_odd_paired_auxiliary_units_structure_20261006_verify.py`，SHA `b445ebd6b1d52eb1a73fbc4aa003542aa7fb11f9f6ab2551e06fa2ed9a5910c5`；

以及完整JSON40案例：

`research/cdt_odd_paired_auxiliary_units_structure_20261006_verify.json`，SHA `cc3417ecff851db9aa7a0b37cf38d7e13f114cb8db8e2dab67de643cbdd0e884`。

只读了代码，没有执行或import。代码确实构造真实folded三组moments、核Wilson节点，再作有限域Gaussian rank/determinant；其范围是r≤90的40个辅助素数。它没有实现全尺度CRT/Padé/Pearson证明，也不能替代这些纸面论证。

## V2. 反射商、middle与Fermat/CRT

纸面独核通过U1–U16。m偶数使m=2r、p=18r+1覆盖原辅助条件；t的反射中心模p为−5r。负节点平移后为−r+1,…,5r，平方节点k²（0≤k≤5r）互异。T/Q的degree profiles正是冻结辅助稿的维r/3r反射偶空间。

逐节点核对μ与γ：k=0的cross2，1≤k<r的cross4，其他cross5，确由η=1/2产生，不是另选lift。U10的full-plus-middle公式和U12的E/D展开准确。middle评价Vandermonde满射且权重非零，所以该修正的秩为r，不能当固定rank误差删除。

U7的Wilson负号由 `(9r−k)!(9r+k)!` 与p−1=18r得到；U8只在内部是正确weight ratio。平方剩余元1²,…,(9r)²给首一恒等式PS=u^(9r+1)−u。微分后的P'S在0处为−1，在非零节点为−1/2；因此U15的ν归一化准确。P/S互素，middle CRT projectorχ及χ²=χ成立。

## V3. 真正的矩分子、inverse与Padé失败条件

纸面独核通过U17–U28。Stieltjes分子由节点值w_kP'(u_k)决定；利用U15，对full F_j正好是−S^(j−1)。真正g/c/h保留 `(1+χ)` 与 `(5−χ)`，没有漏middle。

在χ=0和1两个CRT分量，matrix numerator determinant分别为−6S^−4与−3S^−4，故ambient可逆。U20显示的inverse逐分量相乘为恒等，没有额外basis scale。

U21的descending high-coefficient行到负Laurent行是diagonal1的下三角变换。故scalar determinant精确等于对应高余式矩阵；matrix profile两行组分别应用同一单位三角论证，det亦精确相等。U23/24与U27/28的degree cutoff分别为4r、2r，和profile(r,3r)一致；congruences来自实际inverse，未用未知normality。

环境unit不是截断unit：原稿给出的P=z²−1、q=1、d=1例中首矩为0，确可排除该错误推理。这里通过的是normality的准确重述，不是已证明它成立。

## V4. Full残数与Pearson端点

纸面独核通过U29/30。对 `f/[S_y^5(y^p−y)]dy`，非head点residue为−f/S_y^5；head点的六阶pole给负的v^5 coefficient，p−1>5排除了局部额外项。无穷residue为0，因此总residue确给U29的负号。U30 polynomial degree≤36r−4<2(p−1)，唯一可能贡献的正倍数指数是p−1；constant项在Fp中和为p=0。两式都只是full部分，middle保留。

U33与U35的最低class证明准确适用于r≥2以及本文定义的逐点polynomial Pearson pairs。full低degree假设给≤11次的交叉多项式，在10r内部点为0；actual低degree假设给≤13次多项式，在10r−2个非jump内部点为0。节点数足够使其为恒等式。

互素因式迫上端点a+1至少六重root；下端点之前的真实flux还迫−a为root。actual两jump再迫−r+1与r为root；四个位置模p互异，给σ degree≥9。explicit pairs实现full degrees7/6和actual9/8；最高τ系数分别83/9、101/9，在p=18r+1族不能消失。故class5/class7准确。r1不主张最低class，亦未排除rational gauges或matrix-valued方法。

## V5. 一手来源的实际独读与可用范围

实际全文读取作者来源收据的初稿及正式终稿 `literature/manifest_cdt_odd_paired_auxiliary_units_structure_20261006.json`，终稿SHA `244b2c872e16a01a1822a095b87636e32475238a2e657683c1d12371aa701a4f`，并核JSON与哈希。以下三份原件已在本轮由作者正常TLS归档；审阅者新增下载0。本人实际只读抽取完整页面，全部UTF-8输出，无截断：

- Dominici，PDF1–8（总14页），SHA `52854a7a282f70a414ddbc6fd764a5413d31eeac5108b054031af8b5b394e503`。PDF1–2的OP/Heilermann输入要求nonzero norms；PDF3–6的finite-weight Cauchy–Binet/Hahn product与其具体权重相连。未将待证normality循环作为输入，也未套用其Hahn product到真实U6。
- Rimányi–Varchenko，PDF1–8（总19页），SHA `e412b1b111dee5cd7eee3d471adaf436dc4e86084935038a30b7d876f47ef48f`。实际读Fp-integral的coefficient定义及PDF5–6 Theorem4.1；其指定beta/Vandermonde master polynomial与指数条件明确，尚无合法U6转换。未称读PDF9及其后的证明。
- Rosengren，完整PDF1–10，SHA `f98673a3e94e864faba6b1f117eb0606d01ecf86584017b4311152586a70ad74`。PDF2的Heine形式恒等式与PDF7的discrete balanced参数分别核读；没有从真实middle-corrected measure推得balanced参数。

准确新增独读26 distinct PDF页，本人下载0，数学producer执行0。各原件URL/归档由作者NEW收据记录；这里只证明本文所述谨慎适用范围与实际原件相符，不声称三篇全文独审。

## V6. 独审结论与未证gate

在上述范围内，U1–U35纸面推导、原件适用界线、finite probe叙述全部通过。真正新进展是两个实际有限域determinants已化为完全指定的scalar与matrix高余式/Padé normality问题，并证明middle不是可忽略扰动、端点阻止低class Pearson套用。

仍未证明无限多个p=18r+1上的两unit条件；finite40案例不承担该命题。没有从此得到全prime n²费用改善、matched strict margin或新的数值无理性/线性无关性。审阅者旧/同行数学执行、import、重跑均0；没有Lean声称。本文保存后实际全文回读，再固定最终SHA。
