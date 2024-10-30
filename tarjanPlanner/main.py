
import time
from modules.user_interface import get_user_transport_preference
from modules.graph_builder import create_city_graph #, visualize_city_graph
from modules.route_calculator.route_optimizer import calculate_optimal_route, visualize_city_graph_with_route
from modules.data_loader import DataLoader

def main (): 

     # Log the start time
    start_time = time.time()

    #Asking user for transport preference 
    transport_preferenece = get_user_transport_preference()

    #loading data from json files by creating a instance of the class dataLoader
    data_loader = DataLoader()
    relatives_data = data_loader.load_relative_data()
    transport_modes = data_loader.load_transport_modes()

    #create a city graph
    city_graph = create_city_graph(relatives_data, transport_modes)
    
    #Visualize city: 
    #visualize_city_graph(city_graph)

    #finding optimal route
    optimal_route = calculate_optimal_route(city_graph, transport_preferenece)

    print(optimal_route)

    visualize_city_graph_with_route(city_graph, optimal_route)


    # Log the end time and calculate the duration
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution Time: {execution_time:.2f} seconds")
    

if __name__ == "__main__": 
    main()