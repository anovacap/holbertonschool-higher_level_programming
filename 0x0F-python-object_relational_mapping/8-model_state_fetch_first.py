#!/usr/bin/python3
"""prints the first State object from the database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker


def main(argv):
    """func - main - argv"""
    if len(argv) != 4:
        print("Enter 3 arguments")
        return
    session = sessionmaker()
    engine = create_engine('mysql+mysqldb://'
                           '{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                            sys.argv[2],
                                                            sys.argv[3]),
                           pool_pre_ping=True)
    session.configure(bind=engine)
    Base.metadata.create_all(engine)
    s = session()
    for state in s.query(State).order_by(State.id)[0:1]:
        if not state:
            print("Nothing")
        else:
            print("{}: {}".format(state.id, state.name))
    s.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
