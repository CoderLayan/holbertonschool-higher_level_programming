#!/usr/bin/python3
"""
Defines the State class and Base instance for SQLAlchemy
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the MySQL table 'states'
    
    Attributes:
        id (int): Auto-generated, unique identifier (primary key)
        name (str): Name of the state (max 128 chars, not null)
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
