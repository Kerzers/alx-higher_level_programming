#!/usr/bin/python3
"""deletes all State objects with a name containing 'a' from the database"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_del = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_to_del:
        session.delete(state)
    session.commit()
    session.close()
