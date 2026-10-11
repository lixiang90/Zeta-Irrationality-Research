# 第226轮 Root 外幂分歧模型独立审核收据

2026-10-08。结论 **PASS（最终版）**。本审核只做文档与独立纸核，数学程序0，未修改目标稿、224/225冻结稿、main或manifest。

## 1. 最终身份与实际FULL范围

实际 FULL 读取目标全部六节及两张完整表：

- `research/pade_exterior_ramification_model_round226_20261008.md`：**9351 bytes**，SHA256 `a981d3fa323ee30fd1408c280614cae10f0ef52797083673cd92cdeddab2ceae`。
- 初版9201 / `7f6880ecb8bb6f9bfcbbad794f0427ac25e23da6a2bf35a9caf240308cf9e38a`曾完整读；其中§5先把0当已填点的压缩文字，经本独审要求补明operator在0的例外。该中间身份不作为最终版本。

作者修订后，本人再次实际 FULL 读取最终9351-byte整稿，未只读差分或借Root作者复读代替。本收据只为该最终身份PASS。

本人226已实际 FULL 读224 actual operator14482 / `32d41b069e688a3aa4e93c44721fe39a6f4ebe1ce646df7fe902bf660d507efd`、225 actual symbol13928 / `ee1d70e843e53090cefc84dd750452e2ee6c954ae79bf674d0ea9f25ffede798`、225 powers14444 / `7752b5bfeb3b2090d913b999600695c5a12ffc1c731dd36649d4d89104b5b255`。C226引理13212 / `2bbe912ac345d5afa5c6a999c1ba05b8b79de83d27b58e0a44921490a3ed1772`是本人的新稿，全部七节R1–R14及18公式保存后FULL作者自读；不冒充自身独审。本收据独立核Root的新二十谱分离及该引理的实际应用。

## 2. 二十个谱值及全部精确区间

独立按3 cubic、2 quadratic、1 rational选择三个根，核类别数量1+1+3+3+6+6=20，及 `c1c2c3=q1q2=h` 的符号与九次幂。表的十四个九次根模class完整覆盖二十个值，无漏项或重复领取。

α端点cubic值−109/8、263/64；b的两平方界、u²的12/35>49/144与6/17<9/25均通过。十四组严格区间逐组以有理交叉乘法核过。特别两对近界为

`3b/α<39/17<23/10<30/13<9/(bu)`，

`3bu<117/10<153/13<9α/b`。

其余端界亦正确，例如 `9u/b∈(21/26,36/43)⊂(4/5,17/20)`、`9/(bu)∈(30/13,720/301)⊂(23/10,12/5)`、`3b/u∈(129/4,234/7)⊂(32,34)`。数量2的六组各为c2/c3的非零实倍数或倒数；若其中c2/c3为实，共轭相等将违反已付χ简单性。因此每组内部非实且互异，跨组由严格模界分离，支付全部20 simple eigenvalues。最大M=(3αb)^9及第二模Tκ=(3b/u)^9准确。

## 3. 实际方程、完整head及无log应用

q=p6、P=q∧³C只含一个companion末行分母，故P的确为polynomial，无须q³。乘q的det末行线性性在p6=0处仍由原Σp_jf=0支付；prefix0/1/2所有p_j为0，P亦为0。N=10989同degree计算与完整生成身份 `[q(θ−1)I−zP(θ)]V=q(−1)W0` 均正确，未丢初始state或有限尾。

外幂next层在每个simple triple eigenprojection恰为3γξ=−(33/2)ξ；off-diagonal替换不贡献该投影，亦不要求差分O(1/r)误差逐项求差。普通最高两系数a、b及 `η=−b/a=33/2−N` 的符号和ρ幂核对一致。

rank1 augmented residue保留inhomogeneous常量列，`R²=ηR` 使重复zero块semisimple；正整数k的 `kI−adR` 不遇η的半整数差，C引理的majorant确给convergent gauge。jet chain的N−1 offset回到原V后得到完整 `analytic+t^(31/2)analytic`，不是把最高jet的η直接当V指数。故在全部非零有限operator谱点，所有实际transported branches均local monodromy阶至多2。允许fractional系数为0，未宣称每个谱点都是真实源奇点；也未证明0其他叶、∞或全局monodromy有限。

## 4. 最终共同小图与修订要求已闭合

T(t)=ρM(2t−t²)的0前像0、2，dominant前像1/multiplicity2，均准确。其他点模比≥(3/u)^9>5^9，而盘|t|<3/2的image模比<21/4，故没有其他候选前像或∞。

独审要求的唯一补明已在最终§5付清：先在盘去掉{0,1}；原生0 loop固定初始解析芽，1 loop投影dominant的两圈并在全部解上M²=I，两个generators先支付单值，再填0与1。没有假设所有返回0的transported叶自动解析。有限jets可有poles而保持meromorphic。

φ(w)=T(3w/2)的导数3/M<1，只证明这一张真实非univalent共同图的失败；未将它当作所有ramified/multivalent maps的cap，未免费改原整模型或把difference20当最小微分rank。无新数值ζ/L结论，原goal active。

## 5. 阅读与运行边界

一般Fuchs校准本人已实际读C来源中Novikov–Yakovenko author46页PDF的完整选段PDF33–38（6页）及DLMF2.7(i)相关E1–E6/全部条件；没有FULL46页，也不靠二阶DLMF替本高阶引理。Root的新表与方程纸核不使用数学程序、矩阵执行、复根求值或degree20展开。未重跑224/225任何producer；本独审数学运行 **0**。本收据保存后actual FULL全文自读并登记最终bytes/SHA。

