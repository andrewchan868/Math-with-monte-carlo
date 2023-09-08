def birthday_paradox(num_samples):
    n = 1  # Start with 1 person
    while True:
        shared_birthday_count = 0

        for _ in range(num_samples):
            birthdays = [random.randint(1, 365) for _ in range(n)]
            if len(birthdays) != len(set(birthdays)):
                shared_birthday_count += 1

        probability = shared_birthday_count / num_samples
        if probability > 0.5:
            return n
        n += 1

# Number of simulations per group size
N_birthday_samples = 10000  # 10,000 simulations

# Find the group size for which there's a >50% chance of shared birthday
group_size = birthday_paradox(N_birthday_samples)
group_size

#result is 23
