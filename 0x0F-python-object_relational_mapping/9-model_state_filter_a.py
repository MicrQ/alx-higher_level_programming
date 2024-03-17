#!/usr/bin/python3
""" a script that lists all State objects that contain
    the letter a from the database hbtn_0e_6_usa.
    using SQLAlchemy.
"""

if __name__ == '__main__':
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    results = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    [print('{}: {}'.format(state.id, state.name))
     for state in results]
