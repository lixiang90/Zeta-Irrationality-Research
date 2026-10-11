# actual source pencil regularity 的独立纸面核查

2026-10-07，root。实际完整读取主稿 [source pencil](cdt_odd_paired_source_pencil_regular_20261007.md)，SHA256 879d8889c956d63b7b3c840c94f958a3011541698c25c1b6938c80ef7e506f8a；完整重读冻结 source-radical-response S1–S14，并逐项读回 actual-local-Gram G3 的 literal U,V,W,C 定义及 single-bordered B2–B4 的 lift/normalization。本文纯静态阅读与纸面证明检查，没有运行或导入任何数学程序。

**结论：在主稿注明的范围内通过，无需修改。** P3–8 是任意 char≠2 域上 symmetric pencil 的完整递归判据；P9 是 actual staircase regular 这一未证条件下的原对象推论；P10–18 是真正 first residual 所需的实际 tail 与 jet 精度。没有将其中任何条件当成已验证的原 family 定理。

核查了 rad G 分裂和 A|radG 的常数非退化部分消元：W1,W0 的交叉为0，因此剩余 B 没有额外 Schur 项。B 不满列秩给当前 pencil 的共同 kernel；B 满列秩时可取 BᵀR=I。按 E,R,W0 排列的 hyperbolic border 逆为 [[0,I],[I,−M_t]]，交叉 [D_t,0] 的 Schur 修正准确为0。因此下一步仍是 affine pencil，不产生 t² 项，也不偷偷除未知 G_E。

每个非终止步骤降低维数 a+2b>0。GL basis 变化支付 determinant 的平方；已知 unit A11 与 hyperbolic border 的 (−1)^b 给非零常数，故递归 regular/singular 为必要且充分。G=0、A unit、A singular、d=0 和 b=0 均正确覆盖。最终 degree=d_*≤rank G；主稿3阶无共同 kernel 却恒奇异的例子准确说明为什么不能只查起始 kerA∩kerG。

actual P9 保留 k=dim ker A5，而非误用 d_* 来计算 Smith multiplicity；degree d_* 只控制坏 source residue 个数。X 至少 p³ 的 normalized perturbation 不进入 first residual，所以 conditional whole-X 常数非零和 v_pD_A=−34r+k 均按原费用支付。actual pencil regular、fixed rational α 无限成功和目标无限非零并未获得。

从 frozen G3 直接核 α=0 的 U=−6βH⁽⁴⁾、V=CU+24(X−βH⁽⁵⁾)。tail j=p+l 处 2n+j=p+8r+l、6n−j=6r−1−l，唯一 p 极点准确给 C=2/p+c_l，故 p⁴U≡−6β、p⁵V≡−36β−6pβc_l (mod p²)。归一化 jets x=P/p^ε、y=pP'/p^ε 使 P11 无遗漏 p 因子；head 的最坏归一化仍至少 p²，不能进入第一层。

P15 的 TᵀNT/p 必须先在 mod p² 或整 lift 中算，再除p。leading N 杀K，故已知 unit 补空间的 Schur 交叉乘积除p后模p消失，换 T 为 T+pR 也不改变该 restricted form。weak P(a−p) modp³、P'(a−p) modp² 的精度确实必要；Taylor 展开的 p²R_Q(a) 在 x 的 p 层留下，不能从冻结 halfjet modp² 代表补出。P17 保留真实 −p shift 和 χ/2，P18 支付 strong 一阶修正。

审阅范围不含求 actual A、求实际 staircase 或任何新 prime experiment。数学执行0、失败0、重跑0、旧/同行 execute/import0、Lean0。此次核查支持新的结构判据与精度接口，不支持新的特殊值无理性或线性无关性结论。正式最终收据由作者实际完整阅读本 review 后另存，当前 review bytes 可冻结。
