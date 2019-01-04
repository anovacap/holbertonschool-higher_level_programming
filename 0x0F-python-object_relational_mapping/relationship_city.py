#!/usr/bin/python3
"""Defines class City sets up states database"""
from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()
from relationship_state import Base

class City(Base):
    """City inherits from Base"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    