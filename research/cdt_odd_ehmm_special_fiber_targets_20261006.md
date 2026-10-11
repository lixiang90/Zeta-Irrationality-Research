# EHMM 的真实特殊纤维投影与 Γ 因子的消去

日期：2026-10-06。NEW 原件核查与严格推论。本文不是新的 L 值无理性证明；不执行旧/同行数学 producer。

使用 [Allen–Grove–Long–Tu 2025出版论文](https://link.springer.com/article/10.1007/s40687-025-00566-y) Proposition1.5 的真实复周期公式。固定 y(x)={}_4F_3((1/2)^4;1^3;x)、θ=x∂ₓ，E=f32.2.a.a，g=f32.3.c.a，ω=L(E,1)。准确已证输入为
\[
y(-1)=\frac{32}{\pi^2}\omega\,|\operatorname{Im}L(g,1)|,
\qquad
[(1+4\theta)y](-1)=\frac2{\pi\omega}\operatorname{Re}L(g,1),
\quad
\omega=\frac{\Gamma(1/4)^2}{8\sqrt{2\pi}}.
\tag{E1}
\]
第二公式的 very-well-poised 比值 (5/4)ₙ/(1/4)ₙ=4n+1，故恰为同一实际 y 的 derivative projection；x=−1 是方程的 ordinary 点。边界 derivative 的 alternating series可用 Abel 极限，与该 holomorphic branch 一致。第一公式含真实绝对值，未自行更改 L 值的符号规范。

两式直接相乘，CM Γ 因子完全消去，得到新可用的实际目标投影
\[
\boxed{\frac{\operatorname{Re}L(g,1)\,|\operatorname{Im}L(g,1)|}{\pi^3}
=\frac{y(-1)[(1+4\theta)y](-1)}{64}.}
\tag{E2}
\]
此等式是原文公式的直接推论，不认领其文献首创。它扩大了可研究目标：可以研究一个 weight3 非 CM 模形式的两份真实临界周期的乘积，而不必一直指定 ζ(7)。

要应用函数方法仍须使用完整实际源 G(x)=y(x)(1+4θ)y(x)。它位于真实四维 P₄ 模的 Sym² 中；冻结的 connected Sp₄ 输入给 Sym²标准模绝对不可约、维数10。formal Sym² 到实际二次函数空间的微分映射核是稳定子模；非零 y² 的值在0为1，故此映射非零且因不可约而单射。G(0)=1，又使其生成整个 Sym²。因此 G 的实际最小 rational differential rank是10；若另含常数行则为11（该非平凡不可约模无常数子模）。Γ 因子从端点消去没有把全函数降为rank2，也没有给免费 integral background。

原件 Table1 明确 E 有 Q(i) 的 CM，而 g 标为 non-CM。不能将 CM 椭圆周期的已知超越性自动转成 g 的两个周期或 E2 的乘积超越性。Theorem1.4及Corollary4.7 的 tensor factorization是 x=−1 的 Galois特殊纤维结论，和全参数 connected Sp₄ 不矛盾。Theorem1.3 是 p≡1(modM) 上的 p项 truncation endpoint congruence；它本身不控制 CDT 原 polynomial-source 整评价的全部 n<N_D 和 graded rows。

对 E2 的新目标，native x 中 y 的第 n 系数 binom(2n,n)^4/256^n 保留真实2-adic分母；转到 x=256z 的整数系数也须同步转换 source、grade 与 arch 解析容量。联合源的全prefix mixed costs、conifold 周期抵消及所有地方 comparison尚未完成。单个 ordinary endpoint有很漂亮的动机分解，仍不足以填掉其它 punctures 或产生 CDT 矛盾。

研究策略因而更具体：将特殊纤维的代数 involution/cycle projection与变参数的 integral Taylor lattice比较，寻找能同时消去Γ规范并给 whole-prefix 信用的源；E2提供明确的目标而不是只引用“动机统一性”。目前没有完成该比较。已归档36页原件，根实际读取 PDF2–6、18–21和相应publisher定理；未声称全文通读。[版本、SHA及阅读清单](../literature/manifest_cdt_odd_ehmm_special_fiber_20261006.json)保留此准确范围。
