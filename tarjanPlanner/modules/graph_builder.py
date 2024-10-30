import networkx as nx
from geopy.distance import geodesic 
import matplotlib.pyplot as plt


def create_city_graph(relatives_data, transport_modes):
    """Creates a city graph with nodes for each relative and edges based on transport options."""
    G = nx.MultiGraph()  # Initialize an undirected graph
    
    # Add nodes for each relative
    for relative in relatives_data:
        G.add_node(
            relative["name"],
            pos=(relative["latitude"], relative["longitude"]),
            district=relative["district"]
        )

    # Add edges with weights based on transport modes
    for i, relative1 in enumerate(relatives_data):
        for j, relative2 in enumerate(relatives_data):
            if i < j:  # Avoid duplicate edges by only processing each pair once
                # Calculate the distance between the two nodes
                distance = geodesic(
                    (relative1["latitude"], relative1["longitude"]),
                    (relative2["latitude"], relative2["longitude"])
                ).km

                # Create an edge for each transport mode
                for mode, properties in transport_modes.items():
                    travel_time = (distance / properties["speed_kmh"]) * 60  # Time in minutes
                    cost = distance * properties["cost_per_km"]
                    transfers = properties["transfer_time_min"]

                    # Add an edge with weights for time, cost, and transfers
                    G.add_edge(
                        relative1["name"],
                        relative2["name"],
                        mode=mode,
                        distance=distance,
                        travel_time=travel_time,
                        cost=cost,
                        transfers=transfers
                    )
    '''
    for u, v, data in G.edges(data=True):
        print(f"Edge from {u} to {v} via {data['mode']}:")
        print(f"  - Distance: {data['distance']} km")
        print(f"  - Travel Time: {data['travel_time']} min")
        print(f"  - Cost: {data['cost']} dollars")
        print(f"  - Transfers: {data['transfers']}")
'''
    return G


'''
def visualize_city_graph(G):
    """Visualizes the city graph with nodes and edges using latitude and longitude for positioning."""
    # Get positions from the graph node attributes
    pos = nx.get_node_attributes(G, 'pos')

    # Draw the graph
    plt.figure(figsize=(10, 8))
    
    # Draw nodes with labels
    nx.draw_networkx_nodes(G, pos, node_size=100, node_color="skyblue")
    nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=1, alpha=0.5, edge_color="gray")
    
    # Set plot title and show plot
    plt.title("City Graph Visualization")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()
'''
