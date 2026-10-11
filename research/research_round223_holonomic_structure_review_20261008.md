# 第223轮固定 Padé holonomic/G 结构独审

2026-10-08，agent `/root/round218_packet_audit`。结论：**PASS，无必要数学修正**；范围为下列保存稿的存在性证明与定义条件，不是具体 operator、最小阶数、无限非零或数值 theorem。

## 实际 FULL 身份

独立实际 FULL 读取数学稿全部七节/H1–H9及阅读记录全文，无截断，并核 bytes/SHA256：

| 对象 | bytes | SHA256 |
|---|---:|---|
| [数学稿](pade_holonomic_structure_round223_20261008.md) | 11517 | 54eb60ab2835832855cd268c5dfb4318f2c25019a4589cf713483460fa00866a |
| [作者阅读记录](../literature/pade_structure_sources_round223_20261008/lambert_reading_scope.md) | 3442 | 3b58968f46b60f3f7120691b5515ea319ff8fcf50b7eb8ed8d4e2c497fb1e978 |

本轮此前已实际 FULL 读同源222数学包11908 B / `35cc2ee9e99f667bdb1881efeb6ff8142cdbd1a088cef92822f2577e604c948d`及有限补充3006 B / `c017f50216ba3f9c8d37525ddac139bbceaf27d0f9e2c3aea03a05967e001b7f`，未重跑222程序。

## 条件与推导核对

H1由 pole 处约去v⁶的实际乘积得到，奇n的符号为(−1)^n；H3的Gamma exponents及normalizing factor正确。这里把v当交换参数，使用整数仿射 factorial arguments 和正负整数 powers 的proper项定理，不是由rational shift ratios或逐v存在递推推断一个Q(v) operator。负长度Pochhammer给generic参数下的Q(v)值；不在外侧Gamma极点直接取v=0。

H4两个cutoff生成函数正确且分母常数项1。先在Q(v)上相乘，再有限求和，确实支付全部k/u边界；适用的是**一般holonomic乘法和定义良好的求和closure**，不要求cutoff乘积继续是proper项，也不假定原Gamma项自然终止。H7由 `(u−v)^−2=Σ(a+1)v^a/u^(a+2)` 取v⁵得到所有 `j c_j/u^(j+1)`，保留奇j与全部有限tail。

Taylor lemma成立：清分母并除共同v幂后L0非零，H8给固定h的有限三角非齐次项；低层的shift/多项式乘法及加法closure给其annihilator，shift Ore环无零因子保证逐层齐次化operator非零。有限整数异常点不破坏存在性，不能据此冒称异常集合已算出。

偶section的rational δ、固定shift、六项termwise product分别支付A、C的偶子序列和Δ、Ξ、固定g组合。P-recursive/D-finite对应合法。旧P8–P9对奇n只有最高值符号变化，完整前缀LCD仍指数；旧绝对值界同样延伸，Q系数只有一个embedding。故D-finite、全部embedding增长、共同前缀分母三个G定义条件闭合，固定θ导数保持这些条件。没有用Betti/Hodge欠账拒绝此定义，也没有把G性质当作最小rank、目标非退化或strict overconvergence。

Δ0非零不排除有限支撑。最早recurrence系数无零和跨异常点finite bridge的接口准确，当前尚未提供这些具体数据。相近Zudilin族有不同分式/因子/导数/字符；其第四阶operator或characteristic polynomial未被移入本包。

## 本独审实际 primary 与执行范围

独立实际 FULL 读对应保存的选页TXT：Zeilberger1990 PDF14–20（完整Prop2.1、3.1′–3.5′及§3.2.1和条件）；WZ1992 PDF10–12、16–19（proper定义的参数/仿射条件、fundamental lemma/theorem及有限支持边界）；CDT固定v2 PDF189完整Definition15.1.1所在页；Zudilin作者版PDF23–25（§7与相邻§8开头）。未 FULL 读任一整篇，也不借作者scope冒充自己的读取。

实际核新三PDF的bytes/hash，与作者记录一致：Zeilberger3514835 / `3d6f88a09982574a7c74565d286fb2cd88aa1a3c0d5f76655f4be999cd516966`；WZ2889794 / `8dc85466d9bdffad1f44f33826df31b61076654b1dbf681c3c40ee33002e57b1`；Zudilin317847 / `81eeeca38692773d3760cef033d007c63da4da8747276f707aa09ef0d3de9207`。未重新下载原件或执行telescoping。

数学程序0，无CAS、矩阵执行、prime/参数扫描、guessing、PSLQ或Lean；只保存本NEW收据，未改目标、222、旧稿、main或manifest。收据保存后实际 FULL 复读，最终bytes/SHA另向Root登记。
