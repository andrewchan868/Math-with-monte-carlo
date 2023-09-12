import random

def next_day(current_day):
    """Determine the next day given the current day using the provided probabilities."""
    if current_day == "Good":
        return "Good" if random.random() < 0.6 else "Bad"
    else:  # if current_day is "Bad"
        return "Bad" if random.random() < 0.7 else "Good"

def days_until_bad():
    """Determine the number of days until the next 'Bad' day, starting from a 'Good' day."""
    current_day = "Good"
    days_count = 0
    
    while current_day != "Bad":
        current_day = next_day(current_day)
        days_count += 1
    
    return days_count

def monte_carlo_simulation(num_trials):
    """Perform a Monte Carlo simulation to estimate the average number of days until the next 'Bad' day."""
    total_days = 0
    for _ in range(num_trials):
        total_days += days_until_bad()
        
    return total_days / num_trials

# Running the Monte Carlo simulation with 100,000 trials
num_trials = 100000
average_days = monte_carlo_simulation(num_trials)
average_days_rounded = round(average_days, 2)
average_days_rounded
