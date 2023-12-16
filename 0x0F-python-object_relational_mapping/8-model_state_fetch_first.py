#!/usr/bin/python3
""" Print the first state object from database. """


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    awal_state = session.query(State).order_by(State.id).first()
    if awal_state:
        print('{}: {}'.format(awal_state.id, awal_state.name))
    else:
        print('Nothing')

    session.close()
