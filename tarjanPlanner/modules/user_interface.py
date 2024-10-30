
def get_user_transport_preference(): 
    print("Please select your route optimization preference:")
    print("1. Shortest travel time")
    print("2. Lowest cost")
    print("3. Fewest transfers")
    choice = input("Enter the number (1, 2, or 3): ")
    return choice

'''
def display_route(route, total_time, total_cost, transfers):
    print("Optimal Route:")
    for stop in route:
        print(f"{stop['name']} - {stop['district']}")
    print(f"Total Time: {total_time} mins")
    print(f"Total Cost: {total_cost} currency units")
    print(f"Total Transfers: {transfers}")

print(get_user_transport_preference())
'''