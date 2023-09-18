# Poker Card Game Probability Analysis

In this analysis, we explore the probability of drawing two cards of the same color from different deck configurations. The game rules are simple: if you draw two cards of the same color, you win $1; otherwise, you lose $1.

## Deck Choices:

1. **Choice A**: Deck with 26 Black cards and 26 Red cards.

> P_2Black_A = (26/52) * (25/51)

> P_2Red_A = (26/52) * (25/51)

> P_A = P_2Black_A + P_2Red_A

2. **Choice B**: Deck with 13 Black cards and 13 Red cards.

> P_2Black_B = (13/26) * (12/25)

> P_2Red_B = (13/26) * (12/25)

> P_B = P_2Black_B + P_2Red_B


3. **Choice C**: Deck with a random 26 cards drawn from a standard 52-card deck.

## Probabilities:

- **Choice A**: The probability of drawing two cards of the same color is approximately 49.02%.
  
- **Choice B**: The probability is 48%.
  
- **Choice C**: Using a Monte Carlo simulation with 100,000 iterations, the estimated probability is approximately 48.994%.

## Conclusion:

From our analysis, Choice A offers the highest probability of drawing two cards of the same color, making it the optimal choice for this game. However, the difference in probabilities across the choices is marginal.
