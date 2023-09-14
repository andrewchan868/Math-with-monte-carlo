# Gambler's Ruin Problem Analysis (Two Players)

This repository investigates the classic problem of the gambler's ruin involving two players. Each player starts with an initial fortune, and they bet against each other on a fair coin toss. The players either win or lose money with each toss. The objective is to determine the likelihood of one player going broke and the expected game duration.

## Problem Statement

Two players, A and B, engage in a betting game. Player A starts with k dollars, and Player B starts with N - k dollars, where N is the total combined wealth. They bet against each other on a fair coin toss. If the coin comes up heads, player A wins 1 dollar from player B, and if tails, player A loses 1 dollar to player B. The game concludes when one player loses all their money.

The questions explored:
1. What is the probability that player A will go broke?
2. What is the expected number of tosses before the game ends?

## Approaches

### 1. Mathematical Approach

The Gambler's Ruin problem can be modeled using a recursive relationship. If P_k denotes the probability that player A, starting with k dollars, will eventually go broke against player B (who starts with N−k dollars), and considering the game uses a fair coin:

The recursive equation is:

P_k = 1/2 P_(k-1) + 1/2 P_(k+1)

With Boundary:
P_0 = 1 (if A starts with 0 dollars => already broke.)
P_N = 0 (if A starts with N dollars => have already won since B is broke)

For a fair coin, the equation is 
P_k = (N-k) /N

For our specific case with k = 3, and N = 10:
P_3 = 0.7

This means A begins with k = 3 dollars, there is a 70% probability they will go broke before accumulating all N dollars.


### 2. Monte Carlo Simulation Approach

The game's progress between the two players is simulated over a multitude of games. The outcomes (win or ruin for player A) and the number of tosses for each game are tracked to estimate both the probability of ruin and the expected game duration.

## Results

- **Monte Carlo Simulation(k=3)**:

  > For the two-player scenario in the Gambler's Ruin problem, with player A starting with k=3 dollars:

  - Estimated probability of player A's ruin: 70.02%.
  - Expected game duration: Approximately 21.24 tosses.

