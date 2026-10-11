# D12：严格定周期给完整未知稳定子的conjugate separation

日期：2026-10-06。新的短纯Markdown全尺度证明，无producer、无word/参数/prime扫描。所有旧冻结稿保持不变。

使用[实际signed cocycle](cdt_odd_level12_generator_cocycle_20261006.md)。G*=Γ⋊〈M〉、Γ=PSLΓ1(12)离散torsion-free、εΓ=+1、εΓM=−1；R_g为正det normalized weight−2 slash，c(gh)=R_hc(g)+ε_gc(h)，K=c⁻¹(0)是完整未知稳定子。

## 1. 完整K的定理

若实际quadratic c(g)/(iπ³)严格正定或负定，则

\[
 \boxed{K\cap gKg^{-1}=\{1\}.}
 \tag{F1}
\]

本结论把先前[H0 conjugate证明](cdt_odd_level12_stabilizer_timelike_conjugates_20261006.md)中h∈H0的限制解除。旧证明的原点固定条件仅使用c(h)=0，而不使用H0的生成元或presentation，所以可以严格作用于整个K。

## 2. 右作用与原点固定条件

对h∈K，由inverse cocycle c(g⁻¹)=−ε_gR_g⁻¹c(g)，准确得到

\[
 c(ghg^{-1})=R_g^{-1}\{R_hc(g)-\epsilon_hc(g)\}.
 \tag{F2}
\]

因此ghg⁻¹也在K，等价于

\[
 R_hb=\epsilon_hb,\qquad b=c(g)/(i\pi^3).
 \tag{F3}
\]

该条件是实际三维quadratic的固定条件，不能换成scalar Dedekind-sum homomorphism，也不能只用g的abstract group matrix判断。

若h∈ΓM，则ε_h=−1。正det normalized slash保持正定锥和负定锥各自，所以R_hb=−b不可能。

若h∈Γ，则ε_h=+1，R_hb=b。一个严格定real quadratic的unique upper-half-plane root被h固定；于是h是elliptic或identity。Γ离散使elliptic有限order，torsion-free又排除非identity。故h=1。用(F2)证明(F1)。等价地，SL2(R)中固定严格定quadratic的群是compact SO(2)，其离散torsion-free subgroup为trivial。

## 3. 实际整族与严格范围

[冻结strict-cone证明](cdt_odd_level12_stabilizer_structure_20261006.md)(S18)给的任意长度mixed元素g，只要其真实period严格定型，都满足(F1)。[signed-power引理](cdt_odd_level12_stabilizer_signed_powers_20261006.md)又保证其全部nonidentity powers不是zero。这个conjugate separation作用于未知K，而不仅已知H0。

特别两个固定抛物x4、x5的所有nonzero power周期由全整数discriminant严格负，故(F1)已经统一推出K∩xjⁿKxj⁻ⁿ={1}。[新的self-pair稿](cdt_odd_level12_stabilizer_parabolic_malnormal_20261006.md)另给不同幂doublecosets的完整区分，而[不同尖点稿](cdt_odd_level12_stabilizer_mixed_cusp_pair_20261006.md)另排x4/x5两种幂之间的mixed cancellation；这些更强doublecoset结论没有仅从(F1)推出。

对C≠0的合法joint模型，K_joint⊆K_L；因此若用同一个纯L严格定周期g，K_joint∩gK_jointg⁻¹也只有identity。这里无需删掉joint cocycle的任一carrier。

不把(F1)外推到indefinite、null或zero quadratic；不分类完整K，不证明K与〈g〉的自由积嵌入，不给任何新合法leaf、Taylor Smith信用或数值无理性定理。

## 4. 实际审阅状态

root已实际阅读全文§§1–4，独立核对(F2)right cocycle、完整K固定条件、odd cone保向、even离散torsionfree、joint子群及全部范围，通过。按此actual全文范围冻结本稿。没有producer，不需要有限实例作为全群证明。
