#!/usr/bin/python3
"""Module that contains the class definition of a State."""
import sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Metadata
from sqlalchemy.ext.declarative import declarative_base


class State(Base):
    """Class definition of a State."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states")
