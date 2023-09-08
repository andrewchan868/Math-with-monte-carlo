# Initialize variables for the new simulation
import random

num_trials_large = 1000000  # 1 million trials
total_winnings_large = 0

# Run the Monte Carlo simulation with more trials
for _ in range(num_trials_large):
    game_winnings = 0
    while True:
        red_die = random.randint(1, 4)
        blue_die = random.randint(1, 4)

        # Check if the game is over
        if red_die == blue_die:
            break

        # If blue die shows a greater number, add the difference to the winnings
        if blue_die > red_die:
            game_winnings += blue_die - red_die
            break

    # Add the winnings from this game to the total
    total_winnings_large += game_winnings

# Calculate the average winnings per game
average_winnings_large = total_winnings_large / num_trials_large
average_winnings_large
