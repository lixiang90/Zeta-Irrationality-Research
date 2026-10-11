# 第224轮dual：Fourier实际核来源及读取范围

2026-10-08。对应 `research/pade_direct_fourier_kernel_round224_20261008.md`。所有数学均纸面推导，数学程序0。只写NEW224文件，不改旧/main/manifest。

## 官方原件与actual选读

本人实际web选读完整用到的公式及条件：

- [DLMF1.8](https://dlmf.nist.gov/1.8)：E3/E4复Fourier系数定义、连续同周期同系数唯一性完整段；E14及f∈C²、f和|f″|可积条件完整段。Q7用直接unfold+唯一性，不依赖不满足条件的形式Poisson公式。
- [DLMF1.14](https://dlmf.nist.gov/1.14)：(i)中E1定义、L¹连续性、Inversion段E3/E4和全部相关条件、Convolution段E5和L¹条件。DLMF使用正号及1/√(2π)，卷积局部亦带1/√(2π)；数学稿明确改用普通未归一化负号Fourier和普通卷积，2π常数逐式转换。
- [DLMF5.12](https://dlmf.nist.gov/5.12)：E1的beta–Gamma身份与正实部条件，E5的完整公式及Re a>0条件。实际代入a=2r+1、b=2x，先在beta两参正实部的范围使用，后由整个性延拓。

没有FULL读三个网页的全部章节或参考书。有界检索只定位hypergeometric/Andrews资料，不采用搜索摘要、二手页面或未读原论文定理；没有新增该类PDF。支持lemma以本整个函数的自足轮廓证明给出，无未读Paley–Wiener theorem。r依赖微分核通过普通L¹反演、weighted integral和普通分部积分支付，没有未说明分布边界。

## 保存的真实来源identity

三份官方HTML完整下载存档，但实际阅读仍为上述选段，不能记成整页FULL：

| 文件 | bytes | SHA256 |
|---|---:|---|
| dual_dlmf_1_8.html | 179059 | `64e7d4db21e893cb387996eba067d8a4e4de30cebc1b220e5d3f7a648794eabe` |
| dual_dlmf_1_14.html | 657223 | `16c38cf164a3f6103187f9e184226418bf335a475f11b6763e86dcbf7a114eca` |
| dual_dlmf_5_12.html | 133018 | `30cdb9e6c52c13532cdcd845e7f139b7f3d5454dc2927f88a28fc99849fd9f1c` |

五份官方短TEX下载后均实际FULL读；它们仅含公式，不代替网页条件原文：

| 文件 | bytes | SHA256 |
|---|---:|---|
| dual_dlmf_1_8E4.tex | 89 | `623e5ad0b99d84bd00705c66833464649be043c900ec7fd4f47011329debad05` |
| dual_dlmf_1_8E14.tex | 169 | `f86e19d6c0db94629592c5aef78c45805f1fe5985528f55c62e6e8b9794386ee` |
| dual_dlmf_1_14E4.tex | 101 | `0b6bf5bc52f4d030a8176b2b8219213259016ae88fafc2bd7d89544cdbd749a3` |
| dual_dlmf_1_14E5.tex | 81 | `2377b666a1f2e9858a35765a186769a0e6f5ce96f78594594d847b420d5b472f` |
| dual_dlmf_5_12E5.tex | 158 | `bbf976201943ab9b60724189970d864ebe16df9c8df55abc8e866ea228d0964e` |

## 项目输入与作者/独审边界

222固定数学包11908B/SHA `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`为本人此前已实际FULL读的冻结对象，本轮复用已核身份。223 holonomic11517B/`54eb60ab2835832855cd268c5dfb4318f2c25019a4589cf713483460fa00866a`及报告8464B/`6ee2aa403fdd73e32b6d5cc82f3611b49e4ef231b0b5b3f646e7937fa57f1edd`在上一报告审查任务实际FULL读；本轮没有改这些文件或重跑producer。

Root发送的csc三频率系数消息已逐项独立纸核，与本稿从Fourier jets计算的Q9和det常数一致；消息不是FULL稿。本稿首次封存时尚未actual FULL读取Root224最终保存主稿，不预先登记其独审。自己的kernel稿保存后actual FULL作者复读与同行独审分别登记，不将两者互换。

工具只web搜索/选读、官方网页/TEX下载、文档写入及metadata/hash。本任务数学程序0，无CAS、积分或Fourier数值、矩阵、参数/素数扫描、PSLQ、Lean、222producer或Git操作。来源记录保存后须actual FULL复读，最终bytes/hash另向Root登记。
