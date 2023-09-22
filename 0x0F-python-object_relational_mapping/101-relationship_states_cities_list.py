#!/usr/bin/python3
"""lists all State objects and corresponding city
from the database hbtn_0e_101_usa """
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
    for state_obj in session.query(State).order_by(State.id):
        print(state_obj.id, state_obj.name, sep=": ")
        for city_obj in state_obj.cities:
            print(f"    {city_obj.id}: {city_obj.name}")
