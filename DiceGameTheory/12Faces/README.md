# Unfair Dice Game Strategy

In this game, we're dealing with a 12-faced dice with uneven probabilities. Specifically, the number 11 has a 40% chance of being rolled, while all other numbers have an equal likelihood of 3/55 which is 0.6/11.

Two players compete. Each player chooses a number. The dice is then rolled. The player whose chosen number is closest to the rolled number wins.

Given the unfair nature of the dice, the strategy revolves around maximizing the Expected Value (EV) of the chosen number.

## Expected Values

Here's a table showing the EV for each possible choice:

| Choice | Expected Value (EV) |
|--------|---------------------|
| 1      | 0.0545              |
| 2      | 0.1455              |
| 3      | 0.3255              |
| 4      | 0.5055              |
| 5      | 0.6855              |
| 6      | 0.8655              |
| 7      | 1.0455              |
| 8      | 1.2255              |
| 9      | 1.4055              |
| 10     | 1.5855              |
| 11     | 7.4                 |
| 12     | 0.6545              |

## Strategy

Given the weighted probabilities, the optimal choice for a player is 11 because of its high likelihood of being rolled. The EV decreases as the chosen number moves away from 11.
