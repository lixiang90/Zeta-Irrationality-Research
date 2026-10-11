# 第231轮：boundary Hankel 的全尺度反序、Fermat 因子与精确剩余块

2026-10-08，B。数学程序0；不追加素数案例。本稿支付一个完整有限域结构引理，**没有支付无界素数子族上的非整除**。实数域非零、正性或第230轮有限probe均不用于填补此缺口。

## 1. 同一边界对象及一个完整参数恒等式

令 p=4d+1 为素数，d≥1，k=2d=(p−1)/2，m=d+1。在 Fp 中取

c_n=4^(−n)binom(2n,n)，h_n=H_(2n)−H_n，
A₀=(c_(i+j))_(i,j=0)^d，
B₀=(4c_(i+j)h_(i+j))_(i,j=0)^d。

全部 n≤k，故所有显示 harmonic 分母小于p；c_n也是p单位。J为 m×m 反序矩阵。引入完整形式参数

a_n(z)=∏_(l=1)^n (2l−1+z)/(2l+z)，
𝒜(z)=(a_(i+j)(z))_(i,j=0)^d∈Mat_m(Fp[[z]])。             (F1)

全部常数分母为p单位。a_n(0)=c_n，a_n′(0)=c_nh_n，因此 𝒜(0)=A₀、4𝒜′(0)=B₀。对于0≤n≤k，

a_(k−n)(z)/a_k(z)
=∏_(l=1)^n (p+1−2l+z)/(p−2l+z)
=a_n(−z) in Fp[[z]]。

于是全参数身份为

J𝒜(z)J=a_k(z)𝒜(−z)。                                   (F2)

这里既未在Fp中使用含p分母的高阶n，也未把某个有限样本提升成一般式。由于 k 为偶数，c_k=(-1)^k=1，而 a_k′(0)=h_k=−H_k modp，微分(F2)得

JA₀J=A₀，JB₀J=−B₀−4H_kA₀。                             (F3)

直接的系数核验也成立：c_n=(-1)^n binom(k,n)，故c_(k−n)=c_n；又 H_(p−1−2n)=H_(2n)，且
H_(k−n)=H_k+2H_(2n)−H_n modp，
所以 h_(k−n)=−H_k−h_n。

## 2. 背景A₀是单位，反序两个子空间均非退化

精确有理身份为

det A₀=2^(−d(2d+1))。                                   (F4)

自足证明：c_n是概率arcsine measure dt/(π√(t(1−t)))的n阶矩。令 t=(1+cosθ)/2；首一 shifted Chebyshev 多项式在degree j≥1的平方范数为2^(1−4j)，degree0范数1。乘积即(F4)。这是恒等式；其变基仅有2幂分母，所以可合法模p约化。没有从实数正性推有限域非零。

置 a=ceil(m/2)、b=floor(m/2)。用 e_i+e_(d−i)、e_i−e_(d−i)，以及d偶时中央e_(d/2)，给J的±1 eigenspaces取完整基。此变基S₀的det为符号乘2^b，因p奇而为单位。由(F3)，在同一基下

S₀ᵀA₀S₀=diag(A₊,A₋)，
S₀ᵀB₀S₀=[[λA₊,C],[Cᵀ,λA₋]]，λ=−2H_k。                 (F5)

A₊是a阶、A₋是b阶，C是a×b。A₊、A₋全部Fp整且均可逆：两det的乘积等于单位(detS₀)²detA₀，故各自是单位。交叉块C定义于完整原B₀，不是另选的简化moment source。

## 3. 全尺度det与rank归约

定义 b×b 的实际交叉算子

S=A₋^(−1)Cᵀ A₊^(−1)C。

Schur消元给精确公式

det B₀/det A₀
=λ^(a−b)det(λ²I_b−S)。                                  (F6)

证明可先把λ视为形式变量并在λ≠0处消元，再用多项式恒等式取λ=0；A₊、A₋、C在这一步固定。这样没有在H_k=0处非法除以λ。两个变基det的平方在比值中抵消。

同一式还给出全部rank条件：

- λ≠0：rank B₀=m−dim ker(λ²I_b−S)；
- λ=0：rank B₀=2 rank C。                                (F7)

第二项直接由[[0,C],[Cᵀ,0]]的两个独立映射得到。若m奇，则a=b+1，λ=0时rank至多m−1；若m偶，则a=b，λ=0时满秩恰等价于C可逆。这些都是模p的完整对象结论，不只det上界。

结合230的Chebyshev身份 detB₀=(-1)^m2^(−2d²)detT_m，得到更小块的精确表示

det T_m=(-1)^m2^(−d)λ^(a−b)det(λ²I_b−S)。                (F8)

因此“含H_k因子”指(F6)/(F8)这个**modp身份**，不声称有理数域的detT_m随d具有某个固定整除因子。

## 4. Fermat quotient条件及准确量词

定义整数 q_p(2)=(2^(p−1)−1)/p。由

binom(p,j)/p≡(−1)^(j−1)/j modp，1≤j<p，

把2^p−2的二项式展开除以p，得

2q_p(2)≡Σ_(j=1)^(p−1)(−1)^(j−1)/j
=H_(p−1)−H_k=−H_k modp。

故 λ=4q_p(2)。这一步只需完整二项式乘积和j↔p−j配对，没有借用更强的Wolstenholme假设。

若 p≡1 mod8，则d偶、m奇，满秩必要条件是

q_p(2)≠0 modp，
det(16q_p(2)²I_b−S)≠0 modp。                           (F9)

所以若某个该同余类的p满足base-2 Wieferich条件，B₀必退化。**这是条件结构障碍，不是本稿找出的实际素数反例**，更不是所有boundary失败。没有假定无穷多个non-Wieferich素数；即使付了这一必要条件，也仍须支付第二det的单位性。

若 p≡5 mod8，则d奇、m偶，没有λ^(a−b)这个强制因子。该子族保留可能性，但(F6)的实际b阶det仍未证明为单位；q_p(2)=0时也不能直接认定失败或成功，须核C的完整秩。

第230轮boundary residual的另一平方Cauchy块Z_d仍须另付。由(F6)，本稿把其实际满秩接口改写为

λ^(a−b)det(λ²I_b−S) det Z_d ≠0 modp。                    (F10)

目前没有证明(F10)在任何无界素数子族成立，也没有将该boundary条件推广成general-window no-go；后者仍是230完整kernel restriction。

## 5. Primary对象核对及停止规则

定向核对了 Cigler 作者稿的physical PDF1及8–11：其explicit determinant处理H_n(t)=Σ_(j=1)^n t^j/j，不能直接替代本稿c_n(H_(2n)−H_n)。另实际读 Chammam 作者上传文本的(5.1)、(5.2)及Theorem5.1：其harmonic序列是 ξ^n(α+1)Σ_(j=0)^n1/(j+α+1)，未提供本稿所需parameter-derivative Hankel非整除。源和准确读取范围存于本轮literature目录；不冒称全文已读或已匹配新公式。

Jacobi参数moment的product formula即使评估了det𝒜(z)，也不能免费评估 det𝒜′(0)：前者的Taylor系数含各行不同导数阶的混合项，后者只取每行的一阶项。因此不得把“已知Jacobi Hankel determinant”直接代入B₀。

新增进展是完整(F2)、单位背景(F4)、精确(F6)/(F7)以及强制Fermat条件(F9)。它给下一次纸攻一个真实更小块；本轮不再追加prime扫描，也不声称新数值无理性/LI或无界非零。数学程序0；文档下载、文本提取、元数据/hash核验不计数学执行。保存后实际FULL作者复读并登记身份；旧230/main/manifest不改。

