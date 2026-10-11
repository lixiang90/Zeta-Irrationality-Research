# 第233轮补充：新的有理系数标量目标与∞拉回

2026-10-08，C。应Root指定，只核精确规范化、canonical叶与新Taylor分母；数学程序0，新检索/primary0。不修改已冻canonical∞稿。本文的新对象不是V∈Q或T∈Q的免费换单位，也不证明任何数值无理性。

## 1. 更换算术目标，得到Q系数芽

沿实际周期身份，κ=(10/3)V=(5√3/2)L(2,χ₋₃)，且前稿完整核出

`T=κ−(π/3)log3`，`δ_∞=−π/(3√3)`，
`K=κC+√3log3·Α+√3Ρ`。

定义新的标量目标及family

`t=T/√3=(5/2)L(2,χ₋₃)−πlog3/(3√3)`，
`H_g(z)=Ρ(z)+gC(z)`，`C(z)=(1−z)^(-1/2)`。               (N1)

g∈Q时，native H_g∈Q[[z]]，而非只在Q(√3)中。这是**新假设t=g∈Q**；它既不等价于T∈Q，也不等价于V∈Q。不再需要同一源的第二个系数嵌入；这不反驳前稿对T∈Q的负嵌入branch诊断。

沿native 0到负实轴∞的canonical叶，前稿自含收敛展开给

`M_∞(z)=Α(z)−δ_∞C(z)`
`=Σ_{n≥0}(-1)^n3^n/(2n+1)(1−z)^(-n−1)`，

在|1−z|>3收敛；实际Stieltjes K在|z|>4有收敛整数1/z展开。故

`H_g(z)=K(z)/√3−log3·M_∞(z)+(g−t)C(z)`。                 (N2)

g=t时canonical∞处analytic且值0；g≠t仍有非零平方根。没有把径向主项当全部Puiseux展开。

## 2. Möbius拉回的精确坐标和局部量词

令

`Z(y)=4y/(4y−3)`，`Z′(0)=−4/3`，`Z⁻¹(z)=3z/[4(z−1)]`，
`F_g(y)=H_g(Z(y))`。                                    (N3)

Z把y=0送z=0、y=3/4送z=∞、y=1送z=4、y=∞送z=1。y从0沿[0,3/4)时，z沿负实轴从0到−∞，精确符合(N2)的canonical叶。native square root满足

`C(Z(y))=√(1−4y/3)`。

在v=y−3/4附近，1/Z(y)=v/(3/4+v)为简单零，所以(N2)的两个整数Laurent部分拉回为analytic O(v)。因此本叶有完整局部身份

`F_g(y)=analytic O(v)+(g−t)√(1−4y/3)`。                  (N4)

在g=t处F_t填y=3/4且值0；g≠t处非meromorphic。平方根两条局部sheet由(N4)确切控制；没有支付从别的全局路径到达的叶，也没有证明任意共同图的所有3/4前像都在被填叶上。

Z有pole，本身不是CDT要求的holomorphic φ:D→C。可用的是**新拉回源F_g**，然后另找holomorphic到y平面的φ；不是把原H_g的图免费允许到z=∞。其它有限branch、原z=1对应的新∞、足够Q(y)函数秩、全源共同图及严格CDT margin均未核。

## 3. 变换后的全Taylor安全分母，单独支付

记g=a_g/b_g为约分有理数，h_l=ρ_l+g c_l。由

`Z(y)=−(4/3)y/(1−(4/3)y)`，

F_g(y)=Σa_ny^n的全部系数恰为

`a_0=g`，
`a_n=(4/3)^n Σ_{l=1}^n(-1)^l binom(n−1,l−1)(ρ_l+g c_l)`，n≥1。 (N5)

这是有限组合，包含完整head；没有逐步把递推分母相乘。实际FULL读取232 Fourier公式给

`c_l=4^(-l)binom(2l,l)`，
`ρ_l=−2·4^(-l)Σ_{j=1}^l(-1)^j binom(2l,l−j) v_j/j`，
`v_j=Σ_{b=0}^{j−1}(-1)^(j−1−b)binom(j+b,j−1−b)3^b/(2b+1)`。

令D_n=lcm(1,…,n)。v_j的所有分母≤2j−1，外层j≤l，因此对l≥1，

`4^l D_(2l)^2 ρ_l∈Z`，`4^l c_l∈Z`。

对n≤N，(N5)中的4^n消去每项的4^l，所有奇素数及其全部幂都由D_(2N)^2清。于是

`b_g·3^N D_(2N)^2` 清F_g的完整prefix 0,…,N。              (N6)

特别是此安全表中的固定3线性指数3^N不能免费归入固定有限LCM数组的v₃=O(log N)。未证明它在最简分母中必存在；相消须另核。这是安全LCD上界，不是实际最小LCD或CDT τ。

如另以y=3u定义新源F_g(3u)=H_g(4u/(4u−1))，则其第n项为3^na_n，同一证明给

`b_g D_(2N)^2` 清完整prefix；mark变为u=1/4，Z_u′(0)=−4。   (N7)

这只是精确坐标与费用transport，同时改变位置/derivative/能量。不能只取去掉3^N这一边而沿用原图预算。没有在本文计算margin或宣称已付holonomicity/rank。

## 4. 已知独立组的逻辑限度与准入范围

Root指出CDT另有已知S=3L−πlog3/√3的独立结论；这里只核

`t=S/3+(3/2)L`。

分别含S及含L的两个Q独立组不自动决定该组合。例如在抽象Q空间令1,a,b,u独立，取L=u、S=3−(9/2)u；两组各自仍独立，却有S/3+(3/2)L=1。此例只否定形式蕴含，不给实际CDT常数赋值。本文未实际重读2.11.17原段，也不借Root的阅读登记本人FULL，更不宣称t已知/未知的全球状态。

新候选已付的是exact t、Q系数family、指定canonical叶的条件填点、精确拉回和完整安全Taylor分母。尚缺真实目标新颖性范围、足够源rank、所有transported叶/共同holomorphic图及完整算术—能量严格比较；不把辅助填点重定义为ζ/L目标成功。

实际输入为此前已FULL读取B23212275 B / 8ea824753c808f6a8477cdae536cd6d22dcad1bfc98819bbc0de51d075447227，以及本人已实际FULL保存作者读取的canonical∞稿3947 B / c53b8ccc4f4c4520e45684c8ee76d55ba773bf7e73345314e60e8b6dd5ea68fb。Root关于2.11.17是消息范围，不是新增本人primary阅读。数学程序0、新primary0、未扫描/运行旧producer或archive；只保存此NEW233补充并实际FULL作者复读。
