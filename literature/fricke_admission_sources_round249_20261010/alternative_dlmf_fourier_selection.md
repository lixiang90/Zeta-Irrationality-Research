# NIST DLMF 本轮完整所用 Fourier 公式

实际网页读取：https://dlmf.nist.gov/24.8.E1（重定向§24.8）。本任务仅采用§24.8(i) Equation24.8.1 的完整条件与公式：n≥1，0≤x≤1，

\[
B_{2n}(x)=(-1)^{n+1}\frac{2(2n)!}{(2\pi)^{2n}}
\sum_{k\ge1}\frac{\cos(2\pi kx)}{k^{2n}}.
\]

所以 n=1 时 ∑cos(2πkx)/k²=π²B₂(x)，B₂(x)=x²−x+1/6，包括整数端点。绝对收敛准许本文的有限 Fourier 重排。

网页还实际查看 https://dlmf.nist.gov/25.15(i) 定义25.15.1、Euler product25.15.2、Gauss sum定义25.15.6；没有把这些定义当成未读的 quadratic Gauss evaluation 证明。本文 Gauss χ−7=i√7 用有限 character orthogonality 和正 imaginary sign 自含核定。官方网页采用标准 statement，不声称读 Apostol 上游原证明；其它页面内容不是本任务所用 theorem scope。

只新存 alternative_dlmf24_8.html；本规范化选段是实际已读公式的精确记录，不伪称全文HTML人工读。
