def drunkards_walk(num_samples, N):
    total_distance = 0

    for _ in range(num_samples):
        x, y = 0, 0  # Start at the origin
        for _ in range(N):
            # Randomly decide the direction of the next step
            step = random.choice(['up', 'down', 'left', 'right'])
            if step == 'up':
                y += 1
            elif step == 'down':
                y -= 1
            elif step == 'left':
                x -= 1
            elif step == 'right':
                x += 1

        # Calculate the distance from the origin
        distance = np.sqrt(x**2 + y**2)
        total_distance += distance

    # Calculate the average distance from the origin
    average_distance = total_distance / num_samples
    return average_distance

# Number of steps
N_steps = 100

# Number of simulations
N_drunkard_samples = 100000  # 100,000 simulations

# Estimate the expected distance using Monte Carlo
expected_distance = drunkards_walk(N_drunkard_samples, N_steps)
expected_distance
