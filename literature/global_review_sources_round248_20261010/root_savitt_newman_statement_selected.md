# Savitt 官方论文的完整所用声明：规范化记录

来源：David Savitt, An elementary proof of Newman's eta-quotient theorem，作者官方PDF https://math.jhu.edu/~savitt/papers/pdfs/newman.pdf 。Root实际读取web所展示物理PDF2的完整Theorem1.1、Remark1.2，以及PDF3的η S/T变换及紧邻上下文；不声称全部12页或全部证明FULL。以下是公式与含义的规范化记录，不是下载原PDF的替代身份。

令 f=∏_{m|N}η(mτ)^{r_m}，r_m∈Z，k=(1/2)∑r_m∈Z。Theorem1.1的两个条件为
Σ_{m|N}m r_m≡0 mod24，Σ_{m|N}m r_{N/m}≡0 mod24。
两者成立当且仅当f是Γ1(N)上的weakly holomorphic modular form。Nebentypus为χ(d)=((−1)^k s/d)，s=∏m^{r_m}，d取奇代表；extended Jacobi symbol按正文约定。因此Γ0(N)变换的字符由这一公式确定，不能从整数q系数或只检查T/U自动推Γ0模性。

Remark1.2给η(mτ)在a/c的leading exponent (gcd(c,m)^2)/(24m)，因此全纯/尖点形式条件分别是Σ gcd(c,m)^2 r_m/m≥0或>0，对所有c|N。转换到实际尖点uniformizer还要乘width N/gcd(c²,N)。本文不把weakly holomorphic误作cuspidal。

η(τ+1)=exp(πi/12)η(τ)，η(−1/τ)=exp(−πi/4)√τ η(τ)，√τ在H取第一象限分支。上述给Root使用的实际Fricke因子。

直接shell请求此官方PDF两次都被HTTP403拦截：第一次assert停止，第二次记录root_savitt_download_failure.json；没有保存成功PDF，没有绕过限制。web工具提供了可读官方载体，公式记录如上。没有读取Newman原1950年代论文、其上游完整证明，或声称Savitt整篇已认证。全部数学应用在Root248自行展开，未运行CAS。
