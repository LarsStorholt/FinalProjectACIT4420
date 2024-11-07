from setuptools import setup, find_packages

setup(
    name="TarjanPlanner",  # The package name
    version="0.1",
    packages=find_packages(),  
    include_package_data=True,  
    description="Final project in ACIT4420. This program returns a travelling route for ten positions based on preference (time or price) from the user of the program",
    author="Lars Storholt",
    author_email="s354518@oslomet.no",
    install_requires=[
        "networkx>=2.5",
        "geopy>=2.0",
        "matplotlib>=3.0",
    ],
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'get_route=tarjanPlanner.main:main',  # Points directly to the main function in main.py
        ],
    },
)