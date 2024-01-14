from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    super_name = db.Column(db.String, unique=True)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    
    powers = relationship('Power', secondary='Hero_Power', back_populates='heroes')



    

class Power(db.Model):
    _tablename__ = 'power'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)

    heroes = relationship('Hero', secondary='Hero_Power', back_populates='powers')
class Hero_Power(db.Model):
    _tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'))
    strength = db.Column(db.String(20))
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
 