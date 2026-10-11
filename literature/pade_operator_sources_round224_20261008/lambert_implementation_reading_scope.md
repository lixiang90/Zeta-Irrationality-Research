# 第224轮 A：具体telescoper的实现来源与实际范围

2026-10-08。对应NEW `research/pade_centered_even_telescoper_round224_20261008.md`。本轮新operator由原分式的纸面principal-part reduction构造；以下网页只用于选择实现路线，不以软件介绍充作数学证明。

1. [SymPy official Concrete reference](https://docs.sympy.org/latest/modules/concrete.html)：实际选读Hypergeometric terms及`gosper_normal`、`gosper_term`、`gosper_sum`三个完整API条目。网页展示版本1.14.0。所读内容区分有理项比、Gosper正规形与单项反差分；没有从这一页推断可直接调用完整二变量Zeilberger实现。未FULL读整页所有1292行或包源码，未安装、导入、执行SymPy。
2. [RISC official HolonomicFunctions page](https://www1.risc.jku.at/sw/holonomicfunctions/)：实际读短页面全部64行，含Mathematica package、annihilating ideals、closure与creative telescoping简介、实现背景/用户手册链接。未读或下载该手册、notebook、Mathematica包，不声明已检查它的完整算法实现。
3. [Zeilberger official A=B packages page](https://sites.math.rutgers.edu/~zeilberg/programsAB.html)：实际读短页面全部34行，核EKHAD为Maple package及相关多变量/ZEILBERGER入口。未下载、运行其源码，不以检索摘要当具体certificate。

上述网页说明现成实现接口，但本机命令metadata未定位到Maple/Mathematica/Sage，C:/Python312的site-packages亦未含SymPy。于是采用Python标准库Fraction实现一个已纸证的固定维数特化；不调用现成order搜索，不猜递推。这里只报告这次metadata检查范围，不声称机器全盘没有其他CAS。

223冻结的WZ/Zeilberger primary阅读身份与scope仍由 `literature/pade_structure_sources_round223_20261008/lambert_reading_scope.md`登记，本轮不重复下载或冒称新FULL论文阅读。也未借Zudilin异族四阶operator作先验。本轮没有新PDF/HTML原件归档；此文件为准确URL与选读记录。

数学程序本任务**1次**：仅执行NEW `certify_pade_telescoper_residual_rank_round224_20261008.py`，固定n=6、centered shifts0,…,6，Fraction算principal parts、6×7 residual matrix与七个最大minor，exact reflection/kernel及一个未插值点核验。程序未读任何序列样本，未扫描n、阶数或参数，未运行222 producer。纯文档读取、web查阅、metadata与hash不计数学运行。

producer9628B，SHA256 `b01275768fe9700cc7c3b21befa91bfd5ca1a97676d34f459112f3d3f8e2fd8f`；输出26796B，SHA256 `a47a933aca74e035b49233d1f7cbd7106d770f679f5840934cdbfcfc69e4bbd0`。均实际FULL读取，exit0，rank6，七个最大minor全部非零。所有有理函数degree/boundary结论由数学稿纸证，不从这些检查点外推。该记录保存后需实际FULL作者复读，最终身份另报。
