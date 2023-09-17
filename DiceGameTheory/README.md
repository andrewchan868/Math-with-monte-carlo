# Optimal Strategy for the Number-Picking Game

## Game Description

1. Player A chooses an integer between 1 and 30.
2. Player B chooses a different integer, which is either one less or one more than Player A's choice.
3. A random integer x between 1 and 30 is generated.
4. The player whose number is closer to x receives a payout of x dollars.

## Strategy

Given Player B's ability to react to Player A's choice, they can always position themselves to capture the range of numbers with the higher expected value. The expected value (EV) for each number Player A could choose depends on:

- The sum of the numbers from 1 to Player A's choice if Player B chooses one more than Player A's number.
- The sum of the numbers from Player A's choice to 30 if Player B chooses one less than Player A's number.

### Mathematical Explanation

If Player A chooses \( n \):

![IMG_82C4E4573FA8-1](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/4947847f-f263-4a3e-b831-0b0bd8a9ef1d)


### Optimal Choices

- For Player B: Always choose the number that allows you to capture the higher expected value range.
- For Player A: The analysis shows that choosing 21 offers the highest expected value. However, Player B still retains a strategic advantage.

## Conclusion

Given the structure of the game, Player B always has the upper hand. If given a choice, it's better to go second. If you must go first, 21 is the optimal number to pick.
