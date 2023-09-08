# Drunkard's Walk Simulation

## Introduction:
The Drunkard's Walk, also known as a random walk in two dimensions, is a classic stochastic or random process. In this problem, a "drunkard" starts at the origin of a two-dimensional grid and takes steps in random directions. The question we aim to answer is: after N steps, what is the expected distance the drunkard is from the starting point?

## Problem Statement:
Imagine a drunkard starting at the origin of a two-dimensional grid. At each step, the drunkard randomly moves one step either up, down, left, or right with equal probability. After N steps, what is the expected distance from the starting point?

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/6d20e75f-f828-41f7-b5e6-fba3ff8d3a4d)


## Methodology:

### Mathematical Approach:
The problem can be approached mathematically by considering the expected value of the distance after N steps. It's a complex problem due to the randomness and potential for the drunkard to return to earlier positions.

### Monte Carlo Simulation:
1. Simulate the drunkard's walk a large number of times (e.g., 100,000 simulations).
2. For each simulation, calculate the Euclidean distance from the starting point after N steps.
3. Average all the distances to determine the expected distance.

## Code:
The Python code in this repository simulates the Drunkard's Walk using the `random` module to determine the direction of each step.

## Results:
After simulating the Drunkard's Walk with 100 steps over 100,000 trials, the expected distance from the starting point was found to be approximately 8.87 units.

## Conclusion:
The Drunkard's Walk problem is a fascinating exploration into stochastic processes and the power of randomness. Despite taking a significant number of steps, the drunkard doesn't end up as far from the starting point as one might intuitively expect due to the random nature of the steps.
