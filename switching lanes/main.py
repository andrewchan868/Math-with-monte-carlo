import random

def monte_carlo_simulation(iterations):
    # 0 represents left lane, 1 represents right lane
    current_lane = random.choice([0, 1])
    left_lane_count = 0

    for _ in range(iterations):
        if current_lane == 0:  # If in left lane
            # Decide whether to switch to right lane
            if random.random() < 0.50:
                current_lane = 1
        else:  # If in right lane
            # Decide whether to switch to left lane
            if random.random() < 0.70:
                current_lane = 0

        if current_lane == 0:
            left_lane_count += 1

    return left_lane_count / iterations

# Simulate with a large number of iterations
fraction_left_lane = monte_carlo_simulation(1000000)
fraction_left_lane
