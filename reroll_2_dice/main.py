import random


def dice_throw_reroll(n):
    reroll_quota = n

    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    smaller = min(d1, d2)

    while (reroll_quota > 0) and (smaller < 3.5):
        smaller = random.randint(1, 6)
        reroll_quota -= 1

    return smaller + max(d1, d2)


result = 0
no_of_walks = 10000
for _ in range(no_of_walks):
    result += dice_throw_reroll(1)
print(result/no_of_walks)
