import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith

/-!
# Algebraic core of the comparison-measure obstruction (2026-09-28)

`cross` is mutual logarithmic energy, `eRho/eSigma` are self energies, and
`vSigma` is the external-field integral. `hPotential` is obtained by integrating
`2 U_rho - V <= M` against sigma; `hEnergy` is zero-mass energy nonpositivity.

This file proves only the algebraic implication. The analytic hypotheses and the
numerical certificates are documented in research/restart_analysis.md; this is
NOT a formal proof of those inputs, nor of irrationality of zeta(7).
-/
namespace Zeta7.RestartObstruction

theorem comparison_ge_test (mass M eRho eSigma cross vSigma C : ℝ)
    (hPotential : 2 * cross - vSigma ≤ mass * M)
    (hEnergy : eRho + eSigma - 2 * cross ≤ 0) :
    eSigma - vSigma + C ≤ mass * M - eRho + C := by
  linarith

theorem no_negative_margin (A mass M eRho eSigma cross vSigma C : ℝ)
    (hPotential : 2 * cross - vSigma ≤ mass * M)
    (hEnergy : eRho + eSigma - 2 * cross ≤ 0)
    (hGap : 0 < A + eSigma - vSigma + C) :
    0 < A + (mass * M - eRho + C) := by
  have := comparison_ge_test mass M eRho eSigma cross vSigma C hPotential hEnergy
  linarith

#print axioms comparison_ge_test
#print axioms no_negative_margin

end Zeta7.RestartObstruction
