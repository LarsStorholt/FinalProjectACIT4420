import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches




#from route_calculator.calculate_route import calculate_optimal_route
#from modules.graph_builder import create_city_graph


def calculate_optimal_route(city_graph, preference, transport_mode=None):
    """
    Calculates the optimal route for Tarjan to visit all relatives in a round trip using a consistent transport mode.
    
    Parameters:
        - city_graph: The graph with nodes and edges representing relatives and routes.
        - preference: The criterion for optimization ('time', 'cost', 'transfers').
        - transport_mode: The desired transport mode for the entire route (e.g., 'bus', 'train').

    Returns:
        - The optimal round-trip route and its total travel time, cost, and transfers.
    """
    # Set the weight attribute based on preference
    if preference == '1':
        weight = 'travel_time'
    elif preference == '2':
        weight = 'cost'
    elif preference == '3':
        weight = 'transfers'
    else:
        raise ValueError("Invalid preference. Choose 1 for 'time', 2 for 'cost', or 3 for 'transfers'.")

    # Define the weight function to use only the specified transport mode
    def weight_function(u, v, key=None):
        edge_data = city_graph.get_edge_data(u, v)
        
        # Print debugging info for the edge and weights
        print(f"Calculating weight for edge from {u} to {v} using weight: {weight}")
        print(f"Edge data: {edge_data}")

        # Filter out edges without the selected weight
        filtered_weights = [
            data.get(weight, float('inf')) for data in edge_data.values() if data.get(weight) is not None
        ]

        # Return the minimum filtered weight for the selected attribute (time, cost, or transfers)
        return min(filtered_weights) if filtered_weights else float('inf')


    # Solve the TSP with a round trip (cycle=True), using the specified weight function
    tsp_path = nx.approximation.traveling_salesman_problem(city_graph, cycle=True, weight=weight_function)

    # Print tsp_path to verify the route
    print("TSP Path:", tsp_path)

    # Print each segment of the path with calculated values
    for u, v in zip(tsp_path[:-1], tsp_path[1:]):
        edge_data = city_graph.get_edge_data(u, v)
        print(f"Edge from {u} to {v}: {edge_data}")
        # Calculate total attributes for the chosen path
        total_time = 0
        total_cost = 0
        total_transfers = 0

  

        if transport_mode:
            # Use only the specified transport mode for each edge
            for data in edge_data.values():
                if data.get("mode") == transport_mode:
                    total_time += data.get("travel_time", 0)
                    total_cost += data.get("cost", 0)
                    total_transfers += data.get("transfers", 0)
                    break
        else:
            # Use minimum values for mixed transport modes
            total_time += min(data.get("travel_time", 0) for data in edge_data.values())
            total_cost += min(data.get("cost", 0) for data in edge_data.values())
            total_transfers += min(data.get("transfers", 0) for data in edge_data.values())

    return {
        'path': tsp_path,
        'total_time': f"{total_time} min",
        'total_cost': f"{total_cost} dollars",
        'total_transfers': total_transfers
    }



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

