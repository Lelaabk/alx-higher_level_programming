#!/usr/bin/python3
""" Creates State "California" with city "San Francisco". """


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create.all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_jdida = State(name='California')
    city_jdida = City(name='San Francisco')

    state_jdida.cities.append(city_jdida)

    session.add(state_jdida)
    session.add(city_jdida)
    session.commit()

    session.close()
