import random

def draw_ball(blue, red, yellow):
    balls = ['blue'] * blue + ['red'] * red + ['yellow'] * yellow
    drawn_ball = random.choice(balls)
    
    if drawn_ball == 'blue':
        blue -= 1
    elif drawn_ball == 'red':
        red -= 1
    else:
        yellow -= 1

    return drawn_ball, blue, red, yellow

def simulation_run():
    blue, red, yellow = 75, 25, 1
    earnings = 0
    draws_until_yellow = 0

    while yellow > 0:
        ball, blue, red, yellow = draw_ball(blue, red, yellow)
        draws_until_yellow += 1
        if ball == 'red':
            earnings += 1
        elif ball == 'yellow':
            return earnings, draws_until_yellow

def monte_carlo_simulation(runs=100000):
    total_earnings = 0
    total_draws = 0

    for _ in range(runs):
        earnings, draws = simulation_run()
        total_earnings += earnings
        total_draws += draws

    avg_earnings = total_earnings / runs
    avg_draws = total_draws / runs
    
    return avg_earnings, avg_draws

average_earnings, average_draws = monte_carlo_simulation()
print(f"Average Earnings: ${average_earnings:.2f}")
print(f"Average Draws Until Yellow: {average_draws:.2f}")

# Average Earnings: $12.50
# Average Draws Until Yellow: 51.01
