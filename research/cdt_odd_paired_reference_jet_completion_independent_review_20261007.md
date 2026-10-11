# actual reference-jet completion 的独立纸面审阅

2026-10-07，/root/source_pencil_finalize。实际完整读取[最终主稿](cdt_odd_paired_reference_jet_completion_20261007.md)J1–J6、全部J1–J14公式，最终SHA256 944a8bf8dcc19f1baba2c8f56bae480739ff5c2e2d4e28ea5483efeade13bd68；此前亦完整读过未添J14/J6的candidate。实际完整重读冻结source-radical-response S1–S14与source-pencil-regular P1–P7，并与本人已完整自读的[exact-lift-boundary](cdt_odd_paired_exact_lift_boundary_20261007.md)ca43e16f逐项对接。核查方式为静态阅读及独立纸面推导，未执行/import/rerun任何数学producer。

**结论：PASS，数学上无需修改；各正常性条件仍必须按主稿保留。**

1. J2的strong pR与weak p²R对应normalized values均增加pR(a) modp²；normalized derivatives均增加p²R'，因此不贡献first residual。参考多项式无需char0 exact pairing，却需要指定modp/modp²精度，原primitive满射及本轮exact boundary E8确保这种actual lift确实存在。head最坏仍p²，tail jets整；主稿没有把reference determinant冒称原全局D_A。
2. J4先在literal modp²中形成TᵀN_refT，再在确认整除p后除p，正确保留leading carry。leading matrix杀K使Schur cross乘积和T↦T+pU变化除p后模p消失；不能先删去modp为零的form。J9对K0的表达仍通过J4计算，已避开这个潜在错误。
3. 独立展开原tail −6β(xyᵀ+yxᵀ)−36βxxᵀ，并代入y+6x=−D^-1LᵀΘ，得到J7的正号和系数6β。p层c_l乘value变化只形成p²项；derivative与head不进入。源斜率的冻结S14系数1/6乘8α准确给J8的4α/3。整个边界修正和源斜率rank≤2rankΘ，但这不是非退化证明。
4. K0=kerΘ上J7/J8两侧修正同时消失，故actual子form等于reference子form且不依赖α。参考变化满足同一精度时只改变Θ边界，K0子form不变。该结论允许finite-field相消，主稿没有据此免费求逆H。
5. 明确假设H unit后，J10所有blocks尺寸正确，J11合法Schur得到τ阶二次gate。source cross项为(4α/3)P0，所以二次系数为−(16/9)P0H^-1P0ᵀ，独立actual B。若该压缩也unit，最高det项degree恰2τ、系数J13非零；必须h≥τ。h=0、τ=0的空块情形正确，根数控制不改变原Smith中使用的k。此处合法的二次Schur与前轮affine staircase的hyperbolic零修正对应不同消元，不矛盾。
6. J14对本人E6/E14/E19的桥接正确：各column的actual L-boundary是原E-weighted pair defect的head sum，weak化为H_(4r+z)^(2)+H_(6r+z−1)^(2)，strong可采用A-weighted reference gauge。reference N的carry与这个显式B相加确实计算原actual first form，消除了任意第二阶negative-value选择；未证明所得矩阵正常性、无限nonzero或fixed rational source无限成功。

本人本轮primary PDF实读0、下载0；J6所记37页PDF、6distinct页root实读、SHA和generic论文范围由root来源收据承担，本审阅未独立验证PDF内容。主稿明确未套generic复数regular-pencil perturbation来证明当前有限域实际family。

数学producer执行0、失败0、rerun0，旧/同行execute/import0，辅助单位素数扩表0，Lean0。审阅支持actual first form的结构完成和条件二次gate，不支持新的ζ/L/Catalan无理性或线性无关性定理。最终来源receipt另存；最终此review只读。
