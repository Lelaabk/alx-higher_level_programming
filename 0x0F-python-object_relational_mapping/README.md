# 0x0F. Python - Object-relational mapping

## Description
This project explores the integration of Python with databases, focusing on Object-Relational Mapping (ORM). The primary goal is to connect to a MySQL database using both the MySQLdb module and SQLAlchemy, an ORM.

## Files
- **0-select_states.py:** Lists all states from the database hbtn_0e_0_usa.
- **1-filter_states.py:** Lists states with names starting with 'N'.
- **2-my_filter_states.py:** Displays values in the states table based on user input.
- **3-my_safe_filter_states.py:** Safe version to prevent SQL injection.
- **4-cities_by_state.py:** Lists all cities from the database hbtn_0e_4_usa.
- **5-filter_cities.py:** Lists all cities of a given state.
- **6-model_state.py:** Python file containing the State class and an instance of Base from SQLAlchemy.
- **7-model_state_fetch_all.py:** Lists all State objects from the database hbtn_0e_6_usa.
- **8-model_state_fetch_first.py:** Prints the first State object from the database hbtn_0e_6_usa.
- **9-model_state_filter_a.py:** Lists all State objects containing the letter 'a'.
- **10-model_state_my_get.py:** Prints the State object with the given name.
- **11-model_state_insert.py:** Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
- **12-model_state_update_id_2.py:** Changes the name of a State object from the database hbtn_0e_6_usa.
- **13-model_state_delete_a.py:** Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
- **14-model_city.py:** Contains the class definition of the City class.
- **14-model_city_fetch_by_state.py:** Lists all City objects from the database hbtn_0e_14_usa.
- **relationship_city.py:** Improved version of model_city.py.
- **relationship_state.py:** Improved version of model_state.py.
- **100-relationship_states_cities.py:** Creates the State “California” with the City “San Francisco” from the database hbtn_0e_100_usa.
- **101-relationship_states_cities_list.py:** Lists all State objects and corresponding City objects from the database hbtn_0e_101_usa.
- **102-relationship_cities_states_list.py:** Lists all City objects from the database hbtn_0e_101_usa with their linked State objects.

## Requirements
- Python 3.8.5
- MySQLdb 2.0.x
- SQLAlchemy 1.4.x
- pycodestyle 2.8.*
- MySQL server installed (8.0) on Ubuntu 20.04

## How to Use
1. Install required dependencies using the provided commands.
2. Execute each script with the specified arguments.

## Learning Objectives
- Connect to a MySQL database from a Python script.
- Perform SELECT and INSERT operations using MySQLdb.
- Understand and implement Object-Relational Mapping (ORM) with SQLAlchemy.
- Create a Python Virtual Environment for project dependencies.
