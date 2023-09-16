# D10 Dice Simulator using D6

A simple method to simulate a 10-sided dice (D10) using a standard 6-sided dice (D6).

## Overview

The simulation follows a two-roll approach:

1. The first roll of the D6 determines the range of the outcome.
2. The second roll of the D6 determines the exact outcome within the previously determined range.

## How It Works

1. **First Roll of D6**:
   - If the outcome is 1, 2, or 3, then the desired outcome will be between 1 and 5.
   - If the outcome is 4, 5, or 6, then the desired outcome will be between 6 and 10.

2. **Second Roll of D6**:
   - If the desired outcome from the first roll is between 1 and 5:
     - Use the outcome directly if it's between 1 and 5.
     - If the outcome is 6, discard both rolls and start over.
   - If the desired outcome from the first roll is between 6 and 10:
     - Use the outcome + 5 as the result if the second roll is between 1 and 5.
     - If the outcome is 6, discard both rolls and start over.

![IMG_2207](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/27b6984f-34ca-4bec-939d-972046c6fdcf)


# How about D15 Dice using D6?

The idea would be similar
![IMG_2209](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/642d6244-a265-4638-b54b-ff22c95686d5)

