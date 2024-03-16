#!/usr/bin/python3
""" a script that prints the first
    State object from the database hbtn_0e_6_usa
    using sqlalchemy module
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import State, Base
    """ mandatory + necessary modules """

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    result = session.query(State).first()

    if result:
        print("{}: {}".format(result.id, results.name))
    else:
        print('Nothing')

    session.close()
