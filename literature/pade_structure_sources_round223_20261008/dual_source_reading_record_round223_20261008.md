# 第223轮 dual：固定交错包的来源与实际阅读范围

2026-10-08。对应 `research/pade_actual_growth_structure_round223_20261008.md`。只登记本人的实际阅读，不把同行发现、检索标题或数学稿的作者读充作primary独审。

## 1. 原件及所读范围

1. W. Zudilin, *Well-poised hypergeometric service for zeta values*，作者原件 [z234.pdf](https://www.math.ru.nl/~zudilin/PS/z234.pdf)。共享保存路径 `lambert_zudilin2003_z234_author.pdf`；317847B，SHA256 `81eeeca38692773d3760cef033d007c63da4da8747276f707aa09ef0d3de9207`，33页。由A下载，本人复用既有文件，未再下载另一个别名。本人实际完整读作者PDF页23–25的全部已提取文本两次：§7在页23–24完整，含(62)–(66)、F₇与tildeF两组不同对象和特征多项式；页24–25包含§8开头、(67)–(70)完整定义及Theorem5跨页开头。Theorem5下一页条件没有读，不登记FULL theorem或整篇FULL，不采用该跨页定理。

   本人复制共享既有选页文本为 `dual_zudilin2003_pp23_25.txt`，9237B，SHA256 `93a9984acc8dac0e722e6e2cc7e1e09d5f9b33af09733373a679252edf56d7f0`，实际完整读取，无输出截断。所需比较只是式(62)／tildeF／式(69)的完整定义，不使用异族recurrence、极点除子或未读积分定理。web打开作者原件是primary核对入口，不声称web已FULL读33页。

2. NIST DLMF [§5.11](https://dlmf.nist.gov/5.11)，具体 [E1](https://dlmf.nist.gov/5.11.E1) 与 [E7](https://dlmf.nist.gov/5.11.E7)。实际读网页中两式、E1的避开负实轴扇形条件及E7的固定 a>0、固定 b 参数条件。只在正实n轴、a∈{1,2,3,4}、b∈{1/2,3/2}使用它；没有随n变化的Stirling参数。

   新下载并FULL读公式TEX `dual_dlmf_5_11E1.tex`，167B，SHA256 `7949ca75891c77763fea5a5dc3dae47c6d972cb454d3ab722cdefa2426012b5a`；`dual_dlmf_5_11E7.tex`，67B，SHA256 `90b8dcc8fd86e0ce0b91ea0328d943d45ef6c9531984b426a16a4055188db59d`。TEX只存公式，网页相关条件是另行实际读的范围，不把短TEX等同完整条件原件。没有另外下载大篇幅DLMF页面或异源论文。

## 2. 项目中实际FULL读取的固定数学输入

- `research/relation_source_architecture_global_round222_20261008.md`：11908B，SHA256 `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`。本轮实际FULL复读§1–§7、P1–P15，采用精确 R_n／I_n、周期系数、三行消元及poly(n)2¹⁵ⁿ上界。其旧d_(2n)、24/48是222历史阶段，未修改该冻稿。
- `research/pade_integer_valued_denominators_round223_20261008.md`：最终6110B，SHA256 `cea842775409706034017f9f1dbc7cbcde39ed6d331691dfa3d80588ab79c648`。本轮实际FULL读全部5节、D1–D7，独立纸核normalized binomial jets、vQ jets、完整有限tail与det清整。此前5822B/SHA256 `2d80b399e990204a69efa5b4372e279a1d1da2902571bc0cdc219205820ed182`版本亦已实际FULL读；作者随后澄清D1的b=0乘子及自己的primary读域，本人再次实际FULL复读6110版本。本人未读该作者报告的primary页6–7，不把他的原件印刷异文核定冒充自己的核定。新safe12/26适用于完全相同的实际包，不是最优成本定理；另存独审receipt。上述identity是本人本轮读取的保存版本，若作者日后变更需另登记。

本轮未读A、B尚未完成的223递推或mod-p稿，不替同行认证无限非零或holonomicity。未读尚未存在的归档manifest或阅读总表，不声明已经核定归档链接。没有新增OpenAI仓库检查，222冻结不动。

## 3. 数学与文档操作账

数学程序/CAS/积分或矩阵数值/PSLQ/Lean/prime、参数或网格扫描：**0**。未执行222有限producer或独立verifier，未作Git mutation、checkout、fetch。

实际工具只用于primary网页读取、两个公式TEX下载、共享选页TXT复制、项目文本FULL读取、新文档写入和metadata/hash。G1–G16的Γ重组、半整数留数轮廓、全高度界、有限头、Stirling指数及外积上界均为纸面证明。超几何身份也由项比直接证明，不调用已知异族定理。

来源记录与数学稿保存后的FULL作者复读和最终bytes/hash由另行消息登记；不把作者复读称为独立审阅。此记录不包含任何未做的完整PDF阅读或数学运行。
