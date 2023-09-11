import random

def simulate_cereal_purchase(weeks=20, num_toys=10):
    """Simulate purchasing cereal for a certain number of weeks and return the unique toys collected."""
    collected_toys = set()
    for _ in range(weeks):
        toy = random.randint(1, num_toys)  # Each toy is equally likely
        collected_toys.add(toy)
    return collected_toys

def monte_carlo_simulation_all_toys(simulations=10000, weeks=20, num_toys=10):
    """Estimate the probability of collecting all toys using Monte Carlo simulation."""
    success_count = 0
    for _ in range(simulations):
        collected_toys = simulate_cereal_purchase(weeks, num_toys)
        if len(collected_toys) == num_toys:
            success_count += 1
    return success_count / simulations

# Run the Monte Carlo simulation for part (b)
monte_carlo_prob_all_toys = monte_carlo_simulation_all_toys()
monte_carlo_prob_all_toys
