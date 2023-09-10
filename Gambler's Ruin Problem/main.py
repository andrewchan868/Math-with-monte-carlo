# Parameters
k = 3  # Initial fortune for player A
N = 10  # Goal

def simulate_two_player_game(k, N):
    """Simulate a single game until one player goes broke."""
    player_A_money = k
    player_B_money = N - k
    flips = 0
    
    while 0 < player_A_money < N:
        if random.random() < 0.5:  # Fair coin toss
            player_A_money += 1
            player_B_money -= 1
        else:
            player_A_money -= 1
            player_B_money += 1
        flips += 1

    return player_A_money, flips

def monte_carlo_two_players(k, N, simulations=10000):
    """Estimate the probability that player A goes broke and the expected game length."""
    bankrupt_count = 0
    total_flips = 0
    
    for _ in range(simulations):
        final_money, flips = simulate_two_player_game(k, N)
        if final_money == 0:
            bankrupt_count += 1
        total_flips += flips
        
    probability_broke = bankrupt_count / simulations
    expected_flips = total_flips / simulations
    return probability_broke, expected_flips

# Parameters remain the same: k = 5, N = 10
# Results for the two-player scenario
monte_carlo_two_player_prob, two_player_expected_tosses = monte_carlo_two_players(k, N)

monte_carlo_two_player_prob, two_player_expected_tosses
