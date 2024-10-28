import networkx as nx
from geopy.distance import geodesic 
from modules.data_loader import load_relative_data, load_transport_modes

relatives_data = load_relative_data()
transport_modes = load_transport_modes()

def create_city_graph():
    """Creates a city graph with nodes for each relative and edges based on transport options."""
    G = nx.Graph()  # Initialize an undirected graph
    
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

    return G
