import random

# Finding the EV of sum of 3 cards randomly drawn from a deck


def draw_n_cards(n):
    deck = []

    for i in range(1, 13 + 1):
        for _ in range(4):
            deck.append(i)

    # random.sample --> No replacement
    result = random.sample(deck, n)
    return sum(result)


number_of_walks = 100000
estimate = 0
for _ in range(number_of_walks):
    estimate += draw_n_cards(8)
print(estimate/number_of_walks)



