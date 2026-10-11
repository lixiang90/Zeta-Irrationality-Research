import Mathlib
import PrimeNumberTheoremAnd.Consequences

/-!
# 素数定理（自 `PrimeNumberTheoremAnd` 导入，b-无关）

归一化步（Proposition 5.2-类比）需要 `θ(x) ~ x` 形式的素数定理。
mathlib 未包含；`PrimeNumberTheoremAnd` 项目（path 依赖）有。
镜像 `Apery/PNT.lean`。
-/

open Filter Asymptotics

namespace Zeta7

/-- Chebyshev 函数 `θ(x) = ∑_{p ≤ x} log p` 渐近于 `x`。 -/
theorem theta_asymptotic : Chebyshev.theta ~[atTop] id := chebyshev_asymptotic

end Zeta7
