# beta(4) 实际 Hermite 投影的素数尺度非零门槛

日期：2026-10-07。本稿在原单周期积分矩阵上证明精确的局部投影整性、分层余数与单尺度非零证书。它没有证明无限尺度的实际行列式非零，也没有证明 beta(4) 无理。正面结论是一个已完全支付原投影的有限域门槛；奇数维及 p=13 的失败说明该门槛不能被免费当作一般单位结论。

## 1 原对象及特殊化范围

实际全文回读的输入是 `research/cdt_beta_single_period_confluent_integral_model_20261007.md`，八节 B1–B29，SHA256 `a008a54d3307f151911ad0fc1dfa3587e05fd54eb89bd0172be364d162d64f2c`。固定 r=3、H=3n，沿用

\[
 C_3(u,v)=\sum_{a\ge0}\frac{(-1)^a}{(2a+4u+1)(2a+4v+1)^3},
 \quad J=\{0,\ldots,n-1\},\quad I=\{n,\ldots,3n-1\}.
 \tag{N1}
\]

置 D(z)=prod_(u=0)^(3n−1)(z−u)，Q_I(z)=prod_(u∈I)(z−u)，B_k(z)=prod_(v∈J,v≠k)(z−v)，以及

\[
 N_k(z)=B_k(z)^3\left[Q_I(z)/B_k(z)^2\right]_{k,<3},
 \quad p_{k,u}=N_k(u)/D'(u),\quad F_k=N_k/D.
 \tag{N2}
\]

原完整 regular-part 约束已经证明 p_(k,v)=delta_(k,v) 且 sum_(u≠v)p_(k,u)/(u−v)^ell=0，ell=1,2。故真实投影为

\[
 E=pC_3=q+\beta(4)I_n,\qquad q\in M_n(\mathbb Q).
 \tag{N3}
\]

本稿的有限域证明作用于有理矩阵多项式

\[
 E(T)=q+TI_n\in M_n(\mathbb Q[T]).
 \tag{N4}
\]

对每个素数 p，仅在 T∈Z_p 的特殊化上使用 p-adic 单位结论。如果假设 beta(4)=a/b∈Q，p 不除 b，则真实 E 等于该特殊化，可以使用结论。未知实周期不能未经比较就被视为 Q_p 中的整数。这一范围贯穿全文。

## 2 精确微分表示及正性障碍

令 R_k(t)=sum_u p_(k,u)t^u，delta=t∂_t。直接比较系数有

\[
 R_k(t)=N_k(\delta)\frac{(t-1)^{3n-1}}{(3n-1)!}.
 \tag{N5}
\]

这是原投影行 t=x^4 的精确表示，不含免费缩放。它不保证 Rodrigues 正权重。

例如 n=2，直接展开 N2 得

\[
\begin{aligned}
R_0(t)&=1-\tfrac{196}{3}t^2+990t^3-2736t^4+\tfrac{5800}{3}t^5,\\
R_1(t)&=t-\tfrac{266}{3}t^2+1476t^3-4248t^4+\tfrac{9200}{3}t^5.
\end{aligned}
\tag{N6}
\]

对应的 Wronskian R0 R1′−R1 R0′在 0 为 1，在 1 为 123·2593−207·1562=−4395。因此有序双节点评价行列式并不同号。原 C 的全子式符号不能在此投影后自动继承。

另由 N1、N2 的绝对收敛级数直接得到

\[
 E_{k,v}=-4^{-4}\sum_{a\ge0}
 \frac{(-1)^aF_k(-(2a+1)/4)}{(v+(2a+1)/4)^3}.
 \tag{N7}
\]

F_k(z)=O(1/z)，故该和绝对收敛。交错权重仍然存在，不能把它当正 Stieltjes 配对。以下改从同一原矩阵的确切局部余数入手。

## 3 n=p 时原投影的 p-adic 整性

以下固定素数 p≥13，n=p。把每个 u 写成 u=ap+i，a=0,1,2，0≤i<p。由于 3p<p^2，Legendre 公式与 Wilson 恒等式给

\[
 v_p(D'(u))=2,\qquad
 \frac{D'(ap+i)}{p^2}\equiv(-1)^{a+1}a!(2-a)!\pmod p.
 \tag{N8}
\]

这里并未把 D′当单位：先明确除去它的完整两层。证明中 u! 的剥离单位为 a!(-1)^a i!，(3p−1−u)! 的剥离单位为 (2−a)!(-1)^(2−a)(p−1−i)!；再用 i!(p−1−i)!≡(-1)^(i+1)，及 D′的符号 (-1)^(a+i)，即得 N8。

在 z=k+zeta 附近写

\[
 \frac{Q_I(k+\zeta)}{B_k(k+\zeta)^2}
   =(\zeta-p)(\zeta-2p)U_k(\zeta),
 \quad U_k\in\mathbb Z_p[[\zeta]],\quad U_k\equiv1\pmod p.
 \tag{N9}
\]

B_k(k) 是单位，所以此展开合法。mod p 时 Q_I=(z^p−z)^2，而 B_k=(z^p−z)/(z−k)，删去两个与 k 同余的额外因子后，U_k 恰约化为 1。N9 是全部形式级数的恒等约化，故所有正次数 U 系数都被 p 整除。

令 T_k(zeta) 为 N9 左边次数小于 3 的 Taylor 多项式。其常数、一次、二次系数的估值分别至少 2、1、0，且 T_k≡zeta^2 mod p。

若 u=ap+i∈I、i≠k，则 B_k(u) 恰有一个 p 因子，并且

\[
 B_k(ap+i)/p\equiv-a/(i-k),\qquad
 T_k(ap+i-k)\equiv(i-k)^2\pmod p.
 \tag{N10}
\]

若 i=k，则 B_k(u) 是单位。N9 左边在 zeta=ap 为零，其所有次数至少 3 的系数都被 p 整除。因此 Taylor 余项在该点被 p^4 整除，T_k(ap)∈p^4 Z_p。这个更高层结论需要完整余项，不能只用 T_k≡zeta^2。

结合 N8–N10，得到原投影的精确结论

\[
\boxed{p_{k,u}\in\mathbb Z_p,\qquad
 p_{k,u}\in p\mathbb Z_p\ (u\in I),\qquad
 p_{k,ap+k}\in p^2\mathbb Z_p\ (a=1,2).}
\tag{N11}
\]

进一步，对 i≠k：

\[
\boxed{p_{k,p+i}/p\equiv-1/(i-k),\qquad
 p_{k,2p+i}/p\equiv4/(i-k)\pmod p.}
\tag{N12}
\]

以上作用于未缩放的原 p；没有使用其全素数分母预算代替这里的局部证明，也未将有理投影默认当 unimodular。

## 4 原有理部分的四层与三层

沿用 T_(u,a)=sum_(j=0)^(2u−1)(−1)^j/(2j+1)^a，T_(0,a)=0。对 u≠v，d=4(u−v)，原有理部分为

\[
 A_3(u,v)=-T_{v,3}/d+T_{v,2}/d^2
             +(T_{u,1}-T_{v,1})/d^3,
 \quad A_3(v,v)=-T_{v,4},\quad q=pA_3.
 \tag{N13}
\]

所涉奇分母至多 12p−5<p^2：它出现在 u=3p−1 的 T_(u,1) 中，最大奇数为 4u−1。u−v 的绝对值小于 3p<p^2。故每个非零差的 p 估值至多一，且

\[
 v_p(A_3(u,v))\ge-4\qquad(0\le u<3p,\ 0\le v<p).
 \tag{N14}
\]

这包含 d 有 p 因子的情况：三项分别最多损失 3+1、2+2、1+3 层；对角最多四层。N11 给全部额外行的贡献估值至少 −3。

记 epsilon=(−1)^((p−1)/2)，m=ceil(p/4)，低索引 L={0,…,m−1}，高索引 H0={m,…,p−1}。对所有 T∈Z_p，因低节点投影精确为 I，有

\[
 p^4 E(T)_{k,v}\equiv
 -\epsilon\delta_{k,v}
 \left({\bf1}_{4k>p}-\frac1{81}{\bf1}_{4k>3p}\right)\pmod p.
 \tag{N15}
\]

低节点非对角 d 是单位，最多损失三层，故 p^4 后消失；额外行亦消失。对角只需统计 T_(k,4) 中的奇倍数 p、3p，它们的符号分别 epsilon、−epsilon。H0 上的对角单位是 −epsilon 或 −epsilon·80/81；p≥13 时均非零。

对低列 v∈L，4v−1<p，因此 T_(v,a) 没有 p 分母。低节点与此列的非对角项最多损失一层，对角项为整数；额外行由 N11、N14 最多损失三层。故

\[
 p^3E(T)_{k,v}\in\mathbb Z_p
 \quad(0\le k<p,\ v\in L,\ T\in\mathbb Z_p).
 \tag{N16}
\]

这支付了后来全部列缩放的整性；没有先假设某个 Schur 补已整。

## 5 低块的确切反对称余数

取 k,v∈L。若 k=v，则原低对角无 p 分母；与 v 同余的两条额外行，由 N11 至少有 p^2 因子，故其贡献估值至少 −2。其余额外行因 d 是单位也至少 −2。所以 p^3 E(T)_(v,v)≡0。

若 k≠v，非共余额外行 d 是单位，N11、N13 使贡献至少 −2；仅 u=v+p、v+2p 可以留下三层余数。N13 的前两项在这两点分别最多损失一、二层，不影响 p^4 A 的余数。最后一项精确给

\[
 p^4A_3(v+p,v)\equiv\frac\epsilon{64}(1-1/3)=\frac\epsilon{96},
\quad
 p^4A_3(v+2p,v)\equiv\frac\epsilon{512}(1-1/3+1/5-1/7)
                 =\frac{19\epsilon}{13440}.
 \tag{N17}
\]

这两个区间的倍数列表完整：因为 4v<p，分别恰有 p、3p 与 p、3p、5p、7p。结合 N12，得到

\[
 \boxed{p^3E(T)_{k,v}\equiv S_p(k,v):=
 \begin{cases}
 -\epsilon/[210(v-k)],&k\ne v,\\
 0,&k=v,
 \end{cases}\qquad k,v\in L.}
 \tag{N18}
\]

常数来自 −1/96+4·19/13440=−1/210。p≥13 使所有显示的小整数分母为单位。N18 是同一原投影的余数，而不是把正 Cauchy 矩阵替换成一个便利矩阵。

## 6 已支付的三角门槛及行列式多项式

按 L、H0 排列索引，只对列作显式缩放：

\[
 \mathcal T_p(T)=E(T)\operatorname{diag}(p^3I_m,p^4I_{p-m})
              \in M_p(\mathbb Z_p),\qquad T\in\mathbb Z_p.
 \tag{N19}
\]

由 N15–N18，完整约化是

\[
 \overline{\mathcal T_p(T)}=
 \begin{pmatrix}S_p&0\\ B_p&D_p\end{pmatrix},
 \quad D_p\text{ 为 N15 给出的单位对角矩阵}.
 \tag{N20}
\]

不需要知道 B_p 的值；右乘块矩阵 [[I,0],[−D_p^(-1)B_p,I]] 的合法单位列消元即可得

\[
\boxed{\operatorname{rank}\overline{\mathcal T_p(T)}
     =p-m+\operatorname{rank}S_p,\qquad
 p^{3m+4(p-m)}\det E(T)\equiv\det S_p\det D_p\pmod p.}
\tag{N21}
\]

后式左边属于 Z_p，且其余数与 T 无关。等价地，p^(3m+4(p−m)) det(q+TI)∈Z_p[T]，所有正次数系数都被 p 整除，常数余数为 det S_p det D_p。

若 S_p 是单位，便对每个 T∈Z_p 有 det E(T)≠0，且其估值精确为 −3m−4(p−m)。因此，在 beta(4)=a/b 的有理性假设且 p 不除 b 时，它确实证明实际 det(pC_3)≠0。若 S_p 非单位，N21 只描述第一层秩缺损，不能断言实际行列式为零。

## 7 失效边界与一个有限正证书

N18 是反对称矩阵。m 为奇数时，char F_p≠2 强制 det S_p=0；这包含 p≡1,3 mod 8。m 为偶数也不自动为单位。定义标准 A_m(k,v)=1/(v−k)，k≠v，A_m(k,k)=0，则 S_p=−epsilon A_m/210。

p=13 时 m=4，其 Pfaffian 精确为

\[
 \operatorname{Pf}(A_4)=1-1/4+1/3=13/12.
 \tag{N22}
\]

因此 mod 13 的秩为 2：行列式为零，但一个非零二阶主子式已经给秩至少二。N21 的完整第一层秩为 9+2=11。这是有限层证书失效，而非实际 E_13 奇异的证明。

相反，p=23 时 m=6。沿第一行展开 Pfaffian，五个四阶 Pfaffian 分别给

\[
 \operatorname{Pf}(A_6)
 =\frac{13}{12}-\frac7{24}+\frac{73}{216}
       -\frac7{48}+\frac{13}{60}
 =\frac{2593}{2160}.
 \tag{N23}
\]

例如中项来自 Pf(A_(1,2,4,5))=1−1/9+1/8=73/72，再乘 A_(0,3)=1/3。全部项是手推的有限恒等式，未运行素数程序。2593≡17、2160≡21 mod 23，210 也为单位，故 S_23 是单位。

由此有完全明确的结论：对于所有 T∈Z_23，p=23 的实际有理矩阵多项式 q+TI_23 均非奇异，行列式估值为 −3·6−4·17=−86。特别地，该行列式多项式的有理根若存在，其既约分母必被 23 整除。beta(4) 若有理且分母不被 23 整除，则原尺度 n=23 的真实积分行列式非零。

这一证书不排除分母被 23 整除的有理目标，也不证明未知 beta(4) 的无条件 E_23 非零。更没有从 n=23 免费传到 n=23^j。经典 Schur Pfaffian 的核 `(x_i−x_j)/(x_i+x_j)` 与这里的 `1/(j−i)` 不同，不能借其乘积公式声称所有素数成功。

## 8 尚缺的无限尺度定理与实际记录

N11、N12、N18、N21 是本轮的新纸面结果；它们把原 p-index determinant 的首层核精确收缩到维数 ceil(p/4) 的斜 Cauchy 矩阵，给出完整高块单位、低块常数和一个有限正证书。它们比只声称形式 monic 多项式更具体，但仍没有完成原目标所需的无限尺度非零定理。

至少还有两种明确的后续门槛：证明无限多个素数 p 的 det S_p 非零，并在假设目标有理时删去其有限分母例外；或从某个固定成功素数严格证明完整 Hermite 投影与原 A_3 的高 p-power Frobenius 传递，包含新出现的 p^2、p^3 分母及更高 Taylor 余项。只测试有限成功素数、只保留首层单位或假设高块仍同形，都不能支付后者。失败素数也可能通过更高层残数恢复非零，N22 不能排除该途径。

此外，全有限处 determinant 预算和同一行列式的 n^2 实数处衰减仍是独立接口。本稿只证明 n=p 时指定素数的更强整性；没有把它当作其它素数已经改费的全局模型，未据单尺度证书推出新的数值线性无关性。

本轮实际全文读原模型八节，以及同轮振荡稿六节，并另存正式独审。浏览过 Hermite 插值、Hermite–Padé 与斜 Cauchy/Pfaffian 的 primary 检索页，但没有将检索未发现定理解释为该定理不存在；上述证明全部自足。不新增 PDF，不继承以前 PDF 页数。未创建、执行、导入或重跑数学 producer，未运行或扩展素数表、guards 或 Lean；旧冻结记录保持不变。N1–N23 已收到 source 的独立全文纸核，修正最大奇分母边界为 12p−5 后通过；root 亦独立全文核读。正式独审另存，作者已在收核后最后全文回读；纸面审查不是形式化验证。
