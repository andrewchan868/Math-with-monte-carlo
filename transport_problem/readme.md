# Random Walk Simulation: Drunkard's Dilemma/ Transport Problem

## Introduction:
The Random Walk problem, commonly known as the Drunkard's Walk, is a classic demonstration of stochastic or random processes. In this exploration, we delve into a variant of this problem to determine the average distance from the starting point after a given number of steps and the implications of taking **transport** if too far from the starting point.

## Problem Statement:
Imagine taking n steps in a two-dimensional grid. Each step is in a randomly chosen direction: north, south, east, or west. If, after these steps, you are more than 4 blocks away from your starting point, you'll need to take transport to return.

**The key question:** What's the maximum number of steps you can take such that, on average, you'll end up 4 blocks or fewer from your starting point?

## Observations:

### Even vs Odd Steps:
It has been observed that taking an even number of steps tends to bring you closer to your starting point on average, compared to taking an odd number of steps. The rationale:

1. **Even Steps:** Given the random distribution of step directions, we can expect an even distribution across opposite directions. For instance, the number of steps taken north could roughly equal the number taken south. This balance means you're more likely to hover around your starting point.
   
2. **Odd Steps:** With an odd number of steps, there's always a slight imbalance. One direction will have at least one step more than its opposite. This naturally leads you slightly further from the starting point. However, as the total number of steps increases, this imbalance becomes less significant in proportion, reducing its overall impact.

## Simulation Approach:
A Monte Carlo simulation can be employed to test these observations. By simulating a large number of walks for various step counts, we can approximate the average distance from the starting point. This will give insights into the optimal number of steps to take to remain within 4 blocks of the starting location.

## Conclusion:
The Drunkard's Dilemma provides an engaging way to explore randomness and probability. Through simulation, we can gain insights into stochastic behaviors and make informed decisions, like when to hail that late-night ride home!
