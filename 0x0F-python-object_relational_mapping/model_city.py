#!/usr/bin/python3
"""
   This module contains a class definition for City
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from model_state import Base, State


class City(Base):
    """
       A class definition for the state model class mapped to a declarative
       base object.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
