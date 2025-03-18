#!/usr/bin/python3
"""prints the State object with the name passed as argument"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    data = argv[3]
    state_name = argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, data),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == state_name).first()

    if states is not None:
        print(states.id)
    else:
        print("Not found")
