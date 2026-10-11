import Li2Rational.Completion

namespace Li2RationalAcceptance

theorem originalStatement :
    (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (-1 / 2 : ℝ) ^ (n + 1) / ((n : ℝ) + 1) ^ 2) ∧
    (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (1 / 2 : ℝ) ^ (n + 1) / ((n : ℝ) + 1) ^ 2) ∧
    (∀ k : ℕ, 3 ≤ k → (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (1 / (k : ℝ)) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) ∧
    (∀ k : ℕ, 13 ≤ k → (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (2 / (k : ℝ)) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) ∧
    (∀ k : ℕ, 56 ≤ k → (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (3 / (k : ℝ)) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) ∧
    (∀ p q : ℕ, 5 ≤ p → (1851/10000 : ℝ)*(p : ℝ)^(84/17 : ℝ) ≤ q →
      (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, ((p : ℝ) / q) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) ∧
    (∀ p q : ℕ, 5 ≤ p → (1851/10000 : ℝ)*(p : ℝ)^(84/17 : ℝ)+(27/17 : ℝ)*p ≤ q →
      (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (-(p : ℝ) / q) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) ∧
    (∀ p Q : ℕ, (p,Q) ∈ ([(1,3),
   (2,13),
   (3,56),
   (4,183),
   (5,520),
   (6,1286),
   (7,2764),
   (8,5355),
   (9,9591),
   (10,16149),
   (11,25871),
   (12,39775),
   (13,59079),
   (14,85212),
   (15,119834),
   (16,164852),
   (17,222435),
   (18,295034),
   (19,385393),
   (20,496571),
   (25,1495709),
   (50,45951536),
   (100,1411702110),
   (1000,123287652417772)] : List (ℕ × ℕ)) → ∀ q : ℕ, Q ≤ q →
      (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, ((p : ℝ) / q) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) ∧
    (∀ p Q : ℕ, (p,Q) ∈ ([(1,1),
   (2,16),
   (3,62),
   (4,194),
   (5,535),
   (6,1304),
   (7,2786),
   (8,5380),
   (9,9618),
   (10,16180),
   (11,25905),
   (12,39812),
   (13,59120),
   (14,85256),
   (15,119882),
   (16,164902),
   (17,222489),
   (18,295088),
   (19,385453),
   (20,496634),
   (25,1495788),
   (50,45951694),
   (100,1411702424),
   (1000,123287652420948)] : List (ℕ × ℕ)) → ∀ q : ℕ, Q ≤ q →
      (¬ ∃ a : ℚ, (a : ℝ) = ∑' n : ℕ, (-(p : ℝ) / q) ^ (n + 1) / ((n : ℝ) + 1) ^ 2)) :=
  ⟨Li2Rational.irrational_neg_half,
    Li2Rational.irrational_half,
    Li2Rational.irrational_reciprocal,
    Li2Rational.irrational_two_numerator,
    Li2Rational.irrational_three_numerator,
    Li2Rational.irrational_positive_of_power,
    Li2Rational.irrational_negative_of_power,
    Li2Rational.positive_table,
    Li2Rational.negative_table⟩

end Li2RationalAcceptance

#print axioms Li2RationalAcceptance.originalStatement
