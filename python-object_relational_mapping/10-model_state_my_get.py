#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine and connect to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query state by name
    state = session.query(State)\
        .filter(State.name == state_name)\
        .first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
