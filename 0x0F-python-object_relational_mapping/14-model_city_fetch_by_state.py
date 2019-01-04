#!/usr/bin/python3
"""lists all City objects from the database"""
import sys
from model_state import Base, State
from model_city import Base, City
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
    for city, state in s.query(City, State).filter(State.id == City.state_id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    s.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
