#!/usr/bin/python3
"""lists all State objects that contain the letter a from the database"""
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
    state_change = s.query(State).filter_by(id=2).first()
    state_change.name = "New Mexico"
    s.commit()
    s.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
