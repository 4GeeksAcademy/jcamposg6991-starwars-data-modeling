import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from datetime import datetime, timezone

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

class Planeta(Base):
    __tablename__ = 'planetas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    diameter = Column(String(50))
    rotation_period = Column(String(50))
    orbital_period = Column(String(50))
    gravity = Column(String(50))
    population = Column(String(50))
    climate = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(String(50))
    residents = Column(String)
    films = Column(String)  
    url = Column(String)
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    edited = Column(TIMESTAMP, default=datetime.now(timezone.utc))

class Personaje(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    height = Column(String(50))
    mass = Column(String(50))
    hair_color = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    gender = Column(String(50))
    homeworld = Column(Integer, ForeignKey('planetas.id'))
    films = Column(String)
    url = Column(String)
    created = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    edited = Column(TIMESTAMP, default=datetime.now(timezone.utc))
    planeta = relationship(Planeta)

class Favorito(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    planeta_id = Column(Integer, ForeignKey('planetas.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personajes.id'), nullable=True)
    usuario = relationship(Usuario)
    planeta = relationship(Planeta)
    personaje = relationship(Personaje)

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
