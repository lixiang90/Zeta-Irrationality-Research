# 第230轮 q2：完整有理尾残差、卷积去单位与实际栈接口

2026-10-08，B。全尺度纸面推导，数学程序0。以下得到完整模p残差与准确的rank归约，**未证明无界尺度的完整栈满秩**；不能由第229轮ambient E的实/Q满秩替代本问题。

## 1. 同一对象、全部有限头和素数范围

固定 d≥1、m=d+1、L=3d+1。全部源行 r=0,…,2m−1，逆序偶列 s=0,…,d。记

c_n=binom(2n,n)/4^n，h_n=H_{2n}−H_n，
A_{s,r}=c_{r+s}，B_{s,r}=4c_{r+s}h_{r+s}。

原实际矩为

N_{r,s}=M₂(2(d+r),2(d−s))
       =a_{r,s}+ΘA_{s,r}+GB_{s,r}，
a_{r,s}=R_{r+s}−Σ_{v=0}^{d−s−1} m_{2(r+s+v)}/(2v+1)²。 (R1)

m_{2n}=2/[(2n+1)c_n]；空和为0。R_l=[z]ℛ_l(z)，其中

(2l+z)ℛ_l=(2l−1+z)ℛ_{l−1}+m_{2l−2}，ℛ₀=0。           (R2)

这正是统一真实kernel的有理部分递推；没有删掉任何finite-head项。cofactor-free完整多项式是

W_d(X)=det[B; XA+aᵀ]。                                   (R3)

取奇素数 L<p≤2L，置

k=(p−1)/2，i₀=k+1，ε=(−1)^k，η=2ε，
h=i₀−d，q=L−k=2m−h。

0<h<2m、1≤q≤k。A、B皆p整：l<p时c_l的估值为0或1，h_l最多一个p分母，故c_lh_l无负估值。所有(2v+1)²在(R1)中为p-unit。若要完整栈可能满秩，必须 q≥m，即 p≤4d+1=2(L−m)+1；否则下文直接给第一残差层的rank defect。

## 2. 每个偶矩的真实简单极点

在 n<k 时m_{2n}为p整。c_k≡ε modp，故 p m_{2k}≡η。由

m_{2(n+1)}/m_{2n}=(2n+2)/(2n+3)

逐项得到对0≤t≤L−1−k：

p m_{2(k+t)}≡η c_t modp。                               (R4)

全部分母2t为p-unit；这保留了完整简单p深度，不用一次数值主项猜测。因l≤L<p，(R2)中的2l也为p-unit，故pℛ_l(z)的每个Taylor系数都p整。l≤k时该residue为0。

令 U_b(z)=pℛ_{i₀+b}(z) modp，U_{−1}=0。对0≤b≤q−1，

(2b+1+z)U_b=(2b+z)U_{b−1}+η c_b。                      (R5)

这里 2b+1<p，故在Fp[[z]]中有唯一解。它有特别简单的**完整卷积解**：

U_b(z)=η Σ_{t=0}^b c_t/[2(b−t)+1+z]。                   (R6)

证明可在形式幂级数中完成。C(x)=Σc_tx^t=(1−x)^(−1/2)，F(x,z)=Σ_{j≥0}x^j/(2j+1+z)。则 2xF′+(1+z)F=(1−x)^(−1)，C′=C/[2(1−x)]。V=CF满足

2x(1−x)V′+[1+z−(2+z)x]V=C，

逐项正是(R5)。这些系数只用b≤q−1<p，均合法p-unit；无需在Fp中使用出现分母p的无限高阶系数。取[z]得

pR_{i₀+b}/η=−Σ_{t=0}^b c_t/[2(b−t)+1]²。

## 3. 有限头精确拼成平方Cauchy卷积

r<h时，R1中的所有极点尚未出现，p a_{r,s}≡0。活跃行写为r=h+u，0≤u<q，置b=u+s−d。R部分仅在b≥0时出现；finite-head residue用指标 t=r+s+v−k，从 max(0,b+1)到u。两段**不重叠且没有缺项**，合并为

p a_{h+u,s}/η
=−Σ_{t=0}^u c_t/[2(d−s−u+t)−1]²。                     (R7)

这同时覆盖b负、零、正以及原列j=0的空头边界；不是只在某个partial cluster成立。

定义 q×q 下三角矩阵 T、q×m矩阵 Z：

T_{u,v}=c_{u−v}（u≥v），否则0，
Z_{u,s}=1/[2(d−s−u)−1]²。

所有显示分母非零modp：其绝对值最多 max(2d−1,2q−1)<p。T的diagonal=1，故det T=1。完整残差矩阵精确为

p a modp = [0_{h×m}; −η T Z]。                         (R8)

T逆也可显式取系数 [x^n](1−x)^(1/2)；仅用n<q<p，全部p整。这里finite-head修正正是把局部生成残差补成完整平方Cauchy矩阵所必需的部分。

## 4. 真正stack的准确rank归约与一个无限接口

把B按同一源列分为B=[B₀|B₁]，列数h和q；令 B̂₁=B₁(Tᵀ)^−1。右乘可逆的 diag(I_h,(Tᵀ)^−1)，再将下块乘单位−η的逆，得到

rank_Fp[B; p aᵀ]
=rank_Fp [[B₀,B̂₁];[0,Zᵀ]]。

若 k_Z=rank Z，取V为ker Zᵀ的任意完整q×(q−k_Z)基，则准确公式是

rank[B; p aᵀ]
=k_Z+rank[B₀, B̂₁V]。                                  (R9)

这是rank映射在下块kernel上的标准分解，作用于**实际finite-tail栈**。没有借ambient E=[A;B]的modp或Q秩。

因此若q<m，rank≤m+q<2m：这是该第一残差层的结构defect，只意味着p^m归一化的residue determinant为0，不意味着W_d本身为0。若q≥m，fullrank恰须 k_Z=m 且 [B₀,B̂₁V]rank m。分母unit或Z的Cauchy形式本身，均未证明这两项。

最具体的边界子族 p=4d+1（取其中prime）有h=q=m，栈块三角。令

H_d=(4c_{r+s}h_{r+s})_{0≤r,s≤d}，
Z_d=(1/[2(d−s−u)−1]²)_{0≤u,s≤d}。

由于detT=1，完整determinant为

det[B; p aᵀ]=(−η)^m det H_d·det Z_d modp。               (R10)

所以这条潜在无限子族的**唯一剩余纸接口**是证明 det H_d det Z_d不被p=4d+1整除，在无界prime子族上成立。它是两个明确有理determinant的条件，不是“找合适参数”的扫描计划。本稿没有支付该nondivisibility；即使所有条目分母为unit，也不能免费认定numerator为unit。

一个手算有限边界说明不是普遍defect：d=1,p=5时，H_d≡[[0,1],[1,4]]、Z_d≡[[1,1],[1,4]]，两det分别4、3，η=2，故(R10)给完整stack det=3 mod5。这个单例不能推出无限结论；本人没有运行程序或扩大probe。

## 5. 如何接目标非零，以及本轮严格缺口

对任意p整有理g，p^mW_d(g) modp恰为det[B; p aᵀ]，因为p gA≡0。因此若(R9)或(R10)在无界(d,p)上证明fullrank，即得到 v_p W_d(g)=−m、W_d(g)≠0；固定g分母只排除有限个prime。

反过来，本稿现有结论不能支付实际W_d(Θ)无界非零，更不能由有限8-case证书或ambient函数独立认定∞。缺口就是(R9)的实际kernel restriction，或(R10)的明确两det nondivisibility。也未证明primitive all-place成本或严格实处收益。

实际输入为本人的229 full-pool rank稿、Root统一生成递推与cofactor-free对象，以及C229完整finite-tail定义。本人 actual FULL读C229最终7638-byte稿/SHAfa2a8fa796693f9bf0b51b9562793d3773a431d3bbb68f5cbe7f9d8fa0d63c1e，只据其定义开展独立纸推；不把它作为primitive lower或目标非零证明。数学程序0，无扫描、CAS、旧manifest审计；本轮未复跑Root唯一producer。新稿保存后本人 actual FULL复读并登记bytes/SHA。
