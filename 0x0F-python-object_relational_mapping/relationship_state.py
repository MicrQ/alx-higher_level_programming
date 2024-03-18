#!/usr/bin/python3
""" a python file that contains the class definition of
    a State and Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import City, Base
""" necessary modules """


class State(Base):
    """ represents a state """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
