# A245 模函数提升：实际阅读与执行范围

2026-10-10。对应NEW research/cm_modular_lift_review_round245_20261010.md。独立纸证，不修改冻结rank稿或Root/peer文件。

## 实际FULL内部输入

- 244源global_cm_log_trigger_round244_20261009.md：6783 B，SHA256187cbbd9bda470a07691dc2c962dd5054144e6c65a6542491498bb9342456d9c，六节C1–C7全部；本任务再次FULL读。
- A245冻结rank稿cm_actual_rank_round245_20261010.md：7188 B，fd02e917049de96221007fe6a6edb62615a55b785785b201979cf14338d18cec，七节R1–R8全部；再次FULL读，未改。新稿的F恢复用独立显式P，不以rank稿代替恢复证书。

## 本次primary实际选读

复用Root一次保存的[Chiang大学作者讲义](https://www.math.hkust.edu.hk/~machiang/5030/notes/5030_notes_2017_18_29Nov.pdf)。原PDF1912005 B / ca785c1f6c188943e936191c8228852e74fc443ef1fe466c3bd848022a14cadb。A实际FULL读root_chiang_pdf208_219_modular_lambda.txt全部12825 B / b8cae7fd2d75bdb3e022cf2098018f51b0604f4cdc655d20b550d787085703a2，即物理PDF208–219的完整第6章选段，含Thm6.3.1证明、cover remark及Thm6.3.2。没有读完整224页，未另下载。原(6.8)域误印与§6.3变换分母错由新稿M3明确修正；采用正确三边、K比单调、截角argument principle和反射证明，不逐字认可误印命题。

A实际FULL读以下四个Root保存的官方DLMF选段，只有选段，未FULL读四份HTML：

|文件|B|SHA256|使用范围|
|---|---:|---|---|
|root_dlmf_20_5_selected_equations.txt|653|7c7c9e678bc20b146607ec96fb41d1b89eec2e71b80d8ae7efa4ba9def8e055d|20.5.3 theta₃产品|
|root_dlmf_20_7_selected_equations.txt|1742|fc30bf6c9982e4f3837ecc36f9f08b01d19e8446d57aa35b156e38e45d7e4118|20.7.28/29/32周期与S变换|
|root_dlmf_23_15_selected_equations.txt|595|0d38f18c8b0dd17feb504243e0d04954f9e01015dc8dd6bf89aaa39b78428b9d|23.15.6 λ规范|
|root_dlmf_20_9_selected_equations.txt|881|e183aad255533255622e00d7b8b517d65d79a146fb41dc4dcef8ad59d80d2a5e|20.9.2 K/theta与K'/K|

此前同一任务的定向官方web读域为DLMF16.12.2完整Clausen式及20.5.3、20.7.28/29/32、20.9.1/2、23.15.6的公式与相邻定义；16.12页面也实际读取。15.8仅定位，未用其quadratic式；新稿链式代入自己证明所需quadratic。少量TeX端点访问失败，不算证明证据或完整文本阅读。不继承B/C对其它HTML的FULL声明。

## 新证明与执行账

新稿M1–M11为A实际纸面推导：F–theta身份、修补的覆盖、精确函数芽稳定子、所有branch的局部核查、删点/有界可去提升、Schwarz界、显式有理恢复P及H/S pullback链式。Root提供的P与提升候选均独立逐式核验，不以通信替代primary阅读。当前任务数学程序/CAS/扫描/Lean/git0；无新PDF下载，只有既存选段及文档读写/字节哈希。一次普通shell读取遭环境ACL启动失败，改为同内容授权读取成功；不是数学执行。保存后实际FULL作者复读新稿和本scope；同行独审另记，不以作者自读冒充独审。
