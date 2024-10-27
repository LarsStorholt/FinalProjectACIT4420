from setuptools import setup, find_packages

setup(
    name="greetings_project",  # The package name
    version="0.1",
    packages=find_packages(),  
    include_package_data=True,  
    description="Final project in ACIT4420. ...This program automates the process of sending personlized Good-morning message to a list of friends",
    author="Lars Storholt",
    author_email="s354518@oslomet.no",
    install_requires=[
        # List your project's dependencies here, if any, e.g.,
        # 'requests',
    ],
    entry_points={
        'console_scripts': [
            'greetings=greetings_project.main:main',  # Points directly to the main function in main.py
        ],
    },
)