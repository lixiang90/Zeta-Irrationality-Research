# A240 实际读域

2026-10-08。数学程序/参数扫描/旧producer/Lean执行0。文献复制、文本定位和
identity hash仅是读写记录。只写本轮新稿与本目录 alternative_*，未改旧稿、
main、manifest、外部仓库或任何已保存Root/B/C资料。

## Fresh repository

外部 E:/codex-build/math只读；本轮执行5次Git：
rev-parse HEAD、remote get-url origin、禁fsmonitor的status --short、
log -5、ls-remote --symref origin HEAD refs/heads/main。
各shell设置GIT_OPTIONAL_LOCKS=0。HEAD/cloud main一致：
fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb，status空，origin
https://github.com/openai/math 。没有fetch/reset/write或Lean构建。
本轮actual web读官方GitHub根页；当前三个commits，与236baseline同snapshot。

FULL根README/history及Catalan、DD、凸体Mahler三个README。CONTENTS与目录名
仅定向关键词定位，非FULL；第一条宽文件列表因输出截断，仅作无效定位，
未以其中路径或Lean文件声称阅读/验证。检索未命中不证明全球absence或novelty。

## 三个primary的精确范围

1. OpenAI math Catalan当前作者源：FULL foundations、odd-primes、
nonvanishing、real-place、energy、certificate、conclusion七节；
未读introduction。FULL算法/命题文本不等于独立复算所有有限pivots、
root-count、trial常数或整篇证明认证。源码副本固定在上述commit。
两次合并输出曾截断，已分别重新完整输出相关节，不把被截断读取算FULL。
2. DD当前作者源：FULL introduction和§7 holonomy；未读§2–6/§8、
characteristic-2完整上界或完整依赖。depth-one实际式只用ζ(n)>0；
未声称数值period独立性。
3. Li Lai arXiv2610.06838v1：本轮web actual完整abstract、§1，
§2开头Definition2.1/Lemma2.2及partial-fraction身份，
§6尾Lemma6.3–6.5、Proposition6.6、Remark6.7。浏览结果另可见Lemma6.2，
但未称FULL§6。§3–5、全部paper和任何Lean均未审。
https://arxiv.org/abs/2610.06838 与 https://arxiv.org/html/2610.06838v1 。
Root已共享保存pdf443817B/SHA256
838c0331efb1ea249b60308e00e1fbc2ae8771c55da4eaf22e7beb0243250a58，
html769610B/SHA256
161ffb5d6b8f7221979a40fc55b95e24a30f8ed81a8807115990ca733dba5491。
本人不重复download，不冒称FULL共享pdf/html；third-paper只作有限补充。

本轮浏览3次tool调用：官方GitHub一次，Lai abs+HTML一次，HTML末段一次。
未扩大文献catalogue。Tang/Li2的primary核心读域由Root负责，本人只读Root
纸面扩展稿，不以其作者引用当本人完整源码审阅。

## 新副本身份

下列文件均由外部只读snapshot复制到本目录；FULL实际读域如上。
前缀一律alternative_；原外部文件没有写入。

|suffix|bytes|SHA256|
|---|---:|---|
|openai_math_README.md|4241|b0cc9fed82ea436c974d0d86fc30c8791a433b407254455c6e43c036b2dd5768|
|openai_math_history.md|2312|ff26d9214a6c29c6bb7faf99b0d55e72ba26a547b4e53485809e95f4de7f3374|
|dd_introduction.tex|9745|9d632ee8436f3fd986d2f784d1acc2c3024262aacb13a560e921b31963a7289a|
|dd_holonomy.tex|27594|aec06f4767cf810e421c4a394f543b1d7ce128c4a31f02cec5c32e3ecb2a8c44|
|catalan_foundations.tex|17469|21633dce32e242555dde97f82f1124f3524641bb69a2f16b7485177b667cb738|
|catalan_odd-primes.tex|26263|42228a070b0d0e070f78d78146d0881869578cca9112327d72a7c6c7e8fbea10|
|catalan_nonvanishing.tex|17218|4f8ddcf4a8c8eec1c1225d38a48e63a26a996ca399fea5cce88d3d0d4ef3f93f|
|catalan_real-place.tex|17837|4cd88cafd703b409e581df177cb891f53beb7626b547ec9f6003920861f9a74c|
|catalan_energy.tex|12218|d6c2488e86915f0b7f0af80705796eb8f2e13e03c2e3c59974b702723e5818e9|
|catalan_certificate.tex|19585|75dbdb4a57b54327391a9f883c903d9e8a3c1eef622c93fd569c9a07e94b968c|
|catalan_conclusion.tex|2580|de12e400d16e588d873439158e495a3da00d2a4907866f4ebc9aa94d9813f1a9|

## 本轮FULL研究输入

236 alternative主稿11218B/b99bcb2616a6a2c2fa2640a728464ce209650bce8b3a26e61ca4d3b025b3fe57
及其reading scope；239预算稿10804B/
8c0db240d561764395d958332fd144efb0d1ad6f08ef889c1488805830e31909；
Root logistic稿当前9796B/
a655168bbd86afbacecf29bd91d396c7ce848bd5ea418a3300b71de36a5e316c；
B240最终11398B/
b4d7d8d8ce37223ef1237d2b62c0bfbc58d30d94c7eee83b3578d03cbeac23a2
（新增p>N/a=0边界后，已再次actualFULL最终全文）。
本轮没有重新审历史manifest或重跑236–239程序。R3–R5条件matrix lemma为
纸面自证；源/费用/actual∞均限定所选同对象，不能外推新logistic对象已过关。
保存后作者实际FULL复读本轮主稿和本scope；不冒充独立审核。
