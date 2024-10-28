#from modules.user_interface import get_user_transport_preference
from modules.graph_builder import create_city_graph


def main (): 

    city_graph = create_city_graph()

    print("Graph nodes:")
    for node in city_graph.nodes(data=True):
        print(node)

    print("\nGraph edges:")
    for edge in city_graph.edges(data=True):
        print(edge)

    #relative_data = return_relative_data()
    #print(relative_data)


    '''
    #transport_preferenece = get_user_transport_preference
    #print(transport_preferenece)
    '''

if __name__ == "__main__": 
    main()