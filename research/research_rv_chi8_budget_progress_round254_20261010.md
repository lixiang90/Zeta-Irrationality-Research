# 第254轮进展：精确约分与完整误差预算，结束当前默认RV实现窗口

2026-10-10。前一目标轮253为progress；本轮为可核数学及方向决策的progress。**没有新的ζ/L数值无理性或线性无关性定理，goal active。** 最近正式全局复盘252，完成本轮后计数2，下一定期正式256；本轮不reset。连续两轮核心停滞提前复盘、最迟八轮保持。

## 1. 完成同一具体实现的检验

固定n≥2、r=0,…,4、tuple(10n+r,8n,8n,5n,10n)，v=adj(首四列R=Q/Λ模Φ8)e0、v4=0。没有换参数、投影方向或用第五列寻找更小误差。所检验的目标仍Y=L(2,χ−8)；253的全n秩4与完整原I0−log(z)I1投影作为已付输入。

本轮把首个算术缺口具体化。令B_n是(8n)!(5n)!/[(6n)!(7n)!]的既约分子，则

\[
B_n\ge(4/3)^n,\quad B_n\mid d_{8n},\qquad
\beta_n=2^{\lfloor9n/4\rfloor}B_n^3\mid v_r,A_n,c_n.
\]

这是真正作用于完整整数A/c的指数级共同约分：公共cyclotomic乘法的adjugate向量content自含norm计算，B的连续乘积/既约factorial身份自含纸证。没有把Q额外一份B免费推给完整头。

令U′=Σ(v_r/β_n)R_r、δ′=det(M_R)/β_n，完整有理Gauss头为p_n/q_n既约，则q_n|Λ*_n=d_(13n+3)d_(12n+3)。令d_n=gcd(|p_n|,|δ′|)，精确primitive pair为

\[
g_n=\beta_n(\Lambda_n/q_n)d_n,\qquad
(a_n,b_n)=(p_n/d_n,q_n\delta'/d_n),
\]
\[
\ell_n=a_n-b_nY=-\frac{q_n}{d_n}\int_0^1
(-\log t)U'(t)\frac{1+t^2}{1+t^4}\,dt.
\tag{254E}
\]

原Λ是人为公共标度，最终真实成本是q_n/d_n与同一U′，不能把两者分开各自领取最优值。这不是q/d的全n闭式解；局部共同内容仍不能代替实际primitive费用。

## 2. 更强正交与完整signed误差

双Rodrigues与完整端点证明得到

\[
\int_0^1t^jU'(t)dt=0\quad(-n\le j<4n),\qquad
\int_0^1(-\log t)t^jU'(t)dt=0\quad(0\le j<2n).
\]

负j仍可积；它们等价于正权t^(−n)的5n个多项式矩消失。因此同一U′至少有5n个内部变号，直接常号证明不成立；这不证明实际误差为零。将完整误差转移13n次导数及奇偶精确t^(2n)尾核，仍须控制signed配对。

完整Mellin函数更被压成

\[
\mathcal M_n(s)=\frac{G_n(s)H_n(s)}{D_n(s)},\quad
G_n=\prod_{j=-n}^{4n-1}(s-j)\prod_{j=0}^{2n-1}(s-j),\quad
D_n=\prod_{k=3n}^{16n+3}(s+k+1),
\]

其中H_n∈Z[s]非零、degree≤3n+3，actual ℓ=(q/d)Σχ(k+1)M′(k)绝对收敛。H并非可以任意选择的正多项式；非零H不证明该χ配对非零。

## 3. 真正统一的解析界与预算结论

Root从四个固定复极点的Chebyshev几何级数自含给出常数C>0、1<ρ<7，与n无关，使同一(254E)有

\[
|\ell_n|\le C\rho^{-2n}V_n,\qquad
V_n=\frac{q_n}{d_n}\int_0^1(-\log t)|U'(t)|dt.
\]

若实际limsup n^(−1)log V_n<2logρ，则这份证书给趋零；无界非零仍另付。B另给选中error行替换的精确determinant接口与四维受约束Christoffel表达，均未取得所需的净增长差。

把253全部向量/系数安全upper、已付β与Λ*合入后，现有认证upper为24CΛ*E_n⁴β_n^(−1)ρ^(−2n)，E_n=2^(51n+8)。用B|d8n、自含d_N≤4^N证明，该upper自身至少按(2^(615/4)/49)^n增长。因此**当前这份完整证书不能证明趋零**。这绝不是实际误差的lower，也不排除真实约分、强signed cancellation或最优RV办法更好。

本轮没有实际ℓ_n在无界n上非零证书；也没有同一q/d与实范数相乘后的strict衰减。真实约分收益、5n正交与Mellin压缩均是进展，但未改变数值定理准入结论。

## 4. 明确结算与下一方向

**按253的有界检验条件，结束当前fixed adj(R)e0、v4=0实现的默认续轮投入。** 保留原构造及本轮完整模型作资产；以后重新进入须有作用于同一(254E)的实际无界非零与strict预算核心证据，或明确完整新数值出口。不给prime、第五列、参数、其它向量或同源地图自动开续窗，不把局部引理数量当新结果。

下一255只作一次跨架构数值出口比较：把单值Padé primitive误差路线与CDT/Catalan式mixed周期增长行列式路线放到同一表中，逐项对照真实周期目标、完整整数模型、无界非零机制、全有限处成本和全实处能量；选择一个必须补的新定理及停止条件。复用252已经保存的成功机制与失败门槛，必要时检索/读取新的primary证据；不因改名重开Fricke、朴素Gram或截断mixed源。本轮没有指定新的数值目标来冒称已完成这一比较。

宏观评价仍是新数值ζ/L定理；所有odd ζ、Catalan baseline、已知有理参数dilog结论不能替代它。下一定期formal仍256，本轮数学进展不重置计数；若连续两轮核心停滞则提前全局复盘。

## 5. 核验和资源

Root实际FULL读最终primitive9256、signed-error8062、B8522及三scope并逐式纸核；B稿由Root核，B唯一独审Root7789、primitive、signed-error及本报告。Root的LCM/几何级数/upper边界为自含证明；完整原RV Theorem2.1采用已发表输入，本轮实际FULL复读物理4–6文字，不冒称49页或全Lean/全球新颖性。

数学程序、有限头手算/程序/证书、CAS/区间、Lean、prime/parameter/map/word扫描、外Git写、旧producer均0。Root一次web调用3query仅metadata，不采用新命题；团队新增PDF/HTML下载0。唯一review后一次文档归档；253清单和48非policy文件保持，main/policy旧字节前缀保持，报告追加一次。新数学/读域来源保存于254前缀。
