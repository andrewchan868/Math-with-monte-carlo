## Winning the Dollar Game

### Problem Statement

You're playing a game against an opponent:

- You start with 1 dollar.
- Your opponent starts with 2 dollars.
- Each round, you have a 2/3 chance of winning.
- If you win a round, you gain 1 dollar from your opponent. If you lose, your opponent takes 1 dollar from you.
- The game ends when one of you runs out of money.

What is the probability that you will win the game?

### Combinatorial Approach

![IMG_EA8237D1E1B7-1](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/a23a9d9f-8aed-41da-a684-a76f17e401a8)


Using a combinatorial approach, we formulated a system of equations representing the probabilities of winning given certain starting conditions. By solving these equations, we determined that the probability of you winning the game is approximately 57.14%.

### Monte Carlo Simulation Approach

To validate our combinatorial results, we employed a Monte Carlo simulation:

1. We simulated the game multiple times, considering the probabilities of winning or losing each round.
2. Each simulation continued until one player ran out of money.
3. After a large number of simulations, we calculated the fraction of games you won.

The Monte Carlo simulation, conducted over 100,000 iterations, yielded a result of approximately 57.036%, closely matching our combinatorial calculation.
