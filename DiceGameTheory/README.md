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

If Player A chooses n:

- Player B chooses n−1, the EV for Player A is the sum of numbers from n to 30 inclusive.
- Player B chooses n+1, the EV for Player A is the sum of numbers from 1 to n inclusive.

![IMG_73F61EF1240D-1](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/817c0b40-ba52-4b1b-9b12-8f0412628d09)


### Optimal Choices

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/f372b530-4ee0-4dec-93a3-08e788442a19)



- For Player B: Always choose the number that allows you to capture the higher expected value range.
- For Player A: The analysis shows that choosing 22 offers the highest expected value. However, Player B still retains a strategic advantage.

## Conclusion

Given the structure of the game, Player B always has the upper hand. If given a choice, it's better to go second. If you must go first, 22 is the optimal number to pick.
