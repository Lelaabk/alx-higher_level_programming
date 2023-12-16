#!/usr/bin/python3
""" Lists all State objetcs. """


import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Base.metadata.create.all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
        for city_ins in instance.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")

    # states = session.query(State).order_by(State.id).all()
    # for state in states:
    # print("{}: {}".format(state.id, state.name))
    # for city in state.cities:
    # print("\t{}: {}".format(city.id, city.name))

    session.close()
