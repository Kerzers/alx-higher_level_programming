#!/usr/bin/python3
"""lists all City objects from the database hbtn_0e_14_usa """
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name)\
                    .filter(State.id == City.state_id)
    for elmt in cities:
        print(f"{elmt[0]}: ({elmt[1]}) {elmt[2]}")
