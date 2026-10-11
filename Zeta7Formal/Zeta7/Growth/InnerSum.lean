import Mathlib
import Zeta7.Growth.InnerTable

set_option linter.unusedSimpArgs false
set_option linter.unusedTactic false
set_option maxHeartbeats 4000000

/-! 由 `gen_lean_b8.py` 生成：`Ê_in` 在 `[3, 20]` 上的表（b=8）。可采性界用新 kloI：`-2q-8`。 -/

namespace Zeta7

def tInL : List ℚ := [(3), (120/37), (160/49), (7/2), (180/49), (160/43), (140/37), (4), (200/49), (160/37), (40/9), (220/49), (9/2), (200/43), (180/37), (240/49), (5), (260/49), (200/37), (11/2), (240/43), (40/7), (220/37), (6), (300/49), (240/37), (13/2), (280/43), (320/49), (20/3), (340/49), (7), (260/37), (360/49), (320/43), (15/2), (280/37), (380/49), (8), (300/37), (400/49), (360/43), (17/2), (60/7), (320/37), (80/9), (440/49), (9), (340/37), (400/43), (460/49), (19/2), (360/37), (480/49), (10), (500/49), (440/43), (380/37), (21/2), (520/49), (400/37), (11), (540/49), (100/9), (480/43), (420/37), (80/7), (23/2), (580/49), (440/37), (12), (520/43), (600/49), (460/37), (25/2), (620/49), (480/37), (13), (560/43), (640/49), (40/3), (660/49), (27/2), (500/37), (680/49), (600/43), (14), (520/37), (100/7), (29/2), (540/37), (720/49), (640/43), (15), (740/49), (560/37), (31/2), (760/49), (140/9), (580/37), (680/43), (780/49), (16), (600/37), (800/49), (33/2), (820/49), (720/43), (620/37), (17), (120/7), (640/37), (35/2), (860/49), (760/43), (160/9), (660/37), (880/49), (18), (900/49), (680/37), (37/2), (800/43), (920/49), (700/37), (19), (940/49), (720/37), (39/2), (840/43), (960/49), (20)]
def kInL : List ℤ := [2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6, 7, 7, 7, 7, 8, 8, 9, 9, 9, 9, 10, 10, 10, 11, 11, 11, 11, 12, 13, 14, 14, 14, 15, 15, 15, 15, 16, 16, 16, 17, 17, 17, 18, 18, 19, 20, 20, 20, 20, 21, 21, 21, 22, 22, 23, 23, 23, 23, 24, 24, 24, 25, 26, 26, 26, 27, 27, 28, 28, 28, 28, 29, 29, 29, 30, 30, 30, 30, 31, 32, 33, 33, 33, 34, 34, 34, 34, 35, 35, 35, 36, 36, 36, 37, 37, 37, 38, 39, 39, 39, 40, 40, 40, 41, 41, 42, 42, 42, 42, 43, 43, 43, 44, 44, 45, 45, 46, 46, 47, 47, 47, 47, 48, 48, 48, 49, 49, 49, 49, 50]
def aInL : List ℚ := [(51/20), (81/10), (55/8), (63/8), (133/20), (47/20), (21/5), (67/20), (17/8), (307/40), (149/20), (249/40), (289/40), (117/40), (191/40), (71/20), (27/10), (59/40), (281/40), (321/40), (149/40), (5/2), (87/20), (7/2), (91/40), (313/40), (353/40), (181/40), (33/10), (219/40), (17/4), (17/5), (21/4), (161/40), (-11/40), (29/40), (251/40), (101/20), (21/5), (121/20), (193/40), (21/40), (61/40), (3/10), (117/20), (45/8), (22/5), (71/20), (27/5), (11/10), (-1/8), (7/8), (257/40), (26/5), (87/20), (25/8), (-47/40), (27/40), (67/40), (9/20), (6), (103/20), (157/40), (37/10), (-3/5), (5/4), (1/40), (41/40), (-1/5), (107/20), (9/2), (1/5), (-41/40), (33/40), (73/40), (3/5), (123/20), (53/10), (1), (-9/40), (67/4), (621/40), (661/40), (147/8), (343/20), (257/20), (12), (351/20), (653/40), (693/40), (767/40), (359/20), (273/20), (64/5), (463/40), (137/8), (145/8), (169/10), (667/40), (741/40), (569/40), (13), (243/20), (177/10), (659/40), (699/40), (65/4), (239/20), (69/5), (259/20), (469/40), (691/40), (731/40), (341/20), (51/4), (501/40), (115/8), (263/20), (123/10), (443/40), (133/8), (141/8), (533/40), (121/10), (279/20), (131/10), (95/8), (697/40), (737/40), (113/8), (129/10)]
def bInL : List ℚ := [(1), (-17), (-13), (-33/2), (-12), (4), (-3), (-7), (-2), (-26), (-25), (-39/2), (-24), (-4), (-13), (-7), (-12), (-11/2), (-71/2), (-41), (-17), (-10), (-21), (-27), (-39/2), (-111/2), (-62), (-34), (-26), (-81/2), (-32), (-39), (-52), (-43), (-11), (-37/2), (-121/2), (-51), (-59), (-74), (-64), (-28), (-73/2), (-26), (-74), (-72), (-61), (-70), (-87), (-47), (-71/2), (-45), (-99), (-87), (-97), (-169/2), (-81/2), (-119/2), (-70), (-57), (-117), (-128), (-229/2), (-112), (-64), (-85), (-71), (-165/2), (-68), (-134), (-146), (-94), (-79), (-102), (-229/2), (-99), (-171), (-184), (-128), (-112), (-141), (-249/2), (-138), (-163), (-146), (-86), (-100), (-178), (-321/2), (-175), (-202), (-184), (-120), (-135), (-233/2), (-401/2), (-216), (-197), (-387/2), (-445/2), (-309/2), (-135), (-151), (-241), (-221), (-475/2), (-217), (-145), (-176), (-193), (-172), (-268), (-571/2), (-264), (-188), (-184), (-217), (-195), (-213), (-381/2), (-585/2), (-311), (-231), (-208), (-243), (-262), (-477/2), (-693/2), (-366), (-282), (-258)]

noncomputable def tIn (i : ℕ) : ℝ := ((tInL.getD i 0 : ℚ) : ℝ)
def kIn (i : ℕ) : ℤ := kInL.getD i 0
noncomputable def gIn (i : ℕ) (x : ℝ) : ℝ := ((aInL.getD i 0 : ℚ) : ℝ) * x + ((bInL.getD i 0 : ℚ) : ℝ)

theorem tIn_mono : ∀ i < 131, tIn i < tIn (i + 1) := by
  intro i hi
  interval_cases i <;> simp only [tIn, tInL, List.getD_cons_succ, List.getD_cons_zero] <;> norm_num

theorem inner_table : ∀ i < 131, ∀ x ∈ Set.Ico (tIn i) (tIn (i + 1)), Ein x (kIn i) = gIn i x := by
  intro i hi x hx
  interval_cases i
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_0 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_1 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_2 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_3 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_4 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_5 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_6 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_7 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_8 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_9 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_10 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_11 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_12 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_13 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_14 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_15 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_16 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_17 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_18 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_19 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_20 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_21 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_22 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_23 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_24 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_25 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_26 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_27 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_28 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_29 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_30 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_31 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_32 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_33 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_34 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_35 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_36 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_37 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_38 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_39 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_40 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_41 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_42 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_43 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_44 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_45 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_46 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_47 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_48 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_49 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_50 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_51 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_52 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_53 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_54 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_55 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_56 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_57 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_58 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_59 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_60 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_61 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_62 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_63 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_64 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_65 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_66 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_67 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_68 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_69 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_70 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_71 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_72 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_73 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_74 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_75 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_76 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_77 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_78 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_79 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_80 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_81 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_82 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_83 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_84 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_85 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_86 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_87 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_88 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_89 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_90 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_91 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_92 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_93 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_94 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_95 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_96 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_97 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_98 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_99 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_100 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_101 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_102 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_103 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_104 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_105 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_106 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_107 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_108 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_109 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_110 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_111 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_112 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_113 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_114 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_115 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_116 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_117 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_118 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_119 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_120 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_121 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_122 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_123 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_124 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_125 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_126 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_127 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_128 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_129 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith
  · simp only [tIn, tInL, kIn, kInL, gIn, aInL, bInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx ⊢
    have := inPiece_130 x (by linarith [hx.1]) (by linarith [hx.2])
    linarith

theorem inner_table_k : ∀ i < 131, ∀ x ∈ Set.Ico (tIn i) (tIn (i + 1)),
    -2 * (⌊x⌋₊ : ℤ) - 8 ≤ kIn i ∧ kIn i ≤ 8 * (⌊x⌋₊ : ℤ) + 20 := by
  intro i hi x hx
  interval_cases i
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 3) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 4) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 5) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 6) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 7) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 8) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 9) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 10) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 11) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 12) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 13) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 14) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 15) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 16) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 17) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 18) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 19) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 19) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 19) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 19) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 19) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num
  · simp only [tIn, tInL, kIn, kInL, List.getD_cons_succ, List.getD_cons_zero, Set.mem_Ico] at hx ⊢
    push_cast at hx
    rw [nat_floor_of_bounds (q := 19) (by norm_num; linarith [hx.1]) (by norm_num; linarith [hx.2])]
    norm_num

end Zeta7