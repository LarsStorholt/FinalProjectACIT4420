import time 

def get_user_transport_preference():
    while True:
        try:
            print("Please select your route optimization preference:")
            print("1. Time")
            print("2. Costs")
            start_time = time.time()
            
            choice = input("Enter the number (1 or 2): ").strip()
            end_time = time.time()
            
            lost_time = end_time - start_time

            # Validate input
            if choice not in ('1', '2'):
                raise ValueError("Invalid choice. Please enter '1' for Time or '2' for Costs.")
            
            return choice, lost_time

        except ValueError as e:
            print(e)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def print_route_description(optimal_route, relatives_data, distance, travel_time, travel_costs):
    print("A route has been generated for you, Tarjan: ")
    # Convert relatives data to a dictionary for easy lookup by name
    relatives_info = {relative["name"]: relative for relative in relatives_data}

    # Print each stage in the specified format
    for stage in optimal_route:
        from_location = relatives_info[stage["from"]]
        to_location = relatives_info[stage["to"]]
        
        print(f"From '{from_location['street_name']}' to '{to_location['street_name']}', "
              f"to meet '{stage['to']}', mode: '{stage['mode']}'")
    
    print()
    print(f"The route is in total {distance} km, and will take {travel_time}. The costs are {travel_costs:.2f} ")
