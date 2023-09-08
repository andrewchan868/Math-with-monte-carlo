# Fair Value of the Tetrahedral Dice Game

## Introduction:
In this game, players use two tetrahedral dice, each with faces labeled from 1 to 4. One die is red and the other is blue. Players roll both dice simultaneously in each turn.

## Rules:
1. If the blue die shows a number greater than the red die, players are paid the difference.
2. If both dice show the same number, the game ends immediately.
3. If the blue die does not show a greater number than the red die, but they are not equal, players move to another turn without any payout.

## Objective:
To determine the fair value of this game, or in other words, the expected value or average winnings a player can expect from playing this game.

## Methodology:
There are two primary methods to determine the fair value: a simulation-based approach (Monte Carlo) and a mathematical approach.

### Program (Monte Carlo Simulation):
By simulating the game a large number of times (e.g., a million times), we can approximate the expected winnings of the game. After running the simulation, our program determined the fair value to be approximately **1**.

### Mathematical Approach:
Using probability and expected value calculations, we can derive the fair value of the game. A detailed breakdown of the mathematical calculations can be found in the linked image:
![Mathematical Calculation](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/690fd37d-ef62-464a-b804-ca923b443865)

## Conclusion:
Both the program and the mathematical calculations suggest that the fair value of the game is around **1**. This means that on average, a player can expect to win about **1** unit of currency (e.g., dollar, euro) every time they play this game.
