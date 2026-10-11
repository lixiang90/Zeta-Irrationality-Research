# 第253轮唯一独立RV首关与进展审查

2026-10-10，B。结论：**PASS；以下冻结稿没有必要数学修订。** 本人实际FULL读Root最终六节、A/C最终全文、正式报告及四份scope，独立逐式核Root/A/C及报告范围。本人B作者稿只记录最终身份，不冒称作者自读是独审；其证明另由Root实际FULL核。数学程序、CAS、有限头程序/证书、所有扫描及新GET均0；B推导时三个n=1手算符号检查的读域已经如实更正，不作为全n证明输入。

## 1. 最终绑定

| 文件（research/） | bytes | SHA256 |
|---|---:|---|
| rv_chi8_positive_root_rank_round253_20261010.md | 9888 | 1448f96397dcd1468c91f7780fdcad4dbf7d8e9c030aa292e19c1117c516b0fc |
| rv_chi8_coefficient_intersection_round253_20261010.md | 7641 | 361387718baeceddb10c13cd966c85ece002c0a6bc10eb7c30085e9ab9e5552c |
| rv_chi8_contiguous_rank_round253_20261010.md | 7244 | 0278b174349e9ad6b27b19aaf0fe66c7edfbb4cecbcaf1d9f5c590bf9a101626 |
| rv_chi8_reciprocity_gate_round253_20261010.md | 8159 | ea6e8e703f48c23177b93b1a1ff6cfc69ba4311e6370672a02113bb355058d19 |
| research_rv_chi8_progress_round253_20261010.md | 5913 | ae39da2f4d7090c0cc28c51c512975712c838f0f55cb7e1992da2d5890fd274a |

同目录 literature/rv_chi8_sources_round253_20261010/ 的scope最终身份亦已核且本人实际FULL读：
root_reading_scope.md，3946 / 1697198a31ef42ee32169a1e1fb1f8f7f1a01b8d5cb7e986a2162ebb21632c7e；
alternative_reading_scope.md，2366 / f3a152195d2a56d3779a26d0a0de3b35ed6b30b73771c71080b5d949fe7a3d39；
packet_reading_scope.md，3183 / 882fdded6071597bd916d9cee7cf00ffda03fbfb63d9fb902810ebfa16ab0e52；
dual_reading_scope.md，3452 / f52a6a3324b8cc464891d4fadc0f517244e3f6706dc1d8e8f32ec955cb0dba58。

## 2. 真实系数与全尺度rank

Root(1)–(6)、A R3–R6、C C2–C7均从同一个正向双residue得到相同Q。内阶6n及外阶13n、内符号全部相消、外符号(-1)^(13n+1)=(-1)^(5n+1)、z幂和共同(z−1)^(3n)全部核清。原修正I=I0−log z I1、个别β=3n−r和整数LCM比完整保留；不是替换成另一超几何核或未修正实积分。

Root/C的W闭式证明尤其核过全部endpoint：s在3n+1..8n时测试多项式degree6n−1，0端由f的8n重零消边界；1端若f^(6n−1−j)不消，则j≤n−1，测试仍有至少n重零。故6n次IBP无遗漏边界，额外5n重根与原8n根、Vandermonde首项刚好付degree13n。A另一个交错Vandermonde系数提取也逐阶核清；它不依赖有限n结果。

正移位Euler引理包含重零及0到第一正根的一个Rolle零；0仅要求连续。每因子θ+a的单项式特征值k+a>0，故不把非零输入消掉。四列组合degree≤10n+3且保留≥10n个正实零，Φ8另需四个互异非实零，严格矛盾。这证明全部n≥2的前四列rank4、后三行rank3，没有把“5>3”或generic性当常数保留。

## 3. 整数实现、倒数与安全高度

Root从原整数W(t)证明Q=ΛR、R∈Z[z]；以R余数取adjugate确能省去完整Q-adjugate向量中的人造Λ³。整体P仍须Λ清整，未被删除。A/B/C的完整Q-adjugate也合法，但c分别是不同尺度的determinant；本报告和254选择的是Root的v=adj(R余数)e0、v4=0、c=Λdet(R余数)。

Root(9)的W正权重和、最大二项上指标25n+r给l1≤2^(51n+2r)；模Φ8带符号折叠不能增加l1，3×3和4×4行列式分别以6E³、24E⁴控制。因此O(n)对数向量高度upper真实完整，仍非primitive净成本或strict门槛。

C C10的θ移位不可省略，故h递推不是只乘(1−z)^r。C的倒数指数19n+r、个别归一化19n、首尾T(0)与T(N)绝对值不等均正确。cyclotomic倒数系数(q0,−q3,−q2,−q1)、公共相位(-1)^n z^(−n)以及M^(-1)保留正确；core常数不能替代实际Q的constant目标。这些检查没有被用来代替已经证明的实际rank。

## 4. 完整Cauchy桥与同对象误差

Root(10)–(14)新增链逐式核清。实z≥2时D≥zy使I0=O(z^(−21n−1))，y^(2n−1)可积；I1的u≤6n使O(z^(−23n−1))。共同归一化后完整F趋0。这里n固定，常数允许依赖n，绝不是n→∞的统一误差界。

Q Li2(1/z)在∞有收敛Laurent展开，P减其多项式部是多项式且趋0，故必为0。由Li2的Cauchy表示得
\[
P(z)=\int_0^1(-\log t)\frac{Q(z)-Q(t)}{z-t}\,dt,\quad
F(z)=-\int_0^1\frac{(-\log t)Q(t)}{z-t}\,dt.
\]
这在原real z>1确定同一canonical slit延拓；四个八次根不在[0,1]，不遗漏原log/contour修正。

索引z=ζ^(-a)给
\[
\tau^{-1}\sum_a\frac{\chi(a)}{\zeta^{-a}-t}
=\sum_{k\ge0}\chi(k+1)t^k=\frac{1+t^2}{1+t^4}.
\]
故误差的负号、实核以及Q=c+(1+t4)S的完整有理头全部正确。Gauss模型给A∈Z；不能把该头的逐项分母作为最佳primitive费用。

F=O(z^(-2n−1))+O(log z·z^(-4n−1))迫使前2n个Cauchy矩为0，正交范围j=0..2n−1正确。逐系数P_j=Σ_(k>j)Q_k/(k−j)^2给||P||1<2||Q||1；连同完整投影得到24ΛE⁴/48ΛE⁴及全A/c高度。正核没有使Q常号，也没有证明A−cY非零；c≠0仅是系数非零。

## 5. 报告、读域与下一关

正式报告5913全文PASS：本轮确实通过唯一首关，还付完整canonical实载体及安全高度；未领primitive内容、统一净衰减、实际值无界非零或新数值定理。254仅对已选同一v、v4=0分析gcd(A,c)后的完整实误差；未授权自由换包/向量/第五列/map/prime长期续窗。252为last正式，本轮completed1、next256、不reset；goal active、numeric false。粗upper不足不能变成所有RV方法no-go。

本人实际原文读域是既存RV物理4–6、17–21、22的完整文本，详见本人scope；采用完整published Theorem2.1，不冒称49页或全部前置算术引理全文/视觉认证。三份peer/root scope的FULL是检查其声明范围，不能冒领为本人阅读了他们所有来源。未新下载或采用搜索metadata作为数学定理。

B原7077稿的数学未变，最终7244与scope只明确n=1的W(0..2)三项手核不是全n输入。此处数学程序/有限头程序或证书0不表述成完全无有限纸面手算。仅写本唯一review，不改冻结作者稿、旧main/policy/manifest；一次文档归档是随后计划，执行及pins/prefix需归档后另只读核。保存后本人实际FULL复读本回执，作者自读不代替独审。

