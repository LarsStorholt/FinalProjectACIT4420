import json
import os

class DataLoader:
    def __init__(self):
        # Define paths to the JSON data files
        self.relative_data_path = os.path.join(os.path.dirname(__file__), '../data/relative_data.json')
        self.transport_modes_path = os.path.join(os.path.dirname(__file__), '../data/transport_modes.json')

    def load_json_data(self, file_path):
        # Helper function to load JSON data from a file.
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from file {file_path}: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error while loading {file_path}: {e}")
            return None

    def load_relative_data(self):
        # Load relatives' location data from JSON.
        return self.load_json_data(self.relative_data_path)

    def load_transport_modes(self):
        # Load transport modes data from JSON.
        return self.load_json_data(self.transport_modes_path)
    
"""    
# Define paths to the JSON data files
RELATIVE_DATA_PATH = os.path.join(os.path.dirname(__file__), '../data/relative_data.json')
TRANSPORT_MODES_PATH = os.path.join(os.path.dirname(__file__), '../data/transport_modes.json')

def load_json_data(file_path):
    #Helper function to load JSON data from a file.
    with open(file_path, 'r') as f:
        return json.load(f)

def load_relative_data():
    #Load relatives' location data from JSON.
    return load_json_data(RELATIVE_DATA_PATH)

def load_transport_modes():
    #Load transport modes data from JSON
    return load_json_data(TRANSPORT_MODES_PATH)
"""

