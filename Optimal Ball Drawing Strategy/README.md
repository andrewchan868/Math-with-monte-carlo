# Optimal Ball Drawing Strategy

## Problem Description

You have an urn with the following balls:
- 75 blue balls
- 25 red balls
- 1 yellow ball

Each red ball you draw earns you $1. If you draw the yellow ball, you lose all your earnings. The question is: **How many balls should you draw to maximize your expected earnings?**

## Formula for Expected Value

To determine the optimal number of ball draws, we need to calculate the expected value (EV) of drawing a ball given a certain distribution of balls.

The EV is calculated as:
```
EV = (Probability of Red) * (Earnings from Red) + (Probability of Blue) * (Earnings from Blue) + (Probability of Yellow) * (Earnings from Yellow)
```

Where:
- Earnings from Red = $1 + Expected Earnings from next draw
- Earnings from Blue = Expected Earnings from next draw
- Earnings from Yellow = -$Earnings so far

To determine the expected earnings from the next draw, you need to consider the new distribution of balls after the current draw and calculate its EV. This recursive approach allows us to calculate the EV for each draw until the yellow ball is drawn.

## Strategy to Find Optimal Number of Draws

1. Calculate the initial EV with all balls in the urn.
2. Make a draw:
    - Update the distribution of balls.
    - Calculate the new EV.
3. Compare the new EV to your earnings so far:
    - If the EV is positive and sufficiently high, consider making another draw.
    - If the EV is negative or too close to zero (based on your risk tolerance), stop and keep your current earnings.
4. Repeat the process until the optimal stopping point is determined.

By following this strategy, you can find the number of draws that maximizes your expected earnings without overly risking drawing the yellow ball.

## Monte Carlo

Average Earnings: $12.50
Average Draws Until Yellow: 51.01
