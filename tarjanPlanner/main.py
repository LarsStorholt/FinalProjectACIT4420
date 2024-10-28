from modules.user_interface import get_user_transport_preference
from modules.graph_builder import return_relative_data


def main (): 

    relative_data = return_relative_data()
    print(relative_data)


    '''
    #transport_preferenece = get_user_transport_preference
    #print(transport_preferenece)
    '''

if __name__ == "__main__": 
    main()