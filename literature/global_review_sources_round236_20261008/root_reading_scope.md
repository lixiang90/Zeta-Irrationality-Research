# 第236轮 Root 实际读域

2026-10-08。正式复盘在232后的第4轮完成；不把三份代理读域并入Root。数学程序0、扫描0、Git修改0、Lean构建0、新PDF下载0。仅新增本轮证明、源码副本、选段、一个PDF读用PNG及文档归档。

## 1. 本轮authoritative state

实际 FULL 读235最终report及manifest；实际核主日志609097 B，SHA256 893052a9f26c83b1453b2553c449786e458b5779801bf5a1fa3ebc8af520a687。未全文复读609KB主日志，也未执行235或更早producer。235 producer只实际读前150行以定位归档格式，非FULL或执行。

外仓库只读HEAD/status/remote，另成功执行一次git ls-remote origin refs/heads/main。当前local与fresh main同为fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status无条目。Web工具的GitHub API open不可用，不将失败误读为不存在更新；独立Git观测成功。没有fetch、checkout、pull或外仓库写入。[状态记录](root_repository_state.json)。

适用父路径AGENTS.md existence检查未发现文件；PDF skill已读取，本轮仅读/提取/渲染，不创建或编辑PDF。

## 2. Root实际完整读取的数学输入

- 232、228正式global report逐件完整；首个合并大batch总输出截断后另单独FULL补读。
- 234正式report完整，明确同源目标是t=5L(2,chi−3)/2−πlog3/(3sqrt3)，不混同232的Clausen目标。
- 235 arithmetic8633 B及candidate9563 B两个完整稿；其p²传播、simple-p固定A、完整native定义与rank/leaf使用边界已核。
- C236最终13797 B/cf93376bf4add588566fc577a3cf3bf682b5164dc9b1e02036e1e588cbfbb6a0全文及6104 B个人scope全文；Root独立重导C6–C10完整奇jet、∞叶及log阻碍。C的2433 B独审收据亦实际完整读取。
- A236初稿10986 B完整，发现一个有理试值误算并请求纠正；随后最终11218 B/b99bcb2616a6a2c2fa2640a728464ce209650bce8b3a26e61ca4d3b025b3fe57及4511 B scope均FULL。修正后根区间、指数符号、A8有限头及A10有核/格区别已核。
- B236最终11134 B/b60541c17c0f4440f3c971e3fd7c0224ebcfdd675f6120331d16262e710c4e70及4736 B scope均 actual FULL 补读；此前10236 B版本的阅读没有被当作后来新增部分已读。完整J1–J10独审PASS，具体见本轮Root数学检查稿。

并行消息用于定位与独立推导，不被登记为primary FULL阅读。自己的最终数学检查、正式报告、scope保存后另实际完整复读；最终归档只核新文件及235前缀，不宣称全文重审全部历史。

## 3. Root primary实际读域

**Catalan源码。** 当前外仓库foundations.tex与conclusion.tex完整读取；首批工具总输出截断后，foundations分1–250/251–末行补读，两段完整且连续。精确副本root_catalan_foundations_fd4aeeb.tex（17469 B）及root_catalan_conclusion_fd4aeeb.tex（2580 B）保存于本目录。只采用实际period projection、原2处完整模型和最终同归一化比较。没有Root FULL读另外六节或独立重算有限证书；八节实际读域属于dual。

原文：[foundations](https://raw.githubusercontent.com/openai/math/main/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/foundations.tex)，[conclusion](https://raw.githubusercontent.com/openai/math/main/preprints/Catalans-constant-is-irrational-September-24-2026/build/sections/conclusion.tex)。云端raw浏览作定位，本地完整源码及相同commit身份承担本轮完整读取证据。README只读前45行；全preprints/Lean名字首批检索输出截断，仅locator，未作全仓库数学审计。

**CDT当前作者220页版。** 本轮FULL读packet_cdt_current_pdf50_54.txt的物理50–54五完整页，实际核Theorem3.2.8、3.2.10、Lemma3.2.14及epsilon=0的范围。采用已给定理，不重证Shidlovsky/Chudnovsky；82–88仅由packet实际选读，Root不冒称该段FULL。[原文](https://math.uchicago.edu/~fcale/papers/L2chi.pdf)。

**定量holonomy后续。** 复用literature/pade_galois_normalization_sources_round226_20261008/packet_cdt_icm2026_official.pdf：20页，SHA256 1b3fe13a89d04c3bc570b78c1130e5a03e33d4c2915ab4b065c3dc248b3eb98f。对应pdf3_8.txt六页完整读取，物理4页另以fitz渲染root_icm_pdf04.png并实际view_image原尺寸查看。仅采用Proposition2.4的修正方向及定性极限、Theorem2.6的框架；不认证全部ICM证明。[作者原文](https://math.uchicago.edu/~fcale/papers/ICM.pdf)。

**Brown–Zudilin。** Root实际FULL读本目录保存的物理4–5、27–30（六页），采用实际渐近连接、实验性分母措辞、七重族及有限评价；未重算telescoping、HyperInt、5040群或全32页。原件literature/brown_zudilin_cellular.pdf身份与current v3观测见lambert scope。[primary](https://arxiv.org/abs/2210.03391v3)。其它几何论文的primary选段实际读域属于lambert，Root只读其有范围的比较稿。

本轮web另搜索beta4/holonomy/LI主文；搜索结果及abstract不是未读全文的证明，也不构成全球novelty认证。ICM current官方摘要与原文选段相符；没有依据搜索未命中声明目标全局尚未解决。

## 4. 可使用证据与未付接口

新增自含命题为完整奇部过滤排除、真实prime-window jet秩/格指数/CRT整模型及实际投影指数损失。原文定理与有限评价按注明的来源采用，独立纸核与原文有限证书执行分开。没有新的数值无理性或LI结果。

联合格的raw covolume还不是CDT费用；第237轮须先支付同一BC度量下的degree及全部filtered evaluation高度。c4只有更大的全entry周期投影可恢复，当前空间的直接有理过滤停止。Formal next默认242，窗口240–244；不以文献/归档/状态说明重置计数。
