# 221 微分投影稿独立 FULL 审阅

2026-10-08，round218_dual_audit。**PASS，限目标稿实际范围；无必要修正。**

目标：[cyclotomic_relation_differential_projection_round221_20261008.md](cyclotomic_relation_differential_projection_round221_20261008.md)，5368 bytes，SHA256 `9586adb394cf371588e204077eda32ddc129e4066a85711fc44f0522ab80c03f`。实际 FULL 读取最终保存文件全部6节、P1–P6、输入身份与执行账，无截断。作者是Root；本 agent 是独立审阅者。冻结cross220由本 agent作者读、另agent独审，此角色不与本次混用。

P1–P2符号正确：\(S_g=S_0+g\log(1-x)\)，初始1-leaf中积分核残数为g−G，所以逆时针 \(\Delta_1S_g=2\pi i(g-G)\)。B在1全纯的精确分解证明完整局部恒等式；不是只消一个渐近首项，也没有自动支付所有全局前像的正确branch。

P3的函数秩不循环：实际i-monodromy先证明1,A,B独立；假设S属于背景后比较B系数给 \(r_2'=1/(1-x)\)，简单极点残数不可能来自有理函数导数。因此背景秩3、加S秩4，对任意g成立，不依赖待证的G无理性。

P4对正常排序的有限有理微分算子成立：S'已在微分稳定背景V中，所有高阶导数也在V，所以 \(PS=c_0S+v_P\)。保留完整V时c0非零可反解S，秩仍4；一组投影全部c0为零则均在V。

P5由微分与局部monodromy交换得到。有限阶有理零点不能把非零函数 \(c_0(g-G)\) 的差分变成恒零；有理极点同理。P6也正确：c0=0时log的所有正阶导数有理，故改变g只增加背景中的有理行。仅进一步去掉有理极点不构成新的对数单值化收益，因为direct CDT允许亚纯。

共同图断言正确：非恒定φ下有理系数拉回亚纯，已亚纯的完整背景使c0=0投影对任何固定有理g都亚纯。稿件没有宣称该背景最优图、能量或算术费用已付。它只关闭“保背景、纯有限有理求导、免费降秩并保目标信息”的捷径；明确不排除同秩分母改善、删部分背景后新证源、真正trace、积分、ramified base change或其他关系。新odd-support源不被本结论否定。

数学程序/CAS/矩阵/prime与parameter扫描/数值积分/PSLQ/Lean/Git全部0；仅文档FULL读取、有限纸审、SHA256与本NEW收据保存/作者FULL复读。未改目标稿、旧稿、main或manifest；没有新数值定理。收据final作者读/hash和目标身份复核外部登记。
