# 第246轮 χ−7 Eisenstein 双覆盖源独立审计

2026-10-10，C。结论：**PASS，无待修正数学项**。独立实际 FULL 读取最终主稿全部8节、E1–E13：

- [被审主稿](dirichlet_chi7_eisenstein_source_round246_20261010.md)：10448 bytes；
- SHA256：`544f1df14fc0bbac19756891f000a54961024fe2588b899b731c583ede531679`。

本收据只认证下面的纸面链与明示标准输入；不代替全部上游文献证明、有限计算或数值无理性证明。

## 已核核心

1. **实际坐标和全函数身份。** eta 模单位的两个 cusp 阶数给出 u 的唯一 simple pole，足以使 u 为 degree-one 坐标。Fχ/f 在 H 无 pole、∞有限、另一 cusp 至多 simple pole，先付 degree bound 后再用两个系数确定 Fχ=f(1+8u)，不是有限头拟合。该商不 Fricke invariant，不能偷换为原 t 上的 rational forcing。θt=aδ 的两项展开确给 E6，包括一阶 δ 项精确相消。

2. **整模型和数值响应。** q(u) 的整数逆级数及 e_n∈Z 支付全 prefix d_N²，不仅有限头。E8 的绝对重排及 ρ(am) 的 m⁻² 支配成立，响应为 −Y/2。最终稿直接对 ℰχ 取有限部分，未依赖未证的 A 沿路径无零或正 theta 断言。

3. **E9 的实际非恢复。** 两个 P 根的指数为 1/3、2/3，0、∞为0、0；regular-singular hyperexponential 的 residue 总和排除 order-one 因子。rational particular 的有限 pole 均被排除，polynomial 的最高项 2401d² 与 RHS 的 degree 不匹配。若 A 属于 S_g 的 derivative closure，则简单 rank-two 子模与 K 稳定直和；投影与 K[∂u] 交换，投影 LS_g=r 才推出 Ly=r。这里没有错误地令 L 杀死 V 的所有元素。由此对每个固定 g∈C 得实际 rank3 和不恢复 A，而非 generic-g 结论。

4. **完整 log² 与固定过滤。** v=1/u 的 RHS constant 为392、indicial coefficient 为2401，故 c=4/49。E11 的三个解析递推右端均有零常数项，n≥1 的 pivot 为2401n²，解析系数的几何 majorant 支付收敛。齐次解只改变低层 log；常数补偿与有限 ramification 均不消最高项。固定 Q 的最高 log² 系数为 cQv₀；不可约性与 Ore 右除给 Q=T L，输出仅为 rational forcing 的像。限定为固定 rational differential filtering，不能外推为所有有限图、多源或增长投影的 no-go。

5. **新增 E13 两源族。** h/f=a+bu 给
\[
B_h=(a-b/8)B_f+(b/8)B_\chi.
\]
B_f 的 v 方程 RHS constant 为0，故至多一级 log；最高 log² 系数确为 b/98。为避免 cusp 参数与系数 a 混淆，写 ε↓0，则完整有限部分为
\[
\lim_{\varepsilon\downarrow0}
\left(\mathcal E_h(e^{-\varepsilon})
-\frac b8\frac{L(3,\chi)}{\varepsilon}\right)
=(a-b/8)\kappa-bY/16.
\]
这同时核对了减项及符号。常数线性混合消最高 log² 即删除有效 Eisenstein 方向；无需先假设 κ 与 Y 数值独立。该结论仅限所述 weight、character、native 条件下的全纯 family。

## 依赖与未付接口

Stein、Darmon 作者 draft、Magma 的所用完整选段均实际读取；Yang 只亲自读取 PDF5–6、15–16，并复用此前已读的同源校准稿，未把 Root 的 PDF5–11 读域记成本人 FULL。标准模性和 eta 判据以原文 statement 为输入，未认证 Miyake 全书或整个原著。确切范围见 [本次独立 scope](../literature/forcing_recovery_sources_round246_20261010/dual_dirichlet_review_scope.md)。

已付的是明确 Y 有限部分、全 prefix 整模型、actual rank/nonrecovery 与固定过滤限制。全周期投影、目标敏感 whole-leaf 补点、无限非零、合法大图及 strict holonomy budget 仍未付。没有新 ζ/L 数值定理，主 goal 仍 active。

数学程序/CAS/扫描/Lean：0；新 GET：0；外部 Git mutation：0。未修改被审稿、冻结旧稿、主进展、政策或 manifest。收据保存后实际 FULL 自读并重新检查被审身份。

