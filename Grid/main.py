def updated_move_A(x, y):
    """Move A either up or right."""
    if x == 3:  # On the rightmost column, can only move up
        return x, y + 1
    elif y == 3:  # On the top row, can only move right
        return x + 1, y
    else:
        return (x + 1, y) if random.choice([True, False]) else (x, y + 1)

def updated_move_B(x, y):
    """Move B either down or left."""
    if x == 0:  # On the leftmost column, can only move down
        return x, y - 1
    elif y == 0:  # On the bottom row, can only move left
        return x - 1, y
    else:
        return (x - 1, y) if random.choice([True, False]) else (x, y - 1)

def updated_simulate_meeting():
    """Simulate the paths of A and B to check if they meet."""
    # Starting positions
    A = (0, 0)
    B = (3, 3)
    
    while (A[0] <= 3 and A[1] <= 3) and (B[0] >= 0 and B[1] >= 0):
        if A == B:  # They've met
            return True
        A = updated_move_A(*A)
        B = updated_move_B(*B)
    return False

# Updated Monte Carlo Simulation
meet_count_updated = sum(updated_simulate_meeting() for _ in range(num_simulations))

probability_meet_updated_monte_carlo = meet_count_updated / num_simulations
probability_meet_updated_monte_carlo
