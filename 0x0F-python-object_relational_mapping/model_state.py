"""
   This module contains a class definition for State
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class State(Base):
    """
       A class definition for the state model class mapped to a declarative
       base object.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
