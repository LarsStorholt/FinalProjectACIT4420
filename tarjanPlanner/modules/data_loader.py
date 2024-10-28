import json
import os

# Define paths to the JSON data files
RELATIVE_DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/relative_data.json')
TRANSPORT_MODES_PATH = os.path.join(os.path.dirname(__file__), '../data/transport_modes.json')

def load_json_data(file_path):
    """Helper function to load JSON data from a file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def load_relative_data():
    """Load relatives' location data from JSON."""
    return load_json_data(RELATIVE_DATA_PATH)

def load_transport_modes():
    """Load transport modes data from JSON."""
    return load_json_data(TRANSPORT_MODES_PATH)


