# beta(4) 原列池、约束完美性与Padé来源稿的独立全文纸审

2026-10-07。审阅者：/root/scaled_root_finalize。对象为 research/cdt_beta4_pade_perfectness_sources_20261007.md，收审后的最终SHA256 ba9e63bd8277c48065dabfcbaa997d1ace515bafa8dcd8fa232158c824b676aa，21052 bytes；实际全文读取全部八节、P1–P28及公式(P1)–(P29)，并在作者仅更新审阅状态后再次全文回读最终版。结论：全文纸审通过，无数学修改请求。本记录不是Lean形式化验证，不复算任何旧证书。

## V1 完整约束块、合流符号与原投影

逐列核对低周期身份：原C_3在u≠v处的beta3系数为1/[4(u−v)]，beta2系数为−1/[16(u−v)^2]；在u=v时两列池entries定义为0，目标beta4由J_0提供。因此P4包含全部对角与非对角，并且不假设beta2/beta3的数值有理性。

原regular-part条件确为pL=0。L_I的第二列是对b_v求导，而不是对a_i求导，所以合流极限得到正的(a_i−b_v)^(−2)。普通减法型Cauchy determinant的符号为(−1)^binom(2n,2)=(−1)^n；每个内部差除epsilon后为1，跨组四个差留下V(J)^4，没有遗漏阶乘或额外2。按v先1阶再2阶的给定顺序，P5/P6符号与n1直接二阶校准一致。

delta_n非零使完整投影唯一，p=[I,−L_JL_I^(−1)]和原Hermite行相同。该有限约束正规性不等于实际周期配对非退化性，主稿作了准确区分。P8中+4的V(J)贡献以及分母交叉差的−2均正确，覆盖全部素数及全部p-power。

## V2 精确Schur身份、全素数支付与delta主率

按行J,I与列目标、约束排序，原block是[[A_J+TI,L_J],[A_I,L_I]]。左乘[[I,−L_JL_I^(−1)],[0,I]] determinant为1，给delta_n det(q+TI)，没有隐藏置换符号。实际C中的beta2/beta3列加法不会改变完整block determinant，于是P11为同一E的准确身份。

P12/P13将前n列分别乘d_(12n)^4（有理目标时再乘固定b），每个约束ℓ列乘d_(3n)^ℓ。累计指数是4n和(1+2)n=3n，全部列包括零对角已整；无素数例外，也没有将L_I逆免费当作GL(Z_p)。所得非零整数下界只在另证detE非零后使用。除以delta时符号应为−log|delta|，P14正确。

独立复算logV(2n)+4logV(n)的leading为4n²logn+(2log2−6)n²。交叉差和leading为2n²logn+(9log3/2−2log2−3)n²，乘−2后相加得到(6log2−9log3)n²。n²logn确切相消，连续角点log奇性可积，离散最小差1的边界支付O(nlogn)足够。P18费用57+6log2−9log3准确，是安全预算而非最优预算；同轮另一稿的更强771/40不使这个上界失效。

## V3 原核正则性与条件非零标准

手核Cauchy内核det[(1+x_i²y_j²)^−1]的符号为(−1)^binom(n,2)。广义单项式det与V(y^4)在排序内部为正，log²y/2非负、可积且内部严格正，原C各n阶行子式具有同一严格符号。有限个多项式因子在闭区间有界，Cauchy核≤1，故双Andreief全部绝对可积，没有隐藏端点条件。

若原row evaluation determinant在全部排序配置上有固定弱符号并在正测度集合严格，则另一侧Cauchy与单项式因子为固定严格符号，实际detE非零。这证P20为充分条件，不能由单行函数符号替代。p的全部同阶子式同号是另一份Cauchy–Binet充分条件，主稿未把二者宣称等价。固定GL_n换基只乘一个常数determinant，不能修复配置之间的变号。

## V4 两个actual n2反例的逐式手核

对n2，k0的原Phi在0的正规化Taylor为1+(43/60)z+(41/40)z²，k1在1为1−(49/12)(z−1)+(69/8)(z−1)²。代入原B11与D′得到P21五次多项式系数；这些是同一实际p，不是另选的行。

在t1处R0=123、R1=207、R0′=1562、R1′=2593，故W(1)=123·2593−1562·207=−4395，而W(0)=1。靠近两个端点的内部相邻配置determinants确有相反符号；排序双点空间连通，存在内部零配置。因此现有R行并非正区间Chebyshev系统。这只否定直接AT调用，不证明积分detE为零。

负轴P25两个quadratic判别式分别为−12911/3600与−2567/144，均严格负且leading正。负z处D(z)>0、两个N均负，F1无零点。infinity展开的1/z系数是(1562·207−123·2593)/207²=4395/207²，其导数在足够负处为负。0附近N1=329z³+O(z⁴)、D=−120z+O(z²)，得F1∼−329z²/120，F0∼1/z，比例导数∼360/(329z⁴)>0。因此连续比例不单调并有两个不同负节点同值；负轴Chebyshev捷径同样失败。没有把这一n2反例扩大为所有n或integrated determinant的no-go。

## V5 原始文献假设已实际核对

Fidalgo–López原件PDF2–5：Nikishin generating measures具有固定符号、无限支撑和相邻区间分离，mixed chains共享base measure；Theorems1.1/1.2确为其AT和mixed perfectness结论。Angelesco的零点计数依赖两两分離支撑；现有log²权重同一(0,1)不能免费变成多个分離支撑。

Bertola–Gekhtman–Szmigielski PDF6–13：Definitions2.1/2.5和Theorems2.1/2.4依赖真正TP核与正测度；Hilbert setup另有多项式density、bounded/injective pairing和dense range。本文P10单独证明的有限determinant机制准确，未把投影当作TP变换。

Zhang–Filipuk固定v2 PDF3–7：实际AT权重必须给对应multiple OP；沿每步multi-index加1的path取偶数长度Wronskian；type-I Theorem1.3另要求充分可微与Wronskian有定义。合流Hermite cardinal约束不满足这些假设；主稿没有借名称移植正性。

Wolfs固定v2 PDF2、4–7：near-diagonal条件和Proposition2.3的参数gap及noncollision/alternative gap是实际前提。composition公式只能在起始行determinant和核determinant已有相容符号时传递Chebyshev性，不能用来修复P12/P14反例。

Prévost–Sorokin PDF1–8的完整cycle、端点contact、辅助问题唯一性与Legendre remainder product确比一般functional independence强，末节给模型特定的正三重积分。Sorokin1994两页文本给相应Rodrigues/integral/asymptotic结构；其OCR公式未用于本审任何数值等式或算术常数。文献适用域的否定不排除新的actual orthogonal/cycle构造。

## V6 官方整列池与非零证书的范围

本轮fresh全文读取官方005说明和Catalan nonvanishing.tex，另完整读取odd-primes.tex第298–508行。整列池GL(Z_p)变换及逆均整，两次Cauchy–Binet可转移所有full minors的valuation，再转移prescribed整数filter；允许leading columns相关。新的rational Hermite投影用显式delta支付完整block，是正确对应接口，不能省掉delta付款。

官方nonvanishing假设Catalan有理，实际p² moment层、两个extraction shifts、palindromic Frobenius变基及原四阶column filter使48p reduction分解为三个固定48矩阵。这些具体层与identity尚未为beta4证明，原mod101 pivot文本不替新E非零性。本审只读该文本，没有重算任何pivot、矩阵、producer或Lean证书。

P28/P29的scaled full-block单位判据准确：三个列组各n列，总scale估值为n(v_pS_C+v_pS_1+v_pS_2)，先扣该scale再扣delta。固定beta4分母prime须排除或付清，主稿未当作免费例外。它给明确待证局部接口，未声称已经有非零reduction。

## V7 阅读域与物理证据

本审actual FULL：被审原f023候选及最终ba9e稿全部八节/P1–P28/公式1–29；直接冻结单周期a008稿全部八节/B1–B29；官方nonvanishing.tex全文；005.md全文；odd-primes.tex第298–508行。未继承旧轮或同行的全文读取域，也不把README/CONTENTS关键词定位扩称为全部数学审查。

本人本轮完整PDF文字读取共32个distinct页面：Fidalgo2–5（4），Bertola6–13（8），Zhang–Filipuk3–7（5），Wolfs2、4–7（5），Prévost–Sorokin1–8（8），Sorokin1994 1–2（2）。初次组合输出的截断部分已用Fidalgo5、Zhang3及Prévost5–6重新完整提取和读取；重复页不重复计数。另actual目读Zhang4和Bertola8两个完整页图，均为上述页域子集。

Zhang–Filipuk实读原件物理SHA为4d8bd906d67975c57d3a0ba81d340568c5af03956f9a3c09caa1b0c0580be2eb，与作者§8一致；直接模型a008物理SHA亦核一致。本审未再次下载任何原件，未独立重演作者历史download去重流程，不冒认其35页全文或4个页图。页提取、渲染和hash均为文档操作。

## V8 结论

P1–P28/公式1–29全部纸审通过，无正文修改请求。safe费用51.27与完整Schur内容正确；actual n2反例和严格文献假设阻止免费调用AT/perfectness；仍缺无限尺度detE非零和同一对象的足够实处衰减。因此没有新的beta4、higher beta或odd zeta数值无理性结论。

数学producer创建/执行/import/rerun=0；prime表/guard/Lean=0；新PDF下载=0。未改原仓库、620冻结记录、旧8稿或被审正文。本独审已由审阅者最后全文自读，作者收审后应最后全文回读；统一专项manifest单向固定最终文档，不作循环receipt。
