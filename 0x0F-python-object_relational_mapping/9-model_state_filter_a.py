#!/usr/bin/env python3
"""
   This module contains a MySQLdb query.
"""
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from model_state import Base, State

    USER = argv[1]
    PSWD = argv[2]
    DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    session = Session()

    for instance in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(instance.id, instance.name))
