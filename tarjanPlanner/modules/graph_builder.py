#import networkx as nx
#from geopy.distance import geodesic 
from .data_loader import load_relative_data, load_transport_modes

def return_relative_data(): 
    relatives_data = load_relative_data()
    return(relatives_data)