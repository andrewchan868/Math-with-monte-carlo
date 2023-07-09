import random


def random_walk(n):

    x, y = 0, 0
    for _ in range(n):
        (dx, dy) = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        x += dx
        y += dy
    return x, y


number_of_walks = 10000

# We have 30 cases we need to cal
for walk_length in range(1, 31):
    no_transport = 0

    # NUmber of random walks
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)

        if distance <= 4:
            no_transport += 1

    target_percentage = float(no_transport/number_of_walks) * 100
    print(f'Walk size = {walk_length}, and the percentage of no transport = {target_percentage}%')
