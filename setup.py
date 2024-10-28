from setuptools import setup, find_packages

setup(
    name="TarjanPlanner",  # The package name
    version="0.1",
    packages=find_packages(),  
    include_package_data=True,  
    description="Final project in ACIT4420. This program returns a travelling route for ten positions bases on preference (time, price and number of transfers) from the user of the program",
    author="Lars Storholt",
    author_email="s354518@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'getroute=tarjanPlanner.main:main',  # Points directly to the main function in main.py
        ],
    },
)