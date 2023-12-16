#!/usr/bin/python3
""" Deletes all State objects with name containing letter a in  database"""


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

    state_li_tmseh = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_li_tmseh:
        session.delete(state)
    session.commit()

    session.close()
