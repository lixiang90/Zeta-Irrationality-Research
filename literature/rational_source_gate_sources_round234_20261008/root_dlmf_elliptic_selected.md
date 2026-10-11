# DLMF完整椭圆积分：234选读与参数转换

2026-10-08。Root定向web检索实际读到官方19.4的19.4.1导数、19.7的19.7.1 Legendre关系；不称完整DLMF章节审阅。

一手来源：
[导数公式](https://dlmf.nist.gov/19.4.E1)；
[Legendre关系](https://dlmf.nist.gov/19.7.E1)；
[定义](https://dlmf.nist.gov/19.2)只作定义定位，未登记全文读取。

原来源用modulus k，补modulus k'=√(1−k²)。
K_k=(E−(1−k²)K)/(k(1−k²))；
E(k)K(k')+E(k')K(k)−K(k)K(k')=π/2。
这里撇号k'是补modulus，不能误当对k的导数。

Root正文使用参数x=k²，故定义Kpar(x)=K_DLMF(√x)；
Kpar_x=[Epar−(1−x)Kpar]/[2x(1−x)]。
令τ=iKpar(1−x)/Kpar(x)，从上述两式自证
τ_x=−iπ/[4x(1−x)Kpar(x)^2]。
其后通用覆盖半径和积分粗界均是Root推导，不冒称DLMF直接给出了本研究的全图cap。

新增PDF0、数学程序0。这是精确来源选读记录，网页检索本身不认证新的数值目标。
