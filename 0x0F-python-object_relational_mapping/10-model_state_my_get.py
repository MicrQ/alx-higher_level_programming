#!/usr/bin/python3
""" a script that prints the State object with the name passed as
    argument from the database hbtn_0e_6_usa.
"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    result = session.query(State).filter(State.name.like(argv[4])).first()

    if result:
        print(result.id)
    else:
        print('Not found')
    session.close()
