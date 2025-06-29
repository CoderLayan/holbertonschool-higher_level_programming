#!/usr/bin/python3
"""
Changes the name of the State object with id=2 to "New Mexico"
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

    # Create engine and connect to database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get state with id=2
    state = session.query(State).filter(State.id == 2).first()

    # Update state name if found
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close session
    session.close()
