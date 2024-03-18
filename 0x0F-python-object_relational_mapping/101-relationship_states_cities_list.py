#!/usr/bin/python3
""" a script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usa
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import Session
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    results = session.query(State).order_by(State.id).all()

    for state in results:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))
    session.close()
