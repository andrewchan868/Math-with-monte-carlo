## Sum of Highest Three Dice Rolls

### Problem Statement

Given four dice rolls, what is the probability that the sum of the three highest dice is 18?

### Combinatorial Approach

To achieve a sum of 18 from three dice, each die must roll a 6. Given that we're rolling four dice and considering only the highest three, there are two main scenarios:

1. Three dice roll a 6, and the fourth die rolls a number other than 6.
2. All four dice roll a 6.

Using combinatorics, we calculated the probability for these scenarios:

![IMG_3E76CF450052-1](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/15f4588a-e55e-4e80-b06e-1feb933fc14e)
                      

The total probability was determined by summing up the probabilities of both scenarios, resulting in a probability of approximately 1.620%.

### Monte Carlo Simulation

To validate the combinatorial approach, a Monte Carlo simulation was conducted. The process involved:

1. Simulating the rolling of four dice.
2. Calculating the sum of the highest three dice rolls.
3. Checking if the sum was 18.
4. Repeating the process for 100,000 iterations.
5. Computing the fraction of times the sum was 18.

The Monte Carlo simulation yielded a probability of approximately 1.558%, which is in close agreement with the combinatorial approach.
