import json
import os

class RelativeManager : 
    #init 
    def __init__(self): 
        self.relative_data_path = os.path.join(os.path.dirname(__file__), '../data/relative_data.json')
        self.relatives = self.load_relative_data()

    #add relative 
    def add_relative(self, name , street_name, latitude, longitude) :
        relative = {
            'name' : name, 
            'street_name' : street_name, 
            'latitude' : latitude, 
            'longitude' : longitude
        }
        self.relatives.append(relative)
        self.save_relative_data()

    #remove relative 
    def remove_relative(self, name) : 
        self.relatives = [r for r in self.relatives if r['name'] != name]
        self.save_relative_data()

    #edit relative

    def load_relative_data(self):
        try: 
            with open(self.relative_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
                return []
    
    def print_relatives_data(self) : 
        for relative in self.relatives:
            print(f"Name: {relative['name']}, Street: {relative['street_name']}, "
                  f"Latitude: {relative['latitude']}, Longitude: {relative['longitude']}")

    def save_relative_data(self) : 
        with open(self.relative_data_path, 'w') as f:
            json.dump(self.relatives, f, indent=4)
    
    def edit_relative(self, current_name, new_name, street_name, latitude, longitude):
        for relative in self.relatives:
            if relative['name'] == current_name:
                # Update the relative with the new information
                relative['name'] = new_name
                relative['street_name'] = street_name
                relative['latitude'] = latitude
                relative['longitude'] = longitude
                self.save_relative_data()  # Save changes to the JSON file
                return
        print(f"Relative with name '{current_name}' not found.")


