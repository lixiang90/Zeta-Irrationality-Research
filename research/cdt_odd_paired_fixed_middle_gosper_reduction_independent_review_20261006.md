# 固定 middle 的 Gosper 三初始矩归约：独立全文审阅

2026-10-06，toric_chow_completion，NEW。471 个既存输入与全部旧/同行数学 producer 只读；本审阅不执行、import或重跑任何 producer，不改作者数学文件。

## V1. 实际读域和指纹

实际全文读作者稿 [fixed middle Gosper](cdt_odd_paired_fixed_middle_gosper_reduction_20261006.md)，11 sections、全部 Z1–Z23，终稿候选 SHA f988d6629b01188f175fabcfa0e87fc58d51d1bf482fda8196d1fd67f2bad4c7；§8已包含本轮 root 单一 bordered gate。实际完整静态读同stem_verify.py，SHA4b6dce00c79c0d26d89a418af05966d8f8a7ada32b00ce636c9de20b6576b012；实际完整读JSON全部metadata及3case的每个字段，SHA05907586c7113e74a9e47960de7561f0eb2964a5d56973cb51fd4e333e348b28。

实际全文读 NEW root [single bordered gate](cdt_odd_paired_single_bordered_nonzero_gate_20261006.md)，B1–B8/全部B1–B11，SHAa60d8116c88581028669d9a91aaaf1b848761fcfc4a37b089ca6e5b490b590f8。只核作者§8接入所需的knownunit·detM5和退化strong-block范围；不冒记root producer/JSON或root primary pages为本人已读。

作者来源receipt当前 f988 mathematical pins 已实际全文read；未读到的未来最终状态不倒写本review。不把有限75moments证明提升为all-scale，也不将作者14primary读页冒记为本人读页。

## V2. 真 Wilson 比值与临界 unit triangular 算子

对 head y=k，y^p−y=A_head(y)S_y(y) 且其 derivative为−1，A_head′(k)=(-1)^{a-k}(a-k)!(a+k)!；故 S_y(k)=(-1)^{r+k+1}/[(a-k)!(a+k)!]，独立核 Z3 的sign及factorials。相邻比值正是 (k−a)h_(k+1)=(k+a+1)h_k；没有更换真实 fixed parameters、halfjet 或 middle。

三算子对 g(1−y)=g(y) 的反射逐项使输出even；highest系数分别为 n+2a+2、n+10a+10、n−6a。D1临界最大系数18r−2<p。D5用9(n+10a+10)≡9n+65；在r≥2的0≤n≤4r−8，首次可能根 n=4r−7，超出cutoff。D−3可能根12r−1也超出输入12r−6。每一步只除明确unit，dimension计数给原 critical spaces 的unique decompositions：C无seed、G两个seed、H一个seed。r1的G退化成constantseed范围已单独处理。

这不依赖 unknown G0/H0 norms、中间profiles perfect或critical determinant可逆；也没有把characteristic-zero Gosper gcd定理免费移到modp。

## V3. 两个真实 cutoff 的端点和三个具体种子

Z9内部 telescoping的shift因子及反射符号实际逐项核验。full上端k=a在 h_(a+1) undefined时直接用最后node算子，给2(2a+1)^j h_a^j g(a+1)，保留first denominator pole的flux；middle上端r−1给2(a+r)^j h_(r−1)^j g(r)。负三次幂full边界为0，但middle是−2(a−r+1)^3h_(r−1)^−3g(r)，不能删除。

Wilson端点 w0h_a=−(10r)!、w0h_(r−1)=(4r+1)!(6r−1)!，给 Z15 的两个负号，Z16 的full负/middle正，Z17 的负middle项1/[(4r)!(6r−1)!]^3；全部factorials是units。由unique reductions，每个cross moment完全显式，所有G/H高阶矩分别只需实际 A0,A1 和 B0。三个scalars固定为原目标的指定 sums，不是generic参数。

## V4. Dixon全和、真实中段与三scalar determinant

Good constant-term自证实际核验：Lagrange inverse-product identity给三参数Dixon recurrence；零参数边界是Vandermonde；其唯一归纳解为multinomial。a=b=c时Laurent product的sign和x,y powers给 Σ_(k=−a)^a(-1)^k binom(2a,a+k)^3=(3a)!/(a!)^3。于是Z18 full cubic sum确为factorialunit，15r<p确保所有分母合法。

Z19的真实incomplete middle仍保留，因此full cubicunit不推出B0unit。Z20实际第五幂种子也没有由算子可逆推出非零。Z21/Z22矩阵确在原profile(r,3r)上给 detM5=P_(r,p)(A0,A1,B0)，totaldegree≤4r、A/B combineddegree≤r、Cdegree≤3r；没有声称任意generic值或actualspecialization非零。p37的A0=0不破坏归约。

独核root gate：两次仅使用known-unit ambient/hyperbolic Schur的det比例，m偶数的sign以及6^mκ^m因子正确。p^5矩阵dimension4m、weakq=3m/2给原p^(17m) normalization。故M5unit足以给whole-X非零leading reduction，G0unit已不是额外门槛。M5unit本身仍未证无穷；higher-layerν_max≤2替代充分条件也没有actual证明。作者§8没有将这个normalizedleadinggate冒称所有actual rational nonzero的必要条件。

## V5. primary 实际读取的准确范围

本人本轮只读同行已归档的两份原件，无重复下载。

* Gosper1978，[Rutgers原件](https://sites.math.rutgers.edu/~zeilberg/akherim/gosper1978.pdf)，本地literature/cdt_paired_fixed_middle_gosper_sources_20261006/gosper1978_indefinite_hypergeometric_summation.pdf，SHA64a8a36e946f58a4bd4aab16ee9276e9ea48b3d21e8d25e2111207f7019885e6。实际PDF1–3全文：Eq8、shifted-gcd假设、degree resonance、division-by-zero caveat。
* Adolphson–Sperber2012，[arXiv1209.2448v1](https://arxiv.org/pdf/1209.2448v1)，本地literature/cdt_paired_fixed_middle_gosper_sources_20261006/adolphson_sperber2012_hasse_A_hypergeometric_arxiv1209_2448v1.pdf，SHA0389d5ef9f58475327dd0c7b155fa2c12c269c7527f5725ea701fa350dc272dc。实际PDF1–3及14–17，共7页：Legendre Hasse fixed specialization、Eq1.2/1.3、normalized/unnormalized系统、digit decomposition、真实exponential-sum hypotheses与Th6.6。

共10distinct primary pages，不称第二PDF22页全文。首次只读extract在完成Gosper三页后于AdolphsonPDF1遇GBK输出编码错误，随后UTF8 read-onlyextract实际完整读上述七页；这不是数学producer的失败或rerun。未渲染PDF图，不声称视觉版面核验；这里依赖实际完整数学文本及手核公式。

Th6.6给指定family的Hasse表达，而nonzero polynomial与固定specialization unit是不同条件。Legendre λ=−1在p≡3mod4成对相消；只是逻辑例，不是actualM5反例。作者未把Z19/Z20/M5冒认为已完成fixed-family Hasse comparison。middle mask非零且被实际outside-node polynomial整除，degree≥4r+1的scope也正确。

## V6. 源码、有限输出与独审结论

只读完整源码与全部JSON；其polyoperators、symmetric-basis reduction、unit leading及endpoint符号与论文匹配。r1/2/4三case对应9+21+45=75 criticalmoments，不扩prime表。源没有assert criticaldeterminant非零；fullDixonunit只对应full和。成功源/JSON冻结，不执行/import/rerun。

按以上实际读域，全文数学和声明范围**通过**。本轮实证是原λ2全部criticalmoments的三个指定种子归约以及无G0unit的global leadinggate对接。仍缺真实三scalar values处的防相消、无穷M5units或actualhigher-depth替代、无限rational-targetnonzero与strictmargin。没有新增ζ/L/Catalan特殊值定理或Lean执行。

## V7. 元数据的一向冻结规则

本NEW审阅不改变作者MD/PY/JSON/receipt。按root要求，本review现在以V1–V7实际已读范围完整自读后冻结；不等待同行未来finalreceipt，不再补V8。此后如果实际读取未来finalreceipt，由独立final来源收据或root主报告另登记，root分别pin两个final文件，不倒写本review冒称已经读到未来状态。这避免互相等待或修改已冻结来源。
