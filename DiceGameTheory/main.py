def calculate_ev_for_A_revised(choice_for_A):
    # Calculate EV if B chooses n-1
    ev_below = sum(range(choice_for_A, 31)) / 30
    
    # Calculate EV if B chooses n+1
    ev_above = sum(range(1, choice_for_A + 1)) / 30
    
    if ev_below < ev_above:
        # B will choose choice_for_A + 1 for maximizing his EV
        return ev_below
    else:
        # B will choose choice_for_A - 1 for maximizing his EV
        return ev_above

# Calculating the revised EV for Player A for each choice
ev_list_for_A_revised = [calculate_ev_for_A_revised(choice) for choice in choices_for_A]

ev_list_for_A_revised
