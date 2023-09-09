# Lane Switching Probability Analysis

This repository explores the probability analysis of a driver switching lanes in a two-lane traffic scenario. The driver switches lanes based on given probabilities, and the objective is to determine the fraction of time the driver spends in the left lane.

## Problem Statement

As an impatient driver in a traffic jam on a two-lane highway:

- When in the left lane, the driver switches to the right lane with a probability of 50%.
- When in the right lane, the driver switches back to the left lane with a probability of 70%, assuming the left lane is faster.

The question: Over the long term, what fraction of time does the driver expect to spend in the left lane?

## Approaches

### 1. Mathematical Approach

The problem can be modeled using Markov chains, where the two states represent the left and right lanes. Let:
L represent the probability of being in the left lane.
R represent the probability of being in the right lane.

Given the problem statement:

1. When in the left lane:
   - Switch to the right lane with a probability of 50%. Thus, stay in the left lane with a probability of 50%.
2. When in the right lane:
   - Switch to the left lane with a probability of 70%. Thus, stay in the right lane with a probability of 30%.

From these probabilities, we can set up the following system of equations:

1. **L = 0.5L + 0.7R**
   - This represents the probability of staying in the left lane (either by staying there from the previous state or by switching from the right lane).
2. **L + R = 1**
   - This is based on the total probability, as the driver must be in one of the two lanes.

Solving this system of equations, we find:
L = 0.5833  about 58.33%.

### 2. Monte Carlo Simulation Approach

A simulation is run for a large number of iterations to mimic the driver's behavior of switching lanes based on the given probabilities. The fraction of iterations the driver spends in the left lane gives an estimate of the long-term behavior.

## Results

- Mathematical Approach: Approximately 58.33% of the time in the left lane.
- Monte Carlo Simulation: Approximately 58.31% of the time in the left lane (based on a simulation of 1,000,000 iterations).

