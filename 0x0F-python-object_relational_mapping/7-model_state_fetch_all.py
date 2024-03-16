#!/usr/bin/python3
""" a script that lists all State objects from the database hbtn_0e_6_usa
    using SQLAlchemy
"""

from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv
""" Importing the Base declarative and state class """

engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

Base.metadata.create_all(engine)
session = Session(engine)

results = session.query(State).order_by(State.id).all()

for row in results:
    print("{}: {}".format(row.id, row.name))
session.close()
