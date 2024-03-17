#!/usr/bin/python3
""" a script that changes the name of a State object
    from the database hbtn_0e_6_usa.
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    state = session.query(State).filter(State.id == 2).first()
    state.name = 'New Mexico'
    session.add(state)
    session.commit()
    session.close()
