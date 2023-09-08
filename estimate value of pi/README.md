# Estimating pi Using Monte Carlo Simulation

## Introduction:
The value of pi is a mathematical constant that represents the ratio of a circle's circumference to its diameter. While there are many ways to determine pi, this repository demonstrates a fun and interesting method using Monte Carlo simulation.

## Problem Statement:
Imagine a unit circle (radius = 1) inscribed inside a square with a side length of 2. If we randomly throw darts at the square, the ratio of the number of darts that land inside the circle to the total number of darts thrown should approximate pi /4.

## Methodology:

### Mathematical Approach:
The area of the circle = pi (since radius = 1) and the area of the square = 4. The ratio of the areas is:

![image](https://github.com/andrewchan868/Math-with-monte-carlo/assets/66477660/8920b064-e5b9-480c-bf99-077450c138f6)


### Monte Carlo Simulation:
1. Randomly "throw" a large number N of darts at the square.
2. Count the number M that lands inside the circle.
3. The estimate for pi is given by approx 4M/N.

## Code:
The Python code in this repository uses the `random` module to simulate the dart throws and estimate the value of pi

## Results:
After running the simulation with 1 million darts, the estimated value of pi was found to be approximately 3.140544. The accuracy of this estimation improves with more darts (iterations).

## Conclusion:
The Monte Carlo method provides an interesting and fun way to approximate the value of pi. It serves as a testament to the power of randomness in solving deterministic problems.
