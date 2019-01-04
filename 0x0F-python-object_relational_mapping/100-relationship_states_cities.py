#!/usr/bin/python3
"""lists all City objects from the database"""
import sys
from relationship_state import Base, State
from relationship_city import City
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
    add_sc = State(name="California")
    add_ct = City(name="San Francisco")
    add_sc.cities.append(add_ct)
    s.add(add_sc)
    s.commit()
    s.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
