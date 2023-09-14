import random

def simulate_dice_game():
    """Simulate one round of the dice game."""
    total_payoff = 0
    while True:
        roll = random.randint(1, 6)
        total_payoff += roll
        if roll in [1, 2, 3]:
            break
    return total_payoff

# Monte Carlo Simulation
num_simulations = 100000
total_payoff = sum(simulate_dice_game() for _ in range(num_simulations))

expected_payoff_monte_carlo = total_payoff / num_simulations
expected_payoff_monte_carlo
