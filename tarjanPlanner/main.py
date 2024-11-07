
import time
from core.user_interface import get_user_transport_preference, print_route_description
from core.graph_builder import  create_city_graph
from core.route_optimizer import find_shortest_distance_route, calculate_balanced_route_with_modes, visualize_city_graph_with_route#calculate_optimal_route #, get_information_about_route #, visualize_city_graph_with_route, calculate_fastest_route_with_modes
from data.data_loader import DataLoader

import networkx as nx


def main (): 

    start_time = time.time()

    #Asking user for transport preference 
    transport_preferenece, waiting_time = get_user_transport_preference()


    #loading data from json files by creating a instance of the class dataLoader
    data_loader = DataLoader()

    relatives_data = data_loader.load_relative_data()
    transport_modes = data_loader.load_transport_modes()

    #create a city graph
    city_graph = create_city_graph(relatives_data)

    #finding shortest route
    shortest_route , distance = find_shortest_distance_route(city_graph)

    #Calculate most effiencent travelling modes for the route 
    fastest_route, travel_time, travel_costs = calculate_balanced_route_with_modes(city_graph, shortest_route, transport_modes, transport_preferenece)

    #Get the description of the route
    print_route_description(fastest_route, relatives_data, distance, travel_time, travel_costs)

    #Visualize the route
    visualize_city_graph_with_route(city_graph, fastest_route)


    # Log the end time and calculate the duration
    end_time = time.time()

    execution_time = end_time - (start_time + waiting_time) 
    print(f"\nExecution Time: {execution_time:.2f} seconds")
    
if __name__ == "__main__": 
    main()