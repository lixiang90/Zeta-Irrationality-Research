# 第248轮 C：增长矩阵/相对周期比较实际读域

2026-10-10。仅新增本轮数学稿、此scope及三份复用primary选段；未改旧稿、主日志、政策、manifest或任何外仓库。没有用消息或前轮独审替代本人本轮FULL读取。

## 1. 数学稿最终身份与账

research/global_growth_period_comparison_round248_20261010.md：7892 B，SHA256 98595cf9a440d808022acc167f28603ceef89f98038643fe34adb5c832c7aee3。修订保存后实际FULL读五节、G1/G2两引理及(G1)–(G6)。新证明是同对象外国窗口Schur降维/精确首层饱和判据，以及正Gram比较；G5只用实际|Q|给sym下界，已知|Q|上界不能代入作为下界，也不给sym小上界。未证明余det全尺度非零、宏观内容、strict预算或新数值定理。

历史7816 B / 1db01d46f3f343a846a833cff1ba36bf41c760d1edaaef3b86c8bb4209a791f6亦实际FULL作者读；Root独审指出G5后一语义需澄清，现仅修该推论文字。其余证明及历史输入不改。

数学程序/CAS/interval/素数、参数、map扫描/Lean0；旧producer0；外Git mutation0；新浏览搜索/GET0。文件读取、哈希及既存TXT截选/复制属于文档操作，不计数学执行。一次rg表达式无效、一次新文件patch语法校验失败后纠正，均未执行数学或修改旧文件。

## 2. 本轮实际FULL读取的项目最终稿

| 文件 | Bytes | SHA256 |
|---|---:|---|
| research/global_logistic_whole_functional_bridge_round240_20261008.md | 9796 | a655168bbd86afbacecf29bd91d396c7ce848bd5ea418a3300b71de36a5e316c |
| research/global_period_projection_review_round240_20261008.md | 9494 | 48e480e4529bc5c7132f20a1b7661056a93c7c63200ebfed77f94ec2310897a1 |
| research/global_logistic_direction_review_round244_20261009.md | 9524 | 74a58cdec68dec627b6fd4239797f0535b5c0747a1f5b64006e08b9d73f038a5 |
| research/global_chi7_positive_carrier_round244_20261009.md | 7698 | 639071cdf1d9469046246623e2308069b55271650cd74a17d3f837720b6d34c3 |
| research/logistic_gauss_rate_round242_20261009.md | 11788 | 30b39e40c5581e495cc96e18a903b36ea46354fd7c6cba3d658a48092f2b4631 |
| research/logistic_filtered_residual_round243_20261009.md | 11332 | e74b0ea9841ad09de08b7b039da6c627609d52a2778c4f069e941169536de84c |
| research/global_period_direction_review_round244_20261009.md | 13132 | cd34a475100c637a28c99f72508186d5d1a84a425ed103baa5fe3d871c9fa0a9 |

均实际读取完整正文。一次大批输出被总budget截断，未据此领取缺失部分FULL；A244、Root正载体和B242随后分别完整重读。C243最终六节C1–C14实际完整显示并读取。239的全部旧整格和241prime-edge全证明未在本轮重新FULL；表中241非零是244明确登记的既有输入，不冒本轮独立重认证。

去重只查了所列244稿的外国窗口/Schur相关段及已有文件目录，没有全库穷尽搜索。新G1称该已读范围尚未付的具体余det，不称数学史首次。

## 3. 实际primary读取与新保存选段

未下载新PDF，也未把原PDF全文范围继承过来。以下三份是既有保存TXT的逐byte复制或按完整section边界截取。

| 本轮新文件 | 实际读域 | Bytes / SHA256 |
|---|---|---|
| dual_brown2012_pdf08_11.txt | Brown 2012既存物理PDF8–11，印刷956–959：完整coaction (2.18)、comodule、D定义/derivation、cut (3.4)、Lemma3.2与Theorem3.3及所含证明；四页TXT实际FULL | 10769 / 892a7bf77d14a6672784b8ed0b4b11523dfc6a200d82f214b9a0d5c7d655ebf6 |
| dual_brown2014_pdf34_35.txt | Brown 2014既存物理PDF34–35：本M0,10配置experimental陈述、Definition11.1、Theorem11.2完整statement、Cor11.3证明和两谱序列开端；两页TXT实际FULL，不称FULL后续Theorem11.2全部证明 | 7070 / 655ffef8faee0e8b610fb6da4604ef65647fdce73cd5d9d235b0982e3e265a29 |
| dual_cdt_sections15_1_10_15_2.txt | CDT既存当前220页作者件选段中完整§15.1.10与§15.2，含Question15.2.2、Fact15.2.3及条件机制至§15.3之前；印刷193–197实际FULL，无全文220页claim | 15897 / d60a46044463782dcc98fcbd6fcc7b0453e3a14f604a1b634f4801ee62b46cf0 |

Brown原复制来源分别为239 lambert_brown2012_pdf08_11.txt、237 alternative_brown2014_pdf34_35.txt；CDT原来源为240 packet_cdt_current_pdf190_199.txt，37783 B / f0310bf198a942c1b2d5c33171b7a41d307db555fbeef5b91a18edcb2371a04c。本轮先实际读选段，再保存本目录；不称FULL整个190–199源TXT。其240来源记录实际采用3628820 B / 9d778fc22f82fb064371722ff457d54a2fc787608b8493ed9893a8fd39929a1c的220页作者PDF。未fresh GET，也不混称arXiv218页版本或最新云端证书。

## 4. Tang pinned原源码

复用240 root_zeta23、commit669c92bf7a3728e0de9ad80c373bc29fb5ca3d58。本轮实际FULL读：
- Zeta32/Criterion.lean：4336 B / 5afe2e69a7ac6168921dfd0997232e69d9e8ffdd1edbdbb9251a62e2448e020a。
- Zeta32/Assembly.lean：5670 B / 47b634df5e4b2cf04232658cdc3c1de013cf4b1216d97e816ccb9fc8aeb66276。
- Zeta32/FstarDefs.lean：3177 B / 794dd5ed22c9db1ae8ff4e10764c34d3026d4e5b09445fab63c816a0f7ad04b8。
- 240 pinned README全文；244相同README副本仅重复部分，无新增 theorem 认证。

这些是完整选定文件的paper读取，不是全部依赖、FstarPoints证明、Lean/kernel/Comparator执行，也不是fresh repository HEAD。README的数值结果与核检查按作者声明定位；本轮采用的仅明确criterion/三个node及FstarInput定义，不认证仓库全部结果或指定组合全球新颖性。

本scope保存后实际FULL自读；数学稿的FULL作者读不冒充独立审阅。

