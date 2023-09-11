Certainly! Here's a README.md for the problem of collecting all toys from cereal boxes, including both the mathematical and Monte Carlo simulation approaches:

---

# Cereal Toy Collection Analysis

This repository delves into the problem of collecting toys from cereal boxes. Each box contains one of 10 possible toys, with each toy having an equal chance of being in a box. Over a span of 20 weeks, with one box purchased each week, we want to analyze the probabilities of certain collection scenarios.

## Problem Statement

Each cereal box contains one toy, and there are 10 different types of toys: T1, T2, ..., T10. Each toy has a 1/10 probability of being in a box, independent of any other box. After 20 weeks (or 20 boxes), we want to determine:

1. The probability of having at least one copy of toy T1.
2. The probability of collecting all 10 different toys.

## Approaches

### 1. Mathematical Approach

Using probability theory and the inclusion-exclusion principle, we derived the probabilities for both scenarios.
1. 1 - (9/10)^20
2. ![IMG_B49FA85ED00A-1](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/dbf40564-9eeb-457f-b7d0-d9e3a0bec9e4)

### 2. Monte Carlo Simulation Approach

By simulating the toy collection process over a large number of trials, we estimated the probabilities for the two scenarios.

## Results

- **Mathematical Approach**:
  1. Probability of at least one T1: 87.84%.
  2. Probability of collecting all toys:

'# Single toy missing
prob_single_missing = 10 * (9/10)**20

# Two toys missing
choose_2_from_10 = 45  # 10 choose 2
prob_two_missing = choose_2_from_10 * (8/10)**20

# Three toys missing
choose_3_from_10 = 120  # 10 choose 3
prob_three_missing = choose_3_from_10 * (7/10)**20

# Four and more toys missing will have a very small probability over 20 trials, 
# so they can be ignored for this calculation.

# Using the inclusion-exclusion principle
prob_at_least_one_missing = prob_single_missing - prob_two_missing + prob_three_missing

# Probability of collecting all toys
prob_all_toys = 1 - prob_at_least_one_missing'

- **Monte Carlo Simulation**:
  1. Estimated probability of collecting all toys: 21.85%.


