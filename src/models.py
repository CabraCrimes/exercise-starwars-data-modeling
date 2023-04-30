import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class MyUser(Base):
    __tablename__ = 'my_user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    favourite = relationship('favourites')

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('my_user.id'), nullable=False)
    planet_id = Column(String(250), ForeignKey('planet.id'), nullable=False)
    character_id = Column(String(250), ForeignKey('character.id'), nullable=False)
    
   

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    population = Column(Integer)
    favourite = relationship('favourites')
    

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True, nullable=False)
    alive = Column(Boolean, nullable=False)
    favourite = relationship('favourites')
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
