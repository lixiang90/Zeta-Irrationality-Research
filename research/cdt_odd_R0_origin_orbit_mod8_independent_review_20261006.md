# R0 全路径模8障碍：独立审阅

日期：2026-10-06。NEW 纸面独审。审阅者 toric_chow_completion。全部旧/同行数学 MD/PY/JSON/manifest 只读；未执行、import 或重跑数学 producer。

实际全文阅读 research/cdt_odd_R0_origin_orbit_mod8_obstruction_20261006.md，冻结候选 SHA256 **a510202c396b90fd95abc99fbba950cf6a8a53870f01b769a336ee380bf756dc**。本轮实际回读权威主报告 §§85–93，SHA256 **1e0161b49ee96adae6cc30e9e7c89ca667b81877fd484919b86e7fd38e105f4c**。旧 orbit/real/exterior/holonomy 输入的全文阅读和独审已在前轮实际完成；本轮不冒记重读其全部，以下纸面验算直接核作者列出的矩阵、真实周期身份及所引用固定范围。

## V1. 任意 word 的真正整数不变量

column coordinates 为实际 e_j=U^jδ。M3 的 U 每列和均1，所以 ℓU=ℓ，其逆亦然。M1 的首行变化是−8(0,1,4,11)，其平方零且首列未变，故逆为 I+8e_0b，ℓM1^(±1)=ℓ∓8b。physical M0=−U，且 M0逆=−U逆。

因此在整个实际轨道格上，每个 signed letter保持 ℓ modulo8，每个 physical origin letter只改变符号。δ 的 coordinates为 e_0，ℓδ=1。按任意有限正负 word长度归纳，M6/M7 对全部群元素成立；证明没有有限word搜索。M10 用 z·ΓV=8ℓz转写为模64的±8亦正确。

该群是实际 monodromy group，不是任意整辛变换；同余条件不妨碍 Zariski-dense Sp4。这两个 scope区别作者保持正确。

## V2. cycle-period 等变性和 χ twist

冻结 actual real normalization hδ=−π²(g1+3g2/4) 给 Pc 含真实 δ 的 complex line。ω=√xη 与 algebraic η 的 cycle transport比较时，scalar continuation是 χ(γ)h_{γδ}；χ非零且仅±1，所以不会改变 transported plane或 ℓ 非零条件。使用 inverse representation convention时改成γ逆，同一全word结论仍适用。

P0=kerN²⊂kerN³=kerℓ；如果γPc=P0，则其包含的γδ必须被ℓ杀掉，直接与 M6/M7矛盾。这个推论不要求 Pc有理 Betti坐标，不要求知道 g2的完整 connection matrix。改变参考路径转为η逆γ仍同一 word；有限cover取subgroup且N只乘非零integer，不改变kernel。M11–M14通过。

## V3. primitive quotient 与全部 origin branches

Pc 是 isotropic：它含 vanishing line v；conifold三个 holomorphic germs构成δ的symplectic orthogonal，故 C(v,g2)=0，进而 C(g1,g2)=0。transported Pc仍 isotropic。因此所用 decomposable wedge已经是primitive wedge，不能把某个Tate trace差错误地当成不变primitive quotient。

odd winding在χ-twisted primitive quotient中只有−1的semisimple eigenvalue，不能fixed。even nonzero winding的 unipotent exponential与N有相同invariant subspaces；regular J4 的唯一invariant二plane是kerN²。fixed nonzero decomposable wedge的line要求该plane invariant，故被 V2全部排除。作者 M16 的 primitive quotient jump 非零结论成立，任意 q不影响该商。

冻结 holonomy H2–H4 的 connected-Galois stable evaluation kernel lemma于是适用于每条 transported branch：非零primitive quotient jump迫evaluation kernel含全九维module，任何 algebraic linear differential row若给meromorphic output必恒零。添加独立1只保留target-blind algebraic项；finite integration若其导数属于这个module，也不能产生保留目标的输出。范围不包括新的 nonlinear/tensor packet或新 jump-height theorem。

## V4. conifold criterion与共同 map

作者使用冻结 E20.3 的成对九行tuple，必须保持 paired/raw distinction。对于 isotropic plane Pcγ，conifold transvection固定它当且仅当它含δ：若它含δ，plane内transvection determinant1，wedge固定；若它不含δ却固定，则它必须包含在δ垂直的三维空间中，而其二维isotropic像在该空间的二维非退化symplectic quotient不可能仍二维，矛盾。因此 criterion v∈γPc 与q无关。

paired纯行的source translation在该criterion下也被含δ的wedge消掉，所以实际上holomorphic，而非只从 monodromy固定偷推无poles。该后一步依赖已经证明的 E20.3，不能对raw derivative jets改写；作者明确遵守。

nonconstant holomorphic φ盘内若取target-origin值1，则有限正ramification给 M16 的nonzero local power，矛盾。盘内target-conifold值0的每个 puncture若q*合法，以上q-independent criterion便令全部q合法；其小loops生成punctured disk基本群，于是全部q single-valued并可填点。open disk情形逐compact subdisk证明亦成立。若允许meromorphic map，∞ pole由冻结 E22排除。

CDT boundary regularity不从这些局部延拓推出来；作者保留另外核查范围。逐number-field embedding应用所得共同domain，使同一map的 q=0 rank10 arithmetic reference已强制 M17。map即使先依赖q*挑选，挑完仍可给q0使用；这里并没有要求构造map本来独立于q。

## V5. 独审结论

M6–M17按列明冻结输入通过独立纸面核验。新增实际内容为全部word的模8不变量、全部transported-origin不可填，以及指定 current paired packet/CDT maps的meromorphy自动对参数共同。

最高log³取消仍是有效的 marked-section资料，但它不能填点，也不能仅凭 integer Betti flag变成 arithmetic Taylor gauge。剩余突破需要改变packet/representation或实际构造full-jump local-height收益。没有新的特殊值无理性、超越性、线性无关性或Lean结论。

本 NEW独审全文回读后冻结。数学 producer执行数0；没有新增PDF。来源实际scope如首段，不将本轮另一flag/slopes任务下载的原件算作此模8证明的输入。

