import random

def initialize_urn():
    return ['blue'] * 75 + ['red'] * 25 + ['yellow']

def simulation_run():
    urn = initialize_urn()
    random.shuffle(urn)
    earnings = 0
    draws_until_yellow = 0

    while urn:
        ball = urn.pop()  # Remove and get the last ball
        draws_until_yellow += 1
        if ball == 'red':
            earnings += 1
        elif ball == 'yellow':
            return earnings, draws_until_yellow

    return earnings, draws_until_yellow

def monte_carlo_simulation_extended(runs=100000):
    earnings_distribution = {}
    draws_distribution = {}

    total_earnings = 0
    total_draws = 0

    for _ in range(runs):
        earnings, draws = simulation_run()
        total_earnings += earnings
        total_draws += draws

        # Update earnings distribution
        earnings_distribution[earnings] = earnings_distribution.get(earnings, 0) + 1

        # Update draws distribution
        draws_distribution[draws] = draws_distribution.get(draws, 0) + 1

    avg_earnings = total_earnings / runs
    avg_draws = total_draws / runs

    return avg_earnings, avg_draws, earnings_distribution, draws_distribution

average_earnings, average_draws, earnings_dist, draws_dist = monte_carlo_simulation_extended()

print(f"Average Earnings: ${average_earnings:.2f}")
print(f"Average Draws Until Yellow: {average_draws:.2f}\n")

print("Earnings Distribution:")
for earning, count in sorted(earnings_dist.items()):
    print(f"${earning}: {count} times")

print("\nDraws Distribution:")
for draws, count in sorted(draws_dist.items()):
    print(f"{draws} draws: {count} times")

# Inferring optimal stopping point
cumulative_earnings = 0
cumulative_count = 0
for earning, count in sorted(earnings_dist.items(), reverse=True):
    cumulative_earnings += earning * count
    cumulative_count += count
    average_so_far = cumulative_earnings / cumulative_count
    if average_so_far < average_earnings:
        print(f"\nOptimal stopping point might be around earning: ${earning}")
        break
