# Birthday Paradox Simulation

## Introduction:
The Birthday Paradox, often referred to as the Birthday problem.

## Problem Statement:
If you're in a room with a group of people, how many individuals must there be for there to be a better-than-even chance that at least two of them share the same birthday? Given 365 days in a year, one might assume this number to be quite large. However, the actual number is startlingly smaller than most anticipate.

## Methodology:

### Mathematical Approach:
The Birthday Paradox can be approached mathematically by calculating the probability that no individual in a group has the same birthday. Subtracting this value from 1 gives the probability of at least two people sharing a birthday. Surprisingly, with just 23 people, this probability exceeds 50%.

The probability that two people in a group of n do not share the same birthday can be computed as:

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/a33d7ef1-8afc-418c-877c-af6bb1b23a8f)

The probability that at least two people in a group of n share the same birthday is the complement:

**P (same) = 1 - P (Different)**

For n = 23, P(same) exceeds 50%.

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/3ac141e7-a2ca-4874-bbc6-92934e4e5c81)

### Monte Carlo Simulation:
The Monte Carlo method provides a way to empirically verify this result:
1. For a group of n individuals, simulate a large number of birthdays.
2. Check if any birthday is repeated within the group.
3. Repeat the process across numerous simulations (e.g., 10,000 times) and compute the fraction of instances where shared birthdays were observed.
4. Incrementally increase n until this fraction surpasses 0.5.

## Code:
The Python code in this repository employs the `random` module to simulate birthdays and ascertain the group size where shared birthdays become more probable than not.

## Results:
Upon running the Monte Carlo simulation, it was reaffirmed that a mere group of 23 individuals suffices for there to be a better-than-even chance of two individuals having the same birthday.

## Conclusion:
The Birthday Paradox beautifully encapsulates the surprising and often unintuitive nature of probability. This simulation serves as a reminder of the fascinating results that can emerge from seemingly simple scenarios.
