#!/usr/bin/python3
""" a script that creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa.
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy.schema import Table
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    newCity = City(name='San Francisco')
    newState = State(name='California')

    newState.cities.append(newCity)
    session.add(newState)
    session.add(newCity)
    session.commit()
