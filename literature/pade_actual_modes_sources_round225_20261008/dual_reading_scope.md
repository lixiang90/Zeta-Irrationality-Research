# 第225轮 C：实际 Fourier 渐近的来源与运行范围

2026-10-08。对应 NEW `research/pade_actual_fourier_modes_round225_20261008.md`。本轮只有一项 primary 页面选读；proof 中 contour、全局 maximum、远尾乘积界和 Gaussian connection 自含。

## 官方公式与完整适用条件

实际 web 打开 [DLMF5.11](https://dlmf.nist.gov/5.11)，读取 §i 的固定 sector `|arg z|≤π−δ`、E1 log-Gamma expansion、E3 scaled-Gamma expansion、E4 的 g0=1，以及 §ii 第一段完整 complex remainder bound。网页显示 Release 2026-09-15 的版本。仅这些有关公式和完整条件，不宣称完整读取全部413行或 §iii ratios、所有 exponentially improved bounds。

用 E1 的 complex remainder 在固定 sector 得 uniform O(1/|w|)，再由 Γ(w+1)=wΓ(w)得本文 G7。没有把 E7 的固定正实 a 改成 complex moving a；也没有只读 TEX 而漏 sector 条件。未读该网页所引 Olver、Boyd、Nemes 等原书或论文，没有使用其未读定理。

保存的新官方原件：`dual_dlmf_5_11.html`，212098 bytes，SHA256 `a89274abb01789070d9a97ce30c1e7f9d608523f0a2d3cf851c28e090a0ab1c3`。完整下载网页只表示原件归档，不登记 FULL 整页阅读。

实际 FULL 读取且复用此前原件 [223 E1 TEX](../pade_structure_sources_round223_20261008/dual_dlmf_5_11E1.tex)，167 bytes，SHA256 `7949ca75891c77763fea5a5dc3dae47c6d972cb454d3ab722cdefa2426012b5a`。不重复下载其别名。本轮新增 PDF0、HTML1、TEX0；没有新 hypergeometric、Paley–Wiener 或 saddle paper 被采用。

## 冻结输入与 proof 边界

224本人的 Fourier 最终稿12032B / `16e84deee6e12c94da29cee38171b0f65fabb765b31bb5ac06dd7f9edf6b3530`，本人既有实际 FULL 最终作者读，冻结版本身份本轮复核；使用其 actual centered entire Gamma 身份及 B=2hatA 的归一化。其B独审4324B / `f87001259756b43cc0ddf866491d4d1247882ebacc0e6248a0c665fa3e412199` 在224实际FULL读取。作者读不冒充自身独审。

223本人实际 I 衰减稿11630B / `abc734b21846a221e76daf0941dff3f6e5dba47d723ad420f87d78ce9b60922f` 及对应当轮独审为既有实际读史；本轮复用其已证同一 I_n 界，不宣称重新 FULL 审全部223 primary。没有采用Root/A的形式 stationary polynomial 或未冻结的operator结果作 connection theorem；实际三个 modes 由本文轮廓证明确定。

## 运行账

数学程序 **0**。只 web 选读一次官方页面、下载HTML、FULL读旧短TEX、写NEW数学稿/本记录及metadata查询。没有执行根求解、积分、矩阵、CAS、scan、guessing、PSLQ、Lean或旧producer。三个频率固定为1、3、5；无参数或natural-frequency搜索。

新实际成果是三频率各自非零主渐近、原 Δ actual dominant data 与条件关系的 strict radius gap。J 的 exact small growth、非多项式/非有理、共同source最小秩、完整 meromorphic 图和算术 strict gate仍需另付。保存后实际 FULL 作者复读本记录；最终身份外部登记。
