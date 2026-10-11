# C：244仓库/primary方向复盘实际读域

2026-10-09启动，2026-10-10完成；既定文件名20261009不改。
主稿：[global_repository_direction_review_round244_20261009.md](../../research/global_repository_direction_review_round244_20261009.md)。
本记录只登记本人实际读域；存原件/搜索命中不等于FULL读证明。

## 1. 本地/云端只读身份

E:/codex-build/math本地HEAD与公开openai/math HEAD/main均
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb。
本地commit时间2026-10-07T22:20:00-07:00，status porcelain含普通untracked为空。
实际只读执行rev-parse/log/remote/status/ls-tree/rg，以及网络ls-remote；
最后复核UTC2026-10-09T16:10:32.3563167Z。
没有fetch/pull/reset/checkout、Git mutation、外部repo写入。
最终实际输出保存dual_git_readonly_check.json，557 B /
5787166fd7a7c1138d9af9f2aafb22ba0f0ef37ad059dc179e4008aadb174c23。

FULL读原repo README、history、Catalan目录README，且FULL读下列字节副本；
CONTENTS只是有关family/名称的rg定位，tree只是相关目录名称定位。
首次全tex/pdf名称枚举输出巨大且截断，严格只计定位，不记目录FULL、全部文件FULL。

| 新保存字节副本 | bytes | SHA256 |
|---|---:|---|
| dual_openai_readme_fd4aeeb.md | 4241 | b0cc9fed82ea436c974d0d86fc30c8791a433b407254455c6e43c036b2dd5768 |
| dual_openai_history_fd4aeeb.md | 2312 | ff26d9214a6c29c6bb7faf99b0d55e72ba26a547b4e53485809e95f4de7f3374 |
| dual_catalan_readme_fd4aeeb.md | 533 | 197c77731d4846c84c14345185de1518c1e37b32c9a3a3218e864e3914e407de |
| dual_tang_readme_669c92bf.md | 7228 | ca99b77622320db0b0772baa4f72852a240de1c8163e1e81f9208ea1b37dadbf |

Tang副本复用240/root_zeta23/README.md；本人本轮FULL读原副本及新副本。
GitHub官方页面及实际ls-remote确认
669c92bf7a3728e0de9ad80c373bc29fb5ca3d58，与240相同。
没有FULL读全部Solution.lean/imports，不构建Lean/Comparator/nanoda/con-ron。
仓库百分比、formalization和novelty只是相应作者的声明；
未把README变成本项目kernel认证。236 Catalan核心读域仍是历史，不重新领取。

## 2. Lai固定原件和真正FULL的选页

原件复用
../global_review_sources_round240_20261008/root_lai2026_zeta3_zeta4_v1.pdf，
443817 B /838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58，
25页。官方abs https://arxiv.org/abs/2610.06838
本轮实际读元数据/摘要：只有v1，2026-10-05提交；不称journal发表。

实际FULL读物理PDF3–6、20–23；已保存以下完整选页TXT。
前者包括Definition2.1、Lemma2.2完整证明及Proposition3.1全部证明，
保留原分式、a/b/c假设、所有调和头、局部Gram单位块和Dirichlet无穷子族。
后者包括Lemma6.3、6.4、6.5、Proposition6.6完整statement/proof及末尾remarks/
references所到的页面。未读完整§4–5全prime证明，不认证整个数值定理。
PDF6另实际view_image视觉读取，核局部块与−4b²b_j²。

| 新选页 | bytes | SHA256 |
|---|---:|---|
| dual_lai_v1_pdf03_06.txt | 19647 | 7764b07a899c0843f85d8f05ba1f5e9edb18437ac73449933007605a0a567f60 |
| dual_lai_v1_pdf20_23.txt | 16515 | b94fb21c85bd965ce3cf72e10ade670911e3302c7fd98b874f16ae1b95508c8f |
| dual_lai_v1_pdf06.png | 166380 | 16a8d46a146ecd492f80874a6aee3439a6816f781a9140579360cee55f632d82 |

早期一次合并提取PDF1–6和另一次合并读取20–23输出截断；
没有据此登记FULL1–6。最终已单独FULL读上述3–6及20–23，范围以本表为准。
intro元数据/主结论来自官方页面及所到正文；未把它扩大为整篇paper审计。

## 3. 唯一fresh CDT原件及版本分离

本人一次实际GET https://math.berkeley.edu/~ytang/L2chi.pdf，
UTC2026-10-09T16:00:38.8059681Z，HTTP200，
Last-Modified Wed,10Dec2025 00:43:09GMT，
ETag W/"245388-37446c-6458e4ff70805"。
dual_cdt_L2chi_fresh_author_20261009.pdf：
3621996 B /7100fc291bb5c2bce4880d725eeba11e73114b0a20b4277f522030f855d89835。
实际pdfinfo为218页，创建/修改时间2025-12-10。
HTTP receipt dual_cdt_fresh_http_receipt.json：
332 B /d7daa07fb35b2174095d7d0d7f835ec0c4dc0e4872aa7ade215fd60526afb57e。

已有220页原件
../global_review_sources_round228_20261008/packet_cdt_L2chi_current_author.pdf：
3628820 B /9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c。
本轮核该文件身份，没有重新FULL其220页。
Root web open曾返回220页，本人web/fresh GET返回218页；不推断缓存/撤回/版本原因。
官方abs https://arxiv.org/abs/2408.15403 实际读完整文章元数据/摘要，
仍列2024v2、218pp；页数一致不证明bytes版本相同。

本人实际FULL读fresh物理PDF1–5、33–35：
目录、TheoremA/CorollaryB/C及Apéry比较；Lemma2.11.13证明尾和
Theorem2.11.17完整statement/proof。另视觉view_image读PDF34，确认为三项，
不能继承旧版本四项列表。没有FULL读fresh全部218页。

| 新完整选页 | bytes | SHA256 |
|---|---:|---|
| dual_cdt_fresh_pdf01_05.txt | 19649 | e14049c35e00f9cb714f85ff71c38236aa2c41d4431525348639244e7ab5ec3f |
| dual_cdt_fresh_pdf33_35.txt | 11525 | 0f9c9d2084bf625357068b4fe01780b62f2d1243b8504d0d23d7ddf2cd8a9dca |
| dual_cdt_fresh_pdf34.png | 194263 | 2f9742191107b6ccc74f6e3c2fbe88054b162c47cf36c4d20f400706a01d5ae8 |

复用当前ICM官方原件
../pade_galois_normalization_sources_round226_20261008/packet_cdt_icm2026_official.pdf：
653266 B /1b3fe13a89d04c3bc570b78c1130e5a03e33d4c2915ab4b065c3dc248b3eb98f，
20页。官方abs https://arxiv.org/abs/2510.04156 元数据/摘要实际读，
2025-10-05的v1、ICM2026 submission/to-appear声明；
没有借此称本轮获得新χ₋₇数值定理。
实际FULL选读PDF3–5，含Theorem2.1完整statement、Proposition2.4、
Remark2.5以及Theorem2.6的设置/statement开头；2.6跨页尾和完整证明未读。
保存dual_cdt_icm_pdf03_05.txt：
17482 B /08be95e4026ee04ec428af0703f4bcfa439334c813e119d383bfc6df27dd1ad9。
早期合并读既存3–8 TXT时输出截断，不登记FULL3–8。
本轮不重新认证主文§6–8、quantitative全稿或BC全部证明。

## 4. Sun–Zhou确切导子7评价、其它有界primary范围

官方abs https://arxiv.org/abs/2602.12091：
实际读完整文章元数据/摘要，v2列2026-03-02，37pp。
官方HTML https://arxiv.org/html/2602.12091v2：
实际读引言至完整Thm1.1及Table1，web约行46–139。
HTML正文日期显示August24,2026，官方abs版本日期和这一正文日期分别登记，
不推测差异来源。数学采用所存HTML实际内容，不从日期推新颖性。

复用A实际下载的alternative_sun_zhou_2602_12091v2.html：
1295974 B /45dac041f91f907b566863b6aaa56ff1bf251c0c899b7882460503bc9caa2e2d。
本人没有FULL读这个全HTML。
从section S1起至figure S1.T1结束的原HTML字节内容另存
dual_sun_zhou_v2_intro_thm11_table1.html：
135447 B /b252d2d254a6e321ce645123cb646b79a6f493f5c6caa824b565a2d6e644b095。
对应TeX alttext摘取TXT
dual_sun_zhou_v2_intro_thm11_table1.txt：
13189 B /b4109e83c58a0685fdac5040d2b7d4600db808c3071f3e8fae2abb4f7dd6ae0f。
本人实际FULL读最终TXT并对照官方HTML；正文(1.1)–(1.27)、Thm1.1(a)(b)
全部假设/定义及Table1都在选段中。
标记上的关键是：(1.12)先作为Sun此前conjecture引入，但Thm1.1后说明
与Table1明确声明已经推出(1.9)–(1.12)。此处引用为作者已建立的评价身份；
没有读完§2.2/2.3证明，不称本人独立审通完整proof。
TXT提取曾修正保护TeX中的小于号，属于文档解析修复，不是数学执行。

仅元数据/摘要读取：
https://arxiv.org/abs/2609.04176 （Sun2026 Catalan claim，v1，20页）；
https://arxiv.org/abs/2609.26354 （Eskandari2026逼近改进，v1）。
没有FULL读两篇证明，也没有因作者abstract/搜索摘要而采用irrationality结论。
Yunqing Tang官方主页 https://math.berkeley.edu/~ytang/ 实际读书目及状态：
CDT主稿submitted、ICMto-appear；不是由此认证全篇或期刊publication。

少量指定χ₋₇/Dirichlet L(2)/irrationality arXiv检索未给可采用覆盖定理；
未命中、无关search hits以及初次Tang姓名误配只计定位，不推出全球unresolved。
无更多primary搜索/新PDF扩展；既有Li2/其它χ或Mahler愿望表没有重开。

## 5. 本轮实际源状态输入及运行账

本人FULL读下列两新数学稿全部正文/公式/范围，用于四接口状态核对；
没有声称本阅读记录等于另一个正式独审receipt。

| 244输入 | bytes | SHA256 |
|---|---:|---|
| research/global_logistic_direction_review_round244_20261009.md | 9524 | 74a58cdec68dec627b6fd4239797f0535b5c0747a1f5b64006e08b9d73f038a5 |
| research/global_chi7_positive_carrier_round244_20261009.md | 7698 | 639071cdf1d9469046246623e2308069b55271650cd74a17d3f837720b6d34c3 |

另FULL读A实际scope3085 B /
801090ac4058c7f5805a0088dbb43e874ced8c1339acb55d26360917cf8f7984，
其中Root稿7659版是A当时实际读域，不能改写成本人的7698读域。
A非对称投影/safe LCD/统一线leading转移与Root对称源全尺度非零分开，
没有跨源互借energy、arith、非零。所谓−6仍条件于原完整Fstar认证。

本人新primary网络保存：1个PDF（CDT一次fresh GET）。
Sun–Zhou完整HTML是A的下载，本人仅从其原件抽取，新增GET0。
其余README为文件复制；原PDF复用。新选段TXT6、选段HTML1、PNG2；
实际PDF页面提取/渲染、HTML解析、hash及只读Git命令均为文档处理。
数学程序0、CAS0、有限证书执行0、参数/prime扫描0、Lean0、
历史producer/归档重跑0、外部仓库写0。
本轮只写本人NEW244稿、dual_来源/选段/本scope，不改任何旧稿、main或manifest。
主稿与本scope最终保存后实际FULL作者复读；自读不冒充独立审稿。
