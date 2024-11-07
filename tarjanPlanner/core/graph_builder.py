import networkx as nx
from geopy.distance import geodesic 
import matplotlib.pyplot as plt

def create_city_graph(relatives_data):
    G = nx.Graph()

    # Add nodes to the graph
    for relative in relatives_data:
        G.add_node(relative["name"], pos=(relative["latitude"], relative["longitude"]))

    # Add edges with distance weights between each pair of nodes
    for i, relative1 in enumerate(relatives_data):
        for j, relative2 in enumerate(relatives_data):
            if i < j:  # Avoid duplicate edges
                # Calculate the geodesic distance between nodes
                distance = geodesic(
                    (relative1["latitude"], relative1["longitude"]),
                    (relative2["latitude"], relative2["longitude"])
                ).km
                # Add edge with distance as the weight
                G.add_edge(relative1["name"], relative2["name"], weight=distance)

    return G

