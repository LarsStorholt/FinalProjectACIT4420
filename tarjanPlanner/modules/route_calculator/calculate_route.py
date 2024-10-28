def calculate_optimal_route(preference):
    """Calculates the optimal route based on the user preference."""
    if preference == "1":
        return calculate_fastest_route()
    elif preference == "2":
        return calculate_lowest_cost_route()
    elif preference == "3":
        return calculate_fewest_transfers_route()
    else:
        raise ValueError("Invalid preference selected.")

def calculate_fastest_route(): 
    return("this is the fastest route: ") 

def calculate_lowest_cost_route(): 
    return "this route cost the least: "

def calculate_fewest_transfers_route(): 
    return "this route has fewest transfers: "

