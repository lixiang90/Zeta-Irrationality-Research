# A225：主符号与稳定衰减的实际来源/执行范围

2026-10-08。本文是 precise selected-scope账本，不冒称整篇文献或全部项目FULL。

## 官方新增阅读

URL https://dlmf.nist.gov/2.9，NIST DLMF§2.9。web返回288行；实际数学选读§i lines44–159，E1–E8、distinct-root及coefficient-expansion条件、formal roots与actualsolutions的区别；另定位§iii line279的 arbitrary-order参考句。没有FULL读Wimp/Olver/Wong–Li等引用作品，不将second-order条目当任意sixth-order theorem。本文的谱norm和weighted-Volterra稳定引理自含纸证。

https://dlmf.nist.gov/2.9.E5.tex 与 E8.tex 两次web请求失败（400），无下载、无原件身份、不登记为actualFULL读原件。无新增PDF/HTML下载。旧223/224实现或主论文选页不重下载。

## 实际本地阅读

- 自己224 operator14482B／SHA256 `32d41b069e688a3aa4e93c44721fe39a6f4ebe1ce646df7fe902bf660d507efd`，本轮实际FULL复读T1–T18。
- 自己222 packet11908B／`35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`，本轮实际FULL复读P1–P15。
- C225 actualFourier稿11160B／`37d2a980146055a4b3509d7861f77d674bec6fca40cb55e5ec138aeaccc81788`，实际FULL读G1–G21。仅将G18–G21作为明确companion输入合并；本轮作者自读不冒称其全部proof已由本人独审。
- 223 actualI及强分母复用此前实际FULL及独审身份；未再FULL读CDT218页，也未查最新仓库。

## 数学执行：准确2次

先限定同一个degree6 quotient-algebra算法：g(u)、u逆元、p=−(1+2/u)^9、j0…6幂矩阵、全部七maximal cofactors、归一化χ及三因子代入。没有actualsequence值或recurrenceguessing。

第1次C:/Python312/python.exe执行exit1。手算quadratic trace误为19704582，因子assert失败，未输出JSON；实际Lucas s8=3048354、s9=19704870。失败记录700B／`ec02cd37b1e751c159e36405cd6602d8e7ae42db3b8518b5d59cb1cde14a27cf`。

第2次将同一个固定trace改为计算至s₉的Lucas recurrence，exit0；全部七cofactors非零、χ(p)=0、g/χ squarefree及factorproduct/代入核验通过。final producer5136B／`51822e871272b0aee875042c73aa53be06792a1085bed5d4a97bf525846bdffa`，JSON5526B／`87e412c2184de9c424831dd20e16e0b0b0f4160946a0c63cc69db49331b6f304`。成功运行后仅scope文字metadata明示失败/修复史，数学数据未改，未第三次执行。producer/output/失败记录与本scope保存后均须实际FULL复读。

没有CAS软件调用、浮点根、numericalintegration、prime/parameter/order扫描、PSLQ、Lean、旧producer复跑或Git。文档网页与hash操作不算数学程序。旧稿/main/manifest未修改。
