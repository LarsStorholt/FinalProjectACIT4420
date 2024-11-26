import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from networkx.algorithms import approximation as approx
import time


def find_shortest_distance_route(city_graph):
    # Find the shortest-distance TSP route
    cycle = approx.simulated_annealing_tsp(city_graph, "greedy", source="Tarjan")
 
    #Calculate the distance of the route
    distance = sum(city_graph[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
    distance = int(distance)

    return cycle, distance


def calculate_efficient_route_with_modes(city_graph, cycle, transport_modes, transport_preference):
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


def visualize_route(city_graph, optimal_route):
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

    # Draw all nodes, with a special color and size for the starting node "Tarjan"
    nx.draw_networkx_nodes(city_graph, pos, node_size=100, node_color="skyblue", label="Residential Streets")
    nx.draw_networkx_nodes(city_graph, pos, nodelist=["Tarjan"], node_size=200, node_color="lime", label="Tarjan's Home")

    # Draw only the edges in the optimal route with color based on mode
    for stage in optimal_route:
        u, v = stage["from"], stage["to"]
        mode = stage["mode"]
        color = transport_colors.get(mode, "black")  # Default to black if mode color is not found
        
        # Draw the edge with the specific color for the mode
        nx.draw_networkx_edges(city_graph, pos, edgelist=[(u, v)], edge_color=color, width=2.5, style="solid")

    # Draw labels for each node
    nx.draw_networkx_labels(city_graph, pos, font_size=8, font_family="sans-serif")

    # Create custom legend entries for each transport mode and location
    legend_patches = [
        mpatches.Patch(color="lime", label="Tarjan's Home"),
        mpatches.Patch(color="skyblue", label="Relatives Home")
    ]
    for mode, color in transport_colors.items():
        legend_patches.append(mpatches.Patch(color=color, label=mode))

    # Add the legend with a title
    plt.legend(handles=legend_patches, title="Transportation Modes and Locations", loc="upper right")

    # Add title and labels
    plt.title("Tarjan's Transportation Network in Seoul with Optimal Route Highlighted")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.grid(True)
    plt.tight_layout()
    watch_start = time.time()
    plt.show()
    watch_end = time.time()
    watch_time = watch_end - watch_start

    return watch_time




