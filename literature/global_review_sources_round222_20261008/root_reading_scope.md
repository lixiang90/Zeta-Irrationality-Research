# 第222轮合并阅读范围与运行账

2026-10-08。本记录区别“亲自全文读取新研究稿”“实际原文选读”“有限精确数学执行”和“文档归档”。不把作者复读当独审，不把全文文本抽取或文件hash当整篇数学阅读。

## 1. Root亲自读取与独审

Root本轮实际FULL读取以下最终研究稿及全部证明/范围：

| 文件（相对research/） | bytes | SHA256 |
|---|---:|---|
| elementary_beta_weight_family_global_round222_20261008.md | 7024 | 1004a8326ce6c8fa12e08a79354236b7ec651a0e8f4961afadf506c06051c64d |
| zeta_residue_suspension_rigidity_global_round222_20261008.md | 2798 | 7ff7a3dba66b658b2022d931d7cfcf604908d33d21e6081bda015a69346699c9 |
| cyclotomic_joint_integral_global_round222_20261008.md | 8410 | 6c45b5ab4083d012d32f35cfad6f29f522b66f8b3420c8461490677d460d80cc |
| relation_source_architecture_global_round222_20261008.md | 11908 | 35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d |
| openai_source_architecture_global_round222_20261008.md | 15555 | e6d56d39c27f5ae67021598cac0e3df5a3d0b065582e640168d2cf029437aeb9 |
| pade_target_head_nonzero_round222_20261008.md | 3006 | c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f |
| research_global_review_round222_20261008.md | 9258 | a29a0253b047859a035d8098aafb37cc1773177594548f9429185a239ffb6f32 |

前两稿及有限补充为Root新证明；联合格和关系包由其他agent写，Root独立纸面核P1–P15、J1–J8并保存收据。β族及ζ源不变性由其他agent独审，架构稿由第三作者写并由独立agent审；有限补充由另一算法复核。各独审收据和全局报告收据的最终身份由[本轮manifest](../manifest_cdt_global_source_review_round222_20261008.json)登记；每份均由Root实际FULL最终读取后归档。这个登记不意味着Root重新审定所有primary theorem。

Root实际FULL读取架构初版14995字节、来源记录初版9082字节及修订最终来源记录11126字节。初版把f^(4)、f^(6)导数写成幂，Root/B提出必要数学修正，最终稿已按原文核定；初版不记PASS。完整审定对象仅上表最终身份，未改旧研究稿来遮盖修订历史。

Root本轮实际FULL读取旧输入：221汇总6873字节、221全图7527字节、220全局9404字节、214全局6979字节、zeta7_research_report.md 9310字节、odd_zeta_global_strategy_20261004.md 11981字节、research_navigation_protocol.md 2135字节。其旧验证/扫描声明只用于历史诊断，本轮没有重新执行。曾一次宽rg输出截断，不登记为全文读取；FULL范围只限另行完整读取的指定文件。main只核冻结前缀及新增报告，不登记本轮FULL阅读整个507032字节旧main。

## 2. 实际primary阅读分工

架构作者的[详细来源记录](source_reading_record.md)列出公共版本、读域、原件bytes/hash与必要修订时的补读。其实际读Catalan六个完整TeX section、DD完整introduction、Fauzan固定PDF第1–13页、Fischler固定v1第1–15页；不包括Catalan energy/certificate、Fauzan14–32页、Fischler16页以后或Lean全链。Fischler文件名的2020不替代真实v1日期2019-04-05。

关系包作者实际选读CDT固定v2第189–193页、Fischler–Rivoal固定v1第1–5页、Mistiaen固定v1第1–4页，保存对应TXT；CDT 218页全文、FR整篇及Mistiaen整篇均未在本轮FULL审定。Mistiaen一般维数/计数结果不当成指定ζ7或β4的无理性证明。

β族独审另实际读CDT固定v2第122–123页arbitrary-array完整定义/定理；架构独审另读Fauzan完整Prop2.2、Fischler完整Prop1/Remark3、旧导数核完整第1节及三个DLMF短式。具体限定分别见对应独审收据。

Root本轮实际FULL读取保存的commit JSON和DLMF三条短TeX式E29/E2/E4，未亲自FULL读上述所有primary selected pages/TeX sections；本记录与来源文件hash不能替代这种阅读。目录/README/verification stage只定位与核作者发布范围，不替代实际proof或内核验证。

## 3. 有限数学执行与文档操作

数学程序合计**2次**：

1. Root仅运行一次certify_pade_target_head_round222_20261008.py，以截断正则乘积和Fraction计算n=0,2,4；输出pade_target_head_certificate_round222_20261008.json。
2. 独审仅运行一次review_pade_target_head_bell_round222_20261008.py，以直接F(0)、log derivatives、Bell recurrence和Fraction Gaussian determinant计算同三个n；输出pade_target_head_bell_review_round222_20261008.json。未import/重跑Root producer。

Root实际FULL读取上述四文件。两算法精确相符，Δ₀=11581683398946533579805/32768>0。独审亦FULL补充引理；只核有限三行，未推无限非零或新数值定理。其他本轮数学稿/其独审的“程序0”仅限各自工作，或指生成有限证书之前的阶段，不能拼接成全轮程序0。

没有CAS、参数/素数扫描、PSLQ、数值积分、旧矩阵/能量证书重跑或Lean build。文档PDF文本抽取、rg定位、原件复制、bytes/hash及archive是文档操作，不是新增数学程序。Root对E:/codex-build/math执行只读status/HEAD核对，来源作者另核remote/date和GitHub main API；HEAD同adc7f1241b42e322a6451854ab7e4b4c146bf78a。本轮无fetch/checkout/pull或Git mutation。

## 4. 归档和后续导航

旧221manifest与其除可追加main外全部冻结pin保持身份。main保留507032字节前缀、仅追加完整最终222报告；新文件和复用原件由新manifest冻结，链接/控制字符检查是文档核验。没有新PDF下载；literature保存了实际选读TXT、固定仓库的七个TeX section、commit JSON、DLMF三短式及本记录。

主目标active，没有新数值无理性或线性无关性定理。正常下次全局复盘228（允许226–230），重大反例/上界或两轮无核心接口进展提前。下一窗口先检验实际三周期Padé源的递推、无限非零及真实解析增益；Δ₀非零不能替代这三个缺口。
