
# ACIT4420 - Final Project - Tarjan Planner 

This Python package automates is a route optimization for Tarjan who is to visit ten of his relatives in Seoul-city. 

## Table of Contents
1. [Features](#features)
2. [Package Structure](#package-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Modules](#modules)
6. [Error Handling](#error-handling)
7. [License](#license)


## Features
- Manage a list of relatives with location details and visit preferences.
- Load and parse data on transportation modes with associated costs, speeds, and transfer times.
- Generate an optimal travel route based on time, cost, or other specified criteria.
- Display the calculated route with travel times and costs for each segment.
- User-friendly interface with customizable options for route planning.

## Package Structure
```
TarjanPlanner/
│
├── LICENSE                  # License information for the package.
├── setup.py                 # Installation script for the package.
├── README.md                # Documentation for the package.
│              
└── TarjanPlanner/           # Package directory containing the core modules and data files.
    ├── __init__.py          # Marks the directory as a package.
    ├── main.py              # Main script to run the automation tasks.
    │ 
    ├── core/                # Core modules for handling main functionality.
    │   ├── graph_builder.py       # Builds a graph representation.
    │   ├── route_optimizer.py     # Optimizes the route for visiting relatives.
    │   ├── relatives_manager.py   # Manages information and operations about the relatives.
    │   ├── user_interface.py      # Provides the interface for user interaction.
    │   └── decorators.py          # Utility functions and decorators for data handling.
    │ 
    └── data/                      # Data files and data-handling scripts.
        ├── data_loader.py         # Loads and parses data from files.
        ├── relative_data.json     # JSON file containing information about relatives.
        └── transport_modes.json   # JSON file listing available transportation modes, costs, speed, and time of transfer.
```


## Installation 

To get started, follow these steps:
1. **Clone the Repository** (or download the package): 
   ```bash
   git clone https://github.com/LarsStorholt/TarjanPlanner.git 
   cd TarjanPlanner 
   ``` 

2. **Install the Package**:
   ```bash
   pip install -e .
   ```
## Usage 
After installing the package, you can run the automation task by using the following command:
   ```bash
   getroute
   ```
Alternatively, you can run the main script directly:
   ```bash
   python -m tarjanPlanner.main
   ```

This will:

1. Load the data on relatives and available transportation modes.
2. Build a graph representation of all possible routes.
3. Calculate the optimal route to visit all relatives efficiently.
4. Display the calculated route to the user.

### Customization
* Add or modify relatives using the relatives_manager.py module.


## Modules 
- **`main.py`**: Contains the main function that launches the program.
- **`setup.py`**: Script for installing the package and dependencies.
- **`core/graphbuilder.py`**: Builds a graph representation of all routes between relatives, creating the foundation for route optimization
- **`core/route_optimizer.py`**: Calculates the optimal route to visit all relatives, minimizing time, cost, or other specified criteria.
- **`core/user_interface.py`**: Provides a interface for inputting data, setting preferences, and displaying the calculated route
- **`core/relatives_manager.py`**: Manages the list of relatives, including adding, removing, and retrieving their details (location, preferences, etc.).
- **`core/decorators.py`**: Contains utility functions and decorators used across the project to streamline data processing and add functionality.
- **`data/load_data.py`**: Loads and parses data from JSON files, including relative information and transportation modes.
- **`data/relative_data.json`**: JSON file containing details about each relative, such as location and visit preferences.
- **`data/transpdort_mode.json`**: JSON file listing available transportation modes, including speed, cost, and transfer times.


## Error handling 
The package includes basic error handling for:

- Missing email addresses when sending a message.
- Attempting to send messages to an empty contact list.


## Licence
This project is licensed under the MIT License. See the LICENSE file for more details.
https://github.com/LarsStorholt/tarjanPlanner/blob/master/LICENSE file for details.