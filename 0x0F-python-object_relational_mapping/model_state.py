#!/usr/bin/python3
""" a python file that contains the class definition of
    a State and an instance Base = declarative_base().
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
""" necessary modules """

Base = declarative_base()


class State(Base):
    """ represents a state """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
