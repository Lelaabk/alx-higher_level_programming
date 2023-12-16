#!/usr/bin/python3
""" Prints id of State objects with the specified name. """


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

    smiya_state = sys.argv[4]
    state = session.query(State).filter(State.name == smiya_state).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
