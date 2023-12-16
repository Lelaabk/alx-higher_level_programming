#!/usr/bin/python3
""" Deletes all State objects with name containing letter a in  database"""


import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in cities:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

    session.close()
