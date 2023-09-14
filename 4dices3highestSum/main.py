def simulate_dice_roll():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort(reverse=True)
    return sum(rolls[:3])

# Running Monte Carlo simulation
iterations = 100000
success_count = sum(simulate_dice_roll() == 18 for _ in range(iterations))

monte_carlo_probability = success_count / iterations
monte_carlo_probability
