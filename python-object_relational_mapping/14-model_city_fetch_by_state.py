#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    data = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, data),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    city_states = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id)
    for city, state in city_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
