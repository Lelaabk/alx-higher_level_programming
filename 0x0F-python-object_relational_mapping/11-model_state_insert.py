#!/usr/bin/python3
""" Add State object "Louisiana" to database"""


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

    state_jdida = State(name="Louisiana")
    session.add(state_jdida)
    session.commit()

    print(state_jdida.id)

    session.close()
