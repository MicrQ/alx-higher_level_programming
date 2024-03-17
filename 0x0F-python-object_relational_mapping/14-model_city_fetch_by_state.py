#!/usr/bin/python3
""" a that prints all City objects from the database hbtn_0e_14_usa """

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State
    from model_city import City
    from sys import argv

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    results = session.query(State, City)\
        .filter(City.state_id == State.id).order_by(City.id).all()

    for state, city in results:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
