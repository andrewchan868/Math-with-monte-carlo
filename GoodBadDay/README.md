# Monte Carlo Simulation: Good & Bad Days

## Description

This project simulates the transition between "Good" and "Bad" days based on certain probabilities. The goal is to determine, on average, how many days we have to wait until the next "Bad" day, given that today is a "Good" day.

## Problem Statement

- If a day is a "Good" day, there's a 60% chance that the next day will be "Good" and a 40% chance it will be "Bad".
- If a day is a "Bad" day, there's a 70% chance that the next day will be "Bad" and a 30% chance it will be "Good".

Starting from a "Good" day, the simulation estimates the average number of days until the next "Bad" day.

## Solution

### Mathematical Approach:

![IMG_65771BE86A1E-1](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/1f0e5371-ff95-408f-946f-124a08f73b77)

### Monte Carlo Simulation:

The Monte Carlo method involves using random sampling to get numerical results. In this simulation:

1. We start from a "Good" day.
2. Using the given probabilities, we determine the nature of the subsequent day.
3. We repeat the process until we encounter a "Bad" day.
4. The number of days taken to reach the "Bad" day is recorded.
5. This process is repeated for a large number of trials.
6. The average of all these trials gives us the expected number of days to encounter a "Bad" day.

## Findings

### Mathematical Solution:

The mathematical approach yielded an expected value of approximately 2.50 days until the next "Bad" day, starting from a "Good" day.

### Monte Carlo Simulation:

After running the simulation for 100,000 trials, the average number of days until the next "Bad" day was found to be approximately 2.49 days.

