from itertools import permutations
from geopy.distance import geodesic
import time

# Function to calculate the total distance of a route
def calculate_route_distance(route, relatives_data):
    total_distance = 0
    for i in range(len(route) - 1):
        # Get the coordinates of the two nodes in the route
        node1 = next(relative for relative in relatives_data if relative["name"] == route[i])
        node2 = next(relative for relative in relatives_data if relative["name"] == route[i + 1])
        # Calculate the distance between them
        total_distance += geodesic(
            (node1["latitude"], node1["longitude"]),
            (node2["latitude"], node2["longitude"])
        ).km
    return total_distance

# Brute-force TSP solver
def find_optimal_route(relatives_data):
    start_time = time.time()
    start_node = "Tarjan"  # Starting and ending point
    all_nodes = [relative["name"] for relative in relatives_data if relative["name"] != start_node]

    # Generate all possible permutations of the nodes, starting and ending at the start_node
    shortest_route = None
    min_distance = float('inf')
    
    for perm in permutations(all_nodes):
        # Create a route starting and ending at the start_node
        route = [start_node] + list(perm) + [start_node]
        # Calculate the total distance of this route
        total_distance = calculate_route_distance(route, relatives_data)
        # Check if this is the shortest route so far
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_route = route
            print(min_distance)
    
    end_time = time.time()
    execution_time = end_time-start_time
    print(execution_time)
    return shortest_route, min_distance




relatives_data = [
    {"name": "Tarjan", "latitude": 37.5215, "longitude": 126.9243},
    {"name": "Relative_1", "latitude": 37.4979, "longitude": 127.0276},
    {"name": "Relative_2", "latitude": 37.4833, "longitude": 127.0322},
    {"name": "Relative_3", "latitude": 37.5172, "longitude": 127.0286},
    {"name": "Relative_4", "latitude": 37.5219, "longitude": 127.0411},
    {"name": "Relative_5", "latitude": 37.534, "longitude": 127.0026},
    {"name": "Relative_6", "latitude": 37.5443, "longitude": 127.0557},
    {"name": "Relative_7", "latitude": 37.5172, "longitude": 127.0391},
    {"name": "Relative_8", "latitude": 37.58, "longitude": 126.9844},
    {"name": "Relative_9", "latitude": 37.511, "longitude": 127.059},
    {"name": "Relative_10", "latitude": 37.5133, "longitude": 127.1028}
]

'''
# Find the optimal route
optimal_route, optimal_distance = find_optimal_route(relatives_data)

# Print the results
print("Optimal route:", optimal_route)
print("Optimal distance (km):", optimal_distan