import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from networkx.algorithms import approximation as approx


def find_shortest_distance_route(city_graph):
    # Find the shortest-distance TSP route
    cycle = approx.simulated_annealing_tsp(city_graph, "greedy", source="Tarjan")
 
    #Calculate the distance of the route
    distance = sum(city_graph[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
    distance = int(distance)

    return cycle, distance


def calculate_balanced_route_with_modes(city_graph, cycle, transport_modes, transport_preference):
    """
    Calculate the optimal transport mode for each segment in the cycle to balance total travel time and cost.
    
    :param city_graph: The graph with nodes and weighted edges (distance as weight).
    :param cycle: The TSP cycle (ordered list of nodes) representing the route.
    :param transport_modes: Dictionary of transport modes with speed, cost, and transfer time.
    :param alpha: Weighting factor for cost vs. time. Alpha closer to 1 prioritizes cost, closer to 0 prioritizes time.
    :return: List of segments with optimal transport mode, total travel time, and total cost.
    """
    if transport_preference == '1': 
        alpha = 0
    elif transport_preference == '2': 
        alpha = 0.45 


    total_travel_time = 0
    total_cost = 0
    optimal_route = []

    for n, nbr in nx.utils.pairwise(cycle):
        # Get the distance between the current pair of nodes
        distance_km = city_graph[n][nbr]["weight"]

        # Calculate combined score for each transport mode, choosing the best balance
        best_mode = None
        best_score = float('inf')
        best_cost = 0  # Track the cost associated with the best mode for this segment
        best_time = 0  # Track the time associated with the best mode for this segment
        
        for mode, properties in transport_modes.items():
            speed_kmh = properties["speed_kmh"]
            transfer_time_min = properties["transfer_time_min"]
            cost_per_km = properties["cost_per_km"]

            # Calculate the travel time and cost for this mode
            travel_time_min = (distance_km / speed_kmh) * 60 + transfer_time_min
            travel_cost = distance_km * cost_per_km

            # Calculate the combined score
            score = alpha * travel_cost + (1 - alpha) * travel_time_min

            # Check if this mode gives a lower combined score
            if score < best_score:
                best_score = score
                best_mode = mode
                best_cost = travel_cost
                best_time = travel_time_min

        # Add the best mode for this segment to the route with its cost and time
        optimal_route.append({
            "from": n,
            "to": nbr,
            "mode": best_mode,
            "distance": int(distance_km),  # Remove decimals from distance
            "travel_time": f"{int(best_time // 60)}h {int(best_time % 60)}m",  # Format travel time
            "cost": best_cost
        })

        # Add the time and cost of this segment to the total values
        total_travel_time += best_time
        total_cost += best_cost

    # Convert total travel time to hours and minutes
    total_hours, total_minutes = divmod(total_travel_time, 60)
    return optimal_route, f"{int(total_hours)}h {int(total_minutes)}m", total_cost

'''
def calculate_fastest_route_with_modes(city_graph, cycle, transport_modes):
    """
    Calculate the optimal transport mode for each segment in the cycle to minimize total travel time.

    :param city_graph: The graph with nodes and weighted edges (distance as weight).
    :param cycle: The TSP cycle (ordered list of nodes) representing the shortest route.
    :param transport_modes: Dictionary of transport modes with speed, cost, and transfer time.
    :return: List of segments with optimal transport mode and total travel time.
    """
    total_travel_time = 0
    optimal_route = []
    total_cost = 0

    for n, nbr in nx.utils.pairwise(cycle):
        # Get the distance between the current pair of nodes
        distance_km = city_graph[n][nbr]["weight"]

        # Calculate travel time for each transport mode and choose the fastest
        best_mode = None
        best_time = float('inf')
        cost_step = 0
        
        for mode, properties in transport_modes.items():
            # Calculate the travel time for this mode
            speed_kmh = properties["speed_kmh"]
            transfer_time_min = properties["transfer_time_min"]
            cost_per_km = properties["cost_per_km"]

            travel_time_min = (distance_km / speed_kmh) * 60 + transfer_time_min  # Total time in minutes
            travel_cost = distance_km * cost_per_km

            # Check if this mode gives a lower travel time
            if travel_time_min < best_time:
                best_time = travel_time_min
                best_mode = mode
                cost_step = travel_cost

        # Add the best mode for this segment to the route
        optimal_route.append({
            "from": n,
            "to": nbr,
            "mode": best_mode,
            "distance": distance_km,
            "travel_time": best_time, 
            "cost": cost_step
        })

        # Add the time of this segment to the total travel time and total cost 
        total_travel_time += best_time
        total_cost += cost_step

        # Changing from minutes to hours, minutes
        hours = int(total_travel_time // 60) 
        minutes = int(total_travel_time % 60)
        travel_time = f"{hours} hours and {minutes} minutes"

    return optimal_route, travel_time, total_cost
'''

# Assuming `city_graph` is your graph and `cycle` is the TSP route obtained
optimal_route, total_travel_time = calculate_fastest_route_with_modes(city_graph, cycle, transport_modes)

# Display the optimal route with chosen transport modes
for segment in optimal_route:
    print(f"From {segment['from']} to {segment['to']}: Mode = {segment['mode']}, "
          f"Distance = {segment['distance']} km, Travel time = {segment['travel_time']} min")

print("Total travel time for the route:", total_travel_time, "minutes")
'''
#from route_calculator.calculate_route import calculate_optimal_route
#from modules.graph_builder import create_city_graph
'''
def calculate_optimal_route(city_graph, transport_preferenece): 
    if transport_preferenece == '1':
        weight = 'travel_time'
    elif transport_preferenece == '2':
        weight = 'cost'
    else:
        raise ValueError("Invalid preference. Choose 1 for 'time' or 2 for 'cost'.")

    fastest_route = nx.approximation.traveling_salesman_problem(
        city_graph, 
        weight=weight, 
        cycle=True
    )
    return fastest_route
'''
def get_information_about_route(shortest_route, city_graph, transport_modes) : 
    total_distance = 0
    route_details = []

    # Iterate through each leg of the route to gather details
    for i in range(len(shortest_route) - 1):
        node1, node2 = shortest_route[i], shortest_route[i + 1]

        # Find the edge with the minimum travel time between the nodes
        best_edge = min(
            city_graph.get_edge_data(node1, node2).values(),
            key=lambda x: x['distance']
        )
        
        # Collect the travel time, mode, and speed
        distance = best_edge["distance"]
        mode = best_edge["mode"]
        speed = next(
            (props["speed_kmh"] for m, props in transport_modes.items() if m == mode), 
            None
        )
        
        # Add segment details
        route_details.append({
            "from": node1,
            "to": node2,
            "mode": mode,
            "speed_kmh": speed,
            "distance": distance
        })

        # Sum up the travel time
        total_distance += distance

    return fastest_route, total_distance, route_details
    

def calculate_optimal_route(city_graph, preference, transport_mode=None):
    if preference == '1':
        weight = 'travel_time'
    elif preference == '2':
        weight = 'cost'
    else:
        raise ValueError("Invalid preference. Choose 1 for 'time' or 2 for 'cost'.")

    def weight_function(u, v, key=None):
        edge_data = city_graph.get_edge_data(u, v)
        filtered_weights = [
            data.get(weight, float('inf')) for data in edge_data.values()
        ]
        return min(filtered_weights) if filtered_weights else float('inf')

    tsp_path = nx.approximation.traveling_salesman_problem(city_graph, cycle=True, weight=weight_function)

    total_time, total_cost = 0, 0
    for u, v in zip(tsp_path[:-1], tsp_path[1:]):
        edge_data = city_graph.get_edge_data(u, v)
        if transport_mode:
            for data in edge_data.values():
                if data.get("mode") == transport_mode:
                    total_time += data.get("travel_time", 0)
                    total_cost += data.get("cost", 0)
                    break
        else:
            total_time += min(data.get("travel_time", 0) for data in edge_data.values())
            total_cost += min(data.get("cost", 0) for data in edge_data.values())

    print(f"TSP Path: {tsp_path}")
    print(f"Total Time: {total_time} min, Total Cost: {total_cost} dollars")

    return {
        'path': tsp_path,
        'total_time': f"{total_time} min",
        'total_cost': f"{total_cost} dollars"
    }

'''
def calculate_optimal_route(city_graph):
    """
    Calculates the optimal route for Tarjan to visit all relatives in a round trip,
    optimizing solely for the shortest travel time.
    
    Parameters:
        - city_graph: The graph with nodes and edges representing relatives and routes.
    
    Returns:
        - The optimal round-trip route and its total travel time.
    """
    # Set the weight function to minimize travel time
    def weight_function(u, v, key=None):
        edge_data = city_graph.get_edge_data(u, v)
        
        # Filter out edges without the travel_time attribute
        filtered_times = [
            data.get('travel_time', float('inf')) for data in edge_data.values() if data.get('travel_time') is not None
        ]

        # Return the minimum travel time for the edge
        return min(filtered_times) if filtered_times else float('inf')

    # Solve the TSP with a round trip (cycle=True), using travel time as the weight
    tsp_path = nx.approximation.traveling_salesman_problem(city_graph, cycle=True, weight=weight_function)

    # Calculate the total travel time for the chosen path
    total_time = sum(
        city_graph[u][v]['travel_time'] for u, v in zip(tsp_path[:-1], tsp_path[1:])
    )

    return {
        'path': tsp_path,
        'total_time': f"{total_time} min"
    }
'''



'''
def visualize_city_graph_with_route(city_graph, optimal_route):
    """
    Visualizes the city graph with nodes and edges based on transport types, and highlights the optimal route.
    
    Parameters:
        - city_graph: NetworkX graph with nodes for each location and edges with transport types and weights.
        - optimal_route: Dictionary with the calculated optimal path and total attributes.
    """
    # Get positions for nodes
    pos = nx.get_node_attributes(city_graph, 'pos')
    
    # Define colors for each transport mode
    transport_colors = {
        "bus": "orange",
        "train": "blue",
        "bicycle": "green",
        "walking": "red"
    }
    
    # Set up the plot
    plt.figure(figsize=(12, 8))
    
    # Draw nodes
    nx.draw_networkx_nodes(city_graph, pos, node_size=100, node_color="skyblue", label="Residential Streets")
    nx.draw_networkx_nodes(city_graph, pos, nodelist=["Tarjan"], node_size=200, node_color="lime", label="Tarjan's Home")
    
    # Draw only the edges in the optimal route with color based on mode
   # Draw only the edges in the optimal route with color based on mode
    route_edges = list(zip(optimal_route['path'][:-1], optimal_route['path'][1:]))
    for u, v in route_edges:
        # Get edge data dictionary for all edges between u and v
        edge_data = city_graph.get_edge_data(u, v)
        
        # Find the edge with the correct mode
        mode = edge_data.get(0, {}).get('mode', 'unknown')  # Adjust this to access the first edge's mode if you only need one edge
        color = transport_colors.get(mode, "black")  # Default to black if mode not found
        nx.draw_networkx_edges(city_graph, pos, edgelist=[(u, v)], edge_color=color, width=2.5, style="solid")

    
    # Draw labels
    nx.draw_networkx_labels(city_graph, pos, font_size=8, font_family="sans-serif")
    
    # Create custom legend entries for each transport mode and location
    legend_patches = [
        mpatches.Patch(color="lime", label="Tarjan's Home"),
        mpatches.Patch(color="skyblue", label="Residential Streets")
    ]
    
    # Add a patch for each transport mode
    for mode, color in transport_colors.items():
        legend_patches.append(mpatches.Patch(color=color, label=mode))
    
    # Add the legend with a title
    plt.legend(handles=legend_patches, title="Transportation Modes and Locations", loc="upper right")
    
    # Add title and labels
    plt.title("Tarjan's Transportation Network in Seoul with Optimal Route Highlighted")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.show()
