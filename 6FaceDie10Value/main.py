def simulate_d10_with_d6_revised():
    while True:
        # First roll of D6
        first_roll = random.randint(1, 6)
        
        # Decide the range based on the first roll
        if first_roll <= 3:
            desired_range = (1, 5)
        else:
            desired_range = (6, 10)
        
        # Second roll of D6
        second_roll = random.randint(1, 6)
        
        # If the outcome is in the desired range
        if 1 <= second_roll <= 5:
            if desired_range[0] == 1:
                return second_roll
            else:
                return second_roll + 5

# Let's roll the simulated D10 10000 times again and count the frequency of each outcome.
results_revised = [0] * 10
for _ in range(10000):
    outcome = simulate_d10_with_d6_revised()
    results_revised[outcome-1] += 1

results_revised
