import random

# Number of simulations
N = 100000

# Initialize winnings for each sum
winnings = {i: 0 for i in range(2, 17)}

# Simulate the process for each sum
for guess in range(2, 17):
    for _ in range(N):
        d10 = random.randint(1, 10)
        d6 = random.randint(1, 6)
        if d10 + d6 == guess:
            winnings[guess] += guess

# Compute the average winnings for each sum
average_winnings = {guess: winnings[guess] / N for guess in winnings}

# Find the sum with the maximum average winnings
best_guess_mc = max(average_winnings, key=average_winnings.get)

best_guess_mc, average_winnings[best_guess_mc]

# output is 11 and 1.1
