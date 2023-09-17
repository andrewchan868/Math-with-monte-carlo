# Dice Game: Maximizing Winnings

## Introduction

In this game, players guess a number between 2 and 16. They then roll a 10-sided die and a 6-sided die. If the sum of the dice rolls matches the guessed number, players win that amount in dollars.

## Objective

To determine the best number to guess in order to maximize average winnings.

## Mathematical Approach

The expected value (EV) for each possible sum S can be calculated using the formula:


EV(S) = S x P(S)


Where:
- S is the sum (from 2 to 16)
- P(S) is the probability of rolling that sum

The probabilities P(S) are derived from counting all the possible ways to achieve the sum S  by rolling the two dice and dividing it by the total number of possible outcomes (60, since there are 10 possible outcomes for the 10-sided die and 6 for the 6-sided die).

## Monte Carlo Simulation

In addition to the mathematical approach, a Monte Carlo simulation was used to estimate the expected value for each sum. This involved simulating the dice rolls a large number of times and calculating the average winnings for each guessed sum.

## Results

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/3d1b77d1-84f6-4f69-b613-9718592caf27)

As you can observe, the probability peaks around the sum of 11, further confirming why it offers the highest expected winnings.

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/44acdc5f-f80e-4175-810a-a7173be39ac1)


Both the mathematical approach and the Monte Carlo simulation concluded that the best number to guess to maximize average winnings is **11**. The expected payout for guessing 11 is approximately $1.10.

## Why this Result?

The number 11 lies near the center of the possible outcomes, which means there are many combinations of dice rolls that can result in this sum. While numbers like 2 and 16 have only one possible combination each (1+1 and 10+6 respectively), the number 11 has several (e.g., 5+6, 6+5, 4+7, 7+4, ...). This makes 11 more likely to appear compared to the extreme values, hence maximizing the expected winnings.
