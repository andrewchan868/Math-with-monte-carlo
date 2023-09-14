## Meeting in a 3x3 Grid

### Problem Statement

Imagine a 3x3 grid. Person A starts at the bottom-left corner, and Person B starts at the top-right corner. 

- Person A can only move up or to the right.
- Person B can only move down or to the left.

The goal is to determine the probability that Persons A and B meet on the grid, given their movement restrictions.

### Monte Carlo Simulation Approach

To solve this problem, we employed the Monte Carlo method. This involved simulating the movements of Persons A and B on the grid multiple times and then computing the fraction of times they met. The simulation followed these rules:

1. Randomly select a direction for Person A (up or right) and for Person B (down or left) at each step.
2. If Person A reaches the top row, he can only move right.
3. If Person B reaches the leftmost column, he can only move down.
4. Terminate the simulation if the two persons meet or if they've taken more moves than possible without meeting.

By running this simulation for a large number of iterations, we approximated the probability that the two persons meet.

### Result

After running the simulation for 100,000 iterations, the estimated probability that A and B meet on the 3x3 grid is approximately 31.4%.

While 2 x 2 is 37.5%
