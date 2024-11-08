import json
import os
import re


class DataLoader:

    def __init__(self):
        # Define paths to the JSON data files
        self.relative_data_path = os.path.join(os.path.dirname(__file__), '../data/relative_data.json')
        self.transport_modes_path = os.path.join(os.path.dirname(__file__), '../data/transport_modes.json')

    def is_json_file(self, file_path):
            # Use regular expression to check if the file path ends with .json
            return re.match(r'^.*\.json$', file_path, re.IGNORECASE) is not None

    def load_json_data(self, file_path):
        # Helper function to load JSON data from a file.
        if not self.is_json_file(file_path):
            print(f"Error: {file_path} is not a JSON file.")
            return None
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

