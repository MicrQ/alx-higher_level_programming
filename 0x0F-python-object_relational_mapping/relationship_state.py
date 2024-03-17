#!/usr/bin/python3
""" a python file that contains the class definition of
    a State and Base = declarative_base().
"""

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, relationship
""" necessary modules """

Base = declarative_base(metadata=MetaData())


class State(Base):
    """ represents a state """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states',
                            cascade='all, delete-orphan')
