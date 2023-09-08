import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        
        # Check if the point (x, y) lies inside the unit circle
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Estimate value of pi
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

# Number of samples/darts
N = 1000000  # 1 million

# Estimate value of pi using Monte Carlo
pi_value = estimate_pi(N)
pi_value
