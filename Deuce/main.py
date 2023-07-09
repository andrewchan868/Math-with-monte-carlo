import random


# Finding the probability of me winning a deuce, with n points above our opponent, p of my winning probability


def deuce_match_n(n, p):

    match_list = []
    count = 0
    w_points = 0
    l_points = 0
    while True:

        # Simulate 0.6 probability
        point = random.randint(1, 100)  # random.randint is both left and right inclusive
        if point <= int(p*100):
            match_list.append(1)
        else:
            match_list.append(-1)

        # One match
        if match_list[count] == 1:
            w_points += 1
            count += 1
        elif match_list[count] == -1:
            l_points += 1
            count += 1

        # Break statement
        if w_points - l_points == n:
            return 1
        elif l_points - w_points == n:
            return 0


no_random_walks = 100000
result = 0

# Monte Carlo Simulation
for _ in range(no_random_walks):
    result += deuce_match_n(2, 0.6)
print(result/no_random_walks)






