import Zeta7.Table7.I00
import Zeta7.Table7.I01
import Zeta7.Table7.I02
import Zeta7.Table7.I03
import Zeta7.Table7.I04
import Zeta7.Table7.I05
import Zeta7.Table7.I06
import Zeta7.Table7.I07
import Zeta7.Table7.I08
import Zeta7.Table7.I09
import Zeta7.Table7.I10
import Zeta7.Table7.I11
import Zeta7.Table7.I12
import Zeta7.Table7.I13
import Zeta7.Table7.I14
import Zeta7.Table7.I15
import Zeta7.Table7.I16
import Zeta7.Table7.I17
import Zeta7.Table7.I18
import Zeta7.Table7.I19
import Zeta7.Table7.I20
import Zeta7.PotentialIneq8

namespace Zeta7

lemma J_1_3 : ∀ t : ℝ, (9163 / 250000000000 : ℝ) < t → t ≤ (549 / 10000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (50233 / 1000000000000 : ℝ) with h | h
  · exact I_1 t h1 h
  · exact I_2 t h h2

lemma J_0_3 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (549 / 10000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9163 / 250000000000 : ℝ) with h | h
  · exact I_0 t h1 h
  · exact J_1_3 t h h2

lemma J_4_6 : ∀ t : ℝ, (1 / 10000000 : ℝ) < t → t ≤ (31919 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (111989 / 1000000000000 : ℝ) with h | h
  · exact I_4 t h1 h
  · exact I_5 t h h2

lemma J_3_6 : ∀ t : ℝ, (549 / 10000000000 : ℝ) < t → t ≤ (31919 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1 / 10000000 : ℝ) with h | h
  · exact I_3 t h1 h
  · exact J_4_6 t h h2

lemma J_0_6 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (31919 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (549 / 10000000000 : ℝ) with h | h
  · exact J_0_3 t h1 h
  · exact J_3_6 t h h2

lemma J_7_9 : ∀ t : ℝ, (247221 / 1000000000000 : ℝ) < t → t ≤ (745743 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (95997 / 250000000000 : ℝ) with h | h
  · exact I_7 t h1 h
  · exact I_8 t h h2

lemma J_6_9 : ∀ t : ℝ, (31919 / 200000000000 : ℝ) < t → t ≤ (745743 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (247221 / 1000000000000 : ℝ) with h | h
  · exact I_6 t h1 h
  · exact J_7_9 t h h2

lemma J_10_12 : ∀ t : ℝ, (340081 / 250000000000 : ℝ) < t → t ≤ (3851833 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1564143 / 1000000000000 : ℝ) with h | h
  · exact I_10 t h1 h
  · exact I_11 t h h2

lemma J_9_12 : ∀ t : ℝ, (745743 / 1000000000000 : ℝ) < t → t ≤ (3851833 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (340081 / 250000000000 : ℝ) with h | h
  · exact I_9 t h1 h
  · exact J_10_12 t h h2

lemma J_6_12 : ∀ t : ℝ, (31919 / 200000000000 : ℝ) < t → t ≤ (3851833 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (745743 / 1000000000000 : ℝ) with h | h
  · exact J_6_9 t h1 h
  · exact J_9_12 t h h2

lemma J_0_12 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (3851833 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31919 / 200000000000 : ℝ) with h | h
  · exact J_0_6 t h1 h
  · exact J_6_12 t h h2

lemma J_13_15 : ∀ t : ℝ, (35869 / 8000000000 : ℝ) < t → t ≤ (6890463 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2241937 / 500000000000 : ℝ) with h | h
  · exact I_13 t h1 h
  · exact I_14 t h h2

lemma J_12_15 : ∀ t : ℝ, (3851833 / 1000000000000 : ℝ) < t → t ≤ (6890463 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35869 / 8000000000 : ℝ) with h | h
  · exact I_12 t h1 h
  · exact J_13_15 t h h2

lemma J_16_18 : ∀ t : ℝ, (5951309 / 250000000000 : ℝ) < t → t ≤ (1499417253 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (23805751 / 1000000000000 : ℝ) with h | h
  · exact I_16 t h1 h
  · exact I_17 t h h2

lemma J_15_18 : ∀ t : ℝ, (6890463 / 500000000000 : ℝ) < t → t ≤ (1499417253 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5951309 / 250000000000 : ℝ) with h | h
  · exact I_15 t h1 h
  · exact J_16_18 t h h2

lemma J_12_18 : ∀ t : ℝ, (3851833 / 1000000000000 : ℝ) < t → t ≤ (1499417253 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6890463 / 500000000000 : ℝ) with h | h
  · exact J_12_15 t h1 h
  · exact J_15_18 t h h2

lemma J_19_21 : ∀ t : ℝ, (1451805751 / 2000000000000 : ℝ) < t → t ≤ (18635417253 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4307805751 / 4000000000000 : ℝ) with h | h
  · exact I_19 t h1 h
  · exact I_20 t h h2

lemma J_18_21 : ∀ t : ℝ, (1499417253 / 4000000000000 : ℝ) < t → t ≤ (18635417253 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1451805751 / 2000000000000 : ℝ) with h | h
  · exact I_18 t h1 h
  · exact J_19_21 t h h2

lemma J_21_23 : ∀ t : ℝ, (18635417253 / 16000000000000 : ℝ) < t → t ≤ (21443805751 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (10019805751 / 8000000000000 : ℝ) with h | h
  · exact I_21 t h1 h
  · exact I_22 t h h2

lemma J_23_25 : ∀ t : ℝ, (21443805751 / 16000000000000 : ℝ) < t → t ≤ (9 / 6250 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7 / 5000 : ℝ) with h | h
  · exact I_23 t h1 h
  · exact I_24 t h h2

lemma J_21_25 : ∀ t : ℝ, (18635417253 / 16000000000000 : ℝ) < t → t ≤ (9 / 6250 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (21443805751 / 16000000000000 : ℝ) with h | h
  · exact J_21_23 t h1 h
  · exact J_23_25 t h h2

lemma J_18_25 : ∀ t : ℝ, (1499417253 / 4000000000000 : ℝ) < t → t ≤ (9 / 6250 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (18635417253 / 16000000000000 : ℝ) with h | h
  · exact J_18_21 t h1 h
  · exact J_21_25 t h h2

lemma J_12_25 : ∀ t : ℝ, (3851833 / 1000000000000 : ℝ) < t → t ≤ (9 / 6250 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1499417253 / 4000000000000 : ℝ) with h | h
  · exact J_12_18 t h1 h
  · exact J_18_25 t h h2

lemma J_0_25 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (9 / 6250 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3851833 / 1000000000000 : ℝ) with h | h
  · exact J_0_12 t h1 h
  · exact J_12_25 t h h2

lemma J_26_28 : ∀ t : ℝ, (48661749009 / 32000000000000 : ℝ) < t → t ≤ (54465247027 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (25781749009 / 16000000000000 : ℝ) with h | h
  · exact I_26 t h1 h
  · exact I_27 t h h2

lemma J_25_28 : ∀ t : ℝ, (9 / 6250 : ℝ) < t → t ≤ (54465247027 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (48661749009 / 32000000000000 : ℝ) with h | h
  · exact I_25 t h1 h
  · exact J_26_28 t h h2

lemma J_29_31 : ∀ t : ℝ, (14341749009 / 8000000000000 : ℝ) < t → t ≤ (31585247027 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12053749009 / 6400000000000 : ℝ) with h | h
  · exact I_29 t h1 h
  · exact I_30 t h h2

lemma J_28_31 : ∀ t : ℝ, (54465247027 / 32000000000000 : ℝ) < t → t ≤ (31585247027 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (14341749009 / 8000000000000 : ℝ) with h | h
  · exact I_28 t h1 h
  · exact J_29_31 t h h2

lemma J_25_31 : ∀ t : ℝ, (9 / 6250 : ℝ) < t → t ≤ (31585247027 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (54465247027 / 32000000000000 : ℝ) with h | h
  · exact J_25_28 t h1 h
  · exact J_28_31 t h h2

lemma J_32_34 : ∀ t : ℝ, (66072243063 / 32000000000000 : ℝ) < t → t ≤ (71875741081 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8621749009 / 4000000000000 : ℝ) with h | h
  · exact I_32 t h1 h
  · exact I_33 t h h2

lemma J_31_34 : ∀ t : ℝ, (31585247027 / 16000000000000 : ℝ) < t → t ≤ (71875741081 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (66072243063 / 32000000000000 : ℝ) with h | h
  · exact I_31 t h1 h
  · exact J_32_34 t h h2

lemma J_35_37 : ∀ t : ℝ, (7477749009 / 3200000000000 : ℝ) < t → t ≤ (5761749009 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (20145247027 / 8000000000000 : ℝ) with h | h
  · exact I_35 t h1 h
  · exact I_36 t h h2

lemma J_34_37 : ∀ t : ℝ, (71875741081 / 32000000000000 : ℝ) < t → t ≤ (5761749009 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7477749009 / 3200000000000 : ℝ) with h | h
  · exact I_34 t h1 h
  · exact J_35_37 t h h2

lemma J_31_37 : ∀ t : ℝ, (31585247027 / 16000000000000 : ℝ) < t → t ≤ (5761749009 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (71875741081 / 32000000000000 : ℝ) with h | h
  · exact J_31_34 t h1 h
  · exact J_34_37 t h h2

lemma J_25_37 : ∀ t : ℝ, (9 / 6250 : ℝ) < t → t ≤ (5761749009 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31585247027 / 16000000000000 : ℝ) with h | h
  · exact J_25_31 t h1 h
  · exact J_31_37 t h h2

lemma J_38_40 : ∀ t : ℝ, (5046749009 / 1500000000000 : ℝ) < t → t ≤ (4331749009 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4617749009 / 1200000000000 : ℝ) with h | h
  · exact I_38 t h1 h
  · exact I_39 t h h2

lemma J_37_40 : ∀ t : ℝ, (5761749009 / 2000000000000 : ℝ) < t → t ≤ (4331749009 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5046749009 / 1500000000000 : ℝ) with h | h
  · exact I_37 t h1 h
  · exact J_38_40 t h h2

lemma J_41_43 : ∀ t : ℝ, (28892243063 / 6000000000000 : ℝ) < t → t ≤ (11565247027 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3974249009 / 750000000000 : ℝ) with h | h
  · exact I_41 t h1 h
  · exact I_42 t h h2

lemma J_40_43 : ∀ t : ℝ, (4331749009 / 1000000000000 : ℝ) < t → t ≤ (11565247027 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (28892243063 / 6000000000000 : ℝ) with h | h
  · exact I_40 t h1 h
  · exact J_41_43 t h h2

lemma J_37_43 : ∀ t : ℝ, (5761749009 / 2000000000000 : ℝ) < t → t ≤ (11565247027 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4331749009 / 1000000000000 : ℝ) with h | h
  · exact J_37_40 t h1 h
  · exact J_40_43 t h h2

lemma J_44_46 : ∀ t : ℝ, (3759749009 / 600000000000 : ℝ) < t → t ≤ (3616749009 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (40499239099 / 6000000000000 : ℝ) with h | h
  · exact I_44 t h1 h
  · exact I_45 t h h2

lemma J_43_46 : ∀ t : ℝ, (11565247027 / 2000000000000 : ℝ) < t → t ≤ (3616749009 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3759749009 / 600000000000 : ℝ) with h | h
  · exact I_43 t h1 h
  · exact J_44_46 t h h2

lemma J_46_48 : ∀ t : ℝ, (3616749009 / 500000000000 : ℝ) < t → t ≤ (71914098663 / 8750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (270414412641 / 35000000000000 : ℝ) with h | h
  · exact I_46 t h1 h
  · exact I_47 t h h2

lemma J_48_50 : ∀ t : ℝ, (71914098663 / 8750000000000 : ℝ) < t → t ≤ (161070179337 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (304898376663 / 35000000000000 : ℝ) with h | h
  · exact I_48 t h1 h
  · exact I_49 t h h2

lemma J_46_50 : ∀ t : ℝ, (3616749009 / 500000000000 : ℝ) < t → t ≤ (161070179337 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (71914098663 / 8750000000000 : ℝ) with h | h
  · exact J_46_48 t h1 h
  · exact J_48_50 t h h2

lemma J_43_50 : ∀ t : ℝ, (11565247027 / 2000000000000 : ℝ) < t → t ≤ (161070179337 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3616749009 / 500000000000 : ℝ) with h | h
  · exact J_43_46 t h1 h
  · exact J_46_50 t h h2

lemma J_37_50 : ∀ t : ℝ, (5761749009 / 2000000000000 : ℝ) < t → t ≤ (161070179337 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (11565247027 / 2000000000000 : ℝ) with h | h
  · exact J_37_43 t h1 h
  · exact J_43_50 t h h2

lemma J_25_50 : ∀ t : ℝ, (9 / 6250 : ℝ) < t → t ≤ (161070179337 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5761749009 / 2000000000000 : ℝ) with h | h
  · exact J_25_37 t h1 h
  · exact J_37_50 t h h2

lemma J_0_50 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (161070179337 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9 / 6250 : ℝ) with h | h
  · exact J_0_25 t h1 h
  · exact J_25_50 t h h2

lemma J_51_53 : ∀ t : ℝ, (67876468137 / 7000000000000 : ℝ) < t → t ≤ (53409472101 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (44578040337 / 4375000000000 : ℝ) with h | h
  · exact I_51 t h1 h
  · exact I_52 t h h2

lemma J_50_53 : ∀ t : ℝ, (161070179337 / 17500000000000 : ℝ) < t → t ≤ (53409472101 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (67876468137 / 7000000000000 : ℝ) with h | h
  · exact I_50 t h1 h
  · exact J_51_53 t h h2

lemma J_54_56 : ∀ t : ℝ, (195554143359 / 17500000000000 : ℝ) < t → t ≤ (21279612537 / 1750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (408350268729 / 35000000000000 : ℝ) with h | h
  · exact I_54 t h1 h
  · exact I_55 t h h2

lemma J_53_56 : ∀ t : ℝ, (53409472101 / 5000000000000 : ℝ) < t → t ≤ (21279612537 / 1750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (195554143359 / 17500000000000 : ℝ) with h | h
  · exact I_53 t h1 h
  · exact J_54_56 t h h2

lemma J_50_56 : ∀ t : ℝ, (161070179337 / 17500000000000 : ℝ) < t → t ≤ (21279612537 / 1750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (53409472101 / 5000000000000 : ℝ) with h | h
  · exact J_50_53 t h1 h
  · exact J_53_56 t h h2

lemma J_57_59 : ∀ t : ℝ, (442834232751 / 35000000000000 : ℝ) < t → t ≤ (477318196773 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (230038107381 / 17500000000000 : ℝ) with h | h
  · exact I_57 t h1 h
  · exact I_58 t h h2

lemma J_56_59 : ∀ t : ℝ, (21279612537 / 1750000000000 : ℝ) < t → t ≤ (477318196773 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (442834232751 / 35000000000000 : ℝ) with h | h
  · exact I_56 t h1 h
  · exact J_57_59 t h h2

lemma J_60_62 : ∀ t : ℝ, (2207857941 / 156250000000 : ℝ) < t → t ≤ (264522071403 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (102360432159 / 7000000000000 : ℝ) with h | h
  · exact I_60 t h1 h
  · exact I_61 t h h2

lemma J_59_62 : ∀ t : ℝ, (477318196773 / 35000000000000 : ℝ) < t → t ≤ (264522071403 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2207857941 / 156250000000 : ℝ) with h | h
  · exact I_59 t h1 h
  · exact J_60_62 t h h2

lemma J_56_62 : ∀ t : ℝ, (21279612537 / 1750000000000 : ℝ) < t → t ≤ (264522071403 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (477318196773 / 35000000000000 : ℝ) with h | h
  · exact J_56_59 t h1 h
  · exact J_59_62 t h h2

lemma J_50_62 : ∀ t : ℝ, (161070179337 / 17500000000000 : ℝ) < t → t ≤ (264522071403 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (21279612537 / 1750000000000 : ℝ) with h | h
  · exact J_50_56 t h1 h
  · exact J_56_62 t h h2

lemma J_63_65 : ∀ t : ℝ, (546286124817 / 35000000000000 : ℝ) < t → t ≤ (580770088839 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (140882026707 / 8750000000000 : ℝ) with h | h
  · exact I_63 t h1 h
  · exact I_64 t h h2

lemma J_62_65 : ∀ t : ℝ, (264522071403 / 17500000000000 : ℝ) < t → t ≤ (580770088839 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (546286124817 / 35000000000000 : ℝ) with h | h
  · exact I_62 t h1 h
  · exact J_63_65 t h h2

lemma J_66_68 : ∀ t : ℝ, (11960241417 / 700000000000 : ℝ) < t → t ≤ (79062004359 / 4375000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (87893436123 / 5000000000000 : ℝ) with h | h
  · exact I_66 t h1 h
  · exact I_67 t h h2

lemma J_65_68 : ∀ t : ℝ, (580770088839 / 35000000000000 : ℝ) < t → t ≤ (79062004359 / 4375000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (11960241417 / 700000000000 : ℝ) with h | h
  · exact I_65 t h1 h
  · exact J_66_68 t h h2

lemma J_62_68 : ∀ t : ℝ, (264522071403 / 17500000000000 : ℝ) < t → t ≤ (79062004359 / 4375000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (580770088839 / 35000000000000 : ℝ) with h | h
  · exact J_62_65 t h1 h
  · exact J_65_68 t h h2

lemma J_69_71 : ∀ t : ℝ, (649738016883 / 35000000000000 : ℝ) < t → t ≤ (136844396181 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (333489999447 / 17500000000000 : ℝ) with h | h
  · exact I_69 t h1 h
  · exact I_70 t h h2

lemma J_68_71 : ∀ t : ℝ, (79062004359 / 4375000000000 : ℝ) < t → t ≤ (136844396181 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (649738016883 / 35000000000000 : ℝ) with h | h
  · exact I_68 t h1 h
  · exact J_69_71 t h h2

lemma J_71_73 : ∀ t : ℝ, (136844396181 / 7000000000000 : ℝ) < t → t ≤ (718705944927 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (175365990729 / 8750000000000 : ℝ) with h | h
  · exact I_71 t h1 h
  · exact I_72 t h h2

lemma J_73_75 : ∀ t : ℝ, (718705944927 / 35000000000000 : ℝ) < t → t ≤ (753189908949 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (52567709067 / 2500000000000 : ℝ) with h | h
  · exact I_73 t h1 h
  · exact I_74 t h h2

lemma J_71_75 : ∀ t : ℝ, (136844396181 / 7000000000000 : ℝ) < t → t ≤ (753189908949 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (718705944927 / 35000000000000 : ℝ) with h | h
  · exact J_71_73 t h1 h
  · exact J_73_75 t h h2

lemma J_68_75 : ∀ t : ℝ, (79062004359 / 4375000000000 : ℝ) < t → t ≤ (753189908949 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (136844396181 / 7000000000000 : ℝ) with h | h
  · exact J_68_71 t h1 h
  · exact J_71_75 t h h2

lemma J_62_75 : ∀ t : ℝ, (264522071403 / 17500000000000 : ℝ) < t → t ≤ (753189908949 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (79062004359 / 4375000000000 : ℝ) with h | h
  · exact J_62_68 t h1 h
  · exact J_68_75 t h h2

lemma J_50_75 : ∀ t : ℝ, (161070179337 / 17500000000000 : ℝ) < t → t ≤ (753189908949 / 35000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (264522071403 / 17500000000000 : ℝ) with h | h
  · exact J_50_62 t h1 h
  · exact J_62_75 t h h2

lemma J_76_78 : ∀ t : ℝ, (9630398637 / 437500000000 : ℝ) < t → t ≤ (402457927491 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (787673872971 / 35000000000000 : ℝ) with h | h
  · exact I_76 t h1 h
  · exact I_77 t h h2

lemma J_75_78 : ∀ t : ℝ, (753189908949 / 35000000000000 : ℝ) < t → t ≤ (402457927491 / 17500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9630398637 / 437500000000 : ℝ) with h | h
  · exact I_75 t h1 h
  · exact J_76_78 t h h2

lemma J_79_81 : ∀ t : ℝ, (822157836993 / 35000000000000 : ℝ) < t → t ≤ (24475480029 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (209849954751 / 8750000000000 : ℝ) with h | h
  · exact I_79 t h1 h
  · exact I_80 t h h2

lemma J_78_81 : ∀ t : ℝ, (402457927491 / 17500000000000 : ℝ) < t → t ≤ (24475480029 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (822157836993 / 35000000000000 : ℝ) with h | h
  · exact I_78 t h1 h
  · exact J_79_81 t h h2

lemma J_75_81 : ∀ t : ℝ, (753189908949 / 35000000000000 : ℝ) < t → t ≤ (24475480029 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (402457927491 / 17500000000000 : ℝ) with h | h
  · exact J_75_78 t h1 h
  · exact J_78_81 t h h2

lemma J_82_84 : ∀ t : ℝ, (1497440999647 / 60000000000000 : ℝ) < t → t ≤ (518421798487 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (763176598777 / 30000000000000 : ℝ) with h | h
  · exact I_82 t h1 h
  · exact I_83 t h h2

lemma J_81_84 : ∀ t : ℝ, (24475480029 / 1000000000000 : ℝ) < t → t ≤ (518421798487 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1497440999647 / 60000000000000 : ℝ) with h | h
  · exact I_81 t h1 h
  · exact J_82_84 t h h2

lemma J_84_86 : ∀ t : ℝ, (518421798487 / 20000000000000 : ℝ) < t → t ≤ (64523591651 / 2400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (198022199171 / 7500000000000 : ℝ) with h | h
  · exact I_84 t h1 h
  · exact I_85 t h h2

lemma J_86_88 : ∀ t : ℝ, (64523591651 / 2400000000000 : ℝ) < t → t ≤ (1670914187089 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (273666998197 / 10000000000000 : ℝ) with h | h
  · exact I_86 t h1 h
  · exact I_87 t h h2

lemma J_84_88 : ∀ t : ℝ, (518421798487 / 20000000000000 : ℝ) < t → t ≤ (1670914187089 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (64523591651 / 2400000000000 : ℝ) with h | h
  · exact J_84_86 t h1 h
  · exact J_86_88 t h h2

lemma J_81_88 : ∀ t : ℝ, (24475480029 / 1000000000000 : ℝ) < t → t ≤ (1670914187089 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (518421798487 / 20000000000000 : ℝ) with h | h
  · exact J_81_84 t h1 h
  · exact J_84_88 t h h2

lemma J_75_88 : ∀ t : ℝ, (753189908949 / 35000000000000 : ℝ) < t → t ≤ (1670914187089 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (24475480029 / 1000000000000 : ℝ) with h | h
  · exact J_75_81 t h1 h
  · exact J_81_88 t h h2

lemma J_89_91 : ∀ t : ℝ, (424956596249 / 15000000000000 : ℝ) < t → t ≤ (175765078081 / 6000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (576246194301 / 20000000000000 : ℝ) with h | h
  · exact I_89 t h1 h
  · exact I_90 t h h2

lemma J_88_91 : ∀ t : ℝ, (1670914187089 / 60000000000000 : ℝ) < t → t ≤ (175765078081 / 6000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (424956596249 / 15000000000000 : ℝ) with h | h
  · exact I_88 t h1 h
  · exact J_89_91 t h h2

lemma J_92_94 : ∀ t : ℝ, (1786562978717 / 60000000000000 : ℝ) < t → t ≤ (1844387374531 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (37822399513 / 1250000000000 : ℝ) with h | h
  · exact I_92 t h1 h
  · exact I_93 t h h2

lemma J_91_94 : ∀ t : ℝ, (175765078081 / 6000000000000 : ℝ) < t → t ≤ (1844387374531 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1786562978717 / 60000000000000 : ℝ) with h | h
  · exact I_91 t h1 h
  · exact J_92_94 t h h2

lemma J_88_94 : ∀ t : ℝ, (1670914187089 / 60000000000000 : ℝ) < t → t ≤ (1844387374531 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (175765078081 / 6000000000000 : ℝ) with h | h
  · exact J_88_91 t h1 h
  · exact J_91_94 t h h2

lemma J_95_97 : ∀ t : ℝ, (936649786219 / 30000000000000 : ℝ) < t → t ≤ (482780992063 / 15000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (126814118023 / 4000000000000 : ℝ) with h | h
  · exact I_95 t h1 h
  · exact I_96 t h h2

lemma J_94_97 : ∀ t : ℝ, (1844387374531 / 60000000000000 : ℝ) < t → t ≤ (482780992063 / 15000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (936649786219 / 30000000000000 : ℝ) with h | h
  · exact I_94 t h1 h
  · exact J_95_97 t h h2

lemma J_97_99 : ∀ t : ℝ, (482780992063 / 15000000000000 : ℝ) < t → t ≤ (331491394011 / 10000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1960036166159 / 60000000000000 : ℝ) with h | h
  · exact I_97 t h1 h
  · exact I_98 t h h2

lemma J_99_101 : ∀ t : ℝ, (331491394011 / 10000000000000 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2017860561973 / 60000000000000 : ℝ) with h | h
  · exact I_99 t h1 h
  · exact I_100 t h h2

lemma J_97_101 : ∀ t : ℝ, (482780992063 / 15000000000000 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (331491394011 / 10000000000000 : ℝ) with h | h
  · exact J_97_99 t h1 h
  · exact J_99_101 t h h2

lemma J_94_101 : ∀ t : ℝ, (1844387374531 / 60000000000000 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (482780992063 / 15000000000000 : ℝ) with h | h
  · exact J_94_97 t h1 h
  · exact J_97_101 t h h2

lemma J_88_101 : ∀ t : ℝ, (1670914187089 / 60000000000000 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1844387374531 / 60000000000000 : ℝ) with h | h
  · exact J_88_94 t h1 h
  · exact J_94_101 t h h2

lemma J_75_101 : ∀ t : ℝ, (753189908949 / 35000000000000 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1670914187089 / 60000000000000 : ℝ) with h | h
  · exact J_75_88 t h1 h
  · exact J_88_101 t h h2

lemma J_50_101 : ∀ t : ℝ, (161070179337 / 17500000000000 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (753189908949 / 35000000000000 : ℝ) with h | h
  · exact J_50_75 t h1 h
  · exact J_75_101 t h h2

lemma J_0_101 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (51169318997 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (161070179337 / 17500000000000 : ℝ) with h | h
  · exact J_0_50 t h1 h
  · exact J_50_101 t h h2

lemma J_102_104 : ∀ t : ℝ, (6578585029523 / 192000000000000 : ℝ) < t → t ≤ (6636409425337 / 192000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (220249907581 / 6400000000000 : ℝ) with h | h
  · exact I_102 t h1 h
  · exact I_103 t h h2

lemma J_101_104 : ∀ t : ℝ, (51169318997 / 1500000000000 : ℝ) < t → t ≤ (6636409425337 / 192000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6578585029523 / 192000000000000 : ℝ) with h | h
  · exact I_101 t h1 h
  · exact J_102_104 t h h2

lemma J_105_107 : ∀ t : ℝ, (1666330405811 / 48000000000000 : ℝ) < t → t ≤ (3361573009529 / 96000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2231411273717 / 64000000000000 : ℝ) with h | h
  · exact I_105 t h1 h
  · exact I_106 t h h2

lemma J_104_107 : ∀ t : ℝ, (6636409425337 / 192000000000000 : ℝ) < t → t ≤ (3361573009529 / 96000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1666330405811 / 48000000000000 : ℝ) with h | h
  · exact I_104 t h1 h
  · exact J_105_107 t h h2

lemma J_101_107 : ∀ t : ℝ, (51169318997 / 1500000000000 : ℝ) < t → t ≤ (3361573009529 / 96000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6636409425337 / 192000000000000 : ℝ) with h | h
  · exact J_101_104 t h1 h
  · exact J_104_107 t h h2

lemma J_108_110 : ∀ t : ℝ, (1350411643393 / 38400000000000 : ℝ) < t → t ≤ (6809882612779 / 192000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (282540433953 / 8000000000000 : ℝ) with h | h
  · exact I_108 t h1 h
  · exact I_109 t h h2

lemma J_107_110 : ∀ t : ℝ, (3361573009529 / 96000000000000 : ℝ) < t → t ≤ (6809882612779 / 192000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1350411643393 / 38400000000000 : ℝ) with h | h
  · exact I_107 t h1 h
  · exact J_108_110 t h h2

lemma J_111_113 : ∀ t : ℝ, (3419397405343 / 96000000000000 : ℝ) < t → t ≤ (1159073933719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (13793238413 / 384000000000 : ℝ) with h | h
  · exact I_111 t h1 h
  · exact I_112 t h h2

lemma J_110_113 : ∀ t : ℝ, (6809882612779 / 192000000000000 : ℝ) < t → t ≤ (1159073933719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3419397405343 / 96000000000000 : ℝ) with h | h
  · exact I_110 t h1 h
  · exact J_111_113 t h h2

lemma J_107_113 : ∀ t : ℝ, (3361573009529 / 96000000000000 : ℝ) < t → t ≤ (1159073933719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6809882612779 / 192000000000000 : ℝ) with h | h
  · exact J_107_110 t h1 h
  · exact J_110_113 t h h2

lemma J_101_113 : ∀ t : ℝ, (51169318997 / 1500000000000 : ℝ) < t → t ≤ (1159073933719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3361573009529 / 96000000000000 : ℝ) with h | h
  · exact J_101_107 t h1 h
  · exact J_107_113 t h h2

lemma J_114_116 : ∀ t : ℝ, (438266749883 / 12000000000000 : ℝ) < t → t ≤ (749719381743 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1110122973661 / 30000000000000 : ℝ) with h | h
  · exact I_114 t h1 h
  · exact I_115 t h h2

lemma J_113_116 : ∀ t : ℝ, (1159073933719 / 32000000000000 : ℝ) < t → t ≤ (749719381743 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (438266749883 / 12000000000000 : ℝ) with h | h
  · exact I_113 t h1 h
  · exact J_114_116 t h h2

lemma J_117_119 : ∀ t : ℝ, (71189698223 / 1875000000000 : ℝ) < t → t ≤ (15572631593 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2306982541043 / 60000000000000 : ℝ) with h | h
  · exact I_117 t h1 h
  · exact I_118 t h h2

lemma J_116_119 : ∀ t : ℝ, (749719381743 / 20000000000000 : ℝ) < t → t ≤ (15572631593 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (71189698223 / 1875000000000 : ℝ) with h | h
  · exact I_116 t h1 h
  · exact J_117_119 t h h2

lemma J_113_119 : ∀ t : ℝ, (1159073933719 / 32000000000000 : ℝ) < t → t ≤ (15572631593 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (749719381743 / 20000000000000 : ℝ) with h | h
  · exact J_113_116 t h1 h
  · exact J_116_119 t h h2

lemma J_120_122 : ∀ t : ℝ, (2364806936857 / 60000000000000 : ℝ) < t → t ≤ (807543777557 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (598429783691 / 15000000000000 : ℝ) with h | h
  · exact I_120 t h1 h
  · exact I_121 t h h2

lemma J_119_122 : ∀ t : ℝ, (15572631593 / 400000000000 : ℝ) < t → t ≤ (807543777557 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2364806936857 / 60000000000000 : ℝ) with h | h
  · exact I_119 t h1 h
  · exact J_120_122 t h h2

lemma J_122_124 : ∀ t : ℝ, (807543777557 / 20000000000000 : ℝ) < t → t ≤ (496091145697 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1225771765289 / 30000000000000 : ℝ) with h | h
  · exact I_122 t h1 h
  · exact I_123 t h h2

lemma J_124_126 : ∀ t : ℝ, (496091145697 / 12000000000000 : ℝ) < t → t ≤ (2538280124299 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (104556996933 / 2500000000000 : ℝ) with h | h
  · exact I_124 t h1 h
  · exact I_125 t h h2

lemma J_122_126 : ∀ t : ℝ, (807543777557 / 20000000000000 : ℝ) < t → t ≤ (2538280124299 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (496091145697 / 12000000000000 : ℝ) with h | h
  · exact J_122_124 t h1 h
  · exact J_124_126 t h h2

lemma J_119_126 : ∀ t : ℝ, (15572631593 / 400000000000 : ℝ) < t → t ≤ (2538280124299 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (807543777557 / 20000000000000 : ℝ) with h | h
  · exact J_119_122 t h1 h
  · exact J_122_126 t h h2

lemma J_113_126 : ∀ t : ℝ, (1159073933719 / 32000000000000 : ℝ) < t → t ≤ (2538280124299 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15572631593 / 400000000000 : ℝ) with h | h
  · exact J_113_119 t h1 h
  · exact J_119_126 t h h2

lemma J_101_126 : ∀ t : ℝ, (51169318997 / 1500000000000 : ℝ) < t → t ≤ (2538280124299 / 60000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1159073933719 / 32000000000000 : ℝ) with h | h
  · exact J_101_113 t h1 h
  · exact J_113_126 t h h2

lemma J_127_129 : ∀ t : ℝ, (1283596161103 / 30000000000000 : ℝ) < t → t ≤ (131250835901 / 3000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (865368173371 / 20000000000000 : ℝ) with h | h
  · exact I_127 t h1 h
  · exact I_128 t h h2

lemma J_126_129 : ∀ t : ℝ, (2538280124299 / 60000000000000 : ℝ) < t → t ≤ (131250835901 / 3000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1283596161103 / 30000000000000 : ℝ) with h | h
  · exact I_126 t h1 h
  · exact J_127_129 t h h2

lemma J_130_132 : ∀ t : ℝ, (291413869709 / 6000000000000 : ℝ) < t → t ≤ (222840175691 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3336729871 / 62500000000 : ℝ) with h | h
  · exact I_130 t h1 h
  · exact I_131 t h h2

lemma J_129_132 : ∀ t : ℝ, (131250835901 / 3000000000000 : ℝ) < t → t ≤ (222840175691 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (291413869709 / 6000000000000 : ℝ) with h | h
  · exact I_129 t h1 h
  · exact J_130_132 t h h2

lemma J_126_132 : ∀ t : ℝ, (2538280124299 / 60000000000000 : ℝ) < t → t ≤ (222840175691 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (131250835901 / 3000000000000 : ℝ) with h | h
  · exact J_126_129 t h1 h
  · exact J_129_132 t h h2

lemma J_133_135 : ∀ t : ℝ, (116064819819 / 2000000000000 : ℝ) < t → t ≤ (48283820717 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (473548743223 / 8000000000000 : ℝ) with h | h
  · exact I_133 t h1 h
  · exact I_134 t h h2

lemma J_132_135 : ∀ t : ℝ, (222840175691 / 4000000000000 : ℝ) < t → t ≤ (48283820717 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (116064819819 / 2000000000000 : ℝ) with h | h
  · exact I_132 t h1 h
  · exact J_133_135 t h h2

lemma J_136_138 : ∀ t : ℝ, (492127671117 / 8000000000000 : ℝ) < t → t ≤ (4020626544459 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (62677141883 / 1000000000000 : ℝ) with h | h
  · exact I_136 t h1 h
  · exact I_137 t h h2

lemma J_135_138 : ∀ t : ℝ, (48283820717 / 800000000000 : ℝ) < t → t ≤ (4020626544459 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (492127671117 / 8000000000000 : ℝ) with h | h
  · exact I_135 t h1 h
  · exact J_136_138 t h h2

lemma J_132_138 : ∀ t : ℝ, (222840175691 / 4000000000000 : ℝ) < t → t ≤ (4020626544459 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (48283820717 / 800000000000 : ℝ) with h | h
  · exact J_132_135 t h1 h
  · exact J_135_138 t h h2

lemma J_126_138 : ∀ t : ℝ, (2538280124299 / 60000000000000 : ℝ) < t → t ≤ (4020626544459 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (222840175691 / 4000000000000 : ℝ) with h | h
  · exact J_126_132 t h1 h
  · exact J_132_138 t h h2

lemma J_139_141 : ∀ t : ℝ, (2014958004203 / 32000000000000 : ℝ) < t → t ≤ (40484949363 / 640000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4039205472353 / 64000000000000 : ℝ) with h | h
  · exact I_139 t h1 h
  · exact I_140 t h h2

lemma J_138_141 : ∀ t : ℝ, (4020626544459 / 64000000000000 : ℝ) < t → t ≤ (40484949363 / 640000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2014958004203 / 32000000000000 : ℝ) with h | h
  · exact I_138 t h1 h
  · exact J_139_141 t h h2

lemma J_142_144 : ∀ t : ℝ, (4057784400247 / 64000000000000 : ℝ) < t → t ≤ (4076363328141 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2033536932097 / 32000000000000 : ℝ) with h | h
  · exact I_142 t h1 h
  · exact I_143 t h h2

lemma J_141_144 : ∀ t : ℝ, (40484949363 / 640000000000 : ℝ) < t → t ≤ (4076363328141 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4057784400247 / 64000000000000 : ℝ) with h | h
  · exact I_141 t h1 h
  · exact J_142_144 t h h2

lemma J_138_144 : ∀ t : ℝ, (4020626544459 / 64000000000000 : ℝ) < t → t ≤ (4076363328141 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (40484949363 / 640000000000 : ℝ) with h | h
  · exact J_138_141 t h1 h
  · exact J_141_144 t h h2

lemma J_145_147 : ∀ t : ℝ, (510706599011 / 8000000000000 : ℝ) < t → t ≤ (2052115859991 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (818988451207 / 12800000000000 : ℝ) with h | h
  · exact I_145 t h1 h
  · exact I_146 t h h2

lemma J_144_147 : ∀ t : ℝ, (4076363328141 / 64000000000000 : ℝ) < t → t ≤ (2052115859991 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (510706599011 / 8000000000000 : ℝ) with h | h
  · exact I_144 t h1 h
  · exact J_145_147 t h h2

lemma J_147_149 : ∀ t : ℝ, (2052115859991 / 32000000000000 : ℝ) < t → t ≤ (1030702661969 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4113521183929 / 64000000000000 : ℝ) with h | h
  · exact I_147 t h1 h
  · exact I_148 t h h2

lemma J_149_151 : ∀ t : ℝ, (1030702661969 / 16000000000000 : ℝ) < t → t ≤ (414138957577 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4132100111823 / 64000000000000 : ℝ) with h | h
  · exact I_149 t h1 h
  · exact I_150 t h h2

lemma J_147_151 : ∀ t : ℝ, (2052115859991 / 32000000000000 : ℝ) < t → t ≤ (414138957577 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1030702661969 / 16000000000000 : ℝ) with h | h
  · exact J_147_149 t h1 h
  · exact J_149_151 t h h2

lemma J_144_151 : ∀ t : ℝ, (4076363328141 / 64000000000000 : ℝ) < t → t ≤ (414138957577 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2052115859991 / 32000000000000 : ℝ) with h | h
  · exact J_144_147 t h1 h
  · exact J_147_151 t h h2

lemma J_138_151 : ∀ t : ℝ, (4020626544459 / 64000000000000 : ℝ) < t → t ≤ (414138957577 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4076363328141 / 64000000000000 : ℝ) with h | h
  · exact J_138_144 t h1 h
  · exact J_144_151 t h h2

lemma J_126_151 : ∀ t : ℝ, (2538280124299 / 60000000000000 : ℝ) < t → t ≤ (414138957577 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4020626544459 / 64000000000000 : ℝ) with h | h
  · exact J_126_138 t h1 h
  · exact J_138_151 t h h2

lemma J_101_151 : ∀ t : ℝ, (51169318997 / 1500000000000 : ℝ) < t → t ≤ (414138957577 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2538280124299 / 60000000000000 : ℝ) with h | h
  · exact J_101_126 t h1 h
  · exact J_126_151 t h h2

lemma J_152_154 : ∀ t : ℝ, (4150679039717 / 64000000000000 : ℝ) < t → t ≤ (4169257967611 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (259998031479 / 4000000000000 : ℝ) with h | h
  · exact I_152 t h1 h
  · exact I_153 t h h2

lemma J_151_154 : ∀ t : ℝ, (414138957577 / 6400000000000 : ℝ) < t → t ≤ (4169257967611 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4150679039717 / 64000000000000 : ℝ) with h | h
  · exact I_151 t h1 h
  · exact J_152_154 t h h2

lemma J_155_157 : ∀ t : ℝ, (2089273715779 / 32000000000000 : ℝ) < t → t ≤ (1049281589863 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (837567379101 / 12800000000000 : ℝ) with h | h
  · exact I_155 t h1 h
  · exact I_156 t h h2

lemma J_154_157 : ∀ t : ℝ, (4169257967611 / 64000000000000 : ℝ) < t → t ≤ (1049281589863 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2089273715779 / 32000000000000 : ℝ) with h | h
  · exact I_154 t h1 h
  · exact J_155_157 t h h2

lemma J_151_157 : ∀ t : ℝ, (414138957577 / 6400000000000 : ℝ) < t → t ≤ (1049281589863 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4169257967611 / 64000000000000 : ℝ) with h | h
  · exact J_151_154 t h1 h
  · exact J_154_157 t h h2

lemma J_158_160 : ∀ t : ℝ, (4206415823399 / 64000000000000 : ℝ) < t → t ≤ (4224994751293 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2107852643673 / 32000000000000 : ℝ) with h | h
  · exact I_158 t h1 h
  · exact I_159 t h h2

lemma J_157_160 : ∀ t : ℝ, (1049281589863 / 16000000000000 : ℝ) < t → t ≤ (4224994751293 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4206415823399 / 64000000000000 : ℝ) with h | h
  · exact I_157 t h1 h
  · exact J_158_160 t h h2

lemma J_161_163 : ∀ t : ℝ, (105857105381 / 1600000000000 : ℝ) < t → t ≤ (2126431571567 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4243573679187 / 64000000000000 : ℝ) with h | h
  · exact I_161 t h1 h
  · exact I_162 t h h2

lemma J_160_163 : ∀ t : ℝ, (4224994751293 / 64000000000000 : ℝ) < t → t ≤ (2126431571567 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (105857105381 / 1600000000000 : ℝ) with h | h
  · exact I_160 t h1 h
  · exact J_161_163 t h h2

lemma J_157_163 : ∀ t : ℝ, (1049281589863 / 16000000000000 : ℝ) < t → t ≤ (2126431571567 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4224994751293 / 64000000000000 : ℝ) with h | h
  · exact J_157_160 t h1 h
  · exact J_160_163 t h h2

lemma J_151_163 : ∀ t : ℝ, (414138957577 / 6400000000000 : ℝ) < t → t ≤ (2126431571567 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1049281589863 / 16000000000000 : ℝ) with h | h
  · exact J_151_157 t h1 h
  · exact J_157_163 t h h2

lemma J_164_166 : ∀ t : ℝ, (4262152607081 / 64000000000000 : ℝ) < t → t ≤ (171229261399 / 2560000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1067860517757 / 16000000000000 : ℝ) with h | h
  · exact I_164 t h1 h
  · exact I_165 t h h2

lemma J_163_166 : ∀ t : ℝ, (2126431571567 / 32000000000000 : ℝ) < t → t ≤ (171229261399 / 2560000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4262152607081 / 64000000000000 : ℝ) with h | h
  · exact I_163 t h1 h
  · exact J_164_166 t h h2

lemma J_167_169 : ∀ t : ℝ, (2145010499461 / 32000000000000 : ℝ) < t → t ≤ (134643747713 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4299310462869 / 64000000000000 : ℝ) with h | h
  · exact I_167 t h1 h
  · exact I_168 t h h2

lemma J_166_169 : ∀ t : ℝ, (171229261399 / 2560000000000 : ℝ) < t → t ≤ (134643747713 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2145010499461 / 32000000000000 : ℝ) with h | h
  · exact I_166 t h1 h
  · exact J_167_169 t h h2

lemma J_163_169 : ∀ t : ℝ, (2126431571567 / 32000000000000 : ℝ) < t → t ≤ (134643747713 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (171229261399 / 2560000000000 : ℝ) with h | h
  · exact J_163_166 t h1 h
  · exact J_166_169 t h h2

lemma J_170_172 : ∀ t : ℝ, (4317889390763 / 64000000000000 : ℝ) < t → t ≤ (4336468318657 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (432717885471 / 6400000000000 : ℝ) with h | h
  · exact I_170 t h1 h
  · exact I_171 t h h2

lemma J_169_172 : ∀ t : ℝ, (134643747713 / 2000000000000 : ℝ) < t → t ≤ (4336468318657 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4317889390763 / 64000000000000 : ℝ) with h | h
  · exact I_169 t h1 h
  · exact J_170_172 t h h2

lemma J_172_174 : ∀ t : ℝ, (4336468318657 / 64000000000000 : ℝ) < t → t ≤ (4355047246551 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1086439445651 / 16000000000000 : ℝ) with h | h
  · exact I_172 t h1 h
  · exact I_173 t h h2

lemma J_174_176 : ∀ t : ℝ, (4355047246551 / 64000000000000 : ℝ) < t → t ≤ (874725234889 / 12800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2182168355249 / 32000000000000 : ℝ) with h | h
  · exact I_174 t h1 h
  · exact I_175 t h h2

lemma J_172_176 : ∀ t : ℝ, (4336468318657 / 64000000000000 : ℝ) < t → t ≤ (874725234889 / 12800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4355047246551 / 64000000000000 : ℝ) with h | h
  · exact J_172_174 t h1 h
  · exact J_174_176 t h h2

lemma J_169_176 : ∀ t : ℝ, (134643747713 / 2000000000000 : ℝ) < t → t ≤ (874725234889 / 12800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4336468318657 / 64000000000000 : ℝ) with h | h
  · exact J_169_172 t h1 h
  · exact J_172_176 t h h2

lemma J_163_176 : ∀ t : ℝ, (2126431571567 / 32000000000000 : ℝ) < t → t ≤ (874725234889 / 12800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (134643747713 / 2000000000000 : ℝ) with h | h
  · exact J_163_169 t h1 h
  · exact J_169_176 t h h2

lemma J_151_176 : ∀ t : ℝ, (414138957577 / 6400000000000 : ℝ) < t → t ≤ (874725234889 / 12800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2126431571567 / 32000000000000 : ℝ) with h | h
  · exact J_151_163 t h1 h
  · exact J_163_176 t h h2

lemma J_177_179 : ∀ t : ℝ, (547864454799 / 8000000000000 : ℝ) < t → t ≤ (2200747283143 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4392205102339 / 64000000000000 : ℝ) with h | h
  · exact I_177 t h1 h
  · exact I_178 t h h2

lemma J_176_179 : ∀ t : ℝ, (874725234889 / 12800000000000 : ℝ) < t → t ≤ (2200747283143 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (547864454799 / 8000000000000 : ℝ) with h | h
  · exact I_176 t h1 h
  · exact J_177_179 t h h2

lemma J_180_182 : ∀ t : ℝ, (4410784030233 / 64000000000000 : ℝ) < t → t ≤ (4429362958127 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (221003674709 / 3200000000000 : ℝ) with h | h
  · exact I_180 t h1 h
  · exact I_181 t h h2

lemma J_179_182 : ∀ t : ℝ, (2200747283143 / 32000000000000 : ℝ) < t → t ≤ (4429362958127 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4410784030233 / 64000000000000 : ℝ) with h | h
  · exact I_179 t h1 h
  · exact J_180_182 t h h2

lemma J_176_182 : ∀ t : ℝ, (874725234889 / 12800000000000 : ℝ) < t → t ≤ (4429362958127 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2200747283143 / 32000000000000 : ℝ) with h | h
  · exact J_176_179 t h1 h
  · exact J_179_182 t h h2

lemma J_183_185 : ∀ t : ℝ, (2219326211037 / 32000000000000 : ℝ) < t → t ≤ (278576959373 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4447941886021 / 64000000000000 : ℝ) with h | h
  · exact I_183 t h1 h
  · exact I_184 t h h2

lemma J_182_185 : ∀ t : ℝ, (4429362958127 / 64000000000000 : ℝ) < t → t ≤ (278576959373 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2219326211037 / 32000000000000 : ℝ) with h | h
  · exact I_182 t h1 h
  · exact J_183_185 t h h2

lemma J_185_187 : ∀ t : ℝ, (278576959373 / 4000000000000 : ℝ) < t → t ≤ (2237905138931 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (893304162783 / 12800000000000 : ℝ) with h | h
  · exact I_185 t h1 h
  · exact I_186 t h h2

lemma J_187_189 : ∀ t : ℝ, (2237905138931 / 32000000000000 : ℝ) < t → t ≤ (1123597301439 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4485099741809 / 64000000000000 : ℝ) with h | h
  · exact I_187 t h1 h
  · exact I_188 t h h2

lemma J_185_189 : ∀ t : ℝ, (278576959373 / 4000000000000 : ℝ) < t → t ≤ (1123597301439 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2237905138931 / 32000000000000 : ℝ) with h | h
  · exact J_185_187 t h1 h
  · exact J_187_189 t h h2

lemma J_182_189 : ∀ t : ℝ, (4429362958127 / 64000000000000 : ℝ) < t → t ≤ (1123597301439 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (278576959373 / 4000000000000 : ℝ) with h | h
  · exact J_182_185 t h1 h
  · exact J_185_189 t h h2

lemma J_176_189 : ∀ t : ℝ, (874725234889 / 12800000000000 : ℝ) < t → t ≤ (1123597301439 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4429362958127 / 64000000000000 : ℝ) with h | h
  · exact J_176_182 t h1 h
  · exact J_182_189 t h h2

lemma J_190_192 : ∀ t : ℝ, (4503678669703 / 64000000000000 : ℝ) < t → t ≤ (4522257597597 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (90259362673 / 1280000000000 : ℝ) with h | h
  · exact I_190 t h1 h
  · exact I_191 t h h2

lemma J_189_192 : ∀ t : ℝ, (1123597301439 / 16000000000000 : ℝ) < t → t ≤ (4522257597597 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4503678669703 / 64000000000000 : ℝ) with h | h
  · exact I_189 t h1 h
  · exact J_190_192 t h h2

lemma J_193_195 : ∀ t : ℝ, (566443382693 / 8000000000000 : ℝ) < t → t ≤ (2275062994719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4540836525491 / 64000000000000 : ℝ) with h | h
  · exact I_193 t h1 h
  · exact I_194 t h h2

lemma J_192_195 : ∀ t : ℝ, (4522257597597 / 64000000000000 : ℝ) < t → t ≤ (2275062994719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (566443382693 / 8000000000000 : ℝ) with h | h
  · exact I_192 t h1 h
  · exact J_193_195 t h h2

lemma J_189_195 : ∀ t : ℝ, (1123597301439 / 16000000000000 : ℝ) < t → t ≤ (2275062994719 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4522257597597 / 64000000000000 : ℝ) with h | h
  · exact J_189_192 t h1 h
  · exact J_192_195 t h h2

lemma J_196_198 : ∀ t : ℝ, (911883090677 / 12800000000000 : ℝ) < t → t ≤ (4577994381279 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1142176229333 / 16000000000000 : ℝ) with h | h
  · exact I_196 t h1 h
  · exact I_197 t h h2

lemma J_195_198 : ∀ t : ℝ, (2275062994719 / 32000000000000 : ℝ) < t → t ≤ (4577994381279 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (911883090677 / 12800000000000 : ℝ) with h | h
  · exact I_195 t h1 h
  · exact J_196_198 t h h2

lemma J_198_200 : ∀ t : ℝ, (4577994381279 / 64000000000000 : ℝ) < t → t ≤ (4596573309173 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2293641922613 / 32000000000000 : ℝ) with h | h
  · exact I_198 t h1 h
  · exact I_199 t h h2

lemma J_200_202 : ∀ t : ℝ, (4596573309173 / 64000000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7196660583 / 100000000000 : ℝ) with h | h
  · exact I_200 t h1 h
  · exact I_201 t h h2

lemma J_198_202 : ∀ t : ℝ, (4577994381279 / 64000000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4596573309173 / 64000000000000 : ℝ) with h | h
  · exact J_198_200 t h1 h
  · exact J_200_202 t h h2

lemma J_195_202 : ∀ t : ℝ, (2275062994719 / 32000000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4577994381279 / 64000000000000 : ℝ) with h | h
  · exact J_195_198 t h1 h
  · exact J_198_202 t h h2

lemma J_189_202 : ∀ t : ℝ, (1123597301439 / 16000000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2275062994719 / 32000000000000 : ℝ) with h | h
  · exact J_189_195 t h1 h
  · exact J_195_202 t h h2

lemma J_176_202 : ∀ t : ℝ, (874725234889 / 12800000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1123597301439 / 16000000000000 : ℝ) with h | h
  · exact J_176_189 t h1 h
  · exact J_189_202 t h h2

lemma J_151_202 : ∀ t : ℝ, (414138957577 / 6400000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (874725234889 / 12800000000000 : ℝ) with h | h
  · exact J_151_176 t h1 h
  · exact J_176_202 t h h2

lemma J_101_202 : ∀ t : ℝ, (51169318997 / 1500000000000 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (414138957577 / 6400000000000 : ℝ) with h | h
  · exact J_101_151 t h1 h
  · exact J_151_202 t h h2

lemma J_0_202 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (4615152237067 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (51169318997 / 1500000000000 : ℝ) with h | h
  · exact J_0_101 t h1 h
  · exact J_101_202 t h h2

lemma J_203_205 : ∀ t : ℝ, (2312220850507 / 32000000000000 : ℝ) < t → t ≤ (1160755157227 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4633731164961 / 64000000000000 : ℝ) with h | h
  · exact I_203 t h1 h
  · exact I_204 t h h2

lemma J_202_205 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (1160755157227 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2312220850507 / 32000000000000 : ℝ) with h | h
  · exact I_202 t h1 h
  · exact J_203_205 t h h2

lemma J_206_208 : ∀ t : ℝ, (930462018571 / 12800000000000 : ℝ) < t → t ≤ (4670889020749 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2330799778401 / 32000000000000 : ℝ) with h | h
  · exact I_206 t h1 h
  · exact I_207 t h h2

lemma J_205_208 : ∀ t : ℝ, (1160755157227 / 16000000000000 : ℝ) < t → t ≤ (4670889020749 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (930462018571 / 12800000000000 : ℝ) with h | h
  · exact I_205 t h1 h
  · exact J_206_208 t h h2

lemma J_202_208 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (4670889020749 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1160755157227 / 16000000000000 : ℝ) with h | h
  · exact J_202_205 t h1 h
  · exact J_205_208 t h h2

lemma J_209_211 : ∀ t : ℝ, (585022310587 / 8000000000000 : ℝ) < t → t ≤ (469875741259 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4689467948643 / 64000000000000 : ℝ) with h | h
  · exact I_209 t h1 h
  · exact I_210 t h h2

lemma J_208_211 : ∀ t : ℝ, (4670889020749 / 64000000000000 : ℝ) < t → t ≤ (469875741259 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (585022310587 / 8000000000000 : ℝ) with h | h
  · exact I_208 t h1 h
  · exact J_209_211 t h h2

lemma J_212_214 : ∀ t : ℝ, (4708046876537 / 64000000000000 : ℝ) < t → t ≤ (297155887267 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1179334085121 / 16000000000000 : ℝ) with h | h
  · exact I_212 t h1 h
  · exact I_213 t h h2

lemma J_211_214 : ∀ t : ℝ, (469875741259 / 6400000000000 : ℝ) < t → t ≤ (297155887267 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4708046876537 / 64000000000000 : ℝ) with h | h
  · exact I_211 t h1 h
  · exact J_212_214 t h h2

lemma J_208_214 : ∀ t : ℝ, (4670889020749 / 64000000000000 : ℝ) < t → t ≤ (297155887267 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (469875741259 / 6400000000000 : ℝ) with h | h
  · exact J_208_211 t h1 h
  · exact J_211_214 t h h2

lemma J_202_214 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (297155887267 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4670889020749 / 64000000000000 : ℝ) with h | h
  · exact J_202_208 t h1 h
  · exact J_208_214 t h h2

lemma J_215_217 : ∀ t : ℝ, (153222675607 / 2000000000000 : ℝ) < t → t ≤ (81256069777 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (315734815161 / 4000000000000 : ℝ) with h | h
  · exact I_215 t h1 h
  · exact I_216 t h h2

lemma J_214_217 : ∀ t : ℝ, (297155887267 / 4000000000000 : ℝ) < t → t ≤ (81256069777 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (153222675607 / 2000000000000 : ℝ) with h | h
  · exact I_214 t h1 h
  · exact J_215_217 t h h2

lemma J_218_220 : ∀ t : ℝ, (171801603501 / 2000000000000 : ℝ) < t → t ≤ (1851439740921 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (22636383431 / 250000000000 : ℝ) with h | h
  · exact I_218 t h1 h
  · exact I_219 t h h2

lemma J_217_220 : ∀ t : ℝ, (81256069777 / 1000000000000 : ℝ) < t → t ≤ (1851439740921 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (171801603501 / 2000000000000 : ℝ) with h | h
  · exact I_217 t h1 h
  · exact J_218_220 t h h2

lemma J_214_220 : ∀ t : ℝ, (297155887267 / 4000000000000 : ℝ) < t → t ≤ (1851439740921 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (81256069777 / 1000000000000 : ℝ) with h | h
  · exact J_214_217 t h1 h
  · exact J_217_220 t h h2

lemma J_221_223 : ∀ t : ℝ, (945984403681 / 10000000000000 : ℝ) < t → t ≤ (493256735061 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1932497873803 / 20000000000000 : ℝ) with h | h
  · exact I_221 t h1 h
  · exact I_222 t h h2

lemma J_220_223 : ∀ t : ℝ, (1851439740921 / 20000000000000 : ℝ) < t → t ≤ (493256735061 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (945984403681 / 10000000000000 : ℝ) with h | h
  · exact I_220 t h1 h
  · exact J_221_223 t h h2

lemma J_223_225 : ∀ t : ℝ, (493256735061 / 5000000000000 : ℝ) < t → t ≤ (15824744588393 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6321792022069 / 64000000000000 : ℝ) with h | h
  · exact I_223 t h1 h
  · exact I_224 t h h2

lemma J_225_227 : ∀ t : ℝ, (15824744588393 / 160000000000000 : ℝ) < t → t ≤ (7932636827417 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31690018243227 / 320000000000000 : ℝ) with h | h
  · exact I_225 t h1 h
  · exact I_226 t h h2

lemma J_223_227 : ∀ t : ℝ, (493256735061 / 5000000000000 : ℝ) < t → t ≤ (7932636827417 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15824744588393 / 160000000000000 : ℝ) with h | h
  · exact J_223_225 t h1 h
  · exact J_225_227 t h h2

lemma J_220_227 : ∀ t : ℝ, (1851439740921 / 20000000000000 : ℝ) < t → t ≤ (7932636827417 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (493256735061 / 5000000000000 : ℝ) with h | h
  · exact J_220_223 t h1 h
  · exact J_223_227 t h h2

lemma J_214_227 : ∀ t : ℝ, (297155887267 / 4000000000000 : ℝ) < t → t ≤ (7932636827417 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1851439740921 / 20000000000000 : ℝ) with h | h
  · exact J_214_220 t h1 h
  · exact J_220_227 t h h2

lemma J_202_227 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (7932636827417 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (297155887267 / 4000000000000 : ℝ) with h | h
  · exact J_202_214 t h1 h
  · exact J_214_227 t h h2

lemma J_228_230 : ∀ t : ℝ, (31771076376109 / 320000000000000 : ℝ) < t → t ≤ (31852134508991 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (636232108851 / 6400000000000 : ℝ) with h | h
  · exact I_228 t h1 h
  · exact I_229 t h h2

lemma J_227_230 : ∀ t : ℝ, (7932636827417 / 80000000000000 : ℝ) < t → t ≤ (31852134508991 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31771076376109 / 320000000000000 : ℝ) with h | h
  · exact I_227 t h1 h
  · exact J_228_230 t h h2

lemma J_231_233 : ∀ t : ℝ, (3986582946929 / 40000000000000 : ℝ) < t → t ≤ (15986860854157 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31933192641873 / 320000000000000 : ℝ) with h | h
  · exact I_231 t h1 h
  · exact I_232 t h h2

lemma J_230_233 : ∀ t : ℝ, (31852134508991 / 320000000000000 : ℝ) < t → t ≤ (15986860854157 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3986582946929 / 40000000000000 : ℝ) with h | h
  · exact I_230 t h1 h
  · exact J_231_233 t h h2

lemma J_227_233 : ∀ t : ℝ, (7932636827417 / 80000000000000 : ℝ) < t → t ≤ (15986860854157 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31852134508991 / 320000000000000 : ℝ) with h | h
  · exact J_227_230 t h1 h
  · exact J_230_233 t h h2

lemma J_234_236 : ∀ t : ℝ, (6402850154951 / 64000000000000 : ℝ) < t → t ≤ (32095308907637 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8013694960299 / 80000000000000 : ℝ) with h | h
  · exact I_234 t h1 h
  · exact I_235 t h h2

lemma J_233_236 : ∀ t : ℝ, (15986860854157 / 160000000000000 : ℝ) < t → t ≤ (32095308907637 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6402850154951 / 64000000000000 : ℝ) with h | h
  · exact I_233 t h1 h
  · exact J_234_236 t h h2

lemma J_237_239 : ∀ t : ℝ, (16067918987039 / 160000000000000 : ℝ) < t → t ≤ (402711201337 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32176367040519 / 320000000000000 : ℝ) with h | h
  · exact I_237 t h1 h
  · exact I_238 t h h2

lemma J_236_239 : ∀ t : ℝ, (32095308907637 / 320000000000000 : ℝ) < t → t ≤ (402711201337 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16067918987039 / 160000000000000 : ℝ) with h | h
  · exact I_236 t h1 h
  · exact J_237_239 t h h2

lemma J_233_239 : ∀ t : ℝ, (15986860854157 / 160000000000000 : ℝ) < t → t ≤ (402711201337 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32095308907637 / 320000000000000 : ℝ) with h | h
  · exact J_233_236 t h1 h
  · exact J_236_239 t h h2

lemma J_227_239 : ∀ t : ℝ, (7932636827417 / 80000000000000 : ℝ) < t → t ≤ (402711201337 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15986860854157 / 160000000000000 : ℝ) with h | h
  · exact J_227_233 t h1 h
  · exact J_233_239 t h h2

lemma J_240_242 : ∀ t : ℝ, (32257425173401 / 320000000000000 : ℝ) < t → t ≤ (32338483306283 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16148977119921 / 160000000000000 : ℝ) with h | h
  · exact I_240 t h1 h
  · exact I_241 t h h2

lemma J_239_242 : ∀ t : ℝ, (402711201337 / 4000000000000 : ℝ) < t → t ≤ (32338483306283 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32257425173401 / 320000000000000 : ℝ) with h | h
  · exact I_239 t h1 h
  · exact J_240_242 t h h2

lemma J_243_245 : ∀ t : ℝ, (8094753093181 / 80000000000000 : ℝ) < t → t ≤ (16230035252803 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6483908287833 / 64000000000000 : ℝ) with h | h
  · exact I_243 t h1 h
  · exact I_244 t h h2

lemma J_242_245 : ∀ t : ℝ, (32338483306283 / 320000000000000 : ℝ) < t → t ≤ (16230035252803 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8094753093181 / 80000000000000 : ℝ) with h | h
  · exact I_242 t h1 h
  · exact J_243_245 t h h2

lemma J_239_245 : ∀ t : ℝ, (402711201337 / 4000000000000 : ℝ) < t → t ≤ (16230035252803 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32338483306283 / 320000000000000 : ℝ) with h | h
  · exact J_239_242 t h1 h
  · exact J_242_245 t h h2

lemma J_246_248 : ∀ t : ℝ, (32500599572047 / 320000000000000 : ℝ) < t → t ≤ (32581657704929 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4067641079811 / 40000000000000 : ℝ) with h | h
  · exact I_246 t h1 h
  · exact I_247 t h h2

lemma J_245_248 : ∀ t : ℝ, (16230035252803 / 160000000000000 : ℝ) < t → t ≤ (32581657704929 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32500599572047 / 320000000000000 : ℝ) with h | h
  · exact I_245 t h1 h
  · exact J_246_248 t h h2

lemma J_248_250 : ∀ t : ℝ, (32581657704929 / 320000000000000 : ℝ) < t → t ≤ (32662715837811 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3262218677137 / 32000000000000 : ℝ) with h | h
  · exact I_248 t h1 h
  · exact I_249 t h h2

lemma J_250_252 : ∀ t : ℝ, (32662715837811 / 320000000000000 : ℝ) < t → t ≤ (32743773970693 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8175811226063 / 80000000000000 : ℝ) with h | h
  · exact I_250 t h1 h
  · exact I_251 t h h2

lemma J_248_252 : ∀ t : ℝ, (32581657704929 / 320000000000000 : ℝ) < t → t ≤ (32743773970693 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32662715837811 / 320000000000000 : ℝ) with h | h
  · exact J_248_250 t h1 h
  · exact J_250_252 t h h2

lemma J_245_252 : ∀ t : ℝ, (16230035252803 / 160000000000000 : ℝ) < t → t ≤ (32743773970693 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32581657704929 / 320000000000000 : ℝ) with h | h
  · exact J_245_248 t h1 h
  · exact J_248_252 t h h2

lemma J_239_252 : ∀ t : ℝ, (402711201337 / 4000000000000 : ℝ) < t → t ≤ (32743773970693 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16230035252803 / 160000000000000 : ℝ) with h | h
  · exact J_239_245 t h1 h
  · exact J_245_252 t h h2

lemma J_227_252 : ∀ t : ℝ, (7932636827417 / 80000000000000 : ℝ) < t → t ≤ (32743773970693 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (402711201337 / 4000000000000 : ℝ) with h | h
  · exact J_227_239 t h1 h
  · exact J_239_252 t h h2

lemma J_202_252 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (32743773970693 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7932636827417 / 80000000000000 : ℝ) with h | h
  · exact J_202_227 t h1 h
  · exact J_227_252 t h h2

lemma J_253_255 : ∀ t : ℝ, (16392151518567 / 160000000000000 : ℝ) < t → t ≤ (1027042536563 / 10000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1312993284143 / 12800000000000 : ℝ) with h | h
  · exact I_253 t h1 h
  · exact I_254 t h h2

lemma J_252_255 : ∀ t : ℝ, (32743773970693 / 320000000000000 : ℝ) < t → t ≤ (1027042536563 / 10000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16392151518567 / 160000000000000 : ℝ) with h | h
  · exact I_252 t h1 h
  · exact J_253_255 t h h2

lemma J_256_258 : ∀ t : ℝ, (32905890236457 / 320000000000000 : ℝ) < t → t ≤ (32986948369339 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16473209651449 / 160000000000000 : ℝ) with h | h
  · exact I_256 t h1 h
  · exact I_257 t h h2

lemma J_255_258 : ∀ t : ℝ, (1027042536563 / 10000000000000 : ℝ) < t → t ≤ (32986948369339 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32905890236457 / 320000000000000 : ℝ) with h | h
  · exact I_255 t h1 h
  · exact J_256_258 t h h2

lemma J_252_258 : ∀ t : ℝ, (32743773970693 / 320000000000000 : ℝ) < t → t ≤ (32986948369339 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1027042536563 / 10000000000000 : ℝ) with h | h
  · exact J_252_255 t h1 h
  · exact J_255_258 t h h2

lemma J_259_261 : ∀ t : ℝ, (1651373871789 / 16000000000000 : ℝ) < t → t ≤ (16554267784331 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33068006502221 / 320000000000000 : ℝ) with h | h
  · exact I_259 t h1 h
  · exact I_260 t h h2

lemma J_258_261 : ∀ t : ℝ, (32986948369339 / 320000000000000 : ℝ) < t → t ≤ (16554267784331 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1651373871789 / 16000000000000 : ℝ) with h | h
  · exact I_258 t h1 h
  · exact J_259_261 t h h2

lemma J_262_264 : ∀ t : ℝ, (33149064635103 / 320000000000000 : ℝ) < t → t ≤ (6646024553597 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4148699212693 / 40000000000000 : ℝ) with h | h
  · exact I_262 t h1 h
  · exact I_263 t h h2

lemma J_261_264 : ∀ t : ℝ, (16554267784331 / 160000000000000 : ℝ) < t → t ≤ (6646024553597 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33149064635103 / 320000000000000 : ℝ) with h | h
  · exact I_261 t h1 h
  · exact J_262_264 t h h2

lemma J_258_264 : ∀ t : ℝ, (32986948369339 / 320000000000000 : ℝ) < t → t ≤ (6646024553597 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16554267784331 / 160000000000000 : ℝ) with h | h
  · exact J_258_261 t h1 h
  · exact J_261_264 t h h2

lemma J_252_264 : ∀ t : ℝ, (32743773970693 / 320000000000000 : ℝ) < t → t ≤ (6646024553597 / 64000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32986948369339 / 320000000000000 : ℝ) with h | h
  · exact J_252_258 t h1 h
  · exact J_258_264 t h h2

lemma J_265_267 : ∀ t : ℝ, (16635325917213 / 160000000000000 : ℝ) < t → t ≤ (8337927491827 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33311180900867 / 320000000000000 : ℝ) with h | h
  · exact I_265 t h1 h
  · exact I_266 t h h2

lemma J_264_267 : ∀ t : ℝ, (6646024553597 / 64000000000000 : ℝ) < t → t ≤ (8337927491827 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16635325917213 / 160000000000000 : ℝ) with h | h
  · exact I_264 t h1 h
  · exact J_265_267 t h h2

lemma J_268_270 : ∀ t : ℝ, (33392239033749 / 320000000000000 : ℝ) < t → t ≤ (33473297166631 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3343276810019 / 32000000000000 : ℝ) with h | h
  · exact I_268 t h1 h
  · exact I_269 t h h2

lemma J_267_270 : ∀ t : ℝ, (8337927491827 / 80000000000000 : ℝ) < t → t ≤ (33473297166631 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33392239033749 / 320000000000000 : ℝ) with h | h
  · exact I_267 t h1 h
  · exact J_268_270 t h h2

lemma J_264_270 : ∀ t : ℝ, (6646024553597 / 64000000000000 : ℝ) < t → t ≤ (33473297166631 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8337927491827 / 80000000000000 : ℝ) with h | h
  · exact J_264_267 t h1 h
  · exact J_267_270 t h h2

lemma J_271_273 : ∀ t : ℝ, (2094614139567 / 20000000000000 : ℝ) < t → t ≤ (16797442182977 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33554355299513 / 320000000000000 : ℝ) with h | h
  · exact I_271 t h1 h
  · exact I_272 t h h2

lemma J_270_273 : ∀ t : ℝ, (33473297166631 / 320000000000000 : ℝ) < t → t ≤ (16797442182977 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2094614139567 / 20000000000000 : ℝ) with h | h
  · exact I_270 t h1 h
  · exact J_271_273 t h h2

lemma J_273_275 : ∀ t : ℝ, (16797442182977 / 160000000000000 : ℝ) < t → t ≤ (8418985624709 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6727082686479 / 64000000000000 : ℝ) with h | h
  · exact I_273 t h1 h
  · exact I_274 t h h2

lemma J_275_277 : ∀ t : ℝ, (8418985624709 / 80000000000000 : ℝ) < t → t ≤ (16878500315859 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33716471565277 / 320000000000000 : ℝ) with h | h
  · exact I_275 t h1 h
  · exact I_276 t h h2

lemma J_273_277 : ∀ t : ℝ, (16797442182977 / 160000000000000 : ℝ) < t → t ≤ (16878500315859 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8418985624709 / 80000000000000 : ℝ) with h | h
  · exact J_273_275 t h1 h
  · exact J_275_277 t h h2

lemma J_270_277 : ∀ t : ℝ, (33473297166631 / 320000000000000 : ℝ) < t → t ≤ (16878500315859 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16797442182977 / 160000000000000 : ℝ) with h | h
  · exact J_270_273 t h1 h
  · exact J_273_277 t h h2

lemma J_264_277 : ∀ t : ℝ, (6646024553597 / 64000000000000 : ℝ) < t → t ≤ (16878500315859 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33473297166631 / 320000000000000 : ℝ) with h | h
  · exact J_264_270 t h1 h
  · exact J_270_277 t h h2

lemma J_252_277 : ∀ t : ℝ, (32743773970693 / 320000000000000 : ℝ) < t → t ≤ (16878500315859 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6646024553597 / 64000000000000 : ℝ) with h | h
  · exact J_252_264 t h1 h
  · exact J_264_277 t h h2

lemma J_278_280 : ∀ t : ℝ, (33797529698159 / 320000000000000 : ℝ) < t → t ≤ (33878587831041 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (169190293823 / 1600000000000 : ℝ) with h | h
  · exact I_278 t h1 h
  · exact I_279 t h h2

lemma J_277_280 : ∀ t : ℝ, (16878500315859 / 160000000000000 : ℝ) < t → t ≤ (33878587831041 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33797529698159 / 320000000000000 : ℝ) with h | h
  · exact I_277 t h1 h
  · exact J_278_280 t h h2

lemma J_281_283 : ∀ t : ℝ, (16959558448741 / 160000000000000 : ℝ) < t → t ≤ (8500043757591 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33959645963923 / 320000000000000 : ℝ) with h | h
  · exact I_281 t h1 h
  · exact I_282 t h h2

lemma J_280_283 : ∀ t : ℝ, (33878587831041 / 320000000000000 : ℝ) < t → t ≤ (8500043757591 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16959558448741 / 160000000000000 : ℝ) with h | h
  · exact I_280 t h1 h
  · exact J_281_283 t h h2

lemma J_277_283 : ∀ t : ℝ, (16878500315859 / 160000000000000 : ℝ) < t → t ≤ (8500043757591 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33878587831041 / 320000000000000 : ℝ) with h | h
  · exact J_277_280 t h1 h
  · exact J_280_283 t h h2

lemma J_284_286 : ∀ t : ℝ, (6808140819361 / 64000000000000 : ℝ) < t → t ≤ (34121762229687 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17040616581623 / 160000000000000 : ℝ) with h | h
  · exact I_284 t h1 h
  · exact I_285 t h h2

lemma J_283_286 : ∀ t : ℝ, (8500043757591 / 80000000000000 : ℝ) < t → t ≤ (34121762229687 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6808140819361 / 64000000000000 : ℝ) with h | h
  · exact I_283 t h1 h
  · exact J_284_286 t h h2

lemma J_286_288 : ∀ t : ℝ, (34121762229687 / 320000000000000 : ℝ) < t → t ≤ (34202820362569 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (266892900751 / 2500000000000 : ℝ) with h | h
  · exact I_286 t h1 h
  · exact I_287 t h h2

lemma J_288_290 : ∀ t : ℝ, (34202820362569 / 320000000000000 : ℝ) < t → t ≤ (34283878495451 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3424334942901 / 32000000000000 : ℝ) with h | h
  · exact I_288 t h1 h
  · exact I_289 t h h2

lemma J_286_290 : ∀ t : ℝ, (34121762229687 / 320000000000000 : ℝ) < t → t ≤ (34283878495451 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34202820362569 / 320000000000000 : ℝ) with h | h
  · exact J_286_288 t h1 h
  · exact J_288_290 t h h2

lemma J_283_290 : ∀ t : ℝ, (8500043757591 / 80000000000000 : ℝ) < t → t ≤ (34283878495451 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34121762229687 / 320000000000000 : ℝ) with h | h
  · exact J_283_286 t h1 h
  · exact J_286_290 t h h2

lemma J_277_290 : ∀ t : ℝ, (16878500315859 / 160000000000000 : ℝ) < t → t ≤ (34283878495451 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8500043757591 / 80000000000000 : ℝ) with h | h
  · exact J_277_283 t h1 h
  · exact J_283_290 t h h2

lemma J_291_293 : ∀ t : ℝ, (8581101890473 / 80000000000000 : ℝ) < t → t ≤ (17202732847387 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34364936628333 / 320000000000000 : ℝ) with h | h
  · exact I_291 t h1 h
  · exact I_292 t h h2

lemma J_290_293 : ∀ t : ℝ, (34283878495451 / 320000000000000 : ℝ) < t → t ≤ (17202732847387 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8581101890473 / 80000000000000 : ℝ) with h | h
  · exact I_290 t h1 h
  · exact J_291_293 t h h2

lemma J_294_296 : ∀ t : ℝ, (6889198952243 / 64000000000000 : ℝ) < t → t ≤ (34527052894097 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4310815478457 / 40000000000000 : ℝ) with h | h
  · exact I_294 t h1 h
  · exact I_295 t h h2

lemma J_293_296 : ∀ t : ℝ, (17202732847387 / 160000000000000 : ℝ) < t → t ≤ (34527052894097 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6889198952243 / 64000000000000 : ℝ) with h | h
  · exact I_293 t h1 h
  · exact J_294_296 t h h2

lemma J_290_296 : ∀ t : ℝ, (34283878495451 / 320000000000000 : ℝ) < t → t ≤ (34527052894097 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17202732847387 / 160000000000000 : ℝ) with h | h
  · exact J_290_293 t h1 h
  · exact J_293_296 t h h2

lemma J_297_299 : ∀ t : ℝ, (17283790980269 / 160000000000000 : ℝ) < t → t ≤ (1732432004671 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34608111026979 / 320000000000000 : ℝ) with h | h
  · exact I_297 t h1 h
  · exact I_298 t h h2

lemma J_296_299 : ∀ t : ℝ, (34527052894097 / 320000000000000 : ℝ) < t → t ≤ (1732432004671 / 16000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17283790980269 / 160000000000000 : ℝ) with h | h
  · exact I_296 t h1 h
  · exact J_297_299 t h h2

lemma J_299_301 : ∀ t : ℝ, (1732432004671 / 16000000000000 : ℝ) < t → t ≤ (17364849113151 / 160000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34689169159861 / 320000000000000 : ℝ) with h | h
  · exact I_299 t h1 h
  · exact I_300 t h h2

lemma J_301_303 : ∀ t : ℝ, (17364849113151 / 160000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34770227292743 / 320000000000000 : ℝ) with h | h
  · exact I_301 t h1 h
  · exact I_302 t h h2

lemma J_299_303 : ∀ t : ℝ, (1732432004671 / 16000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17364849113151 / 160000000000000 : ℝ) with h | h
  · exact J_299_301 t h1 h
  · exact J_301_303 t h h2

lemma J_296_303 : ∀ t : ℝ, (34527052894097 / 320000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1732432004671 / 16000000000000 : ℝ) with h | h
  · exact J_296_299 t h1 h
  · exact J_299_303 t h h2

lemma J_290_303 : ∀ t : ℝ, (34283878495451 / 320000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34527052894097 / 320000000000000 : ℝ) with h | h
  · exact J_290_296 t h1 h
  · exact J_296_303 t h h2

lemma J_277_303 : ∀ t : ℝ, (16878500315859 / 160000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34283878495451 / 320000000000000 : ℝ) with h | h
  · exact J_277_290 t h1 h
  · exact J_290_303 t h h2

lemma J_252_303 : ∀ t : ℝ, (32743773970693 / 320000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16878500315859 / 160000000000000 : ℝ) with h | h
  · exact J_252_277 t h1 h
  · exact J_277_303 t h h2

lemma J_202_303 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (2175672272449 / 20000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32743773970693 / 320000000000000 : ℝ) with h | h
  · exact J_202_252 t h1 h
  · exact J_252_303 t h h2

lemma J_304_306 : ∀ t : ℝ, (55762056681 / 512000000000 : ℝ) < t → t ≤ (34932343558507 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17445907246033 / 160000000000000 : ℝ) with h | h
  · exact I_304 t h1 h
  · exact I_305 t h h2

lemma J_303_306 : ∀ t : ℝ, (2175672272449 / 20000000000000 : ℝ) < t → t ≤ (34932343558507 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (55762056681 / 512000000000 : ℝ) with h | h
  · exact I_303 t h1 h
  · exact J_304_306 t h h2

lemma J_307_309 : ∀ t : ℝ, (8743218156237 / 80000000000000 : ℝ) < t → t ≤ (3505393075783 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35013401691389 / 320000000000000 : ℝ) with h | h
  · exact I_307 t h1 h
  · exact I_308 t h h2

lemma J_306_309 : ∀ t : ℝ, (34932343558507 / 320000000000000 : ℝ) < t → t ≤ (3505393075783 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8743218156237 / 80000000000000 : ℝ) with h | h
  · exact I_306 t h1 h
  · exact J_307_309 t h h2

lemma J_303_309 : ∀ t : ℝ, (2175672272449 / 20000000000000 : ℝ) < t → t ≤ (3505393075783 / 32000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34932343558507 / 320000000000000 : ℝ) with h | h
  · exact J_303_306 t h1 h
  · exact J_306_309 t h h2

lemma J_310_312 : ∀ t : ℝ, (35094459824271 / 320000000000000 : ℝ) < t → t ≤ (35175517957153 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4391873611339 / 40000000000000 : ℝ) with h | h
  · exact I_310 t h1 h
  · exact I_311 t h h2

lemma J_309_312 : ∀ t : ℝ, (3505393075783 / 32000000000000 : ℝ) < t → t ≤ (35175517957153 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35094459824271 / 320000000000000 : ℝ) with h | h
  · exact I_309 t h1 h
  · exact J_310_312 t h h2

lemma J_313_315 : ∀ t : ℝ, (17608023511797 / 160000000000000 : ℝ) < t → t ≤ (8824276289119 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7051315218007 / 64000000000000 : ℝ) with h | h
  · exact I_313 t h1 h
  · exact I_314 t h h2

lemma J_312_315 : ∀ t : ℝ, (35175517957153 / 320000000000000 : ℝ) < t → t ≤ (8824276289119 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17608023511797 / 160000000000000 : ℝ) with h | h
  · exact I_312 t h1 h
  · exact J_313_315 t h h2

lemma J_309_315 : ∀ t : ℝ, (3505393075783 / 32000000000000 : ℝ) < t → t ≤ (8824276289119 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35175517957153 / 320000000000000 : ℝ) with h | h
  · exact J_309_312 t h1 h
  · exact J_312_315 t h h2

lemma J_303_315 : ∀ t : ℝ, (2175672272449 / 20000000000000 : ℝ) < t → t ≤ (8824276289119 / 80000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3505393075783 / 32000000000000 : ℝ) with h | h
  · exact J_303_309 t h1 h
  · exact J_309_315 t h h2

lemma J_316_318 : ∀ t : ℝ, (35337634222917 / 320000000000000 : ℝ) < t → t ≤ (35418692355799 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17689081644679 / 160000000000000 : ℝ) with h | h
  · exact I_316 t h1 h
  · exact I_317 t h h2

lemma J_315_318 : ∀ t : ℝ, (8824276289119 / 80000000000000 : ℝ) < t → t ≤ (35418692355799 / 320000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35337634222917 / 320000000000000 : ℝ) with h | h
  · exact I_315 t h1 h
  · exact J_316_318 t h h2

lemma J_319_321 : ∀ t : ℝ, (221620133889 / 2000000000000 : ℝ) < t → t ≤ (574314867943 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2256730405331 / 20000000000000 : ℝ) with h | h
  · exact I_319 t h1 h
  · exact I_320 t h h2

lemma J_318_321 : ∀ t : ℝ, (35418692355799 / 320000000000000 : ℝ) < t → t ≤ (574314867943 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (221620133889 / 2000000000000 : ℝ) with h | h
  · exact I_318 t h1 h
  · exact J_319_321 t h h2

lemma J_315_321 : ∀ t : ℝ, (8824276289119 / 80000000000000 : ℝ) < t → t ≤ (574314867943 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35418692355799 / 320000000000000 : ℝ) with h | h
  · exact J_315_318 t h1 h
  · exact J_318_321 t h h2

lemma J_322_324 : ∀ t : ℝ, (1189158802327 / 10000000000000 : ℝ) < t → t ≤ (1270216935209 / 10000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (38427745899 / 312500000000 : ℝ) with h | h
  · exact I_322 t h1 h
  · exact I_323 t h h2

lemma J_321_324 : ∀ t : ℝ, (574314867943 / 5000000000000 : ℝ) < t → t ≤ (1270216935209 / 10000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1189158802327 / 10000000000000 : ℝ) with h | h
  · exact I_321 t h1 h
  · exact J_322_324 t h h2

lemma J_324_326 : ∀ t : ℝ, (1270216935209 / 10000000000000 : ℝ) < t → t ≤ (53308736251 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (26214920033 / 200000000000 : ℝ) with h | h
  · exact I_324 t h1 h
  · exact I_325 t h h2

lemma J_326_328 : ∀ t : ℝ, (53308736251 / 400000000000 : ℝ) < t → t ≤ (55066528621 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (13546908109 / 100000000000 : ℝ) with h | h
  · exact I_326 t h1 h
  · exact I_327 t h h2

lemma J_324_328 : ∀ t : ℝ, (1270216935209 / 10000000000000 : ℝ) < t → t ≤ (55066528621 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (53308736251 / 400000000000 : ℝ) with h | h
  · exact J_324_326 t h1 h
  · exact J_326_328 t h h2

lemma J_321_328 : ∀ t : ℝ, (574314867943 / 5000000000000 : ℝ) < t → t ≤ (55066528621 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1270216935209 / 10000000000000 : ℝ) with h | h
  · exact J_321_324 t h1 h
  · exact J_324_328 t h h2

lemma J_315_328 : ∀ t : ℝ, (8824276289119 / 80000000000000 : ℝ) < t → t ≤ (55066528621 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (574314867943 / 5000000000000 : ℝ) with h | h
  · exact J_315_321 t h1 h
  · exact J_321_328 t h h2

lemma J_303_328 : ∀ t : ℝ, (2175672272449 / 20000000000000 : ℝ) < t → t ≤ (55066528621 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8824276289119 / 80000000000000 : ℝ) with h | h
  · exact J_303_315 t h1 h
  · exact J_315_328 t h h2

lemma J_329_331 : ∀ t : ℝ, (27972712403 / 200000000000 : ℝ) < t → t ≤ (448442294633 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (896005693081 / 6400000000000 : ℝ) with h | h
  · exact I_329 t h1 h
  · exact I_330 t h h2

lemma J_328_331 : ∀ t : ℝ, (55066528621 / 400000000000 : ℝ) < t → t ≤ (448442294633 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27972712403 / 200000000000 : ℝ) with h | h
  · exact I_328 t h1 h
  · exact J_329_331 t h h2

lemma J_332_334 : ∀ t : ℝ, (897763485451 / 6400000000000 : ℝ) < t → t ≤ (899521277821 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (224660595409 / 1600000000000 : ℝ) with h | h
  · exact I_332 t h1 h
  · exact I_333 t h h2

lemma J_331_334 : ∀ t : ℝ, (448442294633 / 3200000000000 : ℝ) < t → t ≤ (899521277821 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (897763485451 / 6400000000000 : ℝ) with h | h
  · exact I_331 t h1 h
  · exact J_332_334 t h h2

lemma J_328_334 : ∀ t : ℝ, (55066528621 / 400000000000 : ℝ) < t → t ≤ (899521277821 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (448442294633 / 3200000000000 : ℝ) with h | h
  · exact J_328_331 t h1 h
  · exact J_331_334 t h h2

lemma J_335_337 : ∀ t : ℝ, (450200087003 / 3200000000000 : ℝ) < t → t ≤ (112769745797 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (901279070191 / 6400000000000 : ℝ) with h | h
  · exact I_335 t h1 h
  · exact I_336 t h h2

lemma J_334_337 : ∀ t : ℝ, (899521277821 / 6400000000000 : ℝ) < t → t ≤ (112769745797 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (450200087003 / 3200000000000 : ℝ) with h | h
  · exact I_334 t h1 h
  · exact J_335_337 t h h2

lemma J_338_340 : ∀ t : ℝ, (903036862561 / 6400000000000 : ℝ) < t → t ≤ (904794654931 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (451957879373 / 3200000000000 : ℝ) with h | h
  · exact I_338 t h1 h
  · exact I_339 t h h2

lemma J_337_340 : ∀ t : ℝ, (112769745797 / 800000000000 : ℝ) < t → t ≤ (904794654931 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (903036862561 / 6400000000000 : ℝ) with h | h
  · exact I_337 t h1 h
  · exact J_338_340 t h h2

lemma J_334_340 : ∀ t : ℝ, (899521277821 / 6400000000000 : ℝ) < t → t ≤ (904794654931 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (112769745797 / 800000000000 : ℝ) with h | h
  · exact J_334_337 t h1 h
  · exact J_337_340 t h h2

lemma J_328_340 : ∀ t : ℝ, (55066528621 / 400000000000 : ℝ) < t → t ≤ (904794654931 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (899521277821 / 6400000000000 : ℝ) with h | h
  · exact J_328_334 t h1 h
  · exact J_334_340 t h h2

lemma J_341_343 : ∀ t : ℝ, (226418387779 / 1600000000000 : ℝ) < t → t ≤ (453715671743 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (906552447301 / 6400000000000 : ℝ) with h | h
  · exact I_341 t h1 h
  · exact I_342 t h h2

lemma J_340_343 : ∀ t : ℝ, (904794654931 / 6400000000000 : ℝ) < t → t ≤ (453715671743 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (226418387779 / 1600000000000 : ℝ) with h | h
  · exact I_340 t h1 h
  · exact J_341_343 t h h2

lemma J_344_346 : ∀ t : ℝ, (908310239671 / 6400000000000 : ℝ) < t → t ≤ (910068032041 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (56824320991 / 400000000000 : ℝ) with h | h
  · exact I_344 t h1 h
  · exact I_345 t h h2

lemma J_343_346 : ∀ t : ℝ, (453715671743 / 3200000000000 : ℝ) < t → t ≤ (910068032041 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (908310239671 / 6400000000000 : ℝ) with h | h
  · exact I_343 t h1 h
  · exact J_344_346 t h h2

lemma J_340_346 : ∀ t : ℝ, (904794654931 / 6400000000000 : ℝ) < t → t ≤ (910068032041 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (453715671743 / 3200000000000 : ℝ) with h | h
  · exact J_340_343 t h1 h
  · exact J_343_346 t h h2

lemma J_347_349 : ∀ t : ℝ, (455473464113 / 3200000000000 : ℝ) < t → t ≤ (228176180149 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (911825824411 / 6400000000000 : ℝ) with h | h
  · exact I_347 t h1 h
  · exact I_348 t h h2

lemma J_346_349 : ∀ t : ℝ, (910068032041 / 6400000000000 : ℝ) < t → t ≤ (228176180149 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (455473464113 / 3200000000000 : ℝ) with h | h
  · exact I_346 t h1 h
  · exact J_347_349 t h h2

lemma J_349_351 : ∀ t : ℝ, (228176180149 / 1600000000000 : ℝ) < t → t ≤ (457231256483 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (913583616781 / 6400000000000 : ℝ) with h | h
  · exact I_349 t h1 h
  · exact I_350 t h h2

lemma J_351_353 : ∀ t : ℝ, (457231256483 / 3200000000000 : ℝ) < t → t ≤ (114527538167 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (915341409151 / 6400000000000 : ℝ) with h | h
  · exact I_351 t h1 h
  · exact I_352 t h h2

lemma J_349_353 : ∀ t : ℝ, (228176180149 / 1600000000000 : ℝ) < t → t ≤ (114527538167 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (457231256483 / 3200000000000 : ℝ) with h | h
  · exact J_349_351 t h1 h
  · exact J_351_353 t h h2

lemma J_346_353 : ∀ t : ℝ, (910068032041 / 6400000000000 : ℝ) < t → t ≤ (114527538167 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (228176180149 / 1600000000000 : ℝ) with h | h
  · exact J_346_349 t h1 h
  · exact J_349_353 t h h2

lemma J_340_353 : ∀ t : ℝ, (904794654931 / 6400000000000 : ℝ) < t → t ≤ (114527538167 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (910068032041 / 6400000000000 : ℝ) with h | h
  · exact J_340_346 t h1 h
  · exact J_346_353 t h h2

lemma J_328_353 : ∀ t : ℝ, (55066528621 / 400000000000 : ℝ) < t → t ≤ (114527538167 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (904794654931 / 6400000000000 : ℝ) with h | h
  · exact J_328_340 t h1 h
  · exact J_340_353 t h h2

lemma J_303_353 : ∀ t : ℝ, (2175672272449 / 20000000000000 : ℝ) < t → t ≤ (114527538167 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (55066528621 / 400000000000 : ℝ) with h | h
  · exact J_303_328 t h1 h
  · exact J_328_353 t h h2

lemma J_354_356 : ∀ t : ℝ, (917099201521 / 6400000000000 : ℝ) < t → t ≤ (918856993891 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (458989048853 / 3200000000000 : ℝ) with h | h
  · exact I_354 t h1 h
  · exact I_355 t h h2

lemma J_353_356 : ∀ t : ℝ, (114527538167 / 800000000000 : ℝ) < t → t ≤ (918856993891 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (917099201521 / 6400000000000 : ℝ) with h | h
  · exact I_353 t h1 h
  · exact J_354_356 t h h2

lemma J_357_359 : ∀ t : ℝ, (229933972519 / 1600000000000 : ℝ) < t → t ≤ (460746841223 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (920614786261 / 6400000000000 : ℝ) with h | h
  · exact I_357 t h1 h
  · exact I_358 t h h2

lemma J_356_359 : ∀ t : ℝ, (918856993891 / 6400000000000 : ℝ) < t → t ≤ (460746841223 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (229933972519 / 1600000000000 : ℝ) with h | h
  · exact I_356 t h1 h
  · exact J_357_359 t h h2

lemma J_353_359 : ∀ t : ℝ, (114527538167 / 800000000000 : ℝ) < t → t ≤ (460746841223 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (918856993891 / 6400000000000 : ℝ) with h | h
  · exact J_353_356 t h1 h
  · exact J_356_359 t h h2

lemma J_360_362 : ∀ t : ℝ, (922372578631 / 6400000000000 : ℝ) < t → t ≤ (924130371001 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7212902147 / 50000000000 : ℝ) with h | h
  · exact I_360 t h1 h
  · exact I_361 t h h2

lemma J_359_362 : ∀ t : ℝ, (460746841223 / 3200000000000 : ℝ) < t → t ≤ (924130371001 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (922372578631 / 6400000000000 : ℝ) with h | h
  · exact I_359 t h1 h
  · exact J_360_362 t h h2

lemma J_363_365 : ∀ t : ℝ, (462504633593 / 3200000000000 : ℝ) < t → t ≤ (231691764889 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (925888163371 / 6400000000000 : ℝ) with h | h
  · exact I_363 t h1 h
  · exact I_364 t h h2

lemma J_362_365 : ∀ t : ℝ, (924130371001 / 6400000000000 : ℝ) < t → t ≤ (231691764889 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (462504633593 / 3200000000000 : ℝ) with h | h
  · exact I_362 t h1 h
  · exact J_363_365 t h h2

lemma J_359_365 : ∀ t : ℝ, (460746841223 / 3200000000000 : ℝ) < t → t ≤ (231691764889 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (924130371001 / 6400000000000 : ℝ) with h | h
  · exact J_359_362 t h1 h
  · exact J_362_365 t h h2

lemma J_353_365 : ∀ t : ℝ, (114527538167 / 800000000000 : ℝ) < t → t ≤ (231691764889 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (460746841223 / 3200000000000 : ℝ) with h | h
  · exact J_353_359 t h1 h
  · exact J_359_365 t h h2

lemma J_366_368 : ∀ t : ℝ, (927645955741 / 6400000000000 : ℝ) < t → t ≤ (929403748111 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (464262425963 / 3200000000000 : ℝ) with h | h
  · exact I_366 t h1 h
  · exact I_367 t h h2

lemma J_365_368 : ∀ t : ℝ, (231691764889 / 1600000000000 : ℝ) < t → t ≤ (929403748111 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (927645955741 / 6400000000000 : ℝ) with h | h
  · exact I_365 t h1 h
  · exact J_366_368 t h h2

lemma J_369_371 : ∀ t : ℝ, (116285330537 / 800000000000 : ℝ) < t → t ≤ (466020218333 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (931161540481 / 6400000000000 : ℝ) with h | h
  · exact I_369 t h1 h
  · exact I_370 t h h2

lemma J_368_371 : ∀ t : ℝ, (929403748111 / 6400000000000 : ℝ) < t → t ≤ (466020218333 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (116285330537 / 800000000000 : ℝ) with h | h
  · exact I_368 t h1 h
  · exact J_369_371 t h h2

lemma J_365_371 : ∀ t : ℝ, (231691764889 / 1600000000000 : ℝ) < t → t ≤ (466020218333 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (929403748111 / 6400000000000 : ℝ) with h | h
  · exact J_365_368 t h1 h
  · exact J_368_371 t h h2

lemma J_372_374 : ∀ t : ℝ, (932919332851 / 6400000000000 : ℝ) < t → t ≤ (934677125221 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (233449557259 / 1600000000000 : ℝ) with h | h
  · exact I_372 t h1 h
  · exact I_373 t h h2

lemma J_371_374 : ∀ t : ℝ, (466020218333 / 3200000000000 : ℝ) < t → t ≤ (934677125221 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (932919332851 / 6400000000000 : ℝ) with h | h
  · exact I_371 t h1 h
  · exact J_372_374 t h h2

lemma J_374_376 : ∀ t : ℝ, (934677125221 / 6400000000000 : ℝ) < t → t ≤ (936434917591 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (467778010703 / 3200000000000 : ℝ) with h | h
  · exact I_374 t h1 h
  · exact I_375 t h h2

lemma J_376_378 : ∀ t : ℝ, (936434917591 / 6400000000000 : ℝ) < t → t ≤ (938192709961 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (58582113361 / 400000000000 : ℝ) with h | h
  · exact I_376 t h1 h
  · exact I_377 t h h2

lemma J_374_378 : ∀ t : ℝ, (934677125221 / 6400000000000 : ℝ) < t → t ≤ (938192709961 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (936434917591 / 6400000000000 : ℝ) with h | h
  · exact J_374_376 t h1 h
  · exact J_376_378 t h h2

lemma J_371_378 : ∀ t : ℝ, (466020218333 / 3200000000000 : ℝ) < t → t ≤ (938192709961 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (934677125221 / 6400000000000 : ℝ) with h | h
  · exact J_371_374 t h1 h
  · exact J_374_378 t h h2

lemma J_365_378 : ∀ t : ℝ, (231691764889 / 1600000000000 : ℝ) < t → t ≤ (938192709961 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (466020218333 / 3200000000000 : ℝ) with h | h
  · exact J_365_371 t h1 h
  · exact J_371_378 t h h2

lemma J_353_378 : ∀ t : ℝ, (114527538167 / 800000000000 : ℝ) < t → t ≤ (938192709961 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (231691764889 / 1600000000000 : ℝ) with h | h
  · exact J_353_365 t h1 h
  · exact J_365_378 t h h2

lemma J_379_381 : ∀ t : ℝ, (469535803073 / 3200000000000 : ℝ) < t → t ≤ (235207349629 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (939950502331 / 6400000000000 : ℝ) with h | h
  · exact I_379 t h1 h
  · exact I_380 t h h2

lemma J_378_381 : ∀ t : ℝ, (938192709961 / 6400000000000 : ℝ) < t → t ≤ (235207349629 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (469535803073 / 3200000000000 : ℝ) with h | h
  · exact I_378 t h1 h
  · exact J_379_381 t h h2

lemma J_382_384 : ∀ t : ℝ, (941708294701 / 6400000000000 : ℝ) < t → t ≤ (943466087071 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (471293595443 / 3200000000000 : ℝ) with h | h
  · exact I_382 t h1 h
  · exact I_383 t h h2

lemma J_381_384 : ∀ t : ℝ, (235207349629 / 1600000000000 : ℝ) < t → t ≤ (943466087071 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (941708294701 / 6400000000000 : ℝ) with h | h
  · exact I_381 t h1 h
  · exact J_382_384 t h h2

lemma J_378_384 : ∀ t : ℝ, (938192709961 / 6400000000000 : ℝ) < t → t ≤ (943466087071 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (235207349629 / 1600000000000 : ℝ) with h | h
  · exact J_378_381 t h1 h
  · exact J_381_384 t h h2

lemma J_385_387 : ∀ t : ℝ, (118043122907 / 800000000000 : ℝ) < t → t ≤ (473051387813 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (945223879441 / 6400000000000 : ℝ) with h | h
  · exact I_385 t h1 h
  · exact I_386 t h h2

lemma J_384_387 : ∀ t : ℝ, (943466087071 / 6400000000000 : ℝ) < t → t ≤ (473051387813 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (118043122907 / 800000000000 : ℝ) with h | h
  · exact I_384 t h1 h
  · exact J_385_387 t h h2

lemma J_387_389 : ∀ t : ℝ, (473051387813 / 3200000000000 : ℝ) < t → t ≤ (236965141999 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (946981671811 / 6400000000000 : ℝ) with h | h
  · exact I_387 t h1 h
  · exact I_388 t h h2

lemma J_389_391 : ∀ t : ℝ, (236965141999 / 1600000000000 : ℝ) < t → t ≤ (474809180183 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (948739464181 / 6400000000000 : ℝ) with h | h
  · exact I_389 t h1 h
  · exact I_390 t h h2

lemma J_387_391 : ∀ t : ℝ, (473051387813 / 3200000000000 : ℝ) < t → t ≤ (474809180183 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (236965141999 / 1600000000000 : ℝ) with h | h
  · exact J_387_389 t h1 h
  · exact J_389_391 t h h2

lemma J_384_391 : ∀ t : ℝ, (943466087071 / 6400000000000 : ℝ) < t → t ≤ (474809180183 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (473051387813 / 3200000000000 : ℝ) with h | h
  · exact J_384_387 t h1 h
  · exact J_387_391 t h h2

lemma J_378_391 : ∀ t : ℝ, (938192709961 / 6400000000000 : ℝ) < t → t ≤ (474809180183 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (943466087071 / 6400000000000 : ℝ) with h | h
  · exact J_378_384 t h1 h
  · exact J_384_391 t h h2

lemma J_392_394 : ∀ t : ℝ, (950497256551 / 6400000000000 : ℝ) < t → t ≤ (952255048921 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (29730504773 / 200000000000 : ℝ) with h | h
  · exact I_392 t h1 h
  · exact I_393 t h h2

lemma J_391_394 : ∀ t : ℝ, (474809180183 / 3200000000000 : ℝ) < t → t ≤ (952255048921 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (950497256551 / 6400000000000 : ℝ) with h | h
  · exact I_391 t h1 h
  · exact J_392_394 t h h2

lemma J_395_397 : ∀ t : ℝ, (476566972553 / 3200000000000 : ℝ) < t → t ≤ (238722934369 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (954012841291 / 6400000000000 : ℝ) with h | h
  · exact I_395 t h1 h
  · exact I_396 t h h2

lemma J_394_397 : ∀ t : ℝ, (952255048921 / 6400000000000 : ℝ) < t → t ≤ (238722934369 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (476566972553 / 3200000000000 : ℝ) with h | h
  · exact I_394 t h1 h
  · exact J_395_397 t h h2

lemma J_391_397 : ∀ t : ℝ, (474809180183 / 3200000000000 : ℝ) < t → t ≤ (238722934369 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (952255048921 / 6400000000000 : ℝ) with h | h
  · exact J_391_394 t h1 h
  · exact J_394_397 t h h2

lemma J_398_400 : ∀ t : ℝ, (955770633661 / 6400000000000 : ℝ) < t → t ≤ (957528426031 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (478324764923 / 3200000000000 : ℝ) with h | h
  · exact I_398 t h1 h
  · exact I_399 t h h2

lemma J_397_400 : ∀ t : ℝ, (238722934369 / 1600000000000 : ℝ) < t → t ≤ (957528426031 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (955770633661 / 6400000000000 : ℝ) with h | h
  · exact I_397 t h1 h
  · exact J_398_400 t h h2

lemma J_400_402 : ∀ t : ℝ, (957528426031 / 6400000000000 : ℝ) < t → t ≤ (959286218401 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (119800915277 / 800000000000 : ℝ) with h | h
  · exact I_400 t h1 h
  · exact I_401 t h h2

lemma J_402_404 : ∀ t : ℝ, (959286218401 / 6400000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (480082557293 / 3200000000000 : ℝ) with h | h
  · exact I_402 t h1 h
  · exact I_403 t h h2

lemma J_400_404 : ∀ t : ℝ, (957528426031 / 6400000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (959286218401 / 6400000000000 : ℝ) with h | h
  · exact J_400_402 t h1 h
  · exact J_402_404 t h h2

lemma J_397_404 : ∀ t : ℝ, (238722934369 / 1600000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (957528426031 / 6400000000000 : ℝ) with h | h
  · exact J_397_400 t h1 h
  · exact J_400_404 t h h2

lemma J_391_404 : ∀ t : ℝ, (474809180183 / 3200000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (238722934369 / 1600000000000 : ℝ) with h | h
  · exact J_391_397 t h1 h
  · exact J_397_404 t h h2

lemma J_378_404 : ∀ t : ℝ, (938192709961 / 6400000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (474809180183 / 3200000000000 : ℝ) with h | h
  · exact J_378_391 t h1 h
  · exact J_391_404 t h h2

lemma J_353_404 : ∀ t : ℝ, (114527538167 / 800000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (938192709961 / 6400000000000 : ℝ) with h | h
  · exact J_353_378 t h1 h
  · exact J_378_404 t h h2

lemma J_303_404 : ∀ t : ℝ, (2175672272449 / 20000000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (114527538167 / 800000000000 : ℝ) with h | h
  · exact J_303_353 t h1 h
  · exact J_353_404 t h h2

lemma J_202_404 : ∀ t : ℝ, (4615152237067 / 64000000000000 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2175672272449 / 20000000000000 : ℝ) with h | h
  · exact J_202_303 t h1 h
  · exact J_303_404 t h h2

lemma J_0_404 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (961044010771 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4615152237067 / 64000000000000 : ℝ) with h | h
  · exact J_0_202 t h1 h
  · exact J_202_404 t h h2

lemma J_405_407 : ∀ t : ℝ, (240480726739 / 1600000000000 : ℝ) < t → t ≤ (481840349663 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (962801803141 / 6400000000000 : ℝ) with h | h
  · exact I_405 t h1 h
  · exact I_406 t h h2

lemma J_404_407 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (481840349663 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (240480726739 / 1600000000000 : ℝ) with h | h
  · exact I_404 t h1 h
  · exact J_405_407 t h h2

lemma J_408_410 : ∀ t : ℝ, (964559595511 / 6400000000000 : ℝ) < t → t ≤ (966317387881 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (60339905731 / 400000000000 : ℝ) with h | h
  · exact I_408 t h1 h
  · exact I_409 t h h2

lemma J_407_410 : ∀ t : ℝ, (481840349663 / 3200000000000 : ℝ) < t → t ≤ (966317387881 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (964559595511 / 6400000000000 : ℝ) with h | h
  · exact I_407 t h1 h
  · exact J_408_410 t h h2

lemma J_404_410 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (966317387881 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (481840349663 / 3200000000000 : ℝ) with h | h
  · exact J_404_407 t h1 h
  · exact J_407_410 t h h2

lemma J_411_413 : ∀ t : ℝ, (483598142033 / 3200000000000 : ℝ) < t → t ≤ (242238519109 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (968075180251 / 6400000000000 : ℝ) with h | h
  · exact I_411 t h1 h
  · exact I_412 t h h2

lemma J_410_413 : ∀ t : ℝ, (966317387881 / 6400000000000 : ℝ) < t → t ≤ (242238519109 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (483598142033 / 3200000000000 : ℝ) with h | h
  · exact I_410 t h1 h
  · exact J_411_413 t h h2

lemma J_414_416 : ∀ t : ℝ, (969832972621 / 6400000000000 : ℝ) < t → t ≤ (971590764991 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (485355934403 / 3200000000000 : ℝ) with h | h
  · exact I_414 t h1 h
  · exact I_415 t h h2

lemma J_413_416 : ∀ t : ℝ, (242238519109 / 1600000000000 : ℝ) < t → t ≤ (971590764991 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (969832972621 / 6400000000000 : ℝ) with h | h
  · exact I_413 t h1 h
  · exact J_414_416 t h h2

lemma J_410_416 : ∀ t : ℝ, (966317387881 / 6400000000000 : ℝ) < t → t ≤ (971590764991 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (242238519109 / 1600000000000 : ℝ) with h | h
  · exact J_410_413 t h1 h
  · exact J_413_416 t h h2

lemma J_404_416 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (971590764991 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (966317387881 / 6400000000000 : ℝ) with h | h
  · exact J_404_410 t h1 h
  · exact J_410_416 t h h2

lemma J_417_419 : ∀ t : ℝ, (121558707647 / 800000000000 : ℝ) < t → t ≤ (487113726773 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (973348557361 / 6400000000000 : ℝ) with h | h
  · exact I_417 t h1 h
  · exact I_418 t h h2

lemma J_416_419 : ∀ t : ℝ, (971590764991 / 6400000000000 : ℝ) < t → t ≤ (487113726773 / 3200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (121558707647 / 800000000000 : ℝ) with h | h
  · exact I_416 t h1 h
  · exact J_417_419 t h h2

lemma J_420_422 : ∀ t : ℝ, (975106349731 / 6400000000000 : ℝ) < t → t ≤ (976864142101 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (243996311479 / 1600000000000 : ℝ) with h | h
  · exact I_420 t h1 h
  · exact I_421 t h h2

lemma J_419_422 : ∀ t : ℝ, (487113726773 / 3200000000000 : ℝ) < t → t ≤ (976864142101 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (975106349731 / 6400000000000 : ℝ) with h | h
  · exact I_419 t h1 h
  · exact J_420_422 t h h2

lemma J_416_422 : ∀ t : ℝ, (971590764991 / 6400000000000 : ℝ) < t → t ≤ (976864142101 / 6400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (487113726773 / 3200000000000 : ℝ) with h | h
  · exact J_416_419 t h1 h
  · exact J_419_422 t h h2

lemma J_423_425 : ∀ t : ℝ, (488871519143 / 3200000000000 : ℝ) < t → t ≤ (31488297143 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15304700479 / 100000000000 : ℝ) with h | h
  · exact I_423 t h1 h
  · exact I_424 t h h2

lemma J_422_425 : ∀ t : ℝ, (976864142101 / 6400000000000 : ℝ) < t → t ≤ (31488297143 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (488871519143 / 3200000000000 : ℝ) with h | h
  · exact I_422 t h1 h
  · exact J_423_425 t h h2

lemma J_425_427 : ∀ t : ℝ, (31488297143 / 200000000000 : ℝ) < t → t ≤ (33246089513 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2022949583 / 12500000000 : ℝ) with h | h
  · exact I_425 t h1 h
  · exact I_426 t h h2

lemma J_427_429 : ∀ t : ℝ, (33246089513 / 200000000000 : ℝ) < t → t ≤ (35003881883 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17062492849 / 100000000000 : ℝ) with h | h
  · exact I_427 t h1 h
  · exact I_428 t h h2

lemma J_425_429 : ∀ t : ℝ, (31488297143 / 200000000000 : ℝ) < t → t ≤ (35003881883 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33246089513 / 200000000000 : ℝ) with h | h
  · exact J_425_427 t h1 h
  · exact J_427_429 t h h2

lemma J_422_429 : ∀ t : ℝ, (976864142101 / 6400000000000 : ℝ) < t → t ≤ (35003881883 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31488297143 / 200000000000 : ℝ) with h | h
  · exact J_422_425 t h1 h
  · exact J_425_429 t h h2

lemma J_416_429 : ∀ t : ℝ, (971590764991 / 6400000000000 : ℝ) < t → t ≤ (35003881883 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (976864142101 / 6400000000000 : ℝ) with h | h
  · exact J_416_422 t h1 h
  · exact J_422_429 t h h2

lemma J_404_429 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (35003881883 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (971590764991 / 6400000000000 : ℝ) with h | h
  · exact J_404_416 t h1 h
  · exact J_416_429 t h h2

lemma J_430_432 : ∀ t : ℝ, (8970694517 / 50000000000 : ℝ) < t → t ≤ (2264672642597 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (36761674253 / 200000000000 : ℝ) with h | h
  · exact I_430 t h1 h
  · exact I_431 t h h2

lemma J_429_432 : ∀ t : ℝ, (35003881883 / 200000000000 : ℝ) < t → t ≤ (2264672642597 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8970694517 / 50000000000 : ℝ) with h | h
  · exact I_429 t h1 h
  · exact J_430_432 t h h2

lemma J_433_435 : ∀ t : ℝ, (1161822415007 / 6000000000000 : ℝ) < t → t ≤ (794205672477 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (941252369489 / 4800000000000 : ℝ) with h | h
  · exact I_433 t h1 h
  · exact I_434 t h h2

lemma J_432_435 : ∀ t : ℝ, (2264672642597 / 12000000000000 : ℝ) < t → t ≤ (794205672477 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1161822415007 / 6000000000000 : ℝ) with h | h
  · exact I_432 t h1 h
  · exact J_433_435 t h h2

lemma J_429_435 : ∀ t : ℝ, (35003881883 / 200000000000 : ℝ) < t → t ≤ (794205672477 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2264672642597 / 12000000000000 : ℝ) with h | h
  · exact J_429_432 t h1 h
  · exact J_432_435 t h h2

lemma J_436_438 : ∀ t : ℝ, (4824206222279 / 24000000000000 : ℝ) < t → t ≤ (500112278453 / 2400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (152599325303 / 750000000000 : ℝ) with h | h
  · exact I_436 t h1 h
  · exact I_437 t h h2

lemma J_435_438 : ∀ t : ℝ, (794205672477 / 4000000000000 : ℝ) < t → t ≤ (500112278453 / 2400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4824206222279 / 24000000000000 : ℝ) with h | h
  · exact I_435 t h1 h
  · exact J_436_438 t h h2

lemma J_439_441 : ∀ t : ℝ, (426588929947 / 2000000000000 : ℝ) < t → t ≤ (669369488629 / 3000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2618505767099 / 12000000000000 : ℝ) with h | h
  · exact I_439 t h1 h
  · exact I_440 t h h2

lemma J_438_441 : ∀ t : ℝ, (500112278453 / 2400000000000 : ℝ) < t → t ≤ (669369488629 / 3000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (426588929947 / 2000000000000 : ℝ) with h | h
  · exact I_438 t h1 h
  · exact J_439_441 t h h2

lemma J_435_441 : ∀ t : ℝ, (794205672477 / 4000000000000 : ℝ) < t → t ≤ (669369488629 / 3000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (500112278453 / 2400000000000 : ℝ) with h | h
  · exact J_435_438 t h1 h
  · exact J_438_441 t h h2

lemma J_429_441 : ∀ t : ℝ, (35003881883 / 200000000000 : ℝ) < t → t ≤ (669369488629 / 3000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (794205672477 / 4000000000000 : ℝ) with h | h
  · exact J_429_435 t h1 h
  · exact J_435_441 t h h2

lemma J_442_444 : ∀ t : ℝ, (912150047311 / 4000000000000 : ℝ) < t → t ≤ (2854394516767 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (55908446587 / 240000000000 : ℝ) with h | h
  · exact I_442 t h1 h
  · exact I_443 t h h2

lemma J_441_444 : ∀ t : ℝ, (669369488629 / 3000000000000 : ℝ) < t → t ≤ (2854394516767 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (912150047311 / 4000000000000 : ℝ) with h | h
  · exact I_441 t h1 h
  · exact J_442_444 t h h2

lemma J_445_447 : ∀ t : ℝ, (121390279341 / 500000000000 : ℝ) < t → t ≤ (1762694417767 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3462158328541 / 14000000000000 : ℝ) with h | h
  · exact I_445 t h1 h
  · exact I_446 t h h2

lemma J_444_447 : ∀ t : ℝ, (2854394516767 / 12000000000000 : ℝ) < t → t ≤ (1762694417767 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (121390279341 / 500000000000 : ℝ) with h | h
  · exact I_444 t h1 h
  · exact J_445_447 t h h2

lemma J_441_447 : ∀ t : ℝ, (669369488629 / 3000000000000 : ℝ) < t → t ≤ (1762694417767 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2854394516767 / 12000000000000 : ℝ) with h | h
  · exact J_441_444 t h1 h
  · exact J_444_447 t h h2

lemma J_448_450 : ∀ t : ℝ, (3588619342527 / 14000000000000 : ℝ) < t → t ≤ (3715080356513 / 14000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (45648123119 / 175000000000 : ℝ) with h | h
  · exact I_448 t h1 h
  · exact I_449 t h h2

lemma J_447_450 : ∀ t : ℝ, (1762694417767 / 7000000000000 : ℝ) < t → t ≤ (3715080356513 / 14000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3588619342527 / 14000000000000 : ℝ) with h | h
  · exact I_447 t h1 h
  · exact J_448_450 t h h2

lemma J_450_452 : ∀ t : ℝ, (3715080356513 / 14000000000000 : ℝ) < t → t ≤ (548791624357 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1889155431753 / 7000000000000 : ℝ) with h | h
  · exact I_450 t h1 h
  · exact I_451 t h h2

lemma J_452_454 : ∀ t : ℝ, (548791624357 / 2000000000000 : ℝ) < t → t ≤ (793600476897 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (976192969373 / 3500000000000 : ℝ) with h | h
  · exact I_452 t h1 h
  · exact I_453 t h h2

lemma J_450_454 : ∀ t : ℝ, (3715080356513 / 14000000000000 : ℝ) < t → t ≤ (793600476897 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (548791624357 / 2000000000000 : ℝ) with h | h
  · exact J_450_452 t h1 h
  · exact J_452_454 t h h2

lemma J_447_454 : ∀ t : ℝ, (1762694417767 / 7000000000000 : ℝ) < t → t ≤ (793600476897 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3715080356513 / 14000000000000 : ℝ) with h | h
  · exact J_447_450 t h1 h
  · exact J_450_454 t h h2

lemma J_441_454 : ∀ t : ℝ, (669369488629 / 3000000000000 : ℝ) < t → t ≤ (793600476897 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1762694417767 / 7000000000000 : ℝ) with h | h
  · exact J_441_447 t h1 h
  · exact J_447_454 t h h2

lemma J_429_454 : ∀ t : ℝ, (35003881883 / 200000000000 : ℝ) < t → t ≤ (793600476897 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (669369488629 / 3000000000000 : ℝ) with h | h
  · exact J_429_441 t h1 h
  · exact J_441_454 t h h2

lemma J_404_454 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (793600476897 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35003881883 / 200000000000 : ℝ) with h | h
  · exact J_404_429 t h1 h
  · exact J_429_454 t h h2

lemma J_455_457 : ∀ t : ℝ, (2015616445739 / 7000000000000 : ℝ) < t → t ≤ (519711738183 / 1750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4094463398471 / 14000000000000 : ℝ) with h | h
  · exact I_455 t h1 h
  · exact I_456 t h h2

lemma J_454_457 : ∀ t : ℝ, (793600476897 / 2800000000000 : ℝ) < t → t ≤ (519711738183 / 1750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2015616445739 / 7000000000000 : ℝ) with h | h
  · exact I_454 t h1 h
  · exact J_455_457 t h h2

lemma J_458_460 : ∀ t : ℝ, (4220924412457 / 14000000000000 : ℝ) < t → t ≤ (3731612034349 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12240442627 / 40000000000 : ℝ) with h | h
  · exact I_458 t h1 h
  · exact I_459 t h h2

lemma J_457_460 : ∀ t : ℝ, (519711738183 / 1750000000000 : ℝ) < t → t ≤ (3731612034349 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4220924412457 / 14000000000000 : ℝ) with h | h
  · exact I_457 t h1 h
  · exact J_458_460 t h h2

lemma J_454_460 : ∀ t : ℝ, (793600476897 / 2800000000000 : ℝ) < t → t ≤ (3731612034349 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (519711738183 / 1750000000000 : ℝ) with h | h
  · exact J_454_457 t h1 h
  · exact J_457_460 t h h2

lemma J_461_463 : ∀ t : ℝ, (1895545640299 / 6000000000000 : ℝ) < t → t ≤ (488756221637 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1283523508949 / 4000000000000 : ℝ) with h | h
  · exact I_461 t h1 h
  · exact I_462 t h h2

lemma J_460_463 : ∀ t : ℝ, (3731612034349 / 12000000000000 : ℝ) < t → t ≤ (488756221637 / 1500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1895545640299 / 6000000000000 : ℝ) with h | h
  · exact I_460 t h1 h
  · exact J_461_463 t h h2

lemma J_464_466 : ∀ t : ℝ, (793905803869 / 2400000000000 : ℝ) < t → t ≤ (4088487511843 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (671501377599 / 2000000000000 : ℝ) with h | h
  · exact I_464 t h1 h
  · exact I_465 t h h2

lemma J_463_466 : ∀ t : ℝ, (488756221637 / 1500000000000 : ℝ) < t → t ≤ (4088487511843 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (793905803869 / 2400000000000 : ℝ) with h | h
  · exact I_463 t h1 h
  · exact J_464_466 t h h2

lemma J_460_466 : ∀ t : ℝ, (3731612034349 / 12000000000000 : ℝ) < t → t ≤ (4088487511843 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (488756221637 / 1500000000000 : ℝ) with h | h
  · exact J_460_463 t h1 h
  · exact J_463_466 t h h2

lemma J_454_466 : ∀ t : ℝ, (793600476897 / 2800000000000 : ℝ) < t → t ≤ (4088487511843 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3731612034349 / 12000000000000 : ℝ) with h | h
  · exact J_454_460 t h1 h
  · exact J_460_466 t h h2

lemma J_467_469 : ∀ t : ℝ, (1036991689523 / 3000000000000 : ℝ) < t → t ≤ (426692525059 / 1200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1402482001447 / 4000000000000 : ℝ) with h | h
  · exact I_467 t h1 h
  · exact I_468 t h h2

lemma J_466_469 : ∀ t : ℝ, (4088487511843 / 12000000000000 : ℝ) < t → t ≤ (426692525059 / 1200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1036991689523 / 3000000000000 : ℝ) with h | h
  · exact I_466 t h1 h
  · exact J_467_469 t h h2

lemma J_470_472 : ∀ t : ℝ, (4326404496839 / 12000000000000 : ℝ) < t → t ≤ (1035511517989 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (91372577981 / 250000000000 : ℝ) with h | h
  · exact I_470 t h1 h
  · exact I_471 t h h2

lemma J_469_472 : ∀ t : ℝ, (426692525059 / 1200000000000 : ℝ) < t → t ≤ (1035511517989 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4326404496839 / 12000000000000 : ℝ) with h | h
  · exact I_469 t h1 h
  · exact J_470_472 t h h2

lemma J_466_472 : ∀ t : ℝ, (4088487511843 / 12000000000000 : ℝ) < t → t ≤ (1035511517989 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (426692525059 / 1200000000000 : ℝ) with h | h
  · exact J_466_469 t h1 h
  · exact J_469_472 t h h2

lemma J_473_475 : ∀ t : ℝ, (2619125406477 / 7000000000000 : ℝ) < t → t ≤ (1339909314743 / 3500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5298944035963 / 14000000000000 : ℝ) with h | h
  · exact I_473 t h1 h
  · exact I_474 t h h2

lemma J_472_475 : ∀ t : ℝ, (1035511517989 / 2800000000000 : ℝ) < t → t ≤ (1339909314743 / 3500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2619125406477 / 7000000000000 : ℝ) with h | h
  · exact I_472 t h1 h
  · exact J_473_475 t h h2

lemma J_475_477 : ∀ t : ℝ, (1339909314743 / 3500000000000 : ℝ) < t → t ≤ (548102370499 / 1400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5420330481981 / 14000000000000 : ℝ) with h | h
  · exact I_475 t h1 h
  · exact I_476 t h h2

lemma J_477_479 : ∀ t : ℝ, (548102370499 / 1400000000000 : ℝ) < t → t ≤ (175075317219 / 437500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (791673846857 / 2000000000000 : ℝ) with h | h
  · exact I_477 t h1 h
  · exact I_478 t h h2

lemma J_475_479 : ∀ t : ℝ, (1339909314743 / 3500000000000 : ℝ) < t → t ≤ (175075317219 / 437500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (548102370499 / 1400000000000 : ℝ) with h | h
  · exact J_475_477 t h1 h
  · exact J_477_479 t h h2

lemma J_472_479 : ∀ t : ℝ, (1035511517989 / 2800000000000 : ℝ) < t → t ≤ (175075317219 / 437500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1339909314743 / 3500000000000 : ℝ) with h | h
  · exact J_472_475 t h1 h
  · exact J_475_479 t h h2

lemma J_466_479 : ∀ t : ℝ, (4088487511843 / 12000000000000 : ℝ) < t → t ≤ (175075317219 / 437500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1035511517989 / 2800000000000 : ℝ) with h | h
  · exact J_466_472 t h1 h
  · exact J_472_479 t h h2

lemma J_454_479 : ∀ t : ℝ, (793600476897 / 2800000000000 : ℝ) < t → t ≤ (175075317219 / 437500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4088487511843 / 12000000000000 : ℝ) with h | h
  · exact J_454_466 t h1 h
  · exact J_466_479 t h h2

lemma J_480_482 : ∀ t : ℝ, (5663103374017 / 14000000000000 : ℝ) < t → t ≤ (1156897964007 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2861898298513 / 7000000000000 : ℝ) with h | h
  · exact I_480 t h1 h
  · exact I_481 t h h2

lemma J_479_482 : ∀ t : ℝ, (175075317219 / 437500000000 : ℝ) < t → t ≤ (1156897964007 / 2800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5663103374017 / 14000000000000 : ℝ) with h | h
  · exact I_479 t h1 h
  · exact J_480_482 t h h2

lemma J_483_485 : ∀ t : ℝ, (1461295760761 / 3500000000000 : ℝ) < t → t ≤ (426183534933 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5905876266053 / 14000000000000 : ℝ) with h | h
  · exact I_483 t h1 h
  · exact I_484 t h h2

lemma J_482_485 : ∀ t : ℝ, (1156897964007 / 2800000000000 : ℝ) < t → t ≤ (426183534933 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1461295760761 / 3500000000000 : ℝ) with h | h
  · exact I_482 t h1 h
  · exact J_483_485 t h h2

lemma J_479_485 : ∀ t : ℝ, (175075317219 / 437500000000 : ℝ) < t → t ≤ (426183534933 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1156897964007 / 2800000000000 : ℝ) with h | h
  · exact J_479_482 t h1 h
  · exact J_482_485 t h h2

lemma J_486_488 : ∀ t : ℝ, (1033933546217 / 2400000000000 : ℝ) < t → t ≤ (1760199451621 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2612566521487 / 6000000000000 : ℝ) with h | h
  · exact I_486 t h1 h
  · exact I_487 t h h2

lemma J_485_488 : ∀ t : ℝ, (426183534933 / 1000000000000 : ℝ) < t → t ≤ (1760199451621 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1033933546217 / 2400000000000 : ℝ) with h | h
  · exact I_485 t h1 h
  · exact J_486_488 t h h2

lemma J_488_490 : ∀ t : ℝ, (1760199451621 / 4000000000000 : ℝ) < t → t ≤ (5391528978641 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (83375994793 / 187500000000 : ℝ) with h | h
  · exact I_488 t h1 h
  · exact I_489 t h h2

lemma J_490_492 : ∀ t : ℝ, (5391528978641 / 12000000000000 : ℝ) < t → t ≤ (5502459602419 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (181566476351 / 400000000000 : ℝ) with h | h
  · exact I_490 t h1 h
  · exact I_491 t h h2

lemma J_488_492 : ∀ t : ℝ, (1760199451621 / 4000000000000 : ℝ) < t → t ≤ (5502459602419 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5391528978641 / 12000000000000 : ℝ) with h | h
  · exact J_488_490 t h1 h
  · exact J_490_492 t h h2

lemma J_485_492 : ∀ t : ℝ, (426183534933 / 1000000000000 : ℝ) < t → t ≤ (5502459602419 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1760199451621 / 4000000000000 : ℝ) with h | h
  · exact J_485_488 t h1 h
  · exact J_488_492 t h h2

lemma J_479_492 : ∀ t : ℝ, (175075317219 / 437500000000 : ℝ) < t → t ≤ (5502459602419 / 12000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (426183534933 / 1000000000000 : ℝ) with h | h
  · exact J_479_485 t h1 h
  · exact J_485_492 t h h2

lemma J_493_495 : ∀ t : ℝ, (1389481228577 / 3000000000000 : ℝ) < t → t ≤ (2834427769043 / 6000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1871130075399 / 4000000000000 : ℝ) with h | h
  · exact I_493 t h1 h
  · exact I_494 t h h2

lemma J_492_495 : ∀ t : ℝ, (5502459602419 / 12000000000000 : ℝ) < t → t ≤ (2834427769043 / 6000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1389481228577 / 3000000000000 : ℝ) with h | h
  · exact I_492 t h1 h
  · exact J_493_495 t h h2

lemma J_496_498 : ∀ t : ℝ, (228972833999 / 480000000000 : ℝ) < t → t ≤ (2429232048387 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (240824423411 / 500000000000 : ℝ) with h | h
  · exact I_496 t h1 h
  · exact I_497 t h h2

lemma J_495_498 : ∀ t : ℝ, (2834427769043 / 6000000000000 : ℝ) < t → t ≤ (2429232048387 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (228972833999 / 480000000000 : ℝ) with h | h
  · exact I_495 t h1 h
  · exact J_496_498 t h h2

lemma J_492_498 : ∀ t : ℝ, (5502459602419 / 12000000000000 : ℝ) < t → t ≤ (2429232048387 / 5000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2834427769043 / 6000000000000 : ℝ) with h | h
  · exact J_492_495 t h1 h
  · exact J_495_498 t h h2

lemma J_499_501 : ∀ t : ℝ, (306277482833 / 625000000000 : ℝ) < t → t ≤ (1246097745609 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2471207676941 / 5000000000000 : ℝ) with h | h
  · exact I_499 t h1 h
  · exact I_500 t h h2

lemma J_498_501 : ∀ t : ℝ, (2429232048387 / 5000000000000 : ℝ) < t → t ≤ (1246097745609 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (306277482833 / 625000000000 : ℝ) with h | h
  · exact I_498 t h1 h
  · exact J_499_501 t h h2

lemma J_501_503 : ∀ t : ℝ, (1246097745609 / 2500000000000 : ℝ) < t → t ≤ (633542779943 / 1250000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (502636661099 / 1000000000000 : ℝ) with h | h
  · exact I_501 t h1 h
  · exact I_502 t h h2

lemma J_503_505 : ∀ t : ℝ, (633542779943 / 1250000000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2555158934049 / 5000000000000 : ℝ) with h | h
  · exact I_503 t h1 h
  · exact I_504 t h h2

lemma J_501_505 : ∀ t : ℝ, (1246097745609 / 2500000000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (633542779943 / 1250000000000 : ℝ) with h | h
  · exact J_501_503 t h1 h
  · exact J_503_505 t h h2

lemma J_498_505 : ∀ t : ℝ, (2429232048387 / 5000000000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1246097745609 / 2500000000000 : ℝ) with h | h
  · exact J_498_501 t h1 h
  · exact J_501_505 t h h2

lemma J_492_505 : ∀ t : ℝ, (5502459602419 / 12000000000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2429232048387 / 5000000000000 : ℝ) with h | h
  · exact J_492_498 t h1 h
  · exact J_498_505 t h h2

lemma J_479_505 : ∀ t : ℝ, (175075317219 / 437500000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5502459602419 / 12000000000000 : ℝ) with h | h
  · exact J_479_492 t h1 h
  · exact J_492_505 t h h2

lemma J_454_505 : ∀ t : ℝ, (793600476897 / 2800000000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (175075317219 / 437500000000 : ℝ) with h | h
  · exact J_454_479 t h1 h
  · exact J_479_505 t h h2

lemma J_404_505 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (1288073374163 / 2500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (793600476897 / 2800000000000 : ℝ) with h | h
  · exact J_404_454 t h1 h
  · exact J_454_505 t h h2

lemma J_506_508 : ∀ t : ℝ, (2597134562603 / 5000000000000 : ℝ) < t → t ≤ (7398640928157 / 14000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32726529711 / 62500000000 : ℝ) with h | h
  · exact I_506 t h1 h
  · exact I_507 t h h2

lemma J_505_508 : ∀ t : ℝ, (1288073374163 / 2500000000000 : ℝ) < t → t ≤ (7398640928157 / 14000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2597134562603 / 5000000000000 : ℝ) with h | h
  · exact I_505 t h1 h
  · exact J_506_508 t h h2

lemma J_509_511 : ∀ t : ℝ, (149330784021 / 280000000000 : ℝ) < t → t ≤ (1900583936709 / 3500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7534437473943 / 14000000000000 : ℝ) with h | h
  · exact I_509 t h1 h
  · exact I_510 t h h2

lemma J_508_511 : ∀ t : ℝ, (7398640928157 / 14000000000000 : ℝ) < t → t ≤ (1900583936709 / 3500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (149330784021 / 280000000000 : ℝ) with h | h
  · exact I_508 t h1 h
  · exact J_509_511 t h h2

lemma J_505_511 : ∀ t : ℝ, (1288073374163 / 2500000000000 : ℝ) < t → t ≤ (1900583936709 / 3500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7398640928157 / 14000000000000 : ℝ) with h | h
  · exact J_505_508 t h1 h
  · exact J_508_511 t h h2

lemma J_512_514 : ∀ t : ℝ, (7670234019729 / 14000000000000 : ℝ) < t → t ≤ (223029444729 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3869066146311 / 7000000000000 : ℝ) with h | h
  · exact I_512 t h1 h
  · exact I_513 t h h2

lemma J_511_514 : ∀ t : ℝ, (1900583936709 / 3500000000000 : ℝ) < t → t ≤ (223029444729 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7670234019729 / 14000000000000 : ℝ) with h | h
  · exact I_511 t h1 h
  · exact J_512_514 t h h2

lemma J_515_517 : ∀ t : ℝ, (984241104801 / 1750000000000 : ℝ) < t → t ≤ (4004862692097 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7941827111301 / 14000000000000 : ℝ) with h | h
  · exact I_515 t h1 h
  · exact I_516 t h h2

lemma J_514_517 : ∀ t : ℝ, (223029444729 / 400000000000 : ℝ) < t → t ≤ (4004862692097 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (984241104801 / 1750000000000 : ℝ) with h | h
  · exact I_514 t h1 h
  · exact J_515_517 t h h2

lemma J_511_517 : ∀ t : ℝ, (1900583936709 / 3500000000000 : ℝ) < t → t ≤ (4004862692097 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (223029444729 / 400000000000 : ℝ) with h | h
  · exact J_511_514 t h1 h
  · exact J_514_517 t h h2

lemma J_505_517 : ∀ t : ℝ, (1288073374163 / 2500000000000 : ℝ) < t → t ≤ (4004862692097 / 7000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1900583936709 / 3500000000000 : ℝ) with h | h
  · exact J_505_511 t h1 h
  · exact J_511_517 t h h2

lemma J_518_520 : ∀ t : ℝ, (8077623657087 / 14000000000000 : ℝ) < t → t ≤ (8213420202873 / 14000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (407276096499 / 700000000000 : ℝ) with h | h
  · exact I_518 t h1 h
  · exact I_519 t h h2

lemma J_517_520 : ∀ t : ℝ, (4004862692097 / 7000000000000 : ℝ) < t → t ≤ (8213420202873 / 14000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8077623657087 / 14000000000000 : ℝ) with h | h
  · exact I_517 t h1 h
  · exact J_518_520 t h h2

lemma J_521_523 : ∀ t : ℝ, (591522748269 / 1000000000000 : ℝ) < t → t ≤ (481017545197 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4771178719061 / 8000000000000 : ℝ) with h | h
  · exact I_521 t h1 h
  · exact I_522 t h h2

lemma J_520_523 : ∀ t : ℝ, (8213420202873 / 14000000000000 : ℝ) < t → t ≤ (481017545197 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (591522748269 / 1000000000000 : ℝ) with h | h
  · exact I_520 t h1 h
  · exact J_521_523 t h h2

lemma J_517_523 : ∀ t : ℝ, (4004862692097 / 7000000000000 : ℝ) < t → t ≤ (481017545197 / 800000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8213420202873 / 14000000000000 : ℝ) with h | h
  · exact J_517_520 t h1 h
  · exact J_520_523 t h h2

lemma J_524_526 : ∀ t : ℝ, (4849172184879 / 8000000000000 : ℝ) < t → t ≤ (4927165650697 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1222042229447 / 2000000000000 : ℝ) with h | h
  · exact I_524 t h1 h
  · exact I_525 t h h2

lemma J_523_526 : ∀ t : ℝ, (481017545197 / 800000000000 : ℝ) < t → t ≤ (4927165650697 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4849172184879 / 8000000000000 : ℝ) with h | h
  · exact I_523 t h1 h
  · exact J_524_526 t h h2

lemma J_526_528 : ∀ t : ℝ, (4927165650697 / 8000000000000 : ℝ) < t → t ≤ (1001031823303 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2483081191803 / 4000000000000 : ℝ) with h | h
  · exact I_526 t h1 h
  · exact I_527 t h h2

lemma J_528_530 : ∀ t : ℝ, (1001031823303 / 1600000000000 : ℝ) < t → t ≤ (5083152582333 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (315259740589 / 500000000000 : ℝ) with h | h
  · exact I_528 t h1 h
  · exact I_529 t h h2

lemma J_526_530 : ∀ t : ℝ, (4927165650697 / 8000000000000 : ℝ) < t → t ≤ (5083152582333 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1001031823303 / 1600000000000 : ℝ) with h | h
  · exact J_526_528 t h1 h
  · exact J_528_530 t h h2

lemma J_523_530 : ∀ t : ℝ, (481017545197 / 800000000000 : ℝ) < t → t ≤ (5083152582333 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4927165650697 / 8000000000000 : ℝ) with h | h
  · exact J_523_526 t h1 h
  · exact J_526_530 t h h2

lemma J_517_530 : ∀ t : ℝ, (4004862692097 / 7000000000000 : ℝ) < t → t ≤ (5083152582333 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (481017545197 / 800000000000 : ℝ) with h | h
  · exact J_517_523 t h1 h
  · exact J_523_530 t h h2

lemma J_505_530 : ∀ t : ℝ, (1288073374163 / 2500000000000 : ℝ) < t → t ≤ (5083152582333 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4004862692097 / 7000000000000 : ℝ) with h | h
  · exact J_505_517 t h1 h
  · exact J_517_530 t h h2

lemma J_531_533 : ∀ t : ℝ, (2561074657621 / 4000000000000 : ℝ) < t → t ≤ (260007139053 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5161146048151 / 8000000000000 : ℝ) with h | h
  · exact I_531 t h1 h
  · exact I_532 t h h2

lemma J_530_533 : ∀ t : ℝ, (5083152582333 / 8000000000000 : ℝ) < t → t ≤ (260007139053 / 400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2561074657621 / 4000000000000 : ℝ) with h | h
  · exact I_530 t h1 h
  · exact J_531_533 t h h2

lemma J_534_536 : ∀ t : ℝ, (5239139513969 / 8000000000000 : ℝ) < t → t ≤ (5317132979787 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2639068123439 / 4000000000000 : ℝ) with h | h
  · exact I_534 t h1 h
  · exact I_535 t h h2

lemma J_533_536 : ∀ t : ℝ, (260007139053 / 400000000000 : ℝ) < t → t ≤ (5317132979787 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5239139513969 / 8000000000000 : ℝ) with h | h
  · exact I_533 t h1 h
  · exact J_534_536 t h h2

lemma J_530_536 : ∀ t : ℝ, (5083152582333 / 8000000000000 : ℝ) < t → t ≤ (5317132979787 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (260007139053 / 400000000000 : ℝ) with h | h
  · exact J_530_533 t h1 h
  · exact J_533_536 t h h2

lemma J_537_539 : ∀ t : ℝ, (669516214087 / 1000000000000 : ℝ) < t → t ≤ (2717061589257 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1079025289121 / 1600000000000 : ℝ) with h | h
  · exact I_537 t h1 h
  · exact I_538 t h h2

lemma J_536_539 : ∀ t : ℝ, (5317132979787 / 8000000000000 : ℝ) < t → t ≤ (2717061589257 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (669516214087 / 1000000000000 : ℝ) with h | h
  · exact I_536 t h1 h
  · exact J_537_539 t h h2

lemma J_540_542 : ∀ t : ℝ, (5473119911423 / 8000000000000 : ℝ) < t → t ≤ (5551113377241 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1378029161083 / 2000000000000 : ℝ) with h | h
  · exact I_540 t h1 h
  · exact I_541 t h h2

lemma J_539_542 : ∀ t : ℝ, (2717061589257 / 4000000000000 : ℝ) < t → t ≤ (5551113377241 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5473119911423 / 8000000000000 : ℝ) with h | h
  · exact I_539 t h1 h
  · exact J_540_542 t h h2

lemma J_536_542 : ∀ t : ℝ, (5317132979787 / 8000000000000 : ℝ) < t → t ≤ (5551113377241 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2717061589257 / 4000000000000 : ℝ) with h | h
  · exact J_536_539 t h1 h
  · exact J_539_542 t h h2

lemma J_530_542 : ∀ t : ℝ, (5083152582333 / 8000000000000 : ℝ) < t → t ≤ (5551113377241 / 8000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5317132979787 / 8000000000000 : ℝ) with h | h
  · exact J_530_536 t h1 h
  · exact J_536_542 t h h2

lemma J_543_545 : ∀ t : ℝ, (111802202203 / 160000000000 : ℝ) < t → t ≤ (177128236749 / 250000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5629106843059 / 8000000000000 : ℝ) with h | h
  · exact I_543 t h1 h
  · exact I_544 t h h2

lemma J_542_545 : ∀ t : ℝ, (5551113377241 / 8000000000000 : ℝ) < t → t ≤ (177128236749 / 250000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (111802202203 / 160000000000 : ℝ) with h | h
  · exact I_542 t h1 h
  · exact J_543_545 t h h2

lemma J_546_548 : ∀ t : ℝ, (5707100308877 / 8000000000000 : ℝ) < t → t ≤ (1157018754939 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2873048520893 / 4000000000000 : ℝ) with h | h
  · exact I_546 t h1 h
  · exact I_547 t h h2

lemma J_545_548 : ∀ t : ℝ, (177128236749 / 250000000000 : ℝ) < t → t ≤ (1157018754939 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5707100308877 / 8000000000000 : ℝ) with h | h
  · exact I_545 t h1 h
  · exact J_546_548 t h h2

lemma J_542_548 : ∀ t : ℝ, (5551113377241 / 8000000000000 : ℝ) < t → t ≤ (1157018754939 / 1600000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (177128236749 / 250000000000 : ℝ) with h | h
  · exact J_542_545 t h1 h
  · exact J_545_548 t h h2

lemma J_549_551 : ∀ t : ℝ, (1456022626901 / 2000000000000 : ℝ) < t → t ≤ (2951041986711 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5863087240513 / 8000000000000 : ℝ) with h | h
  · exact I_549 t h1 h
  · exact I_550 t h h2

lemma J_548_551 : ∀ t : ℝ, (1157018754939 / 1600000000000 : ℝ) < t → t ≤ (2951041986711 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1456022626901 / 2000000000000 : ℝ) with h | h
  · exact I_548 t h1 h
  · exact J_549_551 t h h2

lemma J_551_553 : ∀ t : ℝ, (2951041986711 / 4000000000000 : ℝ) < t → t ≤ (149501935981 / 200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5941080706331 / 8000000000000 : ℝ) with h | h
  · exact I_551 t h1 h
  · exact I_552 t h h2

lemma J_553_555 : ∀ t : ℝ, (149501935981 / 200000000000 : ℝ) < t → t ≤ (3021288055457 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6011326775077 / 8000000000000 : ℝ) with h | h
  · exact I_553 t h1 h
  · exact I_554 t h h2

lemma J_551_555 : ∀ t : ℝ, (2951041986711 / 4000000000000 : ℝ) < t → t ≤ (3021288055457 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (149501935981 / 200000000000 : ℝ) with h | h
  · exact J_551_553 t h1 h
  · exact J_553_555 t h h2

lemma J_548_555 : ∀ t : ℝ, (1157018754939 / 1600000000000 : ℝ) < t → t ≤ (3021288055457 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2951041986711 / 4000000000000 : ℝ) with h | h
  · exact J_548_551 t h1 h
  · exact J_551_555 t h h2

lemma J_542_555 : ∀ t : ℝ, (5551113377241 / 8000000000000 : ℝ) < t → t ≤ (3021288055457 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1157018754939 / 1600000000000 : ℝ) with h | h
  · exact J_542_548 t h1 h
  · exact J_548_555 t h h2

lemma J_530_555 : ∀ t : ℝ, (5083152582333 / 8000000000000 : ℝ) < t → t ≤ (3021288055457 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5551113377241 / 8000000000000 : ℝ) with h | h
  · exact J_530_542 t h1 h
  · exact J_542_555 t h h2

lemma J_505_555 : ∀ t : ℝ, (1288073374163 / 2500000000000 : ℝ) < t → t ≤ (3021288055457 / 4000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5083152582333 / 8000000000000 : ℝ) with h | h
  · exact J_505_530 t h1 h
  · exact J_530_555 t h h2

lemma J_556_558 : ∀ t : ℝ, (6073825446751 / 8000000000000 : ℝ) < t → t ≤ (245452964737 / 320000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1526268695647 / 2000000000000 : ℝ) with h | h
  · exact I_556 t h1 h
  · exact I_557 t h h2

lemma J_555_558 : ∀ t : ℝ, (3021288055457 / 4000000000000 : ℝ) < t → t ≤ (245452964737 / 320000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6073825446751 / 8000000000000 : ℝ) with h | h
  · exact I_555 t h1 h
  · exact J_556_558 t h h2

lemma J_559_561 : ∀ t : ℝ, (3083786727131 / 4000000000000 : ℝ) < t → t ≤ (389379507871 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6198822790099 / 8000000000000 : ℝ) with h | h
  · exact I_559 t h1 h
  · exact I_560 t h h2

lemma J_558_561 : ∀ t : ℝ, (245452964737 / 320000000000 : ℝ) < t → t ≤ (389379507871 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3083786727131 / 4000000000000 : ℝ) with h | h
  · exact I_558 t h1 h
  · exact J_559_561 t h h2

lemma J_555_561 : ∀ t : ℝ, (3021288055457 / 4000000000000 : ℝ) < t → t ≤ (389379507871 / 500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (245452964737 / 320000000000 : ℝ) with h | h
  · exact J_555_558 t h1 h
  · exact J_558_561 t h h2

lemma J_562_564 : ∀ t : ℝ, (24294174464377 / 31000000000000 : ℝ) < t → t ≤ (24599464417127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1527926215047 / 1937500000000 : ℝ) with h | h
  · exact I_562 t h1 h
  · exact I_563 t h h2

lemma J_561_564 : ∀ t : ℝ, (389379507871 / 500000000000 : ℝ) < t → t ≤ (24599464417127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (24294174464377 / 31000000000000 : ℝ) with h | h
  · exact I_561 t h1 h
  · exact J_562_564 t h h2

lemma J_565_567 : ∀ t : ℝ, (12376054696751 / 15500000000000 : ℝ) < t → t ≤ (6264349836563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (24904754369877 / 31000000000000 : ℝ) with h | h
  · exact I_565 t h1 h
  · exact I_566 t h h2

lemma J_564_567 : ∀ t : ℝ, (24599464417127 / 31000000000000 : ℝ) < t → t ≤ (6264349836563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12376054696751 / 15500000000000 : ℝ) with h | h
  · exact I_564 t h1 h
  · exact J_565_567 t h h2

lemma J_561_567 : ∀ t : ℝ, (389379507871 / 500000000000 : ℝ) < t → t ≤ (6264349836563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (24599464417127 / 31000000000000 : ℝ) with h | h
  · exact J_561_564 t h1 h
  · exact J_564_567 t h h2

lemma J_555_567 : ∀ t : ℝ, (3021288055457 / 4000000000000 : ℝ) < t → t ≤ (6264349836563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (389379507871 / 500000000000 : ℝ) with h | h
  · exact J_555_561 t h1 h
  · exact J_561_567 t h h2

lemma J_568_570 : ∀ t : ℝ, (25210044322627 / 31000000000000 : ℝ) < t → t ≤ (25515334275377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12681344649501 / 15500000000000 : ℝ) with h | h
  · exact I_568 t h1 h
  · exact I_569 t h h2

lemma J_567_570 : ∀ t : ℝ, (6264349836563 / 7750000000000 : ℝ) < t → t ≤ (25515334275377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (25210044322627 / 31000000000000 : ℝ) with h | h
  · exact I_567 t h1 h
  · exact J_568_570 t h h2

lemma J_571_573 : ∀ t : ℝ, (3208497406469 / 3875000000000 : ℝ) < t → t ≤ (12986634602251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (25820624228127 / 31000000000000 : ℝ) with h | h
  · exact I_571 t h1 h
  · exact I_572 t h h2

lemma J_570_573 : ∀ t : ℝ, (25515334275377 / 31000000000000 : ℝ) < t → t ≤ (12986634602251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3208497406469 / 3875000000000 : ℝ) with h | h
  · exact I_570 t h1 h
  · exact J_571_573 t h h2

lemma J_567_573 : ∀ t : ℝ, (6264349836563 / 7750000000000 : ℝ) < t → t ≤ (12986634602251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (25515334275377 / 31000000000000 : ℝ) with h | h
  · exact J_567_570 t h1 h
  · exact J_570_573 t h h2

lemma J_574_576 : ∀ t : ℝ, (26125914180877 / 31000000000000 : ℝ) < t → t ≤ (26431204133627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6569639789313 / 7750000000000 : ℝ) with h | h
  · exact I_574 t h1 h
  · exact I_575 t h h2

lemma J_573_576 : ∀ t : ℝ, (12986634602251 / 15500000000000 : ℝ) < t → t ≤ (26431204133627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (26125914180877 / 31000000000000 : ℝ) with h | h
  · exact I_573 t h1 h
  · exact J_574_576 t h h2

lemma J_576_578 : ∀ t : ℝ, (26431204133627 / 31000000000000 : ℝ) < t → t ≤ (26736494086377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (13291924555001 / 15500000000000 : ℝ) with h | h
  · exact I_576 t h1 h
  · exact I_577 t h h2

lemma J_578_580 : ∀ t : ℝ, (26736494086377 / 31000000000000 : ℝ) < t → t ≤ (27041784039127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (840285595711 / 968750000000 : ℝ) with h | h
  · exact I_578 t h1 h
  · exact I_579 t h h2

lemma J_576_580 : ∀ t : ℝ, (26431204133627 / 31000000000000 : ℝ) < t → t ≤ (27041784039127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (26736494086377 / 31000000000000 : ℝ) with h | h
  · exact J_576_578 t h1 h
  · exact J_578_580 t h h2

lemma J_573_580 : ∀ t : ℝ, (12986634602251 / 15500000000000 : ℝ) < t → t ≤ (27041784039127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (26431204133627 / 31000000000000 : ℝ) with h | h
  · exact J_573_576 t h1 h
  · exact J_576_580 t h h2

lemma J_567_580 : ∀ t : ℝ, (6264349836563 / 7750000000000 : ℝ) < t → t ≤ (27041784039127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12986634602251 / 15500000000000 : ℝ) with h | h
  · exact J_567_573 t h1 h
  · exact J_573_580 t h h2

lemma J_555_580 : ∀ t : ℝ, (3021288055457 / 4000000000000 : ℝ) < t → t ≤ (27041784039127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6264349836563 / 7750000000000 : ℝ) with h | h
  · exact J_555_567 t h1 h
  · exact J_567_580 t h h2

lemma J_581_583 : ∀ t : ℝ, (13597214507751 / 15500000000000 : ℝ) < t → t ≤ (6874929742063 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27347073991877 / 31000000000000 : ℝ) with h | h
  · exact I_581 t h1 h
  · exact I_582 t h h2

lemma J_580_583 : ∀ t : ℝ, (27041784039127 / 31000000000000 : ℝ) < t → t ≤ (6874929742063 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (13597214507751 / 15500000000000 : ℝ) with h | h
  · exact I_580 t h1 h
  · exact J_581_583 t h h2

lemma J_584_586 : ∀ t : ℝ, (27652363944627 / 31000000000000 : ℝ) < t → t ≤ (27957653897377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (13902504460501 / 15500000000000 : ℝ) with h | h
  · exact I_584 t h1 h
  · exact I_585 t h h2

lemma J_583_586 : ∀ t : ℝ, (6874929742063 / 7750000000000 : ℝ) < t → t ≤ (27957653897377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27652363944627 / 31000000000000 : ℝ) with h | h
  · exact I_583 t h1 h
  · exact J_584_586 t h h2

lemma J_580_586 : ∀ t : ℝ, (27041784039127 / 31000000000000 : ℝ) < t → t ≤ (27957653897377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6874929742063 / 7750000000000 : ℝ) with h | h
  · exact J_580_583 t h1 h
  · exact J_583_586 t h h2

lemma J_587_589 : ∀ t : ℝ, (3513787359219 / 3875000000000 : ℝ) < t → t ≤ (14207794413251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (28262943850127 / 31000000000000 : ℝ) with h | h
  · exact I_587 t h1 h
  · exact I_588 t h h2

lemma J_586_589 : ∀ t : ℝ, (27957653897377 / 31000000000000 : ℝ) < t → t ≤ (14207794413251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3513787359219 / 3875000000000 : ℝ) with h | h
  · exact I_586 t h1 h
  · exact J_587_589 t h h2

lemma J_589_591 : ∀ t : ℝ, (14207794413251 / 15500000000000 : ℝ) < t → t ≤ (7180219694813 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (28568233802877 / 31000000000000 : ℝ) with h | h
  · exact I_589 t h1 h
  · exact I_590 t h h2

lemma J_591_593 : ∀ t : ℝ, (7180219694813 / 7750000000000 : ℝ) < t → t ≤ (14513084366001 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (931403992117 / 1000000000000 : ℝ) with h | h
  · exact I_591 t h1 h
  · exact I_592 t h h2

lemma J_589_593 : ∀ t : ℝ, (14207794413251 / 15500000000000 : ℝ) < t → t ≤ (14513084366001 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7180219694813 / 7750000000000 : ℝ) with h | h
  · exact J_589_591 t h1 h
  · exact J_591_593 t h h2

lemma J_586_593 : ∀ t : ℝ, (27957653897377 / 31000000000000 : ℝ) < t → t ≤ (14513084366001 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (14207794413251 / 15500000000000 : ℝ) with h | h
  · exact J_586_589 t h1 h
  · exact J_589_593 t h h2

lemma J_580_593 : ∀ t : ℝ, (27041784039127 / 31000000000000 : ℝ) < t → t ≤ (14513084366001 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27957653897377 / 31000000000000 : ℝ) with h | h
  · exact J_580_586 t h1 h
  · exact J_586_593 t h h2

lemma J_594_596 : ∀ t : ℝ, (29178813708377 / 31000000000000 : ℝ) < t → t ≤ (29484103661127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1833216167797 / 1937500000000 : ℝ) with h | h
  · exact I_594 t h1 h
  · exact I_595 t h h2

lemma J_593_596 : ∀ t : ℝ, (14513084366001 / 15500000000000 : ℝ) < t → t ≤ (29484103661127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (29178813708377 / 31000000000000 : ℝ) with h | h
  · exact I_593 t h1 h
  · exact J_594_596 t h h2

lemma J_597_599 : ∀ t : ℝ, (14818374318751 / 15500000000000 : ℝ) < t → t ≤ (7485509647563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (29789393613877 / 31000000000000 : ℝ) with h | h
  · exact I_597 t h1 h
  · exact I_598 t h h2

lemma J_596_599 : ∀ t : ℝ, (29484103661127 / 31000000000000 : ℝ) < t → t ≤ (7485509647563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (14818374318751 / 15500000000000 : ℝ) with h | h
  · exact I_596 t h1 h
  · exact J_597_599 t h h2

lemma J_593_599 : ∀ t : ℝ, (14513084366001 / 15500000000000 : ℝ) < t → t ≤ (7485509647563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (29484103661127 / 31000000000000 : ℝ) with h | h
  · exact J_593_596 t h1 h
  · exact J_596_599 t h h2

lemma J_600_602 : ∀ t : ℝ, (30094683566627 / 31000000000000 : ℝ) < t → t ≤ (30399973519377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15123664271501 / 15500000000000 : ℝ) with h | h
  · exact I_600 t h1 h
  · exact I_601 t h h2

lemma J_599_602 : ∀ t : ℝ, (7485509647563 / 7750000000000 : ℝ) < t → t ≤ (30399973519377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (30094683566627 / 31000000000000 : ℝ) with h | h
  · exact I_599 t h1 h
  · exact J_600_602 t h h2

lemma J_602_604 : ∀ t : ℝ, (30399973519377 / 31000000000000 : ℝ) < t → t ≤ (30705263472127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3819077311969 / 3875000000000 : ℝ) with h | h
  · exact I_602 t h1 h
  · exact I_603 t h h2

lemma J_604_606 : ∀ t : ℝ, (30705263472127 / 31000000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15428954224251 / 15500000000000 : ℝ) with h | h
  · exact I_604 t h1 h
  · exact I_605 t h h2

lemma J_602_606 : ∀ t : ℝ, (30399973519377 / 31000000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (30705263472127 / 31000000000000 : ℝ) with h | h
  · exact J_602_604 t h1 h
  · exact J_604_606 t h h2

lemma J_599_606 : ∀ t : ℝ, (7485509647563 / 7750000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (30399973519377 / 31000000000000 : ℝ) with h | h
  · exact J_599_602 t h1 h
  · exact J_602_606 t h h2

lemma J_593_606 : ∀ t : ℝ, (14513084366001 / 15500000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7485509647563 / 7750000000000 : ℝ) with h | h
  · exact J_593_599 t h1 h
  · exact J_599_606 t h h2

lemma J_580_606 : ∀ t : ℝ, (27041784039127 / 31000000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (14513084366001 / 15500000000000 : ℝ) with h | h
  · exact J_580_593 t h1 h
  · exact J_593_606 t h h2

lemma J_555_606 : ∀ t : ℝ, (3021288055457 / 4000000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27041784039127 / 31000000000000 : ℝ) with h | h
  · exact J_555_580 t h1 h
  · exact J_580_606 t h h2

lemma J_505_606 : ∀ t : ℝ, (1288073374163 / 2500000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3021288055457 / 4000000000000 : ℝ) with h | h
  · exact J_505_555 t h1 h
  · exact J_555_606 t h h2

lemma J_404_606 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (31010553424877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1288073374163 / 2500000000000 : ℝ) with h | h
  · exact J_404_505 t h1 h
  · exact J_505_606 t h h2

lemma J_607_609 : ∀ t : ℝ, (7790799600313 / 7750000000000 : ℝ) < t → t ≤ (15734244177001 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31315843377627 / 31000000000000 : ℝ) with h | h
  · exact I_607 t h1 h
  · exact I_608 t h h2

lemma J_606_609 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (15734244177001 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7790799600313 / 7750000000000 : ℝ) with h | h
  · exact I_606 t h1 h
  · exact J_607_609 t h h2

lemma J_610_612 : ∀ t : ℝ, (31621133330377 / 31000000000000 : ℝ) < t → t ≤ (31926423283127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (496465286043 / 484375000000 : ℝ) with h | h
  · exact I_610 t h1 h
  · exact I_611 t h h2

lemma J_609_612 : ∀ t : ℝ, (15734244177001 / 15500000000000 : ℝ) < t → t ≤ (31926423283127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31621133330377 / 31000000000000 : ℝ) with h | h
  · exact I_609 t h1 h
  · exact J_610_612 t h h2

lemma J_606_612 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (31926423283127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15734244177001 / 15500000000000 : ℝ) with h | h
  · exact J_606_609 t h1 h
  · exact J_609_612 t h h2

lemma J_613_615 : ∀ t : ℝ, (16039534129751 / 15500000000000 : ℝ) < t → t ≤ (8096089553063 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32231713235877 / 31000000000000 : ℝ) with h | h
  · exact I_613 t h1 h
  · exact I_614 t h h2

lemma J_612_615 : ∀ t : ℝ, (31926423283127 / 31000000000000 : ℝ) < t → t ≤ (8096089553063 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16039534129751 / 15500000000000 : ℝ) with h | h
  · exact I_612 t h1 h
  · exact J_613_615 t h h2

lemma J_616_618 : ∀ t : ℝ, (32537003188627 / 31000000000000 : ℝ) < t → t ≤ (32842293141377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16344824082501 / 15500000000000 : ℝ) with h | h
  · exact I_616 t h1 h
  · exact I_617 t h h2

lemma J_615_618 : ∀ t : ℝ, (8096089553063 / 7750000000000 : ℝ) < t → t ≤ (32842293141377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32537003188627 / 31000000000000 : ℝ) with h | h
  · exact I_615 t h1 h
  · exact J_616_618 t h h2

lemma J_612_618 : ∀ t : ℝ, (31926423283127 / 31000000000000 : ℝ) < t → t ≤ (32842293141377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8096089553063 / 7750000000000 : ℝ) with h | h
  · exact J_612_615 t h1 h
  · exact J_615_618 t h h2

lemma J_606_618 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (32842293141377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31926423283127 / 31000000000000 : ℝ) with h | h
  · exact J_606_612 t h1 h
  · exact J_612_618 t h h2

lemma J_619_621 : ∀ t : ℝ, (4124367264719 / 3875000000000 : ℝ) < t → t ≤ (16650114035251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33147583094127 / 31000000000000 : ℝ) with h | h
  · exact I_619 t h1 h
  · exact I_620 t h h2

lemma J_618_621 : ∀ t : ℝ, (32842293141377 / 31000000000000 : ℝ) < t → t ≤ (16650114035251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4124367264719 / 3875000000000 : ℝ) with h | h
  · exact I_618 t h1 h
  · exact J_619_621 t h h2

lemma J_622_624 : ∀ t : ℝ, (33452873046877 / 31000000000000 : ℝ) < t → t ≤ (33758162999627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (271012242123 / 250000000000 : ℝ) with h | h
  · exact I_622 t h1 h
  · exact I_623 t h h2

lemma J_621_624 : ∀ t : ℝ, (16650114035251 / 15500000000000 : ℝ) < t → t ≤ (33758162999627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33452873046877 / 31000000000000 : ℝ) with h | h
  · exact I_621 t h1 h
  · exact J_622_624 t h h2

lemma J_618_624 : ∀ t : ℝ, (32842293141377 / 31000000000000 : ℝ) < t → t ≤ (33758162999627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16650114035251 / 15500000000000 : ℝ) with h | h
  · exact J_618_621 t h1 h
  · exact J_621_624 t h h2

lemma J_625_627 : ∀ t : ℝ, (16955403988001 / 15500000000000 : ℝ) < t → t ≤ (2138506120547 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34063452952377 / 31000000000000 : ℝ) with h | h
  · exact I_625 t h1 h
  · exact I_626 t h h2

lemma J_624_627 : ∀ t : ℝ, (33758162999627 / 31000000000000 : ℝ) < t → t ≤ (2138506120547 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (16955403988001 / 15500000000000 : ℝ) with h | h
  · exact I_624 t h1 h
  · exact J_625_627 t h h2

lemma J_627_629 : ∀ t : ℝ, (2138506120547 / 1937500000000 : ℝ) < t → t ≤ (17260693940751 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34368742905127 / 31000000000000 : ℝ) with h | h
  · exact I_627 t h1 h
  · exact I_628 t h h2

lemma J_629_631 : ∀ t : ℝ, (17260693940751 / 15500000000000 : ℝ) < t → t ≤ (8706669458563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34674032857877 / 31000000000000 : ℝ) with h | h
  · exact I_629 t h1 h
  · exact I_630 t h h2

lemma J_627_631 : ∀ t : ℝ, (2138506120547 / 1937500000000 : ℝ) < t → t ≤ (8706669458563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17260693940751 / 15500000000000 : ℝ) with h | h
  · exact J_627_629 t h1 h
  · exact J_629_631 t h h2

lemma J_624_631 : ∀ t : ℝ, (33758162999627 / 31000000000000 : ℝ) < t → t ≤ (8706669458563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2138506120547 / 1937500000000 : ℝ) with h | h
  · exact J_624_627 t h1 h
  · exact J_627_631 t h h2

lemma J_618_631 : ∀ t : ℝ, (32842293141377 / 31000000000000 : ℝ) < t → t ≤ (8706669458563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (33758162999627 / 31000000000000 : ℝ) with h | h
  · exact J_618_624 t h1 h
  · exact J_624_631 t h h2

lemma J_606_631 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (8706669458563 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (32842293141377 / 31000000000000 : ℝ) with h | h
  · exact J_606_618 t h1 h
  · exact J_618_631 t h h2

lemma J_632_634 : ∀ t : ℝ, (34979322810627 / 31000000000000 : ℝ) < t → t ≤ (35284612763377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17565983893501 / 15500000000000 : ℝ) with h | h
  · exact I_632 t h1 h
  · exact I_633 t h h2

lemma J_631_634 : ∀ t : ℝ, (8706669458563 / 7750000000000 : ℝ) < t → t ≤ (35284612763377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (34979322810627 / 31000000000000 : ℝ) with h | h
  · exact I_631 t h1 h
  · exact J_632_634 t h h2

lemma J_635_637 : ∀ t : ℝ, (4429657217469 / 3875000000000 : ℝ) < t → t ≤ (17871273846251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35589902716127 / 31000000000000 : ℝ) with h | h
  · exact I_635 t h1 h
  · exact I_636 t h h2

lemma J_634_637 : ∀ t : ℝ, (35284612763377 / 31000000000000 : ℝ) < t → t ≤ (17871273846251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4429657217469 / 3875000000000 : ℝ) with h | h
  · exact I_634 t h1 h
  · exact J_635_637 t h h2

lemma J_631_637 : ∀ t : ℝ, (8706669458563 / 7750000000000 : ℝ) < t → t ≤ (17871273846251 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35284612763377 / 31000000000000 : ℝ) with h | h
  · exact J_631_634 t h1 h
  · exact J_634_637 t h h2

lemma J_638_640 : ∀ t : ℝ, (35895192668877 / 31000000000000 : ℝ) < t → t ≤ (36200482621627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9011959411313 / 7750000000000 : ℝ) with h | h
  · exact I_638 t h1 h
  · exact I_639 t h h2

lemma J_637_640 : ∀ t : ℝ, (17871273846251 / 15500000000000 : ℝ) < t → t ≤ (36200482621627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (35895192668877 / 31000000000000 : ℝ) with h | h
  · exact I_637 t h1 h
  · exact J_638_640 t h h2

lemma J_641_643 : ∀ t : ℝ, (18176563799001 / 15500000000000 : ℝ) < t → t ≤ (1145575548461 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (36505772574377 / 31000000000000 : ℝ) with h | h
  · exact I_641 t h1 h
  · exact I_642 t h h2

lemma J_640_643 : ∀ t : ℝ, (36200482621627 / 31000000000000 : ℝ) < t → t ≤ (1145575548461 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (18176563799001 / 15500000000000 : ℝ) with h | h
  · exact I_640 t h1 h
  · exact J_641_643 t h h2

lemma J_637_643 : ∀ t : ℝ, (17871273846251 / 15500000000000 : ℝ) < t → t ≤ (1145575548461 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (36200482621627 / 31000000000000 : ℝ) with h | h
  · exact J_637_640 t h1 h
  · exact J_640_643 t h h2

lemma J_631_643 : ∀ t : ℝ, (8706669458563 / 7750000000000 : ℝ) < t → t ≤ (1145575548461 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17871273846251 / 15500000000000 : ℝ) with h | h
  · exact J_631_637 t h1 h
  · exact J_637_643 t h h2

lemma J_644_646 : ∀ t : ℝ, (36811062527127 / 31000000000000 : ℝ) < t → t ≤ (37116352479877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (18481853751751 / 15500000000000 : ℝ) with h | h
  · exact I_644 t h1 h
  · exact I_645 t h h2

lemma J_643_646 : ∀ t : ℝ, (1145575548461 / 968750000000 : ℝ) < t → t ≤ (37116352479877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (36811062527127 / 31000000000000 : ℝ) with h | h
  · exact I_643 t h1 h
  · exact J_644_646 t h h2

lemma J_647_649 : ∀ t : ℝ, (9317249364063 / 7750000000000 : ℝ) < t → t ≤ (18787143704501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (37421642432627 / 31000000000000 : ℝ) with h | h
  · exact I_647 t h1 h
  · exact I_648 t h h2

lemma J_646_649 : ∀ t : ℝ, (37116352479877 / 31000000000000 : ℝ) < t → t ≤ (18787143704501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9317249364063 / 7750000000000 : ℝ) with h | h
  · exact I_646 t h1 h
  · exact J_647_649 t h h2

lemma J_643_649 : ∀ t : ℝ, (1145575548461 / 968750000000 : ℝ) < t → t ≤ (18787143704501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (37116352479877 / 31000000000000 : ℝ) with h | h
  · exact J_643_646 t h1 h
  · exact J_646_649 t h h2

lemma J_650_652 : ∀ t : ℝ, (37726932385377 / 31000000000000 : ℝ) < t → t ≤ (38032222338127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4734947170219 / 3875000000000 : ℝ) with h | h
  · exact I_650 t h1 h
  · exact I_651 t h h2

lemma J_649_652 : ∀ t : ℝ, (18787143704501 / 15500000000000 : ℝ) < t → t ≤ (38032222338127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (37726932385377 / 31000000000000 : ℝ) with h | h
  · exact I_649 t h1 h
  · exact J_650_652 t h h2

lemma J_652_654 : ∀ t : ℝ, (38032222338127 / 31000000000000 : ℝ) < t → t ≤ (1236693944867 / 1000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (19092433657251 / 15500000000000 : ℝ) with h | h
  · exact I_652 t h1 h
  · exact I_653 t h h2

lemma J_654_656 : ∀ t : ℝ, (1236693944867 / 1000000000000 : ℝ) < t → t ≤ (38642802243627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9622539316813 / 7750000000000 : ℝ) with h | h
  · exact I_654 t h1 h
  · exact I_655 t h h2

lemma J_652_656 : ∀ t : ℝ, (38032222338127 / 31000000000000 : ℝ) < t → t ≤ (38642802243627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1236693944867 / 1000000000000 : ℝ) with h | h
  · exact J_652_654 t h1 h
  · exact J_654_656 t h h2

lemma J_649_656 : ∀ t : ℝ, (18787143704501 / 15500000000000 : ℝ) < t → t ≤ (38642802243627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (38032222338127 / 31000000000000 : ℝ) with h | h
  · exact J_649_652 t h1 h
  · exact J_652_656 t h h2

lemma J_643_656 : ∀ t : ℝ, (1145575548461 / 968750000000 : ℝ) < t → t ≤ (38642802243627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (18787143704501 / 15500000000000 : ℝ) with h | h
  · exact J_643_649 t h1 h
  · exact J_649_656 t h h2

lemma J_631_656 : ∀ t : ℝ, (8706669458563 / 7750000000000 : ℝ) < t → t ≤ (38642802243627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1145575548461 / 968750000000 : ℝ) with h | h
  · exact J_631_643 t h1 h
  · exact J_643_656 t h h2

lemma J_606_656 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (38642802243627 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (8706669458563 / 7750000000000 : ℝ) with h | h
  · exact J_606_631 t h1 h
  · exact J_631_656 t h h2

lemma J_657_659 : ∀ t : ℝ, (19397723610001 / 15500000000000 : ℝ) < t → t ≤ (2443796073297 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (38948092196377 / 31000000000000 : ℝ) with h | h
  · exact I_657 t h1 h
  · exact I_658 t h h2

lemma J_656_659 : ∀ t : ℝ, (38642802243627 / 31000000000000 : ℝ) < t → t ≤ (2443796073297 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (19397723610001 / 15500000000000 : ℝ) with h | h
  · exact I_656 t h1 h
  · exact J_657_659 t h h2

lemma J_660_662 : ∀ t : ℝ, (39253382149127 / 31000000000000 : ℝ) < t → t ≤ (39558672101877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (19703013562751 / 15500000000000 : ℝ) with h | h
  · exact I_660 t h1 h
  · exact I_661 t h h2

lemma J_659_662 : ∀ t : ℝ, (2443796073297 / 1937500000000 : ℝ) < t → t ≤ (39558672101877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (39253382149127 / 31000000000000 : ℝ) with h | h
  · exact I_659 t h1 h
  · exact J_660_662 t h h2

lemma J_656_662 : ∀ t : ℝ, (38642802243627 / 31000000000000 : ℝ) < t → t ≤ (39558672101877 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2443796073297 / 1937500000000 : ℝ) with h | h
  · exact J_656_659 t h1 h
  · exact J_659_662 t h h2

lemma J_663_665 : ∀ t : ℝ, (9927829269563 / 7750000000000 : ℝ) < t → t ≤ (20008303515501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (39863962054627 / 31000000000000 : ℝ) with h | h
  · exact I_663 t h1 h
  · exact I_664 t h h2

lemma J_662_665 : ∀ t : ℝ, (39558672101877 / 31000000000000 : ℝ) < t → t ≤ (20008303515501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9927829269563 / 7750000000000 : ℝ) with h | h
  · exact I_662 t h1 h
  · exact J_663_665 t h h2

lemma J_666_668 : ∀ t : ℝ, (40169252007377 / 31000000000000 : ℝ) < t → t ≤ (40474541960127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5040237122969 / 3875000000000 : ℝ) with h | h
  · exact I_666 t h1 h
  · exact I_667 t h h2

lemma J_665_668 : ∀ t : ℝ, (20008303515501 / 15500000000000 : ℝ) < t → t ≤ (40474541960127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (40169252007377 / 31000000000000 : ℝ) with h | h
  · exact I_665 t h1 h
  · exact J_666_668 t h h2

lemma J_662_668 : ∀ t : ℝ, (39558672101877 / 31000000000000 : ℝ) < t → t ≤ (40474541960127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (20008303515501 / 15500000000000 : ℝ) with h | h
  · exact J_662_665 t h1 h
  · exact J_665_668 t h h2

lemma J_656_668 : ∀ t : ℝ, (38642802243627 / 31000000000000 : ℝ) < t → t ≤ (40474541960127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (39558672101877 / 31000000000000 : ℝ) with h | h
  · exact J_656_662 t h1 h
  · exact J_662_668 t h h2

lemma J_669_671 : ∀ t : ℝ, (20313593468251 / 15500000000000 : ℝ) < t → t ≤ (10233119222313 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (40779831912877 / 31000000000000 : ℝ) with h | h
  · exact I_669 t h1 h
  · exact I_670 t h h2

lemma J_668_671 : ∀ t : ℝ, (40474541960127 / 31000000000000 : ℝ) < t → t ≤ (10233119222313 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (20313593468251 / 15500000000000 : ℝ) with h | h
  · exact I_668 t h1 h
  · exact J_669_671 t h h2

lemma J_672_674 : ∀ t : ℝ, (41085121865627 / 31000000000000 : ℝ) < t → t ≤ (41390411818377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (20618883421001 / 15500000000000 : ℝ) with h | h
  · exact I_672 t h1 h
  · exact I_673 t h h2

lemma J_671_674 : ∀ t : ℝ, (10233119222313 / 7750000000000 : ℝ) < t → t ≤ (41390411818377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (41085121865627 / 31000000000000 : ℝ) with h | h
  · exact I_671 t h1 h
  · exact J_672_674 t h h2

lemma J_668_674 : ∀ t : ℝ, (40474541960127 / 31000000000000 : ℝ) < t → t ≤ (41390411818377 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (10233119222313 / 7750000000000 : ℝ) with h | h
  · exact J_668_671 t h1 h
  · exact J_671_674 t h h2

lemma J_675_677 : ∀ t : ℝ, (324555131209 / 242187500000 : ℝ) < t → t ≤ (20924173373751 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (41695701771127 / 31000000000000 : ℝ) with h | h
  · exact I_675 t h1 h
  · exact I_676 t h h2

lemma J_674_677 : ∀ t : ℝ, (41390411818377 / 31000000000000 : ℝ) < t → t ≤ (20924173373751 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (324555131209 / 242187500000 : ℝ) with h | h
  · exact I_674 t h1 h
  · exact J_675_677 t h h2

lemma J_677_679 : ∀ t : ℝ, (20924173373751 / 15500000000000 : ℝ) < t → t ≤ (10538409175063 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (42000991723877 / 31000000000000 : ℝ) with h | h
  · exact I_677 t h1 h
  · exact I_678 t h h2

lemma J_679_681 : ∀ t : ℝ, (10538409175063 / 7750000000000 : ℝ) < t → t ≤ (21229463326501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (42306281676627 / 31000000000000 : ℝ) with h | h
  · exact I_679 t h1 h
  · exact I_680 t h h2

lemma J_677_681 : ∀ t : ℝ, (20924173373751 / 15500000000000 : ℝ) < t → t ≤ (21229463326501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (10538409175063 / 7750000000000 : ℝ) with h | h
  · exact J_677_679 t h1 h
  · exact J_679_681 t h h2

lemma J_674_681 : ∀ t : ℝ, (41390411818377 / 31000000000000 : ℝ) < t → t ≤ (21229463326501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (20924173373751 / 15500000000000 : ℝ) with h | h
  · exact J_674_677 t h1 h
  · exact J_677_681 t h h2

lemma J_668_681 : ∀ t : ℝ, (40474541960127 / 31000000000000 : ℝ) < t → t ≤ (21229463326501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (41390411818377 / 31000000000000 : ℝ) with h | h
  · exact J_668_674 t h1 h
  · exact J_674_681 t h h2

lemma J_656_681 : ∀ t : ℝ, (38642802243627 / 31000000000000 : ℝ) < t → t ≤ (21229463326501 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (40474541960127 / 31000000000000 : ℝ) with h | h
  · exact J_656_668 t h1 h
  · exact J_668_681 t h h2

lemma J_682_684 : ∀ t : ℝ, (42611571629377 / 31000000000000 : ℝ) < t → t ≤ (42916861582127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5345527075719 / 3875000000000 : ℝ) with h | h
  · exact I_682 t h1 h
  · exact I_683 t h h2

lemma J_681_684 : ∀ t : ℝ, (21229463326501 / 15500000000000 : ℝ) < t → t ≤ (42916861582127 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (42611571629377 / 31000000000000 : ℝ) with h | h
  · exact I_681 t h1 h
  · exact J_682_684 t h h2

lemma J_685_687 : ∀ t : ℝ, (694669460621 / 500000000000 : ℝ) < t → t ≤ (43374837097881 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (86444343656383 / 62000000000000 : ℝ) with h | h
  · exact I_685 t h1 h
  · exact I_686 t h h2

lemma J_684_687 : ∀ t : ℝ, (42916861582127 / 31000000000000 : ℝ) < t → t ≤ (43374837097881 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (694669460621 / 500000000000 : ℝ) with h | h
  · exact I_684 t h1 h
  · exact J_685_687 t h h2

lemma J_681_687 : ∀ t : ℝ, (21229463326501 / 15500000000000 : ℝ) < t → t ≤ (43374837097881 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (42916861582127 / 31000000000000 : ℝ) with h | h
  · exact J_681_684 t h1 h
  · exact J_684_687 t h h2

lemma J_688_690 : ∀ t : ℝ, (87055004735141 / 62000000000000 : ℝ) < t → t ≤ (87665665813899 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2184008381863 / 1550000000000 : ℝ) with h | h
  · exact I_688 t h1 h
  · exact I_689 t h h2

lemma J_687_690 : ∀ t : ℝ, (43374837097881 / 31000000000000 : ℝ) < t → t ≤ (87665665813899 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (87055004735141 / 62000000000000 : ℝ) with h | h
  · exact I_687 t h1 h
  · exact J_688_690 t h h2

lemma J_690_692 : ∀ t : ℝ, (87665665813899 / 62000000000000 : ℝ) < t → t ≤ (88276326892657 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (43985498176639 / 31000000000000 : ℝ) with h | h
  · exact I_690 t h1 h
  · exact I_691 t h h2

lemma J_692_694 : ∀ t : ℝ, (88276326892657 / 62000000000000 : ℝ) < t → t ≤ (17777397594283 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (22145414358009 / 15500000000000 : ℝ) with h | h
  · exact I_692 t h1 h
  · exact I_693 t h h2

lemma J_690_694 : ∀ t : ℝ, (87665665813899 / 62000000000000 : ℝ) < t → t ≤ (17777397594283 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (88276326892657 / 62000000000000 : ℝ) with h | h
  · exact J_690_692 t h1 h
  · exact J_692_694 t h h2

lemma J_687_694 : ∀ t : ℝ, (43374837097881 / 31000000000000 : ℝ) < t → t ≤ (17777397594283 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (87665665813899 / 62000000000000 : ℝ) with h | h
  · exact J_687_690 t h1 h
  · exact J_690_694 t h h2

lemma J_681_694 : ∀ t : ℝ, (21229463326501 / 15500000000000 : ℝ) < t → t ≤ (17777397594283 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (43374837097881 / 31000000000000 : ℝ) with h | h
  · exact J_681_687 t h1 h
  · exact J_687_694 t h h2

lemma J_695_697 : ∀ t : ℝ, (44596159255397 / 31000000000000 : ℝ) < t → t ≤ (5612686224347 / 3875000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (89497649050173 / 62000000000000 : ℝ) with h | h
  · exact I_695 t h1 h
  · exact I_696 t h h2

lemma J_694_697 : ∀ t : ℝ, (17777397594283 / 12400000000000 : ℝ) < t → t ≤ (5612686224347 / 3875000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (44596159255397 / 31000000000000 : ℝ) with h | h
  · exact I_694 t h1 h
  · exact J_695_697 t h h2

lemma J_698_700 : ∀ t : ℝ, (90108310128931 / 62000000000000 : ℝ) < t → t ≤ (90718971207689 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9041364066831 / 6200000000000 : ℝ) with h | h
  · exact I_698 t h1 h
  · exact I_699 t h h2

lemma J_697_700 : ∀ t : ℝ, (5612686224347 / 3875000000000 : ℝ) < t → t ≤ (90718971207689 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (90108310128931 / 62000000000000 : ℝ) with h | h
  · exact I_697 t h1 h
  · exact J_698_700 t h h2

lemma J_694_700 : ∀ t : ℝ, (17777397594283 / 12400000000000 : ℝ) < t → t ≤ (90718971207689 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5612686224347 / 3875000000000 : ℝ) with h | h
  · exact J_694_697 t h1 h
  · exact J_697_700 t h h2

lemma J_701_703 : ∀ t : ℝ, (22756075436767 / 15500000000000 : ℝ) < t → t ≤ (45817481412913 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (91329632286447 / 62000000000000 : ℝ) with h | h
  · exact I_701 t h1 h
  · exact I_702 t h h2

lemma J_700_703 : ∀ t : ℝ, (90718971207689 / 62000000000000 : ℝ) < t → t ≤ (45817481412913 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (22756075436767 / 15500000000000 : ℝ) with h | h
  · exact I_700 t h1 h
  · exact J_701_703 t h h2

lemma J_703_705 : ∀ t : ℝ, (45817481412913 / 31000000000000 : ℝ) < t → t ≤ (11530702988073 / 7750000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (18388058673041 / 12400000000000 : ℝ) with h | h
  · exact I_703 t h1 h
  · exact I_704 t h h2

lemma J_705_707 : ∀ t : ℝ, (11530702988073 / 7750000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (92550954443963 / 62000000000000 : ℝ) with h | h
  · exact I_705 t h1 h
  · exact I_706 t h h2

lemma J_703_707 : ∀ t : ℝ, (45817481412913 / 31000000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (11530702988073 / 7750000000000 : ℝ) with h | h
  · exact J_703_705 t h1 h
  · exact J_705_707 t h h2

lemma J_700_707 : ∀ t : ℝ, (90718971207689 / 62000000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (45817481412913 / 31000000000000 : ℝ) with h | h
  · exact J_700_703 t h1 h
  · exact J_703_707 t h h2

lemma J_694_707 : ∀ t : ℝ, (17777397594283 / 12400000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (90718971207689 / 62000000000000 : ℝ) with h | h
  · exact J_694_700 t h1 h
  · exact J_700_707 t h h2

lemma J_681_707 : ∀ t : ℝ, (21229463326501 / 15500000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (17777397594283 / 12400000000000 : ℝ) with h | h
  · exact J_681_694 t h1 h
  · exact J_694_707 t h h2

lemma J_656_707 : ∀ t : ℝ, (38642802243627 / 31000000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (21229463326501 / 15500000000000 : ℝ) with h | h
  · exact J_656_681 t h1 h
  · exact J_681_707 t h h2

lemma J_606_707 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (46428142491671 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (38642802243627 / 31000000000000 : ℝ) with h | h
  · exact J_606_656 t h1 h
  · exact J_656_707 t h h2

lemma J_708_710 : ∀ t : ℝ, (93161615522721 / 62000000000000 : ℝ) < t → t ≤ (93772276601479 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (934669460621 / 620000000000 : ℝ) with h | h
  · exact I_708 t h1 h
  · exact I_709 t h h2

lemma J_707_710 : ∀ t : ℝ, (46428142491671 / 31000000000000 : ℝ) < t → t ≤ (93772276601479 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (93161615522721 / 62000000000000 : ℝ) with h | h
  · exact I_707 t h1 h
  · exact J_708_710 t h h2

lemma J_711_713 : ∀ t : ℝ, (47038803570429 / 31000000000000 : ℝ) < t → t ≤ (2959008381863 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (94382937680237 / 62000000000000 : ℝ) with h | h
  · exact I_711 t h1 h
  · exact I_712 t h h2

lemma J_710_713 : ∀ t : ℝ, (93772276601479 / 62000000000000 : ℝ) < t → t ≤ (2959008381863 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (47038803570429 / 31000000000000 : ℝ) with h | h
  · exact I_710 t h1 h
  · exact J_711_713 t h h2

lemma J_707_713 : ∀ t : ℝ, (46428142491671 / 31000000000000 : ℝ) < t → t ≤ (2959008381863 / 1937500000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (93772276601479 / 62000000000000 : ℝ) with h | h
  · exact J_707_710 t h1 h
  · exact J_710_713 t h h2

lemma J_714_716 : ∀ t : ℝ, (18998719751799 / 12400000000000 : ℝ) < t → t ≤ (3084008381863 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (47649464649187 / 31000000000000 : ℝ) with h | h
  · exact I_714 t h1 h
  · exact I_715 t h h2

lemma J_713_716 : ∀ t : ℝ, (2959008381863 / 1937500000000 : ℝ) < t → t ≤ (3084008381863 / 2000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (18998719751799 / 12400000000000 : ℝ) with h | h
  · exact I_713 t h1 h
  · exact J_714_716 t h h2

lemma J_717_719 : ∀ t : ℝ, (23977397594283 / 15500000000000 : ℝ) < t → t ≤ (9652025145589 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (96214920916511 / 62000000000000 : ℝ) with h | h
  · exact I_717 t h1 h
  · exact I_718 t h h2

lemma J_716_719 : ∀ t : ℝ, (3084008381863 / 2000000000000 : ℝ) < t → t ≤ (9652025145589 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (23977397594283 / 15500000000000 : ℝ) with h | h
  · exact I_716 t h1 h
  · exact J_717_719 t h h2

lemma J_713_719 : ∀ t : ℝ, (2959008381863 / 1937500000000 : ℝ) < t → t ≤ (9652025145589 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3084008381863 / 2000000000000 : ℝ) with h | h
  · exact J_713_716 t h1 h
  · exact J_716_719 t h h2

lemma J_707_719 : ∀ t : ℝ, (46428142491671 / 31000000000000 : ℝ) < t → t ≤ (9652025145589 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2959008381863 / 1937500000000 : ℝ) with h | h
  · exact J_707_713 t h1 h
  · exact J_713_719 t h h2

lemma J_720_722 : ∀ t : ℝ, (96825581995269 / 62000000000000 : ℝ) < t → t ≤ (97436243074027 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12141364066831 / 7750000000000 : ℝ) with h | h
  · exact I_720 t h1 h
  · exact I_721 t h h2

lemma J_719_722 : ∀ t : ℝ, (9652025145589 / 6200000000000 : ℝ) < t → t ≤ (97436243074027 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (96825581995269 / 62000000000000 : ℝ) with h | h
  · exact I_719 t h1 h
  · exact J_720_722 t h h2

lemma J_723_725 : ∀ t : ℝ, (48870786806703 / 31000000000000 : ℝ) < t → t ≤ (24588058673041 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (19609380830557 / 12400000000000 : ℝ) with h | h
  · exact I_723 t h1 h
  · exact I_724 t h h2

lemma J_722_725 : ∀ t : ℝ, (97436243074027 / 62000000000000 : ℝ) < t → t ≤ (24588058673041 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (48870786806703 / 31000000000000 : ℝ) with h | h
  · exact I_722 t h1 h
  · exact J_723_725 t h h2

lemma J_719_725 : ∀ t : ℝ, (9652025145589 / 6200000000000 : ℝ) < t → t ≤ (24588058673041 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (97436243074027 / 62000000000000 : ℝ) with h | h
  · exact J_719_722 t h1 h
  · exact J_722_725 t h h2

lemma J_726_728 : ∀ t : ℝ, (98657565231543 / 62000000000000 : ℝ) < t → t ≤ (99268226310301 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (49481447885461 / 31000000000000 : ℝ) with h | h
  · exact I_726 t h1 h
  · exact I_727 t h h2

lemma J_725_728 : ∀ t : ℝ, (24588058673041 / 15500000000000 : ℝ) < t → t ≤ (99268226310301 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (98657565231543 / 62000000000000 : ℝ) with h | h
  · exact I_725 t h1 h
  · exact J_726_728 t h h2

lemma J_728_730 : ∀ t : ℝ, (99268226310301 / 62000000000000 : ℝ) < t → t ≤ (99878887389059 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1244669460621 / 775000000000 : ℝ) with h | h
  · exact I_728 t h1 h
  · exact I_729 t h h2

lemma J_730_732 : ∀ t : ℝ, (99878887389059 / 62000000000000 : ℝ) < t → t ≤ (100489548467817 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (50092108964219 / 31000000000000 : ℝ) with h | h
  · exact I_730 t h1 h
  · exact I_731 t h h2

lemma J_728_732 : ∀ t : ℝ, (99268226310301 / 62000000000000 : ℝ) < t → t ≤ (100489548467817 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (99878887389059 / 62000000000000 : ℝ) with h | h
  · exact J_728_730 t h1 h
  · exact J_730_732 t h h2

lemma J_725_732 : ∀ t : ℝ, (24588058673041 / 15500000000000 : ℝ) < t → t ≤ (100489548467817 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (99268226310301 / 62000000000000 : ℝ) with h | h
  · exact J_725_728 t h1 h
  · exact J_728_732 t h h2

lemma J_719_732 : ∀ t : ℝ, (9652025145589 / 6200000000000 : ℝ) < t → t ≤ (100489548467817 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (24588058673041 / 15500000000000 : ℝ) with h | h
  · exact J_719_725 t h1 h
  · exact J_725_732 t h h2

lemma J_707_732 : ∀ t : ℝ, (46428142491671 / 31000000000000 : ℝ) < t → t ≤ (100489548467817 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (9652025145589 / 6200000000000 : ℝ) with h | h
  · exact J_707_719 t h1 h
  · exact J_719_732 t h h2

lemma J_733_735 : ∀ t : ℝ, (25198719751799 / 15500000000000 : ℝ) < t → t ≤ (50702770042977 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4044008381863 / 2480000000000 : ℝ) with h | h
  · exact I_733 t h1 h
  · exact I_734 t h h2

lemma J_732_735 : ∀ t : ℝ, (100489548467817 / 62000000000000 : ℝ) < t → t ≤ (50702770042977 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (25198719751799 / 15500000000000 : ℝ) with h | h
  · exact I_732 t h1 h
  · exact J_733_735 t h h2

lemma J_736_738 : ∀ t : ℝ, (101710870625333 / 62000000000000 : ℝ) < t → t ≤ (102321531704091 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12752025145589 / 7750000000000 : ℝ) with h | h
  · exact I_736 t h1 h
  · exact I_737 t h h2

lemma J_735_738 : ∀ t : ℝ, (50702770042977 / 31000000000000 : ℝ) < t → t ≤ (102321531704091 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (101710870625333 / 62000000000000 : ℝ) with h | h
  · exact I_735 t h1 h
  · exact J_736_738 t h h2

lemma J_732_738 : ∀ t : ℝ, (100489548467817 / 62000000000000 : ℝ) < t → t ≤ (102321531704091 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (50702770042977 / 31000000000000 : ℝ) with h | h
  · exact J_732_735 t h1 h
  · exact J_735_738 t h h2

lemma J_739_741 : ∀ t : ℝ, (10262686224347 / 6200000000000 : ℝ) < t → t ≤ (25809380830557 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (102932192782849 / 62000000000000 : ℝ) with h | h
  · exact I_739 t h1 h
  · exact I_740 t h h2

lemma J_738_741 : ∀ t : ℝ, (102321531704091 / 62000000000000 : ℝ) < t → t ≤ (25809380830557 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (10262686224347 / 6200000000000 : ℝ) with h | h
  · exact I_738 t h1 h
  · exact J_739_741 t h h2

lemma J_741_743 : ∀ t : ℝ, (25809380830557 / 15500000000000 : ℝ) < t → t ≤ (51924092200493 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (103542853861607 / 62000000000000 : ℝ) with h | h
  · exact I_741 t h1 h
  · exact I_742 t h h2

lemma J_743_745 : ∀ t : ℝ, (51924092200493 / 31000000000000 : ℝ) < t → t ≤ (1632169460621 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (20830702988073 / 12400000000000 : ℝ) with h | h
  · exact I_743 t h1 h
  · exact I_744 t h h2

lemma J_741_745 : ∀ t : ℝ, (25809380830557 / 15500000000000 : ℝ) < t → t ≤ (1632169460621 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (51924092200493 / 31000000000000 : ℝ) with h | h
  · exact J_741_743 t h1 h
  · exact J_743_745 t h h2

lemma J_738_745 : ∀ t : ℝ, (102321531704091 / 62000000000000 : ℝ) < t → t ≤ (1632169460621 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (25809380830557 / 15500000000000 : ℝ) with h | h
  · exact J_738_741 t h1 h
  · exact J_741_745 t h h2

lemma J_732_745 : ∀ t : ℝ, (100489548467817 / 62000000000000 : ℝ) < t → t ≤ (1632169460621 / 968750000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (102321531704091 / 62000000000000 : ℝ) with h | h
  · exact J_732_738 t h1 h
  · exact J_738_745 t h h2

lemma J_746_748 : ∀ t : ℝ, (104764176019123 / 62000000000000 : ℝ) < t → t ≤ (105374837097881 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1694669460621 / 1000000000000 : ℝ) with h | h
  · exact I_746 t h1 h
  · exact I_747 t h h2

lemma J_745_748 : ∀ t : ℝ, (1632169460621 / 968750000000 : ℝ) < t → t ≤ (105374837097881 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (104764176019123 / 62000000000000 : ℝ) with h | h
  · exact I_745 t h1 h
  · exact J_746_748 t h h2

lemma J_749_751 : ∀ t : ℝ, (5284008381863 / 3100000000000 : ℝ) < t → t ≤ (53145414358009 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (105985498176639 / 62000000000000 : ℝ) with h | h
  · exact I_749 t h1 h
  · exact I_750 t h h2

lemma J_748_751 : ∀ t : ℝ, (105374837097881 / 62000000000000 : ℝ) < t → t ≤ (53145414358009 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5284008381863 / 3100000000000 : ℝ) with h | h
  · exact I_748 t h1 h
  · exact J_749_751 t h h2

lemma J_745_751 : ∀ t : ℝ, (1632169460621 / 968750000000 : ℝ) < t → t ≤ (53145414358009 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (105374837097881 / 62000000000000 : ℝ) with h | h
  · exact J_745_748 t h1 h
  · exact J_748_751 t h h2

lemma J_752_754 : ∀ t : ℝ, (106596159255397 / 62000000000000 : ℝ) < t → t ≤ (21441364066831 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (13362686224347 / 7750000000000 : ℝ) with h | h
  · exact I_752 t h1 h
  · exact I_753 t h h2

lemma J_751_754 : ∀ t : ℝ, (53145414358009 / 31000000000000 : ℝ) < t → t ≤ (21441364066831 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (106596159255397 / 62000000000000 : ℝ) with h | h
  · exact I_751 t h1 h
  · exact J_752_754 t h h2

lemma J_754_756 : ∀ t : ℝ, (21441364066831 / 12400000000000 : ℝ) < t → t ≤ (107817481412913 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (53756075436767 / 31000000000000 : ℝ) with h | h
  · exact I_754 t h1 h
  · exact I_755 t h h2

lemma J_756_758 : ∀ t : ℝ, (107817481412913 / 62000000000000 : ℝ) < t → t ≤ (108428142491671 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27030702988073 / 15500000000000 : ℝ) with h | h
  · exact I_756 t h1 h
  · exact I_757 t h h2

lemma J_754_758 : ∀ t : ℝ, (21441364066831 / 12400000000000 : ℝ) < t → t ≤ (108428142491671 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (107817481412913 / 62000000000000 : ℝ) with h | h
  · exact J_754_756 t h1 h
  · exact J_756_758 t h h2

lemma J_751_758 : ∀ t : ℝ, (53145414358009 / 31000000000000 : ℝ) < t → t ≤ (108428142491671 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (21441364066831 / 12400000000000 : ℝ) with h | h
  · exact J_751_754 t h1 h
  · exact J_754_758 t h h2

lemma J_745_758 : ∀ t : ℝ, (1632169460621 / 968750000000 : ℝ) < t → t ≤ (108428142491671 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (53145414358009 / 31000000000000 : ℝ) with h | h
  · exact J_745_751 t h1 h
  · exact J_751_758 t h h2

lemma J_732_758 : ∀ t : ℝ, (100489548467817 / 62000000000000 : ℝ) < t → t ≤ (108428142491671 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (1632169460621 / 968750000000 : ℝ) with h | h
  · exact J_732_745 t h1 h
  · exact J_745_758 t h h2

lemma J_707_758 : ∀ t : ℝ, (46428142491671 / 31000000000000 : ℝ) < t → t ≤ (108428142491671 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (100489548467817 / 62000000000000 : ℝ) with h | h
  · exact J_707_732 t h1 h
  · exact J_732_758 t h h2

lemma J_759_761 : ∀ t : ℝ, (2174669460621 / 1240000000000 : ℝ) < t → t ≤ (6834008381863 / 3875000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (109038803570429 / 62000000000000 : ℝ) with h | h
  · exact I_759 t h1 h
  · exact I_760 t h h2

lemma J_758_761 : ∀ t : ℝ, (108428142491671 / 62000000000000 : ℝ) < t → t ≤ (6834008381863 / 3875000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2174669460621 / 1240000000000 : ℝ) with h | h
  · exact I_758 t h1 h
  · exact J_759_761 t h h2

lemma J_762_764 : ∀ t : ℝ, (109649464649187 / 62000000000000 : ℝ) < t → t ≤ (22052025145589 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (54977397594283 / 31000000000000 : ℝ) with h | h
  · exact I_762 t h1 h
  · exact I_763 t h h2

lemma J_761_764 : ∀ t : ℝ, (6834008381863 / 3875000000000 : ℝ) < t → t ≤ (22052025145589 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (109649464649187 / 62000000000000 : ℝ) with h | h
  · exact I_761 t h1 h
  · exact J_762_764 t h h2

lemma J_758_764 : ∀ t : ℝ, (108428142491671 / 62000000000000 : ℝ) < t → t ≤ (22052025145589 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (6834008381863 / 3875000000000 : ℝ) with h | h
  · exact J_758_761 t h1 h
  · exact J_761_764 t h h2

lemma J_765_767 : ∀ t : ℝ, (27641364066831 / 15500000000000 : ℝ) < t → t ≤ (55588058673041 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (110870786806703 / 62000000000000 : ℝ) with h | h
  · exact I_765 t h1 h
  · exact I_766 t h h2

lemma J_764_767 : ∀ t : ℝ, (22052025145589 / 12400000000000 : ℝ) < t → t ≤ (55588058673041 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (27641364066831 / 15500000000000 : ℝ) with h | h
  · exact I_764 t h1 h
  · exact J_765_767 t h h2

lemma J_768_770 : ∀ t : ℝ, (111481447885461 / 62000000000000 : ℝ) < t → t ≤ (112092108964219 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (2794669460621 / 1550000000000 : ℝ) with h | h
  · exact I_768 t h1 h
  · exact I_769 t h h2

lemma J_767_770 : ∀ t : ℝ, (55588058673041 / 31000000000000 : ℝ) < t → t ≤ (112092108964219 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (111481447885461 / 62000000000000 : ℝ) with h | h
  · exact I_767 t h1 h
  · exact J_768_770 t h h2

lemma J_764_770 : ∀ t : ℝ, (22052025145589 / 12400000000000 : ℝ) < t → t ≤ (112092108964219 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (55588058673041 / 31000000000000 : ℝ) with h | h
  · exact J_764_767 t h1 h
  · exact J_767_770 t h h2

lemma J_758_770 : ∀ t : ℝ, (108428142491671 / 62000000000000 : ℝ) < t → t ≤ (112092108964219 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (22052025145589 / 12400000000000 : ℝ) with h | h
  · exact J_758_764 t h1 h
  · exact J_764_770 t h h2

lemma J_771_773 : ∀ t : ℝ, (56198719751799 / 31000000000000 : ℝ) < t → t ≤ (28252025145589 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (112702770042977 / 62000000000000 : ℝ) with h | h
  · exact I_771 t h1 h
  · exact I_772 t h h2

lemma J_770_773 : ∀ t : ℝ, (112092108964219 / 62000000000000 : ℝ) < t → t ≤ (28252025145589 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (56198719751799 / 31000000000000 : ℝ) with h | h
  · exact I_770 t h1 h
  · exact J_771_773 t h h2

lemma J_774_776 : ∀ t : ℝ, (22662686224347 / 12400000000000 : ℝ) < t → t ≤ (113924092200493 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (56809380830557 / 31000000000000 : ℝ) with h | h
  · exact I_774 t h1 h
  · exact I_775 t h h2

lemma J_773_776 : ∀ t : ℝ, (28252025145589 / 15500000000000 : ℝ) < t → t ≤ (113924092200493 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (22662686224347 / 12400000000000 : ℝ) with h | h
  · exact I_773 t h1 h
  · exact J_774_776 t h h2

lemma J_770_776 : ∀ t : ℝ, (112092108964219 / 62000000000000 : ℝ) < t → t ≤ (113924092200493 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (28252025145589 / 15500000000000 : ℝ) with h | h
  · exact J_770_773 t h1 h
  · exact J_773_776 t h h2

lemma J_777_779 : ∀ t : ℝ, (3569669460621 / 1937500000000 : ℝ) < t → t ≤ (11484008381863 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3694669460621 / 2000000000000 : ℝ) with h | h
  · exact I_777 t h1 h
  · exact I_778 t h h2

lemma J_776_779 : ∀ t : ℝ, (113924092200493 / 62000000000000 : ℝ) < t → t ≤ (11484008381863 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (3569669460621 / 1937500000000 : ℝ) with h | h
  · exact I_776 t h1 h
  · exact J_777_779 t h h2

lemma J_779_781 : ∀ t : ℝ, (11484008381863 / 6200000000000 : ℝ) < t → t ≤ (28862686224347 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (115145414358009 / 62000000000000 : ℝ) with h | h
  · exact I_779 t h1 h
  · exact I_780 t h h2

lemma J_781_783 : ∀ t : ℝ, (28862686224347 / 15500000000000 : ℝ) < t → t ≤ (58030702988073 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (115756075436767 / 62000000000000 : ℝ) with h | h
  · exact I_781 t h1 h
  · exact I_782 t h h2

lemma J_779_783 : ∀ t : ℝ, (11484008381863 / 6200000000000 : ℝ) < t → t ≤ (58030702988073 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (28862686224347 / 15500000000000 : ℝ) with h | h
  · exact J_779_781 t h1 h
  · exact J_781_783 t h h2

lemma J_776_783 : ∀ t : ℝ, (113924092200493 / 62000000000000 : ℝ) < t → t ≤ (58030702988073 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (11484008381863 / 6200000000000 : ℝ) with h | h
  · exact J_776_779 t h1 h
  · exact J_779_783 t h h2

lemma J_770_783 : ∀ t : ℝ, (112092108964219 / 62000000000000 : ℝ) < t → t ≤ (58030702988073 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (113924092200493 / 62000000000000 : ℝ) with h | h
  · exact J_770_776 t h1 h
  · exact J_776_783 t h h2

lemma J_758_783 : ∀ t : ℝ, (108428142491671 / 62000000000000 : ℝ) < t → t ≤ (58030702988073 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (112092108964219 / 62000000000000 : ℝ) with h | h
  · exact J_758_770 t h1 h
  · exact J_770_783 t h h2

lemma J_784_786 : ∀ t : ℝ, (4654669460621 / 2480000000000 : ℝ) < t → t ≤ (116977397594283 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (14584008381863 / 7750000000000 : ℝ) with h | h
  · exact I_784 t h1 h
  · exact I_785 t h h2

lemma J_783_786 : ∀ t : ℝ, (58030702988073 / 31000000000000 : ℝ) < t → t ≤ (116977397594283 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (4654669460621 / 2480000000000 : ℝ) with h | h
  · exact I_783 t h1 h
  · exact J_784_786 t h h2

lemma J_787_789 : ∀ t : ℝ, (58641364066831 / 31000000000000 : ℝ) < t → t ≤ (5894669460621 / 3100000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (117588058673041 / 62000000000000 : ℝ) with h | h
  · exact I_787 t h1 h
  · exact I_788 t h h2

lemma J_786_789 : ∀ t : ℝ, (116977397594283 / 62000000000000 : ℝ) < t → t ≤ (5894669460621 / 3100000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (58641364066831 / 31000000000000 : ℝ) with h | h
  · exact I_786 t h1 h
  · exact J_787_789 t h h2

lemma J_783_789 : ∀ t : ℝ, (58030702988073 / 31000000000000 : ℝ) < t → t ≤ (5894669460621 / 3100000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (116977397594283 / 62000000000000 : ℝ) with h | h
  · exact J_783_786 t h1 h
  · exact J_786_789 t h h2

lemma J_790_792 : ∀ t : ℝ, (118198719751799 / 62000000000000 : ℝ) < t → t ≤ (118809380830557 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (59252025145589 / 31000000000000 : ℝ) with h | h
  · exact I_790 t h1 h
  · exact I_791 t h h2

lemma J_789_792 : ∀ t : ℝ, (5894669460621 / 3100000000000 : ℝ) < t → t ≤ (118809380830557 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (118198719751799 / 62000000000000 : ℝ) with h | h
  · exact I_789 t h1 h
  · exact J_790_792 t h h2

lemma J_792_794 : ∀ t : ℝ, (118809380830557 / 62000000000000 : ℝ) < t → t ≤ (23884008381863 / 12400000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (7444669460621 / 3875000000000 : ℝ) with h | h
  · exact I_792 t h1 h
  · exact I_793 t h h2

lemma J_794_796 : ∀ t : ℝ, (23884008381863 / 12400000000000 : ℝ) < t → t ≤ (120030702988073 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (59862686224347 / 31000000000000 : ℝ) with h | h
  · exact I_794 t h1 h
  · exact I_795 t h h2

lemma J_792_796 : ∀ t : ℝ, (118809380830557 / 62000000000000 : ℝ) < t → t ≤ (120030702988073 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (23884008381863 / 12400000000000 : ℝ) with h | h
  · exact J_792_794 t h1 h
  · exact J_794_796 t h h2

lemma J_789_796 : ∀ t : ℝ, (5894669460621 / 3100000000000 : ℝ) < t → t ≤ (120030702988073 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (118809380830557 / 62000000000000 : ℝ) with h | h
  · exact J_789_792 t h1 h
  · exact J_792_796 t h h2

lemma J_783_796 : ∀ t : ℝ, (58030702988073 / 31000000000000 : ℝ) < t → t ≤ (120030702988073 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (5894669460621 / 3100000000000 : ℝ) with h | h
  · exact J_783_789 t h1 h
  · exact J_789_796 t h h2

lemma J_797_799 : ∀ t : ℝ, (30084008381863 / 15500000000000 : ℝ) < t → t ≤ (12094669460621 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (120641364066831 / 62000000000000 : ℝ) with h | h
  · exact I_797 t h1 h
  · exact I_798 t h h2

lemma J_796_799 : ∀ t : ℝ, (120030702988073 / 62000000000000 : ℝ) < t → t ≤ (12094669460621 / 6200000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (30084008381863 / 15500000000000 : ℝ) with h | h
  · exact I_796 t h1 h
  · exact J_797_799 t h h2

lemma J_800_802 : ∀ t : ℝ, (121252025145589 / 62000000000000 : ℝ) < t → t ≤ (121862686224347 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (15194669460621 / 7750000000000 : ℝ) with h | h
  · exact I_800 t h1 h
  · exact I_801 t h h2

lemma J_799_802 : ∀ t : ℝ, (12094669460621 / 6200000000000 : ℝ) < t → t ≤ (121862686224347 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (121252025145589 / 62000000000000 : ℝ) with h | h
  · exact I_799 t h1 h
  · exact J_800_802 t h h2

lemma J_796_802 : ∀ t : ℝ, (120030702988073 / 62000000000000 : ℝ) < t → t ≤ (121862686224347 / 62000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (12094669460621 / 6200000000000 : ℝ) with h | h
  · exact J_796_799 t h1 h
  · exact J_799_802 t h h2

lemma J_803_805 : ∀ t : ℝ, (61084008381863 / 31000000000000 : ℝ) < t → t ≤ (30694669460621 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (24494669460621 / 12400000000000 : ℝ) with h | h
  · exact I_803 t h1 h
  · exact I_804 t h h2

lemma J_802_805 : ∀ t : ℝ, (121862686224347 / 62000000000000 : ℝ) < t → t ≤ (30694669460621 / 15500000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (61084008381863 / 31000000000000 : ℝ) with h | h
  · exact I_802 t h1 h
  · exact J_803_805 t h h2

lemma J_805_807 : ∀ t : ℝ, (30694669460621 / 15500000000000 : ℝ) < t → t ≤ (61694669460621 / 31000000000000 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (123084008381863 / 62000000000000 : ℝ) with h | h
  · exact I_805 t h1 h
  · exact I_806 t h h2

lemma J_807_809 : ∀ t : ℝ, (61694669460621 / 31000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (123694669460621 / 62000000000000 : ℝ) with h | h
  · exact I_807 t h1 h
  · exact I_808 t h h2

lemma J_805_809 : ∀ t : ℝ, (30694669460621 / 15500000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (61694669460621 / 31000000000000 : ℝ) with h | h
  · exact J_805_807 t h1 h
  · exact J_807_809 t h h2

lemma J_802_809 : ∀ t : ℝ, (121862686224347 / 62000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (30694669460621 / 15500000000000 : ℝ) with h | h
  · exact J_802_805 t h1 h
  · exact J_805_809 t h h2

lemma J_796_809 : ∀ t : ℝ, (120030702988073 / 62000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (121862686224347 / 62000000000000 : ℝ) with h | h
  · exact J_796_802 t h1 h
  · exact J_802_809 t h h2

lemma J_783_809 : ∀ t : ℝ, (58030702988073 / 31000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (120030702988073 / 62000000000000 : ℝ) with h | h
  · exact J_783_796 t h1 h
  · exact J_796_809 t h h2

lemma J_758_809 : ∀ t : ℝ, (108428142491671 / 62000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (58030702988073 / 31000000000000 : ℝ) with h | h
  · exact J_758_783 t h1 h
  · exact J_783_809 t h h2

lemma J_707_809 : ∀ t : ℝ, (46428142491671 / 31000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (108428142491671 / 62000000000000 : ℝ) with h | h
  · exact J_707_758 t h1 h
  · exact J_758_809 t h h2

lemma J_606_809 : ∀ t : ℝ, (31010553424877 / 31000000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (46428142491671 / 31000000000000 : ℝ) with h | h
  · exact J_606_707 t h1 h
  · exact J_707_809 t h h2

lemma J_404_809 : ∀ t : ℝ, (961044010771 / 6400000000000 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (31010553424877 / 31000000000000 : ℝ) with h | h
  · exact J_404_606 t h1 h
  · exact J_606_809 t h h2

lemma J_0_809 : ∀ t : ℝ, (0 : ℝ) < t → t ≤ (2 : ℝ) → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t h1 h2
  rcases le_or_gt t (961044010771 / 6400000000000 : ℝ) with h | h
  · exact J_0_404 t h1 h
  · exact J_404_809 t h h2

theorem potential_ineq_le_two : ∀ t : ℝ, 0 < t → t ≤ 2 → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := J_0_809

/-- 全 t 的位势不等式：(0, 2] 由分割证书，[2, ∞) 由尾部。 -/
theorem potential_ineq : ∀ t : ℝ, 0 < t → 2 * Uρ8 t - Vfield8 t ≤ M0_8 := by
  intro t ht
  rcases le_or_gt t 2 with h | h
  · exact potential_ineq_le_two t ht h
  · exact potential_ineq_tail8 (le_of_lt h)

end Zeta7
