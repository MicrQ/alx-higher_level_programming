#!/usr/bin/python3
""" class definition for City class """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """ Difines City """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
