# Estimating \( \pi \) Using Monte Carlo Simulation

## Introduction:
The value of \( \pi \) is a mathematical constant that represents the ratio of a circle's circumference to its diameter. While there are many ways to determine \( \pi \), this repository demonstrates a fun and interesting method using Monte Carlo simulation.

## Problem Statement:
Imagine a unit circle (radius = 1) inscribed inside a square with side length 2. If we randomly throw darts at the square, the ratio of the number of darts that land inside the circle to the total number of darts thrown should approximate \( \frac{\pi}{4} \).

## Methodology:

### Mathematical Approach:
The area of the circle \( A_{\text{circle}} = \pi \) (since radius = 1) and the area of the square \( A_{\text{square}} = 4 \). The ratio of the areas is:

\[
\frac{A_{\text{circle}}}{A_{\text{square}}} = \frac{\pi}{4}
\]

### Monte Carlo Simulation:
1. Randomly "throw" a large number \( N \) of darts at the square.
2. Count the number \( M \) that land inside the circle.
3. The estimate for \( \pi \) is given by \( \pi \approx \frac{4M}{N} \).

## Code:
The Python code in this repository uses the `random` module to simulate the dart throws and estimate the value of \( \pi \).

## Results:
After running the simulation with 1 million darts, the estimated value of \( \pi \) was found to be approximately 3.140544. The accuracy of this estimation improves with more darts (iterations).

## Conclusion:
The Monte Carlo method provides an interesting and fun way to approximate the value of \( \pi \). It serves as a testament to the power of randomness in solving deterministic problems.
