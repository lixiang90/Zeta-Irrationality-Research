# 第225轮：实际径向分支与共同图桥的独立审核

2026-10-08，C。结论 **PASS，无必要修改**。只新增本收据，未改作者稿、冻结稿、main 或 manifest。本审数学程序 **0**。

## 实际 FULL 对象

实际 FULL 读取 [branch 稿](pade_actual_branch_graph_bridge_round225_20261008.md) 五节/S1–S4及全部结论边界：6523 bytes，SHA256 `5001f4693f14768d3a9ebc39f71934aaeb64aaac733225b7201911864c60be6a`。

实际 FULL 读取 [CDT 完整选段](../literature/pade_singular_bridge_sources_round225_20261008/root_cdt_fixed_v2_theorems2_5_1_2_7_1_remark2_11_1.txt)：10820 bytes，SHA256 `f0dd7f1b8dccd640392dfe1c8a0dfc86e8c735d8bfa201ff515b521fa7cc201b`。范围是完整 Th2.5.1 及紧接说明（印刷16–17页）、完整 Th2.7.1 statement/跨页证明及相邻定义（19–20页）、完整 Basic Remark2.11.1 的 Koebe/应用段（29–30页）。本人此次读取保存 text 选段，未重新 FULL 读220页PDF、证明Th2.5.1全章或其参考书，也不冒称Root的official web核对为本人阅读。

实际 FULL 读取 [Root 三模态独审](research_round225_actual_modes_review_20261008.md)：3437 bytes，SHA256 `2d9fe448e12eeff306dbd7a249c3d35ae750a69f6675fc119d091c79bfe80d35`。其输入 C 三模态最终稿11160 bytes / `37d2a980146055a4b3509d7861f77d674bec6fca40cb55e5ec138aeaccc81788`及scope3038 bytes / `2ae339ba537a254c7aee104a182b41540fa1ffdcb2da1a610f71e5d2b879924f`为本人已实际 FULL 最终作者读；这不能充作本人对自己稿的独审。

## 径向非亚纯与域上分离

S1给真实 radius R，不是两个安全下界。F(t)=D(−t/M)的系数最终为正，绝对和在t=1有限；16阶下降阶乘使系数为d r^−1/2(1+O(1/r))，error绝对可求和。将t=e^−s，所写Riemann和的近0/远∞以积分控制，得sqrt(π)s^−1/2；t^−16及s/(1−t)→1，因此S3的常数、指数正确。

有限径向极限排除兼容该径向分支的pole，16阶导数发散又排除可去点。故不能在此分支上亚纯延拓。它没有证明完整Puiseux展开或其他绕行分支都奇异。J的strict smaller指数使X首项为−ζ(7)S1；g≠ζ(7)时Hg也有非零同首项，g=ζ(7)时Hg在更大圆盘全纯。范围正确。

在目标假设g=ζ(7)∈Q下，有理函数P,Q,T的关系若P不恒零，QHg+T在z0邻域亚纯，除以非零有理P仍亚纯。P在该点的有限零/pole不能消除非亚纯障碍；与原disc内身份的唯一性使它必须兼容原径向D。故P必为0，D不属于span_Q(z){1,Hg}。进而三行field维数为3等价于Hg不属于Q(z)，没有把非多项式误作非有理。

完整指数分母加无限非零可提供有限radius，但不能替非有理证明。B正在研究的其他225接口不是这份作者稿已付内容，本PASS没有预先认证它或要求回改作者范围。

## Koebe的实际路径条件与入口上限

若D∘φ是unit disc上的亚纯延拓且φ univalent，逆函数确给Ω=φ(D_unit)上的single-valued亚纯函数，并与原D芽在0附近相符。假定|φ′(0)|>4R，Koebe quarter定理给半径>R的完整圆盘包含在Ω；这同时包含原收敛disc、从0到z0的径向路径及z0邻域。

于是identity theorem在整个原disc内将Ω的亚纯函数固定为D，而非任意其他branch。它在z0的亚纯性必与S3矛盾。严格假设的反证因此只给|φ′(0)|≤4R，等号未免费排除。M=(3ab)^9>4，故4R<1；必要log derivative正值的入口已经失败。

CDT选段中Th2.5.1的holonomic版本确要求|φ′(0)|>exp τ(b)，τ(b)非负，并要求所用Q(x)-独立行在同一φ上亚纯；Th2.7.1是univalent specialization。稿中只排除**原变量下、保留D行的这个univalent普通图入口**，不以安全flat费用最优性或difference20当作前提。

没有“Ω包含z0便所有branch都奇异”的推断。相对radius ratio不能直接充作|φ′(0)|；关系Hg自己的图、完整付费的变量变换/shear、ramified/multivalent图或别的holonomy模板均未被排除。这里是明确入口障碍，不是ζ值目标的不可能性定理。

## 执行与保存

本审只做文档全文读取、metadata查询和纸面核验；无数学程序、扫描、CAS、积分、root solver、PSLQ、Lean、旧producer或Git。没有采用A尚未独审的stable改善或B未来Galois结论。原数值目标仍开放。保存后实际 FULL 复读本收据，最终bytes/hash另报。
